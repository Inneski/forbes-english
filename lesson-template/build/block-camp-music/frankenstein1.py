#!/usr/bin/env python3
"""Block Camp soundtrack "Ambitions" (Frankenstein Part I: Ambitions - Going To Voxel RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". Part I is Victor's story up
to the spark: a storm over the oak in Geneva, the university, the workshop,
the machines at full power, the night the body moves. So: the idiom of a
1930s-50s laboratory monster film, played for fun - a theremin singing the
tune, scurrying staccato strings, timpani, brass stabs as the power builds,
a Tesla coil zapping on the off-beats, the lab clock ticking, thunder. Spooky
but cheerful: a mad-science romp for 10-16 year olds, never a horror cue.
An original piece in that idiom; nothing is taken from any film.

THE AMBITION MOTIF (bars 4-5), shared with Part II (frankenstein2.py):
    D4 A4 D5 . . E5 | F5 . . E5 D5 A4      up a fifth, up a fourth, reach
A rising, reaching figure: Victor's ambition. Part II sets it falling.

D minor, 128 BPM, 4/4 (a sixteenth is exactly 5625 samples, a bar 1.875 s).
One chord a bar:

  intro  Dm | Dm | Bb | A                         bars 0-3    storm: contrabass drone, the lab clock, thunder,
                                                              the theremin sliding A - Bb - A - C# and down
  A      Dm | Dm | Bb | A | Dm | F | Gm | A7      bars 4-11   the motif on the theremin over 3+3+2 staccato
                                                              strings, the clock still ticking
  A'     Dm | Dm | Bb | A | Dm | F | Bb | F       bars 12-19  the motif again, strings doubling it an octave
                                                              down, a celesta, Tesla zaps on the 'and' of 4
  B      Gm | A | Bb | C | Dm | Eb | A | A7       bars 20-27  full power: the bass climbs G A Bb C D Eb, the
                                                              theremin climbs in tenths over it, sixteenth
                                                              strings, brass stabs and timpani on 3+3+2,
                                                              zaps on 2 and 4, a timpani roll and a swell
  C      D | Bb | D | Bb | Gm | Eb | A | A7       bars 28-35  THE SPARK: an arc, and the motif in D MAJOR on
                                                              brass; the theremin's descant F#-F-F# turns
                                                              the major to the flat sixth and back; celesta
                                                              sparkles; the strings gallop
  turn   Dm | Bb | Gm | A                         bars 36-39  the storm again: the motif's head, thunder,
                                                              crackles, the clock, a timpani roll on A

check_lines() proves the harmony at every render: every theremin, string-
melody and brass note that is a quarter or longer, or falls on beat 1 or 3,
is a tone of its chord and sits no semitone or minor ninth from the bass,
the pad, the brass chord or the ostinato under it; every ostinato, pad,
brass, celesta, bass, timpani, Tesla and clock pitch is a chord tone, and no
voicing holds a semitone. The named dissonances, all an eighth long and off
the beat: the passing E over Dm and Bb (bars 4, 5, 12, 13, 28, 29), the G
over Bb (6, 14), the chromatic G-F descent over A (7, 15: an augmented fifth
for one eighth, the gothic touch), the A over Gm and Bb (10, 31).

Instruments, all synthesised here:
  Theremin    one continuous voice per lap: a sine with a little 2nd and 3rd
              harmonic, pitch gliding between notes (portamento, 55 ms), a
              vibrato that grows in over 0.4 s, volume-hand swells.
  Strings     staccato: two band-limited saws 12 cents apart, a bow scrape,
              a short bite; the pad: three saws, slow attack, delayed
              vibrato, through a chorus; in A' the pad voice doubles the
              theremin an octave down.
  Contrabass  a saw and a sine under a 420 Hz low-pass, bowed.
  Brass       two saws with a pitch scoop and a filter that snaps open.
  Celesta     a sine bar with a quick octave and a glint.
  Tesla coil  a 25% pulse at a chord tone, amplitude-shaken by noise, with
              crackle; the spark is three of them (D A D) and a swell.
  Percussion  timpani on D and A, the lab clock (two wood blocks tuned to
              the chord's root and fifth), thunder.
40 bars = 75 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/frankenstein1.py [--wav preview.wav] [--stems stems.npz]
"""
import sys
import numpy as np
from scipy.signal import lfilter, fftconvolve
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, make_ir, reverb, chorus, finish)

NAME = 'frankenstein-ambitions'
BARS = 40
tl = Timeline(bpm=128, bars=BARS)
BAR, BEAT = tl.bar, tl.beat
E8, S16 = BEAT / 2, BEAT / 4
LOOP = tl.loop
assert abs(S16 * SR - 5625) < 1e-6

