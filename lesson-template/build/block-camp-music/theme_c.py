#!/usr/bin/env python3
"""Block Camp theme tune, OPTION C: "chiptune quest" (the hub page, offered
next to theme.py as an alternative). An 8-bit / NES-style overworld theme:
bouncy, catchy, a platformer's first level. The tune is new; it quotes no
game music.

C major, 144 BPM (a sixteenth is exactly 5000 samples), 4/4, one chord a bar:
    intro  C | Am | F | G                          arps, bass, drums; no lead
    A      C | G | Am | F | C | G | F | G          the hook, then its answer
    A'     C | G | Am | F | Dm | G | C | C         the hook again, up to C6
    B      Am | Em | F | C | Dm | Am | F | G       minor side, long notes on
                                                   a thin 12.5% pulse,
                                                   half-time drums
    A''    C | G | Am | F | F | G | C | G          the hook, busiest drums,
                                                   the peak (F6), down to G4
All diatonic. 36 bars = 60 s, a seamless loop (see synthkit.py).

The hook (bars 4-5, sixteenths):
    G4 C5 E5-- G5 C6--- G5- E5- | D5-- B4 D5- G5- B5--- G5---
    - a bouncing C arpeggio that jumps to the top C and skips back down.

The parts (the NES's five channels, more or less):
  pulse 1 = lead, 50% duty (12.5% in B), delayed vibrato, band-limited;
  pulse 2 = the classic "echo channel": the lead again at 25% duty, a dotted
            eighth late and quieter, panned the other way;
  arp     = a 25% pulse cycling the chord in sixteenths (the fast arpeggio
            standing in for a chord);
  triangle= bass: root/octave bounce in eighths (root-fifth quarters in B);
  noise   = drums: a triangle-drop kick with a noise click, a noise snare,
            short noise hats.
All pulses are low-passed (6-10 kHz) so the brightness sits with the rest
of the soundtrack, not above it.

Asserted at import (check_harmony): the same rules as theme.py: every lead
note on a beat or a beat long is a chord tone; no semitone / major 7th /
minor 9th against the bass under it or any arp tone; bass notes are chord
tones; a bar sums to 16 sixteenths or less.

Review, 2026-10-01 (measured on the m4a and the five buses):
- Key: Krumhansl (32768 points, 65-2000 Hz) C major r 0.883, G major 0.671.
- Brightness: the first draft double-low-passed the pulses at ~5 kHz and
  came out dull (6-8 kHz -34.2, 8 kHz+ -36.8 dB of the total). Pulses now a
  single 2-pole LP at 10 kHz lead / 8 in B / 7 arp / 6 echo, hats opened to
  15 kHz and up ~7 dB: 6-8 kHz -24.8, 8 kHz+ -25.8 (present-simple
  -25.7/-25.0). Bass 1.8 dB down, arp 2.3 dB up.
- Balance (rms): lead -18.7, bass -15.6, drums -23.7, arp -26.7, echo -30.2.
- Clicks: largest second-difference jump per bus at most 2.6x its 99.9th
  percentile (drum transients).
- Peak 0.68, rms -16.7 dBFS, seam 0.0000.

    py lesson-template/build/block-camp-music/theme_c.py [--wav preview.wav] [--stems stems.npz]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, lp1, hp1, lp, bp, pulse, tri, adsr, perc,
                      pingpong, make_ir, reverb, finish)

NAME = 'block-camp-theme-c'
BARS = 36
tl = Timeline(bpm=144, bars=BARS)
BAR, S16 = tl.bar, tl.s16

#        name  bass  arp tones          pitch classes
C_  = ('C',  36, [60, 64, 67, 72], {0, 4, 7})
G_  = ('G',  43, [59, 62, 67, 71], {7, 11, 2})
AM  = ('Am', 45, [60, 64, 69, 72], {9, 0, 4})
F_  = ('F',  41, [60, 65, 69, 72], {5, 9, 0})
DM  = ('Dm', 38, [62, 65, 69, 74], {2, 5, 9})
EM  = ('Em', 40, [59, 64, 67, 71], {4, 7, 11})

SECTIONS = [('intro', 0, [C_, AM, F_, G_]),
            ('A', 4, [C_, G_, AM, F_, C_, G_, F_, G_]),
            ("A'", 12, [C_, G_, AM, F_, DM, G_, C_, C_]),
            ('B', 20, [AM, EM, F_, C_, DM, AM, F_, G_]),
            ("A''", 28, [C_, G_, AM, F_, F_, G_, C_, G_])]
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
HOOK = [[(0, 67, 2), (2, 72, 2), (4, 76, 3), (7, 79, 1), (8, 84, 4), (12, 79, 2), (14, 76, 2)],   # C
        [(0, 74, 3), (3, 71, 1), (4, 74, 2), (6, 79, 2), (8, 83, 4), (12, 79, 4)],               # G
        [(0, 76, 2), (2, 72, 2), (4, 69, 2), (6, 72, 2), (8, 76, 4), (12, 81, 4)],               # Am
        [(0, 77, 2), (2, 81, 2), (4, 84, 3), (7, 81, 1), (8, 77, 4), (12, 72, 2), (14, 74, 2)]]  # F
LEAD = {}
for _k, _bar in enumerate(HOOK):
    LEAD[4 + _k] = LEAD[12 + _k] = LEAD[28 + _k] = _bar
LEAD.update({
    8:  HOOK[0], 9: HOOK[1],
    10: [(0, 81, 2), (2, 77, 2), (4, 72, 4), (8, 77, 2), (10, 81, 2), (12, 84, 4)],   # F
    11: [(0, 79, 4), (4, 83, 2), (6, 86, 2), (8, 83, 4), (12, 79, 2), (14, 74, 2)],   # G
    16: [(0, 77, 2), (2, 74, 2), (4, 69, 2), (6, 74, 2), (8, 77, 4), (12, 81, 4)],    # Dm
    17: [(0, 83, 4), (4, 86, 4), (8, 79, 4), (12, 83, 4)],                            # G
    18: [(0, 84, 8), (8, 79, 4), (12, 76, 4)],                                        # C
    19: [(0, 72, 4), (4, 76, 2), (6, 79, 2), (8, 76, 4), (12, 72, 4)],                # C
    20: [(0, 69, 6), (6, 72, 2), (8, 76, 8)],                                         # Am
    21: [(0, 79, 6), (6, 76, 2), (8, 71, 8)],                                         # Em
    22: [(0, 72, 6), (6, 77, 2), (8, 81, 8)],                                         # F
    23: [(0, 79, 8), (8, 76, 4), (12, 72, 4)],                                        # C
    24: [(0, 74, 6), (6, 77, 2), (8, 81, 8)],                                         # Dm
    25: [(0, 84, 6), (6, 81, 2), (8, 76, 8)],                                         # Am
    26: [(0, 77, 4), (4, 81, 4), (8, 84, 4), (12, 81, 4)],                            # F
    27: [(0, 79, 8), (8, 83, 4), (12, 86, 4)],                                        # G
    32: [(0, 81, 4), (4, 84, 4), (8, 89, 4), (12, 84, 4)],                            # F
    33: [(0, 86, 4), (4, 83, 4), (8, 79, 4), (12, 74, 4)],                            # G
    34: [(0, 84, 12), (12, 79, 4)],                                                   # C
    35: [(0, 74, 4), (4, 71, 4), (8, 67, 8)],                                         # G
})

BASS_BOUNCE = [(s, 0 if s % 4 == 0 else 12, 2) for s in range(0, 16, 2)]
BASS_HALF = [(0, 0, 4), (4, 7, 4), (8, 0, 4), (12, 7, 4)]
CLASH = {1, 11, 13}
ARP_ORDER = [0, 1, 2, 3, 2, 1]


def bass_notes(b):
    root = chord(b)[1]
    return [(s, root + iv, d) for s, iv, d in (BASS_HALF if section(b) == 'B' else BASS_BOUNCE)]


def check_harmony():
    bad = []
    for b in range(BARS):
        name, root, arp, pcs = chord(b)
        mel = LEAD.get(b, [])
        assert all(s + d <= 16 for s, _, d in mel), b
        assert all(m % 12 in pcs for m in arp), b
        for s, m, d in bass_notes(b):
            if m % 12 not in pcs:
                bad.append((b, 'bass', m, name))
        for s, m, d in mel:
            strong = s % 4 == 0 or d >= 4
            if strong and m % 12 not in pcs:
                bad.append((b, s, m, name, 'not a chord tone'))
            under = [bm for bs, bm, bd in bass_notes(b) if bs < s + d and bs + bd > s] + arp + [a + 12 for a in arp]
            for u in under:
                if abs(m - u) in CLASH or (abs(m - u) % 12 in (1, 11) and (strong or d >= 2)):
                    bad.append((b, s, m, name, 'clash', u))
    assert not bad, bad


check_harmony()


# ── instruments ─────────────────────────────────────────────────────────────
def bl_pulse(f, n, duty, fc):
    """A pulse, DC removed and band-limited (a naive pulse aliases; the NES
    output stage is dull anyway)."""
    x = pulse(f, n, duty) - (2 * duty - 1)
    return lp(x, fc, 0.6)


def lead_note(m, d16, duty, fc=10000):
    gate = d16 * S16 * (0.9 if d16 >= 4 else 0.75)
    n = int((gate + 0.08) * SR); t = np.arange(n) / SR
    vib = np.clip((t - 0.18) / 0.15, 0, 1) * np.sin(2 * np.pi * 6.0 * t)
    f = hz(m) * 2 ** (0.25 / 12 * vib)
    x = bl_pulse(f, n, duty, fc)
    trim = 10 ** (-0.35 * max(0, m - 84) / 20)
    return x * adsr(n, 0.003, 0.12, 0.7, 0.05, gate) * trim


def arp_note(m):
    n = int(S16 * 0.95 * SR)
    x = bl_pulse(hz(m), n, 0.25, 7000)
    return x * adsr(n, 0.002, 0.04, 0.6, 0.012, S16 * 0.8)


def tri_bass(m, dur):
    n = int((dur + 0.02) * SR)
    x = lp(tri(hz(m), n), 3000, 0.6)
    return x * adsr(n, 0.003, 0.05, 0.9, 0.015, dur)


def kick():
    n = int(0.18 * SR); t = np.arange(n) / SR
    f = 55 + 180 * np.exp(-t / 0.02)
    ph = np.cumsum(f) / SR % 1.0
    body = (2 * np.abs(2 * ph - 1) - 1) * np.exp(-t / 0.07)
    click = lp(np.random.default_rng(4).standard_normal(n), 3000) * np.exp(-t / 0.006) * 0.4
    return lp(body + click, 4000) * np.minimum(1, t / 0.001)


def snare():
    n = int(0.2 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(5).standard_normal(n)
    noise = lp(hp1(z, 400), 5000, 0.6) * np.exp(-t / 0.06)
    tone = np.sin(2 * np.pi * 220 * t) * np.exp(-t / 0.03)
    return (noise + 0.5 * tone) * np.minimum(1, t / 0.001)


def hat(seed, long_=False):
    n = int((0.12 if long_ else 0.04) * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return lp(hp1(z, 5000), 15000, 0.6) * perc(n, 0.001, 0.04 if long_ else 0.01)


KICK, SNARE = kick(), snare()


def render(wav=None):
    lead, echo, arp, bass, drums = (tl.bus() for _ in range(5))
    for b in tl.bars_range():
        t = b * BAR
        bm = b % BARS
        sec = section(b)
        i = bm - START[sec]
        name, root, tones, _ = chord(b)
        # pulse 1 lead + pulse 2 echo
        duty = 0.125 if sec == 'B' else 0.5
        g = 0.20 if sec == "A''" else 0.18 if sec != 'B' else 0.21
        for s, m, d in LEAD.get(bm, []):
            fc = 8000 if sec == 'B' else 10000
            lead.add(t + s * S16, lead_note(m, d, duty, fc), pan=-0.12, gain=g)
            echo.add(t + (s + 3) * S16, lead_note(m, d, 0.25, 6000), pan=0.35, gain=g * 0.3)
        # the arp: chord tones in sixteenths, an octave up in A''
        up = 12 if sec == "A''" else 0
        for s in range(16):
            if sec == 'B' and s % 2:
                continue                                          # eighths in B: calmer
            m = tones[ARP_ORDER[s % len(ARP_ORDER)]] + up
            arp.add(t + s * S16, arp_note(m), pan=0.25, gain=0.09 if sec != 'intro' else 0.105)
        # triangle bass
        for s, m, d in bass_notes(bm):
            bass.add(t + s * S16, tri_bass(m, d * S16 * 0.85), gain=0.34)
        # noise drums
        if sec == 'intro':
            kicks, snares = ((0, 8) if i >= 1 else (0,)), ((4, 12) if i >= 2 else ())
        elif sec == 'B':
            kicks, snares = (0, 6), (8,)
        else:
            kicks, snares = ((0, 6, 10) if i % 2 else (0, 8)), (4, 12)
        for s in kicks:
            drums.add(t + s * S16, KICK, gain=0.5)
        for s in snares:
            drums.add(t + s * S16, SNARE, gain=0.22)
        step = 1 if sec == "A''" else 2
        for s in range(0, 16, step):
            long_ = s == 14 and sec != 'B'
            drums.add(t + s * S16, hat(bm * 16 + s, long_), pan=0.15,
                      gain=0.11 if long_ else 0.10 if s % 4 == 2 else 0.07)
        if bm in (3, 19, 27):                                     # fills into A, B, A''
            for s in (12, 13, 14, 15):
                drums.add(t + s * S16, SNARE, gain=0.10 + 0.03 * (s - 12))

    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.2, 3, 3000) * 0.2
    ir = make_ir(0.9, dark=3500)
    wet = reverb(leadx * 0.3 + echo.x * 0.3 + arp.x * 0.3 + drums.x * 0.05, ir)
    mix = leadx + echo.x + arp.x + bass.x + drums.x + wet * 0.22
    if '--stems' in sys.argv:
        np.savez_compressed(sys.argv[sys.argv.index('--stems') + 1], lead=leadx, echo=echo.x,
                            arp=arp.x, bass=bass.x, drums=drums.x, a=tl.smp(-0.5), b=tl.smp(tl.loop + 0.5))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
