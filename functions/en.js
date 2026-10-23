// Cloudflare Pages Function : GET /en
// Version anglaise du site : la même page que « / » (index.html), servie à l'adresse /en avec l'anglais forcé à l'arrivée.
// Rien n'est copié : la page est reprise à chaque visite, donc toujours à jour. Fiche : site/architecture-et-deploiement.md.
// L'anglais est imposé une fois par onglet (sessionStorage) : si le visiteur choisit FR ensuite, son choix est respecté.

const SITE = 'https://blundercheck.app';
const TEXTES = {
  description: 'BlunderCheck analyzes all your chess games with Stockfish, and an AI coach explains every move with a tip.',
  ogTitle: 'BlunderCheck: the chess coach that analyzes all your games',
  ogDescription: 'Import your Chess.com or Lichess game: every move explained, a tip each time, and your mistakes turned into puzzles.',
  titre: 'BlunderCheck · Chess game analysis with an AI coach',
};
const FORCER = "<script>try{if(!sessionStorage.getItem('bc-en')){sessionStorage.setItem('bc-en','1');localStorage.setItem('bc-lang','en');}}catch(e){}</script>";

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  if (url.pathname !== '/en') return Response.redirect(url.origin + '/en' + url.search, 301);   // /en/ → /en (sinon Stockfish se chargerait depuis /en/)
  const page = await env.ASSETS.fetch(new Request(url.origin + '/', { headers: { accept: 'text/html' } }));
  if (!page.ok) return page;
  const attr = (nom, valeur) => ({ element(e) { e.setAttribute(nom, valeur); } });
  const reponse = new HTMLRewriter()
    .on('html', attr('lang', 'en'))
    .on('meta[charset]', { element(e) { e.after(FORCER + `<link rel="canonical" href="${SITE}/en"><meta property="og:locale" content="en_US">`, { html: true }); } })
    .on('meta[name="description"]', attr('content', TEXTES.description))
    .on('meta[property="og:title"]', attr('content', TEXTES.ogTitle))
    .on('meta[property="og:description"]', attr('content', TEXTES.ogDescription))
    .on('meta[property="og:url"]', attr('content', SITE + '/en'))
    .on('title', { element(e) { e.setInnerContent(TEXTES.titre); } })
    .transform(page);
  const h = new Headers(reponse.headers);
  h.set('content-type', 'text/html; charset=utf-8');
  h.set('cache-control', 'public, max-age=0, must-revalidate');
  h.set('content-language', 'en');
  h.delete('etag');
  return new Response(reponse.body, { status: 200, headers: h });
}
