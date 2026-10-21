"""Format « Ta pire gaffe » (démo du 22/10, sans voix) : une vraie gaffe tirée d'une vraie partie Lichess,
puis la punition. Source : le puzzle du jour Lichess (partie réelle, gaffe et solution déjà vérifiées par Lichess),
recontrôlé avec Stockfish si le binaire est présent.
Plus tard : même chose à partir d'une partie envoyée en commentaire (lien Lichess / Chess.com).
"""
import json, urllib.request, shutil
import chess, chess.pgn, io

def puzzle_du_jour():
    r = urllib.request.Request("https://lichess.org/api/puzzle/daily", headers={"Accept": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=30))

def controle_stockfish(avant, gaffe, punition, secs=2.0):
    """Écart d'évaluation (centipions, point de vue du camp qui gaffe) entre le meilleur coup et la gaffe."""
    exe = shutil.which("stockfish") or "/usr/games/stockfish"
    try:
        import chess.engine
        eng = chess.engine.SimpleEngine.popen_uci(exe)
    except Exception as e:
        return {"stockfish": f"absent ({e})"}
    cote = avant.turn
    best = eng.analyse(avant, chess.engine.Limit(time=secs))
    joue = eng.analyse(avant, chess.engine.Limit(time=secs), root_moves=[gaffe])
    eng.quit()
    f = lambda s: s.pov(cote).score(mate_score=10000)
    return {"meilleur": avant.san(best["pv"][0]), "eval_meilleur": f(best["score"]), "eval_gaffe": f(joue["score"]),
            "perte": f(best["score"]) - f(joue["score"])}

FR = str.maketrans({"N": "C", "B": "F", "R": "T", "Q": "D", "K": "R"})
def fr(san): return san.translate(FR)  # notation française pour l'affichage

def spec_depuis_puzzle(pz):
    g = chess.pgn.read_game(io.StringIO(pz["game"]["pgn"]))
    b = g.board(); coups = list(g.mainline_moves())
    for mv in coups[:-1]: b.push(mv)
    avant = b.copy(); gaffe = coups[-1]
    san_gaffe = avant.san(gaffe); n = avant.fullmove_number
    joueur = "Blancs" if avant.turn == chess.WHITE else "Noirs"
    puni = "Noirs" if joueur == "Blancs" else "Blancs"
    b.push(gaffe)
    sol = []; bb = b.copy()
    for u in pz["puzzle"]["solution"][:3]:
        mv = chess.Move.from_uci(u); sol.append(bb.san(mv)); bb.push(mv)
    teaser_fin = " ".join(m.uci() for m in coups)  # positions données en coups depuis le départ
    fen_avant = avant.fen().replace(" ", "_")
    actions = [
        (2.4, "position", [f"fen:{fen_avant}"]),
        (3.4, "coup", (san_gaffe, "gaffe")),
    ]
    caps = [(2.5, 4.6, f"Coup {n} : les {joueur} jouent {fr(san_gaffe)}…")]
    t = 5.0
    actions.append((t, "quiz", (3, f"Trouve la punition des {puni}")))
    t += 3.2
    for i, s in enumerate(sol):
        actions.append((t, "coup", (s, "brillant" if i == 0 else None))); t += 1.3
    caps.append((8.2, t, f"{' '.join(fr(s) for s in sol)} : ça gagne !"))
    duree = t + 3.6
    pos_fin = bb
    return {
        "duree": duree, "captions": caps, "actions": actions, "noirs": puni == "Noirs",
        "hook": ("Ce coup a perdu la partie.|Tu vois pourquoi ?", 2.4),
        "teaser_board": b.copy(),  # image 1 : juste après la gaffe
        "question": "Envoie ta partie en commentaire.|On trouve ta pire gaffe.",
        "musique": 0.0,
    }, {"partie": pz["game"]["id"], "coup": f"{n}. {san_gaffe}", "camp": joueur, "solution": sol,
        "classement": pz["puzzle"].get("rating"), "controle": controle_stockfish(avant, gaffe, sol)}
