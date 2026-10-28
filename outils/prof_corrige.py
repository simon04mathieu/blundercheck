#!/usr/bin/env python3
"""Format « Le prof corrige ma partie » (prof_corrige) : capture d'une vraie partie de Simon corrigée par le vrai site.

Commande : commandes/prof/<nom>.json  {"nom": "prof_1", "partie": 1, "moments": 3}
  partie  = 1 pour la partie la plus récente (parties standard d'au moins 30 demi-coups), 2 pour l'avant-dernière…
Pseudo Chess.com : variable d'environnement CHESSCOM_PSEUDO (secret GitHub posé par Simon). Il n'est JAMAIS écrit
dans le dépôt ni affiché : le PGN est réduit aux coups (aucun en-tête, aucun nom, aucune date, aucun lien).
Sorties : sorties/prof/<nom>/partie.pgn, moments.json, ecran_<demi-coup>.png (écrans réels de blundercheck.app/en,
navigateur passé par ?admin pour ne pas fausser les stats). Les commentaires sont ceux du vrai prof, recopiés tels quels.
Essai sans réseau Chess.com : PGN_FICHIER=<fichier.pgn> COULEUR=w|b ; autre site : SITE=http://localhost:8788
"""
import json, os, re, sys, time, urllib.request
from pathlib import Path

SITE = os.environ.get("SITE", "https://blundercheck.app").rstrip("/")
UA = {"User-Agent": "BlunderCheck-video/1.0 (+https://blundercheck.app)"}


def lire_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.load(r)


def partie_chesscom(pseudo, n):
    """n-ième partie standard récente (≥ 30 demi-coups) ; renvoie (pgn complet, couleur de Simon)."""
    arch = lire_json(f"https://api.chess.com/pub/player/{pseudo.lower()}/games/archives").get("archives", [])
    vues = 0
    for url in reversed(arch[-6:]):
        jeux = sorted(lire_json(url).get("games", []), key=lambda g: g.get("end_time", 0), reverse=True)
        for g in jeux:
            if g.get("rules") != "chess" or not g.get("pgn"):
                continue
            coups = nettoyer(g["pgn"])
            if len(re.findall(r"\d+\.(?!\.)", coups)) < 15:
                continue
            vues += 1
            if vues == n:
                blanc = (g.get("white", {}).get("username", "")).lower() == pseudo.lower()
                return g["pgn"], "w" if blanc else "b"
    raise SystemExit(f"ÉCHEC : partie n° {n} introuvable (parties standard d'au moins 30 demi-coups, 6 derniers mois)")


def nettoyer(pgn):
    """Garde seulement les coups : aucun en-tête (noms, Elo, date, lien), aucun commentaire ni temps à la pendule."""
    corps = "\n".join(l for l in pgn.splitlines() if not l.startswith("["))
    corps = re.sub(r"\{[^}]*\}", " ", corps)
    corps = re.sub(r"\$\d+", " ", corps)
    corps = re.sub(r"\d+\.\.\.", " ", corps)
    return re.sub(r"\s+", " ", corps).strip()


