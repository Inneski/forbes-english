#!/usr/bin/env python3
"""Block Camp soundtrack "Tidewater" (Present Perfect): a rolling 12/8 sea song.

Innes, 2026-09-30: "for Present Perfect a sound similar to Ween's 'The
Mollusk'", and he listed what he meant: an uncommon 12/8 time signature with a
rolling, wave-like cadence; a gentle, relaxing acoustic-guitar melody layered
with swirling, atmospheric psychedelic keyboards; dreamy, ethereal trumpet
solos that drift in, in the middle and again later. The original's spoken-word
section is left out. An original piece in that idiom: no melody, riff or
progression is taken from the record.

D major with a mixolydian C (bVII), 12/8 at a dotted-quarter pulse of 58.2 a
minute (an eighth is exactly 16500 samples, a bar 4.125 s). One chord a bar:

    A   D      Cadd9  G      D           bars 0-3    guitar, sea, organ; bass and shaker from bar 2
    B   Bm7    Gmaj7  Em7    A7sus4 A7   bars 4-7    trumpet solo 1
    A'  D      Cadd9  G      D           bars 8-11   the guitar melody, hand drum
    C   Gmaj7  Gm6    D/F#   A7sus4 A7   bars 12-15  mellotron flute, the organ at its fullest
    B'  Bm7    Gmaj7  Em7    A7sus4 A7   bars 16-19  trumpet solo 2, easing back into A

(D/F# is Dmaj7 over F#.) Instruments, all synthesised here: a fingerpicked
steel-string guitar made of Karplus-Strong strings (tuned exactly by an
all-pass in the loop, a body resonance after), a bass note on every dotted beat
and a soft strum spread on each downbeat, strings damped when the chord changes
under them, plus a single-string melody in A'; a drawbar organ through a slow
phaser and a chorale-speed rotary speaker; a mellotron-style flute with tape
wow; a round soft bass; a brushed shaker and a hand drum tuned to D3 and E4;
sea-wash noise breaking every two bars; and a trumpet (band-limited harmonics
that brighten as it swells, a formant near 1.25 kHz, breath at the attack, a
scoop into each note, lip vibrato that deepens on long notes) through a
dotted-quarter echo and a long reverb.

Innes, 2026-10-01: "a SUB 37 keyboard playing 2 square wave LFOs modulating
the oscillators slightly off pitch with each other at the equivalent of a 2nd
and 4th, short attack long delay and release, filter settings pretty low". So
a Moog Sub 37 patch, mono, one note a chord (two in the sus4 bar), all the
way through (level by section A .55, B 1, A' .65, C .9, B' 1): oscillator 1
a saw at -4 cents, its square LFO (120 cycles a lap, 1.455 Hz) stepping it up
a major 2nd and back; oscillator 2 a square at +5 cents, its square LFO (124 a
lap, 1.503 Hz) stepping it up a perfect 4th, so the two drift in and out of
step four times a lap. Steps slewed ~4 ms, 25 ms glide between notes. Slight
tanh drive into a four-pole low-pass (two biquads, Q .54 and 1.1) at 260 Hz +
1.2x the note + a 520 Hz filter envelope decaying over 1.4 s: 400 Hz-1 kHz.
Amp: 10 ms attack, a slow decay to .62, released after 70% of the note
(tau .75 s, about 2.2 s to -25 dB), retriggered mono. A dotted-half (two
beats, 2.06 s) ping-pong echo, feedback .42, repeats low-passed at 1.1 kHz,
then the reverb. Each note's base is searched so that it, its 2nd and its 4th
all sit a tone or more from everything sounding there (on D the root's 4th, G,
would rub the F#, so it plays A-B-D). 20 bars = 82.5 s, a seamless loop (see
synthkit.py).

Checked in code at import: every long or on-beat note of the solos, the guitar
melody and the flute is a chord tone; every bass note is a chord tone and sits
neither a semitone nor a minor ninth from anything the guitar or organ holds;
every Sub 37 pitch (base, 2nd, 4th) is in the key and no semitone, major
seventh or minor ninth from the chord, guitar, organ, bass or line above it.

    py lesson-template/build/block-camp-music/tidewater.py [--wav preview.wav] [--stems]
"""
import re, sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

E8 = 0.34375                     # an eighth: 16500 samples
BEAT = 3 * E8                    # the dotted quarter, 58.2 a minute
BAR = 12 * E8                    # 4.125 s
BARS = 20
tl = Timeline(bpm=60 / BEAT, bars=BARS, pre=4, post=1)
LOOP = BARS * BAR                # 82.5 s
assert abs(tl.bar - BAR) < 1e-9 and abs(tl.loop - LOOP) < 1e-9
CHUNK = 240                      # time-varying filters: divides the loop and the pre-roll

