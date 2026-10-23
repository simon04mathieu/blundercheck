// Cloudflare Pages Function : GET /api/stats?token=ADMIN_TOKEN
// Tableau de bord privé : usage du prof, comptes, liste d'attente. &format=json pour les chiffres bruts.
// Les visites (pages vues, provenance) sont dans Cloudflare Web Analytics.

import { ETAPES } from '../../lib/src.js';

const PRIX_PARTIE = 0.3;     // centimes de dollar, mesuré le 21/10/2026
const PRIX_QUESTION = 0.05;  // estimation

function egal(a, b) { if (!a || !b || a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return d === 0; }
const jour = (decalage = 0) => new Date(Date.now() - decalage * 864e5).toISOString().slice(0, 10);
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

async function toutesLesCles(ns, prefix, max = 5000) {
  const out = []; let cursor;
  do {
    const r = await ns.list({ prefix, cursor });
    out.push(...r.keys.map(k => k.name));
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor && out.length < max);
  return out;
}
async function valeurs(ns, cles, max = 1000) {
  return (await Promise.all(cles.slice(0, max).map(async k => { try { return JSON.parse(await ns.get(k) || 'null'); } catch { return null; } }))).filter(Boolean);
}

// ---------- Provenance (?src) : base D1 STATS + vues des vidéos (relevés publics de la branche videos) ----------
const RELEVES = 'https://raw.githubusercontent.com/simon04mathieu/blundercheck/videos/stats/';
async function releve(nom) {
  try { const r = await fetch(RELEVES + nom, { cf: { cacheTtl: 600, cacheEverything: true } }); return r.ok ? await r.json() : null; } catch { return null; }
}
// Vues des vidéos publiées depuis `debut` (AAAA-MM-JJ), par source ; null si le relevé manque
async function vuesParSource(debut) {
  const t0 = Date.parse(debut + 'T00:00:00Z'), out = {};
  const tk = await releve('tiktok.json');
  if (tk && Array.isArray(tk.videos)) out.tiktok = { vues: tk.videos.filter(v => (v.create_time || 0) * 1000 >= t0).reduce((a, v) => a + (+v.view_count || 0), 0), releve: tk.date };
  const yt = await releve('youtube.json');
  if (yt && yt.videos) out.youtube = { vues: Object.values(yt.videos).filter(v => Date.parse(v.publiee || 0) >= t0).reduce((a, v) => a + (+v.vues || 0), 0), releve: yt.date };
  return out;
}
async function provenance(env, nbJours) {
  if (!env.STATS) return null;
  const debut = nbJours ? jour(nbJours - 1) : '2000-01-01';
  const [r, vues] = await Promise.all([
    env.STATS.prepare('SELECT src, evt, SUM(n) AS n FROM compteur WHERE jour >= ?1 GROUP BY src, evt').bind(debut).all(),
    vuesParSource(nbJours ? debut : '2000-01-01'),
  ]);
  const par = {};
  const moi = {};
  for (const x of r.results || []) { if (x.src === 'moi') { moi[x.evt] = x.n; continue; } (par[x.src] ||= { src: x.src })[x.evt] = x.n; }
  for (const k of Object.keys(vues)) (par[k] ||= { src: k }).vues = vues[k].vues;
  const lignes = Object.values(par).sort((a, b) => (b.visite || 0) - (a.visite || 0) || (b.vues || 0) - (a.vues || 0));
  const total = { src: 'total' }; for (const l of lignes) for (const e of [...ETAPES, 'vues']) if (l[e] != null) total[e] = (total[e] || 0) + l[e];
  const premier = await env.STATS.prepare('SELECT MIN(jour) AS j FROM compteur').first('j').catch(() => null);
  return { debut: nbJours ? debut : premier, depuis: premier, lignes, total, moi, releves: Object.fromEntries(Object.entries(vues).map(([k, v]) => [k, v.releve])) };
}

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  if (!env.ADMIN_TOKEN || !egal(url.searchParams.get('token') || '', env.ADMIN_TOKEN)) return new Response('Non autorisé', { status: 401 });

  // 1. Prof : 30 derniers jours
  const jours = [];
  for (let d = 0; d < 30; d++) {
    const j = jour(d);
    let s = { appels: 0, parties: 0, questions: 0 };
    if (env.QUOTA) { try { s = { ...s, ...JSON.parse(await env.QUOTA.get('stats:' + j) || '{}') }; } catch { } }
    jours.push({ jour: j, ...s });
  }
  const somme = (n, k) => jours.slice(0, n).reduce((a, x) => a + (x[k] || 0), 0);
  const visiteursProf = env.QUOTA ? (await toutesLesCles(env.QUOTA, jour() + ':')).length : null;

  // 2. Comptes
  let comptes = null;
  if (env.COMPTES) {
    const us = await valeurs(env.COMPTES, await toutesLesCles(env.COMPTES, 'user:'));
    const il7 = Date.now() - 7 * 864e5;
    comptes = {
      total: us.length,
      plus: us.filter(u => u.plan === 'plus' && (!u.fin || u.fin * 1000 > Date.now())).length,
      nouveaux7j: us.filter(u => u.creeLe && Date.parse(u.creeLe) > il7).length,
    };
  }

  // 3. Liste d'attente
  let liste = null;
  if (env.LISTE) {
    const ls = await valeurs(env.LISTE, await toutesLesCles(env.LISTE, 'email:'));
    const il7 = Date.now() - 7 * 864e5, sources = {}, langues = {};
    ls.forEach(v => { sources[v.source || '?'] = (sources[v.source || '?'] || 0) + 1; langues[v.langue || '?'] = (langues[v.langue || '?'] || 0) + 1; });
    liste = { total: ls.length, nouveaux7j: ls.filter(v => v.date && Date.parse(v.date) > il7).length, sources, langues };
  }

  const nbJours = { '1': 1, '7': 7, '30': 30, tout: 0 }[url.searchParams.get('jours') || '7'] ?? 7;
  let sources = null;
  try { sources = await provenance(env, nbJours); } catch (e) { sources = { erreur: String(e) }; }

  const cout = n => (somme(n, 'parties') * PRIX_PARTIE + somme(n, 'questions') * PRIX_QUESTION) / 100;
  const data = {
    genere: new Date().toISOString(),
    prof: {
      aujourdhui: { parties: somme(1, 'parties'), questions: somme(1, 'questions'), appels: somme(1, 'appels'), visiteurs: visiteursProf },
      sept_jours: { parties: somme(7, 'parties'), questions: somme(7, 'questions'), appels: somme(7, 'appels') },
      trente_jours: { parties: somme(30, 'parties'), questions: somme(30, 'questions'), appels: somme(30, 'appels') },
      cout_estime_dollars: { aujourdhui: cout(1), sept_jours: cout(7), trente_jours: cout(30) },
      par_jour: jours,
    },
    comptes, liste, sources,
  };
  if (url.searchParams.get('format') === 'json') return new Response(JSON.stringify(data, null, 2), { headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });

  const tuile = (label, v, sous = '') => `<div class="t"><div class="l">${esc(label)}</div><div class="v">${esc(v ?? '—')}</div>${sous ? `<div class="s">${esc(sous)}</div>` : ''}</div>`;
  const max = Math.max(1, ...jours.map(j => j.parties));
  const barres = jours.slice().reverse().map(j => `<div class="b" title="${esc(j.jour)} : ${j.parties} parties, ${j.questions} questions"><i style="height:${Math.round(j.parties / max * 100)}%"></i><span>${esc(j.jour.slice(8))}</span></div>`).join('');
  const liste_ = o => Object.entries(o || {}).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${esc(k)} : ${v}`).join(' · ') || '—';
  const dollars = v => v.toLocaleString('fr-FR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' $';
  const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Stats BlunderCheck</title>
<style>
:root{--bg:#111614;--c:#18201C;--l:#2A342F;--t:#EDE7D8;--m:#A8A99A;--a:#C9A45C;--g:#4F7363}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--t);font:15px/1.5 system-ui,sans-serif;padding:24px 16px}
main{max-width:980px;margin:auto}h1{font-size:26px;margin:0 0 4px}h2{font-size:15px;color:var(--a);text-transform:uppercase;letter-spacing:.08em;margin:28px 0 10px}
.m{color:var(--m);font-size:13px}.g{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
.t{background:var(--c);border:1px solid var(--l);border-radius:12px;padding:14px}.l{color:var(--m);font-size:12px;text-transform:uppercase;letter-spacing:.06em}.v{font-size:28px;font-weight:700;font-variant-numeric:tabular-nums}.s{color:var(--m);font-size:12.5px}
.ch{display:flex;align-items:flex-end;gap:3px;height:140px;background:var(--c);border:1px solid var(--l);border-radius:12px;padding:12px 10px 22px}
table{width:100%;border-collapse:collapse;background:var(--c);border:1px solid var(--l);border-radius:12px;overflow:hidden;font-variant-numeric:tabular-nums}th,td{padding:9px 10px;text-align:right;border-bottom:1px solid var(--l);white-space:nowrap}th{color:var(--m);font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;font-weight:600}td:first-child,th:first-child{text-align:left}tr.tot td{font-weight:700;border-bottom:0}td small{color:var(--m);display:block;font-size:11px}.tw{overflow-x:auto;border-radius:12px}.per a{display:inline-block;margin-right:6px;padding:4px 10px;border:1px solid var(--l);border-radius:999px;text-decoration:none;font-size:13px}.per a.on{background:var(--a);color:#1A1407;border-color:var(--a)}
.b{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;position:relative}.b i{display:block;background:linear-gradient(var(--a),var(--g));border-radius:3px 3px 0 0;min-height:1px}.b span{position:absolute;bottom:-18px;left:0;right:0;text-align:center;font-size:10px;color:var(--m)}
a{color:var(--a)}p{margin:6px 0}
</style></head><body><main>
<h1>Stats BlunderCheck</h1><p class="m">Mis à jour le ${esc(new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' }))}. Les visites du site (pages vues, provenance TikTok/Google…) sont dans Cloudflare › blundercheck.app › Web Analytics.</p>
${blocSources(sources, nbJours, url)}
<h2>Prof IA · aujourd'hui</h2><div class="g">
${tuile('Parties commentées', data.prof.aujourdhui.parties)}${tuile('Questions', data.prof.aujourdhui.questions)}${tuile('Visiteurs ayant utilisé le prof', visiteursProf)}${tuile('Coût estimé', dollars(cout(1)))}
</div>
<h2>Prof IA · 7 et 30 jours</h2><div class="g">
${tuile('Parties · 7 j', data.prof.sept_jours.parties, `${data.prof.sept_jours.questions} question${data.prof.sept_jours.questions > 1 ? 's' : ''}`)}${tuile('Parties · 30 j', data.prof.trente_jours.parties, `${data.prof.trente_jours.questions} question${data.prof.trente_jours.questions > 1 ? 's' : ''}`)}${tuile('Coût · 7 j', dollars(cout(7)))}${tuile('Coût · 30 j', dollars(cout(30)))}
</div>
<h2>Parties commentées par jour (30 jours)</h2><div class="ch">${barres}</div>
<h2>Comptes</h2><div class="g">
${comptes ? tuile('Comptes créés', comptes.total, `+${comptes.nouveaux7j} cette semaine`) + tuile('Abonnés BlunderCheck+', comptes.plus) : tuile('Comptes', 'non configuré')}
</div>
<h2>Liste d'attente</h2><div class="g">
${liste ? tuile('Inscrits', liste.total, `+${liste.nouveaux7j} cette semaine`) + tuile('Par source', '', liste_(liste.sources)) + tuile('Par langue', '', liste_(liste.langues)) : tuile('Liste', 'non configurée')}
</div>
<p class="m" style="margin-top:22px">Export de la liste : <code>/api/liste?token=…</code> · Chiffres bruts : ajoute <code>&amp;format=json</code> à l'adresse. Le coût est une estimation (${String(PRIX_PARTIE).replace('.', ',')} centime par partie) : le vrai montant est dans la console Anthropic.</p>
</main></body></html>`;
  return new Response(html, { headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store', 'x-robots-tag': 'noindex', 'referrer-policy': 'no-referrer' } });
}

function blocSources(S, nbJours, url) {
  const per = [['1', "Aujourd'hui"], ['7', '7 jours'], ['30', '30 jours'], ['tout', 'Depuis le début']].map(([k, l]) => {
    const u = new URL(url); u.searchParams.set('jours', k); u.searchParams.delete('format');
    const on = String(nbJours || 'tout') === k;
    return `<a class="${on ? 'on' : ''}" href="${esc(u.pathname + u.search)}">${esc(l)}</a>`;
  }).join('');
  if (!S) return `<h2>Provenance (?src)</h2><p class="m">La base D1 n'est pas encore liée au site : Cloudflare › Pages › blundercheck › Settings › Bindings › D1 database, nom <code>STATS</code>, base <code>blundercheck-stats</code>, puis redéployer.</p>`;
  if (S.erreur) return `<h2>Provenance (?src)</h2><p class="m">Erreur de lecture : ${esc(S.erreur)}</p>`;
  const n = v => v == null ? '<span class="m">—</span>' : v.toLocaleString('fr-FR');
  const pct = (a, b) => a && b ? `<small>${(a / b * 100).toLocaleString('fr-FR', { maximumFractionDigits: a / b < 0.1 ? 1 : 0 })} %</small>` : '';
  const ligne = (l, tot) => `<tr${tot ? ' class="tot"' : ''}><td>${esc(tot ? 'Total' : l.src)}</td><td>${n(l.vues)}</td><td>${n(l.visite)}${pct(l.visite, l.vues)}</td><td>${n(l.appli)}${pct(l.appli, l.visite)}</td><td>${n(l.liste)}${pct(l.liste, l.visite)}</td><td>${n(l.compte)}${pct(l.compte, l.visite)}</td><td>${n(l.partie)}${pct(l.partie, l.visite)}</td><td>${n(l.abonne)}</td></tr>`;
  const corps = S.lignes.length ? S.lignes.map(l => ligne(l)).join('') + (S.lignes.length > 1 ? ligne(S.total, true) : '') : '<tr><td colspan="8" class="m" style="text-align:left">Aucune arrivée comptée sur cette période.</td></tr>';
  const rel = Object.entries(S.releves || {}).map(([k, d]) => `${esc(k)} relevé le ${esc(new Date(d).toLocaleString('fr-FR', { timeZone: 'Europe/Paris', dateStyle: 'short', timeStyle: 'short' }))}`).join(' · ');
  return `<h2>Provenance (?src) · vues → visites → inscriptions</h2>
<p class="per">${per}</p>
<div class="tw"><table><thead><tr><th>Source</th><th>Vues vidéos</th><th>Visiteurs</th><th>→ Appli</th><th>Liste</th><th>Comptes</th><th>Parties prof</th><th>Abonnés</th></tr></thead><tbody>${corps}</tbody></table></div>
<p class="m">Vues : vidéos publiées sur la période (TikTok et YouTube seulement pour l'instant${rel ? ' ; ' + rel : ''}). Visiteurs : une fois par jour, par navigateur et par source ; le % = visiteurs ÷ vues. Appli, liste, comptes, parties : le % est rapporté aux visiteurs. Les étapes après la visite sont rattachées à la source de la 1re arrivée (cookie de 30 jours). « direct » = arrivé sans ?src. ${Object.keys(S.moi || {}).length ? 'Non comptés (toi, navigateurs passés par ?admin) : ' + esc(Object.entries(S.moi).map(([k, v]) => v + ' ' + k).join(', ')) + '. ' : ''}Compteur démarré le ${esc((S.depuis || "2026-10-23").split("-").reverse().join("/"))}.</p>`;
}
