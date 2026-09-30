#!/usr/bin/env python3
"""Block Camp soundtrack "Glass" (Passive Present Perfect): baroque counterpoint on Moog-style synths.

The brief: Wendy Carlos, Switched-On Bach, and Isao Tomita. Baroque counterpoint
played on analogue synths: a two- or three-voice invention with a running
sixteenth-note subject answered at the fifth over a walking bass, each voice
on its own analogue timbre, a light spring-style reverb and no drums.
Everything here is original. No Bach piece is quoted.

G major, 100 BPM, 4/4. There are four 8-bar periods: G (bars 0-7), C a fourth
up (8-15), E minor (16-23, written out in the minor), then G again (24-31).
That is I - IV - vi - I, the usual key plan for an invention. Each period
runs like this:
  bar 0  subject in the upper voice        I  I   IV V7
  bar 1  answer at the fifth, in the middle voice; the upper voice has a
         countersubject. The answer is tonal in the major periods and real
         in E minor (it is in B minor there).
                                           V  V7  I  ii7
  bar 2  link                              V  V   V7 V7
  bar 3  subject in the bass               I  I   IV V7
  bars 4-6  episode: a falling-fifths sequence, one bar down a step each time,
         over a chain of prepared sevenths held in the middle voice and a
         walking bass
                                           vi vi ii7 ii7 | V V Imaj7 Imaj7 | IV IV V7/V V7/V
  bar 7  cadence into the next period's key, written out for each period
At the top of the loop the last cadence lands on a tonic pedal, under the saw
playing the subject alone. The levels follow the orchestration: P1 builds from
that solo, P3 is about 2 dB lighter, and P4 is the fullest. The whole thing is
32 bars = 76.8 s, a seamless loop (see synthkit.py).

Instruments (all synthesised here):
  saw     two slightly detuned saws through a resonant low-pass with a fast
          filter envelope. This is the bright "Moog lead".
  square  a round square wave, low-passed, soft attack.
  harp    a narrow pulse with an added octave, plucked by a very fast filter
          and amplitude decay. This is the harpsichord-like voice.
  bass    saw plus square through an enveloped low-pass, with a sine under it.
          In bar 3 of each period, where it carries the subject, it is 3.5 dB
          up with the filter further open, so the entry is heard on a laptop.
All saws and pulses are band-limited (PolyBLEP, defined below). This keeps
aliasing in the high voices at -47 to -61 dB, where it cannot be heard.
Who plays what rotates by period:
  P1: saw subject, square answer. The period opens on the saw alone.
  P2: harp subject, saw answer. This period is a fourth higher, so it is the brightest.
  P3: square subject, harp answer. There is no saw, so this is the lighter middle.
  P4: saw subject with the harp doubling it, square answer. This is the fullest period.
The reverb is a short spring-style one: a noise tail plus a train of
dispersive "boing" echoes, mixed low.

    py lesson-template/build/block-camp-music/glass.py [--wav preview.wav] [--check]

--check prints the counterpoint audit instead of rendering. It lists non-chord
tones on the beat, dissonances on the beat, parallel fifths and octaves, and
voice crossings.
"""
import sys
from functools import lru_cache
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, phase, adsr, perc,
                      make_ir, reverb, finish)

tl = Timeline(bpm=100, bars=32)
BAR, S16 = tl.bar, tl.s16
STEPS = 16 * tl.bars                                 # sixteenths in the loop

# ── notation ────────────────────────────────────────────────────────────────
_PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def midi(tok):
    p = _PC[tok[0]]; i = 1
    while i < len(tok) and tok[i] in '#b':
        p += 1 if tok[i] == '#' else -1; i += 1
    return p + 12 * (int(tok[i:]) + 1)


def parse(s):
    """'r G4 B4:2 ...' -> [(dur16, midi|None)]; '@2' sets the default length."""
    out, dflt = [], 1
    for tok in s.split():
        if tok == '|':
            continue
        if tok.startswith('@'):
            dflt = int(tok[1:]); continue
        name, _, d = tok.partition(':')
        out.append((int(d) if d else dflt, None if name == 'r' else midi(name)))
    assert sum(d for d, _ in out) == 16, (s, sum(d for d, _ in out))
    return out


