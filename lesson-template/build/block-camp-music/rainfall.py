#!/usr/bin/env python3
"""Block Camp soundtrack "Rainfall" (Past Continuous): a nocturnal CS-80 piece.

Brief, 2026-09-30, for the Past Continuous camp ("it was raining when..."):
Vangelis, Blade Runner - slow, huge detuned brassy CS-80-style pads that
swell in with a slow filter opening and a hint of pitch bend and aftertouch
vibrato, a deep bass drone and slow bass movement, a sparse bell-like glassy
lead, long reverb, and rain: filtered noise with drops and, now and then, a
soft distant thunder roll. No drums. An original piece in that idiom; nothing
is taken from the film's score.

E minor, 68.6 BPM (a beat is exactly 42000 samples, a bar 3.5 s), one chord
every two bars:

    A  Em9      Cmaj7/E   Am9/E     B7sus4/E        bars 0-7    drone on E, pads swelling in, rain, a bell motif in 4-7
    B  Cmaj7    Am9       Fmaj7#11  B7sus4 | B7     bars 8-15   the bass moves, pads full, the glass lead's first phrase
    C  Em9      Gmaj7/D   Cmaj9#11  B7sus4 | B7     bars 16-23  the lead's second phrase, higher; the pads at their widest

The pads are two polyBLEP saws a voice, detuned 7 cents either side, and a
pulse, through a resonant low-pass that opens over about a second; each note
bends up into pitch and grows a delayed vibrato. Where the lead holds a note
the pad leaves out whatever would sit a semitone under it (check_rub). The
bass is a filtered detuned-saw drone with a sine locked to its main saw, so
it breathes by about 3.5 dB rather than throbbing. The lead is a two-operator
FM voice whose index jumps at each attack (the bell) and relaxes to a glassy
sustain, gliding between notes, with a dotted-eighth echo. Rain is
overlapping sine-windowed noise grains, band-limited, with a patter of single
drops under the hiss and sparse chirped drops over it; thunder is low-passed
noise in a few slow bumps, in bars 3 and 13, with enough 200-600 Hz rumble to
survive a laptop speaker. 24 bars = 84 s, a seamless loop (see synthkit.py).

Reviewed 2026-09-30: voicings changed where the lead rubbed a semitone
against the pad (Am9/E, Am9, Fmaj7#11, Cmaj7#11 -> Cmaj9#11) and where a
voicing had B3 under C4 (Cmaj7); pad release 2.6 -> 1.8 s and bass release
2.0 -> 1.2 s, so semitone and tritone chord changes do not smear; the drone's
sine phase-locked; the rain patter added; the thunder's upper rumble raised.

    py lesson-template/build/block-camp-music/rainfall.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, pingpong,
                      make_ir, reverb, chorus, finish)

BEAT = 0.875                     # 42000 samples, 68.57 BPM
BAR = 4 * BEAT                   # 3.5 s
S16 = BEAT / 4
BARS = 24
tl = Timeline(bpm=60 / BEAT, bars=BARS, pre=6, post=1)
LOOP = BARS * BAR                # 84 s
assert abs(tl.bar - BAR) < 1e-9
CHUNK = 240                      # divides the loop and the pre-roll

PC = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'Bb': 10, 'B': 11}

#            bass  pad voicing              chord tones (the lead may use any)
# Where the lead holds C5 (Am9, Fmaj7#11) the pad leaves the B out and the
# lead supplies the 9th / #11 itself: a pad B4 under a held C5 is a semitone
# rub for three beats. Cmaj9#11 likewise leaves the F# to the lead, which
# holds G5 over it (an F#4 in the pad, doubled to F#5 in C, rubbed at a
# semitone and a minor ninth). No voicing has a semitone in it either; the
# old Cmaj7 and Cmaj7#11 had B3 against C4. check_rub() below keeps it so.
CH = {
    'Em9':      (40, (52, 55, 59, 62, 66), 'E G B D F#'),
    'Cmaj7/E':  (40, (52, 55, 60, 64, 71), 'C E G B'),
    'Am9/E':    (40, (52, 57, 60, 64, 67), 'A C E G B'),
    'B7sus4/E': (40, (52, 57, 59, 64, 66), 'B E F# A'),
    'Cmaj7':    (36, (55, 60, 64, 67, 71), 'C E G B'),
    'Am9':      (33, (52, 57, 60, 64, 67), 'A C E G B'),
    'Fmaj7#11': (41, (53, 57, 60, 64, 67), 'F A C E G B'),
    'B7sus4':   (35, (52, 57, 59, 64, 66), 'B E F# A'),
    'B7':       (35, (51, 57, 59, 63, 66), 'B D# F# A'),
    'Gmaj7/D':  (38, (55, 59, 62, 66, 71), 'G B D F#'),
    'Cmaj9#11': (36, (52, 59, 62, 67, 71), 'C E G B D F#'),
}
PROG = ['Em9', 'Em9', 'Cmaj7/E', 'Cmaj7/E', 'Am9/E', 'Am9/E', 'B7sus4/E', 'B7sus4/E',
        'Cmaj7', 'Cmaj7', 'Am9', 'Am9', 'Fmaj7#11', 'Fmaj7#11', 'B7sus4', 'B7',
        'Em9', 'Em9', 'Gmaj7/D', 'Gmaj7/D', 'Cmaj9#11', 'Cmaj9#11', 'B7sus4', 'B7']


def chord_at(b):
    return PROG[b % BARS]


def tones(name):
    return {PC[s] for s in CH[name][2].split()}


PAD_LEVEL = (0.7, 1.0, 1.1)       # by section, A B C
PAD_CUT = (1100, 1700, 2200)      # how far the filters open

# ── the lead: (midi, sixteenths), 0 = rest; 128 = 8 bars ────────────────────
MOTIF = [(76, 8), (71, 8), (0, 4), (72, 12),              # Am9/E
         (69, 8), (71, 8), (76, 16)]                      # B7sus4/E        (bars 4-7, 64)
PHRASE_B = [(0, 4), (71, 8), (67, 4), (76, 12), (74, 4),  # Cmaj7
            (72, 8), (71, 4), (69, 4), (76, 16),          # Am9
            (71, 8), (72, 4), (76, 4), (72, 12), (69, 4),  # Fmaj7#11
            (71, 8), (69, 4), (66, 4), (75, 12), (0, 4)]  # B7sus4 | B7
PHRASE_C = [(76, 8), (78, 4), (79, 4), (78, 12), (76, 4),  # Em9
            (74, 8), (71, 8), (78, 12), (76, 4),          # Gmaj7/D
            (76, 8), (78, 4), (79, 4), (79, 8), (76, 8),  # Cmaj9#11
            (78, 8), (76, 8), (75, 16)]                   # B7sus4 | B7
LINES = (('motif', MOTIF, 4, 64), ('phrase B', PHRASE_B, 8, 128), ('phrase C', PHRASE_C, 16, 128))


def check_line(name, mel, bar0, total):
    """A note that starts on beat 1 or 3, or lasts a dotted quarter or more,
    or sounds across a barline, must be a tone of the chord there."""
    pos = 0
    for m, d in mel:
        if m:
            for q in range(pos, pos + d):
                if q == pos and (q % 8 == 0 or d >= 6) or (q > pos and q % 16 == 0):
                    ch = chord_at(bar0 + q // 16)
                    assert m % 12 in tones(ch), f'{name}: {m} at bar {bar0 + q // 16} 16th {q % 16} over {ch}'
        pos += d
    assert pos == total, (name, pos)


def pad_voices(b):
    """What the pads sound in bar b: the voicing, plus the octave-up top voice in C."""
    voic = list(CH[chord_at(b)][1])
    return voic + [voic[-1] + 12] if (b % BARS) // 8 == 2 else voic


def check_rub(name, mel, bar0):
    """Being a chord tone is not enough: a lead note on beat 1 or 3, or a half
    note or longer, must not sit a semitone or minor ninth against a pad voice
    (a major seventh above one is the chord's own colour and is allowed)."""
    pos = 0
    for m, d in mel:
        if m and (pos % 8 == 0 or d >= 8):
            for v in pad_voices(bar0 + pos // 16):
                assert m - v not in (1, 13, 25) and v - m not in (1, 13), \
                    f'{name}: lead {m} against pad {v} at bar {bar0 + pos // 16} 16th {pos % 16}'
        pos += d


for _n, _m, _b, _t in LINES:
    check_line(_n, _m, _b, _t)
    check_rub(_n, _m, _b)


def part(name, b):
    b %= BARS; sec, i = b // 8, b % 8
    return {
        'thunder': b in (3, 13),
    }[name]


# ── oscillators and filters ─────────────────────────────────────────────────
def blep_saw(f, n, ph0=0.0):
    """A saw with polyBLEP corners, so the high voices do not alias."""
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


def tv_lp(x, fc, q=0.707):
    """Low-pass with cutoff fc[j] for the chunk starting at sample j*CHUNK."""
    out = np.empty_like(x); zi = np.zeros(2)
    for j, i in enumerate(range(0, len(x), CHUNK)):
        w = 2 * np.pi * min(fc[j], SR * 0.45) / SR
        al = np.sin(w) / (2 * q); c = np.cos(w)
        b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); a = np.array([1 + al, -2 * c, 1 - al])
        out[i:i + CHUNK], zi = lfilter(b / a[0], a / a[0], x[i:i + CHUNK], zi=zi)
    return out


# ── instruments ─────────────────────────────────────────────────────────────
def cs80(m, dur, cut, key):
    """A CS-80-style brass pad voice: it bends up into the note, the filter
    opens over about a second, and vibrato grows in as if pressed harder."""
    n = int((dur + 2.8) * SR); t = np.arange(n) / SR
    r = rng('cs80', key)
    cents = -22 * np.exp(-t / 0.4) + 8 * np.clip((t - 1.8) / 1.6, 0, 1) * np.sin(2 * np.pi * 5.2 * t + r.uniform(0, 6.3))
    f = hz(m) * 2 ** (cents / 1200)
    x = (0.5 * blep_saw(f * 2 ** (-7 / 1200), n, r.random()) + 0.5 * blep_saw(f * 2 ** (7 / 1200), n, r.random())
         + 0.3 * blep_pulse(f * 2 ** (-1 / 1200), n, 0.42, r.random()))
    tc = t[::CHUNK]
    # the release darkens as it fades; 1.8 s rather than 2.6, because where
    # the chords move by a semitone (sus4 to 3 in bar 15, B7 to Em9 across the
    # seam, F to B7sus4) the old voice sat under the new one for two seconds.
    # The 5.2 s reverb still carries the long tail.
    opening = np.where(tc < dur, 1 - np.exp(-tc / 1.1), (1 - np.exp(-dur / 1.1)) * np.exp(-(tc - dur) / 0.7))
    x = tv_lp(x, 260 + (cut - 260) * opening, 1.4)
    return x * adsr(n, 0.8, 1.2, 0.8, 1.8, dur)


def drone(m, dur, key):
    """Two saws 4 cents apart and a sine. The sine is locked to the louder
    saw's phase (a saw's fundamental is -sin, hence the sign), so the two
    always add; only the quieter saw drifts against them, a swell of about
    3.5 dB. With a free-running sine between the saws the fundamental
    cancelled every few seconds and the drone throbbed by 9-10 dB."""
    n = int((dur + 1.4) * SR)
    r = rng('drone', key)
    f1, f2 = hz(m) * 2 ** (-2 / 1200), hz(m) * 2 ** (2 / 1200)
    p1, p2 = r.random(), r.random()
    ph1 = 2 * np.pi * ((p1 + np.cumsum(np.full(n, f1 / SR))) % 1.0)
    x = 0.75 * blep_saw(f1, n, p1) + 0.25 * blep_saw(f2, n, p2) - 0.21 * np.sin(ph1)
    x = lp(lp(x, 260, 1.0), 320) * 1.4
    return x * adsr(n, 1.4, 0.5, 0.9, 1.2, dur)       # a short release: no tritone mush from F to B


def glass_phrase(mel):
    """One voice gliding through a phrase: the FM index jumps at each
    attack (a bell) and relaxes to a glassy sustain; delayed vibrato."""
    total = sum(d for _, d in mel) * S16
    n = int((total + 2.5) * SR)
    f = np.zeros(n); g = np.zeros(n); vib = np.zeros(n); ons = np.zeros(n)
    last = hz(next(m for m, _ in mel if m)); pos = 0; b = 0; lv = 0.0
    for m, d in mel:
        a, b = int(round(pos * S16 * SR)), int(round((pos + d) * S16 * SR))
        tt = np.arange(b - a) / SR
        if m:
            f[a:b] = hz(m); last = hz(m)
            g[a:b] = np.minimum(1, tt / 0.012) * (0.62 + 0.38 * np.exp(-tt / 0.5))
            g[max(a, b - int(0.04 * SR)):b] *= 0.5
            vib[a:b] = np.clip((tt - 0.5) / 1.0, 0, 1)
            ons[a:b] = np.exp(-tt / 0.35)
        else:                                            # a rest: the last note rings away
            f[a:b] = last; g[a:b] = lv * np.exp(-tt / 0.5)
        lv = g[b - 1]
        pos += d
    f[b:] = last
    g[b:] = lv * np.exp(-np.arange(n - b) / SR / 0.6)   # and after the phrase
    g = lp1(g, 40)
    a1 = np.exp(-1 / (0.045 * SR))
    fl = lfilter([1 - a1], [1, -a1], f - f[0]) + f[0]
    t = np.arange(n) / SR
    fl = fl * 2 ** (12 * vib * np.sin(2 * np.pi * 5.0 * t) / 1200)
    ph = 2 * np.pi * np.cumsum(fl) / SR
    idx = 0.7 + 2.2 * ons
    x = np.sin(ph + idx * np.sin(ph)) * 0.8 + 0.25 * np.sin(2 * ph)
    x += 0.18 * np.sin(3.5 * ph) * ons ** 2                  # the bell's inharmonic glint
    return lp1(x, 5000) * g


PATTER = 4.2                      # puts the patter 9 dB under the hiss (measured)


def rain_grain(key):
    """Two bars of rain under a sine window; laid a bar apart, the power sums flat.
    A steady hiss with a little sparkle, and under it a patter: about 120
    single drops a second in each ear, of random, heavy-tailed strength,
    each a short tick band-limited to 1.2-4 kHz. The hiss alone read as air
    or surf; the patter (9 dB under it) roughly doubles the texture's crest
    and adds nothing above 6 kHz."""
    n = int(2 * BAR * SR)
    r = rng('rain', key)
    z = r.standard_normal((n, 2))
    y = hp(lp(lp1(z, 5000), 2300, 0.7), 400) + 0.12 * lp(lp(hp(z, 2800), 6000), 6500)   # a little sparkle
    k = int(120 * 2 * BAR) * 2
    imp = np.zeros((n, 2))
    np.add.at(imp, (r.integers(0, n, k), r.integers(0, 2, k)), r.exponential(1.0, k) * r.choice((-1.0, 1.0), k))
    pat = hp(hp(imp, 1200, 0.8), 1200, 0.8)
    pat = lp(lp(lp1(pat, 6000), 4000, 0.8), 4000, 0.8)
    y = y + PATTER * pat
    return y * np.sin(np.pi * (np.arange(n) + 0.5) / n)[:, None]


def drop(f0, seed):
    n = int(0.05 * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.5 * np.exp(-t / 0.004))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.007) * np.minimum(1, t / 0.0008)


