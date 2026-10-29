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


if __name__ == "__main__":
    main()
