#!/usr/bin/env python3
"""Montage du format « Le prof corrige ma partie » (prof_corrige), demandé par Simon le 29/10.

Commande (commandes/<nom>.json, fabriquée par le workflow « Fabrique vidéos ») :
  {"type": "prof", "nom": "prof_1", "source": "essai_1", "langue": "en", "voix": "<voice_id>", "sans_musique": true}
Matière : sorties/prof/<source>/ (partie.pgn sans en-têtes, moments.json, ecran_<ply>.png), faite par outils/prof_corrige.py.

Déroulé (30-45 s) :
  1. image 0 = ton pire coup joué sur l'échiquier ; voix = conseil du vrai prof ; transition vers l'écran du site (stop 1)
  2. la partie repart du début jusqu'à un bon coup ; voix = commentaire du prof ; écran du site (stop 2)
  3. la partie défile jusqu'au pire coup ; voix = résumé du prof
  4. leçon du prof ; retour à l'écran du site (stop 3)
  5. fin : « Analyze your own game, free » + blundercheck.app/try
Règles : les phrases dites sont celles du prof, seulement COUPÉES (jamais réécrites) : on garde le début d'une phrase et on
s'arrête avant le premier morceau qui nomme une case ou un coup (aucune case prononcée). Seuls les coups de Simon sont
commentés. Les écrans sont recadrés : l'en-tête (résultat, ouverture, DATE) et la barre du bas ne sont jamais montrés.
"""
import io, json, os, re, subprocess, sys
import chess, chess.pgn

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE); SORTIES = os.path.join(ROOT, "sorties")

CASE = re.compile(r"\b(?:[KQRBN]?[a-h]?x?[a-h][1-8](?:=[QRBN])?[+#]?|O-O(?:-O)?)\b")
HOOK = {"en": "The AI teacher found|my worst move.", "fr": "Le prof IA a trouvé|mon pire coup."}
FIN = {"en": ("Analyze your own game, free: blundercheck dot app.", "Analyze your own game, free|blundercheck.app/try"),
       "fr": ("Analyse ta partie gratuitement : blundercheck point app.", "Analyse ta partie, gratuit|blundercheck.app/try")}
# recadrage des écrans du site (1075 × 2330) : de l'échiquier jusqu'au-dessus de la barre de navigation
CROP_Y0, CROP_Y1 = 575, 2210
LARGEUR, X0, Y0 = 860, 110, 470


def couper(texte):
    """Garde le début de la phrase du prof jusqu'au premier morceau qui nomme une case ou un coup ; '' si rien ne reste."""
    phrase = re.split(r"(?<=[.!?])\s", texte.strip())[0]
    morceaux = re.split(r"(,\s|:\s|;\s|\swhile\s|\sbecause\s|\swhich\s|\salors que\s|\scar\s)", phrase)
    garde = ""
    for i in range(0, len(morceaux), 2):
        if CASE.search(morceaux[i]): break
        garde += (morceaux[i - 1] if i else "") + morceaux[i]
    garde = garde.strip().rstrip(",:;")
    if not garde or len(garde.split()) < 3: return ""
    return garde if garde[-1] in ".!?" else garde + "."


def matiere(source):
    d = os.path.join(SORTIES, "prof", source)
    m = json.load(open(os.path.join(d, "moments.json"), encoding="utf-8"))
    jeu = chess.pgn.read_game(io.StringIO(open(os.path.join(d, "partie.pgn"), encoding="utf-8").read()))
    sans = []; b = jeu.board()
    for mv in jeu.mainline_moves(): sans.append(b.san(mv)); b.push(mv)
    moi = m["couleur_de_simon"]
    miens = [x for x in m["moments"] if x["camp"] == moi]
    pires = [x for x in miens if x["tag"] in ("gaffe", "erreur")]
    if not pires: raise SystemExit("ÉCHEC : aucun coup raté de Simon dans moments.json (vidéo reportée, jamais simulée)")
    pire = max(pires, key=lambda x: x.get("delta", 0))
    bons = [x for x in miens if x["tag"] in ("meilleur", "brillant", "bon") and x["ply"] < pire["ply"]]
    bon = bons[0] if bons else None
    return d, m, sans, pire, bon


