#!/usr/bin/env python3
"""Block Camp soundtrack "Conveyor" (Passive Present Continuous).

Style brief, 2026-09-30: Steve Reich / minimalist mallet music - about
128-136 BPM, interlocking marimba and vibraphone-like FM mallet patterns,
short repeating cells that shift against each other by a sixteenth over the
loop, phasing-style, a soft sustained pad underneath, a gentle pulse, no
conventional drum kit. Bright major key. Mesmerising, calm energy. The cell
and the changes are new; nothing is copied from Piano Phase or Music for 18
Musicians.

D major, 128 BPM (a sixteenth is exactly 5625 samples), 4/4. Six chords,
six bars each:
    D6/9 | Gmaj9 | Bm11 | Em9 | G6/9 | A11        -> D
The mallet cell is twelve sixteenths long on the D major pentatonic (D E F#
A B), so it sits inside every chord and runs across the 4/4 bar lines
(three beats against four).

The phase process: marimba 1 plays the cell unchanged; marimba 2 plays the
same cell, a sixteenth later every three bars. Twelve shifts x 3 bars = 36
bars, so the two meet in unison again exactly at the loop point - the phase
cycle IS the loop.

Instruments: two additive marimbas (fundamental, the first overtone tuned
to the double octave as a real bar is, a little ~10x, a mallet tick),
panned apart and very slightly different so the unison sounds like one
wide instrument; a bass marimba (softer mallet) pulsing in eighths on the
root and fifth; an FM vibraphone (ratio 1:1, decaying index, the 4x
partial, motor tremolo) in dotted quarters, two dyads a chord; "voices" -
formant-filtered saws re-struck in eighths, each chord one breath-long
swell, voiced so each carries its chord's third (VOX); the resultant - a
soft glockenspiel an octave up that plays only the eighth-note strokes
where the two marimbas coincide, so the figure it draws changes with every
shift; a soft triangle pad with chorus; a hall. The bass notes are choked
at the next eighth: left to ring, strokes 0.234 s apart piled up in phase
on G2 (23 cycles) and the level swung by 8 dB from chord to chord.

Review, 2026-09-30: the first overtone was at 3.9x, 44 cents flat of the
double octave, a sour attack; now 3.99x. The Bm11 bass was B1 (62 Hz,
below a five-octave marimba's C2): that section carried 20 dB more energy
under 80 Hz than the rest, a sub bump on headphones and no bass on a
phone; now B2. The mix measured dull (magnitude-centroid median 835 Hz
against 1480-1700 for the shipped tracks, -39 dB above 6 kHz), and the
resultant glock and the voices sat 13-16 dB under the marimbas, all but
inaudible: harder mallets, a brighter vibraphone strike and pad, the glock
+4.7 dB, the voices +3.3 dB. The Em9 and G6/9 thirds were only in the
quiet pad (chroma G 0.04 over Em9): the voices now carry them.

Arrangement (by six-bar chord):
    0      D6/9   marimbas and pad alone (the unison, then shift 1)
    1      Gmaj9  bass pulse and vibraphone join
    2-4           voices swell in, one breath per chord; the resultant glock
    5      A11    vibraphone, voices and glock drop, back toward the unison
The level stays level (a process piece, not a build); the texture moves.
Checked in code: each chord's voicing holds every cell note but one, and
that one is a colour tone - the 13th over Gmaj9 and A11, the 11th over
Em9, the major 7th over G6/9. No b9, no tritone over the bass, and no
semitone between any part (cell, glock, vibraphone, voices) and the pad.
36 bars = 67.5 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/conveyor.py [--wav preview.wav]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, lp, bp, tri, adsr, make_ir, reverb, chorus,
                      finish)

BARS = 36
tl = Timeline(bpm=128, bars=BARS)
BAR, S16 = tl.bar, tl.s16

#          bass  pad voicing
CHORDS = [(38, [50, 57, 64, 66, 71]),     # D6/9   D  A  E  F# B
          (43, [55, 59, 62, 66, 69]),     # Gmaj9  G  B  D  F# A
          (47, [54, 59, 62, 64, 69]),     # Bm11   F# B  D  E  A  (bass B2, not B1: see above)
          (40, [52, 55, 62, 66, 71]),     # Em9    E  G  D  F# B
          (43, [55, 59, 64, 69, 74]),     # G6/9   G  B  E  A  D
          (45, [55, 59, 62, 64, 69])]     # A11    G  B  D  E  A


def chord_at(b):
    return CHORDS[(b % BARS) // 6]


# the voices' three notes per chord: each holds the chord's third, which the
# cell, vibraphone and (quiet) pad otherwise leave out of Em9 and G6/9. The
# Em9 third sits at G3, not G4, which would rub a semitone on the pad's F#4.
# D E A -> G D F# -> B E A: every voice moves by a step, a third or a fourth.
VOX = {2: [62, 64, 69],                   # Bm11:  3rd, 11th, 7th
       3: [55, 62, 66],                   # Em9:   3rd, 7th, 9th
       4: [59, 64, 69]}                   # G6/9:  3rd, 6th, 9th


# the cell: (sixteenth within the 12, midi); four of the twelve are rests
CELL = [(0, 78), (2, 69), (3, 74), (5, 76), (6, 69), (8, 71), (10, 74), (11, 81)]
CELL_AT = dict(CELL)


def shift_at(b):
    return (b % BARS) // 3                    # 0..11 sixteenths


def part(name, b):
    b %= BARS; sec = b // 6
    return {
        'mar1':   True,
        'mar2':   True,
        'pad':    True,
        'bass':   sec >= 1,
        'vibes':  1 <= sec <= 4,
        'voices': 2 <= sec <= 4,
        'glock':  2 <= sec <= 4,
    }[name]


# ── a band-limited saw for the voices ──────────────────────────────────────
def bsaw(f, n, ph0=0.0):
    dt = np.broadcast_to(np.asarray(f, float), (n,)) / SR
    p = (ph0 + np.cumsum(dt)) % 1.0
    y = 2 * p - 1
    lo = p < dt; t = p[lo] / dt[lo]; y[lo] -= t + t - t * t - 1
    hi = p > 1 - dt; t = (p[hi] - 1) / dt[hi]; y[hi] -= t * t + t + t + 1
    return y


# ── instruments ─────────────────────────────────────────────────────────────
def marimba(m, vel=1.0, var=0.0, choke=None, bright=1.0):
    """A struck bar: the fundamental rings, the first overtone (tuned to the
    double octave, as a marimba bar is undercut to be) and the ~10x glint
    die fast, a mallet tick. `var` detunes and re-weights the partials
    slightly so the second marimba is a different instrument. `choke`
    (seconds) damps the bar there, as the next stroke would. `bright`
    scales the overtones and tick (the bass marimba uses a softer mallet)."""
    f = hz(m) * 2 ** (var * 3 / 1200)
    tau = 0.5 * (440 / f) ** 0.6
    n = int((min(2.5, 5 * tau) if choke is None else choke + 0.03) * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / tau)
    p2 = 3.99 + 0.02 * var
    if f * p2 < 9000:
        x += bright * (0.62 - 0.08 * var) * np.sin(2 * np.pi * f * p2 * t + 0.4) * np.exp(-t / (tau * 0.3))
    if f * 9.9 < 9000:
        x += bright * 0.14 * np.sin(2 * np.pi * f * 9.9 * t + 1.1) * np.exp(-t / (tau * 0.07))
    tick = lp1(np.random.default_rng(31).standard_normal(n), 6000) * np.exp(-t / 0.0018) * 0.24 * bright
    x = (x + tick) * np.minimum(1, t / 0.0008) * vel
    if choke is not None:
        x *= np.clip(1 - (t - choke) / 0.03, 0, 1)
    return x


def vibe(m, dur):
    """FM vibraphone: carrier:modulator 1:1 with the index falling (bright
    strike, mellow ring), the 4x bar partial, a motor tremolo, the damper
    lifting after `dur`."""
    f = hz(m)
    n = int((dur + 0.5) * SR); t = np.arange(n) / SR
    idx = 0.15 + 1.35 * np.exp(-t / 0.15)
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
    x += 0.35 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.3)
    trem = 1 - 0.28 * 0.5 * (1 - np.cos(2 * np.pi * 5.3 * t))
    env = np.exp(-t / 2.2) * np.minimum(1, t / 0.001) * np.clip(1 - (t - dur) / 0.35, 0, 1)
    return x * trem * env


def glock(m):
    """A soft glockenspiel: nearly a sine, the bar's 2.76x partial faint."""
    f = hz(m)
    n = int(1.6 * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.55) + 0.12 * np.sin(2 * np.pi * 2.76 * f * t) * np.exp(-t / 0.08)
    return x * np.minimum(1, t / 0.0006)


