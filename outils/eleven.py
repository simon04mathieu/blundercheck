"""Voix ElevenLabs (abonnement de Simon, 21/10). La clé vient UNIQUEMENT de la variable d'environnement
ELEVENLABS_API_KEY (secret GitHub Actions) : jamais dans le code, jamais dans les journaux.
"""
import os, json, urllib.request, urllib.parse

API = "https://api.elevenlabs.io/v1"
MODELE = "eleven_v3"  # le plus expressif ; comprend les indications de jeu entre crochets ([excited], [whispers]…)

def _req(method, path, body=None, params=None, accept="application/json"):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key: raise SystemExit("ELEVENLABS_API_KEY absente (secret GitHub Actions)")
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method=method,
                               headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": accept})
    try:
        with urllib.request.urlopen(r, timeout=300) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ElevenLabs {method} {path} -> {e.code} : {e.read()[:400].decode(errors='replace')}")

def tts(texte, voice_id, out_mp3, stabilite=0.5, modele=MODELE):
    """stabilite (v3) : 0 = créatif (très expressif, parfois instable), 0,5 = naturel, 1 = stable."""
    audio = _req("POST", f"/text-to-speech/{voice_id}", accept="audio/mpeg",
                 params={"output_format": "mp3_44100_128"},
                 body={"text": texte, "model_id": modele, "language_code": "fr",
                       "voice_settings": {"stability": stabilite}})
    open(out_mp3, "wb").write(audio)
    return out_mp3

def voix_francaises(n=5, genre="male"):
    """Voix françaises de la bibliothèque partagée, classées par tendance."""
    js = json.loads(_req("GET", "/shared-voices", params={"language": "fr", "gender": genre, "sort": "trending",
                                                          "page_size": 30}))
    out = []
    for v in js.get("voices", []):
        out.append({"public_owner_id": v["public_owner_id"], "voice_id": v["voice_id"], "nom": v.get("name", "?"),
                    "accent": v.get("accent"), "usage": v.get("use_case"), "description": (v.get("description") or "")[:120]})
        if len(out) >= n: break
    return out

def ajouter(v):
    """Ajoute une voix partagée à « Mes voix » (nécessaire pour la synthèse) et renvoie son voice_id."""
    mine = json.loads(_req("GET", "/voices"))
    for x in mine.get("voices", []):
        if x.get("name") == "BC " + v["nom"]: return x["voice_id"]
    js = json.loads(_req("POST", f"/voices/add/{v['public_owner_id']}/{v['voice_id']}", body={"new_name": "BC " + v["nom"]}))
    return js["voice_id"]
