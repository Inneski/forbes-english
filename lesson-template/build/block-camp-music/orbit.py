#!/usr/bin/env python3
"""Block Camp soundtrack "Orbit" (Passive Future Simple): space ambient.

The brief, 2026-09-30: the Passive Future Simple station as space ambient
in the manner of Eno's Apollo and Music for Airports - no drums, slow
evolving pads with long attacks and releases, a few sparse piano-like and
bell notes at irregular-feeling positions, a warm low drone, gentle
shimmering high partials, a very long reverb; calm, spacious, wonder.
An original piece; nothing copied.

D major with one lydian moment, over a D drone. The grid is 64 BPM (a
sixteenth is exactly 11250 samples) and is used only to place events. Five
chords, four bars each, all over the drone:
    Dmaj9 | Gmaj9/D | E/D (the lydian II) | Em9/D (G# falls back to G) | A9sus4/D
A first draft had the E/D for a quarter of the loop and little G natural
to answer it; it measured as A major (D lydian and A major share their
notes). So the lydian colour is now one chord, its G# only in the pad
(the piano and bell voices avoid it), and three chords carry G natural.
The notes are placed the Music-for-Airports way: each piano or bell voice
repeats one pitch on its own cycle - a third, a quarter, a fifth, a seventh
or a half of the loop - so the voices drift against each other and the
coincidences never seem to repeat, yet all of them come round together
once a loop. Positions are rounded to the sixteenth grid. A voice whose
pitch is not in the chord under it moves to the nearest note that is (A
over E/D becomes B), so nothing clashes. The voice that comes round most
often (a seventh of the loop) is F#, the major third, so the key reads as
D major rather than A major or B minor.

No two notes that sound together are a semitone or a minor ninth apart;
the script asserts it. That rule, added in review, did three things:
  - The shimmer no longer has G5 over the breath pad's F#5 (Gmaj9/D, Em9/D:
    eleven seconds of a 44 Hz rub, twice a lap) or D6 over the strings'
    C#5 (Dmaj9). It is now A5 C#6 F#6 | B5 D6 F#6 | B5 D6 E6 | D6 B5 F#6 |
    G5 A5 D6.
  - A pad note whose semitone neighbour arrives in the next chord (F#3 to
    G3, G3 to G#3 and back, F#4 to G4...) lets go in about a second instead
    of 6.5 s, so the crossfades no longer rub at equal level for 2-3 s.
  - A piano or bell note still ringing when the next chord comes in must
    suit that chord too: A4 at 24.8 s becomes B4 (G# is coming), D5 at
    69.6 s becomes E5 (C#5 is coming), F#4 at 57.0 s becomes E4 (G4).
Instruments: a drone (D2, A2, D3 as near-sines with a quieter copy a hair
sharp on the left and flat on the right, so it turns slowly without ever
cancelling in mono; frequencies rounded to whole cycles per loop so it is
seamless), a string pad (band-limited saws, a filter that opens with
the swell), a breath pad an octave up, a soft FM piano, a glass FM bell
(both fade out at the end of their buffers rather than being cut off),
shimmer (beating pairs of high sines on chord tones, with a quieter pair
an octave up for the high partials), and a 9-second reverb that most of
it is sent into.

Arrangement (bar mod 20):
    0-3    Dmaj9: drone, string pad, piano; faint shimmer
    4-7    Gmaj9/D: + breath pad, shimmer up, the high piano voice joins
    8-11   E/D: + bells, everything
    12-15  Em9/D: everything
    16-19  A9sus4/D: the breath pad and most bells drop out, back to the top

20 bars = 75 s, a seamless loop (see synthkit.py). Measured: D major
(Krumhansl 0.81; B minor, the relative, next at 0.77), centroid ~1000 Hz,
RMS by 4-bar block -17.8 -16.4 -16.2 -15.5 -18.5 dB.

    py lesson-template/build/block-camp-music/orbit.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, adsr, make_ir, reverb, chorus, finish)

NAME = 'passive-future-simple'
BARS = 20
tl = Timeline(bpm=64, bars=BARS, pre=12)
BAR, BEAT, S16 = tl.bar, tl.beat, tl.s16
LOOP = tl.loop

#          name       string/breath pad voicing      shimmer           allowed for piano and bells
CHORDS = [('Dmaj9',   [54, 57, 62, 64, 73],   [81, 85, 90],    {2, 4, 6, 9, 1}),        # D E F# A C#
          ('Gmaj9/D', [55, 59, 62, 66, 69],   [83, 86, 90],    {2, 4, 6, 7, 9, 11}),    # D F# G A B (+E)
          ('E/D',     [56, 59, 64, 66, 71],   [83, 86, 88],    {2, 4, 6, 11}),          # D E F# (G#) B
          ('Em9/D',   [55, 59, 62, 64, 66],   [86, 83, 90],    {2, 4, 6, 7, 11}),       # D E F# G B
          ('A9sus4/D', [57, 62, 64, 67, 71],  [79, 81, 86],    {2, 4, 7, 9, 11})]       # D E G A B
DRONE = (38, 45, 50)
CLASH = (1, 13)      # a semitone, or a minor ninth: never between two notes that sound together
RING = 7.0           # a piano or bell note this close to the next chord must suit that chord too
FAST_TAU = 0.8       # the release of a pad note whose semitone neighbour arrives in the next chord
SHIM_HI = 0.22       # the shimmer's octave-up pair, relative to the main pair


def chord_at(b):
    return CHORDS[(b % BARS) // 4]


def section(b):
    return (b % BARS) // 4


def sounding(s):
    """Every sustained pitch in section s: string pad, breath pad (sections
    1-3, an octave above the top three string notes), shimmer and drone."""
    _, voicing, sh, _ = CHORDS[s % 5]
    br = [m + 12 for m in voicing[2:]] if s % 5 in (1, 2, 3) else []
    return list(voicing) + br + list(sh) + list(DRONE)


def fast_release(m, s):
    """A pad note lets go quickly when the next chord brings a note a
    semitone (or a minor ninth) away, so the crossfade never rubs."""
    return any(abs(n - m) in CLASH for n in sounding(s + 1))


# the loops: (repeats per lap, offset in seconds, midi, sections it sounds in)
PIANO = [(3, 1.4, 64, {0, 1, 2, 3, 4}),     # E4
         (4, 6.1, 69, {0, 1, 2, 3, 4}),     # A4
         (5, 9.7, 74, {1, 2, 3, 4}),        # D5
         (7, 3.3, 66, {0, 1, 2, 3}),        # F#4
         (2, 21.6, 59, {0, 1, 2, 3, 4})]    # B3
BELLS = [(3, 12.8, 81, {1, 2, 3, 4}),       # A5
         (4, 4.6, 78, {2, 3}),              # F#5
         (5, 17.3, 86, {2, 3})]             # D6


def fit(m, allowed, avoid=()):
    """The nearest pitch to m whose pitch class is allowed and which is not a
    semitone or a minor ninth from anything in avoid (down on a tie)."""
    for d in (0, -1, 1, -2, 2, -3, 3, -4, 4):
        c = m + d
        if c % 12 in allowed and all(abs(c - n) not in CLASH for n in avoid):
            return c
    raise ValueError(m)


def events(voices, label):
    """Every note of every loop voice from a lap before to a lap after, each
    time rounded to the sixteenth grid (the loop is a whole number of
    sixteenths, so the rounding repeats too)."""
    out, log = [], []
    for v, (k, off, m, secs) in enumerate(voices):
        per = LOOP / k
        for lap in (-1, 0, 1):
            for j in range(k):
                q = round((off + j * per) / S16) * S16
                t = lap * LOOP + q
                b = int(q // BAR)
                if section(b) not in secs:
                    continue
                name, _, _, allowed = chord_at(b)
                s = section(b)
                avoid = sounding(s)
                if (s + 1) * 4 * BAR - q < RING:      # still ringing when the next chord comes in
                    avoid = avoid + sounding(s + 1)
                mm = fit(m, allowed, avoid)
                if lap == 0:
                    log.append((q, label, v, m, mm, name))
                if -tl.pre * BAR - 12 < t < (BARS + tl.post) * BAR:
                    out.append((t, mm, v))
    return out, log


# ── instruments ─────────────────────────────────────────────────────────────
def _blep(p, dt):
    y = np.zeros_like(p)
    a = p < dt; t = p[a] / dt[a]; y[a] = 2 * t - t * t - 1
    b = p > 1 - dt; t = (p[b] - 1) / dt[b]; y[b] = t * t + 2 * t + 1
    return y


def blsaw(f, n, ph=0.0):
    dt = np.full(n, f / SR)
    p = (ph + np.cumsum(dt)) % 1.0
    return 2 * p - 1 - _blep(p, dt)


def var_lp(x, fc, q=0.7, chunk=512):
    """A low-pass that follows the cutoff curve fc (one value per sample)."""
    n = len(x); out = np.empty(n); zi = np.zeros(2)
    for i in range(0, n, chunk):
        w = 2 * np.pi * min(fc[min(i + chunk // 2, n - 1)], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


def pad_env(n, a, d, s, r, gate, fast):
    """adsr, or, for a note whose neighbour is coming, an exponential release
    (tau FAST_TAU) that is out of the way within a second or so."""
    if not fast:
        return adsr(n, a, d, s, r, gate)
    t = np.arange(n) / SR
    return adsr(n, a, d, s, 1e9, gate) * np.exp(-np.maximum(t - gate, 0) / FAST_TAU)


def fade_tail(x, start):
    """A raised-cosine fade from start (s) to the end of the buffer, so a
    note's tail dies away instead of being chopped."""
    i = int(start * SR); k = len(x) - i
    x[i:] *= 0.5 + 0.5 * np.cos(np.pi * np.arange(k) / k)
    return x


