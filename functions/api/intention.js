// Cloudflare Pages Function : POST /api/intention
// Test d'intention de paiement (fiche site/test-intention-paiement.md). Aucun paiement, aucune donnée personnelle :
//   {evt: 'offre' | 'clic' | 'clic-an' | 'clic-mois'} → compteur (clic = au moins un prix cliqué) D1 (source = 1re arrivée, cookie bc_src)
//   {evt: 'reponse', choix: 'an'|'mois', texte, lang} → compteur + texte libre dans la table intention_reponses
// La page dédoublonne (une fois par jour et par navigateur pour chaque événement).
import { origineOk } from '../../lib/compte.js';
import { srcDe, compter, compterPlusTard } from '../../lib/src.js';

const rien = (status = 204) => new Response(null, { status, headers: { 'cache-control': 'no-store' } });

async function enregistrer(env, src, choix, langue, texte) {
  await compter(env, src, ['reponse']);
  if (!env.STATS) return;
  try {
    await env.STATS.prepare('INSERT INTO intention_reponses (date, src, choix, langue, texte) VALUES (?1, ?2, ?3, ?4, ?5)')
      .bind(new Date().toISOString(), src, choix, langue, texte).run();
  } catch (e) { console.log('Intention réponse', String(e)); }
}

export async function onRequestPost(ctx) {
  const { request, env } = ctx;
  if (!origineOk(request)) return rien(403);
  let b;
  try { b = JSON.parse((await request.text()).slice(0, 4000)); } catch { return rien(400); }
  const src = srcDe(request), evt = String(b && b.evt || '');
  if (evt === 'offre' || evt === 'clic' || evt === 'clic-an' || evt === 'clic-mois') { compterPlusTard(ctx, src, [evt]); return rien(); }
  if (evt === 'reponse') {
    const texte = String(b.texte || '').replace(/\s+/g, ' ').trim().slice(0, 500);
    if (!texte) return rien(400);
    const choix = b.choix === 'an' || b.choix === 'mois' ? b.choix : '';
    const p = enregistrer(env, src, choix, b.lang === 'en' ? 'en' : 'fr', texte);
    if (ctx.waitUntil) ctx.waitUntil(p); else await p;
    return rien();
  }
  return rien(400);
}