PC = {'C': 0, 'C#': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}

#          bass  guitar bass  guitar trebles  organ              chord tones
CH = {
    'D':      (38, (50, 45), (57, 62, 66), (57, 62, 66, 69), 'D F# A'),
    'Cadd9':  (36, (48, 43), (55, 62, 64), (55, 60, 62, 64), 'C E G D'),
    'G':      (43, (43, 50), (55, 59, 62), (55, 59, 62, 67), 'G B D'),
    'Bm7':    (47, (47, 42), (57, 62, 66), (57, 62, 66, 71), 'B D F# A'),
    'Gmaj7':  (43, (43, 50), (59, 62, 66), (55, 59, 62, 66), 'G B D F#'),
    'Em7':    (40, (40, 47), (55, 62, 64), (55, 59, 62, 64), 'E G B D'),
    'A7sus4': (45, (45, 52), (55, 62, 64), (55, 62, 64, 69), 'A D E G'),
    'A7':     (45, (45, 52), (55, 61, 64), (55, 61, 64, 69), 'A C# E G'),
    'Gm6':    (43, (43, 50), (58, 62, 64), (55, 58, 62, 64), 'G Bb D E'),
    'D/F#':   (42, (42, 50), (57, 61, 66), (57, 61, 66, 69), 'D F# A C#'),
}
# D/F# is Dmaj7 over F#. Its D sits in the guitar's thumb (D3); the organ
# carries no D4, which would rub a semitone against the C#4 beside it.
PROG = ['D', 'Cadd9', 'G', 'D',
        'Bm7', 'Gmaj7', 'Em7', 'A7sus4',
        'D', 'Cadd9', 'G', 'D',
        'Gmaj7', 'Gm6', 'D/F#', 'A7sus4',
        'Bm7', 'Gmaj7', 'Em7', 'A7sus4']


def chord_at(b, e=0):
    """The chord at eighth e of bar b; the sus4 resolves halfway through."""
    name = PROG[b % BARS]
    return 'A7' if name == 'A7sus4' and e >= 6 else name


def tones(name):
    return {PC[s] for s in CH[name][4].split()}


def fifth_of(name):
    """The bass's fifth: the fifth of the chord's own root (not of a slash
    bass), the nearest one above the bass note, dropped an octave if above D3."""
    root = CH[name][0]; pc = (PC[re.match(r'[A-G][#b]?', name).group()] + 7) % 12
    m = root + 1 + (pc - root - 1) % 12
    return m if m <= 50 else m - 12


def segments(b):
    return [(0, 6, 'A7sus4'), (6, 6, 'A7')] if PROG[b % BARS] == 'A7sus4' else [(0, 12, PROG[b % BARS])]


def part(name, b):
    b %= BARS; sec, i = b // 4, b % 4
    return {
        'bass':   sec > 0 or i >= 2,
        'shaker': sec > 0 or i >= 2,
        'hand':   sec in (2, 3) or (sec == 4 and i < 3),
        'melody': sec == 2,
        'flute':  sec == 3,
    }[name]


SUB_GAIN = 0.24
ORGAN_LEVEL = (0.5, 0.7, 0.8, 1.0, 0.8)        # by section, A B A' C B'

# ── the lines: (midi, eighths), 0 = rest; 48 eighths = 4 bars ───────────────
SOLO_1 = [(0, 3), (78, 5), (76, 1), (74, 3),            # Bm7
          (71, 5), (69, 1), (71, 3), (74, 3),           # Gmaj7
          (76, 8), (74, 1), (71, 3),                    # Em7
          (69, 3), (74, 3), (73, 6)]                    # A7sus4 - A7
SOLO_2 = [(71, 2), (74, 1), (78, 9),                    # Bm7
          (78, 4), (76, 1), (74, 1), (71, 6),           # Gmaj7
          (79, 7), (78, 1), (76, 1), (74, 3),           # Em7
          (76, 6), (73, 3), (69, 3)]                    # A7sus4 - A7
MELODY = [(69, 3), (66, 3), (69, 2), (71, 1), (69, 3),  # D
          (67, 3), (64, 3), (62, 3), (64, 3),           # Cadd9
          (71, 3), (74, 4), (72, 1), (71, 1), (67, 3),  # G
          (66, 7), (64, 1), (62, 4)]                    # D
FLUTE = [(78, 6), (74, 6),                              # Gmaj7
         (76, 6), (74, 3), (70, 3),                     # Gm6
         (73, 6), (69, 6),                              # D/F#
         (74, 6), (73, 6)]                              # A7sus4 - A7
LINES = (('solo 1', SOLO_1, 4), ('solo 2', SOLO_2, 16), ('melody', MELODY, 8), ('flute', FLUTE, 12))


