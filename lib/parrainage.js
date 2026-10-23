// Parrainage de la liste d'attente (23/10/2026) : « invite 3 amis, passe dans le groupe prioritaire ».
// Table D1 `parrainage` (base STATS) : numero (ordre d'inscription), code, email, parrain (code), filleuls, langue, cree.
// D1 plutôt que KV : KV gratuit = 1 000 écritures/jour, déjà partagées avec le prof. Fiche : site/parrainage.md.

export const OBJECTIF = 3;   // filleuls pour entrer dans le groupe prioritaire
export const CODE_OK = /^[a-z2-9]{7}$/;
const ALPHABET = 'abcdefghjkmnpqrstuvwxyz23456789';   // sans i, l, o, 0, 1 (confusions)

const nouveauCode = () => Array.from(crypto.getRandomValues(new Uint8Array(7)), b => ALPHABET[b % ALPHABET.length]).join('');

// Code du parrain : cookie bc_ref posé par la page à l'arrivée avec ?ref=… (30 jours)
export function refDe(request) {
  const m = (request.headers.get('Cookie') || '').match(/(?:^|;\s*)bc_ref=([a-z2-9]{7})/);
  return m ? m[1] : null;
}

// Nouvelle inscription : crée son code et crédite le parrain. Renvoie { code, numero } ou null (base absente, erreur).
export async function inscrire(env, email, parrain, langue) {
  if (!env.STATS) return null;
  try {
    let ligne = null, nouveau = false;
    for (let essai = 0; essai < 3 && !ligne; essai++) {
      const r = await env.STATS.prepare('INSERT OR IGNORE INTO parrainage (code, email, parrain, langue, cree) VALUES (?1, ?2, ?3, ?4, ?5)')
        .bind(nouveauCode(), email, CODE_OK.test(parrain || '') ? parrain : null, langue, new Date().toISOString()).run();
      nouveau = nouveau || !!(r.meta && r.meta.changes);
      ligne = await env.STATS.prepare('SELECT numero, code, parrain FROM parrainage WHERE email = ?1').bind(email).first();
    }
    if (!ligne) return null;
    // le parrain gagne un filleul (pas soi-même)
    if (nouveau && ligne.parrain) await env.STATS.prepare('UPDATE parrainage SET filleuls = filleuls + 1 WHERE code = ?1 AND email != ?2').bind(ligne.parrain, email).run();
    return { code: ligne.code, numero: ligne.numero };
  } catch (e) { console.log('Parrainage', String(e)); return null; }
}

export async function statut(env, code) {
  if (!env.STATS || !CODE_OK.test(code || '')) return null;
  const l = await env.STATS.prepare('SELECT numero, filleuls, langue FROM parrainage WHERE code = ?1').bind(code).first();
  if (!l) return null;
  const total = await env.STATS.prepare('SELECT COUNT(*) AS n FROM parrainage').first('n');
  return { numero: l.numero, filleuls: l.filleuls, prioritaire: l.filleuls >= OBJECTIF, manque: Math.max(0, OBJECTIF - l.filleuls), total, langue: l.langue };
}

export async function resume(env) {
  if (!env.STATS) return null;
  try {
    return await env.STATS.prepare(`SELECT COUNT(*) AS inscrits, COALESCE(SUM(filleuls), 0) AS filleuls,
      SUM(CASE WHEN filleuls >= ${OBJECTIF} THEN 1 ELSE 0 END) AS prioritaires,
      SUM(CASE WHEN parrain IS NOT NULL THEN 1 ELSE 0 END) AS venus_par_parrain FROM parrainage`).first();
  } catch { return null; }
}
