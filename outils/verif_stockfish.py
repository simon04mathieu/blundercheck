"""Vérification Stockfish d'une ligne de piège avant fabrication.
Usage : python3 verif_stockfish.py <moteur> "<coups depuis le départ ou fen:...>" [secondes par position]
<moteur> : chemin d'un binaire UCI. Sans binaire natif, Stockfish 19 WASM marche via npm :
  npm i stockfish  puis un script  « exec node node_modules/stockfish/bin/stockfish-19-single.js »
Affiche, pour chaque coup de la ligne, l'évaluation du coup joué et des 3 meilleurs coups (point de vue des Blancs, centipions).
"""
import sys
import chess, chess.engine

def verifier(moteur, ligne, secs=3.0):
    eng = chess.engine.SimpleEngine.popen_uci(moteur)
    toks = ligne.split()
    b = chess.Board(toks[0][4:].replace("_", " ")) if toks and toks[0].startswith("fen:") else chess.Board()
    if toks and toks[0].startswith("fen:"): toks = toks[1:]
    rapport = []
    for san in toks:
        mv = b.parse_san(san)
        top = eng.analyse(b, chess.engine.Limit(time=secs), multipv=3)
        joue = eng.analyse(b, chess.engine.Limit(time=secs), root_moves=[mv])
        f = lambda s: s.white().score(mate_score=100000)
        meilleurs = [(b.san(x["pv"][0]), f(x["score"])) for x in top]
        rapport.append((b.fullmove_number, san, f(joue["score"]), meilleurs))
        print(f"{b.fullmove_number:>3} {san:<8} joué {f(joue['score']):>7}   meilleurs {meilleurs}", flush=True)
        b.push(mv)
    eng.quit()
    return rapport

if __name__ == "__main__":
    verifier(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 3.0)
