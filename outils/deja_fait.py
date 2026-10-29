#!/usr/bin/env python3
"""Base anti-doublon (demande de Simon, 29/10) : tout ce qu'on a déjà fait, en FR et en EN, pour ne jamais refaire la même vidéo.

    python3 outils/deja_fait.py                      # régénère stock/deja-fait.json et stock/deja-fait.md
    python3 outils/deja_fait.py --verifier "e4 e5 Nf3 d6 Bc4 Bg4 Nc3 g6 Nxe5 Bxd1 Bxf7+ Ke7 Nd5#"
    python3 outils/deja_fait.py --verifier "fen:5k2/6pp/8/5b2/8/3pK3/6PP/5R2_w_-_-_0_1"

Sources : scripts (outils/scripts_coach.py : PERSO et SCRIPTS) + fichiers de publication (publications/<réseau>/, faites/, reserve/).
Clé de doublon = la position finale de la ligne jouée dans la vidéo (placement des pièces + trait), donc un même piège
est reconnu même si le nom, la langue ou le texte changent. --verifier dit si une ligne passe par une position déjà
montrée (position finale ou position de départ d'un quiz), dans quelle langue et sur quels réseaux.
Lecture seule : ne publie rien, ne touche à aucun outil ni workflow.
"""
import glob, json, os, re, sys
import chess

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
from scripts_coach import PERSO, SCRIPTS
import coach2

RESEAUX = ["youtube", "tiktok", "tiktok-en", "instagram", "facebook", "threads"]


def cle(b):
    return " ".join(b.fen().split()[:2])


def parcours(nom):
    """Positions traversées par la vidéo (ordre du script) ; [] si le script ne se rejoue pas."""
    script = PERSO[nom]["script"] if nom in PERSO else SCRIPTS[nom][1]
    toks = coach2.tokens(script)
    marks = [m for t in toks for m in t["marks"]] + [m for t in toks for m in t.get("marks_after", [])]
    b, vues, depart = None, [], None
    try:
        for mk in marks:
            if mk[0] == "p":
                r = mk[1:]
                if r and r[0].startswith("fen:"):
                    b = chess.Board(r[0][4:].replace("_", " ")); r = r[1:]
                else:
                    b = chess.Board()
                for s in r: b.push_san(s)
                if depart is None: depart = cle(b)
                vues.append(cle(b))
            elif mk[0] == "m" and b is not None:
                b.push_san(mk[1]); vues.append(cle(b))
    except Exception:
        pass
    if b is None:
        return None, None, [], ""
    # ligne principale = la plus longue suite de coups depuis le départ (pour l'affichage)
    ligne = " ".join(m.uci() for m in b.move_stack)
    return depart, cle(b), vues, ligne


def langue_nom(nom):
    if "_en" in nom or nom.endswith("_en"): return "en"
    return "fr"


def publications():
    pubs = {}
    for res in RESEAUX:
        for f in glob.glob(f"{ROOT}/publications/{res}/*.json") + glob.glob(f"{ROOT}/publications/{res}/faites/*.json") \
                + glob.glob(f"{ROOT}/publications/{res}/reserve/*.json"):
            try: d = json.load(open(f, encoding="utf-8"))
            except Exception: continue
            nom = os.path.basename(f)[:-5]
            statut = "publié" if "/faites/" in f else ("réserve" if "/reserve/" in f else "programmé")
            quand = (d.get("heure_conseillee") or d.get("envoyer_apres") or "")[:10]
            p = pubs.setdefault(nom, {"reseaux": {}, "langue": d.get("langue"), "concept": d.get("concept"),
                                      "titre": d.get("titre"), "legende": None, "test": d.get("test"), "variante": d.get("variante")})
            p["reseaux"][res] = f"{statut} {quand}".strip()
            if d.get("titre") and not p["titre"]: p["titre"] = d["titre"]
            if d.get("legende") and not p["legende"]: p["legende"] = d["legende"]
            if d.get("langue") and not p["langue"]: p["langue"] = d["langue"]
    return pubs


def construire():
    pubs = publications()
    base = []
    for nom in sorted(set(PERSO) | set(SCRIPTS) | set(pubs)):
        p = pubs.get(nom, {})
        depart, fin, vues, ligne = parcours(nom) if (nom in PERSO or nom in SCRIPTS) else (None, None, [], "")
        hook = PERSO.get(nom, {}).get("hook") if nom in PERSO else None
        sujet = p.get("titre") or (p.get("legende") or "").split("\n")[0] or (hook or "").replace("|", " ")
        sujet = re.sub(r"\s*#\w+", "", sujet).strip()[:110]
        langue = p.get("langue") or langue_nom(nom)
        base.append({"nom": nom, "langue": langue, "concept": p.get("concept") or re.sub(r"_\d+.*$", "", nom),
                     "sujet": sujet, "reseaux": p.get("reseaux", {}),
                     "statut": "publié" if any(v.startswith("publié") for v in p.get("reseaux", {}).values())
                               else "programmé" if any(v.startswith("programmé") for v in p.get("reseaux", {}).values())
                               else "réserve" if p.get("reseaux") else "script seulement (publication avant le 22/10 ou jamais)",
                     "test": p.get("test"), "variante": p.get("variante"),
                     "position_depart": depart, "position_finale": fin, "positions": sorted(set(vues)), "ligne_uci": ligne})
    return base


