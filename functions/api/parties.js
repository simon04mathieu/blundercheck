// Cloudflare Pages Function : /api/parties
// Synchronise la liste des parties (PGN, couleur, commentaires du prof) entre les appareils d'un compte.
// Les évaluations Stockfish ne sont pas envoyées : chaque appareil les recalcule, gratuitement.
import { json, origineOk, lireSession } from '../../lib/compte.js';

const MAX = 4 * 1024 * 1024;

export async function onRequestGet({ request, env }) {
  if (!env.COMPTES) return json(503, { error: 'Non configuré.' });
  const email = await lireSession(request, env);
  if (!email) return json(401, { error: 'Non connecté.' });
  const v = await env.COMPTES.get('lib:' + email);
  return new Response(v || '{"parties":[],"maj":0}', { headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
}

export async function onRequestPut({ request, env }) {
  if (!origineOk(request)) return json(403, { error: 'Origine refusée.' });
  if (!env.COMPTES) return json(503, { error: 'Non configuré.' });
  const email = await lireSession(request, env);
  if (!email) return json(401, { error: 'Non connecté.' });
  const corps = await request.text();
  if (corps.length > MAX) return json(413, { error: 'Bibliothèque trop grande pour la synchronisation.' });
  let b; try { b = JSON.parse(corps); } catch { return json(400, { error: 'Demande illisible.' }); }
  if (!Array.isArray(b.parties)) return json(400, { error: 'Demande invalide.' });
  await env.COMPTES.put('lib:' + email, JSON.stringify({ parties: b.parties.slice(0, 2000), maj: Date.now() }));
  return json(200, { ok: true });
}
