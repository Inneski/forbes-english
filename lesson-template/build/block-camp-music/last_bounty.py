#!/usr/bin/env python3
"""Block Camp soundtrack "Last Bounty" (The Last Bounty RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is a revenge
western: a bounty hunter pushes open the saloon doors, finds the man who shot
his brother, and the story ends at sunset with a bank on fire and a duel in an
empty street. So: the idiom of an Italian western's standoff music - a lone
whistler carrying the tune over a fingerpicked nylon guitar and a trotting
horse, a male choir humming under it, a mariachi trumpet for the lament, a
twangy baritone guitar for the standoff, a church bell, anvils, a whip, and a
timpani heartbeat as the street goes quiet. An original piece in that idiom:
no melody or progression is taken from any film.

G minor, 75 BPM, 4/4 (a sixteenth is exactly 9600 samples, a bar 3.2 s).
One chord a bar:

  intro     Gm | Gm | Eb | D                 bars 0-3    wind, a bell, the whistler's call
  A         Gm | F  | Eb | D                 bars 4-11   the tune, whistled; nylon guitar,
            Gm | Bb | Cm | D7                            choir "oo", trotting hooves, bass
  B         Bb | F  | Gm | D                 bars 12-19  the trumpet's lament over strummed
            Eb | Bb | Cm | D7                            guitar; timpani, whip, choir "ah";
                                                         twang an octave under it, anvils
  standoff  Gm | Ab | Gm | D                 bars 20-23  the twang alone, the Phrygian Ab,
                                                         a bell, the heartbeat, a roll on D

The hook (whistle, bar 4): D5 G5 D6 ~ C6 Bb5 | A5 ~ G5 F5 C5 | Eb5 G5 Bb5 ~ G5
| F#5 ~ A5 F#5 D5. The trumpet answers in Bb: F5 D5 Bb4 | C5 F5 A5 | G5 F5 D5 |
F#5 ~ E5 D5.

check() proves the harmony at import. Every note the score holds is an event
with the span it really sounds for (a plucked string to its damping, a bell to
its fade), and: every lead note on beat 1 or 3, or a beat long, is a tone of
every chord it sounds over; every bass, guitar, choir, timpani, anvil and bell
note is; no two notes sounding together sit 1, 11 or 13 semitones apart, and
no two long ones a semitone apart in any octave. Guitar strings are damped
when the chord changes under them (unless the note belongs to the new chord);
the bell, whose partials are G, Bb and D, fades out before the D and the Ab.

Instruments, all synthesised here:
  Whistle   one continuous voice per phrase: a near-sine with a 6 ms glide
            between notes, a scoop up into each phrase, slow vibrato on held
            notes, breath (noise ring-modulated onto the tone, and air);
            a dotted-eighth echo.
  Nylon     Karplus-Strong strings (fractional all-pass tuning, a soft
            ramp pick, a comb for the plucking point) through a small body;
            eighth-note arpeggios in A, rasgueado strums in B.
  Twang     a baritone electric: a bright pick near the bridge, a touch of
            drive, an upper-mid lift, a cabinet, a slapback echo (no
            tremolo, no spring).
  Trumpet   band-limited harmonics brightening as it swells, a formant near
            1.3 kHz, a fast wide mariachi vibrato, a scoop and a breath burst.
  Choir     three singers a note, additive harmonics shaped by vowel
            formants ("mm", "oo", "ah"), common tones held across chords.
  Bass      a picked string, root and fifth, a gallop in B.
  Percussion coconut hooves (unpitched), a whip, anvils tuned to the chord,
            a church bell on G (hum G2, prime G3, tierce Bb3, quint D4),
            timpani on the root, desert wind; maracas in B, a rattlesnake
            (a ~50 Hz buzz of clicks) in the intro and the Ab bar, a cymbal
            swelling into B and into the top of the loop.
24 bars = 76.8 s, a seamless loop (see synthkit.py).

Review, 2026-10-05 (measured on the render; --stems prints the table):
- Key: Krumhansl (32768 points, 65-2000 Hz) G minor r 0.884, D minor 0.691.
- Brightness. The first render was dull: 6-8 kHz -38.8, 8 kHz+ -36.2 dB of
  the total (present-simple.m4a -25.7 / -24.9). The pick noise, whistle
  air, trumpet band-limit, guitar cabinet and hall were opened up, and the
  maracas, rattlesnake and cymbal added; the noise sources were then tilted
  toward 7 kHz, because white noise put its energy above 8 kHz and left 6-8
  short. Now 6-8 kHz -26.9, 8 kHz+ -24.4.
- Balance (A-weighted, re the mix): the whistle sat at -0.5 dB over the
  guitar's -12.7 in A; it is down 3 dB (the guitar now -10.1, the bass -12.2,
  the hooves -21.5, the choir -18.2). B: trumpet -3.4, strums -7.7, twang
  -8.0, timpani -19.4, maracas -18.4. Standoff: twang -2.1, bell -12.8,
  heartbeat -12.0, choir -13.9, wind -19.1. Every part audible where it plays.
- The bell and the timpani released 0.35 s and 0.1 s past the chord change
  (a decaying G under the Ab); their fades now end at the change, as check()
  assumes. The pluck's noise was not periodic over the string's length, a
  step at each pass; it is windowed now.
- Clicks: the mix's twelve largest HF jumps (one per 50 ms) are all on the
  sixteenth grid within 1 ms - hooves, maracas, the whip - at most 4.0x the
  99.9th percentile. Peak 0.86, rms -16.9 dBFS, seam 0.0000.

    py lesson-template/build/block-camp-music/last_bounty.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import (SR, Timeline, hz, rng, lp1, hp1, lp, hp, bp, adsr, pingpong, make_ir, reverb, finish)

NAME = 'last-bounty'
BARS = 24
tl = Timeline(bpm=75, bars=BARS)
BAR, BEAT, LOOP = tl.bar, tl.beat, tl.loop
S16 = BEAT / 4
assert abs(S16 * SR - 9600) < 1e-6

# ── the changes ─────────────────────────────────────────────────────────────
#        pitch classes  bass root/fifth  guitar (low to high)      choir
CH = {
    'Gm': dict(pcs={7, 10, 2}, root=43, fifth=50, gtr=[43, 50, 55, 58, 62], choir=[55, 58, 62]),
    'F':  dict(pcs={5, 9, 0}, root=41, fifth=48, gtr=[41, 48, 53, 57, 60], choir=[53, 57, 60]),
    'Eb': dict(pcs={3, 7, 10}, root=39, fifth=46, gtr=[46, 51, 55, 58, 63], choir=[55, 58, 63]),
    'D':  dict(pcs={2, 6, 9}, root=38, fifth=45, gtr=[45, 50, 57, 62, 66], choir=[54, 57, 62]),
    'D7': dict(pcs={2, 6, 9, 0}, root=38, fifth=45, gtr=[45, 50, 57, 60, 66], choir=[54, 57, 60]),
    'Bb': dict(pcs={10, 2, 5}, root=46, fifth=41, gtr=[46, 53, 58, 62, 65], choir=[53, 58, 62]),
    'Cm': dict(pcs={0, 3, 7}, root=36, fifth=43, gtr=[48, 55, 60, 63, 67], choir=[55, 60, 63]),
    'Ab': dict(pcs={8, 0, 3}, root=44, fifth=39, gtr=[44, 51, 56, 60, 63], choir=[56, 60, 63]),
}
CHORDS = (['Gm', 'Gm', 'Eb', 'D'] +
          ['Gm', 'F', 'Eb', 'D', 'Gm', 'Bb', 'Cm', 'D7'] +
          ['Bb', 'F', 'Gm', 'D', 'Eb', 'Bb', 'Cm', 'D7'] +
          ['Gm', 'Ab', 'Gm', 'D'])
assert len(CHORDS) == BARS


def section(lb):
    lb %= BARS
    return 'intro' if lb < 4 else 'A' if lb < 12 else 'B' if lb < 20 else 'standoff'


def chord_at(t):
    return CHORDS[int(np.floor(t / BAR + 1e-9)) % BARS]


# ── the tunes: (midi, sixteenths) per bar, 0 = rest ─────────────────────────
WHISTLE = {
    0: [(0, 8), (74, 2), (79, 6)],                              # Gm  .. D G~
    1: [(82, 4), (79, 12)],                                     # Gm  Bb G~
    2: [(0, 4), (75, 2), (79, 2), (82, 8)],                     # Eb  .. Eb G Bb~
    3: [(81, 12), (0, 4)],                                      # D   A~
    4: [(74, 2), (79, 2), (86, 10), (84, 1), (82, 1)],          # Gm  D G D~ C Bb
    5: [(81, 10), (79, 2), (77, 2), (72, 2)],                   # F   A~ G F C
    6: [(75, 2), (79, 2), (82, 10), (79, 2)],                   # Eb  Eb G Bb~ G
    7: [(78, 8), (81, 2), (78, 2), (74, 4)],                    # D   F#~ A F# D
    8: [(74, 2), (79, 2), (82, 4), (86, 8)],                    # Gm  D G Bb D~
    9: [(86, 6), (84, 2), (82, 4), (77, 4)],                    # Bb  D C Bb F
    10: [(84, 6), (82, 2), (79, 4), (75, 4)],                   # Cm  C Bb G Eb
    11: [(78, 6), (81, 2), (84, 8)],                            # D7  F# A C~
}
TRUMPET = {
    12: [(77, 6), (74, 2), (70, 8)],                            # Bb  F D Bb
    13: [(72, 4), (77, 4), (81, 8)],                            # F   C F A
    14: [(79, 6), (77, 2), (74, 8)],                            # Gm  G F D
    15: [(78, 12), (76, 2), (74, 2)],                           # D   F#~ E D
    16: [(79, 6), (82, 2), (79, 4), (75, 4)],                   # Eb  G Bb G Eb
    17: [(77, 8), (74, 4), (70, 4)],                            # Bb  F D Bb
    18: [(72, 4), (75, 4), (79, 4), (77, 2), (75, 2)],          # Cm  C Eb G F Eb
    19: [(74, 12), (0, 4)],                                     # D7  D~
}
# the twang: an octave under the trumpet for bars 16-19, then the standoff
TWANG = {lb: [(m - 12 if m else 0, d) for m, d in TRUMPET[lb]] for lb in (16, 17, 18, 19)}
TWANG.update({
    20: [(43, 4), (50, 4), (55, 8)],                            # Gm  G2 D3 G3~
    21: [(44, 4), (51, 4), (56, 8)],                            # Ab  Ab2 Eb3 Ab3~
    22: [(43, 4), (50, 4), (55, 4), (58, 4)],                   # Gm  G2 D3 G3 Bb3
    23: [(50, 8), (45, 8)],                                     # D   D3~ A2~
})
for _tune in (WHISTLE, TRUMPET, TWANG):
    for _row in _tune.values():
        assert sum(d for _, d in _row) == 16, _row


# ── every note the score holds, as (start s, sounding s, midi, part, role, written s) ──
def tune_notes(tune, part):
    out = []
    for lb, row in tune.items():
        pos = 0
        for m, d in row:
            if m:
                out.append((lb * BAR + pos * S16, d * S16, m, part, 'lead', d * S16))
            pos += d
    return out


def bass_line(lb):
    """(sixteenth, midi, sixteenths) for loop bar lb."""
    sec, v = section(lb), CH[CHORDS[lb]]
    r, f = v['root'], v['fifth']
    if sec == 'intro':
        return [(0, r, 15)] if lb >= 2 else []
    if sec == 'A':
        return [(0, r, 6), (6, f, 2), (8, r, 6), (14, f, 2)]
    if sec == 'B':
        return [(0, r, 3), (3, r, 1), (4, f, 4), (8, r, 3), (11, r, 1), (12, f, 4)]
    return [(0, r, 15)] if lb < 23 else [(0, r, 8), (8, r, 7)]


ARP = [0, 1, 2, 3, 4, 3, 2, 1]                     # nylon, A: string order on the eighths
STRUM = [(0, 'd', 1.0), (6, 'u', 0.6), (8, 'd', 0.85), (11, 'u', 0.55), (12, 'd', 0.8), (14, 'u', 0.5)]


def nylon_plucks():
    """(t, string, midi, vel, strum offset index) for the whole loop."""
    ev = []
    for lb in range(BARS):
        sec, v = section(lb), CH[CHORDS[lb]]
        t = lb * BAR
        if sec == 'A':
            for k, s in enumerate(ARP):
                ev.append((t + 2 * k * S16, s, v['gtr'][s], 0.95 if k == 0 else 0.7, 0))
        elif sec == 'B':
            for pos, way, vel in STRUM:
                strings = range(5) if way == 'd' else (4, 3, 2)
                for j, s in enumerate(strings):
                    ev.append((t + pos * S16 + j * 0.011, s, v['gtr'][s], vel * (0.8 if way == 'u' else 1.0), j))
        elif sec == 'intro' and lb >= 2:                 # one soft spread chord a bar
            for j, s in enumerate(range(5)):
                ev.append((t + j * 0.045, s, v['gtr'][s], 0.55, j))
    return sorted(ev)


def ring_out(events, start_of, string_of, midi_of, cap):
    """How long each pluck sounds: until its string is plucked again (around the
    loop), or until the chord changes to one it is not in (the fretting hand
    lets go), at most `cap` seconds."""
    by = {}
    for i, e in enumerate(events):
        by.setdefault(string_of(e), []).append(i)
    ring = [0.0] * len(events)
    for s, idx in by.items():
        for j, i in enumerate(idx):
            t = start_of(events[i])
            nxt = start_of(events[idx[(j + 1) % len(idx)]])
            gap = (nxt - t) % LOOP or LOOP
            dur = min(gap, cap)
            tc = (np.floor(t / BAR + 1e-9) + 1) * BAR
            while tc < t + dur:
                if midi_of(events[i]) % 12 not in CH[chord_at(tc)]['pcs']:
                    dur = tc - t
                    break
                tc += BAR
            ring[i] = dur
    return ring


NYLON = nylon_plucks()
NYLON_RING = ring_out(NYLON, lambda e: e[0], lambda e: e[1], lambda e: e[2], 2.4)


def choir_notes():
    """(t, dur, midi, vowel): each voice held while its note stays."""
    vowel = {'intro': 'mm', 'A': 'oo', 'B': 'ah', 'standoff': 'mm'}
    out = []
    for k in range(3):
        cur = None
        for lb in range(BARS):
            if section(lb) == 'intro' and lb < 1:
                if cur:
                    out.append(cur); cur = None
                continue
            m = CH[CHORDS[lb]]['choir'][k]; vw = vowel[section(lb)]
            if cur and cur[2] == m and cur[3] == vw and abs(cur[0] + cur[1] - lb * BAR) < 1e-9:
                cur[1] += BAR
            else:
                if cur:
                    out.append(cur)
                cur = [lb * BAR, BAR, m, vw]
        out.append(cur)
    return [tuple(c) for c in out]


CHOIR = choir_notes()


def timp_hits():
    """(t, midi, vel, length): a stroke on each B downbeat, the standoff's heartbeat, a roll on D."""
    out = []
    root = {'Gm': 43, 'Ab': 44, 'D': 38, 'D7': 38, 'Bb': 46, 'F': 41, 'Eb': 39, 'Cm': 43}
    for lb in range(BARS):
        sec, c = section(lb), CHORDS[lb]
        t = lb * BAR
        if sec == 'B' or lb == 0:                       # bar 0: the roll lands on G, with the bell
            out.append((t, root[c], 0.8 if lb else 0.9, BAR))
        elif sec == 'standoff' and lb < 23:
            for q in range(4):
                out.append((t + q * BEAT, root[c], 0.75, S16))
                out.append((t + q * BEAT + S16, root[c], 0.45, BEAT - S16))
        elif lb == 23:
            for k in range(24):
                out.append((t + k * BEAT / 6, 38, 0.15 + 0.6 * (k / 24) ** 1.5, BEAT / 6))
    return out


