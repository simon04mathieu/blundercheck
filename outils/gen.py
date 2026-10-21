"""Générateur de vidéos TikTok BlunderCheck (pièges d'ouverture).
Usage : python3 gen.py <nom_du_piege> <sortie.mp4>
"""
import sys, subprocess, math
import chess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
# Palette « Club »
FORET = (22, 46, 36)
FORET2 = (30, 61, 48)
IVOIRE = (245, 239, 225)
LAITON = (201, 162, 75)
CASE_C = (233, 224, 200)
CASE_F = (96, 128, 98)
NOIR = (24, 28, 26)
ROUGE = (200, 52, 44)
ORANGE = (222, 132, 40)
VERT_OK = (64, 150, 92)

F_BLACK = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
F_BOLD = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
F_SEMI = "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf"
F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_PIECE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(p, s): return ImageFont.truetype(p, s)

SQ = 112
# intensité des effets (réglable par format)
SHAKE = {"mat": 26, "gaffe": 14}
REDFLASH = 1.0
FIN_SECS = 2.6
BX, BY = (W - 8 * SQ) // 2, 600   # plateau 896 px, de y=600 à 1496

# ---------- sprites ----------
GLYPH = {chess.KING: "♚", chess.QUEEN: "♛", chess.ROOK: "♜",
         chess.BISHOP: "♝", chess.KNIGHT: "♞", chess.PAWN: "♟"}

