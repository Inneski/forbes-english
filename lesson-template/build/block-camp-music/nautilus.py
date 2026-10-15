#!/usr/bin/env python3
"""Block Camp soundtrack "Nautilus" (Nautilus: The Black Archive, both pages).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game: Captain Nemo's
Nautilus follows an impossible signal down through a crystal trench and a
drowned turquoise city to the Black Archive, with something vast waking in
the dark. So: a modern deep-sea thriller score in the voxel camp's synth
palette - sonar, a throbbing engine, an ondes-like lead that glides like a
signal through water, glass crystals, a choir-dark pad, a hymn for the
thing in the deep and its call. An original piece in that idiom; no melody
or progression is taken from any film or game.

C# minor, 90 BPM, 4/4 (a beat is exactly 32000 samples, a bar 2.667 s).
One chord a bar; the engine throbs on a C# pedal except in B, where the
bass walks the roots:

  intro  C#m | C#m | C#m | C#m                    bars 0-3    sonar alone, the engine starts,
                                                              the signal beeping, bubbles
  A      C#m C#m | A A | F#m F#m | G#m G#m         bars 4-11   the theme on the ondes lead,
                                                              hull drum heartbeat
  A'     (the same)                               bars 12-19  the theme an octave up over a saw
                                                              cello, glass crystals in sixteenths,
                                                              ticks, the clank on 3
  B      E | B | C#m | A | F#m | G#m | A | B       bars 20-27  something vast: synth brass hymn,
                                                              the bass walks, full drums, booms
  turn   C#m | A | F#m | G#m                      bars 28-31  the creature's call, signal again;
                                                              G#m falls back into the intro's C#m

The hook (A, eighths): C#4. G#4---- | E4 D#4 E4 G#4- B4 G#4 | A4----- G#4 F#4 | E4- A4- C#5---
- a rising fifth that falls back through the minor third, the "signal".

The C# is the one pitch that sits a tone or more from every chord here
(no C or D in the key), so the pedal, the sonar ping (C#6), the signal
beeps (C#7), the hull drum and the clank are all tuned to it and can never
rub. check_lines() proves the rest at import: every lead, brass and call
note a quarter or longer, or on beat 1 or 3, is a chord tone; every voicing
(pad, glass) is chord tones with no semitone, major seventh or minor ninth
inside it or against the pedal or bass; every bass note is a chord tone.

Instruments, all synthesised here:
  Ondes lead   a sine-rich voice (2nd, 3rd, 4th harmonics soft) whose pitch
               glides from note to note (one continuous voice a phrase),
               vibrato after a moment, a slow chorus: the signal's voice.
  Saw cello    two detuned band-limited saws through a body and a low-pass,
               doubling the theme an octave down in A'.
  Brass        a five-saw stack whose low-pass swells open on each note:
               the B hymn, with the octave below.
  Pad          four detuned saws a voice, an "oo" formant, slow attack; common
               tones held across the change, a quick release where the next
               chord brings a semitone neighbour.
  Glass        FM (carrier f, modulator 2f, index decaying): odd harmonics,
               a hollow crystal; sixteenth arpeggios that rest on the last
               beat before a change so their echo does not smear it.
  Engine       band-limited saw + square, a low-pass that snaps shut, a
               3-3-2 throb in sixteenths; C#2 pedal, roots in B.
  Sub          one continuous sine on the bass note (loop-exact phase).
  Sonar        a C#6 ping every two bars, its return off the sea floor
               a beat and a half later, darker; a long space around it.
  Signal       C#7 beeps in a broken Morse rhythm (intro and turn).
  Percussion   hull drum (C#2, pitch falling), a metal clank (resonances
               on C#6 and C#7), ticks (high noise, 16ths), a deep boom in B.
  Creature     a low formant voice gliding between chord tones, in the turn.
  Bubbles      rising chirps from the C# minor pentatonic, intro and turn.
32 bars = 85.33 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/nautilus.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

NAME = 'nautilus'
BARS = 32
tl = Timeline(bpm=90, bars=BARS)
BAR, BEAT = tl.bar, tl.beat
E8, S16 = BEAT / 2, BEAT / 4
LOOP = tl.loop
assert round(BEAT * SR) == 32000

KEY = {1, 3, 4, 6, 8, 9, 11}                      # C# minor: C# D# E F# G# A B
PEDAL = 37                                        # C#2
PING, BEEP = 85, 97                               # C#6, C#7

# ── the changes ─────────────────────────────────────────────────────────────
CH = {
    'C#m': dict(pcs={1, 4, 8}, root=37, pad=[56, 61, 64, 68], glass=[73, 76, 80, 85]),
    'A':   dict(pcs={9, 1, 4}, root=33, pad=[57, 61, 64, 69], glass=[73, 76, 81, 85]),
    'F#m': dict(pcs={6, 9, 1}, root=42, pad=[57, 61, 66, 69], glass=[73, 78, 81, 85]),
    'G#m': dict(pcs={8, 11, 3}, root=44, pad=[56, 59, 63, 68], glass=[71, 75, 80, 83]),
    'E':   dict(pcs={4, 8, 11}, root=40, pad=[56, 59, 64, 68], glass=[71, 76, 80, 83]),
    'B':   dict(pcs={11, 3, 6}, root=35, pad=[54, 59, 63, 66], glass=[71, 75, 78, 83]),
}
A_PROG = ['C#m', 'C#m', 'A', 'A', 'F#m', 'F#m', 'G#m', 'G#m']
PROG = ['C#m'] * 4 + A_PROG + A_PROG + ['E', 'B', 'C#m', 'A', 'F#m', 'G#m', 'A', 'B'] + ['C#m', 'A', 'F#m', 'G#m']
assert len(PROG) == BARS


def section(lb):
    lb %= BARS
    return 'intro' if lb < 4 else 'A' if lb < 12 else "A'" if lb < 20 else 'B' if lb < 28 else 'turn'


def bass_of(lb):
    """The engine's note: the C# pedal, or the root in B (in a sensible octave)."""
    c = PROG[lb % BARS]
    return CH[c]['root'] if section(lb) == 'B' else PEDAL


