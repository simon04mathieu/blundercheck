"""Format BOUCLE (7-12 s, sans voix) : une position, un coup qui a l'air d'une gaffe (??), puis la révélation (!!).
Raccord fin/début (fondu vers l'image 1), musique rythmée avec coupure juste avant la révélation.
Usage : python3 boucle.py <nom> <sortie.mp4>
Vérifier chaque ligne avec Stockfish avant d'ajouter une boucle (voir verif_stockfish.py).
"""
import sys, subprocess, os, tempfile
import chess
import coach

VERT = (40, 170, 90)

BOUCLES = {
    # Piège de Lasker (contre-gambit Albin) : 1.d4 d5 2.c4 e5 3.dxe5 d4 4.e3 Bb4+ 5.Bd2 dxe3 6.Bxb4?? exf2+ 7.Ke2
    # Stockfish 19 : 7...fxg1=N+! -7,5 ; 7...fxg1=Q? 8.Qxd8+ égalise (-0,1) ; 8.Rxg1 Bg4+ 9.Kf2 Bxd1 -10.
    "lasker": {
        "fen": "rnbqk1nr/ppp2ppp/8/4P3/1BP5/8/PP2KpPP/RN1Q1BNR b kq - 1 7",
        "noirs": True,
        "duree": 10.0,
        "hook": ("Ici, tu fais un CAVALIER.|Pas une dame.", 2.2),
        "fx": {"brillant": "impact"},
        "coupures": [(4.4, 4.85)],
        "actions": [
            (0.0, "fleches", [("f2", "g1")]),
            (2.3, "coup", ("fxg1=N+", "gaffe")),
            (3.4, "coup", ("Rxg1", None)),
            (4.85, "coup", ("Bg4+", "brillant")),
            (4.85, "zoom", ("e2f3", 1.55, 2.1)),
            (5.25, "fleches", [("g4", "d1")]),
            (6.1, "coup", ("Kf2", None)),
            (6.8, "coup", ("Bxd1", None)),
            (7.05, "tampon", ("!!", VERT, 1.4, "La dame tombe.")),
            (8.45, "tampon", ("!!", VERT, 1.6, "Merci le cavalier.")),
        ],
    },
}

def fabriquer(nom, out_mp4):
    spec = dict(BOUCLES[nom]); spec.setdefault("captions", []); spec["boucle"] = True
    coach.FLIP = spec.get("noirs", False); coach.BG = coach.fond()
    d = tempfile.mkdtemp()
    v, a = os.path.join(d, "muet.mp4"), os.path.join(d, "son.wav")
    dur = coach.run(spec, v, a, 1.0)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", v, "-i", a, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", "-movflags", "+faststart", out_mp4], check=True)
    return dur

if __name__ == "__main__":
    print(sys.argv[1], "durée", round(fabriquer(sys.argv[1], sys.argv[2]), 2))
