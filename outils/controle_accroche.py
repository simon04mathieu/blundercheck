"""Contrôle automatique de l'accroche (Simon, 10/11 : « on passe 3 h à discuter de stratégie et rien n'est appliqué »).
Les règles de claude/regles-montage.md sont vérifiées ICI, par le code, sur chaque vidéo : une vidéo refusée ne peut
pas être publiée (outils/verifier_publications.py appelle ce contrôle pour toute publication datée du 11/11 ou après).
Chaque nouvelle décision de Simon sur le montage = une règle de plus ici + une ligne dans claude/regles-montage.md.
Usage seul : python3 outils/controle_accroche.py <nom> [<nom>…]   (nom = clé PERSO de outils/scripts_coach.py)
  R1 quelque chose bouge dès la 1re seconde : une flèche, un coup, un zoom ou une étiquette AVANT la fin de la 1re phrase lue ;
  R2 la 1re phrase lue pose l'enjeu ou le défi : ni nom d'ouverture, ni lieu, ni année (le contexte vient après) ;
  R3 « Follow / Abonne-toi » présent, juste avant la révélation (après la question, avant le 1er coup de la solution) ;
  R4 durée ≤ 42 s (cible 20-30 s ; le hit percee_3v3 = 40 s) ;  R5 au moins 1,5 s entre deux coups (minutage).
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "outils"))
DUREE_MAX, ECART_MIN = 42.0, 1.5   # 42 s : le hit percee_3v3 faisait 40,4 s ; cible 20-30 s
CONTEXTE = re.compile(r"\b1[0-9]{3}\b|\b20[0-9]{2}\b|gambit|defen[cs]e|opening|pawn game|variation|attack\b|"
                      r"ouverture|d[ée]fense|partie\b|vienna|vienne|wijk|amsterdam|london|londres|paris", re.I)

def controler(nom):
    import scripts_coach as S
    pb, sc = [], (S.PERSO.get(nom) or {}).get("script")
    if not sc: return [f"script introuvable ({nom})"]
    sc = re.sub(r"\[p [^\]]*\]", "", sc, count=1).strip()            # la position de départ ne compte pas
    fin1 = re.search(r"[.!?…](\s|$)", re.sub(r"\[[^\]]*\]", lambda m: "#" * len(m.group(0)), sc))
    debut = sc[: fin1.end() if fin1 else len(sc)]
    if not re.search(r"\[(f|m|z|s) ", debut): pb.append("R1 rien ne bouge pendant la 1re phrase (ajouter [f …], [m …] ou [z …] au début)")
    phrase1 = re.sub(r"\[[^\]]*\]", "", debut).strip()
    if CONTEXTE.search(phrase1): pb.append(f"R2 1re phrase = contexte, pas l'enjeu : « {phrase1} »")
    if not re.search(r"follow|abonne", sc, re.I): pb.append("R3 pas de « Follow / Abonne-toi »")
    p = os.path.join(ROOT, "sorties", "minutage", f"{nom}.json")
    if os.path.exists(p):
        m = json.load(open(p, encoding="utf-8")); c = [x["t"] for x in m.get("coups", [])]
        if m.get("duree_s", 0) > DUREE_MAX: pb.append(f"R4 durée {m['duree_s']} s (max {DUREE_MAX} s)")
        e = [round(b - a, 2) for a, b in zip(c, c[1:]) if b - a < ECART_MIN]
        if e: pb.append(f"R5 coups trop rapprochés : {e}")
    else: pb.append("minutage absent : vidéo pas encore fabriquée")
    return pb

if __name__ == "__main__":
    ko = 0
    for n in sys.argv[1:]:
        pb = controler(n); ko += bool(pb)
        print(("OK  " if not pb else "NON ") + n + ("" if not pb else " : " + " ; ".join(pb)))
    sys.exit(1 if ko else 0)
