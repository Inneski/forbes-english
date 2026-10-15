#!/usr/bin/env python3
"""Block Camp soundtrack "Long Way" (The Long Way Home RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is Homer's
Odyssey in a block-built world: from Troy past the Lotus-eaters, the Cyclops,
the bag of winds, Circe, the Sirens, Scylla and Charybdis and Poseidon's storm
to Ithaca at dawn. So: an epic ancient-Mediterranean voyage - a lyre, an aulos
(the Greek double reed) carrying the hero's tune, a frame drum rowing, a low
drone, a choir, and the wind over the sea. An original piece in that idiom:
no melody or progression is taken from any film or record.

C minor (aeolian, with a dorian F major for the Sirens), 90 BPM, 4/4 (a
sixteenth is exactly 8000 samples, a bar 2.667 s). One chord a bar:

  intro  Cm Cm Ab Bb                    bars 0-3    the sea: wind, the drone, the lyre alone
  A      Cm Cm Bb Bb Ab Ab G G          bars 4-11   rowing out: the frame drum and the oars;
                                                    the hero's tune on the aulos
  B      Eb Eb Bb Bb F F G G            bars 12-19  the Sirens: a wordless voice over a soft
                                                    choir, the lyre rippling in sixteenths,
                                                    finger cymbals
  C      Cm Ab Bb G Cm Ab Bb G          bars 20-27  the storm: a chord a bar, the big drum,
                                                    the choir full, the tune high, the wind up
  D      Eb Bb Ab G                     bars 28-31  the homecoming: the tune comes down to
                                                    rest on the leading note; back to the sea

The hook is the aulos's opening, G-C-Eb rising to G (a fourth, then the
minor triad), answered by a falling Andalusian line through Bb and Ab to G.
The lyre's eighths are grouped 3+3+2 against the drum's four-square rowing.

Instruments, all synthesised here:
  Lyre         Karplus-Strong strings (grand_hotel.py's: fractional all-pass
               tuning, a ramp pick, a comb near the bridge), gut-dark loss, a
               tortoise-shell soundbox (resonances near 280 Hz, 950 Hz and
               2.3 kHz). Each string rings until it is plucked again or the
               chord changes under it and it is not a tone of the new chord.
  Aulos        additive reed: odd harmonics stronger, formants near 1.3 and
               2.9 kHz, breath; a scoop into each note, delayed vibrato, and a
               quick upper-neighbour grace before long notes on the beat (only
               where the neighbour rubs nothing). One voice per passage.
  Siren voice  the same engine with an open "ah" (formants 800, 1200, 2800 Hz),
               wider vibrato, more air.
  Choir        four continuous voices of three detuned saws through three
               formants, gliding from chord to chord (so a change is a glide,
               never two chords at once).
  Drone        two continuous reed voices: C2 and G2; the C moves to D on the G
               chords (C against B) and the G rests on the Ab chords.
  Percussion   a frame drum (a low DUM on F2, rim teks), a big drum in the storm
               (C2, G1 on the G chords), finger cymbals (on F7), oar strokes.
  Sea          wind: noise through two band-passes swept by slow loop-periodic
               LFOs, gusting harder in the storm; a soft lap of waves.

Pitched percussion is tuned into the key: F is the one pitch class that is
never a semitone from a tone of any chord here, so the frame drum and the
finger cymbals sit on it; the big drum plays C, or G under the G chords.

check_lines() asserts at import: no chord, voicing or drone carries a
semitone; every lyre, choir and drone note is a chord tone; every aulos and
Siren note on beat 1 or 3, or a quarter or longer, is a chord tone; and no
melody note or grace note sits a semitone or a minor ninth from anything the
lyre, choir or drone is sounding.

32 bars = 85.33 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/long_way.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

NAME = 'long-way-home'
BARS = 32
tl = Timeline(bpm=90, bars=BARS)
BAR, BEAT, S16 = tl.bar, tl.beat, tl.s16          # 2.667 s, 0.667 s, 0.1667 s (8000 samples)
E8 = 2 * S16
LOOP = tl.loop                                     # 85.33 s
CHUNK = 250                                        # divides a sixteenth, the pre-roll and the loop
assert round(LOOP * SR) % CHUNK == 0 and tl.smp(0) % CHUNK == 0

# ── the changes ─────────────────────────────────────────────────────────────
#        pcs            lyre strings                  choir (four voices)
CH = {
    'Cm': ({0, 3, 7},   [48, 60, 63, 67, 72, 75], [55, 63, 67, 72]),
    'Ab': ({8, 0, 3},   [44, 56, 60, 63, 68, 72], [56, 63, 68, 72]),
    'Bb': ({10, 2, 5},  [46, 53, 58, 62, 65, 70], [58, 62, 65, 70]),
    'G':  ({7, 11, 2},  [43, 50, 59, 62, 67, 71], [55, 62, 67, 71]),
    'Eb': ({3, 7, 10},  [51, 58, 63, 67, 70, 75], [55, 63, 67, 70]),
    'F':  ({5, 9, 0},   [53, 57, 60, 65, 69, 72], [57, 65, 69, 72]),
    'Fm': ({5, 8, 0},   [53, 56, 60, 65, 68, 72], [56, 65, 68, 72]),
}
CHORDS = (['Cm', 'Cm', 'Ab', 'Bb'] +
          ['Cm', 'Cm', 'Bb', 'Bb', 'Ab', 'Ab', 'G', 'G'] +
          ['Eb', 'Eb', 'Bb', 'Bb', 'F', 'F', 'G', 'G'] +
          ['Cm', 'Ab', 'Fm', 'G', 'Cm', 'Ab', 'Fm', 'G'] +
          ['Eb', 'Bb', 'Ab', 'G'])
assert len(CHORDS) == BARS


def drone(c):
    """(low voice, high voice): C2 and C3; G1 and G2 under the G chords (C against B)."""
    return (31, 43) if c == 'G' else (36, 48)


def section(lb):
    return 'intro' if lb < 4 else 'A' if lb < 12 else 'B' if lb < 20 else 'C' if lb < 28 else 'D'


def part(name, lb):
    s = section(lb)
    return {
        'frame':  s in ('A', 'B', 'C', 'D') and lb != 31,
        'big':    s == 'C',
        'roll':   lb in (23, 27),
        'zils':   s in ('B', 'C', 'D') and lb % 2 == 0 or lb in (4, 8),
        'oars':   s in ('A', 'D'),
        'choir':  s in ('B', 'C', 'D'),
        'waves':  s in ('intro', 'D') and lb % 2 == 0,
    }[name]


LYRE_LEVEL = {'intro': 1.2, 'A': 0.85, 'B': 0.8, 'C': 0.9, 'D': 0.85}
CHOIR_LEVEL = {'intro': 0.0, 'A': 0.0, 'B': 0.7, 'C': 1.0, 'D': 0.6}
WIND = [(0, 1.0), (3.5, 0.9), (4.5, 0.45), (12, 0.4), (19.5, 0.45), (20.5, 1.0), (27.5, 1.0),
        (28.5, 0.55), (31, 0.8), (32, 1.0)]                 # (bar, level); periodic

# ── the lines: (midi, eighths), 0 = rest ─────────────────────────────────────
AULOS_A = [                                  # bars 4-11, the hero's tune
    (67, 3), (72, 1), (75, 4),               # 4  Cm   G, C Eb
    (72, 3), (75, 1), (79, 4),               # 5  Cm   C, Eb G (a passing D rubbed the lyre's Eb5)
    (77, 3), (72, 1), (74, 4),               # 6  Bb   F, C D
    (70, 2), (72, 1), (74, 1), (77, 4),      # 7  Bb   Bb C D F
    (75, 3), (74, 1), (72, 4),               # 8  Ab   Eb, D C
    (72, 6), (70, 1), (68, 1),               # 9  Ab   C, Bb Ab
    (67, 4), (71, 2), (74, 2),               # 10 G    G B D
    (71, 6), (0, 2),                         # 11 G    B
]
SIREN = [                                    # bars 12-19, the Sirens
    (75, 6), (77, 1), (79, 1),               # 12 Eb   Eb, F G
    (82, 4), (79, 2), (75, 2),               # 13 Eb   Bb G Eb
    (77, 8),                                 # 14 Bb   F
    (74, 6), (77, 2),                        # 15 Bb   D F
    (81, 8),                                 # 16 F    A (the dorian sixth)
    (77, 4), (72, 4),                        # 17 F    F C
    (74, 4), (71, 4),                        # 18 G    D B
    (74, 6), (0, 2),                         # 19 G    D
]
AULOS_C = [                                  # bars 20-31, the storm and the way home
    (79, 3), (75, 1), (72, 4),               # 20 Cm   G, Eb C
    (75, 3), (77, 1), (80, 4),               # 21 Ab   Eb, F Ab
    (77, 3), (75, 1), (72, 4),               # 22 Fm   F, Eb C
    (74, 2), (71, 1), (74, 1), (79, 4),      # 23 G    D B D G
    (72, 3), (75, 1), (84, 4),               # 24 Cm   C, Eb C
    (80, 3), (84, 1), (87, 4),               # 25 Ab   Ab, C Eb: the top of the storm
    (84, 3), (82, 1), (80, 4),               # 26 Fm   C, Bb Ab
    (79, 4), (74, 2), (71, 2),               # 27 G    G D B
    (79, 6), (77, 1), (75, 1),               # 28 Eb   G, F Eb
    (74, 4), (70, 4),                        # 29 Bb   D Bb
    (72, 8),                                 # 30 Ab   C
    (71, 6), (0, 2),                         # 31 G    B
]
LINES = (('aulos A', AULOS_A, 4), ('siren', SIREN, 12), ('aulos C', AULOS_C, 20))
SCALE = {'aeolian': {0, 2, 3, 5, 7, 8, 10}, 'dorian': {0, 2, 3, 5, 7, 9, 10}}    # dorian for the Sirens; B over G
GRACE = 0.075                                # seconds, taken from the end of the note before
FRAME_PITCH, ZIL_PITCH = 48, 101             # C3 (G2 under the G chords), F7
assert [sum(d for _, d in _l) for _, _l, _ in LINES] == [64, 64, 96]


def frame_pitch(c):
    return 43 if c == 'G' else FRAME_PITCH


def accompaniment(lb):
    """Every pitch the lyre, choir and drone can be sounding in loop bar lb."""
    c = CHORDS[lb]; pcs, ly, ch = CH[c]
    notes = set(ly) | {m for m in drone(c) if m}
    if part('choir', lb):
        notes |= set(ch)
    return notes


def chord_at_eighth(bar0, q):
    return CHORDS[(bar0 + q // 8) % BARS]


def graces(name, line, bar0):
    """(position in eighths of the target, grace midi) for each long note on a
    beat that follows a note: the scale step above it, if that step rubs
    nothing sounding where the grace falls (the end of the note before)."""
    out = []
    pos = 0; prev = 0
    for m, d in line:
        if m and prev and d >= 3 and pos % 2 == 0:
            lb = (bar0 + (pos - 1) // 8) % BARS               # where the grace sounds
            scale = SCALE['dorian' if name == 'siren' else 'aeolian'] | ({11} if CHORDS[lb] == 'G' else set())
            up = next(u for u in (m + 1, m + 2) if u % 12 in scale)
            if not any(abs(up - v) in (1, 13) for v in accompaniment(lb)) and up != prev:
                out.append((pos, up))
        prev = m; pos += d
    return out


def check_lines():
    bad = []
    for c, (pcs, ly, ch) in CH.items():
        if any((a - b) % 12 in (1, 11) for a in pcs for b in pcs):
            bad.append(('chord has a semitone', c))
        for nm, ms in (('lyre', ly), ('choir', ch), ('drone', [m for m in drone(c) if m])):
            if any(m % 12 not in pcs for m in ms) and nm != 'drone':
                bad.append((nm, c, ms))
        dr = {m % 12 for m in drone(c) if m}
        if any((a - b) % 12 in (1, 11) for a in dr for b in pcs):
            bad.append(('drone rubs', c))
        if any((frame_pitch(c) - p) % 12 in (1, 11) for p in pcs) or any((ZIL_PITCH - p) % 12 in (1, 11) for p in pcs):
            bad.append(('drum or cymbal rubs', c))
    for name, line, bar0 in LINES:
        pos = 0
        for m, d in line:
            if m:
                for q in range(pos, pos + d):
                    lb = (bar0 + q // 8) % BARS
                    c = CHORDS[lb]
                    if q == pos or q % 8 == 0:
                        strong = (q == pos and q % 4 == 0) or d >= 2 or q % 8 == 0
                        if strong and m % 12 not in CH[c][0]:
                            bad.append((name, 'not a chord tone', lb, q % 8, m, c))
                        rub = [v for v in accompaniment(lb) if abs(m - v) in (1, 13)]
                        if rub:
                            bad.append((name, 'rubs', lb, q % 8, m, c, rub))
            pos += d
        for p, g in graces(name, line, bar0):
            lb = (bar0 + (p - 1) // 8) % BARS
            if any(abs(g - v) in (1, 13) for v in accompaniment(lb)):
                bad.append((name, 'grace rubs', lb, g))
    print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad)
    assert not bad, 'a wrong note (listed above)'


check_lines()


# ── oscillators and filters ─────────────────────────────────────────────────
def _blep(p, dt):
    y = np.zeros_like(p)
    a = p < dt; u = p[a] / dt[a]; y[a] = 2 * u - u * u - 1
    b = p > 1 - dt; u = (p[b] - 1) / dt[b]; y[b] = u * u + 2 * u + 1
    return y


def saw_ph(p, dt):
    """A polyBLEP saw from a phase (cycles, mod 1) and its per-sample increment."""
    return 2 * p - 1 - _blep(p, dt)


def loop_phase(f):
    """Phase (cycles) of a timeline-long frequency track, nudged by well under
    a thousandth of a hertz so it advances a whole number of cycles per lap:
    a continuous oscillator that is seam-exact (as tidewater.py)."""
    ph = np.cumsum(f / SR); i0, N = tl.smp(0), int(round(LOOP * SR))
    d = ph[i0 + N] - ph[i0]
    ph -= (d - np.round(d)) / N * np.arange(len(ph))
    return ph % 1.0


def tv_bp(x, fc, q):
    """Band-pass whose centre is fc[j] for chunk j (state carried)."""
    out = np.empty_like(x); zi = np.zeros(2)
    for j, i in enumerate(range(0, len(x), CHUNK)):
        w = 2 * np.pi * min(fc[j], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + CHUNK], zi = lfilter(b / a[0], a / a[0], x[i:i + CHUNK], zi=zi)
    return out


def bar_curve(points, t):
    """A periodic curve through (bar, value) points, at loop time t (seconds)."""
    xs, ys = zip(*points)
    return np.interp((t % LOOP) / BAR, xs, ys)


# ── strings: Karplus-Strong, as grand_hotel.py ──────────────────────────────
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
    return exc / np.abs(exc).max()


def lyre(m, ring, v, seed):
    """A gut string, plucked with the fingertip; `ring` seconds until it is
    stopped (by the next pluck of the string or the hand), 20 ms to silence."""
    f = hz(m)
    t60 = float(np.interp(m, [43, 84], [3.4, 1.6]))
    N, c, den = ks_setup(f, 0.86, t60)
    exc = pick(N, f, 0.55, 0.2, 0.19, seed, top=11000)
    n = int((ring + 0.03) * SR); t = np.arange(n) / SR
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    y += 0.1 * v * hp1(np.random.default_rng(seed + 1).standard_normal(n), 3000) * np.exp(-t / 0.004)
    return y * np.clip((ring + 0.02 - t) / 0.02, 0, 1)


def soundbox(x):
    y = x + 0.5 * bp(x, 280, 1.4) + 0.35 * bp(x, 950, 1.8) + 0.25 * bp(x, 2300, 1.5)
    return hp1(y, 90)


# ── reeds and voices: one additive engine ───────────────────────────────────
AULOS = dict(formants=((1300, 380, 1.6), (2900, 600, 0.9)), tilt=0.75, even=0.55, breath=0.15,
             vib=(5.3, 16), scoop=45, top=9000)
VOICE = dict(formants=((800, 160, 2.2), (1200, 220, 1.4), (2800, 400, 0.8)), tilt=1.0, even=0.9,
             breath=0.06, vib=(5.0, 28), scoop=30, top=8000)


def sing(line, gr, timbre, bar0):
    """One continuous voice: (midi, eighths) and grace notes [(pos, midi)]."""
    total = sum(d for _, d in line) * E8
    n = int((total + 1.0) * SR)
    semi = np.zeros(n); g = np.zeros(n); vib = np.zeros(n); sc = np.zeros(n); burst = np.zeros(n)
    gmap = dict(gr)
    pos = 0; last = next(m for m, _ in line if m); prev_rest = True; e = 0
    for j, (m, d) in enumerate(line):
        a, e = int(round(pos * E8 * SR)), int(round((pos + d) * E8 * SR))
        tt = np.arange(e - a) / SR
        if m:
            nd = (e - a) / SR
            semi[a:e] = m; last = m
            nxt = line[j + 1][0] if j + 1 < len(line) else 0
            env = np.minimum(1, tt / 0.03) * (0.85 + 0.15 * np.sin(np.pi * np.clip(tt / nd, 0, 1)))
            env *= np.clip((nd - tt) / 0.05, 0.7 if nxt else 0.0, 1)
            g[a:e] = env
            vib[a:e] = np.clip((tt - 0.35) / 0.5, 0, 1) * (1.0 if nd > 0.6 else 0.2)
            sc[a:e] = -timbre['scoop'] * np.exp(-tt / 0.04) * (1.0 if prev_rest else 0.5)
            burst[a:e] = np.exp(-tt / 0.05) * (1.0 if prev_rest else 0.3)
            if pos + d in gmap:                         # the grace before the next note
                k = int(GRACE * SR)
                semi[e - k:e] = gmap[pos + d]
            prev_rest = False
        else:
            semi[a:e] = last; prev_rest = True
        pos += d
    semi[e:] = last
    g = lp1(g, 30)
    c = np.exp(-1 / (0.012 * SR))                       # a quick slur between notes
    semi = lfilter([1 - c], [1, -c], semi - semi[0]) + semi[0]
    t = np.arange(n) / SR
    rate, depth = timbre['vib']
    cents = sc + depth * vib * np.sin(2 * np.pi * rate * t + 0.3 * np.sin(2 * np.pi * 0.23 * t))
    f = hz(semi) * 2 ** (cents / 1200)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.zeros(n)
    for k in range(1, int(timbre['top'] / hz(min(m for m, _ in line if m))) + 1):
        fk = k * f
        amp = k ** -timbre['tilt'] * (1.0 if k % 2 else timbre['even'])
        amp = amp * (0.35 + sum(a_ * np.exp(-0.5 * ((fk - fc) / bw) ** 2) for fc, bw, a_ in timbre['formants']))
        x += amp * np.clip((timbre['top'] - fk) / 1500, 0, 1) * np.sin(k * ph)
    z = rng('breath', bar0).standard_normal(n)
    air = bp(z, 1800, 0.8) * (0.4 * burst + 0.25 * g) + hp1(z, 5000) * 0.25 * g
    return hp1(x, 150) * g + timbre['breath'] * air * 3


# ── continuous voices across the timeline: choir and drone ──────────────────
def voice_track(pitch_of_bar, level_of_bar, glide=0.06, fade_in=0.3, fade_out=0.3):
    """Pitch and gain tracks for one continuous voice across the timeline.
    pitch_of_bar(lb) is a midi note or None (the voice rests that bar; it
    waits on its next note). A change of pitch is a glide (95% in `glide` s)
    from the bar line. A voice getting quieter has finished by the bar line
    (fade_out before it); one getting louder starts at it (fade_in after)."""
    n = tl.n
    bars = [b for b in tl.bars_range()] + [tl.bars + tl.post]
    pitch = {}
    for b in bars:
        k = 0
        while pitch_of_bar((b + k) % BARS) is None:
            k += 1
        pitch[b] = pitch_of_bar((b + k) % BARS)
    level = {b: (level_of_bar(b % BARS) if pitch_of_bar(b % BARS) is not None else 0.0) for b in bars}
    semi = np.zeros(n); lv = np.zeros(n)
    for b in bars:
        i = max(tl.smp(b * BAR), 0); j = min(tl.smp((b + 1) * BAR), n)
        semi[i:j] = pitch[b]; lv[i:j] = level[b]
    for b in bars[1:]:
        old, new = level[b - 1], level[b]
        if old == new:
            continue
        w = fade_out if new < old else fade_in
        i0 = tl.smp(b * BAR - (w if new < old else 0)); k = int(w * SR)
        i0c, i1c = max(i0, 0), min(i0 + k, n)
        if i1c > i0c:
            lv[i0c:i1c] = old + (new - old) * (np.arange(i0c, i1c) - i0) / k
    c = np.exp(-1 / (glide * SR / 3))
    semi = lfilter([1 - c], [1, -c], semi - semi[0]) + semi[0]
    return semi, lp1(lv, 20)


def choir():
    t = np.arange(tl.n) / SR - tl.t0
    out = np.zeros((tl.n, 2))
    for k in range(4):
        semi, lv = voice_track(lambda lb, k=k: CH[CHORDS[lb]][2][k] if part('choir', lb) else None,
                               lambda lb: CHOIR_LEVEL[section(lb)], fade_in=1.2, fade_out=1.5)
        semi = semi + 0.07 * np.sin(2 * np.pi * (380 + 17 * k) * t / LOOP + k)     # ~4.5 Hz, whole cycles a lap
        x = np.zeros(tl.n)
        for j, cents in enumerate((-8, 0, 8)):
            f = hz(semi) * 2 ** (cents / 1200)
            x += saw_ph(loop_phase(f), f / SR)
        x /= 3
        y = bp(x, 760, 2.4) + 0.7 * bp(x, 1180, 3.0) + 0.3 * bp(x, 2700, 4.0)
        pan = (-0.55, -0.2, 0.2, 0.55)[k]
        out += np.stack([y * np.cos((pan + 1) * np.pi / 4), y * np.sin((pan + 1) * np.pi / 4)], 1) * lv[:, None] * np.sqrt(2)
    return out


def drone_voices():
    out = np.zeros(tl.n)
    for k in range(2):
        semi, lv = voice_track(lambda lb, k=k: drone(CHORDS[lb])[k], lambda lb: 1.0, glide=0.15,
                               fade_in=0.5, fade_out=0.35)
        f = hz(semi)
        ph = loop_phase(f)
        x = saw_ph(ph, f / SR)
        x = lp(lp1(x, 900), 700, 0.8)
        x = x + 0.6 * bp(x, 1300, 2.0)                  # a reed's nasal edge
        out += x * lv * (1.0 if k == 0 else 0.6)
    return out


# ── percussion and the sea ──────────────────────────────────────────────────
def frame_dum(m, seed, v=1.0):
    n = int(0.6 * SR); t = np.arange(n) / SR
    f = hz(m) * (1 + 0.25 * np.exp(-t / 0.03))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.22)
    x += 0.3 * np.sin(2 * np.pi * np.cumsum(f * 1.59) / SR) * np.exp(-t / 0.08)
    x += lp1(np.random.default_rng(seed).standard_normal(n), 1200) * np.exp(-t / 0.012) * 0.3
    # the bendir's snare: a buzz under the skin
    x += 0.12 * bp(np.random.default_rng(seed + 9).standard_normal(n), 3500, 0.7) * np.exp(-t / 0.09)
    return x * np.minimum(1, t / 0.001) * v


def frame_tek(seed, v=1.0):
    n = int(0.25 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = bp(z, 2600, 1.2) * np.exp(-t / 0.02) + 0.8 * hp1(z, 5500) * np.exp(-t / 0.014)
    x += 0.25 * np.sin(2 * np.pi * hz(77) * t) * np.exp(-t / 0.03)       # the rim, on F5: clear of every chord
    x += 0.1 * bp(z, 3500, 0.7) * np.exp(-t / 0.07)
    return x * np.minimum(1, t / 0.0005) * v


def big_drum(m, seed, v=1.0):
    n = int(1.4 * SR); t = np.arange(n) / SR
    f = hz(m) * (1 + 0.4 * np.exp(-t / 0.05))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.45)
    x += 0.35 * np.sin(2 * np.pi * np.cumsum(f * 2.0) / SR) * np.exp(-t / 0.15)      # the octave: audible on a laptop
    x += lp1(np.random.default_rng(seed).standard_normal(n), 900) * np.exp(-t / 0.02) * 0.4
    return np.tanh(1.3 * x) / np.tanh(1.3) * np.minimum(1, t / 0.002) * v


def zils(seed):
    n = int(1.6 * SR); t = np.arange(n) / SR
    f = hz(ZIL_PITCH)
    x = np.zeros(n)
    r = rng('zil', seed)
    for ratio, a, tau in ((1.0, 1.0, 0.9), (1.53, 0.5, 0.5), (2.31, 0.35, 0.3), (3.07, 0.2, 0.18)):
        x += a * np.sin(2 * np.pi * f * ratio * (1 + 0.0007 * r.random()) * t + r.uniform(0, 6.3)) * np.exp(-t / tau)
    x *= 1 + 0.35 * np.sin(2 * np.pi * 5.5 * t)                          # two cymbals beating
    x += 0.2 * hp1(r.standard_normal(n), 6000) * np.exp(-t / 0.01)
    return x * np.minimum(1, t / 0.0008)


def oar(seed):
    """An oar stroke: the blade's dip, the pull through the water."""
    n = int(1.3 * SR); t = np.arange(n) / SR
    z = rng('oar', seed).standard_normal(n)
    dip = hp1(lp1(z, 5000), 1500) * np.exp(-t / 0.05) * np.minimum(1, t / 0.004)
    pull = lp(z, 900, 0.7) * np.sin(np.pi * np.clip(t / 1.1, 0, 1)) ** 2
    return 0.6 * dip + 0.8 * pull


