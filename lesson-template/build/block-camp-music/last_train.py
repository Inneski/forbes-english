#!/usr/bin/env python3
"""Block Camp soundtrack "Last Train" (The Last Train Home RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game: a cybervoxel
megacity at night; Jax's last train dies after a club gig, lockdown is
coming, and he, Nyra, the one-eyed android Mono and the runner Rook cross
the city on foot - under the drones, through the market, over the
skybridge - to reach his tower before the checkpoints seal it. So: driving
synthwave with a cyberpunk edge and a clock running, but nothing a ten-year
-old would find menacing. An original piece in that idiom: no melody, riff
or progression is taken from any record.

F# minor, 128 BPM, 4/4 (a sixteenth is exactly 5625 samples, a bar 1.875 s).
One chord a bar:

  intro  F#m F#m F#m F#m                    bars 0-3    the countdown: timer blips, the station
                                                        chime, the gallop under a shut filter
  A      F#m F#m D D Bm Bm C#sus4 C#        bars 4-11   kick, hats, the arpeggio; the gallop opens
  A'     F#m F#m D D Bm Bm C#sus4 C#        bars 12-19  the hook on the sync lead, snare and clap
  B      Bm Bm F#m F#m G G C#sus4 C#        bars 20-27  the checkpoint: a second chime, Jax's
                                                        guitar chugging the gallop, a distant
                                                        two-tone siren, the lead answering low
  C      D E A A D E C#sus4 C#              bars 28-35  home ahead: the major lift, the hook up
                                                        an octave, power chords, open hats
  outro  F#m F#m D C#                       bars 36-39  the drums stop; the timer comes back and
                                                        the loop closes on the dominant

The hook is the train itself: the gallop (an eighth and two sixteenths,
DUM da-da) runs under the whole loop in the bass, and the tune opens with the
same rhythm. The G in B is the Neapolitan, the one dark chord; C is the only
section in a major key.

Instruments, all synthesised here:
  Gallop bass  two polyBLEP saws 10 cents apart and a sine, each note through
               a resonant low-pass with its own envelope, the cutoff riding one
               curve across the loop (shut in the intro and outro, widest in C).
  Pad          five detuned saws a voice, low-passed, two choruses; it ducks
               a little under the kick.
  Arpeggio     a narrow pulse, sixteenths up and down two octaves of the chord,
               a dotted-eighth ping-pong echo.
  Sync lead    additive, one continuous voice from bar 12 to 35: saw harmonics
               under a resonant peak that sweeps from the 7th harmonic down to
               the 2nd at each attack (the hard-sync "zap"), glide, delayed
               vibrato, a dotted-eighth echo.
  Guitar       Jax's: Karplus-Strong strings (as grand_hotel.py) through a soft
               valve-ish drive and a cabinet, double-tracked left and right.
               Palm-muted in B (the strings damped to a 0.12 s ring), ringing
               power chords in C, damped at the next hit or chord change.
  Siren        a soft triangle a long way off, two tones a bar (the chord's
               fifth and root above it), gliding between them.
  Drums        a kick settling on B1, a snare whose shell rings on B3 with a
               clap layer, hats, toms on the C# chord (G#3 F3 C#3 G#2).
  Signals      timer blips on the chord's root and fifth (F#6, C#7 ...); a
               three-note station chime (C#6 A5 F#5 at the top, F#5 D5 B4 at
               the checkpoint); noise whooshes into A, B and C.

Pitched percussion is tuned into the key. B is the one pitch class that is
never a semitone from a tone of any chord here, so the kick and the snare
shell sit on it; the toms only play over C#.

check_lines() asserts at import: every chord is free of semitones; every
bass, pad, arpeggio, guitar, siren, blip and chime note is a chord tone; every
lead note on beat 1 or 3, or a quarter or longer, is a chord tone; and no lead
note at all sits a semitone or a minor ninth from any accompanying note.

40 bars = 75 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/last_train.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

NAME = 'last-train-home'
BARS = 40
tl = Timeline(bpm=128, bars=BARS)
BAR, BEAT, S16 = tl.bar, tl.beat, tl.s16         # 1.875 s, 0.46875 s, 0.1171875 s (5625 samples)
LOOP = tl.loop                                    # 75 s
CHUNK = 225                                       # 25 chunks a sixteenth

# ── the changes ─────────────────────────────────────────────────────────────
#          pcs           bass  pad voicing         guitar (power chord)
CH = {
    'F#m':    ({6, 9, 1},  42, [61, 66, 69, 73], [42, 49, 54]),
    'D':      ({2, 6, 9},  38, [62, 66, 69, 74], [50, 57, 62]),
    'Bm':     ({11, 2, 6}, 35, [62, 66, 71, 74], [47, 54, 59]),
    'C#sus4': ({1, 6, 8},  37, [61, 66, 68, 73], [49, 56, 61]),
    'C#':     ({1, 5, 8},  37, [61, 65, 68, 73], [49, 56, 61]),
    'E':      ({4, 8, 11}, 40, [64, 68, 71, 76], [40, 47, 52]),
    'A':      ({9, 1, 4},  45, [64, 69, 73, 76], [45, 52, 57]),
    'G':      ({7, 11, 2}, 43, [62, 67, 71, 74], [43, 50, 55]),
}
CHORDS = (['F#m'] * 4 +
          ['F#m', 'F#m', 'D', 'D', 'Bm', 'Bm', 'C#sus4', 'C#'] +
          ['F#m', 'F#m', 'D', 'D', 'Bm', 'Bm', 'C#sus4', 'C#'] +
          ['Bm', 'Bm', 'F#m', 'F#m', 'G', 'G', 'C#sus4', 'C#'] +
          ['D', 'E', 'A', 'A', 'D', 'E', 'C#sus4', 'C#'] +
          ['F#m', 'F#m', 'D', 'C#'])
assert len(CHORDS) == BARS


def section(lb):
    return ('intro' if lb < 4 else 'A' if lb < 12 else "A'" if lb < 20 else 'B' if lb < 28
            else 'C' if lb < 36 else 'outro')


def part(name, lb):
    s = section(lb)
    return {
        'kick':   s in ('A', "A'", 'B', 'C'),
        'snare':  s in ("A'", 'B', 'C') or (s == 'A' and lb >= 8),
        'clap':   s in ("A'", 'C'),
        'hat16':  s in ("A'", 'B', 'C') or (s == 'A' and lb >= 8),
        'hat8':   s == 'A' and lb < 8,
        'ohat':   s == 'C',
        'fill':   lb in (11, 19, 27, 35),
        'roll':   lb == 27,
        'whoosh': lb in (3, 19, 27),
        'arp':    s in ('A', "A'", 'C'),
        'timer':  s in ('intro', 'outro'),
        'chug':   s == 'B',
        'power':  s == 'C',
        'siren':  s == 'B',
    }[name]


PAD_LEVEL = {'intro': 0.7, 'A': 0.85, "A'": 0.8, 'B': 0.75, 'C': 1.0, 'outro': 0.8}
ARP_LEVEL = {'A': 1.0, "A'": 0.7, 'C': 0.85}
# the bass cutoff across the loop (bar, Hz), log-interpolated; the value at 40 is the value at 0
CUT = [(0, 260), (3.5, 420), (4, 650), (12, 900), (20, 1050), (28, 1250), (35.9, 1500), (36, 420), (40, 260)]


def cutoff(bpos):
    xs, ys = zip(*CUT)
    return float(np.exp(np.interp(bpos % BARS, xs, np.log(ys))))


# ── the lead: (midi, sixteenths), 0 = rest; one voice from bar 12 to bar 35 ──
LEAD = [
    (73, 2), (73, 1), (76, 1), (78, 8), (76, 2), (73, 2),            # 12 F#m   C#, C# E F#: the gallop
    (69, 4), (71, 2), (73, 8), (0, 2),                               # 13 F#m   A B C#
    (74, 2), (74, 1), (76, 1), (78, 8), (81, 2), (78, 2),            # 14 D     D, D E F# A F#
    (81, 4), (78, 2), (76, 2), (74, 8),                              # 15 D     A F# E D
    (74, 2), (74, 1), (76, 1), (78, 8), (76, 2), (74, 2),            # 16 Bm    D, D E F# E D
    (71, 4), (74, 10), (0, 2),                                       # 17 Bm    B D
    (80, 4), (78, 4), (73, 8),                                       # 18 C#sus4 G# F# C#
    (77, 6), (80, 2), (73, 4), (0, 4),                               # 19 C#    E# G# C#
    (71, 1), (74, 1), (78, 4), (76, 2), (78, 4), (74, 2), (71, 2),   # 20 Bm    the answer
    (74, 4), (76, 2), (78, 8), (0, 2),                               # 21 Bm
    (73, 1), (76, 1), (81, 4), (78, 2), (81, 4), (76, 2), (73, 2),   # 22 F#m
    (78, 4), (76, 2), (73, 8), (0, 2),                               # 23 F#m
    (71, 1), (74, 1), (79, 4), (81, 2), (79, 4), (74, 2), (71, 2),   # 24 G
    (74, 4), (76, 2), (79, 8), (0, 2),                               # 25 G
    (73, 2), (78, 2), (80, 4), (78, 8),                              # 26 C#sus4
    (77, 8), (73, 4), (0, 4),                                        # 27 C#
    (78, 2), (78, 1), (81, 1), (86, 8), (83, 2), (81, 2),            # 28 D     the hook, up a sixth
    (80, 4), (83, 2), (88, 8), (0, 2),                               # 29 E
    (85, 2), (85, 1), (83, 1), (81, 8), (76, 2), (81, 2),            # 30 A
    (88, 4), (85, 2), (81, 8), (0, 2),                               # 31 A
    (86, 3), (83, 1), (81, 4), (78, 2), (81, 6),                     # 32 D
    (80, 4), (83, 4), (88, 6), (0, 2),                               # 33 E
    (85, 4), (80, 4), (78, 8),                                       # 34 C#sus4
    (77, 8), (80, 4), (73, 4),                                       # 35 C#
]
LEAD_BAR0 = 12
assert sum(d for _, d in LEAD) == 16 * 24

TIMER = {_c: (84 + _r % 12, 79 + _r % 12)       # chord -> (beat 1: the root, C6-B6; the rest: the fifth below)
         for _c, (_p, _r, _v, _g) in CH.items()}
CHIME = {0: (85, 81, 78), 20: (78, 74, 71)}      # loop bar -> three notes, a beat apart
TOMS = (56, 53, 49, 44)                          # G#3 F3 C#3 G#2: the C# chord
KICK_PITCH, SNARE_PITCH = 35, 59                 # B1, B3


def arp_tones(c):
    return [m for m in range(64, 94) if m % 12 in CH[c][0]][:7]


def siren_notes(c):
    """The chord's fifth and the root a fourth above it, between E4 and G5."""
    pcs, root = CH[c][0], CH[c][1]
    hi = 67 + (root % 12 - 67) % 12
    return (hi - 5, hi) if (hi - 5) % 12 in pcs else (hi - 7, hi)


