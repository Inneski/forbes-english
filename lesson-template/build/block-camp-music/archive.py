#!/usr/bin/env python3
"""Block Camp soundtrack "Archive" (Passive Past Simple).

Style brief, 2026-09-30: 8-bit chiptune adventure, NES-style - about
136-144 BPM, two pulse-wave channels (a lead with 12.5%/25% duty and
vibrato; harmony as fast chord arpeggios), a triangle-wave bass, a
noise-channel drum kit (short noise bursts for hats and snare, a pitched-down
triangle kick). Soft-edged: a gentle low-pass on the pulses so nothing is
shrill. Heroic, upbeat, major. The tune is new; it quotes no game.

C major, 144 BPM (a sixteenth is exactly 5000 samples), 4/4, one chord a
bar (two where marked):
    intro   C | Bb/C | F/C | G
    A       C | Am | F | G | C | Am | F G | C
    A'      C | Am | F | G | C | Em | F G | C
    B       Ab | Bb | C | C | Ab | Bb | G | G          (the heroic bVI-bVII-I)
    bridge  F | G | Em | Am | F | G | Am | G
    fanfare Ab | Bb | C | G                           -> intro
The borrowed Ab and Bb are the "adventure" colour; everything else is
diatonic.

The channels, as on the console: pulse 1 is the lead (25% duty, 12.5% in
the bridge, low-passed harder there), with delayed vibrato and a short
slap echo; pulse 2 plays the
chords as frame-rate arpeggios (the chord tones cycled every 1/30 s),
struck on the beat, held through the intro and bridge; the triangle is the
bass, a 4-bit stepped triangle as on the chip, root-octave eighths; the
noise channel (sample-and-hold noise at a chosen clock, as the chip's
shift register sounds) gives hats and snare, and the kick is a triangle
blip swept down. The pulses are band-limited (polyBLEP) and low-passed at
3.6 kHz, the noise at 4.5-7 kHz; a small room around everything.

Measured (2026-09-30): key C major, centroid median ~2.0 kHz - the
brightest of the camp tracks, as pulse waves are, but the least energy
above 6 kHz of any of them; the bridge sits ~2.5 dB under the rest and B
is the loudest section.

Review, same day. By RMS the four channels looked balanced, but RMS is
the triangle's (it holds ~2/3 of the power, below 250 Hz). A-weighted, the
arpeggio channel sat 14 dB under the lead in A and 5.5 dB under it in the
bridge where it is meant to be in front: the harmony was all but inaudible
on a laptop and the lead was the whole track. Pulse 2 is now ~5 dB up and
the lead ~1 dB down (A-weighted in A: lead -24.7, arp -32.6, bass -29.0,
drums -29.7 dB; bridge lead -29.1, arp -30.6). Lead notes above C6 are
eased 0.3 dB a semitone (E6 -1.2 dB), so the B climax is no longer the
brightest 2-5 kHz passage. The echo was a dotted eighth (312 ms), not the
slap the brief names; it is now one sixteenth (104 ms, ~6 frames).
Re-measured: C major (Krumhansl 0.835, G major 0.738), centroid median
~1.83 kHz (frame-mean 1.90), peak 0.64, rms -16.7 dBFS, seam 0.0000.

Arrangement: intro vamp (no lead) - A - A' - B, the climax, crash on its
first beat - bridge, half-time bass and snare, the arpeggio in front -
fanfare with a snare roll into the intro. 40 bars = 66.67 s, a seamless
loop (see synthkit.py).

    py lesson-template/build/block-camp-music/archive.py [--wav preview.wav]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, lp1, hp1, lp, adsr, pingpong, make_ir, reverb, finish)

BARS = 40
tl = Timeline(bpm=144, bars=BARS)
BAR, S16 = tl.bar, tl.s16
FRAME = 1 / 60

#       name    triangle root  arp tones (octave 4)
C_   = ('C',    48, [60, 64, 67])
AM   = ('Am',   45, [57, 60, 64])
F_   = ('F',    41, [60, 65, 69])
G_   = ('G',    43, [59, 62, 67])
EM   = ('Em',   40, [59, 64, 67])
BB   = ('Bb',   46, [58, 62, 65])
AB   = ('Ab',   44, [60, 63, 68])
BB_C = ('Bb/C', 48, [58, 62, 65])
F_C  = ('F/C',  48, [60, 65, 69])
FG   = (F_, G_)                                 # a bar split in two

SECTIONS = [('intro', 0, [C_, BB_C, F_C, G_]),
            ('A', 4, [C_, AM, F_, G_, C_, AM, FG, C_]),
            ("A'", 12, [C_, AM, F_, G_, C_, EM, FG, C_]),
            ('B', 20, [AB, BB, C_, C_, AB, BB, G_, G_]),
            ('bridge', 28, [F_, G_, EM, AM, F_, G_, AM, G_]),
            ('fanfare', 36, [AB, BB, C_, G_])]
SEC_OF, CH_OF, START = {}, {}, {}
for name, start, chords in SECTIONS:
    START[name] = start
    for k, c in enumerate(chords):
        SEC_OF[start + k], CH_OF[start + k] = name, c
assert sorted(SEC_OF) == list(range(BARS))


def section(b):
    return SEC_OF[b % BARS]


def chord_at(b, step=0):
    c = CH_OF[b % BARS]
    return (c[0] if step < 8 else c[1]) if isinstance(c[0], tuple) else c


# ── the lead, per bar: (sixteenth, midi, length in sixteenths) ─────────────
A1 = [[(0, 67, 2), (2, 72, 2), (4, 76, 4), (8, 79, 6), (14, 76, 2)],        # C
      [(0, 81, 6), (6, 79, 2), (8, 76, 4), (12, 72, 4)],                    # Am
      [(0, 77, 2), (2, 81, 2), (4, 84, 6), (10, 81, 2), (12, 77, 4)],       # F
      [(0, 79, 4), (4, 83, 2), (6, 81, 2), (8, 79, 6), (14, 74, 2)]]        # G
LEAD = {}
for k, bar in enumerate(A1):
    LEAD[4 + k] = LEAD[12 + k] = bar
LEAD.update({
    8:  [(0, 76, 6), (6, 79, 2), (8, 84, 4), (12, 83, 2), (14, 81, 2)],                 # C
    9:  [(0, 76, 4), (4, 72, 2), (6, 76, 2), (8, 81, 8)],                               # Am
    10: [(0, 81, 2), (2, 79, 2), (4, 77, 4), (8, 79, 2), (10, 83, 2), (12, 86, 4)],     # F | G
    11: [(0, 84, 12)],                                                                  # C
    16: [(0, 76, 4), (4, 79, 4), (8, 84, 2), (10, 83, 2), (12, 84, 4)],                 # C
    17: [(0, 83, 6), (6, 79, 2), (8, 76, 6), (14, 79, 2)],                              # Em
    18: [(0, 81, 4), (4, 77, 2), (6, 81, 2), (8, 83, 4), (12, 86, 2), (14, 83, 2)],     # F | G
    19: [(0, 84, 8), (8, 79, 2), (10, 76, 2), (12, 72, 2), (14, 75, 2)],                # C (Eb: into Ab)
    20: [(0, 72, 4), (4, 75, 4), (8, 80, 6), (14, 79, 2)],                              # Ab
    21: [(0, 77, 4), (4, 82, 4), (8, 86, 6), (14, 84, 2)],                              # Bb
    22: [(0, 84, 12), (12, 83, 2), (14, 84, 2)],                                        # C
    23: [(0, 88, 4), (4, 86, 2), (6, 84, 2), (8, 79, 8)],                               # C
    24: [(0, 80, 4), (4, 84, 4), (8, 87, 6), (14, 84, 2)],                              # Ab
    25: [(0, 86, 4), (4, 82, 4), (8, 77, 6), (14, 82, 2)],                              # Bb
    26: [(0, 83, 6), (6, 86, 2), (8, 83, 4), (12, 79, 4)],                              # G
    27: [(0, 86, 4), (4, 83, 4), (8, 79, 8)],                                           # G
    28: [(0, 81, 8), (8, 84, 4), (12, 81, 4)],                                          # F
    29: [(0, 79, 8), (8, 74, 8)],                                                       # G
    30: [(0, 79, 8), (8, 83, 8)],                                                       # Em
    31: [(0, 84, 8), (8, 81, 8)],                                                       # Am
    32: [(0, 81, 4), (4, 84, 4), (8, 77, 8)],                                           # F
    33: [(0, 79, 4), (4, 83, 4), (8, 86, 8)],                                           # G
    34: [(0, 84, 8), (8, 76, 8)],                                                       # Am
    35: [(0, 79, 12), (12, 74, 4)],                                                     # G
    36: [(0, 72, 2), (2, 75, 2), (4, 80, 4), (8, 84, 8)],                               # Ab
    37: [(0, 74, 2), (2, 77, 2), (4, 82, 4), (8, 86, 8)],                               # Bb
    38: [(0, 84, 16)],                                                                  # C
    39: [(0, 86, 2), (2, 83, 2), (4, 79, 2), (6, 74, 2), (8, 71, 4)],                   # G
})


# ── band-limited pulse ──────────────────────────────────────────────────────
def _blep_saw_ph(f, n, ph0):
    dt = np.broadcast_to(np.asarray(f, float), (n,)) / SR
    p = (ph0 + np.cumsum(dt)) % 1.0
    y = 2 * p - 1
    lo = p < dt; t = p[lo] / dt[lo]; y[lo] -= t + t - t * t - 1
    hi = p > 1 - dt; t = (p[hi] - 1) / dt[hi]; y[hi] -= t * t + t + t + 1
    return y


def bpulse(f, n, duty=0.5, ph0=0.0):
    """High for `duty` of each cycle, DC removed; two BLEP saws."""
    return -(_blep_saw_ph(f, n, ph0) - _blep_saw_ph(f, n, (ph0 - duty) % 1.0))


def soft(x, fc=3600):
    return lp1(lp(x, fc, 0.6), 6500)


def stepped_tri(f, n):
    """The chip's 32-step triangle."""
    p = (np.cumsum(np.broadcast_to(np.asarray(f, float), (n,))) / SR) % 1.0
    return (np.floor(np.abs(2 * p - 1) * 16) - 7.5) / 7.5