# ── the lines: (midi, eighths) per bar, 0 = rest ────────────────────────────
THEME = [
    [(61, 3), (68, 5)],                                          # C#m  C# G#
    [(64, 2), (63, 1), (64, 1), (68, 2), (71, 1), (68, 1)],      # C#m  E D# E G# B G#
    [(69, 6), (68, 1), (66, 1)],                                 # A    A (G# F#)
    [(64, 2), (69, 2), (73, 4)],                                 # A    E A C#
    [(73, 3), (71, 1), (69, 2), (66, 2)],                        # F#m  C# B A F#
    [(69, 2), (68, 1), (66, 1), (61, 4)],                        # F#m  A G# F# C#
    [(63, 3), (66, 1), (68, 4)],                                 # G#m  D# F# G#
    [(71, 3), (68, 1), (63, 4)],                                 # G#m  B G# D#
]
LEAD = {}
for k, row in enumerate(THEME):
    LEAD[4 + k] = row                                            # A: as written
    LEAD[12 + k] = [(m + 12 if m else 0, d) for m, d in row]     # A': an octave up
CELLO = {12 + k: row for k, row in enumerate(THEME)}             # A': the saw cello, as written
BRASS = {                                                        # B: the hymn
    20: [(64, 4), (68, 4)],                                      # E    E G#
    21: [(66, 4), (63, 2), (59, 2)],                             # B    F# D# B
    22: [(68, 6), (64, 2)],                                      # C#m  G# E
    23: [(69, 4), (73, 4)],                                      # A    A C#
    24: [(73, 4), (69, 2), (66, 2)],                             # F#m  C# A F#
    25: [(71, 4), (75, 4)],                                      # G#m  B D#
    26: [(76, 4), (73, 2), (69, 2)],                             # A    E C# A
    27: [(75, 6), (71, 2)],                                      # B    D# B
}
CALL = {                                                         # turn: the creature, gliding
    28: [(49, 4), (52, 4)],                                      # C#m  C#3 E3
    29: [(57, 3), (52, 5)],                                      # A    A3 E3
    30: [(54, 4), (57, 4)],                                      # F#m  F#3 A3
    31: [(56, 5), (51, 3)],                                      # G#m  G#3 D#3
}
for row in list(LEAD.values()) + list(BRASS.values()) + list(CALL.values()):
    assert sum(d for _, d in row) == 8, row