def string_pad(m, dur, seed, fast=False):
    n = int((dur + 7.0) * SR)
    r = rng('str', seed, m)
    x = sum(blsaw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-7, 0, 7)) / 3
    env = pad_env(n, 4.0, 2.0, 0.85, 6.5, dur, fast)
    return var_lp(x, 450 + 2300 * env ** 1.5) * env


def breath_pad(m, dur, seed, fast=False):
    n = int((dur + 8.0) * SR); t = np.arange(n) / SR
    r = rng('breath', seed, m)
    f = hz(m) * (1 + 0.0018 * np.sin(2 * np.pi * 0.21 * t + r.random() * 6))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + 0.3 * np.sin(2 * ph) + 0.12 * np.sin(3 * ph) + 0.04 * np.sin(4 * ph)
    return x * pad_env(n, 5.5, 2.0, 0.85, 7.5, dur, fast)


def shimmer(m, dur, seed, fast=False):
    """A pair of sines 0.2-0.5 Hz apart (a slow beat) with a slower flicker,
    and a quieter pair an octave up beating at a different rate: the high
    partials the brief asks for (1.6-3 kHz), soft enough not to whistle."""
    n = int((dur + 7.0) * SR); t = np.arange(n) / SR
    r = rng('shim', seed, m)
    f = hz(m); d = 0.2 + 0.3 * r.random()
    x = np.sin(2 * np.pi * f * t + r.random() * 6) + np.sin(2 * np.pi * (f + d) * t + r.random() * 6)
    x *= 0.75 + 0.25 * np.sin(2 * np.pi * (0.11 + 0.1 * r.random()) * t + r.random() * 6)
    d2 = 0.3 + 0.4 * r.random()
    x += SHIM_HI * (np.sin(2 * np.pi * 2 * f * t + r.random() * 6) + np.sin(2 * np.pi * (2 * f + d2) * t + r.random() * 6))
    return x * pad_env(n, 5.0, 2.0, 0.8, 6.5, dur, fast)



