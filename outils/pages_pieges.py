#!/usr/bin/env python3
"""Pages Google « un piège = une page » (demande de Simon, 29/10) : blundercheck.app/traps/<piège>.

    python3 outils/pages_pieges.py <dossier du site, branche main>

Écrit dans le site : traps/<slug>/index.html (un piège), traps/index.html (la liste), sitemap.xml, robots.txt.
Sources : stock/pieges-candidats.json (pièges vérifiés Stockfish, réserve du Scénariste) + CLASSIQUES ci-dessous.
Chaque page : 3 échiquiers (le piège posé, la gaffe, le mat), la ligne complète, une explication courte, et le bouton
vers /try. Les coups sont rejoués avec python-chess (une ligne illégale ou sans mat est écartée).
Ne touche ni à index.html, ni aux fonctions /api, ni au paiement.
"""
import html, json, os, re, sys
import chess, chess.svg

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SITE = "https://blundercheck.app"
TROP_FACILES = {"e4 Nc6 Bc4 Nb8 Qh5 c6 Bxf7#", "f3 d5 Kf2 e5 Kg3 Bc5 c4 Qg5#"}
CLASSIQUES = [  # pièges déjà en vidéo (lignes vérifiées par le producteur, Stockfish)
    {"ouverture": "Légal's Mate (Philidor Defense)", "ligne_san": "e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6 Nxe5 Bxd1 Bxf7+ Ke7 Nd5#", "gaffe_index": 9, "coup_juste": "dxe5"},
    {"ouverture": "Kieninger Trap (Budapest Gambit)", "ligne_san": "d4 Nf6 c4 e5 dxe5 Ng4 Bf4 Nc6 Nf3 Bb4+ Nbd2 Qe7 a3 Ngxe5 axb4 Nd3#", "gaffe_index": 14, "coup_juste": "Nxe5"},
    {"ouverture": "Vienna Game Frankenstein-Dracula Trap", "ligne_san": "e4 e5 Nc3 Nf6 Bc4 Nxe4 Qh5 Nxc3 Qxf7#", "gaffe_index": 7, "coup_juste": "Nd6"},
    {"ouverture": "Italian Game Queen Trap", "ligne_san": "e4 e5 Nf3 Bc5 Bc4 Qf6 Nxe5 Qxf2#", "gaffe_index": 6, "coup_juste": "O-O"},
]
NOMS_DEBUT = [("e4 d5", "Scandinavian Defense"), ("e4 c6", "Caro-Kann Defense"), ("e4 e6", "French Defense"), ("d4 f5", "Dutch Defense"),
              ("e4 c5", "Sicilian Defense"), ("e4 e5", "Open Game"), ("d4 d5", "Queen's Pawn Game"), ("d4 Nf6", "Indian Defense")]
COULEURS = {"square light": "#D9D0BC", "square dark": "#1F3B30", "square light lastmove": "#E6CF8F", "square dark lastmove": "#9C8240",
            "margin": "#111614", "coord": "#A7B0A8"}


def slug(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:70]


def nom(c):
    o = (c.get("ouverture") or "").strip(" ?")
    if o: return o
    for debut, n in NOMS_DEBUT:
        if c["ligne_san"].startswith(debut + " "): return n
    return "Opening"


def numerotee(sans, depart=0):
    out = []
    for i, s in enumerate(sans, depart):
        if i % 2 == 0: out.append(f"{i // 2 + 1}.{s}")
        elif not out or i == depart: out.append(f"{i // 2 + 1}...{s}")
        else: out.append(s)
    return " ".join(out)


def svg(b, fleche=None, couleur="#E5534B", flip=False):
    fl = [chess.svg.Arrow(fleche.from_square, fleche.to_square, color=couleur)] if fleche else []
    s = chess.svg.board(b, arrows=fl, lastmove=b.peek() if b.move_stack else None, size=360, colors=COULEURS,
                        flipped=flip, coordinates=True, check=b.king(b.turn) if b.is_check() else None)
    return s.replace("<svg ", '<svg role="img" class="board" ', 1)


def preparer(c):
    sans = c["ligne_san"].split()
    b = chess.Board(); coups = []
    for s in sans: m = b.parse_san(s); coups.append(m); b.push(m)
    if not b.is_checkmate() or " ".join(sans) in TROP_FACILES: return None
    g = c.get("gaffe_index", (c["demi_coup_gaffe"] - 1) if c.get("demi_coup_gaffe") else None)
    if g is None: g = len(sans) - (2 * c.get("mat_en", 1) - 1) - 1
    victime = "White" if g % 2 == 0 else "Black"; heros = "Black" if victime == "White" else "White"
    n = nom(c); gaffe = sans[g]; mat_en = (len(sans) - g) // 2
    titre = f"{n}{'' if 'trap' in n.lower() else ' trap'}: {gaffe}?? and mate in {mat_en}"
    return {"nom": n, "titre": titre, "slug": slug(f"{n}-{gaffe}"), "sans": sans, "coups": coups, "g": g, "victime": victime,
            "heros": heros, "mat_en": mat_en, "juste": c.get("coup_juste"), "parties": c.get("parties_reelles"),
            "note": c.get("note_moyenne")}


