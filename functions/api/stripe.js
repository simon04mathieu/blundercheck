// Cloudflare Pages Function : POST /api/stripe  (webhook Stripe)
// Met à jour la formule du compte quand un abonnement est payé, renouvelé, en retard ou résilié.
// Événements à cocher dans Stripe : checkout.session.completed, customer.subscription.created,
// customer.subscription.updated, customer.subscription.deleted
import { json, signatureStripeOk, lireCompte, compteOuCree, ecrireCompte } from '../../lib/compte.js';

const ACTIFS = ['active', 'trialing', 'past_due'];

async function majAbonnement(env, sub) {
  let email = sub.metadata && sub.metadata.email;
  if (!email && sub.customer) email = await env.COMPTES.get('client:' + sub.customer);
  if (!email) return;
  const u = await compteOuCree(env, email);
  const fin = sub.current_period_end || (sub.items && sub.items.data && sub.items.data[0] && sub.items.data[0].current_period_end) || null;
  u.client = sub.customer || u.client;
  u.abonnement = sub.id;
  u.statut = sub.status;
  u.plan = ACTIFS.includes(sub.status) ? 'plus' : 'gratuit';
  u.fin = fin;
  u.resiliation = !!sub.cancel_at_period_end;
  await ecrireCompte(env, u);
  if (u.client) await env.COMPTES.put('client:' + u.client, email);
}

export async function onRequestPost({ request, env }) {
  if (!env.COMPTES || !env.STRIPE_WEBHOOK_SECRET) return json(503, { error: 'Non configuré.' });
  const corps = await request.text();
  if (!(await signatureStripeOk(env.STRIPE_WEBHOOK_SECRET, request.headers.get('Stripe-Signature'), corps))) return json(400, { error: 'Signature invalide.' });
  const ev = JSON.parse(corps), o = ev.data && ev.data.object || {};
  // un même événement peut arriver deux fois : on ne le traite qu'une fois
  if (await env.COMPTES.get('ev:' + ev.id)) return json(200, { ok: true, deja: true });
  if (ev.type === 'checkout.session.completed') {
    const email = (o.client_reference_id || (o.customer_details && o.customer_details.email) || '').toLowerCase();
    if (email && o.customer) {
      const u = await compteOuCree(env, email);
      u.client = o.customer;
      if (o.mode === 'subscription') { u.plan = 'plus'; u.statut = 'active'; u.fin = u.fin || Math.floor(Date.now() / 1000) + 31 * 86400; }
      await ecrireCompte(env, u);
      await env.COMPTES.put('client:' + o.customer, email);
    }
  } else if (/^customer\.subscription\.(created|updated|deleted)$/.test(ev.type)) {
    await majAbonnement(env, ev.type.endsWith('deleted') ? { ...o, status: 'canceled' } : o);
  }
  await env.COMPTES.put('ev:' + ev.id, '1', { expirationTtl: 60 * 60 * 24 * 7 });
  return json(200, { ok: true });
}
