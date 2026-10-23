// Cloudflare Pages Function : GET /api/connexion?t=…
// Lien reçu par e-mail : ouvre la session (cookie signé) puis renvoie vers la page Mon compte.
import { lireCompte, ecrireCompte, cookieSession } from '../../lib/compte.js';
import { srcDe, compterPlusTard } from '../../lib/src.js';

export async function onRequestGet(ctx) {
  const { request, env } = ctx;
  const url = new URL(request.url), t = url.searchParams.get('t') || '';
  const retour = (q) => new Response(null, { status: 302, headers: { Location: `${url.origin}/?${q}#compte` } });
  if (!env.COMPTES || !env.SESSION_SECRET || !/^[A-Za-z0-9_-]{20,64}$/.test(t)) return retour('connexion=invalide');
  const email = await env.COMPTES.get('lien:' + t);
  if (!email) return retour('connexion=expire');
  await env.COMPTES.delete('lien:' + t);   // un lien ne sert qu'une fois
  let u = await lireCompte(env, email);
  if (!u) {   // nouveau compte : on retient d'où vient la personne (cookie bc_src de ce navigateur)
    u = { email, plan: 'gratuit', creeLe: new Date().toISOString(), src: srcDe(request) };
    compterPlusTard(ctx, u.src, ['compte']);
  }
  u.derniereConnexion = new Date().toISOString();
  await ecrireCompte(env, u);
  return new Response(null, { status: 302, headers: { Location: `${url.origin}/?connexion=ok#compte`, 'set-cookie': await cookieSession(env, email) } });
}
