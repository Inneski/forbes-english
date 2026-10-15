#!/usr/bin/env python3
"""Block Camp soundtrack "Consequences" (Frankenstein Part II: Consequences - Going To Voxel RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". Part II is what the night
of the spark cost: the Creature alone, William and Justine, the glacier, the
cottage where he learns words by the fire, the island, the chase into the
Arctic ice. So: a gothic lament in a slow 6/8 lilt - a solo cello over a
harp, a falling "lament bass", a glass harmonica for the ice, a music box
for the cottage and the family he watches, wind, and a galloping chase north.
Sad and mysterious rather than frightening; tender, never gory. An original
piece in that idiom; nothing is taken from any film.

THE AMBITION MOTIF from Part I (frankenstein1.py: D4 A4 D5 E5 | F5 E5 D5 A4)
comes back here in B minor, on the cello, two octaves down in a slower
metre - B2 F#3 B3 C#4 | D4 C#4 B3 F#3, the same intervals - and now every
answer to it falls (bars 6-7: B A G, C# A#) over a bass that walks down
B A G F#. In C the violins take it two octaves up for the chase.

B minor, 6/8, an eighth exactly 19200 samples (0.4 s; a dotted quarter = 50,
a bar 2.4 s). One chord a bar:

  intro  Bm | Bm | G | F#                               bars 0-3    the ice: wind, the glass harmonica alone,
                                                                    a low B drone
  A      Bm | Bm7/A | G | F# | Bm | D | Em | F#         bars 4-11   the lament: the motif on the cello, harp
                                                                    arpeggios, a soft heartbeat, the bass
                                                                    walking down B A G F#
  B      D | A/C# | Bm | G | D | A | Em | F#            bars 12-19  the cottage: a music-box tune in D, the
                                                                    cello under it, pizzicato bass walking
                                                                    D C# B, string pad, a fire crackling
  C      Bm | G | Em | F# | Bm | G | C | F#7            bars 20-27  the chase north: galloping low strings,
                                                                    timpani, the motif on the violins two
                                                                    octaves up, the Neapolitan C, the wind
  coda   Em | Bm | F#sus4 | F#                          bars 28-31  the far north: the music box plays the
                                                                    motif's head slowly, the cello sinks to
                                                                    A#, the wind takes it back to the top

check_lines() proves the harmony at every render: every cello, violin,
music-box and glass note a quarter or longer, or on either beat of the bar
(eighth 0 or 3), is a tone of its chord and sits no semitone or minor ninth
from the bass, the pads, the harp or the gallop under it; every pad, harp,
gallop, bass, timpani and heartbeat pitch is a chord tone; no voicing holds a
semitone. The named dissonances, each an eighth, off the beat: the C# passing
from D to B in the motif's second bar (5, and 21 and 29 two octaves up: C#
against the pad's D for 0.4 s; over G in 21 a passing tritone), the A
passing between B and G (6, 22), the E passing under F# (9, 16 in the music
box), the B5 passing between C#6 and A5 (13).

Instruments, all synthesised here:
  Cello       a band-limited saw through a body (resonances near 280 Hz,
              650 Hz, 1.7 kHz, 3.2 kHz), rosin noise, a scoop into each note,
              vibrato that grows in, a swell over long notes; the violins are
              the same, three a note, an octave pair, brighter.
  Harp        Karplus-Strong strings (grand_hotel.py's), a soft pick.
  Music box   a steel tine: fundamental, a fast 5.4x overtone, a click.
  Glass       a glass harmonica: two sines a hair apart (a slow beat), a
              rubbed attack, a little 2nd and 3rd partial.
  Low strings bowed contrabass, pizzicato in B, a staccato gallop in C.
  Percussion  timpani on B and F#, a heartbeat (two soft thumps on B1 or F#1).
  Air         wind (noise through slow, wandering band-passes), the fire in
              the cottage (pops and a low breath).
32 bars = 76.8 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/frankenstein2.py [--wav preview.wav] [--stems stems.npz]
"""
import sys
import numpy as np
from scipy.signal import lfilter, fftconvolve
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, make_ir, reverb, chorus, finish)

