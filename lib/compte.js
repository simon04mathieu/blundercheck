// Outils communs aux fonctions serveur : sessions, comptes, formules, quotas, Stripe.
// Rien ici n'est actif tant que les secrets correspondants ne sont pas posés dans Cloudflare.

export const json = (status, obj, headers = {}) => new Response(JSON.stringify(obj), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', ...headers } });
export const EMAIL = /^[^\s@<>"']{1,64}@[^\s@<>"']{1,190}\.[a-z]{2,24}$/i;

export function origineOk(request) {
  const origin = request.headers.get('Origin');
  if (!origin) return true;
  try {
    const h = new URL(origin).hostname;
    return h === 'blundercheck.app' || h.endsWith('.blundercheck.app') || h.endsWith('.pages.dev') || h === 'localhost' || h === '127.0.0.1';
  } catch { return false; }
}

// ---------- Formules et quotas (par mois civil) ----------
export const LIMITES = {
  gratuit: { parties: 3, questions: 10 },
  plus: { parties: 100, questions: 300 },
};
export const APPELS_PAR_PARTIE = 12;   // morceaux + rattrapages + synthèse : au-delà, la même partie ne peut plus être recommentée ce mois-ci

// Les quotas par formule ne s'appliquent qu'une fois le paiement ouvert (ou si QUOTAS_ACTIFS = 1)
export const paiementActif = env => !!(env.COMPTES && env.SESSION_SECRET && env.STRIPE_SECRET_KEY && env.STRIPE_PRIX_MOIS && env.STRIPE_PRIX_AN);
export const quotasActifs = env => !!env.COMPTES && (paiementActif(env) || env.QUOTAS_ACTIFS === '1');
export const connexionActive = env => !!(env.COMPTES && env.SESSION_SECRET && env.RESEND_API_KEY);

// ---------- Encodage et signature ----------
const enc = new TextEncoder();
export const b64url = buf => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const deb64url = s => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((s.length + 3) % 4)), c => c.charCodeAt(0));
async function cleHmac(secret) { return crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']); }
export async function hmac(secret, data) { return new Uint8Array(await crypto.subtle.sign('HMAC', await cleHmac(secret), enc.encode(data))); }
const hex = u8 => [...u8].map(b => b.toString(16).padStart(2, '0')).join('');
function egal(a, b) { if (a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return d === 0; }
export const jeton = (n = 24) => b64url(crypto.getRandomValues(new Uint8Array(n)));

// ---------- Session (cookie signé, valable 90 jours) ----------
const COOKIE = 'bc_s';
const DUREE = 60 * 60 * 24 * 90;
export async function cookieSession(env, email) {
  const p = b64url(enc.encode(JSON.stringify({ e: email, x: Math.floor(Date.now() / 1000) + DUREE })));
  const s = b64url(await hmac(env.SESSION_SECRET, p));
  return `${COOKIE}=${p}.${s}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${DUREE}`;
}
export const cookieSortie = () => `${COOKIE}=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0`;
export async function lireSession(request, env) {
  if (!env.SESSION_SECRET) return null;
  const m = (request.headers.get('Cookie') || '').match(/(?:^|;\s*)bc_s=([A-Za-z0-9_-]+)\.([A-Za-z0-9_-]+)/);
  if (!m) return null;
  const attendu = b64url(await hmac(env.SESSION_SECRET, m[1]));
  if (!egal(attendu, m[2])) return null;
  try {
    const o = JSON.parse(new TextDecoder().decode(deb64url(m[1])));
    if (!o.e || o.x < Date.now() / 1000) return null;
    return String(o.e);
  } catch { return null; }
}

// ---------- Comptes ----------
export async function lireCompte(env, email) {
  const v = await env.COMPTES.get('user:' + email);
  return v ? JSON.parse(v) : null;
}
export async function ecrireCompte(env, u) { await env.COMPTES.put('user:' + u.email, JSON.stringify(u)); }
export async function compteOuCree(env, email) {
  return (await lireCompte(env, email)) || { email, plan: 'gratuit', creeLe: new Date().toISOString() };
}
// abonné tant que la période payée court (plus 3 jours de marge pour un paiement en retard)
export const formule = u => u && u.plan === 'plus' && (!u.fin || u.fin * 1000 + 3 * 864e5 > Date.now()) ? 'plus' : 'gratuit';

// ---------- Quotas ----------
export const mois = () => new Date().toISOString().slice(0, 7);
export async function lireQuota(env, qui) {
  const v = await env.COMPTES.get(`q:${mois()}:${qui}`);
  return v ? JSON.parse(v) : { parties: {}, questions: 0 };
}
export async function ecrireQuota(env, qui, q) { await env.COMPTES.put(`q:${mois()}:${qui}`, JSON.stringify(q), { expirationTtl: 60 * 60 * 24 * 40 }); }
export const resumeQuota = (q, plan) => ({ parties: Object.keys(q.parties).length, questions: q.questions, limites: LIMITES[plan] });

// ---------- Stripe (API REST, sans bibliothèque) ----------
function formulaire(obj, pre = '', out = []) {
  for (const [k, v] of Object.entries(obj)) {
    if (v === undefined || v === null) continue;
    const cle = pre ? `${pre}[${k}]` : k;
    if (typeof v === 'object') formulaire(v, cle, out); else out.push(encodeURIComponent(cle) + '=' + encodeURIComponent(String(v)));
  }
  return out.join('&');
}
export async function stripe(env, chemin, params, methode = 'POST') {
  const r = await fetch('https://api.stripe.com/v1/' + chemin + (methode === 'GET' && params ? '?' + formulaire(params) : ''), {
    method: methode,
    headers: { Authorization: 'Bearer ' + env.STRIPE_SECRET_KEY, 'content-type': 'application/x-www-form-urlencoded' },
    body: methode === 'GET' ? undefined : formulaire(params || {}),
  });
  const j = await r.json();
  if (!r.ok) throw { status: r.status, message: (j.error && j.error.message) || 'Erreur Stripe' };
  return j;
}
// Vérifie l'en-tête Stripe-Signature (t=…,v1=…) sur le corps brut, 5 minutes de tolérance
export async function signatureStripeOk(secret, entete, corps) {
  if (!secret || !entete) return false;
  const parts = Object.fromEntries(entete.split(',').map(x => x.split('=')).filter(x => x.length === 2).map(([k, v]) => [k.trim(), v.trim()]));
  const v1s = entete.split(',').filter(x => x.trim().startsWith('v1=')).map(x => x.trim().slice(3));
  if (!parts.t || !v1s.length || Math.abs(Date.now() / 1000 - Number(parts.t)) > 300) return false;
  const attendu = hex(await hmac(secret, `${parts.t}.${corps}`));
  return v1s.some(v => egal(v, attendu));
}