# ── the changes ─────────────────────────────────────────────────────────────
#  bass: contrabass; ost: the staccato strings' root, third, fifth, octave;
#  pad: the sustained strings; brass: the stab chord; tes: the Tesla coil's note
CH = {
    'Dm': dict(pcs={2, 5, 9},     bass=38, ost=[50, 53, 57, 62], pad=[57, 62, 65, 69], brass=[62, 65, 69], tes=74),
    'Bb': dict(pcs={10, 2, 5},    bass=34, ost=[46, 50, 53, 58], pad=[58, 62, 65, 70], brass=[58, 62, 65], tes=70),
    'A':  dict(pcs={9, 1, 4},     bass=33, ost=[45, 49, 52, 57], pad=[57, 61, 64, 69], brass=[57, 61, 64], tes=69),
    'A7': dict(pcs={9, 1, 4, 7},  bass=33, ost=[45, 49, 52, 55], pad=[55, 61, 64, 69], brass=[55, 61, 64], tes=69),
    'F':  dict(pcs={5, 9, 0},     bass=41, ost=[41, 45, 48, 53], pad=[57, 60, 65, 69], brass=[57, 60, 65], tes=72),
    'Gm': dict(pcs={7, 10, 2},    bass=43, ost=[43, 46, 50, 55], pad=[55, 58, 62, 67], brass=[55, 58, 62], tes=67),
    'C':  dict(pcs={0, 4, 7},     bass=48, ost=[48, 52, 55, 60], pad=[55, 60, 64, 67], brass=[55, 60, 64], tes=72),
    'Eb': dict(pcs={3, 7, 10},    bass=39, ost=[51, 55, 58, 63], pad=[55, 58, 63, 67], brass=[55, 58, 63], tes=70),
    'D':  dict(pcs={2, 6, 9},     bass=38, ost=[50, 54, 57, 62], pad=[57, 62, 66, 69], brass=[57, 62, 66], tes=74),
}
CHORDS = (['Dm', 'Dm', 'Bb', 'A'] +
          ['Dm', 'Dm', 'Bb', 'A', 'Dm', 'F', 'Gm', 'A7'] +
          ['Dm', 'Dm', 'Bb', 'A', 'Dm', 'F', 'Bb', 'F'] +
          ['Gm', 'A', 'Bb', 'C', 'Dm', 'Eb', 'A', 'A7'] +
          ['D', 'Bb', 'D', 'Bb', 'Gm', 'Eb', 'A', 'A7'] +
          ['Dm', 'Bb', 'Gm', 'A'])
assert len(CHORDS) == BARS
BASS_B = {20: 43, 21: 45, 22: 46, 23: 48, 24: 50, 25: 51, 26: 45, 27: 45}   # the climb


def section(lb):
    return ('intro' if lb < 4 else 'A' if lb < 12 else "A'" if lb < 20 else 'B' if lb < 28
            else 'C' if lb < 36 else 'turn')


def bass_note(lb):
    return BASS_B.get(lb, CH[CHORDS[lb]]['bass'])


# ── the tunes: (midi, eighths) per bar, 0 = rest ─────────────────────────────
MOTIF = [
    [(62, 2), (69, 2), (74, 3), (76, 1)],              # Dm  D A D E      the ambition motif
    [(77, 3), (76, 1), (74, 2), (69, 2)],              # Dm  F E D A
    [(70, 2), (74, 2), (77, 3), (79, 1)],              # Bb  Bb D F G     reaching again
    [(81, 2), (79, 1), (77, 1), (76, 4)],              # A   A G F E      the chromatic slip
    [(74, 2), (77, 2), (81, 2), (86, 2)],              # Dm  D F A D      the climb
    [(84, 4), (81, 2), (77, 2)],                       # F   C A F
]
TH = {1: [(69, 8)], 2: [(70, 8)], 3: [(69, 4), (73, 4)]}                    # intro: A, Bb, A C#, slide down
for k, row in enumerate(MOTIF):
    TH[4 + k] = TH[12 + k] = row
TH[10] = [(82, 3), (81, 1), (79, 2), (74, 2)]                               # Gm  Bb A G D
TH[11] = [(73, 4), (76, 2), (79, 2)]                                        # A7  C# E G
TH[18] = [(82, 2), (86, 2), (82, 2), (77, 2)]                               # Bb  Bb D Bb F
TH[19] = [(77, 4), (72, 2), (69, 2)]                                        # F   F C A, up a step into B
TH.update({20: [(70, 6), (74, 2)], 21: [(73, 6), (76, 2)], 22: [(74, 6), (77, 2)],    # B: tenths over
           23: [(76, 6), (79, 2)], 24: [(77, 6), (81, 2)], 25: [(79, 6), (82, 2)],    # the climbing bass
           26: [(81, 4), (76, 2), (81, 2)], 27: [(79, 2), (81, 2), (85, 4)]})
