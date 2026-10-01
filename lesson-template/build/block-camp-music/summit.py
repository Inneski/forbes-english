#!/usr/bin/env python3
"""Block Camp soundtrack "Summit" (the route maps, up and down).

Innes, 2026-10-01: "add ethnic flute atmospheric music to route camp pages".
block-camp-map.html is the climb through nine camps, block-camp-descent-map.html
the way down, so: high mountains, Himalayan air. An original piece, nothing
quoted:

  D minor pentatonic (D F G A C) and nothing else, over a D-A drone. The
  mode has no semitones in it and none of its notes sits a semitone or a
  minor ninth from D or A, and check() proves the lines keep to it.
  No beat to speak of: 60 a minute, 18 bars of four = 72 s, a seamless loop
  (see synthkit.py). Four flute phrases float over it with long silences
  between, placed on fractional beats so they feel free.

  Flute     a bansuri-like voice: a near-sine (2nd and 3rd harmonics soft)
            with strong breath noise (band-passed around the note and a broad
            airy band), each note sliding up into pitch from below or flicked
            from a grace note a scale step above, a slow vibrato that grows
            on long notes, and one overblown accent (brighter, more breath)
            at the top of the third phrase. A dotted-quarter echo and a long
            hall.
  Tanpura   a plucked Pa-Sa-Sa-Sa cycle (A2 D3 D3 D2), one pluck a beat;
            additive harmonics whose upper partials bloom after the pluck
            (the jawari buzz), slightly detuned pairs so it shimmers.
  Pad       a sustained open fifth D3-A3-D4, soft detuned triangles, low-passed,
            a new overlapping note each bar so it breathes.
  Bowls     singing bowls on D4 and A3 - partials at 1, 3 and 6 times the
            fundamental (so every partial is D or A), each a pair a fraction
            of a hertz apart for the slow beating; 16 s decays across the seam.
  Drum      a very soft frame drum tuned to D2 in the middle section.
  Wind      band-limited noise, grain per bar, so it is periodic too.

    py lesson-template/build/block-camp-music/summit.py [--wav preview.wav]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, perc, pingpong,
                      make_ir, reverb, finish)

NAME = 'route-map'
BARS = 18
tl = Timeline(bpm=60, bars=BARS, pre=7, post=1, tail=6.0)
BAR, BEAT = tl.bar, tl.beat
LOOP = tl.loop
MODE = {2, 5, 7, 9, 0}                    # D F G A C
DRONE = {2, 9}                            # D, A

# ── the flute: (beat in the loop, midi, beats, ornament) ────────────────────
#   ornament: 'bend' slides up from a step below, 'grace' flicks down from the
#   scale note above, 'accent' is overblown, '' is a plain tongued change.
FLUTE = [
    (4.0, 69, 3.0, 'bend'), (7.2, 72, 0.6, ''), (7.8, 74, 3.2, 'grace'), (11.1, 72, 0.5, ''),
    (11.7, 69, 3.8, 'bend'),
    (20.3, 62, 2.4, 'bend'), (22.8, 65, 0.9, ''), (23.8, 67, 1.1, ''), (25.0, 69, 4.2, 'grace'),
    (34.2, 74, 2.4, 'bend'), (36.7, 77, 3.0, 'accent'), (39.8, 74, 1.0, ''), (40.9, 72, 0.6, ''),
    (41.6, 69, 4.2, 'bend'),
    (50.1, 67, 2.0, 'bend'), (52.3, 65, 0.9, ''), (53.3, 62, 1.2, ''), (54.6, 60, 0.8, ''),
    (55.5, 62, 5.0, 'grace'),
]
SCALE = sorted(m for m in range(48, 90) if m % 12 in MODE)


def above(m):
    return SCALE[SCALE.index(m) + 1]


def below(m):
    return SCALE[SCALE.index(m) - 1]


TANPURA = [45, 50, 50, 38]                # Pa Sa Sa Sa(low), one a beat
PAD = [50, 57, 62, 65]                    # the open fifth, and a soft F4 to name the minor
BOWLS = [(0, 0.0, 62), (6, 2.5, 57), (11, 1.0, 62), (15, 3.0, 57)]   # (bar, beat, midi)
BOWL_PARTIALS = [(1.0, 1.0), (3.0, 0.35), (6.0, 0.12)]
DRUM = [(b, q) for b in range(7, 13) for q in ((0,) if b % 2 else (0, 2.5))]


def check():
    """Every flute note - held, strong or passing, graces and bend starts
    included - is in D minor pentatonic; nothing pitched sits a semitone or a
    minor ninth from the drone's D and A; bowls, pad, tanpura and drum are on
    D or A."""
    bad = []
    for bt, m, d, orn in FLUTE:
        ext = [m] + ([above(m)] if orn == 'grace' else []) + ([below(m)] if orn == 'bend' else [])
        for x in ext:
            if x % 12 not in MODE:
                bad.append(('flute', bt, x))
            for dr in DRONE:
                if (x - dr) % 12 in (1, 11):
                    bad.append(('clash', bt, x, dr))
        assert bt + d <= LOOP / BEAT + 4
    starts = [f[0] for f in FLUTE]
    assert starts == sorted(starts) and all(a[0] + a[2] <= b[0] + 0.01 for a, b in zip(FLUTE, FLUTE[1:]))
    for name, ms in (('tanpura', TANPURA), ('pad', PAD[:3]), ('bowl', [b[2] for b in BOWLS]),
                     ('drum', [38])):
        bad += [(name, m) for m in ms if m % 12 not in DRONE]
    bad += [('pad third', m) for m in PAD[3:] if m % 12 not in MODE or any((m - d) % 12 in (1, 11) for d in DRONE)]
    for _, p in [(0, r) for r, _ in BOWL_PARTIALS]:
        assert abs(p - round(p)) < 1e-9 and round(p) in (1, 2, 3, 4, 6, 8)   # octaves and 12ths only
    print('flute vs mode and drone:', 'all in D minor pentatonic, no semitone/b9 against D-A'
          if not bad else bad)
    assert not bad


check()


# ── instruments ─────────────────────────────────────────────────────────────
def flute_note(m, dur, orn, seed):
    n = int((dur + 0.6) * SR); t = np.arange(n) / SR
    r = rng('fl', seed)
    f0 = hz(m)
    semis = np.zeros(n)
    if orn == 'bend':                           # slide up from the step below
        k = below(m) - m
        semis += k * np.exp(-t / 0.07) * (t < 0.5)
    elif orn == 'grace':                        # a flick from the step above
        k = above(m) - m
        semis += k * (t < 0.07) * (1 - np.clip((t - 0.05) / 0.02, 0, 1))
    vd = np.clip((t - 0.5) / 1.2, 0, 1) * (0.25 if dur > 1.5 else 0.08)
    semis += vd * np.sin(2 * np.pi * 4.7 * t + r.random() * 6)
    semis += 0.04 * np.sin(2 * np.pi * 0.7 * t + r.random() * 6)        # breath drift
    f = f0 * 2 ** (semis / 12)
    ph = 2 * np.pi * np.cumsum(f) / SR
    acc = orn == 'accent'
    tone = np.sin(ph) + (0.22 if acc else 0.1) * np.sin(2 * ph) + (0.16 if acc else 0.05) * np.sin(3 * ph) \
        + (0.06 if acc else 0.0) * np.sin(4 * ph)
    z = r.standard_normal(n)
    breath = bp(z, f0 * 1.0, 4.0) * 1.2 + bp(z, f0 * 2.0, 3.0) * 0.5 + lp(hp(z, 1500), 9000) * 0.6
    breath = breath * (1.6 if acc else 1.0)
    att = 0.18 if orn == 'bend' else 0.09
    env = adsr(n, att, 0.3, 0.85, 0.35, dur)
    swell = 1 + 0.12 * np.sin(np.pi * np.clip(t / max(dur, 0.1), 0, 1))
    chiff = np.exp(-t / 0.05) * 0.8                                   # the attack's puff
    return (tone * env * swell + breath * (env * 0.18 + chiff * env ** 0.3 * 0.25)) * 0.5


def tanpura(m, seed):
    n = int(5.5 * SR); t = np.arange(n) / SR
    r = rng('tp', seed)
    x = np.zeros(n)
    for k in range(1, 30):
        bloom = 1 + 2.5 * np.exp(-((k - 10) / 4) ** 2) * (1 - np.exp(-t / 0.6))
        a = k ** -1.1 * bloom * np.exp(-t / (3.0 / (1 + 0.05 * k)))
        for det in (-0.25, 0.25):
            x += a * np.sin(2 * np.pi * (hz(m) * k + det) * t + r.random() * 6)
    x *= np.minimum(1, t / 0.004) * np.clip((5.5 - t) / 0.5, 0, 1)
    return lp1(x, 9000) * 0.06


def pad_note(m, seed):
    dur = 3 * BAR
    n = int(dur * SR); t = np.arange(n) / SR
    r = rng('pad', seed)
    x = np.zeros(n)
    for c in (-4, 0, 4):
        p = (r.random() + np.cumsum(np.full(n, hz(m) * 2 ** (c / 1200))) / SR) % 1.0
        x += 2 * np.abs(2 * p - 1) - 1
    env = np.sin(np.pi * t / dur) ** 2                     # overlapping thirds sum flat
    return lp(x / 3, 900) * env


def bowl(m, seed):
    n = int(20 * SR); t = np.arange(n) / SR
    r = rng('bowl', seed)
    x = np.zeros(n)
    for ratio, a in BOWL_PARTIALS:
        f = hz(m) * ratio
        tau = 9.0 / ratio ** 0.5
        for det in (-0.35, 0.35):
            x += a * np.sin(2 * np.pi * (f + det * ratio) * t + r.random() * 6) * np.exp(-t / tau)
    strike = lp(r.standard_normal(n), 2500) * np.exp(-t / 0.01) * 0.3
    x = (x + strike) * np.minimum(1, t / 0.003) * np.clip((20 - t) / 2, 0, 1)
    return x


def drum(seed):
    n = int(1.2 * SR); t = np.arange(n) / SR
    f = hz(38) * (1 + 0.25 * np.exp(-t / 0.03))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.35)
    skin = lp(rng('dr', seed).standard_normal(n), 900) * np.exp(-t / 0.02) * 0.3
    return (body + skin) * np.minimum(1, t / 0.004)


def wind_grain(seed):
    dur = 2 * BAR
    n = int(dur * SR); t = np.arange(n) / SR
    z = rng('wind', seed).standard_normal(n)
    return z * np.sin(np.pi * t / dur) ** 2


STEMS = {}


def render(wav=None):
    fl, tp, pad, bw, dr, wd = (tl.bus() for _ in range(6))
    TP = [tanpura(m, q) for q, m in enumerate(TANPURA)]        # four plucks, reused
    for b in tl.bars_range():
        lb, t = b % BARS, b * BAR
        lap = b - lb
        for q, m in enumerate(TANPURA):
            tp.add(t + q * BEAT + 0.01 * ((lb * 4 + q) % 3), TP[q],
                   pan=(-0.3, 0.2, 0.25, -0.15)[q], gain=0.9)
        for k, m in enumerate(PAD):
            pad.add(t, pad_note(m, (lb, k)), pan=(-0.4, 0.4, 0.0, 0.2)[k], gain=(0.09, 0.09, 0.09, 0.05)[k])
        wd.add(t, wind_grain(lb), pan=0.3 * np.sin(lb), gain=1.0)
        for bb, bt, m in BOWLS:
            if bb == lb:
                bw.add(t + bt * BEAT, bowl(m, bb), pan=(0.45 if m == 62 else -0.45), gain=0.1)
        for bb, bt in DRUM:
            if bb == lb:
                dr.add(t + bt * BEAT, drum((bb, bt)), pan=-0.1, gain=0.3 if bt == 0 else 0.18)
    for L in range(-1, 2):
        for i, (bt, m, d, orn) in enumerate(FLUTE):
            fl.add(L * LOOP + bt * BEAT, flute_note(m, d * BEAT, orn, i), pan=0.05, gain=0.4)
    wind = lp(hp(wd.x, 180), 1100) * 0.04
    wind = wind + bp(wd.x, 2400, 1.5) * 0.012 + lp(hp(wd.x, 6000), 14000) * 0.012
    STEMS.update(flute=fl.x, tanpura=tp.x, pad=pad.x, bowls=bw.x, drum=dr.x, wind=wind)
    echo = pingpong(fl.x, 0.75 * BEAT, 0.35, 5, 3000)
    hall = make_ir(5.0, dark=3500, seed=81, pre=0.035)
    dry = fl.x + echo * 0.45 + tp.x + pad.x + bw.x + dr.x + wind
    wet = reverb(fl.x * 0.9 + echo * 0.5 + tp.x * 0.5 + pad.x * 0.4 + bw.x * 0.7 + dr.x * 0.6, hall)
    mix = dry + wet * 0.5
    mix = mix + 1.4 * bp(mix, 3000, 0.9)              # presence: the breath and the jawari
    return finish(tl, mix, NAME, target_db=-18.0, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