def wave(seed):
    n = int(2 * BAR * SR); u = np.arange(n) / n
    z = rng('wave', seed).standard_normal((n, 2))
    env = np.sin(np.pi * u) ** 2 * np.exp(-2.0 * u)
    y = lp(z, 700, 0.7) * env[:, None] + 0.25 * hp1(lp1(z, 7000), 2500) * (env ** 3)[:, None]
    return y


def wind():
    """Noise made a bar at a time (keyed by loop bar, so it repeats every lap),
    crossfaded, through two band-passes swept by loop-periodic curves."""
    n = tl.n; out = np.zeros((n, 2))
    ov = int(0.25 * SR)
    for b in tl.bars_range():
        lb = b % BARS
        i = tl.smp(b * BAR) - ov
        z = rng('wind', lb).standard_normal((int(BAR * SR) + 2 * ov, 2))
        w = np.ones(len(z)); w[:2 * ov] = np.sin(np.linspace(0, np.pi / 2, 2 * ov))   # equal power:
        w[-2 * ov:] = np.cos(np.linspace(0, np.pi / 2, 2 * ov))                           # the bars are uncorrelated
        j0, j1 = max(i, 0), min(i + len(z), n)
        if j1 > j0:
            out[j0:j1] += z[j0 - i:j1 - i] * w[j0 - i:j1 - i, None]
    tc = (np.arange(0, n, CHUNK) - tl.t0 * SR) / SR
    lv = bar_curve(WIND, tc)
    f1 = 520 * 2.2 ** (0.5 + 0.5 * np.sin(2 * np.pi * 3 * tc / LOOP) * np.sin(2 * np.pi * 7 * tc / LOOP + 1))
    f2 = 2200 * 2.0 ** (0.5 + 0.5 * np.sin(2 * np.pi * 5 * tc / LOOP + 2))
    gust = 0.55 + 0.45 * np.sin(2 * np.pi * 11 * tc / LOOP) ** 2 * (0.5 + 0.5 * np.sin(2 * np.pi * 2 * tc / LOOP))
    y = np.zeros_like(out)
    for ch in range(2):
        a = tv_bp(out[:, ch], f1 * (1 + 0.04 * ch), 1.6)
        b = tv_bp(out[:, ch], f2 * (1 - 0.03 * ch), 2.0)
        y[:, ch] = a + 0.6 * b
    env = np.repeat(lv * gust, CHUNK)[:n]
    return lp1(y * lp1(env, 3)[:, None], 9000)


