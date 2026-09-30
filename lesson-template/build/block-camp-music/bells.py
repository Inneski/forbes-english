#!/usr/bin/env python3
"""Block Camp soundtrack "Bells" (Passive Past Perfect, the end of the descent): minimalist 7/8.

The brief is Mike Oldfield's Tubular Bells, with a hypnotic and wistful mood.
It calls for an interlocking piano/organ-like figure in 7/8, a second figure
layered on top, a glockenspiel line, a warm organ pad, a soft bass, and near
the end of the loop a single deep tubular-bell strike. Everything here is
original: the main figure is a flowing arpeggio, not a pedal-note
alternation, and no melody is taken from the record.

E minor, 7/8 at 160 eighths a minute. Each bar lasts 2.625 s, which is built
on Timeline(bpm=640/7), whose 4-beat bar is also 2.625 s. Three layers
interlock by grouping:
  figure A  piano (with a faint 4' + 2' organ doubling), 2+2+3:
            E4 G4 | B4 E5 | D5 G4 F#4, a rising arch with a turn back to E.
            It is the same every bar, except that G becomes A over D
            (E4 A4 | B4 E5 | D5 A4 F#4), and over the closing Bsus4 it becomes
            E4 A4 | B4 E5 | B4 A4 F#4. It has a slight periodic humanisation
            (+-0.6 dB, +-4 ms).
  figure B  a reedy organ, 3+2+2, three held notes a bar: a falling sigh
            that follows the chord: Em G-F#-D, C G-E-D, Am E-D-C (a 4-3),
            D F#-E-D, Bsus4 F#-E-B
  bass      a soft root and its octave, 4+3
So the accents fall on eighths 0/2/4 (A), 0/3/5 (B) and 0/4 (bass).
Changes, one chord per bar group:
  bars 0-7 Em | 8-11 C | 12-15 Am | 16-19 C | 20-23 D | 24-27 Em | 28-29 Am | 30-31 Bsus4
That is i - VI - iv - VI - VII - i - iv - v(sus), the Aeolian mode throughout.
Arrangement:
  bars 0-3    figure A alone
  bars 4-7    the warm organ pad comes in (drawbar sines with a slow swell)
  bars 8-15   figure B and the bass
  bars 16-29  a glockenspiel melody (A5-B6, an octave above the figure) over it all
  bars 30-31  down to figure A and the pad, with one deep tubular bell (strike
              note E3) on bar 30. It rings across the seam into the top of the loop
              and fades out over bars 2-3.
The bell is additive and FM. It has the free-bar partials of a real chime, so
its low partials at about 102 and 199 Hz are inharmonic, and partials 4-6
(about 2:3:4) give the E3 strike note. The low modes are weak and short, so the
tail rings E4 and B4. An FM clang sits on the attack.
The pad's 16' drawbar is on its lowest voice only.
The whole thing is 32 bars = 84 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/bells.py [--wav preview.wav] [--check]

--check lists the glockenspiel and figure-B notes against the chord under them. A note
that is not a chord tone must be a named colour (a 9th, 6th or 11th that the figures
supply) or an appoggiatura that resolves by step.
"""
import sys
from functools import lru_cache
import numpy as np
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, pulse, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

tl = Timeline(bpm=640 / 7, bars=32)     # 4 x 0.65625 s = 2.625 s = one 7/8 bar at 160 eighths/min
BAR = tl.bar
E8 = BAR / 7                            # 0.375 s
BARS = tl.bars
_N = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# chord: bass root (midi), chord tones, colour tones (9ths, 6ths, the #11 of the fixed figure), pad voicing
CHORDS = {
    'Em':   (40, {4, 7, 11, 2},  {6},     [52, 55, 59, 62]),
    'C':    (36, {0, 4, 7, 11},  {2, 6},  [48, 52, 55, 60]),
    'Am':   (45, {9, 0, 4, 7},   {11, 6, 2}, [45, 52, 55, 60]),
    'D':    (38, {2, 6, 9},      {4, 11, 7}, [50, 54, 57, 62]),
    'Bsus': (35, {11, 4, 6, 9},  {1},     [47, 52, 54, 57]),
}
HARM = ['Em'] * 8 + ['C'] * 4 + ['Am'] * 4 + ['C'] * 4 + ['D'] * 4 + ['Em'] * 4 + ['Am'] * 2 + ['Bsus'] * 2
assert len(HARM) == BARS


