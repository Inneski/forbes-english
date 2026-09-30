#!/usr/bin/env python3
"""Block Camp soundtrack "Courtroom" (Passive Trial): John Carpenter-style suspense in 5/4.

The brief: the Passive Trial station, a courtroom trial, in the style of John
Carpenter's suspense scores. That means a piano-like ostinato in 5/4 that
never lets up, low synth drones, brass-synth stabs on the structural beats, a
slow and simple synth melody over it all, and an occasional deep boom. It
should be tense but not horror, because it plays under a children's lesson.
Everything here is original. The ostinato is grouped 4+3+3 (rising
arpeggio, then two falling cells around A4), not 3+3+2+2.

A minor, 120 BPM (quarter notes), 5/4. Each bar lasts 2.5 s, which is built on
Timeline(bpm=96), whose 4-beat bar is also 2.5 s. The ostinato is the same bar
throughout: ten eighths, A3 E4 A4 C5 | B4 E4 A4 | G4 E4 A4. On E bars the G
becomes G#. The bass and drone move underneath it, so the fixed figure keeps
changing colour: Fmaj7 over F, Dm9 over D, E7sus4 over E (the piano's A is
the 4th, its G# the leading tone that climbs back to A).
A fixed figure over a moving bass means everything else has to fit round it.
The stabs are voiced clear of the ostinato's A3 and E4 (no G#3 under the A3,
no F4 against the E4, no cluster at A3), and the pickup stab drops any note
a semitone from the drone it lands over. The melody never holds a note over
an ostinato note a semitone away. It keeps off C through the piano's B4
(beat 3), off B through its C5 (the fourth eighth), off F wherever the
piano's E sounds more than once or the bell's E5 sounds at all, and off G#
entirely, because the piano's A is always there. `--check` measures all of
this.
  bars  0-7   Am (the drone comes in at bar 2)
        8-15  F F F F | G G | E E
       16-23  Dm Dm Dm Dm | F F | E E
       24-31  Am Am | F F | Dm Dm | E E
Instruments (all synthesised here): an FM piano for the ostinato; a drone
of detuned saws on the root, with a slowly breathing filter (the LFO period
is 10 s, which divides the loop); stabs from a brassy detuned-saw chord; a
two-saw lead with glide and delayed vibrato; a deep boom (a falling sine
thud); a soft woodblock clock tick. The hall is dark, and the lead has a
dotted-quarter echo.
Arrangement:
  bars 0-1    piano alone, with a boom on the downbeat
  bars 2-7    the drone comes in; stabs on bars 4 and 6
  bars 8-15   the melody, first phrase; a stab on every change of chord
  bars 16-23  second phrase; the clock ticks on the quarter notes; extra stabs
              on the syncopated accent
  bars 24-29  third phrase; a bell doubles the ostinato an octave up (the peak)
  bars 30-31  a breakdown to piano and the E drone, which falls back into the top
Booms fall on bars 0, 8, 16 and 24. The piano is 1 dB softer in bars 0-7 and 30-31,
and 0.7 dB louder at the peak.
The whole thing is 32 bars = 80 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/courtroom.py [--wav preview.wav] [--check]

--check lists every melody note against the chord under it and against the
ostinato notes sounding with it, and every stab note against the ostinato.
It exits 1 on any unmarked non-chord tone or semitone clash.
"""
import sys
from functools import lru_cache
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, saw, pulse, adsr, perc,
                      swept_lp, pingpong, make_ir, reverb, chorus, finish)

tl = Timeline(bpm=96, bars=32)          # 4 x 0.625 s = 2.5 s = one 5/4 bar at 120
BAR = tl.bar
BEAT = BAR / 5                          # 0.5 s
E8 = BEAT / 2                           # 0.25 s
BARS = tl.bars

# ── harmony: (bass root midi, chord tones as pitch classes, name) per bar ────
_CH = {'Am': (45, {9, 0, 4, 7}),        # Am7 (the ostinato supplies the G)
       'F':  (41, {5, 9, 0, 4}),        # Fmaj7 (and the E)
       'G':  (43, {7, 11, 2}),
       'E':  (40, {4, 9, 11, 2}),       # E7sus4: the ostinato's A is a chord tone, its G# the leading tone
       'Dm': (38, {2, 5, 9, 0})}        # Dm7
HARM = (['Am'] * 8 + ['F'] * 4 + ['G'] * 2 + ['E'] * 2 +
        ['Dm'] * 4 + ['F'] * 2 + ['E'] * 2 + ['Am'] * 2 + ['F'] * 2 + ['Dm'] * 2 + ['E'] * 2)
assert len(HARM) == BARS


def chord(b):
    return HARM[b % BARS]


