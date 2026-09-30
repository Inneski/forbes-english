#!/usr/bin/env python3
"""Block Camp soundtrack "Horizon" (Future Simple, both parts): dark analogue
sequencer music.

Brief, 2026-09-30: music for the Future Simple camp in the idiom of Tangerine
Dream and the Stranger Things title music - a dark, hypnotic analogue
arpeggio through a resonant low-pass, thick detuned pads, a sub bass on the
roots, a slow build, mysterious and forward-looking but not scary for
children. An original piece in that idiom, nothing copied:

  E minor, 100 BPM, 4/4. A 16-bar harmonic cycle played twice:
  Em9 (4 bars) - Cmaj7 (4) - Am9 (4) - Bsus4 (1) - B7 (3), so bar 31 is the
  dominant and the loop resolves into its own start.

  Sequencer   eighth-note ostinato on a band-limited pulse wave, a rising
              zig-zag through the chord (1 8 5 10 8 12 10 14), accents in
              3+3+2, each note through a resonant (Q 3.4) low-pass with a
              short filter envelope. The cutoff itself follows one slow
              curve across the loop (490-2450 Hz): shut at the top, opening
              through the second cycle to its widest at bar 24, closing
              again for the seam; the voice's level follows the same curve.
              Measured: median centroid 460-640 Hz in bars 0-7, about 1220
              Hz in bars 20-27.
  Counter     a second, higher arpeggio in sixteenths, grouped in threes
              against the bar, softer, with a dotted-eighth ping-pong echo.
  Pad         seven-voice detuned saw chords, slow attack, a low-pass that
              opens as each chord swells, chorus, a long dark hall.
  Sub bass    a round sine-based bass holding each root.
  Heartbeat   a distant lub-dub kick on beats 1 and 3, low-passed and
              drowned in the hall. No other drums.
  Lead        a warm two-saw lead with glide and delayed vibrato, one
              14-bar phrase over the second cycle.

  Arrangement (bar mod 32): 0-3 sequencer and a soft pad; 4 sub bass;
  8 heartbeat, pad fuller; 16 counter-arpeggio joins and the lead begins;
  24-27 the widest filter and the lead's high point; 30-31 the counter and
  heartbeat drop out and the filter closes, back to the opening.

Review, 2026-09-30: the pulse oscillator carried a DC offset (2*duty - 1),
so every sequencer and counter note began with a sub-bass thump (37% of the
counter's power sat below 60 Hz); it is zero-mean now. The heartbeat was a
bare 56 Hz sine that a laptop speaker could not play; it has a short second
partial now. The lead was 4-5 dB under the accompaniment in its own band
and is level with it. Bar 22's half-note C5 over the Cmaj7 pad's B4 is B4.
The pad's release (2.4 -> 1.6 s) and the bass's (1.0 -> 0.3 s) were long
enough to leave the old chord sounding against the new one at every change.
Measured on the m4a: E minor (Krumhansl r 0.72-0.77), median centroid about
900 Hz (the darkest Block Camp track, by design), -14.5 LUFS.

32 bars = 76.8 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/horizon.py [--wav preview.wav]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, lp, bp, adsr, perc, pingpong, make_ir,
                      reverb, chorus, finish)

NAME = 'future-simple'
BARS = 32
tl = Timeline(bpm=100, bars=BARS)
BAR, S16 = tl.bar, tl.s16
E8 = 2 * S16

# ── the changes ─────────────────────────────────────────────────────────────
#            name     root  pad voicing                arpeggio tones               counter
EM9 = dict(name='Em9', root=40, pad=[52, 55, 59, 62, 66], arp=[52, 59, 64, 67, 71, 74], ctr=[71, 74, 78],
           pcs={4, 7, 11, 2, 6})
CM7 = dict(name='Cmaj7', root=36, pad=[52, 55, 60, 64, 71], arp=[48, 55, 60, 64, 67, 71], ctr=[67, 71, 76],
           pcs={0, 4, 7, 11})
AM9 = dict(name='Am9', root=45, pad=[52, 57, 60, 64, 71], arp=[45, 52, 57, 60, 64, 71], ctr=[69, 72, 76],
           pcs={9, 0, 4, 7, 11})
BS4 = dict(name='Bsus4', root=47, pad=[54, 59, 64, 66, 69], arp=[47, 54, 59, 64, 66, 69], ctr=[71, 76, 78],
           pcs={11, 4, 6, 9})
B7 = dict(name='B7', root=47, pad=[54, 59, 63, 66, 69], arp=[47, 54, 59, 63, 66, 69], ctr=[71, 75, 78],
          pcs={11, 3, 6, 9})
CYCLE = [EM9] * 4 + [CM7] * 4 + [AM9] * 4 + [BS4] + [B7] * 3          # 16 bars


def chord_at(b):
    return CYCLE[b % 16]


def chord_starts(b):
    """(chord, length in bars) if a chord starts on bar b, else None."""
    i = b % 16
    if i == 0 or CYCLE[i] is not CYCLE[i - 1]:
        j = i
        while j < 16 and CYCLE[j] is CYCLE[i]:
            j += 1
        return CYCLE[i], j - i
    return None


def part(name, b):
    b %= BARS
    return {
        'arp':   True,
        'bass':  b >= 4,
        'heart': 8 <= b < 30,
        'ctr':   16 <= b < 30,
        'riser': b == 15,
    }[name]


def pad_level(b):
    b %= BARS
    return 0.4 if b < 8 else 0.75 if b < 16 else 1.0


# the sequencer's cutoff across the loop: a point every 4 bars, eased between
CUT = [540, 490, 680, 950, 1300, 1800, 2450, 1900]


def cutoff(pos_bars):
    u = (pos_bars % BARS) / 4
    k = int(u) % 8; fr = u - int(u)
    fr = 0.5 - 0.5 * np.cos(np.pi * fr)
    a, b = np.log(CUT[k]), np.log(CUT[(k + 1) % 8])
    return float(np.exp(a + (b - a) * fr))


def openness(pos_bars):
    """0 with the filter shut, 1 wide open: the sequencer's level follows
    it, as if the same slow control voltage drove its amplifier."""
    lo, hi = np.log(min(CUT)), np.log(max(CUT))
    return (np.log(cutoff(pos_bars)) - lo) / (hi - lo)


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
    """Zero-mean: a +-1 pulse of duty d sits at 2d-1 on average, and under a
    note envelope that offset is a sub-bass thump on every note (it was 37%
    of the counter-arpeggio's power, below 60 Hz). An analogue oscillator is
    AC-coupled, so take it out."""
    f = np.broadcast_to(np.asarray(f, float), (n,))
    p = (ph + np.cumsum(f / SR)) % 1.0
    dt = f / SR
    y = np.where(p < duty, 1.0, -1.0)
    return y + polyblep(p, dt) - polyblep((p + 1 - duty) % 1.0, dt) - (2 * duty - 1)


def env_lp(x, fc_of_t, q, chunk=64):
    """Resonant low-pass whose cutoff is any function of time since the
    note began, recomputed every `chunk` samples with the state carried."""
    n = len(x); out = np.empty(n); zi = np.zeros(2)
    for i in range(0, n, chunk):
        fc = min(fc_of_t(i / SR), SR * 0.2)
        w = 2 * np.pi * fc / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + chunk], zi = lfilter(b / a[0], a / a[0], x[i:i + chunk], zi=zi)
    return out


# ── instruments ─────────────────────────────────────────────────────────────
def seq_note(m, fc, accent):
    """The sequencer voice: pulse plus a quiet detuned saw, a resonant
    low-pass snapping down from above the cutoff."""
    gate = E8 * 0.72
    n = int((gate + 0.12) * SR)
    x = 0.75 * bl_pulse(hz(m), n, 0.36) + 0.35 * bl_saw(hz(m) * 1.004, n, 0.3)
    amt = 2.3 if accent else 1.3
    x = env_lp(x, lambda t: fc * (1 + amt * np.exp(-t / 0.065)), 3.4)
    return x * adsr(n, 0.002, 0.12, 0.62, 0.07, gate) * (1.0 if accent else 0.78)


def ctr_note(m, fc):
    n = int(0.24 * SR)
    x = bl_pulse(hz(m), n, 0.25, 0.1)
    x = lp(lp1(x, fc * 1.5), fc, 1.4)
    return x * perc(n, 0.002, 0.075)


def pad_note(m, dur, seed):
    n = int((dur + 2.6) * SR)
    r = rng('pad', m, seed)
    x = sum(bl_saw(hz(m) * 2 ** (c / 1200), n, r.random()) for c in (-14, -8, -3, 0, 3, 8, 14)) / 7
    x = env_lp(x, lambda t: 480 + 1250 * min(1.0, t / 2.2) * (1 - 0.25 * min(1.0, max(0.0, t - 2.2) / 4)),
               0.8, chunk=512)
    # release 1.6 s, was 2.4: the outgoing chord (already bright) rang on
    # against the incoming one (still dark), a semitone cluster at every
    # change - D#4/D4 across the loop seam, E4/D#4 at Bsus4-B7, B3/C4 and
    # C4/B3 at the others. D#4/D4 with both within 10 dB of each other:
    # 0.30 s before, 0.02 s now. The dip at the change is about 1 dB deeper;
    # the hall carries the legato.
    return x * adsr(n, 1.5, 1.2, 0.85, 1.6, dur)


def bass_note(m, dur):
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.32 * np.sin(4 * np.pi * f * t) + 0.1 * np.sin(6 * np.pi * f * t)
    grit = lp(bl_saw(f * 1.002, n), 320, 0.9) * 0.35
    # attack 0.2 s and release 0.3 s, were 0.35 and 1.0: two roots
    # overlapped for about half a second at each change (0.48 s within 10 dB
    # of each other), A2 against B2 - a major second at 110 Hz - into bar
    # 12. Now 0.06 s in the render, with a dip of about 2.6 dB.
    return (x + grit) * adsr(n, 0.2, 0.6, 0.88, 0.3, dur)


def heartbeat(v):
    """A 58 Hz thump with a short second partial (200 -> 116 Hz) on top. The
    first version was a bare 56 Hz sine: 99.5% of it below 120 Hz, 29 dB
    down through a laptop speaker's roll-off, so the heartbeat that marks
    bar 8 was only there on headphones. The partial makes it 11 dB more
    audible there while the full-range level (and the sub) drops 2 dB."""
    n = int(0.55 * SR); t = np.arange(n) / SR
    f = 58 + 42 * np.exp(-t / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = 0.7 * np.sin(ph) * np.exp(-t / 0.15) + 0.6 * np.sin(2 * ph) * np.exp(-t / 0.06)
    x = x * np.minimum(1, t / 0.004)
    return lp1(lp1(x, 380), 380) * v


def lead_voice(mel):
    """One continuous voice over the whole phrase: two detuned saws and a
    sine, glide between notes, a soft attack and delayed vibrato."""
    total = sum(d for _, d in mel)
    n = int((total * S16 + 2.0) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n)
    pos = 0
    first = next(m for m, _ in mel if m)
    last = hz(first)
    for m, d in mel:
        a, b = int(pos * S16 * SR), int((pos + d) * S16 * SR)
        if m:
            f[a:b] = hz(m); last = hz(m)
            tt = np.arange(b - a) / SR
            g[a:b] = np.minimum(1, tt / 0.07) * (0.85 + 0.15 * np.exp(-tt / 0.3))
            g[max(b - int(0.03 * SR), a):b] *= 0.8
            vib[a:b] = np.clip((tt - 0.4) / 0.7, 0, 1)
        else:
            f[a:b] = last
        pos += d
    f[int(pos * S16 * SR):] = last
    g[int(pos * S16 * SR):] = 0
    g = lp1(g, 18)
    k = np.exp(-1 / (0.06 * SR))
    fl = lfilter([1 - k], [1, -k], f); fl[:int(0.01 * SR)] = f[0]
    t = np.arange(n) / SR
    fl = fl * 2 ** (0.16 / 12 * vib * np.sin(2 * np.pi * 4.9 * t))
    x = 0.5 * bl_saw(fl, n) + 0.5 * bl_saw(fl * 2 ** (7 / 1200), n, 0.4)
    x = lp1(lp1(x, 1900), 2300)
    x += 0.5 * np.sin(2 * np.pi * np.cumsum(fl) / SR)
    return x * g


# the lead: (midi, sixteenths), 0 = rest; bars 16-30, one bar = 16
LEAD = [(0, 8), (71, 8),                          # 16 Em9
        (76, 12), (74, 4),                        # 17
        (71, 16),                                 # 18
        (67, 6), (69, 2), (71, 8),                # 19
        (76, 12), (74, 2), (72, 2),               # 20 Cmaj7
        (71, 16),                                 # 21
        (67, 8), (71, 8),                         # 22 (B4, not C5: see below)
        (76, 8), (79, 8),                         # 23
        (79, 12), (76, 4),                        # 24 Am9
        (72, 8), (71, 8),                         # 25
        (69, 8), (72, 4), (76, 4),                # 26
        (79, 8), (76, 8),                         # 27
        (76, 16),                                 # 28 Bsus4
        (75, 16),                                 # 29 B7
        (71, 16)]                                 # 30
LEAD_BAR = 16
assert sum(d for _, d in LEAD) == 15 * 16
# Bar 22 was G4 C5: C is a chord tone, but a half-note C5 sits a semitone
# above the Cmaj7 pad's B4 (and the counter's B4) and rises away without
# resolving. G4 B4 E5 G5 climbs the chord's upper triad instead. The two C5s
# over the Am9 pad's B4 stay: bar 25's resolves onto B4, bar 26's is a
# passing quarter in an A-C-E arpeggio.


def check_melody():
    """Every note of a quarter or longer, and every note on a strong beat,
    must be a chord tone; short passing notes are allowed."""
    pos, bad = 0, []
    for m, d in LEAD:
        if m:
            bar = LEAD_BAR + pos // 16
            ch = chord_at(bar)
            strong = pos % 8 == 0
            if (d >= 4 or strong) and m % 12 not in ch['pcs']:
                bad.append((bar, pos % 16, m, ch['name']))
        pos += d
    print('melody vs chords:', 'all long/strong notes are chord tones' if not bad else bad)


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    check_melody()
    seq, ctr, pad, bass, heart, lead, fx = (tl.bus() for _ in range(7))
    ORDER = [0, 2, 1, 3, 2, 4, 3, 5]
    CPAT = [0, 2, 1] * 5 + [2]
    for b in tl.bars_range():
        t = b * BAR
        lb = b % BARS
        ch = chord_at(b)
        # sequencer: eighths, accents 3+3+2
        for s, k in enumerate(ORDER):
            fc = cutoff(lb + s / 8)
            seq.add(t + s * E8, seq_note(ch['arp'][k], fc, s in (0, 3, 6)),
                    gain=0.14 * (0.62 + 0.38 * openness(lb + s / 8)))
        # counter-arpeggio: sixteenths in threes, a gentle swell in
        if part('ctr', b):
            lvl = min(1.0, 0.45 + 0.14 * (lb - 16))
            fc2 = 1500 + 700 * np.sin(2 * np.pi * lb / 8)
            for s, k in enumerate(CPAT):
                ctr.add(t + s * S16, ctr_note(ch['ctr'][k], fc2), pan=(-0.45 if s % 2 else 0.45),
                        gain=lvl * (0.07 if s % 3 == 0 else 0.05))
        # pad and bass on each change
        st = chord_starts(b)
        if st:
            c, length = st
            dur = length * BAR
            for k, m in enumerate(c['pad']):
                pad.add(t, pad_note(m, dur, k), pan=(-0.6, -0.3, 0.0, 0.3, 0.6)[k],
                        gain=0.055 * pad_level(b))
        if b % 4 == 0 and part('bass', b):
            bass.add(t, bass_note(ch['root'], 4 * BAR - 0.05), gain=0.075)
        # distant heartbeat: lub-dub on 1 and 3
        if part('heart', b):
            for s, v in ((0, 1.0), (2, 0.55), (8, 1.0), (10, 0.55)):
                heart.add(t + s * S16, heartbeat(v), gain=0.3)
        # a soft rising wind into the second cycle
        if part('riser', b):
            n = int(BAR * SR); u = np.arange(n) / n
            z = rng('riser', lb).standard_normal(n)
            y = np.zeros(n)
            for c in range(12):
                a0, a1 = c * n // 12, (c + 1) * n // 12
                y[a0:a1] = bp(z[a0:a1], 250 * (8 ** (c / 11)), 1.5)
            fx.add(t, lp1(y, 3000) * u ** 2, gain=0.09)
    for lap in (-1, 0, 1):
        t0 = lap * tl.loop + LEAD_BAR * BAR
        if -tl.pre * BAR - 16 * BAR < t0 < (tl.bars + tl.post) * BAR:
            # 0.11 left it 4-5 dB under the sequencer, counter and pad in its
            # own band (300-2000 Hz); 0.155 puts it level with them.
            lead.add(t0, lead_voice(LEAD), pan=0.05, gain=0.155)

    seqx = seq.x + pingpong(seq.x, 3 * S16, 0.32, 5, 2400) * 0.55
    ctrx = ctr.x + pingpong(ctr.x, 3 * S16, 0.45, 6, 2800)
    padx = chorus(pad.x, tl.loop / 8, depth_ms=3.0, base_ms=8.0, mix=0.5, t0=tl.t0)
    leadx = lead.x + pingpong(lead.x, 6 * S16, 0.28, 4, 2200) * 0.5
    ir = make_ir(3.8, dark=3200, seed=21, pre=0.02)
    wet = reverb(seqx * 0.22 + ctrx * 0.4 + padx * 0.35 + heart.x * 0.7 + leadx * 0.45 + fx.x * 0.6, ir)
    mix = seqx + ctrx + padx + bass.x + heart.x * 0.35 + leadx + fx.x + wet * 0.5
    return finish(tl, mix, NAME, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
