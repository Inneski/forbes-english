#!/usr/bin/env python3
"""The sound of the Sailing the Seas page: the sea, gulls, a distant foghorn,
and now and then an accordion drifting faintly in and out.

    py lesson-template/build/sailing_sound.py      # writes sailing-the-seas-of-grammar/sound/*.m4a

Innes, 2026-10-01: "sea and birds sounds occasional foghorn, accordion fades
faintly in and out occasionally". Everything is synthesised here (the Block
Camp synth kit's filters and reverb); nothing is recorded or downloaded.
sailing-sound.js (inlined by build_sailing.py) plays it:

  sea.m4a        48 s, loops seamlessly between PAD and PAD + LOOP (written
                 into the page by the builder from sound/loops.json). Swells
                 come in irregularly, roll, break bright and wash back as
                 foam over a low ocean bed.
  gull-1..5.m4a  one-shot calls: a single "kyow", a laughing series, a long
                 mew and two exchanges. Built from harmonics through formants
                 (a gull's nasal "ow"), a "k" at the onset, a little roughness.
                 The player gives each a random pan, pitch and level.
  foghorn.m4a    one diaphone blast with its grunt at the end, far off,
                 echoing over the water.
  accordion.m4a  an original musette waltz in A minor, 32 bars at 150: three
                 reeds a few cents apart on the melody (the musette shimmer),
                 oom-pah-pah on the left hand, heard from along the quay. The
                 player fades a stretch of it in and out, faintly.
"""
import json, os, subprocess, sys
import numpy as np
import imageio_ffmpeg
from scipy.signal import lfilter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'block-camp-music'))
import synthkit as K                                    # noqa: E402

SR = K.SR
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'sailing-the-seas-of-grammar', 'sound')
PAD = 0.5


def R(*key):
    return K.rng('sailing', *key)