def chord(b):
    return HARM[b % BARS]


def part(name, b):
    b %= BARS
    return {
        'figA':  True,
        'pad':   b >= 4,
        'figB':  8 <= b < 30,
        'bass':  8 <= b < 30,
        'glock': 16 <= b < 30,
        'bell':  b == 30,
    }[name]


FIG_A = [64, 67, 71, 76, 74, 67, 66]            # E4 G4 | B4 E5 | D5 G4 F#4
FIG_A_D = [64, 69, 71, 76, 74, 69, 66]          # over D: G -> A (G4 was a semitone on the reed's F#4)
FIG_A_SUS = [64, 69, 71, 76, 71, 69, 66]        # over Bsus4: G -> A, D -> B
A_ACC = {0: 1.0, 2: 0.82, 4: 0.85}
# Am is E-D-C, a 4-3 sigh. (E-C-B left B3 held a semitone under the pad's C4.)
FIG_B = {'Em': [(67, 3), (66, 2), (62, 2)], 'C': [(67, 3), (64, 2), (62, 2)], 'Am': [(64, 3), (62, 2), (60, 2)],
         'D': [(66, 3), (64, 2), (62, 2)], 'Bsus': [(66, 3), (64, 2), (59, 2)]}
BASS = {k: [(v[0], 4), (v[0] + 12, 3)] for k, v in CHORDS.items()}

# glockenspiel melody: bar -> [(midi, eighths)], 7 eighths a bar. It sits at A5-B6, an octave
# above the piano figure. (At A4-B5 it sat inside the figure's E4-E5 and doubled its E5. Up here it
# stands 24 dB over the backing in its own band, against 18 dB before, at 2 dB less gain.)
GLOCK = {16: [(88, 4), (91, 3)], 17: [(95, 7)], 18: [(93, 4), (91, 3)], 19: [(88, 7)],
         20: [(86, 4), (90, 3)], 21: [(93, 7)], 22: [(91, 4), (90, 3)], 23: [(88, 7)],
         24: [(91, 7)], 25: [(93, 4), (91, 3)], 26: [(90, 4), (88, 3)], 27: [(88, 7)],
         28: [(88, 4), (84, 3)], 29: [(83, 4), (81, 3)]}
for _b, _m in GLOCK.items():
    assert sum(d for _, d in _m) == 7


def fig_a(b):
    return {'Bsus': FIG_A_SUS, 'D': FIG_A_D}.get(chord(b), FIG_A)


def check():
    bad = 0
    for b, mel in sorted(GLOCK.items()):
        pos = 0
        for m, d in mel:
            ch, (root, tones, colour, _) = chord(b), CHORDS[chord(b)]
            nxt = mel[mel.index((m, d)) + 1][0] if (m, d) != mel[-1] else None
            kind = 'ok ' if m % 12 in tones else ('col' if m % 12 in colour else 'BAD')
            if kind == 'BAD' and nxt is not None and 0 < abs(nxt - m) <= 2 and nxt % 12 in tones:
                kind = 'app'                       # an appoggiatura, resolved by step inside the bar
            iv = (m - root) % 12
            res = f' -> {_N[nxt % 12]}' if kind != 'ok ' and nxt is not None else ''
            print(f'  glock {kind} bar {b} eighth {pos} {_N[m % 12]}{m // 12 - 1} ({d}/8) over {ch} [+{iv}]{res}')
            bad += kind == 'BAD'
            pos += d
    for ch, notes in FIG_B.items():
        for i, (m, d) in enumerate(notes):
            tones, colour = CHORDS[ch][1], CHORDS[ch][2]
            kind = 'ok ' if m % 12 in tones else ('col' if m % 12 in colour else 'BAD')
            bad += kind == 'BAD'
            if kind != 'ok ':
                print(f'  figB  {kind} {ch}: {_N[m % 12]} ({d}/8), after {_N[notes[i - 1][0] % 12]}')
    for ch in CHORDS:
        b = HARM.index(ch)
        for i, m in enumerate(fig_a(b)):
            tones, colour = CHORDS[ch][1], CHORDS[ch][2]
            if m % 12 not in tones:
                kind = 'col' if m % 12 in colour else 'BAD'
                bad += kind == 'BAD'
                print(f'  figA  {kind} {ch}: eighth {i} {_N[m % 12]}' + (' (accented)' if i in A_ACC else ''))
    print(f'{bad} unintended non-chord tones')
    return bad