def check_line(name, mel, bar0):
    """Every note that sounds across a dotted beat, or starts on one, must be
    a tone of the chord there; short notes between beats may pass."""
    pos = 0
    for m, d in mel:
        if m:
            for q in range(pos, pos + d):
                if q == pos and q % 3 and d < 3:
                    continue                              # a short note off the beat
                if q == pos or q % 3 == 0:
                    ch = chord_at(bar0 + q // 12, q % 12)
                    assert m % 12 in tones(ch), f'{name}: {m} at bar {bar0 + q // 12} eighth {q % 12} over {ch}'
        pos += d
    assert pos == 48, (name, pos)


for _n, _m, _b in LINES:
    check_line(_n, _m, _b)


# ── time-varying filters (per chunk, state carried) ─────────────────────────
def tv_lp(x, fc, q=0.707, chunk=CHUNK):
    """Low-pass whose cutoff is fc[i] for the chunk starting at sample i*chunk."""
    out = np.empty_like(x); zi = np.zeros(2)
    for j, i in enumerate(range(0, len(x), chunk)):
        w = 2 * np.pi * min(fc[j], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


def phaser(x, k, lo=320, hi=2400, stages=4, mix=0.5):
    """Four all-passes swept between lo and hi, k sweeps per loop."""
    n = len(x); out = np.empty(n); zis = [np.zeros(1) for _ in range(stages)]
    for i in range(0, n, CHUNK):
        u = 0.5 - 0.5 * np.cos(2 * np.pi * k * (i / SR - tl.t0) / LOOP)
        tn = np.tan(np.pi * lo * (hi / lo) ** u / SR); a = (tn - 1) / (tn + 1)
        seg = x[i:i + CHUNK]
        for s in range(stages):
            seg, zis[s] = lfilter([a, 1.0], [1.0, a], seg, zi=zis[s])
        out[i:i + CHUNK] = seg
    return (1 - mix) * x + mix * out


def rotary(x, k_horn=66, k_drum=55):
    """A Leslie at chorale speed: horn above 700 Hz, drum below, each a
    rotating Doppler delay and amplitude, the two channels a quarter-turn apart.
    66 and 55 turns per loop = 0.80 and 0.67 Hz."""
    n = len(x); t = np.arange(n) / SR - tl.t0; idx = np.arange(n, dtype=float)
    low = lp(lp(x, 700), 700); high = x - low
    out = np.zeros((n, 2))
    for band, k, dms, am in ((high, k_horn, 0.32, 0.28), (low, k_drum, 0.18, 0.10)):
        w = 2 * np.pi * k * t / LOOP
        for ch, ph in ((0, 0.0), (1, np.pi / 2)):
            d = (1.2 + dms * np.sin(w + ph)) / 1000 * SR
            out[:, ch] += np.interp(idx - d, idx, band) * (1 + am * np.sin(w + ph + np.pi / 2))
    return out


# ── instruments ─────────────────────────────────────────────────────────────
def ks(m, dur, vel, bright, key):
    """A Karplus-Strong string. The loop is L samples of delay, the two-point
    average (the string's loss) and a first-order all-pass carrying the rest
    of the period, so the pitch is exact. dur is how long it rings before the
    finger (or the next pluck) stops it."""
    f = hz(m); P = SR / f
    L = int(P - 0.6); D = P - 0.5 - L; c = (1 - D) / (1 + D)
    t60 = float(np.clip(4.4 * (150 / f) ** 0.4, 1.8, 5.0))
    g = 10 ** (-3 / (f * t60))
    n = int((dur + 0.06) * SR)
    blocks = n // L + 2
    r = rng('ks', key)
    fc = 700 + 3600 * bright                                   # a fingertip on steel, not a pick
    exc = lp1(lp1(r.standard_normal(L + 256), fc), fc)[256:]
    exc = exc - np.roll(exc, max(1, int(0.19 * L)))            # plucked a fifth of the way along
    exc -= exc.mean(); exc *= vel / (np.abs(exc).max() + 1e-9)
    y = np.zeros(blocks * L); y[:L] = exc
    fb = np.convolve([0.5, 0.5], [c, 1.0]); fa = np.array([1.0, c]); zi = np.zeros(2)
    for j in range(1, blocks):
        v, zi = lfilter(fb, fa, y[(j - 1) * L:j * L], zi=zi)
        y[j * L:(j + 1) * L] = g * v
    y = y[:n]
    y[:96] *= np.linspace(0, 1, 96)
    k = int(0.06 * SR)
    y[-k:] *= np.cos(np.linspace(0, np.pi / 2, k)) ** 2
    return y


def body(x):
    """The guitar's box: resonances at 100, 200 and 400 Hz, the top rolled off."""
    y = x + 0.55 * bp(x, 102, 2.5) + 0.35 * bp(x, 205, 3.0) + 0.2 * bp(x, 410, 2.0)
    return lp1(hp1(y, 70), 7000)


DRAWBARS = ((0.5, 0.28), (1, 1.0), (2, 0.5), (3, 0.2), (4, 0.14), (6, 0.04))


def organ_note(m, dur, key):
    n = int((dur + 0.6) * SR); t = np.arange(n) / SR
    f = hz(m); r = rng('organ', key)
    x = sum(a * np.sin(2 * np.pi * f * h * t + r.uniform(0, 2 * np.pi)) for h, a in DRAWBARS if f * h < 5000)
    # a swell-pedal attack but an organ's quick release: with 0.5 s the old
    # note hung on under the new one, and half the changes step a semitone
    # (C-B, G-F#, the sus4 D-C#, C#-D, B-Bb), so each smeared for 0.4 s
    return x * adsr(n, 0.25, 0.5, 0.85, 0.15, dur)


def flute_note(m, dur, t_abs, key):
    """Mellotron flute: a soft near-sine with breath, the tape wowing a little."""
    n = int((dur + 0.5) * SR); tt = np.arange(n) / SR
    tg = t_abs + tt
    cents = 7 * np.sin(2 * np.pi * 50 * tg / LOOP) + 2 * np.sin(2 * np.pi * 206 * tg / LOOP + 1.3)
    ph = 2 * np.pi * np.cumsum(hz(m) * 2 ** (cents / 1200)) / SR
    x = np.sin(ph) + 0.22 * np.sin(2 * ph) + 0.06 * np.sin(3 * ph)
    z = rng('flute', key).standard_normal(n)
    breath = bp(z, 2 * hz(m), 2.0) * 0.35 + lp1(hp1(z, 1500), 4000) * 0.03
    return (x + breath) * adsr(n, 0.09, 0.3, 0.85, 0.35, dur)


def bass_note(m, dur):
    n = int((dur + 0.2) * SR); t = np.arange(n) / SR; f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.38 * np.sin(4 * np.pi * f * t) + 0.1 * np.sin(6 * np.pi * f * t)
    x += 0.25 * np.sin(8 * np.pi * f * t) * np.exp(-t / 0.04)                 # a finger's edge
    return x * adsr(n, 0.018, 0.4, 0.72, 0.15, dur)


def clash(a, b):
    """A semitone or a minor ninth: the two intervals a bass note must not make."""
    return abs(a - b) in (1, 13)


def above(name):
    """Everything the guitar and organ hold over the bass in this chord."""
    c = CH[name]
    return c[1] + c[2] + c[3]


def approach(b):
    """A walking note on the last dotted beat into the next bar's root: a
    chord tone a step from it, unless that rubs against the chord above (in
    Gmaj7 the F#2 lead-in sat a minor ninth under the organ's G3 and a
    semitone under the thumb's ringing G2); else the thumb's own note."""
    name = chord_at(b, 9); r2 = CH[chord_at(b + 1)][0]
    for m in (r2 - 1, r2 + 1, r2 - 2, r2 + 2):
        if m % 12 in tones(name) and not any(clash(m, o) for o in above(name)):
            return m
    return CH[name][1][1]


def bass_line(b):
    """(eighth, midi, eighths held) for bar b: root, fifth, a walk into the next bar."""
    name = PROG[b % BARS]; root = CH[chord_at(b)][0]
    six = root if name == 'A7sus4' else fifth_of(name)
    return ((0, root, 5.6), (6, six, 2.7), (9, approach(b), 2.7))


for _b in range(BARS):              # every bass note: a chord tone, no rub with the chord above it
    for _e, _m, _ in bass_line(_b):
        _c = chord_at(_b, _e)
        assert _m % 12 in tones(_c), f'bass {_m} not in {_c} (bar {_b})'
        assert not any(clash(_m, o) for o in above(_c)), f'bass {_m} rubs against {_c} (bar {_b} eighth {_e})'


# ── the Sub 37 ──────────────────────────────────────────────────────────────
# A Moog Sub 37 patch, one note a chord (two in the sus4 bar). Oscillator 1
# is a square LFO stepping between the note and a 2nd above it; oscillator 2
# is a second square LFO stepping between the note and a 4th above. So each
# note is a trio - base, 2nd, 4th - and the base is chosen so that none of the
# three sits a semitone (or a major seventh / minor ninth) from anything
# sounding there: the chord, the guitar's thumb, the organ, the bass line and
# the solo, melody or flute. On a plain D chord the root would not do (its G
# rubs the F#); the search lands on A (A, B, D) instead.
KEY = {PC[s] for s in 'D E F# G A B C C#'.split()}
SUB_LEVEL = (0.55, 1.0, 0.65, 0.9, 1.0)          # by section, A B A' C B'


def rubs(p, q):
    return (p - q) % 12 in (1, 11)


def line_pcs(b, e0, e1):
    """Pitch classes of the solo / melody / flute sounding in bar b, eighths e0..e1."""
    out = set()
    for _, mel, bar0 in LINES:
        pos = 0
        for m, d in mel:
            q0, q1 = bar0 * 12 + pos, bar0 * 12 + pos + d
            if m and q0 < b * 12 + e1 and q1 > b * 12 + e0:
                out.add(m % 12)
            pos += d
    return out


def around(b, e0, sl):
    name = chord_at(b, e0)
    return (tones(name) | {m % 12 for m in above(name)} | line_pcs(b, e0, e0 + sl)
            | {m % 12 for e, m, d in bass_line(b) if e < e0 + sl and e + d > e0})


def sub_pick(b, e0, sl):
    """(base pc, 2nd in semitones): chord tones first, then the key; a major 2nd before a minor."""
    name = chord_at(b, e0); near = around(b, e0, sl)
    order = [PC[s] for s in CH[name][4].split()] + sorted(KEY - tones(name))
    for pc in order:
        for sec in (2, 1):
            trio = (pc, (pc + sec) % 12, (pc + 5) % 12)
            if all(x in KEY for x in trio) and not any(rubs(x, o) for x in trio for o in near):
                return pc, sec
    raise AssertionError(f'Sub 37: no rub-free note in bar {b} eighth {e0} ({name})')


SUB = {}                                          # (bar, eighth) -> (midi, eighths, 2nd)
for _b in range(BARS):
    for _e0, _sl, _ in segments(_b):
        _pc, _sec = sub_pick(_b, _e0, _sl)
        SUB[_b, _e0] = (45 + (_pc - 9) % 12, _sl, _sec)       # A2 .. G#3
for (_b, _e0), (_m, _sl, _sec) in SUB.items():   # the three stepped pitches against everything held there
    _near = around(_b, _e0, _sl)
    for _x in (_m, _m + _sec, _m + 5):
        assert _x % 12 in KEY and not any(rubs(_x % 12, o) for o in _near), f'Sub 37 {_x} rubs in bar {_b}'


def blep(ph, dt):
    y = np.zeros_like(ph)
    a = ph < dt; u = ph[a] / dt[a]; y[a] = 2 * u - u * u - 1
    z = ph > 1 - dt; u = (ph[z] - 1) / dt[z]; y[z] = u * u + 2 * u + 1
    return y


def loop_phase(f):
    """Phase (cycles) of frequency f, nudged by under a thousandth of a hertz so
    that it advances a whole number of cycles per lap: seam-exact."""
    ph = np.cumsum(f / SR); i0, N = tl.smp(0), int(round(LOOP * SR))
    d = ph[i0 + N] - ph[i0]
    ph -= (d - np.round(d)) / N * np.arange(len(ph))
    return ph % 1.0


def sub37():
    n = tl.n; t = np.arange(n) / SR - tl.t0
    base = np.zeros(n); sec = np.zeros(n); starts = []
    for b in tl.bars_range():
        for e0, sl, _ in segments(b):
            m, _, s2 = SUB[b % BARS, e0]; i = max(tl.smp(b * BAR + e0 * E8), 0)
            base[i:] = m; sec[i:] = s2; starts.append((i, sl))
    base[:starts[0][0]] = base[starts[0][0]]
    base = lp1(base, 7.0)                                         # a 25 ms glide
    # square LFOs in integer samples (a sine's sign flickers at its exact zeros from lap to lap)
    N = int(round(LOOP * SR)); idx = np.arange(n) - tl.smp(0)
    sq1 = ((idx * 120) % N < N // 2).astype(float)                # 1.455 Hz
    sq2 = ((idx * 124) % N < N // 2).astype(float)                # 1.503 Hz: they drift apart and back 4 times a lap
    off1 = lp1(lp1(sq1 * sec, 60), 60)                            # slewed ~4 ms: no click at the step
    off2 = lp1(lp1(sq2 * 5.0, 60), 60)
    f1 = hz(base + off1 - 0.04); f2 = hz(base + off2 + 0.05)      # -4 / +5 cents
    p1, p2 = loop_phase(f1), loop_phase(f2)
    d1, d2 = f1 / SR, f2 / SR
    saw1 = 2 * p1 - 1 - blep(p1, d1)
    sq_2 = np.where(p2 < 0.5, 1.0, -1.0) + blep(p2, d2) - blep((p2 + 0.5) % 1.0, d2)
    x = 0.6 * saw1 + 0.45 * sq_2
    x = np.tanh(1.8 * x) / np.tanh(1.8)                           # a little drive into the ladder
    # mono, retriggered: each note attacks (10 ms) from wherever the last one's release had got to
    amp = np.zeros(n); fenv = np.zeros(n); lvl = 0.0
    for j, (i, sl) in enumerate(starts):
        k = starts[j + 1][0] if j + 1 < len(starts) else n
        tt = np.arange(k - i) / SR; gate = sl * E8 * 0.7
        att = np.minimum(1, tt / 0.010)
        held = 0.62 + 0.38 * np.exp(-np.maximum(tt - 0.010, 0) / 0.9)
        env = (lvl + (1 - lvl) * att) * np.where(tt < 0.010, 1, held)
        rel = np.where(tt < gate, 1.0, np.exp(-np.maximum(tt - gate, 0) / 0.75))   # ~2.2 s to -25 dB
        amp[i:k] = env * rel; lvl = amp[k - 1]
        fenv[i:k] = np.minimum(1, tt / 0.010) * np.exp(-tt / 1.4)
    fc = (260 + 520 * fenv + 1.2 * hz(base))[::CHUNK]              # 400 Hz .. ~1 kHz
    y = tv_lp(tv_lp(x, fc, 0.54), fc, 1.1)                        # four poles, gentle resonance
    lv = np.interp((t % LOOP) / BAR, np.arange(BARS + 1), [SUB_LEVEL[(b % BARS) // 4] for b in range(BARS + 1)])
    return hp1(y * amp * lp1(lv, 0.5), 40)


def shaker(seed):
    n = int(0.1 * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return lp1(hp1(hp1(z, 3800), 3800), 8500) * perc(n, 0.014, 0.03)


def hand_drum(f0, tau, seed):
    n = int(0.5 * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.3 * np.exp(-t / 0.018))
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / tau)
    skin = lp1(np.random.default_rng(seed).standard_normal(n), 2500) * np.exp(-t / 0.008) * 0.25
    return (tone + skin) * np.minimum(1, t / 0.002)


def wave(key, dur):
    """One wave: a dull roar building, breaking bright, hissing back out."""
    n = int(dur * SR); r = rng('sea', key)
    u = np.arange(n) / n
    pk = 0.3 + 0.08 * r.random()
    env = np.where(u < pk, np.sin(0.5 * np.pi * u / pk) ** 2, np.exp(-(u - pk) / 0.2))
    env *= np.clip((1 - u) / 0.12, 0, 1)
    ce = env[::CHUNK]
    out = np.zeros((n, 2))
    for ch in range(2):
        z = r.standard_normal(n)
        y = tv_lp(z, 300 + 2300 * ce ** 1.4, 0.6)
        foam = lp1(hp1(z, 2500), 6000) * env ** 3 * 0.12
        out[:, ch] = hp1(y, 140) * env + foam
    return out


def trumpet_phrase(mel):
    """One continuous trumpet voice across a solo."""
    total = sum(d for _, d in mel) * E8
    n = int((total + 0.6) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n); sc = np.zeros(n); burst = np.zeros(n)
    last = hz(next(m for m, _ in mel if m)); prev_rest = True; pos = 0; b = 0
    for j, (m, d) in enumerate(mel):
        a, b = int(round(pos * E8 * SR)), int(round((pos + d) * E8 * SR))
        if m:
            nd = (b - a) / SR; tt = np.arange(b - a) / SR
            legato = j + 1 < len(mel) and mel[j + 1][0] != 0
            f[a:b] = hz(m)
            swell = np.sin(np.pi * tt / nd) if nd > 0.8 else np.ones_like(tt)
            env = np.minimum(1, tt / 0.07) * (0.7 + 0.3 * swell)
            env *= np.clip((nd - tt) / 0.08, 0.55 if legato else 0.0, 1)
            g[a:b] = env
            vib[a:b] = np.clip((tt - 0.3) / 0.8, 0, 1) * (1.0 if nd > 0.7 else 0.3)
            sc[a:b] = -(80 if prev_rest else 40) * np.exp(-tt / 0.05)
            burst[a:b] = np.exp(-tt / 0.06) * (1.0 if prev_rest else 0.45)
            last = hz(m); prev_rest = False
        else:
            f[a:b] = last; prev_rest = True
        pos += d
    f[b:] = last
    g = lp1(g, 22)
    a1 = np.exp(-1 / (0.03 * SR))
    fl = lfilter([1 - a1], [1, -a1], f - f[0]) + f[0]
    t = np.arange(n) / SR
    vph = 2 * np.pi * np.cumsum(5.0 + 0.35 * np.sin(2 * np.pi * t / 3.3)) / SR
    cents = sc + 18 * vib * np.sin(vph)
    ph = 2 * np.pi * np.cumsum(fl * 2 ** (cents / 1200)) / SR
    s = 0.56 - 0.34 * g                                  # brighter as it swells
    K = int(7500 / min(hz(m) for m, _ in mel if m))
    x = sum(k ** -0.6 * np.exp(-(k - 1) * s) * np.clip((7500 - k * fl) / 1500, 0, 1) * np.sin(k * ph)
            for k in range(1, K + 1))                    # band-limited: nothing above 7.5 kHz
    x = x + 0.8 * bp(x, 1250, 1.3)                       # the brass formant
    x = lp(hp1(x, 220), 5200, 0.6)
    z = rng('breath', total).standard_normal(n)
    breath = bp(z, 1500, 0.9) * (0.35 * burst + 0.05 * g)
    return x * g + breath


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    gtr, mel, organ, flute, bass, perc_, sea, tpt = (tl.bus() for _ in range(8))
    gtr_events = []                                      # (t, string, midi, vel, bright, key)
    organ_segs = []                                      # (t, eighths, name)
    for b in tl.bars_range():
        t = b * BAR; bb = b % BARS; sec, i = bb // 4, bb % 4
        # guitar: pinch-and-roll, a bass note on each dotted beat
        for e in range(12):
            name = chord_at(b, e); _, (r0, r1), treb, _, _ = CH[name]
            h = rng('gh', bb, e)
            off = float(h.uniform(-0.006, 0.006)); swell = 0.5 + 0.5 * np.sin(np.pi * (e % 6) / 6)
            if e % 3 == 0:
                gtr_events.append((t + e * E8 + off, 'B%d' % (e // 3 % 2), r0 if e % 6 == 0 else r1,
                                   0.95 if e % 6 == 0 else 0.8, 0.3, (bb, e, 'b')))
            s = {1: 0, 2: 1, 4: 2, 5: 1, 7: 0, 8: 1, 10: 2, 11: 1}.get(e)
            if s is not None:
                gtr_events.append((t + e * E8 + off, 's%d' % s, treb[s], 0.5 + 0.15 * swell, 0.5, (bb, e, 't')))
            if e == 0:                                   # the downbeat: a soft strum up the trebles
                for k in range(3):
                    gtr_events.append((t + off + 0.022 * (k + 1), 's%d' % k, treb[k], 0.42, 0.45, (bb, e, 'st', k)))
        for s0, sl, name in segments(b):
            organ_segs.append((t + s0 * E8, sl, name))
        # bass: root, fifth, a walk into the next bar
        if part('bass', b):
            for e, m, d in bass_line(b):
                bass.add(t + e * E8, bass_note(m, d * E8), gain=0.13 if e == 0 else 0.11)
        # shaker: a brushed twelve with the dotted beats leaning
        if part('shaker', b):
            acc = (1.0, 0.45, 0.6, 0.85, 0.45, 0.6, 0.95, 0.45, 0.6, 0.85, 0.45, 0.6)
            for e in range(12):
                perc_.add(t + e * E8 + 0.01, shaker(bb * 12 + e), pan=0.45,
                          gain=(0.2 if sec else 0.12) * acc[e])
        if part('hand', b):
            # tuned to the key: a low open tone on D3 and a high one on E4. E
            # is a tone or more from every note of every chord here, and D
            # rubs only the A7's C# once a lap. (At 96 Hz, a flat G2, the low
            # stroke was a pitched boom under every chord and the mix's peaks.)
            lo_, hi_ = hz(50), hz(64)
            for e, (f0, tau, gn) in {0: (lo_, 0.15, 0.10), 6: (lo_, 0.14, 0.07), 3: (hi_, 0.06, 0.042),
                                     8: (hi_, 0.05, 0.028), 9: (hi_, 0.06, 0.042), 11: (hi_, 0.05, 0.024)}.items():
                perc_.add(t + e * E8, hand_drum(f0, tau, bb * 12 + e), pan=-0.3, gain=gn)
        # sea: a wave breaking every two bars
        if b % 2 == 0:
            sea.add(t - 0.3 * BAR, wave(bb, 2.6 * BAR), gain=0.085)

    # guitar strings ring until they are plucked again, or until the chord
    # changes and the fretting hand lets go: a treble string whose note is not
    # in the new chord, a bass string whose note is not one the new chord's
    # thumb plays. (Without this the thumb's last note rang a dotted beat into
    # the next bar - Bm7's F#2 under Gmaj7's G2 - and the sus4 D4 on under
    # the A7's C#.)
    changes = [(t, name) for t, _, name in organ_segs]
    by_string = {}
    for ev in sorted(gtr_events, key=lambda v: v[0]):
        by_string.setdefault(ev[1], []).append(ev)
    for s, evs in by_string.items():
        for j, (t, _, m, vel, br, key) in enumerate(evs):
            dur = min(evs[j + 1][0] - t, 2.6) if j + 1 < len(evs) else 2.6
            for tc, name in changes:
                keep = {n % 12 for n in CH[name][1]} if s[0] == 'B' else tones(name)
                if tc > t + 0.01 and tc - t < dur and m % 12 not in keep:
                    dur = tc - t
                    break
            pan = {'B0': -0.3, 'B1': -0.3, 's0': -0.45, 's1': -0.2, 's2': -0.05}[s]
            gtr.add(t, ks(m, dur, vel, br, key), pan=pan, gain=0.34)

    # the melody on a single string, let ring
    pos = 0
    for lap in (-1, 0, 1):
        t0 = lap * LOOP + 8 * BAR
        if t0 > (BARS + tl.post) * BAR or t0 + 4 * BAR < -tl.pre * BAR:
            continue
        pos = 0
        for j, (m, d) in enumerate(MELODY):
            nxt = MELODY[(j + 1) % len(MELODY)][0]
            # a leap lets the note ring on under the next (a second string);
            # a step stops it, or the two would rub a tone or a semitone apart
            ring = d * E8 if j + 1 < len(MELODY) and abs(nxt - m) <= 2 else min(d * E8 * 1.6, 2.2)
            mel.add(t0 + pos * E8, ks(m, ring, 0.9, 0.75, ('mel', j)), pan=0.35, gain=0.50)
            pos += d

    # organ: each voice held while its note stays, so common tones sustain
    for k in range(4):
        notes = []
        for t, sl, name in organ_segs:
            m = CH[name][3][k]
            if notes and notes[-1][2] == m and abs(notes[-1][0] + notes[-1][1] - t) < 1e-9:
                notes[-1][1] += sl * E8
            else:
                notes.append([t, sl * E8, m])
        for t, d, m in notes:
            organ.add(t, organ_note(m, d - 0.02, (round(t / E8) % (BARS * 12), k)), gain=0.08)
    tt = np.arange(tl.n) / SR - tl.t0
    lv = np.interp((tt % LOOP) / BAR, np.arange(BARS + 1), [ORGAN_LEVEL[(b % BARS) // 4] for b in range(BARS + 1)])
    orgm = phaser(organ.x.mean(1) * lp1(lv, 0.5), k=10)
    orgx = rotary(orgm)

    # mellotron flute in C
    for lap in (-1, 0, 1):
        t0 = lap * LOOP + 12 * BAR
        if t0 > (BARS + tl.post) * BAR or t0 + 4 * BAR < -tl.pre * BAR:
            continue
        pos = 0
        for j, (m, d) in enumerate(FLUTE):
            flute.add(t0 + pos * E8, flute_note(m, d * E8 - 0.06, (12 * BAR + pos * E8), ('fl', j)),
                      pan=0.3, gain=0.16)
            pos += d

    # trumpet solos
    for lap in (-1, 0, 1):
        for bar0, line in ((4, SOLO_1), (16, SOLO_2)):
            t0 = lap * LOOP + bar0 * BAR
            if t0 > (BARS + tl.post) * BAR or t0 + 5 * BAR < -tl.pre * BAR:
                continue
            tpt.add(t0, trumpet_phrase(line), pan=0.05, gain=0.085)

    gtrx = body(gtr.x); melx = body(mel.x)
    melx = melx + pingpong(melx, 2 * E8, 0.3, 4, 3000) * 0.5
    flutex = chorus(flute.x, LOOP / 40, depth_ms=2.0, base_ms=8.0, mix=0.5, t0=tl.t0)
    tptx = tpt.x + pingpong(tpt.x, BEAT, 0.36, 5, 2400) * 0.75
    sub = sub37(); sub = np.stack([sub * 0.95, sub * 1.05], 1) * SUB_GAIN
    subx = sub + pingpong(sub, 2 * BEAT, 0.42, 6, 1100) * 0.6     # a dotted-half echo, darkening
    wet = reverb(gtrx * 0.22 + melx * 0.3 + orgx * 0.3 + flutex * 0.45 + tptx * 0.6
                 + perc_.x * 0.12 + sea.x * 0.3 + subx * 0.35, make_ir(3.6, dark=3600, seed=17, pre=0.03))
    stems = dict(guitar=gtrx, melody=melx, organ=orgx, flute=flutex, bass=bass.x, perc=perc_.x,
                 sea=sea.x, trumpet=tptx, sub37=subx, reverb=wet * 0.5)
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        i0 = tl.smp(0)
        for k, v in stems.items():
            row = []
            for s in range(0, BARS, 2):
                seg = v[i0 + int(s * BAR * SR):i0 + int((s + 2) * BAR * SR)]
                row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9))
            print(f'{k:8s}' + ' '.join(f'{r:6.0f}' for r in row))
    return finish(tl, mix, 'present-perfect', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
