#!/usr/bin/env python3
"""Block Camp soundtrack "Night Drive" (Passive Going To): Miami-TV synth.

The brief, 2026-09-30: the Passive Going To station in the style of Jan
Hammer's mid-80s TV scores - big gated-reverb drums, a sultry, expressive
synth lead with pitch bends and vibrato, warm Prophet/Fairlight-style
polysynth chords, a pulsing eighth-note bass, atmospheric pads; minor,
cool and nocturnal, not aggressive. An original piece in that idiom: the
melody, changes and bass are new; nothing is copied.

B minor, 106.67 BPM (320/3: a sixteenth is exactly 6750 samples, so the
loop is a whole number of samples), 4/4. Chords two bars each, a 16-bar
form played twice:
    A  Bm9  | Gmaj9 | Em9 | Aadd9
    B  Gmaj9 | Aadd9 | Em9 | F#7sus4 F#7    (the F#7 turns back to Bm9)
Instruments: a polysynth (two band-limited saws and a pulse per voice,
filter opening over each chord, chorus; rootless where the bass has the
root, and a short release so the F#7 does not smear over the Bm9), a
"vocal" pad (saws through three formants; it holds C# E F# across the
F#7sus4 and the F#7), a pulsing eighth-note bass with a per-note filter
envelope, gated-reverb drums (kick, snare into a big room cut at 0.32 s,
Simmons-style toms, soft hats), soft noise swells into the sections, and
an additive lead: legato glides, bends up into notes (a half or whole
tone, guitar-style), delayed vibrato, a fall-off at the end of a phrase,
a dotted-eighth echo and a long reverb.
Pitched drums are tuned into the key: the kick settles on B1, the snare's
shell modes are F#3 and D4, and the toms fall to F#3 E3 C#3 B2. (Tuned at
52 Hz, G#1, the kick's saturated body put G# and D# under every G chord;
toms tuned G E C# A# put an A#2 against the A2 bass in the bar-23 fill.)
check_melody() asserts at render time that every lead note is a chord tone
and that no held note rubs a semitone against a voice of the chord.

Arrangement (bar mod 32):
    0-3    pad, polysynth, bass pulse; a tom fill into bar 4
    4-7    + drums
    8-15   lead phrase 1 (B)
    16-23  lead phrase 2 (A), higher; open hats
    24-27  lead phrase 3 (B), a short answer ending in a fall
    28-29  drums thin to kick and hats
    30-31  drums out, a swell back into the top
Tom fills in bars 3, 15 and 23; noise swells in bars 7, 15, 23 and 31.

32 bars = 72 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/nightdrive.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, swept_lp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

NAME = 'passive-going-to'
BARS = 32
tl = Timeline(bpm=320 / 3, bars=BARS)
BAR, BEAT, S16 = tl.bar, tl.beat, tl.s16

#          name       bass  polysynth voicing
BM9 = ('Bm9', 47, [47, 57, 62, 66, 73])           # B A D F# C#
GM9 = ('Gmaj9', 43, [43, 54, 59, 62, 69])         # G F# B D A
EM9 = ('Em9', 40, [52, 55, 59, 62, 66])           # E G B D F#
AA9 = ('Aadd9', 45, [45, 57, 61, 64, 71])         # A A C# E B
FS4 = ('F#7sus4', 42, [54, 59, 61, 64, 66])       # F# B C# E F#
FS7 = ('F#7', 42, [54, 58, 61, 64, 66])           # F# A# C# E F#
FORM = [BM9, GM9, EM9, AA9, GM9, AA9, EM9, FS4]    # one per 2 bars, 16 bars
assert FS4[2][2:] == FS7[2][2:]                     # the pad (top three voices) holds across bars 14-15


def chord_at(b):
    b %= 16
    return FS7 if b == 15 else FORM[b // 2]


def chord_tones(b):
    _, root, v = chord_at(b)
    return {root % 12} | {m % 12 for m in v}


def part(name, b):
    b %= BARS
    return {
        'drums': 4 <= b < 30,
        'snare': 4 <= b < 28,
        'openhat': 16 <= b < 24,
        'fill': b in (3, 15, 23),
        'swell': b in (7, 15, 23, 31),
    }[name]


# ── band-limited oscillators ────────────────────────────────────────────────
def _blep(p, dt):
    y = np.zeros_like(p)
    a = p < dt; t = p[a] / dt[a]; y[a] = 2 * t - t * t - 1
    b = p > 1 - dt; t = (p[b] - 1) / dt[b]; y[b] = t * t + 2 * t + 1
    return y


def blsaw(f, n, ph=0.0):
    dt = np.broadcast_to(np.asarray(f, float) / SR, (n,)).copy()
    p = (ph + np.cumsum(dt)) % 1.0
    return 2 * p - 1 - _blep(p, dt)


def blpulse(f, n, duty=0.5, ph=0.0):
    dt = np.broadcast_to(np.asarray(f, float) / SR, (n,)).copy()
    p = (ph + np.cumsum(dt)) % 1.0
    q = (p + 1 - duty) % 1.0
    return (2 * p - 1 - _blep(p, dt)) - (2 * q - 1 - _blep(q, dt))


# ── drums ───────────────────────────────────────────────────────────────────
ROOM = make_ir(1.9, dark=4200, seed=7, pre=0.006)


def gated(dry, hold, rel=0.04, wet_gain=1.2):
    n = len(dry); t = np.arange(n) / SR
    wet = reverb(np.stack([dry, dry], 1), ROOM)
    gate = np.clip(1 - (t - hold) / rel, 0, 1)
    return np.stack([dry, dry], 1) * 0.8 + wet * gate[:, None] * wet_gain


def kick():
    n = int(0.55 * SR); t = np.arange(n) / SR
    f = hz(35) + 85 * np.exp(-t / 0.035)                            # settles on B1, the tonic
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)
    click = lp1(hp1(np.random.default_rng(31).standard_normal(n), 1500), 5000) * np.exp(-t / 0.005) * 0.3
    return gated(np.tanh(1.4 * (body + click)) / np.tanh(1.4), 0.12, 0.03, 0.35)


def snare():
    n = int(0.75 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(32).standard_normal(n)
    noise = lp(bp(z, 2100, 0.6), 5500) * np.exp(-t / 0.1)
    # shell modes a ratio of 1.59 apart, tuned to F#3 and D4 so the ringing room stays in the key
    tone = np.sin(2 * np.pi * hz(54) * t) * np.exp(-t / 0.07) * 0.8 + np.sin(2 * np.pi * hz(62) * t) * np.exp(-t / 0.04) * 0.3
    return gated(noise * 1.2 + tone, 0.32, 0.045, 1.5)


def tom(f0):
    n = int(0.7 * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.5 * np.exp(-t / 0.08))                        # the Simmons pitch drop
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.22)
    x += lp1(np.random.default_rng(int(f0)).standard_normal(n), 3000) * np.exp(-t / 0.02) * 0.15
    return gated(x, 0.3, 0.05, 1.0)


def hat(seed, open_=False):
    n = int((0.35 if open_ else 0.07) * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    x = lp1(hp1(hp1(z, 6500), 6500), 11000)
    return x * perc(n, 0.001, 0.13 if open_ else 0.018)


KICK, SNARE = kick(), snare()


def panned(x, pan):
    """Place a stereo one-shot: an equal-power balance, like Bus.add's pan."""
    return x * np.array([np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)]) * np.sqrt(2)
