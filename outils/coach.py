"""Format « coach » (21/10) inspiré de ChessReps : échiquier en gros plan, voix off, sous-titres calés.
Rend la vidéo muette (images) + une piste de bruitages ; la voix est ajoutée au montage.
"""
import sys, subprocess, json, math
import chess
from PIL import Image, ImageDraw, ImageFilter
import gen, sons
from gen import font, F_BLACK, F_BOLD, IVOIRE, LAITON, FORET

W, H, FPS = 1080, 1920, 30
SQ = 135
BX, BY = 0, 500
CASE_C = (238, 233, 214)
CASE_F = (106, 140, 96)
SURL = (222, 196, 92)
FOND = (22, 30, 26)

def sprite(pt, color):
    im = Image.new("RGBA", (SQ, SQ), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = font(gen.F_PIECE, 118)
    g = gen.GLYPH[pt]
    bb = d.textbbox((0, 0), g, font=f)
    x = (SQ - (bb[2] - bb[0])) / 2 - bb[0]; y = (SQ - (bb[3] - bb[1])) / 2 - bb[1]
    if color == chess.WHITE:
        d.text((x, y), g, font=f, fill=(252, 249, 240), stroke_width=5, stroke_fill=(30, 30, 30))
    else:
        d.text((x, y), g, font=f, fill=(32, 32, 32), stroke_width=3, stroke_fill=(90, 90, 90))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.paste((0, 0, 0, 80), (0, 0), im.split()[3])
    sh = sh.filter(ImageFilter.GaussianBlur(3))
    out = Image.new("RGBA", im.size, (0, 0, 0, 0)); out.alpha_composite(sh, (3, 5)); out.alpha_composite(im)
    return out

SPR = {(pt, c): sprite(pt, c) for pt in gen.GLYPH for c in (chess.WHITE, chess.BLACK)}

FLIP = False

def xy(sq):
    f, r = chess.square_file(sq), chess.square_rank(sq)
    if FLIP: f, r = 7 - f, 7 - r
    return BX + f * SQ, BY + (7 - r) * SQ

def fond():
    im = Image.new("RGBA", (W, H), FOND + (255,))
    d = ImageDraw.Draw(im)
    fc = font(F_BOLD, 24)
    for s in chess.SQUARES:
        x, y = xy(s)
        light = (chess.square_file(s) + chess.square_rank(s)) % 2 == 1
        d.rectangle([x, y, x + SQ - 1, y + SQ - 1], fill=CASE_C if light else CASE_F)
    files = "hgfedcba" if FLIP else "abcdefgh"
    for i in range(8):
        d.text((BX + i * SQ + SQ - 20, BY + 8 * SQ - 30), files[i], font=fc, fill=CASE_F if i % 2 else CASE_C)
        d.text((BX + 6, BY + i * SQ + 4), str(i + 1) if FLIP else str(8 - i), font=fc, fill=CASE_F if i % 2 == 0 else CASE_C)
    fw = font(F_BOLD, 34); t = "blundercheck.app"
    d.text(((W - d.textlength(t, font=fw)) / 2, BY + 8 * SQ + 36), t, font=fw, fill=LAITON)
    return im

BG = fond()
ICON = {"livre": ("📖", (150, 110, 70)), "bizarre": ("!?", (60, 160, 190)), "erreur": ("?", (230, 140, 40)),
        "gaffe": ("??", (210, 50, 45)), "mat": ("#", (60, 60, 60)), "meilleur": ("★", (100, 170, 70)),
        "bon": ("!", (90, 160, 90))}

def icone(im, sq, kind):
    lab, col = ICON[kind]
    if kind == "livre": lab = "≡"
    d = ImageDraw.Draw(im)
    x, y = xy(sq); cx, cy, r = x + SQ - 8, y + 8, 30
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col, outline=(255, 255, 255), width=4)
    f = font(F_BLACK, 34 if len(lab) < 2 else 28)
    tw = d.textlength(lab, font=f)
    d.text((cx - tw / 2, cy - 22), lab, font=f, fill=(255, 255, 255))

def fleche(im, a, b, col=(240, 170, 40)):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ax, ay = xy(a); bx, by = xy(b); ax += SQ / 2; ay += SQ / 2; bx += SQ / 2; by += SQ / 2
    ang = math.atan2(by - ay, bx - ax); ex, ey = bx - math.cos(ang) * 50, by - math.sin(ang) * 50
    d.line([(ax, ay), (ex, ey)], fill=col + (210,), width=28)
    p2 = (ex + math.cos(ang + math.pi / 2) * 40, ey + math.sin(ang + math.pi / 2) * 40)
    p3 = (ex + math.cos(ang - math.pi / 2) * 40, ey + math.sin(ang - math.pi / 2) * 40)
    d.polygon([(bx, by), p2, p3], fill=col + (210,))
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