# ── instruments ─────────────────────────────────────────────────────────────
@lru_cache(maxsize=None)
def piano(m, acc):
    """A soft additive piano: eight slightly stretched partials, the upper ones
    dying faster, a felt thump; held a little past its eighth (half pedal)."""
    n = int(1.3 * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.zeros(n)
    for k in range(1, 9):
        fk = k * f * np.sqrt(1 + 0.0004 * k * k)
        if fk > 9000:
            break
        x += (acc ** (0.3 * k)) / k ** 0.6 * np.sin(2 * np.pi * fk * t + 0.7 * k) * np.exp(-t * (1.2 + 0.4 * k))
    z = np.random.default_rng(m).standard_normal(n)
    thump = (lp1(z, 700) * 0.2 + hp1(lp1(z, 5000), 1500) * 0.06) * np.exp(-t / 0.008)
    organ = 0.15 * (np.sin(4 * np.pi * f * t) + 0.5 * np.sin(8 * np.pi * f * t)) * adsr(n, 0.01, 0.1, 0.8, 0.08, 0.34)
    damp = np.clip((0.62 - t) / 0.18, 0, 1)
    return ((x + thump) * np.minimum(1, t / 0.003) * damp + organ) * acc


@lru_cache(maxsize=None)
def reed(m, d):
    """Figure B: a reedy organ, a narrow-ish pulse with a gentle low-pass and a
    touch of vibrato."""
    gate = d * E8 * 0.92
    n = int((gate + 0.2) * SR); t = np.arange(n) / SR
    f = hz(m) * 2 ** (0.08 / 12 * np.sin(2 * np.pi * 5.5 * t) * np.clip((t - 0.15) / 0.3, 0, 1))
    x = 0.6 * pulse(f, n, 0.38) + 0.4 * pulse(f * 1.003, n, 0.42, 0.3)
    x = lp(lp(x, 3500, 0.7), 5000, 0.7)
    return x * adsr(n, 0.012, 0.15, 0.7, 0.12, gate)


def drawbar(m, dur, sub=0.5):
    """The warm pad: 16', 8', 4' and a little 2 2/3', slow swell. The full 16' goes on
    the lowest voice only. On every voice it stacked E2-G2 and C2-E2 thirds, and over
    Bsus4 (which has no bass) a B1 E2 F#2 A2 cluster."""
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR
    f = hz(m); ph = 0.37 * (m % 7)
    x = (sub * np.sin(np.pi * f * t + ph) + np.sin(2 * np.pi * f * t + ph) + 0.35 * np.sin(4 * np.pi * f * t + ph)
         + 0.12 * np.sin(6 * np.pi * f * t + ph))
    return x * adsr(n, 0.7, 0.4, 0.9, 1.0, dur)


@lru_cache(maxsize=None)
def glock(m):
    """Free-bar partials 1 : 2.756 : 5.404. The upper two are kept faint and short, because
    at A5-B6 they reach 5-10 kHz. The buffer runs 3.2 s and fades to zero. (It used to stop
    at 2.2 s, a step 15 dB under the note.)"""
    n = int(3.2 * SR); t = np.arange(n) / SR
    f = hz(m)
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.9)
         + 0.10 * np.sin(2 * np.pi * 2.756 * f * t) * np.exp(-t / 0.22)
         + 0.02 * np.sin(2 * np.pi * 5.404 * f * t) * np.exp(-t / 0.05))
    return x * np.minimum(1, t / 0.0015) * np.clip((3.2 - t) / 0.8, 0, 1)


@lru_cache(maxsize=None)
def bass_note(m, d):
    gate = d * E8 * 0.9
    n = int((gate + 0.25) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t) + 0.08 * np.sin(6 * np.pi * f * t)
    return x * adsr(n, 0.02, 0.3, 0.7, 0.2, gate)


