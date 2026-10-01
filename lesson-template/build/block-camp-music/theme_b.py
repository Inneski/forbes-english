#!/usr/bin/env python3
"""Block Camp theme tune, OPTION B, "gentle wonder" (the hub page,
block-camp/index). Option A (theme.py) is a bright 120 BPM synth adventure in
D; this is its opposite number: a calm, nostalgic, piano-led ambient theme
for a blocky world at first light - soft felt piano, warm pads, a music box,
a lot of space. An original tune; it quotes no game and no C418.

F major, 75 BPM (a sixteenth is exactly 9600 samples), 4/4, one chord a bar:
    intro  F | Bb | Dm7 | C                     pad and music box alone
    A      F | Am | Bbmaj7 | F                  the motif on piano
           Dm7 | Bbmaj7 | Gm7 | C               its answer
    B      Dm | Bb | F | C | Dm | Bb | Gm7 | C  longer notes, higher; the
                                                music box answers the piano
                                                with the motif's head
    A'     F | Am | Bbmaj7 | F                  the motif once more, piano
                                                doubled by the music box,
                                                and home to the intro
All diatonic. 24 bars = 76.8 s, a seamless loop (see synthkit.py).

The motif (bars 4-7, eighths):
    A4 C5 F5--- | E5-- (D5) C5--- | D5 F5 A5-- (G5) | F5----- C5
    - a slow climb up the F triad that settles, lifts to A over Bbmaj7 and
    sighs back to F. It comes back in bars 20-23 and its head (A C F, up
    a triad) is what the music box sings in B.

The parts: piano = additive felt piano (slightly stretched partials, each
decaying at its own rate, a soft low-passed hammer), right-hand melody plus
a quiet left hand on beats 1 and 3; pad = detuned saws and a sine, low-passed
~1 kHz, slow swell, chorused; music box = a sine with a 2.76x and 5.4x
inharmonic partial, fast bright decay, dotted-eighth ping-pong echo; bass =
a soft sine-and-triangle root, whole notes (root and fifth in B); air = a
very quiet band-passed noise breath, swelling over each four bars. No drums.

Asserted at import (check_harmony): every melody or music-box note that
starts on a beat or is held a quarter or more is a chord tone; no such note
is a semitone, major 7th or minor 9th (or compound semitone) from the bass
or any pad voice under it, and no note of any length forms a semitone or
minor ninth with them; every bass note is a chord tone; bars sum to 8
eighths or less.

    py lesson-template/build/block-camp-music/theme_b.py [--wav preview.wav]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, saw, tri, adsr, perc,
                      pingpong, make_ir, reverb, chorus, finish)

NAME = 'block-camp-theme-b'
BARS = 24
tl = Timeline(bpm=75, bars=BARS)
BAR, BEAT, E8 = tl.bar, tl.beat, tl.beat / 2

#        name     bass  pad voicing          pitch classes
F_   = ('F',      41, [53, 57, 60, 65], {5, 9, 0})
BB   = ('Bb',     46, [53, 58, 62, 65], {10, 2, 5})
BBM7 = ('Bbmaj7', 46, [53, 57, 62, 65], {10, 2, 5, 9})
AM   = ('Am',     45, [52, 57, 60, 64], {9, 0, 4})
DM   = ('Dm',     38, [53, 57, 62, 65], {2, 5, 9})
DM7  = ('Dm7',    38, [53, 57, 60, 62], {2, 5, 9, 0})
GM7  = ('Gm7',    43, [53, 58, 62, 65], {7, 10, 2, 5})
C_   = ('C',      36, [52, 55, 60, 64], {0, 4, 7})

SECTIONS = [('intro', 0, [F_, BB, DM7, C_]),
            ('A', 4, [F_, AM, BBM7, F_, DM7, BBM7, GM7, C_]),
            ('B', 12, [DM, BB, F_, C_, DM, BB, GM7, C_]),
            ("A'", 20, [F_, AM, BBM7, F_])]
SEC_OF, CH_OF, START = {}, {}, {}
for _n, _s, _cs in SECTIONS:
    START[_n] = _s
    for _k, _c in enumerate(_cs):
        SEC_OF[_s + _k], CH_OF[_s + _k] = _n, _c
assert sorted(SEC_OF) == list(range(BARS))


def section(b):
    return SEC_OF[b % BARS]


def chord(b):
    return CH_OF[b % BARS]


# ── the piano melody, per bar: (eighth, midi, eighths) ──────────────────────
MOTIF = [[(0, 69, 2), (2, 72, 2), (4, 77, 4)],                   # F      A C F
         [(0, 76, 3), (3, 74, 1), (4, 72, 4)],                   # Am     E (D) C
         [(0, 74, 2), (2, 77, 2), (4, 81, 3), (7, 79, 1)],       # Bbmaj7 D F A (G)
         [(0, 77, 6), (6, 72, 2)]]                               # F      F C
MEL = {}
for _k, _bar in enumerate(MOTIF):
    MEL[4 + _k] = MEL[20 + _k] = _bar
MEL.update({
    8:  [(0, 69, 2), (2, 72, 2), (4, 74, 4)],                    # Dm7    A C D
    9:  [(0, 77, 3), (3, 76, 1), (4, 74, 4)],                    # Bbmaj7 F (E) D
    10: [(0, 70, 2), (2, 74, 2), (4, 77, 4)],                    # Gm7    Bb D F
    11: [(0, 76, 6)],                                            # C      E
    12: [(0, 81, 4), (4, 77, 4)],                                # Dm     A F
    13: [(0, 74, 6)],                                            # Bb     D
    14: [(0, 72, 4), (4, 77, 4)],                                # F      C F
    15: [(0, 79, 6)],                                            # C      G
    16: [(0, 77, 4), (4, 81, 4)],                                # Dm     F A
    17: [(0, 82, 4), (4, 77, 4)],                                # Bb     Bb F
    18: [(0, 79, 4), (4, 74, 4)],                                # Gm7    G D
    19: [(0, 76, 6)],                                            # C      E
})
# the music box, per bar: intro twinkles, the motif's head in B's gaps, and
# the motif doubled two octaves up in A'
BOX = {
    0: [(1, 84, 1), (3, 89, 1), (6, 93, 2)],                     # F      C F A
    1: [(1, 86, 1), (3, 89, 1), (6, 94, 2)],                     # Bb     D F Bb
    2: [(1, 84, 1), (3, 86, 1), (6, 93, 2)],                     # Dm7    C D A
    3: [(1, 84, 1), (3, 88, 1), (6, 91, 2)],                     # C      C E G
    13: [(5, 86, 1), (6, 89, 1), (7, 94, 1)],                    # Bb     D F Bb  (the head, up)
    15: [(5, 84, 1), (6, 88, 1), (7, 91, 1)],                    # C      C E G
    17: [(5, 86, 1), (6, 89, 1), (7, 94, 1)],                    # Bb
    19: [(5, 88, 1), (6, 91, 1), (7, 96, 1)],                    # C      E G C
}
for _k, _bar in enumerate(MOTIF):
    BOX[20 + _k] = [(s, m + 12, d) for s, m, d in _bar]


def bass_notes(b):
    root = chord(b)[1]
    if section(b) == 'B':
        return [(0, root, 4), (4, root + 7, 4)]
    return [(0, root, 8)]


def left_hand(b):
    """Quiet piano chords on beats 1 and 3 in A and A' (the pad's voicing)."""
    if section(b) in ('A', "A'"):
        v = chord(b)[2]
        return [(0, v[:3]), (4, v[1:])]
    if section(b) == 'B':
        v = chord(b)[2]
        return [(0, v[:2]), (4, v[2:])]
    return []


def check_harmony():
    bad = []
    for b in range(BARS):
        name, root, pad, pcs = chord(b)
        for s, m, d in bass_notes(b):
            if m % 12 not in pcs:
                bad.append((b, 'bass', m, name))
        for part, line in (('mel', MEL.get(b, [])), ('box', BOX.get(b, []))):
            assert sum(d for _, _, d in line) <= 8 and all(s + d <= 8 for s, _, d in line), (b, part)
            for s, m, d in line:
                strong = s % 2 == 0 or d >= 2
                if strong and m % 12 not in pcs:
                    bad.append((b, part, s, m, name, 'not a chord tone'))
                under = [bm for bs, bm, bd in bass_notes(b) if bs < s + d and bs + bd > s] + list(pad)
                for bs, ns in left_hand(b):
                    under += ns
                for u in under:
                    iv = abs(m - u)
                    if iv % 12 == 1 or (strong and iv == 11):
                        bad.append((b, part, s, m, name, 'clash', u))
    assert not bad, bad


check_harmony()


# ── instruments ─────────────────────────────────────────────────────────────
def piano(m, dur, vel=1.0):
    """Felt piano: stretched partials, higher ones dying faster, a soft
    hammer, damped `dur` seconds after the strike."""
    f0 = hz(m)
    ring = dur + 1.6
    n = int(ring * SR); t = np.arange(n) / SR
    r = rng('pno', m)
    x = np.zeros(n)
    B = 0.00025
    for k in range(1, 13):
        fk = f0 * k * np.sqrt(1 + B * k * k)
        if fk > 12000:
            break
        amp = (0.9 / k ** 1.25) * (1.0 if k == 1 else 0.8)
        tau = 2.6 * (261.6 / f0) ** 0.35 / k ** 0.8
        det = 1 + (r.random() - 0.5) * 0.0006
        x += amp * np.sin(2 * np.pi * fk * det * t + r.random() * 2 * np.pi) * np.exp(-t / tau)
    hammer = lp(r.standard_normal(n), 2500) * np.exp(-t / 0.010) * 0.06
    x = x + hammer
    x = lp1(x, 6500 + 30 * m)                      # felt: soft, a touch brighter up top
    damp = np.clip(1 - (t - dur) / 0.35, 0, 1)
    env = np.minimum(1, t / 0.006) * damp
    return x * env * vel


def music_box(m):
    n = int(2.2 * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.7)
    x += 0.22 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t / 0.18)
    x += 0.15 * np.sin(2 * np.pi * f * 5.40 * t) * np.exp(-t / 0.10)
    x *= np.minimum(1, t / 0.002)
    return lp1(x, 10000)


def pad_chord(notes, dur, seed):
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for i, m in enumerate(notes):
        r = rng('pad', seed, i)
        for c in (-7, 0, 7):
            x += 0.35 * saw(hz(m) * 2 ** (c / 1200), n, r.random())
        x += 0.8 * np.sin(2 * np.pi * hz(m) * t)
    x = lp(lp(x / len(notes), 1100, 0.6), 1600, 0.6)
    return x * adsr(n, 0.9, 0.6, 0.85, 1.0, dur)


def bass_note(m, dur):
    n = int((dur + 0.6) * SR); t = np.arange(n) / SR
    x = 0.8 * np.sin(2 * np.pi * hz(m) * t) + 0.25 * lp1(tri(hz(m), n), 600)
    return lp1(x * adsr(n, 0.08, 0.5, 0.7, 0.6, dur), 500)


def render(wav=None, buses=None):
    mel, lh, pad, box, bass, air = (tl.bus() for _ in range(6))
    for b in tl.bars_range():
        t = b * BAR
        bm = b % BARS
        sec = section(b)
        name, root, voic, _ = chord(b)
        for s, m, d in MEL.get(bm, []):
            mel.add(t + s * E8, piano(m, d * E8 * 1.05, 0.95 if s % 4 == 0 else 0.8), pan=0.05, gain=0.30)
        for s, ns in left_hand(bm):
            for j, m in enumerate(ns):
                lh.add(t + s * E8 + j * 0.018, piano(m, 4 * E8 * 0.95, 0.5), pan=-0.15, gain=0.13)
        pad.add(t, pad_chord(voic, BAR - 0.3, bm),
                gain=0.30 if sec in ('intro', 'B') else 0.24)
        for s, m, d in BOX.get(bm, []):
            box.add(t + s * E8, music_box(m), pan=0.35 if s % 2 else -0.25,
                    gain=0.11 if sec == "A'" else 0.14)
        for s, m, d in bass_notes(bm):
            bass.add(t + s * E8, bass_note(m, d * E8 * 0.95), gain=0.24)
    # air: a quiet breath, one swell per four bars (so it is periodic)
    # filtered in the frequency domain, so the 4-bar tile is exactly periodic
    # and tiles butt together with no edge
    N = int(round(4 * BAR * SR))
    Z = np.fft.rfft(np.random.default_rng(3).standard_normal((N, 2)), axis=0)
    f = np.fft.rfftfreq(N, 1 / SR)[:, None]
    shape = np.exp(-0.5 * (np.log2(np.maximum(f, 1) / 700) / 0.7) ** 2)         + 0.5 * np.exp(-0.5 * (np.log2(np.maximum(f, 1) / 3000) / 0.6) ** 2)
    z = np.fft.irfft(Z * shape, n=N, axis=0)
    z /= np.sqrt(np.mean(z ** 2))
    u = np.arange(N) / N
    tile = z * (0.35 + 0.65 * np.sin(np.pi * u) ** 2)[:, None]
    for b in range(-tl.pre, BARS + tl.post, 4):
        air.add(b * BAR, tile, gain=0.02)

    melx = mel.x + pingpong(mel.x, 3 * E8, 0.25, 3, 2500) * 0.25
    boxx = box.x + pingpong(box.x, 3 * E8, 0.4, 5, 4000) * 0.5
    padx = chorus(pad.x, 4 * BAR, depth_ms=3.0, mix=0.5, t0=-tl.t0)
    ir = make_ir(3.6, dark=5000)
    wet = reverb(melx * 0.45 + lh.x * 0.5 + padx * 0.5 + boxx * 0.7 + air.x * 0.3, ir)
    mix = melx + lh.x + padx + boxx + bass.x + air.x + wet * 0.38
    if buses is not None:
        buses.update(mel=melx, lh=lh.x, pad=padx, box=boxx, bass=bass.x, air=air.x, wet=wet * 0.38)
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
