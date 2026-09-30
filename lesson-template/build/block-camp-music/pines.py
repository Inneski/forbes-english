#!/usr/bin/env python3
"""Block Camp soundtrack "Pines" (Past Perfect): slow, dreamy small-town
mystery.

Innes, 2026-09-30: music for the Past Perfect camp "with a Twin Peaks style".
So: the idiom of Angelo Badalamenti's score - a twangy low electric guitar
drenched in spring reverb and amp tremolo, lush slow synth strings, a deep
round bass, and a cool-jazz passage with finger snaps and brushes. An
original piece in that idiom, nothing copied:

  D minor (with F major colour), 64 BPM, 4/4 (a sixteenth is exactly
  11250 samples). An 8-bar cycle, one chord a bar, two where marked:
  Dm9 | Bbmaj7 | Fmaj7 | Em7b5 A7 | Dm9 | Gm9 | Bbmaj7 | A7sus4 A7b9.
  The 4-bar intro is the cycle's second half, so every section ends on A7
  and falls back into Dm9. check_lines() proves the harmony at every render:
  long or strong melody notes are chord tones, and no two held notes sit a
  semitone or minor ninth apart except the rubs the chords are made of.

  Guitar    a Karplus-Strong string (fractional-delay tuned; the pick is one
            period of a band-limited ramp plus a little noise, so every
            note has the same tone; a comb for a pickup near the bridge), a
            touch of drive, an upper-mid lift for the twang and a cabinet
            low-pass (measured harmonics 2-4 at -3, -6, -10 dB), then a
            spring reverb (a diffuse bright tail plus a train of dispersive
            chirps 34-37 ms apart for the drip), then amp tremolo at 5
            cycles a beat (5.33 Hz), so a lap holds a whole number of
            cycles. Octave-fifth chords ring in the intro, one a chord, each
            damped before the next; the melody sits in the low guitar
            register, straight eighths in A, swung (triplet) in the jazz
            section to sit with the brushes.
  Strings   three detuned saws a voice with delayed vibrato, slow attack
            and release, a doubled top voice, chorus and a long hall; no
            semitone inside a voicing (the maj7s carry the 7th above the
            root, Gm9 its 9th on top).
  Bass      a round sine bass (a little 2nd and 3rd) in half notes, walking
            in quarter notes through the jazz section.
  Snaps     finger snaps on 2 and 4 in the jazz section.
  Brushes   a swirl on every beat and a swung tap on the "and" of 2 and 4
            (triplet swing) in the jazz section.

  Arrangement (bar mod 20): 0-3 intro - strings, half-note bass, four
  ringing guitar chords (D, G, Bb, then A on beat 3 of bar 3); 4-11 the
  guitar melody; 12-19 the cool-jazz
  section - the melody's answer a little higher, snaps, brushes, walking
  bass, the strings' top voice lifted.

20 bars = 75 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/pines.py [--wav preview.wav]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, lp1, hp1, lp, bp, adsr, perc, make_ir, reverb, chorus,
                      finish)

NAME = 'past-perfect'
BARS = 20
tl = Timeline(bpm=64, bars=BARS)
BAR, BEAT = tl.bar, tl.beat

# ── the changes ─────────────────────────────────────────────────────────────
#   Voicings keep semitones and minor ninths out of the pad: the maj7 chords
#   put the 7th above the root (Fmaj7 F-A-C-E, Bbmaj7's A on top), and Gm9
#   puts its 9th on top rather than in an A-Bb cluster at 220 Hz.
CH = {
    'Dm9':    dict(root=38, fifth=45, pad=[50, 53, 57, 64], top=72, pcs={2, 5, 9, 0, 4}),
    'Bbmaj7': dict(root=34, fifth=41, pad=[53, 62, 65, 69], top=74, pcs={10, 2, 5, 9}),
    'Fmaj7':  dict(root=41, fifth=48, pad=[53, 57, 60, 64], top=72, pcs={5, 9, 0, 4}),
    'Em7b5':  dict(root=40, fifth=46, pad=[52, 55, 58, 62], top=67, pcs={4, 7, 10, 2}),
    'A7':     dict(root=45, fifth=40, pad=[52, 55, 61, 64], top=67, pcs={9, 1, 4, 7}),
    'Gm9':    dict(root=43, fifth=50, pad=[50, 53, 58, 62], top=69, pcs={7, 10, 2, 5, 9}),
    'A7sus4': dict(root=45, fifth=40, pad=[52, 55, 57, 62], top=67, pcs={9, 2, 4, 7}),
    'A7b9':   dict(root=45, fifth=40, pad=[52, 55, 58, 61], top=67, pcs={9, 1, 4, 7, 10}),
}
#          (beat, chord) segments per bar of the 8-bar cycle
CYCLE = [[(0, 'Dm9')], [(0, 'Bbmaj7')], [(0, 'Fmaj7')], [(0, 'Em7b5'), (2, 'A7')],
         [(0, 'Dm9')], [(0, 'Gm9')], [(0, 'Bbmaj7')], [(0, 'A7sus4'), (2, 'A7b9')]]


def cyc_bar(b):
    lb = b % BARS
    return lb + 4 if lb < 4 else (lb - 4) % 8


def section(b):
    lb = b % BARS
    return 'intro' if lb < 4 else 'A' if lb < 12 else 'B'


def chord_on(b, beat):
    segs = CYCLE[cyc_bar(b)]
    return [c for s, c in segs if s <= beat][-1]


# ── the guitar's lines: (midi, eighths) per bar of the cycle, 0 = rest ──────
MEL_A = [
    [(0, 2), (57, 2), (60, 2), (62, 2)],       # Dm9       A3 C4 D4
    [(65, 6), (64, 1), (62, 1)],               # Bbmaj7    F4 (E4) D4
    [(64, 6), (60, 2)],                        # Fmaj7     E4 C4
    [(62, 4), (61, 4)],                        # Em7b5 A7  D4 C#4
    [(62, 6), (57, 2)],                        # Dm9       D4 A3
    [(58, 4), (57, 2), (55, 2)],               # Gm9       Bb3 A3 G3
    [(53, 6), (50, 2)],                        # Bbmaj7    F3 D3
    [(52, 4), (49, 4)],                        # A7sus4 A7b9  E3 C#3
]
MEL_B = [
    [(65, 3), (64, 1), (62, 2), (57, 2)],      # Dm9       F4 E4 D4 A3
    [(58, 4), (62, 2), (65, 2)],               # Bbmaj7    Bb3 D4 F4
    [(69, 6), (67, 1), (65, 1)],               # Fmaj7     A4 (G4) F4
    [(64, 4), (61, 2), (64, 2)],               # Em7b5 A7  E4 C#4 E4
    [(62, 2), (64, 2), (65, 4)],               # Dm9       D4 E4 F4
    [(62, 6), (58, 2)],                        # Gm9       D4 Bb3
    [(57, 6), (53, 2)],                        # Bbmaj7    A3 F3
    [(64, 4), (61, 2), (58, 2)],               # A7sus4 A7b9  E4 C#4 Bb3
]
for row in MEL_A + MEL_B:
    assert sum(d for _, d in row) == 8
# the intro's ringing chords: (bar of the loop, beat, notes, beats to ring).
# Each is damped before the next chord: a D chord left ringing into Gm9 put
# its A2 a minor ninth under the pad's Bb3, and a Bb chord left ringing into
# A7sus4 put Bb2 a semitone over the bass's A2.
INTRO = [(0, 0, [38, 45, 50], 4), (1, 0, [43, 50, 55], 4), (2, 0, [34, 41, 46], 4),
         (3, 2, [33, 40, 45], 2)]
# the jazz section's walking bass, quarter notes per bar of the cycle
WALK = [[38, 40, 41, 45], [46, 45, 41, 40], [41, 45, 48, 41], [40, 43, 45, 49],
        [50, 48, 45, 42], [43, 46, 50, 47], [46, 45, 41, 44], [45, 40, 45, 49]]


def check_lines():
    """Melody: every note of a quarter or longer and every note on beat 1 or
    3 must be a chord tone. Walking bass: beats 1 and 3 must be chord tones."""
    bad = []
    for name, mel in (('A', MEL_A), ('B', MEL_B)):
        for cb, row in enumerate(mel):
            pos = 0
            for m, d in row:
                if m:
                    beat = pos / 2
                    c = [c for s, c in CYCLE[cb] if s <= beat][-1]
                    if (d >= 2 or pos % 4 == 0) and m % 12 not in CH[c]['pcs']:
                        bad.append((name, cb, pos, m, c))
                pos += d
    for cb, row in enumerate(WALK):
        for beat in (0, 2):
            c = [c for s, c in CYCLE[cb] if s <= beat][-1]
            if row[beat] % 12 not in CH[c]['pcs']:
                bad.append(('walk', cb, beat, row[beat], c))
    print('lines vs chords:', 'every long or strong note is a chord tone' if not bad else bad)
    # Everything that sounds together, per eighth of the loop: no semitone or
    # minor ninth between two held notes (a quarter or longer; walking-bass
    # passing notes on beats 2 and 4 excepted), apart from the rubs the
    # chords are made of: A7b9's b9 over its root, and a minor ninth chord's
    # 9th a semitone under its 3rd (E-F in Dm9, A-Bb in Gm9) - the last two
    # only from A3 up, since lower down the same rub is mud.
    # OK: chord -> {(lower pc, upper pc): lowest allowed lower note}
    OK = {'A7b9': {(9, 10): 33}, 'Dm9': {(4, 5): 57}, 'Gm9': {(9, 10): 57}}
    ev = []                                    # (start, end) in eighths, midi, part
    for lb in range(BARS):
        sec, segs = section(lb), CYCLE[cyc_bar(lb)]
        for j, (s, c) in enumerate(segs):
            e = segs[j + 1][0] if j + 1 < len(segs) else 4
            ev += [(lb * 8 + 2 * s, lb * 8 + 2 * e, m, 'pad') for m in CH[c]['pad'] + [CH[c]['top']]]
            if sec != 'B':
                ms = [CH[c]['root']] if len(segs) > 1 else [CH[c]['root'], CH[c]['fifth']]
                ev += [(lb * 8 + 2 * s + 4 * k, lb * 8 + 2 * s + 4 * k + 4, m, 'bass') for k, m in enumerate(ms)]
        if sec == 'B':
            ev += [(lb * 8 + 2 * q, lb * 8 + 2 * q + 2, m, 'walk' if q % 2 == 0 else 'pass')
                   for q, m in enumerate(WALK[cyc_bar(lb)])]
        if sec == 'intro':
            ev += [(lb * 8 + 2 * bt, lb * 8 + 2 * (bt + n), m, 'gtr')
                   for bb, bt, ms, n in INTRO if bb == lb for m in ms]
        else:
            pos = 0
            for m, d in (MEL_A if sec == 'A' else MEL_B)[cyc_bar(lb)]:
                if m and d >= 2:
                    ev.append((lb * 8 + pos, lb * 8 + pos + d, m, 'mel'))
                pos += d
    rubs = set()
    for e8 in range(BARS * 8):
        on = [(m, p) for s, e, m, p in ev if s <= e8 < e and p != 'pass']
        c = chord_on(e8 // 8, (e8 % 8) / 2)
        for lo, lp_ in on:
            for hi, hp_ in on:
                if hi - lo in (1, 13) and lo < OK.get(c, {}).get((lo % 12, hi % 12), 999):
                    rubs.add((e8 // 8, c, lo, lp_, hi, hp_))
    print('held semitones / minor ninths:', 'none outside the chords\' own' if not rubs else sorted(rubs))
    assert not (bad or rubs), 'a wrong note or a clash in the voicings (listed above)'


# ── the guitar ──────────────────────────────────────────────────────────────
def ks_string(m, dur, v=1.0, t60=5.0, seed=0):
    """Karplus-Strong: a pick's noise burst circulating in a delay line of
    one period, through a two-tap loop filter (a = 0.6) and a
    first-order all-pass that supplies the fractional part of the delay.
    Damped with a short fade `dur` seconds after the pluck."""
    f = hz(m)
    a = 0.6
    L = SR / f
    N = int(np.floor(L - (1 - a) - 0.1))
    d = L - (1 - a) - N
    c = (1 - d) / (1 + d)
    g = 10 ** (-3 / (t60 * f))
    den = np.zeros(N + 3)
    den[0] = 1.0; den[1] = c
    den[N] -= g * a * c
    den[N + 1] -= g * (a + (1 - a) * c)
    den[N + 2] -= g * (1 - a)
    n = int((dur + 0.12) * SR)
    # the pick: one period of a band-limited ramp (harmonics falling as
    # 1/k), so every note has the same tone, plus a little noise for the
    # scrape; then a gentle comb for the pickup's place near the bridge
    kk = np.arange(1, int(min(40, 4500 / f)) + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -0.9 * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    exc += 0.15 * lp1(np.random.default_rng(seed).uniform(-1, 1, N), 3000)
    k = max(1, int(0.2 * N))
    exc[k:] -= 0.45 * exc[:-k]
    x = np.zeros(n); x[:N] = exc * v
    y = lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    y *= np.clip((dur + 0.1 - t) / 0.1, 0, 1)                # fret released
    return y


def amp(y):
    """A touch of drive, the upper-mid twang, the cabinet."""
    y = np.tanh(1.8 * y) / 1.8
    y = y + 0.2 * bp(y, 1100, 0.9)
    return lp(lp1(y, 4500), 3300, 0.8)


def spring_ir(seed, gap):
    """A spring tank: a bright diffuse tail with thin lows, plus a train of
    short falling chirps (the springs' dispersion), each quieter."""
    n = int(2.6 * SR); t = np.arange(n) / SR
    rg = np.random.default_rng(seed)
    tail = rg.standard_normal(n) * np.exp(-6.9 * t / 2.3)
    tail = hp1(lp1(tail, 6000), 300)
    cn = int(0.022 * SR); ct = np.arange(cn) / SR
    fch = 3200 * (0.12 ** (ct / ct[-1]))                    # 3.2 kHz falling to 380 Hz
    chirp = np.sin(2 * np.pi * np.cumsum(fch) / SR) * np.hanning(cn)
    train = np.zeros(n)
    for j in range(60):
        i = int((0.006 + j * gap) * SR)
        if i + cn >= n:
            break
        train[i:i + cn] += chirp * 0.78 ** j * (1 if j % 2 == 0 else -0.8)
    ir = tail / np.sqrt(np.sum(tail ** 2)) + 0.6 * train / np.sqrt(np.sum(train ** 2))
    return ir / np.sqrt(np.sum(ir ** 2))


def spring(x):
    irs = [spring_ir(51, 0.034), spring_ir(52, 0.037)]
    mono = x.mean(1)
    from scipy.signal import fftconvolve
    return np.stack([fftconvolve(mono, irs[ch])[:len(x)] for ch in range(2)], 1)


# ── the others ──────────────────────────────────────────────────────────────
def string_note(m, dur, seed):
    n = int((dur + 2.2) * SR); t = np.arange(n) / SR
    vib = 1 + 0.004 * np.clip((t - 0.6) / 1.0, 0, 1) * np.sin(2 * np.pi * 4.6 * t + seed)
    x = np.zeros(n)
    for k, cents in enumerate((-7, 0, 7)):
        f = hz(m) * 2 ** (cents / 1200) * vib
        p = (0.31 * k + 0.17 * seed + np.cumsum(f / SR)) % 1.0
        x += 2 * p - 1
    x = lp1(lp1(x / 3, 1900), 2600)
    return x * adsr(n, 1.3, 0.8, 0.9, 1.9, dur)


def bass_note(m, dur):
    n = int((dur + 0.4) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    thump = np.sin(2 * np.pi * f * 2 * t) * np.exp(-t / 0.03) * 0.25
    return (x + thump) * adsr(n, 0.02, 0.4, 0.75, 0.25, dur)


def snap():
    n = int(0.14 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(61).standard_normal(n)
    x = bp(z, 2300, 2.2) * np.exp(-t / 0.016) + np.sin(2 * np.pi * 1250 * t) * np.exp(-t / 0.008) * 0.5
    return x * np.minimum(1, t / 0.0006)


def swirl(length, seed):
    n = int(length * SR); u = np.arange(n) / n
    z = np.random.default_rng(seed).standard_normal(n)
    return lp1(lp1(bp(z, 2600, 0.8), 5000), 5000) * np.sin(np.pi * u) ** 1.5


def tap(seed):
    n = int(0.12 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    return lp1(bp(z, 3200, 0.9), 8000) * perc(n, 0.002, 0.035)


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    check_lines()
    gtr, strings, bass, perc_ = (tl.bus() for _ in range(4))
    for b in tl.bars_range():
        t = b * BAR
        lb, sec, cb = b % BARS, section(b), cyc_bar(b)
        segs = CYCLE[cb]
        # strings: each chord for as long as it lasts
        lvl = {'intro': 0.9, 'A': 0.7, 'B': 0.85}[sec]
        for j, (s, c) in enumerate(segs):
            end = segs[j + 1][0] if j + 1 < len(segs) else 4
            dur = (end - s) * BEAT
            v = CH[c]
            for k, m in enumerate(v['pad']):
                strings.add(t + s * BEAT, string_note(m, dur, k), pan=(-0.55, -0.2, 0.2, 0.55)[k],
                            gain=0.1 * lvl)
            strings.add(t + s * BEAT, string_note(v['top'], dur, 7), pan=0.1,
                        gain=0.056 * lvl * (1.3 if sec == 'B' else 1.0))
        # bass
        if sec == 'B':
            for q, m in enumerate(WALK[cb]):
                bass.add(t + q * BEAT, bass_note(m, BEAT * 0.9), gain=0.09 if q % 2 == 0 else 0.08)
        else:
            if len(segs) == 1:
                v = CH[segs[0][1]]
                bass.add(t, bass_note(v['root'], 2 * BEAT * 0.95), gain=0.09)
                bass.add(t + 2 * BEAT, bass_note(v['fifth'], 2 * BEAT * 0.95), gain=0.08)
            else:
                for s, c in segs:
                    bass.add(t + s * BEAT, bass_note(CH[c]['root'], 2 * BEAT * 0.95), gain=0.09)
        # guitar
        if sec == 'intro':
            for bb, beat, notes, beats in INTRO:
                if lb == bb:
                    ring = beats * BEAT - 0.06
                    for k, m in enumerate(notes):
                        gtr.add(t + beat * BEAT + k * 0.018, ks_string(m, ring, 0.6 - 0.08 * k, 7.0, 100 + k),
                                gain=0.3)
        else:
            # the jazz section swings its off-beat eighths to the triplet, as
            # the brush taps do; played straight they flammed 156 ms against them
            row = (MEL_A if sec == 'A' else MEL_B)[cb]
            sw = 2 / 3 if sec == 'B' else 1 / 2
            def at(p):
                return (p // 2 + (p % 2) * sw) * BEAT
            pos = 0
            for m, d in row:
                if m:
                    v = 1.0 if pos % 4 == 0 else 0.85
                    gtr.add(t + at(pos), ks_string(m, at(pos + d) - at(pos), v, 5.0, m * 8 + pos), gain=0.3)
                pos += d
        # snaps and brushes in the jazz section
        if sec == 'B':
            for q in (1, 3):
                perc_.add(t + q * BEAT, snap(), pan=0.35, gain=0.24)
            for q in range(4):
                perc_.add(t + q * BEAT - 0.08, swirl(BEAT * 0.95, 300 + q), pan=-0.25, gain=0.05)
            for q in (1, 3):
                perc_.add(t + (q + 2 / 3) * BEAT, tap(400 + q), pan=-0.2, gain=0.09)

    # guitar chain: amp, spring, then the amp's tremolo on both
    g = np.stack([amp(gtr.x[:, 0]), amp(gtr.x[:, 1])], 1) * 1.9
    g = g + spring(g) * 0.55
    tt = np.arange(tl.n) / SR - tl.t0
    trem = 1 - 0.42 * (0.5 + 0.5 * np.sin(2 * np.pi * (5 / BEAT) * tt))
    g = g * trem[:, None]
    strx = chorus(strings.x, tl.loop / 8, depth_ms=3.5, base_ms=9.0, mix=0.55, t0=tl.t0)
    hall = make_ir(3.6, dark=4200, seed=71, pre=0.03)
    wet = reverb(g * 0.35 + strx * 0.45 + perc_.x * 0.5 + bass.x * 0.05, hall)
    mix = g + strx + bass.x + perc_.x + wet * 0.55
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