# ── the template, in G; bars 0-6 of every period ────────────────────────────
TEMPLATE = [
    dict(L='r G4 B4 D5 G5 F#5 G5 D5 E5 C5 D5 B4 C5 A4 B4 F#4',             # subject
         R='@2 B3 D4 G4 D4 C4 G4 F#4 D4',
         B='@2 G2 D3 B2 G2 C3 E3 D3 C3'),
    dict(L='@2 A4 D5 F#5 A5 G5 D5 E5 G5',                                   # countersubject
         R='r D4 F#4 A4 D5 C5 D5 A4 B4 G4 A4 F#4 G4 E4 F#4 C4',             # tonal answer, at the fifth
         B='@2 D3 C3 A2 F#2 G2 B2 C3 A2'),
    dict(L='F#5 E5 D5 E5 F#5 A5 G5 F#5 D5 C5 B4 C5 A4 F#4 A4 C5',           # link
         R='@2 D4 F#4 A4 F#4 F#4 D4 C4 C4',
         B='@2 D3 E3 F#3 D3 C3 A2 F#2 D2'),
    dict(L='@2 D5 C5 B4 D5 C5 E5 A4 C5',
         R='B3:4 D4:2 B3:2 C4:2 G4:2 F#4:2 D4:2',
         B='r G2 B2 D3 G3 F#3 G3 D3 E3 C3 D3 B2 C3 A2 B2 F#2'),             # subject in the bass
    dict(L='E5 B4 G4 B4 E5 F#5 G5 E5 C5 A4 E4 A4 C5 D5 E5 C5',              # episode
         R='G3:8 G3:8',
         B='@2 E2 B2 G2 E2 A2 C3 E3 A2'),
    dict(L='D5 A4 F#4 A4 D5 E5 F#5 D5 B4 G4 D4 G4 B4 C5 D5 B4',
         R='F#3:8 F#3:8',
         B='@2 D3 A2 F#2 A2 G2 B2 D3 G2'),
    dict(L='C5 G4 E4 G4 C5 D5 E5 C5 E5 C#5 A4 C#5 G4 A4 C#5 E5',
         R='E3:8 E3:8',
         B='@2 C3 G2 E2 G2 A2 G2 E2 C#3'),
]
T_HARM = [('G', 'G', 'C', 'D7'), ('D', 'D7', 'G', 'Am7'), ('D', 'D', 'D7', 'D7'), ('G', 'G', 'C', 'D7'),
          ('Em', 'Em', 'Am7', 'Am7'), ('D', 'D', 'Gmaj7', 'Gmaj7'), ('C', 'C', 'A7', 'A7')]