def thunder(key, dur=8.0):
    n = int(dur * SR); t = np.arange(n) / SR
    r = rng('thunder', key)
    env = np.zeros(n)
    for c, w, a in ((0.25, 0.5, 0.5), (0.9, 0.8, 1.0), (1.9, 1.2, 0.8), (3.2, 1.6, 0.5), (4.8, 2.0, 0.3)):
        c += r.uniform(-0.15, 0.15)
        env += a * np.exp(-0.5 * ((t - c) / w) ** 2)
    env *= np.clip(t / 0.3, 0, 1) * np.clip((dur - t) / 1.5, 0, 1)
    out = np.zeros((n, 2))
    for ch in range(2):
        z = r.standard_normal(n)
        # the upper rumble (200-600 Hz) is what a laptop or phone can play;
        # below 190 Hz alone the roll vanished on small speakers
        y = lp(lp(z, 150, 0.8), 190) + 0.4 * lp(bp(z, 280, 0.7), 650)
        out[:, ch] = hp(y, 38) * env
    return out


# ── render ──────────────────────────────────────────────────────────────────
def render(wav=None):
    pads, bass, lead, rain, drops, thund = (tl.bus() for _ in range(6))
    bass_segs = []
    for b in tl.bars_range():
        t = b * BAR; bb = b % BARS; sec = bb // 8
        name = chord_at(b)
        # pads: a new chord every two bars, or where the sus resolves
        new = b % 2 == 0 or chord_at(b - 1) != name
        if new:
            span = 2 if chord_at(b + 1) == name else 1
            voic = CH[name][1]
            lvl = PAD_LEVEL[sec] * (0.85 if bb >= 22 else 1.0)
            for k, m in enumerate(voic):
                pads.add(t, cs80(m, span * BAR - 0.1, PAD_CUT[sec] * (1 + 0.12 * k), (bb, k)),
                         pan=(-0.7, -0.35, 0.0, 0.35, 0.7)[k], gain=0.10 * lvl)
            # the top voice doubled an octave up, softly, in C
            if sec == 2:
                pads.add(t, cs80(voic[-1] + 12, span * BAR - 0.1, PAD_CUT[sec] * 1.2, (bb, 9)),
                         pan=0.2, gain=0.04)
        bass_segs.append((t, CH[name][0]))
        # rain: a grain every bar, and a scatter of drops
        rain.add(t, rain_grain(bb), gain=0.06)
        r = rng('drops', bb)
        for _ in range(14):
            dt_ = float(r.uniform(0, BAR)); f0 = float(r.choice([900, 1400, 2100, 2800, 3400])) * float(r.uniform(0.9, 1.1))
            # 0.008-0.028: at half this each plip peaked about 8 dB under the
            # hiss in its own band, so the drops were masked
            drops.add(t + dt_, drop(f0, 0), pan=float(r.uniform(-0.8, 0.8)), gain=float(r.uniform(0.008, 0.028)))
        if part('thunder', b):
            # 0.55: at 0.2 the roll raised its own bars by 0.1-0.3 dB in every
            # band, i.e. it sat 12-16 dB under the drone and pads and was not there
            thund.add(t + 0.4 * BAR, thunder(bb), gain=0.55)

    # the bass holds while its note stays, so the A section is one long drone on E
    notes = []
    for t, m in bass_segs:
        if notes and notes[-1][2] == m:
            notes[-1][1] = t + BAR - notes[-1][0]
        else:
            notes.append([t, BAR, m])
    for t, d, m in notes:
        # 0.08: with the sine locked the drone no longer cancels itself, and
        # sits about 2 dB hotter on average than the free-running version
        bass.add(t, drone(m, d - 0.2, (round(t / BAR) % BARS, m)), gain=0.08)

    for lap in (-1, 0, 1):
        for bar0, line in ((4, MOTIF), (8, PHRASE_B), (16, PHRASE_C)):
            t0 = lap * LOOP + bar0 * BAR
            if t0 > (BARS + tl.post) * BAR or t0 + 11 * BAR < -tl.pre * BAR:
                continue
            lead.add(t0, glass_phrase(line), pan=0.1, gain=0.10 if line is MOTIF else 0.12)

    padx = chorus(pads.x, LOOP / 12, depth_ms=3.0, base_ms=9.0, mix=0.5, t0=tl.t0)
    leadx = lead.x + pingpong(lead.x, 3 * S16, 0.42, 6, 2600) * 0.7
    rainx = rain.x + drops.x
    wet = reverb(padx * 0.4 + leadx * 0.55 + bass.x * 0.1 + drops.x * 0.6 + rain.x * 0.15 + thund.x * 0.3,
                 make_ir(5.2, dark=3800, seed=23, pre=0.035))
    stems = dict(pads=padx, bass=bass.x, lead=leadx, rain=rainx, thunder=thund.x, reverb=wet * 0.55)
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        i0 = tl.smp(0)
        for k, v in stems.items():
            row = []
            for s in range(0, BARS, 2):
                seg = v[i0 + int(s * BAR * SR):i0 + int((s + 2) * BAR * SR)]
                row.append(20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9))
            seg = v[i0:i0 + int(LOOP * SR)].mean(1)
            sp = np.abs(np.fft.rfft(seg)) ** 2; fq = np.fft.rfftfreq(len(seg), 1 / SR)
            hi = 10 * np.log10(sp[fq > 3000].sum() / (sp.sum() + 1e-12) + 1e-12)
            print(f'{k:8s}' + ' '.join(f'{r:6.0f}' for r in row) + f'   >3k {hi:5.1f} dB')
    return finish(tl, mix, 'past-continuous', wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