def part(name, b):
    b %= BARS
    return {
        'piano':  True,
        'drone':  b >= 2,
        'bell':   24 <= b < 30,
        'tick':   16 <= b < 30,
        'boom':   b in (0, 8, 16, 24),
        'stab':   b in (4, 6) or (8 <= b < 30 and (HARM[b] != HARM[b - 1] or b % 2 == 0)),
        'stab2':  16 <= b < 30 and HARM[(b + 1) % BARS] != HARM[b],     # pickup into a change
    }[name]


OSTINATO = [57, 64, 69, 72, 71, 64, 69, 67, 64, 69]      # A3 E4 A4 C5 | B4 E4 A4 | G4 E4 A4
ACCENT = {0: 1.0, 4: 0.92, 7: 0.92}                       # the 4+3+3 grouping


def ostinato(b):
    return [(m + 1 if (m == 67 and chord(b) == 'E') else m) for m in OSTINATO]


# melody: (bar, [(midi, beats), ...]) phrases; beats add up to 5 per bar
PHRASES = [
    (8,  [(69, 5), (72, 2), (76, 3), (79, 5, '9th over F (the ostinato G), falls to the 7th'), (76, 3), (72, 2),
          (74, 5), (67, 3), (71, 2), (76, 5), (74, 3), (71, 2)]),   # F F F F G G E E
    (16, [(69, 5), (74, 3), (77, 2), (81, 5), (79, 3, '11th over Dm, falls to the 3rd'), (77, 2), (81, 3),
          (79, 2, 'passing, 3rd to 7th of F'), (76, 3), (72, 2), (76, 5), (74, 3), (71, 2)]),  # Dm x4 F F E E
    (24, [(76, 5), (81, 3), (79, 2), (81, 5), (79, 3, '9th over F, falls to the 7th'), (76, 2), (74, 3), (72, 2),
          (69, 5)]),                                                # Am Am F F Dm Dm
]
for _b, _mel in PHRASES:
    assert sum(n[1] for n in _mel) % 5 == 0


def check():
    """Melody against the chord, and against the notes actually sounding with
    it: a melody note held over an ostinato (or bell) note a semitone away, or
    a stab note a semitone from the ostinato note it lands on, is a clash."""
    bad = 0
    nm = lambda m: ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'][m % 12] + str(m // 12 - 1)
    for b0, mel in PHRASES:
        pos = 0
        for n in mel:
            m, d = n[0], n[1]
            b = b0 + pos // 5
            ok = m % 12 in _CH[chord(b)][1]
            note = n[2] if len(n) > 2 else ''
            flag = 'ok ' if ok else ('TEN' if note else 'BAD')
            e0 = (pos % 5) * 2
            under = [o for i, o in enumerate(ostinato(b)) if e0 <= i < e0 + 2 * d]
            if part('bell', b):
                under += [o + 12 for o in under]
            rub = [nm(o) for o in under if abs(o - m) == 1]
            m9 = sum(abs(o - m) == 13 for o in under)
            extra = (f'  CLASH: a semitone from {", ".join(rub)}' if rub else '') + (f'  (m9 x{m9})' if m9 else '')
            print(f'  {flag} bar {b:2d} beat {pos % 5 + 1} {nm(m):4s} {d} beats over {chord(b):2s} {note}{extra}')
            bad += (not ok and not note) + bool(rub)
            pos += d
    for ch, v in VOICINGS.items():
        b = HARM.index(ch)
        for o in ostinato(b)[:4]:            # the stab sounds for about four eighths
            for s in v:
                if abs(o - s) == 1 or (abs(o - s) == 2 and min(o, s) < 60):
                    print(f'  CLASH: stab {ch} {nm(s)} against the ostinato\'s {nm(o)}')
                    bad += 1
    colour = {}
    for b in range(BARS):
        for i, m in enumerate(ostinato(b)):
            if i in ACCENT and m % 12 not in _CH[chord(b)][1]:
                colour.setdefault((chord(b), i, m % 12), []).append(b)
    for (ch, i, pc), bars in sorted(colour.items()):
        iv = (pc - _CH[ch][0]) % 12
        print(f'  ostinato colour: accented eighth {i} is {iv} semitones over the {ch} root, bars {bars[0]}-{bars[-1]} ({len(bars)})')
    print(f'{bad} unintended non-chord tones')
    return bad


