// Cloudflare Pages Function : GET /api/editeur
// Adresse de l'éditeur pour les mentions légales. Elle n'est PAS dans le code (dépôt public) :
// elle est rangée dans la base D1 `blundercheck-stats`, table `editeur` (cle = 'adresse').
// Affichée seulement quand un visiteur clique « Afficher l'adresse » ; jamais indexée
// (robots.txt interdit /api/, en-tête X-Robots-Tag noindex). Fiche : admin/juridique.md.
export async function onRequestGet({ request, env }) {
  const h = { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', 'x-robots-tag': 'noindex, nofollow, noarchive' };
  if (request.headers.get('x-bc') !== '1') return new Response('{}', { status: 400, headers: h });
  let adresse = null;
  try { const r = await env.STATS.prepare("SELECT valeur FROM editeur WHERE cle = 'adresse'").first(); adresse = r && r.valeur; } catch { }
  return new Response(JSON.stringify({ adresse }), { status: adresse ? 200 : 503, headers: h });
}
