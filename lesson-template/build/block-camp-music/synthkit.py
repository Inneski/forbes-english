"""Shared parts for the Block Camp soundtrack generators (neon.py, blossom.py).

A track is a LOOP rendered PERIODICALLY: the timeline starts PRE bars before
the loop and every event is placed from (bar mod BARS), so what plays before
bar 0 is literally the end of the previous lap and its echoes and reverb fall
across the seam exactly as on a real repeat. finish() keeps PAD seconds of
that continuation either side and measures the seam; the page's
data-loop="PAD PAD+LOOP" tells camp-music.js where to loop.

lakeside.py predates this file and carries its own copy of the same ideas.
"""
import os, subprocess, zlib
import numpy as np
import imageio_ffmpeg
from scipy.signal import fftconvolve, lfilter

SR = 48000
PAD = 0.5
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def rng(*key):
    return np.random.default_rng(zlib.crc32(repr(key).encode()))


class Timeline:
    def __init__(self, bpm, bars, pre=8, post=1, tail=6.0):
        self.bpm, self.bars, self.pre, self.post = bpm, bars, pre, post
        self.beat = 60 / bpm
        self.bar = 4 * self.beat
        self.s16 = self.beat / 4
        self.loop = bars * self.bar
        self.t0 = pre * self.bar
        self.n = int(((pre + bars + post) * self.bar + tail) * SR)

    def smp(self, t):
        return int(round((t + self.t0) * SR))

    def bars_range(self):
        return range(-self.pre, self.bars + self.post)

    def bus(self):
        return Bus(self)


class Bus:
    def __init__(self, tl):
        self.tl = tl
        self.x = np.zeros((tl.n, 2))

    def add(self, t, sig, pan=0.0, gain=1.0):
        i = self.tl.smp(t)
        if sig.ndim == 1:
            l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
            sig = np.stack([sig * l, sig * r], 1) * np.sqrt(2)
        n = self.tl.n
        j0, j1 = max(i, 0), min(i + len(sig), n)
        if j1 > j0:
            self.x[j0:j1] += sig[j0 - i:j1 - i] * gain


# ── filters ─────────────────────────────────────────────────────────────────
def lp1(x, fc):
    a = np.exp(-2 * np.pi * fc / SR)
    return lfilter([1 - a], [1, -a], x, axis=0)


def hp1(x, fc):
    return x - lp1(x, fc)


def _biquad(x, fc, q, kind):
    w = 2 * np.pi * min(fc, SR * 0.45) / SR
    al = np.sin(w) / (2 * q); c = np.cos(w)
    if kind == 'lp':
        b = [(1 - c) / 2, 1 - c, (1 - c) / 2]
    elif kind == 'hp':
        b = [(1 + c) / 2, -(1 + c), (1 + c) / 2]
    else:  # band-pass, constant peak
        b = [al, 0, -al]
    a = [1 + al, -2 * c, 1 - al]
    return lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)


def lp(x, fc, q=0.707):
    return _biquad(x, fc, q, 'lp')


def hp(x, fc, q=0.707):
    return _biquad(x, fc, q, 'hp')


def bp(x, fc, q=1.0):
    return _biquad(x, fc, q, 'bp')


def swept_lp(x, fc_start, fc_end, q=1.2, chunk=256):
    """A low-pass whose cutoff glides from fc_start to fc_end over the note
    (exponentially), filtered in short chunks with the state carried over."""
    n = len(x); out = np.empty(n); zi = np.zeros(2)
    for i in range(0, n, chunk):
        u = i / max(n - 1, 1)
        fc = fc_start * (fc_end / fc_start) ** u
        w = 2 * np.pi * min(fc, SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


# ── oscillators and envelopes ───────────────────────────────────────────────
def phase(f, n, ph=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,))
    return (ph + np.cumsum(f / SR)) % 1.0


def saw(f, n, ph=0.0):
    return 2 * phase(f, n, ph) - 1


def pulse(f, n, duty=0.5, ph=0.0):
    return np.where(phase(f, n, ph) < duty, 1.0, -1.0)


def tri(f, n, ph=0.0):
    return 2 * np.abs(2 * phase(f, n, ph) - 1) - 1


def supersaw(f, n, cents=(-11, -5, 0, 5, 11), seed=0):
    r = rng('ss', seed, round(f, 2))
    x = sum(saw(f * 2 ** (c / 1200), n, r.random()) for c in cents)
    return x / len(cents)