# ── instruments ─────────────────────────────────────────────────────────────
@lru_cache(maxsize=None)
def piano(m, acc):
    """FM piano: a 1:1 pair whose index falls fast (the hammer's brightness),
    a slightly sharp second partial, a thump of felt, damped after an eighth."""
    dur = E8
    n = int((dur + 0.35) * SR); t = np.arange(n) / SR
    f = hz(m)
    idx = 0.5 + 2.4 * acc * np.exp(-t / 0.12)
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
    x += 0.22 * np.sin(2 * np.pi * 2.004 * f * t) * np.exp(-t / 0.25)
    x += 0.10 * np.sin(2 * np.pi * 3.01 * f * t) * np.exp(-t / 0.12)
    x += 0.06 * np.sin(2 * np.pi * 4.03 * f * t) * np.exp(-t / 0.08)
    thump = lp1(np.random.default_rng(m).standard_normal(n), 900) * np.exp(-t / 0.01) * 0.3
    tau = float(np.clip(1.1 - (m - 57) * 0.03, 0.5, 1.2))
    damp = np.clip((dur + 0.12 - t) / 0.12, 0, 1) ** 2
    env = np.minimum(1, t / 0.002) * np.exp(-t / tau) * (0.25 + 0.75 * damp)
    return (x + thump) * env * acc


@lru_cache(maxsize=None)
def bell(m):
    n = int(1.4 * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t + 1.2 * np.exp(-t / 0.3) * np.sin(2 * np.pi * f * 3.0 * t))
    return x * perc(n, 0.002, 0.35)


def env_lp(x, fcf, q=1.0, chunk=256):
    n = len(x); out = np.empty(n); zi = np.zeros(2)
    for i in range(0, n, chunk):
        fc = fcf((i + chunk / 2) / SR)
        w = 2 * np.pi * min(fc, SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


def drone(root, bars, t0):
    """Root and fifth an octave above it, detuned saws, a sine an octave under;
    the cutoff breathes with a 10 s period measured from the loop's start."""
    dur = bars * BAR
    n = int((dur + 1.6) * SR); t = np.arange(n) / SR
    f = hz(root)
    r = rng('drone', root, round(t0, 3) % tl.loop)
    x = sum(saw(f * 2 ** (c / 1200), n, r.random()) for c in (-7, 0, 6)) / 3
    x += 0.45 * sum(saw(f * 1.5 * 2 ** (c / 1200), n, r.random()) for c in (-5, 4)) / 2
    x = env_lp(x, lambda tt: 420 * (1 + 0.35 * np.sin(2 * np.pi * (t0 + tt) / 10.0)), q=1.1)
    x += 0.30 * np.sin(2 * np.pi * f / 2 * t)
    return x * adsr(n, 0.9, 0.5, 0.85, 1.4, dur)


@lru_cache(maxsize=None)
def brass(m, dur):
    n = int((dur + 0.5) * SR)
    f = hz(m)
    x = sum(saw(f * 2 ** (c / 1200), n, 0.13 * k) for k, c in enumerate((-9, -3, 3, 9))) / 4
    x = swept_lp(x, 4800, 900, q=1.0)
    return x * adsr(n, 0.008, 0.18, 0.35, 0.35, dur)


# Voiced round the ostinato, which lands on A3 and E4 as the stab sounds: no
# note a semitone from either (no F4 over the E4, no G#3 under the A3) and no
# cluster round A3. E is E7sus4 in fourths, so the piano's A is its 4th and
# the piano's G# (eighth 7) the only third; F and Dm share F3 A3 C4.
VOICINGS = {'Am': [45, 57, 60, 64], 'F': [41, 53, 57, 60], 'G': [43, 50, 62, 67],
            'E': [40, 52, 57, 62], 'Dm': [38, 53, 57, 60]}


def pickup(b):
    """The pickup stab anticipates the next chord over this bar's drone, so it
    drops any note a semitone (or major 7th) from the drone's root or fifth:
    no F3 over the Am drone's E3, no C4 over the E drone's B2."""
    r = _CH[chord(b)][0]
    return [m for m in VOICINGS[chord(b + 1)][1:] if all((m - d) % 12 not in (1, 11) for d in (r, r + 7))]


def boom():
    n = int(2.6 * SR); t = np.arange(n) / SR
    f = 44 + 46 * np.exp(-t / 0.07)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.75)
    body += 0.35 * np.sin(2 * np.pi * 2 * np.cumsum(f) / SR) * np.exp(-t / 0.3)
    thud = lp1(np.random.default_rng(3).standard_normal(n), 400) * np.exp(-t / 0.03) * 0.6
    return lp(np.tanh(1.4 * (body + thud)), 700)


