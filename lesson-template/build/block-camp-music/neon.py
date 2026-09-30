#!/usr/bin/env python3
"""Block Camp soundtrack "Neon" (Present Simple): upbeat 80s synthwave.

Innes, 2026-09-30: "add a soundtrack to present simple that sounds like the
one in the kung fury trailer (80s synth upbeat)". An original piece in that
idiom, nothing copied: A minor, 120 BPM, i-VI-III-VII (Am F C G), driving
octave eighths in the bass, a drum machine with the big gated-reverb snare,
brassy detuned-saw chords pumping against the kick, a sixteenth arpeggio with
echo, and a heroic saw lead in two phrases. 32 bars = 64 s, a seamless loop
(see synthkit.py).

    py lesson-template/build/block-camp-music/neon.py [--wav preview.wav]
"""
import sys
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, swept_lp, saw, supersaw, pulse,
                      adsr, perc, pingpong, make_ir, reverb, chorus, finish)

tl = Timeline(bpm=120, bars=32)
BAR, S16 = tl.bar, tl.s16

#            root  voicing                 (one chord per 2 bars)
CHORDS = [(33, [57, 60, 64, 69]),          # Am
          (29, [57, 60, 65, 69]),          # F  (A C F A: the top stays put)
          (36, [55, 60, 64, 67]),          # C
          (31, [55, 59, 62, 67])]          # G


def chord_at(b):
    return CHORDS[(b % 8) // 2]


def part(name, b):
    b %= 32; cyc, i = b // 8, b % 8
    return {
        'kick':   True,
        'snare':  cyc in (1, 2) or (cyc == 3 and i >= 4),
        'hats':   True,
        'bass':   not (cyc == 3 and i < 4),
        'chords': cyc in (1, 2, 3),
        'arp':    cyc in (0, 2, 3),
        'lead':   cyc in (1, 2),
        'toms':   cyc in (1, 2) and i == 7,
        'riser':  cyc == 3 and i >= 6,
    }[name]


# ── drums ───────────────────────────────────────────────────────────────────
def kick():
    n = int(0.45 * SR); t = np.arange(n) / SR
    f = 46 + 110 * np.exp(-t / 0.03)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.22)
    click = hp1(np.random.default_rng(1).standard_normal(n), 2000) * np.exp(-t / 0.004) * 0.35
    return np.tanh(1.6 * (body + click)) / np.tanh(1.6)


IR_GATE = make_ir(1.6, dark=6000, seed=3, pre=0.004)


def gated_snare():
    """The 80s snare: a crack into a big room, the room cut dead at 0.3 s."""
    n = int(0.6 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(2).standard_normal(n)
    noise = bp(z, 2600, 0.7) * np.exp(-t / 0.09)
    tone = np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.06) + 0.5 * np.sin(2 * np.pi * 330 * t) * np.exp(-t / 0.04)
    dry = noise * 1.2 + tone * 0.8
    wet = reverb(np.stack([dry, dry], 1), IR_GATE)
    gate = np.where(t < 0.26, 1.0, np.clip(1 - (t - 0.26) / 0.035, 0, 1))
    return np.stack([dry, dry], 1) * 0.8 + wet * gate[:, None] * 1.4


def hat(open_=False, seed=0):
    n = int((0.32 if open_ else 0.07) * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return hp1(hp1(z, 7000), 7000) * perc(n, 0.001, 0.12 if open_ else 0.018)


def tom(f0):
    n = int(0.4 * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.6 * np.exp(-t / 0.05))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)


SNARE = gated_snare()


# ── synths ──────────────────────────────────────────────────────────────────
def bass_note(m, dur):
    n = int((dur + 0.08) * SR)
    x = 0.6 * saw(hz(m), n) + 0.4 * pulse(hz(m) * 1.004, n, 0.5)
    x = swept_lp(x, 1400, 260, q=1.4)
    x += 0.5 * np.sin(2 * np.pi * hz(m) * np.arange(n) / SR)       # sub
    return x * adsr(n, 0.003, 0.06, 0.75, 0.05, dur)


