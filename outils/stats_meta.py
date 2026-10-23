"""Relevés quotidiens Instagram, Facebook et Threads (LECTURE SEULE, rien n'est publié). Créé le 24/10/2026 (chantier du chef).
Usage :
  python3 stats_meta.py              -> écrit stats/instagram.json, stats/facebook.json, stats/threads.json
  python3 stats_meta.py essai        -> affiche les requêtes sans rien appeler (test sans secret)
Secrets (jamais dans le dépôt) : META_TOKEN, META_IG_ID, META_PAGE_ID (Instagram + Page), THREADS_TOKEN + CHIFFRE (Threads,
jeton géré par outils/threads.py). Chaque fichier contient : date du relevé, abonnés, et par publication les chiffres que
l'API accepte de donner. Une statistique refusée (permission manquante) est notée dans « erreurs » sans faire échouer le reste.
Garde-fou : on vérifie aussi l'identité des comptes (outils/garde_fou.py) avant d'écrire quoi que ce soit.
Code retour : 0 = au moins un réseau relevé ; 1 = aucun réseau relevé.
"""
import sys, os, json, datetime, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from garde_fou import verifier as _verifier
META = "https://graph.facebook.com/v26.0"
THREADS = "https://graph.threads.com/v1.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESSAI = False

class Refus(Exception): pass

def verifier(*a, **k):
    if not ESSAI: _verifier(*a, **k)

def get(url, params):
    if ESSAI:
        print("ESSAI GET", url, json.dumps({k: ("***" if k == "access_token" else v) for k, v in params.items()}))
        return {"data": []}
    try:
        with urllib.request.urlopen(url + "?" + urllib.parse.urlencode(params), timeout=60) as f: return json.load(f)
    except urllib.error.HTTPError as e:
        raise Refus(f"{e.code} {url.split('/')[-1]} : {e.read().decode()[:200]}")

def maintenant(): return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def metriques(url, tok, noms, erreurs, cle="metric"):
    """Insights d'un objet, métrique par métrique (une métrique refusée ne bloque pas les autres)."""
    out = {}
    for m in noms:
        try:
            for x in get(url, {cle: m, "access_token": tok}).get("data", []):
                v = x.get("values", [{}])[0].get("value") if x.get("values") else x.get("total_value", {}).get("value")
                out[x.get("name", m)] = v
        except Refus as e:
            erreurs.add(f"{m} : {str(e)[:160]}")
    return out

def instagram(tok, ig):
    erreurs = set()
    u = get(f"{META}/{ig}", {"fields": "username,followers_count,media_count", "access_token": tok})
    verifier("instagram", u.get("username"))
    pubs = []
    for p in get(f"{META}/{ig}/media", {"fields": "id,caption,timestamp,media_product_type,like_count,comments_count,permalink",
                                         "limit": 30, "access_token": tok}).get("data", []):
        p["insights"] = metriques(f"{META}/{p['id']}/insights", tok, ["views", "reach", "shares", "saved", "total_interactions"], erreurs)
        p["caption"] = (p.get("caption") or "")[:80]; pubs.append(p)
    return {"releve": maintenant(), "compte": u.get("username"), "abonnes": u.get("followers_count"),
            "publications": pubs, "erreurs": sorted(erreurs)}

def facebook(tok, page):
    erreurs = set()
    p = get(f"{META}/{page}", {"fields": "name,category,followers_count,fan_count", "access_token": tok})
    verifier("facebook", p.get("name"), page=bool(p.get("category")))
    pubs = []
    try:
        reels = get(f"{META}/{page}/video_reels", {"fields": "id,description,created_time,permalink_url", "limit": 30,
                                                   "access_token": tok}).get("data", [])
    except Refus as e:
        reels = []; erreurs.add(f"video_reels : {str(e)[:160]}")
    for r in reels:
        r["insights"] = metriques(f"{META}/{r['id']}/video_insights", tok,
                                  ["blue_reels_play_count", "post_impressions_unique", "post_video_likes_by_reaction_type",
                                   "post_video_social_actions", "post_video_followers"], erreurs)
        r["description"] = (r.get("description") or "")[:80]; pubs.append(r)
    return {"releve": maintenant(), "page": p.get("name"), "abonnes": p.get("followers_count"), "fans": p.get("fan_count"),
            "publications": pubs, "erreurs": sorted(erreurs)}

def threads(tok):
    erreurs = set()
    u = get(f"{THREADS}/me", {"fields": "id,username", "access_token": tok})
    verifier("threads", u.get("username"))
    ab = metriques(f"{THREADS}/me/threads_insights", tok, ["followers_count"], erreurs)
    pubs = []
    for t in get(f"{THREADS}/me/threads", {"fields": "id,text,timestamp,permalink,media_type", "limit": 30,
                                            "access_token": tok}).get("data", []):
        t["insights"] = metriques(f"{THREADS}/{t['id']}/insights", tok, ["views", "likes", "replies", "reposts", "quotes", "shares"], erreurs)
        t["text"] = (t.get("text") or "")[:80]; pubs.append(t)
    return {"releve": maintenant(), "compte": u.get("username"), "abonnes": ab.get("followers_count"),
            "publications": pubs, "erreurs": sorted(erreurs)}

def main():
    ok = 0
    tok, ig, page = (os.environ.get(k) for k in ("META_TOKEN", "META_IG_ID", "META_PAGE_ID"))
    if ESSAI: tok, ig, page = "essai", "IG_ID", "PAGE_ID"
    taches = [("instagram", lambda: instagram(tok, ig), tok and ig), ("facebook", lambda: facebook(tok, page), tok and page)]
    import threads as T
    T.ESSAI = ESSAI
    ttok = T.jeton() if (os.environ.get("THREADS_TOKEN") or os.path.exists(T.JETON) or ESSAI) else None
    taches.append(("threads", lambda: threads(ttok), ttok))
    for nom, f, actif in taches:
        if not actif: print(f"{nom} : secrets absents, sauté"); continue
        try:
            r = f()
        except Refus as e:
            print(f"ÉCHEC : {nom} : {e}"); continue
        if ESSAI: print(nom, "essai OK"); ok += 1; continue
        os.makedirs(os.path.join(ROOT, "stats"), exist_ok=True)
        json.dump(r, open(os.path.join(ROOT, "stats", f"{nom}.json"), "w"), ensure_ascii=False, indent=1)
        print(f"{nom} OK : {r.get('abonnes')} abonnés, {len(r['publications'])} publications, {len(r['erreurs'])} statistiques refusées")
        ok += 1
    return ok

if __name__ == "__main__":
    ESSAI = len(sys.argv) > 1 and sys.argv[1] == "essai"
    sys.exit(0 if main() else 1)