TIMP = timp_hits()
ANVIL = [(lb * BAR + q * S16, CH[CHORDS[lb]]['fifth'] % 12 + 84 if CHORDS[lb] != 'Bb' else 89)
         for lb in (16, 17, 18, 19) for q in (4, 12)]
BELLS = [(0.0, 2 * BAR), (20 * BAR, BAR), (22 * BAR, BAR)]       # (t, how long it rings before it is stopped)
BELL_PARTIALS = [(0.5, 0.35, 2.6), (1.0, 1.0, 2.0), (2 ** (3 / 12), 0.55, 1.4), (2 ** (7 / 12), 0.35, 1.1),
                 (2.0, 0.42, 0.9), (3.0, 0.12, 0.5), (4.0, 0.08, 0.35)]   # ratio (G, Bb, D only), amp, tau
BELL_ROOT = 55


def score():
    notes = tune_notes(WHISTLE, 'whistle') + tune_notes(TRUMPET, 'trumpet') + tune_notes(TWANG, 'twang')
    for lb in range(BARS):
        for pos, m, d in bass_line(lb):
            notes.append((lb * BAR + pos * S16, d * S16, m, 'bass', 'harm', d * S16))
    for (t, s, m, vel, _), r in zip(NYLON, NYLON_RING):
        notes.append((t, r, m, 'nylon', 'harm', r))
    for t, d, m, _ in CHOIR:
        notes.append((t, d, m, 'choir', 'harm', d))
    for t, m, v, d in TIMP:
        notes.append((t, d, m, 'timpani', 'harm', d))
    for t, m in ANVIL:
        notes.append((t, 0.45, m, 'anvil', 'harm', 0.45))
    for t, d in BELLS:
        for ratio, _, _ in BELL_PARTIALS:
            notes.append((t, d, BELL_ROOT + round(12 * np.log2(ratio)), 'bell', 'harm', d))
    return notes