NAME = 'frankenstein-consequences'
BARS = 32
tl = Timeline(bpm=100, bars=BARS)              # synthkit counts 4/4: 4 x 0.6 s = one 6/8 bar of 2.4 s
BAR = tl.bar
E8 = BAR / 6
DQ = 3 * E8
LOOP = tl.loop
assert abs(E8 * SR - 19200) < 1e-6

# ── the changes ─────────────────────────────────────────────────────────────
CH = {
    'Bm':     dict(pcs={11, 2, 6},     bass=35, pad=[59, 62, 66, 71]),
    'Bm7/A':  dict(pcs={11, 2, 6, 9},  bass=33, pad=[57, 62, 66, 71]),
    'G':      dict(pcs={7, 11, 2},     bass=31, pad=[55, 59, 62, 67]),
    'F#':     dict(pcs={6, 10, 1},     bass=30, pad=[54, 58, 61, 66]),
    'D':      dict(pcs={2, 6, 9},      bass=38, pad=[57, 62, 66, 69]),
    'Em':     dict(pcs={4, 7, 11},     bass=40, pad=[55, 59, 64, 67]),
    'A/C#':   dict(pcs={9, 1, 4},      bass=37, pad=[57, 61, 64, 69]),
    'A':      dict(pcs={9, 1, 4},      bass=33, pad=[57, 61, 64, 69]),
    'C':      dict(pcs={0, 4, 7},      bass=36, pad=[55, 60, 64, 67]),
    'F#7':    dict(pcs={6, 10, 1, 4},  bass=30, pad=[52, 58, 61, 66]),
    'F#sus4': dict(pcs={6, 11, 1},     bass=30, pad=[54, 59, 61, 66]),
}
CHORDS = (['Bm', 'Bm', 'G', 'F#'] +
          ['Bm', 'Bm7/A', 'G', 'F#', 'Bm', 'D', 'Em', 'F#'] +
          ['D', 'A/C#', 'Bm', 'G', 'D', 'A', 'Em', 'F#'] +
          ['Bm', 'G', 'Em', 'F#', 'Bm', 'G', 'C', 'F#7'] +
          ['Em', 'Bm', 'F#sus4', 'F#'])
assert len(CHORDS) == BARS


def section(lb):
    return 'intro' if lb < 4 else 'A' if lb < 12 else 'B' if lb < 20 else 'C' if lb < 28 else 'coda'


