#!/usr/bin/env python3
"""Réserve de pièges inédits (demande de Simon, 29/10) : les pièges d'ouverture où des joueurs réels tombent le plus souvent.

Source : base publique des puzzles Lichess (database.lichess.org, licence CC0). Chaque puzzle vient d'une vraie partie
où un joueur a gaffé ; quand le MÊME position de gaffe revient dans beaucoup de puzzles, c'est un piège récurrent.
Filtres : thème « opening » + mat en 2 à 4 coups, puzzle classé 1300-2000 (Simon, 30/10), gaffe avant le 31e demi-coup.
La ligne depuis le départ est reprise de la vraie partie (export public Lichess, sans nom de joueur), puis vérifiée :
python-chess (légalité, mat) + Stockfish (la gaffe perd vraiment, le coup juste existait), anti-doublon (outils/deja_fait.py).

    python3 outils/chercher_pieges.py [--max 20]       # dans GitHub Actions (réseau Lichess) : écrit stock/pieges-candidats.{json,md}
Lancement : pousser commandes/pieges/<nom>.json ({"max": 20}) sur la branche videos (workflow « Chercher des pièges »).
Lecture seule côté comptes : ne publie rien. L'anti-doublon compare des positions : un même piège joué dans un autre ordre
(ex. Caro-Kann Nd6#) n'est pas reconnu, le Scénariste vérifie aussi le nom de l'ouverture dans deja-fait.
"""
import collections, csv, io, json, os, re, shutil, sys, time, urllib.request
import chess, chess.engine, chess.pgn

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
URL = "https://database.lichess.org/lichess_db_puzzle.csv.zst"
UA = {"User-Agent": "BlunderCheck-pieges/1.0 (+https://blundercheck.app)"}
MATS = {"mateIn2": 2, "mateIn3": 3, "mateIn4": 4}  # 30/10 (Simon) : plus de mat en 1, combinaisons jusqu'à 4 coups
# 31/10 (Simon : « fais des pièges variés, c'est souvent sacrifice de dame avec mat cavalier + fou, sois innovant ») :
# on garde aussi les pièges qui GAGNENT une pièce (fourchette, clouage, enfilade, pièce piégée…), et on impose la variété
# (au plus 1 piège par « signature » motif + pièce qui mate, au plus 3 sacrifices de dame par réserve).
MOTIFS = ["smotheredMate", "backRankMate", "anastasiaMate", "arabianMate", "bodenMate", "doubleBishopMate", "dovetailMate",
          "hookMate", "killBoxMate", "vukovicMate", "underPromotion", "enPassant", "castling", "doubleCheck", "discoveredAttack",
          "trappedPiece", "skewer", "xRayAttack", "interference", "clearance", "deflection", "attraction", "quietMove",
          "fork", "pin", "capturingDefender", "hangingPiece", "sacrifice"]
GAIN = {"fork", "pin", "skewer", "trappedPiece", "discoveredAttack", "doubleCheck", "xRayAttack", "underPromotion", "deflection", "attraction"}
NOMS_PIECES = {1: "pion", 2: "cavalier", 3: "fou", 4: "tour", 5: "dame", 6: "roi"}