def accompaniment(lb):
    """Every pitch the band can be sounding in loop bar lb."""
    c = CHORDS[lb]; pcs, root, pad, gtr = CH[c]
    notes = {root, root + 12} | set(pad)
    if part('arp', lb):
        notes |= set(arp_tones(c))
    if part('chug', lb) or part('power', lb):
        notes |= set(gtr)
    if part('siren', lb):
        notes |= set(siren_notes(c))
    if part('timer', lb):
        notes |= set(TIMER[c])
    notes |= set(CHIME.get(lb, ())) | set(CHIME.get(lb - 1, ()))      # a chime rings into the next bar
    return notes


def check_lines():
    bad = []
    for c, (pcs, root, pad, gtr) in CH.items():
        if any((a - b) % 12 in (1, 11) for a in pcs for b in pcs):
            bad.append(('chord has a semitone', c))
        for nm, ms in (('bass', [root, root + 12]), ('pad', pad), ('guitar', gtr), ('arp', arp_tones(c)),
                       ('siren', siren_notes(c)), ('timer', TIMER[c])):
            if any(m % 12 not in pcs for m in ms):
                bad.append((nm, c, ms))
        if any(m % 12 in (10, 0) for m in pcs):     # B (pc 11) must stay clear of every chord: kick and snare
            bad.append(('kick/snare B rubs', c))
    for lb, notes in CHIME.items():
        if any(m % 12 not in CH[CHORDS[lb]][0] for m in notes):
            bad.append(('chime', lb))
    for lb in range(BARS):
        if part('fill', lb) and any(m % 12 not in CH[CHORDS[lb]][0] for m in TOMS):
            bad.append(('toms', lb, CHORDS[lb]))
    pos = 0
    for m, d in LEAD:
        lb = LEAD_BAR0 + pos // 16
        if m:
            for q in range(pos, pos + d):               # every bar the note sounds in
                qb = LEAD_BAR0 + q // 16
                c = CHORDS[qb]
                strong = (q == pos and q % 8 == 0) or d >= 4 or (q > pos and q % 16 == 0)
                if strong and (q == pos or q % 16 == 0) and m % 12 not in CH[c][0]:
                    bad.append(('lead not a chord tone', qb, q % 16, m, c))
                if q == pos or q % 16 == 0:
                    rub = [v for v in accompaniment(qb) if abs(m - v) in (1, 13)]
                    if rub:
                        bad.append(('lead rubs', qb, q % 16, m, c, rub))
        pos += d
    print('lines vs chords:', 'every long or strong lead note is a chord tone, nothing rubs' if not bad else bad)
    assert not bad, 'a wrong note (listed above)'