TH.update({28: [(78, 8)], 29: [(77, 8)], 30: [(78, 4), (81, 4)], 31: [(82, 8)],      # C: the descant
           32: [(86, 8)], 33: [(82, 8)], 34: [(76, 8)], 35: [(79, 8)]})
TH[36] = [(62, 2), (69, 2), (74, 4)]                                        # turn: the motif's head
TH[37] = [(74, 3), (0, 5)]
BRASS = {                                                                   # C: the motif in D major
    28: [(62, 2), (69, 2), (74, 3), (76, 1)],          # D   D A D E
    29: [(77, 3), (76, 1), (74, 2), (70, 2)],          # Bb  F E D Bb
    30: [(74, 2), (78, 2), (81, 4)],                   # D   D F# A
    31: [(82, 3), (81, 1), (77, 4)],                   # Bb  Bb A F
    32: [(79, 2), (82, 2), (86, 4)],                   # Gm  G Bb D
    33: [(87, 4), (82, 2), (79, 2)],                   # Eb  Eb Bb G
    34: [(81, 4), (85, 4)],                            # A   A C#
    35: [(76, 4), (79, 2), (73, 2)],                   # A7  E G C#
}
CELLO = {lb: [(m - 12 if m else 0, d) for m, d in TH[lb]] for lb in range(12, 20)}   # A': strings double
for row in list(TH.values()) + list(BRASS.values()):
    assert sum(d for _, d in row) == 8, row

OST8 = [0, 0, 2, 0, 3, 0, 2, 1]                        # eighths, accents on 0 3 6 (3+3+2)
OST16 = [0, 0, 2, 0, 3, 0, 2, 0, 0, 0, 2, 0, 3, 2, 1, 2]


def tick_hz(pc, lo=1500.0):
    """A wood block tuned to pitch class pc, in 1500-3000 Hz."""
    f = hz(60 + pc)
    while f < lo:
        f *= 2
    return f


def timp_note(c):
    """The timpani are D2 and A2: whichever is in the chord, else silent."""
    pcs = CH[c]['pcs']
    return 38 if 2 in pcs else 45 if 9 in pcs else None


def check_lines():
    """Every melody note a quarter or longer, or on beat 1 or 3, is a chord
    tone and no semitone or minor ninth from anything held under it; every
    accompaniment pitch is a chord tone; no voicing holds a semitone."""
    bad = []
    rub = (1, 13, 25, 37)
    for name, tune in (('theremin', TH), ('brass', BRASS), ('strings', CELLO)):
        for lb, row in tune.items():
            c = CH[CHORDS[lb]]
            under = [bass_note(lb)] + c['pad'] + c['ost'] + (c['brass'] if section(lb) in ('B', 'C') else [])
            pos = 0
            for m, d in row:
                if m and (d >= 2 or pos % 4 == 0):
                    if m % 12 not in c['pcs']:
                        bad.append((name, lb, pos, m, CHORDS[lb], 'not a chord tone'))
                    if any(abs(m - v) in rub for v in under):
                        bad.append((name, lb, pos, m, CHORDS[lb], 'rubs'))
                pos += d
    for lb in range(BARS):
        c = CHORDS[lb]
        if bass_note(lb) % 12 not in CH[c]['pcs']:
            bad.append(('bass', lb))
    for c, v in CH.items():
        for key in ('ost', 'pad', 'brass'):
            if any(m % 12 not in v['pcs'] for m in v[key]):
                bad.append((key, c))
            ms = sorted(v[key])
            if any((hi - lo) in rub for i, lo in enumerate(ms) for hi in ms[i + 1:]):
                bad.append((key, c, 'semitone'))
        if v['tes'] % 12 not in v['pcs']:
            bad.append(('tesla', c))
        t = timp_note(c)
        if t is not None and t % 12 not in v['pcs']:
            bad.append(('timpani', c))
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


def blep_pulse(f, n, duty=0.5, ph0=0.0):
    return 0.5 * (blep_saw(f, n, ph0) - blep_saw(f, n, (ph0 + duty) % 1.0))