def brass(m, dur, seed):
    n = int((dur + 0.5) * SR)
    x = supersaw(hz(m), n, seed=seed)
    x = swept_lp(x, 700, 3600, q=0.9) if dur > 0.6 else swept_lp(x, 3800, 900, q=0.9)
    return x * adsr(n, 0.02, 0.25, 0.7, 0.35, dur)


def arp_note(m):
    n = int(0.25 * SR)
    x = pulse(hz(m), n, 0.3)
    x = lp1(lp1(x, 4200), 4200)
    return x * perc(n, 0.002, 0.07)


# melody: (midi, sixteenths), 32 per chord, 128 per 8-bar phrase
LEAD_A = [(64, 4), (69, 4), (71, 4), (72, 4), (71, 8), (69, 4), (64, 4),
          (65, 8), (69, 4), (72, 4), (71, 4), (69, 4), (67, 8),
          (67, 4), (64, 4), (67, 4), (72, 4), (74, 12), (72, 4),
          (71, 8), (74, 4), (71, 4), (67, 8), (64, 8)]
LEAD_B = [(69, 8), (72, 4), (76, 4), (74, 4), (72, 4), (71, 4), (69, 4),
          (72, 12), (69, 4), (65, 8), (69, 8),
          (76, 8), (74, 4), (72, 4), (67, 8), (72, 8),
          (74, 8), (71, 4), (67, 4), (74, 16)]
assert sum(d for _, d in LEAD_A) == 128 and sum(d for _, d in LEAD_B) == 128


def lead_phrase(mel):
    n = int((8 * BAR + 1.0) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n)
    pos = 0; last = hz(mel[0][0])
    for m, d in mel:
        a, b = int(pos * S16 * SR), int((pos + d) * S16 * SR)
        f[a:b] = hz(m); last = hz(m)
        tt = np.arange(b - a) / SR
        g[a:b] = np.minimum(1, tt / 0.01) * (0.85 + 0.15 * np.exp(-tt / 0.15))
        g[max(b - int(0.025 * SR), a):b] *= 0.7
        vib[a:b] = np.clip((tt - 0.25) / 0.4, 0, 1)
        pos += d
    f[pos * int(S16 * SR):] = last
    g[int(pos * S16 * SR):] = 0
    g = lp1(g, 60)
    a = np.exp(-1 / (0.03 * SR))
    from scipy.signal import lfilter
    fl = lfilter([1 - a], [1, -a], f); fl[:int(0.01 * SR)] = f[0]
    t = np.arange(n) / SR
    fl = fl * 2 ** (0.18 / 12 * vib * np.sin(2 * np.pi * 5.8 * t))
    x = sum(2 * ((np.cumsum(fl * 2 ** (c / 1200)) / SR + k * 0.31) % 1) - 1 for k, c in enumerate((-7, 0, 7))) / 3
    x = lp1(lp1(x, 5200), 5200) * g
    return x


