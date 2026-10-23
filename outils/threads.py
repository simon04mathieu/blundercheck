"""Publication des vidéos sur Threads (API Threads de Meta), sans Metricool. INACTIF tant que le jeton manque. Créé le 23/10/2026.
Usage :
  python3 threads.py envoi publications/threads/<nom>.json   -> publie la vidéo sur le profil Threads (@blundercheckapp)
  python3 threads.py essai <fichier.json>                     -> affiche les requêtes sans rien envoyer (test sans secret)
  python3 threads.py verif                                    -> vérifie le jeton (nom du profil), le renouvelle si besoin, ne publie rien
Fichier : {"fichier": "sorties/x.mp4", "legende": "... (500 caractères max)", "envoyer_apres": "2026-10-24T12:00:00+02:00",
           "concept": "...", "etiquettes": {...}}
Jeton : THREADS_TOKEN (secret GitHub, jeton longue durée de 60 jours donné une seule fois par Simon). L'outil le renouvelle
lui-même (au plus une fois par semaine) et range le jeton à jour chiffré dans threads/jeton.enc avec le mot de passe
TIKTOK_CHIFFRE (variable CHIFFRE). Sans passage pendant 60 jours, le jeton expire : Simon en redonne un.
La vidéo doit être publique : on donne à Threads l'URL brute GitHub de la branche videos (comme pour Instagram).
Code retour : 0 = envoyé ou rien à faire (pas encore l'heure, outil inactif) ; 1 = échec (message « ÉCHEC : ... »).
"""
import sys, os, json, time, subprocess, urllib.request, urllib.parse, datetime
API = "https://graph.threads.com/v1.0"
BASE = "https://graph.threads.com"
RAW = "https://raw.githubusercontent.com/simon04mathieu/blundercheck/videos/"
JETON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "threads", "jeton.enc")
RENOUVELER_APRES = 7 * 86400
ESSAI = False

def req(method, url, data=None):
    if ESSAI:
        cache = {k: ("***" if k == "access_token" else v) for k, v in (data or {}).items()}
        print("ESSAI", method, url.split("?")[0], json.dumps(cache, ensure_ascii=False))
        return {"id": "essai", "status": "FINISHED", "username": "essai", "access_token": "essai", "expires_in": 5184000}
    body = urllib.parse.urlencode(data).encode() if data and method == "POST" else None
    if data and method == "GET": url += "?" + urllib.parse.urlencode(data)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body, method=method), timeout=120) as f: return json.load(f)
    except urllib.error.HTTPError as e:
        sys.exit(f"ÉCHEC : Threads {method} {url.split('?')[0]} -> {e.code} : {e.read().decode()[:400]}")

def _chiffrer(js):
    os.makedirs(os.path.dirname(JETON), exist_ok=True)
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-salt", "-pass", "env:CHIFFRE", "-out", JETON],
                   input=json.dumps(js).encode(), check=True)

def _dechiffrer():
    out = subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-pass", "env:CHIFFRE", "-in", JETON],
                         capture_output=True, check=True).stdout
    return json.loads(out)

def jeton():
    """Jeton à jour : celui du fichier chiffré s'il existe, sinon le secret THREADS_TOKEN ; renouvelé chaque semaine."""
    if ESSAI: return "essai"
    if not os.environ.get("CHIFFRE"): return os.environ.get("THREADS_TOKEN")
    j = None
    if os.path.exists(JETON):
        try: j = _dechiffrer()
        except Exception: j = None
    if not j or (os.environ.get("THREADS_TOKEN") and os.environ["THREADS_TOKEN"] != j.get("depart")):
        if not os.environ.get("THREADS_TOKEN"): return None
        # premier passage, ou Simon a donné un nouveau jeton : on repart de lui (renouvellement possible après 24 h)
        j = {"jeton": os.environ["THREADS_TOKEN"], "depart": os.environ["THREADS_TOKEN"], "le": time.time() - RENOUVELER_APRES + 86400 + 3600}
        _chiffrer(j)
    if time.time() - j["le"] > RENOUVELER_APRES:
        r = req("GET", BASE + "/refresh_access_token", {"grant_type": "th_refresh_token", "access_token": j["jeton"]})
        j.update({"jeton": r["access_token"], "le": time.time()}); _chiffrer(j)
        print(f"jeton Threads renouvelé (valable {int(r.get('expires_in', 0)) // 86400} jours)")
    return j["jeton"]

def heure_venue(d):
    ea = d.get("envoyer_apres")
    return not ea or datetime.datetime.now(datetime.timezone.utc) >= datetime.datetime.fromisoformat(ea)

def publier(d, tok):
    c = req("POST", f"{API}/me/threads", {"media_type": "VIDEO", "video_url": RAW + d["fichier"],
            "text": d["legende"].encode()[:500].decode(errors="ignore"), "access_token": tok})
    for _ in range(40):  # Threads télécharge et encode la vidéo : jusqu'à ~10 min
        s = req("GET", f"{API}/{c['id']}", {"fields": "status,error_message", "access_token": tok})
        if s.get("status") == "FINISHED": break
        if s.get("status") in ("ERROR", "EXPIRED"): sys.exit(f"ÉCHEC : Threads encodage : {s.get('error_message') or s.get('status')}")
        time.sleep(15)
    else: sys.exit("ÉCHEC : Threads encodage trop long (10 min)")
    p = req("POST", f"{API}/me/threads_publish", {"creation_id": c["id"], "access_token": tok})
    return {"reseau": "threads", "id": p.get("id")}

def envoi(chemin):
    d = json.load(open(chemin))
    if not heure_venue(d): print("pas encore l'heure :", d.get("envoyer_apres")); return None
    tok = jeton()
    if not tok: print("outil Threads inactif : secret THREADS_TOKEN absent (normal tant que Simon ne l'a pas posé)"); return None
    for k in ("fichier", "legende", "concept", "etiquettes"):
        if k not in d: sys.exit(f"ÉCHEC : champ « {k} » manquant dans {chemin}")
    if len(d["legende"].encode()) > 500: print("légende raccourcie à 500 caractères (limite Threads)")
    r = publier(d, tok); print(json.dumps(r, ensure_ascii=False)); return r

def verif():
    tok = jeton()
    if not tok: sys.exit("ÉCHEC : secret THREADS_TOKEN absent")
    u = req("GET", f"{API}/me", {"fields": "id,username", "access_token": tok})
    print(f"VÉRIF OK : profil Threads @{u.get('username')} (id {u.get('id')})"
          + (", jeton rangé chiffré dans threads/jeton.enc" if os.environ.get("CHIFFRE") else ", ATTENTION : CHIFFRE absent, le jeton ne sera pas renouvelé"))

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "verif": verif(); sys.exit(0)
    if len(sys.argv) < 3 or sys.argv[1] not in ("envoi", "essai"): sys.exit(__doc__)
    ESSAI = sys.argv[1] == "essai"
    envoi(sys.argv[2])