def piano(m, vel=1.0):
    n = int(10.0 * SR); t = np.arange(n) / SR
    f = hz(m)
    idx = 0.1 + 0.8 * np.exp(-t / 0.5)
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
    x += 0.22 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 1.1)
    x += 0.04 * np.sin(2 * np.pi * 3.003 * f * t) * np.exp(-t / 0.25)
    env = np.minimum(1, t / 0.006) * (0.6 * np.exp(-t / 0.9) + 0.4 * np.exp(-t / 3.6))
    return fade_tail(lp1(x * env, 3200), 6.5) * vel


def bell(m):
    n = int(11.0 * SR); t = np.arange(n) / SR
    f = hz(m)
    idx = 1.3 * np.exp(-t / 1.2)
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * 3.5 * f * t))
    env = np.minimum(1, t / 0.004) * np.exp(-t / 2.6)
    return fade_tail(lp1(x * env, 4500), 7.5)


def drone():
    """D2, A2 and D3 as near-sines, each partial rounded to a whole number of
    cycles per loop so the seam is invisible. Each channel adds a quieter
    copy three cycles per loop sharp (left) or flat (right): the image turns
    slowly, and a mono speaker hears a gentle swell every 25 s, never a
    null. The whole drone breathes on a half-loop cycle."""
    t = np.arange(tl.n) / SR - tl.t0
    out = np.zeros((tl.n, 2))
    for m, g in ((38, 0.6), (45, 0.45), (50, 0.5)):
        cyc = round(hz(m) * LOOP)
        for ch, side in ((0, 3), (1, -3)):
            for c, w in ((cyc, 1.0), (cyc + side, 0.3)):
                ph = 2 * np.pi * c / LOOP * t
                out[:, ch] += g * w * (np.sin(ph) + 0.18 * np.sin(2 * ph) + 0.06 * np.sin(3 * ph))
    breathe = 0.8 + 0.2 * np.sin(2 * np.pi * t / (LOOP / 2))
    return lp1(out, 700) * breathe[:, None] / 1.3