CSS = """:root{--bg:#111614;--card:#18201C;--line:#29332D;--fg:#EDE7D8;--mut:#A7B0A8;--accent:#C9A45C;--ink:#1A1407;--bad:#E5534B;--good:#5DBB8A}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font-family:Geist,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
main{max-width:640px;margin:0 auto;padding:24px 16px 48px}a{color:var(--accent)}
.logo{display:inline-flex;align-items:center;gap:10px;font-weight:700;color:var(--fg);text-decoration:none}
.logo i{width:28px;height:28px;border-radius:7px;background:#111614;border:1px solid var(--line);position:relative}
.logo i:before,.logo i:after{content:"";position:absolute;width:9px;height:9px;border-radius:2px}
.logo i:before{left:6px;top:6px;background:var(--accent)}.logo i:after{left:13px;top:13px;background:#fff}
h1{font-family:Fraunces,Georgia,serif;font-weight:800;font-size:34px;line-height:1.1;letter-spacing:-.02em;margin:22px 0 10px}
h2{font-size:20px;margin:30px 0 8px}p,li{color:var(--mut);font-size:16px;line-height:1.55}
.step{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px;margin:14px 0}
.step h3{margin:0 0 8px;font-size:16px;color:var(--fg)}.board{width:100%;height:auto;max-width:360px;display:block;margin:0 auto}
.moves{font-family:ui-monospace,Menlo,monospace;font-size:15px;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px;line-height:1.7;word-spacing:2px}
.bad{color:var(--bad);font-weight:700}.good{color:var(--good);font-weight:700}
.cta{display:block;text-align:center;background:var(--accent);color:var(--ink);font-weight:700;font-size:18px;padding:16px;border-radius:14px;text-decoration:none;margin:26px 0 6px}
.small{font-size:13px;color:var(--mut);text-align:center}ul.list{padding-left:18px}ul.list li{margin:6px 0}
footer{color:var(--mut);font-size:13px;text-align:center;margin-top:34px}"""

COMPTEUR = """<script>/* Compteur ?src (site/compteur-src.md) ; pages /traps : arrivée Google ou Bing comptée « google ». */
(function(){try{var u=new URL(location.href),q=u.searchParams,s=(q.get('src')||'').toLowerCase(),ok=/^[a-z0-9][a-z0-9-]{0,29}$/,ls=null;
try{ls=window.localStorage;}catch(e){}if(!ok.test(s))s='';
if(!s&&/google\\.|bing\\.|duckduckgo\\.|qwant\\.|ecosia\\./.test(document.referrer))s='google';
var c=document.cookie.match(/(?:^|;\\s*)bc_src=([a-z0-9-]{1,30})/),sec=location.protocol==='https:'?'; Secure':'';
if(q.has('src')){q.delete('src');history.replaceState(history.state,'',u.pathname+(q.toString()?'?'+q:'')+u.hash);}
if(ls&&ls.getItem('bc-moi'))return;
if(s&&!c)document.cookie='bc_src='+s+'; Path=/; Max-Age=2592000; SameSite=Lax'+sec;
var src=s||'direct',j=new Date().toISOString().slice(0,10),vu={};try{vu=JSON.parse(ls&&ls.getItem('bc-vu')||'{}');}catch(e){}
if(vu.j!==j)vu={j:j};if(vu[src])return;
var b=JSON.stringify({src:src,evts:['visite']}),fini=function(){vu[src]=1;try{ls&&ls.setItem('bc-vu',JSON.stringify(vu));}catch(e){}};
if(navigator.sendBeacon&&navigator.sendBeacon('/api/src',new Blob([b],{type:'application/json'})))fini();
else fetch('/api/src',{method:'POST',body:b,keepalive:true,headers:{'content-type':'application/json'}}).then(fini,function(){});
}catch(e){}})();</script>"""