def render(wav=None):
    drums, bass, chords, arp, lead, fx, send = (tl.bus() for _ in range(7))
    kicks = []
    for b in tl.bars_range():
        t = b * BAR
        root, voicing = chord_at(b)
        cyc, i = (b % 32) // 8, b % 8
        # drums
        if part('kick', b):
            steps = (0, 4, 8, 12) if cyc != 0 or i >= 2 else (0, 8)
            for s in steps:
                drums.add(t + s * S16, kick(), gain=0.55); kicks.append(t + s * S16)
        if part('snare', b):
            for s in (4, 12):
                drums.add(t + s * S16, SNARE, gain=0.32)
        if part('hats', b):
            for s in range(16):
                if cyc == 0 and i < 4 and s % 2:
                    continue
                op = cyc == 2 and s % 4 == 2
                drums.add(t + s * S16, hat(op, (b % 32) * 16 + s), pan=0.3,
                          gain=(0.10 if op else 0.075 if s % 4 == 2 else 0.045))
        if part('toms', b):
            for k, (s, f0) in enumerate(((12, 190), (13, 160), (14, 130), (15, 105))):
                drums.add(t + s * S16, tom(f0), pan=0.5 - k * 0.33, gain=0.30)
        # bass: driving eighths, the octave on the offbeat
        if part('bass', b):
            for s in range(8):
                m = root + 12 if s % 2 else root
                bass.add(t + s * 2 * S16, bass_note(m, 2 * S16 * 0.8), gain=0.30)
        # brass: long chords in cycle 1, offbeat stabs in 2, swells in 3
        if part('chords', b) and b % 2 == 0:
            if cyc == 1 or cyc == 3:
                for k, m in enumerate(voicing):
                    chords.add(t, brass(m, 2 * BAR - 0.05, k), pan=(-0.6, -0.2, 0.2, 0.6)[k], gain=0.13)
            else:
                for bb in (0, 1):
                    for s in (2, 6, 10, 14):
                        for k, m in enumerate(voicing):
                            chords.add(t + bb * BAR + s * S16, brass(m, 0.16, k),
                                       pan=(-0.6, -0.2, 0.2, 0.6)[k], gain=0.12)
        # arpeggio: up through the chord and an octave, sixteenths
        if part('arp', b):
            tones = voicing + [voicing[1] + 12, voicing[2] + 12]
            order = [0, 1, 2, 3, 4, 5, 4, 3, 1, 2, 3, 4, 5, 4, 2, 3]
            for s, k in enumerate(order):
                arp.add(t + s * S16, arp_note(tones[k] + 12), pan=(-0.4 if s % 2 else 0.4),
                        gain=0.05 + (0.02 if s % 4 == 0 else 0))
        # riser into the loop's top: noise swelling up through a band
        if part('riser', b) and i == 6:
            n = int(2 * BAR * SR); u = np.arange(n) / n
            z = rng('riser', b % 32).standard_normal(n)
            from synthkit import bp as _bp
            y = np.zeros(n)
            for c in range(16):
                a0, a1 = c * n // 16, (c + 1) * n // 16
                y[a0:a1] = _bp(z[a0:a1], 400 * (12 ** (c / 15)), 1.2)
            fx.add(t, y * u ** 2.2, gain=0.20)
    # lead
    for lap in (-1, 0, 1):
        for cyc, mel in ((1, LEAD_A), (2, LEAD_B)):
            t0 = lap * tl.loop + cyc * 8 * BAR
            if -tl.pre * BAR - 8 * BAR < t0 < (tl.bars + tl.post) * BAR:
                x = lead_phrase(mel)
                lead.add(t0, x, pan=0.0, gain=0.20)

    # side-chain pump: everything but the drums ducks under each kick
    tt = np.arange(tl.n) / SR - tl.t0
    pump = np.ones(tl.n)
    for k in kicks:
        i0 = tl.smp(k); i1 = min(tl.n, i0 + int(0.4 * SR))
        if i1 > max(i0, 0):
            j0 = max(i0, 0)
            pump[j0:i1] = np.minimum(pump[j0:i1], 1 - 0.45 * np.exp(-(tt[j0:i1] - k) / 0.11))
    pump = pump[:, None]

    chordsx = chorus(chords.x, tl.loop / 8, t0=tl.t0)
    arpx = arp.x + pingpong(arp.x, 3 * S16, 0.45, 6, 3500)
    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.32, 5, 3000) * 0.7
    ir = make_ir(2.4, dark=4500)
    wet = reverb(chordsx * 0.35 + arpx * 0.3 + leadx * 0.3 + fx.x * 0.5, ir)
    mix = drums.x + (bass.x + chordsx + arpx + wet * 0.5) * pump + leadx + fx.x
    return finish(tl, mix, 'present-simple', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
