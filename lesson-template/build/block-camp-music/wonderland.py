#!/usr/bin/env python3
"""Block Camp soundtrack "The Stolen Now" (Wonderland: The Stolen Now RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is a voxel
Wonderland where the Warden has stolen Now: clockwork guards, a Rabbit
racing, a Cheshire Cat between mirrors, a teacup boat on a river that flows
backwards, a Gear Prison, and a palace bell that "loses another number"
(Present Continuous: everything happening at this moment). So: a toy-box
waltz - a music box winding up, a clarinet asking the tune, a bassoon
oom on the one, celesta and harp on the two and three, a clockwork tick on
every beat - with two Wonderland tricks built into the form:

  * the Reverse River: the B section is the whole tune played BACKWARDS
    (bars in reverse order, each bar's notes reversed, the chords reversed
    with them), low on the bassoon, over celesta chords whose envelopes run
    backwards - swelling up into each barline and cut off there;
  * the stolen beat: the bar after the river has two beats, not three. The
    clock stops for it, the waltz stops, and a celesta run climbs into A'.

An original piece: no melody or progression is taken from any film, game or
song.

G major, 3/4, 144 BPM (a beat is exactly 20000 samples). The Timeline is told
bpm=576 so that its 4-beat "bar" is ONE beat; everything here is placed in
beats. One chord a bar:

  intro  G  G  Am D7 | G  Eb D7 G                 bars 0-7    the music box alone, then oom-pah
  A      G  G  Am D7 | G  E7 Am D7 |              bars 8-23   the clarinet tune, celesta pah-pah
         G  G  C  Cm | G  Eb D7 G
  B      G  D7 Eb G  | Cm C  G  G  |              bars 24-39  the Reverse River: the tune backwards
         D7 Am E7 G  | D7 Am G  G                             on the bassoon, reversed celesta
  stolen G (two beats)                            bar 40      no clock; a celesta run up
  A'     (as A)                                   bars 41-56  celesta and music box on the tune,
                                                              harp pah-pah, a clarinet counter-line
57 bars, 170 beats = 70.83 s, a seamless loop (see synthkit.py).

The hook (A, eighths): B4- D5 C#5 D5- | B5--- G5- - a curious wiggle round D,
then a leap of a sixth; the same wiggle on A (bar 3) and on high D (bar 5).
Two borrowed chords keep it topsy-turvy: C minor straight after C major, and
E-flat major falling to D7.

check_lines() runs at import on the score the render plays: every melody note
on the one, or a beat or longer, is a tone of its chord; every shorter one
steps on to its next note; every accompaniment note is a chord tone (the
chords are voiced bar by bar round the tune, by voice()); nothing makes a
semitone or a minor ninth with anything sounding with it, and no two
sustained notes a major seventh. The clock is tuned to D7 (tick) and G6
(tock), both in the key; the ratchet is unpitched.

Instruments, all synthesised here:
  Clarinet   one continuous blown line per phrase: additive, odd harmonics
             strong in the low register and evens growing above it, a soft
             tongue, breath, a hint of vibrato.
  Bassoon    the same engine with a double reed's formants (near 480 Hz and
             1.15 kHz): staccato for the oom, legato for the river tune.
  Celesta    struck bars over resonators: fundamental, a weak octave, a
             brief inharmonic ping and a felt hammer; damped when its key is
             let go. Reversed for the river.
  Music box  steel tines (a clamped bar: partials 1 and 6.27), a pin click,
             damped at the barline when the next chord lacks the note.
  Harp       Karplus-Strong strings (grand_hotel.py's, with a circular
             excitation), bright pluck, long ring, damped at their gates.
  Clock      tuned ticks; the ratchet of the music box being wound.

    py lesson-template/build/block-camp-music/wonderland.py [--wav preview.wav] [--stems]
"""
import sys, itertools
from functools import lru_cache
import numpy as np
from scipy.signal import lfilter, bilinear
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, make_ir, reverb, pingpong, finish)

NAME = 'wonderland'
BEAT = 60 / 144                                  # 0.41667 s, 20000 samples
KEY = {7, 9, 11, 0, 2, 4, 6}                     # G major