# ── the tunes: (midi, eighths) per bar, six eighths, 0 = rest ───────────────
MOTIF = [(47, 2), (54, 1), (59, 2), (61, 1)]            # B2 F#3 B3 C#4      Part I's motif, in B minor
CELLO = {
    4: MOTIF,
    5: [(62, 2), (61, 1), (59, 2), (54, 1)],            # Bm7/A  D4 C#4 B3 F#3
    6: [(59, 2), (57, 1), (55, 3)],                     # G      B3 A3 G3      falling
    7: [(61, 3), (58, 3)],                              # F#     C#4 A#3       falling to the leading note
    8: MOTIF,
    9: [(62, 3), (66, 2), (64, 1)],                     # D      D4 F#4 E4
    10: [(67, 2), (66, 1), (64, 3)],                    # Em     G4 F#4 E4
    11: [(66, 3), (61, 3)],                             # F#     F#4 C#4
    12: [(54, 6)], 13: [(52, 6)], 14: [(50, 6)],        # B: long notes under the music box
    15: [(55, 3), (59, 3)], 16: [(57, 6)], 17: [(57, 3), (61, 3)], 18: [(59, 6)], 19: [(58, 3), (61, 3)],
    28: [(52, 6)], 29: [(54, 6)], 30: [(47, 6)], 31: [(46, 6)],     # coda: E F# B A#, home to B
}
MBOX = {
    12: [(78, 2), (81, 1), (86, 3)],                    # D      F#5 A5 D6
    13: [(85, 2), (83, 1), (81, 3)],                    # A/C#   C#6 B5 A5
    14: [(83, 2), (86, 1), (90, 3)],                    # Bm     B5 D6 F#6
    15: [(86, 2), (83, 1), (79, 3)],                    # G      D6 B5 G5
    16: [(78, 2), (81, 1), (86, 2), (85, 1)],           # D      F#5 A5 D6 C#6
    17: [(88, 3), (85, 3)],                             # A      E6 C#6
    18: [(83, 2), (79, 1), (76, 3)],                    # Em     B5 G5 E5
    19: [(82, 3), (78, 3)],                             # F#     A#5 F#5
    28: [(71, 2), (78, 1), (83, 3)],                    # Em     B4 F#5 B5     the motif's head, slowly
    29: [(86, 2), (85, 1), (83, 3)],                    # Bm     D6 C#6 B5
    30: [(83, 6)],                                      # F#sus4 B5
    31: [(82, 3), (0, 3)],                              # F#     A#5
}
VIOLIN = {
    20: [(71, 2), (78, 1), (83, 2), (85, 1)],           # Bm     B4 F#5 B5 C#6  the motif, two octaves up
    21: [(86, 2), (85, 1), (83, 2), (79, 1)],           # G      D6 C#6 B5 G5
    22: [(83, 2), (81, 1), (79, 3)],                    # Em     B5 A5 G5
    23: [(78, 3), (82, 3)],                             # F#     F#5 A#5
    24: [(71, 2), (78, 1), (83, 2), (85, 1)],           # Bm     the motif again
    25: [(86, 3), (83, 3)],                             # G      D6 B5
    26: [(84, 3), (79, 2), (76, 1)],                    # C      C6 G5 E5       the Neapolitan
    27: [(82, 3), (76, 3)],                             # F#7    A#5 E5
}
GLASS = {1: [(78, 6)], 2: [(79, 6)], 3: [(78, 3), (82, 3)]}     # intro: F#5 G5 F#5 A#5
for row in list(CELLO.values()) + list(MBOX.values()) + list(VIOLIN.values()) + list(GLASS.values()):
    assert sum(d for _, d in row) == 6, row

HARP_A = [0, 1, 2, 3, 4, 3]                             # into the voicing, bass+12 first
HARP_B = [0, 2, 1, 3, 2, 4]
GALLOP = [(0, 0, 2), (2, 7, 1), (3, 0, 2), (5, 7, 1)]   # (eighth, interval over the root, eighths): long-short


def harp_tones(c):
    v = CH[c]
    return [v['bass'] + 12] + v['pad']


def gallop_tones(c):
    r = CH[c]['bass'] + 12
    return [r + iv for _, iv, _ in GALLOP]


def drum_note(c, lo, hi):
    """The B or the F# (timpani B2/F#2, heartbeat B1/F#1) the chord holds."""
    pcs = CH[c]['pcs']
    return lo if lo % 12 in pcs else hi if hi % 12 in pcs else None


def check_lines():
    """Every melody note a quarter or longer, or on either beat of a 6/8 bar,
    is a chord tone and no semitone or minor ninth from what is held under
    it; every accompaniment pitch is a chord tone; no voicing holds a
    semitone."""
    bad = []
    rub = (1, 13, 25, 37)
    for name, tune in (('cello', CELLO), ('music box', MBOX), ('violins', VIOLIN), ('glass', GLASS)):
        for lb, row in tune.items():
            c = CH[CHORDS[lb]]
            under = [c['bass']] + c['pad'] + [p + 12 for p in c['pad']] + harp_tones(CHORDS[lb])
            if section(lb) == 'C':
                under += gallop_tones(CHORDS[lb])
            pos = 0
            for m, d in row:
                if m and (d >= 2 or pos % 3 == 0):
                    if m % 12 not in c['pcs']:
                        bad.append((name, lb, pos, m, CHORDS[lb], 'not a chord tone'))
                    if any(abs(m - v) in rub for v in under):
                        bad.append((name, lb, pos, m, CHORDS[lb], 'rubs'))
                pos += d
    for c, v in CH.items():
        if v['bass'] % 12 not in v['pcs']:
            bad.append(('bass', c))
        used_in_c = any(CHORDS[lb] == c and section(lb) == 'C' for lb in range(BARS))
        for nm, ms in (('pad', v['pad']), ('harp', harp_tones(c)), ('gallop', gallop_tones(c) if used_in_c else [])):
            if any(m % 12 not in v['pcs'] for m in ms):
                bad.append((nm, c))
        ms = sorted(set(v['pad'] + harp_tones(c)))
        if any((hi - lo) in rub for i, lo in enumerate(ms) for hi in ms[i + 1:]):
            bad.append(('voicing', c, 'semitone'))
    for lb in range(BARS):
        if section(lb) == 'A' and drum_note(CHORDS[lb], 35, 30) is None:
            bad.append(('heartbeat', lb))
    print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad)
    assert not bad, 'a wrong note (listed above)'


