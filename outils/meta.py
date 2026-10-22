"""Publication des Reels Instagram + Facebook (API Graph de Meta), sans Metricool. INACTIF tant que les secrets manquent.
Usage :
  python3 meta.py envoi publications/instagram/<nom>.json     -> Reel Instagram (compte pro relié à la Page)
  python3 meta.py envoi publications/facebook/<nom>.json      -> Reel de Page Facebook
  python3 meta.py essai <fichier.json>                        -> affiche les requêtes sans rien envoyer (test sans secret)
Fichier : {"fichier": "sorties/x.mp4", "legende": "...", "envoyer_apres": "2026-10-24T12:00:00+02:00",
           "concept": "...", "etiquettes": {...}}
Secrets GitHub (jamais dans le dépôt) : META_TOKEN (jeton de Page longue durée), META_IG_ID (id du compte Instagram pro),
META_PAGE_ID (id de la Page). La vidéo doit être publique : on donne à Meta l'URL brute GitHub de la branche videos.
Code retour : 0 = envoyé ou rien à faire (pas encore l'heure, outil inactif) ; 1 = échec (message « ÉCHEC : ... »).
"""
import sys, os, json, time, urllib.request, urllib.parse, datetime
API = "https://graph.facebook.com/v21.0"   # version de l'API : à vérifier sur developers.facebook.com à l'activation
RAW = "https://raw.githubusercontent.com/simon04mathieu/blundercheck/videos/"
ESSAI = False

def req(method, url, data=None, headers=None):
    if ESSAI:
        cache = {k: ("***" if k == "access_token" else v) for k, v in (data or {}).items()}
        print("ESSAI", method, url.split("?")[0], json.dumps(cache, ensure_ascii=False), headers or "")
        return {"id": "essai", "status_code": "FINISHED", "video_id": "essai", "upload_url": "essai", "success": True}
    body = urllib.parse.urlencode(data).encode() if data and method == "POST" else None
    if data and method == "GET": url += "?" + urllib.parse.urlencode(data)
    r = urllib.request.Request(url, data=body, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(r, timeout=120) as f: return json.load(f)
    except urllib.error.HTTPError as e:
        sys.exit(f"ÉCHEC : Meta {method} {url.split('?')[0]} -> {e.code} : {e.read().decode()[:400]}")

def heure_venue(d):
    ea = d.get("envoyer_apres")
    return not ea or datetime.datetime.now(datetime.timezone.utc) >= datetime.datetime.fromisoformat(ea)

def instagram(d, tok, ig):
    c = req("POST", f"{API}/{ig}/media", {"media_type": "REELS", "video_url": RAW + d["fichier"],
            "caption": d["legende"], "share_to_feed": "true", "access_token": tok})
    for _ in range(40):  # Meta télécharge et encode la vidéo : jusqu'à ~10 min
        s = req("GET", f"{API}/{c['id']}", {"fields": "status_code,status", "access_token": tok})
        if s.get("status_code") == "FINISHED": break
        if s.get("status_code") == "ERROR": sys.exit(f"ÉCHEC : Instagram encodage : {s.get('status')}")
        time.sleep(15)
    else: sys.exit("ÉCHEC : Instagram encodage trop long (10 min)")
    p = req("POST", f"{API}/{ig}/media_publish", {"creation_id": c["id"], "access_token": tok})
    return {"reseau": "instagram", "id": p.get("id")}

def facebook(d, tok, page):
    s = req("POST", f"{API}/{page}/video_reels", {"upload_phase": "start", "access_token": tok})
    vid = s["video_id"]
    req("POST", s.get("upload_url") or f"https://rupload.facebook.com/video-upload/v21.0/{vid}", None,
        {"Authorization": f"OAuth {tok}", "file_url": RAW + d["fichier"]})
    f = req("POST", f"{API}/{page}/video_reels", {"upload_phase": "finish", "video_id": vid, "video_state": "PUBLISHED",
            "description": d["legende"], "access_token": tok})
    return {"reseau": "facebook", "id": vid, "ok": f.get("success")}

def envoi(chemin):
    d = json.load(open(chemin))
    reseau = "instagram" if "/instagram/" in chemin else "facebook"
    if not heure_venue(d): print("pas encore l'heure :", d.get("envoyer_apres")); return None
    tok, ig, page = (os.environ.get(k) for k in ("META_TOKEN", "META_IG_ID", "META_PAGE_ID"))
    if ESSAI: tok, ig, page = "essai", "IG_ID", "PAGE_ID"
    if not tok or (reseau == "instagram" and not ig) or (reseau == "facebook" and not page):
        print("outil Meta inactif : secrets META_* absents (normal tant que Simon n'a pas ouvert les comptes)"); return None
    for k in ("fichier", "legende", "concept", "etiquettes"):
        if k not in d: sys.exit(f"ÉCHEC : champ « {k} » manquant dans {chemin}")
    r = instagram(d, tok, ig) if reseau == "instagram" else facebook(d, tok, page)
    print(json.dumps(r, ensure_ascii=False)); return r

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("envoi", "essai"): sys.exit(__doc__)
    ESSAI = sys.argv[1] == "essai"
    envoi(sys.argv[2])