# ── render ──────────────────────────────────────────────────────────────────
def mixdown():
    lyr, perc_, big, sea = (tl.bus() for _ in range(4))
    strings = []                                  # (t, midi, vel, seed)
    for b in tl.bars_range():
        t = b * BAR; lb = b % BARS
        sec, c = section(lb), CHORDS[lb]
        pcs, ly, ch = CH[c]
        lv = LYRE_LEVEL[sec]

        # lyre: eighths grouped 3+3+2 (sixteenths for the Sirens), a strum on 1 in the storm
        if sec == 'B':
            order = (0, 1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1)
            for s, k in enumerate(order):
                strings.append((t + s * S16, ly[k], lv * (0.75 if s % 4 == 0 else 0.55), (lb, s)))
        else:
            order = (0, 2, 3, 1, 3, 4, 5, 4)
            for s, k in enumerate(order):
                acc = 1.0 if s in (0, 3, 6) else 0.65
                strings.append((t + s * E8, ly[k], lv * acc, (lb, s)))
            if sec == 'C':
                for k, m in enumerate(ly[1:]):
                    strings.append((t + 0.016 * (k + 1), m, lv * 0.55, (lb, 'strum', k)))

        # frame drum: DUM on 1 and 3, teks between; lighter for the Sirens
        if part('frame', lb):
            if sec == 'B':
                hits = {0: ('d', 0.7), 3: ('t', 0.5), 4: ('t', 0.7), 6: ('t', 0.45), 7: ('t', 0.35)}
            else:
                hits = {0: ('d', 1.0), 2: ('t', 0.45), 3: ('t', 0.7), 4: ('d', 0.8), 5: ('t', 0.35),
                        6: ('t', 0.8), 7: ('t', 0.5)}
            for e, (kind, v) in hits.items():
                if kind == 'd':
                    perc_.add(t + e * E8, frame_dum(frame_pitch(c), lb * 8 + e, v), pan=-0.2, gain=0.22)
                else:
                    perc_.add(t + e * E8, frame_tek(lb * 8 + e, v), pan=0.25, gain=0.12)
        if part('big', lb):
            m = 31 if c == 'G' else 36
            for q in (0, 2):
                big.add(t + q * BEAT, big_drum(m, lb * 4 + q, 1.0 if q == 0 else 0.75), pan=0.0, gain=0.17)
        if part('roll', lb):
            for s in range(8, 16):
                big.add(t + s * S16, big_drum(31, 7000 + lb * 16 + s, 0.25 + 0.6 * (s - 8) / 7), gain=0.13)
        if part('zils', lb):
            sea.add(t, zils(lb), pan=0.45, gain=0.08)
            sea.add(t + 2 * BEAT, zils(lb + 100), pan=0.45, gain=0.05)
        if part('oars', lb):
            sea.add(t, oar(lb), pan=-0.35, gain=0.1)
            sea.add(t + 0.03, oar(lb + 50), pan=0.35, gain=0.08)
        if part('waves', lb):
            sea.add(t, wave(lb), gain=0.05)

    # each lyre string rings until it is plucked again or the chord changes
    # and its note is not in the new chord (the hand stops it), at most 3 s
    by_m = {}
    for ev in sorted(strings, key=lambda e: e[0]):
        by_m.setdefault(ev[1], []).append(ev)
    for m, evs in by_m.items():
        for j, (t0, _, v, key) in enumerate(evs):
            ring = min(evs[j + 1][0] - t0, 3.0) if j + 1 < len(evs) else 3.0
            b0 = int(np.floor(t0 / BAR + 1e-6))
            for b in range(b0 + 1, b0 + 3):
                if b * BAR - t0 < ring and m % 12 not in CH[CHORDS[b % BARS]][0]:
                    ring = b * BAR - t0
                    break
            seed = int(rng('lyre', key).integers(1 << 30))
            lyr.add(t0, lyre(m, ring, v, seed), pan=-0.5 + (m - 43) / 30, gain=0.22)

    # the melodies, one voice a passage, every lap
    mel = tl.bus()
    for name, line, bar0 in LINES:
        timbre = VOICE if name == 'siren' else AULOS
        x = sing(line, graces(name, line, bar0), timbre, bar0)
        for lap in (-1, 0, 1):
            t0 = lap * LOOP + bar0 * BAR
            if -tl.pre * BAR - 14 * BAR < t0 < (BARS + tl.post) * BAR:
                mel.add(t0, x, pan=0.1 if name != 'siren' else -0.1, gain=0.07 if name != 'siren' else 0.045)

    lyrx = soundbox(lyr.x)
    choirx = chorus(choir(), LOOP / 16, depth_ms=3.0, base_ms=12.0, mix=0.5, t0=tl.t0) * 0.15
    dr = drone_voices() * 0.055
    dronex = np.stack([dr, dr], 1)
    windx = wind() * 0.075
    melx = mel.x + pingpong(mel.x, 3 * E8, 0.25, 3, 2800) * 0.5
    percx = perc_.x
    hall = make_ir(3.2, dark=7000, seed=29, pre=0.03)
    wet = reverb(hp1(lyrx * 0.3 + melx * 0.35 + choirx * 0.6 + percx * 0.12 + big.x * 0.25
                     + sea.x * 0.3 + dronex * 0.1, 150), hall)
    return dict(lyre=lyrx, melody=melx, choir=choirx, drone=dronex, frame=percx, big=big.x,
                sea=sea.x, wind=windx, reverb=wet * 0.45)


def render(wav=None):
    stems = mixdown()
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        i0 = tl.smp(0)
        print('stem      ' + ''.join(f'{s:>7d}' for s in range(0, BARS, 4)))
        for k, v in stems.items():
            row = [20 * np.log10(np.sqrt(np.mean(v[i0 + int(s * BAR * SR):i0 + int((s + 4) * BAR * SR)] ** 2)) + 1e-9)
                   for s in range(0, BARS, 4)]
            print(f'{k:9s} ' + ''.join(f'{r:7.1f}' for r in row))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