def make_sprite(pt, color):
    im = Image.new("RGBA", (SQ, SQ), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = font(F_PIECE, 98)
    g = GLYPH[pt]
    bb = d.textbbox((0, 0), g, font=f)
    x = (SQ - (bb[2] - bb[0])) / 2 - bb[0]
    y = (SQ - (bb[3] - bb[1])) / 2 - bb[1]
    if color == chess.WHITE:
        d.text((x, y), g, font=f, fill=(250, 246, 236), stroke_width=4, stroke_fill=(20, 26, 22))
    else:
        d.text((x, y), g, font=f, fill=(28, 30, 29), stroke_width=3, stroke_fill=(236, 228, 208))
    # ombre légère
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sh.paste((0, 0, 0, 90), (0, 0), im.split()[3])
    sh = sh.filter(ImageFilter.GaussianBlur(3))
    out = Image.new("RGBA", im.size, (0, 0, 0, 0))
    out.alpha_composite(sh, (3, 5))
    out.alpha_composite(im)
    return out

SPRITES = {(pt, c): make_sprite(pt, c) for pt in GLYPH for c in (chess.WHITE, chess.BLACK)}

def sq_xy(sq):
    return BX + chess.square_file(sq) * SQ, BY + (7 - chess.square_rank(sq)) * SQ

def board_bg():
    im = Image.new("RGBA", (W, H), FORET + (255,))
    d = ImageDraw.Draw(im)
    # léger dégradé vertical
    for y in range(H):
        t = y / H
        c = tuple(int(FORET[i] * (1 - t) + FORET2[i] * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    # cadre laiton
    d.rounded_rectangle([BX - 14, BY - 14, BX + 8 * SQ + 14, BY + 8 * SQ + 14], 14, fill=LAITON)
    d.rectangle([BX - 4, BY - 4, BX + 8 * SQ + 4, BY + 8 * SQ + 4], fill=NOIR)
    fc = font(F_BOLD, 22)
    for s in chess.SQUARES:
        x, y = sq_xy(s)
        light = (chess.square_file(s) + chess.square_rank(s)) % 2 == 1
        d.rectangle([x, y, x + SQ - 1, y + SQ - 1], fill=CASE_C if light else CASE_F)
    for i in range(8):
        d.text((BX + i * SQ + SQ - 18, BY + 8 * SQ - 28), "abcdefgh"[i], font=fc,
               fill=CASE_F if i % 2 == 1 else CASE_C)
        d.text((BX + 6, BY + i * SQ + 4), str(8 - i), font=fc,
               fill=CASE_F if i % 2 == 0 else CASE_C)
    # signature discrète sous le plateau
    fw = font(F_SEMI, 34)
    t = "blundercheck.app"
    tw = d.textlength(t, font=fw)
    d.text(((W - tw) / 2, BY + 8 * SQ + 40), t, font=fw, fill=(*LAITON, ))
    return im

BG = board_bg()

def fr(san):
    return san.translate(str.maketrans("KQRBN", "RDTFC"))

# ---------- dessin ----------
def wrap(d, text, f, maxw):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if d.textlength(t, font=f) <= maxw: cur = t
            else:
                if cur: lines.append(cur)
                cur = w_
        lines.append(cur)
    return lines

def draw_text_block(im, text, y0, y1, size=82, color=IVOIRE, accent=None):
    d = ImageDraw.Draw(im)
    f = font(F_BLACK, size)
    lines = wrap(d, text, f, W - 120)
    while len(lines) * size * 1.12 > (y1 - y0) and size > 44:
        size -= 6; f = font(F_BLACK, size); lines = wrap(d, text, f, W - 120)
    lh = size * 1.12
    y = y0 + ((y1 - y0) - len(lines) * lh) / 2
    for ln in lines:
        tw = d.textlength(ln, font=f)
        d.text(((W - tw) / 2, y), ln, font=f, fill=color, stroke_width=6, stroke_fill=(10, 22, 16))
        y += lh

def draw_tag(im, tag):
    if not tag: return
    d = ImageDraw.Draw(im)
    f = font(F_BOLD, 38)
    tw = d.textlength(tag, font=f)
    x = (W - tw) / 2
    d.rounded_rectangle([x - 26, 186, x + tw + 26, 246], 30, fill=LAITON)
    d.text((x, 191), tag, font=f, fill=FORET)

def draw_arrow(im, a, b, color=LAITON, alpha=230):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    ax, ay = sq_xy(a); bx, by = sq_xy(b)
    ax += SQ / 2; ay += SQ / 2; bx += SQ / 2; by += SQ / 2
    ang = math.atan2(by - ay, bx - ax)
    head = 46
    ex, ey = bx - math.cos(ang) * head * 0.9, by - math.sin(ang) * head * 0.9
    d.line([(ax, ay), (ex, ey)], fill=color + (alpha,), width=24)
    p1 = (bx, by)
    p2 = (ex + math.cos(ang + math.pi / 2) * 34, ey + math.sin(ang + math.pi / 2) * 34)
    p3 = (ex + math.cos(ang - math.pi / 2) * 34, ey + math.sin(ang - math.pi / 2) * 34)
    d.polygon([p1, p2, p3], fill=color + (alpha,))
    im.alpha_composite(lay)

BADGES = {"gaffe": ("?? GAFFE", ROUGE), "erreur": ("? ERREUR", ORANGE),
          "mat": ("MAT", ROUGE), "bon": ("✓ BON COUP", VERT_OK),
          "meilleur": ("✓ LE BON COUP", VERT_OK), "brillant": ("!! BRILLANT", LAITON),
          "bizarre": ("!? BIZARRE", LAITON)}

def draw_badge(im, sq, kind, pop):
    label, col = BADGES[kind]
    d = ImageDraw.Draw(im)
    s = 1.0 if pop >= 1 else 0.6 + 0.4 * pop + 0.15 * math.sin(pop * math.pi)
    f = font(F_BLACK, int(46 * s))
    tw = d.textlength(label, font=f)
    x, y = sq_xy(sq)
    cx = min(max(x + SQ / 2, BX + tw / 2 + 30), BX + 8 * SQ - tw / 2 - 30)
    cy = y - 34 if chess.square_rank(sq) < 7 else y + SQ + 34
    pad = 22 * s
    d.rounded_rectangle([cx - tw / 2 - pad, cy - 36 * s, cx + tw / 2 + pad, cy + 36 * s], int(36 * s),
                        fill=col, outline=IVOIRE, width=4)
    d.text((cx - tw / 2, cy - 30 * s), label, font=f, fill=IVOIRE)

def draw_movebar(im, txt):
    if not txt: return
    d = ImageDraw.Draw(im)
    f = font(F_BLACK, 64)
    tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, 470), txt, font=f, fill=LAITON, stroke_width=5, stroke_fill=(10, 22, 16))

def render(st, anim=None, badge_pop=1.0, overlay_num=None, flash=0.0, redflash=0.0, shake=None):
    im = BG.copy()
    d = ImageDraw.Draw(im)
    b = st["board"]
    # surbrillance du dernier coup
    if st.get("last"):
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for s in st["last"]:
            x, y = sq_xy(s); ld.rectangle([x, y, x + SQ - 1, y + SQ - 1], fill=(*LAITON, 120))
        im.alpha_composite(lay)
    # roi en échec / mat
    if b.is_check():
        k = b.king(b.turn); x, y = sq_xy(k)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.ellipse([x + 4, y + 4, x + SQ - 4, y + SQ - 4], fill=(*ROUGE, 190))
        lay = lay.filter(ImageFilter.GaussianBlur(10)); im.alpha_composite(lay)
    hidden = anim["from_board_sq"] if anim else None
    for s, p in b.piece_map().items():
        if anim and s in anim["hide"]: continue
        x, y = sq_xy(s)
        im.alpha_composite(SPRITES[(p.piece_type, p.color)], (int(x), int(y)))
    if anim:
        for (pt, c, a, bsq) in anim["movers"]:
            t = anim["t"]; e = t * t * (3 - 2 * t)
            ax, ay = sq_xy(a); bx, by = sq_xy(bsq)
            im.alpha_composite(SPRITES[(pt, c)], (int(ax + (bx - ax) * e), int(ay + (by - ay) * e)))
    for a, bb in st.get("arrows", []):
        draw_arrow(im, a, bb)
    if st.get("badge"):
        draw_badge(im, st["badge"][0], st["badge"][1], badge_pop)
    draw_tag(im, st.get("tag"))
    draw_text_block(im, st.get("text", ""), 262, 462)
    draw_movebar(im, st.get("movetxt"))
    if overlay_num is not None:
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.rectangle([BX, BY, BX + 8 * SQ, BY + 8 * SQ], fill=(10, 20, 15, 120))
        f = font(F_BLACK, 400); t = str(overlay_num)
        tw = ld.textlength(t, font=f)
        ld.text(((W - tw) / 2, BY + 180), t, font=f, fill=(*IVOIRE, 235), stroke_width=10, stroke_fill=(10, 22, 16))
        im.alpha_composite(lay)
    if flash > 0:
        im.alpha_composite(Image.new("RGBA", (W, H), (*IVOIRE, int(200 * flash))))
    if redflash > 0:
        im.alpha_composite(Image.new("RGBA", (W, H), (*ROUGE, int(150 * redflash))))
    if shake:
        dx, dy = shake
        sh = Image.new("RGBA", (W, H), FORET + (255,))
        sh.alpha_composite(im, (int(dx), int(dy)))
        im = sh
    return im

def shake_vec(i, amp):
    import random
    r = random.Random(i * 7919)
    return (r.uniform(-amp, amp), r.uniform(-amp, amp))

def end_card(t):
    im = Image.new("RGBA", (W, H), FORET + (255,))
    d = ImageDraw.Draw(im)
    f1 = font(F_SERIF, 118); f2 = font(F_BOLD, 54); f3 = font(F_BLACK, 76)
    a = min(1, t * 3)
    def c(col): return tuple(int(FORET[i] + (col[i] - FORET[i]) * a) for i in range(3))
    # petit roi laiton
    k = SPRITES[(chess.KING, chess.WHITE)].resize((200, 200))
    im.alpha_composite(k, ((W - 200) // 2, 560))
    for txt, f, col, y in [("BlunderCheck", f1, IVOIRE, 800), ("Analyse tes parties", f2, IVOIRE, 990),
                           ("gratuitement", f2, IVOIRE, 1056), ("blundercheck.app", f3, LAITON, 1190)]:
        tw = d.textlength(txt, font=f)
        d.text(((W - tw) / 2, y), txt, font=f, fill=c(col))
    d.line([(W / 2 - 160, 1150), (W / 2 + 160, 1150)], fill=c(LAITON), width=4)
    return im

# ---------- moteur de scénario ----------
class Video:
    def __init__(self, out):
        self.p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                   "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                                   "-crf", "19", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out],
                                  stdin=subprocess.PIPE)
        self.n = 0
        self.events = []      # (seconde, son)
        self.music_env = []   # (début, fin, niveau) : coupures de la musique
    @property
    def t(self): return self.n / FPS
    def ev(self, kind, offset=0.0):
        self.events.append((max(0.0, self.t + offset), kind))
    def frame(self, im, k=1):
        raw = im.convert("RGB").tobytes()
        for _ in range(k):
            self.p.stdin.write(raw); self.n += 1
    def close(self):
        self.p.stdin.close(); self.p.wait()

def move_label(b, mv, suffix=""):
    num = b.fullmove_number
    san = fr(b.san(mv))
    return (f"{num}. " if b.turn == chess.WHITE else f"{num}… ") + san + suffix

def play(v, st, san, hold, badge=None, suffix="", text=None, slide=0.33):
    b = st["board"]
    mv = b.parse_san(san)
    label = move_label(b, mv, suffix)
    p = b.piece_at(mv.from_square)
    movers = [(p.piece_type, p.color, mv.from_square, mv.to_square)]
    hide = {mv.from_square, mv.to_square}
    if b.is_castling(mv):
        rf, rt = (chess.H1, chess.F1) if mv.to_square == chess.G1 else (chess.A1, chess.D1)
        if b.turn == chess.BLACK: rf, rt = rf + 56, rt + 56
        movers.append((chess.ROOK, b.turn, rf, rt)); hide |= {rf, rt}
    if text is not None and text != st.get("text"):
        v.ev("whoosh", -0.15)
    if text is not None: st["text"] = text
    st["badge"] = None; st["arrows"] = []
    st["movetxt"] = label
    is_cap = b.is_capture(mv)
    if badge == "mat":
        # tension : la musique se coupe, montée, puis explosion
        v.ev("riser", -0.25)
        v.music_env.append((v.t - 0.3, v.t + slide + 2.4, 0.0))
    nf = max(1, int(slide * FPS))
    for i in range(nf):
        v.frame(render(st, anim={"movers": movers, "hide": hide, "t": (i + 1) / nf, "from_board_sq": None}))
    b.push(mv)
    v.ev("check" if b.is_check() and badge != "mat" else ("capture" if is_cap else "move"), -1 / FPS)
    st["last"] = [mv.from_square, mv.to_square]
    if badge:
        snd = {"gaffe": "impact", "erreur": "bwomp", "mat": "explosion", "brillant": "sparkle",
               "bizarre": "sparkle", "meilleur": "chime", "bon": "chime"}[badge]
        v.ev(snd)
        st["badge"] = (mv.to_square, badge)
        amp = SHAKE.get(badge, 0)
        nshake = int(0.6 * FPS) if amp else 0
        pf = 8
        for i in range(pf):
            k = 1 - i / max(1, nshake)
            v.frame(render(st, badge_pop=(i + 1) / pf,
                           shake=shake_vec(v.n, amp * k) if amp else None,
                           redflash=REDFLASH * (1 - i / pf) if badge == "mat" else 0))
        hold -= pf / FPS
        for i in range(pf, nshake):
            k = 1 - i / nshake
            v.frame(render(st, shake=shake_vec(v.n, amp * k)))
            hold -= 1 / FPS
    v.frame(render(st), max(1, int(hold * FPS)))

def hold(v, st, secs, **kw):
    st.update(kw)
    if v.n == 0:
        v.ev("end")   # coup d'accroche dès la première image
    v.frame(render(st), max(1, int(secs * FPS)))

def rewind(v, st, sans_upto, text):
    b = chess.Board()
    for s in sans_upto: b.push_san(s)
    v.ev("rewind")
    v.music_env.append((v.t, v.t + 0.5, 0.25))
    for i in range(6): v.frame(render(st, flash=(i + 1) / 6))
    st.update(board=b, last=[b.peek().from_square, b.peek().to_square] if b.move_stack else None,
              badge=None, arrows=[], text=text, movetxt="Retour en arrière")
    for i in range(6): v.frame(render(st, flash=1 - (i + 1) / 6))
    v.frame(render(st), int(1.0 * FPS))

def countdown(v, st, text):
    st["text"] = text; st["movetxt"] = ""
    v.ev("whoosh")
    v.music_env.append((v.t, v.t + 3.0, 0.15))
    for n in (3, 2, 1):
        v.ev("tick_hi" if n == 1 else "tick"); v.ev("heart")
        v.frame(render(st, overlay_num=n), FPS)

def show_arrow(v, st, san, text, secs):
    mv = st["board"].parse_san(san)
    v.ev("sparkle")
    st.update(arrows=[(mv.from_square, mv.to_square)], text=text, badge=None,
              movetxt=move_label(st["board"], mv, " !"))
    v.frame(render(st), int(secs * FPS))

def finish(v):
    v.ev("whoosh", -0.2); v.ev("end")
    for i in range(int(FIN_SECS * FPS)):
        v.frame(end_card(i / FPS))

# ---------- les pièges ----------
def blackburne(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #1", "text": "Ce piège gagne\nen 7 coups"}
    hold(v, st, 1.8)
    st["text"] = "Une ouverture normale…"
    for s in ["e4", "e5", "Nf3", "Nc6", "Bc4"]:
        play(v, st, s, 0.32)
    play(v, st, "Nd4", 1.5, badge="bizarre", suffix="!?", text="Les Noirs lâchent le pion e5 ?!")
    play(v, st, "Nxe5", 1.5, badge="erreur", suffix="?", text="Les Blancs le prennent…")
    play(v, st, "Qg5", 2.0, text="Dame g5 : elle attaque g2 ET le cavalier")
    play(v, st, "Nxf7", 1.7, badge="gaffe", suffix="??", text="Il attaque la tour… et ignore la menace")
    st["text"] = "Et tout s'effondre"
    for s in ["Qxg2", "Rf1", "Qxe4+", "Be2"]:
        play(v, st, s, 0.45)
    play(v, st, "Nf3#", 2.2, badge="mat", text="Cavalier f3. MAT.")
    rewind(v, st, ["e4", "e5", "Nf3", "Nc6", "Bc4", "Nd4"], "Retour au coup 4")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "Nxd4", "Prends le CAVALIER, pas le pion", 1.6)
    play(v, st, "Nxd4", 2.0, badge="meilleur", suffix=" !", text="Piège évité.\nLes Blancs sont mieux.")
    finish(v)

def legal(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #2", "text": "Il lâche sa DAME…\net il gagne"}
    hold(v, st, 1.8)
    st["text"] = "Début de partie tranquille"
    for s in ["e4", "e5", "Nf3", "d6", "Bc4"]:
        play(v, st, s, 0.32)
    play(v, st, "Bg4", 1.6, text="Le fou cloue le cavalier sur la dame")
    play(v, st, "Nc3", 0.4)
    play(v, st, "g6", 1.2, badge="erreur", suffix="?", text="Les Noirs jouent un coup lent")
    play(v, st, "Nxe5", 2.0, badge="brillant", suffix="!!", text="Le cavalier bouge… et laisse la DAME")
    play(v, st, "Bxd1", 1.7, badge="gaffe", suffix="??", text="Les Noirs la prennent")
    play(v, st, "Bxf7+", 1.0, text="Échec !")
    play(v, st, "Ke7", 0.5)
    play(v, st, "Nd5#", 2.2, badge="mat", text="MAT. Sans la dame.")
    rewind(v, st, ["e4", "e5", "Nf3", "d6", "Bc4", "Bg4", "Nc3", "g6", "Nxe5"], "Les Noirs pouvaient s'en sortir")
    countdown(v, st, "Trouve le bon coup pour les Noirs")
    show_arrow(v, st, "dxe5", "Prends le CAVALIER, pas la dame", 1.6)
    play(v, st, "dxe5", 2.0, badge="meilleur", suffix=" !", text="Un pion de perdu.\nPas la partie.")
    finish(v)

def berger(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #3", "text": "Mat en 4 coups\n(et comment l'éviter)"}
    hold(v, st, 1.8)
    st["text"] = "Le coup du berger"
    for s in ["e4", "e5", "Bc4", "Nc6"]:
        play(v, st, s, 0.35)
    play(v, st, "Qh5", 0.6, text="Dame et fou visent f7")
    st["arrows"] = [(chess.H5, chess.F7), (chess.C4, chess.F7)]
    v.frame(render(st), int(1.4 * FPS))
    play(v, st, "Nf6", 1.6, badge="gaffe", suffix="??", text="Il attaque la dame… et oublie f7")
    play(v, st, "Qxf7#", 2.2, badge="mat", text="MAT en 4 coups.")
    rewind(v, st, ["e4", "e5", "Bc4", "Nc6", "Qh5"], "Comment se défendre ?")
    countdown(v, st, "Trouve la parade pour les Noirs")
    show_arrow(v, st, "g6", "g6 ! On chasse la dame", 1.6)
    play(v, st, "g6", 1.2, badge="meilleur", suffix=" !", text="g6 ! On chasse la dame")
    play(v, st, "Qf3", 1.4, text="Elle revient viser f7…")
    show_arrow(v, st, "Nf6", "Cf6 bloque tout", 1.2)
    play(v, st, "Nf6", 2.0, badge="bon", text="La route vers f7 est fermée.\nLes Noirs sont bien.")
    finish(v)

def elephant(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #4", "text": "Ce pion gratuit\ncoûte une pièce"}
    hold(v, st, 1.8)
    st["text"] = "Gambit dame, tout est normal"
    for s in ["d4", "d5", "c4", "e6", "Nc3", "Nf6", "Bg5"]:
        play(v, st, s, 0.3)
    play(v, st, "Nbd7", 1.5, text="Les Noirs bloquent leur cavalier ?")
    play(v, st, "cxd5", 0.35)
    play(v, st, "exd5", 1.3, text="Le pion d5 a l'air gratuit…")
    play(v, st, "Nxd5", 1.7, badge="gaffe", suffix="??", text="Le cavalier le prend")
    play(v, st, "Nxd5", 1.6, text="Les Noirs lâchent leur DAME ?!")
    play(v, st, "Bxd8", 1.0, text="Les Blancs la prennent…")
    play(v, st, "Bb4+", 1.6, badge="brillant", suffix="!", text="ÉCHEC ! Et la dame blanche tombe")
    st["text"] = "Bilan : une pièce de moins"
    for s in ["Qd2", "Bxd2+", "Kxd2", "Kxd8"]:
        play(v, st, s, 0.5)
    hold(v, st, 1.4, text="Les Noirs ont gagné\nune pièce entière")
    rewind(v, st, ["d4", "d5", "c4", "e6", "Nc3", "Nf6", "Bg5", "Nbd7", "cxd5", "exd5"], "Retour au coup 6")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "e3", "Ne prends pas d5 ! e3 tout simplement", 1.6)
    play(v, st, "e3", 2.0, badge="meilleur", suffix=" !", text="Piège évité.\nPartie normale.")
    finish(v)

def lasker(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #5", "text": "Il promeut en…\nCAVALIER ?!"}
    hold(v, st, 1.8)
    st["text"] = "Le contre-gambit Albin"
    for s in ["d4", "d5", "c4", "e5", "dxe5"]:
        play(v, st, s, 0.3)
    play(v, st, "d4", 1.2, text="Le pion noir s'enfonce")
    play(v, st, "e3", 1.3, badge="erreur", suffix="?", text="Les Blancs l'attaquent")
    play(v, st, "Bb4+", 0.9, text="Échec du fou")
    play(v, st, "Bd2", 0.4)
    play(v, st, "dxe3", 1.3, text="Le pion continue…")
    play(v, st, "Bxb4", 1.7, badge="gaffe", suffix="??", text="Les Blancs prennent le fou")
    play(v, st, "exf2+", 1.0, text="ÉCHEC !")
    play(v, st, "Ke2", 0.6)
    play(v, st, "fxg1=N+", 2.2, badge="brillant", suffix="!!", text="Promotion en CAVALIER… avec échec !")
    play(v, st, "Ke1", 0.5)
    play(v, st, "Qh4+", 2.0, text="Les Noirs sont gagnants")
    rewind(v, st, ["d4", "d5", "c4", "e5", "dxe5", "d4", "e3", "Bb4+", "Bd2", "dxe3"], "Retour au coup 6")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "fxe3", "Prends le PION, pas le fou", 1.6)
    play(v, st, "fxe3", 2.0, badge="meilleur", suffix=" !", text="Piège évité.\nLa partie est égale.")
    finish(v)

def englund(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #6", "text": "Mat en 8 coups\navec les Noirs"}
    hold(v, st, 1.8)
    st["text"] = "Le gambit Englund"
    for s in ["d4", "e5", "dxe5", "Nc6", "Nf3"]:
        play(v, st, s, 0.3)
    play(v, st, "Qe7", 1.2, text="La dame sort tout de suite ?")
    play(v, st, "Bf4", 0.4)
    play(v, st, "Qb4+", 1.1, text="Échec !")
    play(v, st, "Bd2", 0.4)
    play(v, st, "Qxb2", 1.5, badge="bizarre", suffix="!?", text="Elle croque b2…")
    play(v, st, "Bc3", 1.7, badge="gaffe", suffix="??", text="Le fou attaque la dame")
    play(v, st, "Bb4", 1.6, badge="brillant", suffix="!", text="Le fou noir cloue le fou blanc")
    play(v, st, "Qd2", 0.6, text="Les Blancs paniquent")
    play(v, st, "Bxc3", 0.6)
    play(v, st, "Qxc3", 0.6)
    play(v, st, "Qc1#", 2.2, badge="mat", text="Dame c1. MAT.")
    rewind(v, st, ["d4", "e5", "dxe5", "Nc6", "Nf3", "Qe7", "Bf4", "Qb4+", "Bd2", "Qxb2"], "Retour au coup 6")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "Nc3", "Le CAVALIER protège tout", 1.6)
    play(v, st, "Nc3", 2.0, badge="meilleur", suffix=" !", text="Le gambit a échoué.\nLes Blancs sont mieux.")
    finish(v)

def canne(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #7", "text": "Le piège de\nla canne à pêche"}
    hold(v, st, 1.8)
    st["text"] = "Espagnole, tout est normal"
    for s in ["e4", "e5", "Nf3", "Nc6", "Bb5", "Nf6", "O-O"]:
        play(v, st, s, 0.3)
    play(v, st, "Ng4", 1.3, badge="bizarre", suffix="!?", text="Le cavalier s'avance… c'est l'appât")
    play(v, st, "h3", 0.8, text="Les Blancs le chassent")
    play(v, st, "h5", 1.5, text="Les Noirs le laissent en prise !")
    play(v, st, "hxg4", 1.7, badge="gaffe", suffix="??", text="Les Blancs mordent à l'hameçon")
    play(v, st, "hxg4", 1.2, text="La colonne h s'ouvre…")
    play(v, st, "Ne1", 0.5)
    play(v, st, "Qh4", 1.2, text="La dame arrive")
    play(v, st, "f3", 0.5)
    play(v, st, "g3", 1.2, text="Plus rien n'arrête Dh1")
    play(v, st, "Bxc6", 0.4)
    play(v, st, "Qh1#", 2.2, badge="mat", text="Dame h1. MAT.")
    rewind(v, st, ["e4", "e5", "Nf3", "Nc6", "Bb5", "Nf6", "O-O", "Ng4", "h3", "h5"], "Retour au coup 6")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "c3", "Ne mords pas ! c3 et les Blancs sont mieux", 1.6)
    play(v, st, "c3", 2.0, badge="meilleur", suffix=" !", text="Hameçon évité.\nLes Blancs sont mieux.")
    finish(v)

def siberien(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #8", "text": "Un coup « normal »…\net c'est mat"}
    hold(v, st, 1.8)
    st["text"] = "Le gambit Smith-Morra"
    for s in ["e4", "c5", "d4", "cxd4", "c3", "dxc3", "Nc3", "Nc6", "Nf3", "e6", "Bc4"]:
        play(v, st, s, 0.27)
    play(v, st, "Qc7", 0.9, text="La dame vise h2…")
    play(v, st, "O-O", 0.4)
    play(v, st, "Nf6", 0.4)
    play(v, st, "Qe2", 0.6)
    play(v, st, "Ng4", 1.4, text="Le cavalier menace h2")
    play(v, st, "h3", 1.7, badge="gaffe", suffix="??", text="Les Blancs chassent le cavalier")
    play(v, st, "Nd4", 1.8, badge="brillant", suffix="!!", text="Le 2e cavalier attaque la dame !")
    play(v, st, "Nxd4", 0.6, text="Les Blancs le prennent…")
    play(v, st, "Qh2#", 2.2, badge="mat", text="Dame h2. MAT.")
    rewind(v, st, ["e4", "c5", "d4", "cxd4", "c3", "dxc3", "Nc3", "Nc6", "Nf3", "e6", "Bc4", "Qc7", "O-O",
                   "Nf6", "Qe2", "Ng4"], "Retour au coup 9")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "Rd1", "Td1 ! Ne touche pas au pion h", 1.6)
    play(v, st, "Rd1", 2.0, badge="meilleur", suffix=" !", text="Piège évité.\nPartie égale.")
    finish(v)

def kieninger(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #9", "text": "Il gagne un fou…\net se fait mater"}
    hold(v, st, 1.8)
    st["text"] = "Le gambit de Budapest"
    for s in ["d4", "Nf6", "c4", "e5", "dxe5", "Ng4", "Bf4", "Nc6", "Nf3"]:
        play(v, st, s, 0.28)
    play(v, st, "Bb4+", 0.9, text="Échec du fou")
    play(v, st, "Nbd2", 0.4)
    play(v, st, "Qe7", 1.2, text="La dame se place sur e7")
    play(v, st, "a3", 1.0, text="Les Blancs attaquent le fou")
    play(v, st, "Ngxe5", 1.5, text="Les Noirs le laissent en prise ?!")
    play(v, st, "axb4", 1.7, badge="gaffe", suffix="??", text="Les Blancs prennent le fou")
    play(v, st, "Nd3#", 2.4, badge="mat", text="Cavalier d3. MAT\nen plein milieu !")
    rewind(v, st, ["d4", "Nf6", "c4", "e5", "dxe5", "Ng4", "Bf4", "Nc6", "Nf3", "Bb4+", "Nbd2", "Qe7", "a3", "Ngxe5"],
           "Retour au coup 8")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "Nxe5", "Prends le CAVALIER, pas le fou", 1.6)
    play(v, st, "Nxe5", 2.0, badge="meilleur", suffix=" !", text="Piège évité.\nPartie normale.")
    finish(v)

def stafford(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #10", "text": "Il lâche sa dame…\nEXPRÈS"}
    hold(v, st, 1.8)
    st["text"] = "Défense russe, tout est calme"
    for s in ["e4", "e5", "Nf3", "Nf6", "Nxe5"]:
        play(v, st, s, 0.3)
    play(v, st, "Nc6", 1.4, badge="bizarre", suffix="!?", text="Le gambit Stafford : il offre un pion")
    play(v, st, "Nxc6", 0.4)
    play(v, st, "dxc6", 0.6)
    play(v, st, "d3", 0.4)
    play(v, st, "Bc5", 1.3, text="Le fou noir vise f2")
    play(v, st, "Bg5", 1.6, badge="gaffe", suffix="??", text="Les Blancs attaquent la dame")
    play(v, st, "Nxe4", 1.8, badge="brillant", suffix="!!", text="Le cavalier part… et laisse la DAME")
    play(v, st, "Bxd8", 1.0, text="Les Blancs la prennent…")
    play(v, st, "Bxf2+", 0.9, text="Échec !")
    play(v, st, "Ke2", 0.5)
    play(v, st, "Bg4#", 2.2, badge="mat", text="Fou g4. MAT.\nSans la dame.")
    rewind(v, st, ["e4", "e5", "Nf3", "Nf6", "Nxe5", "Nc6", "Nxc6", "dxc6", "d3", "Bc5"], "Retour au coup 6")
    countdown(v, st, "Trouve le bon coup pour les Blancs")
    show_arrow(v, st, "Be2", "Fe2 ! On protège tout", 1.6)
    play(v, st, "Be2", 2.0, badge="meilleur", suffix=" !", text="Le gambit a échoué.\nLes Blancs sont mieux.")
    finish(v)

def carokann(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #11", "text": "Mat en 6 coups,\nle roi n'a rien vu"}
    hold(v, st, 1.8)
    st["text"] = "La Caro-Kann, une défense solide"
    for s in ["e4", "c6", "d4", "d5", "Nc3", "dxe4", "Nxe4"]:
        play(v, st, s, 0.3)
    play(v, st, "Nd7", 1.0, text="Le cavalier va en d7")
    play(v, st, "Qe2", 1.6, text="La dame blanche se place face au roi")
    play(v, st, "Ngf6", 1.7, badge="gaffe", suffix="??", text="Les Noirs sortent l'autre cavalier")
    play(v, st, "Nd6#", 2.4, badge="mat", text="Cavalier d6. MAT.\nAu 6e coup.")
    rewind(v, st, ["e4", "c6", "d4", "d5", "Nc3", "dxe4", "Nxe4", "Nd7", "Qe2"], "Retour au coup 5")
    countdown(v, st, "Trouve le bon coup pour les Noirs")
    show_arrow(v, st, "Ndf6", "Le cavalier de d7, pas l'autre !", 1.6)
    play(v, st, "Ndf6", 2.0, badge="meilleur", suffix=" !", text="Le roi garde la case d7.\nPartie égale.")
    finish(v)

def petrov(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #12", "text": "Il copie son adversaire…\net perd sa dame"}
    hold(v, st, 1.8)
    st["text"] = "La défense russe"
    for s in ["e4", "e5", "Nf3", "Nf6"]:
        play(v, st, s, 0.3)
    play(v, st, "Nxe5", 1.0, text="Les Blancs prennent e5")
    play(v, st, "Nxe4", 1.3, text="Les Noirs copient : ils prennent e4")
    play(v, st, "Qe2", 1.4, text="La dame attaque le cavalier")
    play(v, st, "Nf6", 1.7, badge="gaffe", suffix="??", text="Le cavalier recule…")
    play(v, st, "Nc6+", 1.9, badge="brillant", suffix="!", text="ÉCHEC À LA DÉCOUVERTE !\nEt la dame noire est attaquée")
    play(v, st, "Qe7", 0.6)
    play(v, st, "Nxe7", 2.0, text="La dame noire tombe")
    rewind(v, st, ["e4", "e5", "Nf3", "Nf6", "Nxe5", "Nxe4", "Qe2"], "Retour au coup 4")
    countdown(v, st, "Trouve le bon coup pour les Noirs")
    show_arrow(v, st, "Qe7", "De7 ! On bloque la colonne e", 1.6)
    play(v, st, "Qe7", 2.0, badge="meilleur", suffix=" !", text="La dame est sauvée.\nLes Noirs limitent la casse.")
    finish(v)

def mat2(v):
    st = {"board": chess.Board(), "tag": "PIÈGE #13", "text": "Mat en 2 coups.\nOui, 2."}
    hold(v, st, 1.8)
    play(v, st, "f3", 1.2, badge="erreur", suffix="?", text="Les Blancs ouvrent la diagonale du roi")
    play(v, st, "e5", 1.0, text="Les Noirs libèrent leur dame")
    play(v, st, "g4", 1.7, badge="gaffe", suffix="??", text="Et ils l'ouvrent encore plus")
    play(v, st, "Qh4#", 2.6, badge="mat", text="Dame h4. MAT\nen 2 coups.")
    rewind(v, st, ["f3", "e5"], "Retour au coup 2")
    countdown(v, st, "Trouve un coup qui ne perd pas")
    show_arrow(v, st, "Nc3", "Tout sauf g4 ! Par exemple Cc3", 1.6)
    play(v, st, "Nc3", 2.0, badge="bon", text="Le roi respire.\nLa partie continue.")
    finish(v)

PIEGES = {"stafford": stafford, "carokann": carokann, "petrov": petrov, "mat2": mat2,
          "blackburne": blackburne, "legal": legal, "berger": berger, "elephant": elephant,
          "lasker": lasker, "englund": englund, "canne": canne, "siberien": siberien, "kieninger": kieninger}

if __name__ == "__main__":
    import os, sons
    nom, out = sys.argv[1], sys.argv[2]
    muet, wav = out + ".muet.mp4", out + ".wav"
    v = Video(muet)
    PIEGES[nom](v)
    v.close()
    sons.mix(v.events, v.n / FPS, v.music_env, wav)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", muet, "-i", wav, "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], check=True)
    os.remove(muet); os.remove(wav)
    print(nom, v.n, "images", round(v.n / FPS, 1), "s,", len(v.events), "sons")