def render(wav=None, stems=False):
    pnotes, plog = events(PIANO, 'piano')
    bnotes, blog = events(BELLS, 'bell')
    # no semitone or minor ninth inside any chord (pads, shimmer, drone) ...
    for s in range(5):
        ns = sounding(s)
        bad = [(a, c) for a in ns for c in ns if a < c and c - a in CLASH]
        assert not bad, (CHORDS[s][0], bad)
    # ... nor between a piano or bell note and the chord under it
    for q, label, v, m, mm, name in sorted(plog + blog):
        s = section(int(q // BAR))
        near = sounding(s) + (sounding(s + 1) if (s + 1) * 4 * BAR - q < RING else [])
        if stems:
            print(f'  {q:6.2f}s bar {q / BAR:5.2f} {label}{v} {m}->{mm} over {name}')
        assert mm % 12 in chord_at(int(q // BAR))[3]
        assert all(abs(mm - n) not in CLASH for n in near), (q, label, mm)

    strings, breath, shim, pno, bells = (tl.bus() for _ in range(5))
    for b in tl.bars_range():
        if b % 4:
            continue
        t = b * BAR
        name, voicing, sh, _ = chord_at(b)
        sec = section(b)
        dur = 4 * BAR
        for k, m in enumerate(voicing):
            strings.add(t, string_pad(m, dur, k, fast_release(m, sec)), pan=(-0.7, -0.35, 0.0, 0.35, 0.7)[k],
                        gain=0.085)
        if sec in (1, 2, 3):
            for k, m in enumerate(voicing[2:]):
                breath.add(t + 0.5 * k * BAR, breath_pad(m + 12, dur - 0.5 * k * BAR, k, fast_release(m + 12, sec)),
                           pan=(-0.5, 0.5, 0.0)[k], gain=0.035)
        for k, m in enumerate(sh):
            shim.add(t + k * BAR, shimmer(m, dur - k * BAR, k, fast_release(m, sec)), pan=(-0.6, 0.6, 0.0)[k],
                     gain=0.016 if sec == 0 else 0.03)
    for t, m, v in pnotes:
        pno.add(t, piano(m, 0.9 + 0.1 * (v % 2)), pan=(-0.4, 0.3, 0.1, -0.2, 0.45)[v], gain=0.13)
    for t, m, v in bnotes:
        bells.add(t, bell(m), pan=(0.55, -0.55, 0.2)[v], gain=0.075)

    dr = drone()
    stringx = chorus(strings.x, LOOP / 5, depth_ms=3.0, base_ms=9.0, mix=0.5, t0=tl.t0)
    wet = reverb(stringx * 0.45 + breath.x * 0.6 + shim.x * 0.8 + pno.x * 0.6 + bells.x * 0.9 + dr * 0.08,
                 make_ir(9.0, dark=4200, seed=17, pre=0.03))
    mix = dr * 0.065 + stringx + breath.x + shim.x + pno.x + bells.x + wet * 0.6
    if stems:
        a = tl.smp(0)
        for nm, x in (('drone', dr * 0.065), ('string', stringx), ('breath', breath.x), ('shim', shim.x),
                      ('piano', pno.x), ('bells', bells.x), ('wet', wet * 0.6)):
            row = []
            for q in range(0, BARS, 4):
                seg = x[a + int(q * BAR * SR):a + int((q + 4) * BAR * SR)]
                row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9))
            print(f'  {nm:6s}' + ''.join(f'{v:7.1f}' for v in row))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None, '--stems' in sys.argv)
