"""Calage automatique : script à repères + mots horodatés -> spec pour coach.run.
Usage : python3 coach2.py <nom> <mots.txt> <sortie_muette.mp4> <sortie_fx.wav> <tempo>
mots.txt : lignes « début-fin mot » (sortie de faster-whisper).
"""
import sys, re, difflib, unicodedata
import chess
import coach
from scripts_coach import SCRIPTS, PERSO, HOOKS

def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", w)

def tokens(script):
    """Liste de mots du script, avec les repères rattachés au mot qui les suit."""
    out = []; pending = []
    for part in re.split(r"(\[[^\]]*\])", script):
        if part.startswith("["):
            pending.append(part[1:-1].split())
            continue
        for w in part.split():
            out.append({"w": w, "marks": pending}); pending = []
    if pending and out:
        out[-1]["marks_after"] = pending
    return out

def aligner(toks, mots):
    a = [norm(t["w"]) for t in toks]
    b = [norm(m[2]) for m in mots]
    times = [None] * len(toks)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            times[blk.a + k] = (mots[blk.b + k][0], mots[blk.b + k][1])
    # remplissage des mots non reconnus (cases mal transcrites…) par interpolation
    for opcode, i1, i2, j1, j2 in sm.get_opcodes():
        if opcode in ("replace", "delete") and i2 > i1:
            if j2 > j1:
                t0, t1 = mots[j1][0], mots[j2 - 1][1]
            else:
                t0 = mots[j1 - 1][1] if j1 > 0 else 0.0
                t1 = mots[j1][0] if j1 < len(mots) else t0 + 0.3
            n = i2 - i1
            for k in range(n):
                if times[i1 + k] is None:
                    s = t0 + (t1 - t0) * k / n
                    times[i1 + k] = (s, s + (t1 - t0) / n)
    last = 0.0
    for i, t in enumerate(times):
        if t is None:
            times[i] = (last, last + 0.2)
        last = times[i][1]
    return times

def construire(nom, mots):
    """Scripts coach (SCRIPTS) ou PERSO (dict avec cote, script, hook)."""
    opts = {}
    if nom in PERSO:
        opts = PERSO[nom]; cote, script = opts["cote"], opts["script"]
    else:
        cote, script = SCRIPTS[nom]
    toks = tokens(script)
    times = aligner(toks, mots)
    actions = []; hook_end = None
    for t, (s, e) in zip(toks, times):
        for mk in t["marks"]:
            typ = mk[0]
            if typ == "m":
                actions.append((s, "coup", (mk[1], mk[2] if len(mk) > 2 else None)))
            elif typ == "f":
                actions.append((s, "fleches", [(x[:2], x[2:]) for x in mk[1:]]))
            elif typ == "p":  # une position posée sur le premier mot vaut dès l'image 1
                actions.append((0.0 if not actions and s < 0.6 else s - 0.05, "position", mk[1:]))
            elif typ == "s":   # autocollant : genre case durée [texte]
                actions.append((s, "sticker", tuple(mk[1:])))
            elif typ == "z":   # zoom : case(s) facteur durée
                actions.append((s, "zoom", (mk[1], float(mk[2]), float(mk[3]))))
            elif typ == "x":   # bruitage
                actions.append((s, "son", mk[1]))
            elif typ == "h":   # fin du hook
                hook_end = s
    # sous-titres : groupes de 2 à 5 mots, coupés sur la ponctuation
    caps = []; cur = []; t0 = None
    for t, (s, e) in zip(toks, times):
        if not cur: t0 = s
        cur.append(t["w"])
        w = t["w"]; fin_phrase = w[-1] in ".!?…"; virgule = w[-1] in ",:;"
        if fin_phrase or (virgule and len(cur) >= 3) or len(cur) >= 6:
            caps.append((t0, e, " ".join(cur))); cur = []
    if cur:
        caps.append((t0, times[-1][1], " ".join(cur)))
    caps = [(a, b, re.sub(r"[,:]$", "", c)) for a, b, c in caps]
    duree = times[-1][1] + 0.3
    spec = {"duree": duree, "captions": caps, "actions": actions, "noirs": cote == "noirs"}
    if not opts and nom in HOOKS:  # coach : bandeau jusqu'à la fin de la première phrase
        fin = next((e for t, (s, e) in zip(toks, times) if t["w"][-1] in ".!?…"), 2.0)
        spec["hook"] = (HOOKS[nom], fin)
    if opts:
        # mot géant : chaque mot du script, en majuscules, sans ponctuation (« ? » et « ! » gardés)
        spec["mots"] = [(s, e, re.sub(r"[.,:;…]", "", t["w"]).upper()) for t, (s, e) in zip(toks, times)
                        if re.search(r"\w", t["w"])]  # « ? » ou « ! » isolés ne deviennent pas un mot géant
        spec["sous_titres"] = opts.get("sous_titres", "mot")
        spec["musique"] = opts.get("musique", 0.0)          # PERSO : pas de musique sous la voix
        spec["fx"] = opts.get("fx", {"gaffe": "bwomp", "brillant": "impact"})
        if opts.get("hook"):
            spec["hook"] = (opts["hook"], hook_end if hook_end is not None else 2.0)
    return spec

if __name__ == "__main__":
    nom, fmots, out_v, out_a, tempo = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5])
    mots = []
    for line in open(fmots, encoding="utf-8"):
        line = line.strip()
        if not line: continue
        tt, w = line.split(" ", 1)
        a, b = tt.split("-"); mots.append((float(a), float(b), w))
    spec = construire(nom, mots)
    coach.FLIP = spec["noirs"]
    coach.BG = coach.fond()
    d = coach.run(spec, out_v, out_a, tempo)
    print(nom, "durée", round(d, 1), "actions", len(spec["actions"]), "sous-titres", len(spec["captions"]))