check_lines()


# ── oscillators ─────────────────────────────────────────────────────────────
def blep_saw(f, n, ph0=0.0):
    """A saw with polyBLEP corners (rainfall.py), so high notes do not alias."""
    f = np.broadcast_to(np.asarray(f, float), (n,))
    dt = f / SR
    p = (ph0 + np.cumsum(dt)) % 1.0
    y = 2 * p - 1
    m = p < dt
    u = p[m] / dt[m]; y[m] -= u + u - u * u - 1
    m = p > 1 - dt
    u = (p[m] - 1) / dt[m]; y[m] -= u * u + u + u + 1
    return y


def tv_bp(x, fc, q, chunk=256):
    """Band-pass with centre fc[j] for the chunk starting at sample j*chunk."""
    out = np.empty_like(x); zi = np.zeros(2)
    for j, i in enumerate(range(0, len(x), chunk)):
        w = 2 * np.pi * min(fc[min(j, len(fc) - 1)], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


# ── bowed strings ───────────────────────────────────────────────────────────
def bowed(m, dur, v, seed, voices=(0,), bright=1.0, vib=16, att=0.09, rel=0.2):
    """A bowed string: a scoop into the note, vibrato that grows in after a
    quarter of a second, rosin noise, a swell over long notes, a body."""
    n = int((dur + rel + 0.05) * SR); t = np.arange(n) / SR
    r = rng('bow', seed)
    rate = 5.2 + 0.4 * r.random()
    cents = -14 * np.exp(-t / 0.06) + vib * np.clip((t - 0.25) / 0.45, 0, 1) * np.sin(2 * np.pi * rate * t + r.uniform(0, 6.3))
    f = hz(m) * 2 ** (cents / 1200)
    x = sum(blep_saw(f * 2 ** (c / 1200), n, r.random()) for c in voices) / len(voices)
    z = r.standard_normal(n)
    x += (0.035 * hp(z, 2500) + 0.025 * bright * hp(z, 7000)) * (1 + 3 * np.exp(-t / 0.04))
    x = lp(x, 2500 + 4500 * bright, 0.7)
    body = x + 0.8 * bp(x, 280, 1.6) + 0.55 * bp(x, 650, 2.0) + 0.35 * bp(x, 1700, 1.5) + 0.3 * bright * bp(x, 3200, 1.2)
    swell = 0.82 + 0.18 * np.sin(np.pi * np.clip(t / max(dur, 0.1), 0, 1))
    return body * adsr(n, att, 0.2, 0.9, rel, dur) * swell * v


def stacc(m, dur, v, seed):
    f = hz(m); n = int((dur + 0.08) * SR); t = np.arange(n) / SR
    r = rng('stacc', seed)
    x = 0.5 * blep_saw(f * 2 ** (-7 / 1200), n, r.random()) + 0.5 * blep_saw(f * 2 ** (7 / 1200), n, r.random())
    x = lp(x, 1600 + 2400 * v, 0.7) + 0.6 * bp(x, 300, 1.4)
    x += 0.1 * bp(r.standard_normal(n), 2400, 1.2) * np.exp(-t / 0.015)
    env = np.minimum(1, t / 0.006) * (0.6 + 0.4 * np.exp(-t / 0.08)) * np.clip((dur + 0.07 - t) / 0.07, 0, 1)
    return x * env * v


# ── plucked: Karplus-Strong, as grand_hotel.py ──────────────────────────────
def ks_setup(f, a, t60):
    L = SR / f
    N = int(np.floor(L - (1 - a) - 0.1))
    d = L - (1 - a) - N
    c = (1 - d) / (1 + d)
    g = 10 ** (-3 / (t60 * f))
    den = np.zeros(N + 3)
    den[0] = 1.0; den[1] = c
    den[N] -= g * a * c
    den[N + 1] -= g * (a + (1 - a) * c)
    den[N + 2] -= g * (1 - a)
    return N, c, den


def pick(N, f, tilt, noise, comb, seed, top=6000):
    kk = np.arange(1, int(max(2, min(48, top / f))) + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -tilt * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    exc += noise * lp1(np.random.default_rng(seed).uniform(-1, 1, N), 3500)
    k = max(1, int(comb * N))
    exc[k:] -= 0.5 * exc[:-k]
    # taper both ends: an excitation that stops on a non-zero sample is a click
    # (measured on the pizzicato, a 0.14 step 6.8 ms into every D3)
    j = max(2, N // 10)
    exc[-j:] *= 0.5 + 0.5 * np.cos(np.pi * np.arange(1, j + 1) / j)
    exc[:3] *= np.array([0.25, 0.5, 0.75])[:min(3, N)]
    return exc / np.abs(exc).max()


def harp(m, ring, v, seed):
    f = hz(m)
    N, c, den = ks_setup(f, 0.8, float(np.interp(m, [40, 90], [5.0, 2.2])))
    exc = pick(N, f, 0.9, 0.06, 0.18, seed, top=10000)
    n = int((ring + 0.15) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    return y * np.minimum(1, t / 0.001) * np.clip((ring + 0.12 - t) / 0.12, 0, 1)


def pizz(m, v, seed, ring=0.9):
    f = hz(m)
    N, c, den = ks_setup(f, 0.55, 1.2)
    exc = pick(N, f, 1.6, 0.04, 0.22, seed, top=1500)
    n = int((ring + 0.1) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    y = y + 0.4 * bp(y, 2.2 * f, 1.0)
    t = np.arange(n) / SR
    return y * np.minimum(1, t / 0.002) * np.clip((ring + 0.08 - t) / 0.08, 0, 1)


# ── bells and glass ─────────────────────────────────────────────────────────
def musicbox(m, v=1.0):
    f = hz(m); n = int(2.2 * SR); t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 1.3) + 0.1 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.5)
         + 0.3 * np.sin(2 * np.pi * 5.4 * f * t) * np.exp(-t / 0.1))
    if 11.2 * f < 16000:
        x += 0.1 * np.sin(2 * np.pi * 11.2 * f * t) * np.exp(-t / 0.035)
    z = np.random.default_rng(int(m)).standard_normal(n)
    x += 0.07 * hp(z, 3000) * np.exp(-t / 0.003)
    return x * np.minimum(1, t / 0.0006) * v


def glass(m, dur, seed, att=0.35, rel=0.7):
    """A glass harmonica: two sines a hair apart beat slowly; the wet-finger
    attack rubs in."""
    f = hz(m); n = int((dur + rel + 0.05) * SR); t = np.arange(n) / SR
    r = rng('glass', seed)
    x = (np.sin(2 * np.pi * f * t + r.uniform(0, 6.3)) + np.sin(2 * np.pi * f * 1.0016 * t + r.uniform(0, 6.3))
         + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)) / 2.2
    rub = 0.04 * bp(r.standard_normal(n), 2 * f, 4.0) * np.exp(-t / 0.25)
    return (x + rub) * adsr(n, att, 0.3, 0.85, rel, dur)


def ice(m, v=1.0):
    """A crystal of ice: a tiny high bell, gone in a third of a second."""
    f = hz(m); n = int(0.5 * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.22) + 0.3 * np.sin(2 * np.pi * 2.76 * f * t) * np.exp(-t / 0.05)
    return x * np.minimum(1, t / 0.0008) * v


# ── percussion ──────────────────────────────────────────────────────────────
def timp(m, v, seed, length=2.4):
    f = hz(m); n = int(length * SR); t = np.arange(n) / SR
    bend = np.cumsum(1 + 0.012 * np.exp(-t / 0.08)) / SR
    x = np.zeros(n)
    for r_, a, tau in ((1, 1, 1.2), (1.5, 0.5, 0.75), (1.98, 0.32, 0.5), (2.44, 0.16, 0.35), (2.92, 0.08, 0.25)):
        x += a * np.sin(2 * np.pi * f * r_ * bend) * np.exp(-t / tau)
    x += 0.4 * lp(np.random.default_rng(seed).standard_normal(n), 300) * np.exp(-t / 0.02)
    return x * np.minimum(1, t / 0.003) * np.clip((length - t) / 0.05, 0, 1) * v


def heart(m, v=1.0):
    """Lub-dub: two soft thumps, settling onto the pitch m."""
    n = int(1.0 * SR); t = np.arange(n) / SR
    out = np.zeros(n)
    for t0, a in ((0.0, 1.0), (0.21, 0.7)):
        i = int(t0 * SR); tt = t[:n - i]
        f = hz(m) * (1 + 0.6 * np.exp(-tt / 0.025))
        out[i:] += a * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.11) * np.minimum(1, tt / 0.004)
    return lp(out, 400) * np.clip((1.0 - t) / 0.1, 0, 1) * v


