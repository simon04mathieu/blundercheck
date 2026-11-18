"""Phrase d'abonnement + hashtags ajoutés automatiquement aux textes publiés (18/11, Simon : « mets des hashtags, mais surtout
des trucs genre abonnez-vous si vous avez trouvé la solution, ou si c'était trop facile, des trucs putaclic »).
Appelé par credits_musique.ajouter (donc par tous les outils d'envoi) : 0 token, les agents n'écrivent rien.
Phrase choisie en rotation selon le nom de la vidéo ; langue = FR si le fichier finit par _fr. Jamais ajoutée deux fois."""
import hashlib, os, re

EN = ["Found it? Follow, a new puzzle drops every day.",
      "Too easy? Follow and try tomorrow's.",
      "Got it in 3 seconds? Follow and prove it tomorrow.",
      "Missed it? Follow, you'll get the next one.",
      "Write your move in the comments, then follow for tomorrow's.",
      "Only real players find this. Found it? Follow."]
FR = ["Trouvé ? Abonne-toi, un nouveau défi chaque jour.",
      "Trop facile ? Abonne-toi et tente celui de demain.",
      "Trouvé en 3 secondes ? Abonne-toi et prouve-le demain.",
      "Raté ? Abonne-toi, tu auras le prochain.",
      "Écris ton coup en commentaire, puis abonne-toi pour celui de demain.",
      "Seuls les vrais joueurs trouvent. Trouvé ? Abonne-toi."]
TAGS_EN = ["#chess", "#chesspuzzle", "#chesstactics", "#chesstok", "#chessgame"]
TAGS_FR = ["#echecs", "#chess", "#echecsfr", "#chesstok", "#puzzle"]
MARQUES = EN + FR

def phrase(fichier_video):
    nom = os.path.splitext(os.path.basename(fichier_video or ""))[0]
    fr = nom.endswith("_fr")
    liste = FR if fr else EN
    return liste[int(hashlib.sha1(nom.encode()).hexdigest(), 16) % len(liste)], (TAGS_FR if fr else TAGS_EN)

def ajouter(texte, fichier_video):
    texte = texte or ""
    if any(p in texte for p in MARQUES): return texte
    p, tags = phrase(fichier_video)
    # hashtags déjà présents à la fin du texte : on les sépare pour mettre la phrase juste avant
    m = re.search(r"(\s*(?:#\w+\s*)+)$", texte)
    corps, fin = (texte[:m.start()], m.group(1).strip()) if m else (texte, "")
    deja = set(t.lower() for t in re.findall(r"#\w+", texte))
    fin = " ".join([fin] + [t for t in tags if t.lower() not in deja]).strip()
    return f"{corps.rstrip()}\n\n{p}\n\n{fin}" if corps.strip() else f"{p}\n\n{fin}"