# ── the form ────────────────────────────────────────────────────────────────
THEME_CH = ['G', 'G', 'Am', 'D7', 'G', 'E7', 'Am', 'D7', 'G', 'G', 'C', 'Cm', 'G', 'Eb', 'D7', 'G']
INTRO_CH = THEME_CH[0:4] + THEME_CH[12:16]
BARS = ([('intro', c, 3) for c in INTRO_CH] + [('A', c, 3) for c in THEME_CH] +
        [('B', c, 3) for c in THEME_CH[::-1]] + [('stolen', 'G', 2)] + [("A'", c, 3) for c in THEME_CH])
NB = len(BARS)                                   # 57
START = np.concatenate([[0], np.cumsum([n for _, _, n in BARS])]).astype(int)
LOOPB = int(START[-1])                           # 170 beats
tl = Timeline(bpm=4 * 144, bars=LOOPB, pre=24, post=6)     # one Timeline "bar" = one beat
assert abs(tl.bar - BEAT) < 1e-12
LOOP = tl.loop                                   # 70.833 s

CH = {
    'G':  {7, 11, 2}, 'Am': {9, 0, 4}, 'D7': {2, 6, 9, 0}, 'E7': {4, 8, 11, 2},
    'C':  {0, 4, 7}, 'Cm': {0, 3, 7}, 'Eb': {3, 7, 10},
}
ROOT = {'G': 43, 'Am': 45, 'D7': 38, 'E7': 40, 'C': 48, 'Cm': 48, 'Eb': 39}       # the bassoon's oom
FIFTH = {'G': 38, 'Am': 40, 'D7': 45, 'E7': 47, 'C': 43, 'Cm': 43, 'Eb': 46}
THIRD = {'G': 11, 'Am': 0, 'D7': 6, 'E7': 8, 'C': 4, 'Cm': 3, 'Eb': 7}


def bar_of(beat):
    return int(np.searchsorted(START, beat % LOOPB, side='right') - 1)


def chord_at(beat):
    return BARS[bar_of(beat)][1]


# ── the tune: (midi, eighths) per bar, six eighths a bar ────────────────────
THEME = [
    [(71, 2), (74, 1), (73, 1), (74, 2)],        # G   B D C# D
    [(83, 4), (79, 2)],                          # G   B G
    [(76, 2), (81, 1), (80, 1), (81, 2)],        # Am  E A G# A
    [(84, 4), (81, 2)],                          # D7  C A
    [(83, 2), (86, 1), (85, 1), (86, 2)],        # G   B D C# D
    [(83, 2), (80, 2), (76, 2)],                 # E7  B G# E
    [(81, 2), (84, 1), (83, 1), (81, 2)],        # Am  A C B A
    [(78, 2), (81, 2), (84, 2)],                 # D7  F# A C
    [(71, 2), (74, 1), (73, 1), (74, 2)],        # G   B D C# D
    [(83, 4), (79, 2)],                          # G   B G
    [(79, 2), (84, 1), (83, 1), (84, 2)],        # C   G C B C
    [(87, 4), (84, 2)],                          # Cm  Eb C
    [(83, 2), (79, 2), (74, 2)],                 # G   B G D
    [(79, 2), (75, 2), (70, 2)],                 # Eb  G Eb Bb
    [(81, 2), (78, 1), (76, 1), (74, 2)],        # D7  A F# E D
    [(79, 6)],                                   # G   G
]
for row in THEME:
    assert sum(d for _, d in row) == 6, row
RIVER = [row[::-1] for row in THEME[::-1]]       # the tune backwards
INTRO = THEME[0:4] + THEME[12:16]
RUN = [67, 69, 71, 74, 76, 79, 81, 83, 86, 88, 91]      # the stolen bar: G4 up to G6, pentatonic (no semitone)


def tune_rows(sec):
    return {'intro': INTRO, 'A': THEME, 'B': RIVER, "A'": THEME}.get(sec)


# ── voicing: chords placed round the tune ───────────────────────────────────
def clash(a, b, long_):
    iv = abs(a - b)
    return iv in (1, 13) or (long_ and iv % 12 in (1, 11))