# the same seven bars in E minor (for period 3), written out: the mode
# changes the leading tones and the episode's sequence of suspensions
MINOR = [
    dict(L='r E4 G4 B4 E5 D#5 E5 B4 C5 A4 B4 G4 A4 F#4 G4 D#4',
         R='@2 G3 B3 E4 B3 A3 E4 D#4 B3',
         B='@2 E2 B2 G2 E2 A2 C3 B2 A2'),
    dict(L='@2 F#4 B4 D5 F#5 E5 B4 C#5 E5',
         R='r B3 D4 F#4 B4 A#4 B4 F#4 G4 E4 F#4 D4 E4 C#4 D4 A#3',            # answer, in B minor
         B='@2 B2:4 F#2 D2 E2 G2 F#2:4'),
    dict(L='D#5 C#5 B4 C#5 D#5 F#5 E5 D#5 B4 A4 G4 A4 F#4 D#4 F#4 A4',
         R='@2 B3 D#4 F#4 D#4 D#4 B3 A3 A3',
         B='@2 B2 C#3 D#3 B2 A2 F#2 D#2 B1'),
    dict(L='@2 B4 A4 G4 B4 A4 C5 F#4 A4',
         R='G3:4 B3:2 G3:2 A3:2 E4:2 D#4:2 B3:2',
         B='r E2 G2 B2 E3 D#3 E3 B2 C3 A2 B2 G2 A2 F#2 G2 D#2'),
    dict(L='C5 G4 E4 G4 C5 D5 E5 C5 A4 F#4 C4 F#4 A4 B4 C5 A4',
         R='E3:8 E3:8',
         B='@2 C2 G2 E2 C2 F#2 A2 C3 F#2'),
    dict(L='B4 F#4 D#4 F#4 B4 C#5 D#5 B4 G4 E4 B3 E4 G4 A4 B4 G4',
         R='D#3:8 E3:8',
         B='@2 B2 A2 F#2 A2 G2 B2 E2 G2'),
    dict(L='C5 A4 E4 A4 C5 E5 D5 B4 C5 A4 F#4 A4 D4 F#4 A4 C5',
         R='C3:8 C3:8',
         B='@2 A2 C2 E2 G2 F#2 D2 F#2 D2'),
]
M_HARM = [('Em', 'Em', 'Am', 'B7'), ('Bm', 'Bm', 'Em', 'F#7'), ('B', 'B', 'B7', 'B7'), ('Em', 'Em', 'Am', 'B7'),
          ('C', 'C', 'F#m7b5', 'F#m7b5'), ('B', 'B', 'Em', 'Em'), ('Am', 'Am', 'D7', 'D7')]

# bar 7 of each period, at sounding pitch: the way into the next key
CADENCE = [
    (dict(L='F5 E5 D5 A4 D5 E5 F5 D5 B4 G4 B4 D5 F5 D5 B4 G4',             # G -> C
          R='A3:4 A3:4 D4:4 F4:4', B='@2 D3 C3 A2 F2 G2 D3 B2 G2'), ('Dm', 'Dm', 'G7', 'G7')),
    (dict(L='E5 B4 G4 B4 E5 F#5 G5 E5 D#5 B4 F#4 B4 A4 F#4 D#4 F#4',        # C -> E minor
          R='B3:8 A3:8', B='@2 G3 E3 B2 E3 B2 D#3 F#2 A2'), ('Em', 'Em', 'B7', 'B7')),
    (dict(L='B4 G4 D4 G4 B4 A4 G4 B4 C5 A4 F#4 A4 D5 C5 B4 A4',             # E minor -> G
          R='D3:8 C3:8', B='@2 B1 D2 G2 D2 F#2 A2 D2 F#2'), ('G', 'G', 'D7', 'D7')),
    (dict(L='F#5 E5 D5 A4 F#4 A4 D5 F#5 C5 A4 F#4 A4 D5 C5 A4 F#4',         # G -> G (the seam)
          R='A3:4 A3:4 A3:4 C4:4', B='@2 D3 A2 D2 F#2 D3 C3 A2 F#2'), ('D', 'D', 'D7', 'D7')),
]

# period: which seven bars, transposed how far, and which timbre plays each voice
PERIODS = [dict(bars=TEMPLATE, harm=T_HARM, shift=0, L='saw',    R='square', B='bass'),
           dict(bars=TEMPLATE, harm=T_HARM, shift=5, L='harp',   R='saw',    B='bass'),
           dict(bars=MINOR,    harm=M_HARM, shift=0, L='square', R='harp',   B='bass'),
           dict(bars=TEMPLATE, harm=T_HARM, shift=0, L='saw',    R='square', B='bass', double='harp')]

_ROOT = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
_QUAL = {'': (0, 4, 7), 'm': (0, 3, 7), '7': (0, 4, 7, 10), 'm7': (0, 3, 7, 10), 'maj7': (0, 4, 7, 11),
         'm7b5': (0, 3, 6, 10)}
_NAMES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']


def chord_pcs(name, shift=0):
    r = _ROOT[name[0]]; q = name[1:]
    if q.startswith('#'):
        r += 1; q = q[1:]
    r = (r + shift) % 12
    return r, {(r + i) % 12 for i in _QUAL[q]}


