#!/usr/bin/env python3
"""Block Camp soundtrack "Lakeside": an original analogue-synth loop.

Innes, 2026-09-30: "make music more like the fishing piece - Jean Michel
Jarre Oxygene type music". So: the fishing clip's own key and pace (measured:
D and A, open fifths, about 100 BPM), and the Oxygene palette - a string
machine through a phaser, a bouncing sequenced bass, a bubbling arpeggio with
echo, a gliding vibrato lead, a soft rhythm box, sea-wind swooshes. The
melody and changes are new; nothing is copied.

It is a LOOP, 32 bars at 100 BPM = 76.8 s. To make the seam invisible the
whole timeline is rendered from 8 bars before the loop to 1 bar after, with
every event, random choice and LFO a function of (bar mod 32), so the
pre-roll is literally the end of the previous lap and its echo and reverb
tails fall across bar 0 exactly as they would on a real repeat. The file
keeps 0.5 s of that continuation either side of the loop:
data-loop="0.5 77.3" in the page's <script> tag.

    py lesson-template/build/block-camp-music/lakeside.py            -> block-camp/music/past-simple.m4a
    py lesson-template/build/block-camp-music/lakeside.py --wav X    also a preview WAV
"""
import os, subprocess, sys, zlib
import numpy as np
import imageio_ffmpeg
from scipy.signal import fftconvolve, lfilter, stft, istft

SR = 48000
BPM = 100
BEAT = 60 / BPM                  # 0.6 s
BAR = 4 * BEAT                   # 2.4 s
S16 = BEAT / 4                   # 0.15 s
BARS = 32
LOOP = BARS * BAR                # 76.8 s
PRE, POST = 8, 1                 # bars rendered either side of the loop
PAD = 0.5                        # seconds of continuation kept either side
T0 = PRE * BAR
TOTAL = (PRE + BARS + POST) * BAR + 6.0   # + room for tails
N = int(TOTAL * SR)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
OUT = os.path.join(ROOT, 'block-camp', 'music', 'past-simple.m4a')


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def rng(*key):
    return np.random.default_rng(zlib.crc32(repr(('lakeside',) + key).encode()))


def smp(t):
    return int(round((t + T0) * SR))


class Bus:
    def __init__(self):
        self.x = np.zeros((N, 2))

    def add(self, t, sig, pan=0.0, gain=1.0):
        i = smp(t)
        if sig.ndim == 1:
            l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
            sig = np.stack([sig * l, sig * r], 1) * np.sqrt(2)
        j0, j1 = max(i, 0), min(i + len(sig), N)
        if j1 > j0:
            self.x[j0:j1] += sig[j0 - i:j1 - i] * gain


def lp1(x, fc):
    a = np.exp(-2 * np.pi * fc / SR)
    return lfilter([1 - a], [1, -a], x, axis=0)


def biquad_lp(x, fc, q):
    w = 2 * np.pi * min(fc, SR * 0.45) / SR
    al = np.sin(w) / (2 * q); c = np.cos(w)
    b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
    return lfilter(b / a[0], a / a[0], x)


def saw(f, n, ph=0.0):
    p = (ph + np.cumsum(np.full(n, f / SR))) % 1.0
    return 2 * p - 1


def env_ar(n, att, rel_start, rel):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(att, 1e-4))
    r = np.clip((t - rel_start) / max(rel, 1e-4), 0, 1)
    return e * (1 - r) ** 2


# ── the changes: one chord per 2 bars, an 8-bar cycle ─────────────────────
#   Dm9            Bbmaj7          Gm7             A7sus4 -> A
CHORDS = [
    (38, [50, 53, 57, 64]),
    (34, [46, 50, 53, 57]),
    (31, [43, 46, 50, 53]),
    (33, [45, 50, 52, 55]),
]
A_TRIAD = [45, 49, 52, 55]       # bar 7 of each cycle: the sus resolves


def chord_at(bar):
    c = (bar % 8) // 2
    root, tones = CHORDS[c]
    if bar % 8 == 7:
        tones = A_TRIAD
    return root, tones