def tete(titre, desc, chemin, ld=None):
    e = html.escape
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(titre)} · BlunderCheck</title>
<meta name="description" content="{e(desc)}"><link rel="canonical" href="{SITE}{chemin}">
<meta property="og:title" content="{e(titre)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="article">
<meta name="theme-color" content="#111614">
{COMPTEUR}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@144,800&family=Geist:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>{f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ''}</head><body><main>
<a class="logo" href="/traps"><i></i>BlunderCheck · Chess Traps</a>"""


def page(p):
    sans, coups, g = p["sans"], p["coups"], p["g"]
    flip = p["heros"] == "Black"
    b1 = chess.Board(); [b1.push(m) for m in coups[:g]]
    b2 = b1.copy(); b2.push(coups[g])
    b3 = chess.Board(); [b3.push(m) for m in coups]
    pose = numerotee(sans[:g]); gaffe_txt = numerotee([sans[g]], g); fin = numerotee(sans[g + 1:], g + 1)
    juste = f" The safe move was <span class=\"good\">{html.escape(p['juste'])}</span>." if p.get("juste") and p["juste"] != sans[g] else ""
    reel = (f" This exact blunder shows up again and again in real online games (Lichess puzzle database, puzzles rated about {p['note']})."
            if p.get("parties") else "")
    desc = (f"{p['nom']}: after {pose[:60]}…, {p['victime']} plays {sans[g]}?? and {p['heros']} mates in {p['mat_en']}. "
            f"See the trap move by move, and how to avoid it.")[:158]
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": p["titre"], "description": desc,
          "publisher": {"@type": "Organization", "name": "BlunderCheck", "url": SITE}}
    return tete(p["titre"], desc, f"/traps/{p['slug']}", ld) + f"""
<h1>{html.escape(p['titre'])}</h1>
<p>A trap from the <b>{html.escape(p['nom'])}</b>. {p['victime']} grabs something that looks free, and {p['heros']} delivers mate in {p['mat_en']}.{reel}</p>
<div class="step"><h3>1. The trap is set</h3>{svg(b1, flip=flip)}<p>After <span class="moves" style="display:inline;padding:2px 6px">{html.escape(pose)}</span>, it is {p['victime']}'s move. Everything looks normal.</p></div>
<div class="step"><h3>2. The blunder: <span class="bad">{html.escape(gaffe_txt)}??</span></h3>{svg(b2, coups[g], "#E5534B", flip)}<p>It looks tempting, but it walks straight into the trap.{juste}</p></div>
<div class="step"><h3>3. Mate in {p['mat_en']}: <span class="good">{html.escape(fin)}</span></h3>{svg(b3, coups[-1], "#5DBB8A", flip)}<p>Checkmate. {p['victime']}'s king has no escape.</p></div>
<h2>The full line</h2><p class="moves">{html.escape(numerotee(sans))}</p>
<h2>How not to fall for it</h2><ul class="list"><li>Before taking a "free" piece, look at every check your opponent gets next move.</li>
<li>Ask what your opponent's last move is aiming at, not only what it leaves hanging.</li></ul>
<a class="cta" href="/try">Did you blunder like this? Check your last game, free</a>
<p class="small">Type your Chess.com or Lichess username: Stockfish finds your mistakes, an AI coach explains them. No sign-up.</p>
<footer><a href="/traps">All chess traps</a> · <a href="/en">blundercheck.app</a></footer></main></body></html>
"""


def index(pages):
    li = "\n".join(f'<li><a href="/traps/{p["slug"]}">{html.escape(p["titre"])}</a></li>' for p in sorted(pages, key=lambda x: x["titre"]))
    return tete("Chess opening traps that real players fall for", "Short chess opening traps with mate, each shown in 3 boards: the setup, the blunder and the mate. Check your own games for free.", "/traps") + f"""
<h1>Chess opening traps real players fall for</h1>
<p>Each trap in 3 boards: the setup, the blunder, the mate. Most of them come from real online games.</p>
<ul class="list">{li}</ul>
<a class="cta" href="/try">Check your last game for blunders, free</a>
<footer><a href="/en">blundercheck.app</a></footer></main></body></html>
"""


def main(site):
    cands = json.load(open(os.path.join(ROOT, "stock/pieges-candidats.json"), encoding="utf-8"))
    pages, vus = [], set()
    for c in CLASSIQUES + cands:
        try: p = preparer(c)
        except Exception as e: print("écarté (ligne illégale) :", c.get("ligne_san"), e); continue
        if not p: continue
        while p["slug"] in vus: p["slug"] += "-2"
        vus.add(p["slug"]); pages.append(p)
    for p in pages:
        d = os.path.join(site, "traps", p["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(p))
    open(os.path.join(site, "traps", "index.html"), "w", encoding="utf-8").write(index(pages))
    urls = ["/", "/en", "/try", "/traps"] + [f"/traps/{p['slug']}" for p in pages]
    open(os.path.join(site, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls) + "\n</urlset>\n")
    open(os.path.join(site, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: {SITE}/sitemap.xml\n")
    print(f"OK : {len(pages)} pages de pièges + traps/index.html + sitemap.xml + robots.txt")


if __name__ == "__main__":
    main(sys.argv[1])