NOTES = score()


def check():
    """Chord tones where it matters, and no rubs: see the docstring."""
    bad = []
    eps = 1e-6

    def chords_over(t, d):
        out, tc = [chord_at(t)], (np.floor(t / BAR + 1e-9) + 1) * BAR
        while tc < t + d - eps:
            out.append(chord_at(tc)); tc += BAR
        return out

    def long_(n):
        t, d, m, part, role, w = n
        return role != 'lead' or w >= BEAT - eps or abs((t / (2 * BEAT)) - round(t / (2 * BEAT))) < 1e-6

    for n in NOTES:
        t, d, m, part, role, w = n
        if long_(n):
            span = d if role != 'lead' else w
            for c in chords_over(t, span):
                if m % 12 not in CH[c]['pcs']:
                    bad.append((part, round(t / BAR, 3), m, c, 'not a chord tone'))
    ev = sorted(NOTES + [(n[0] - LOOP,) + n[1:] for n in NOTES] + [(n[0] + LOOP,) + n[1:] for n in NOTES])
    for i, a in enumerate(ev):
        if not 0 <= a[0] < LOOP:
            continue
        for b in ev[i + 1:]:
            if b[0] >= a[0] + a[1] - eps:
                break
            if b[0] + b[1] <= a[0] + eps or b is a:
                continue
            iv = abs(a[2] - b[2])
            if iv in (1, 11, 13) or (long_(a) and long_(b) and iv % 12 in (1, 11)):
                bad.append((a[3], round(a[0] / BAR, 3), a[2], b[3], round(b[0] / BAR, 3), b[2], 'rub'))
    print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad[:20])
    assert not bad, 'a wrong note (listed above)'


