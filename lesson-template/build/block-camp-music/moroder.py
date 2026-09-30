#!/usr/bin/env python3
"""Block Camp soundtrack "Momentum" (Going To): Italo-disco, plans in motion.

Brief, 2026-09-30, for the Going To camp: Giorgio Moroder / Italo-disco -
about 122-126 BPM, a relentless sixteenth-note sequenced bass (an octave-and-
fifth gated pattern on a warm saw through a resonant filter that sweeps across
the phrases), four on the floor, handclaps on 2 and 4, open hats on the
offbeats, shimmering string-machine chords, a bright arpeggio, and a simple
singable synth lead in the middle section. Minor, euphoric not aggressive. An
original piece in that idiom: no sequence, riff or melody is taken from any
record.

G minor, 4/4, 125 BPM (a sixteenth is exactly 0.12 s), a chord every two bars:

    P1  Gm  Eb  Cm  D7    i   VI iv  V7
    P2  Eb  F   Bb  D7    VI  VII III V7   (the lift: three major chords)

    bars  0-7   P1  kick, sequenced bass, closed hats; open hats and strings from bar 4
    bars  8-15  P1  + claps, strings full, the arpeggio
    bars 16-23  P1  the lead, first phrase
    bars 24-31  P2  the lead, second phrase, higher; the arpeggio back
    bars 32-39  P1  breakdown: no kick for four bars while the bass filter closes;
                    then the kick, the filter opening, a snare roll and a riser to the top

The bass is two polyBLEP saws a few cents apart with a sine under them, each
sixteenth gated at 60% through a resonant low-pass with its own envelope
(accents on the beat), the cutoff riding a slow curve across the loop. Strings
are three detuned saws a note through two choruses (the ensemble shimmer); the
arpeggio a narrow pulse with a dotted-eighth echo; the lead two saws and a
pulse, gliding, with delayed vibrato, one voice across both phrases. Everything
but the drums ducks gently under the kick (the bass at a third of the depth,
so its beat accents survive). 40 bars = 76.8 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/moroder.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, perc, pingpong,
                      make_ir, reverb, chorus, finish)

tl = Timeline(bpm=125, bars=40, pre=4, post=1)
BAR, S16, BARS = tl.bar, tl.s16, tl.bars       # 1.92 s, 0.12 s
LOOP = tl.loop                                 # 76.8 s
CHUNK = 240                                    # 5760 samples a sixteenth = 24 chunks

PC = {'C': 0, 'C#': 1, 'D': 2, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'A': 9, 'Bb': 10, 'B': 11}

#        bass root  strings            chord tones
CH = {
    'Gm': (43, (62, 67, 70, 74), 'G Bb D'),
    'Eb': (39, (63, 67, 70, 75), 'Eb G Bb'),
    'Bb': (46, (62, 65, 70, 74), 'Bb D F'),
    'F':  (41, (60, 65, 69, 72), 'F A C'),
    'Cm': (36, (60, 63, 67, 72), 'C Eb G'),
    'D7': (38, (62, 66, 69, 72), 'D F# A C'),
}
P1 = ('Gm', 'Eb', 'Cm', 'D7')
P2 = ('Eb', 'F', 'Bb', 'D7')


def chord_at(b):
    b %= BARS
    return (P2 if b // 8 == 3 else P1)[(b % 8) // 2]


def tones(name):
    return {PC[s] for s in CH[name][2].split()}


def part(name, b):
    b %= BARS; blk, i = b // 8, b % 8
    return {
        'kick':    not (blk == 4 and i < 4),
        'clap':    blk in (1, 2, 3) or (blk == 4 and i >= 4),
        'ohat':    blk in (1, 2, 3) or (blk == 0 and i >= 4) or (blk == 4 and i >= 4),
        'chat':    blk != 4 or i >= 6,
        'strings': blk != 0 or i >= 4,
        'arp':     blk in (1, 3, 4),
        'roll':    b == 39,
        'riser':   b in (38, 39),
    }[name]


# bass cutoff across the loop (bar, Hz), log-interpolated; the value at 40 is the value at 0
CUT = [(0, 650), (8, 1000), (16, 950), (24, 1250), (32, 1500), (35.5, 380), (40, 650)]


def cutoff(bpos):
    xs, ys = zip(*CUT)
    return float(np.exp(np.interp(bpos % BARS, xs, np.log(ys))))


# the sequence: sixteenths as intervals over the root; the second bar of each chord turns around
SEQ_A = (0, 12, 0, 12, 7, 12, 0, 12, 0, 12, 0, 12, 7, 12, 7, 12)
SEQ_B = (0, 12, 0, 12, 7, 12, 0, 12, 0, 12, 7, 12, 0, 12, 19, 12)

# ── the lead: (midi, sixteenths), 128 = 8 bars ─────────────────────────────
LEAD_A = [(67, 4), (70, 4), (74, 6), (72, 2),     (70, 4), (69, 4), (67, 8),        # Gm
          (67, 4), (70, 4), (75, 6), (72, 2),     (70, 8), (67, 8),                 # Eb
          (79, 6), (75, 2), (72, 4), (75, 4),     (79, 6), (77, 2), (75, 8),        # Cm
          (74, 4), (72, 4), (69, 4), (66, 4),     (69, 8), (72, 4), (74, 4)]        # D7
LEAD_B = [(79, 6), (77, 2), (75, 4), (79, 4),     (70, 8), (75, 4), (79, 4),        # Eb
          (77, 6), (75, 2), (72, 4), (77, 4),     (77, 12), (75, 4),                # F
          (74, 6), (72, 2), (70, 4), (74, 4),     (77, 12), (79, 4),                # Bb
          (78, 8), (74, 4), (72, 4),              (69, 4), (74, 12)]                # D7
LEAD = LEAD_A + LEAD_B                          # one continuous voice, bars 16-31


def check_line(name, mel, bar0):
    """A note on beat 1 or 3, or a dotted quarter or longer, or held across
    a barline, must be a tone of the chord there. A non-chord tone a quarter
    long, or one a semitone from a string note, must move on by step (a
    passing or neighbour tone); a quarter-long one that rubs a semitone must
    be a true passing tone, stepped into and out of in the same direction.
    (A short one clear of the strings may leap: the Eb over F is F7's 7th.)"""
    pos = 0
    for j, (m, d) in enumerate(mel):
        ch0 = chord_at(bar0 + pos // 16)
        for q in range(pos, pos + d):
            if q == pos and (q % 8 == 0 or d >= 6) or (q > pos and q % 16 == 0):
                ch = chord_at(bar0 + q // 16)
                assert m % 12 in tones(ch), f'{name}: {m} at bar {bar0 + q // 16} 16th {q % 16} over {ch}'
        rub = any(abs(v - m) == 1 for v in CH[ch0][1])
        if m % 12 not in tones(ch0) and (d >= 4 or rub):
            prv = mel[j - 1][0] if j else None
            nxt = mel[j + 1][0] if j + 1 < len(mel) else None
            where = f'{name}: {m} at bar {bar0 + pos // 16} 16th {pos % 16} over {ch0}'
            assert nxt is not None and 0 < abs(nxt - m) <= 2, where + ' does not resolve by step'
            if d >= 4 and rub:
                assert prv is not None and 0 < abs(m - prv) <= 2 and (m - prv) * (nxt - m) > 0, \
                    where + ' rubs a semitone on the strings and is not a passing tone'
        pos += d
    assert pos % 128 == 0, (name, pos)


assert sum(d for _, d in LEAD_A) == sum(d for _, d in LEAD_B) == 128
check_line('lead', LEAD, 16)


# ── oscillators and filters ─────────────────────────────────────────────────
def blep_saw(f, n, ph0=0.0):
    f = np.broadcast_to(np.asarray(f, float), (n,))
    dt = f / SR
    p = (ph0 + np.cumsum(dt)) % 1.0
    y = 2 * p - 1
    m = p < dt
    u = p[m] / dt[m]; y[m] -= u + u - u * u - 1
    m = p > 1 - dt
    u = (p[m] - 1) / dt[m]; y[m] -= u * u + u + u + 1
    return y


def blep_pulse(f, n, duty=0.5, ph0=0.0):
    return 0.5 * (blep_saw(f, n, ph0) - blep_saw(f, n, (ph0 + duty) % 1.0))


def swept_bp(x, f0, f1, q, chunk=256):
    """A band-pass whose centre glides f0 -> f1 (exponentially), the filter
    state carried from chunk to chunk so the sweep has no seams."""
    out = np.empty_like(x); zi = np.zeros(2); n = len(x)
    for i in range(0, n, chunk):
        fc = f0 * (f1 / f0) ** (i / max(n - 1, 1))
        w = 2 * np.pi * fc / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


def tv_lp(x, fc, q=0.707):
    out = np.empty_like(x); zi = np.zeros(2)
    for j, i in enumerate(range(0, len(x), CHUNK)):
        w = 2 * np.pi * min(fc[j], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + CHUNK], zi = lfilter(b / a[0], a / a[0], x[i:i + CHUNK], zi=zi)
    return out


# ── instruments ─────────────────────────────────────────────────────────────
def bass_note(m, cut, acc, key):
    n = int(0.22 * SR); t = np.arange(n) / SR
    r = rng('bass', key)
    x = 0.55 * blep_saw(hz(m) * 2 ** (-4 / 1200), n, r.random()) + 0.45 * blep_saw(hz(m) * 2 ** (4 / 1200), n, r.random())
    tc = t[::CHUNK]
    x = tv_lp(x, cut * (1 + (1.2 + 1.6 * acc) * np.exp(-tc / 0.04)), 2.4)
    x = x * 0.8 + 0.4 * np.sin(2 * np.pi * hz(m) * t)
    return x * adsr(n, 0.002, 0.05, 0.75, 0.035, 0.6 * S16)


def string_note(m, dur, key):
    # release short enough that a chord is gone ~0.3 s into the next: D7 into Eb or Gm
    # moves every voice by a semitone, and a long crossfade sounds both chords at once
    n = int((dur + 0.6) * SR)
    r = rng('str', key)
    x = sum(blep_saw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-9, 0, 9)) / 3
    x = hp1(lp(lp1(x, 4500), 2600, 0.7), 200)
    return x * adsr(n, 0.2, 0.4, 0.85, 0.4, dur)


def arp_note(m):
    n = int(0.22 * SR)
    x = lp(blep_pulse(hz(m), n, 0.3), 3400, 0.8)
    return x * perc(n, 0.002, 0.065)


def lead_phrase(mel):
    n = int((sum(d for _, d in mel) * S16 + 1.0) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n)
    pos = 0; b = 0
    for m, d in mel:
        a, b = int(pos * S16 * SR), int((pos + d) * S16 * SR)
        tt = np.arange(b - a) / SR
        f[a:b] = hz(m)
        g[a:b] = np.minimum(1, tt / 0.012) * (0.8 + 0.2 * np.exp(-tt / 0.18))
        g[max(b - int(0.03 * SR), a):b] *= 0.55
        vib[a:b] = np.clip((tt - 0.28) / 0.35, 0, 1)
        pos += d
    f[b:] = f[b - 1]
    g[b:] = g[b - 1] * np.exp(-np.arange(n - b) / SR / 0.12)
    g = lp1(g, 60)
    a1 = np.exp(-1 / (0.028 * SR))
    fl = lfilter([1 - a1], [1, -a1], f - f[0]) + f[0]
    t = np.arange(n) / SR
    fl = fl * 2 ** (0.15 / 12 * vib * np.sin(2 * np.pi * 5.6 * t))
    x = (0.4 * blep_saw(fl * 2 ** (-6 / 1200), n, 0.1) + 0.4 * blep_saw(fl * 2 ** (6 / 1200), n, 0.6)
         + 0.3 * blep_pulse(fl, n, 0.5, 0.3))
    return lp(lp1(x, 5000), 2600, 0.9) * g


def kick():
    n = int(0.4 * SR); t = np.arange(n) / SR
    f = 56 + 90 * np.exp(-t / 0.03)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.15)
    click = lp1(np.random.default_rng(1).standard_normal(n), 3000) * np.exp(-t / 0.003) * 0.25
    return np.tanh(1.3 * (body + click)) / np.tanh(1.3)


def clap():
    n = int(0.35 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(4).standard_normal(n)
    env = sum(np.where(t >= d, np.exp(-(t - d) / 0.006), 0) for d in (0.0, 0.011, 0.021))
    env += 0.7 * np.where(t >= 0.028, np.exp(-(t - 0.028) / 0.09), 0)
    return (bp(z, 1250, 0.9) + 0.35 * bp(z, 2600, 1.2)) * env


def hat(open_, seed):
    n = int((0.26 if open_ else 0.06) * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    return lp(hp(hp(z, 5000), 5000), 7500) * perc(n, 0.001, 0.1 if open_ else 0.016)


def snare(seed):
    n = int(0.2 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    return bp(z, 2200, 0.7) * np.exp(-t / 0.05) + 0.5 * np.sin(2 * np.pi * 200 * t) * np.exp(-t / 0.04)


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    drums, bass, strings, arp, lead, fx = (tl.bus() for _ in range(6))
    kicks = []
    for b in tl.bars_range():
        t = b * BAR; bb = b % BARS; blk, i = bb // 8, bb % 8
        name = chord_at(b); root, voic, _ = CH[name]
        if part('kick', b):
            for s in (0, 4, 8, 12):
                drums.add(t + s * S16, kick(), gain=0.2); kicks.append(t + s * S16)
        if part('clap', b):
            for s in (4, 12):
                drums.add(t + s * S16, clap(), pan=0.05, gain=0.14)
        if part('ohat', b):
            for s in (2, 6, 10, 14):
                drums.add(t + s * S16, hat(True, bb * 16 + s), pan=0.25, gain=0.04)
        if part('chat', b):
            for s in range(16):
                if s % 4 != 2:
                    drums.add(t + s * S16, hat(False, 999 + bb * 16 + s), pan=-0.25,
                              gain=0.025 if s % 2 else 0.016)
        if part('roll', b):
            for s in range(16):
                drums.add(t + s * S16, snare(bb * 16 + s), pan=0.1, gain=0.03 + 0.14 * (s / 15) ** 1.6)
        # the sequencer: sixteenths, accent on the beat, the cutoff riding the loop's curve
        seq = SEQ_B if b % 2 else SEQ_A
        for s, iv in enumerate(seq):
            c = cutoff(bb + s / 16)
            bass.add(t + s * S16, bass_note(root + iv, c, 1.0 if s % 4 == 0 else 0.35, (bb, s)),
                     pan=0.0, gain=0.23 if s % 4 == 0 else 0.19)
        # strings: a chord every two bars
        if part('strings', b) and b % 2 == 0:
            lvl = 0.6 if blk == 0 else 1.0
            for k, m in enumerate(voic):
                strings.add(t, string_note(m, 2 * BAR - 0.12, (bb, k)), pan=(-0.6, -0.2, 0.2, 0.6)[k], gain=0.15 * lvl)
        # the arpeggio: up and down two octaves of the chord
        if part('arp', b):
            tn = [m for m in range(67, 100) if m % 12 in tones(name)][:6]      # G4 up to about D6
            order = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1)
            lv = 0.8 if blk == 3 else 1.0
            for s, k in enumerate(order):
                arp.add(t + s * S16, arp_note(tn[k]), pan=(-0.45 if s % 2 else 0.45),
                        gain=(0.07 + (0.02 if s % 4 == 0 else 0)) * lv)
        if part('riser', b) and bb == 38:
            n = int(2 * BAR * SR); u = np.arange(n) / n
            z = rng('riser', bb).standard_normal(n)
            y = swept_bp(z, 350, 3500, 1.1)                                 # up to 3.5 kHz, no higher
            fade = np.minimum(1, (n - np.arange(n)) / (0.02 * SR))           # 20 ms off, not a cut
            fx.add(t, y * u ** 2.4 * fade, gain=0.10)
    # the lead is one voice across both phrases, so bar 24 is a glide, not two notes at once
    for lap in (-1, 0, 1):
        t0 = lap * LOOP + 16 * BAR
        if -tl.pre * BAR - 17 * BAR < t0 < (BARS + tl.post) * BAR:
            lead.add(t0, lead_phrase(LEAD), pan=0.0, gain=0.15)

    # everything but the drums ducks under the kick, gently: a 6 ms dip in (not a
    # 32% step, which clicked on the held strings and the reverb) and a release
    # that lands exactly on 1 just before the next kick (0.48 s on)
    tt = np.arange(tl.n) / SR - tl.t0
    pump = np.ones(tl.n)
    WIN = 0.47
    for k in kicks:
        i0 = tl.smp(k); i1 = min(tl.n, i0 + int(WIN * SR))
        if i1 > max(i0, 0):
            j0 = max(i0, 0)
            u = tt[j0:i1] - k
            duck = 0.32 * np.minimum(1, u / 0.006) * (np.exp(-u / 0.1) - np.exp(-WIN / 0.1)) / (1 - np.exp(-WIN / 0.1))
            pump[j0:i1] = np.minimum(pump[j0:i1], 1 - duck)
    pump = pump[:, None]

    stringsx = chorus(chorus(strings.x, LOOP / 96, depth_ms=1.6, base_ms=6.0, mix=0.6, t0=tl.t0),
                      LOOP / 20, depth_ms=3.0, base_ms=10.0, mix=0.4, t0=tl.t0)
    arpx = arp.x + pingpong(arp.x, 3 * S16, 0.42, 6, 3800)
    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.3, 4, 3000) * 0.6
    # the send is high-passed so the kick does not leave a low rumble in the room
    wet = reverb(hp1(stringsx * 0.35 + arpx * 0.3 + leadx * 0.3 + drums.x * 0.08 + fx.x * 0.4, 160),
                 make_ir(2.2, dark=4200, seed=5, pre=0.02))
    # the bass ducks at a third of the depth: at full depth the pump took 32% off exactly
    # the notes the sequencer accents, and the beat came out quieter than the offbeats
    bpump = 1 - (1 - pump) / 3
    stems = dict(drums=drums.x, bass=bass.x * bpump, strings=stringsx * pump, arp=arpx * pump,
                 lead=leadx, fx=fx.x, reverb=wet * 0.45 * pump)
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        i0 = tl.smp(0)
        for k, v in stems.items():
            row = []
            for s in range(0, BARS, 4):
                seg = v[i0 + int(s * BAR * SR):i0 + int((s + 4) * BAR * SR)]
                row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9))
            seg = v[i0:i0 + int(LOOP * SR)].mean(1)
            sp = np.abs(np.fft.rfft(seg)) ** 2; fq = np.fft.rfftfreq(len(seg), 1 / SR)
            hi = 10 * np.log10(sp[fq > 3000].sum() / (sp.sum() + 1e-12) + 1e-12)
            print(f'{k:8s}' + ' '.join(f'{r:6.0f}' for r in row) + f'   >3k {hi:5.1f} dB')
    return finish(tl, mix, 'going-to', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