check_lines()


# ── oscillators and filters ─────────────────────────────────────────────────
def _blep(p, dt):
    y = np.zeros_like(p)
    a = p < dt; u = p[a] / dt[a]; y[a] = 2 * u - u * u - 1
    b = p > 1 - dt; u = (p[b] - 1) / dt[b]; y[b] = u * u + 2 * u + 1
    return y


def blsaw(f, n, ph=0.0):
    dt = np.broadcast_to(np.asarray(f, float) / SR, (n,)).copy()
    p = (ph + np.cumsum(dt)) % 1.0
    return 2 * p - 1 - _blep(p, dt)


def blpulse(f, n, duty=0.5, ph=0.0):
    """Zero-mean band-limited pulse (no DC thump at each attack)."""
    dt = np.broadcast_to(np.asarray(f, float) / SR, (n,)).copy()
    p = (ph + np.cumsum(dt)) % 1.0
    q = (p + 1 - duty) % 1.0
    return (2 * p - 1 - _blep(p, dt)) - (2 * q - 1 - _blep(q, dt))     # two zero-mean saws: no DC


def tv_lp(x, fc, q=0.707):
    out = np.empty_like(x); zi = np.zeros(2)
    for j, i in enumerate(range(0, len(x), CHUNK)):
        w = 2 * np.pi * min(fc[min(j, len(fc) - 1)], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + CHUNK], zi = lfilter(b / a[0], a / a[0], x[i:i + CHUNK], zi=zi)
    return out


