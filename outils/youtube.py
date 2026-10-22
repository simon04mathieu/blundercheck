"""YouTube : envoi de Shorts et relevé des chiffres, sans Metricool.
Identifiants (secrets GitHub Actions, jamais dans le code) : YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN
(autorisations : youtube.upload, youtube.readonly ; compte de la chaîne : ben.white).
Seuls des chiffres publics (vues, j'aime, commentaires) sont enregistrés : le dépôt est public.

Usage :
  python3 youtube.py chaine                       -> nom et identifiant de la chaîne (test)
  python3 youtube.py envoi <fichier.json>         -> envoie la vidéo décrite (voir publications/)
  python3 youtube.py stats <sortie.json> [jours]  -> chiffres par vidéo (vues, durée vue, rétention, j'aime, abonnés)

Fichier d'envoi (publications/youtube/*.json) :
  {"fichier": "sorties/v_englund.mp4", "titre": "...", "description": "...", "tags": ["échecs"],
   "envoyer_apres": "2026-10-23T12:00:00+02:00"}  # facultatif : le workflow horaire l'envoie (en public) à partir de cette heure
  ("publier_le" existe aussi : programmation YouTube native, mais elle passe par le mode privé, à éviter avant l'audit)
Note : tant que Google n'a pas audité l'appli, YouTube peut forcer les vidéos envoyées par l'API en privé.
"""
import os, sys, json, datetime, urllib.request, urllib.parse

def jeton():
    data = urllib.parse.urlencode({
        "client_id": os.environ["YT_CLIENT_ID"], "client_secret": os.environ["YT_CLIENT_SECRET"],
        "refresh_token": os.environ["YT_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode()
    with urllib.request.urlopen("https://oauth2.googleapis.com/token", data, timeout=30) as r:
        return json.load(r)["access_token"]

def appel(url, tok, data=None, headers=None, method=None):
    h = {"Authorization": f"Bearer {tok}"}; h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(f"YouTube {e.code} : {e.read()[:500].decode(errors='replace')}")

def chaine(tok):
    _, _, b = appel("https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&mine=true", tok)
    it = json.loads(b)["items"][0]
    return {"id": it["id"], "nom": it["snippet"]["title"], "abonnes": it["statistics"].get("subscriberCount"),
            "uploads": it["contentDetails"]["relatedPlaylists"]["uploads"]}

def envoi(cmd, tok):
    status = {"privacyStatus": "public", "selfDeclaredMadeForKids": False, "containsSyntheticMedia": False}
    if cmd.get("publier_le"):
        status["privacyStatus"] = "private"
        status["publishAt"] = datetime.datetime.fromisoformat(cmd["publier_le"]).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    meta = {"snippet": {"title": cmd["titre"][:100], "description": cmd.get("description", ""),
                        "tags": cmd.get("tags", []), "categoryId": "27", "defaultLanguage": "fr",
                        "defaultAudioLanguage": "fr"}, "status": status}
    taille = os.path.getsize(cmd["fichier"])
    _, h, _ = appel("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status", tok,
                    data=json.dumps(meta).encode(), method="POST",
                    headers={"Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": "video/mp4",
                             "X-Upload-Content-Length": str(taille)})
    url = h.get("Location") or h.get("location")
    with open(cmd["fichier"], "rb") as f:
        _, _, b = appel(url, tok, data=f.read(), method="PUT", headers={"Content-Type": "video/mp4"})
    v = json.loads(b)
    return {"id": v["id"], "url": f"https://www.youtube.com/shorts/{v['id']}", "statut": v["status"].get("privacyStatus"),
            "publier_le": v["status"].get("publishAt")}

def stats(tok, jours=28):
    c = chaine(tok)
    ids = []; page = ""
    while True:
        _, _, b = appel("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50"
                        f"&playlistId={c['uploads']}{'&pageToken=' + page if page else ''}", tok)
        js = json.loads(b); ids += [i["contentDetails"]["videoId"] for i in js.get("items", [])]
        page = js.get("nextPageToken")
        if not page or len(ids) >= 200: break
    videos = {}
    for k in range(0, len(ids), 50):
        _, _, b = appel("https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails,status&id="
                        + ",".join(ids[k:k + 50]), tok)
        for v in json.loads(b)["items"]:
            s = v["statistics"]
            videos[v["id"]] = {"titre": v["snippet"]["title"], "publiee": v["snippet"]["publishedAt"],
                               "statut": v["status"]["privacyStatus"], "duree": v["contentDetails"]["duration"],
                               "vues": int(s.get("viewCount", 0)), "jaime": int(s.get("likeCount", 0)),
                               "commentaires": int(s.get("commentCount", 0))}
    # Pas de YouTube Analytics : le dépôt est public, on n'y garde que des chiffres publics (décision du 22/10).
    return {"date": datetime.datetime.now(datetime.timezone.utc).isoformat(), "chaine": c, "videos": videos}

if __name__ == "__main__":
    tok = jeton(); action = sys.argv[1]
    if action == "chaine":
        c = chaine(tok); print(json.dumps({k: c[k] for k in ("nom", "id", "abonnes")}, ensure_ascii=False))
    elif action == "envoi":
        print(json.dumps(envoi(json.load(open(sys.argv[2])), tok), ensure_ascii=False))
    elif action == "stats":
        r = stats(tok, int(sys.argv[3]) if len(sys.argv) > 3 else 28)
        json.dump(r, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
        print(r["chaine"]["nom"], len(r["videos"]), "vidéos")
