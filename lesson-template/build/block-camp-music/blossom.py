#!/usr/bin/env python3
"""Block Camp soundtrack "Blossom" (Present Continuous): 80s city pop.

Innes, 2026-09-30, asked for a soundtrack for present continuous with no
style named. Its world is pink cherry blossom, so: bright Japanese 80s city
pop, lighter than Neon (Present Simple) and Lakeside (Past Simple) so the
three camps sound different. Original: F major, 96 BPM, Fmaj9 Dm9 Bbmaj9
C11-C9; a DX7-style FM electric piano comping on the offbeats, a bouncing
syncopated bass, soft drums with a shaker, FM bell sparkles on the F major
pentatonic, and a round pentatonic lead in two phrases. 32 bars = 80 s, a
seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/blossom.py [--wav preview.wav]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, bp, perc, adsr, pingpong, make_ir,
                      reverb, chorus, finish)

tl = Timeline(bpm=96, bars=32)
BAR, S16 = tl.bar, tl.s16

CHORDS = [(41, [53, 57, 60, 64, 67]),      # Fmaj9
          (38, [50, 53, 57, 60, 64]),      # Dm9
          (34, [46, 50, 53, 57, 60]),      # Bbmaj9 (no 3rd doubling)
          (36, [48, 53, 55, 58, 62])]      # C11
C9 = [48, 52, 55, 58, 62]                  # bar 7 of each cycle: the 11 resolves


def chord_at(b):
    root, v = CHORDS[(b % 8) // 2]
    return root, (C9 if b % 8 == 7 else v)


def part(name, b):
    b %= 32; cyc, i = b // 8, b % 8
    return {
        'ep':     True,
        'bells':  cyc in (0, 3) or i % 4 == 3,
        'bass':   cyc in (1, 2, 3),
        'drums':  cyc in (1, 2) or (cyc == 3 and i < 6),
        'lead':   cyc in (2, 3),
        'shaker': cyc in (0, 1, 2) or i < 6,
    }[name]


# ── instruments ─────────────────────────────────────────────────────────────
def fm_ep(m, dur):
    """Two-operator FM electric piano: a bright tine at the attack that
    mellows as the modulation index decays, and a long soft body."""
    n = int((dur + 0.6) * SR); t = np.arange(n) / SR
    f = hz(m)
    idx = 0.25 + 2.3 * np.exp(-t / 0.18)
    mod = np.sin(2 * np.pi * f * t)
    body = np.sin(2 * np.pi * f * t + idx * mod)
    tine = np.sin(2 * np.pi * f * 7.0 * t) * np.exp(-t / 0.03) * 0.25
    x = (body + tine) * adsr(n, 0.002, 0.9, 0.35, 0.3, dur) * np.exp(-t / 2.5)
    return x


def fm_bell(m):
    n = int(2.2 * SR); t = np.arange(n) / SR
    f = hz(m)
    idx = 3.2 * np.exp(-t / 0.5)
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * 3.5 * t))
    return x * perc(n, 0.001, 0.7)


def bass_note(m, dur):
    n = int((dur + 0.06) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    pluck = np.exp(-t / 0.04) * 0.4 * np.sin(2 * np.pi * f * 5 * t)
    return (x + pluck) * adsr(n, 0.004, 0.12, 0.7, 0.05, dur)


def kick():
    n = int(0.3 * SR); t = np.arange(n) / SR
    f = 50 + 60 * np.exp(-t / 0.03)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def snare():
    n = int(0.3 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(5).standard_normal(n)
    return bp(z, 3200, 0.8) * np.exp(-t / 0.07) * 1.1 + np.sin(2 * np.pi * 210 * t) * np.exp(-t / 0.05) * 0.6


def rim():
    n = int(0.06 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1750 * t) + 0.5 * np.sin(2 * np.pi * 2600 * t)) * np.exp(-t / 0.012)


def shaker(seed):
    n = int(0.08 * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return hp1(hp1(z, 6000), 6000) * perc(n, 0.008, 0.025)


# pentatonic lead: (midi, sixteenths), 32 per chord, 128 per phrase
LEAD_A = [(69, 6), (72, 2), (74, 8), (72, 4), (69, 4), (67, 8),
          (65, 4), (67, 4), (69, 4), (72, 4), (74, 12), (72, 4),
          (74, 6), (77, 2), (74, 8), (72, 8), (69, 8),
          (67, 8), (69, 4), (72, 4), (69, 4), (67, 4), (65, 8)]
LEAD_B = [(72, 4), (74, 4), (77, 8), (79, 4), (77, 4), (74, 8),
          (72, 8), (69, 4), (72, 4), (74, 16),
          (77, 6), (79, 2), (77, 8), (74, 8), (72, 8),
          (74, 4), (72, 4), (69, 8), (67, 16)]
assert sum(d for _, d in LEAD_A) == 128 and sum(d for _, d in LEAD_B) == 128


def lead_phrase(mel):
    """A round, flute-like voice (sine plus a little 2nd and 3rd), short
    glides, gentle vibrato, detached notes."""
    n = int((8 * BAR + 1.0) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n)
    pos = 0; last = hz(mel[0][0])
    for m, d in mel:
        a, b = int(pos * S16 * SR), int((pos + d) * S16 * SR)
        f[a:b] = hz(m); last = hz(m)
        tt = np.arange(b - a) / SR
        g[a:b] = np.minimum(1, tt / 0.025) * (0.8 + 0.2 * np.exp(-tt / 0.2))
        g[max(b - int(0.05 * SR), a):b] *= 0.25
        vib[a:b] = np.clip((tt - 0.3) / 0.5, 0, 1)
        pos += d
    f[pos * int(S16 * SR):] = last
    g[int(pos * S16 * SR):] = 0
    g = lp1(g, 40)
    a = np.exp(-1 / (0.02 * SR))
    fl = lfilter([1 - a], [1, -a], f); fl[:int(0.01 * SR)] = f[0]
    t = np.arange(n) / SR
    fl = fl * 2 ** (0.15 / 12 * vib * np.sin(2 * np.pi * 5.2 * t))
    ph = 2 * np.pi * np.cumsum(fl) / SR
    breath = lp1(np.random.default_rng(9).standard_normal(n), 3000) * 0.04
    return (np.sin(ph) + 0.22 * np.sin(2 * ph) + 0.08 * np.sin(3 * ph) + breath) * g


def render(wav=None):
    ep, bass, drums, bells, lead = (tl.bus() for _ in range(5))
    for b in tl.bars_range():
        t = b * BAR
        root, voicing = chord_at(b)
        cyc, i = (b % 32) // 8, b % 8
        # electric piano: offbeat comping, a pushed chord into the next bar
        if part('ep', b):
            hits = [(0, 5), (6, 3), (10, 4), (14, 2)] if cyc else [(0, 12)]
            for s, d in hits:
                for k, m in enumerate(voicing):
                    ep.add(t + s * S16 + k * 0.004, fm_ep(m, d * S16), pan=-0.5 + k * 0.25,
                           gain=0.075 if s else 0.09)
        # bass: syncopated, root - octave - fifth
        if part('bass', b):
            for s, iv, d in ((0, 0, 3), (3, 12, 1), (6, 7, 2), (8, 0, 2), (11, 12, 1), (14, 7, 2)):
                bass.add(t + s * S16, bass_note(root + iv, d * S16 * 0.85), gain=0.36)
        # drums
        if part('drums', b):
            for s in (0, 7, 10):
                drums.add(t + s * S16, kick(), gain=0.40)
            for s in (4, 12):
                drums.add(t + s * S16, snare(), pan=0.05, gain=0.20)
            drums.add(t + 15 * S16, rim(), pan=0.4, gain=0.05)
        if part('shaker', b):
            for s in range(16):
                drums.add(t + s * S16, shaker((b % 32) * 16 + s), pan=-0.35,
                          gain=0.045 if s % 2 else 0.028)
        # bells: a falling pentatonic figure across the bar
        if part('bells', b):
            r = rng('bells', b % 32)
            pent = [77, 79, 81, 84, 86, 89]
            for s in (0, 3, 6, 10):
                m = pent[int(r.integers(0, len(pent)))]
                bells.add(t + s * S16, fm_bell(m), pan=float(r.uniform(-0.6, 0.6)), gain=0.045)
    for lap in (-1, 0, 1):
        for cyc, mel in ((2, LEAD_A), (3, LEAD_B)):
            t0 = lap * tl.loop + cyc * 8 * BAR
            if -tl.pre * BAR - 8 * BAR < t0 < (tl.bars + tl.post) * BAR:
                lead.add(t0, lead_phrase(mel), pan=0.1, gain=0.16)

    epx = chorus(ep.x, tl.loop / 8, depth_ms=1.8, base_ms=6.0, mix=0.6, t0=tl.t0)
    bellx = bells.x + pingpong(bells.x, 3 * S16, 0.45, 6, 5000)
    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.25, 3, 3500) * 0.6
    wet = reverb(epx * 0.3 + bellx * 0.5 + leadx * 0.35 + drums.x * 0.12, make_ir(2.2, dark=5000))
    mix = epx + bass.x + drums.x + bellx + leadx + wet * 0.45
    return finish(tl, mix, 'present-continuous', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