def swept_bp(x, f0, f1, q):
    out = np.empty_like(x); zi = np.zeros(2); n = len(x)
    for i in range(0, n, CHUNK):
        fc = f0 * (f1 / f0) ** (i / max(n - 1, 1))
        w = 2 * np.pi * fc / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + CHUNK], zi = lfilter(b / a[0], a / a[0], x[i:i + CHUNK], zi=zi)
    return out


# ── instruments ─────────────────────────────────────────────────────────────
def bass_note(m, dur, cut, acc, key):
    n = int((dur + 0.05) * SR); t = np.arange(n) / SR
    r = rng('bass', key)
    x = 0.5 * blsaw(hz(m) * 2 ** (-5 / 1200), n, r.random()) + 0.5 * blsaw(hz(m) * 2 ** (5 / 1200), n, r.random())
    tc = t[::CHUNK]
    x = tv_lp(x, cut * (1 + (0.9 + 1.8 * acc) * np.exp(-tc / 0.045)), 2.2)
    x = 0.85 * x + 0.5 * np.sin(2 * np.pi * hz(m) * t)
    return x * adsr(n, 0.002, 0.07, 0.7, 0.03, dur)


def pad_note(m, dur, key):
    n = int((dur + 0.3) * SR)
    r = rng('pad', key)
    x = sum(blsaw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-14, -6, 0, 7, 13)) / 5
    x = hp1(lp(lp1(x, 6500), 3000, 0.8), 180)
    # a short release, gone 20 ms after the bar line: at G -> C#sus4, C# -> D and C# -> Bm
    # every voice moves a semitone, and a longer tail sounded both chords at once
    return x * adsr(n, 0.12, 0.5, 0.8, 0.12, dur)


