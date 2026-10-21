"""Vidéos BlunderCheck : échiquier en gros plan, voix off, sous-titres calés (format coach, PERSO, BOUCLE).
Rend la vidéo muette (images) + une piste de bruitages ; la voix est ajoutée au montage.
Style « Club » v2 (21/10, 22 h 30) : pièces vectorielles, plateau aux coins arrondis avec ombre, fond dégradé,
zoom rendu en haute définition (pas d'agrandissement flou). Nécessite : pip install cairosvg.
"""
import sys, subprocess, math, io
import chess, chess.svg
from PIL import Image, ImageDraw, ImageFilter
import gen, sons
from gen import font, F_BLACK, F_BOLD, IVOIRE, LAITON, FORET

W, H, FPS = 1080, 1920, 30
SQ = 129                      # case de base (plateau 1032 px)
BX, BY = 24, 500              # coin haut gauche du plateau dans l'image
CASE_C = (239, 234, 220)      # ivoire
CASE_F = (112, 146, 108)      # vert sauge
SURL = (246, 214, 92)         # dernier coup
RAYON = 26                    # coins arrondis du plateau

FLIP = False
GROW = 0.16  # grossissement max de la pièce pendant son déplacement

# ---------- pièces vectorielles (jeu « cburnett », licence libre), mises en cache par taille ----------
_SPR = {}
def sprite(pt, color, size):
    key = (pt, color, size)
    if key not in _SPR:
        import cairosvg
        svg = chess.svg.piece(chess.Piece(pt, color), size=size)
        im = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=size, output_height=size))).convert("RGBA")
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.paste((0, 0, 0, 70), (0, 0), im.split()[3])
        sh = sh.filter(ImageFilter.GaussianBlur(max(2, size // 40)))
        out = Image.new("RGBA", im.size, (0, 0, 0, 0)); out.alpha_composite(sh, (size // 45, size // 28)); out.alpha_composite(im)
        _SPR[key] = out
    return _SPR[key]

def bxy(sq, s):
    """Coin haut gauche d'une case, en coordonnées du plateau (case de s pixels)."""
    f, r = chess.square_file(sq), chess.square_rank(sq)
    if FLIP: f, r = 7 - f, 7 - r
    return f * s, (7 - r) * s

def xy(sq):
    x, y = bxy(sq, SQ); return BX + x, BY + y

_DAMIER = {}
def damier(s):
    if s not in _DAMIER:
        im = Image.new("RGBA", (8 * s, 8 * s), CASE_C + (255,)); d = ImageDraw.Draw(im)
        for q in chess.SQUARES:
            if (chess.square_file(q) + chess.square_rank(q)) % 2 == 0:
                x, y = bxy(q, s); d.rectangle([x, y, x + s - 1, y + s - 1], fill=CASE_F)
        fc = font(F_BOLD, max(14, s // 6))
        files = "hgfedcba" if FLIP else "abcdefgh"
        for i in range(8):  # coordonnées discrètes dans les coins
            d.text((i * s + s - s // 7 - 4, 8 * s - s // 5 - 2), files[i], font=fc, fill=CASE_C if i % 2 == 0 else CASE_F)
            d.text((s // 18, i * s + s // 30), str(i + 1) if FLIP else str(8 - i), font=fc, fill=CASE_C if i % 2 == 1 else CASE_F)
        _DAMIER[s] = im
    return _DAMIER[s]

def fond():
    _DAMIER.clear()
    """Fond dégradé vert forêt + ombre du plateau + signature."""
    g = Image.new("RGB", (1, 256))
    for i in range(256):
        k = i / 255; g.putpixel((0, i), (int(14 + 12 * k), int(30 + 16 * k), int(24 + 12 * k)))
    im = g.resize((W, H)).convert("RGBA")
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle(
        [BX + 4, BY + 18, BX + 8 * SQ + 4, BY + 8 * SQ + 22], radius=RAYON, fill=(0, 0, 0, 150))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    d = ImageDraw.Draw(im); fw = font(F_BOLD, 36); t = "blundercheck.app"
    d.text(((W - d.textlength(t, font=fw)) / 2, BY + 8 * SQ + 44), t, font=fw, fill=LAITON)
    return im

BG = fond()
_MASK = {}
def masque(n):
    if n not in _MASK:
        m = Image.new("L", (n, n), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, n - 1, n - 1], radius=int(RAYON * n / (8 * SQ)), fill=255)
        _MASK[n] = m
    return _MASK[n]

ICON = {"livre": ("≡", (150, 110, 70)), "bizarre": ("!?", (60, 160, 190)), "erreur": ("?", (230, 140, 40)),
        "gaffe": ("??", (214, 48, 49)), "mat": ("#", (55, 55, 60)), "meilleur": ("★", (110, 175, 70)),
        "bon": ("!", (60, 130, 215)), "brillant": ("!!", (30, 175, 120))}  # règle 11 : ! bleu, !! vert

def icone(im, sq, kind, s):
    lab, col = ICON[kind]; k = s / 135
    d = ImageDraw.Draw(im)
    x, y = bxy(sq, s); r = 32 * k; cx, cy = x + s - 10 * k, y + 10 * k
    cx = min(cx, 8 * s - r - 2); cy = max(cy, r + 2)
    d.ellipse([cx - r + 2 * k, cy - r + 5 * k, cx + r + 2 * k, cy + r + 5 * k], fill=(0, 0, 0, 90))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col, outline=(255, 255, 255), width=max(2, int(4 * k)))
    f = font(F_BLACK, int((36 if len(lab) < 2 else 30) * k))
    bb = d.textbbox((0, 0), lab, font=f)
    d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), lab, font=f, fill=(255, 255, 255))

def fleche(im, a, b, s, col=(255, 170, 30)):
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ax, ay = bxy(a, s); bx, by = bxy(b, s); ax += s / 2; ay += s / 2; bx += s / 2; by += s / 2
    ang = math.atan2(by - ay, bx - ax); hl = s * 0.42; hw = s * 0.32
    ex, ey = bx - math.cos(ang) * hl, by - math.sin(ang) * hl
    d.line([(ax, ay), (ex, ey)], fill=col + (215,), width=int(s * 0.2))
    d.ellipse([ax - s * 0.1, ay - s * 0.1, ax + s * 0.1, ay + s * 0.1], fill=col + (215,))
    p2 = (ex + math.cos(ang + math.pi / 2) * hw, ey + math.sin(ang + math.pi / 2) * hw)
    p3 = (ex + math.cos(ang - math.pi / 2) * hw, ey + math.sin(ang - math.pi / 2) * hw)
    d.polygon([(bx - math.cos(ang) * s * 0.08, by - math.sin(ang) * s * 0.08), p2, p3], fill=col + (215,))
    im.alpha_composite(lay)

def sous_titre(im, txt):
    if not txt: return
    d = ImageDraw.Draw(im)
    f = font(F_BLACK, 84)
    lines = gen.wrap(d, txt, f, W - 100)
    y = 330 - len(lines) * 48
    for ln in lines:
        tw = d.textlength(ln, font=f)
        d.text(((W - tw) / 2, y), ln, font=f, fill=(255, 255, 255), stroke_width=8, stroke_fill=(0, 0, 0))
        y += 96

# ---------- autocollants des personnages (dessinés, réutilisés) ----------
def bonbon(im, sq, age, s):
    x, y = bxy(sq, s); k = s / 135
    p = min(1, age / 0.18); r = 26 * k * p * (1 + 0.15 * math.sin(p * math.pi))
    if r < 2: return
    cx, cy = x + 40 * k, y + s - 38 * k
    d = ImageDraw.Draw(im)
    for sgn in (-1, 1):
        d.polygon([(cx + sgn * r * 0.8, cy), (cx + sgn * r * 1.9, cy - r * 0.75), (cx + sgn * r * 1.9, cy + r * 0.75)],
                  fill=(235, 60, 70), outline=(255, 255, 255))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(235, 60, 70), outline=(255, 255, 255), width=max(2, int(4 * k)))
    for k2 in (-0.45, 0.1, 0.65):
        d.arc([cx - r, cy - r, cx + r, cy + r], int(200 + k2 * 60), int(260 + k2 * 60), fill=(255, 255, 255), width=max(2, int(6 * k)))

def couronne(im, sq, age, s):
    x, y = bxy(sq, s); k = s / 135; g = (0.8 + min(0.6, age * 0.25)) * k
    w = 70 * g; h = 44 * g; cx = x + s / 2; base = y + 0.42 * s  # posée sur la tête de la dame
    d = ImageDraw.Draw(im)
    pts = [(cx - w / 2, base), (cx - w / 2, base - h * 0.55), (cx - w / 4, base - h * 0.2), (cx, base - h),
           (cx + w / 4, base - h * 0.2), (cx + w / 2, base - h * 0.55), (cx + w / 2, base)]
    pts = [(px, max(2, py)) for px, py in pts]
    d.polygon(pts, fill=(240, 196, 60), outline=(40, 30, 10))
    for px, py in (pts[1], pts[3], pts[5]):
        d.ellipse([px - 7 * g, py - 7 * g, px + 7 * g, py + 7 * g], fill=(235, 60, 70), outline=(40, 30, 10))

def etiquette(im, sq, texte, age, s, col=(245, 239, 225), fg=(22, 46, 36)):
    x, y = bxy(sq, s); k = s / 135; e = min(1, age / 0.15)
    if e <= 0: return
    f = font(F_BLACK, int(40 * k * (0.7 + 0.3 * e)))
    d = ImageDraw.Draw(im); tw = d.textlength(texte, font=f)
    cx = min(max(x + s / 2, tw / 2 + 24 * k), 8 * s - tw / 2 - 24 * k)
    top = y - 30 * k if y > 40 * k else y + s - 26 * k
    d.rounded_rectangle([cx - tw / 2 - 18 * k, top, cx + tw / 2 + 18 * k, top + 56 * k], radius=int(28 * k),
                        fill=col, outline=(0, 0, 0), width=max(2, int(4 * k)))
    d.text((cx - tw / 2, top + 5 * k), texte, font=f, fill=fg)

def plateau(b, last, anim, icons, arrows, stickers, t, s):
    """Image du plateau seul (8 s × 8 s), coins arrondis."""
    im = damier(s).copy()
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    for q in (last or []):
        x, y = bxy(q, s); ld.rectangle([x, y, x + s - 1, y + s - 1], fill=SURL + (120,))
    im.alpha_composite(lay)
    if b.is_check():
        x, y = bxy(b.king(b.turn), s)
        lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).ellipse([x + s * 0.05, y + s * 0.05, x + s * 0.95, y + s * 0.95], fill=(235, 40, 40, 200))
        im.alpha_composite(lay.filter(ImageFilter.GaussianBlur(s // 10)))
    hide = anim["hide"] if anim else set()
    for q, p in b.piece_map().items():
        if q in hide: continue
        x, y = bxy(q, s); im.alpha_composite(sprite(p.piece_type, p.color, s), (x, y))
    for t0, t1, kind, sq, lab in stickers:
        if t0 <= t < t1 and kind == "bonbon": bonbon(im, chess.parse_square(sq), t - t0, s)
    if anim:
        u = anim["t"]; e = u * u * (3 - 2 * u)
        g = 1 + GROW * math.sin(math.pi * min(1, u))  # règle 13 : la pièce jouée grossit pendant le trajet
        for pt, c, a, bb in anim["movers"]:
            ax, ay = bxy(a, s); bx2, by2 = bxy(bb, s)
            n = int(s * g); spr = sprite(pt, c, s) if n == s else sprite(pt, c, s).resize((n, n), Image.LANCZOS)
            off = (s - n) // 2
            im.alpha_composite(spr, (int(ax + (bx2 - ax) * e) + off, int(ay + (by2 - ay) * e) + off))
    for a, bb in arrows: fleche(im, a, bb, s)
    for q, kind in icons: icone(im, q, kind, s)
    for t0, t1, kind, sq, lab in stickers:
        if t0 <= t < t1:
            q = chess.parse_square(sq)
            if kind == "couronne": couronne(im, q, t - t0, s)
            elif kind == "tag": etiquette(im, q, lab.replace("_", " "), t - t0, s)
    out = Image.new("RGBA", im.size, (0, 0, 0, 0)); out.paste(im, (0, 0), masque(im.width))
    return out

def image(b, last, anim=None, icons=(), arrows=(), stickers=(), t=0.0, zoom=(1.0, None)):
    """Image complète : fond + plateau (zoomé en haute définition si besoin)."""
    frame = BG.copy()
    z, c = zoom
    if z <= 1.001 or c is None:
        frame.alpha_composite(plateau(b, last, anim, icons, arrows, stickers, t, SQ), (BX, BY))
        return frame
    s2 = int(round(SQ * z)); big = plateau(b, last, anim, icons, arrows, stickers, t, s2)
    n = 8 * SQ; cx, cy = c[0] * z, c[1] * z
    x0 = min(max(cx - n / 2, 0), 8 * s2 - n); y0 = min(max(cy - n / 2, 0), 8 * s2 - n)
    crop = big.crop((int(x0), int(y0), int(x0) + n, int(y0) + n))
    out = Image.new("RGBA", (n, n), (0, 0, 0, 0)); out.paste(crop, (0, 0), masque(n))
    frame.alpha_composite(out, (BX, BY))
    return frame

# compatibilité avec l'ancien appel render(b, last, anim, icons, arrows, txt)
def render(b, last, anim=None, icons=(), arrows=(), txt=""):
    im = image(b, last, anim, icons, arrows); sous_titre(im, txt); return im

# ---------- surcouches : hook fixe, zoom, mot géant, tampon ----------
def centre(spec_sq):
    """'e4' ou 'g4d1' (milieu des deux cases) -> centre en pixels du plateau (case SQ)."""
    sqs = [chess.parse_square(spec_sq[k:k + 2]) for k in range(0, len(spec_sq), 2)]
    pts = [bxy(q, SQ) for q in sqs]
    return sum(p[0] for p in pts) / len(pts) + SQ / 2, sum(p[1] for p in pts) / len(pts) + SQ / 2

def ease(x): x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

def zoom_factor(t, zooms):
    """zooms : [(t0, case, facteur, durée)] -> (facteur, centre). Entrée 0,3 s, sortie 0,35 s."""
    for t0, sq, fz, d in zooms:
        if t0 <= t < t0 + d + 0.35:
            if t < t0 + 0.3: k = ease((t - t0) / 0.3)
            elif t < t0 + d: k = 1.0
            else: k = 1 - ease((t - t0 - d) / 0.35)
            return 1 + (fz - 1) * k, centre(sq)
    return 1.0, None

def bandeau_hook(im, texte, alpha=1.0):
    """Règle 2 : hook affiché en entier dès l'image 1 (bandeau fixe en haut). « | » force un retour à la ligne."""
    if alpha <= 0: return
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    def lignes(f, mw): return [ln for part in texte.split("|") for ln in gen.wrap(d, part.strip(), f, mw)]
    parts = texte.split("|"); size = 82
    while size > 60 and any(d.textlength(p.strip(), font=font(F_BLACK, size)) > W - 150 for p in parts):
        size -= 4  # chaque morceau « | » tient sur une ligne si possible
    f = font(F_BLACK, size); lines = lignes(f, W - 150)
    lh = f.size + 14; hb = len(lines) * lh + 54; top = max(40, 280 - hb // 2)
    d.rounded_rectangle([40, top + 10, W - 40, top + hb + 10], radius=36, fill=(0, 0, 0, int(110 * alpha)))
    d.rounded_rectangle([40, top, W - 40, top + hb], radius=36, fill=LAITON + (int(252 * alpha),))
    yy = top + 24
    for ln in lines:
        tw = d.textlength(ln, font=f)
        d.text(((W - tw) / 2, yy), ln, font=f, fill=(16, 28, 22, int(255 * alpha)))
        yy += lh
    im.alpha_composite(lay.filter(ImageFilter.SMOOTH) if False else lay)

def mot_geant(im, mot, age):
    """Règle 16 (PERSO) : un seul mot géant au centre de l'échiquier."""
    if not mot: return
    d = ImageDraw.Draw(im); size = 150
    f = font(F_BLACK, size)
    while d.textlength(mot, font=f) > W - 80 and size > 70:
        size -= 10; f = font(F_BLACK, size)
    pop = 1 + 0.12 * (1 - ease(age / 0.09))
    if pop > 1.01: f = font(F_BLACK, int(size * pop))
    tw = d.textlength(mot, font=f); cy = BY + 4 * SQ
    d.text(((W - tw) / 2, cy - f.size * 0.62), mot, font=f, fill=(255, 255, 255), stroke_width=12, stroke_fill=(0, 0, 0))

def tampon(im, texte, col, age, sous=""):
    """Grand badge au centre (ex. « !! » vert de la révélation)."""
    k = ease(age / 0.16); s = 0.6 + 0.4 * k + 0.12 * math.sin(min(1, age / 0.3) * math.pi)
    if k <= 0: return
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    r = int(150 * s); cx, cy = W // 2, BY + 4 * SQ - 40
    d.ellipse([cx - r + 6, cy - r + 14, cx + r + 6, cy + r + 14], fill=(0, 0, 0, 110))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (245,), outline=(255, 255, 255, 255), width=10)
    f = font(F_BLACK, int(170 * s)); bb = d.textbbox((0, 0), texte, font=f)
    d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), texte, font=f, fill=(255, 255, 255, 255))
    if sous:
        f2 = font(F_BLACK, 74); tw = d.textlength(sous, font=f2)
        d.text(((W - tw) / 2, cy + r + 24), sous, font=f2, fill=(255, 255, 255, 255), stroke_width=8, stroke_fill=(0, 0, 0, 255))
    im.alpha_composite(lay)

def decompte(im, n, age):
    """Chiffre du décompte, entre le bandeau et l'échiquier (ne cache pas la position à chercher)."""
    d = ImageDraw.Draw(im); s = 1 + 0.25 * (1 - ease(age / 0.15)); r = int(62 * s); cx, cy = W // 2, BY - 92
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(245, 239, 225), outline=(0, 0, 0), width=6)
    f = font(F_BLACK, int(88 * s)); bb = d.textbbox((0, 0), n, font=f)
    d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), n, font=f, fill=(16, 28, 22))

FX_BADGE = {"gaffe": "bwomp", "mat": "impact", "meilleur": "chime"}

def run(spec, out_video, out_wav, tempo=1.0):
    """spec : 'duree', 'actions' [(t, type, données)], 'captions' [(t0, t1, texte)] en secondes de voix originale.
    Options (toutes facultatives) :
      hook (texte, secondes)       bandeau fixe en haut dès l'image 1 (au moins 2 s) ; sous-titres masqués pendant
      sous_titres 'phrase' | 'mot' 'mot' = un mot géant au centre (format PERSO), à partir de spec['mots']
      fx {badge: son}              bruitage par badge (défaut FX_BADGE), 4 effets marqués maximum
      musique float                niveau de la musique synthétique (0 par défaut : abandonnée le 21/10)
      boucle True                  fondu final vers l'image 1 (raccord) ; bruitages seuls, le son tendance s'ajoute dans TikTok
    Actions en plus de coup/fleches/position/son :
      zoom (case|caseCase, facteur, durée)  ·  sticker (genre, case, durée[, texte])  ·  tampon (texte, couleur, durée, sous-texte)
    """
    k = 1 / tempo
    dur = spec["duree"] * k + (0.0 if spec.get("boucle") else 0.6)
    nfr = int(round(dur * FPS))
    caps = [(a * k, b * k, t) for a, b, t in spec["captions"]]
    mots = [(a * k, b * k, w) for a, b, w in spec.get("mots", [])]
    acts = sorted([(t * k, typ, data) for t, typ, data in spec["actions"]], key=lambda x: x[0])
    hook = spec.get("hook"); hook_end = max(2.0, hook[1] * k) if hook else 0
    if hook: caps = [c for c in caps if c[0] >= hook_end - 0.2]
    fxmap = spec.get("fx", FX_BADGE)
    b = chess.Board(spec["fen"]) if spec.get("fen") else chess.Board()
    last = None; icons = []; arrows = []; events = []
    zooms = []; stickers = []; stamps = []; quizs = []
    # règle 3 : image 1 = position finale (teaser) sous le hook, puis on rembobine
    teaser = None
    if spec.get("teaser_board") is not None:
        tb = spec["teaser_board"]; mv_ = tb.peek()
        teaser = (tb, [mv_.from_square, mv_.to_square], [(mv_.to_square, "gaffe")])
    elif spec.get("teaser"):
        tb = chess.Board()
        for s_ in spec["teaser"].split(): tb.push_san(s_)
        mv_ = tb.peek(); teaser = (tb, [mv_.from_square, mv_.to_square],
                                   [(mv_.to_square, "mat" if tb.is_checkmate() else "brillant")])
    teaser_end = hook_end if teaser else 0
    if teaser: events.append((teaser_end, "rewind"))
    question = spec.get("question"); q_start = dur - 3.2 if question else dur + 1
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                          "-pix_fmt", "yuv420p", out_video], stdin=subprocess.PIPE)
    ai = 0; anim = None; pending = None
    SLIDE = spec.get("slide", 0.28)
    first = None; fade = 0.35 if spec.get("boucle") else 0
    def badge_fx(at, badge):
        if badge and badge in fxmap: events.append((at, fxmap[badge]))
    for f in range(nfr):
        t = f / FPS
        while ai < len(acts) and acts[ai][0] <= t:
            ta, typ, data = acts[ai]; ai += 1
            if typ in ("coup", "position") and anim:
                mv0, badge0, cap0 = pending
                b.push(mv0); last = [mv0.from_square, mv0.to_square]
                events.append((t, "capture" if cap0 else "move"))
                if badge0: icons = [(mv0.to_square, badge0)]
                anim = None
            if typ == "coup":
                san, badge = data
                mv = b.parse_san(san)
                pc = b.piece_at(mv.from_square)
                pt = mv.promotion or pc.piece_type  # une promotion glisse déjà sous sa nouvelle forme
                movers = [(pt, pc.color, mv.from_square, mv.to_square)]
                hide = {mv.from_square, mv.to_square}
                if b.is_castling(mv):
                    rf, rt = (chess.H1, chess.F1) if mv.to_square == chess.G1 else (chess.A1, chess.D1)
                    if b.turn == chess.BLACK: rf, rt = rf + 56, rt + 56
                    movers.append((chess.ROOK, b.turn, rf, rt)); hide |= {rf, rt}
                cap = b.is_capture(mv)
                anim = {"movers": movers, "hide": hide, "t0": t}; pending = (mv, badge, cap)
                icons = []; arrows = []
            elif typ == "fleches":
                arrows = [(chess.parse_square(a), chess.parse_square(c)) for a, c in data]
            elif typ == "position":
                if data and data[0].startswith("fen:"):
                    b = chess.Board(data[0][4:].replace("_", " ")); rest = data[1:]
                else:
                    b = chess.Board(); rest = data
                for s in rest: b.push_san(s)
                last = [b.peek().from_square, b.peek().to_square] if b.move_stack else None
                icons = []; arrows = []; stickers = []; events.append((t, "rewind"))
            elif typ == "zoom":
                sq, fz, d = data; zooms.append((t, sq, float(fz), float(d) * k))
            elif typ == "sticker":
                stickers.append((t, t + float(data[2]) * k, data[0], data[1], data[3] if len(data) > 3 else ""))
            elif typ == "tampon":
                stamps.append((t, t + float(data[2]) * k, data[0], data[1], data[3] if len(data) > 3 else ""))
            elif typ == "quiz":  # pause « trouve le coup » : décompte 3-2-1
                d_, txt_ = data; quizs.append((t, t + float(d_) * k, txt_))
                for i_ in range(int(float(d_) * k)): events.append((t + i_, "tick_hi" if i_ == 0 else "tick"))
            elif typ == "son":
                events.append((t, data))
        zf = zoom_factor(t, zooms)
        if teaser and t < teaser_end:  # image 1 : la fin de l'histoire
            frame = image(teaser[0], teaser[1], None, teaser[2], (), (), t, (1.0, None))
            bandeau_hook(frame, hook[0])
            p.stdin.write(frame.convert("RGB").tobytes())
            if first is None: first = frame.copy()
            continue
        if anim:
            prog = (t - anim["t0"]) / SLIDE
            if prog >= 1:
                mv, badge, cap = pending
                b.push(mv); last = [mv.from_square, mv.to_square]
                at = anim["t0"] + SLIDE
                events.append((at, "check" if b.is_check() and not b.is_checkmate() else ("capture" if cap else "move")))
                if badge:
                    icons = [(mv.to_square, badge)]; badge_fx(at, badge)
                    if badge in ("mat", "brillant", "gaffe") and not any(abs(z0 - at) < 1 for z0, *_ in zooms):
                        fz, dz = (1.35, 1.1) if badge == "gaffe" else (1.5, 1.8)  # règle 12 : zoom au payoff (et sur la gaffe, pour le rythme)
                        zooms.append((at, chess.square_name(mv.to_square), fz, dz))
                anim = None
                frame = image(b, last, None, icons, arrows, stickers, t, zf)
            else:
                frame = image(b, last, {"movers": anim["movers"], "hide": anim["hide"], "t": max(0, prog)}, icons, arrows, stickers, t, zf)
        else:
            frame = image(b, last, None, icons, arrows, stickers, t, zf)
        for t0, t1, txt, col, sous in stamps:
            if t0 <= t < t1: tampon(frame, txt, tuple(col), t - t0, sous)
        qz = next(((a, b2, tx) for a, b2, tx in quizs if a <= t < b2), None)
        if qz:  # décompte au centre + consigne en haut
            bandeau_hook(frame, qz[2])
            decompte(frame, str(max(1, math.ceil(qz[1] - t))), (t - qz[0]) % 1.0)
        if t >= q_start:
            bandeau_hook(frame, question, min(1.0, (t - q_start) / 0.25))
        if qz or t >= q_start: pass
        elif hook and t < hook_end + 0.25:
            bandeau_hook(frame, hook[0], 1.0 if t < hook_end else 1 - (t - hook_end) / 0.25)
        if qz or t >= q_start: pass  # pas de sous-titres sous un bandeau
        elif spec.get("sous_titres") == "mot":
            cur = None
            for i2, (a, z2, w) in enumerate(mots):
                nxt = mots[i2 + 1][0] if i2 + 1 < len(mots) else z2 + 0.4
                if a <= t < min(nxt, z2 + 0.6): cur = (w, t - a)
            if cur and t >= hook_end - 0.2: mot_geant(frame, cur[0], cur[1])
        else:
            txt = next((c2 for a, z2, c2 in caps if a <= t < z2 + 0.15), "")
            if txt: sous_titre(frame, txt)
        if first is None: first = frame.copy()
        if fade and t > dur - fade:  # raccord de boucle : on revient sur l'image 1
            frame = Image.blend(frame, first, ease((t - (dur - fade)) / fade))
        p.stdin.write(frame.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    import numpy as np
    from scipy.io import wavfile
    n = int(dur * sons.SR)
    fx = np.zeros(n + 3 * sons.SR)
    for at, kind in events:
        s = sons.FX[kind](); i0 = int(at * sons.SR); fx[i0:i0 + len(s)] += s
    fx = fx[:n]
    lvl = spec.get("musique", 0.0)  # musique synthétique abandonnée le 21/10 (trop mauvaise)
    m = sons.music(dur) * lvl if lvl else np.zeros(n)
    y = np.tanh((fx * 0.55 + m) * 1.1) * 0.9
    fade_n = int(0.5 * sons.SR); y[-fade_n:] *= np.linspace(1, 0, fade_n)
    wavfile.write(out_wav, sons.SR, (np.stack([y, y], 1) * 32767).astype(np.int16))
    return dur

BLACKBURNE = {
    "duree": 46.1,
    "captions": [
        (0.0, 1.8, "Après e4 e5,"), (2.28, 4.76, "cavalier f3, cavalier c6,"), (5.24, 6.4, "tu joues fou c4 ?"),
        (6.94, 7.98, "Attention à ce coup :"), (8.62, 9.5, "cavalier d4."), (9.9, 10.62, "Ça a l'air nul."),
        (11.18, 12.78, "Le pion e5 a l'air gratuit…"), (13.32, 15.28, "Surtout, ne le prends pas !"),
        (15.82, 18.0, "Si tu joues cavalier prend e5,"), (18.48, 20.56, "la dame noire sort en g5."),
        (21.1, 22.44, "Elle attaque ton cavalier"), (22.44, 24.02, "et ton pion g2."),
        (24.62, 25.8, "Tu prends f7 ?"), (25.8, 27.38, "Dame prend g2."), (27.8, 28.52, "Tour f1."),
        (29.12, 31.26, "Dame prend e4, échec."), (31.7, 32.68, "Fou e2…"), (32.68, 34.38, "et cavalier f3."),
        (34.96, 35.7, "MAT."), (36.1, 37.64, "Le bon coup, c'était"), (37.64, 39.08, "cavalier prend d4."),
        (39.74, 41.3, "Tu veux savoir quelles erreurs"), (41.3, 42.2, "te coûtent tes parties ?"),
        (42.78, 44.34, "Analyse-les gratuitement"), (44.34, 46.1, "sur BlunderCheck."),
    ],
    "actions": [
        (0.44, "coup", ("e4", "livre")), (1.32, "coup", ("e5", "livre")), (2.8, "coup", ("Nf3", "livre")),
        (4.24, "coup", ("Nc6", "livre")), (5.92, "coup", ("Bc4", "livre")), (9.06, "coup", ("Nd4", "bizarre")),
        (11.4, "fleches", [("f3", "e5")]),
        (17.26, "coup", ("Nxe5", "erreur")), (19.92, "coup", ("Qg5", None)),
        (21.4, "fleches", [("g5", "e5"), ("g5", "g2")]),
        (25.12, "coup", ("Nxf7", "gaffe")), (26.72, "coup", ("Qxg2", None)), (28.06, "coup", ("Rf1", None)),
        (29.74, "coup", ("Qxe4+", None)), (32.1, "coup", ("Be2", None)), (33.98, "coup", ("Nf3#", "mat")),
        (36.1, "position", ["e4", "e5", "Nf3", "Nc6", "Bc4", "Nd4"]),
        (37.0, "fleches", [("f3", "d4")]), (38.4, "coup", ("Nxd4", "meilleur")),
    ],
}

if __name__ == "__main__":
    d = run(BLACKBURNE, sys.argv[1], sys.argv[2], float(sys.argv[3]))
    print("durée", round(d, 1))