def notes_of(table, lb):
    """[(eighth, midi, eighths)] for bar lb of a line table."""
    out, pos = [], 0
    for m, d in table.get(lb, []):
        if m:
            out.append((pos, m, d))
        pos += d
    return out


def check_lines():
    """Long or strong line notes are chord tones; voicings carry no semitone,
    major 7th or minor 9th, inside or against the pedal or bass; every pitched
    hit is a C#, a tone or more from every chord in the piece."""
    bad = []
    for name, table in (('lead', LEAD), ('cello', CELLO), ('brass', BRASS), ('call', CALL)):
        for lb in table:
            c = PROG[lb]
            for pos, m, d in notes_of(table, lb):
                if m % 12 not in KEY:
                    bad.append((name, lb, pos, m, 'not in C# minor'))
                if (d >= 2 or pos % 4 == 0) and m % 12 not in CH[c]['pcs']:
                    bad.append((name, lb, pos, m, c))
                if d >= 2 and any(abs(m - o) in (1, 11, 13) for o in CH[c]['pad'] + CH[c]['glass'] + [bass_of(lb)]):
                    bad.append((name, lb, pos, m, c, 'rubs the voicing'))
    for c, v in CH.items():
        if v['root'] % 12 not in v['pcs']:
            bad.append(('bass', c))
        for key in ('pad', 'glass'):
            ms = sorted(v[key] + [v['root'], PEDAL])
            if any(m % 12 not in v['pcs'] for m in v[key]):
                bad.append((key, c, 'not a chord tone'))
            if any((hi - lo) in (1, 11, 13) or ((hi - lo) % 12 in (1, 11) and hi - lo > 13)
                   for i, lo in enumerate(ms) for hi in ms[i + 1:]):
                bad.append((key, c, 'semitone'))
        for p in (PEDAL, PING, BEEP):
            if any((p - q) % 12 in (1, 11) for q in v['pcs']):
                bad.append(('C# rubs', c))
    for p in (PEDAL, PING, BEEP):
        assert p % 12 in KEY
    print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad)
    assert not bad, 'a wrong note (listed above)'


check_lines()


# ── oscillators ─────────────────────────────────────────────────────────────
def blep(ph, dt):
    y = np.zeros_like(ph)
    a = ph < dt; u = ph[a] / dt[a]; y[a] = 2 * u - u * u - 1
    z = ph > 1 - dt; u = (ph[z] - 1) / dt[z]; y[z] = u * u + 2 * u + 1
    return y


def blsaw(f, n, ph0=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,)); dt = f / SR
    ph = (ph0 + np.cumsum(dt)) % 1.0
    return 2 * ph - 1 - blep(ph, dt)


def blsquare(f, n, ph0=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,)); dt = f / SR
    ph = (ph0 + np.cumsum(dt)) % 1.0
    return np.where(ph < 0.5, 1.0, -1.0) + blep(ph, dt) - blep((ph + 0.5) % 1.0, dt)