check()


# ── instruments ─────────────────────────────────────────────────────────────
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
    kk = np.arange(1, int(max(2, min(60, top / f))) + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -tilt * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    exc += noise * lp1(np.random.default_rng(seed).uniform(-1, 1, N), min(top, 9000)) * np.sin(np.pi * np.arange(N) / N)
    k = max(1, int(comb * N))
    exc[k:] -= 0.5 * exc[:-k]
    return exc / np.abs(exc).max()


def string(m, ring, vel, seed, a=0.8, t60=3.0, tilt=0.9, noise=0.15, comb=0.18, top=6000, rel=0.06):
    f = hz(m)
    N, c, den = ks_setup(f, a, t60)
    exc = pick(N, f, tilt, noise, comb, seed, top)
    n = int((ring + rel + 0.01) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * vel
    y = lfilter([1.0, c], den, x)
    y[:48] *= np.linspace(0, 1, 48)                          # 1 ms: the pick, not a step
    t = np.arange(n) / SR
    return y * np.clip((ring + rel - t) / rel, 0, 1)


def nylon_body(x):
    y = x + 0.5 * bp(x, 110, 2.2) + 0.3 * bp(x, 230, 2.5) + 0.12 * bp(x, 2600, 1.5)
    return hp1(y, 75)


def twang_amp(x):
    y = np.tanh(2.2 * x) / 2.2
    y = y + 0.35 * bp(y, 1300, 0.9) + 0.25 * bp(y, 3400, 1.4)
    return lp(lp1(y, 11000), 6200, 0.8)


def voice_phrase(notes, f_vib=5.6, vib_c=22, glide_hz=26, scoop_c=55, attack=0.03, release=0.07):
    """A continuous monophonic voice through notes [(t, d, midi)] (t from the
    phrase start): pitch curve with glides, an envelope that dips between
    tied notes and closes at rests, vibrato growing on long notes. Returns
    (phase, gain, f) for an oscillator bank."""
    total = notes[-1][0] + notes[-1][1]
    n = int((total + release + 0.05) * SR)
    f = np.full(n, hz(notes[0][2])); g = np.zeros(n); vw = np.zeros(n); sc = np.zeros(n)
    for j, (t, d, m) in enumerate(notes):
        a, b = int(round(t * SR)), int(round((t + d) * SR))
        tt = np.arange(n - a) / SR
        tied = j + 1 < len(notes) and abs(notes[j + 1][0] - (t + d)) < 1e-6
        fresh = j == 0 or abs(notes[j - 1][0] + notes[j - 1][1] - t) > 1e-6
        f[a:] = hz(m)
        env = np.minimum(1, tt / attack) if fresh else 1 - 0.18 * np.exp(-tt / 0.04)   # a legato note: a dip, not a new attack
        if not tied:
            g[a:] = np.maximum(g[a:], env * np.clip((d + release - tt) / release, 0, 1))
        else:
            g[a:b] = env[:b - a]
        vw[a:b] = np.clip((tt[:b - a] - 0.22) / 0.5, 0, 1) * (1.0 if d > 0.45 else 0.25)
        sc[a:b] += -(scoop_c if fresh else scoop_c * 0.3) * np.exp(-tt[:b - a] / 0.045)
    f = lfilter([1 - np.exp(-2 * np.pi * glide_hz / SR)], [1, -np.exp(-2 * np.pi * glide_hz / SR)],
                f - f[0]) + f[0]
    t = np.arange(n) / SR
    cents = sc + vib_c * lp1(vw, 8) * np.sin(2 * np.pi * f_vib * t + 0.4 * np.sin(2 * np.pi * 0.31 * t))
    fr = f * 2 ** (cents / 1200)
    return 2 * np.pi * np.cumsum(fr) / SR, lp1(g, 60), fr


def whistle_phrase(notes, seed):
    ph, g, fr = voice_phrase(notes, f_vib=5.4, vib_c=24, glide_hz=30, scoop_c=60, attack=0.035)
    n = len(ph)
    z = rng('whistle', seed).standard_normal(n)
    tone = np.sin(ph) + 0.035 * np.sin(2 * ph)
    breath = lp1(z, 140) * np.sin(ph) * 2.2 + (hp1(lp(z, 10000), 4000) * 0.16 + bp(z, 7000, 1.4) * 0.17)
    return (tone + breath * 0.5) * g


def trumpet_phrase(notes, seed):
    ph, g, fr = voice_phrase(notes, f_vib=6.3, vib_c=30, glide_hz=40, scoop_c=90, attack=0.04, release=0.09)
    n = len(ph)
    s = 0.62 - 0.4 * g                                       # brighter as it swells
    K = int(11000 / fr.min())
    x = np.zeros(n)
    for k in range(1, K + 1):
        x += k ** -0.5 * np.exp(-(k - 1) * s) * np.clip((11000 - k * fr) / 2000, 0, 1) * np.sin(k * ph)
    x = x + 0.9 * bp(x, 1300, 1.2) + 0.25 * bp(x, 2900, 1.8)
    x = lp(hp1(x, 250), 9500, 0.6)
    z = rng('tpt', seed).standard_normal(n)
    onset = np.zeros(n)
    for t, d, m in notes:
        a = int(round(t * SR)); tt = np.arange(n - a) / SR
        onset[a:] += np.exp(-tt / 0.05)
    breath = bp(z, 1600, 0.8) * (0.3 * np.minimum(onset, 1) + 0.04) + hp1(z, 5000) * 0.02
    return x * g + breath * g


VOWELS = {'mm': [(260, 120, 1.0), (1900, 400, 0.04)],
          'oo': [(330, 120, 1.0), (760, 160, 0.55), (2400, 300, 0.06)],
          'ah': [(700, 150, 1.0), (1150, 180, 0.7), (2600, 300, 0.22), (3400, 400, 0.08)]}


def choir_note(m, dur, vowel, seed, attack=0.6, release=0.8):
    n = int((dur + release + 0.05) * SR); t = np.arange(n) / SR
    r = rng('choir', seed)
    F = VOWELS[vowel]
    x = np.zeros(n)
    for v, cents in enumerate((-8, -1, 7)):
        f0 = hz(m) * 2 ** (cents / 1200)
        vib = 1 + 0.0032 * np.sin(2 * np.pi * (4.7 + 0.35 * v) * t + r.uniform(0, 6.3)) * np.clip((t - 0.4) / 0.8, 0, 1)
        ph = 2 * np.pi * np.cumsum(f0 * vib) / SR
        for k in range(1, int(min(60, 7500 / f0)) + 1):
            fk = k * f0
            a = k ** -0.7 * (0.03 + sum(gn * np.exp(-((fk - fc) / bw) ** 2) for fc, bw, gn in F))
            x += a * np.sin(k * ph + r.uniform(0, 6.3))
    z = r.standard_normal(n)
    x += 0.6 * bp(z, F[0][0] * 1.6, 1.5) * (0.4 if vowel == 'ah' else 0.15) + hp1(lp1(z, 12000), 5000) * 0.05
    return x / 3 * adsr(n, attack, 0.4, 0.88, release, dur)


def coconut(seed, tone):
    n = int(0.07 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = (bp(z, 1250 * tone, 1.6) * np.exp(-t / 0.009) + 0.6 * hp(z, 3500) * np.exp(-t / 0.0025)
         + 1.2 * bp(z, 7000, 1.2) * np.exp(-t / 0.002))
    return x * np.minimum(1, t / 0.0004)


def maraca(seed, acc):
    n = int(0.09 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = (hp(lp(z, 9500), 4200) + 1.2 * bp(z, 7000, 1.6)) * (np.minimum(1, t / 0.006) * np.exp(-t / (0.018 + 0.012 * acc)))
    return x


def rattle(seed, dur):
    """A rattlesnake: a dry buzz of clicks about 50 a second, swelling and dying."""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    r = rng('rattle', seed)
    z = r.standard_normal(n)
    rate = 46 + 6 * np.sin(2 * np.pi * u * 1.3)
    am = (0.5 + 0.5 * np.sin(2 * np.pi * np.cumsum(rate) / SR)) ** 6
    env = np.sin(np.pi * u) ** 0.7 * (0.75 + 0.25 * np.sin(2 * np.pi * 3.1 * u))
    return hp(lp1(z, 15000), 3800) * am * env


def cymbal_swell(dur, seed):
    """A suspended cymbal rolled with soft mallets, swelling to the beat."""
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR
    r = rng('cym', seed)
    z = r.standard_normal(n)
    env = np.where(t < dur, (t / dur) ** 2.2, np.exp(-(t - dur) / 0.35))
    x = hp(lp1(z, 16000), 2500) + 0.5 * bp(z, 5200, 0.8)
    return x * env


def whip(seed):
    n = int(0.3 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    sw = np.clip(t / 0.17, 0, 1) ** 2 * (t < 0.17)
    whoosh = bp(z, 900, 0.7) * sw * 0.25
    k = int(0.17 * SR); tc = np.clip(t - 0.17, 0, None)
    crack = (hp(z, 2500) * np.exp(-tc / 0.004) + 0.6 * bp(z, 1800, 1.0) * np.exp(-tc / 0.012)) * np.clip((t - 0.17) / 0.0004, 0, 1)
    return whoosh + crack


def anvil(m, seed):
    f = hz(m); n = int(0.9 * SR); t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.35) + 0.4 * np.sin(2 * np.pi * 2.76 * f * t) * np.exp(-t / 0.09)
         + 0.25 * np.sin(2 * np.pi * 5.4 * f * t) * np.exp(-t / 0.03))
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.6 * hp(z, 4000) * np.exp(-t / 0.003)
    return x * np.minimum(1, t / 0.0006)


def bell(ring, seed):
    """A church bell on G: hum, prime, minor-third tierce, quint, nominal, and
    two upper partials on the same three notes; stopped `ring` s after the strike."""
    f = hz(BELL_ROOT); n = int((ring + 0.4) * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    r = rng('bell', seed)
    for ratio, a, tau in BELL_PARTIALS:
        beat = 1 + 0.0009 * r.uniform(-1, 1)
        x += a * np.sin(2 * np.pi * f * ratio * beat * t + r.uniform(0, 6.3)) * np.exp(-t / tau)
    z = r.standard_normal(n)
    x += 0.3 * bp(z, 2400, 1.0) * np.exp(-t / 0.006)
    return x * np.minimum(1, t / 0.0015) * np.clip((ring - t) / 0.35, 0, 1)        # stopped by the change


def timp(m, v, seed, ring):
    f = hz(m); n = int((ring + 0.12) * SR); t = np.arange(n) / SR
    bend = np.cumsum(1 + 0.012 * np.exp(-t / 0.08)) / SR
    x = np.zeros(n)
    for r_, a, tau in ((1, 1, 1.1), (1.5, 0.45, 0.6), (1.99, 0.3, 0.45), (2.44, 0.14, 0.3), (2.98, 0.08, 0.22)):
        x += a * np.sin(2 * np.pi * f * r_ * bend) * np.exp(-t / tau)
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.45 * lp(z, 400) * np.exp(-t / 0.02) + 0.08 * hp(z, 3000) * np.exp(-t / 0.004)
    return x * np.minimum(1, t / 0.002) * v * np.clip((ring - t) / min(0.1, ring / 2), 0, 1)


def wind(seed, dur):
    """A gust: band-passed noise whose centre rises and falls, stereo."""
    n = int(dur * SR); u = np.arange(n) / n
    r = rng('wind', seed)
    env = np.sin(np.pi * u) ** 2 * (0.7 + 0.3 * np.sin(2 * np.pi * (u * r.uniform(1.5, 2.5) + r.random())))
    out = np.zeros((n, 2))
    CH_ = 960
    for ch in range(2):
        z = r.standard_normal(n); y = np.empty(n); zi = np.zeros(2)
        for i in range(0, n, CH_):
            fc = 380 + 900 * env[i] ** 1.3
            w = 2 * np.pi * fc / SR; q = 0.9; al = np.sin(w) / (2 * q); c = np.cos(w)
            b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
            y[i:i + CH_], zi = lfilter(b / a[0], a / a[0], z[i:i + CH_], zi=zi)
        out[:, ch] = y * env + hp1(lp1(z, 7000), 3000) * env ** 2 * 0.08
    return out


# ── render ──────────────────────────────────────────────────────────────────
def place(bus, t, sig, pan=0.0, gain=1.0):
    """Add an event of the loop on every lap the timeline holds."""
    for k in (-1, 0, 1):
        tt = t + k * LOOP
        if tt + len(sig) / SR > -tl.pre * BAR and tt < (BARS + tl.post) * BAR + 1:
            bus.add(tt, sig, pan, gain)


def phrases(tune):
    """Split a tune into phrases at its rests: [(t0, [(t, d, midi), ...])]."""
    notes = sorted((s, d, m) for s, d, m, *_ in tune_notes(tune, ''))
    out = []
    for s, d, m in notes:
        if out and abs(out[-1][1][-1][0] + out[-1][0] + out[-1][1][-1][1] - s) < 1e-6:
            out[-1][1].append((s - out[-1][0], d, m))
        else:
            out.append((s, [(0.0, d, m)]))
    return out


LEVEL = {'intro': 0.8, 'A': 1.0, 'B': 1.0, 'standoff': 0.85}


def render(wav=None):
    whis, tpt, nyl, twg, cho, low, hoof, perc_, bells, air, shk = (tl.bus() for _ in range(11))

    for i, (t0, notes) in enumerate(phrases(WHISTLE)):
        place(whis, t0, whistle_phrase(notes, i), pan=-0.08, gain=0.105)
    for i, (t0, notes) in enumerate(phrases(TRUMPET)):
        place(tpt, t0, trumpet_phrase(notes, i), pan=0.12, gain=0.05)
    for (t, s, m, vel, j), r in zip(NYLON, NYLON_RING):
        lb = int(t // BAR) % BARS
        place(nyl, t, string(m, r, vel, int(t * 1000) + s, a=0.8, t60=2.6, tilt=0.95, noise=0.2, comb=0.2, top=8000),
              pan=-0.35 + 0.08 * s, gain=0.22 if section(lb) == 'A' else 0.17)
    for t, d, m, part, role, w in NOTES:
        if part == 'twang':
            place(twg, t, string(m, d, 1.0, int(t * 1000), a=0.88, t60=3.5, tilt=0.7, noise=0.2, comb=0.08, top=9000,
                                 rel=0.05), pan=0.3, gain=0.42)
    for j, (t, d, m, vowel) in enumerate(CHOIR):
        place(cho, t, choir_note(m, d - 0.05, vowel, j), pan=(-0.45, 0.05, 0.45)[j % 3],
              gain={'mm': 0.05, 'oo': 0.045, 'ah': 0.045}[vowel])
    for lb in range(BARS):
        t = lb * BAR; sec = section(lb)
        for pos, m, d in bass_line(lb):
            place(low, t + pos * S16, string(m, d * S16, 1.0, lb * 16 + pos, a=0.55, t60=2.2, tilt=1.4, noise=0.05,
                                             comb=0.22, top=2400, rel=0.05), gain=0.34)
        # hooves: a trot in A, a gallop in B
        if sec in ('A', 'B'):
            pat = (0, 3, 4, 7, 8, 11, 12, 15) if sec == 'A' else (0, 2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15)
            for k, pos in enumerate(pat):
                acc = 1.0 if pos % 4 == 0 else 0.7
                place(hoof, t + pos * S16, coconut(lb * 32 + pos, 1.0 if k % 2 == 0 else 1.25),
                      pan=0.25 if k % 2 == 0 else 0.4, gain=(0.2 if sec == 'A' else 0.2) * acc)
        if sec == 'B':                                 # maracas on the eighths
            for pos in range(0, 16, 2):
                acc = 1.0 if pos % 4 == 0 else 0.6
                place(shk, t + pos * S16, maraca(lb * 16 + pos, acc), pan=-0.4, gain=0.085 * acc)
        if lb in (1, 21):                              # the rattlesnake
            place(shk, t + (BEAT if lb == 1 else 0), rattle(lb, 2.6), pan=0.5 if lb == 1 else -0.5, gain=0.05)
        if lb in (11, 23):                             # a cymbal swells into B, and into the top of the loop
            place(shk, t + 2 * BEAT, cymbal_swell(2 * BEAT, lb), pan=0.1, gain=0.045)
        if lb in (12, 16):
            place(perc_, t - 0.17, whip(lb), pan=-0.3, gain=0.16)
        if sec in ('intro', 'standoff') and lb % 2 == 0:
            place(air, t - 0.4 * BAR, wind(lb, 2.8 * BAR), gain=0.07 if sec == 'intro' else 0.06)
    for t, m, v, d in TIMP:
        place(perc_, t, timp(m, v, int(t * 100), d), pan=-0.2, gain=0.3)
    for t, m in ANVIL:
        place(bells, t, anvil(m, int(t * 10)), pan=0.45, gain=0.05)
    for j, (t, d) in enumerate(BELLS):
        place(bells, t, bell(d, j), pan=0.0, gain=0.11)

    nx = nylon_body(nyl.x)
    tx = twang_amp(twg.x)
    tx = tx + 0.4 * np.roll(tx, int(0.105 * SR), axis=0)            # slapback (the roll's wrap lands in the pre-roll)
    wx = whis.x + pingpong(whis.x, 3 * S16, 0.32, 4, 3500) * 0.55
    px = tpt.x + pingpong(tpt.x, 3 * S16, 0.25, 3, 3000) * 0.45
    hall = make_ir(3.0, dark=7500, seed=23, pre=0.035)
    stems = dict(whistle=wx, trumpet=px, nylon=nx, twang=tx, choir=cho.x, bass=low.x, hooves=hoof.x,
                 perc=perc_.x, bells=bells.x, wind=air.x, shakers=shk.x)
    send = dict(whistle=0.45, trumpet=0.45, nylon=0.25, twang=0.35, choir=0.4, bass=0.05, hooves=0.2,
                perc=0.3, bells=0.5, wind=0.3, shakers=0.25)
    wet = reverb(sum(stems[k] * send[k] for k in stems), hall) * 0.5
    stems['reverb'] = wet
    mix = sum(stems.values())
    if '--stems' in sys.argv:
        stem_report(stems, mix)
    return finish(tl, mix, NAME, wav=wav)


def a_weight(f):
    f2 = np.asarray(f, float) ** 2
    ra = 12194 ** 2 * f2 ** 2 / ((f2 + 20.6 ** 2) * np.sqrt((f2 + 107.7 ** 2) * (f2 + 737.9 ** 2)) * (f2 + 12194 ** 2))
    return ra * 10 ** (2.0 / 20)


def stem_report(stems, mix):
    """Per stem: A-weighted level (dB re the mix) by section, and the biggest
    sample jump of its top octave against its 99.9th percentile (a click
    stands out)."""
    i0, N = tl.smp(0), int(round(LOOP * SR))
    secs = [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ('standoff', 20, 24)]

    def lev(x):
        X = np.fft.rfft(x.mean(1)); f = np.fft.rfftfreq(len(x), 1 / SR)
        return np.sum(np.abs(X) ** 2 * a_weight(f) ** 2) / len(x) ** 2

    refs = [lev(mix[i0 + int(a * BAR * SR):i0 + int(b * BAR * SR)]) for _, a, b in secs]

    def band(x, lo, hi):
        X = np.fft.rfft(x[i0:i0 + N].mean(1)); f = np.fft.rfftfreq(N, 1 / SR)
        return np.sum(np.abs(X[(f >= lo) & (f < hi)]) ** 2)

    tot = band(mix, 0, SR)
    hm = np.abs(np.diff(hp(mix.mean(1), 6000)[i0:i0 + N])); hm = np.percentile(hm, 99.9)
    print('stem (dBA re mix) ' + ' '.join(f'{s:>9s}' for s, _, _ in secs) + '    click (own, vs mix)        6-8k   8k+ (dB of the mix)')
    for k, v in stems.items():
        row = [10 * np.log10(lev(v[i0 + int(a * BAR * SR):i0 + int(b * BAR * SR)]) / r + 1e-12)
               for (_, a, b), r in zip(secs, refs)]
        h = np.abs(np.diff(hp(v.mean(1), 6000)[i0:i0 + N]))
        ratio = h.max() / (np.percentile(h, 99.9) + 1e-12)
        hf = [10 * np.log10(band(v, lo, hi) / tot + 1e-12) for lo, hi in ((6000, 8000), (8000, SR))]
        print(f'{k:15s}   ' + ' '.join(f'{r:9.1f}' for r in row) + f'   {ratio:6.1f}x {20 * np.log10(h.max() / hm):+6.1f} dB at {np.argmax(h) / SR:6.2f} s'
              + f'   {hf[0]:6.1f} {hf[1]:6.1f}')


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
