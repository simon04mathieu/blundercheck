#!/usr/bin/env python3
"""Résumé des chiffres des réseaux sur 24 h, en ~25 lignes (demande de Simon, 29/10 : le Pilote lit ce résumé au lieu
des fichiers bruts de stats/). Compare le relevé actuel de stats/<réseau>.json au dernier relevé d'il y a au moins
24 h (historique git : cloner SANS --depth, avec --filter=blob:none). Seulement des chiffres lus ; manque = « indisponible ».

    python3 outils/resume_chiffres.py [heures=24]
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = int(sys.argv[1]) if len(sys.argv) > 1 else 24


def lire(nom, avant=False):
    f = f"stats/{nom}.json"
    try:
        if not avant:
            return json.load(open(os.path.join(ROOT, f), encoding="utf-8"))
        sha = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%H", f"--before={H} hours ago", "--", f],
                             capture_output=True, text=True).stdout.strip()
        if not sha: return None
        out = subprocess.run(["git", "-C", ROOT, "show", f"{sha}:{f}"], capture_output=True, text=True)
        return json.loads(out.stdout) if out.returncode == 0 else None
    except Exception:
        return None


def videos(nom, d):
    """{id: (titre, vues)} et abonnés, quel que soit le format du réseau."""
    if not d: return {}, None
    if nom == "youtube":
        return {k: (v.get("titre", ""), int(v.get("vues") or 0)) for k, v in d.get("videos", {}).items()}, d.get("chaine", {}).get("abonnes")
    if nom.startswith("tiktok"):
        return {v["id"]: (v.get("title") or "", int(v.get("view_count") or 0)) for v in d.get("videos", [])}, d.get("compte", {}).get("follower_count")
    cle = {"instagram": "views", "instagram-en": "views", "threads": "views", "facebook": "blue_reels_play_count"}[nom]
    txt = {"facebook": "description", "threads": "text"}.get(nom, "caption")
    return {p["id"]: ((p.get(txt) or "")[:60], int((p.get("insights") or {}).get(cle) or 0)) for p in d.get("publications", [])}, d.get("abonnes")


def main():
    lignes, total, tops = [], 0, []
    for nom in ["youtube", "tiktok-en", "tiktok", "instagram-en", "instagram", "facebook", "threads"]:
        maint = lire(nom)
        if not maint:
            if os.path.exists(os.path.join(ROOT, f"stats/{nom}.json")): lignes.append(f"| {nom} | indisponible | | |")
            continue
        vn, an = videos(nom, maint)
        vv, aa = videos(nom, lire(nom, avant=True))
        if not vv:
            lignes.append(f"| {nom} | {sum(v for _, v in vn.values())} (total, pas de relevé d'il y a {H} h) | {an} | |"); continue
        delta = {k: v - vv.get(k, ("", 0))[1] for k, (_, v) in vn.items()}
        d = sum(x for x in delta.values() if x > 0); total += d
        try: da = int(an) - int(aa)
        except Exception: da = "?"
        lignes.append(f"| {nom} | +{d} | {an} ({'+' if isinstance(da, int) and da >= 0 else ''}{da}) | {len(vn)} |")
        tops += [(x, nom, vn[k][0]) for k, x in delta.items() if x > 0]
    print(f"Vues sur {H} h (relevés stats/, différence avec le relevé d'il y a ≥ {H} h)\n")
    print("| Réseau | Vues | Abonnés (variation) | Vidéos suivies |\n|---|---|---|---|")
    print("\n".join(lignes))
    print(f"\nTotal : +{total} vues.")
    print("\nMeilleures vidéos (vues gagnées) :")
    for x, nom, t in sorted(tops, reverse=True)[:5]:
        print(f"- +{x} · {nom} · {t[:70]}")


CATEGORIES = {"quiz_legal": "enigme", "pigeon_en": "piege", "pigeon_jour": "piege", "gourmande": "piege",
              "prof_corrige": "prof", "prof_partie": "prof", "analyse_celebre": "analyse"}


def categories(jours=7):
    """Pré-indicateur du Pilote (Simon, 1/11) : vues YouTube à 48 h par catégorie, vidéos EN des `jours` derniers jours.
    Catégorie = etiquettes.categorie du fichier de publication (énigme, tactique, finale, histoire, stratégie, ouverture,
    piège…), sinon déduite du concept. Vidéos de moins de 48 h : comptées à part (vues actuelles, « jeunes »)."""
    import datetime as dt, glob
    fich = {}
    chemins = glob.glob(os.path.join(ROOT, "publications/youtube/faites/*.json")) + glob.glob(os.path.join(ROOT, "publications/youtube/*.json"))
    textes = []
    for f in chemins:
        try: textes.append(open(f, encoding="utf-8").read())
        except Exception: pass
    if not chemins:   # checkout partiel (workflow « Résumé chiffres » : stats + outils seulement) : lecture dans git
        ls = subprocess.run(["git", "-C", ROOT, "ls-tree", "-r", "--name-only", "HEAD", "publications/youtube"],
                            capture_output=True, text=True).stdout.split()
        for f in ls:
            if f.endswith(".json"):
                textes.append(subprocess.run(["git", "-C", ROOT, "show", f"HEAD:{f}"], capture_output=True, text=True).stdout)
    for t in textes:
        try: d = json.loads(t)
        except Exception: continue
        cat = (d.get("etiquettes") or {}).get("categorie") or CATEGORIES.get(d.get("concept", ""), d.get("concept") or "?")
        fich[(d.get("titre") or "")[:100]] = cat
    maint = lire("youtube")
    if not maint: return
    now = dt.datetime.now(dt.timezone.utc)
    vids = {k: v for k, v in maint.get("videos", {}).items() if "#echecs" not in v.get("titre", "")
            and now - dt.datetime.fromisoformat(v["publiee"].replace("Z", "+00:00")) < dt.timedelta(days=jours)}
    if not vids: return
    log = subprocess.run(["git", "-C", ROOT, "log", "--format=%H %ct", f"--since={jours + 3} days ago", "--", "stats/youtube.json"],
                         capture_output=True, text=True).stdout.split()
    snaps, dernier = [], 0
    for h, t in sorted(zip(log[::2], map(int, log[1::2])), key=lambda x: x[1]):
        if t - dernier < 3 * 3600: continue
        o = subprocess.run(["git", "-C", ROOT, "show", f"{h}:stats/youtube.json"], capture_output=True, text=True)
        try: snaps.append((t, json.loads(o.stdout).get("videos", {}))); dernier = t
        except Exception: pass
    par, jeunes = {}, {}
    for k, v in vids.items():
        cat = fich.get(v.get("titre", "")[:100], "?")
        pub = dt.datetime.fromisoformat(v["publiee"].replace("Z", "+00:00")).timestamp()
        a48 = next((s[k]["vues"] for t, s in snaps if t >= pub + 48 * 3600 and k in s), None)
        if a48 is None and now.timestamp() - pub >= 48 * 3600: a48 = int(v.get("vues") or 0)
        if a48 is None: jeunes.setdefault(cat, []).append(int(v.get("vues") or 0))
        else: par.setdefault(cat, []).append(a48)
    tout = [x for l in par.values() for x in l]
    if not tout: return
    moy = sum(tout) / len(tout); med = sorted(tout)[len(tout) // 2]
    print(f"\nPar catégorie (YouTube EN, {jours} derniers jours, vues à 48 h ; moyenne {moy:.0f}, médiane {med} sur {len(tout)} vidéos ; règle 17 = moyenne) :")
    print("| Catégorie | Vidéos | Moyenne à 48 h | % de la moyenne | Jeunes (< 48 h, vues actuelles) |\n|---|---|---|---|---|")
    for cat in sorted(set(par) | set(jeunes), key=lambda c: -(sum(par.get(c, [0])) / max(len(par.get(c, [])), 1))):
        l = par.get(cat, []); m = sum(l) / len(l) if l else 0
        alerte = " ⚠ < 50 %" if l and m < moy / 2 else ""
        print(f"| {cat} | {len(l)} | {m:.0f} | {100 * m / moy:.0f} %{alerte} | {', '.join(map(str, jeunes.get(cat, []))) or '–'} |")


def j0_j1(jours=10):
    """Tableau J0/J1 (marketing/suivi-j0-j1.md, intégré le 13/11) : vues YouTube des 24 premières heures (J0), des 24 suivantes (J1),
    ratio J1/J0 et total, par vidéo des `jours` derniers jours. Vues interpolées entre deux relevés git de stats/youtube.json ; manque = n/a."""
    import datetime as dt
    maint = lire("youtube")
    if not maint: return
    log = subprocess.run(["git", "-C", ROOT, "log", "--format=%H %ct", f"--since={jours + 3} days ago", "--", "stats/youtube.json"],
                         capture_output=True, text=True).stdout.split()
    snaps, dernier = [], 0
    for h, t in sorted(zip(log[::2], map(int, log[1::2])), key=lambda x: x[1]):
        if t - dernier < 2.5 * 3600: continue
        o = subprocess.run(["git", "-C", ROOT, "show", f"{h}:stats/youtube.json"], capture_output=True, text=True)
        try: snaps.append((t, json.loads(o.stdout).get("videos", {}))); dernier = t
        except Exception: pass
    def at(k, t):
        prev = None
        for T, s in snaps:
            if k not in s: continue
            v = int(s[k].get("vues") or 0)
            if T >= t:
                if prev is None: return None
                T0, v0 = prev; return v0 + (v - v0) * (t - T0) / max(T - T0, 1)
            prev = (T, v)
        return None
    now = dt.datetime.now(dt.timezone.utc).timestamp(); rows = []
    for k, v in maint.get("videos", {}).items():
        if not v.get("publiee"): continue
        pub = dt.datetime.fromisoformat(v["publiee"].replace("Z", "+00:00")).timestamp()
        if now - pub > jours * 86400: continue
        a, b = at(k, pub + 86400), at(k, pub + 2 * 86400)
        rows.append((pub, v.get("titre", "")[:50], a, b, int(v.get("vues") or 0)))
    if not rows: return
    f = lambda x: "n/a" if x is None else f"{x:.0f}"
    print(f"\nJ0/J1 (YouTube, {jours} derniers jours ; J0 = vues des 24 premières heures, J1 = des 24 suivantes) :")
    print("| Publiée (UTC) | J0 | J1 | J1/J0 | Total | Titre |\n|---|---|---|---|---|---|")
    for pub, ti, a, b, tot in sorted(rows):
        j1 = None if a is None or b is None else b - a
        r = f"{j1 / a:.2f}" if j1 is not None and a else "–"
        print(f"| {dt.datetime.fromtimestamp(pub, dt.timezone.utc):%d/%m %H:%M} | {f(a)} | {f(j1)} | {r} | {tot} | {ti} |")


if __name__ == "__main__":
    main()
    categories()
    j0_j1()
