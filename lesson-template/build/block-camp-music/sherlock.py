#!/usr/bin/env python3
"""Block Camp soundtrack "The Blue Hour" (Sherlock Holmes: The Blue Hour RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is Victorian
London at dusk: a stolen Blue Star, a museum clock that rings at nine, a
guard who leaves his post for tea, a metal owl on the roof, and Holmes
reading the city's routines (Present Simple). So: the idiom of a gaslit
detective score - a solo violin (Holmes's own instrument) carrying the
tune, a string section plucking a "deduction" ostinato under it, a walking
pizzicato bass for the streets, muted low strings holding the harmony, a
pocket watch ticking, and one church bell striking the hour at the top of
the loop. An original piece in that idiom: no melody or progression is
taken from any film or series.

D minor, 96 BPM, 4/4 (a beat is exactly 30000 samples, a bar 2.5 s). One
chord a bar:

  intro  Dm | Dm | Bb | A7                         bars 0-3    the bell, the watch, low strings;
                                                               the ostinato creeps in, a high harmonic
  A      Dm | Gm | A7 | Dm | Bb | Gm | E7 | A7     bars 4-11   the violin tune over the ostinato
  B      Bb | F  | Gm | Dm | Bb | F  | E7 | A7     bars 12-19  the streets: a walking pizzicato bass,
                                                               the violin long and high, the watch
  A'     Dm | Gm | A7 | Dm | Bb | Gm | A7 | Dm     bars 20-27  the tune again, a bowed cello
                                                               counter-line under it
  coda   Bb | Gm | A7 | A7                         bars 28-31  the violin climbs and stops; the
                                                               plucked A7 and the watch alone -> the bell

The hook (A, eighths): A4 D5 F5 E5 D5- A5- | Bb5- A5 G5 D5- G5- - the
question that opens every A, rising from the fifth through the tonic chord.

check_lines() runs at import and proves the harmony from the same score the
render plays: every violin and cello note on beat 1 or 3, or a beat or
longer, is a tone of its chord (and of the next chord, if it is held across
the barline); every shorter one steps on to its next note; every plucked
and held accompaniment note is a chord tone; no note makes a semitone or a
minor ninth with anything sounding with it, and no two sustained notes make
a major seventh. The pitched percussion is in the key: the watch ticks on
A6 and D6, the bell is a minor-third bell on D (its partials D, F and A)
and strikes only over D minor, damped before the Bb.

Instruments, all synthesised here:
  Violin     one continuous bowed line per phrase: additive harmonics through
             a violin body curve (resonances near 280 Hz, 450-560 Hz and the
             2.5-3 kHz bridge hill, with fine ripple), so the vibrato moves
             the partials across the resonances as on a real instrument;
             short glides between notes, bow-change dips, delayed vibrato,
             bow noise. A flautando harmonic in the intro.
  Pizzicato  Karplus-Strong strings (grand_hotel.py's string), a soft
             finger pluck, short gut decay and a small body; each note is
             damped when its gate ends, and at the barline if the next
             chord does not contain it.
  Bass       a plucked cello-and-bass string, root and fifth, or walking.
  Cello      the A' counter-line, bowed (the violin's engine, a cello body).
  Strings    muted low strings: three detuned bowed voices a note, dark.
  Watch      a pocket watch, tick on A6 and tock on D6, on the eighths.
  Bell       a church bell on D, partials D3 D4 F4 A4 D5 F5 A5 D6.
32 bars = 80 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/sherlock.py [--wav preview.wav] [--stems]
"""
import sys
from functools import lru_cache
import numpy as np
from scipy.signal import lfilter, bilinear
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, make_ir, reverb, pingpong, finish)

NAME = 'sherlock-blue-hour'
BARS = 32
tl = Timeline(bpm=96, bars=BARS, pre=4, post=1)
BAR, BEAT = tl.bar, tl.beat                      # 2.5 s, 0.625 s
LOOP = tl.loop                                   # 80 s
LOOPB = 4 * BARS                                 # the loop in beats
KEY = {2, 4, 5, 7, 9, 10, 0, 1}                  # D minor, natural and harmonic