# ── the air ─────────────────────────────────────────────────────────────────
_t = np.arange(int(0.012 * SR)) / SR
POP = np.random.default_rng(8).standard_normal(len(_t)) * np.exp(-_t / 0.002)


def air_grain(key, kind):
    """Two bars under a sine window; laid a bar apart, the power sums flat.
    'wind': noise through two band-passes that wander (the whistle) and a
    breath of high air; 'fire': pops and a low breath."""
    n = int(2 * BAR * SR)
    r = rng(kind, key)
    z = r.standard_normal((n, 2))
    nc = n // 1024 + 1
    u = np.arange(nc) / nc
    if kind == 'wind':
        y = np.zeros((n, 2))
        for ch in range(2):
            for base, q, a in ((520, 3.5, 1.0), (1300, 5.0, 0.5)):
                fc = base * 2 ** (0.9 * np.sin(2 * np.pi * (u * r.uniform(0.6, 1.4) + r.random()))
                                  + 0.3 * np.sin(2 * np.pi * (3 * u + r.random())))
                y[:, ch] += a * tv_bp(z[:, ch], fc, q, chunk=1024)
        y += 0.5 * lp(hp(z, 5000), 12000)
    else:
        k = int(14 * 2 * BAR) * 2
        imp = np.zeros((n, 2))
        np.add.at(imp, (r.integers(0, n, k), r.integers(0, 2, k)), np.minimum(r.pareto(2.0, k), 5) * r.choice((-1.0, 1.0), k))
        y = 1.5 * lp(hp(fftconvolve(imp, POP[:, None])[:n], 700), 7000) + 0.3 * lp(hp(z, 150), 700)
    return y * np.sin(np.pi * (np.arange(n) + 0.5) / n)[:, None]


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    lead, vln, mbox, gls, hrp, pad, low, perc_, wind, fire, ice_bus = (tl.bus() for _ in range(11))
    for b in tl.bars_range():
        t = b * BAR
        lb = b % BARS
        sec, c = section(lb), CHORDS[lb]
        v = CH[c]

        # the bass: a bowed drone in the intro, a bowed note a bar in A and C
        # and the coda, pizzicato on both beats in B
        if sec == 'intro':
            if lb == 0:
                low.add(t, bowed(v['bass'], 2 * BAR - 0.1, 1.0, lb, voices=(-6, 6), bright=0.0, vib=4, att=0.8,
                                 rel=0.4), gain=0.2)
            elif lb >= 2:
                low.add(t, bowed(v['bass'], BAR - 0.08, 1.0, lb, voices=(-6, 6), bright=0.0, vib=4, att=0.3,
                                 rel=0.3), gain=0.2)
        elif sec == 'B':
            for q in (0, 3):
                low.add(t + q * E8, pizz(v['bass'] + 12, 1.0 if q == 0 else 0.8, lb * 4 + q), gain=0.36)
        else:
            low.add(t, bowed(v['bass'], BAR - 0.06, 1.0, lb, voices=(-6, 6), bright=0.0, vib=5, att=0.12, rel=0.25),
                    gain=0.2 if sec != 'C' else 0.18)

        # harp: rising arpeggios in A, a rocking figure in B, a few notes in the coda
        ht = harp_tones(c)
        if sec in ('A', 'B'):
            pat = HARP_A if sec == 'A' else HARP_B
            for k, ix in enumerate(pat):
                m = ht[ix]
                hrp.add(t + k * E8, harp(m, min(BAR - k * E8 + 0.3, 2.0), 0.9 if k in (0, 3) else 0.7, lb * 8 + k),
                        pan=-0.45 + (m - 45) / 30 * 0.7, gain=0.3 if sec == 'A' else 0.22)
        elif sec == 'coda' or lb == 3:
            for k, ix in ((0, 0), (3, 2)):
                m = ht[ix]
                hrp.add(t + k * E8, harp(m, 2.0, 0.7, lb * 8 + k), pan=-0.3, gain=0.22)

        # string pad in B and C; the glass harmonica on top in the intro, A, C and the coda
        if sec in ('B', 'C'):
            for k, m in enumerate(v['pad']):
                pad.add(t, bowed(m, BAR - 0.08, 1.0, lb * 8 + k, voices=(-8, 0, 7), bright=0.5, vib=8, att=0.35,
                                 rel=0.25), pan=(-0.6, -0.2, 0.2, 0.6)[k], gain=0.045 if sec == 'B' else 0.05)
        if sec in ('intro', 'A', 'C', 'coda'):
            g = {'intro': 0.07, 'A': 0.042, 'C': 0.05, 'coda': 0.07}[sec]
            for k, m in enumerate(v['pad'][1:]):
                gls.add(t, glass(m + 12, BAR - 0.1, lb * 8 + k), pan=(-0.5, 0.0, 0.5)[k], gain=g)

        # the gallop and the timpani in C; heartbeats in A
        if sec == 'C':
            for (e8, iv, d), m in zip(GALLOP, gallop_tones(c)):
                low.add(t + e8 * E8, stacc(m, d * E8 * 0.6, 1.0 if e8 in (0, 3) else 0.75, lb * 8 + e8),
                        pan=-0.2, gain=0.13)
                low.add(t + e8 * E8 + 0.004, stacc(m + 12, d * E8 * 0.6, 0.8 if e8 in (0, 3) else 0.6, lb * 8 + e8 + 50),
                        pan=0.2, gain=0.08)
            tn = drum_note(c, 47, 42)
            if tn is not None and lb not in (23, 27):
                perc_.add(t, timp(tn, 0.9, lb), pan=-0.1, gain=0.18)
                perc_.add(t + 3 * E8, timp(tn, 0.6, lb + 40), pan=-0.1, gain=0.14)
        if lb in (23, 27, 31):                         # rolls on F#
            steps = 18
            for k in range(steps):
                vv = (0.1 + 0.5 * (k / steps) ** 1.4) * (0.6 if lb == 31 else 1.0)
                perc_.add(t + k * BAR / steps, timp(42, vv, 600 + lb * 20 + k, length=0.8), pan=-0.1, gain=0.15)
        if sec == 'A':
            hn = drum_note(c, 35, 30)
            perc_.add(t, heart(hn, 1.0), gain=0.32)
            perc_.add(t + 3 * E8, heart(hn, 0.75), gain=0.32)

        # ice crystals: chord tones scattered high in the cold sections
        n_ice = {'intro': 5, 'A': 2, 'C': 4, 'coda': 6}.get(sec, 0)
        if n_ice:
            r = rng('ice', lb)
            tones = sorted({p % 12 for p in v['pad']})
            for _ in range(n_ice):
                m = 96 + int(r.choice(tones))
                ice_bus.add(t + int(r.integers(0, 12)) * E8 / 2, ice(m, float(r.uniform(0.5, 1.0))),
                            pan=float(r.uniform(-0.8, 0.8)), gain=0.045)

        # air: wind outside, the fire in the cottage
        wl = {'intro': 1.0, 'A': 0.45, 'B': 0.0, 'C': 0.8, 'coda': 1.0}[sec]
        if lb == 11:
            wl = 0.25
        if wl:
            wind.add(t, air_grain(lb, 'wind'), gain=0.05 * wl)
        if sec == 'B' or lb == 11:
            fire.add(t, air_grain(lb, 'fire'), gain=0.065 if lb != 11 else 0.03)

        # the tunes
        if lb in CELLO:
            pos = 0
            for m, d in CELLO[lb]:
                if m:
                    g = 0.16 if sec == 'A' else 0.11 if sec == 'B' else 0.14
                    lead.add(t + pos * E8, bowed(m, d * E8 + 0.04, 1.0 if pos % 3 == 0 else 0.85, lb * 64 + pos),
                             pan=-0.1, gain=g)
                pos += d
        if lb in VIOLIN:
            pos = 0
            for m, d in VIOLIN[lb]:
                if m:
                    for o, g, pn in ((0, 0.13, 0.15), (-12, 0.09, -0.25)):
                        vln.add(t + pos * E8, bowed(m + o, d * E8 + 0.03, 1.0 if pos % 3 == 0 else 0.85,
                                                    lb * 64 + pos + o, voices=(-7, 0, 6), bright=1.0, vib=14,
                                                    att=0.05), pan=pn, gain=g)
                pos += d
        if lb in MBOX:
            pos = 0
            for m, d in MBOX[lb]:
                if m:
                    mbox.add(t + pos * E8, musicbox(m, 1.0 if pos % 3 == 0 else 0.8), pan=0.35,
                             gain=0.11 if sec == 'B' else 0.09)
                pos += d
        if lb in GLASS:
            pos = 0
            for m, d in GLASS[lb]:
                gls.add(t + pos * E8, glass(m, d * E8 - 0.05, lb * 64 + pos, att=0.25, rel=0.5), pan=0.2, gain=0.09)
                pos += d

    padx = chorus(pad.x, LOOP / 16, depth_ms=2.5, base_ms=8.0, mix=0.4, t0=tl.t0)
    glsx = chorus(gls.x, LOOP / 24, depth_ms=1.5, base_ms=6.0, mix=0.35, t0=tl.t0)
    hall = make_ir(3.0, dark=4500, seed=47, pre=0.03)
    stems = dict(cello=lead.x, violins=vln.x, musicbox=mbox.x, glass=glsx, harp=hrp.x, pad=padx, low=low.x,
                 percussion=perc_.x, wind=wind.x, fire=fire.x, ice=ice_bus.x)
    sends = dict(cello=0.45, violins=0.45, musicbox=0.55, glass=0.6, harp=0.45, pad=0.45, low=0.12,
                 percussion=0.3, wind=0.25, fire=0.15, ice=0.6)
    wet = reverb(sum(stems[k] * sends[k] for k in stems), hall) * 0.55
    stems['reverb'] = wet
    mix = sum(stems.values())
    for nm, bus in stems.items():
        print('  %-11s rms %6.1f dB rel. mix' % (nm, 20 * np.log10(np.sqrt(np.mean(bus ** 2)) / np.sqrt(np.mean(mix ** 2)) + 1e-12)))
    if '--stems' in sys.argv:
        i0, i1 = tl.smp(-0.5), tl.smp(tl.loop + 0.5)
        np.savez(sys.argv[sys.argv.index('--stems') + 1], a=0, b=i1 - i0,
                 **{k: v[i0:i1].astype(np.float32) for k, v in stems.items()})
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