def phrase(notes, total, glide=0.05, attack=0.035, release=0.12, legato_dip=0.88):
    """One continuous voice: notes [(t0, dur, midi)] in seconds from the phrase
    start. Returns (midi per sample, gain per sample, seconds since the note
    began); the pitch glides between notes, the gain re-articulates a little
    on a joined note and releases exponentially into a rest."""
    from scipy.signal import lfilter
    n = int((total + release * 6 + 0.3) * SR)
    mid = np.full(n, np.nan); g = np.zeros(n); since = np.zeros(n)
    for j, (t0, d, m) in enumerate(notes):
        a, b = int(round(t0 * SR)), int(round((t0 + d) * SR))
        joined = j > 0 and abs(notes[j - 1][0] + notes[j - 1][1] - t0) < 1e-6
        mid[a:b] = m
        tt = np.arange(b - a) / SR
        g[a:b] = np.minimum(1, tt / attack) if not joined else legato_dip + (1 - legato_dip) * np.minimum(1, tt / 0.08)
        since[a:] = np.arange(n - a) / SR
    idx = np.where(np.isnan(mid), 0, np.arange(n)); np.maximum.accumulate(idx, out=idx)
    mid = mid[idx]; mid[np.isnan(mid)] = notes[0][2]          # the pitch carries through rests
    a1 = np.exp(-1 / (glide * SR))
    mid = lfilter([1 - a1], [1, -a1], mid - mid[0]) + mid[0]
    a2 = np.exp(-1 / (release / 4 * SR))
    rel = lfilter([1 - a2], [1, -a2], g)                       # follows the gate, slow to fall
    return mid, lp1(np.maximum(g, rel), 120), since


def ondes(mid, g, since, key):
    n = len(mid); t = np.arange(n) / SR
    r = rng('ondes', key)
    vib = np.clip((since - 0.25) / 0.45, 0, 1) * np.sin(2 * np.pi * 5.1 * t + r.uniform(0, 6))
    f = hz(mid + 0.16 * vib)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + 0.32 * np.sin(2 * ph) + 0.16 * np.sin(3 * ph) + 0.07 * np.sin(4 * ph) + 0.03 * np.sin(5 * ph)
    return x * g


def creature(mid, g, since, key):
    """A low voice: two saws through two vowel formants."""
    n = len(mid); t = np.arange(n) / SR
    r = rng('creature', key)
    f = hz(mid + 0.1 * np.sin(2 * np.pi * 3.1 * t + r.uniform(0, 6)))
    x = blsaw(f, n, r.random()) * 0.7 + blsaw(f * 1.004, n, r.random()) * 0.5
    x = 0.8 * bp(x, 420, 2.5) + 0.6 * bp(x, 900, 3.0) + 0.25 * lp(x, 300)
    return x * g


def tail(n, sec=0.03):
    """A raised-cosine fade over the last `sec` of a hit, so nothing is cut off mid-wave."""
    k = min(n, int(sec * SR)); w = np.ones(n)
    w[n - k:] = 0.5 + 0.5 * np.cos(np.linspace(0, np.pi, k))
    return w


# ── instruments ─────────────────────────────────────────────────────────────
def saw_cello(m, dur, key):
    n = int((dur + 0.3) * SR); t = np.arange(n) / SR; r = rng('cello', key)
    f = hz(m) * (1 + 0.002 * np.clip((t - 0.3) / 0.5, 0, 1) * np.sin(2 * np.pi * 5.4 * t + r.uniform(0, 6)))
    x = blsaw(f * 2 ** (-6 / 1200), n, r.random()) + blsaw(f * 2 ** (6 / 1200), n, r.random())
    x = lp(x, 2200, 0.8) + 0.5 * bp(x, 280, 2.0) + 0.3 * bp(x, 1300, 2.5)
    return x * adsr(n, 0.09, 0.3, 0.85, 0.08 if dur < 0.4 else 0.2, dur)   # a passing note lets go at once


def brass(m, dur, key):
    n = int((dur + 0.35) * SR); t = np.arange(n) / SR; r = rng('brass', key)
    x = sum(blsaw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-9, -4, 0, 4, 9)) / 5
    fc = 1100 + 4000 * np.clip(t / 0.35, 0, 1) ** 1.5 * np.exp(-np.maximum(t - 0.35, 0) / 1.4)
    out = np.empty(n); zi = np.zeros(2); ch = 240
    from scipy.signal import lfilter
    for i in range(0, n, ch):
        w = 2 * np.pi * min(fc[i], SR * 0.45) / SR; al = np.sin(w) / (2 * 0.9); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + ch], zi = lfilter(b / a[0], a / a[0], x[i:i + ch], zi=zi)
    return out * adsr(n, 0.12, 0.4, 0.8, 0.3, dur)


