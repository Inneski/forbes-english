#!/usr/bin/env python3
"""Block Camp soundtrack "Grand Hotel" (The Last Night at the Grand Hotel RPG).

Innes, 2026-10-03: "add some fitting music" (the Udio recording he had made
for it turned out corrupted). The game is a mountain grand hotel on its last
night: a ballroom, a vanished owner, a cable car and a deadline at midnight.
So: the idiom of a Mitteleuropean grand-hotel caper score - balalaikas in
tremolo carrying the tune, a cimbalom rocking under it, a wheezy harmonium
on the off-beats, a plucked contrabass oom-pah, sleigh bells for the snow, a
ticking clock, and one chime for midnight. An original piece in that idiom:
no melody or progression is taken from any film.

A minor, 112.5 BPM, 4/4 (a beat is exactly 25600 samples, a sixteenth 6400,
a bar 2.1333 s). One chord a bar:

  intro  Am  | Am | Dm | E7                         bars 0-3    clock and cimbalom alone, a timpani A
  A      Am  | Dm | E7 | Am | F | Dm | E7 | E7      bars 4-11   the tune on two balalaikas, oom-pah
  A'     Am  | Dm | E7 | Am | F | Dm | E7 | Am      bars 12-19  the tune again, alto balalaika an
                                                                octave down, glockenspiel, sleigh bells
  B      C   | G7 | C  | Am | F | Dm | G7 | C       bars 20-27  the ballroom: the harmonium sings,
                                                                balalaikas hold tremolo chords, clock
  turn   F   | Bb | E7 | E7                         bars 28-31  the Neapolitan Bb, a timpani roll on E,
                                                                the midnight chime, two ticks of silence

check_lines() proves the harmony at every render: every melody note a
quarter or longer, and every note on beat 1 or 3, is a tone of its chord.
The voicings carry no semitone, so long notes cannot rub; short passing
notes (the G# before A, the B before C) are the only dissonances.

Instruments, all synthesised here:
  Balalaika   Karplus-Strong strings (pines.py's string: fractional all-pass
              tuning, a ramp pick plus a little noise, a comb near the bridge),
              brighter loop filter, a short sustain; tremolo is a train of
              re-plucks into the SAME string, six a beat, down-strokes harder
              than up-strokes, so a held note shimmers as a real one does;
              a triangular body (resonances near 420 Hz and 1.6 kHz).
  Cimbalom    two strings a course 4.5 cents apart, struck (a bright pick, a
              hammer click), long ring, damped by the next chord.
  Harmonium   additive reeds (two or three, a few cents apart, a nasal
              formant near 1.15 kHz), slow bellows attack; staccato on the
              off-beats in A, legato for the B tune, pads in the intro and turn.
  Bass        a plucked contrabass string, root and fifth.
  Percussion  a woodblock clock (tick, tock), sleigh bells, glockenspiel,
              timpani (a hit on A, a roll on E), a hall-clock chime on E.
32 bars = 68.27 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/grand_hotel.py [--wav preview.wav]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, make_ir, reverb, finish)

NAME = 'grand-hotel'
BARS = 32
tl = Timeline(bpm=112.5, bars=BARS)
BAR, BEAT = tl.bar, tl.beat
E8 = BEAT / 2

# ── the changes ─────────────────────────────────────────────────────────────
CH = {
    'Am': dict(pcs={9, 0, 4}, root=45, fifth=40, pah=[57, 60, 64], pad=[57, 60, 64, 69], cim=[57, 64, 69, 72]),
    'Dm': dict(pcs={2, 5, 9}, root=38, fifth=45, pah=[57, 62, 65], pad=[57, 62, 65, 69], cim=[57, 62, 65, 69]),
    'E7': dict(pcs={4, 8, 11, 2}, root=40, fifth=47, pah=[56, 59, 62, 64], pad=[56, 59, 62, 64], cim=[56, 59, 64, 68]),
    'F':  dict(pcs={5, 9, 0}, root=41, fifth=48, pah=[57, 60, 65], pad=[57, 60, 65, 69], cim=[57, 60, 65, 69]),
    'C':  dict(pcs={0, 4, 7}, root=36, fifth=43, pah=[55, 60, 64], pad=[55, 60, 64, 67], cim=[55, 60, 64, 67]),
    'G7': dict(pcs={7, 11, 2, 5}, root=43, fifth=38, pah=[55, 59, 62, 65], pad=[55, 59, 62, 65], cim=[55, 59, 62, 65]),
    'Bb': dict(pcs={10, 2, 5}, root=46, fifth=41, pah=[53, 58, 62], pad=[53, 58, 62, 65], cim=[53, 58, 62, 65]),
}
CHORDS = (['Am', 'Am', 'Dm', 'E7'] +
          ['Am', 'Dm', 'E7', 'Am', 'F', 'Dm', 'E7', 'E7'] +
          ['Am', 'Dm', 'E7', 'Am', 'F', 'Dm', 'E7', 'Am'] +
          ['C', 'G7', 'C', 'Am', 'F', 'Dm', 'G7', 'C'] +
          ['F', 'Bb', 'E7', 'E7'])
assert len(CHORDS) == BARS


def section(lb):
    return 'intro' if lb < 4 else 'A' if lb < 12 else "A'" if lb < 20 else 'B' if lb < 28 else 'turn'


# ── the tunes: (midi, eighths) per bar, 0 = rest ─────────────────────────────
THEME = [
    [(69, 1), (72, 1), (76, 2), (81, 3), (80, 1)],              # Am  A C E A G#
    [(77, 2), (76, 1), (74, 1), (77, 3), (76, 1)],              # Dm  F E D F E
    [(74, 2), (71, 1), (68, 1), (71, 3), (74, 1)],              # E7  D B G# B D
    [(72, 2), (71, 1), (69, 1), (76, 4)],                       # Am  C B A E
    [(81, 2), (77, 1), (81, 1), (84, 3), (83, 1)],              # F   A F A C B
    [(81, 2), (77, 1), (74, 1), (77, 3), (76, 1)],              # Dm  A F D F E
]
BAL = {}                                         # loop bar -> the balalaika's bar
for k, row in enumerate(THEME):
    BAL[4 + k] = row; BAL[12 + k] = row
BAL[10] = [(74, 2), (76, 1), (77, 1), (76, 2), (74, 1), (71, 1)]     # E7  D E F E D B
BAL[11] = [(68, 2), (71, 2), (76, 4)]                                 # E7  G# B E, a half close
BAL[18] = [(74, 2), (72, 1), (71, 1), (68, 2), (71, 2)]               # E7  D C B G# B
BAL[19] = [(69, 4), (0, 2), (67, 1), (71, 1)]                         # Am  A, then G B up into C
BAL[28] = [(84, 2), (81, 2), (77, 2), (72, 2)]                        # F   C A F C
BAL[29] = [(74, 2), (77, 2), (82, 4)]                                 # Bb  D F Bb
BAL[30] = [(80, 2), (76, 2), (74, 2), (71, 2)]                        # E7  G# E D B
BAL[31] = [(76, 4), (0, 4)]                                           # E7  E, and the chime
HARM = {                                                              # the B tune, harmonium
    20: [(72, 2), (76, 2), (79, 4)],                                  # C   C E G
    21: [(77, 4), (74, 2), (71, 2)],                                  # G7  F D B
    22: [(72, 2), (76, 2), (79, 2), (84, 2)],                         # C   C E G C
    23: [(81, 6), (79, 1), (76, 1)],                                  # Am  A (G E)
    24: [(77, 4), (81, 2), (77, 2)],                                  # F   F A F
    25: [(74, 4), (77, 2), (81, 2)],                                  # Dm  D F A
    26: [(79, 2), (77, 2), (74, 2), (71, 2)],                         # G7  G F D B
    27: [(72, 6), (0, 2)],                                            # C   C
}
for row in list(BAL.values()) + list(HARM.values()):
    assert sum(d for _, d in row) == 8, row


def check_lines():
    """Every melody note of a quarter or longer, and every one on beat 1 or 3,
    is a chord tone; so is every bass note. The voicings carry no semitone or
    minor ninth, so no two long notes can rub."""
    bad = []
    for name, tune in (('balalaika', BAL), ('harmonium', HARM)):
        for lb, row in tune.items():
            pos = 0
            for m, d in row:
                if m and (d >= 2 or pos % 4 == 0) and m % 12 not in CH[CHORDS[lb]]['pcs']:
                    bad.append((name, lb, pos, m, CHORDS[lb]))
                pos += d
    for c, v in CH.items():
        for key in ('root', 'fifth'):
            if v[key] % 12 not in v['pcs']:
                bad.append(('bass', c, key))
        for key in ('pah', 'pad', 'cim'):
            if any(m % 12 not in v['pcs'] for m in v[key]):
                bad.append((key, c))
            ms = sorted(v[key])
            if any((hi - lo) in (1, 13) for i, lo in enumerate(ms) for hi in ms[i + 1:]):
                bad.append((key, c, 'semitone'))
    print('lines vs chords:', 'every long or strong note is a chord tone' if not bad else bad)
    assert not bad, 'a wrong note (listed above)'


# ── strings: Karplus-Strong, as pines.py ────────────────────────────────────
def ks_setup(f, a, t60):
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
    return N, c, den


def pick(N, f, tilt, noise, comb, seed, top=6000):
    """One period of a band-limited ramp (harmonics falling as 1/k^tilt),
    a little noise, and a comb for where the string is plucked."""
    kk = np.arange(1, int(max(2, min(48, top / f))) + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -tilt * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    exc += noise * lp1(np.random.default_rng(seed).uniform(-1, 1, N), 3500)
    k = max(1, int(comb * N))
    exc[k:] -= 0.5 * exc[:-k]
    return exc / np.abs(exc).max()


def balalaika(m, dur, v, seed, cents=0.0, trem=True, rate=6, offset=0.0):
    """A held note is a tremolo: re-plucks into the one string, `rate` a beat,
    down-strokes harder than up-strokes. A short note is a single pluck."""
    f = hz(m) * 2 ** (cents / 1200)
    N, c, den = ks_setup(f, 0.86, 1.4)
    exc = pick(N, f, 0.62, 0.22, 0.13, seed, top=9000)
    rel = 0.08
    n = int((dur + rel + 0.02) * SR)
    x = np.zeros(n)
    r = rng('bal', seed)
    if trem and dur >= BEAT * 0.95:
        step, k, tt = BEAT / rate, 0, offset
        while tt < dur - step * 0.5:
            i = int(round(tt * SR))
            a = (1.15 if k == 0 else 1.0 if k % 2 == 0 else 0.72) * (1 + 0.1 * (r.random() - 0.5))
            j = min(n, i + N)
            x[i:j] += (exc if k % 2 == 0 else -exc)[:j - i] * a * v
            k += 1; tt += step
    else:
        x[:min(N, n)] += exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    return y * np.clip((dur + rel - t) / rel, 0, 1)


def cimbalom(m, ring, v, seed):
    f0 = hz(m)
    n = int((ring + 0.12) * SR)
    out = np.zeros(n)
    t60 = float(np.interp(m, [50, 90], [4.0, 2.0]))
    for j, cents in enumerate((-2.3, 2.2)):
        f = f0 * 2 ** (cents / 1200)
        N, c, den = ks_setup(f, 0.9, t60)
        exc = pick(N, f, 0.5, 0.12, 0.11, seed * 3 + j, top=11000)
        x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
        out += lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    click = lp1(np.random.default_rng(seed).standard_normal(n), 2500) * np.exp(-t / 0.003) * 0.25 * v
    out = out * 0.5 + click
    return out * np.clip((ring + 0.1 - t) / 0.1, 0, 1)


def bass(m, dur, v, seed):
    f = hz(m)
    N, c, den = ks_setup(f, 0.55, 1.7)
    exc = pick(N, f, 1.5, 0.04, 0.2, seed, top=1400)
    n = int((dur + 0.09) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    y = y + 0.5 * bp(y, 2.2 * f, 1.0)
    t = np.arange(n) / SR
    return y * np.clip((dur + 0.08 - t) / 0.08, 0, 1)


# ── harmonium: additive reeds ───────────────────────────────────────────────
def reed(m, dur, reeds=((-5, 0.13), (5, 0.71)), attack=0.06, release=0.12, decay_to=0.9):
    n = int((dur + release + 0.02) * SR); t = np.arange(n) / SR
    f0 = hz(m)
    x = np.zeros(n)
    for cents, ph0 in reeds:
        f = f0 * 2 ** (cents / 1200)
        for k in range(1, int(min(26, 8500 / f)) + 1):
            fk = k * f
            a = k ** -1.15 * (1 + 1.3 * np.exp(-((fk - 1150) / 420) ** 2) + 0.5 * np.exp(-((fk - 2700) / 650) ** 2))
            x += a * np.sin(2 * np.pi * fk * t + 2 * np.pi * k * ph0)
    x /= len(reeds)
    env = adsr(n, attack, 0.15, decay_to, release, dur) * (1 + 0.025 * np.sin(2 * np.pi * 0.8 * t))
    return x * env


# ── percussion and bells ────────────────────────────────────────────────────
def block(freq, seed):
    n = int(0.09 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = (np.sin(2 * np.pi * freq * t) * np.exp(-t / 0.013) + 0.35 * np.sin(2 * np.pi * 1.58 * freq * t) * np.exp(-t / 0.007)
         + 0.25 * bp(z, freq * 1.3, 3.0) * np.exp(-t / 0.004))
    return x * np.minimum(1, t / 0.0005)


def jingle(seed):
    r = rng('jingle', seed)
    n = int(0.24 * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for _ in range(16):
        i0 = int(r.uniform(0, 0.04) * SR); tt = t[:n - i0]
        f = r.uniform(4200, 8600); tau = r.uniform(0.025, 0.08)
        x[i0:] += r.uniform(0.4, 1) * np.sin(2 * np.pi * f * tt + r.uniform(0, 6.28)) * np.exp(-tt / tau) \
            * (1 + 0.5 * np.sin(2 * np.pi * 1.47 * f * tt))
    x += 0.2 * hp(np.random.default_rng(seed + 7).standard_normal(n), 6000) * np.exp(-t / 0.03)
    return x / np.abs(x).max()


def glock(m, v=1.0):
    f = hz(m); n = int(1.6 * SR); t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.85) + 0.25 * np.sin(2 * np.pi * 2.756 * f * t) * np.exp(-t / 0.16)
         + 0.07 * np.sin(2 * np.pi * 5.404 * f * t) * np.exp(-t / 0.05))
    return x * np.minimum(1, t / 0.0008) * v


def timp(m, v, seed, length=2.4):
    f = hz(m); n = int(length * SR); t = np.arange(n) / SR
    bend = np.cumsum(1 + 0.012 * np.exp(-t / 0.08)) / SR             # the head settles after the strike
    x = np.zeros(n)
    for r_, a, tau in ((1, 1, 1.1), (1.5, 0.5, 0.7), (1.98, 0.32, 0.5), (2.44, 0.16, 0.35), (2.92, 0.08, 0.25)):
        x += a * np.sin(2 * np.pi * f * r_ * bend) * np.exp(-t / tau)
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.5 * lp(z, 320) * np.exp(-t / 0.02)
    return x * np.minimum(1, t / 0.002) * v


def chime(m):
    f = hz(m); n = int(4.6 * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for r_, a, tau in ((1, 1, 3.0), (2, 0.42, 1.7), (3, 0.22, 0.95), (4.07, 0.1, 0.55), (5.2, 0.04, 0.3)):
        x += a * np.sin(2 * np.pi * f * r_ * t) * np.exp(-t / tau)
    return x * np.minimum(1, t / 0.0015)


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    check_lines()
    bal, cim, harm, low, perc_, bells = (tl.bus() for _ in range(6))
    for b in tl.bars_range():
        t = b * BAR
        lb = b % BARS
        sec, c = section(lb), CHORDS[lb]
        v = CH[c]
        nxt_change = BAR                         # every chord lasts a bar

        # cimbalom: the rocking figure (intro, A, A'), a spread chord (B),
        # sixteenth runs (turn)
        if sec in ('intro', 'A', "A'"):
            pat = [0, 1, 2, 1, 3, 1, 2, 1]
            g = {'intro': 0.8, 'A': 0.48, "A'": 0.54}[sec]
            for k, ix in enumerate(pat):
                m = v['cim'][ix]
                ring = nxt_change - k * E8
                cim.add(t + k * E8, cimbalom(m, min(ring, 1.4), 0.9 if k % 2 == 0 else 0.7, lb * 16 + k),
                        pan=-0.3 + (m - 55) / 30 * 0.8, gain=g)
        elif sec == 'B':
            for k, m in enumerate(v['cim']):
                cim.add(t + k * BEAT / 4, cimbalom(m, BAR - k * BEAT / 4, 0.8, lb * 16 + k),
                        pan=-0.3 + (m - 55) / 30 * 0.8, gain=0.38)
        elif lb < 31:
            run = sorted(set(v['cim'] + [p + 12 for p in v['cim']]))[:8]
            seq = run + run[::-1]
            for k in range(16):
                m = seq[k % len(seq)]
                cim.add(t + k * BEAT / 4, cimbalom(m, min(BAR - k * BEAT / 4, 0.9), 0.75, lb * 16 + k),
                        pan=-0.3 + (m - 55) / 30 * 0.8, gain=0.4)

        # bass and the off-beat "pah"
        if sec == 'intro':
            low.add(t, bass(v['root'], BAR * 0.95, 0.9, lb), gain=0.3)
        elif sec in ('A', "A'"):
            for q, key in ((0, 'root'), (2, 'fifth')):
                low.add(t + q * BEAT, bass(v[key], BEAT * 0.85, 1.0, lb * 4 + q), gain=0.33)
            for q in (1, 3):
                for k, m in enumerate(v['pah']):
                    harm.add(t + q * BEAT, reed(m, 0.17, attack=0.012, release=0.07),
                             pan=-0.15 + 0.1 * k, gain=0.05)
                    bal.add(t + q * BEAT + k * 0.011, balalaika(m, 0.2, 0.7, lb * 40 + q * 4 + k, trem=False),
                            pan=0.4, gain=0.13)
                if sec == "A'":
                    bells.add(t + q * BEAT, jingle(lb * 4 + q), pan=0.55, gain=0.05)
        elif sec == 'B':
            low.add(t, bass(v['root'], BEAT * 1.9, 1.0, lb * 4), gain=0.33)
            low.add(t + 2 * BEAT, bass(v['fifth'], BEAT * 1.9, 0.9, lb * 4 + 2), gain=0.3)
            for k, m in enumerate(v['pad'][:3]):
                bal.add(t, balalaika(m, BAR * 0.97, 0.45, lb * 40 + k, cents=(-3, 0, 3)[k], rate=5,
                                     offset=k * BEAT / 15),
                        pan=(-0.45, 0.0, 0.45)[k], gain=0.24)
        else:                                    # turn
            if lb < 30:
                for q, key in ((0, 'root'), (2, 'fifth')):
                    low.add(t + q * BEAT, bass(v[key], BEAT * 1.8, 1.0, lb * 4 + q), gain=0.33)
            elif lb == 30:
                for q in range(4):
                    low.add(t + q * BEAT, bass(v['root'], BEAT * 0.8, 0.9, lb * 4 + q), gain=0.3)
            else:
                low.add(t, bass(v['root'], BEAT * 1.9, 1.0, lb * 4), gain=0.33)
            pad_len = BEAT * 1.9 if lb == 31 else BAR * 0.98
            for k, m in enumerate(v['pad']):
                harm.add(t, reed(m, pad_len, attack=0.25, release=0.3), pan=-0.3 + 0.2 * k, gain=0.045)

        # the intro's harmonium pads, swelling in under the cimbalom
        if sec == 'intro' and lb >= 2:
            for k, m in enumerate(v['pad']):
                harm.add(t, reed(m, BAR * 0.98, attack=0.6, release=0.35), pan=-0.3 + 0.2 * k, gain=0.04)

        # the tunes
        if lb in BAL:
            pos = 0
            for m, d in BAL[lb]:
                if m:
                    dur = d * E8
                    acc = 1.0 if pos % 4 == 0 else 0.85
                    seed = lb * 64 + pos * 4
                    bal.add(t + pos * E8, balalaika(m, dur, acc, seed, cents=-3), pan=-0.22, gain=0.32)
                    bal.add(t + pos * E8 + 0.006, balalaika(m, dur, acc * 0.9, seed + 1, cents=3.5, rate=6,
                                                           offset=BEAT / 14), pan=0.25, gain=0.28)
                    if sec == "A'":
                        bal.add(t + pos * E8 + 0.004, balalaika(m - 12, dur, acc * 0.8, seed + 2, rate=6,
                                                               offset=BEAT / 9), pan=-0.5, gain=0.2)
                        if d >= 2:
                            bells.add(t + pos * E8, glock(m + 12), pan=0.3, gain=0.07)
                pos += d
        if lb in HARM:
            pos = 0
            for m, d in HARM[lb]:
                if m:
                    harm.add(t + pos * E8, reed(m, d * E8 * 0.98, reeds=((-6, 0.13), (0, 0.41), (6, 0.77)),
                                                attack=0.05, release=0.1), pan=0.05, gain=0.14)
                pos += d

        # the clock: tick on 1 and 3, tock on 2 and 4 (intro, B, turn)
        if sec in ('intro', 'B', 'turn'):
            for q in range(4):
                perc_.add(t + q * BEAT, block(2350 if q % 2 == 0 else 1700, lb * 4 + q), pan=0.45,
                          gain=0.055 if sec != 'B' else 0.045)

        # timpani: A at the top of the loop, a roll on E into the chime
        if lb == 0:
            perc_.add(t, timp(45, 1.0, 900), pan=-0.15, gain=0.2)
        if lb == 30:
            steps = 24
            for k in range(steps):
                vv = 0.12 + 0.6 * (k / steps) ** 1.6
                perc_.add(t + k * BEAT / 6, timp(40, vv, 910 + k, length=0.9), pan=-0.15, gain=0.18)
        if lb == 31:
            perc_.add(t, timp(40, 1.0, 950), pan=-0.15, gain=0.22)
            bells.add(t, chime(76), pan=0.0, gain=0.16)
            bells.add(t + 0.004, chime(64), pan=0.0, gain=0.1)

    # the balalaikas' triangular body; a little air off the cimbalom's lows
    bx = bal.x + 0.6 * bp(bal.x, 420, 1.4) + 0.4 * bp(bal.x, 1600, 1.8) + 0.15 * bp(bal.x, 3200, 1.2)
    bx = hp1(bx, 140)
    cx = hp1(cim.x, 160)
    hall = make_ir(1.9, dark=5200, seed=81, pre=0.02)
    dry = bx + cx + harm.x + low.x + perc_.x + bells.x
    wet = reverb(bx * 0.35 + cx * 0.45 + harm.x * 0.4 + perc_.x * 0.35 + bells.x * 0.5 + low.x * 0.06, hall)
    mix = dry + wet * 0.5
    for nm, bus in (('balalaika', bx), ('cimbalom', cx), ('harmonium', harm.x), ('bass', low.x),
                    ('percussion', perc_.x), ('bells', bells.x)):
        print('  %-11s rms %6.1f dB rel. mix' % (nm, 20 * np.log10(np.sqrt(np.mean(bus ** 2)) / np.sqrt(np.mean(mix ** 2)) + 1e-12)))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