# ── the changes ─────────────────────────────────────────────────────────────
#   bass: root, fifth   pad: muted strings   pz: the ostinato's four strings
CH = {
    'Dm': dict(pcs={2, 5, 9}, bass=(38, 45), pad=(50, 57, 65), pz=(50, 57, 62, 65)),
    'Gm': dict(pcs={7, 10, 2}, bass=(43, 38), pad=(55, 58, 62), pz=(50, 55, 58, 62)),
    'A7': dict(pcs={9, 1, 4, 7}, bass=(45, 40), pad=(55, 61, 64), pz=(52, 57, 61, 67)),
    'Bb': dict(pcs={10, 2, 5}, bass=(46, 41), pad=(53, 58, 62), pz=(50, 53, 58, 62)),
    'E7': dict(pcs={4, 8, 11, 2}, bass=(40, 47), pad=(52, 56, 62), pz=(52, 56, 59, 62)),
    'F':  dict(pcs={5, 9, 0}, bass=(41, 48), pad=(53, 57, 60), pz=(48, 53, 57, 60)),
}
CHORDS = (['Dm', 'Dm', 'Bb', 'A7'] +
          ['Dm', 'Gm', 'A7', 'Dm', 'Bb', 'Gm', 'E7', 'A7'] +
          ['Bb', 'F', 'Gm', 'Dm', 'Bb', 'F', 'E7', 'A7'] +
          ['Dm', 'Gm', 'A7', 'Dm', 'Bb', 'Gm', 'A7', 'Dm'] +
          ['Bb', 'Gm', 'A7', 'A7'])
assert len(CHORDS) == BARS


def section(lb):
    lb %= BARS
    return 'intro' if lb < 4 else 'A' if lb < 12 else 'B' if lb < 20 else "A'" if lb < 28 else 'coda'


def chord_at(beat):
    return CHORDS[int(np.floor(beat / 4 + 1e-9)) % BARS]


# ── the tunes: (midi, eighths) per bar, 0 = rest ─────────────────────────────
A_TUNE = {
    0: [(69, 1), (74, 1), (77, 1), (76, 1), (74, 2), (81, 2)],            # Dm  A D F E D A
    1: [(82, 2), (81, 1), (79, 1), (74, 2), (79, 2)],                     # Gm  Bb A G D G
    2: [(79, 2), (76, 1), (73, 1), (69, 2), (73, 1), (76, 1)],            # A7  G E C# A C# E
    3: [(74, 4), (0, 1), (69, 1), (74, 1), (77, 1)],                      # Dm  D, then A D F up
    4: [(86, 2), (84, 1), (82, 1), (77, 2), (74, 2)],                     # Bb  D C Bb F D
    5: [(82, 2), (81, 1), (79, 1), (86, 3), (82, 1)],                     # Gm  Bb A G D Bb
}
VLN = {}
for k in range(6):
    VLN[4 + k] = A_TUNE[k]; VLN[20 + k] = A_TUNE[k]
