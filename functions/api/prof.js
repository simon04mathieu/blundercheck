// Cloudflare Pages Function : POST /api/prof
// Relaie la demande du prof vers l'API Claude avec TA clé (variable ANTHROPIC_API_KEY),
// sans jamais l'exposer au navigateur.
// Garde-fous : origine vérifiée, taille limitée, quota par visiteur et par jour (si le KV "QUOTA" est relié).

const LIMITE_JOUR = 60;          // appels au prof par visiteur et par jour
const MAX_CARACTERES = 60000;    // taille maximale d'une demande
const MAX_TOKENS = 8192;

import { quotasActifs, lireSession, lireCompte, formule, lireQuota, ecrireQuota, LIMITES, APPELS_PAR_PARTIE } from '../../lib/compte.js';

const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { 'content-type': 'application/json; charset=utf-8' } });

export async function onRequestPost({ request, env }) {
  if (!env.ANTHROPIC_API_KEY) return json(503, { error: "Le prof n'est pas encore configuré sur ce site." });

  const origin = request.headers.get('Origin');
  if (origin) {
    const h = new URL(origin).hostname;
    const ok = h === 'blundercheck.app' || h.endsWith('.blundercheck.app') || h.endsWith('.pages.dev') || h === 'localhost';
    if (!ok) return json(403, { error: 'Origine refusée.' });
  }

  let body;
  try { body = await request.json(); } catch { return json(400, { error: 'Demande illisible.' }); }
  const messages = Array.isArray(body.messages) ? body.messages.slice(-12) : [];
  if (!messages.length || messages.some(m => !['user', 'assistant'].includes(m.role) || typeof m.content !== 'string')) return json(400, { error: 'Demande invalide.' });
  if (messages.reduce((n, m) => n + m.content.length, 0) > MAX_CARACTERES) return json(413, { error: "Cette partie est trop longue pour être commentée d'un coup." });

  // Quota par visiteur (adresse IP) et par jour, si un espace KV nommé QUOTA est relié au projet
  if (env.QUOTA) {
    const ip = request.headers.get('CF-Connecting-IP') || 'inconnu';
    const cle = `${new Date().toISOString().slice(0, 10)}:${ip}`;
    const n = parseInt(await env.QUOTA.get(cle) || '0', 10);
    if (n >= LIMITE_JOUR) return json(429, { error: "Tu as atteint la limite du prof pour aujourd'hui. Reviens demain !" });
    await env.QUOTA.put(cle, String(n + 1), { expirationTtl: 60 * 60 * 26 });
  }

  // Quotas par formule (gratuit / BlunderCheck+), par mois, une fois le paiement ouvert
  if (quotasActifs(env)) {
    const email = await lireSession(request, env);
    const plan = formule(email ? await lireCompte(env, email) : null), lim = LIMITES[plan];
    const qui = email || 'ip:' + (request.headers.get('CF-Connecting-IP') || 'inconnu');
    const q = await lireQuota(env, qui);
    const partie = (request.headers.get('x-bc-partie') || '').replace(/[^A-Za-z0-9_-]/g, '').slice(0, 40);
    const plus = plan === 'plus';
    if (partie) {
      const deja = q.parties[partie] || 0;
      if (!deja && Object.keys(q.parties).length >= lim.parties) return json(402, { error: plus ? `Tu as atteint les ${lim.parties} parties commentées de ce mois-ci.` : `Tu as utilisé tes ${lim.parties} parties commentées gratuites de ce mois-ci.`, limite: 'parties', plan });
      if (deja >= APPELS_PAR_PARTIE) return json(402, { error: 'Cette partie a déjà été commentée plusieurs fois ce mois-ci.', limite: 'partie', plan });
      q.parties[partie] = deja + 1;
    } else {
      if (q.questions >= lim.questions) return json(402, { error: plus ? `Tu as atteint les ${lim.questions} questions de ce mois-ci.` : `Tu as utilisé tes ${lim.questions} questions gratuites de ce mois-ci.`, limite: 'questions', plan });
      q.questions++;
    }
    await ecrireQuota(env, qui, q);
  }

  // Statistiques du jour (pour la page /api/stats) : appels, parties commencées, questions
  if (env.QUOTA) {
    try {
      const cle = `stats:${new Date().toISOString().slice(0, 10)}`;
      const s = JSON.parse(await env.QUOTA.get(cle) || '{"appels":0,"parties":0,"questions":0}');
      s.appels++;
      if (!request.headers.get('x-bc-partie')) s.questions++;
      else if (request.headers.get('x-bc-premier') === '1') s.parties++;
      await env.QUOTA.put(cle, JSON.stringify(s), { expirationTtl: 60 * 60 * 24 * 400 });
    } catch { }
  }

  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'x-api-key': env.ANTHROPIC_API_KEY, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
    body: JSON.stringify({
      model: env.MODELE || 'claude-haiku-5-5',
      max_tokens: Math.min(Number(body.max_tokens) || MAX_TOKENS, MAX_TOKENS),
      stream: true,
      thinking: { type: 'disabled' },  // pas de réflexion cachée facturée
      system: "Tu es le prof d'échecs de BlunderCheck. Tu réponds en français, avec bienveillance, et tu ne parles que d'échecs.",
      messages,
    }),
  });
  if (!r.ok) {
    const t = await r.text();
    console.log('Erreur API Claude', r.status, t.slice(0, 500));
    return json(r.status === 429 ? 429 : 502, { error: r.status === 429 ? 'Le prof est très demandé. Réessaie dans une minute.' : 'Le prof est indisponible pour le moment.' });
  }
  return new Response(r.body, { headers: { 'content-type': 'text/event-stream; charset=utf-8', 'cache-control': 'no-store' } });
}
