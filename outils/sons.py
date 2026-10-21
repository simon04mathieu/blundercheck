"""Bande-son synthétisée des vidéos BlunderCheck (aucun échantillon externe)."""
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

SR = 48000
rng = np.random.default_rng(7)

def t_(d): return np.arange(int(d * SR)) / SR
def env(d, a=0.002, decay=0.1):
    t = t_(d); return np.minimum(1, t / a) * np.exp(-t / decay)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], "bandpass", fs=SR, output="sos"), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, "lowpass", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "highpass", fs=SR, output="sos"), x)
def noise(d): return rng.standard_normal(int(d * SR))
def norm(x, g=1.0): m = np.max(np.abs(x)) or 1; return x / m * g

def sweep(f0, f1, d, curve=3.0):
    t = t_(d); f = f1 + (f0 - f1) * np.exp(-t * curve / d * 3)
    return np.sin(2 * np.pi * np.cumsum(f) / SR)

def reverb(x, d=0.9, mix=0.25):
    ir = noise(d) * np.exp(-t_(d) / (d / 5)); ir = lp(ir, 5000)
    w = fftconvolve(x, ir)[:len(x) + int(d * SR)]
    out = np.zeros(len(w)); out[:len(x)] = x
    return out * (1 - mix) + norm(w, np.max(np.abs(x))) * mix

# ---------- effets ----------
def piece(force=1.0):
    d = 0.09
    click = bp(noise(d), 1800, 5200) * env(d, 0.0005, 0.006)
    body = (np.sin(2 * np.pi * 820 * t_(d)) * 0.5 + np.sin(2 * np.pi * 310 * t_(d))) * env(d, 0.001, 0.022)
    return norm(click * 1.2 + body * 0.8, 0.55 * force)

def capture():
    a = piece(1.25); b = piece(0.8)
    out = np.zeros(int(0.16 * SR)); out[:len(a)] += a; o = int(0.035 * SR); out[o:o + len(b)] += b
    thud = np.sin(2 * np.pi * 120 * t_(0.16)) * env(0.16, 0.001, 0.05) * 0.45
    return out + thud

def check():
    d = 0.25
    s = (np.sign(np.sin(2 * np.pi * 880 * t_(d))) * 0.15 + np.sin(2 * np.pi * 1320 * t_(d)) * 0.3) * env(d, 0.003, 0.08)
    out = np.zeros(int(0.3 * SR)); p = capture(); out[:len(p)] += p; out[:len(s)] += s * 0.6
    return out

def whoosh(d=0.35, up=True, g=0.35):
    n = noise(d); t = t_(d)
    shape = np.sin(np.pi * t / d) ** 2
    lo = bp(n, 300, 1500); hi = bp(n, 1500, 6000)
    mixw = t / d if up else 1 - t / d
    return norm((lo * (1 - mixw) + hi * mixw) * shape, g)

def impact(g=0.9):
    d = 1.1
    sub = sweep(140, 38, d, 2.5) * env(d, 0.002, 0.35)
    hit = lp(noise(d), 2500) * env(d, 0.001, 0.06)
    x = np.tanh((sub * 1.4 + hit * 0.8) * 1.8)
    return norm(reverb(x, 0.8, 0.2), g)

def explosion():
    d = 2.4
    burst = lp(noise(d), 1800, 4) * env(d, 0.002, 0.45)
    crack = hp(noise(d), 2500) * env(d, 0.001, 0.12) * 0.6
    sub = sweep(110, 30, d, 2) * env(d, 0.003, 0.7) * 1.4
    deb = np.zeros(int(d * SR))
    for _ in range(70):  # débris
        p = int(rng.uniform(0.05, 1.6) * SR); L = int(0.015 * SR)
        if p + L < len(deb): deb[p:p + L] += bp(noise(0.015), 1000, 6000) * env(0.015, 0.0005, 0.004) * rng.uniform(0.1, 0.5) * np.exp(-p / SR / 0.6)
    x = np.tanh((burst * 1.3 + crack + sub + deb) * 2.2)
    return norm(reverb(x, 1.6, 0.3), 1.0)

def ding(freqs=(1568, 2093), g=0.4, d=1.0):
    out = np.zeros(int((d + 0.12 * len(freqs)) * SR))
    for i, f in enumerate(freqs):
        s = sum(np.sin(2 * np.pi * f * k * t_(d)) / k ** 1.6 for k in (1, 2.76, 5.4)) * env(d, 0.002, 0.28)
        o = int(i * 0.11 * SR); out[o:o + len(s)] += s
    return norm(reverb(out, 0.8, 0.3), g)

def bwomp(g=0.55):
    d = 0.9
    s = sum(np.sin(2 * np.pi * np.cumsum(np.linspace(f, f * 0.5, int(d * SR))) / SR) for f in (220, 233))
    s = lp(np.tanh(s * 2), 1800) * env(d, 0.01, 0.35)
    return norm(s, g)