VLN[10] = [(86, 2), (83, 1), (80, 1), (76, 2), (80, 1), (83, 1)]          # E7  D B G# E G# B
VLN[11] = [(81, 3), (79, 1), (76, 2), (73, 2)]                            # A7  A G E C#: half close
VLN.update({
    12: [(77, 4), (74, 2), (77, 2)],                                      # Bb  F D F
    13: [(81, 4), (84, 2), (81, 2)],                                      # F   A C A
    14: [(82, 6), (81, 1), (79, 1)],                                      # Gm  Bb (A G)
    15: [(77, 6), (76, 1), (74, 1)],                                      # Dm  F (E D)
    16: [(86, 4), (82, 2), (77, 2)],                                      # Bb  D Bb F
    17: [(84, 4), (81, 2), (84, 2)],                                      # F   C A C
    18: [(86, 4), (83, 2), (80, 2)],                                      # E7  D B G#
    19: [(81, 4), (76, 2), (73, 2)],                                      # A7  A E C#, into A'
    26: [(88, 2), (85, 1), (81, 1), (79, 2), (76, 2)],                    # A7  E C# A G E
    27: [(74, 6), (0, 2)],                                                # Dm  D
    28: [(77, 2), (82, 2), (86, 4)],                                      # Bb  F Bb D
    29: [(86, 2), (82, 2), (79, 4)],                                      # Gm  D Bb G
    30: [(76, 8)],                                                        # A7  E, held
})
HARMONIC = {3: [(88, 8)]}                                                 # A7  a flautando E6
CELLO = {                                                                 # A': the bowed counter-line
    20: [(57, 4), (53, 4)], 21: [(55, 4), (58, 4)], 22: [(57, 4), (55, 4)], 23: [(53, 8)],
    24: [(53, 4), (50, 4)], 25: [(58, 4), (55, 4)], 26: [(57, 4), (61, 4)], 27: [(62, 8)],
}
# B: the walking bass, a quarter a beat (midi); beats 2 and 4 may pass
WALK = {
    12: [46, 50, 53, 43], 13: [41, 45, 48, 45], 14: [43, 46, 50, 48], 15: [50, 45, 41, 45],
    16: [46, 50, 53, 43], 17: [41, 48, 45, 41], 18: [40, 44, 47, 44], 19: [45, 49, 52, 49],
}
for tune in (VLN, HARMONIC, CELLO):
    for row in tune.values():
        assert sum(d for _, d in row) == 8, row
PZ_PAT = [0, 2, 1, 2, 3, 2, 1, 2]               # the ostinato, eighths, over the chord's four strings


# ── the score: every pitched note, in beats ─────────────────────────────────
def score():
    """(start beat, midi, beats sounding, part). The render plays exactly
    this list and check_lines() proves it."""
    ev = []
    for lb in range(BARS):
        t = lb * 4; c = CHORDS[lb]; v = CH[c]; sec = section(lb)
        nxt = CH[CHORDS[(lb + 1) % BARS]]['pcs']

        def gate(m, start, want):
            """ring for `want` beats, but stop at the barline if the next chord lacks the note"""
            end = start + want
            if end > t + 4 and m % 12 not in nxt:
                end = t + 4
            return end - start

        for tune, part in ((VLN, 'vln'), (HARMONIC, 'harm'), (CELLO, 'vc')):
            pos = 0
            for m, d in tune.get(lb, []):
                if m:
                    ev.append((t + pos / 2, m, d / 2, part))
                pos += d
        # the ostinato
        if sec in ('A', "A'") or (sec == 'intro' and lb >= 2):
            for k, ix in enumerate(PZ_PAT):
                m = v['pz'][ix]; s = t + k / 2
                ev.append((s, m, gate(m, s, 1.0), 'pz'))
        elif sec == 'coda':
            for q in range(4):
                if lb == 31 and q > 0:
                    m = (57, 52, 49)[q - 1]                    # A3 E3 C#3, winding down
                else:
                    m = v['pz'][(1, 3, 2, 3)[q]]
                ev.append((t + q, m, gate(m, t + q, 1.5), 'pz'))
        # the bass
        if sec == 'B':
            for q, m in enumerate(WALK[lb]):
                ev.append((t + q, m, 0.95, 'bass' if m % 12 in v['pcs'] else 'bass-pass'))
        elif sec == 'intro':
            ev.append((t, v['bass'][0], gate(v['bass'][0], t, 3.5), 'bass'))
        else:
            for q, m in ((0, v['bass'][0]), (2, v['bass'][1])):
                ev.append((t + q, m, gate(m, t + q, 1.9), 'bass'))
        # the muted strings
        for m in v['pad']:
            ev.append((t, m, 4.0, 'pad'))
    return sorted(ev)


EVENTS = score()


