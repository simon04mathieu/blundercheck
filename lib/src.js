// Compteur de provenance (?src=…) : outils communs aux fonctions serveur.
// Base D1 liée sous le nom STATS (table compteur : jour, src, evt, n). Sans liaison, tout est ignoré sans erreur.
// Fiche : site/compteur-src.md dans le projet claude.ai.

export const SRC_OK = /^[a-z0-9][a-z0-9-]{0,29}$/;

// Étapes de l'entonnoir, dans l'ordre
export const ETAPES = ['visite', 'appli', 'liste', 'compte', 'partie', 'abonne'];
// Celles que le navigateur a le droit d'envoyer lui-même (les autres sont comptées par le serveur)
export const ETAPES_NAVIGATEUR = ['visite', 'appli'];

// Source d'origine du visiteur : cookie bc_src posé par la page à la première arrivée avec ?src (30 jours)
export function srcDe(request) {
  const m = (request.headers.get('Cookie') || '').match(/(?:^|;\s*)bc_src=([a-z0-9-]{1,30})/);
  return m && SRC_OK.test(m[1]) ? m[1] : 'direct';
}

export async function compter(env, src, evts) {
  if (!env.STATS || !evts || !evts.length) return;
  const jour = new Date().toISOString().slice(0, 10);
  src = SRC_OK.test(src || '') ? src : 'direct';
  try {
    const st = env.STATS.prepare('INSERT INTO compteur (jour, src, evt, n) VALUES (?1, ?2, ?3, 1) ON CONFLICT (jour, src, evt) DO UPDATE SET n = n + 1');
    await env.STATS.batch(evts.map(e => st.bind(jour, src, e)));
  } catch (e) { console.log('Compteur src', String(e)); }
}

// Lancer le comptage sans retarder la réponse
export function compterPlusTard(ctx, src, evts) {
  const p = compter(ctx.env, src, evts);
  if (ctx.waitUntil) ctx.waitUntil(p); else return p;
}