# ── arrangement: what plays in each bar of the 32 (bar mod 32) ────────────
def has(part, b):
    b %= 32
    cyc, inbar = b // 8, b % 8
    if part == 'bass':  return not (cyc == 0 and inbar < 4)
    if part == 'arp':   return cyc in (1, 2) or (cyc == 3 and inbar < 6)
    if part == 'drums': return cyc in (1, 2) or (cyc == 3 and inbar < 6)
    if part == 'lead':  return cyc in (1, 2)
    return True


# ── instruments ───────────────────────────────────────────────────────────
def pad_note(m, dur):
    n = int((dur + 1.8) * SR)
    x = np.zeros(n)
    for k, cents in enumerate((-9, -4, 0, 4, 9)):
        x += saw(hz(m) * 2 ** (cents / 1200), n, ph=(k * 0.217) % 1)
    x = lp1(lp1(x, 2400), 2600) / 5
    return x * env_ar(n, 0.9, dur, 1.6)


def bass_note(m, cutoff):
    n = int(0.42 * SR)
    x = saw(hz(m), n) * 0.7 + saw(hz(m) * 1.003, n) * 0.3
    x = biquad_lp(x, cutoff, 3.2)
    t = np.arange(n) / SR
    return x * np.exp(-t / 0.2) * np.minimum(1, t / 0.004)


def arp_note(m):
    n = int(0.3 * SR)
    p = np.cumsum(np.full(n, hz(m) / SR)) % 1.0
    x = np.where(p < 0.5, 1.0, -1.0)
    x = lp1(lp1(x, 3200), 3600)
    t = np.arange(n) / SR
    return x * np.exp(-t / 0.09) * np.minimum(1, t / 0.003)


def kick():
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = 52 + 70 * np.exp(-t / 0.035)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.13)


def clave():
    n = int(0.08 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 2450 * t) + 0.4 * np.sin(2 * np.pi * 1630 * t)) * np.exp(-t / 0.018)


def maraca(seed):
    n = int(0.09 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    z = z - lp1(z, 5500)
    return z * np.exp(-t / 0.028) * np.minimum(1, t / 0.006)


# ── melody: (midi, sixteenths); 0 = rest. Two 8-bar phrases ───────────────
MEL_A = [(69, 8), (74, 4), (76, 4), (77, 12), (76, 4), (74, 8), (72, 4), (74, 4), (77, 16),
         (79, 8), (77, 4), (74, 4), (70, 12), (72, 4), (69, 8), (73, 4), (76, 4), (69, 12), (0, 4)]
MEL_B = [(74, 4), (77, 4), (81, 8), (79, 8), (77, 4), (76, 4), (77, 12), (74, 4), (72, 16),
         (74, 4), (77, 4), (79, 8), (82, 8), (81, 8), (81, 8), (79, 4), (76, 4), (73, 8), (74, 8)]
assert sum(d for _, d in MEL_A) == 128 and sum(d for _, d in MEL_B) == 128


def render_lead(bus, send):
    """One continuous voice across each 8-bar phrase: gliding pitch,
    delayed vibrato, legato with a small dip at each new note."""
    for lap in range(-1, 2):
        for cyc, mel in ((1, MEL_A), (2, MEL_B)):
            t0 = lap * LOOP + cyc * 8 * BAR
            if t0 + 8 * BAR < -PRE * BAR or t0 > (BARS + POST) * BAR:
                continue
            n = int((8 * BAR + 1.2) * SR)
            f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n)
            pos = 0
            last = hz(mel[0][0])
            for m, d in mel:
                a, b = int(pos * S16 * SR), int((pos + d) * S16 * SR)
                if m:
                    f[a:b] = hz(m); last = hz(m)
                    tt = np.arange(b - a) / SR
                    g[a:b] = np.minimum(1, tt / 0.03) * (0.82 + 0.18 * np.exp(-tt / 0.25))
                    g[max(b - int(0.02 * SR), a):b] *= 0.85
                    vib[a:b] = np.clip((tt - 0.35) / 0.6, 0, 1)
                else:
                    f[a:b] = last
                pos += d
            f[pos * int(S16 * SR):] = last
            g = lp1(g, 30)
            fl = lfilter([1 - np.exp(-1 / (0.055 * SR))], [1, -np.exp(-1 / (0.055 * SR))], f)
            fl[:int(0.01 * SR)] = f[0]
            t = np.arange(n) / SR
            fl = fl * 2 ** (0.22 / 12 * vib * np.sin(2 * np.pi * 5.4 * t))
            ph = 2 * np.pi * np.cumsum(fl) / SR
            x = np.sin(ph) + 0.28 * np.sin(2 * ph) + 0.1 * np.sin(3 * ph)
            x = lp1(x, 3800) * g
            bus.add(t0, x, pan=0.08, gain=0.17)
            send.add(t0, x, pan=0.08, gain=0.10)