def check_lines(ev=EVENTS):
    """See the docstring. Melody = violin, harmonic, cello; accompaniment =
    pizzicato, held strings, bass. Pairs are checked across the seam too."""
    bad = []
    mel = ('vln', 'harm', 'vc')
    by_part = {}
    for e in ev:
        by_part.setdefault(e[3], []).append(e)
    for e in ev:
        s, m, d, part = e
        bars = range(int(np.floor(s / 4 + 1e-9)), int(np.ceil((s + d) / 4 - 1e-9)))
        chords = [CHORDS[b % BARS] for b in bars]
        pcs0 = CH[chords[0]]['pcs']
        if part in mel:
            strong = abs(s - round(s)) < 1e-9 and round(s) % 2 == 0
            if strong or d >= 1:
                if any(m % 12 not in CH[c]['pcs'] for c in chords):
                    bad.append((part, s, m, chords, 'not a chord tone'))
            elif m % 12 not in pcs0:
                line = by_part[part]; j = line.index(e)
                nx = line[(j + 1) % len(line)][1]
                if not 0 < abs(nx - m) <= 2:
                    bad.append((part, s, m, chords[0], 'a non-chord tone that does not step on'))
        elif part == 'bass-pass':
            line = sorted(by_part['bass'] + by_part['bass-pass']); j = line.index(e)
            nx = line[(j + 1) % len(line)][1]
            if round(s) % 2 == 0 or not 0 < abs(nx - m) <= 2:
                bad.append((part, s, m, chords[0], 'a passing bass note on a strong beat or not stepping'))
        else:
            if any(m % 12 not in CH[c]['pcs'] for c in chords):
                bad.append((part, s, m, chords, 'accompaniment not a chord tone'))
    # clashes: every overlapping pair from different parts, across the seam
    ext = ev + [(s + LOOPB, m, d, p) for s, m, d, p in ev if s < 8]
    ext.sort()
    for i, (s1, m1, d1, p1) in enumerate(ext):
        if s1 >= LOOPB:
            break
        for s2, m2, d2, p2 in ext[i + 1:]:
            if s2 >= s1 + d1 - 1e-9:
                break
            if p1 == p2 or {p1, p2} <= {'bass', 'bass-pass'}:
                continue
            iv = abs(m1 - m2)
            if iv in (1, 13) or (d1 >= 1 and d2 >= 1 and iv % 12 in (1, 11)):
                bad.append(('clash', p1, s1, m1, p2, s2, m2, chord_at(s2)))
    # the watch and the bell are tuned, and in the key
    for m in (WATCH_TICK, WATCH_TOCK):
        if m % 12 not in KEY:
            bad.append(('watch', m))
    for m in BELL_PARTIALS:
        if round(m) % 12 not in CH['Dm']['pcs']:
            bad.append(('bell', m))
    for lb in BELL_BARS:
        if CHORDS[lb] != 'Dm' or CHORDS[(lb + 1) % BARS] != 'Dm':
            bad.append(('bell over', lb, CHORDS[lb], CHORDS[(lb + 1) % BARS]))
    print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad[:12])
    assert not bad, 'a wrong note (listed above)'


WATCH_TICK, WATCH_TOCK = 93, 86                   # A6, D6
BELL_ROOT = 62                                    # D4 (the prime)
BELL_RATIOS = ((0.5, 1.0, 4.2), (1.0, 0.8, 2.6), (1.189, 0.55, 2.0), (1.5, 0.35, 1.5), (2.0, 0.6, 1.3),
               (2.378, 0.18, 0.8), (3.0, 0.14, 0.6), (4.0, 0.08, 0.4))     # ratio, amplitude, tau
BELL_PARTIALS = [BELL_ROOT + 12 * np.log2(r) for r, _, _ in BELL_RATIOS]
BELL_BARS = (0,)
check_lines()


# ── bowed strings: one continuous line through a body ───────────────────────
VIOLIN_BODY = [(100, -30), (190, -12), (280, 3), (360, -2), (450, 3), (560, 4), (800, -1), (1100, -5),
               (1600, -1), (2400, 5), (3100, 5), (4300, 1), (6000, 0), (8500, -2), (12000, -7), (16000, -18)]
CELLO_BODY = [(40, -30), (65, -10), (100, 2), (190, 3), (300, 0), (450, 2), (800, -4), (1400, -6),
              (2200, -8), (3500, -16), (6000, -30), (12000, -50)]
