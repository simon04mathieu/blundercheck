"""Crédit de musique ajouté automatiquement aux textes publiés (14/11, Simon : créditer Kevin MacLeod, CC BY 4.0).
La fabrique note la musique utilisée dans sorties/minutage/<nom>.json ("musique") ; si outils/musique/libre/credits.json
demande un crédit pour ce fichier, il est ajouté à la fin du texte (une seule fois). 0 token : les agents n'ont rien à écrire."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(HERE)

def credit(fichier_video):
    nom = os.path.splitext(os.path.basename(fichier_video or ""))[0]
    try:
        m = json.load(open(os.path.join(RACINE, "sorties", "minutage", f"{nom}.json"))).get("musique")
        return json.load(open(os.path.join(HERE, "musique", "libre", "credits.json"))).get(m) if m else None
    except (OSError, ValueError):
        return None

def ajouter(texte, fichier_video, limite=None):
    c = credit(fichier_video)
    if not c or c in (texte or ""): return texte
    if limite:  # Threads (500 octets) : on raccourcit le texte, jamais le crédit
        place = limite - len(c.encode()) - 2
        texte = (texte or "").encode()[:max(0, place)].decode(errors="ignore").rstrip()
    return f"{texte}\n\n{c}" if texte else c