def pingpong(x, d, fb, reps, fc):
    y = np.zeros_like(x); dn = int(d * SR); tap = x.copy()
    for k in range(1, reps + 1):
        tap = lp1(tap, fc) * fb
        ch = k % 2
        y[dn * k:, ch] += tap[:len(x) - dn * k, ch] + tap[:len(x) - dn * k, 1 - ch] * 0.3
    return y


def phaser(x, period):
    """A swept comb (the string-machine 'jet'): the pad plus a copy delayed
    by 0.6-3.6 ms, the delay swept on a period that divides the loop."""
    t = (np.arange(len(x)) / SR) - T0
    d = (2.1 + 1.5 * np.sin(2 * np.pi * t / period)) / 1000 * SR
    idx = np.arange(len(x)) - d
    out = np.empty_like(x)
    for ch in range(2):
        dd = np.interp(idx + (0 if ch == 0 else 0.35 * SR / 1000), np.arange(len(x)), x[:, ch])
        out[:, ch] = x[:, ch] + 0.72 * dd
    return out * 0.6


def swoosh(bus, t0, dur, lo, hi, seed, gain, pan_from, pan_to):
    n = int(dur * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    f, tt, Z = stft(z, SR, nperseg=2048)
    u = tt / dur
    centre = lo * (hi / lo) ** np.sin(np.pi * np.clip(u, 0, 1))
    band = np.exp(-0.5 * (np.log(np.maximum(f[:, None], 1) / centre[None, :]) / 0.55) ** 2)
    _, y = istft(Z * band, SR, nperseg=2048)
    y = y[:n]
    e = np.sin(np.pi * np.clip(np.arange(n) / n, 0, 1)) ** 1.6
    y = y / (np.abs(y).max() + 1e-9) * e
    p = np.linspace(pan_from, pan_to, n)
    st = np.stack([y * np.cos((p + 1) * np.pi / 4), y * np.sin((p + 1) * np.pi / 4)], 1) * np.sqrt(2)
    bus.add(t0, st, gain=gain)


def make_ir(rt60=3.2):
    n = int(rt60 * 1.2 * SR); t = np.arange(n) / SR
    r = np.random.default_rng(11)
    ir = r.standard_normal((n, 2)) * np.exp(-6.9 * t / rt60)[:, None]
    ir = lp1(ir, 3000)
    ir[:int(0.02 * SR)] *= np.linspace(0, 1, int(0.02 * SR))[:, None]
    return ir / np.sqrt((ir ** 2).sum() / 2)


def render():
    pad, bass, arp, drums, sea, send = Bus(), Bus(), Bus(), Bus(), Bus(), Bus()
    for b in range(-PRE, BARS + POST):
        t = b * BAR
        root, tones = chord_at(b)
        # pad: a new chord every 2 bars, and the resolution on bar 7
        if b % 2 == 0 or b % 8 == 7:
            dur = (1 if (b % 8 in (6, 7)) else 2) * BAR
            for k, m in enumerate(tones):
                pad.add(t, pad_note(m, dur), pan=(-0.5, -0.15, 0.15, 0.5)[k], gain=0.20)
        # bass: bouncing eighths, octave and fifth
        if has('bass', b):
            pat = [0, 12, 0, 12, 7, 12, 0, 10]
            sweep = 380 + 520 * (0.5 - 0.5 * np.cos(2 * np.pi * ((b % 32) * BAR) / (LOOP / 2)))
            for i, iv in enumerate(pat):
                bass.add(t + i * 2 * S16, bass_note(root + 12 + iv, sweep * (1.25 if i % 2 else 1.0)),
                         gain=0.30 if i % 2 == 0 else 0.22)
        # arpeggio: sixteenths up and down the chord, an octave up
        if has('arp', b):
            order = [0, 1, 2, 3, 2, 1, 2, 3, 0, 1, 2, 3, 2, 3, 1, 2]
            for i, k in enumerate(order):
                a = arp_note(tones[k] + 12)
                arp.add(t + i * S16, a, pan=0.35 if i % 2 else -0.35, gain=0.055 + (0.02 if i % 4 == 0 else 0))
        # rhythm box: kick on 1, 2-and, 3; clave on the offbeat 16ths; maracas
        if has('drums', b):
            for s in (0, 6, 8):
                drums.add(t + s * S16, kick(), gain=0.30)
            for s in (3, 10, 14):
                drums.add(t + s * S16, clave(), pan=0.25, gain=0.045)
            for s in range(16):
                drums.add(t + s * S16, maraca(((b % 32) * 16 + s) + 7), pan=-0.3,
                          gain=0.05 if s % 2 else 0.028)
        # sea wind: a long swoosh every 4 bars, a bigger one into each cycle
        if b % 4 == 0:
            big = b % 8 == 0
            r = rng('sea', b % 32)
            lo, hi = (300, 5200) if big else (500, 2600 + 900 * r.random())
            swoosh(sea, t - (0.6 if big else 0), 4 * BAR + 0.6, lo, hi, (b % 32) + 100,
                   0.11 if big else 0.06, -0.7 if (b // 4) % 2 else 0.7, 0.7 if (b // 4) % 2 else -0.7)
    dry, wet = Bus(), Bus()
    render_lead(dry, wet)

    padx = phaser(pad.x, LOOP / 4)
    arpx = arp.x + pingpong(arp.x, 3 * S16, 0.42, 6, 3000)
    leadx = dry.x + pingpong(dry.x, 3 * S16, 0.28, 4, 2500) * 0.8
    rev_in = padx * 0.45 + arpx * 0.35 + wet.x + drums.x * 0.12 + sea.x * 0.4
    ir = make_ir(3.4)
    rev = np.stack([fftconvolve(rev_in[:, 0], ir[:, 0])[:N], fftconvolve(rev_in[:, 1], ir[:, 1])[:N]], 1)
    mix = padx + bass.x + arpx + drums.x + leadx + sea.x + rev * 0.55
    mix = mix - lp1(mix, 28)                        # no sub rumble
    a, b = smp(-PAD), smp(LOOP + PAD)
    out = mix[a:b]
    rms = np.sqrt(np.mean(out ** 2))
    out = out * (10 ** (-16.5 / 20) / rms)          # about the old track's level
    out = 0.95 * np.tanh(out / 0.95)                # soft ceiling, never past -0.4 dB
    return out


def main():
    out = render()
    # Periodic render: the half-second after the loop's end must be the
    # half-second after its start, sample for sample.
    i0, i1, k = smp(0) - smp(-PAD), smp(LOOP) - smp(-PAD), int(PAD * SR)
    wrap = float(np.abs(out[i1:i1 + k] - out[i0:i0 + k]).max())
    print(f'{len(out) / SR:.2f} s, loop {PAD} .. {PAD + LOOP}, peak {np.abs(out).max():.2f}, '
          f'rms {20 * np.log10(np.sqrt(np.mean(out ** 2))):.1f} dBFS, seam mismatch {wrap:.4f}')
    pcm = (np.clip(out, -1, 1) * 32767).astype('<i2').tobytes()
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    subprocess.run([ff, '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-',
                    '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', OUT], input=pcm, check=True)
    print('wrote', os.path.relpath(OUT, ROOT))
    if '--wav' in sys.argv:
        w = sys.argv[sys.argv.index('--wav') + 1]
        subprocess.run([ff, '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-', w],
                       input=pcm, check=True)
        print('wrote', w)


if __name__ == '__main__':
    main()