# ── the channels ────────────────────────────────────────────────────────────
def lead_note(m, length16, duty):
    gate = length16 * S16 * (0.9 if length16 >= 4 else 0.75)
    n = int((gate + 0.12) * SR); t = np.arange(n) / SR
    vib = np.clip((t - 0.16) / 0.12, 0, 1) * np.sin(2 * np.pi * 6.0 * t)
    f = hz(m) * 2 ** (0.22 / 12 * vib)
    x = soft(bpulse(f, n, duty), 2600 if duty < 0.2 else 3600)   # the thin 12.5% duty, darker
    trim = 10 ** (-0.3 * max(0, m - 84) / 20)       # above C6 the 2nd harmonic reaches 2.3-2.6 kHz: ease off
    return x * adsr(n, 0.003, 0.25, 0.7, 0.07, gate) * trim


def arp_note(tones, dur, decay):
    """The chord as one channel: the tones cycled every two frames."""
    n = int((dur + 0.06) * SR); t = np.arange(n) / SR
    k = np.floor(t / (2 * FRAME)).astype(int) % len(tones)
    f = np.array([hz(m) for m in tones])[k]
    x = soft(bpulse(f, n, 0.5))
    return x * adsr(n, 0.002, decay, 0.35, 0.05, dur)


def triangle(m, dur):
    """No volume control on the chip's triangle: only on and off."""
    n = int((dur + 0.01) * SR); t = np.arange(n) / SR
    gate = np.clip(np.minimum(t / 0.002, (dur + 0.01 - t) / 0.006), 0, 1)
    return lp1(stepped_tri(hz(m), n), 6000) * gate