def env_lp(x, fc_of_t, q=0.9, chunk=128):
    """Low-pass whose cutoff follows fc_of_t (an array, one value per chunk)."""
    out = np.empty_like(x); zi = np.zeros(2)
    for j, i in enumerate(range(0, len(x), chunk)):
        w = 2 * np.pi * min(fc_of_t[min(j, len(fc_of_t) - 1)], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


# ── instruments ─────────────────────────────────────────────────────────────
def stacc(m, dur, v, seed):
    """A staccato string section note: two saws 12 cents apart, a bite, a scrape."""
    f = hz(m); n = int((dur + 0.07) * SR); t = np.arange(n) / SR
    r = rng('stacc', seed)
    x = 0.5 * blep_saw(f * 2 ** (-6 / 1200), n, r.random()) + 0.5 * blep_saw(f * 2 ** (6 / 1200), n, r.random())
    x = lp(x, 3000 + 4000 * v, 0.7)
    z = r.standard_normal(n)
    x += (0.12 * bp(z, 2600, 1.4) + 0.08 * hp(z, 6500)) * np.exp(-t / 0.01)
    env = np.minimum(1, t / 0.005) * (0.55 + 0.45 * np.exp(-t / 0.045)) * np.clip((dur + 0.06 - t) / 0.06, 0, 1)
    return x * env * v


def pad_note(m, dur, seed, att=0.3, rel=0.3, cut=2300):
    f = hz(m); n = int((dur + rel + 0.05) * SR); t = np.arange(n) / SR
    r = rng('pad', seed)
    vib = 1 + (5 / 1200 * np.log(2)) * np.clip((t - 0.35) / 0.5, 0, 1) * np.sin(2 * np.pi * 5.3 * t + r.uniform(0, 6.3))
    x = sum(blep_saw(f * 2 ** (c / 1200) * vib, n, r.random()) for c in (-8, 0, 7)) / 3
    x = lp(lp1(x, cut * 1.6), cut, 0.7)
    return x * adsr(n, att, 0.25, 0.85, rel, dur)


def contrabass(m, dur, seed, att=0.05):
    f = hz(m); n = int((dur + 0.3) * SR); t = np.arange(n) / SR
    r = rng('cb', seed)
    x = 0.7 * blep_saw(f, n, r.random()) + 0.6 * np.sin(2 * np.pi * f * t)
    x = lp(x, 420, 0.8)
    x += 0.08 * bp(r.standard_normal(n), 900, 1.2) * np.exp(-t / 0.03)
    return x * adsr(n, att, 0.2, 0.85, 0.25, dur)


def brass(m, dur, v, seed):
    """Two saws with a pitch scoop and a filter that snaps open, then settles."""
    n = int((dur + 0.12) * SR); t = np.arange(n) / SR
    r = rng('brass', seed)
    f = hz(m) * 2 ** ((-28 * np.exp(-t / 0.035)) / 1200)
    x = 0.5 * blep_saw(f * 2 ** (-5 / 1200), n, r.random()) + 0.5 * blep_saw(f * 2 ** (5 / 1200), n, r.random())
    tc = t[::128]
    fc = (400 + 4800 * v * (1 - np.exp(-tc / 0.03)) * (0.65 + 0.35 * np.exp(-tc / 0.25))) * np.where(tc > dur, np.exp(-(tc - dur) / 0.05), 1)
    x = env_lp(x, np.maximum(fc, 200), 1.1)
    return x * adsr(n, 0.012, 0.15, 0.8, 0.09, dur) * v


def theremin_line(rows, bar0):
    """One theremin voice through `rows` (bars of (midi, eighths)) starting at
    bar bar0: pitch glides between legato notes, starts clean after a rest;
    vibrato grows over each note; the volume hand swells in and lets go."""
    notes, pos = [], 0
    for row in rows:
        for m, d in row:
            notes.append((pos * E8, d * E8, m)); pos += d
    total = pos * E8
    n = int((total + 1.5) * SR)
    p = np.zeros(n); g = np.zeros(n); vd = np.zeros(n)
    last_p, last_g, prev_rest = None, 0.0, True
    for st, du, m in notes:
        a, b = int(round(st * SR)), int(round((st + du) * SR))
        tt = np.arange(b - a) / SR
        if m:
            tgt = float(m)
            if last_p is None or prev_rest:
                p[a:b] = tgt
                g[a:b] = np.minimum(1, tt / 0.05) * (1 + 0.12 * np.exp(-tt / 0.25))
            else:
                p[a:b] = tgt + (last_p - tgt) * np.exp(-tt / 0.055)
                g[a:b] = (0.82 + 0.18 * np.minimum(1, tt / 0.08)) * (1 + 0.1 * np.exp(-tt / 0.3))
            vd[a:b] = np.clip((tt - 0.12) / 0.4, 0, 1)
            last_p, prev_rest = p[b - 1], False
        else:
            p[a:b] = last_p if last_p is not None else 60
            g[a:b] = last_g * np.exp(-tt / 0.12)
            prev_rest = True
        last_g = g[b - 1]
    b = int(round(total * SR))
    p[b:] = last_p; g[b:] = last_g * np.exp(-np.arange(n - b) / SR / 0.12)
    g = lp1(g, 60)
    t = np.arange(n) / SR
    cents = 22 * vd * np.sin(2 * np.pi * 5.8 * t)
    f = hz(69) * 2 ** ((p - 69) / 12 + cents / 1200)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + 0.22 * np.sin(2 * ph + 0.4) + 0.1 * np.sin(3 * ph + 1.1) + 0.03 * np.sin(4 * ph + 2.0)
    return lp1(x, 7000) * g


def celesta(m, v=1.0):
    f = hz(m); n = int(1.4 * SR); t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.7) + 0.22 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.18)
         + 0.07 * np.sin(2 * np.pi * 3.9 * f * t) * np.exp(-t / 0.05))
    return x * np.minimum(1, t / 0.001) * v


