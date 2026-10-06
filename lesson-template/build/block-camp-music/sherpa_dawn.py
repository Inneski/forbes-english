#!/usr/bin/env python3
"""Sherpa Tensing soundtrack "Dawn" (the second track on the Sherpa games).

Innes, 2026-10-06: "Can we have an extra music track to alternate with at
touch of toggle?" The Climb and The Descent already play "Summit"
(summit.py, route-map.m4a): a bansuri flute over a tanpura drone. This is its
companion, so that switching between them feels like the same mountain at
another hour. An original piece, nothing quoted:

  The same mode and drone as Summit: D minor pentatonic (D F G A C) over D-A,
  and check() proves the melody keeps to it. 60 a minute, 16 bars of four =
  64 s, a seamless loop (see synthkit.py).

  Lute      a dranyen-like plucked voice (the Himalayan lute): additive
            partials that decay faster the higher they are, a short bright
            attack that falls a little in pitch, and a strummed tremolo on
            the long notes. Four phrases with long rests between.
  Hum       a low hummed drone on D2, an "oo" vowel: a soft saw through two
            formant bands, swelling a little each bar so it breathes.
  Pad       the open fifth D3-A3, quieter than Summit's.
  Tingsha   small cymbal pairs, high and inharmonic, at the end of the
            second and fourth phrases.
  Wind      band-limited noise, one grain every two bars, so it is periodic.

    py lesson-template/build/block-camp-music/sherpa_dawn.py [--wav preview.wav]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, lp, hp, bp, adsr, pingpong, make_ir, reverb, finish)

NAME = 'sherpa-dawn'
BARS = 16
tl = Timeline(bpm=60, bars=BARS, pre=7, post=1, tail=6.0)
BAR, BEAT = tl.bar, tl.beat
LOOP = tl.loop
MODE = {2, 5, 7, 9, 0}                    # D F G A C
DRONE = {2, 9}                            # D, A

# ── the lute: (beat in the loop, midi, beats, strum) ─────────────────────────
#   strum: a tremolo of repeated plucks across a long note
LUTE = [
    (2.0, 62, 1.0, False), (3.0, 65, 1.0, False), (4.0, 67, 0.5, False), (4.5, 69, 2.5, True),
    (7.5, 67, 0.5, False), (8.0, 65, 2.0, False),
    (16.0, 69, 1.0, False), (17.0, 72, 1.0, False), (18.0, 74, 3.0, True), (21.5, 72, 0.5, False),
    (22.0, 69, 1.0, False), (23.0, 67, 3.0, False),
    (34.0, 62, 0.5, False), (34.5, 65, 0.5, False), (35.0, 67, 1.0, False), (36.0, 69, 1.0, False),
    (37.0, 72, 2.0, True), (39.5, 69, 0.5, False), (40.0, 67, 2.0, False),
    (48.0, 74, 1.5, False), (49.5, 72, 0.5, False), (50.0, 69, 1.0, False), (51.0, 67, 1.0, False),
    (52.0, 65, 1.0, False), (53.0, 62, 4.0, True),
]
TINGSHA = [(6, 0.5), (15, 1.0)]           # (bar, beat): after the second and fourth phrases
PAD = [50, 57]                            # D3, A3
HUM = 38                                  # D2


def check():
    """Every lute note is in D minor pentatonic and none sits a semitone or a
    minor ninth from the drone's D and A; the notes do not overlap; the hum and
    the pad are on D or A."""
    bad = []
    for bt, m, d, _ in LUTE:
        if m % 12 not in MODE:
            bad.append(('lute', bt, m))
        for dr in DRONE:
            if (m - dr) % 12 in (1, 11):
                bad.append(('clash', bt, m, dr))
        assert bt + d <= LOOP / BEAT
    assert all(a[0] + a[2] <= b[0] + 0.01 for a, b in zip(LUTE, LUTE[1:]))
    bad += [('pad', m) for m in PAD if m % 12 not in DRONE]
    if HUM % 12 not in DRONE:
        bad.append(('hum', HUM))
    print('lute vs mode and drone:', 'all in D minor pentatonic, no semitone/b9 against D-A' if not bad else bad)
    assert not bad


check()


# ── instruments ─────────────────────────────────────────────────────────────
def pluck(m, dur, seed, bright=1.0):
    n = int((dur + 2.5) * SR); t = np.arange(n) / SR
    r = rng('pl', seed)
    f0 = hz(m) * (1 + 0.006 * np.exp(-t / 0.03))            # the string settles after the pick
    ph = 2 * np.pi * np.cumsum(f0) / SR
    x = np.zeros(n)
    for k in range(1, 14):
        a = k ** -1.0 * bright ** (k - 1) * np.exp(-t / (1.6 / k ** 0.8))
        x += a * np.sin(k * ph + r.random() * 6)
    pick = hp(r.standard_normal(n), 2000) * np.exp(-t / 0.004) * 0.25
    x = (x + pick) * np.minimum(1, t / 0.002)
    return lp1(x, 6500) * np.clip((dur + 2.5 - t) / 0.4, 0, 1)


def lute_note(m, dur, strum, seed):
    if not strum:
        return pluck(m, dur, seed) * 0.5
    out = np.zeros(int((dur + 2.5) * SR))
    k, step = 0, 0.125 * BEAT                              # a tremolo of light plucks
    while k * step < dur:
        p = pluck(m, dur - k * step, (seed, k), bright=0.82) * (0.5 if k == 0 else 0.28)
        i = int(k * step * SR)
        out[i:i + len(p)] += p[:len(out) - i]
        k += 1
    return out


def hum_bar(seed):
    dur = 2 * BAR
    n = int(dur * SR); t = np.arange(n) / SR
    r = rng('hum', seed)
    x = np.zeros(n)
    for c in (-3, 0, 3):
        p = (r.random() + np.cumsum(np.full(n, hz(HUM) * 2 ** (c / 1200))) / SR) % 1.0
        x += 2 * p - 1
    x = bp(x, 300, 2.0) * 1.0 + bp(x, 870, 3.0) * 0.35       # "oo"
    return lp(x, 1200) * np.sin(np.pi * t / dur) ** 2


def pad_note(m, seed):
    dur = 3 * BAR
    n = int(dur * SR); t = np.arange(n) / SR
    r = rng('pad', seed)
    x = np.zeros(n)
    for c in (-4, 0, 4):
        p = (r.random() + np.cumsum(np.full(n, hz(m) * 2 ** (c / 1200))) / SR) % 1.0
        x += 2 * np.abs(2 * p - 1) - 1
    return lp(x / 3, 800) * np.sin(np.pi * t / dur) ** 2


def tingsha(seed):
    n = int(7 * SR); t = np.arange(n) / SR
    r = rng('ting', seed)
    x = np.zeros(n)
    for ratio, a in ((1.0, 1.0), (2.71, 0.45), (5.13, 0.2)):
        for det in (-1.6, 1.6):                             # the two cymbals, beating
            x += a * np.sin(2 * np.pi * (hz(86) * ratio + det) * t + r.random() * 6) * np.exp(-t / (2.4 / ratio ** 0.5))
    return x * np.minimum(1, t / 0.001) * np.clip((7 - t) / 1.0, 0, 1)


def wind_grain(seed):
    dur = 2 * BAR
    n = int(dur * SR); t = np.arange(n) / SR
    return rng('wind', seed).standard_normal(n) * np.sin(np.pi * t / dur) ** 2


STEMS = {}


def render(wav=None):
    lu, hm, pad, tg, wd = (tl.bus() for _ in range(5))
    for b in tl.bars_range():
        lb, t = b % BARS, b * BAR
        if lb % 2 == 0:
            hm.add(t, hum_bar(lb), pan=0.0, gain=0.08)
            wd.add(t, wind_grain(lb), pan=0.3 * np.sin(lb), gain=1.0)
        for k, m in enumerate(PAD):
            pad.add(t, pad_note(m, (lb, k)), pan=(-0.35, 0.35)[k], gain=0.05)
        for bb, bt in TINGSHA:
            if bb == lb:
                tg.add(t + bt * BEAT, tingsha(bb), pan=0.4, gain=0.05)
    for L in range(-1, 2):
        for i, (bt, m, d, s) in enumerate(LUTE):
            lu.add(L * LOOP + bt * BEAT, lute_note(m, d * BEAT, s, i), pan=-0.08, gain=0.5)
    wind = lp(hp(wd.x, 180), 1100) * 0.035 + lp(hp(wd.x, 6000), 14000) * 0.01
    STEMS.update(lute=lu.x, hum=hm.x, pad=pad.x, tingsha=tg.x, wind=wind)
    echo = pingpong(lu.x, 0.75 * BEAT, 0.3, 4, 3500)
    hall = make_ir(4.5, dark=3800, seed=82, pre=0.03)
    dry = lu.x + echo * 0.35 + hm.x + pad.x + tg.x + wind
    wet = reverb(lu.x * 0.8 + echo * 0.4 + hm.x * 0.4 + pad.x * 0.4 + tg.x * 0.8, hall)
    return finish(tl, dry + wet * 0.45, NAME, target_db=-18.0, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