def main():
    cmd = json.load(open(sys.argv[1]))
    nom = re.sub(r"[^a-z0-9_-]", "", cmd["nom"].lower())
    n, nb_moments = int(cmd.get("partie", 1)), int(cmd.get("moments", 3))
    out = Path("sorties/prof") / nom
    out.mkdir(parents=True, exist_ok=True)

    if os.environ.get("PGN_FICHIER"):
        brut, couleur, pseudo = open(os.environ["PGN_FICHIER"]).read(), os.environ.get("COULEUR", "w"), ""
    else:
        pseudo = os.environ.get("CHESSCOM_PSEUDO", "").strip()
        if not pseudo:
            raise SystemExit("ÉCHEC : secret CHESSCOM_PSEUDO absent (à poser par Simon dans GitHub › Settings › Secrets › Actions)")
        try:
            brut, couleur = partie_chesscom(pseudo, n)
        except SystemExit:
            raise
        except Exception as e:   # message générique : jamais l'adresse (elle contient le pseudo)
            raise SystemExit(f"ÉCHEC : Chess.com ne répond pas ({type(e).__name__})")
    resultat = (re.search(r'\[Result "([^"]+)"\]', brut) or [None, "*"])[1]
    pgn = f'[Result "{resultat}"]\n\n{nettoyer(brut)}\n'
    if pseudo and pseudo.lower() in pgn.lower():
        raise SystemExit("ÉCHEC : le pseudo apparaît encore dans le PGN nettoyé, rien n'est écrit")
    (out / "partie.pgn").write_text(pgn)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav = p.chromium.launch()
        page = nav.new_page(viewport={"width": 430, "height": 932}, device_scale_factor=2.5, locale="en-US")
        if os.environ.get("CHESSJS_LOCAL"):   # essais hors GitHub seulement : bibliothèque servie depuis un fichier local
            page.route("**/chess.js@0.10.3/chess.js", lambda r: r.fulfill(path=os.environ["CHESSJS_LOCAL"], content_type="application/javascript"))
        page.goto(f"{SITE}/?admin", wait_until="load")          # ce navigateur est rangé sous « moi » (stats non faussées)
        page.goto(f"{SITE}/en", wait_until="load")
        page.wait_for_function("() => typeof window.ajouterPartie === 'function' && typeof window.analyserPartie === 'function'", timeout=60000)
        page.wait_for_timeout(1500)
        gid = page.evaluate("([pgn, c]) => { const g = ajouterPartie(pgn, c, 'import'); return g && g.id; }", [pgn, couleur])
        if not gid:
            raise SystemExit("ÉCHEC : le site n'a pas pu importer la partie")
        page.evaluate("id => ouvrirAnalyse(id, 0)", gid)
        # Stockfish dans le navigateur : on attend la fin de l'analyse (affinage compris)
        page.evaluate("id => analyserPartie(LIB.find(g => g.id === id))", gid)
        page.wait_for_function("id => { const g = LIB.find(x => x.id === id); return g && estAffinee(g); }", arg=gid, timeout=20 * 60000, polling=2000)
        # Le vrai prof (même appel que le bouton du site)
        prof = page.evaluate("""async id => {
            const g = LIB.find(x => x.id === id);
            for (let k = 0; k < 30 && !IA.fn; k++) await new Promise(r => setTimeout(r, 500));
            if (!IA.fn) return { erreur: 'prof indisponible' };
            try { await commenterPartie(g, { silencieux: true }); } catch (e) { return { erreur: String(e && e.message || e) }; }
            return { erreur: (g.prof && g.prof.erreur) || '', n: g.prof ? Object.keys(g.prof.comments || {}).length : 0 };
        }""", gid)
        infos = page.evaluate("""id => {
            const g = LIB.find(x => x.id === id), D = deriver(g), pr = g.prof || { comments: {} };
            return { color: g.color, resume: pr.resume || '', lecons: pr.lecons || [],
              coups: D.P.moves.map((m, i) => ({ ply: i + 1, san: m.san, camp: m.color, tag: D.tags[i] || '', delta: +(D.deltas[i] || 0).toFixed(3),
                commentaire: (pr.comments[i + 1] || {}).c || '', conseil: (pr.comments[i + 1] || {}).k || '' })) };
        }""", gid)

        # Choix des moments : les plus grosses fautes (des deux camps), puis le meilleur coup de Simon qui suit une faute adverse
        coups = infos["coups"]
        fautes = sorted([c for c in coups if c["tag"] in ("gaffe", "erreur")], key=lambda c: -c["delta"])
        choisis = fautes[: max(1, nb_moments - 1)]
        punis = [c for c in coups if c["camp"] == infos["color"] and c["tag"] in ("meilleur", "excellent")
                 and any(f["ply"] == c["ply"] - 1 for f in fautes)]
        if punis:
            choisis.append(punis[0])
        for c in coups:
            if len(choisis) >= nb_moments:
                break
            if c not in choisis and c["commentaire"]:
                choisis.append(c)
        choisis = sorted({c["ply"]: c for c in choisis}.values(), key=lambda c: c["ply"])[:nb_moments]

        for c in choisis:
            page.evaluate("([id, ply]) => ouvrirAnalyse(id, ply)", [gid, c["ply"]])
            page.wait_for_timeout(1200)
            texte = page.inner_text("body").lower()
            if pseudo and pseudo.lower() in texte:
                raise SystemExit("ÉCHEC : le pseudo apparaît à l'écran, capture annulée")
            fichier = f"ecran_{c['ply']:03d}.png"
            page.screenshot(path=str(out / fichier))
            c["ecran"] = fichier
        page.evaluate("id => ouvrirAnalyse(id, 0)", gid)
        page.wait_for_timeout(800)
        page.screenshot(path=str(out / "ecran_000.png"))
        nav.close()

    moments = {"nom": nom, "partie": n, "couleur_de_simon": infos["color"], "demi_coups": len(coups),
               "prof": prof, "resume_du_prof": infos["resume"], "lecons_du_prof": infos["lecons"],
               "moments": choisis, "ecran_depart": "ecran_000.png",
               "regle": "Commentaires du vrai prof, à montrer tels quels (on peut couper, jamais réécrire). Partie anonyme : aucun nom à l'écran ni dans la voix."}
    (out / "moments.json").write_text(json.dumps(moments, ensure_ascii=False, indent=1))
    etat = "OK" if not prof.get("erreur") else "OK sans prof (" + prof["erreur"][:80] + ")"
    print(f"{etat} : {nom}, {len(coups)} demi-coups, {len(choisis)} moments, {prof.get('n', 0)} commentaires du prof")


if __name__ == "__main__":
    main()