def voice(c, lo, hi, avoid, prev, n=3):
    """n chord tones in [lo, hi] (the third always), no semitone, major 7th
    or minor 9th inside, none against `avoid` (midi, long), as close to
    `prev` as that allows. Distinct pitch classes within a 14th if it can;
    a wider spread, then a doubled tone, only if the tune rules that out;
    last, a two-note open fifth with no third (the river's Am, where the tune's B4
    under it leaves C6 a minor ninth and no other C in range)."""
    pcs = CH[c]
    cands = [m for m in range(lo, hi + 1) if m % 12 in pcs]
    for k, distinct, span, third in ((n, n, 14, True), (n, n, 19, True), (n, n - 1, 14, True), (n, n - 1, 19, True),
                                     (n - 1, n - 1, 19, False)):
        best, best_cost = None, 1e9
        for combo in itertools.combinations(cands, k):
            if combo[-1] - combo[0] > span or len({m % 12 for m in combo}) < distinct:
                continue
            if third and THIRD[c] not in {m % 12 for m in combo}:
                continue
            if any(clash(a, b, True) for a, b in itertools.combinations(combo, 2)):
                continue
            if any(clash(m, a, lg) for m in combo for a, lg in avoid):
                continue
            cost = (sum(abs(a - b) for a, b in zip(combo, prev)) if prev else 0) + 0.1 * abs(np.mean(combo) - (lo + hi) / 2)
            if cost < best_cost:
                best, best_cost = combo, cost
        if best:
            return best
    raise AssertionError(('no voicing', c, lo, hi, avoid))


# ── the score: every pitched note, in beats ─────────────────────────────────
def score():
    """(start beat, midi, beats sounding, part)."""
    ev = []
    mel_in_bar = {}

    def mel(part, t, row, shift):
        pos = 0
        for m, d in row:
            if m:
                ev.append((t + pos / 2, m + shift, d / 2, part))
                mel_in_bar.setdefault(bar_of(t), []).append((m + shift, d >= 2))
            pos += d

    for b, (sec, c, nbeats) in enumerate(BARS):
        t = int(START[b]); rows = tune_rows(sec)
        k = b - {'intro': 0, 'A': 8, 'B': 24, "A'": 41}.get(sec, 0)
        if sec == 'intro':
            mel('box', t, rows[k], 12)
        elif sec == 'A':
            mel('clar', t, rows[k], 0)
        elif sec == 'B':
            mel('bsn', t, rows[k], -12)
        elif sec == "A'":
            mel('cel', t, rows[k], 0)
            mel('box', t, rows[k], 12)
        else:                                                      # the stolen bar: the run, ringing
            for j, m in enumerate(RUN):
                s_ = t + j * 2 / len(RUN)
                # a passing tone (A, E over G) is damped inside the beat; the chord tones ring on
                ring = 1.2 if m % 12 in CH[c] else 0.9
                ev.append((s_, m, min(ring, t + 2 - s_), 'run'))
                mel_in_bar.setdefault(b, []).append((m, False))

    # the music box rings: a chord tone on to the barline (and past it, if the
    # next chord has it), unless a tune note a semitone or minor 9th away comes first
    tune = sorted(e for e in ev if e[3] in ('box', 'cel'))
    for i, e in enumerate(ev):
        s_, m, d, part = e
        if part != 'box':
            continue
        b = bar_of(s_); end = START[b + 1]
        if m % 12 not in CH[BARS[b][1]]:
            continue
        if m % 12 in CH[BARS[(b + 1) % NB][1]]:
            end += 0.5
        for s2, m2, d2, p2 in tune:
            if s_ < s2 < end and clash(m, m2, False):
                end = s2
        ev[i] = (s_, m, max(d, end - s_), part)

    # the clarinet's counter-line in A': a chord tone a bar, near the last, rubbing on nothing
    prev = 62
    for b in range(41, 57):
        c = BARS[b][1]; t = int(START[b])
        avoid = mel_in_bar.get(b, [])
        cands = [m for m in range(55, 70) if m % 12 in CH[c] and not any(clash(m, a, True) for a, _ in avoid)]
        m = min(cands, key=lambda x: (abs(x - prev) == 0, abs(x - prev), x))
        ev.append((t, m, 3.0, 'ctr'))
        mel_in_bar.setdefault(b, []).append((m, True))
        prev = m

    # accompaniment
    prev_pah, prev_sw = None, None
    for b, (sec, c, nbeats) in enumerate(BARS):
        t = int(START[b]); nxt = CH[BARS[(b + 1) % NB][1]]
        avoid = mel_in_bar.get(b, [])
        if sec in ('A', "A'") or (sec == 'intro' and b >= 4):
            alt = (b % 2 == 1 and BARS[b - 1][1] == c)
            ev.append((t, FIFTH[c] if alt else ROOT[c], 0.45, 'oom'))
            v = voice(c, 55, 72, avoid, prev_pah)
            prev_pah = v
            part = 'pah-cel' if sec == 'A' else 'pah-harp'
            for q in (1, 2):
                for m in v:
                    ev.append((t + q, m, 0.55 if q == 1 else (0.9 if m % 12 in nxt else 0.85), part))
        elif sec == 'B':
            ev.append((t, ROOT[c] if b % 2 == 0 else FIFTH[c], 2.9, 'harpbass'))
            v = voice(c, 77, 92, avoid, prev_sw)
            prev_sw = v
            for m in v:
                ev.append((t, m, 3.0, 'swell'))
        elif sec == 'stolen':
            ev.append((t, ROOT[c], 1.9, 'harpbass'))
    return sorted(ev)