def construire(cmd):
    """Écrit l'entrée PERSO (script + voix) en mémoire et renvoie (phrases, écrans par phrase)."""
    from scripts_coach import PERSO, QUESTIONS
    lg = cmd.get("langue", "en")
    d, m, sans, pire, bon = matiere(cmd["source"])
    P = lambda n: " ".join(sans[:n])          # position après n demi-coups
    phrases = []                               # (texte, marques par mot, écran ou None)
    s1 = couper(pire.get("conseil", "")) or couper(pire.get("commentaire", ""))
    if not s1: raise SystemExit("ÉCHEC : commentaire du prof inutilisable sans dire de case (vidéo reportée)")
    w = s1.split()
    phrases.append((s1, {0: f"[p {P(pire['ply'] - 1)}] [m {sans[pire['ply'] - 1]} gaffe] [x impact]"}, pire["ecran"]))
    if bon and couper(bon["commentaire"]):
        s2 = couper(bon["commentaire"])
        phrases.append((s2, {0: f"[h] [p {P(bon['ply'] - 1)}]", 1: f"[m {sans[bon['ply'] - 1]} brillant]"}, bon["ecran"]))
        debut = bon["ply"]
    else:
        debut = 0
    s3 = couper(m.get("resume_du_prof", ""))
    if s3:
        w3 = s3.split(); n = len(w3); marques = {}
        cibles = [debut + round((pire["ply"] - 1 - debut) * (k + 1) / (n - 1)) for k in range(n - 1)]
        for k, c in enumerate(cibles):
            marques[k] = f"[p {P(c)}]" if c > 0 else ""
        marques[n - 1] = f"[m {sans[pire['ply'] - 1]} gaffe]"
        if not phrases[1:]: marques[0] = "[h] " + marques[0]
        phrases.append((s3, marques, None))
    lecon = next((couper(x) for x in m.get("lecons_du_prof", []) if couper(x)), "")
    if lecon: phrases.append((lecon, {}, pire["ecran"]))
    phrases.append((FIN[lg][0], {}, None))
    script, voix = [], []
    for texte, marques, _ in phrases:
        mots = texte.split()
        script.append(" ".join((marques.get(i, "") + " " + w_).strip() for i, w_ in enumerate(mots)))
        voix.append(texte)
    nom = cmd["nom"]
    PERSO[nom] = {"cote": "blancs" if m["couleur_de_simon"] == "w" else "noirs", "sous_titres": "phrase",
                  "hook": HOOK[lg], "voix": " ".join(voix), "script": " ".join(script)}
    QUESTIONS[nom] = FIN[lg][1]
    return d, [(t, e) for t, _, e in phrases]


def incruster(video, dossier, phrases, minutage, out):
    """Écrans du vrai site par-dessus l'échiquier, pendant les phrases qui en ont un (glissé depuis la droite, 0,35 s)."""
    ph = json.load(open(minutage, encoding="utf-8"))["phrases"]
    if len(ph) != len(phrases): raise SystemExit(f"ÉCHEC : {len(ph)} phrases minutées pour {len(phrases)} écrites")
    duree_v = json.load(open(minutage, encoding="utf-8"))["duree_s"]
    ins, filtres, prev, k = ["-i", video], [], "0:v", 0
    for i, (texte, ecran) in enumerate(phrases):
        if not ecran: continue
        a = ph[i]["t"] + (1.0 if i == 0 else 0.4)
        b = ph[i + 1]["t"] - 0.15 if i + 1 < len(ph) else duree_v
        if b - a < 0.8: continue
        k += 1; ins += ["-loop", "1", "-t", f"{duree_v:.2f}", "-i", os.path.join(dossier, ecran)]
        filtres.append(f"[{k}:v]crop=iw:{CROP_Y1 - CROP_Y0}:0:{CROP_Y0},scale={LARGEUR}:-2,"
                       f"pad=iw+12:ih+12:6:6:color=0xE8C468,format=rgba[e{k}]")
        x = f"if(lt(t-{a:.2f}\\,0.35)\\,{X0}+1080*(1-(t-{a:.2f})/0.35)\\,{X0})"
        filtres.append(f"[{prev}][e{k}]overlay=x='{x}':y={Y0}:enable='between(t,{a:.2f},{b:.2f})'[v{k}]")
        prev = f"v{k}"
    if not filtres:
        os.replace(video, out); return 0
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(filtres), "-map", f"[{prev}]",
                    "-map", "0:a?", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "copy",
                    "-t", f"{duree_v:.2f}", "-movflags", "+faststart", out], check=True)
    return k