VIOLA_BODY = [(80, -26), (130, -8), (230, 3), (380, 1), (600, 2), (900, -3), (1500, -7), (2500, -12),
              (4000, -22), (8000, -40)]


def body_gain(f, curve, ripple_seed):
    lf = np.log2(np.maximum(f, 20.0))
    xs, ys = zip(*curve)
    db = np.interp(lf, np.log2(xs), ys)
    r = np.random.default_rng(ripple_seed)
    for per, depth in ((0.21, 2.5), (0.13, 2.0), (0.37, 1.5)):          # fine peaks: octaves per cycle
        db = db + depth * np.sin(2 * np.pi * lf / per + r.uniform(0, 6.28))
    return 10 ** (db / 20)


def bowed_line(notes, curve, seed, vib_depth=0.2, vib_rate=5.6, tilt=1.0, noise=0.03, top=11000.0,
               attack=0.07, release=0.16, glide=0.035, body_seed=7):
    """notes: [(t seconds from the line's start, midi, seconds)], gaps are rests.
    Returns the line, starting at notes[0][0]."""
    t_start = notes[0][0]
    end = max(t + d for t, _, d in notes) - t_start
    n = int((end + release + 0.3) * SR)
    lf = np.full(n, np.log2(hz(notes[0][1])))
    g = np.zeros(n); vib = np.zeros(n)
    r = rng('bow', seed)
    for j, (t, m, d) in enumerate(notes):
        a, b = int((t - t_start) * SR), int((t - t_start + d) * SR)
        nxt = notes[j + 1] if j + 1 < len(notes) else None
        legato_in = j > 0 and abs(notes[j - 1][0] + notes[j - 1][2] - t) < 1e-6
        legato_out = nxt is not None and abs(t + d - nxt[0]) < 1e-6
        lf[a:] = np.log2(hz(m))
        tt = np.arange(b - a) / SR
        env = np.minimum(1, (0.55 if legato_in else 0.0) + tt / attack * (0.45 if legato_in else 1.0))
        if d > 0.8:                                                       # a long note swells
            env = env * (0.88 + 0.12 * np.sin(np.pi * np.clip(tt / d, 0, 1)))
        if legato_out:                                                    # a bow change
            k = min(int(0.05 * SR), b - a)
            env[b - a - k:] *= np.linspace(1, 0.72, k)
            g[a:b] = env
        else:
            g[a:b] = env
            k = int(release * SR)
            g[b:b + k] = env[-1] * np.exp(-np.arange(min(k, n - b)) / SR / (release / 3))
        vib[a:b] = np.clip((tt - 0.17) / 0.3, 0, 1)
    # glides in pitch, not in Hz
    al = np.exp(-1 / (glide * SR))
    lf = lfilter([1 - al], [1, -al], lf - lf[0]) + lf[0]
    g = lp1(g, 35)
    vib = lp1(vib, 8)
    t = np.arange(n) / SR
    rate = vib_rate * (1 + 0.04 * np.sin(2 * np.pi * 0.37 * t + r.uniform(0, 6)))
    f = 2 ** lf * 2 ** (vib_depth / 12 * vib * np.sin(2 * np.pi * np.cumsum(rate) / SR + r.uniform(0, 6)))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.zeros(n)
    kmax = int(min(48, top / (2 ** lf.min())))
    for k in range(1, kmax + 1):
        fk = k * f
        amp = k ** -tilt * body_gain(fk, curve, body_seed) * (fk < top)
        x += amp * np.sin(k * ph + r.uniform(0, 6.28))
    z = r.standard_normal(n)
    hiss = bp(z, 3200, 0.6) * noise + lp1(hp1(hp1(z, 6500), 6500), 15000) * noise * 3.0
    return (x + hiss * (1 + 2 * np.exp(-((t - 0.0) / 0.04) ** 2))) * g


