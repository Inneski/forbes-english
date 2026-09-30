#!/usr/bin/env python3
"""Block Camp soundtrack "Factory" (Passive Present Simple: the descent).

Style brief, 2026-09-30: Harold Faltermeyer's bouncy 80s synth-pop of the
Beverly Hills Cop era - a staccato, playful square/saw lead with octave
jumps and rests, a punchy syncopated synth bass, a crisp drum machine with
claps, chord stabs. The melody is new and deliberately unlike Axel F: the
hook starts on the minor third and drops an octave, it never runs
root-fifth-octave. Bar 9's answer climbs F Ab Bb C; the review's first
pass found it as F C Db C, the shape and register of Axel F's second
phrase, and changed it.

F minor, 118 BPM (118.03, so a sixteenth is a whole 6100 samples and the
seam is sample-exact), 4/4. Two eight-bar progressions, two bars a chord:
    A  Fm | Bbm | Db | C C7          (cycles 0, 1, 3)
    B  Db | Eb  | Fm | C C7          (cycle 2)
The bass walks into every change from the scale step below.

Instruments: an anti-aliased (polyBLEP) square+saw lead with a filter pluck
per note, detached, with a dotted-eighth echo; a saw+square bass with a
snapping filter and a little sub; four-note detuned-saw chord stabs; a soft
string pad in the middle; a square pluck counter-riff on the chord's top
three notes; a drum machine - a round kick tuned to F2, the tonic, a
four-burst hand clap with a short snare body on F3, closed and open hats,
toms tuned down a C7 arpeggio. Every pitched drum is in the key: at 56 Hz
the kick pulled the key toward F major, at C2 it glided through Db (a
semitone on the Db bass) and toward Db major, and the clap rang F#.

The pulse waves are zero-mean (see bpulse): the pluck's DC offset was a
quarter of its energy, all a sub-bass thump under 60 Hz.

Measured (render + analysis, review 2026-09-30): key F minor (Krumhansl
0.76, next F major 0.62), magnitude centroid median ~1570 Hz, under 60 Hz
-13 dB of the total, the breakdown about 3 dB under the rest (level with
it through a 250 Hz high-pass, which is what a phone plays).

Arrangement (cycle = 8 bars):
    0  groove: drums, bass, offbeat stabs; the pluck riff joins at bar 4
    1  lead A over progression A, stabs sparse under it
    2  lead B over progression B, offbeat stabs, pad, open hats
    3  breakdown: no kick, half-time bass, pad and pluck, a snare roll and
       riser in bar 27; bars 28-31 the groove rebuilds into bar 0
32 bars = 65.07 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/factory.py [--wav preview.wav]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, bp, swept_lp, adsr, perc,
                      pingpong, make_ir, reverb, chorus, finish)

tl = Timeline(bpm=720000 / 6100, bars=32)     # 118.03: a sixteenth is exactly 6100 samples
BAR, S16 = tl.bar, tl.s16

#        bass root  stab voicing
FM   = (41, [53, 56, 60, 65])     # F  Ab C  F
BBM  = (34, [53, 58, 61, 65])     # F  Bb Db F
DB   = (37, [53, 56, 61, 65])     # F  Ab Db F
EB   = (39, [55, 58, 63, 67])     # G  Bb Eb G
C    = (36, [52, 55, 60, 64])     # E  G  C  E
C7   = (36, [52, 55, 58, 64])     # E  G  Bb E
PROG_A = [FM, FM, BBM, BBM, DB, DB, C, C7]
PROG_B = [DB, DB, EB, EB, FM, FM, C, C7]
KEY_PCS = {5, 7, 8, 10, 0, 1, 3, 4}           # F minor plus E, the leading tone


def chord_at(b):
    b %= 32
    return (PROG_B if b // 8 == 2 else PROG_A)[b % 8]


def part(name, b):
    b %= 32; cyc, i = b // 8, b % 8
    brk = cyc == 3 and i < 4
    return {
        'kick':   not brk,
        'clap':   True,
        'hats16': not ((cyc == 0 and i < 2) or brk),
        'ohat':   cyc == 2,
        'bass':   True,
        'stabs':  not brk,
        'pad':    cyc == 2 or brk,
        'pluck':  cyc == 3 or (cyc == 0 and i >= 4),
        'lead':   cyc in (1, 2),
    }[name]


# ── band-limited oscillators (polyBLEP), kept soft ─────────────────────────
def _blep_saw_ph(f, n, ph0):
    dt = np.broadcast_to(np.asarray(f, float), (n,)) / SR
    p = (ph0 + np.cumsum(dt)) % 1.0
    y = 2 * p - 1
    lo = p < dt
    t = p[lo] / dt[lo]
    y[lo] -= t + t - t * t - 1
    hi = p > 1 - dt
    t = (p[hi] - 1) / dt[hi]
    y[hi] -= t * t + t + t + 1
    return y


def bsaw(f, n, ph0=0.0):
    return _blep_saw_ph(f, n, ph0)


def bpulse(f, n, duty=0.5, ph0=0.0):
    """High for the first `duty` of each cycle, low after; two BLEP saws.
    Zero-mean on purpose: a +1/-1 pulse of duty 0.25 averages -0.5, and that
    offset, shaped by the note envelope, is a sub-bass thump on every note
    (it was a quarter of the pluck's energy, all under 60 Hz)."""
    return -(_blep_saw_ph(f, n, ph0) - _blep_saw_ph(f, n, (ph0 - duty) % 1.0))


# ── drums ───────────────────────────────────────────────────────────────────
def kick():
    n = int(0.4 * SR); t = np.arange(n) / SR
    # Settles on F2, the tonic. A C2 kick spent most of its body gliding
    # through 65-80 Hz (C2 to Eb2): a semitone under the Db bass for a
    # quarter of the loop, and it pulled the measured key toward Db major.
    f = hz(41) + 110 * np.exp(-t / 0.016)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.1)
    click = lp1(hp1(np.random.default_rng(21).standard_normal(n), 1500), 6000) * np.exp(-t / 0.003) * 0.3
    return np.tanh(1.5 * (body + click)) / np.tanh(1.5)