def prof_video(cmd):
    if cmd.get("mode") == "complet": return prof_complet(cmd)
    import fabrique
    dossier, phrases = construire(cmd)
    nom = cmd["nom"]
    brut, info = fabrique.video_voix(dict(cmd, type="perso", sortie=nom + "_plateau"))
    mt = os.path.join(SORTIES, "minutage", nom + "_plateau.json")
    out = os.path.join(SORTIES, nom + ".mp4")
    n = incruster(brut, dossier, phrases, mt, out)
    os.replace(mt, os.path.join(SORTIES, "minutage", nom + ".json"))
    if os.path.exists(brut): os.remove(brut)
    info.update({"video_s": round(fabrique.duree(out), 1), "ecrans": n, "phrases_du_prof": len(phrases) - 1})
    return out, info


# ---------------- format « partie complète » (Simon, 29/10) ----------------
# Toute la partie défile coup par coup, sans saut (rythme régulier, badge du vrai site sur chaque coup analysé) ;
# arrêt seulement sur les fautes de Simon : écran du site + phrase du prof. Résumé du prof pendant l'ouverture,
# leçon à la fin, puis « Analyze your own game ». Commande : {"type": "prof", "mode": "complet", "nom": ..., "source": ...}
BADGE_SITE = {"gaffe": "gaffe", "erreur": "erreur", "meilleur": "meilleur", "excellent": "bon", "bon": "bon",
              "brillant": "brillant", "livre": "livre"}
HOOK_COMPLET = {"en": "The AI teacher checked|every move of my game.", "fr": "Le prof IA a vérifié|chaque coup de ma partie."}


def _voix(texte, cmd, nom):
    """(échantillons 48 kHz mono int16, mots [(début, fin, mot)]) ; voix gardée dans sorties/voix/ (une relance ne repaie rien)."""
    import hashlib, tempfile
    import numpy as np
    from scipy.io import wavfile
    import fabrique, eleven
    if cmd.get("muet"):  # essai sans crédit : 0,38 s par mot, silence
        mots = [(i * 0.38, i * 0.38 + 0.32, w) for i, w in enumerate(texte.split())]
        return np.zeros(int((mots[-1][1] + 0.1) * 48000), np.int16), mots
    vid = cmd.get("voix") or fabrique.voix_defaut().get("voice_id"); lg = cmd.get("langue", "en")
    cle = hashlib.sha1(f"{vid}|{texte}".encode()).hexdigest()[:10]
    dv = os.path.join(SORTIES, "voix"); os.makedirs(dv, exist_ok=True)
    mp3 = os.path.join(dv, f"{nom}_{cle}.mp3")
    if not os.path.exists(mp3):
        eleven.tts(texte, vid, mp3, cmd.get("stabilite", 0.5), langue=lg)
        print("voix générée :", len(texte), "caractères", flush=True)
    else:
        print("voix réutilisée (0 crédit)", flush=True)
    wav = os.path.join(tempfile.mkdtemp(), "v.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-ac", "1", "-ar", "48000", wav], check=True)
    _, x = wavfile.read(wav)
    mots = fabrique.transcrire(wav, lg)
    # sous-titres = le texte exact du prof (Whisper entend parfois mal : « pawn » → « porn ») ; seuls les temps viennent de Whisper
    vrais = texte.split()
    if mots and len(mots) != len(vrais):
        a, z = mots[0][0], mots[-1][1]; pas = (z - a) / len(vrais)
        mots = [(a + i * pas, a + (i + 1) * pas - 0.04, "") for i in range(len(vrais))]
    return x, [(s_, e_, w_) for (s_, e_, _), w_ in zip(mots, vrais)]


def _legendes(mots, t0):
    caps, cur, a = [], [], None
    for s, e, w in mots:
        if not cur: a = s
        cur.append(w)
        if w[-1:] in ".!?" or (w[-1:] in ",:;" and len(cur) >= 3) or len(cur) >= 6:
            caps.append((t0 + a, t0 + e, re.sub(r"[,:;]$", "", " ".join(cur)))); cur = []
    if cur: caps.append((t0 + a, t0 + mots[-1][1], " ".join(cur)))
    return caps


