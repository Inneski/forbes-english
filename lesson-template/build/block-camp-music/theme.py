#!/usr/bin/env python3
"""Block Camp theme tune (the hub page, block-camp/index): the front door of
the course, so a THEME - one hummable, heroic-but-warm hook, stated early and
brought back, with a contrasting middle. Adventure-game title screen:
bright, optimistic, a journey. The tune is new; it quotes no game and no
C418.

D major, 120 BPM (a sixteenth is exactly 6000 samples), 4/4, one chord a bar:
    intro  D | G/D | Bm | A                       pad, plucks, bass; no lead
    A      D | A | Bm | G | D | A | G | A7         the hook, then its answer
    A'     D | A | Bm | G | Em | A | D | A7        the hook again, rising to D6
    B      G | D/F# | Em | Bm | G | D | Em | A7    starts on IV: longer notes,
                                                   half-time drums, lower lead
    A''    D | A | Bm | G | G | A | D | A7         the hook, full band, the
                                                   peak (E6), and down to A4
                                                   for the intro
All diatonic. 36 bars = 72 s, a seamless loop (see synthkit.py).

The hook (bars 4-5, sixteenths):
    A4 D5 F#5- A5--- F#5 | E5-- C#5 E5- A4-
    - a rising D-major arpeggio that leaps to the fifth and falls back
    through the A chord: 1-4-5-6-8... in plain terms "la, re-mi-SOL, mi".

The parts: lead = two detuned saws and a quiet square an octave down, low-
passed ~3 kHz, delayed vibrato, a dotted-eighth ping-pong echo; pad = a
seven-voice supersaw chord, chorused, into a warm hall; plucks = a pulse
arpeggio in eighths through the chord; bass = saw + sine, root and octave
eighths (the fifth only as a chord tone); drums = sine kick, noise snare,
closed hats in eighths (sixteenths in A''), a crash at the top of A, B, A''.

Asserted at import (check_harmony): every bar has a chord; every lead note
that starts on a beat or lasts a beat or more is a chord tone; no lead note
forms a semitone, major 7th or minor 9th with the bass note under it or with
any pad voice held under it; every bass note is a chord tone; the melody
sums to 16 sixteenths a bar or less.

Review, 2026-09-30 (measured on the m4a and on the five buses):
- Key. The first draft had an A chord in 12 of 36 bars (and F#m in B); the
  chroma leaned to A and a coarse (8192-point) Krumhansl read said A major.
  The turnarounds are A7 now (the G natural is the D-major tell) and B runs
  G | D/F# | Em | Bm | G | D | Em | A7. At 32768 points, 65-2000 Hz:
  D major r 0.868, A major 0.791 (the same method reads archive's track as
  C major 0.910).
- Brightness. 8 kHz+ was -22.6 dB of the total against present-simple's
  -25.2: the snare's hiss layer and the crash, not the hats (drums were
  -23 dB above 8 kHz, lead -45). Snare hiss 0.3 -> 0.1, crash low-passed at
  8 kHz and 2 dB down, hats down ~4 dB. Now 6-8 kHz -25.0, 8 kHz+ -24.3
  (present-simple -26.1/-25.2, passive-past-simple -31.1/-35.1).
- Balance. The pad sat 10.5 dB (A-weighted) under the lead in A; it is up
  2.5 dB. A-weighted in A: lead -20.0, pluck -24.2, drums -25.9, bass
  -26.2, pad -28.0 dB; in B the lead drops to -21.2 and the pad rises to
  -26.9.
- Clicks: no bus has an HF sample jump more than 3x its 99.9th percentile
  except the pad, whose largest (0.0018, about -55 dBFS, mid-bar) is the
  chorus on a very smooth signal, not an edge.
- Peak 0.76 under the tanh limiter, rms -16.9 dBFS, seam 0.0000.

    py lesson-template/build/block-camp-music/theme.py [--wav preview.wav]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, swept_lp, saw, pulse, supersaw,
                      adsr, perc, pingpong, make_ir, reverb, chorus, finish)

NAME = 'block-camp-theme'
BARS = 36
tl = Timeline(bpm=120, bars=BARS)
BAR, S16 = tl.bar, tl.s16

#        name    bass root  pad voicing       pitch classes
D_   = ('D',     38, [62, 66, 69, 74], {2, 6, 9})
G_D  = ('G/D',   38, [62, 67, 71, 74], {7, 11, 2})
G_   = ('G',     43, [62, 67, 71, 74], {7, 11, 2})
A_   = ('A',     45, [61, 64, 69, 73], {9, 1, 4})
A7   = ('A7',    45, [61, 64, 67, 69], {9, 1, 4, 7})
D_FS = ('D/F#',  42, [62, 66, 69, 74], {2, 6, 9})
BM   = ('Bm',    47, [62, 66, 71, 74], {11, 2, 6})
EM   = ('Em',    40, [64, 67, 71, 76], {4, 7, 11})

SECTIONS = [('intro', 0, [D_, G_D, BM, A_]),
            ('A', 4, [D_, A_, BM, G_, D_, A_, G_, A7]),
            ("A'", 12, [D_, A_, BM, G_, EM, A_, D_, A7]),
            ('B', 20, [G_, D_FS, EM, BM, G_, D_, EM, A7]),
            ("A''", 28, [D_, A_, BM, G_, G_, A_, D_, A7])]
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


# ── the lead, per bar: (sixteenth, midi, length in sixteenths) ─────────────
HOOK = [[(0, 69, 2), (2, 74, 2), (4, 78, 4), (8, 81, 6), (14, 78, 2)],          # D
        [(0, 76, 6), (6, 73, 2), (8, 76, 4), (12, 69, 4)],                      # A
        [(0, 74, 2), (2, 78, 2), (4, 83, 6), (10, 81, 2), (12, 78, 4)],         # Bm
        [(0, 79, 4), (4, 83, 2), (6, 81, 2), (8, 79, 4), (12, 74, 4)]]          # G
LEAD = {}
for _k, _bar in enumerate(HOOK):
    LEAD[4 + _k] = LEAD[8 + _k] = LEAD[12 + _k] = LEAD[28 + _k] = _bar
LEAD.update({
    9:  [(0, 76, 4), (4, 81, 4), (8, 85, 6), (14, 81, 2)],                      # A
    10: [(0, 86, 4), (4, 83, 4), (8, 79, 6), (14, 81, 2)],                      # G
    11: [(0, 81, 12), (12, 76, 4)],                                             # A
    15: HOOK[3],                                                                # G
    16: [(0, 79, 4), (4, 76, 2), (6, 79, 2), (8, 83, 6), (14, 81, 2)],          # Em
    17: [(0, 81, 4), (4, 85, 4), (8, 88, 6), (14, 85, 2)],                      # A
    18: [(0, 86, 12), (12, 81, 4)],                                             # D
    19: [(0, 85, 4), (4, 81, 4), (8, 76, 8)],                                   # A
    20: [(0, 71, 4), (4, 74, 4), (8, 79, 8)],                                   # G
    21: [(0, 78, 4), (4, 74, 4), (8, 69, 8)],                                   # D/F#
    22: [(0, 71, 4), (4, 76, 4), (8, 79, 8)],                                   # Em
    23: [(0, 83, 8), (8, 78, 4), (12, 74, 4)],                                  # Bm
    24: [(0, 74, 4), (4, 79, 4), (8, 83, 8)],                                   # G
    25: [(0, 86, 4), (4, 81, 4), (8, 78, 8)],                                   # D
    26: [(0, 76, 4), (4, 79, 4), (8, 83, 6), (14, 81, 2)],                      # Em
    27: [(0, 81, 8), (8, 76, 4), (12, 73, 4)],                                  # A
    32: [(0, 83, 4), (4, 86, 4), (8, 83, 4), (12, 79, 4)],                      # G
    33: [(0, 85, 4), (4, 88, 4), (8, 85, 4), (12, 81, 4)],                      # A
    34: [(0, 86, 12), (12, 81, 4)],                                             # D
    35: [(0, 76, 4), (4, 73, 4), (8, 69, 8)],                                   # A
})

BASS_DRIVE = [(0, 0), (2, 12), (4, 0), (6, 12), (8, 0), (10, 12), (12, 0), (14, 12)]
BASS_HALF = [(0, 0, 6), (6, 0, 2), (8, 12, 6), (14, 0, 2)]
CLASH = {1, 11, 13}


def bass_notes(b):
    root = chord(b)[1]
    pat = BASS_HALF if section(b) == 'B' else [(s, iv, 2) for s, iv in BASS_DRIVE]
    return [(s, root + iv, d) for s, iv, d in pat]


def check_harmony():
    bad = []
    for b in range(BARS):
        name, root, pad, pcs = chord(b)
        mel = LEAD.get(b, [])
        assert all(s + d <= 16 for s, _, d in mel), b
        for s, m, d in bass_notes(b):
            if m % 12 not in pcs:
                bad.append((b, 'bass', m, name))
        for s, m, d in mel:
            strong = s % 4 == 0 or d >= 4
            if strong and m % 12 not in pcs:
                bad.append((b, s, m, name, 'not a chord tone'))
            under = [bm for bs, bm, bd in bass_notes(b) if bs < s + d and bs + bd > s] + pad
            for u in under:
                if abs(m - u) in CLASH or (abs(m - u) % 12 in (1, 11) and (strong or d >= 2)):
                    bad.append((b, s, m, name, 'clash', u))
    assert not bad, bad


check_harmony()


# ── instruments ─────────────────────────────────────────────────────────────
def lead_note(m, d16):
    gate = d16 * S16 * (0.92 if d16 >= 4 else 0.8)
    n = int((gate + 0.25) * SR); t = np.arange(n) / SR
    vib = np.clip((t - 0.22) / 0.2, 0, 1) * np.sin(2 * np.pi * 5.5 * t)
    f = hz(m) * 2 ** (0.18 / 12 * vib)
    r = rng('lead', m)
    x = 0.5 * saw(f * 2 ** (6 / 1200), n, r.random()) + 0.5 * saw(f * 2 ** (-6 / 1200), n, r.random())
    x += 0.3 * pulse(f / 2, n, 0.5)
    x = swept_lp(x, 4200, 2600, q=0.8)
    x = lp1(x, 7000)
    trim = 10 ** (-0.3 * max(0, m - 84) / 20)
    return x * adsr(n, 0.012, 0.3, 0.75, 0.18, gate) * trim


def pad_chord(notes, dur, seed):
    n = int((dur + 0.6) * SR)
    x = sum(supersaw(hz(m), n, cents=(-14, -8, -3, 0, 3, 8, 14), seed=seed + i) for i, m in enumerate(notes))
    x = lp(x / len(notes), 2200, 0.7)
    return x * adsr(n, 0.25, 0.4, 0.8, 0.5, dur)


def pluck(m):
    n = int(0.3 * SR)
    x = pulse(hz(m), n, 0.25) - (2 * 0.25 - 1)          # zero-mean
    x = swept_lp(x, 5000, 900, q=1.0)
    return x * perc(n, 0.002, 0.09)


def bass_note(m, dur):
    n = int((dur + 0.05) * SR); t = np.arange(n) / SR
    x = 0.55 * swept_lp(saw(hz(m), n), 1500, 300, q=1.1) + 0.6 * np.sin(2 * np.pi * hz(m) * t)
    return x * adsr(n, 0.004, 0.08, 0.8, 0.04, dur)


def kick():
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = 50 + 110 * np.exp(-t / 0.03)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16)
    x += 0.25 * np.sin(2 * np.pi * np.cumsum(2 * f) / SR) * np.exp(-t / 0.05)
    return x * np.minimum(1, t / 0.001)


def snare():
    n = int(0.3 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(7).standard_normal(n)
    noise = (bp(z, 2800, 0.6) + 0.1 * hp1(z, 6000)) * np.exp(-t / 0.08)
    tone = np.sin(2 * np.pi * 200 * t) * np.exp(-t / 0.05)
    return noise * 1.1 + tone * 0.7


def hat(seed, open_=False):
    n = int((0.25 if open_ else 0.06) * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return lp1(hp1(hp1(z, 6000), 6000), 9000) * perc(n, 0.001, 0.08 if open_ else 0.015)


def crash():
    n = int(1.6 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(9).standard_normal(n)
    return lp1(hp1(z, 3500), 8000) * np.exp(-t / 0.5) * np.minimum(1, t / 0.002)


KICK, SNARE, CRASH = kick(), snare(), crash()


def render(wav=None):
    lead, pad, plk, bass, drums = (tl.bus() for _ in range(5))
    for b in tl.bars_range():
        t = b * BAR
        bm = b % BARS
        sec = section(b)
        i = bm - START[sec]
        name, root, voic, _ = chord(b)
        # lead
        for s, m, d in LEAD.get(bm, []):
            lead.add(t + s * S16, lead_note(m, d), pan=-0.08,
                     gain=0.16 if sec == "A''" else 0.145 if sec != 'B' else 0.13)
        # pad
        pad.add(t, pad_chord(voic, BAR - 0.05, bm), gain=0.36 if sec in ('intro', 'B') else 0.32)
        # plucks: the chord cycled up in eighths
        tones = sorted(voic) + [voic[1] + 12]
        if sec != 'intro' or i >= 2:
            for k, s in enumerate(range(0, 16, 2)):
                m = tones[[0, 1, 2, 3, 4, 3, 2, 1][k]] + 12
                plk.add(t + s * S16, pluck(m), pan=0.3 if k % 2 else -0.3,
                        gain=0.07 if sec == 'B' else 0.085)
        # bass
        for s, m, d in bass_notes(bm):
            bass.add(t + s * S16, bass_note(m, d * S16 * 0.85), gain=0.24)
        # drums
        if sec == 'intro':
            kicks, snares = ((0, 8) if i >= 2 else (0,)), ((4, 12) if i == 3 else ())
        elif sec == 'B':
            kicks, snares = (0, 10), (8,)
        else:
            kicks, snares = ((0, 6, 8) if i % 2 else (0, 8)), (4, 12)
        for s in kicks:
            drums.add(t + s * S16, KICK, gain=0.55)
        for s in snares:
            drums.add(t + s * S16, SNARE, gain=0.20)
        step = 1 if sec == "A''" else 2
        if sec != 'intro' or i >= 2:
            for s in range(0, 16, step):
                open_ = s == 14 and sec in ('A', "A'", "A''")
                drums.add(t + s * S16, hat(bm * 16 + s, open_), pan=0.2,
                          gain=0.03 if open_ else 0.026 if s % 4 == 2 else 0.017)
        if bm in (4, 20, 28):
            drums.add(t, CRASH, pan=-0.2, gain=0.06)
        if bm in (3, 19, 27):                                   # fills into A, B, A''
            for s in (12, 13, 14, 15):
                drums.add(t + s * S16, SNARE, gain=0.10 + 0.025 * (s - 12))

    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.3, 4, 3200) * 0.35
    padx = chorus(pad.x, 4 * BAR, mix=0.5, t0=-tl.t0)
    ir = make_ir(1.8, dark=3500)
    wet = reverb(leadx * 0.3 + padx * 0.5 + plk.x * 0.4 + drums.x * 0.1, ir)
    mix = leadx + padx + plk.x + bass.x + drums.x + wet * 0.3
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