EVENTS = score()
MEL = ('box', 'clar', 'bsn', 'cel', 'ctr', 'run')
TICK, TOCK = 98, 91                              # D7, G6


def check_lines(ev=EVENTS):
    bad = []
    by_part = {}
    for e in ev:
        by_part.setdefault(e[3], []).append(e)
    for e in ev:
        s, m, d, part = e
        b0, b1 = bar_of(s), bar_of(s + d - 1e-6)
        chords = [BARS[b % NB][1] for b in range(b0, b0 + ((b1 - b0) % NB) + 1)]
        if part in MEL:
            strong = abs(s - START[b0]) < 1e-9
            if strong or d >= 1:
                if any(m % 12 not in CH[c] for c in chords):
                    bad.append((part, s, m, chords, 'not a chord tone'))
            elif m % 12 not in CH[chords[0]] and part != 'run':
                line = by_part[part]; j = line.index(e)
                nx = line[(j + 1) % len(line)][1]
                if not 0 < abs(nx - m) <= 2:
                    bad.append((part, s, m, chords[0], 'a non-chord tone that does not step on'))
            elif part == 'run' and m % 12 not in KEY:
                bad.append((part, s, m, 'run out of the key'))
        else:
            if any(m % 12 not in CH[c] for c in chords):
                bad.append((part, s, m, chords, 'accompaniment not a chord tone'))
    ext = sorted(ev + [(s + LOOPB, m, d, p) for s, m, d, p in ev if s < 6])
    same = []
    for i, (s1, m1, d1, p1) in enumerate(ext):
        if s1 >= LOOPB:
            break
        for s2, m2, d2, p2 in ext[i + 1:]:
            if s2 >= s1 + d1 - 1e-9:
                break
            if p1 == p2 or {p1, p2} in same:
                continue
            if clash(m1, m2, d1 >= 1 and d2 >= 1):
                bad.append(('clash', p1, s1, m1, p2, s2, m2, chord_at(s2)))
    for m in (TICK, TOCK):
        if m % 12 not in KEY:
            bad.append(('clock', m))
    print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad[:12])
    assert not bad, 'a wrong note (listed above)'


check_lines()


# ── blown lines: additive, one continuous line per phrase ───────────────────
def clar_amp(k, f0, fk):
    odd = k % 2 == 1
    even_w = 0.08 + 0.55 * np.clip((f0 - 330) / 500, 0, 1)            # evens grow above the throat
    a = k ** -0.9 * (1.0 if odd else even_w)
    return a * 10 ** (-np.clip(fk - 2500, 0, None) / 1000 * 3.2 / 20)   # gently down above 2.5 kHz


def bsn_amp(k, f0, fk):
    lf = np.log2(np.maximum(fk, 20))
    db = (9 * np.exp(-((lf - np.log2(480)) / 0.45) ** 2) + 6 * np.exp(-((lf - np.log2(1150)) / 0.35) ** 2)
          + 3 * np.exp(-((lf - np.log2(2900)) / 0.4) ** 2) - 6 * np.clip(np.log2(np.maximum(fk, 1) / 3500), 0, None) * 3
          - 8 * (k == 1))
    return k ** -0.55 * 10 ** (db / 20)


