#!/usr/bin/env python3
"""Block Camp soundtrack "Circuit" (Present Perfect Continuous, both parts):
clean robotic electro.

Brief, 2026-09-30: music for the Present Perfect Continuous camp in the
idiom of Kraftwerk's Computer World / Trans-Europe Express era - a tight, dry
drum machine (electronic toms, metallic snare, crisp hats), staccato
square-wave melodies in call and response, a pulsing bass, a vocoder-like
chord pad with no words, clean and precise, little reverb. An original piece
in that idiom, nothing copied:

  A minor, 112.5 BPM, 4/4 (a sixteenth is exactly 6400 samples, so every
  event and every filter chunk falls on the same sample in every lap).
  An 8-bar cycle, one chord a bar: Am Am F G | Am Am Dm E.

  Drums      a short electronic kick, a metallic snare (band-passed noise
             and a ring-modulated tone), 808-style hats from six square
             oscillators (the open hat choked by the next closed one),
             pitched electronic toms (A2 D3 G3, the high one retuned to G#3
             over E) with a pitch drop. Dry; every one-shot fades to zero.
  Bass       pulsing staccato eighths, root-root-octave-root-root-fifth-
             octave-fifth, square and saw through a snapping low-pass.
  Vocoder    saw chords through three formant band-passes that move between
             vowels (ah, oh, oo, eh), no words: held and slowly changing
             vowel in most sections, chopped into quarter notes with a new
             vowel on each beat in the breakdown.
  Melody     two staccato square voices in call and response: the call on a
             50% square (left of centre), the answer on a thin 12.5% pulse
             (right), two bars each, with a short slapback echo.
  Blips      quiet sine computer blips on the A minor pentatonic, leaving
             out whichever notes rub a semitone against the chord.

  Arrangement (bar mod 32): 0-3 drums and bass with blips; 4-7 vocoder
  chords join; 8-15 the melody in call and response; 16-23 breakdown - no
  snare, eighth hats, a tom figure, the vocoder chopped into vowels, blips;
  24-31 everything, the call doubled in octaves and the answer doubled
  above; tom fills in bars 15, 23 and 31.

32 bars = 68.27 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/circuit.py [--wav preview.wav]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, perc, make_ir,
                      reverb, finish)

NAME = 'present-perfect-continuous'
BARS = 32
tl = Timeline(bpm=112.5, bars=BARS)
BAR, S16 = tl.bar, tl.s16
BEAT, E8 = tl.beat, 2 * S16


# ── the changes ─────────────────────────────────────────────────────────────
CH = {
    'Am': dict(root=45, voc=[57, 60, 64, 69], pcs={9, 0, 4}),
    'F':  dict(root=41, voc=[57, 60, 65, 69], pcs={5, 9, 0}),
    'G':  dict(root=43, voc=[55, 59, 62, 67], pcs={7, 11, 2}),
    'Dm': dict(root=38, voc=[57, 62, 65, 69], pcs={2, 5, 9}),
    'E':  dict(root=40, voc=[56, 59, 64, 68], pcs={4, 8, 11}),
}
CYCLE = ['Am', 'Am', 'F', 'G', 'Am', 'Am', 'Dm', 'E']


def chord_at(b):
    return CYCLE[b % 8]


def section(b):
    return 'ABCD'[(b % BARS) // 8]


def part(name, b):
    b %= BARS; sec = 'ABCD'[b // 8]
    return {
        'kick':  True,
        'snare': sec in 'ABD',
        'hats':  True,
        'toms':  sec == 'C',
        'fill':  b in (15, 23, 31),
        'bass':  True,
        'voc':   b >= 4,
        'mel':   sec in 'BD',
        'blips': sec in 'AC',
    }[name]


# ── the melody: one 16-step string per bar of the 8-bar cycle ───────────────
MEL = [
    'E5 . E5 . A5 . E5 . C5 . D5 . E5 . . .',            # Am  call
    'E5 . C5 . D5 . C5 . A4 . . . . . . .',              # Am  call
    'A4 . C5 . F5 . C5 . A4 . . . F4 . . .',             # F   answer
    'G4 . B4 . D5 . B4 . G4 . . . D5 . B4 .',            # G   answer
    'E5 . E5 . A5 . E5 . C6 . B5 . A5 . . .',            # Am  call
    'E5 . G5 . E5 . D5 . A4 . . . . . . .',              # Am  call
    'A4 . D5 . F5 . D5 . A4 . . . F4 . . .',             # Dm  answer
    'G#4 . B4 . E5 . B4 . G#4 . . . E4 . G#4 .',         # E   answer
]
CALL = {0, 1, 4, 5}
PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def note(s):
    return 12 * (int(s[-1]) + 1) + PC[s[0]] + (1 if '#' in s else 0)


STEPS = [[None if w == '.' else note(w) for w in row.split()] for row in MEL]
assert all(len(r) == 16 for r in STEPS)


def check_melody():
    """Notes on beats 1 and 3 must be chord tones; a non-chord note on beat 2
    or 4 must step (a tone or less) to a chord tone next; the rest are short
    staccato passing notes."""
    bad = []
    for i, row in enumerate(STEPS):
        ch = CH[CYCLE[i]]
        notes = [(s, m) for s, m in enumerate(row) if m is not None]
        for k, (s, m) in enumerate(notes):
            if s % 4 or m % 12 in ch['pcs']:
                continue
            nxt = notes[k + 1][1] if k + 1 < len(notes) else None
            if s % 8 == 0 or nxt is None or abs(nxt - m) > 2 or nxt % 12 not in ch['pcs']:
                bad.append((i, s, m, CYCLE[i]))
    print('melody vs chords:', 'every on-beat note is a chord tone or steps to one' if not bad else bad)
    assert not bad


def clashes(m, chord):
    """True if pitch m sits a semitone from any tone of the chord."""
    return any((m - p) % 12 in (1, 11) for p in CH[chord]['pcs'])


# ── oscillators: band-limited (polyBLEP) saw and pulse ──────────────────────
def polyblep(p, dt):
    y = np.zeros_like(p)
    dt = np.broadcast_to(dt, p.shape)
    m = p < dt
    t = p[m] / dt[m]; y[m] = t + t - t * t - 1
    m = p > 1 - dt
    t = (p[m] - 1) / dt[m]; y[m] = t * t + t + t + 1
    return y


def bl_saw(f, n, ph=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,))
    p = (ph + np.cumsum(f / SR)) % 1.0
    return 2 * p - 1 - polyblep(p, f / SR)


def bl_pulse(f, n, duty=0.5, ph=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,))
    p = (ph + np.cumsum(f / SR)) % 1.0
    dt = f / SR
    y = np.where(p < duty, 1.0, -1.0)
    return y + polyblep(p, dt) - polyblep((p + 1 - duty) % 1.0, dt)


def swept(x, fc0, fc1, tau, q, chunk=64):
    """Low-pass snapping from fc0 down to fc1 with time constant tau."""
    n = len(x); out = np.empty(n); zi = np.zeros(2)
    for i in range(0, n, chunk):
        fc = fc1 + (fc0 - fc1) * np.exp(-i / SR / tau)
        w = 2 * np.pi * fc / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


# ── drums ───────────────────────────────────────────────────────────────────
def tail(n, fade):
    """A raised-cosine fade over the last `fade` seconds of an n-sample
    one-shot, so a truncated decay ends at zero instead of a click."""
    t = np.arange(n) / SR
    u = np.clip((n / SR - t) / fade, 0, 1)
    return 0.5 - 0.5 * np.cos(np.pi * u)


def kick():
    n = int(0.26 * SR); t = np.arange(n) / SR
    f = 55 + 110 * np.exp(-t / 0.018)          # settles on A1
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.085)
    click = hp1(np.random.default_rng(31).standard_normal(n), 2500) * np.exp(-t / 0.0025) * 0.25
    return np.tanh(1.4 * (body + click)) / np.tanh(1.4) * tail(n, 0.05)


def snare():
    """Metallic: band-passed noise, a ring-modulated pair and a short body."""
    n = int(0.22 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(32).standard_normal(n)
    noise = bp(hp1(z, 1200), 3400, 0.9) * np.exp(-t / 0.055)
    ring = np.sin(2 * np.pi * 220 * t) * np.sin(2 * np.pi * 1540 * t) * np.exp(-t / 0.035)   # E6 + A6
    body = np.sin(2 * np.pi * 220 * t) * np.exp(-t / 0.03)       # tuned to A
    return (noise * 1.3 + ring * 0.55 + body * 0.45) * tail(n, 0.03)


METAL = [205.3, 304.4, 369.6, 522.7, 540.0, 800.0]


def _metal(n):
    x = sum(bl_pulse(f * 1.02, n, 0.5, k * 0.13) for k, f in enumerate(METAL)) / 6
    return hp(bp(x, 8200, 1.1), 6500, 0.7)


HAT_SRC = _metal(int(0.3 * SR))


def hat(open_=False, v=1.0):
    """An open hat is choked, as on an 808, by the closed hat a sixteenth
    later: it rings for one step and fades in 8 ms."""
    n = int((S16 + 0.004 if open_ else 0.06) * SR)
    return lp1(HAT_SRC[:n], 11000) * perc(n, 0.0008, 0.11 if open_ else 0.022) * tail(n, 0.008 if open_ else 0.012) * v


def tom(m):
    n = int(0.32 * SR); t = np.arange(n) / SR
    f = hz(m) * (1 + 0.55 * np.exp(-t / 0.045))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = (np.sin(ph) + 0.18 * np.sin(2 * ph)) * np.exp(-t / 0.17)
    z = np.random.default_rng(33).standard_normal(n)
    return (x + bp(z, 1800, 1.0) * np.exp(-t / 0.01) * 0.25) * tail(n, 0.1)


TOMS = {'hi': 55, 'mid': 50, 'lo': 45}           # G3 D3 A2
TOM_PAN = {'hi': 0.35, 'mid': 0.0, 'lo': -0.35}


def tom_pitch(which, chord):
    """A2 D3 G3, except that the high tom is retuned to G#3 over E (whose
    G# the G3 would rub against): every fill falls on the E bar, where it
    now runs leading note - seventh - tonic into the next Am."""
    m = TOMS[which]
    return m + 1 if clashes(m, chord) and not clashes(m + 1, chord) else m


# ── pitched voices ──────────────────────────────────────────────────────────
def bass_note(m, accent):
    gate = E8 * 0.55
    n = int((gate + 0.05) * SR)
    x = 0.6 * bl_pulse(hz(m), n, 0.5) + 0.4 * bl_saw(hz(m) * 1.003, n, 0.2)
    x = swept(x, 1800 if accent else 1300, 400, 0.045, 1.5)
    return x * adsr(n, 0.002, 0.06, 0.7, 0.03, gate)


def square_note(m, duty, v=1.0):
    """A staccato square blip: hard on, short, clean off."""
    n = int(0.17 * SR); t = np.arange(n) / SR
    x = bl_pulse(hz(m), n, duty, 0.25)
    x = lp1(lp1(x, 3400), 4200)
    env = np.minimum(1, t / 0.0015) * (0.75 + 0.25 * np.exp(-t / 0.03)) * np.clip((0.1 - t) / 0.012, 0, 1)
    return x * env * v


def blip(m):
    n = int(0.09 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * hz(m) * t) * perc(n, 0.001, 0.025) * tail(n, 0.01)


PENT = [81, 84, 86, 88, 91, 93]                  # A minor pentatonic, A5 - A6


def blip_notes(chord):
    """The pentatonic notes that do not rub a semitone against the chord:
    all six over Am, no E over F or Dm, no C over G, only D and E over E."""
    return [m for m in PENT if not clashes(m, chord)]


def carrier(chord, dur):
    """The vocoder's carrier: each chord tone as two saws and a pulse."""
    n = int((dur + 0.06) * SR)
    x = np.zeros(n)
    for k, m in enumerate(chord):
        x += bl_saw(hz(m) * 2 ** (-4 / 1200), n, 0.1 * k) + bl_saw(hz(m) * 2 ** (4 / 1200), n, 0.37 + 0.1 * k)
        x += 0.5 * bl_pulse(hz(m) / 2, n, 0.5, 0.2 * k)
    return x / len(chord) * adsr(n, 0.012, 0.08, 0.9, 0.05, dur)