def clap():
    """Drum-machine hand clap: four close bursts then a short tail, centred
    near 1.2 kHz so it cracks without hiss; a snare body underneath."""
    n = int(0.4 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(22).standard_normal(n)
    env = np.zeros(n)
    for k, d in enumerate((0.0, 0.009, 0.018, 0.027)):
        env += (t >= d) * np.exp(-np.clip(t - d, 0, None) / 0.0045) * (0.75 if k < 3 else 1.0)
    tail = (t >= 0.027) * np.exp(-np.clip(t - 0.027, 0, None) / 0.11)
    x = bp(z, 1250, 0.9) * (env + 0.55 * tail) + 0.35 * bp(z, 2600, 1.4) * env
    body = np.sin(2 * np.pi * hz(53) * t) * np.exp(-t / 0.05) * 0.5   # F3; at 185 Hz it rang F# on every backbeat
    return lp1(x * 1.6 + body, 7000)


def snare_tick(v):
    n = int(0.2 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(23).standard_normal(n)
    return (bp(z, 1800, 0.8) * np.exp(-t / 0.05) + np.sin(2 * np.pi * hz(53) * t) * np.exp(-t / 0.04) * 0.6) * v


def hat(open_=False, seed=0):
    n = int((0.3 if open_ else 0.06) * SR)
    z = np.random.default_rng(seed).standard_normal(n)
    x = lp(hp1(hp1(z, 6500), 6500), 11000)
    return x * perc(n, 0.0008, 0.11 if open_ else 0.016)


def tom(f0):
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.5 * np.exp(-t / 0.04))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16)


def swept_bp(x, fc_start, fc_end, q, chunk=256):
    """Band-pass whose centre glides exponentially, the filter state carried
    from chunk to chunk (restarting it per chunk left a step at each join)."""
    n = len(x); out = np.empty(n); zi = np.zeros(2)
    for i in range(0, n, chunk):
        fc = fc_start * (fc_end / fc_start) ** (i / max(n - 1, 1))
        w = 2 * np.pi * fc / SR; al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