def blown_line(notes, amp_fn, seed, vib_depth=0.04, vib_rate=5.0, attack=0.03, release=0.09, glide=0.02,
               breath=0.02, top=12000.0, staccato=False):
    """notes: [(t seconds, midi, seconds)] -> the line from notes[0][0]."""
    t_start = notes[0][0]
    end = max(t + d for t, _, d in notes) - t_start
    n = int((end + release + 0.2) * SR)
    lf = np.full(n, np.log2(hz(notes[0][1])))
    g = np.zeros(n); vib = np.zeros(n)
    r = rng('blow', seed)
    for j, (t, m, d) in enumerate(notes):
        a, b = int((t - t_start) * SR), int((t - t_start + d) * SR)
        nxt = notes[j + 1] if j + 1 < len(notes) else None
        legato_in = j > 0 and abs(notes[j - 1][0] + notes[j - 1][2] - t) < 1e-6 and not staccato
        legato_out = nxt is not None and abs(t + d - nxt[0]) < 1e-6 and not staccato
        lf[a:] = np.log2(hz(m))
        tt = np.arange(b - a) / SR
        env = np.minimum(1, (0.7 if legato_in else 0.0) + tt / attack * (0.3 if legato_in else 1.0))
        env = env * (1 + 0.15 * np.exp(-tt / 0.05))                 # a little tongue
        if legato_out:
            k = min(int(0.03 * SR), b - a)
            env[b - a - k:] *= np.linspace(1, 0.82, k)
            g[a:b] = env
        else:
            g[a:b] = env
            k = int(release * SR)
            g[b:b + k] = env[-1] * np.exp(-np.arange(min(k, n - b)) / SR / (release / 3))
        vib[a:b] = np.clip((tt - 0.25) / 0.3, 0, 1)
    al = np.exp(-1 / (glide * SR))
    lf = lfilter([1 - al], [1, -al], lf - lf[0]) + lf[0]
    g = lp1(g, 60)
    t = np.arange(n) / SR
    f = 2 ** lf * 2 ** (vib_depth / 12 * lp1(vib, 6) * np.sin(2 * np.pi * vib_rate * t + r.uniform(0, 6)))
    ph = 2 * np.pi * np.cumsum(f) / SR
    f0 = 2 ** lf
    x = np.zeros(n)
    for k in range(1, int(min(40, top / f0.min())) + 1):
        fk = k * f
        x += amp_fn(k, f0, fk) * (fk < top) * np.sin(k * ph + r.uniform(0, 6.28))
    z = r.standard_normal(n)
    x += breath * (bp(z, 2.2 * hz(notes[0][1]), 2.0) * 0.6 + lp1(hp1(z, 4000), 12000))
    return x * g


def phrases(part, gap=0.99):
    notes = [(s * BEAT, m, d * BEAT) for s, m, d, p in EVENTS if p == part]
    out, cur = [], []
    for nt in notes:
        if cur and nt[0] - (cur[-1][0] + cur[-1][2]) > BEAT * gap:
            out.append(cur); cur = []
        cur.append(nt)
    if cur:
        out.append(cur)
    return out


# ── struck and plucked ──────────────────────────────────────────────────────
@lru_cache(maxsize=None)
def celesta(m, gate, v=1.0):
    f = hz(m); n = int((gate + 0.08) * SR); t = np.arange(n) / SR
    tau = float(np.interp(m, [55, 96], [1.6, 0.6]))
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / tau) + 0.18 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / (tau * 0.4))
         + 0.1 * np.sin(2 * np.pi * 4.07 * f * t) * np.exp(-t / 0.03) * (f * 4.07 < 18000))
    z = np.random.default_rng(m).standard_normal(n)
    x += 0.12 * lp1(hp1(z, 1500), 6000) * np.exp(-t / 0.004)                # the felt hammer
    x *= np.minimum(1, t / 0.0015)
    return x * np.clip((gate + 0.06 - t) / 0.06, 0, 1) * v                   # the damper


