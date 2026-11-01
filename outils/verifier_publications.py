#!/usr/bin/env python3
"""Vérifie chaque fichier de publication AVANT le push (demande de Simon, 1/11 : `quiz_legal_9_fr` n'est jamais sorti
sur Instagram FR, champ `etiquettes` manquant). À lancer par le Producteur juste avant chaque `git push` de `publications/` :

    python3 outils/verifier_publications.py        # vérifie publications/<réseau>/*.json (pas faites/ ni reserve/)

Sortie 0 = tout est bon ; sortie 1 = au moins un fichier refusé (liste affichée) : corriger, puis relancer. Ne publie rien.
"""
import datetime as dt, glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = ("fichier", "envoyer_apres")
REQUIS = {
    "youtube": BASE + ("titre",),
    "tiktok": BASE + ("legende",),
    "tiktok-en": BASE + ("legende",),
    "instagram": BASE + ("legende", "concept", "etiquettes"),
    "instagram-en": BASE + ("legende", "concept", "etiquettes"),
    "facebook": BASE + ("legende", "concept", "etiquettes"),
    "threads": BASE + ("legende", "concept", "etiquettes"),
}
# Créneaux de la règle fixe 5 (heure de Paris). TikTok : l'heure d'envoi est celle du brouillon, pas de la publication.
CRENEAUX = {"instagram": {14, 20}, "youtube": {11, 14, 17, 20}, "instagram-en": {11, 14, 17, 20},
            "facebook": {11, 14, 17, 20}, "threads": {11, 14, 17, 20}}
FIN_PROF = dt.date(2026, 11, 1)   # prof IA arrêté par Simon le 1/11 : plus aucune vidéo prof après cette date


def existe(chemin):
    if os.path.exists(os.path.join(ROOT, chemin)): return True
    return subprocess.run(["git", "-C", ROOT, "cat-file", "-e", f"HEAD:{chemin}"], capture_output=True).returncode == 0


def verifier(chemin, reseau):
    try:
        d = json.load(open(chemin, encoding="utf-8"))
    except Exception as e:
        return [f"JSON illisible ({e})"]
    pb = [f"champ « {k} » manquant" for k in REQUIS[reseau] if not d.get(k)]
    if "etiquettes" in REQUIS[reseau] and d.get("etiquettes") is not None and not isinstance(d["etiquettes"], dict):
        pb.append("« etiquettes » doit être un objet {...}")
    try:
        h = dt.datetime.fromisoformat(d["envoyer_apres"])
        if h.tzinfo is None: pb.append("« envoyer_apres » sans fuseau (+01:00)")
        elif reseau in CRENEAUX and (h.hour not in CRENEAUX[reseau] or h.minute):
            pb.append(f"créneau {h:%H:%M} hors règle 5 ({sorted(CRENEAUX[reseau])} h)")
        if "prof" in (d.get("concept") or os.path.basename(chemin)) and h.date() > FIN_PROF:
            pb.append("vidéo prof IA : format arrêté par Simon le 1/11")
    except (KeyError, TypeError, ValueError):
        if d.get("envoyer_apres"): pb.append("« envoyer_apres » n'est pas une date ISO")
    if d.get("fichier") and not existe(d["fichier"]):
        pb.append(f"vidéo introuvable : {d['fichier']}")
    if reseau == "youtube" and len(d.get("titre", "")) > 100:
        pb.append("titre YouTube > 100 caractères")
    return pb


def main():
    erreurs, n = [], 0
    for reseau in REQUIS:
        for chemin in sorted(glob.glob(os.path.join(ROOT, "publications", reseau, "*.json"))):
            n += 1
            for p in verifier(chemin, reseau):
                erreurs.append(f"- {os.path.relpath(chemin, ROOT)} : {p}")
    if erreurs:
        print(f"ÉCHEC : {len(erreurs)} problème(s) sur {n} fichier(s) de publication — ne pas pousser avant correction :")
        print("\n".join(erreurs)); sys.exit(1)
    print(f"OK : {n} fichier(s) de publication vérifiés.")


if __name__ == "__main__":
    main()