KICK, CLAP = kick(), clap()


# ── synths ──────────────────────────────────────────────────────────────────
def bass_note(m, dur):
    """Punchy: saw+square through a filter that snaps shut, a little sub."""
    n = int((dur + 0.06) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = 0.55 * bsaw(f, n) + 0.45 * bpulse(f * 1.003, n, 0.5, 0.25)
    x = swept_lp(x, 2200, 320, q=1.5)
    x += 0.25 * np.sin(2 * np.pi * f * t)
    return x * adsr(n, 0.002, 0.07, 0.65, 0.04, dur)


def stab(m, dur, seed):
    n = int((dur + 0.25) * SR)
    r = rng('stab', seed)
    x = sum(bsaw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-9, 0, 9)) / 3
    x += 0.4 * bpulse(hz(m), n, 0.3, r.random())
    x = swept_lp(x, 3400, 850, q=0.9)
    return x * adsr(n, 0.003, 0.09, 0.45, 0.12, dur)


def pad_chord(voicing, dur):
    n = int((dur + 0.8) * SR)
    x = np.zeros(n)
    for k, m in enumerate(voicing):
        r = rng('pad', m, k)
        x += sum(bsaw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-12, -4, 5, 13)) / 4
    x = lp(lp1(x, 1500), 1900, 0.6)
    return x * adsr(n, 0.45, 0.3, 0.8, 0.7, dur) / len(voicing)


def pluck(m):
    n = int(0.35 * SR)
    x = bpulse(hz(m), n, 0.25)
    x = swept_lp(x, 3000, 700, q=1.0)
    return x * perc(n, 0.002, 0.09)


def lead_note(m, length16):
    """Detached square+saw with a filter pluck; notes of an eighth or more
    get a late, shallow vibrato."""
    gate = max(0.075, length16 * S16 * 0.62)
    n = int((gate + 0.14) * SR); t = np.arange(n) / SR
    vib = 1.0
    if length16 >= 2:
        vib = 2 ** (0.14 / 12 * np.clip((t - 0.12) / 0.15, 0, 1) * np.sin(2 * np.pi * 6.0 * t))
    f = hz(m) * vib
    x = 0.55 * bpulse(f, n, 0.5) + 0.4 * bsaw(f * 1.0035, n, 0.37) + 0.2 * bpulse(f * 0.9965, n, 0.3, 0.6)
    x = swept_lp(x, 4200, 1500, q=1.25)
    x = lp1(x, 5500)
    return x * adsr(n, 0.002, 0.07, 0.72, 0.06, gate)