def adsr(n, a, d, s, r, gate):
    """gate: seconds held; r: release seconds after the gate."""
    t = np.arange(n) / SR
    e = np.where(t < a, t / max(a, 1e-4),
                 np.where(t < a + d, 1 - (1 - s) * (t - a) / max(d, 1e-4), s))
    rel = np.clip((t - gate) / max(r, 1e-4), 0, 1)
    return e * (1 - rel)


def perc(n, attack, tau):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(attack, 1e-4)) * np.exp(-t / tau)


# ── effects ─────────────────────────────────────────────────────────────────
def pingpong(x, d, fb, reps, fc):
    y = np.zeros_like(x); dn = int(round(d * SR)); tap = x.copy()
    for k in range(1, reps + 1):
        tap = lp1(tap, fc) * fb
        ch = k % 2
        if dn * k >= len(x):
            break
        y[dn * k:, ch] += tap[:len(x) - dn * k, ch] + tap[:len(x) - dn * k, 1 - ch] * 0.3
    return y


def make_ir(rt60, dark=3000, seed=11, pre=0.012):
    n = int(rt60 * 1.2 * SR); t = np.arange(n) / SR
    ir = np.random.default_rng(seed).standard_normal((n, 2)) * np.exp(-6.9 * t / rt60)[:, None]
    ir = lp1(ir, dark)
    k = int(pre * SR)
    ir = np.concatenate([np.zeros((k, 2)), ir])
    return ir / np.sqrt((ir ** 2).sum() / 2)


def reverb(x, ir):
    n = len(x)
    return np.stack([fftconvolve(x[:, 0], ir[:, 0])[:n], fftconvolve(x[:, 1], ir[:, 1])[:n]], 1)


def chorus(x, period, depth_ms=2.5, base_ms=7.0, mix=0.5, t0=0.0):
    """Two modulated taps, opposite phase per channel. period should divide
    the loop so the modulation is periodic too."""
    n = len(x); t = np.arange(n) / SR - t0
    out = x.copy()
    for ch in range(2):
        ph = 0 if ch == 0 else np.pi
        d = (base_ms + depth_ms * np.sin(2 * np.pi * t / period + ph)) / 1000 * SR
        out[:, ch] += mix * np.interp(np.arange(n) - d, np.arange(n), x[:, ch])
    return out / (1 + mix)


# ── out ─────────────────────────────────────────────────────────────────────
def record_loop(name, start, end):
    """block-camp/music/loops.json: where each track loops. deck_music.py
    reads it to write the pages' data-loop, so a re-render can never leave a
    page looping at the old length. Six decimals: sub-sample at 48 kHz."""
    import json
    p = os.path.join(ROOT, 'block-camp', 'music', 'loops.json')
    try:
        loops = json.load(open(p, encoding='utf-8'))
    except FileNotFoundError:
        loops = {}
    loops[name] = [round(start, 6), round(end, 6)]
    tmp = p + '.tmp'
    json.dump(dict(sorted(loops.items())), open(tmp, 'w', encoding='utf-8'), indent=1)
    os.replace(tmp, p)


def finish(tl, mix, name, target_db=-16.5, wav=None):
    mix = hp1(mix, 30)
    a, b = tl.smp(-PAD), tl.smp(tl.loop + PAD)
    out = mix[a:b]
    out = out * (10 ** (target_db / 20) / np.sqrt(np.mean(out ** 2)))
    out = 0.95 * np.tanh(out / 0.95)
    i0, i1, k = tl.smp(0) - a, tl.smp(tl.loop) - a, int(PAD * SR)
    seam = float(np.abs(out[i1:i1 + k] - out[i0:i0 + k]).max())
    print(f'{name}: {len(out) / SR:.2f} s, loop {PAD} .. {PAD + tl.loop:.2f}, peak {np.abs(out).max():.2f}, '
          f'rms {20 * np.log10(np.sqrt(np.mean(out ** 2))):.1f} dBFS, seam mismatch {seam:.4f}')
    assert seam < 1e-3, 'the loop is not periodic'
    pcm = (np.clip(out, -1, 1) * 32767).astype('<i2').tobytes()
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    dst = os.path.join(ROOT, 'block-camp', 'music', name + '.m4a')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    subprocess.run([ff, '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-',
                    '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', dst], input=pcm, check=True)
    print('wrote', os.path.relpath(dst, ROOT), f'   data-loop="{PAD} {PAD + tl.loop:g}"')
    record_loop(name, PAD, PAD + tl.loop)
    if wav:
        subprocess.run([ff, '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-', wav],
                       input=pcm, check=True)
    return out