def arp_note(m, key):
    n = int(0.2 * SR)
    x = lp(blpulse(hz(m), n, 0.28, rng('arp', key).random()), 7500, 0.9)
    return x * perc(n, 0.0015, 0.07)


def lead_phrase(mel):
    total = sum(d for _, d in mel)
    n = int((total * S16 + 1.2) * SR)
    semi = np.zeros(n); g = np.zeros(n); vib = np.zeros(n); zap = np.zeros(n)
    pos = 0; last = next(m for m, _ in mel if m); e = 0
    for j, (m, d) in enumerate(mel):
        a, e = int(round(pos * S16 * SR)), int(round((pos + d) * S16 * SR))
        tt = np.arange(e - a) / SR
        if m:
            semi[a:e] = m; last = m
            nxt = mel[j + 1][0] if j + 1 < len(mel) else 0
            env = np.minimum(1, tt / 0.006) * (0.82 + 0.18 * np.exp(-tt / 0.16))
            k = min(len(tt), int(0.025 * SR))
            if k:
                env[-k:] *= np.linspace(1, 0.6 if nxt else 0.0, k)
            g[a:e] = env
            vib[a:e] = np.clip((tt - 0.22) / 0.3, 0, 1) * (1.0 if d >= 4 else 0.0)
            zap[a:e] = np.exp(-tt / 0.07)
        else:
            semi[a:e] = last
        pos += d
    semi[e:] = last
    g = lp1(g, 90)
    c = np.exp(-1 / (0.018 * SR))                                      # a short glide
    semi = lfilter([1 - c], [1, -c], semi - semi[0]) + semi[0]
    t = np.arange(n) / SR
    semi = semi + 0.22 * vib * np.sin(2 * np.pi * 5.5 * t)
    f = hz(semi)
    ph = 2 * np.pi * np.cumsum(f) / SR
    peak = f * (2.0 + 5.0 * zap)                                       # the sync sweep: 7th harmonic -> 2nd
    x = np.zeros(n)
    for k in range(1, 30):
        fk = k * f
        amp = (1 / k) * (0.45 + 1.5 * np.exp(-0.5 * ((fk - peak) / (0.7 * f)) ** 2))
        x += amp * np.clip((11000 - fk) / 2000, 0, 1) * np.sin(k * ph)
    return lp1(x, 12000) * g