# ── the melody: per bar, (sixteenth, midi, written length in sixteenths) ────
LEAD_A = [
    [(0, 80, 1), (2, 68, 1), (4, 72, 1), (6, 77, 2), (10, 79, 1), (11, 80, 2)],                       # Fm
    [(0, 77, 1), (2, 75, 1), (3, 72, 2), (6, 65, 1), (8, 68, 1), (11, 70, 1), (12, 72, 3)],           # Fm
    [(0, 77, 1), (2, 65, 1), (4, 70, 1), (6, 73, 2), (10, 75, 1), (11, 77, 2)],                       # Bbm
    [(0, 73, 1), (2, 72, 1), (3, 70, 2), (6, 65, 1), (8, 70, 1), (11, 72, 1), (12, 73, 3)],           # Bbm
    [(0, 80, 1), (2, 68, 1), (4, 73, 1), (6, 77, 2), (10, 75, 1), (11, 73, 2)],                       # Db
    [(0, 77, 1), (2, 80, 1), (4, 77, 1), (6, 73, 2), (12, 77, 1), (14, 76, 1)],                       # Db
    [(0, 79, 2), (3, 76, 1), (4, 72, 1), (6, 67, 1), (8, 72, 1), (10, 76, 1), (12, 79, 2), (14, 74, 1)],  # C
    [(0, 72, 1), (2, 60, 1), (4, 64, 1), (6, 67, 2), (10, 70, 1), (12, 67, 2)],                       # C7
]
LEAD_B = [
    [(0, 73, 1), (1, 73, 1), (3, 77, 1), (5, 80, 2), (8, 68, 1), (10, 73, 1), (11, 77, 2)],           # Db
    [(0, 77, 1), (2, 73, 2), (6, 68, 1), (8, 73, 1), (10, 72, 1), (11, 73, 1), (12, 77, 1), (14, 75, 1)],  # Db
    [(0, 75, 1), (1, 75, 1), (3, 79, 1), (5, 82, 2), (8, 70, 1), (10, 75, 1), (11, 79, 2)],           # Eb
    [(0, 79, 1), (2, 75, 2), (6, 70, 1), (8, 75, 1), (10, 73, 1), (11, 75, 1), (12, 82, 1), (14, 79, 1)],  # Eb
    [(0, 80, 2), (3, 77, 1), (4, 72, 1), (6, 77, 1), (8, 80, 1), (10, 79, 1), (11, 80, 1),
     (12, 77, 2), (14, 72, 1)],                                                                       # Fm
    [(2, 65, 1), (3, 77, 1), (6, 65, 1), (7, 77, 1), (10, 75, 1), (11, 77, 1), (12, 80, 1), (13, 79, 1),
     (14, 77, 1)],                                                                                   # Fm
    [(0, 76, 2), (3, 72, 1), (4, 67, 1), (6, 72, 1), (7, 76, 1), (8, 79, 2), (11, 76, 1), (12, 72, 2)],    # C
    [(0, 70, 1), (2, 67, 1), (4, 64, 2), (8, 67, 1), (10, 72, 2)],                                    # C7
]
LEAD = {8 + k: bar for k, bar in enumerate(LEAD_A)}
LEAD.update({16 + k: bar for k, bar in enumerate(LEAD_B)})

# bass, one bar: (sixteenth, interval above the root, length); 'W' walks into the next chord
BASS_1 = [(0, 0, 2), (3, 0, 1), (5, 12, 1), (6, 0, 1), (8, 0, 2), (11, 12, 1), (12, 0, 1), (14, 12, 1)]
BASS_2 = [(0, 0, 2), (3, 0, 1), (5, 12, 1), (6, 0, 1), (8, 0, 2), (11, 12, 1), (12, 7, 2), (14, 'W', 2)]
BASS_HALF = [(0, 0, 5), (6, 12, 1), (8, 0, 5), (14, 12, 1)]
PLUCK = [(0, 2), (3, 0), (6, 1), (8, 2), (11, 0), (14, 1)]    # (sixteenth, index into the top three)


def walk_into(nxt_root):
    for d in (1, 2):
        if (nxt_root - d) % 12 in KEY_PCS:
            return nxt_root - d