def render(b, last, anim=None, icons=(), arrows=(), txt=""):
    im = BG.copy()
    if last:
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for s in last:
            x, y = xy(s); ld.rectangle([x, y, x + SQ - 1, y + SQ - 1], fill=SURL + (150,))
        im.alpha_composite(lay)
    if b.is_check():
        k = b.king(b.turn); x, y = xy(k)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.ellipse([x + 6, y + 6, x + SQ - 6, y + SQ - 6], fill=(220, 40, 40, 190))
        im.alpha_composite(lay.filter(ImageFilter.GaussianBlur(12)))
    hide = anim["hide"] if anim else set()
    for s, p in b.piece_map().items():
        if s in hide: continue
        x, y = xy(s); im.alpha_composite(SPR[(p.piece_type, p.color)], (x, y))
    if anim:
        t = anim["t"]; e = t * t * (3 - 2 * t)
        for pt, c, a, bb in anim["movers"]:
            ax, ay = xy(a); bx, by = xy(bb)
            im.alpha_composite(SPR[(pt, c)], (int(ax + (bx - ax) * e), int(ay + (by - ay) * e)))
    for a, bb in arrows: fleche(im, a, bb)
    for sq, kind in icons: icone(im, sq, kind)
    sous_titre(im, txt)
    return im

def run(spec, out_video, out_wav, tempo):
    """spec : dict avec 'actions' [(t, type, données)] et 'captions' [(t0, t1, texte)] en secondes de voix originale."""
    k = 1 / tempo
    dur = spec["duree"] * k + 0.6
    nfr = int(dur * FPS)
    caps = [(a * k, b * k, t) for a, b, t in spec["captions"]]
    acts = sorted([(t * k, typ, data) for t, typ, data in spec["actions"]], key=lambda x: x[0])
    b = chess.Board(); last = None; icons = []; arrows = []
    events = []
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                          "-pix_fmt", "yuv420p", out_video], stdin=subprocess.PIPE)
    ai = 0; anim = None; anim_end = None; pending = None
    SLIDE = 0.28
    for f in range(nfr):
        t = f / FPS
        while ai < len(acts) and acts[ai][0] <= t:
            _, typ, data = acts[ai]; ai += 1
            if typ in ("coup", "position") and anim:
                # termine tout de suite le coup en cours avant le suivant
                mv0, badge0, cap0 = pending
                b.push(mv0); last = [mv0.from_square, mv0.to_square]
                events.append((t, "capture" if cap0 else "move"))
                if badge0: icons = [(mv0.to_square, badge0)]
                anim = None
            if typ == "coup":
                san, badge = data
                mv = b.parse_san(san)
                pc = b.piece_at(mv.from_square)
                movers = [(pc.piece_type, pc.color, mv.from_square, mv.to_square)]
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
                icons = []; arrows = []; events.append((t, "rewind"))
            elif typ == "son":
                events.append((t, data))
        if anim:
            prog = (t - anim["t0"]) / SLIDE
            if prog >= 1:
                mv, badge, cap = pending
                b.push(mv); last = [mv.from_square, mv.to_square]
                events.append((anim["t0"] + SLIDE, "check" if b.is_check() and not b.is_checkmate() else ("capture" if cap else "move")))
                if badge:
                    icons = [(mv.to_square, badge)]
                    if badge in ("gaffe",): events.append((anim["t0"] + SLIDE, "bwomp"))
                    if badge == "mat": events.append((anim["t0"] + SLIDE, "impact"))
                    if badge == "meilleur": events.append((anim["t0"] + SLIDE, "chime"))
                anim = None
                frame = render(b, last, None, icons, arrows, "")
            else:
                frame = render(b, last, {"movers": anim["movers"], "hide": anim["hide"], "t": max(0, prog)}, icons, arrows, "")
        else:
            frame = render(b, last, None, icons, arrows, "")
        txt = next((c for a, z, c in caps if a <= t < z + 0.15), "")
        if txt:
            sous_titre(frame, txt)
        p.stdin.write(frame.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    # bruitages + musique très basse (la voix est ajoutée au montage)
    import numpy as np
    from scipy.io import wavfile
    n = int(dur * sons.SR)
    fx = np.zeros(n + 3 * sons.SR)
    for at, kind in events:
        s = sons.FX[kind](); i0 = int(at * sons.SR); fx[i0:i0 + len(s)] += s
    fx = fx[:n]
    m = sons.music(dur) * 0.10
    y = np.tanh((fx * 0.55 + m) * 1.1) * 0.9
    fade = int(0.5 * sons.SR); y[-fade:] *= np.linspace(1, 0, fade)
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
