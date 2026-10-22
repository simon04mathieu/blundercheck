"""TikTok sans Metricool : publication directe (Content Posting API) et relevé des chiffres (Display API).
Secrets GitHub Actions : TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET (appli « BlunderCheck », bac à sable « test » puis
production après l'audit), TIKTOK_CHIFFRE (mot de passe qui chiffre le jeton rangé dans tiktok/jeton.enc).
Le jeton d'accès dure 24 h, le jeton de rafraîchissement 365 jours ; il est renouvelé et re-chiffré à chaque passage.

Usage :
  python3 tiktok.py code <code>              -> échange le code de blundercheck.app/tiktok/retour contre les jetons
  python3 tiktok.py moi                      -> compte autorisé + options de publication (test)
  python3 tiktok.py envoi <fichier.json>     -> publie la vidéo décrite (publications/tiktok/*.json)
  python3 tiktok.py stats <sortie.json>      -> chiffres par vidéo (vues, j'aime, commentaires, partages)

Fichier d'envoi : {"fichier": "sorties/v_noe.mp4", "legende": "...", "envoyer_apres": "2026-10-23T12:00:00+02:00",
                   "ia": true, "marque": true}
Tant que l'appli n'est pas auditée par TikTok, les vidéos publiées par l'API sont forcément privées (SELF_ONLY).
"""
import os, sys, json, math, subprocess, urllib.request, urllib.parse, datetime

API = "https://open.tiktokapis.com"
REDIRECT = "https://blundercheck.app/tiktok/retour"
JETON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tiktok", "jeton.enc")

def _http(method, url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            b = r.read(); return json.loads(b) if b else {}
    except urllib.error.HTTPError as e:
        raise SystemExit(f"TikTok {method} {url.split('?')[0]} -> {e.code} : {e.read()[:500].decode(errors='replace')}")

def _oauth(champs):
    champs.update({"client_key": os.environ["TIKTOK_CLIENT_KEY"], "client_secret": os.environ["TIKTOK_CLIENT_SECRET"]})
    js = _http("POST", API + "/v2/oauth/token/", urllib.parse.urlencode(champs).encode(),
               {"Content-Type": "application/x-www-form-urlencoded", "Cache-Control": "no-cache"})
    if "access_token" not in js: raise SystemExit(f"TikTok jeton refusé : {js.get('error')} {js.get('error_description')}")
    return js

def _chiffrer(js):
    os.makedirs(os.path.dirname(JETON), exist_ok=True)
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-salt", "-pass", "env:TIKTOK_CHIFFRE", "-out", JETON],
                   input=json.dumps(js).encode(), check=True)

def _dechiffrer():
    out = subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-pass", "env:TIKTOK_CHIFFRE", "-in", JETON],
                         capture_output=True, check=True).stdout
    return json.loads(out)

def jeton():
    """Renouvelle le jeton (et le refresh token) et le re-chiffre ; renvoie le jeton d'accès."""
    ancien = _dechiffrer()
    js = _oauth({"grant_type": "refresh_token", "refresh_token": ancien["refresh_token"]})
    _chiffrer(js)
    return js["access_token"]

def _api(tok, method, chemin, corps=None):
    js = _http(method, API + chemin, json.dumps(corps).encode() if corps is not None else None,
               {"Authorization": f"Bearer {tok}", "Content-Type": "application/json; charset=UTF-8"})
    err = js.get("error", {})
    if err.get("code") not in (None, "ok"): raise SystemExit(f"TikTok {chemin} : {err}")
    return js.get("data", {})

def moi(tok):
    u = _api(tok, "GET", "/v2/user/info/?fields=open_id,display_name,username,follower_count,likes_count,video_count")
    c = _api(tok, "POST", "/v2/post/publish/creator_info/query/", {})
    return {"compte": u.get("user", {}), "options": c}

def envoi(cmd, tok):
    info = _api(tok, "POST", "/v2/post/publish/creator_info/query/", {})
    options = info.get("privacy_level_options", [])
    vie_privee = "PUBLIC_TO_EVERYONE" if "PUBLIC_TO_EVERYONE" in options else (options[-1] if options else "SELF_ONLY")
    taille = os.path.getsize(cmd["fichier"])
    morceau = taille if taille < 5_000_000 else 10_000_000
    n = 1 if morceau == taille else math.floor(taille / morceau)
    post = {"title": cmd["legende"][:2200], "privacy_level": vie_privee,
            "disable_comment": False, "disable_duet": False, "disable_stitch": False,
            "brand_content_toggle": False, "brand_organic_toggle": bool(cmd.get("marque", True)),
            "is_aigc": bool(cmd.get("ia", True))}
    d = _api(tok, "POST", "/v2/post/publish/video/init/",
             {"post_info": post, "source_info": {"source": "FILE_UPLOAD", "video_size": taille,
                                                 "chunk_size": morceau, "total_chunk_count": n}})
    with open(cmd["fichier"], "rb") as f:
        donnees = f.read()
    for i in range(n):
        debut = i * morceau; fin = taille if i == n - 1 else debut + morceau
        _http("PUT", d["upload_url"], donnees[debut:fin],
              {"Content-Type": "video/mp4", "Content-Length": str(fin - debut),
               "Content-Range": f"bytes {debut}-{fin - 1}/{taille}"})
    return {"publish_id": d["publish_id"], "vie_privee": vie_privee}

def statut(tok, publish_id):
    return _api(tok, "POST", "/v2/post/publish/status/fetch/", {"publish_id": publish_id})

def stats(tok):
    u = _api(tok, "GET", "/v2/user/info/?fields=display_name,follower_count,likes_count,video_count").get("user", {})
    videos = []; curseur = None
    champs = "id,title,create_time,duration,view_count,like_count,comment_count,share_count,share_url"
    for _ in range(10):
        corps = {"max_count": 20}
        if curseur: corps["cursor"] = curseur
        d = _api(tok, "POST", "/v2/video/list/?fields=" + champs, corps)
        videos += d.get("videos", [])
        if not d.get("has_more"): break
        curseur = d.get("cursor")
    return {"date": datetime.datetime.now(datetime.timezone.utc).isoformat(), "compte": u, "videos": videos}

if __name__ == "__main__":
    action = sys.argv[1]
    if action == "code":
        js = _oauth({"grant_type": "authorization_code", "code": sys.argv[2].strip(), "redirect_uri": REDIRECT})
        _chiffrer(js); print("Jetons TikTok enregistrés (chiffrés). Portées :", js.get("scope"))
    else:
        tok = jeton()
        if action == "moi":
            r = moi(tok); print(json.dumps({"compte": r["compte"].get("display_name"), "abonnes": r["compte"].get("follower_count"),
                                            "options_vie_privee": r["options"].get("privacy_level_options")}, ensure_ascii=False))
        elif action == "envoi":
            r = envoi(json.load(open(sys.argv[2])), tok); print(json.dumps(r, ensure_ascii=False))
        elif action == "stats":
            r = stats(tok); json.dump(r, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
            print(r["compte"].get("display_name"), len(r["videos"]), "vidéos")