def voice(m, seed):
    """One sung eighth: a saw through 'ah' formants, soft onset."""
    n = int(0.42 * SR); t = np.arange(n) / SR
    r = rng('vox', seed)
    f = hz(m) * (1 + 0.004 * np.sin(2 * np.pi * 4.8 * t + r.random() * 6.28))
    x = bsaw(f, n, r.random())
    y = bp(x, 750, 3.0) + 0.6 * bp(x, 1150, 3.5) + 0.25 * bp(x, 2600, 4.0) + 0.3 * lp(x, 500)
    return y * adsr(n, 0.035, 0.12, 0.6, 0.15, 0.22)


def pad_chord(voicing, dur):
    n = int((dur + 1.8) * SR)
    x = np.zeros(n)
    for m in voicing:
        r = rng('pad', m)
        x += sum(tri(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-6, 5)) / 2
    x = lp(x, 2000, 0.6)
    return x * adsr(n, 1.4, 0.5, 0.85, 1.6, dur) / len(voicing)


def render(wav=None):
    mar1, mar2, bass, vib, vox, pad, glk = (tl.bus() for _ in range(7))
    for b in tl.bars_range():
        t = b * BAR
        bm = b % BARS; sec, i = bm // 6, bm % 6
        root, voicing = chord_at(b)
        k = shift_at(b)
        # ── the two marimbas: one steady, one k sixteenths behind
        for s in range(16):
            g = bm * 16 + s                     # sixteenth within the loop; 576 = 48 cells
            accent = 1.0 if s % 4 == 0 else 0.85
            if g % 12 in CELL_AT and part('mar1', b):
                mar1.add(t + s * S16, marimba(CELL_AT[g % 12], accent), pan=-0.45, gain=0.12)
            if (g - k) % 12 in CELL_AT and part('mar2', b):
                mar2.add(t + s * S16, marimba(CELL_AT[(g - k) % 12], accent, var=1.0), pan=0.45, gain=0.12)
            # the resultant: where the two marimbas strike together, a glockenspiel
            # an octave above marimba 1 picks the note out, so the figure it draws
            # changes with every shift
            if part('glock', b) and g % 12 in CELL_AT and (g - k) % 12 in CELL_AT and s % 2 == 0:
                glk.add(t + s * S16, glock(CELL_AT[g % 12] + 12), pan=0.1, gain=0.06)
        # ── bass marimba: eighths, root on the beats, fifth on the & of 2 and 4
        if part('bass', b):
            for s in range(0, 16, 2):
                m = root + 7 if s in (6, 14) else root
                bass.add(t + s * S16, marimba(m, 1.0 if s % 4 == 0 else 0.6, choke=2 * S16, bright=0.7), gain=0.09)
        # ── vibraphone: dotted quarters (three against the bar), two dyads a chord
        if part('vibes', b):
            dyads = [voicing[3:5], voicing[2:4]]
            for s in range(16):
                g = bm * 16 + s
                if g % 6 == 0:
                    d = dyads[(g // 6) % 2]
                    for kk, m in enumerate(d):
                        vib.add(t + s * S16 + kk * 0.006, vibe(m, 5 * S16), pan=(-0.2, 0.25)[kk], gain=0.065)
        # ── voices: eighth pulses, one breath-long swell per chord
        if part('voices', b):
            for s in range(0, 16, 2):
                u = (i * 16 + s) / 96                     # position in the six-bar breath
                sw = np.sin(np.pi * u) ** 2
                for kk, m in enumerate(VOX.get(sec, voicing[2:])):
                    vox.add(t + s * S16, voice(m, (bm, s, kk)), pan=(-0.5, 0.0, 0.5)[kk], gain=0.19 * sw)
        # ── pad, one chord per six bars
        if part('pad', b) and i == 0:
            pad.add(t, pad_chord(voicing, 6 * BAR - 0.3), gain=0.30)

    padx = chorus(pad.x, tl.loop / 12, depth_ms=2.5, base_ms=9.0, mix=0.5, t0=tl.t0)
    voxx = chorus(vox.x, tl.loop / 18, depth_ms=1.5, base_ms=6.0, mix=0.4, t0=tl.t0)
    glkx = glk.x + np.roll(glk.x, int(3 * S16 * SR), axis=0)[:, ::-1] * 0.3   # one dotted-eighth echo, swapped sides
    dry = mar1.x + mar2.x + bass.x + vib.x + voxx + padx + glkx
    wet = reverb(mar1.x * 0.3 + mar2.x * 0.3 + vib.x * 0.45 + voxx * 0.5 + padx * 0.3 + bass.x * 0.1 + glkx * 0.6,
                 make_ir(2.4, dark=4200))
    return finish(tl, dry + wet * 0.35, 'passive-present-continuous', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