def pad_note(m, dur, rel, key):
    n = int((dur + rel + 0.05) * SR); r = rng('pad', key)
    x = sum(blsaw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-11, -4, 3, 10)) / 4
    x = lp(x, 1300, 0.6) + 0.6 * bp(x, 330, 1.8) + 0.3 * bp(x, 820, 2.5)
    return x * adsr(n, 1.1, 0.6, 0.85, rel, dur)


def glass(m, v, ring=1.4):
    f = hz(m); n = int(ring * SR); t = np.arange(n) / SR
    idx = 1.6 * np.exp(-t / 0.18) + 0.25
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * 2 * f * t))
    x += 0.14 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.08) + 0.06 * np.sin(2 * np.pi * 8 * f * t) * np.exp(-t / 0.03)
    return x * perc(n, 0.0015, 0.42) * np.clip((ring - t) / 0.08, 0, 1) * v


def engine(m, dur, v):
    n = int((dur + 0.08) * SR); t = np.arange(n) / SR; f = hz(m)
    x = 0.65 * blsaw(f, n) + 0.45 * blsquare(f * 0.5 if m > 40 else f, n, 0.25)
    from synthkit import swept_lp
    y = swept_lp(x, 380 + 1500 * v, 180, q=1.4)
    return y * adsr(n, 0.004, 0.09, 0.55, 0.06, dur) * v


def ping(m):
    f = hz(m); n = int(3.0 * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.55) + 0.16 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.18)
    x += 0.05 * np.sin(6 * np.pi * f * t) * np.exp(-t / 0.06)
    click = bp(np.random.default_rng(5).standard_normal(n), 2400, 1.5) * np.exp(-t / 0.004) * 0.12
    return (x + click) * np.minimum(1, t / 0.003) * tail(n)


def beep(m, dur):
    f = hz(m); n = int((dur + 0.01) * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.22 * np.sin(6 * np.pi * f * t)
    return x * np.clip(t / 0.003, 0, 1) * np.clip((dur - t) / 0.004, 0, 1)


def hull_drum(m, v, seed, tau=0.32):
    f0 = hz(m); n = int(max(0.9, 5 * tau) * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.6 * np.exp(-t / 0.025))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t / tau) + 0.25 * np.sin(2 * ph) * np.exp(-t / (tau * 0.4))   # an octave: still C#
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.35 * lp(z, 700) * np.exp(-t / 0.015)
    return x * np.minimum(1, t / 0.0015) * v * tail(n)


