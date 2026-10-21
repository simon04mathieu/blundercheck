// Cloudflare Pages Function : GET /api/stats?token=ADMIN_TOKEN
// Tableau de bord privé : usage du prof, comptes, liste d'attente. &format=json pour les chiffres bruts.
// Les visites (pages vues, provenance) sont dans Cloudflare Web Analytics.

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
    comptes, liste,
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
.b{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;position:relative}.b i{display:block;background:linear-gradient(var(--a),var(--g));border-radius:3px 3px 0 0;min-height:1px}.b span{position:absolute;bottom:-18px;left:0;right:0;text-align:center;font-size:10px;color:var(--m)}
a{color:var(--a)}p{margin:6px 0}
</style></head><body><main>
<h1>Stats BlunderCheck</h1><p class="m">Mis à jour le ${esc(new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' }))}. Les visites du site (pages vues, provenance TikTok/Google…) sont dans Cloudflare › blundercheck.app › Web Analytics.</p>
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
