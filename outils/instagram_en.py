"""Reels Instagram EN (blundercheckches), via l'« API Instagram avec connexion Instagram » (pas besoin de Page Facebook).
Ajouté le 29/10/2026 à la demande de Simon. INACTIF tant que le secret INSTAGRAM_EN_TOKEN manque.
Usage :
  python3 instagram_en.py envoi publications/instagram-en/<nom>.json   -> Reel sur le compte Instagram anglais
  python3 instagram_en.py essai <fichier.json>                         -> affiche les requêtes sans rien envoyer
  python3 instagram_en.py verif                                        -> lit le nom du compte, ne publie rien
Fichier : même format qu'Instagram FR ({"fichier", "legende", "envoyer_apres", "concept", "etiquettes"}).
Jeton : secret GitHub INSTAGRAM_EN_TOKEN (jeton longue durée de 60 jours, donné une fois par Simon). L'outil le renouvelle
lui-même chaque semaine et range la version à jour chiffrée dans instagram-en/jeton.enc (mot de passe TIKTOK_CHIFFRE,
variable CHIFFRE). Garde-fou : le nom du compte est lu chez Instagram juste avant chaque envoi (outils/garde_fou.py).
"""
import sys, os, json, time, subprocess, urllib.request, urllib.parse, datetime
from garde_fou import verifier

BASE = "https://graph.instagram.com"
API = BASE + "/v23.0"
RAW = "https://raw.githubusercontent.com/simon04mathieu/blundercheck/videos/"
JETON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "instagram-en", "jeton.enc")
RENOUVELER_APRES = 7 * 86400
ESSAI = False


def req(method, url, data=None):
    if ESSAI:
        print("ESSAI", method, url.split("?")[0], json.dumps({k: ("***" if k == "access_token" else v) for k, v in (data or {}).items()}, ensure_ascii=False))
        return {"id": "essai", "status_code": "FINISHED", "username": "essai", "access_token": "essai"}
    body = urllib.parse.urlencode(data).encode() if data and method == "POST" else None
    if data and method == "GET": url += "?" + urllib.parse.urlencode(data)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body, method=method), timeout=120) as f:
            return json.load(f)
    except urllib.error.HTTPError as e:
        sys.exit(f"ÉCHEC : Instagram EN {method} {url.split('?')[0]} -> {e.code} : {e.read().decode()[:400]}")


def _chiffrer(js):
    os.makedirs(os.path.dirname(JETON), exist_ok=True)
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-salt", "-pass", "env:CHIFFRE", "-out", JETON],
                   input=json.dumps(js).encode(), check=True)


def _dechiffrer():
    out = subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-pass", "env:CHIFFRE", "-in", JETON],
                         capture_output=True, check=True).stdout
    return json.loads(out)


def jeton():
    if ESSAI: return "essai"
    depart = os.environ.get("INSTAGRAM_EN_TOKEN")
    if not os.environ.get("CHIFFRE"): return depart
    j = None
    if os.path.exists(JETON):
        try: j = _dechiffrer()
        except Exception: j = None
    if not j or (depart and depart != j.get("depart")):
        if not depart: return None
        j = {"jeton": depart, "depart": depart, "le": time.time() - RENOUVELER_APRES + 86400 + 3600}   # renouvelable après 24 h
        _chiffrer(j)
    if time.time() - j["le"] > RENOUVELER_APRES:
        r = req("GET", BASE + "/refresh_access_token", {"grant_type": "ig_refresh_token", "access_token": j["jeton"]})
        j.update({"jeton": r["access_token"], "le": time.time()}); _chiffrer(j)
        print(f"jeton Instagram EN renouvelé (valable {int(r.get('expires_in', 0)) // 86400} jours)")
    return j["jeton"]


def heure_venue(d):
    ea = d.get("envoyer_apres")
    return not ea or datetime.datetime.now(datetime.timezone.utc) >= datetime.datetime.fromisoformat(ea)


def envoi(chemin):
    d = json.load(open(chemin))
    if not heure_venue(d): print("pas encore l'heure :", d.get("envoyer_apres")); return None
    tok = jeton()
    if not tok: print("Instagram EN inactif : secret INSTAGRAM_EN_TOKEN absent (normal tant que Simon ne l'a pas posé)"); return None
    for k in ("fichier", "legende", "concept", "etiquettes"):
        if k not in d: sys.exit(f"ÉCHEC : champ « {k} » manquant dans {chemin}")
    moi = req("GET", f"{API}/me", {"fields": "user_id,username", "access_token": tok})
    if not ESSAI: verifier("instagram", moi.get("username"))   # garde-fou juste avant l'envoi
    ig = moi.get("user_id") or "me"
    c = req("POST", f"{API}/{ig}/media", {"media_type": "REELS", "video_url": RAW + d["fichier"], "caption": d["legende"],
                                          "share_to_feed": "true", "access_token": tok})
    for _ in range(40):
        s = req("GET", f"{API}/{c['id']}", {"fields": "status_code,status", "access_token": tok})
        if s.get("status_code") == "FINISHED": break
        if s.get("status_code") == "ERROR": sys.exit(f"ÉCHEC : Instagram EN encodage : {s.get('status')}")
        time.sleep(15)
    else: sys.exit("ÉCHEC : Instagram EN encodage trop long (10 min)")
    p = req("POST", f"{API}/{ig}/media_publish", {"creation_id": c["id"], "access_token": tok})
    r = {"reseau": "instagram-en", "id": p.get("id")}
    print(json.dumps(r, ensure_ascii=False)); return r


def verif():
    tok = jeton()
    if not tok: sys.exit("ÉCHEC : secret INSTAGRAM_EN_TOKEN absent")
    moi = req("GET", f"{API}/me", {"fields": "user_id,username,account_type,followers_count", "access_token": tok})
    verifier("instagram", moi.get("username"))
    print(f"VÉRIF OK : Instagram EN @{moi.get('username')} ({moi.get('account_type')}, {moi.get('followers_count')} abonnés)"
          + (", jeton rangé chiffré dans instagram-en/jeton.enc" if os.environ.get("CHIFFRE") else ", ATTENTION : CHIFFRE absent, jeton non renouvelé"))


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "verif": verif(); sys.exit(0)
    if len(sys.argv) < 3 or sys.argv[1] not in ("envoi", "essai"): sys.exit(__doc__)
    ESSAI = sys.argv[1] == "essai"
    envoi(sys.argv[2])
