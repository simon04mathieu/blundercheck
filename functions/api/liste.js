// Cloudflare Pages Function : /api/liste
// POST : inscrit une adresse e-mail sur la liste d'attente de BlunderCheck+ (espace KV « LISTE »).
// GET ?token=... : exporte la liste en CSV (jeton secret ADMIN_TOKEN, à garder pour toi).

const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { 'content-type': 'application/json; charset=utf-8' } });
const EMAIL = /^[^\s@<>"']{1,64}@[^\s@<>"']{1,190}\.[a-z]{2,24}$/i;

export async function onRequestPost({ request, env }) {
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
  if (!(await env.LISTE.get(cle))) {
    await env.LISTE.put(cle, JSON.stringify({ date: new Date().toISOString(), langue: b.lang === 'en' ? 'en' : 'fr', source: String(b.source || '').slice(0, 30) }));
  }
  return json(200, { ok: true });
}

export async function onRequestGet({ request, env }) {
  const token = new URL(request.url).searchParams.get('token');
  if (!env.LISTE || !env.ADMIN_TOKEN || token !== env.ADMIN_TOKEN) return new Response('Non autorisé', { status: 401 });
  const lignes = ['email,date,langue,source'];
  let cursor;
  do {
    const r = await env.LISTE.list({ prefix: 'email:', cursor });
    for (const k of r.keys) {
      const v = JSON.parse(await env.LISTE.get(k.name) || '{}');
      lignes.push([k.name.slice(6), v.date || '', v.langue || '', v.source || ''].join(','));
    }
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  return new Response(lignes.join('\n') + '\n', { headers: { 'content-type': 'text/csv; charset=utf-8', 'content-disposition': 'attachment; filename="liste-blundercheck.csv"' } });
}