def clank(seed):
    n = int(0.4 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = bp(z, hz(PING), 18.0) * 3.0 + bp(z, hz(BEEP), 14.0) * 2.0 + hp(z, 5000) * 0.25 * np.exp(-t / 0.01)
    return x * np.exp(-t / 0.07) * np.minimum(1, t / 0.0008) * tail(n)


def tick(seed, acc):
    n = int(0.06 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = hp(z, 4200) * 0.8 + 1.0 * bp(z, 5600, 1.4) + 0.7 * bp(z, 7200, 2.0) + 0.1 * bp(z, 10500, 2.0)
    return x * np.exp(-t / (0.006 + 0.008 * acc)) * acc * tail(n)


def swell(dur, seed):
    """Filtered noise rising into a section: the water rushing past the hull."""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    out = np.zeros((n, 2))
    for ch in range(2):
        z = np.random.default_rng(seed + ch).standard_normal(n)
        y = hp(z, 2500) * 0.6 + bp(z, 6000, 1.2)
        out[:, ch] = y * u ** 2.2 * np.clip((1 - u) / 0.02, 0, 1)
    return out


def bubble(m, seed):
    n = int(0.09 * SR); t = np.arange(n) / SR
    f = hz(m) * 2 ** (np.minimum(t / 0.05, 1) * 7 / 12)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR)
    return x * np.sin(np.pi * np.minimum(t / 0.07, 1)) ** 2


def loop_phase(f):
    """Phase (cycles) nudged by a hair so it advances a whole number of cycles a lap."""
    ph = np.cumsum(f / SR); i0, N = tl.smp(0), int(round(LOOP * SR))
    d = ph[i0 + N] - ph[i0]
    ph -= (d - np.round(d)) / N * np.arange(len(ph))
    return ph % 1.0


LEVEL = {'intro': 0.6, 'A': 0.8, "A'": 0.95, 'B': 1.0, 'turn': 0.75}


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    lead, cello, brs, pad, gls, eng, sonar, sig, drm, fx = (tl.bus() for _ in range(10))

    def laps(bar0, nbars):
        for lap in (-1, 0, 1):
            t0 = lap * LOOP + bar0 * BAR
            if t0 + (nbars + 1) * BAR > -tl.pre * BAR and t0 < (BARS + tl.post) * BAR + 4:
                yield t0

    # the gliding voices: one phrase per section
    for table, bar0, nbars, voice, gain, pan in ((LEAD, 4, 8, ondes, 0.085, 0.08), (LEAD, 12, 8, ondes, 0.072, 0.08),
                                                (CALL, 28, 4, creature, 0.16, -0.2)):
        notes = []
        for lb in range(bar0, bar0 + nbars):
            for pos, m, d in notes_of(table, lb):
                notes.append(((lb - bar0) * BAR + pos * E8, d * E8, m))
        glide = 0.05 if voice is ondes else 0.16
        mid, g, since = phrase(notes, nbars * BAR, glide=glide, attack=0.04 if voice is ondes else 0.25,
                               release=0.35 if voice is ondes else 0.8)
        sig_ = voice(mid, g, since, bar0)
        for t0 in laps(bar0, nbars):
            (lead if voice is ondes else fx).add(t0, sig_, pan=pan, gain=gain)

    # the sub: one continuous sine following the engine's note (loop-exact)
    n = tl.n; tt = np.arange(n) / SR - tl.t0
    bidx = np.floor(tt / BAR).astype(int)
    sub_m = np.array([bass_of(b) for b in range(-tl.pre, BARS + tl.post + 4)])[np.clip(bidx + tl.pre, 0, None)]
    sub_m = np.where(sub_m < 36, sub_m + 12, sub_m)
    from scipy.signal import lfilter
    a1 = np.exp(-1 / (0.03 * SR)); sub_m = lfilter([1 - a1], [1, -a1], sub_m - sub_m[0]) + sub_m[0]
    sub_ph = loop_phase(hz(sub_m))
    sub_lv = np.array([{'intro': 0.5, 'A': 0.8, "A'": 0.85, 'B': 1.0, 'turn': 0.7}[section(b % BARS)]
                       for b in range(-tl.pre, BARS + tl.post + 4)])[np.clip(bidx + tl.pre, 0, None)]
    sub = np.sin(2 * np.pi * sub_ph) * lp1(sub_lv, 1.0)

    for b in tl.bars_range():
        t = b * BAR; lb = b % BARS; sec = section(lb); c = PROG[lb]; v = CH[c]
        nxt = PROG[(lb + 1) % BARS]; lv = LEVEL[sec]

        # engine throb: 3-3-2 in sixteenths, the accent on the one
        bm = bass_of(lb)
        if not (sec == 'intro' and lb < 1):
            for k, (s, oct_, acc) in enumerate(((0, 0, 1.0), (3, 0, 0.7), (6, 0, 0.8), (8, 12, 0.75),
                                                (11, 0, 0.7), (14, 0, 0.8))):
                vel = acc * (0.7 if sec == 'intro' else 1.0)
                eng.add(t + s * S16, engine(bm + oct_, S16 * 2.2, vel), gain=0.11 * lv)

        # pad: per voice below (needs the next chord)
        # glass arpeggio in A' and B; rests on the last beat before a change
        if sec in ("A'", 'B'):
            pat = [0, 1, 2, 3, 2, 1, 2, 3]
            last = 12 if nxt != c else 16
            for s in range(last):
                m = v['glass'][pat[s % 8]]
                gls.add(t + s * S16, glass(m, 1.0 if s % 4 == 0 else 0.7), pan=0.35 if s % 2 else -0.15,
                        gain=0.05 if sec == "A'" else 0.06)

        # saw cello (A') and brass (B)
        for pos, m, d in notes_of(CELLO, lb):
            cello.add(t + pos * E8, saw_cello(m, d * E8 - 0.02, (lb, pos)), pan=-0.25, gain=0.06)
        for pos, m, d in notes_of(BRASS, lb):
            brs.add(t + pos * E8, brass(m, d * E8 - 0.03, (lb, pos)), pan=0.12, gain=0.16)
            brs.add(t + pos * E8, brass(m - 12, d * E8 - 0.03, (lb, pos, 'lo')), pan=-0.12, gain=0.10)

        # sonar: a ping every two bars, its return a beat and a half later
        if lb % 2 == 0:
            p = ping(PING)
            sonar.add(t, p, pan=-0.2, gain=0.085)
            sonar.add(t + 1.5 * BEAT, lp(p, 1800), pan=0.35, gain=0.035)
            sonar.add(t + 3.0 * BEAT, lp(p, 1200), pan=-0.4, gain=0.014)

        # the signal: broken Morse on C#7 (intro and turn)
        if sec in ('intro', 'turn') and lb % 2 == 1:
            for s, d in ((0, 1), (2, 1), (4, 3), (8, 1), (10, 3), (14, 1)):
                sig.add(t + s * S16, beep(BEEP, d * S16 * 0.7), pan=0.45, gain=0.022)

        # percussion
        if sec in ('A', "A'", 'B', 'turn'):
            hits = {'A': ((0, 1.0), (10, 0.7)), "A'": ((0, 1.0), (10, 0.7), (11, 0.4)),
                    'B': ((0, 1.0), (6, 0.6), (10, 0.8), (11, 0.5)), 'turn': ((0, 0.9),)}[sec]
            for s, vv in hits:
                drm.add(t + s * S16, hull_drum(PEDAL, vv, lb * 16 + s), pan=-0.05, gain=0.26 if sec == 'B' else 0.20)
        if sec in ("A'", 'B'):
            for s in (8,) if sec == "A'" else (4, 12):
                drm.add(t + s * S16, clank(lb * 16 + s), pan=0.3, gain=0.05)
        if sec != 'intro':
            for s in range(0, 16, 2 if sec == 'A' else 1):
                acc = (1.0, 0.45, 0.7, 0.45)[s % 4]
                drm.add(t + s * S16 + 0.004, tick(lb * 16 + s + 500, acc), pan=0.5,
                        gain={'A': 0.045, "A'": 0.06, 'B': 0.065, 'turn': 0.045}[sec])
        if sec == 'B' and lb % 2 == 0:
            drm.add(t, hull_drum(25, 1.0, lb + 900, tau=0.9), pan=0.0, gain=0.2)
        if lb in (10, 18):                                 # the water rushing in, into A' and B
            fx.add(t, swell(2 * BAR, lb), gain=0.035 if lb == 10 else 0.05)

        # bubbles (intro and turn)
        if sec in ('intro', 'turn'):
            r = rng('bub', lb)
            for _ in range(5):
                m = int(r.choice([73, 76, 78, 80, 83, 85]))
                fx.add(t + r.uniform(0, BAR - 0.1), bubble(m, lb), pan=r.uniform(-0.6, 0.6), gain=0.03)

    # pad: each of four voices held while its note stays; a quick release
    # where the next chord brings that note's semitone neighbour
    segs = [(b * BAR, PROG[b % BARS]) for b in tl.bars_range()]
    for k in range(4):
        notes = []
        for t, c in segs:
            m = CH[c]['pad'][k]
            if notes and notes[-1][2] == m and abs(notes[-1][0] + notes[-1][1] - t) < 1e-9:
                notes[-1][1] += BAR
            else:
                notes.append([t, BAR, m])
        for j, (t, d, m) in enumerate(notes):
            nb = int(round((t + d) / BAR))
            nxt = CH[PROG[nb % BARS]]['pad'] + CH[PROG[nb % BARS]]['glass']
            rel = 0.18 if any(abs(m - o) % 12 in (1, 11) for o in nxt) else 0.9
            lb0 = int(round(t / BAR)) % BARS
            pad.add(t, pad_note(m, d - 0.02, rel, (lb0, k)), pan=-0.4 + 0.27 * k, gain=0.05)
    tt = np.arange(tl.n) / SR - tl.t0
    plv = np.interp((tt % LOOP) / BAR, np.arange(BARS + 1),
                    [{'intro': 0.7, 'A': 0.8, "A'": 0.9, 'B': 1.0, 'turn': 0.9}[section(b % BARS)] for b in range(BARS + 1)])
    padx = chorus(pad.x * lp1(plv, 0.5)[:, None], 2 * BAR, depth_ms=3.0, base_ms=9.0, mix=0.5, t0=tl.t0)

    leadx = chorus(lead.x, BAR, depth_ms=1.6, base_ms=6.0, mix=0.35, t0=tl.t0)
    glsx = gls.x + pingpong(gls.x, 3 * S16, 0.32, 4, 5000) * 0.55
    sonx = sonar.x
    engx = eng.x
    subx = np.stack([sub, sub], 1) * 0.07
    hall = make_ir(3.4, dark=6500, seed=29, pre=0.025)
    deep = make_ir(5.5, dark=3000, seed=31, pre=0.06)
    wet = reverb(leadx * 0.45 + cello.x * 0.3 + brs.x * 0.35 + padx * 0.4 + glsx * 0.4 + drm.x * 0.18
                 + fx.x * 0.6 + sig.x * 0.4, hall)
    wet2 = reverb(sonx * 1.0 + fx.x * 0.3, deep)
    stems = dict(lead=leadx, cello=cello.x, brass=brs.x, pad=padx, glass=glsx, engine=engx, sub=subx,
                 sonar=sonx, signal=sig.x, drums=drm.x, fx=fx.x, reverb=wet * 0.45 + wet2 * 0.5)
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        report(stems, mix)
    return finish(tl, mix, NAME, wav=wav)


def report(stems, mix):
    """Stem rms above 150 Hz (dB rel. the mix's, so a sub-heavy stem does not
    read louder than it sounds) per section, and the HF click ratio per stem."""
    i0 = tl.smp(0); secs = [(0, 4), (4, 12), (12, 20), (20, 28), (28, 32)]
    tot = np.sqrt(np.mean(hp(mix[i0:i0 + int(LOOP * SR)], 150) ** 2))
    print('         ' + ' '.join(f'{section(a):>7}' for a, _ in secs) + '   click')
    for k, v in stems.items():
        row = []
        vh = hp(v, 150)
        for a, b in secs:
            seg = vh[i0 + int(a * BAR * SR):i0 + int(b * BAR * SR)]
            row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) / tot + 1e-9))
        h = hp(v.mean(1), 4000)[i0:i0 + int(LOOP * SR)]          # filter first, then cut: no edge
        d = np.abs(np.diff(h, 2)); cr = d.max() / (np.percentile(d, 99.9) + 1e-12)
        hf = 20 * np.log10(np.abs(h).max() / (np.abs(v[i0:i0 + int(LOOP * SR)]).max() + 1e-12) + 1e-12)
        print(f'{k:8s} ' + ' '.join(f'{r:7.1f}' for r in row) + f'   {cr:5.1f} (HF peak {hf:5.0f} dB)')


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
