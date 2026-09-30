#!/usr/bin/env python3
"""Block Camp soundtrack "Slow Tape" (Passive Past Continuous): vaporwave.

The brief, 2026-09-30: the Passive Past Continuous station in vaporwave -
lush slowed-down 80s jazz-pop chords, electric piano and a soft pad, tape
wow-and-flutter on everything, a lazy muted drum loop with a soft snare, a
rounded bass, a hazy filtered sax fragment and a little tape hiss;
nostalgic and dreamy. An original piece in that idiom, nothing copied.

A-flat major, 76.8 BPM, 4/4, one chord a bar in an 8-bar cycle:
    Abmaj9 | Fm7 | Dbmaj9 | Eb9sus4 | Abadd9/C | Fm7 | Bbm7 | Eb9
The tempo is 76.8, not 78, because the loop must be a whole number of
samples (here a sixteenth is exactly 9375): at 78 BPM every event landed
up to a sample off its copy a lap later and the hiss and hats alone failed
the seam check. The piano's left hand always has the root and Ab is
doubled where it fits: with rootless maj9/m9 voicings and a C in every
chord the key measured as C minor, so the tonic is stated and C is used
more sparingly (Krumhansl: Ab major 0.93, next Eb major 0.74).
Bass: root, a ghost, a chord tone on beat 3 and a pickup that steps into
the next root (BASS3, PICK). Beat 3 under Abadd9/C is Eb, not the G a fifth
above the C, which sat a minor 9th under the piano's Ab3; the only
chromatic note is the walk C-Eb-E-F in bar 4. The offbeat eighths are
swung by SWING (70 ms) in every part, not just the hats: the kick on the
and of 3, the bass ghost and pickup, the second piano strum and the sax.
The sax check (check_melody) also refuses a long or on-beat note a
semitone or minor 9th from a voicing note, which is how a root sung over
the maj7 below it (Ab over G, Db over C) was caught and rewritten.
Instruments: a Rhodes-style FM electric piano (strummed, a slow stereo
tremolo, chorus), a soft detuned-saw pad, a rounded fretless-ish bass with
a scoop into each note, a lazy swung drum loop through a low-pass (soft
kick, late soft snare, quiet hats), a glassy FM bell figure in the intro and
the breakdown, and an additive "sax" (formant-shaped harmonics, breath
noise, a scoop into each note, delayed vibrato) played through a dotted-
eighth echo. The whole mix then goes through a tape model: a time-varying
delay for wow (half a bar), drift (two bars) and flutter (~6.8 Hz), every
period dividing the loop; top-end loss, a little saturation and hiss.

Arrangement (bar mod 24):
    0-3    electric piano (one long strum a bar), pad, bells, hiss
    4-7    + bass, + drums through a low-pass that opens; bells go on
    8-15   full: two strums a bar, sax phrase A (two 4-bar sentences)
    16-21  full: sax phrase B, higher (up to Ab5 in bar 17)
    22-23  breakdown: drums and bass out, bells return, the end of
           phrase B (Db-Bb-Ab, then a held G) floats over it into bar 0

24 bars = 75 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/slowtape.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

NAME = 'passive-past-continuous'
BARS = 24
tl = Timeline(bpm=76.8, bars=BARS)       # a 16th is exactly 9375 samples, the loop 75 s
BAR, BEAT, S16 = tl.bar, tl.beat, tl.s16

#            name        bass  voicing: the left hand's root, then 3-5-7-9 where it can be
CHORDS = [('Abmaj9',    44, [56, 60, 63, 67, 70]),     # Ab | C Eb G Bb
          ('Fm7',       41, [53, 56, 60, 63, 68]),     # F  | Ab C Eb Ab
          ('Dbmaj9',    37, [49, 56, 60, 63, 65]),     # Db | Ab C Eb F
          ('Eb9sus4',   39, [51, 58, 61, 65, 68]),     # Eb | Bb Db F Ab
          ('Abadd9/C',  36, [48, 56, 63, 68, 70]),     # C  | Ab Eb Ab Bb
          ('Fm7',       41, [53, 56, 60, 63, 68]),
          ('Bbm7',      34, [46, 56, 61, 65, 68]),     # Bb | Ab Db F Ab
          ('Eb9',       39, [51, 61, 65, 67, 70])]     # Eb | Db F G Bb
# The bass on beat 3 (the chord's own fifth, or Eb under Abadd9/C: a fifth
# above the BASS note would be G there, a minor 9th under the Ab3) and its
# pickup into the next bar, which steps into the next root: a chord tone
# where one is a step away, and one chromatic walk, C-Eb-E-F, in bar 4.
BASS3 = [51, 48, 44, 46, 39, 48, 41, 46]
PICK = [43, 39, 41, 37, 40, 36, 37, 43]                 # G Eb F Db E C Db G
SWING = 0.07                                            # the and of each beat, seconds late
FIFTH = [3, 0, 8, 10, 3, 0, 5, 10]                      # each chord's real fifth (pitch class)


def chord_at(b):
    return CHORDS[b % 8]


def chord_tones(b):
    _, root, v = chord_at(b)
    return {root % 12, FIFTH[b % 8]} | {m % 12 for m in v}


def sw(p):
    """Seconds from the bar line to sixteenth p, the offbeat eighths swung
    exactly as the hats are."""
    return p * S16 + (SWING if p % 4 == 2 else 0.0)


def part(name, b):
    b %= BARS; cyc, i = b // 8, b % 8
    return {
        'bass':  not (cyc == 0 and i < 4) and not (cyc == 2 and i >= 6),
        'drums': not (cyc == 0 and i < 4) and not (cyc == 2 and i >= 6),
        'bells': cyc == 0 or (cyc == 2 and i >= 6),
    }[name]


# ── instruments ─────────────────────────────────────────────────────────────
def rhodes(m, dur, vel):
    """FM tine piano: carrier and modulator at 1:1, the index (the bark)
    falling from the attack; a faint 4th-harmonic ping; a soft asymmetric
    saturation for the pickup."""
    n = int((dur + 1.4) * SR); t = np.arange(n) / SR
    f = hz(m)
    idx = 0.15 + (0.5 + 1.3 * vel) * np.exp(-t / 0.22)
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
    x += 0.06 * vel * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.06)
    x = np.tanh(1.2 * x + 0.15) - np.tanh(0.15)
    return x * adsr(n, 0.003, 1.6, 0.45, 0.4, dur) * np.exp(-t / 4.0) * vel


def pad_note(m, dur, seed):
    n = int((dur + 2.2) * SR)
    r = rng('pad', seed, m)
    x = sum(2 * ((np.arange(n) * hz(m) * 2 ** (c / 1200) / SR + r.random()) % 1) - 1 for c in (-8, 0, 8)) / 3
    x = lp(lp1(x, 1500), 1900, 0.6)
    return x * adsr(n, 1.1, 0.5, 0.85, 2.0, dur)


def bass_note(m, dur, vel):
    n = int((dur + 0.2) * SR); t = np.arange(n) / SR
    f = hz(m) * 2 ** (-0.6 * np.exp(-t / 0.035) / 12)          # a small scoop up
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + 0.32 * np.sin(2 * ph) + 0.12 * np.sin(3 * ph) + 0.05 * np.sin(4 * ph)
    return lp1(x, 1100) * adsr(n, 0.01, 0.35, 0.72, 0.09, dur) * vel


def glass(m):
    n = int(1.8 * SR); t = np.arange(n) / SR
    f = hz(m)
    idx = 1.4 * np.exp(-t / 0.12)
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * 2 * f * t))
    return x * perc(n, 0.002, 0.5)


def kick():
    n = int(0.5 * SR); t = np.arange(n) / SR
    f = 53 + 66 * np.exp(-t / 0.04)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)
    knock = lp1(np.random.default_rng(21).standard_normal(n), 1400) * np.exp(-t / 0.012) * 0.5
    return np.tanh(1.3 * (body + knock)) / np.tanh(1.3)


def snare():
    n = int(0.5 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(22).standard_normal(n)
    noise = lp(bp(z, 1800, 0.7), 4200) * np.exp(-t / 0.12)
    tone = np.sin(2 * np.pi * 182 * t) * np.exp(-t / 0.05) * 0.7 + np.sin(2 * np.pi * 287 * t) * np.exp(-t / 0.03) * 0.3
    return noise * 1.3 + tone


def hat(seed):
    n = int(0.12 * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return lp1(hp1(hp1(z, 5000), 5000), 8000) * perc(n, 0.001, 0.022)


KICK, SNARE = kick(), snare()


# ── the sax: (midi or 0 for a rest, sixteenths), 16 a bar, 128 a phrase ─────
SAX_A = [(0, 4), (75, 2), (72, 2), (70, 4), (67, 4),        # Abmaj9
         (68, 6), (67, 2), (65, 8),                         # Fm7
         (0, 8), (72, 2), (75, 2), (77, 4),                 # Dbmaj9
         (75, 6), (73, 2), (70, 8),                         # Eb9sus4
         (0, 4), (75, 2), (72, 2), (70, 4), (68, 4),        # Abadd9/C
         (68, 6), (70, 2), (72, 8),                         # Fm7
         (0, 6), (73, 2), (70, 4), (68, 4),                 # Bbm7
         (67, 8), (70, 4), (73, 4)]                         # Eb9
SAX_B = [(75, 6), (77, 2), (79, 8),                         # Abmaj9
         (80, 8), (77, 4), (75, 4),                         # Fm7
         (77, 6), (75, 2), (72, 8),                         # Dbmaj9
         (70, 12), (0, 4),                                  # Eb9sus4
         (0, 2), (68, 2), (70, 2), (72, 2), (75, 8),        # Abadd9/C
         (77, 4), (75, 4), (72, 4), (68, 4),                # Fm7
         (73, 8), (70, 4), (68, 4),                         # Bbm7
         (67, 12), (0, 4)]                                  # Eb9
assert sum(d for _, d in SAX_A) == 128 and sum(d for _, d in SAX_B) == 128
SAX_AT = ((8, SAX_A), (16, SAX_B))                          # (first bar, phrase)


def check_melody(mel, bar0, label):
    """Every note a quarter or longer, or starting on a beat, must be a chord
    tone of the chord it starts over, and must not sit a semitone or a minor
    9th from a note of the voicing (a root over the maj7 below it is a chord
    tone and still clashes). Returns the offenders."""
    bad, pos = [], 0
    for m, d in mel:
        if m and (d >= 4 or pos % 4 == 0):
            b = bar0 + pos // 16
            if m % 12 not in chord_tones(b):
                bad.append(f'{label}: midi {m} at bar {b} over {chord_at(b)[0]}')
            rub = [v for v in chord_at(b)[2] if abs(m - v) in (1, 13)]
            if rub:
                bad.append(f'{label}: midi {m} at bar {b} rubs on {rub} in {chord_at(b)[0]}')
        pos += d
    return bad


def check_bass():
    """Beat 3 is a chord tone; the pickup steps (1 or 2 semitones) into the
    next bass note and is a chord tone unless it is the one chromatic walk."""
    bad = []
    for i in range(8):
        name, root, _ = CHORDS[i]; nxt = CHORDS[(i + 1) % 8][1]
        if BASS3[i] % 12 not in chord_tones(i):
            bad.append(f'bass beat 3 {BASS3[i]} over {name}')
        if abs(PICK[i] - nxt) not in (1, 2):
            bad.append(f'bass pickup {PICK[i]} does not step into {nxt}')
        if PICK[i] % 12 not in chord_tones(i) and not (i == 4 and PICK[i] == BASS3[i] + 1):
            bad.append(f'bass pickup {PICK[i]} over {name}')
    return bad


def sax_phrase(mel, seed):
    """One continuous breathy voice for a whole phrase, built from harmonics
    under a formant envelope: body near 550 Hz, a second hump near 1.5 kHz,
    everything rolled off above ~2.6 kHz (the haze), brighter on attacks."""
    n = int((8 * BAR + 1.5) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n); scoop = np.zeros(n); bright = np.zeros(n)
    pos = 0; last = hz(next(m for m, _ in mel if m))
    for m, d in mel:                      # swung like the hats: positions are bar-relative
        a = int(round(((pos // 16) * BAR + sw(pos % 16)) * SR))
        b = int(round((((pos + d) // 16) * BAR + sw((pos + d) % 16)) * SR))
        if m:
            f[a:b] = hz(m); last = hz(m)
            tt = np.arange(b - a) / SR
            g[a:b] = np.minimum(1, tt / 0.045) * (0.82 + 0.18 * np.exp(-tt / 0.3))
            g[max(b - int(0.07 * SR), a):b] *= np.linspace(1, 0.2, min(int(0.07 * SR), b - a))
            scoop[a:b] = -0.55 * np.exp(-tt / 0.06)
            vib[a:b] = np.clip((tt - 0.35) / 0.5, 0, 1)
            bright[a:b] = np.exp(-tt / 0.25)
        else:
            f[a:b] = last
        pos += d
    e = int(pos * S16 * SR)
    f[e:] = last; g[e:] = 0
    g = lp1(g, 22)
    k = np.exp(-1 / (0.035 * SR))
    fl = lfilter([1 - k], [1, -k], f); fl[:int(0.02 * SR)] = f[0]
    t = np.arange(n) / SR
    fl = fl * 2 ** ((scoop + 0.22 * vib * np.sin(2 * np.pi * 4.9 * t)) / 12)
    ph = 2 * np.pi * np.cumsum(fl) / SR
    x = np.zeros(n)
    for h in range(1, 15):
        fk = h * fl
        env = (np.exp(-0.5 * (np.log(fk / 560) / 0.55) ** 2) + 0.55 * np.exp(-0.5 * (np.log(fk / 1500) / 0.3) ** 2)
               + 0.08) / (1 + (fk / (2400 + 1400 * bright)) ** 4)
        x += env * np.sin(h * ph) / h ** 0.35
    breath = bp(rng('breath', seed).standard_normal(n), 1700, 0.9) * (0.05 + 0.1 * bright)
    return (x * 0.5 + breath) * g


# ── the tape ────────────────────────────────────────────────────────────────
def tape(x):
    """Wow, drift and flutter as a time-varying delay; every period divides
    the loop, so the wobble is periodic too. A deviation of c cents at
    period P needs a delay swing of c*ln2/1200 * P/2pi seconds."""
    n = len(x); t = np.arange(n) / SR - tl.t0
    d = np.full(n, 0.012)
    for cents, per, ph in ((8.0, tl.loop / 48, 0.0), (6.0, tl.loop / 12, 1.3), (1.5, tl.loop / 504, 0.4)):
        d += cents * np.log(2) / 1200 * per / (2 * np.pi) * np.sin(2 * np.pi * t / per + ph)
    idx = np.arange(n) - d * SR
    return np.stack([np.interp(idx, np.arange(n), x[:, c]) for c in range(2)], 1)


def tremolo(x, period, depth):
    t = np.arange(len(x)) / SR - tl.t0
    s = np.sin(2 * np.pi * t / period)
    return np.stack([x[:, 0] * (1 - depth * (0.5 + 0.5 * s)), x[:, 1] * (1 - depth * (0.5 - 0.5 * s))], 1)


def render(wav=None, stems=False):
    bad = check_bass()
    for bar0, mel in SAX_AT:
        bad += check_melody(mel, bar0, f'sax@{bar0}')
    assert not bad, bad

    ep, pad, bass, drums, bells, sax, hiss = (tl.bus() for _ in range(7))
    for b in tl.bars_range():
        t = b * BAR
        name, root, voicing = chord_at(b)
        cyc, i = (b % BARS) // 8, b % 8
        r = rng('bar', b % BARS)
        # electric piano: a lazy strum on 1, a softer one on the (swung) and of 3
        hits = [(0, 14, 0.85)] if cyc == 0 or (cyc == 2 and i >= 6) else [(0, 9, 0.9), (10, 5, 0.55)]
        for s, d, vel in hits:
            for k, m in enumerate(voicing):
                ep.add(t + sw(s) + k * 0.014, rhodes(m, d * S16, vel * (0.9 + 0.2 * r.random())),
                       pan=-0.45 + k * 0.225, gain=0.22)
        # pad: the whole bar, long attack, long release
        for k, m in enumerate(voicing):
            pad.add(t, pad_note(m, BAR, k), pan=(-0.6, -0.3, 0.0, 0.3, 0.6)[k], gain=0.09)
        # bass: root, a ghost, the fifth (BASS3), and a pickup into the next root
        if part('bass', b):
            for s, m, d, vel in ((0, root, 5.5, 1.0), (6, root, 1.2, 0.45), (8, BASS3[i], 4.5, 0.8),
                                 (14, PICK[i], 1.5, 0.6)):
                bass.add(t + sw(s), bass_note(m, d * S16, vel), gain=0.245)
        # drums: swung, the snare a little late; bars 4-7 open up a low-pass.
        # The kick on the and of 3 is swung with the hat it lands on.
        if part('drums', b):
            fc = 900 * 2 ** (i - 3) if cyc == 0 else None
            swing = SWING
            hitlist = [(0, KICK, 0.42, 0, 0.0), (10, KICK, 0.30, swing, 0.0),
                       (4, SNARE, 0.19, 0.028, -0.05), (12, SNARE, 0.20, 0.028, -0.05)]
            if b % 2:
                hitlist.append((7, KICK, 0.2, 0, 0.0))
            if i == 7 and cyc != 0:
                hitlist.append((15, SNARE, 0.06, 0.02, -0.05))
            for s in range(0, 16, 2):
                hitlist.append((s, hat((b % BARS) * 16 + s), 0.035 if s % 4 == 0 else 0.022,
                                swing if s % 4 == 2 else 0, 0.3))
            for s, x, gain, late, pan in hitlist:
                x = lp(x, fc) if fc else x
                drums.add(t + s * S16 + late, x, pan=pan, gain=0.87 * gain * (0.9 + 0.2 * r.random()))
        # glass bells: a falling figure through the chord, 3-3-3
        if part('bells', b):
            tones = [voicing[4], voicing[3], voicing[2], voicing[0] + 12]
            for k, s in enumerate((2, 5, 8, 11)):
                bells.add(t + s * S16, glass(tones[k] + 12), pan=0.5 - k * 0.33, gain=0.07)
        # tape hiss: a fresh bar of noise, keyed to the bar
        hiss.add(t, rng('hiss', b % BARS).standard_normal((int(BAR * SR) + 1, 2)), gain=1.0)
    for lap in (-1, 0, 1):
        for bar0, mel in SAX_AT:
            t0 = (lap * BARS + bar0) * BAR
            if -tl.pre * BAR - 8 * BAR < t0 < (BARS + tl.post) * BAR:
                sax.add(t0, sax_phrase(mel, bar0), pan=0.12, gain=0.2)

    epx = tremolo(chorus(ep.x, tl.loop / 12, depth_ms=1.6, base_ms=6.0, mix=0.5, t0=tl.t0), BEAT * 2, 0.35)
    padx = chorus(pad.x, tl.loop / 6, depth_ms=3.0, base_ms=9.0, mix=0.6, t0=tl.t0)
    drumx = lp(drums.x, 5200)
    drumx = drumx + reverb(drumx, make_ir(0.7, dark=4000, seed=5)) * 0.18
    bellx = bells.x + pingpong(bells.x, 3 * S16, 0.4, 5, 3500)
    saxx = sax.x + pingpong(sax.x, 3 * S16, 0.36, 6, 2400) * 0.8
    hissx = lp1(hp1(hiss.x, 2500), 7000) * 0.0045
    wet = reverb(epx * 0.3 + padx * 0.35 + saxx * 0.45 + bellx * 0.5 + drumx * 0.06, make_ir(3.4, dark=3400))
    mix = epx + padx + bass.x + drumx + bellx + saxx + wet * 0.55
    mix = tape(mix)
    mix = lp1(mix, 8500)
    norm = 1 / np.abs(mix).max()
    mix = np.tanh(1.3 * mix * norm) / 1.3 + hissx          # a little tape saturation on the peaks
    if stems:
        a = tl.smp(0)
        for nm, x in (('ep', epx), ('pad', padx), ('bass', bass.x), ('drums', drumx), ('bells', bellx),
                      ('sax', saxx), ('hiss', hissx / norm), ('wet', wet * 0.55)):
            row = []
            for q in range(0, BARS, 4):
                seg = x[a + int(q * BAR * SR):a + int((q + 4) * BAR * SR)]
                row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) * norm + 1e-9))
            print(f'  {nm:6s}' + ''.join(f'{v:7.1f}' for v in row))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None, '--stems' in sys.argv)