def line_events(part):
    """Group a part's notes into phrases: a rest of a beat or more splits."""
    notes = [(s * BEAT, m, d * BEAT) for s, m, d, p in EVENTS if p == part]
    phrases, cur = [], []
    for nt in notes:
        if cur and nt[0] - (cur[-1][0] + cur[-1][2]) > BEAT * 0.99:
            phrases.append(cur); cur = []
        cur.append(nt)
    if cur:
        phrases.append(cur)
    return phrases


@lru_cache(maxsize=None)
def pad_note(m, dur, att):
    """Muted low strings: three bowed voices six cents apart, dark."""
    n = int((dur + 0.3) * SR)
    x = np.zeros(n)
    for c in (-6, 0, 6):
        x += bowed_line([(0.0, m + c / 100, dur)], VIOLA_BODY, m * 10 + c, vib_depth=0.1, vib_rate=4.8,
                        tilt=1.1, noise=0.004, attack=att, release=0.22, top=4000.0, body_seed=29)[:n]
    return lp(x, 1500)


# ── plucked strings: Karplus-Strong, as grand_hotel.py ──────────────────────
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
    """One period of a band-limited ramp (harmonics falling as 1/k^tilt), a
    little noise, and a comb for where the string is plucked - all circular,
    so the buffer wraps without a step when the loop takes it round, and
    rotated to start at a zero crossing, so the pluck starts without one."""
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


def pizz(m, gate, v, seed, low=False):
    """A finger pluck, damped when its gate ends (40 ms)."""
    f = hz(m)
    t60 = float(np.interp(m, [36, 50, 70], [1.6, 0.9, 0.5])) if not low else 1.5
    N, c, den = ks_setup(f, 0.62 if not low else 0.55, t60)
    exc = pick(N, f, 0.95 if not low else 1.5, 0.12 if not low else 0.05, 0.17, seed, top=12000 if not low else 1600)
    n = int((gate + 0.05) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    thump = lp1(np.random.default_rng(seed + 5).standard_normal(n), 900) * np.exp(-t / 0.004) * np.minimum(1, t / 0.001) * 0.12 * v
    y = y + thump
    return y * np.clip((gate + 0.04 - t) / 0.04, 0, 1)


# ── percussion ──────────────────────────────────────────────────────────────
def watch(m, v, seed):
    """A pocket-watch escapement: a tuned ring and a tiny click."""
    n = int(0.05 * SR); t = np.arange(n) / SR
    f = hz(m)
    z = np.random.default_rng(seed).standard_normal(n)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.006) + 0.3 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.003)
    x += 0.6 * hp(z, 6000) * np.exp(-t / 0.002) * np.minimum(1, t / 0.0008)
    return x * np.minimum(1, t / 0.0012) * v