TOMS = [tom(hz(m)) for m in (54, 52, 49, 47)]                   # F#3 E3 C#3 B2: fine over G, A and F#


# ── synths ──────────────────────────────────────────────────────────────────
def bass_note(m, dur, acc, bright):
    n = int((dur + 0.06) * SR); t = np.arange(n) / SR
    x = 0.65 * blsaw(hz(m), n) + 0.35 * blsaw(hz(m) * 1.004, n, 0.37)
    x = swept_lp(x, bright * (0.8 + 0.5 * acc), 240, q=1.1)
    x += 0.4 * np.sin(2 * np.pi * hz(m) * t)
    return x * adsr(n, 0.003, 0.09, 0.62, 0.04, dur) * (0.7 + 0.3 * acc)


def poly(m, dur, seed):
    # a short release: with 1.1 s the old chord was still louder than the new one 0.25 s after
    # the change, so the F#7 -> Bm9 cadence smeared A#3 over A3 on every return to the top
    n = int((dur + 0.6) * SR)
    r = rng('poly', seed, m)
    f = hz(m)
    x = (0.45 * blsaw(f * 2 ** (-6 / 1200), n, r.random()) + 0.45 * blsaw(f * 2 ** (6 / 1200), n, r.random())
         + 0.25 * blpulse(f, n, 0.42, r.random()))
    x = swept_lp(x, 700, 2600, q=0.8)
    return x * adsr(n, 0.18, 0.8, 0.8, 0.45, dur)


def vox(m, dur, seed):
    """A choir-ish pad: saws through three formants of an open 'ah'."""
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR
    r = rng('vox', seed, m)
    f = hz(m) * 2 ** (0.08 / 12 * np.sin(2 * np.pi * 4.6 * t + r.random() * 6))
    x = sum(blsaw(f * 2 ** (c / 1200), n, r.random()) for c in (-7, 0, 7)) / 3
    y = bp(x, 720, 2.2) + 0.7 * bp(x, 1150, 3.0) + 0.25 * bp(x, 2600, 4.0)
    return y * adsr(n, 1.1, 1.0, 0.85, 1.0, dur)