def tv_lp(x, fc, chunk=256, q=0.707):
    """Low-pass with a cutoff that follows fc (an array, one value per
    sample), filtered in chunks with the state carried over."""
    x = np.asarray(x, float)
    out = np.empty_like(x)
    zi = np.zeros(2)
    for i in range(0, len(x), chunk):
        f = float(np.mean(fc[i:i + chunk]))
        w = 2 * np.pi * min(max(f, 20), SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


def pan2(x, p):
    return np.stack([x * np.cos((p + 1) * np.pi / 4), x * np.sin((p + 1) * np.pi / 4)], 1) * np.sqrt(2)


def encode(x, name, kbps=96):
    os.makedirs(OUT, exist_ok=True)
    pcm = (np.clip(x, -1, 1) * 32767).astype('<i2').tobytes()
    dst = os.path.join(OUT, name + '.m4a')
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2',
                    '-i', '-', '-c:a', 'aac', '-b:a', '%dk' % kbps, '-movflags', '+faststart', dst],
                   input=pcm, check=True)
    print('  %-14s %5.1f s  peak %.2f  rms %5.1f dBFS  %4d KB' % (
        name, len(x) / SR, np.abs(x).max(), 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12),
        os.path.getsize(dst) // 1024))
    return dst


def norm(x, db):
    x = x * (10 ** (db / 20) / np.sqrt(np.mean(x ** 2)))
    return 0.97 * np.tanh(x / 0.97)


# ── the sea ─────────────────────────────────────────────────────────────────
LOOP = 48.0


def wave(dur, strength, key):
    """One swell: it rolls in low, breaks bright, and washes back as foam."""
    r = R('wave', key)
    n = int(dur * SR); t = np.arange(n) / SR
    tb = r.uniform(1.8, 2.8)                              # when it breaks
    rise = np.clip(t / tb, 0, 1) ** 2
    after = np.exp(-np.clip(t - tb, 0, None) / r.uniform(1.5, 2.3))
    amp = np.where(t < tb, 0.18 + 0.55 * rise, 0.73 + 0.27 * np.exp(-np.clip(t - tb, 0, None) / 0.25))
    amp = amp * np.where(t < tb, 1.0, after) * np.clip((dur - t) / 0.8, 0, 1)
    fc = np.where(t < tb, 220 + 500 * rise, 600 + 1900 * np.exp(-np.clip(t - tb, 0, None) / 0.9))
    out = []
    for ch in range(2):
        # surf is dark: its energy sits low and falls away above a few hundred Hz
        nz = K.lp1(r.standard_normal(n), 350) * 3.5 + r.standard_normal(n) * 0.25
        body = tv_lp(nz, fc) * amp
        # the foam: fine hiss that crackles as the water drains back
        crackle = np.repeat(r.random(n // 480 + 1), 480)[:n] ** 3
        foam = K.hp(r.standard_normal(n), 2600) * crackle * 1.4
        foam *= np.where(t < tb + 0.2, 0, np.exp(-np.clip(t - tb - 0.2, 0, None) / r.uniform(1.8, 2.8)))
        out.append(body + 0.11 * foam)
    p = r.uniform(-0.45, 0.45)
    x = np.stack(out, 1) * strength
    x[:, 0] *= np.cos((p + 1) * np.pi / 4) * np.sqrt(2)
    x[:, 1] *= np.sin((p + 1) * np.pi / 4) * np.sqrt(2)
    return x


def sea():
    """Rendered with a tail past LOOP; the tail is crossfaded (equal power, the
    two halves are unrelated noise) into the head, so the loop has no seam.
    No swell breaks inside the crossfade."""
    tail = 9.0
    n = int((LOOP + tail) * SR)
    x = np.zeros((n, 2))
    r = R('sea-times')
    t = 0.6
    while t < LOOP - 1.0:
        dur = r.uniform(6.5, 9.0)
        i = int(t * SR); w = wave(dur, r.uniform(0.6, 1.0), round(t, 3))
        j = min(n, i + len(w)); x[i:j] += w[:j - i]
        t += r.uniform(4.2, 7.5)
    # the ocean bed: a low, slow roar under everything, and distant surf
    bed = np.stack([K.lp(r.standard_normal(n), 320) for _ in range(2)], 1)
    swell = 0.75 + 0.25 * np.sin(2 * np.pi * np.arange(n) / SR / (LOOP / 4))
    surf = np.stack([K.bp(r.standard_normal(n), 900, 0.6) for _ in range(2)], 1)
    x += bed * 0.45 * swell[:, None] + surf * 0.05
    F = int(tail * SR); L = int(LOOP * SR)
    w = np.linspace(0, 1, F)[:, None]
    y = x[:L].copy()
    y[:F] = x[:F] * np.sqrt(w) + x[L:L + F] * np.sqrt(1 - w)
    y = 0.7 * K.lp1(y, 1100) + 0.3 * y               # a gentle tilt: surf, not static
    y = norm(K.hp1(y, 25), -21)
    out = np.concatenate([y[-int(PAD * SR):], y, y[:int(PAD * SR)]])
    seam = float(np.abs(out[int(PAD * SR) + L - 1] - out[int(PAD * SR) + L - 2]).max())
    encode(out, 'sea', 112)
    return seam


# ── gulls ───────────────────────────────────────────────────────────────────
FORMANTS = [(1500, 500, 1.0), (2700, 700, 0.75), (4100, 900, 0.35)]


def formant_gain(f):
    g = 0.12 * np.exp(-((f - 700) / 600) ** 2)
    for fc, bw, a in FORMANTS:
        g = g + a * np.exp(-((f - fc) / bw) ** 2)
    return g


def gull_note(f0_curve, dur, key, rough=0.3, bright=1.0):
    """f0_curve: f(u) for u in 0..1, the pitch through the note."""
    r = R('gull', key)
    n = int(dur * SR); u = np.linspace(0, 1, n)
    f0 = f0_curve(u) * (1 + 0.012 * K.lp1(r.standard_normal(n), 30) * 8)
    ph = np.cumsum(f0) / SR
    x = np.zeros(n)
    for k in range(1, 14):
        fk = f0 * k
        x += formant_gain(fk / bright) * np.sin(2 * np.pi * k * ph) / k ** 0.35 * (fk < 9000)
    x *= 1 + rough * np.sin(2 * np.pi * r.uniform(70, 110) * np.arange(n) / SR)  # the rasp
    env = np.minimum(1, u * dur / 0.025) * np.minimum(1, (1 - u) * dur / 0.07)
    env *= 0.75 + 0.25 * np.sin(np.pi * u)
    x *= env
    k = int(0.012 * SR)                                    # the "k"
    click = K.bp(r.standard_normal(k), 3200, 1.5) * np.linspace(1, 0, k) * 0.8
    x[:k] += click
    return x


def kyow(lo, hi, dur, key, **kw):
    return gull_note(lambda u: lo + (hi - lo) * np.sin(np.pi * np.clip(u * 1.25, 0, 1)) ** 0.8 * (1 - 0.35 * u), dur, key, **kw)


def place(parts, total):
    x = np.zeros(int(total * SR))
    for t, s in parts:
        i = int(t * SR); j = min(len(x), i + len(s)); x[i:j] += s[:j - i]
    return x


def distant(x, near=0.5):
    """Out over the water: a little high end lost, an open-air reflection."""
    x = K.lp(x, 6500)
    st = np.stack([x, x], 1)
    wet = K.reverb(st, IR_OPEN)
    return st * near + wet * (1 - near) * 0.6


IR_OPEN = K.make_ir(0.9, dark=4000, seed=21, pre=0.03)


def gulls():
    calls = {
        # one call, high and clear
        'gull-1': place([(0.05, kyow(820, 1350, 0.42, 1))], 1.6),
        # the laugh: kyow-kyow-kyow-kow-kow, falling and quickening
        'gull-2': place([(0.05 + i * (0.25 - i * 0.012), kyow(900 - i * 45, 1300 - i * 70, 0.19 - i * 0.008, 10 + i, rough=0.4))
                         for i in range(7)], 2.6),
        # a long plaintive mew
        'gull-3': place([(0.05, gull_note(lambda u: 760 + 300 * np.sin(np.pi * u) ** 1.5 - 120 * u, 0.85, 20, rough=0.15))], 2.0),
        # two birds answering each other
        'gull-4': place([(0.05, kyow(860, 1400, 0.38, 30)), (0.62, kyow(700, 1150, 0.36, 31, bright=0.9)),
                         (1.05, kyow(880, 1420, 0.3, 32))], 2.4),
        'gull-5': place([(0.05, kyow(760, 1250, 0.33, 40, bright=0.92)), (0.42, kyow(740, 1220, 0.3, 41, bright=0.92)),
                         (1.3, gull_note(lambda u: 820 + 250 * np.sin(np.pi * u) - 150 * u, 0.6, 42, rough=0.2))], 2.6),
    }
    for name, x in calls.items():
        y = distant(x, 0.55)
        y = norm(y, -20)
        fade = int(0.15 * SR)
        y[-fade:] *= np.linspace(1, 0, fade)[:, None]
        encode(y, name, 96)


# ── the foghorn ─────────────────────────────────────────────────────────────
def foghorn():
    r = R('horn')
    blast, tail = 3.4, 6.5
    n = int((blast + tail) * SR); t = np.arange(n) / SR
    grunt = 0.55
    f0 = np.where(t < blast - grunt, 152 * (1 + 0.003 * np.sin(2 * np.pi * 4.6 * t)),
                  152 - 52 * np.clip((t - (blast - grunt)) / grunt, 0, 1) ** 1.6)
    ph = np.cumsum(f0) / SR
    tone = 0.6 * (2 * (ph % 1) - 1) + 0.5 * np.where((ph % 1) < 0.32, 1.0, -1.0)
    amp = np.clip(t / 0.35, 0, 1) ** 1.5 * np.where(t < blast - grunt, 1.0,
                                                     np.clip(1 - (t - (blast - grunt)) / grunt, 0, 1) ** 0.7)
    fc = 300 + 1300 * np.clip(t / 0.5, 0, 1) * np.where(t < blast - grunt, 1, np.clip(1 - (t - (blast - grunt)) / grunt, 0.25, 1))
    x = tv_lp(tone, fc, q=1.4) * amp
    x += 0.04 * K.bp(r.standard_normal(n), 600, 0.8) * amp          # the air in it
    x = K.lp(x, 2200)
    st = np.stack([x, x], 1)
    wet = K.reverb(st, K.make_ir(3.2, dark=1400, seed=7, pre=0.08))
    echo = K.pingpong(st, 0.41, 0.42, 5, 1200)
    y = st * 0.35 + wet * 0.55 + echo * 0.4
    y = norm(K.hp1(y, 35), -19)
    fade = int(1.0 * SR)
    y[-fade:] *= np.linspace(1, 0, fade)[:, None]
    encode(y, 'foghorn', 96)


# ── the accordion ───────────────────────────────────────────────────────────
BPM = 150
BEAT = 60 / BPM
BAR = 3 * BEAT
A4, B4, C5, D5, E5, F5, G5, Gs5, A5, B5, C6 = 69, 71, 72, 74, 76, 77, 79, 80, 81, 83, 84
Gs4, G4 = 68, 67
q, e, h3, h = 1, 0.5, 3, 2
# (bar's chord, [(midi, beats), ...]); 32 bars of 3/4. An original tune.
TUNE = [
    ('Am', [(A4, e), (C5, e), (E5, q), (E5, q)]), ('Am', [(D5, e), (C5, e), (B4, q), (C5, q)]),
    ('Dm', [(D5, e), (F5, e), (A5, q), (A5, q)]), ('Dm', [(G5, e), (F5, e), (E5, q), (F5, q)]),
    ('E7', [(E5, e), (Gs5, e), (B5, q), (B5, q)]), ('E7', [(A5, e), (Gs5, e), (F5, q), (D5, q)]),
    ('Am', [(C5, q), (E5, q), (A5, q)]), ('Am', [(A5, h3)]),
    ('Am', [(A4, e), (C5, e), (E5, q), (E5, q)]), ('Am', [(F5, e), (E5, e), (D5, q), (C5, q)]),
    ('Dm', [(D5, e), (F5, e), (A5, q), (G5, q)]), ('Dm', [(F5, e), (E5, e), (D5, q), (F5, q)]),
    ('E7', [(E5, q), (D5, q), (B4, q)]), ('E7', [(Gs4, q), (B4, q), (D5, q)]),
    ('Am', [(C5, q), (B4, q), (E5, q)]), ('A7', [(A4, h3)]),
    ('Dm', [(F5, h), (E5, q)]), ('Dm', [(D5, q), (F5, q), (A5, q)]),
    ('Am', [(C6, h), (B5, q)]), ('Am', [(A5, q), (E5, q), (C5, q)]),
    ('E7', [(B4, e), (D5, e), (Gs5, q), (B5, q)]), ('E7', [(A5, e), (Gs5, e), (F5, q), (E5, q)]),
    ('Am', [(E5, q), (A5, q), (C6, q)]), ('Am', [(B5, e), (A5, e), (A5, h)]),
    ('F', [(A5, h), (C6, q)]), ('F', [(A5, q), (F5, q), (C5, q)]),
    ('C', [(E5, h), (G5, q)]), ('C', [(E5, q), (C5, q), (G4, q)]),
    ('E7', [(Gs4, e), (B4, e), (D5, q), (F5, q)]), ('E7', [(E5, e), (D5, e), (B4, q), (Gs4, q)]),
    ('Am', [(A4, q), (C5, q), (E5, q)]), ('Am', [(A4, h3)]),
]
CHORDS = {'Am': (45, [57, 60, 64]), 'Dm': (50, [57, 62, 65]), 'E7': (40, [56, 59, 62]), 'A7': (45, [57, 61, 64]),
          'F': (41, [57, 60, 65]), 'C': (48, [55, 60, 64])}
FIFTH = {'Am': 40, 'Dm': 45, 'E7': 47, 'A7': 40, 'F': 48, 'C': 43}


def reed(m, dur, cents, key, bright=1.0):
    """One free reed: a buzzy, slightly nasal tone; the bellows set its
    envelope."""
    r = R('reed', key)
    n = int((dur + 0.12) * SR)
    f = K.hz(m) * 2 ** (cents / 1200)
    f = f * (1 + 0.0015 * np.sin(2 * np.pi * r.uniform(4, 6) * np.arange(n) / SR + r.uniform(0, 6)))
    ph = np.cumsum(f) / SR + r.random()
    x = 0.55 * (2 * (ph % 1) - 1) + 0.45 * np.where((ph % 1) < 0.42, 1.0, -1.0)
    t = np.arange(n) / SR
    env = np.minimum(1, t / 0.035) * np.clip((dur + 0.06 - t) / 0.08, 0, 1)
    return K.lp(x * env, 3800 * bright, 0.9)


def accordion():
    total = len(TUNE) * BAR + 3.0
    mel = np.zeros(int(total * SR)); left = np.zeros(int(total * SR))
    r = R('acc')

    def put(buf, t, s, g):
        i = int(max(t, 0) * SR); j = min(len(buf), i + len(s)); buf[i:j] += s[:j - i] * g

    for b, (ch, notes) in enumerate(TUNE):
        t = b * BAR
        for m, beats in notes:
            d = beats * BEAT
            jit = r.normal(0, 0.006)
            # musette: one reed true, one a little sharp, one a little flat
            s = reed(m, d * 0.96, 0, (b, t, 0)) + reed(m, d * 0.96, 13, (b, t, 1)) * 0.8 + reed(m, d * 0.96, -11, (b, t, 2)) * 0.7
            put(mel, t + jit, s, 0.33)
            t += d
        root, chord = CHORDS[ch]
        bass = root if b % 2 == 0 else FIFTH[ch]
        put(left, b * BAR, reed(bass, BEAT * 0.85, 0, ('b', b), 0.5) + reed(bass + 12, BEAT * 0.85, 4, ('b2', b), 0.5) * 0.5, 0.3)
        for k in (1, 2):
            put(left, b * BAR + k * BEAT, sum(reed(c, BEAT * 0.42, 0, ('c', b, k, c), 0.7) for c in chord), 0.11)
    # the player's breath on the bellows: phrases swell and ebb
    tt = np.arange(len(mel)) / SR
    swell = 0.82 + 0.18 * np.sin(2 * np.pi * tt / (4 * BAR) - np.pi / 2)
    x = np.stack([mel * swell * 0.95 + left * 0.8, mel * swell * 0.85 + left * 0.95], 1)
    x = K.lp(x, 4200)                                    # along the quay: no air at the top
    wet = K.reverb(x, K.make_ir(1.6, dark=2500, seed=5, pre=0.04))
    y = norm(K.hp1(x * 0.6 + wet * 0.55, 60), -20)
    fade = int(2.0 * SR)
    y[-fade:] *= np.linspace(1, 0, fade)[:, None]
    encode(y, 'accordion', 96)


if __name__ == '__main__':
    print('sailing sound ->', os.path.relpath(OUT, ROOT))
    sea()
    gulls()
    foghorn()
    accordion()
    json.dump({'sea': [PAD, PAD + LOOP]}, open(os.path.join(OUT, 'loops.json'), 'w'), indent=1)
    print('  loops.json: sea %g .. %g' % (PAD, PAD + LOOP))