@lru_cache(maxsize=None)
def music_box(m, gate):
    f = hz(m); n = int((gate + 0.06) * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 1.1)
    if 6.27 * f < 19000:
        x += 0.2 * np.sin(2 * np.pi * 6.27 * f * t) * np.exp(-t / 0.07)
    z = np.random.default_rng(m + 1).standard_normal(n)
    x += 0.25 * hp1(z, 4000) * np.exp(-t / 0.0015) * np.minimum(1, t / 0.0005)   # the pin
    x *= np.minimum(1, t / 0.001)
    return x * np.clip((gate + 0.05 - t) / 0.05, 0, 1)


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
    """Circular, zero-start excitation (see sherlock.py)."""
    kk = np.arange(1, int(max(2, min(48, top / f))) + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -tilt * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    Z = np.fft.rfft(np.random.default_rng(seed).uniform(-1, 1, N))
    Z /= np.sqrt(1 + (np.fft.rfftfreq(N, 1 / SR) / 3500) ** 2)
    z = np.fft.irfft(Z, N)
    exc += noise * z / (np.abs(z).max() + 1e-12)
    exc = exc - 0.5 * np.roll(exc, max(1, int(comb * N)))
    zc = np.nonzero((exc[:-1] <= 0) & (exc[1:] > 0))[0]
    if len(zc):
        exc = np.roll(exc, -int(zc[0] + 1))
    return exc / np.abs(exc).max()


@lru_cache(maxsize=None)
def harp(m, gate, v=1.0):
    f = hz(m)
    N, c, den = ks_setup(f, 0.8, float(np.interp(m, [36, 60, 90], [4.0, 2.5, 1.2])))
    exc = pick(N, f, 0.9, 0.06, 0.12, m, top=9000)
    n = int((gate + 0.07) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    return y * np.clip((gate + 0.06 - t) / 0.06, 0, 1)


def tick(m, v, seed):
    n = int(0.05 * SR); t = np.arange(n) / SR
    f = hz(m)
    z = np.random.default_rng(seed).standard_normal(n)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.008) + 0.4 * np.sin(2 * np.pi * 1.5 * f * t) * np.exp(-t / 0.004)
    x += 0.4 * hp(z, 5000) * np.exp(-t / 0.002)
    return x * np.minimum(1, t / 0.001) * v


def ratchet(seed, clicks=9, gap=0.045):
    n = int((clicks * gap + 0.1) * SR); x = np.zeros(n)
    r = rng('ratchet', seed)
    for j in range(clicks):
        i = max(0, int((j * gap + r.uniform(-0.003, 0.003)) * SR))      # the first click can jitter early
        k = int(0.02 * SR); t = np.arange(k) / SR
        z = r.standard_normal(k)
        x[i:i + k] += (bp(z, 2600, 2.0) + 0.5 * bp(z, 5200, 2.5)) * np.exp(-t / 0.004) * np.minimum(1, t / 0.0006) \
            * (0.7 + 0.3 * (j % 2))
    return x


# ── render ──────────────────────────────────────────────────────────────────
def add_laps(bus, t, sig, pan=0.0, gain=1.0):
    for lap in (-1, 0, 1):
        tt = t + lap * LOOP
        if tt + len(sig) / SR > -tl.t0 and tt < LOOP + tl.post * BEAT:
            bus.add(tt, sig, pan=pan, gain=gain)


def render(wav=None):
    clar, bsn, cel, box, harp_b, clock, low = (tl.bus() for _ in range(7))

    for part, bus, fn, gain, pan, kw in (
            ('clar', clar, clar_amp, 0.11, 0.1, dict(breath=0.025)),
            ('bsn', bsn, bsn_amp, 0.13, -0.15, dict(vib_depth=0.08, vib_rate=4.6, attack=0.04, breath=0.015)),
            ('ctr', clar, clar_amp, 0.07, -0.3, dict(attack=0.2, release=0.25, breath=0.02))):
        for k, ph in enumerate(phrases(part)):
            add_laps(bus, ph[0][0], blown_line(ph, fn, len(part) * 1000 + k, **kw), pan=pan, gain=gain)

    for s, m, d, part in EVENTS:
        t = s * BEAT; b = bar_of(s); sec = BARS[b][0]
        if part == 'oom':
            x = blown_line([(0.0, m, d * BEAT)], bsn_amp, m, attack=0.012, release=0.06, staccato=True, breath=0.01)
            add_laps(low, t, x, pan=-0.1, gain=0.15 if sec != 'intro' else 0.12)
        elif part == 'pah-cel':
            add_laps(cel, t, celesta(m, round(d * BEAT, 4), 0.8), pan=0.25 + (m - 64) / 40, gain=0.09)
        elif part == 'pah-harp':
            g = 0.06 if sec == 'intro' else 0.075
            add_laps(harp_b, t + (m - 55) * 0.0015, harp(m, round(d * BEAT, 4), 0.8), pan=-0.3 + (m - 64) / 40, gain=g)
        elif part == 'harpbass':
            add_laps(harp_b, t, harp(m, round(d * BEAT, 4)), pan=-0.05, gain=0.2)
        elif part == 'swell':
            x = celesta(m, round(d * BEAT - 0.08, 4))[::-1].copy()      # the river's chords, backwards
            k = int(0.012 * SR); x[-k:] *= np.cos(np.linspace(0, np.pi / 2, k)) ** 2
            # the reversed note's cut lands on the next barline
            add_laps(cel, t + d * BEAT - len(x) / SR, x, pan=-0.4 + (m - 77) / 15 * 0.8, gain=0.075)
        elif part == 'cel':
            add_laps(cel, t, celesta(m, round(d * BEAT, 4), 1.0), pan=0.15, gain=0.14)
        elif part == 'box':
            add_laps(box, t, music_box(m, round(d * BEAT, 4)), pan=0.3, gain=0.12 if sec == 'intro' else 0.06)
        elif part == 'run':
            add_laps(cel, t, celesta(m, round(d * BEAT, 4), 0.7 + 0.3 * (m - 67) / 24), pan=-0.5 + (m - 67) / 24,
                     gain=0.1)

    # the clock: a tick a beat, tock on the one; silent in the stolen bar
    for b, (sec, c, nbeats) in enumerate(BARS):
        if sec == 'stolen':
            continue
        for q in range(nbeats):
            s = START[b] + q
            g = 0.05 if sec in ('intro', 'B') else 0.042
            add_laps(clock, s * BEAT, tick(TOCK if q == 0 else TICK, 1.0 if q == 0 else 0.7, int(s)), pan=0.45, gain=g)
    add_laps(clock, (START[56] + 1) * BEAT, ratchet(1), pan=0.35, gain=0.05)   # winding the box for the intro

    boxx = box.x + pingpong(box.x, BEAT, 0.3, 4, 6000) * 0.5
    room = make_ir(1.7, dark=8000, seed=57, pre=0.015)
    stems = dict(clarinet=clar.x, bassoon=bsn.x, celesta=cel.x, music_box=boxx, harp=harp_b.x, oom=low.x,
                 clock=clock.x)
    wet = reverb(hp1(clar.x * 0.35 + bsn.x * 0.3 + cel.x * 0.45 + boxx * 0.5 + harp_b.x * 0.35 + low.x * 0.08
                     + clock.x * 0.2, 120), room)
    stems['room'] = wet * 0.45
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        print_stems(stems, mix)
    return finish(tl, mix, NAME, wav=wav)


def a_weight(x):
    f1, f2, f3, f4 = 20.598997, 107.65265, 737.86223, 12194.217
    num = [(2 * np.pi * f4) ** 2 * 10 ** (1.9997 / 20), 0, 0, 0, 0]
    den = np.polymul([1, 4 * np.pi * f4, (2 * np.pi * f4) ** 2], [1, 4 * np.pi * f1, (2 * np.pi * f1) ** 2])
    den = np.polymul(np.polymul(den, [1, 2 * np.pi * f3]), [1, 2 * np.pi * f2])
    b, a = bilinear(num, den, SR)
    return lfilter(b, a, x, axis=0)


def print_stems(stems, mix):
    i0 = tl.smp(0)
    secs = [('intro', 0, 8), ('A', 8, 24), ('B', 24, 40), ('stolen', 40, 41), ("A'", 41, 57)]
    seg = lambda x, b0, b1: x[i0 + int(START[b0] * BEAT * SR):i0 + int(START[b1] * BEAT * SR)]
    mw = a_weight(mix)
    print(f'{"A-wt dB vs mix":16s}' + ''.join(f'{s:>8s}' for s, _, _ in secs))
    for k, v in stems.items():
        vw = a_weight(v)
        row = []
        for _, b0, b1 in secs:
            p = np.mean(seg(vw, b0, b1) ** 2)
            row.append(10 * np.log10(p / np.mean(seg(mw, b0, b1) ** 2)) if p > 1e-10 else -99)
        print(f'{k:16s}' + ''.join(f'{r:8.1f}' for r in row))


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