def ecrire(base):
    os.makedirs(f"{ROOT}/stock", exist_ok=True)
    json.dump(base, open(f"{ROOT}/stock/deja-fait.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # regroupement par position finale : un même piège = une ligne, avec FR et EN
    groupes = {}
    for v in base:
        groupes.setdefault(v["position_finale"] or ("sans_position:" + v["nom"]), []).append(v)
    L = ["# Déjà fait (FR / EN) : base anti-doublon", "",
         "*Généré par `python3 outils/deja_fait.py` (branche `videos`). Une ligne = une même position finale (même piège ou même quiz),",
         "quels que soient le nom, la langue ou le texte. Avant d'écrire une fiche : chercher ici, ou lancer `--verifier \"<coups>\"`.*", "",
         "| Sujet | FR | EN | Concept | Statut | Position finale |", "|---|---|---|---|---|---|"]
    def resume(vs):
        if not vs: return "—"
        out = []
        for v in vs:
            r = ", ".join(f"{k} {d.split()[-1] if len(d.split()) > 1 else ''}".strip() for k, d in sorted(v["reseaux"].items()))
            out.append(f"`{v['nom']}`" + (f" ({r})" if r else ""))
        return " ; ".join(out)
    lignes = []
    for k, vs in groupes.items():
        fr = [v for v in vs if v["langue"] == "fr"]; en = [v for v in vs if v["langue"] == "en"]
        sujet = next((v["sujet"] for v in en + fr if v["sujet"]), vs[0]["nom"])
        statut = "publié" if any(v["statut"] == "publié" for v in vs) else vs[0]["statut"]
        pos = "" if k.startswith("sans_position:") else f"`{k}`"
        lignes.append((min(v["nom"] for v in vs), f"| {sujet.replace('|', '/')} | {resume(fr)} | {resume(en)} | {vs[0]['concept']} | {statut} | {pos} |"))
    L += [l for _, l in sorted(lignes)]
    n_fr = sum(1 for v in base if v["langue"] == "fr"); n_en = len(base) - n_fr
    L += ["", f"Total : {len(base)} vidéos ({n_fr} FR, {n_en} EN), {len(groupes)} sujets distincts.",
          "« script seulement » = fabriqué dans le dépôt mais sans fichier de publication (publié avant le 22/10 par Metricool ou jamais) : à considérer comme déjà fait."]
    open(f"{ROOT}/stock/deja-fait.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    return len(base), len(groupes)


def verifier(texte, base):
    toks = texte.split()
    b = chess.Board(toks[0][4:].replace("_", " ")) if toks and toks[0].startswith("fen:") else chess.Board()
    if toks and toks[0].startswith("fen:"): toks = toks[1:]
    vues = [cle(b)]
    for s in toks: b.push_san(s); vues.append(cle(b))
    touches = []
    for v in base:
        connues = {v["position_finale"], v["position_depart"]} - {None}
        commun = [p for p in vues[1:] if p in connues] or ([vues[0]] if vues[0] in connues and not toks else [])
        if v["position_finale"] and v["position_finale"] == vues[-1]: commun = [vues[-1]]
        if commun:
            touches.append(v)
    if not touches:
        print("NOUVEAU : aucune vidéo déjà faite ne passe par cette position finale."); return 0
    print("DÉJÀ FAIT :")
    for v in touches:
        print(f"  {v['nom']} ({v['langue']}, {v['statut']}) {v['sujet']} · {', '.join(f'{k} {d}' for k, d in v['reseaux'].items())}")
    langues = {v["langue"] for v in touches}
    if langues == {"fr"}: print("→ fait en FR seulement : un jumeau EN reste possible.")
    elif langues == {"en"}: print("→ fait en EN seulement : un jumeau FR reste possible.")
    else: print("→ fait en FR ET en EN : ne pas refaire.")
    return 1


if __name__ == "__main__":
    base = construire()
    if len(sys.argv) > 2 and sys.argv[1] == "--verifier":
        sys.exit(verifier(sys.argv[2], base))
    n, g = ecrire(base)
    print(f"OK stock/deja-fait.json et stock/deja-fait.md : {n} vidéos, {g} sujets distincts")
