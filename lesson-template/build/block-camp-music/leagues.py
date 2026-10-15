#!/usr/bin/env python3
"""Block Camp soundtrack "Twenty Thousand Leagues" (The Sealed Log RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is the same
voyage as Nautilus: The Black Archive told the other way round: the
Nautilus came home in 1868, her log was sealed, and the player reads it,
every entry looking back at what had already happened in the dark. So the
idiom here is Victorian, not electronic: Captain Nemo's pipe organ in the
salon, a cello and a string section, a harp, a cylinder music box that
opens the log, a celesta for the marvels at the salon window, a marine
chronometer beating half-seconds, timpani and the hull groaning under the
pressure. An original piece in that idiom; no melody or progression is
taken from any film, opera or hymn.

C minor (B natural only in the G chord), 3/4 at 60 a minute: a beat is a
second, an eighth half a second (the chronometer's beat), a bar 3 s. The
Timeline is told bpm=80 so its 4-beat "bar" is one 3/4 bar. One chord a bar:

  intro  Cm | Ab | Fm | G                          bars 0-3    the music box plays the head of the
                                                               theme; chronometer, a soft flute stop
  A      Cm | Fm | Bb | Eb | Ab | Fm | G | G       bars 4-11   pressure: the cello theme over the
                                                               organ chorale and a 16' pedal, the hull
  B      Eb | Bb/D | Cm | Gm/Bb | Ab | Eb/G | Fm7 | Bb7
                                                   bars 12-19  wonder: violins in Eb, harp arpeggios,
                                                               celesta, pizzicato basses; the organ rests
  A''    Cm | Fm | Bb | Eb | Ab | Fm | G | G       bars 20-27  the theme on violins an octave up, the
                                                               cello as written, full organ, harp; a
                                                               timpani roll on G hands back to the box

The theme (A, eighths): C4- G4-- Ab4 | Ab4- G4 F4 C4- | D4- F4-- G4 | Bb4---- Ab4 G4 |
C5-- Bb4 Ab4- | Ab4- F4- C4- | B3- D4- G4- | G4---- F4 D4 - a rising fifth with a
sigh on the minor sixth above it, then a slow fall through the circle.

check_lines() proves the harmony at import: every line note a quarter or
longer, or on the downbeat, is a tone of its chord, and none of them sits a
semitone, major seventh or minor ninth from the bass or from anything the
organ, harp or string pad holds there; the voicings are chord tones without
a semitone inside them; every note is in C minor (B natural only over G);
the timpani are tuned to C and G and only strike under chords that hold them.
Strings that ring - harp, music box, celesta - are damped at a change of
chord when their note is not in the new chord, as a player's hand would.

Instruments, all synthesised here:
  Organ       additive flue pipes - an 8' principal, a 4' octave, a stopped
              8' flute, a 16' bourdon in the pedal - each rank a cent or two
              off the next, a chiff of wind at the speech, common tones held.
  Strings     band-limited saws, several a section, each with its own slow
              vibrato and a cent or so of detune, through a body (resonances
              at 280 Hz, 1.1 and 2.9 kHz) and a little bow noise: a solo-ish
              cello (two voices) and a violin section (five).
  Harp        Karplus-Strong strings (one IIR each, all-pass tuned), a bright
              pluck near the middle of the string, long ring.
  Music box   comb tines: a fundamental with the beam's inharmonic modes
              (6.27 and 17.55 times) that die fast, a pluck tick.
  Celesta     struck bars: fundamental and a quiet fourth harmonic.
  Pizzicato   low KS strings, short ring, in B.
  Timpani     C2 and G2, a strike at A and A'', a roll into the loop's top.
  Chronometer a half-second tick and tock, high and fine.
  Hull        a groan every four bars in A and A'' (noise through a band
              that slides down, no fixed pitch), and a low sea rumble.
28 bars = 84 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/leagues.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

NAME = 'twenty-thousand-leagues'
BARS = 28
tl = Timeline(bpm=80, bars=BARS)
BEAT = 1.0
E8 = 0.5
BAR = 3.0
assert abs(tl.bar - BAR) < 1e-12
LOOP = tl.loop

KEY = {0, 2, 3, 5, 7, 8, 10}                      # C natural minor; B natural only over G

# ── the changes ─────────────────────────────────────────────────────────────
#  bass: the pedal / pizzicato note; organ: manual voicing; harp: six notes
#  for the broken chord, low to high; pad: the string pad in B
CH = {
    'Cm':    dict(pcs={0, 3, 7}, bass=36, organ=[55, 60, 63, 67], harp=[48, 55, 60, 63, 67, 72], pad=[55, 60, 63]),
    'Fm':    dict(pcs={5, 8, 0}, bass=41, organ=[56, 60, 65, 68], harp=[41, 48, 53, 56, 60, 65], pad=[56, 60, 65]),
    'Bb':    dict(pcs={10, 2, 5}, bass=34, organ=[53, 58, 62, 65], harp=[46, 53, 58, 62, 65, 70], pad=[53, 58, 62]),
    'Eb':    dict(pcs={3, 7, 10}, bass=39, organ=[55, 58, 63, 67], harp=[39, 46, 51, 55, 58, 63], pad=[55, 58, 63]),
    'Ab':    dict(pcs={8, 0, 3}, bass=44, organ=[56, 60, 63, 68], harp=[44, 51, 56, 60, 63, 68], pad=[56, 60, 63]),
    'G':     dict(pcs={7, 11, 2}, bass=43, organ=[55, 59, 62, 67], harp=[43, 50, 55, 59, 62, 67], pad=[55, 59, 62]),
    'Bb/D':  dict(pcs={10, 2, 5}, bass=38, organ=[53, 58, 62, 65], harp=[38, 46, 53, 58, 62, 65], pad=[53, 58, 62]),
    'Gm/Bb': dict(pcs={7, 10, 2}, bass=34, organ=[55, 58, 62, 67], harp=[46, 50, 55, 58, 62, 67], pad=[55, 58, 62]),
    'Eb/G':  dict(pcs={3, 7, 10}, bass=43, organ=[55, 58, 63, 67], harp=[43, 51, 55, 58, 63, 67], pad=[55, 58, 63]),
    'Fm7':   dict(pcs={5, 8, 0, 3}, bass=41, organ=[56, 60, 63, 68], harp=[41, 48, 51, 56, 60, 63], pad=[56, 60, 63]),
    'Bb7':   dict(pcs={10, 2, 5, 8}, bass=34, organ=[53, 56, 62, 65], harp=[46, 53, 56, 62, 65, 70], pad=[53, 56, 62]),
}
A_PROG = ['Cm', 'Fm', 'Bb', 'Eb', 'Ab', 'Fm', 'G', 'G']
B_PROG = ['Eb', 'Bb/D', 'Cm', 'Gm/Bb', 'Ab', 'Eb/G', 'Fm7', 'Bb7']
PROG = ['Cm', 'Ab', 'Fm', 'G'] + A_PROG + B_PROG + A_PROG
assert len(PROG) == BARS


def section(lb):
    lb %= BARS
    return 'intro' if lb < 4 else 'A' if lb < 12 else 'B' if lb < 20 else "A''"


# ── the lines: (midi, eighths) per bar, six eighths a bar, 0 = rest ─────────
THEME = [
    [(60, 2), (67, 3), (68, 1)],                     # Cm   C G (Ab)
    [(68, 2), (67, 1), (65, 1), (60, 2)],            # Fm   Ab (G F) C
    [(62, 2), (65, 3), (67, 1)],                     # Bb   D F (G)
    [(70, 4), (68, 1), (67, 1)],                     # Eb   Bb (Ab G)
    [(72, 3), (70, 1), (68, 2)],                     # Ab   C (Bb) Ab
    [(68, 2), (65, 2), (60, 2)],                     # Fm   Ab F C
    [(59, 2), (62, 2), (67, 2)],                     # G    B D G
    [(67, 4), (65, 1), (62, 1)],                     # G    G (F D)
]
WONDER = [
    [(70, 2), (75, 4)],                              # Eb     Bb Eb
    [(74, 3), (72, 1), (70, 2)],                     # Bb/D   D (C) Bb
    [(72, 2), (75, 2), (79, 2)],                     # Cm     C Eb G
    [(79, 4), (77, 1), (74, 1)],                     # Gm/Bb  G (F D)
    [(75, 3), (72, 1), (80, 2)],                     # Ab     Eb (C) Ab
    [(79, 4), (77, 1), (75, 1)],                     # Eb/G   G (F Eb)
    [(77, 2), (75, 2), (72, 2)],                     # Fm7    F Eb C
    [(74, 4), (70, 2)],                              # Bb7    D Bb
]
BOX = [                                              # the music box: the head, two octaves up
    [(84, 2), (91, 3), (92, 1)],                     # Cm  C G (Ab)
    [(87, 2), (84, 2), (80, 2)],                     # Ab  Eb C Ab
    [(89, 3), (87, 1), (84, 2)],                     # Fm  F (Eb) C
    [(83, 2), (86, 2), (91, 2)],                     # G   B D G
]
CELLO, VIOLIN, MUSICBOX = {}, {}, {}
for k, row in enumerate(THEME):
    CELLO[4 + k] = row
    CELLO[20 + k] = row
    VIOLIN[20 + k] = [(m + 12 if m else 0, d) for m, d in row]
for k, row in enumerate(WONDER):
    VIOLIN[12 + k] = row
for k, row in enumerate(BOX):
    MUSICBOX[k] = row
LINES = (('cello', CELLO), ('violin', VIOLIN), ('music box', MUSICBOX))
for _, table in LINES:
    for row in table.values():
        assert sum(d for _, d in row) == 6, row


def notes_of(table, lb):
    out, pos = [], 0
    for m, d in table.get(lb % BARS, []):
        if m:
            out.append((pos, m, d))
        pos += d
    return out


# what sounds under a line in each section (for the rub check)
def held(lb):
    c = CH[PROG[lb]]; sec = section(lb)
    out = [c['bass']]
    if sec in ('intro', 'A', "A''"):
        out += c['organ']
    if sec in ('B', "A''"):
        out += c['harp']
    if sec == 'B':
        out += c['pad']
    return out


TIMP = {4: 36, 20: 36, 26: 43, 27: 43}               # bar -> C2 / G2


def in_key(m, chord):
    return m % 12 in KEY or (m % 12 == 11 and chord == 'G')


def check_lines():
    bad = []
    for name, table in LINES:
        for lb in table:
            c = PROG[lb]
            for pos, m, d in notes_of(table, lb):
                if not in_key(m, c):
                    bad.append((name, lb, pos, m, 'out of key'))
                if (d >= 2 or pos == 0) and m % 12 not in CH[c]['pcs']:
                    bad.append((name, lb, pos, m, c, 'not a chord tone'))
                if d >= 2 and any(abs(m - o) in (1, 11, 13) for o in held(lb)):
                    bad.append((name, lb, pos, m, c, 'rubs'))
    for c, v in CH.items():
        if v['bass'] % 12 not in v['pcs']:
            bad.append(('bass', c))
        for key in ('organ', 'harp', 'pad'):
            ms = sorted(v[key] + [v['bass']])
            if any(m % 12 not in v['pcs'] for m in v[key]):
                bad.append((key, c, 'not a chord tone'))
            if any((hi - lo) in (1, 11, 13) for i, lo in enumerate(ms) for hi in ms[i + 1:]):
                bad.append((key, c, 'semitone'))
            if any(not in_key(m, c) for m in ms):
                bad.append((key, c, 'out of key'))
    for lb, m in TIMP.items():
        if m % 12 not in CH[PROG[lb]]['pcs']:
            bad.append(('timpani', lb, m))
    print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad)
    assert not bad, 'a wrong note (listed above)'


check_lines()


def ring_for(t_abs, m, ring):
    """How long a ringing string may sound: until `ring` runs out, or until
    the first change of chord whose chord does not hold its note."""
    b = int(np.floor(t_abs / BAR + 1e-9))
    tc = (b + 1) * BAR
    while tc < t_abs + ring:
        if m % 12 not in CH[PROG[(int(round(tc / BAR))) % BARS]]['pcs']:
            return tc - t_abs
        tc += BAR
    return ring


# ── oscillators ─────────────────────────────────────────────────────────────
def blep(ph, dt):
    y = np.zeros_like(ph)
    a = ph < dt; u = ph[a] / dt[a]; y[a] = 2 * u - u * u - 1
    z = ph > 1 - dt; u = (ph[z] - 1) / dt[z]; y[z] = u * u + 2 * u + 1
    return y


def blsaw(f, n, ph0=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,)); dt = f / SR
    ph = (ph0 + np.cumsum(dt)) % 1.0
    return 2 * ph - 1 - blep(ph, dt)


def tail(n, sec=0.03):
    k = min(n, int(sec * SR)); w = np.ones(n)
    w[n - k:] = 0.5 + 0.5 * np.cos(np.linspace(0, np.pi, k))
    return w


# ── organ ───────────────────────────────────────────────────────────────────
RANKS = {   # name: (pitch ratio, level, harmonic amplitudes, cents)
    'principal': (1.0, 1.0, (1, .5, .32, .22, .14, .1, .07, .05, .035, .025, .018), 0.0),
    'octave':    (2.0, 0.42, (1, .45, .25, .14, .08, .05, .03), 1.6),
    'flute':     (1.0, 0.8, (1, .04, .22, .02, .06, .01, .02), -1.2),
    'bourdon':   (0.5, 1.0, (1, .05, .3, .03, .1, .01, .03), 0.0),
}


def pipe(m, dur, ranks, key, attack=0.07, release=0.14):
    n = int((dur + release + 0.05) * SR); t = np.arange(n) / SR; r = rng('pipe', key)
    f0 = hz(m); x = np.zeros(n)
    for rk in ranks:
        ratio, lvl, harm, cents = RANKS[rk]
        f = f0 * ratio * 2 ** (cents / 1200)
        for k, a in enumerate(harm, 1):
            if k * f > 9000:
                break
            sp = np.minimum(1, t / (attack * (0.6 + 0.8 / k)))       # high harmonics speak first
            x += lvl * a * np.sin(2 * np.pi * k * f * t + r.uniform(0, 6.28)) * sp
    z = r.standard_normal(n)
    chiff = bp(z, min(f0 * 4, 6000), 3.0) * np.exp(-t / 0.03) * 0.5 + hp(z, 3000) * np.exp(-t / 0.02) * 0.05
    env = adsr(n, 0.015, 0.1, 1.0, release, dur)
    return (x + chiff) * env * tail(n)


# ── strings ─────────────────────────────────────────────────────────────────
def bowed(m, dur, key, voices=5, attack=0.18, release=0.28, bright=1.0):
    n = int((dur + release + 0.05) * SR); t = np.arange(n) / SR; r = rng('bow', key)
    f0 = hz(m); x = np.zeros(n)
    for v in range(voices):
        det = r.uniform(-7, 7) if voices > 1 else 0.0
        vr = r.uniform(5.0, 6.2); vd = r.uniform(0.0025, 0.0045)
        onset = r.uniform(0.15, 0.35)
        vib = 1 + vd * np.clip((t - onset) / 0.4, 0, 1) * np.sin(2 * np.pi * vr * t + r.uniform(0, 6.28))
        x += blsaw(f0 * 2 ** (det / 1200) * vib, n, r.random())
    x /= voices
    y = 0.55 * lp(x, 1800 + 2600 * bright, 0.7) + 0.6 * bp(x, 280, 1.6) + 0.45 * bp(x, 1100, 1.8) \
        + 0.3 * bright * bp(x, 2900, 2.2)
    bow = hp(r.standard_normal(n), 2500) * 0.02 * bright
    env = adsr(n, attack, 0.3, 0.9, release, dur)
    return (y + bow) * env


# ── plucked and struck ──────────────────────────────────────────────────────
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


def pick(N, f, tilt, noise, comb, seed, top=8000):
    """One period of the pluck: harmonics falling as 1/k^tilt, a little noise,
    a comb for where the string is plucked. All of it periodic in N - the
    comb wraps and the noise is built from whole harmonics - so the string
    does not click when the loop first comes round (grand_hotel's pick,
    with a linear comb and filtered white noise, jumps there by ~15 dB)."""
    K = int(max(2, min(48, top / f)))
    kk = np.arange(1, K + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -tilt * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    r = np.random.default_rng(seed)
    kn = np.arange(1, N // 2)[:, None] if N < 400 else np.arange(1, 200)[:, None]
    nz = (np.sin(2 * np.pi * kn * ph + r.uniform(0, 2 * np.pi, (len(kn), 1)))
          / (1 + (kn * f / 4000.0) ** 2)).sum(0)
    exc += noise * nz / (np.abs(nz).max() + 1e-12)
    exc -= 0.5 * np.roll(exc, max(1, int(comb * N)))
    # start the period at its quietest sample: the pluck then begins at zero,
    # and the loop's all-pass, which first answers with c * y[0], has nothing
    # to step on (a 0.25 start put a one-sample notch in every period)
    exc = np.roll(exc, -int(np.argmin(np.abs(exc))))
    return exc / np.abs(exc).max()


def harp(m, dur, v, seed):
    f = hz(m)
    t60 = float(np.interp(m, [36, 84], [5.0, 2.2]))
    N, c, den = ks_setup(f, 0.8, t60)
    exc = pick(N, f, 0.9, 0.08, 0.48, seed, top=7000)            # plucked mid-string: round
    n = int((dur + 0.05) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    return y * np.clip((dur + 0.04 - t) / 0.04, 0, 1)


def pizz(m, v, seed):
    f = hz(m); N, c, den = ks_setup(f, 0.55, 0.9)
    exc = pick(N, f, 1.4, 0.05, 0.25, seed, top=1800)
    n = int(1.2 * SR); x = np.zeros(n); x[:N] = exc * v
    y = lfilter([1.0, c], den, x)
    y = y + 0.6 * bp(y, 2.1 * f, 1.2)
    return y * tail(n, 0.1)


def music_box(m, dur):
    f = hz(m); n = int((dur + 0.02) * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 1.3)
    x += 0.22 * np.sin(2 * np.pi * 6.27 * f * t) * np.exp(-t / 0.09)
    x += 0.05 * np.sin(2 * np.pi * 17.55 * f * t) * np.exp(-t / 0.02) if 17.55 * f < 20000 else 0
    tick = hp(np.random.default_rng(int(m)).standard_normal(n), 3000) * np.exp(-t / 0.003) * 0.25
    return (x + tick) * np.minimum(1, t / 0.0008) * np.clip((dur + 0.01 - t) / 0.03, 0, 1)


def celesta(m, dur):
    f = hz(m); n = int((dur + 0.02) * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 1.1) + 0.12 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.15)
    x += 0.04 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.4)
    return x * np.minimum(1, t / 0.002) * np.clip((dur + 0.01 - t) / 0.03, 0, 1)


def timp(m, v, seed, length=2.6):
    f = hz(m); n = int(length * SR); t = np.arange(n) / SR
    bend = np.cumsum(1 + 0.015 * np.exp(-t / 0.07)) / SR
    x = np.zeros(n)
    for r_, a, tau in ((1, 1, 1.0), (1.5, 0.45, 0.6), (1.99, 0.3, 0.45), (2.44, 0.12, 0.3)):
        x += a * np.sin(2 * np.pi * f * r_ * bend) * np.exp(-t / tau)
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.4 * lp(z, 350) * np.exp(-t / 0.02)
    return x * np.minimum(1, t / 0.002) * v * tail(n, 0.2)


def chrono(tock, seed):
    """A marine chronometer's beat: a fine metal click, the tock a shade lower."""
    n = int(0.05 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = hp(z, 5000) * np.exp(-t / 0.0025) + 0.6 * bp(z, 3200 if tock else 4100, 2.0) * np.exp(-t / 0.006)
    return x * tail(n, 0.01)


def groan(dur, seed):
    """The hull under pressure: noise through a band that slides down, crackle."""
    n = int(dur * SR); t = np.arange(n) / SR; r = rng('groan', seed)
    z = r.standard_normal(n)
    out = np.zeros(n); zi = np.zeros(2); ch = 480
    f0, f1 = r.uniform(170, 210), r.uniform(105, 125)
    for i in range(0, n, ch):
        u = i / n; fc = f0 * (f1 / f0) ** u
        w = 2 * np.pi * fc / SR; q = 7.0; al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + ch], zi = lfilter(b / a[0], a / a[0], z[i:i + ch], zi=zi)
    env = np.sin(np.pi * t / dur) ** 2
    crack = np.zeros(n)
    for _ in range(14):
        i = int(r.uniform(0.1, 0.9) * n); k = int(0.012 * SR)
        crack[i:i + k] += bp(r.standard_normal(k), r.uniform(900, 1600), 3.0) * np.exp(-np.arange(k) / SR / 0.003)
    return out * env * 3.0 + crack * env * 0.5