def render(wav=None):
    drums, bass, stabs, pad, plk, lead, fx = (tl.bus() for _ in range(7))
    for b in tl.bars_range():
        t = b * BAR
        bm = b % 32; cyc, i = bm // 8, bm % 8
        root, voicing = chord_at(b)
        nroot, _ = chord_at(b + 1)
        # ── drums
        if part('kick', b):
            steps = (0, 8, 10) if i % 2 else (0, 7, 8)
            for s in steps:
                drums.add(t + s * S16, KICK, gain=0.36 if s in (0, 8) else 0.26)
        if part('clap', b):
            if cyc == 3 and i < 4:
                drums.add(t + 12 * S16, CLAP, pan=0.05, gain=0.26)
            else:
                for s in (4, 12):
                    drums.add(t + s * S16, CLAP, pan=0.05, gain=0.30)
        for s in range(16):
            if not part('hats16', b) and s % 2:
                continue
            if part('ohat', b) and s in (6, 14):
                drums.add(t + s * S16, hat(True, bm * 16 + s), pan=0.3, gain=0.06)
                continue
            drums.add(t + s * S16, hat(False, bm * 16 + s), pan=0.3,
                      gain=0.05 if s % 4 == 2 else 0.035 if s % 2 == 0 else 0.022)
        if bm in (15, 23):                    # tom fills, tuned down a C7 arpeggio (G E C G)
            for k, (s, f0) in enumerate(((12, hz(55)), (13, hz(52)), (14, hz(48)), (15, hz(43)))):
                drums.add(t + s * S16, tom(f0), pan=0.45 - k * 0.3, gain=0.28)
        if bm == 27:                                          # snare roll into the rebuild
            for s in range(16):
                if s < 8 and s % 2:
                    continue
                drums.add(t + s * S16, snare_tick(0.25 + 0.75 * s / 15), pan=-0.1, gain=0.22)
        if bm == 31:
            for s in (13, 14, 15):
                drums.add(t + s * S16, CLAP, pan=0.05, gain=0.14 + 0.04 * (s - 13))
        # ── bass
        if part('bass', b):
            pat = BASS_HALF if (cyc == 3 and i < 4) else (BASS_2 if i % 2 else BASS_1)
            for s, iv, d in pat:
                m = walk_into(nroot) if iv == 'W' else root + iv
                if iv == 'W' and nroot == root:
                    m = root + 12
                bass.add(t + s * S16, bass_note(m, d * S16 * 0.8), gain=0.25)
        # ── chord stabs
        if part('stabs', b):
            if cyc == 1:
                hits = [(0, 3), (10, 1)] if i % 2 == 0 else [(0, 1), (3, 1), (10, 1)]
            elif cyc == 3:
                hits = [(2, 1), (6, 1), (10, 1), (14, 1)] if i < 7 else [(2, 1), (6, 1)]
            else:
                hits = [(2, 1), (6, 1), (10, 1), (14, 1)]
            for s, d in hits:
                for k, m in enumerate(voicing):
                    stabs.add(t + s * S16, stab(m, d * S16 * 0.7, k + 4 * s),
                              pan=(-0.55, -0.2, 0.2, 0.55)[k], gain=0.085)
        # ── pad, one chord per two bars
        if part('pad', b) and i % 2 == 0:
            pad.add(t, pad_chord(voicing, 2 * BAR - 0.1), gain=0.46 if cyc == 3 else 0.34)
        # ── pluck counter-riff on the top three chord tones, up an octave
        if part('pluck', b):
            top = [m + 12 for m in voicing[1:]]
            for s, k in PLUCK:
                plk.add(t + s * S16, pluck(top[k]), pan=(-0.35 if s % 2 else 0.35),
                        gain=0.1 if (cyc == 3 and i < 4) else 0.075)
        # ── lead
        if part('lead', b) and bm in LEAD:
            for s, m, d in LEAD[bm]:
                lead.add(t + s * S16, lead_note(m, d), pan=0.0, gain=0.17)
        # ── riser into the rebuild
        if bm == 26:
            n = int(2 * BAR * SR); u = np.arange(n) / n
            z = rng('riser', bm).standard_normal(n)
            fx.add(t, swept_bp(z, 350, 2800, 1.3) * u ** 2.5, gain=0.12)

    padx = chorus(pad.x, tl.loop / 8, depth_ms=2.0, base_ms=8.0, mix=0.5, t0=tl.t0)
    stabx = chorus(stabs.x, tl.loop / 16, depth_ms=1.2, base_ms=5.0, mix=0.35, t0=tl.t0)
    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.28, 4, 3200) * 0.55
    plkx = plk.x + pingpong(plk.x, 3 * S16, 0.4, 5, 3000) * 0.6
    wet = reverb(stabx * 0.3 + padx * 0.4 + leadx * 0.3 + plkx * 0.35 + drums.x * 0.1 + fx.x * 0.5,
                 make_ir(1.8, dark=4200))
    mix = drums.x + bass.x + stabx + padx + plkx + leadx + fx.x + wet * 0.4
    return finish(tl, mix, 'passive-present-simple', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