# vowel formants (Hz) and their weights
VOWELS = {'ah': (760, 1150, 2500), 'oh': (560, 850, 2400), 'oo': (320, 820, 2250), 'eh': (540, 1750, 2480)}
FGAIN = (1.0, 0.7, 0.32)
FQ = (5.0, 7.0, 9.0)
CHOP_VOWELS = ['ah', 'oh', 'eh', 'oo']


def vowel_at(tl_time):
    """The vowel target at a time in the loop: in the breakdown a new vowel
    on every beat, elsewhere a slow ah - oh - ah over two bars."""
    pos = (tl_time / BAR) % BARS
    b = int(pos)
    if section(b) == 'C':
        beat = int((pos - b) * 4)
        return VOWELS[CHOP_VOWELS[(b * 4 + beat + b // 2) % 4]]
    u = (pos % 2) / 2
    w = 0.5 - 0.5 * np.cos(2 * np.pi * u)
    a, o = VOWELS['ah'], VOWELS['oh']
    if b % 8 in (6, 7):
        o = VOWELS['eh']
    return tuple(a[i] + (o[i] - a[i]) * w for i in range(3))


def formant_bank(x, chunk=256):
    """Carrier through three band-passes whose centres glide (25 ms) to the
    current vowel. The chunk grid is the loop's own (a lap is 12800 chunks),
    so the result is periodic."""
    n = len(x)
    out = np.zeros_like(x)
    zi = np.zeros((3, 2, 2))
    fcur = np.array(VOWELS['ah'], float)
    k = np.exp(-chunk / SR / 0.025)
    for i in range(0, n, chunk):
        tgt = np.array(vowel_at(i / SR - tl.t0))
        fcur = tgt + (fcur - tgt) * k
        for j in range(3):
            w = 2 * np.pi * fcur[j] / SR
            al = np.sin(w) / (2 * FQ[j]); c = np.cos(w)
            b = np.array([al, 0, -al]) / (1 + al); a = np.array([1, -2 * c / (1 + al), (1 - al) / (1 + al)])
            for ch in range(2):
                y, zi[j, ch] = lfilter(b, a, x[i:i + chunk, ch], zi=zi[j, ch])
                out[i:i + chunk, ch] += FGAIN[j] * y
    return out


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    check_melody()
    drums, bass, voc, mel, blips = (tl.bus() for _ in range(5))
    for b in tl.bars_range():
        t = b * BAR
        lb, sec = b % BARS, section(b)
        c = CH[chord_at(b)]
        # drums
        kicks = (0, 8) if lb % 2 == 0 else (0, 8, 14)
        if sec == 'C':
            kicks = (0, 8)
        for s in kicks:
            drums.add(t + s * S16, kick(), gain=0.42 if s != 14 else 0.3)
        if part('snare', b):
            for s in (4, 12):
                drums.add(t + s * S16, snare(), pan=0.05, gain=0.2)
        for s in range(16):
            if sec == 'C' and s % 2:
                continue
            open_ = sec == 'D' and s == 14 and lb % 2 == 1
            v = 1.0 if s % 4 == 2 else 0.55 if s % 2 == 0 else 0.4
            if sec == 'A':
                v *= 0.8
            drums.add(t + s * S16, hat(open_, v), pan=0.3, gain=0.075)
        if part('toms', b):
            fig = ([(3, 'hi'), (6, 'mid'), (10, 'lo'), (11, 'lo')] if lb % 2 == 0 else
                   [(3, 'hi'), (6, 'mid'), (12, 'mid'), (13, 'lo'), (14, 'lo')])
            for s, which in fig:
                if part('fill', b) and s >= 12:
                    continue                     # the fill has the end of the bar
                drums.add(t + s * S16, tom(tom_pitch(which, chord_at(b))), pan=TOM_PAN[which], gain=0.18)
        if part('fill', b):
            for s, which in ((12, 'hi'), (13, 'hi'), (14, 'mid'), (15, 'lo')):
                drums.add(t + s * S16, tom(tom_pitch(which, chord_at(b))), pan=TOM_PAN[which], gain=0.26)
        # bass: pulsing eighths
        for k, iv in enumerate((0, 0, 12, 0, 0, 7, 12, 7)):
            bass.add(t + k * E8, bass_note(c['root'] + iv, k in (0, 3)), gain=0.2)
        # vocoder carrier
        if part('voc', b):
            if sec == 'C':
                for q in range(4):
                    voc.add(t + q * BEAT, carrier(c['voc'], BEAT * 0.72), gain=0.9)
            else:
                voc.add(t, carrier(c['voc'], BAR - 0.02), gain=0.85)
        # melody: call and response
        if part('mel', b):
            row = STEPS[b % 8]
            call = (b % 8) in CALL
            for s, m in enumerate(row):
                if m is None:
                    continue
                v = 1.0 if s % 8 == 0 else 0.85
                if call:
                    mel.add(t + s * S16, square_note(m, 0.5, v), pan=-0.3, gain=0.25)
                    if sec == 'D':
                        mel.add(t + s * S16, square_note(m - 12, 0.125, v), pan=0.2, gain=0.17)
                else:
                    mel.add(t + s * S16, square_note(m, 0.125, v), pan=0.3, gain=0.265)
                    if sec == 'D':
                        mel.add(t + s * S16, square_note(m + 12, 0.5, v), pan=-0.2, gain=0.085)
        # blips
        if part('blips', b):
            r = rng('blips', lb)
            pool = blip_notes(chord_at(b))
            for s in range(16):
                if r.random() < 0.28:
                    blips.add(t + s * S16, blip(pool[int(r.integers(0, len(pool)))]),
                              pan=float(r.uniform(-0.7, 0.7)), gain=0.15)

    vocx = formant_bank(voc.x)
    # a short slapback on the melody and blips: a dotted eighth, two repeats
    d = int(3 * S16 * SR)
    melx = mel.x.copy()
    for k, g in ((1, 0.28), (2, 0.1)):
        melx[d * k:] += lp1(mel.x[:-d * k], 3000)[:, ::-1] * g
    blx = blips.x.copy()
    blx[d:] += blips.x[:-d][:, ::-1] * 0.35
    room = make_ir(0.7, dark=5000, seed=41, pre=0.006)
    wet = reverb(drums.x * 0.1 + vocx * 0.2 + melx * 0.15 + blx * 0.3, room)
    mix = drums.x + bass.x + vocx * 0.5 + melx + blx + wet * 0.35
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