def bell(seed):
    f0 = hz(BELL_ROOT)
    n = int(5.0 * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    r = rng('bell', seed)
    for (ratio, a, tau), m in zip(BELL_RATIOS, BELL_PARTIALS):
        beat = 1 + 0.0007 * r.uniform(-1, 1)                             # each partial a doublet, beating slowly
        x += a * (np.sin(2 * np.pi * f0 * ratio * t) + 0.6 * np.sin(2 * np.pi * f0 * ratio * beat * t)) / 1.6 \
            * np.exp(-t / tau)
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.25 * bp(z, 2400, 1.2) * np.exp(-t / 0.008)                    # the clapper
    # struck at bar 0, it must be gone before the Bb at bar 2: damped over the second bar
    damp = np.clip((2 * BAR - 0.05 - t) / (BAR * 0.9), 0, 1) ** 2
    return x * np.minimum(1, t / 0.002) * damp


# ── render ──────────────────────────────────────────────────────────────────
def add_laps(bus, t, sig, pan=0.0, gain=1.0):
    """Place a sound at loop time t on every lap the timeline shows."""
    for lap in (-1, 0, 1):
        tt = t + lap * LOOP
        if tt + len(sig) / SR > -tl.t0 and tt < LOOP + tl.post * BAR:
            bus.add(tt, sig, pan=pan, gain=gain)


def render(wav=None):
    vln, vc, pad, pzb, low, watch_b, bell_b = (tl.bus() for _ in range(7))
    lvl = {'intro': 0.8, 'A': 1.0, 'B': 0.95, "A'": 1.05, 'coda': 0.9}

    # violin phrases (and the harmonic, and the cello line)
    for part, bus, curve, gain, pan, kw in (
            ('vln', vln, VIOLIN_BODY, 0.06, 0.12, dict(top=16000.0)),
            ('harm', vln, VIOLIN_BODY, 0.05, 0.12, dict(tilt=2.4, vib_depth=0.08, noise=0.06, attack=0.6)),
            ('vc', vc, CELLO_BODY, 0.11, -0.3, dict(vib_depth=0.16, vib_rate=5.0, tilt=0.9, noise=0.015,
                                                     attack=0.12, top=6000.0, body_seed=19))):
        for k, ph in enumerate(line_events(part)):
            add_laps(bus, ph[0][0], bowed_line(ph, curve, len(part) * 100 + k, **kw), pan=pan, gain=gain)

    for s, m, d, part in EVENTS:
        t = s * BEAT; lb = int(s // 4); sec = section(lb)
        if part == 'pz':
            acc = 1.0 if abs(s - round(s)) < 1e-9 else 0.7
            g = {'intro': 0.6, 'A': 1.0, "A'": 1.1, 'coda': 1.0}.get(sec, 1.0)
            add_laps(pzb, t, pizz(m, d * BEAT, acc, int(s * 8) * 7 + m), pan=-0.35 + (m - 50) / 17 * 0.6,
                     gain=0.22 * g)
        elif part in ('bass', 'bass-pass'):
            add_laps(low, t, pizz(m, d * BEAT, 1.0, int(s * 8) * 3 + m, low=True), pan=0.05,
                     gain=0.42 if sec != 'intro' else 0.34)
        elif part == 'pad':
            att = 1.4 if sec == 'intro' and lb < 2 else 0.35
            g = {'intro': 0.9, 'A': 0.8, 'B': 1.0, "A'": 0.7, 'coda': 1.0}[sec]
            add_laps(pad, t, pad_note(m, d * BEAT, att), pan=-0.4 + (m - 50) / 15 * 0.8, gain=0.022 * g)

    # the watch: all the way through, softer under the ostinato in A and A'
    for lb in range(BARS):
        sec = section(lb)
        if True:
            for e in range(8):
                g = {'intro': 0.07, 'B': 0.065, 'coda': 0.07}.get(sec, 0.05)
                add_laps(watch_b, lb * BAR + e * BEAT / 2,
                         watch(WATCH_TICK if e % 2 == 0 else WATCH_TOCK, 1.0 if e % 2 == 0 else 0.75, lb * 8 + e),
                         pan=0.5, gain=g)
    for lb in BELL_BARS:
        add_laps(bell_b, lb * BAR, bell(lb), pan=-0.1, gain=0.16)

    vx = vln.x + 0.5 * hp(vln.x, 8000)                          # a little more rosin and air on top
    pzx = pzb.x + 0.5 * bp(pzb.x, 520, 1.3) + 0.25 * bp(pzb.x, 2600, 1.5)
    lowx = low.x + 0.35 * bp(low.x, 180, 1.2)
    hall = make_ir(2.3, dark=9000, seed=41, pre=0.022)
    stems = dict(violin=vx, cello=vc.x, strings=pad.x, pizzicato=pzx, bass=lowx, watch=watch_b.x, bell=bell_b.x)
    wet = reverb(hp1(vx * 0.4 + vc.x * 0.3 + pad.x * 0.4 + pzx * 0.35 + lowx * 0.05 + watch_b.x * 0.25
                     + bell_b.x * 0.6, 120), hall)
    stems['hall'] = wet * 0.5
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
    """A-weighted level of each part against the whole mix, per section,
    over the bars where the part plays."""
    i0 = tl.smp(0)
    secs = [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ("A'", 20, 28), ('coda', 28, 32)]
    seg = lambda x, b0, b1: x[i0 + int(b0 * BAR * SR):i0 + int(b1 * BAR * SR)]
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