def prof_complet(cmd):
    import tempfile
    import numpy as np
    from scipy.io import wavfile
    import coach, fabrique
    nom, lg = cmd["nom"], cmd.get("langue", "en")
    d = os.path.join(SORTIES, "prof", cmd["source"])
    m = json.load(open(os.path.join(d, "moments.json"), encoding="utf-8"))
    jeu = chess.pgn.read_game(io.StringIO(open(os.path.join(d, "partie.pgn"), encoding="utf-8").read()))
    sans, b = [], jeu.board()
    for mv in jeu.mainline_moves(): sans.append(b.san(mv)); b.push(mv)
    moi = m["couleur_de_simon"]
    tags = {c["ply"]: c["tag"] for c in m.get("coups", [])}
    arrets = {}
    for x in m["moments"]:
        if x["camp"] != moi or x["tag"] not in ("gaffe", "erreur"): continue
        phrase = couper(x.get("commentaire", "")) or couper(x.get("conseil", ""))
        if phrase: arrets[x["ply"]] = (phrase, x.get("ecran")); tags.setdefault(x["ply"], x["tag"])
    if not arrets: raise SystemExit("ÉCHEC : aucune faute de Simon commentable sans dire de case (vidéo reportée, jamais simulée)")
    pire = max((x for x in m["moments"] if x["ply"] in arrets), key=lambda x: x.get("delta", 0))
    resume = couper(m.get("resume_du_prof", ""))
    lecon = next((couper(x) for x in m.get("lecons_du_prof", []) if couper(x)), "")
    # voix (une par phrase, mêmes crédits qu'une seule)
    V = {}
    for cle_, texte in [("resume", resume), ("lecon", lecon), ("fin", FIN[lg][0])] + [(p, a[0]) for p, a in arrets.items()]:
        if texte: V[cle_] = _voix(texte, cmd, nom)
    dur = lambda k: len(V[k][0]) / 48000
    # calendrier : image 0 = pire faute (teaser), puis la partie entière à rythme régulier
    n = len(sans)
    fixe = 2.0 + sum(dur(p) + 0.75 for p in arrets) + (dur("lecon") + 0.9 if "lecon" in V else 0) + dur("fin") + 0.9
    dt = max(0.33, min(0.6, (57.5 - fixe) / n))   # toute la partie, jamais plus de 58 s au total (YouTube < 1 min)
    t = 2.0; actions = [(2.0, "position", [])]; segments = []; ecrans = []
    if "resume" in V: segments.append((2.2, "resume"))
    for ply in range(1, n + 1):
        badge = BADGE_SITE.get(tags.get(ply, ""))
        if ply == n and b.is_checkmate(): badge = "mat"
        actions.append((t, "coup", (sans[ply - 1], badge)))
        t += dt
        if ply in arrets:
            t0 = t + 0.35
            if segments and segments[-1][0] + dur(segments[-1][1]) > t0: t0 = segments[-1][0] + dur(segments[-1][1]) + 0.2
            segments.append((t0, ply)); fin = t0 + dur(ply) + 0.4
            if arrets[ply][1]: ecrans.append((t0 + 0.2, fin - 0.15, arrets[ply][1]))
            t = fin
    if segments and segments[-1][0] + dur(segments[-1][1]) > t: t = segments[-1][0] + dur(segments[-1][1]) + 0.2
    t += 0.5
    if "lecon" in V:
        segments.append((t, "lecon")); ecrans.append((t + 0.2, t + dur("lecon") + 0.2, pire.get("ecran"))); t += dur("lecon") + 0.4
    segments.append((t, "fin")); t += dur("fin") + 0.3
    # audio voix + légendes
    voix = np.zeros(int((t + 1.0) * 48000), np.int16); caps = []; phrases = []
    for t0, k in segments:
        x, mots = V[k]; i = int(t0 * 48000); voix[i:i + len(x)] = x[: len(voix) - i]
        caps += _legendes(mots, t0); phrases.append({"t": round(t0, 2), "texte": " ".join(w for _, _, w in mots)})
    tb = chess.Board()
    for s_ in sans[: pire["ply"]]: tb.push_san(s_)
    spec = {"duree": t, "captions": caps, "actions": actions, "noirs": moi == "b", "sous_titres": "phrase",
            "hook": (HOOK_COMPLET[lg], 2.0), "teaser_board": tb, "question": FIN[lg][1], "musique": 0.0,
            "fx": {"gaffe": "bwomp", "mat": "impact"}, "slide": min(0.28, dt * 0.6)}
    tmp = tempfile.mkdtemp(); muet, fx, wv = (os.path.join(tmp, f) for f in ("muet.mp4", "fx.wav", "voix.wav"))
    coach.FLIP = spec["noirs"]; coach.BG = coach.fond()
    coach.run(spec, muet, fx, 1.0)
    wavfile.write(wv, 48000, voix)
    plateau = os.path.join(tmp, "plateau.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", muet, "-i", wv, "-i", fx, "-filter_complex",
                    "[1:a]aformat=channel_layouts=mono[v];[2:a]aresample=48000,aformat=channel_layouts=mono,volume=0.45[f];"
                    "[v][f]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", plateau], check=True)
    # minutage (rétention) puis incrustation des écrans du site
    dm = os.path.join(SORTIES, "minutage"); os.makedirs(dm, exist_ok=True)
    json.dump({"nom": nom, "tempo": 1.0, "duree_s": round(t + 0.6, 2), "hook": {"texte": HOOK_COMPLET[lg], "fin": 2.0},
               "question": {"texte": FIN[lg][1], "t": round(t + 0.6 - 3.2, 2)}, "phrases": phrases,
               "coups": [{"t": round(a, 2), "coup": dd[0], "badge": dd[1]} for a, ty, dd in actions if ty == "coup"],
               "pauses": [], "ecrans": [{"t": round(a, 2), "fin": round(z, 2), "ecran": e} for a, z, e in ecrans]},
              open(os.path.join(dm, nom + ".json"), "w"), ensure_ascii=False, indent=1)
    out = os.path.join(SORTIES, nom + ".mp4")
    _incruster_fenetres(plateau, d, ecrans, out, t + 0.6)
    return out, {"video_s": round(fabrique.duree(out), 1), "demi_coups": n, "rythme_s": round(dt, 2), "arrets": len(arrets),
                 "ecrans": len(ecrans), "voix": "aucune" if cmd.get("muet") else (cmd.get("voix") or "défaut"), "musique": "aucune"}


