// Cloudflare Pages Function : POST /api/src
// Reçoit les arrivées envoyées par les pages : {src, evts: ['visite', 'appli']}.
// Le navigateur ne l'envoie qu'une fois par jour et par source (dédoublonnage côté page).
import { origineOk } from '../../lib/compte.js';
import { SRC_OK, ETAPES_NAVIGATEUR, compterPlusTard } from '../../lib/src.js';

const rien = (status = 204) => new Response(null, { status, headers: { 'cache-control': 'no-store' } });

export async function onRequestPost(ctx) {
  const { request } = ctx;
  if (!origineOk(request)) return rien(403);
  let b;
  try { b = JSON.parse((await request.text()).slice(0, 500)); } catch { return rien(400); }
  const src = String(b.src || '').toLowerCase();
  const evts = [...new Set((Array.isArray(b.evts) ? b.evts : []).filter(e => ETAPES_NAVIGATEUR.includes(e)))];
  if (!SRC_OK.test(src) || !evts.length) return rien(400);
  compterPlusTard(ctx, src, evts);
  return rien();
}