def tubular_bell(strike=52):
    """Partials of a free-free bar, (2k+1)^2 over the first, scaled so that
    modes 4-6 (about 2:3:4) imply the strike note. The low modes 2 and 3
    (about 102 and 199 Hz) are the deep, inharmonic 'bong' of the attack.
    They are kept weaker and shorter than the strike partials, as on a real
    chime, where they radiate poorly. So the tail that crosses the seam
    rings E4 and B4 over the bare Em opening, not a G#2-ish hum. The buffer
    runs 14 s and fades to zero. (At 9 s it stopped dead at loop time 3.75 s.)
    An FM clang (ratio 1.41) sits on the attack."""
    n = int(14.0 * SR); t = np.arange(n) / SR
    u = hz(strike) / 40.5
    x = np.zeros(n)
    for k, amp, tau in ((2, 0.22, 2.5), (3, 0.30, 3.0), (4, 1.00, 5.5), (5, 0.75, 4.2),
                        (6, 0.45, 2.6), (7, 0.22, 1.5), (8, 0.10, 0.9)):
        fk = u * (2 * k + 1) ** 2
        x += amp * np.sin(2 * np.pi * fk * t + k) * np.exp(-t / tau)
    x *= 1 + 0.08 * np.sin(2 * np.pi * 1.3 * t)                     # the slow beat of a real chime
    f = hz(strike)
    clang = np.sin(2 * np.pi * f * t + 3.0 * np.exp(-t / 0.25) * np.sin(2 * np.pi * 1.41 * f * t)) * np.exp(-t / 1.2)
    strike_tick = lp1(np.random.default_rng(30).standard_normal(n), 3000) * np.exp(-t / 0.005) * 0.3
    return lp((x + 0.35 * clang + strike_tick) * np.minimum(1, t / 0.002), 5000) * np.clip((14.0 - t) / 4.0, 0, 1)


def render(wav=None):
    pno, reedb, pad, glk, bass, bell = (tl.bus() for _ in range(6))
    BELL = tubular_bell()
    for b in tl.bars_range():
        t = b * BAR
        bb, ch = b % BARS, chord(b)
        root, tones, colour, voicing = CHORDS[ch]
        lift = 0.85 if bb < 4 else 1.0
        hum = rng('pno', bb).uniform(-1, 1, (7, 2))       # a player, not a sequencer: +-0.6 dB, +-4 ms
        for i, m in enumerate(fig_a(b)):
            acc = A_ACC.get(i, 0.7)
            pno.add(t + i * E8 + 0.004 * hum[i, 1] * (i > 0), piano(m, acc), pan=-0.25 + 0.08 * (i % 2),
                    gain=0.17 * lift * 10 ** (0.03 * hum[i, 0]))
        if part('figB', b):
            s = 0
            for m, d in FIG_B[ch]:
                reedb.add(t + s * E8, reed(m, d), pan=0.35, gain=(0.085 if s else 0.095) * (1.15 if bb >= 24 else 1.0))
                s += d
        if part('bass', b):
            s = 0
            for m, d in BASS[ch]:
                bass.add(t + s * E8, bass_note(m, d), gain=0.12 if s == 0 else 0.09)
                s += d
        if part('pad', b) and (bb == 4 or HARM[bb] != HARM[bb - 1]):
            run = 1
            while bb + run < BARS and HARM[bb + run] == HARM[bb]:
                run += 1
            g = 0.026 if bb < 8 else 0.038 if bb >= 24 else 0.031
            for k, m in enumerate(voicing):
                pad.add(t, drawbar(m, run * BAR, 0.5 if k == 0 else 0.1),
                        pan=-0.5 + k / max(len(voicing) - 1, 1), gain=g)
        if part('glock', b) and bb in GLOCK:
            s = 0
            for m, d in GLOCK[bb]:
                glk.add(t + s * E8, glock(m), pan=0.2, gain=0.12)
                s += d
        if part('bell', b):
            bell.add(t, BELL, pan=-0.05, gain=0.15)

    padx = chorus(pad.x, BAR, depth_ms=2.2, base_ms=8.0, mix=0.6, t0=tl.t0)
    reedx = chorus(reedb.x, BAR / 2, depth_ms=1.2, base_ms=5.0, mix=0.4, t0=tl.t0)
    glkx = glk.x + pingpong(glk.x, 3 * E8, 0.35, 4, 4000) * 0.6
    hall = make_ir(3.2, dark=5500, seed=23)
    wet = reverb(pno.x * 0.3 + reedx * 0.3 + padx * 0.25 + glkx * 0.45 + bell.x * 0.55 + bass.x * 0.05, hall)
    mix = pno.x + reedx + padx + glkx + bass.x + bell.x + wet * 0.5
    return finish(tl, mix, 'passive-past-perfect', wav=wav)


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(1 if check() else 0)
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