def _incruster_fenetres(video, dossier, ecrans, out, duree_v):
    ins, filtres, prev = ["-i", video], [], "0:v"
    for k, (a, b, ecran) in enumerate(ecrans, 1):
        ins += ["-loop", "1", "-t", f"{duree_v:.2f}", "-i", os.path.join(dossier, ecran)]
        filtres.append(f"[{k}:v]crop=iw:{CROP_Y1 - CROP_Y0}:0:{CROP_Y0},scale={LARGEUR}:-2,"
                       f"pad=iw+12:ih+12:6:6:color=0xE8C468,format=rgba[e{k}]")
        x = f"if(lt(t-{a:.2f}\\,0.35)\\,{X0}+1080*(1-(t-{a:.2f})/0.35)\\,{X0})"
        filtres.append(f"[{prev}][e{k}]overlay=x='{x}':y={Y0}:enable='between(t,{a:.2f},{b:.2f})'[v{k}]"); prev = f"v{k}"
    if not filtres: os.replace(video, out); return
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(filtres), "-map", f"[{prev}]",
                    "-map", "0:a?", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "copy",
                    "-t", f"{duree_v:.2f}", "-movflags", "+faststart", out], check=True)


if __name__ == "__main__":  # essai local : python3 outils/prof_montage.py essai_1 [en]  → affiche le texte et le script, sans voix
    from scripts_coach import PERSO
    c = {"nom": "essai_prof", "source": sys.argv[1], "langue": sys.argv[2] if len(sys.argv) > 2 else "en"}
    _, ph = construire(c)
    print("VOIX (", len(PERSO["essai_prof"]["voix"]), "car.) :", PERSO["essai_prof"]["voix"])
    for t, e in ph: print(" -", e or "—", ":", t)
    print("SCRIPT :", PERSO["essai_prof"]["script"])