def swell(dur, seed):
    n = int(dur * SR); u = np.arange(n) / n
    z = rng('swell', seed).standard_normal(n)
    y = np.zeros(n)
    for c in range(12):
        a0, a1 = c * n // 12, (c + 1) * n // 12
        y[a0:a1] = bp(z[a0:a1], 350 * (8 ** (c / 11)), 1.4)
    return lp1(y, 5000) * u ** 2.5 * (1 - np.clip((u - 0.97) / 0.03, 0, 1))


# ── the lead: (midi or 0 for rest, sixteenths, bend up from this many semitones below)
LEAD_1 = [(0, 8, 0), (71, 4, 0), (74, 12, 2), (71, 4, 0), (69, 4, 0),       # Gmaj9
          (73, 12, 1), (71, 4, 0), (69, 4, 0), (64, 4, 0), (69, 8, 0),       # Aadd9
          (71, 16, 2), (74, 4, 0), (71, 4, 0), (66, 8, 0),                  # Em9
          (73, 8, 0), (71, 8, 0), (70, 12, 0), (0, 4, 0)]                   # F#7sus4, F#7
LEAD_2 = [(71, 8, 2), (74, 4, 0), (78, 12, 1), (73, 4, 0), (74, 4, 0),      # Bm9
          (71, 12, 0), (69, 4, 0), (71, 4, 0), (74, 12, 2),                 # Gmaj9
          (76, 12, 2), (74, 4, 0), (71, 8, 0), (66, 8, 0),                  # Em9
          (69, 16, 0), (71, 4, 0), (73, 12, 0)]                             # Aadd9
LEAD_3 = [(74, 8, 0), (71, 4, 0), (69, 4, 0), (66, 16, 2),                  # Gmaj9
          (69, 8, 2), (71, 4, 0), (73, 20, 0)]                              # Aadd9
LEADS = ((8, LEAD_1, False), (16, LEAD_2, False), (24, LEAD_3, True))       # (bar, phrase, fall at the end)
assert [sum(d for _, d, _ in p) for _, p, _ in LEADS] == [128, 128, 64]


def check_melody(mel, bar0, label):
    bad, pos = [], 0
    for m, d, _ in mel:
        if m and (d >= 4 or pos % 4 == 0):
            b = bar0 + pos // 16
            if m % 12 not in chord_tones(b):
                bad.append(f'{label}: midi {m} at bar {b} over {chord_at(b)[0]}')
            # a held note must not sit a semitone from a voice of the chord (poly or pad) in the same octave
            if d >= 8 and any(abs(m - v) == 1 for v in chord_at(b)[2]):
                bad.append(f'{label}: midi {m} at bar {b} rubs a semitone against the {chord_at(b)[0]} voicing')
        pos += d
    return bad


def lead_phrase(mel, fall):
    total = sum(d for _, d, _ in mel)
    n = int((total * S16 + 1.2) * SR)
    semi = np.zeros(n); g = np.zeros(n); vib = np.zeros(n); bright = np.zeros(n)
    pos = 0; last = next(m for m, _, _ in mel if m)
    for m, d, bend in mel:
        a, b = int(pos * S16 * SR), int((pos + d) * S16 * SR)
        tt = np.arange(b - a) / SR
        if m:
            semi[a:b] = m; last = m
            if bend:
                semi[a:b] -= bend * (1 - np.clip(tt / 0.17, 0, 1)) ** 2   # bend up and settle
            g[a:b] = np.minimum(1, tt / 0.012) * (0.86 + 0.14 * np.exp(-tt / 0.2))
            vib[a:b] = np.clip((tt - 0.32) / 0.45, 0, 1) * min(1.0, d / 8)
            bright[a:b] = np.exp(-tt / 0.3)
        else:
            semi[a:b] = last
        pos += d
    e = int(pos * S16 * SR)
    semi[e:] = last
    if fall:                                                                  # the fall-off
        k = int(0.35 * SR); w = np.linspace(0, 1, k) ** 2
        semi[e - k:e] -= 2.5 * w; g[e - k:e] *= 1 - w
    g[e:] = 0
    g = lp1(g, 45)
    c = np.exp(-1 / (0.028 * SR))                                             # portamento
    semi = lfilter([1 - c], [1, -c], semi - semi[0]) + semi[0]
    t = np.arange(n) / SR
    semi = semi + 0.32 * vib * np.sin(2 * np.pi * 5.4 * t)
    fl = hz(semi)
    ph = 2 * np.pi * np.cumsum(fl) / SR
    fc = 1500 + 1500 * bright
    x = np.zeros(n)
    for h in range(1, 17):
        fk = h * fl
        amp = (1 / h) * (1.0 if h % 2 else 0.6)                # saw leaning square: a little hollow
        resp = 1 / np.sqrt(1 + (fk / fc) ** 4) * (1 + 0.5 * np.exp(-0.5 * ((fk - fc) / (0.25 * fc)) ** 2))
        x += amp * resp * np.sin(h * ph) * (fk < 9000)
    return x * g


