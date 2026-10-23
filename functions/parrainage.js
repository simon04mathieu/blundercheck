// Cloudflare Pages Function : GET /parrainage?c=<code>[&lang=en]
// Page de suivi du parrainage : numéro sur la liste, filleuls (objectif 3), lien personnel à partager. Fiche : site/parrainage.md.
import { statut, OBJECTIF } from '../lib/parrainage.js';

const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

const TXT = {
  fr: {
    titre: 'Mon parrainage', rang: n => `Tu es n°${n} sur la liste d'attente`,
    sur: (f, o) => `${f} ami${f > 1 ? 's' : ''} inscrit${f > 1 ? 's' : ''} sur ${o}`,
    oui: 'Tu es dans le groupe prioritaire : accès en premier au lancement de BlunderCheck+.',
    non: m => `Encore ${m} ami${m > 1 ? 's' : ''} à inviter pour passer dans le groupe prioritaire (accès en premier au lancement).`,
    lien: 'Ton lien perso', copier: 'Copier', copie: 'Copié !', partager: 'Partager', whatsapp: 'WhatsApp',
    regle: "Un ami compte quand il s'inscrit sur la liste d'attente depuis ton lien (dans les 30 jours après avoir cliqué).",
    message: "Analyse tes parties d'échecs gratuitement, avec un prof IA qui explique chaque coup : ",
    inconnu: "Ce lien de parrainage n'existe pas. Ton lien perso est dans l'e-mail de confirmation de la liste d'attente.",
    site: 'Analyser une partie', total: t => `${t} inscrit${t > 1 ? 's' : ''} au total`,
  },
  en: {
    titre: 'My invites', rang: n => `You're #${n} on the waiting list`,
    sur: (f, o) => `${f} friend${f > 1 ? 's' : ''} signed up out of ${o}`,
    oui: "You're in the priority group: first access when BlunderCheck+ launches.",
    non: m => `${m} more friend${m > 1 ? 's' : ''} to invite to join the priority group (first access at launch).`,
    lien: 'Your personal link', copier: 'Copy', copie: 'Copied!', partager: 'Share', whatsapp: 'WhatsApp',
    regle: 'A friend counts when they join the waiting list from your link (within 30 days of clicking it).',
    message: 'Analyze your chess games for free, with an AI coach that explains every move: ',
    inconnu: "This invite link doesn't exist. Your personal link is in the waiting-list confirmation e-mail.",
    site: 'Analyze a game', total: t => `${t} sign-up${t > 1 ? 's' : ''} in total`,
  },
};

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const code = (url.searchParams.get('c') || '').toLowerCase();
  const s = await statut(env, code).catch(() => null);
  const lang = url.searchParams.get('lang') === 'en' || (!url.searchParams.get('lang') && s && s.langue === 'en') ? 'en' : 'fr';
  const T = TXT[lang], en = lang === 'en';
  const accueil = en ? '/en' : '/';
  let corps;
  if (!s) {
    corps = `<p class="m">${esc(T.inconnu)}</p><a class="btn" href="${accueil}">${esc(T.site)}</a>`;
  } else {
    const lien = `https://blundercheck.app/${en ? 'en' : ''}?ref=${code}`;
    const pct = Math.min(100, Math.round(s.filleuls / OBJECTIF * 100));
    corps = `<div class="rang">${esc(T.rang(s.numero))}</div><p class="m">${esc(T.total(s.total))}</p>
<div class="carte"><div class="l">${esc(T.sur(Math.min(s.filleuls, 99), OBJECTIF))}</div>
<div class="barre"><i style="width:${pct}%"></i></div>
<p class="${s.prioritaire ? 'ok' : ''}">${esc(s.prioritaire ? T.oui : T.non(s.manque))}</p></div>
<div class="l">${esc(T.lien)}</div>
<div class="ligne"><input readonly value="${esc(lien)}" id="lien"><button class="btn" id="cp">${esc(T.copier)}</button></div>
<div class="ligne"><button class="btn sec" id="pa">${esc(T.partager)}</button><a class="btn sec" target="_blank" rel="noopener" href="https://wa.me/?text=${encodeURIComponent(T.message + lien)}">${esc(T.whatsapp)}</a></div>
<p class="m petit">${esc(T.regle)}</p>
<script>const L=${JSON.stringify(lien)},M=${JSON.stringify(T.message)};
document.getElementById('cp').onclick=e=>{document.getElementById('lien').select();(navigator.clipboard?navigator.clipboard.writeText(L):Promise.reject()).catch(()=>document.execCommand('copy')).then(()=>{e.target.textContent=${JSON.stringify(T.copie)};});};
document.getElementById('pa').onclick=()=>{if(navigator.share)navigator.share({text:M,url:L}).catch(()=>{});else window.open('https://wa.me/?text='+encodeURIComponent(M+L),'_blank');};</script>`;
  }
  const html = `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>${esc(T.titre)} · BlunderCheck</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600;700&family=Geist+Mono&display=swap">
<style>
:root{--bg:#111614;--c:#18201C;--l:#2A342F;--t:#EDE7D8;--m:#A8A99A;--a:#C9A45C;--g:#2F4A3E;--v:#70926C}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--t);font:16px/1.5 Geist,system-ui,sans-serif}
main{max-width:520px;margin:0 auto;padding:28px 16px 48px}a{color:var(--a)}
.logo{font-weight:700;letter-spacing:.02em;color:var(--a);text-decoration:none;font-size:15px}
h1{font-size:28px;margin:14px 0 4px}.rang{font-size:20px;font-weight:700}.m{color:var(--m);margin:4px 0 18px}.petit{font-size:13px;margin-top:18px}
.carte{background:var(--c);border:1px solid var(--l);border-radius:14px;padding:16px;margin-bottom:18px}.carte p{margin:10px 0 0}.ok{color:#9CC596;font-weight:600}
.l{color:var(--m);font-size:12px;text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px}
.barre{height:10px;background:var(--l);border-radius:99px;overflow:hidden}.barre i{display:block;height:100%;background:linear-gradient(90deg,var(--v),var(--a));border-radius:99px}
.ligne{display:flex;gap:8px;margin-bottom:10px}input{flex:1;min-width:0;background:var(--c);color:var(--t);border:1px solid var(--l);border-radius:10px;padding:11px;font:13px "Geist Mono",monospace}
.btn{display:inline-flex;align-items:center;justify-content:center;flex:none;background:var(--a);color:#1A1407;border:0;border-radius:10px;padding:11px 16px;font:600 15px Geist,system-ui,sans-serif;cursor:pointer;text-decoration:none}
.btn.sec{flex:1;background:var(--g);color:var(--t)}
</style></head><body><main><a class="logo" href="${accueil}">BlunderCheck</a><h1>${esc(T.titre)}</h1>${corps}</main></body></html>`;
  return new Response(html, { headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store', 'x-robots-tag': 'noindex', 'referrer-policy': 'no-referrer' } });
}