def tick(high=False):
    d = 0.08; f = 2400 if high else 1600
    s = np.sin(2 * np.pi * f * t_(d)) * env(d, 0.0005, 0.012) + bp(noise(d), 3000, 8000) * env(d, 0.0003, 0.004) * 0.5
    return norm(s, 0.5)

def heartbeat():
    out = np.zeros(int(0.5 * SR))
    for o, g in ((0, 1), (0.17, 0.7)):
        s = np.sin(2 * np.pi * 55 * t_(0.2)) * env(0.2, 0.004, 0.06) * g
        p = int(o * SR); out[p:p + len(s)] += s
    return norm(lp(out, 300), 0.7)

def rewind():
    d = 0.45; t = t_(d)
    f = 3000 * np.exp(-t * 4) + 200
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.3 + bp(noise(d), 800, 4000) * 0.5
    s *= np.sin(np.pi * t / d) * (1 + 0.5 * np.sign(np.sin(2 * np.pi * 28 * t)))
    return norm(s, 0.4)

def riser(d=0.6):
    t = t_(d); s = bp(noise(d), 500, 7000) * (t / d) ** 2
    return norm(s, 0.35)

FX = {"move": lambda: piece(), "capture": capture, "check": check, "whoosh": lambda: whoosh(),
      "impact": impact, "explosion": explosion, "ding": lambda: ding(), "chime": lambda: ding((1047, 1319, 1568), 0.45),
      "sparkle": lambda: ding((2093, 2637, 3136), 0.3, 0.7), "bwomp": bwomp, "tick": lambda: tick(),
      "tick_hi": lambda: tick(True), "heart": heartbeat, "rewind": rewind, "riser": riser,
      "end": lambda: impact(0.6)}

# ---------- musique ----------
def music(dur, bpm=140):
    beat = 60 / bpm; n = int(dur * SR) + SR
    out = np.zeros(n)
    def add(sig, at, g=1.0):
        p = int(at * SR)
        if p < n: L = min(len(sig), n - p); out[p:p + L] += sig[:L] * g
    kick = np.tanh(sweep(160, 45, 0.35, 3) * env(0.35, 0.001, 0.12) * 2)
    clap = sum(np.roll(np.pad(bp(noise(0.12), 900, 5000) * env(0.12, 0.001, 0.035), (0, 600)), k * 240) for k in range(3))
    hat = hp(noise(0.04), 7000) * env(0.04, 0.0005, 0.01)
    notes = [55.0, 43.65, 65.41, 49.0]  # La, Fa, Do, Sol (mineur)
    bar = beat * 4; t = 0.0; i = 0
    while t < dur:
        root = notes[i % 4]
        for k in (0, 1.5, 2.5):
            add(kick, t + k * beat, 0.9)
        add(clap, t + 2 * beat, 0.5)
        for h in range(8):
            add(hat, t + h * beat / 2, 0.22 if h % 2 else 0.32)
        if i % 2 == 1:
            for h in range(4): add(hat, t + 3.5 * beat + h * beat / 8, 0.18)
        b = np.sin(2 * np.pi * root * t_(bar)) + 0.3 * np.sin(2 * np.pi * root * 2 * t_(bar))
        b *= np.minimum(1, t_(bar) / 0.01) * np.exp(-t_(bar) / 1.2)
        add(np.tanh(b * 1.5) * 0.55, t)
        # petite mélodie pluck
        mel = [4, 7, 11, 7] if i % 2 == 0 else [3, 7, 10, 12]
        for j, st in enumerate(mel):
            f = root * 8 * 2 ** (st / 12)
            pl = (np.sin(2 * np.pi * f * t_(0.3)) + 0.4 * np.sin(4 * np.pi * f * t_(0.3))) * env(0.3, 0.002, 0.09)
            add(pl, t + j * beat + (beat / 2 if j % 2 else 0), 0.12)
        t += bar; i += 1
    return out[:int(dur * SR)]

def mix(events, dur, music_env, out_wav):
    n = int(dur * SR)
    fx = np.zeros(n + 3 * SR)
    for at, kind in events:
        s = FX[kind](); p = int(at * SR)
        fx[p:p + len(s)] += s
    fx = fx[:n]
    m = music(dur)
    g = np.ones(n)
    for a, b, lvl in music_env:  # coupures / baisses de la musique
        pa, pb = int(a * SR), min(n, int(b * SR))
        ramp = int(0.04 * SR)
        g[pa:pb] = np.minimum(g[pa:pb], lvl)
        if pb + ramp < n: g[pb:pb + ramp] = np.minimum(g[pb:pb + ramp], np.linspace(lvl, 1, ramp))
    # sidechain : la musique baisse sous les effets forts
    envfx = np.convolve(np.abs(fx), np.ones(2400) / 2400, mode="same")
    duck = 1 - np.clip(envfx * 2.2, 0, 0.6)
    y = m * 0.32 * g * duck + fx * 0.9
    y = np.tanh(y * 1.15) * 0.92
    fade = int(0.4 * SR); y[-fade:] *= np.linspace(1, 0, fade)
    st = np.stack([y, y], 1)
    wavfile.write(out_wav, SR, (st * 32767).astype(np.int16))