def tesla(m, dur, seed, crackle=1.0):
    """A singing Tesla coil: a hard 25% pulse at the note, shaken by noise,
    and the crackle of the arc."""
    n = int((dur + 0.04) * SR); t = np.arange(n) / SR
    r = rng('tesla', seed)
    f = hz(m)
    x = blep_pulse(f, n, 0.25, r.random()) + 0.35 * blep_pulse(2 * f, n, 0.3, r.random())
    x *= 1 + 0.45 * lp1(r.standard_normal(n), 90) * 3
    x = lp(x, 5200, 0.8)
    k = int(n * 0.6)
    imp = np.zeros(n); imp[r.integers(0, n, k // 40 + 1)] = r.uniform(-1, 1, k // 40 + 1)
    x += crackle * 1.4 * lp(hp(imp, 1800), 7000)
    env = np.minimum(1, t / 0.002) * np.clip((dur + 0.03 - t) / 0.03, 0, 1)
    return x * env


def swell(dur, seed):
    """A reverse-cymbal swell: band noise rising to a cut."""
    n = int(dur * SR); t = np.arange(n) / SR
    z = rng('swell', seed).standard_normal((n, 2))
    x = lp(hp(z, 1800), 6500)
    return x * ((t / dur) ** 2.5)[:, None] * np.clip((dur - t) / 0.01, 0, 1)[:, None]


def timp(m, v, seed, length=2.0):
    f = hz(m); n = int(length * SR); t = np.arange(n) / SR
    bend = np.cumsum(1 + 0.012 * np.exp(-t / 0.08)) / SR
    x = np.zeros(n)
    for r_, a, tau in ((1, 1, 1.0), (1.5, 0.5, 0.65), (1.98, 0.32, 0.45), (2.44, 0.16, 0.3), (2.92, 0.08, 0.22)):
        x += a * np.sin(2 * np.pi * f * r_ * bend) * np.exp(-t / tau)
    x += 0.5 * lp(np.random.default_rng(seed).standard_normal(n), 320) * np.exp(-t / 0.02)
    return x * np.minimum(1, t / 0.002) * np.clip((length - t) / 0.05, 0, 1) * v


def block(freq, seed):
    n = int(0.09 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = (np.sin(2 * np.pi * freq * t) * np.exp(-t / 0.012) + 0.3 * np.sin(2 * np.pi * 2 * freq * t) * np.exp(-t / 0.006)
         + 0.2 * bp(z, freq * 1.3, 3.0) * np.exp(-t / 0.004))
    return x * np.minimum(1, t / 0.0005)


def machine(seed, v=1.0):
    """The lab machinery: a bright metal tick (six square partials, as an
    analogue hat is made, high-passed), short."""
    n = int(0.06 * SR); t = np.arange(n) / SR
    r = rng('machine', seed)
    x = sum(np.sign(np.sin(2 * np.pi * f * t + r.uniform(0, 6.3))) for f in (317, 449, 562, 701, 843, 1129))
    x = hp(hp(x / 6 + 0.6 * r.standard_normal(n), 6500), 6500)
    return lp1(x, 13000) * np.exp(-t / 0.014) * np.minimum(1, t / 0.0004) * v


def snare(seed, v=1.0):
    n = int(0.25 * SR); t = np.arange(n) / SR
    z = rng('snare', seed).standard_normal(n)
    x = (bp(z, 3200, 0.6) + 0.35 * hp(z, 7000)) * np.exp(-t / 0.07)
    x += 0.6 * np.sin(2 * np.pi * (190 + 60 * np.exp(-t / 0.01)) * t) * np.exp(-t / 0.03)
    return x * np.minimum(1, t / 0.0006) * v


def crash(seed):
    n = int(2.4 * SR); t = np.arange(n) / SR
    z = rng('crash', seed).standard_normal((n, 2))
    x = lp1(hp(z, 3000), 11000) * np.exp(-t / 0.7)[:, None] + 0.4 * hp(z, 8000) * np.exp(-t / 0.25)[:, None]
    return x * np.minimum(1, t / 0.0015)[:, None]


_t = np.arange(int(0.004 * SR)) / SR
SPARK = np.random.default_rng(5).standard_normal(len(_t)) * np.exp(-_t / 0.0008)   # one spark: 1 ms of noise
DROP = np.random.default_rng(6).standard_normal(len(_t)) * np.exp(-_t / 0.0005)


def air_grain(key, kind):
    """Two bars of texture under a sine window; laid a bar apart, the power
    sums flat. 'rain': a hiss with a patter of drops; 'arc': the electric
    crackle of the lab, sparse sparks high-passed, with a faint fizz."""
    n = int(2 * BAR * SR)
    r = rng(kind, key)
    z = r.standard_normal((n, 2))
    if kind == 'rain':
        y = hp(lp(lp1(z, 7000), 4500, 0.7), 500) + 0.25 * lp(hp(z, 6000), 11000)
        k = int(90 * 2 * BAR) * 2
        imp = np.zeros((n, 2))
        np.add.at(imp, (r.integers(0, n, k), r.integers(0, 2, k)), np.minimum(r.exponential(1.0, k), 3.0) * r.choice((-1.0, 1.0), k))
        y += 3.0 * lp(hp(fftconvolve(imp, DROP[:, None])[:n], 1500, 0.8), 6000, 0.8)
    else:
        k = int(70 * 2 * BAR) * 2
        imp = np.zeros((n, 2))
        np.add.at(imp, (r.integers(0, n, k), r.integers(0, 2, k)),
                  np.minimum(r.pareto(2.5, k), 4.0) * r.choice((-1.0, 1.0), k))
        y = 1.2 * lp(hp(fftconvolve(imp, SPARK[:, None])[:n], 3500, 0.8), 12000, 0.7) + 0.05 * lp(hp(z, 7000), 12000)
    return y * np.sin(np.pi * (np.arange(n) + 0.5) / n)[:, None]


def thunder(key, dur=6.0):
    """rainfall.py's thunder: low noise in slow bumps, with 200-600 Hz rumble
    so a laptop can play it."""
    n = int(dur * SR); t = np.arange(n) / SR
    r = rng('thunder', key)
    env = np.zeros(n)
    for c, w, a in ((0.15, 0.25, 0.8), (0.7, 0.6, 1.0), (1.6, 0.9, 0.6), (2.8, 1.2, 0.35)):
        c += r.uniform(-0.1, 0.1)
        env += a * np.exp(-0.5 * ((t - c) / w) ** 2)
    env *= np.clip(t / 0.05, 0, 1) * np.clip((dur - t) / 1.2, 0, 1)
    out = np.zeros((n, 2))
    for ch in range(2):
        z = r.standard_normal(n)
        y = lp(lp(z, 150, 0.8), 190) + 0.45 * lp(bp(z, 300, 0.7), 700)
        out[:, ch] = hp(y, 38) * env
    return out


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    th, stc, pad, low, brs, cel, tes, arc, perc_, kit, storm = (tl.bus() for _ in range(11))
    for b in tl.bars_range():
        t = b * BAR
        lb = b % BARS
        sec, c = section(lb), CHORDS[lb]
        v = CH[c]

        # contrabass: a drone in the intro and turn, a bowed note a bar elsewhere
        if sec in ('intro', 'turn'):
            if lb in (0, 36):
                low.add(t, contrabass(v['bass'], 2 * BAR - 0.1, lb, att=0.4), gain=0.22)
            elif lb in (2, 3, 38, 39):
                low.add(t, contrabass(v['bass'], BAR - 0.08, lb, att=0.15), gain=0.22)
        else:
            low.add(t, contrabass(bass_note(lb), BAR - 0.06, lb), gain=0.24 if sec != 'A' else 0.2)

        # staccato strings: 3+3+2 eighths; sixteenths in B; fading in and out
        if sec in ('A', "A'", 'C') or lb in (2, 3, 36, 37):
            g = {'A': 0.15, "A'": 0.16, 'C': 0.15}[sec] if sec in ('A', "A'", 'C') else \
                {2: 0.06, 3: 0.1, 36: 0.12, 37: 0.07}[lb]
            for k, ix in enumerate(OST8):
                acc = 1.0 if k in (0, 3, 6) else 0.7
                stc.add(t + k * E8, stacc(v['ost'][ix], E8 * 0.5, acc, lb * 16 + k), pan=-0.25 + 0.08 * ix, gain=g)
        elif sec == 'B':
            for k, ix in enumerate(OST16):
                acc = 1.0 if k in (0, 6, 12) else 0.65
                stc.add(t + k * S16, stacc(v['ost'][ix], S16 * 0.6, acc, lb * 16 + k), pan=-0.25 + 0.08 * ix,
                        gain=0.14 + 0.012 * (lb - 20))

        # string pad
        if sec != 'intro' or lb >= 2:
            g = {'intro': 0.035, 'A': 0.038, "A'": 0.045, 'B': 0.05, 'C': 0.06, 'turn': 0.04}[sec]
            if sec == 'turn' and lb >= 38:
                g = 0.03
            for k, m in enumerate(v['pad']):
                pad.add(t, pad_note(m, BAR - 0.05, lb * 8 + k, att=0.35 if sec in ('intro', 'turn') else 0.2,
                                    rel=0.25, cut=2000 if sec in ('A', 'intro', 'turn') else 2700),
                        pan=(-0.6, -0.2, 0.2, 0.6)[k], gain=g)

        # A': the strings double the theremin an octave down
        if lb in CELLO:
            pos = 0
            for m, d in CELLO[lb]:
                if m:
                    pad.add(t + pos * E8, pad_note(m, d * E8 - 0.02, lb * 64 + pos, att=0.04, rel=0.12, cut=2600),
                            pan=-0.15, gain=0.1)
                pos += d

        # brass: stabs on 3+3+2 in B, the motif and a held chord in C
        if sec == 'B':
            hits = (0, 3, 6) if lb != 27 else (0, 3)
            for k in hits:
                for j, m in enumerate(v['brass']):
                    brs.add(t + k * E8, brass(m, E8 * 0.7, 0.9 if k == 0 else 0.75, lb * 32 + k * 4 + j),
                            pan=0.15 + 0.12 * j, gain=0.075 + 0.004 * (lb - 20))
        if lb in BRASS:
            pos = 0
            for m, d in BRASS[lb]:
                if m:
                    brs.add(t + pos * E8, brass(m, d * E8 * 0.92, 1.0 if pos % 4 == 0 else 0.85, lb * 64 + pos),
                            pan=0.1, gain=0.14)
                pos += d
            for j, m in enumerate(v['brass']):
                brs.add(t, brass(m - 12, BAR * 0.9, 0.55, lb * 64 + 40 + j), pan=-0.2 + 0.15 * j, gain=0.05)

        # celesta: a few chimes in A', running sixteenths in C
        if sec == "A'":
            tones = sorted(set(p % 12 for p in v['pad']))
            for k, e8 in enumerate((2, 5, 7)):
                pc = tones[(lb + k) % len(tones)]
                m = 84 + pc if 84 + pc <= 93 else 72 + pc
                cel.add(t + e8 * E8, celesta(m, 0.8), pan=0.45, gain=0.06)
        elif sec == 'C':
            up = sorted({p + 12 * o for p in v['brass'] for o in (1, 2)})[:6]
            seq = up + up[-2:0:-1]
            for k in range(16):
                cel.add(t + k * S16, celesta(seq[k % len(seq)], 0.85 if k % 4 == 0 else 0.6),
                        pan=0.5 - 0.1 * (k % 4), gain=0.045)

        # the Tesla coil
        if sec == "A'" and lb % 2 == 1:
            tes.add(t + 7 * E8, tesla(v['tes'], E8 * 0.8, lb * 8), pan=0.55, gain=0.07)
        elif sec == 'B':
            for k in (2, 6):
                tes.add(t + k * E8, tesla(v['tes'], E8 * 0.7, lb * 8 + k), pan=(-0.55, 0.55)[k // 4], gain=0.075)
        elif sec == 'C' and lb in (29, 31, 33):
            tes.add(t + 7 * E8, tesla(v['tes'], E8 * 0.8, lb * 8), pan=-0.5, gain=0.07)
        elif sec == 'turn' and lb in (36, 37, 38):
            tes.add(t + (3 if lb != 37 else 5) * E8, tesla(v['tes'], E8 * 0.5, lb * 8, crackle=1.6), pan=0.4,
                    gain=0.018)
        if lb == 27:                                     # the swell into the spark
            kit.add(t + 2 * BEAT, swell(2 * BEAT, lb), gain=0.06)
        if lb == 28:                                     # THE SPARK
            for j, m in enumerate((62, 69, 74)):
                tes.add(t, tesla(m, BEAT * 1.6, 900 + j, crackle=1.3), pan=(-0.5, 0.0, 0.5)[j], gain=0.045)

        # timpani
        tn = timp_note(c)
        if tn is not None:
            if lb == 0:
                perc_.add(t, timp(tn, 0.9, 700), pan=-0.1, gain=0.2)
            elif sec == 'A' and lb in (4, 8):
                perc_.add(t, timp(tn, 0.8, lb), pan=-0.1, gain=0.18)
            elif sec == "A'":
                perc_.add(t, timp(tn, 0.75, lb), pan=-0.1, gain=0.16)
            elif sec == 'B' and lb != 27:
                for k in (0, 3, 6):
                    perc_.add(t + k * E8, timp(tn, 0.9 if k == 0 else 0.7, lb * 8 + k, length=1.2), pan=-0.1,
                              gain=0.15)
            elif sec == 'C':
                perc_.add(t, timp(tn, 1.0, lb), pan=-0.1, gain=0.18)
                if lb in (28, 30):
                    perc_.add(t + 2 * BEAT, timp(tn, 0.8, lb + 50), pan=-0.1, gain=0.15)
        if lb in (27, 39):                               # rolls on A
            steps = 16 if lb == 27 else 24
            for k in range(steps):
                tt = (k / steps) * BAR if lb == 39 else 2 * BEAT + (k / steps) * 2 * BEAT
                vv = 0.12 + 0.55 * (k / steps) ** 1.5
                perc_.add(t + tt, timp(45, vv, 800 + lb * 30 + k, length=0.7), pan=-0.1, gain=0.15)

        # the lab clock: tick (root) on 1 and 3, tock (fifth) on 2 and 4
        if sec in ('intro', 'A', 'turn'):
            pcs = sorted(v['pcs'])
            root, fifth = v['bass'] % 12, (v['bass'] + 7) % 12
            assert fifth in v['pcs']
            for q in range(4):
                perc_.add(t + q * BEAT, block(tick_hz(root if q % 2 == 0 else fifth), lb * 4 + q),
                          pan=0.45, gain=0.04 if sec == 'A' else 0.05)

        # the machinery (sixteenths, accents on 3+3+2), a snare in B and C,
        # crashes at the top of A and at the spark
        if sec in ('A', "A'", 'B', 'C'):
            steps = {'A': (2, 6, 10, 14), "A'": tuple(range(16)), 'B': tuple(range(16)), 'C': (0, 2, 4, 6, 8, 10, 12, 14)}[sec]
            g = {'A': 0.1, "A'": 0.08, 'B': 0.1, 'C': 0.1}[sec]
            for k in steps:
                acc = 1.0 if k in (0, 6, 12) else 0.75 if k % 2 == 0 else 0.5
                kit.add(t + k * S16, machine(lb * 16 + k, acc), pan=0.3 if k % 2 else 0.2, gain=g)
        if sec in ('B', 'C') and lb != 27:
            for q in (1, 3):
                kit.add(t + q * BEAT, snare(lb * 4 + q), pan=0.05, gain=0.07 if sec == 'B' else 0.06)
        if lb == 27:
            for k in range(8, 16):
                kit.add(t + k * S16, snare(lb * 16 + k, 0.35 + 0.65 * (k - 8) / 7), pan=0.05, gain=0.055)
        if lb in (4, 28):
            kit.add(t, crash(lb), gain=0.07 if lb == 4 else 0.1)

        # the air: rain in the storm, the arc's crackle while the machines run
        rl = {0: 1.0, 1: 1.0, 2: 0.8, 3: 0.5, 36: 0.6, 37: 1.0, 38: 1.0, 39: 1.0}.get(lb, 0)
        if rl:
            storm.add(t, air_grain(lb, 'rain'), gain=0.03 * rl)
        al = {"A'": 0.6, 'B': 0.8, 'C': 1.0}.get(sec, 0)
        if al:
            arc.add(t, air_grain(lb, 'arc'), gain=0.032 * al)

        # thunder
        if lb in (1, 36):
            storm.add(t + 0.2 * BAR, thunder(lb), gain=0.5)

    # the theremin: one continuous voice a lap
    rows = [TH.get(lb, [(0, 8)]) for lb in range(BARS)]
    line = theremin_line(rows, 0)
    for lap in (-1, 0, 1):
        th.add(lap * LOOP, line, pan=0.05, gain=0.11)

    padx = chorus(pad.x, LOOP / 16, depth_ms=2.5, base_ms=8.0, mix=0.45, t0=tl.t0)
    stcx = stc.x + 0.5 * bp(stc.x, 1100, 1.0) + 0.9 * hp(stc.x, 5000)
    brsx = brs.x + 0.5 * hp(brs.x, 4500)
    hall = make_ir(2.3, dark=4800, seed=31, pre=0.022)
    stems = dict(theremin=th.x, strings=stcx, pad=padx, bass=low.x, brass=brsx, celesta=cel.x,
                 tesla=tes.x, arc=arc.x, percussion=perc_.x, kit=kit.x, storm=storm.x)
    sends = dict(theremin=0.45, strings=0.25, pad=0.4, bass=0.08, brass=0.3, celesta=0.5, tesla=0.3, arc=0.2,
                 percussion=0.3, kit=0.2, storm=0.3)
    wet = reverb(sum(stems[k] * sends[k] for k in stems), hall) * 0.5
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