def tick(seed):
    n = int(0.08 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    return (bp(z, 1500, 4.0) * 1.5 + np.sin(2 * np.pi * 1150 * t)) * np.exp(-t / 0.012)


def lead_phrase(mel):
    total = sum(n[1] for n in mel) * BEAT
    n = int((total + 1.0) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n)
    pos = 0.0; last = hz(mel[0][0])
    for note in mel:
        m, d = note[0], note[1]
        a, b = int(pos * SR), int((pos + d * BEAT) * SR)
        f[a:b] = hz(m); last = hz(m)
        tt = np.arange(b - a) / SR
        g[a:b] = np.minimum(1, tt / 0.06) * (0.85 + 0.15 * np.exp(-tt / 0.4))
        g[max(b - int(0.06 * SR), a):b] *= 0.55
        vib[a:b] = np.clip((tt - 0.6) / 0.8, 0, 1)
        pos += d * BEAT
    f[int(pos * SR):] = last
    g[int(pos * SR):] = 0
    g[int(pos * SR) - int(0.4 * SR):int(pos * SR)] *= np.linspace(1, 0, int(0.4 * SR))
    g = lp1(g, 25)
    a = np.exp(-1 / (0.05 * SR))
    fl = lfilter([1 - a], [1, -a], f); fl[:int(0.05 * SR)] = f[0]
    t = np.arange(n) / SR
    fl = fl * 2 ** (0.14 / 12 * vib * np.sin(2 * np.pi * 5.0 * t))
    x = sum(2 * ((np.cumsum(fl * 2 ** (c / 1200)) / SR + k * 0.29) % 1) - 1 for k, c in enumerate((-6, 0, 6))) / 3
    x = lp(lp1(x, 3800), 4200, 0.9) * g
    return x


def render(wav=None):
    pno, bells, drn, brs, lead, fx = (tl.bus() for _ in range(6))
    B0 = boom()
    for b in tl.bars_range():
        t = b * BAR
        ch = chord(b)
        bb = b % BARS
        swell = 0.88 if bb < 8 or bb >= 30 else 1.08 if bb >= 24 else 1.0
        # piano ostinato, relentless
        for i, m in enumerate(ostinato(b)):
            acc = ACCENT.get(i, 0.72)
            pno.add(t + i * E8, piano(m, acc), pan=-0.15 + 0.03 * (i % 3), gain=0.15 * swell)
            if part('bell', b):
                bells.add(t + i * E8, bell(m + 12), pan=0.35, gain=0.035 * acc)
        if part('boom', b):
            fx.add(t, B0, gain=0.24)
        if part('tick', b):
            for k in range(5):
                fx.add(t + k * BEAT, tick((b % BARS) * 5 + k), pan=0.45, gain=0.030 if k else 0.040)
        if part('stab', b):
            for k, m in enumerate(VOICINGS[ch]):
                brs.add(t, brass(m, 0.42), pan=(0.0, -0.4, 0.1, 0.4)[k], gain=0.34 if k else 0.38)
        if part('stab2', b):
            ups = pickup(b)
            for k, m in enumerate(ups):
                brs.add(t + 7 * E8, brass(m, 0.22), pan=(-0.4, 0.1, 0.4)[k], gain=0.24 * (3 / len(ups)) ** 0.5)
    # drone: one note per run of equal chords, laid for three laps so the pre-roll is the last lap
    runs, b = [], 2
    while b < BARS:
        e = b
        while e + 1 < BARS and HARM[e + 1] == HARM[b]:
            e += 1
        runs.append((b, e - b + 1, _CH[HARM[b]][0]))
        b = e + 1
    for lap in (-1, 0, 1):
        for b0, nb, root in runs:
            t0 = lap * tl.loop + b0 * BAR
            if -tl.pre * BAR - nb * BAR - 2 < t0 < (BARS + tl.post) * BAR:
                drn.add(t0, drone(root, nb, b0 * BAR), gain=0.12)
        for b0, mel in PHRASES:
            t0 = lap * tl.loop + b0 * BAR
            if -tl.pre * BAR - 8 * BAR < t0 < (BARS + tl.post) * BAR:
                lead.add(t0, lead_phrase(mel), pan=0.12, gain=0.22)

    drnx = chorus(drn.x, 10.0, depth_ms=3.0, base_ms=9.0, mix=0.5, t0=tl.t0)
    brsx = chorus(brs.x, 5.0, depth_ms=1.5, base_ms=6.0, mix=0.4, t0=tl.t0)
    leadx = lead.x + pingpong(lead.x, 3 * E8, 0.32, 4, 2400) * 0.6
    hall = make_ir(3.0, dark=4200, seed=17)
    wet = reverb(pno.x * 0.28 + bells.x * 0.5 + brsx * 0.45 + leadx * 0.35 + fx.x * 0.4 + drnx * 0.15, hall)
    mix = pno.x + bells.x + drnx + brsx + leadx + fx.x + wet * 0.5
    return finish(tl, mix, 'passive-trial', wav=wav)


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(1 if check() else 0)
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