def score():
    """-> notes [(step, dur16, midi, voice, timbre)], harmony per beat [(root, pcs, label)]"""
    notes, harm = [], []
    for p, P in enumerate(PERIODS):
        for k in range(8):
            bar = 8 * p + k
            if k < 7:
                lines, sh, hs = dict(P['bars'][k]), P['shift'], P['harm'][k]
            else:
                (lines, hs), sh = CADENCE[p], 0
            if p == 0 and k == 0:                   # the loop's top: the cadence lands on a tonic pedal under the saw alone
                lines['R'], lines['B'] = 'B3:6 r:10', 'G2:12 r:4'
            if p == 0 and k == 1:
                lines['B'] = 'r:16'
            for v in 'LRB':
                s = 16 * bar
                for d, m in parse(lines[v]):
                    if m is not None:
                        notes.append((s, d, m + sh, v, P[v]))
                        if v == 'L' and 'double' in P:
                            notes.append((s, d, m + sh, 'D', P['double']))
                    s += d
            for h in hs:
                r, pcs = chord_pcs(h, sh if k < 7 else 0)
                harm.append((r, pcs, _NAMES[r] + h[1:].lstrip('#')))
    return notes, harm


# ── counterpoint audit ──────────────────────────────────────────────────────
def check():
    notes, harm = score()
    grid = {v: [None] * STEPS for v in 'LRB'}
    onset = {v: [False] * STEPS for v in 'LRB'}
    for s, d, m, v, _ in notes:
        if v == 'D':
            continue
        for i in range(s, s + d):
            grid[v][i] = m
        onset[v][s] = True

    def where(s):
        return f'bar {s // 16:2d} beat {s % 16 // 4 + 1}.{s % 4}'

    def nm(m):
        return _NAMES[m % 12] + str(m // 12 - 1)
    problems = 0
    # 1. chord membership: every note on a beat, and every note a quarter or longer
    for s, d, m, v, _ in notes:
        if v == 'D':
            continue
        beats = [b for b in range(s, s + d) if b % 4 == 0] if d >= 4 else ([s] if s % 4 == 0 else [])
        for b in beats:
            r, pcs, lab = harm[b // 4]
            if m % 12 not in pcs:
                held = b != s
                print(f'  NCT  {where(b)} {v} {nm(m)} over {lab}' + (' (held: suspension)' if held else ''))
                problems += not held
    # 2. vertical dissonance on beats (both not chord tones), and a 4th over the bass
    for s in range(0, STEPS, 4):
        r, pcs, lab = harm[s // 4]
        vs = [(v, grid[v][s]) for v in 'BRL' if grid[v][s] is not None]
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                (va, a), (vb, b) = vs[i], vs[j]
                lo, hi = min(a, b), max(a, b)
                ic = (hi - lo) % 12
                both_ct = a % 12 in pcs and b % 12 in pcs
                if ic in (1, 2, 10, 11) and not both_ct:
                    print(f'  DISS {where(s)} {va}-{vb} {nm(a)}/{nm(b)} over {lab}'); problems += 1
                if ic == 5 and 'B' in (va, vb) and lo == (a if va == 'B' else b) and not both_ct:
                    print(f'  4TH  {where(s)} {va}-{vb} over bass {nm(lo)}'); problems += 1
    # 3. parallel fifths/octaves, beat to beat and eighth to eighth (when both voices move)
    for step in (4, 2):
        for s in range(0, STEPS, step):
            t = (s + step) % STEPS
            for a, b in (('L', 'R'), ('L', 'B'), ('R', 'B')):
                p0, q0, p1, q1 = grid[a][s], grid[b][s], grid[a][t], grid[b][t]
                if None in (p0, q0, p1, q1) or p0 == p1 or q0 == q1:
                    continue
                if step == 2 and not (onset[a][t] and onset[b][t]):
                    continue
                i0, i1 = abs(p0 - q0) % 12, abs(p1 - q1) % 12
                if i0 == i1 and i0 in (0, 7) and (p1 - p0) * (q1 - q0) > 0:
                    print(f'  PAR  {where(s)} -> {where(t)} {a}-{b} {"8ve" if i0 == 0 else "5th"} '
                          f'{nm(p0)}/{nm(q0)} -> {nm(p1)}/{nm(q1)}'); problems += 1
    # 4. crossings (reported, not errors: the voices are different timbres)
    cross = [s for s in range(STEPS) if None not in (grid['L'][s], grid['R'][s]) and grid['L'][s] < grid['R'][s]]
    bcross = [s for s in range(STEPS) if None not in (grid['R'][s], grid['B'][s]) and grid['R'][s] <= grid['B'][s]]
    print(f'  crossings L<R: {len(cross)} sixteenths ({sorted({c // 16 for c in cross})}), '
          f'R<=B: {len(bcross)} ({sorted({c // 16 for c in bcross})})')
    print(f'{problems} problems')
    return problems


# ── instruments ─────────────────────────────────────────────────────────────
# Band-limited oscillators (PolyBLEP). synthkit's saw() and pulse() are naive,
# and on this track's exposed upper voices (G5-D6) their aliasing measured
# -23 to -27 dB against the harmonics: an inharmonic sizzle on every note that
# an analogue Moog never had. Smoothing each edge brings it to -47 to -61 dB.
def _blep(t, dt):
    y = np.zeros_like(t)
    a = t < dt; u = t[a] / dt[a]; y[a] = 2 * u - u * u - 1
    b = t > 1 - dt; u = (t[b] - 1) / dt[b]; y[b] = u * u + 2 * u + 1
    return y


def saw(f, n, ph=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,)); t = phase(f, n, ph)
    return 2 * t - 1 - _blep(t, f / SR)


def pulse(f, n, duty=0.5, ph=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,)); t = phase(f, n, ph); dt = f / SR
    return np.where(t < duty, 1.0, -1.0) + _blep(t, dt) - _blep((t - duty) % 1.0, dt)


def env_lp(x, fcf, q=1.0, chunk=128):
    """Two-pole low-pass whose cutoff follows fcf(t seconds), chunk by chunk."""
    n = len(x); out = np.empty(n); zi = np.zeros(2)
    for i in range(0, n, chunk):
        fc = fcf((i + chunk / 2) / SR)
        w = 2 * np.pi * min(fc, SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


@lru_cache(maxsize=None)
def saw_lead(m, d16):
    gate = d16 * S16 * 0.92
    n = int((gate + 0.12) * SR)
    f = hz(m)
    x = 0.5 * (saw(f, n) + saw(f * 1.0035, n, 0.37))
    top, base = min(6000.0, f * 10), min(2800.0, f * 3.2)
    x = env_lp(x, lambda t: base + (top - base) * np.exp(-t / 0.09), q=1.5)
    x = lp(x, 6500)
    return x * adsr(n, 0.004, 0.12, 0.75, 0.06, gate)


@lru_cache(maxsize=None)
def square(m, d16):
    gate = d16 * S16 * 0.9
    n = int((gate + 0.15) * SR); t = np.arange(n) / SR
    f = hz(m)
    fv = f * 2 ** (0.1 / 12 * np.clip((t - 0.35) / 0.4, 0, 1) * np.sin(2 * np.pi * 5.0 * t)) if d16 >= 8 else f
    x = 0.6 * pulse(fv, n, 0.5) + 0.4 * pulse(fv * 1.002, n, 0.5, 0.25)
    x = lp(lp(x, min(f * 5.5, 3200.0), 0.8), min(f * 7, 4200.0), 0.7)
    return x * adsr(n, 0.015, 0.1, 0.85, 0.09, gate)


@lru_cache(maxsize=None)
def harp(m, d16):
    dur = d16 * S16
    n = int((dur + 0.12) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = hp1(pulse(f, n, 0.18) + 0.4 * pulse(2 * f, n, 0.3, 0.1), 40)
    x = env_lp(x, lambda tt: f * 2.5 + min(6500.0, f * 14) * np.exp(-tt / 0.045), q=0.9)
    click = hp1(np.random.default_rng(m).standard_normal(n), 2500) * np.exp(-t / 0.003) * 0.08
    tau = float(np.clip(0.25 + 0.5 * (72 - m) / 24, 0.2, 0.8))
    amp = perc(n, 0.0015, tau) * np.clip((dur + 0.1 - t) / 0.1, 0, 1)
    return (x + click) * amp


@lru_cache(maxsize=None)
def bass(m, d16, lead=False):
    """lead: the bar where the bass carries the subject. The filter opens
    further so the line speaks on laptop speakers, which lose its fundamental."""
    gate = d16 * S16 * 0.85
    n = int((gate + 0.08) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = 0.65 * saw(f, n) + 0.35 * pulse(f * 1.002, n, 0.5)
    base, env = (max(4.5 * f, 420.0), 1900) if lead else (max(3.2 * f, 300.0), 1300)
    x = env_lp(x, lambda tt: base + env * np.exp(-tt / 0.07), q=1.3)
    x += 0.35 * np.sin(2 * np.pi * f * t)
    return x * adsr(n, 0.003, 0.09, 0.7, 0.05, gate)


VOICE = dict(saw=saw_lead, square=square, harp=harp, bass=bass)
PAN = dict(saw=-0.35, square=0.35, harp=0.15, bass=0.0)
GAIN = dict(saw=0.45, square=0.26, harp=0.20, bass=0.33)
SEND = dict(saw=0.30, square=0.28, harp=0.35, bass=0.06)


def spring_ir():
    """A short spring-style tank: a dark noise tail plus a train of falling
    chirps (the spring's dispersive echoes) about 40 ms apart."""
    n = int(1.8 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(21).standard_normal((n, 2)) * np.exp(-6.9 * t / 1.3)[:, None]
    ir = hp1(lp1(z, 3800), 220) * 0.6
    cn = int(0.03 * SR); ct = np.arange(cn) / SR
    fch = 3200 * (300 / 3200) ** (ct / 0.03)
    chirp = np.sin(2 * np.pi * np.cumsum(fch) / SR) * np.hanning(cn)
    for ch, gap in ((0, 0.041), (1, 0.037)):
        for k in range(1, 24):
            i = int(k * gap * SR)
            if i + cn < n:
                ir[i:i + cn, ch] += chirp * 0.5 * 0.72 ** k
    ir = lp1(ir, 4500)
    return ir / np.sqrt((ir ** 2).sum() / 2)


PERIOD_GAIN = (1.0, 0.95, 0.8, 1.12)                 # the arc: P3 is the light middle, P4 the fullest


def bass_subject(s, v):
    """Bar 3 of every period puts the subject in the bass."""
    return v == 'B' and (s // 16) % 8 == 3


def note_gain(s, v, timbre):
    acc = 1.0 if s % 4 == 0 else 0.9                 # a touch of weight on the beat
    # the bass entry of the subject was 5-7 dB under the upper voices on a
    # laptop-speaker weighting: bring it forward so the imitation is heard
    lift = 1.5 if bass_subject(s, v) else 1.0
    return GAIN[timbre] * acc * lift * (0.7 if v == 'D' else 1.0) * PERIOD_GAIN[s // 128]


def render(wav=None):
    notes, _ = score()
    buses = {k: tl.bus() for k in VOICE}
    for s, d, m, v, timbre in notes:
        g = note_gain(s, v, timbre)
        sig = bass(m, d, True) if bass_subject(s, v) else VOICE[timbre](m, d)
        for lap in (-1, 0, 1):
            t = s * S16 + lap * tl.loop
            if -tl.pre * BAR - 2 < t < (tl.bars + tl.post) * BAR:
                buses[timbre].add(t, sig, pan=PAN[timbre] + (0.2 if v == 'D' else 0), gain=g)
    dry = sum(buses[k].x for k in buses)
    send = sum(buses[k].x * SEND[k] for k in buses)
    wet = reverb(send, spring_ir()) * 0.55 + reverb(send, make_ir(1.6, dark=3500, seed=5)) * 0.35
    mix = lp(dry + wet, 9000)
    return finish(tl, mix, 'passive-present-perfect', wav=wav)


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(1 if check() else 0)
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
