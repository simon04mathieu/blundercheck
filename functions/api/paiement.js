// Cloudflare Pages Function : POST /api/paiement
// { action: 'abonner', formule: 'mois' | 'an' } -> page de paiement Stripe Checkout
// { action: 'portail' } -> espace client Stripe (changer de carte, résilier, factures)
import { json, origineOk, lireSession, compteOuCree, ecrireCompte, paiementActif, stripe } from '../../lib/compte.js';

export async function onRequestPost({ request, env }) {
  if (!origineOk(request)) return json(403, { error: 'Origine refusée.' });
  if (!paiementActif(env)) return json(503, { error: "Le paiement n'est pas encore ouvert." });
  const email = await lireSession(request, env);
  if (!email) return json(401, { error: 'Connecte-toi d’abord.', connexion: true });
  let b; try { b = await request.json(); } catch { return json(400, { error: 'Demande illisible.' }); }
  const u = await compteOuCree(env, email);
  const origin = new URL(request.url).origin;
  try {
    if (b.action === 'abonner') {
      if (b.renonciation !== true) return json(400, { error: 'Coche la case sur l’accès immédiat pour continuer.' });
      const prix = b.formule === 'mois' ? env.STRIPE_PRIX_MOIS : env.STRIPE_PRIX_AN;
      const s = await stripe(env, 'checkout/sessions', {
        mode: 'subscription',
        line_items: { 0: { price: prix, quantity: 1 } },
        success_url: `${origin}/?paiement=ok#compte`,
        cancel_url: `${origin}/?paiement=annule#tarifs`,
        client_reference_id: email,
        ...(u.client ? { customer: u.client } : { customer_email: email }),
        allow_promotion_codes: 'true',
        locale: b.lang === 'en' ? 'en' : 'fr',
        subscription_data: { metadata: { email } },
        metadata: { email, renonciation_retractation: new Date().toISOString() },
      });
      u.renonciation = new Date().toISOString();   // preuve de la demande d'exécution immédiate
      await ecrireCompte(env, u);
      return json(200, { url: s.url });
    }
    if (b.action === 'portail') {
      if (!u.client) return json(400, { error: "Tu n'as pas encore d'abonnement." });
      const s = await stripe(env, 'billing_portal/sessions', { customer: u.client, return_url: `${origin}/#compte` });
      return json(200, { url: s.url });
    }
  } catch (e) {
    console.log('Erreur Stripe', e && e.status, e && e.message);
    return json(502, { error: 'Le service de paiement ne répond pas. Réessaie dans un instant.' });
  }
  return json(400, { error: 'Action inconnue.' });
}
