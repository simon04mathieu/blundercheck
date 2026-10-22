"""Fabrication automatique (GitHub Actions) : une commande JSON -> une vidéo finie dans sorties/.
Commandes (fichiers commandes/*.json) :
  {"type": "boucle", "nom": "lasker"}                          BOUCLE sans voix (outils/boucle.py)
  {"type": "perso", "nom": "perso_lasker", "voix": "<id>"?}     voix ElevenLabs + calage + rendu + mixage
  {"type": "coach", "nom": "v_stafford"}                        idem pour un script coach (sous-titres en phrases)
  options : "sans_musique": true, "volume_musique": 0.14, "duree_max": 52
  {"type": "test_voix", "nom": "cases", "versions": ["..."]}  une phrase par version, voix habituelle
  {"type": "echantillons", "n": 5}                              voix françaises de la bibliothèque, à écouter
La voix par défaut est dans outils/voix.json ; sinon la première voix des échantillons.
"""
import sys, os, json, re, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE); SORTIES = os.path.join(ROOT, "sorties")
import eleven

def sh(*a): subprocess.run(a, check=True)

def duree(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True, check=True).stdout)

LETTRES = {"a": "a", "b": "bé", "c": "cé", "d": "dé", "e": "e", "f": "effe", "g": "gé", "h": "hache"}
CHIFFRES = {"1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "6": "six", "7": "sept", "8": "huit"}
def texte_parle(script):
    """Script à repères -> texte lu (cases en toutes lettres : « dé quatre »)."""
    # « d prend [m dxc3] c3 » s'entendait « dé prend c'est trois » : on dit « le pion prend en c3 » (remarque de Simon, 21/10)
    script = re.sub(r"\b[a-h] prend (\[m [a-h]x[a-h][1-8][^\]]*\]\s*)", r"le pion prend en \1", script)
    t = re.sub(r"\[[^\]]*\]\s*", "", script)
    return re.sub(r"\b([a-h])([1-8])\b", lambda m: f"{LETTRES[m.group(1)]} {CHIFFRES[m.group(2)]}", t)

def test_voix(cmd):
    """Plusieurs écritures lues par la voix habituelle, un mp3 par version (sorties/echantillons/test_<nom>_<n>.mp3)."""
    d = os.path.join(SORTIES, "echantillons"); os.makedirs(d, exist_ok=True)
    vd = voix_defaut(); vid = cmd.get("voix") or vd.get("voice_id")
    for i, t in enumerate(cmd["versions"], 1):
        f = os.path.join(d, f"test_{cmd['nom']}_{i}.mp3")
        eleven.tts(t, vid, f, vd.get("stabilite", 0.5)); print("version", i, ":", t, flush=True)
    return d, {"versions": len(cmd["versions"])}

def voix_defaut():
    f = os.path.join(HERE, "voix.json")
    return json.load(open(f)) if os.path.exists(f) else {}

def transcrire(audio):
    from faster_whisper import WhisperModel
    import numpy as np
    from scipy.io import wavfile
    w16 = audio + ".16k.wav"  # on décode nous-mêmes : la lecture de fichier de faster-whisper casse avec PyAV récent
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", audio, "-ac", "1", "-ar", "16000", w16)
    sr, x = wavfile.read(w16)
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(x.astype(np.float32) / 32768.0, language="fr", word_timestamps=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]

def echantillons(cmd):
    d = os.path.join(SORTIES, "echantillons"); os.makedirs(d, exist_ok=True)
    phrase = cmd.get("texte", "[mischievously] Arrête de faire une dame à chaque promotion. Ici, tu fais un poney. "
                              "[excited] Il prend le poney ? Fou gé quatre, échec. [laughs] Et la Gourmande tombe.")
    lignes = ["# Échantillons de voix (ElevenLabs v3)", "", "| # | Nom | voice_id | Accent | Fichier |", "|---|---|---|---|---|"]
    for i, v in enumerate(eleven.voix_francaises(cmd.get("n", 5), cmd.get("genre", "male")), 1):
        vid = eleven.ajouter(v)
        nom = re.sub(r"[^A-Za-z0-9]+", "_", v["nom"])[:30]
        f = os.path.join(d, f"{i}_{nom}.mp3"); eleven.tts(phrase, vid, f)
        lignes.append(f"| {i} | {v['nom']} | `{vid}` | {v.get('accent') or ''} | {os.path.basename(f)} |")
        print("échantillon", i, v["nom"], flush=True)
    open(os.path.join(d, "liste.md"), "w").write("\n".join(lignes) + "\n")
    return d

MUSIQUE_PROMPT = ("Calm, pleasant lo-fi hip hop instrumental, warm Rhodes piano, soft brushed drums, mellow bass, "
                  "85 BPM, relaxed and focused, light and positive, no vocals, seamless loop")

def musique_fond(cmd):
    """Musique douce générée une fois par ElevenLabs Music, gardée dans outils/musique/ et réutilisée.
    Renvoie None si la génération échoue (la vidéo sort alors sans musique, c'est noté au journal)."""
    d = os.path.join(HERE, "musique"); os.makedirs(d, exist_ok=True)
    f = os.path.join(d, cmd.get("musique_fichier", "fond1.mp3"))
    if os.path.exists(f): return f
    try:
        return eleven.musique(cmd.get("musique_prompt", MUSIQUE_PROMPT), f, 60000)
    except SystemExit as e:
        print("MUSIQUE INDISPONIBLE :", e, flush=True); return None

def video_voix(cmd):
    """Format coach (SCRIPTS) ou PERSO : voix ElevenLabs + calage + rendu + mixage (voix devant, musique douce dessous)."""
    import coach, coach2
    from scripts_coach import PERSO, SCRIPTS
    nom = cmd["nom"]
    script = PERSO[nom]["script"] if nom in PERSO else SCRIPTS[nom][1]
    lu = PERSO[nom].get("voix") if nom in PERSO else None
    vd = voix_defaut(); voice_id = cmd.get("voix") or vd.get("voice_id")
    if not voice_id:
        voice_id = eleven.ajouter(eleven.voix_francaises(1)[0])
    tmp = tempfile.mkdtemp()
    # voix gardée dans le dépôt (sorties/voix/) : une relance ne repaie jamais les crédits ElevenLabs
    texte = lu or texte_parle(script)
    import hashlib
    cle = hashlib.sha1(f"{voice_id}|{texte}".encode()).hexdigest()[:10]
    dv = os.path.join(SORTIES, "voix"); os.makedirs(dv, exist_ok=True)
    brut = os.path.join(dv, f"{nom}_{cle}.mp3")
    if not os.path.exists(brut):
        eleven.tts(texte, voice_id, brut, cmd.get("stabilite", vd.get("stabilite", 0.5)))
        print("voix générée :", len(texte), "caractères", flush=True)
    else:
        print("voix réutilisée (0 crédit)", flush=True)
    d0 = duree(brut)
    wav = os.path.join(tmp, "voix.wav")
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", brut, "-ac", "1", "-ar", "48000", wav)
    mots = transcrire(wav)
    spec = coach2.construire(nom, mots)
    if spec.get("pauses"):  # silences « trouve le coup » insérés dans la voix
        import numpy as np
        from scipy.io import wavfile
        sr, x = wavfile.read(wav); parts = []; prev = 0
        for p0, d in sorted(spec["pauses"]):
            i = int(p0 * sr); parts += [x[prev:i], np.zeros(int(d * sr), x.dtype)]; prev = i
        parts.append(x[prev:]); wavfile.write(wav, sr, np.concatenate(parts))
    d1 = d0 + sum(d for _, d in spec.get("pauses", []))
    vmax = cmd.get("duree_max", 55.0)
    tempo = min(1.18, d1 / vmax) if d1 > vmax else 1.0
    if cmd.get("sans_musique") is not True: spec["musique"] = 0.0
    if cmd.get("hook") and spec.get("hook"): spec["hook"] = (cmd["hook"], spec["hook"][1])  # test A/B du hook (0 crédit)  # la musique de fond vient d'ElevenLabs, pas du synthé
    minutage = ecrire_minutage(cmd.get("sortie", nom), spec, tempo)
    coach.FLIP = spec["noirs"]; coach.BG = coach.fond()
    muet, fx = os.path.join(tmp, "muet.mp4"), os.path.join(tmp, "fx.wav")
    coach.run(spec, muet, fx, tempo)
    os.makedirs(SORTIES, exist_ok=True); out = os.path.join(SORTIES, f"{cmd.get('sortie', nom)}.mp4")
    mus = None if cmd.get("sans_musique") else musique_fond(cmd)
    vol = cmd.get("volume_musique", 0.14)  # ≈ -20 dB, encore baissée sous la voix par le compresseur
    if mus:
        fc = (f"[1:a]atempo={tempo:.4f},asplit=2[v][key];[2:a]aresample=48000,aformat=channel_layouts=mono,volume=0.45[f];"
              f"[3:a]aresample=48000,aformat=channel_layouts=mono,volume={vol}[m0];[m0][key]sidechaincompress=threshold=0.02:ratio=6:attack=20:release=400[m];"
              "[v][f][m]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
        ins = ["-i", muet, "-i", wav, "-i", fx, "-stream_loop", "-1", "-i", mus]
    else:
        fc = (f"[1:a]atempo={tempo:.4f}[v];[2:a]volume=0.45[f];"
              "[v][f]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
        ins = ["-i", muet, "-i", wav, "-i", fx]
    sh("ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", fc,
       "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
       "-movflags", "+faststart", out)
    return out, {"voix_brute_s": round(d0, 1), "tempo": round(tempo, 3), "video_s": round(duree(out), 1),
                 "voice_id": voice_id, "musique": os.path.basename(mus) if mus else "aucune", "mots_transcrits": len(mots), "minutage": minutage}

perso = video_voix

def ecrire_minutage(nom, spec, tempo=1.0):
    """sorties/minutage/<nom>.json : seconde (dans la vidéo finie) du début de chaque phrase lue, de chaque coup
    montré, de chaque pause, du hook et de la question finale. Sert au data analyst (rétention seconde par seconde)."""
    k = 1.0 / tempo if tempo else 1.0
    r = lambda t: round(float(t) * k, 2)
    phrases, cur, t0 = [], [], None
    for a, b, txt in spec.get("captions", []):
        if not cur: t0 = a
        cur.append(txt)
        if txt.rstrip()[-1:] in ".!?…":
            phrases.append({"t": r(t0), "texte": " ".join(cur)}); cur = []
    if cur: phrases.append({"t": r(t0), "texte": " ".join(cur)})
    coups = [{"t": r(t), "coup": d[0], "badge": d[1]} for t, typ, d in spec.get("actions", []) if typ == "coup"]
    pauses = [{"t": r(t), "duree": round(float(d[0]) * k, 2), "texte": d[1]}
              for t, typ, d in spec.get("actions", []) if typ == "quiz"]
    duree_v = r(spec.get("duree", 0))
    m = {"nom": nom, "tempo": round(tempo, 3), "duree_s": duree_v,
         "hook": {"texte": spec["hook"][0], "fin": r(spec["hook"][1])} if spec.get("hook") else None,
         "question": {"texte": spec.get("question"), "t": round(max(0.0, duree_v - 3.2), 2)} if spec.get("question") else None,
         "phrases": phrases, "coups": coups, "pauses": pauses}
    d = os.path.join(SORTIES, "minutage"); os.makedirs(d, exist_ok=True)
    json.dump(m, open(os.path.join(d, f"{nom}.json"), "w"), ensure_ascii=False, indent=1)
    return f"{len(phrases)} phrases, {len(coups)} coups, {len(pauses)} pauses"  # dans la ligne OK : le journal ne garde que 3 lignes

def gaffe(cmd):
    """Démo « Ta pire gaffe » sans voix : puzzle du jour Lichess, bruitages + musique jazz chill."""
    import coach, gaffe as G
    spec, info = G.spec_depuis_puzzle(G.puzzle_du_jour())
    coach.FLIP = spec["noirs"]; coach.BG = coach.fond()
    tmp = tempfile.mkdtemp(); muet, fx = os.path.join(tmp, "muet.mp4"), os.path.join(tmp, "fx.wav")
    coach.run(spec, muet, fx, 1.0)
    os.makedirs(SORTIES, exist_ok=True); out = os.path.join(SORTIES, f"gaffe_{info['partie']}.mp4")
    mus = musique_fond(cmd)
    if mus:
        fc = ("[1:a]aresample=48000,aformat=channel_layouts=mono[f];[2:a]aresample=48000,aformat=channel_layouts=mono,volume=0.35[m];"
              "[f][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
        sh("ffmpeg", "-y", "-loglevel", "error", "-i", muet, "-i", fx, "-stream_loop", "-1", "-i", mus, "-filter_complex", fc,
           "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out)
    else:
        sh("ffmpeg", "-y", "-loglevel", "error", "-i", muet, "-i", fx, "-c:v", "copy", "-c:a", "aac", "-shortest", out)
    info["video_s"] = round(duree(out), 1)
    return out, info

def boucle(cmd):
    import boucle as B
    out = os.path.join(SORTIES, f"boucle_{cmd['nom']}.mp4")
    B.fabriquer(cmd["nom"], out)
    return out, {"video_s": round(duree(out), 1)}

if __name__ == "__main__":
    os.makedirs(SORTIES, exist_ok=True)
    cmd = json.load(open(sys.argv[1]))
    res = {"echantillons": lambda c: (echantillons(c), {}), "perso": video_voix, "coach": video_voix, "boucle": boucle, "gaffe": gaffe, "test_voix": test_voix}[cmd["type"]](cmd)
    print("OK", res[0], json.dumps(res[1], ensure_ascii=False))
