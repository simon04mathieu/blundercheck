"""Fabrication automatique (GitHub Actions) : une commande JSON -> une vidéo finie dans sorties/.
Commandes (fichiers commandes/*.json) :
  {"type": "boucle", "nom": "lasker"}                          BOUCLE sans voix (outils/boucle.py)
  {"type": "perso", "nom": "perso_lasker", "voix": "<id>"?}     voix ElevenLabs + calage + rendu + mixage
  {"type": "coach", "nom": "v_stafford"}                        idem pour un script coach (sous-titres en phrases)
  options : "sans_musique": true, "volume_musique": 0.14, "duree_max": 52
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
    t = re.sub(r"\[[^\]]*\]\s*", "", script)
    return re.sub(r"\b([a-h])([1-8])\b", lambda m: f"{LETTRES[m.group(1)]} {CHIFFRES[m.group(2)]}", t)

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
    vmax = cmd.get("duree_max", 52.0)
    tempo = min(1.18, d0 / vmax) if d0 > vmax else 1.0
    wav = os.path.join(tmp, "voix.wav")
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", brut, "-ac", "1", "-ar", "48000", wav)
    mots = transcrire(wav)
    spec = coach2.construire(nom, mots)
    if cmd.get("sans_musique") is not True: spec["musique"] = 0.0  # la musique de fond vient d'ElevenLabs, pas du synthé
    coach.FLIP = spec["noirs"]; coach.BG = coach.fond()
    muet, fx = os.path.join(tmp, "muet.mp4"), os.path.join(tmp, "fx.wav")
    coach.run(spec, muet, fx, tempo)
    os.makedirs(SORTIES, exist_ok=True); out = os.path.join(SORTIES, f"{nom}.mp4")
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
                 "voice_id": voice_id, "musique": os.path.basename(mus) if mus else "aucune", "mots_transcrits": len(mots)}

perso = video_voix

def boucle(cmd):
    import boucle as B
    out = os.path.join(SORTIES, f"boucle_{cmd['nom']}.mp4")
    B.fabriquer(cmd["nom"], out)
    return out, {"video_s": round(duree(out), 1)}

if __name__ == "__main__":
    os.makedirs(SORTIES, exist_ok=True)
    cmd = json.load(open(sys.argv[1]))
    res = {"echantillons": lambda c: (echantillons(c), {}), "perso": video_voix, "coach": video_voix, "boucle": boucle}[cmd["type"]](cmd)
    print("OK", res[0], json.dumps(res[1], ensure_ascii=False))