def sh_noise(n, clock, seed):
    """Sample-and-hold noise at `clock` Hz: the NES noise channel's colour."""
    r = np.random.default_rng(seed)
    hold = max(1, int(SR / clock))
    v = r.choice([-1.0, 1.0], size=n // hold + 1)
    return np.repeat(v, hold)[:n]


def kick():
    n = int(0.16 * SR); t = np.arange(n) / SR
    x = stepped_tri(55 + 170 * np.exp(-t / 0.025), n) * np.exp(-t / 0.07)
    x += sh_noise(n, 8000, 41) * np.exp(-t / 0.004) * 0.3
    return lp1(x, 5000)


def snare():
    n = int(0.22 * SR); t = np.arange(n) / SR
    x = sh_noise(n, 9000, 42) * np.exp(-t / 0.06)
    x += stepped_tri(120 + 120 * np.exp(-t / 0.02), n) * np.exp(-t / 0.035) * 0.6
    return lp(x, 4500, 0.6)


def hat(seed, long_=False):
    n = int((0.12 if long_ else 0.04) * SR); t = np.arange(n) / SR
    x = hp1(sh_noise(n, 30000, seed), 3000)
    return lp(x, 7000, 0.6) * np.exp(-t / (0.04 if long_ else 0.012))


def crash():
    n = int(1.2 * SR); t = np.arange(n) / SR
    x = hp1(sh_noise(n, 24000, 43), 2500)
    return lp(x, 7000, 0.6) * np.exp(-t / 0.4) * np.minimum(1, t / 0.002)


KICK, SNARE, CRASH = kick(), snare(), crash()

BASS_DRIVE = [(0, 0), (2, 12), (4, 0), (6, 12), (8, 0), (10, 12), (12, 7), (14, 12)]
BASS_HALF = [(0, 0, 6), (6, 7, 2), (8, 12, 6), (14, 7, 2)]


def render(wav=None):
    p1, p2, trib, noise = (tl.bus() for _ in range(4))
    for b in tl.bars_range():
        t = b * BAR
        bm = b % BARS
        sec = section(b)
        i = bm - START[sec]
        # ── pulse 1: the lead
        if bm in LEAD:
            duty = 0.125 if sec == 'bridge' else 0.25
            for s, m, d in LEAD[bm]:
                p1.add(t + s * S16, lead_note(m, d, duty), pan=-0.12, gain=0.145 if sec == 'B' else 0.133)
        # ── pulse 2: arpeggiated chords, held in the intro and bridge, struck on the beat elsewhere
        if sec in ('intro', 'bridge'):
            for s in (0, 8):
                tones = chord_at(b, s)[2]
                p2.add(t + s * S16, arp_note(tones, 8 * S16 - 0.02, 0.5), pan=0.2,
                       gain=0.12)
        elif sec == 'B':                                   # the climax: struck in eighths
            for s in range(0, 16, 2):
                tones = chord_at(b, s)[2]
                p2.add(t + s * S16, arp_note(tones, 1.6 * S16, 0.08), pan=0.2, gain=0.14)
        else:
            for s in (0, 4, 8, 12):
                tones = chord_at(b, s)[2]
                p2.add(t + s * S16, arp_note(tones, 3 * S16, 0.12), pan=0.2, gain=0.125)
        # ── triangle bass
        if sec == 'bridge':
            for s, iv, d in BASS_HALF:
                trib.add(t + s * S16, triangle(chord_at(b, s)[1] + iv, d * S16 * 0.9), gain=0.21)
        else:
            for s, iv in BASS_DRIVE:
                trib.add(t + s * S16, triangle(chord_at(b, s)[1] + iv, 2 * S16 * 0.8), gain=0.30)
        # ── noise channel and triangle kick
        if sec == 'bridge':
            kicks, snares = (0, 10), (12,)
        elif sec == 'intro':
            kicks, snares = (0, 8), ((4, 12) if i >= 2 else ())
        else:
            kicks, snares = ((0, 8, 10) if i % 2 else (0, 8)), (4, 12)
        for s in kicks:
            noise.add(t + s * S16, KICK, gain=0.30 if sec == 'bridge' else 0.40)
        for s in snares:
            noise.add(t + s * S16, SNARE, gain=0.26)
        hat16 = sec in ('B', 'fanfare', "A'")
        for s in range(16):
            if s % 2 and not hat16:
                continue
            open_ = s in (6, 14) and sec == 'B'
            noise.add(t + s * S16, hat(bm * 16 + s, open_), pan=0.25,
                      gain=(0.04 if open_ else 0.036 if s % 4 == 2 else 0.024 if s % 2 == 0 else 0.016))
        if bm in (4, 20):
            noise.add(t, CRASH, pan=-0.2, gain=0.06)
        if bm == 3:                                         # intro fill into A
            for s in (13, 14, 15):
                noise.add(t + s * S16, SNARE, gain=0.16)
        if bm == 19:                                        # into B
            for s in (12, 14, 15):
                noise.add(t + s * S16, SNARE, gain=0.18)
        if bm == 39:                                        # fanfare roll into the intro
            for s in range(8, 16):
                noise.add(t + s * S16, SNARE, gain=0.08 + 0.02 * (s - 8))

    p1x = p1.x + pingpong(p1.x, S16, 0.25, 3, 3000) * 0.5      # the slap: one sixteenth, ~6 frames
    wet = reverb(p1x * 0.25 + p2.x * 0.3 + noise.x * 0.08, make_ir(0.9, dark=4000))
    mix = p1x + p2.x + trib.x + noise.x + wet * 0.35
    return finish(tl, mix, 'passive-past-simple', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
