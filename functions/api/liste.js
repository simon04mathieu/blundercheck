// Cloudflare Pages Function : /api/liste
// POST : inscrit une adresse e-mail sur la liste d'attente de BlunderCheck+ (espace KV « LISTE »).
// GET ?token=... : exporte la liste en CSV (jeton secret ADMIN_TOKEN, à garder pour toi).

import { srcDe, compterPlusTard } from '../../lib/src.js';
import { refDe, inscrire } from '../../lib/parrainage.js';

const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { 'content-type': 'application/json; charset=utf-8' } });
const EMAIL = /^[^\s@<>"']{1,64}@[^\s@<>"']{1,190}\.[a-z]{2,24}$/i;

export async function onRequestPost(ctx) {
  const { request, env } = ctx;
  if (!env.LISTE) return json(503, { error: "La liste d'attente n'est pas encore configurée." });
  const origin = request.headers.get('Origin');
  if (origin) {
    const h = new URL(origin).hostname;
    if (!(h === 'blundercheck.app' || h.endsWith('.blundercheck.app') || h.endsWith('.pages.dev') || h === 'localhost')) return json(403, { error: 'Origine refusée.' });
  }
  let b;
  try { b = await request.json(); } catch { return json(400, { error: 'Demande illisible.' }); }
  if (b.site) return json(200, { ok: true }); // champ piège : les robots le remplissent
  const email = String(b.email || '').trim().toLowerCase();
  if (!EMAIL.test(email) || email.length > 254) return json(400, { error: 'Adresse e-mail invalide.' });
  if (b.consent !== true) return json(400, { error: 'Coche la case pour accepter de recevoir l’e-mail de lancement.' });

  // limite : 5 inscriptions par adresse IP et par jour
  const ip = request.headers.get('CF-Connecting-IP') || 'inconnu';
  const cleIp = `ip:${new Date().toISOString().slice(0, 10)}:${ip}`;
  const n = parseInt(await env.LISTE.get(cleIp) || '0', 10);
  if (n >= 5) return json(429, { error: 'Trop d’inscriptions depuis cette connexion aujourd’hui.' });
  await env.LISTE.put(cleIp, String(n + 1), { expirationTtl: 60 * 60 * 26 });

  const cle = `email:${email}`;
  let parrainage = null;
  if (!(await env.LISTE.get(cle))) {
    // parrainage : code personnel de la personne, et un filleul de plus pour celui qui l'a invitée (cookie bc_ref)
    parrainage = await inscrire(env, email, refDe(request), b.lang === 'en' ? 'en' : 'fr');
    await env.LISTE.put(cle, JSON.stringify({ date: new Date().toISOString(), langue: b.lang === 'en' ? 'en' : 'fr', source: String(b.source || '').slice(0, 30), canal: srcDe(request), parrain: refDe(request) || undefined, code: parrainage ? parrainage.code : undefined }));
    compterPlusTard(ctx, srcDe(request), ['liste']);
    // e-mail de confirmation, si l'envoi d'e-mails est configuré (Resend) ; une erreur d'envoi ne bloque pas l'inscription
    if (env.RESEND_API_KEY) {
      const en = b.lang === 'en', site = new URL(request.url).origin;
      const lien = parrainage ? `https://blundercheck.app/${en ? 'en' : ''}?ref=${parrainage.code}` : '';
      const invite = !lien ? '' : en
        ? `\n\nWant to be in the priority group at launch? Invite 3 friends with your personal link: ${lien}\nTrack your invites: https://blundercheck.app/parrainage?c=${parrainage.code}`
        : `\n\nTu veux être dans le groupe prioritaire au lancement ? Invite 3 amis avec ton lien perso : ${lien}\nSuis tes invitations : https://blundercheck.app/parrainage?c=${parrainage.code}`;
      const sujet = en ? "You're on the BlunderCheck+ waiting list" : 'Tu es sur la liste d’attente de BlunderCheck+';
      const texte = en
        ? `Hi,

You're on the list! We'll send you a single e-mail on the day BlunderCheck+ launches, with the launch price for early sign-ups.

Until then, analysis stays free: ${site}${invite}

To be removed from the list, just reply to this e-mail.

BlunderCheck`
        : `Bonjour,

C’est noté ! Tu recevras un seul e-mail, le jour du lancement de BlunderCheck+, avec le prix de lancement réservé aux premiers inscrits.

En attendant, l’analyse reste gratuite : ${site}${invite}

Pour être retiré de la liste, réponds simplement à cet e-mail.

BlunderCheck`;
      const html = `<div style="font-family:system-ui,sans-serif;max-width:480px;margin:auto;color:#1b1f1d"><h2 style="color:#2f4a3e">BlunderCheck</h2>${texte.split('\n\n').slice(1, -1).map(p => `<p>${p.replace(/https?:\/\/[^\s]+/g, u => `<a href="${u}" style="color:#2f4a3e">${u.replace(/^https?:\/\//, '')}</a>`).replace(/\n/g, '<br>')}</p>`).join('')}</div>`;
      try {
        const r = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: { Authorization: 'Bearer ' + env.RESEND_API_KEY, 'content-type': 'application/json' },
          body: JSON.stringify({ from: env.EMAIL_FROM || 'BlunderCheck <connexion@blundercheck.app>', reply_to: 'contact@blundercheck.app', to: [email], subject: sujet, text: texte, html }),
        });
        if (!r.ok) console.log('Erreur Resend (liste)', r.status, (await r.text()).slice(0, 300));
      } catch (e) { console.log('Erreur Resend (liste)', String(e)); }
    }
  }
  return json(200, parrainage ? { ok: true, code: parrainage.code, numero: parrainage.numero } : { ok: true });
}

export async function onRequestGet({ request, env }) {
  const token = new URL(request.url).searchParams.get('token');
  if (!env.LISTE || !env.ADMIN_TOKEN || token !== env.ADMIN_TOKEN) return new Response('Non autorisé', { status: 401 });
  const lignes = ['email,date,langue,source,canal'];
  let cursor;
  do {
    const r = await env.LISTE.list({ prefix: 'email:', cursor });
    for (const k of r.keys) {
      const v = JSON.parse(await env.LISTE.get(k.name) || '{}');
      lignes.push([k.name.slice(6), v.date || '', v.langue || '', v.source || '', v.canal || ''].join(','));
    }
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  return new Response(lignes.join('\n') + '\n', { headers: { 'content-type': 'text/csv; charset=utf-8', 'content-disposition': 'attachment; filename="liste-blundercheck.csv"' } });
}
