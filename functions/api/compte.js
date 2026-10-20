// Cloudflare Pages Function : /api/compte
// GET  : état du compte (connecté ?, formule, quota du mois, paiement ouvert ?)
// POST : { action: 'lien', email } envoie un lien de connexion par e-mail ; { action: 'sortie' } déconnecte.
import { json, EMAIL, origineOk, lireSession, lireCompte, formule, quotasActifs, paiementActif, connexionActive, lireQuota, resumeQuota, cookieSortie, jeton } from '../../lib/compte.js';

export async function onRequestGet({ request, env }) {
  const base = { paiement: paiementActif(env), connexion: connexionActive(env) };
  if (!env.COMPTES) return json(200, { ...base, connecte: false });
  const email = await lireSession(request, env);
  const u = email ? await lireCompte(env, email) : null;
  const plan = formule(u);
  const qui = email || 'ip:' + (request.headers.get('CF-Connecting-IP') || 'inconnu');
  const quota = quotasActifs(env) ? resumeQuota(await lireQuota(env, qui), plan) : null;
  return json(200, { ...base, connecte: !!u, email: u ? u.email : null, plan, fin: u && u.fin || null, abonne: !!(u && u.client), quota });
}

export async function onRequestPost({ request, env }) {
  if (!origineOk(request)) return json(403, { error: 'Origine refusée.' });
  let b; try { b = await request.json(); } catch { return json(400, { error: 'Demande illisible.' }); }

  if (b.action === 'sortie') return json(200, { ok: true }, { 'set-cookie': cookieSortie() });

  if (b.action === 'lien') {
    if (!connexionActive(env)) return json(503, { error: "La connexion n'est pas encore ouverte." });
    if (b.site) return json(200, { ok: true });   // champ piège anti-robots
    const email = String(b.email || '').trim().toLowerCase();
    if (!EMAIL.test(email) || email.length > 254) return json(400, { error: 'Adresse e-mail invalide.' });
    // limites : 5 liens par connexion et 3 par adresse, par heure
    const h = new Date().toISOString().slice(0, 13), ip = request.headers.get('CF-Connecting-IP') || 'inconnu';
    for (const [cle, max] of [[`rl:${h}:ip:${ip}`, 5], [`rl:${h}:e:${email}`, 3]]) {
      const n = parseInt(await env.COMPTES.get(cle) || '0', 10);
      if (n >= max) return json(429, { error: 'Trop de demandes. Réessaie dans une heure.' });
      await env.COMPTES.put(cle, String(n + 1), { expirationTtl: 3700 });
    }
    const t = jeton();
    await env.COMPTES.put('lien:' + t, email, { expirationTtl: 15 * 60 });
    const url = new URL(request.url);
    const lien = `${url.origin}/api/connexion?t=${t}`;
    const en = b.lang === 'en';
    const sujet = en ? 'Your BlunderCheck sign-in link' : 'Ton lien de connexion à BlunderCheck';
    const texte = en
      ? `Hi,\n\nClick this link to sign in to BlunderCheck (valid for 15 minutes):\n${lien}\n\nIf you didn't ask for it, just ignore this e-mail.\n\nBlunderCheck`
      : `Bonjour,\n\nClique sur ce lien pour te connecter à BlunderCheck (valable 15 minutes) :\n${lien}\n\nSi tu n'as rien demandé, ignore simplement cet e-mail.\n\nBlunderCheck`;
    const html = `<div style="font-family:system-ui,sans-serif;max-width:480px;margin:auto;color:#1b1f1d"><h2 style="color:#2f4a3e">BlunderCheck</h2><p>${en ? 'Click the button to sign in (valid for 15 minutes).' : 'Clique sur le bouton pour te connecter (valable 15 minutes).'}</p><p><a href="${lien}" style="display:inline-block;background:#C9A45C;color:#111614;padding:12px 20px;border-radius:8px;text-decoration:none;font-weight:600">${en ? 'Sign in' : 'Me connecter'}</a></p><p style="color:#666;font-size:13px">${en ? "If you didn't ask for it, just ignore this e-mail." : "Si tu n'as rien demandé, ignore simplement cet e-mail."}</p></div>`;
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: 'Bearer ' + env.RESEND_API_KEY, 'content-type': 'application/json' },
      body: JSON.stringify({ from: env.EMAIL_FROM || 'BlunderCheck <connexion@blundercheck.app>', to: [email], subject: sujet, text: texte, html }),
    });
    if (!r.ok) { console.log('Erreur Resend', r.status, (await r.text()).slice(0, 300)); return json(502, { error: "L'e-mail n'a pas pu partir. Réessaie dans un instant." }); }
    return json(200, { ok: true });
  }
  return json(400, { error: 'Action inconnue.' });
}