def render(wav=None, stems=False):
    bad = []
    for bar0, mel, _ in LEADS:
        bad += check_melody(mel, bar0, f'lead@{bar0}')
    assert not bad, bad

    drums, bass, polys, pads, lead, fx = (tl.bus() for _ in range(6))
    for b in tl.bars_range():
        t = b * BAR
        name, root, voicing = chord_at(b)
        bb = b % BARS
        r = rng('bar', bb)
        # polysynth and pad: a chord every two bars (F#7sus4 and F#7 a bar each)
        if b % 2 == 0 or b % 16 == 15:
            dur = BAR if b % 16 in (14, 15) else 2 * BAR
            for k, m in enumerate(voicing):
                if m == root:                    # the bass has it: rootless over the bass keeps 100-250 Hz clear
                    continue
                polys.add(t, poly(m, dur - 0.05, k), pan=(-0.7, -0.35, 0.0, 0.35, 0.7)[k], gain=0.1)
        # the pad holds C# E F# across F#7sus4 and F#7 (the same three notes) rather than re-attacking
        if b % 2 == 0:
            for k, m in enumerate(voicing[2:]):
                pads.add(t, vox(m, 2 * BAR, k), pan=(-0.5, 0.5, 0.0)[k], gain=0.15)
        # bass: straight eighths, accented on the beat; the filter breathes over 8 bars
        bright = 700 + 500 * (0.5 - 0.5 * np.cos(2 * np.pi * (bb % 8) / 8))
        if bb < 4:
            bright *= 0.6 + 0.1 * bb
        for s in range(8):
            acc = (1.0, 0.45, 0.7, 0.5, 0.9, 0.45, 0.7, 0.55)[s]
            bass.add(t + s * 2 * S16, bass_note(root, 2 * S16 * 0.78, acc, bright), gain=0.4)
        # drums
        if part('drums', b):
            kicks = (0, 8, 10) if bb % 2 == 0 else (0, 6, 8)
            for s in kicks:
                drums.add(t + s * S16, KICK, gain=0.34 if s in (0, 8) else 0.24)
            if part('snare', b):
                for s in (4, 12):
                    drums.add(t + s * S16, SNARE, gain=0.19)
            for s in range(16):
                if part('openhat', b) and s % 4 == 2:
                    drums.add(t + s * S16, hat(bb * 16 + s, True), pan=0.3, gain=0.03)
                else:
                    drums.add(t + s * S16, hat(bb * 16 + s), pan=0.3,
                              gain=(0.035 if s % 2 == 0 else 0.018) * (0.85 + 0.3 * r.random()))
        if part('fill', b):
            for k, s in enumerate((12, 13, 14, 15)):
                drums.add(t + s * S16, panned(TOMS[k], 0.5 - k * 0.33), gain=0.24)
        if part('swell', b):
            fx.add(t, swell(BAR, bb), pan=0.0, gain=0.16 if bb != 31 else 0.2)
    for lap in (-1, 0, 1):
        for bar0, mel, fall in LEADS:
            t0 = (lap * BARS + bar0) * BAR
            if -tl.pre * BAR - 9 * BAR < t0 < (BARS + tl.post) * BAR:
                lead.add(t0, lead_phrase(mel, fall), pan=0.05, gain=0.11)

    polyx = chorus(polys.x, tl.loop / 16, depth_ms=2.2, base_ms=7.0, mix=0.55, t0=tl.t0)
    padx = chorus(pads.x, tl.loop / 8, depth_ms=3.0, base_ms=10.0, mix=0.5, t0=tl.t0)
    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.35, 6, 3000) * 0.75
    wet = reverb(polyx * 0.3 + padx * 0.5 + leadx * 0.4 + fx.x * 0.6 + drums.x * 0.05, make_ir(2.8, dark=3800))
    mix = drums.x + bass.x + polyx + padx + leadx + fx.x + wet * 0.5
    mix = lp1(mix, 12000)
    if stems:
        a = tl.smp(0)
        for nm, x in (('drums', drums.x), ('bass', bass.x), ('poly', polyx), ('pad', padx), ('lead', leadx),
                      ('fx', fx.x), ('wet', wet * 0.5)):
            row = []
            for q in range(0, BARS, 4):
                seg = x[a + int(q * BAR * SR):a + int((q + 4) * BAR * SR)]
                row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9))
            print(f'  {nm:6s}' + ''.join(f'{v:7.1f}' for v in row))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None, '--stems' in sys.argv)
