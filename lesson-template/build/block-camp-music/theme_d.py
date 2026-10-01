#!/usr/bin/env python3
"""Block Camp theme tune, OPTION D: "campfire folk anthem". An alternative to
theme.py (option A: D major, 4/4, 120 BPM, synth adventure). Here the same
job - the front door of the course, one singable hook - is done acoustically:
a fingerpicked guitar by a fire, a low whistle carrying a tune the whole camp
could sing, and the band joining in chorus by chorus. Original; it quotes no
game, no C418 and no folk tune.

G major, 6/8 at a dotted-quarter pulse of 100 (an eighth is exactly 0.2 s,
9600 samples; a bar 1.2 s). The Timeline is told bpm=200 so that its 4-beat
"bar" is one 6/8 bar. Two bars per chord unit:

    intro   G  | C  | G  | D                     bars 0-7    guitar alone, bass + shaker from bar 4
    verse   G  | C  | G  | D  | Em | C | G | D   bars 8-23   the whistle, quiet; bodhran on the one
    chorus  C  | G  | D  | Em | C  | G | Am D | G bars 24-39  the hook; strums, full bodhran
    chorus' (the same)                          bars 40-55  fiddle counter-line, claps, a whistle
                                                            an octave up, stomps; back to the intro
56 bars = 67.2 s, a seamless loop (see synthkit.py).

The hook (chorus, first four bars, eighths):
    G5-- G5- A5 | G5-- E5-- | D5-- G5- A5 | B5-----
    "so" "so-la so mi, re so-la ti" - it climbs to B5, then C6 in the second half.
Verse:  D5-- B4- D5 | G5--- D5- | E5-- C5- E5 | G5-- E5-- | ...

Instruments, all synthesised: a steel-string guitar of Karplus-Strong strings
(tidewater.py's string: exact tuning via an all-pass, a body resonance after),
picked bass-treble-treble twice a bar, strummed on the dotted beats in the
choruses, and every string damped when the chord changes under it; a low
whistle (near-sine, breath, delayed vibrato, a cut ornament on phrase starts);
a bowed fiddle (saw through body formants, slow bow attack, vibrato); a round
finger bass; a bodhran tuned to D2 with an A3 rim tone (D and A sit a tone or
more from every note of G, C, D, Em and Am); a shaker, hand claps and a foot
stomp.

Checked at import: every melody and fiddle note on a dotted beat or held a
dotted beat or more is a chord tone; no melody/fiddle note makes a semitone,
major seventh or minor ninth with the bass, the guitar's held strings or each
other; every bass note is a chord tone.

Measured on the render (2026-10-01): Krumhansl key G major r 0.93 (next D
major 0.76). Band shares against present-simple.m4a: 6-8 kHz -27.8 dB (-25.7),
8 kHz+ -23.8 (-24.9) - the first render was dull (-33/-32), so the string
excitation and body were opened up, the shaker raised and brightened, the
whistle given more breath air and the reverb made less dark. The fiddle sat
13 dB under the whistle; it is up 7 dB. Stem rms per 8 bars: every part
audible where it plays. No HF sample jump over 2.3x its 99.9th percentile.
Seam 0.0000.

    py lesson-template/build/block-camp-music/theme_d.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

NAME = 'block-camp-theme-d'
E8 = 0.2
BAR = 6 * E8
BARS = 56
tl = Timeline(bpm=200, bars=BARS, pre=6, post=1)
assert abs(tl.bar - BAR) < 1e-12

#        bass  guitar bass strings   guitar trebles     pitch classes
CH = {
    'G':  (31, (43, 50), (59, 62, 67), {7, 11, 2}),
    'C':  (36, (48, 43), (60, 64, 67), {0, 4, 7}),
    'D':  (38, (50, 45), (62, 66, 69), {2, 6, 9}),
    'Em': (40, (40, 47), (59, 64, 67), {4, 7, 11}),
    'Am': (33, (45, 52), (60, 64, 69), {9, 0, 4}),
}
INTRO = ['G', 'C', 'G', 'D']
VERSE = ['G', 'C', 'G', 'D', 'Em', 'C', 'G', 'D']
CHORUS = ['C', 'G', 'D', 'Em', 'C', 'G', ('Am', 'D'), 'G']
PROG = []                                   # one chord name per bar
for u in INTRO + VERSE + CHORUS + CHORUS:
    PROG += list(u) if isinstance(u, tuple) else [u, u]
assert len(PROG) == BARS
SECTIONS = [('intro', 0), ('verse', 8), ('chorus', 24), ('chorus2', 40)]


def section(b):
    b %= BARS
    return [n for n, s in SECTIONS if s <= b][-1]


# ── melody: per two-bar unit, (eighth 0..11, midi, eighths) ─────────────────
VERSE_MEL = [
    [(0, 74, 3), (3, 71, 2), (5, 74, 1), (6, 79, 4), (10, 74, 2)],            # G
    [(0, 76, 3), (3, 72, 2), (5, 76, 1), (6, 79, 3), (9, 76, 3)],             # C
    [(0, 74, 3), (3, 71, 2), (5, 69, 1), (6, 67, 4), (10, 71, 2)],            # G
    [(0, 69, 3), (3, 74, 2), (5, 72, 1), (6, 69, 6)],                         # D
    [(0, 71, 3), (3, 76, 2), (5, 79, 1), (6, 76, 3), (9, 71, 3)],             # Em
    [(0, 72, 3), (3, 76, 2), (5, 72, 1), (6, 67, 6)],                         # C
    [(0, 71, 2), (2, 69, 1), (3, 74, 3), (6, 79, 3), (9, 74, 3)],             # G
    [(0, 78, 3), (3, 74, 2), (5, 71, 1), (6, 69, 6)],                         # D
]
CHORUS_MEL = [
    [(0, 79, 3), (3, 79, 2), (5, 81, 1), (6, 79, 3), (9, 76, 3)],             # C
    [(0, 74, 3), (3, 79, 2), (5, 81, 1), (6, 83, 6)],                         # G
    [(0, 81, 3), (3, 78, 2), (5, 74, 1), (6, 81, 3), (9, 78, 3)],             # D
    [(0, 79, 2), (2, 81, 1), (3, 76, 3), (6, 71, 6)],                         # Em
    [(0, 79, 3), (3, 79, 2), (5, 81, 1), (6, 84, 3), (9, 79, 3)],             # C
    [(0, 83, 3), (3, 79, 2), (5, 81, 1), (6, 74, 6)],                         # G
    [(0, 76, 2), (2, 74, 1), (3, 72, 3), (6, 78, 3), (9, 81, 3)],             # Am | D
    [(0, 79, 9), (9, 74, 3)],                                                 # G
]
MEL = {}                                     # bar -> [(eighth in bar, midi, eighths)]
for base, table in ((8, VERSE_MEL), (24, CHORUS_MEL), (40, CHORUS_MEL)):
    for k, unit in enumerate(table):
        for e, m, d in unit:
            MEL.setdefault(base + 2 * k + e // 6, []).append((e % 6, m, d))


def chord_at(b, e=0):
    return PROG[(b + e // 6) % BARS]


def bass_line(b):
    """(eighth, midi, eighths): root on the one; root again (verse) or the fifth
    (choruses) on the second dotted beat."""
    name = chord_at(b); r = CH[name][0]; sec = section(b)
    if sec == 'intro':
        return [(0, r, 5.5)] if b % BARS >= 4 else []
    if sec == 'verse':
        return [(0, r, 2.7), (3, r, 2.7)]
    fifth = r + 7
    return [(0, r, 2.7), (3, fifth, 1.8), (5, r + 12 if name != 'Em' else r, 0.9)]


def clash(a, b, long_):
    d = abs(a - b)
    return d in (1, 11, 13) or (long_ and d % 12 in (1, 11))


# the fiddle (chorus'): a note on each dotted beat, a chord tone near the last one,
# chosen so it rubs against nothing
def _fiddle():
    out, prev = {}, 71
    for b in range(40, 56):
        name = chord_at(b); pcs = CH[name][3]
        mel = MEL.get(b, [])
        cand = [m for m in range(62, 77) if m % 12 in pcs
                and not any(clash(m, mm, True) for _, mm, _ in mel)
                and not any(abs(m - mm) < 3 for _, mm, _ in mel)]
        notes = []
        for e in (0, 3):
            m = min(cand, key=lambda x: (x == prev, abs(x - prev), -x))
            notes.append((e, m, 3))
            prev = m
        out[b] = notes
    return out


FIDDLE = _fiddle()


def check_harmony():
    bad = []
    for b in range(BARS):
        name = chord_at(b)
        for e, m, d in bass_line(b):
            if m % 12 not in CH[chord_at(b, e)][3]:
                bad.append((b, 'bass', m))
        for part, table in (('mel', MEL), ('fid', FIDDLE)):
            for e, m, d in table.get(b, []):
                c = chord_at(b, e)
                strong = e % 3 == 0 or d >= 3
                if strong and m % 12 not in CH[c][3]:
                    bad.append((b, part, e, m, c, 'not a chord tone'))
                under = [bm for be, bm, bd in bass_line(b) if be < e + d and be + bd > e]
                under += list(CH[c][1]) + list(CH[c][2])
                if part == 'mel':
                    under += [fm for _, fm, _ in FIDDLE.get(b, [])]
                for u in under:
                    if clash(m, u, strong or d >= 2):
                        bad.append((b, part, e, m, c, 'clash', u))
    assert not bad, bad


check_harmony()


# ── instruments ─────────────────────────────────────────────────────────────
def ks(m, dur, vel, bright, key):
    """Karplus-Strong string, as tidewater.py: exact pitch through an all-pass."""
    f = hz(m); P = SR / f
    L = int(P - 0.6); D = P - 0.5 - L; c = (1 - D) / (1 + D)
    t60 = float(np.clip(4.4 * (150 / f) ** 0.4, 1.8, 5.0))
    g = 10 ** (-3 / (f * t60))
    n = int((dur + 0.06) * SR)
    blocks = n // L + 2
    r = rng('ks', key)
    fc = 1500 + 5000 * bright
    exc = lp1(lp1(r.standard_normal(L + 256), fc), fc)[256:]
    exc = exc - np.roll(exc, max(1, int(0.19 * L)))
    exc -= exc.mean(); exc *= vel / (np.abs(exc).max() + 1e-9)
    y = np.zeros(blocks * L); y[:L] = exc
    fb = np.convolve([0.5, 0.5], [c, 1.0]); fa = np.array([1.0, c]); zi = np.zeros(2)
    for j in range(1, blocks):
        v, zi = lfilter(fb, fa, y[(j - 1) * L:j * L], zi=zi)
        y[j * L:(j + 1) * L] = g * v
    y = y[:n]
    y[:96] *= np.linspace(0, 1, 96)
    k = int(0.06 * SR)
    y[-k:] *= np.cos(np.linspace(0, np.pi / 2, k)) ** 2
    return y


def body(x):
    y = x + 0.5 * bp(x, 102, 2.5) + 0.35 * bp(x, 205, 3.0) + 0.2 * bp(x, 410, 2.0)
    return lp1(hp1(y, 70), 12000)


def whistle_note(m, dur, key, cut=False):
    """Low whistle: a near-sine, breath, vibrato after a moment; a 'cut'
    ornament (a flick up to the next scale note) on phrase starts."""
    n = int((dur + 0.25) * SR); t = np.arange(n) / SR
    vib = np.clip((t - 0.25) / 0.25, 0, 1) * np.sin(2 * np.pi * 5.2 * t + rng('wv', key).uniform(0, 6))
    f = hz(m) * 2 ** (0.2 / 12 * vib)
    if cut:
        f = f * np.where(t < 0.035, 2 ** (2 / 12), 1.0)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + 0.12 * np.sin(2 * ph) + 0.05 * np.sin(3 * ph)
    z = rng('wb', key).standard_normal(n)
    breath = bp(z, hz(m) * 2, 3.0) * 0.25 + lp1(hp1(z, 3000), 9000) * 0.035
    return (x + breath) * adsr(n, 0.03, 0.2, 0.85, 0.12, dur)


def fiddle_note(m, dur, key):
    n = int((dur + 0.3) * SR); t = np.arange(n) / SR
    r = rng('fid', key)
    vib = np.clip((t - 0.3) / 0.4, 0, 1) * np.sin(2 * np.pi * 5.6 * t + r.uniform(0, 6))
    f = hz(m) * 2 ** (0.12 / 12 * vib)
    ph = np.cumsum(f) / SR
    x = 2 * ((ph + r.random()) % 1.0) - 1
    x = 0.6 * x + 0.4 * (2 * ((ph * 1.003 + r.random()) % 1.0) - 1)
    x = bp(x, 450, 1.2) * 0.9 + bp(x, 1200, 1.5) * 0.7 + bp(x, 2800, 2.0) * 0.35 + lp(x, 900) * 0.3
    x = lp(x, 5000)
    return x * adsr(n, 0.18, 0.3, 0.9, 0.2, dur)


def bass_note(m, dur):
    n = int((dur + 0.2) * SR); t = np.arange(n) / SR; f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    x += 0.25 * np.sin(8 * np.pi * f * t) * np.exp(-t / 0.04)
    return x * adsr(n, 0.012, 0.35, 0.7, 0.12, dur)


def bodhran(f0, tau, seed, skin=0.3):
    n = int(0.5 * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.25 * np.exp(-t / 0.02))
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / tau)
    z = lp1(np.random.default_rng(seed).standard_normal(n), 2200) * np.exp(-t / 0.01) * skin
    return (tone + z) * np.minimum(1, t / 0.002)


def shaker(seed):
    n = int(0.1 * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return lp1(hp1(hp1(z, 4500), 4500), 12000) * perc(n, 0.012, 0.028)


def clap(seed):
    n = int(0.25 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    env = sum(np.exp(-np.clip(t - d, 0, None) / 0.006) * (t >= d) for d in (0, 0.009, 0.018)) / 3
    env = env + (t >= 0.027) * np.exp(-np.clip(t - 0.027, 0, None) / 0.07)
    return bp(z, 1300, 0.9) * env


def stomp():
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = 55 + 60 * np.exp(-t / 0.025)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12)
    x += lp1(np.random.default_rng(3).standard_normal(n), 900) * np.exp(-t / 0.015) * 0.4
    return x * np.minimum(1, t / 0.001)


STOMP = stomp()
LEVEL = {'intro': 0.7, 'verse': 0.8, 'chorus': 1.0, 'chorus2': 1.0}


def render(wav=None):
    gtr, wh, fid, bass, drum = (tl.bus() for _ in range(5))
    gtr_events = []
    changes = []
    for b in tl.bars_range():
        t = b * BAR; bb = b % BARS; sec = section(b)
        name = chord_at(b); _, (r0, r1), treb, _ = CH[name]
        if chord_at(b - 1) != name:
            changes.append((t, name))
        lv = LEVEL[sec]
        # guitar: bass-treble-treble, twice a bar
        for e in range(6):
            off = float(rng('go', bb, e).uniform(-0.005, 0.005))
            if e % 3 == 0:
                gtr_events.append((t + e * E8 + off, 'B%d' % (e // 3), r0 if e == 0 else r1,
                                   0.9 * lv, 0.35, (bb, e, 'b')))
            else:
                s = 1 if e % 3 == 1 else 2
                if e == 4: s = 0
                gtr_events.append((t + e * E8 + off, 's%d' % s, treb[s], 0.5 * lv, 0.5, (bb, e, 't')))
            if sec in ('chorus', 'chorus2') and e % 3 == 0:      # strum on the dotted beats
                for k in range(3):
                    gtr_events.append((t + e * E8 + off + 0.018 * (k + 1), 's%d' % k, treb[k],
                                       0.4 if e else 0.48, 0.6, (bb, e, 'st', k)))
        # bass
        for e, m, d in bass_line(b):
            bass.add(t + e * E8, bass_note(m, d * E8), gain=0.15 if sec != 'intro' else 0.11)
        # whistle
        for e, m, d in MEL.get(bb, []):
            cut = e == 0 and bb % 2 == 0 and d >= 3
            g = {'verse': 0.10, 'chorus': 0.125, 'chorus2': 0.13}[sec]
            wh.add(t + e * E8, whistle_note(m, d * E8 - 0.03, (bb, e), cut), pan=0.1, gain=g)
            if sec == 'chorus2':
                wh.add(t + e * E8, whistle_note(m + 12, d * E8 - 0.03, (bb, e, 'hi'), cut),
                       pan=-0.25, gain=0.035)
        # fiddle
        for e, m, d in FIDDLE.get(bb, []):
            fid.add(t + e * E8, fiddle_note(m, d * E8 - 0.02, bb), pan=-0.35, gain=0.16)
        # percussion
        lo, hi_ = hz(38), hz(57)                               # D2, A3
        if sec == 'intro' and bb >= 4 or sec == 'verse':
            for e in range(6):
                drum.add(t + e * E8 + 0.008, shaker(bb * 6 + e), pan=0.4,
                         gain=(0.2 if e % 3 == 0 else 0.12) * (1.2 if sec == 'verse' else 0.8))
        if sec == 'verse':
            drum.add(t, bodhran(lo, 0.16, bb), pan=-0.15, gain=0.16)
        if sec in ('chorus', 'chorus2'):
            for e, (f0, tau, gn) in {0: (lo, 0.17, 0.2), 2: (hi_, 0.06, 0.05), 3: (lo, 0.13, 0.13),
                                     4: (hi_, 0.05, 0.04), 5: (hi_, 0.06, 0.06)}.items():
                drum.add(t + e * E8, bodhran(f0, tau, bb * 6 + e, 0.35 if f0 == hi_ else 0.3),
                         pan=-0.15, gain=gn)
            for e in range(6):
                drum.add(t + e * E8 + 0.008, shaker(bb * 6 + e + 999), pan=0.4,
                         gain=0.2 if e % 3 == 0 else 0.12)
        if sec == 'chorus2':
            drum.add(t, STOMP, gain=0.3)
            drum.add(t + 3 * E8, STOMP, gain=0.22)
            drum.add(t + 3 * E8, clap(bb), pan=0.2, gain=0.12)
        if bb in (23, 39):                                    # a bodhran roll into each chorus
            for e in (3, 4, 5):
                for k in (0, 0.5):
                    drum.add(t + (e + k) * E8, bodhran(hi_, 0.05, bb * 13 + e * 2 + int(k * 2)),
                             pan=-0.15, gain=0.03 + 0.012 * (e - 3))

    # damp strings: each rings until replucked, or until the chord changes
    # and the note is not in the new chord
    by_string = {}
    for ev in sorted(gtr_events, key=lambda v: v[0]):
        by_string.setdefault(ev[1], []).append(ev)
    for s, evs in by_string.items():
        for j, (t, _, m, vel, br, key) in enumerate(evs):
            dur = min(evs[j + 1][0] - t, 2.4) if j + 1 < len(evs) else 2.4
            for tc, name in changes:
                keep = {n % 12 for n in CH[name][1]} if s[0] == 'B' else CH[name][3]
                if tc > t + 0.01 and tc - t < dur and m % 12 not in keep:
                    dur = tc - t
                    break
            pan = {'B0': -0.25, 'B1': -0.25, 's0': -0.4, 's1': -0.15, 's2': 0.0}[s]
            gtr.add(t, ks(m, dur, vel, br, key), pan=pan, gain=0.34)

    gtrx = body(gtr.x)
    whx = wh.x + pingpong(wh.x, 3 * E8, 0.25, 3, 3500) * 0.35
    fidx = chorus(fid.x, 4 * BAR, depth_ms=1.5, base_ms=9.0, mix=0.35, t0=-tl.t0)
    wet = reverb(gtrx * 0.2 + whx * 0.4 + fidx * 0.45 + drum.x * 0.12 + bass.x * 0.03,
                 make_ir(2.2, dark=5500, seed=23, pre=0.02))
    stems = dict(guitar=gtrx, whistle=whx, fiddle=fidx, bass=bass.x, perc=drum.x, reverb=wet * 0.35)
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        i0 = tl.smp(0)
        for k, v in stems.items():
            row = []
            for s in range(0, BARS, 8):
                seg = v[i0 + int(s * BAR * SR):i0 + int((s + 8) * BAR * SR)]
                row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9))
            print(f'{k:8s}' + ' '.join(f'{r:6.0f}' for r in row))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