# ── strings: Karplus-Strong, as grand_hotel.py ──────────────────────────────
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
    kk = np.arange(1, int(max(2, min(48, top / f))) + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -tilt * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    exc += noise * lp1(np.random.default_rng(seed).uniform(-1, 1, N), 3500)
    k = max(1, int(comb * N))
    exc[k:] -= 0.5 * exc[:-k]
    return exc / np.abs(exc).max()


def gtr_string(m, ring, v, seed, muted):
    """A steel string. Palm-muted: the loss filter darker and a 0.12 s ring.
    Open: it rings until `ring`, then the hand comes down over 25 ms."""
    f = hz(m)
    N, c, den = ks_setup(f, 0.62 if muted else 0.8, 0.12 if muted else 2.4)
    exc = pick(N, f, 0.8 if muted else 0.55, 0.15, 0.12, seed, top=5000 if muted else 8000)
    n = int((ring + 0.03) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * v
    y = lfilter([1.0, c], den, x)
    t = np.arange(n) / SR
    return y * np.clip((ring + 0.025 - t) / 0.025, 0, 1)


def amp_cab(x):
    """A soft drive and a 1x12 cabinet: not a metal tone."""
    y = np.tanh(2.0 * hp1(x, 80)) / np.tanh(2.0)
    y = y + 0.3 * bp(y, 1900, 1.1) + 0.3 * bp(y, 130, 1.5)
    return lp(lp(y, 5200, 0.7), 6500, 0.6)


def siren_bar(c, key):
    """One bar: the low tone two beats, the high tone two, a 60 ms glide each way."""
    lo_, hi_ = siren_notes(c)
    n = int(BAR * SR); t = np.arange(n) / SR
    k = int(0.06 * SR); h = int(2 * BEAT * SR)
    semi = np.full(n, float(lo_))
    semi[h:h + k] = lo_ + (hi_ - lo_) * (0.5 - 0.5 * np.cos(np.pi * np.arange(k) / k))
    semi[h + k:] = hi_
    f = hz(semi + 0.08 * np.sin(2 * np.pi * 5.0 * t))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) - np.sin(3 * ph) / 9 + np.sin(5 * ph) / 25
    env = np.minimum(1, t / 0.08) * np.clip((BAR - 0.02 - t) / 0.3, 0, 1)    # out before the next chord
    return lp1(x, 2500) * env


def blip(m):
    n = int(0.09 * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.01)
    return x * np.minimum(1, t / 0.001) * np.exp(-t / 0.028)


def chime(m):
    f = hz(m); n = int(3.0 * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for r_, a, tau in ((1, 1.0, 1.3), (2, 0.28, 0.6), (3, 0.12, 0.3), (4.2, 0.06, 0.12)):
        x += a * np.sin(2 * np.pi * f * r_ * t) * np.exp(-t / tau)
    return x * np.minimum(1, t / 0.002)


def kick():
    n = int(0.42 * SR); t = np.arange(n) / SR
    f = hz(KICK_PITCH) + 110 * np.exp(-t / 0.028)                       # settles on B1
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16)
    click = lp1(hp1(np.random.default_rng(41).standard_normal(n), 1200), 6000) * np.exp(-t / 0.004) * 0.3
    x = np.tanh(1.4 * (body + click)) / np.tanh(1.4)
    return x * np.clip((n - np.arange(n)) / (0.02 * SR), 0, 1)


def snare(seed):
    n = int(0.32 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    noise = lp(bp(z, 2400, 0.6), 9000) * np.exp(-t / 0.075) + 0.55 * hp1(z, 6000) * np.exp(-t / 0.05)
    tone = np.sin(2 * np.pi * hz(SNARE_PITCH) * t) * np.exp(-t / 0.06) * 0.7    # the shell on B3
    return (noise + tone) * np.minimum(1, t / 0.0008)


def clap(seed):
    n = int(0.3 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    env = sum(np.where(t >= d, np.exp(-(t - d) / 0.005), 0) for d in (0.0, 0.009, 0.019))
    env += 0.6 * np.where(t >= 0.026, np.exp(-(t - 0.026) / 0.08), 0)
    return (bp(z, 1300, 0.8) + 0.5 * bp(z, 3200, 1.0)) * env


def hat(seed, open_=False):
    n = int((0.28 if open_ else 0.06) * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    x = lp1(hp(hp(z, 7000), 7000), 14000)
    return x * perc(n, 0.0008, 0.11 if open_ else 0.017)


def tom(m, seed):
    n = int(0.5 * SR); t = np.arange(n) / SR
    f0 = hz(m)
    f = f0 * (1 + 0.35 * np.exp(-t / 0.05))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.18)
    x += lp1(np.random.default_rng(seed).standard_normal(n), 3500) * np.exp(-t / 0.012) * 0.2
    return x * np.minimum(1, t / 0.001)


def whoosh(key):
    n = int(BAR * SR); u = np.arange(n) / n
    z = rng('whoosh', key).standard_normal(n)
    y = swept_bp(z, 300, 5000, 1.3)
    return y * u ** 2.2 * np.clip((1 - u) * n / (0.02 * SR), 0, 1)


# ── render ──────────────────────────────────────────────────────────────────
def mixdown():
    drums, bass, pad, arp, lead, gtr_l, gtr_r, siren, sig = (tl.bus() for _ in range(9))
    kicks = []
    gtr_ev = []                                   # (t, midi, vel, seed, muted, side)
    for b in tl.bars_range():
        t = b * BAR; lb = b % BARS
        sec, c = section(lb), CHORDS[lb]
        pcs, root, voic, gv = CH[c]

        # the gallop: DUM da-da on every beat, the octave on the last sixteenth of beats 2 and 4
        for q in range(4):
            for s, dur, acc in ((0, 1.6, 1.0), (2, 0.75, 0.35), (3, 0.75, 0.45)):
                m = root + 12 if (s == 3 and q % 2 == 1) else root
                p = q * 4 + s
                bass.add(t + p * S16, bass_note(m, dur * S16, cutoff(lb + p / 16), acc, (lb, p)),
                         gain=0.2 if s == 0 else 0.16)

        # pad: one chord a bar, ending just before the change
        for k, m in enumerate(voic):
            pad.add(t, pad_note(m, BAR - 0.1, (lb, k)), pan=(-0.6, -0.2, 0.2, 0.6)[k],
                    gain=0.15 * PAD_LEVEL[sec])

        # arpeggio
        if part('arp', lb):
            tn = arp_tones(c)
            order = (0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 3, 2, 1)
            for s, k in enumerate(order):
                arp.add(t + s * S16, arp_note(tn[k], (lb, s)), pan=0.45 if s % 2 else -0.45,
                        gain=(0.065 + (0.02 if s % 4 == 0 else 0)) * ARP_LEVEL[sec])

        # drums
        if part('kick', lb):
            for q in range(4):
                drums.add(t + q * BEAT, KICK, gain=0.24); kicks.append(t + q * BEAT)
        if part('snare', lb):
            for q in (1, 3):
                drums.add(t + q * BEAT, snare(lb * 4 + q), pan=0.05, gain=0.11)
                if part('clap', lb):
                    drums.add(t + q * BEAT + 0.004, clap(lb * 4 + q), pan=-0.1, gain=0.07)
        if part('hat16', lb):
            for s in range(16):
                if part('ohat', lb) and s % 4 == 2:
                    drums.add(t + s * S16, hat(9000 + lb * 16 + s, True), pan=0.3, gain=0.05)
                else:
                    drums.add(t + s * S16, hat(lb * 16 + s), pan=0.3,
                              gain=0.055 if s % 4 == 2 else 0.036 if s % 2 == 0 else 0.026)
        elif part('hat8', lb):
            for s in range(0, 16, 2):
                drums.add(t + s * S16, hat(lb * 16 + s), pan=0.3, gain=0.05 if s % 4 == 2 else 0.03)
        if part('fill', lb):
            steps = (12, 13, 14, 15) if lb != 35 else (8, 10, 12, 13, 14, 15)
            ms = TOMS if lb != 35 else (TOMS[0], TOMS[0], TOMS[1], TOMS[1], TOMS[2], TOMS[3])
            for k, (s, m) in enumerate(zip(steps, ms)):
                drums.add(t + s * S16, tom(m, lb * 16 + s), pan=-0.4 + 0.8 * (m - 44) / 12, gain=0.16)
        if part('roll', lb):
            for s in range(8, 16):
                drums.add(t + s * S16, snare(5000 + s), pan=0.05, gain=0.03 + 0.07 * ((s - 8) / 7) ** 1.5)
        if part('whoosh', lb):
            sig.add(t, whoosh(lb), pan=0.0, gain=0.07)

        # timer blips (intro, outro) and the station chime
        if part('timer', lb):
            one, rest = TIMER[c]
            for q in range(4):
                sig.add(t + q * BEAT, blip(one if q == 0 else rest), pan=0.35 if q % 2 else -0.35,
                        gain=0.13 if q == 0 else 0.1)
        if lb in CHIME:
            for k, m in enumerate(CHIME[lb]):
                sig.add(t + k * BEAT, chime(m), pan=(-0.25, 0.25, 0.0)[k], gain=0.09)

        # Jax's guitar
        if part('chug', lb):
            for q in range(4):
                for s, v in ((0, 1.0), (2, 0.7), (3, 0.75)):
                    for k, m in enumerate(gv[:2]):
                        for side in (0, 1):
                            jit = float(rng('gj', lb, q, s, side).uniform(-0.004, 0.004))
                            gtr_ev.append((t + (q * 4 + s) * S16 + jit + 0.006 * k, m, v, (lb, q, s, k, side), True, side))
        if part('power', lb):
            for s in (0, 6, 10):
                for k, m in enumerate(gv):
                    for side in (0, 1):
                        jit = float(rng('gj', lb, s, side).uniform(-0.005, 0.005))
                        gtr_ev.append((t + s * S16 + jit + 0.009 * k, m, 0.55 if s == 0 else 0.45,
                                       (lb, s, k, side), False, side))

        # the siren, far off
        if part('siren', lb):
            siren.add(t, siren_bar(c, lb), pan=-0.35, gain=0.05)

    # guitar strings ring until the next hit on that string or the next bar line
    ev = sorted(gtr_ev, key=lambda e: e[0])
    for j, (t0, m, v, key, muted, side) in enumerate(ev):
        if muted:
            ring = 0.16
        else:
            nxt = [e[0] for e in ev[j + 1:] if e[5] == side and e[1] == m]
            bar_end = (np.floor(t0 / BAR + 1e-6) + 1) * BAR
            ring = min(nxt[0] - t0 if nxt else 2.0, bar_end - t0 - 0.01, 2.0)
        seed = int(rng('gtr', key).integers(1 << 30))
        (gtr_l if side == 0 else gtr_r).add(t0, gtr_string(m, ring, v, seed, muted), gain=0.5)

    # the lead: one voice across bars 12-35, every lap
    phrase = lead_phrase(LEAD)
    for lap in (-1, 0, 1):
        t0 = lap * LOOP + LEAD_BAR0 * BAR
        if -tl.pre * BAR - 25 * BAR < t0 < (BARS + tl.post) * BAR:
            lead.add(t0, phrase, pan=0.0, gain=0.085)

    # the pad and arpeggio duck a little under the kick
    tt = np.arange(tl.n) / SR - tl.t0
    pump = np.ones(tl.n)
    WIN = BEAT - 0.01
    for k in kicks:
        i0 = tl.smp(k); i1 = min(tl.n, i0 + int(WIN * SR))
        if i1 > max(i0, 0):
            j0 = max(i0, 0); u = tt[j0:i1] - k
            duck = 0.3 * np.minimum(1, u / 0.006) * (np.exp(-u / 0.12) - np.exp(-WIN / 0.12)) / (1 - np.exp(-WIN / 0.12))
            pump[j0:i1] = np.minimum(pump[j0:i1], 1 - duck)
    pump = pump[:, None]

    padx = chorus(chorus(pad.x, LOOP / 80, depth_ms=1.8, base_ms=6.0, mix=0.5, t0=tl.t0),
                  LOOP / 25, depth_ms=3.0, base_ms=11.0, mix=0.35, t0=tl.t0) * pump
    # the echo is gated for a dotted eighth after a change of chord, so the last
    # notes of a C# bar do not repeat over the D (or F#m, Bm) that follows
    gate = np.ones(tl.n)
    for b in tl.bars_range():
        if CHORDS[b % BARS] != CHORDS[(b - 1) % BARS]:
            i = tl.smp(b * BAR); k = int(0.01 * SR); w = int(3 * S16 * SR)
            if 0 <= i - k and i + w + k <= tl.n:
                gate[i - k:i] = np.minimum(gate[i - k:i], np.linspace(1, 0, k))
                gate[i:i + w] = 0
                gate[i + w:i + w + k] = np.minimum(gate[i + w:i + w + k], np.linspace(0, 1, k))
    arpx = (arp.x + pingpong(arp.x, 3 * S16, 0.4, 5, 4200) * gate[:, None]) * pump
    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.32, 4, 3500) * 0.6
    gl, gr = amp_cab(gtr_l.x.mean(1)), amp_cab(gtr_r.x.mean(1))
    gtrx = np.stack([gl * 0.95 + gr * 0.2, gr * 0.95 + gl * 0.2], 1) * 0.6
    sirenx = siren.x
    wet = reverb(hp1(padx * 0.3 + arpx * 0.3 + leadx * 0.3 + gtrx * 0.15 + sirenx * 1.2
                     + sig.x * 0.5 + drums.x * 0.07, 180), make_ir(1.8, dark=7000, seed=23, pre=0.018))
    return dict(drums=drums.x, bass=bass.x, pad=padx, arp=arpx, lead=leadx, guitar=gtrx,
                siren=sirenx, signals=sig.x, reverb=wet * 0.45)


KICK = kick()


def render(wav=None):
    stems = mixdown()
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        i0 = tl.smp(0)
        print('stem      ' + ''.join(f'{s:>7d}' for s in range(0, BARS, 4)))
        for k, v in stems.items():
            row = [20 * np.log10(np.sqrt(np.mean(v[i0 + int(s * BAR * SR):i0 + int((s + 4) * BAR * SR)] ** 2)) + 1e-9)
                   for s in range(0, BARS, 4)]
            print(f'{k:9s} ' + ''.join(f'{r:7.1f}' for r in row))
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