def rumble(seed):
    """One bar of the sea's low rumble (a grain a bar keeps it periodic)."""
    n = int((BAR + 0.5) * SR); t = np.arange(n) / SR
    z = rng('rumble', seed).standard_normal((n, 2))
    y = lp(lp(z, 140), 140)
    w = np.clip(t / 0.25, 0, 1) * np.clip((BAR + 0.5 - t) / 0.25, 0, 1)
    return y * w[:, None]


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    organ, cello, vln, pad, hrp, box, cel, bass, drum, hull = (tl.bus() for _ in range(10))

    for b in tl.bars_range():
        t = b * BAR; lb = b % BARS; sec = section(lb); c = PROG[lb]; v = CH[c]

        # the cello (A and A'') and the violins (B and A'')
        for pos, m, d in notes_of(CELLO, lb):
            cello.add(t + pos * E8, bowed(m, d * E8 - 0.03, ('vc', lb, pos), voices=2, attack=0.1,
                                          release=0.12 if d == 1 else 0.3, bright=0.8),
                      pan=-0.3, gain=0.17 if sec == 'A' else 0.13)
        for pos, m, d in notes_of(VIOLIN, lb):
            vln.add(t + pos * E8, bowed(m, d * E8 - 0.03, ('vn', lb, pos), voices=5, attack=0.14,
                                        release=0.1 if d == 1 else 0.3, bright=1.0),
                    pan=0.25, gain=0.15 if sec == 'B' else 0.13)

        # the string pad in B: the lower strings holding the chord
        if sec == 'B':
            for k, m in enumerate(v['pad']):
                pad.add(t, bowed(m, BAR - 0.05, ('pad', lb, k), voices=3, attack=0.5, release=0.25, bright=0.5),
                        pan=-0.35 + 0.35 * k, gain=0.06)

        # harp: a broken chord up and down, an eighth each (B, A'')
        if sec in ('B', "A''"):
            order = [0, 1, 2, 3, 4, 5] if lb % 2 == 0 else [5, 4, 3, 2, 1, 0]
            for e, ix in enumerate(order):
                m = v['harp'][ix]; ta = t + e * E8
                d = ring_for(ta, m, 2.6)
                hrp.add(ta, harp(m, d, 0.9 if e == 0 else 0.7, lb * 8 + e), pan=-0.5 + (m - 40) / 40, gain=0.17)

        # music box (intro): the head of the theme, damped at the changes
        for pos, m, d in notes_of(MUSICBOX, lb):
            ta = t + pos * E8
            box.add(ta, music_box(m, ring_for(ta, m, 2.4)), pan=0.2, gain=0.1)

        # celesta (B): the long notes of the violin line, an octave up
        if sec == 'B':
            for pos, m, d in notes_of(VIOLIN, lb):
                if d >= 2:
                    ta = t + pos * E8
                    cel.add(ta, celesta(m + 12, ring_for(ta, m + 12, 1.8)), pan=0.45, gain=0.06)

        # bass: pedal bourdon (intro, A, A''), pizzicato (B)
        if sec == 'B':
            bass.add(t, pizz(v['bass'], 1.0, lb), pan=-0.1, gain=0.3)
            bass.add(t + 2 * BEAT, pizz(v['bass'] + 12 if v['bass'] < 40 else v['bass'], 0.6, lb + 50),
                     pan=-0.1, gain=0.18)

        # chronometer: every half second (the intro and A sections), quarters in B
        step = 1 if sec != 'B' else 2
        for e in range(0, 6, step):
            drum.add(t + e * E8, chrono(e % 2 == 1, lb * 6 + e), pan=0.55,
                     gain={'intro': 0.05, 'A': 0.05, 'B': 0.035, "A''": 0.045}[sec])

        # timpani: C at A and A'', a roll on G into the top of the loop
        if lb in (4, 20):
            drum.add(t, timp(36, 1.0, lb), pan=-0.2, gain=0.22)
        if lb == 26:
            drum.add(t, timp(43, 0.8, lb), pan=-0.2, gain=0.16)
        if lb == 27:
            for k in range(18):
                vv = 0.15 + 0.55 * np.sin(np.pi * (k + 1) / 19) ** 1.5           # swells and dies away
                drum.add(t + k * BEAT / 6, timp(43, vv, 300 + k, length=1.2), pan=-0.2, gain=0.15)

        # the hull: a groan every four bars in A and A''; the rumble throughout
        if sec in ('A', "A''") and lb % 4 == 1:
            hull.add(t + 0.5, np.stack([groan(4.5, lb)] * 2, 1) * [0.9, 1.1], gain=0.04)
        hull.add(t - 0.25, rumble(lb), gain=0.05 if sec != 'B' else 0.035)

    # organ: chorale chords and the pedal, each voice held while its note stays
    segs = [(b * BAR, PROG[b % BARS]) for b in tl.bars_range()]
    for k in range(5):                                    # four manual voices + the pedal
        notes = []
        for t, c in segs:
            sec = section(int(round(t / BAR)))
            if sec == 'B':
                continue
            m = CH[c]['bass'] if k == 4 else CH[c]['organ'][k]
            if notes and notes[-1][2] == m and notes[-1][3] == sec and abs(notes[-1][0] + notes[-1][1] - t) < 1e-9:
                notes[-1][1] += BAR
            else:
                notes.append([t, BAR, m, sec])
        for t, d, m, sec in notes:
            lb0 = int(round(t / BAR)) % BARS
            if k == 4:
                ranks, g = ('bourdon',), {'intro': 0.05, 'A': 0.11, "A''": 0.12}[sec]
            elif sec == 'intro':
                ranks, g = ('flute',), 0.022
            elif sec == 'A':
                ranks, g = ('flute', 'principal'), 0.03
            else:
                ranks, g = ('flute', 'principal', 'octave'), 0.032
            organ.add(t, pipe(m, d - 0.03, ranks, (lb0, k)), pan=-0.25 + 0.15 * k if k < 4 else 0.0, gain=g)

    hrpx = hrp.x + 0.25 * bp(hrp.x, 350, 1.2)
    vlnx = chorus(vln.x, BAR, depth_ms=1.2, base_ms=8.0, mix=0.3, t0=tl.t0)
    salon = make_ir(2.6, dark=6000, seed=41, pre=0.025)
    wet = reverb(organ.x * 0.5 + cello.x * 0.35 + vlnx * 0.45 + pad.x * 0.4 + hrpx * 0.35 + box.x * 0.4
                 + cel.x * 0.5 + bass.x * 0.15 + drum.x * 0.2 + hull.x * 0.3, salon)
    stems = dict(organ=organ.x, cello=cello.x, violins=vlnx, pad=pad.x, harp=hrpx, musicbox=box.x,
                 celesta=cel.x, bass=bass.x, perc=drum.x, hull=hull.x, reverb=wet * 0.42)
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        report(stems, mix)
    return finish(tl, mix, NAME, wav=wav)


def report(stems, mix):
    """Stem rms above 150 Hz (dB rel. the mix's) per section, and the HF click ratio per stem."""
    i0 = tl.smp(0); N = int(LOOP * SR); secs = [(0, 4), (4, 12), (12, 20), (20, 28)]
    tot = np.sqrt(np.mean(hp(mix, 150)[i0:i0 + N] ** 2))
    print('         ' + ' '.join(f'{section(a):>7}' for a, _ in secs) + '   click')
    for k, v in stems.items():
        vh = hp(v, 150)
        row = [20 * np.log10(np.sqrt(np.mean(vh[i0 + int(a * BAR * SR):i0 + int(b * BAR * SR)] ** 2)) / tot + 1e-9)
               for a, b in secs]
        h = hp(v.mean(1), 4000)[i0:i0 + N]
        d = np.abs(np.diff(h, 2)); cr = d.max() / (np.percentile(d, 99.9) + 1e-12)
        hf = 20 * np.log10(np.abs(h).max() / (np.abs(v[i0:i0 + N]).max() + 1e-12) + 1e-12)
        print(f'{k:8s} ' + ' '.join(f'{r:7.1f}' for r in row) + f'   {cr:5.1f} (HF peak {hf:5.0f} dB)')


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