def lignes_puzzles():
    import zstandard
    req = urllib.request.Request(URL, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        flux = zstandard.ZstdDecompressor().stream_reader(r)
        yield from csv.DictReader(io.TextIOWrapper(flux, encoding="utf-8"))


def regrouper(lignes, rmin=1300, rmax=2000, ply_max=30):  # 30/10 (Simon) : niveau 1300-2000
    groupes = collections.defaultdict(list)
    for p in lignes:
        th = p["Themes"].split()
        if "opening" not in th: continue
        mat = next((MATS[t] for t in th if t in MATS), None)
        nb = len(p["Moves"].split())
        gain = (not mat and "crushing" in th and GAIN & set(th) and 4 <= nb <= 8)   # 2 à 4 coups du héros
        if not mat and not gain: continue
        r = int(p["Rating"])
        if not rmin <= r <= rmax: continue
        m = re.search(r"#(\d+)$", p["GameUrl"])
        if not m or int(m.group(1)) > ply_max: continue
        cle = " ".join(p["FEN"].split()[:2])   # placement + trait : mêmes pièges même si droits de roque différents
        groupes[cle].append({"id": p["PuzzleId"], "fen": p["FEN"], "coups": p["Moves"].split(), "note": r, "mat": mat,
                             "pop": int(p["Popularity"]), "jeux": int(p["NbPlays"]), "url": p["GameUrl"],
                             "ouverture": p.get("OpeningTags", ""), "themes": th,
                             "type": "mat" if mat else "gain"})
    return groupes


def ligne_depuis_partie(url, fen):
    """Coups SAN de la vraie partie jusqu'à la position du puzzle (aucun nom n'est lu ni gardé)."""
    gid = url.split("lichess.org/")[1].split("/")[0].split("#")[0][:8]
    req = urllib.request.Request(f"https://lichess.org/game/export/{gid}?moves=true&tags=false&clocks=false&evals=false&opening=false",
                                 headers=dict(UA, Accept="application/x-chess-pgn"))
    with urllib.request.urlopen(req, timeout=30) as r:
        pgn = r.read().decode()
    jeu = chess.pgn.read_game(io.StringIO(pgn))
    b = jeu.board(); sans = []; cible = " ".join(fen.split()[:4])
    for mv in jeu.mainline_moves():
        if " ".join(b.fen().split()[:4]) == cible: return sans
        sans.append(b.san(mv)); b.push(mv)
        if len(sans) > 40: break
    return sans if " ".join(b.fen().split()[:4]) == cible else None


def signature(ligne, n_depart, themes, mat):
    """Motif principal (thème Lichess), pièce qui donne le mat (ou « gain »), et sacrifice de dame du héros."""
    b = chess.Board()
    for x in ligne[:n_depart]: b.push_san(x)
    heros = not b.turn            # le pigeon joue la gaffe, le héros a le trait juste avant lui
    dame_sac = False; piece = None
    for x in ligne[n_depart:]:
        mv = b.parse_san(x); cible = b.piece_at(mv.to_square)
        if cible and cible.piece_type == chess.QUEEN and cible.color == heros: dame_sac = True
        piece = b.piece_at(mv.from_square).piece_type; b.push(mv)
    motif = next((t for t in MOTIFS if t in themes), "autre")
    return motif, (NOMS_PIECES[piece] if mat else "gain"), dame_sac


def verifier(moteur, depart, gaffe_uci, suite_uci):
    """Rejoue la ligne, contrôle la gaffe et le mat ; renvoie (ligne SAN complète, éval avant, meilleur coup, mat ok)."""
    b = chess.Board()
    for s in depart: b.push_san(s)
    avant = moteur.analyse(b, chess.engine.Limit(time=1.0))
    meilleur = b.san(avant["pv"][0]); ev = avant["score"].pov(b.turn).score(mate_score=10000)
    ligne = list(depart)
    gaffe = chess.Move.from_uci(gaffe_uci); ligne.append(b.san(gaffe)); b.push(gaffe)
    for u in suite_uci:
        mv = chess.Move.from_uci(u); ligne.append(b.san(mv)); b.push(mv)
    fin = moteur.analyse(b, chess.engine.Limit(time=1.0))["score"].pov(not b.turn if len(suite_uci) % 2 else b.turn)
    gain_cp = fin.score(mate_score=10000)   # vu du héros (dernier coup de la suite = coup du héros)
    return ligne, ev, meilleur, b.is_checkmate(), gain_cp


def principal(nmax=20):
    import deja_fait
    t0 = time.time(); groupes = regrouper(lignes_puzzles())
    print(f"puzzles regroupés : {sum(len(v) for v in groupes.values())} dans {len(groupes)} positions ({time.time() - t0:.0f} s)", flush=True)
    base = deja_fait.construire()
    connues = {}
    for v in base:
        for p in [v["position_finale"], v["position_depart"]] + v.get("positions", []):
            if p: connues.setdefault(p, set()).add(v["langue"])
    sf = shutil.which("stockfish") or "/usr/games/stockfish"
    moteur = chess.engine.SimpleEngine.popen_uci(sf)
    tri = sorted(groupes.items(), key=lambda kv: (-len(kv[1]), min(int(re.search(r"#(\d+)$", p["url"]).group(1)) for p in kv[1])))
    sortie = []; vues_sig = collections.Counter(); n_dame = 0
    essais, t_debut = 0, time.time()
    for cle, ps in tri:
        if len(sortie) >= nmax: break
        essais += 1
        if essais > 220 or time.time() - t_debut > 18 * 60:   # budget : 220 parties lues ou 18 min, on garde ce qui est trouvé
            print("budget atteint :", essais - 1, "positions essayées", flush=True); break
        if len(ps) < 2: break                                    # un piège = au moins 2 parties réelles
        ex = max(ps, key=lambda p: (p["pop"], p["jeux"]))
        try:
            depart = ligne_depuis_partie(ex["url"], ex["fen"]); time.sleep(1.2)
        except Exception as e:
            print("export Lichess refusé :", type(e).__name__, flush=True); time.sleep(3); continue
        if depart is None: continue
        try:
            ligne, ev, meilleur, mat, gain_cp = verifier(moteur, depart, ex["coups"][0], ex["coups"][1:])
        except Exception as e:
            print("ligne illégale écartée :", type(e).__name__, flush=True); continue
        if ex["type"] == "mat" and not mat: continue
        if ex["type"] == "gain" and (gain_cp is None or gain_cp < 300): continue   # gain réel : ≥ +3 pions pour le héros
        if ligne[len(depart)] == meilleur: continue   # la « gaffe » doit être une vraie faute
        motif, piece, dame_sac = signature(ligne, len(depart), ex["themes"], mat)
        if vues_sig[(motif, piece)] >= 1 or (dame_sac and n_dame >= 3): continue   # variété (Simon, 31/10)
        vues_sig[(motif, piece)] += 1; n_dame += dame_sac
        fin = chess.Board(); [fin.push_san(s) for s in ligne]
        bb = chess.Board()
        for s in ligne[: len(depart) + 1]: bb.push_san(s)
        cles_ligne = {" ".join(bb.fen().split()[:2]), " ".join(fin.fen().split()[:2])}   # après la gaffe + mat final (pas l'ouverture commune)
        langues = set().union(*[connues[k] for k in cles_ligne if k in connues]) if any(k in connues for k in cles_ligne) else set()
        sortie.append({"ouverture": (ex["ouverture"].split() or [""])[-1].replace("_", " "), "parties_reelles": len(ps),
                       "note_moyenne": round(sum(p["note"] for p in ps) / len(ps)), "mat_en": ex["mat"],
                       "demi_coup_gaffe": len(depart) + 1, "ligne_san": " ".join(ligne),
                       "gaffe": ligne[len(depart)], "coup_juste": meilleur, "eval_avant_cp": ev,
                       "camp_du_heros": "noirs" if len(depart) % 2 == 0 else "blancs",
                       "type": ex["type"], "motif": motif, "piece_finale": piece, "sacrifice_dame": dame_sac, "gain_cp": gain_cp,
                       "fen_mat": fin.fen(), "deja_fait": sorted(langues) or "non", "puzzle": ex["id"]})
        print(f"OK {len(ps):>4} parties · {ex['ouverture'][:40]} · {' '.join(ligne)}", flush=True)
    moteur.quit()
    os.makedirs(os.path.join(ROOT, "stock"), exist_ok=True)
    json.dump(sortie, open(os.path.join(ROOT, "stock/pieges-candidats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = ["# Pièges candidats (réserve du Scénariste)", "",
         f"*Généré le {time.strftime('%d/%m/%Y')} par `outils/chercher_pieges.py` (puzzles Lichess, CC0) : pièges d'ouverture à mat où de vrais joueurs",
         "tombent souvent (puzzle classé 1300-2000, mat en 2 à 4 **ou gain d'une pièce** en 2 à 4 coups). Ligne vérifiée python-chess + Stockfish 1 s. « Déjà fait » = d'après `marketing/deja-fait.md`.",
         "**Variété (Simon, 31/10)** : au plus 1 piège par motif + pièce finale, au plus 3 sacrifices de dame ; le Scénariste ne répète pas le motif ni la pièce qui mate de la veille.",
         "Le Scénariste prend d'abord les « non » ; « fr » seul = jumeau EN possible, et inversement.*", "",
         "| # | Ouverture | Parties réelles | Note moy. | Type | Motif | Pièce finale | Sac. dame | Héros | Gaffe (coup juste) | Ligne | Déjà fait |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(sortie, 1):
        df = "non" if c["deja_fait"] == "non" else "/".join(c["deja_fait"])
        L.append(f"| {i} | {c['ouverture'] or '?'} | {c['parties_reelles']} | {c['note_moyenne']} | {'mat en ' + str(c['mat_en']) if c['type'] == 'mat' else 'gain'} | "
                 f"{c['motif']} | {c['piece_finale']} | {'oui' if c['sacrifice_dame'] else 'non'} | {c['camp_du_heros']} | "
                 f"{c['gaffe']}?? ({c['coup_juste']}) | `{c['ligne_san']}` | {df} |")
    open(os.path.join(ROOT, "stock/pieges-candidats.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"OK stock/pieges-candidats.md : {len(sortie)} pièges, dont {sum(1 for c in sortie if c['deja_fait'] == 'non')} jamais faits")


if __name__ == "__main__":
    n = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 20
    principal(n)
