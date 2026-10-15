#!/usr/bin/env python3
"""Block Camp soundtrack "Castle of If" (Blocula RPG, dracula-castle-of-if.html).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is Bram Stoker's
journey as a branching grammar nightmare (conditionals and the passive):
Jonathan Harker in Transylvania to complete a property sale, a castle whose
gates close at the end. So: the idiom of a gothic horror score - a storm,
a tolling bell, a church organ, a harpsichord turning its arpeggios like a
music box, a solo violin for the tune; then a wordless choir and timpani as
the castle closes in, the organ taking the tune low. An original piece in
that idiom: no melody or progression is taken from any film or record.

D minor (harmonic: an A major dominant), 64 BPM, 4/4 (a sixteenth is exactly
11250 samples, a bar 3.75 s). One chord a bar:

  intro  Dm | Dm | Bb | A                     bars 0-3    thunder, the bell, the organ; the
                                                          harpsichord's chords
  A      Dm | Gm | A  | Dm | Bb | Gm | A | A  bars 4-11   the violin's tune over the harpsichord
  B      Gm | Dm | Bb | F  | Gm | Dm | A | A  bars 12-19  the organ's tune, choir "ah", timpani;
                                                          a roll on A back to the top

The tune (violin, bar 4): D5 F5 A5~ G5 | Bb5~ A5 G5 | E5 C#5 A4~ B4 | D5 A4 F4.

rpgkit.Song.check() proves the harmony at import (see rpgkit.py). The bell
(partials D, F, A only) strikes over D minor and is damped at the change.

Instruments (rpgkit.py): violin = bowed_phrase; harpsichord =
Karplus-Strong, plucked near the bridge, bright and short; organ =
pad_note('organ') (held chords, the pedal, and the B tune note by note);
choir = choir_note('ah'); timpani; a church bell; thunder; wind.
20 bars = 75 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/blocula.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from synthkit import Timeline
from rpgkit import (Song, string, body, bowed_phrase, choir_note, pad_note, bell, timp, thunder, wind, pingpong)

NAME = 'blocula'
tl = Timeline(bpm=64, bars=20)
CH = {'Dm': {2, 5, 9}, 'Gm': {7, 10, 2}, 'A': {9, 1, 4}, 'Bb': {10, 2, 5}, 'F': {5, 9, 0}}
CHORDS = (['Dm', 'Dm', 'Bb', 'A'] +
          ['Dm', 'Gm', 'A', 'Dm', 'Bb', 'Gm', 'A', 'A'] +
          ['Gm', 'Dm', 'Bb', 'F', 'Gm', 'Dm', 'A', 'A'])
S = Song(tl, CH, CHORDS, [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20)])
BAR, BEAT, S16, LOOP = S.BAR, S.BEAT, S.S16, S.LOOP

PEDAL = {'Dm': 38, 'Gm': 43, 'A': 45, 'Bb': 46, 'F': 41}
ORGAN = {'Dm': [50, 57, 62, 65], 'Gm': [50, 55, 58, 62], 'A': [52, 57, 61, 64], 'Bb': [50, 53, 58, 62],
         'F': [48, 53, 57, 60]}
HARPSI = {'Dm': [50, 57, 62, 65, 69, 74], 'Gm': [43, 50, 55, 58, 62, 67], 'A': [45, 52, 57, 61, 64, 69],
          'Bb': [46, 53, 58, 62, 65, 70], 'F': [41, 48, 53, 57, 60, 65]}
CHOIR = {'Gm': [62, 67, 70], 'Dm': [62, 65, 69], 'Bb': [62, 65, 70], 'F': [60, 65, 69], 'A': [61, 64, 69]}
TIMP = {'Dm': 38, 'Gm': 43, 'A': 45, 'Bb': 46, 'F': 41}

VIOLIN = {
    4: [(74, 4), (77, 4), (81, 6), (79, 2)],                # Dm  D F A~ G
    5: [(82, 6), (81, 2), (79, 8)],                         # Gm  Bb~ A G~
    6: [(76, 4), (73, 4), (69, 6), (71, 2)],                # A   E C# A~ B
    7: [(74, 4), (69, 4), (65, 8)],                         # Dm  D A F~
    8: [(74, 4), (77, 4), (82, 8)],                         # Bb  D F Bb~
    9: [(79, 6), (77, 2), (74, 4), (70, 4)],                # Gm  G~ F D Bb
    10: [(76, 6), (73, 2), (76, 4), (81, 4)],               # A   E~ C# E A
    11: [(73, 8), (69, 8)],                                 # A   C#~ A~
}
ORGAN_TUNE = {
    12: [(67, 8), (70, 8)],                                 # Gm  G~ Bb~
    13: [(69, 8), (65, 4), (62, 4)],                        # Dm  A~ F D
    14: [(70, 6), (72, 2), (74, 8)],                        # Bb  Bb~ C D~
    15: [(72, 8), (69, 4), (65, 4)],                        # F   C~ A F
    16: [(67, 4), (70, 4), (74, 6), (72, 2)],               # Gm  G Bb D~ C
    17: [(77, 8), (74, 4), (69, 4)],                        # Dm  F~ D A
    18: [(73, 8), (76, 4), (69, 4)],                        # A   C#~ E A
    19: [(69, 8), (64, 4), (61, 4)],                        # A   A~ E C#
}
S.tune(VIOLIN, 'violin')
S.tune(ORGAN_TUNE, 'organ tune')

ORG = S.held(lambda lb: ORGAN[S.chord(lb)], 'organ')
PED = S.held(lambda lb: [PEDAL[S.chord(lb)]], 'pedal')
CHOIRN = S.held(lambda lb: CHOIR[S.chord(lb)] if S.section(lb) == 'B' else None, 'choir')

ARP = [0, 1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]


def harpsichord():
    ev = []
    for lb in range(tl.bars):
        sec, v = S.section(lb), HARPSI[S.chord(lb)]
        t = lb * BAR
        if sec == 'A':
            for k, s in enumerate(ARP):
                ev.append((t + k * S16, s, v[s], 0.9 if k % 4 == 0 else 0.65))
        else:                                               # spread chords on 1 (and on 3 in B)
            if sec == 'intro' and lb < 2:
                continue
            for h in ((0, 8) if sec == 'B' else (0,)):
                for j, s in enumerate(range(6)):
                    ev.append((t + h * S16 + j * 0.035, s, v[s], 0.6))
    return sorted(ev)


HARP = harpsichord()
HRING = S.ring_out(HARP, 1.2)
for (t, s, m, v), r in zip(HARP, HRING):
    S.harm(t, r, m, 'harpsichord')

TIMPS = []                                                  # (t, midi, vel, length)
for lb in range(12, 19):
    TIMPS.append((lb * BAR, TIMP[S.chord(lb)], 0.85, BAR / 2))
    TIMPS.append((lb * BAR + 2 * BEAT, TIMP[S.chord(lb)], 0.55, BAR / 2))
for k in range(32):                                         # the roll on A, back to the top
    TIMPS.append((19 * BAR + k * BEAT / 8, 45, 0.15 + 0.65 * (k / 32) ** 1.5, BEAT / 8))
for t, m, v, d in TIMPS:
    S.harm(t, d, m, 'timpani')

BELL_ROOT = 50
BELL_PARTIALS = [(0.5, 0.35, 2.8), (1.0, 1.0, 2.2), (2 ** (3 / 12), 0.55, 1.5), (2 ** (7 / 12), 0.35, 1.2),
                 (2.0, 0.4, 1.0), (3.0, 0.12, 0.55), (4.0, 0.08, 0.4)]          # D, F, A only
BELLS = [(0.0, 2 * BAR), (BAR, BAR), (13 * BAR, BAR), (17 * BAR, BAR)]           # (t, rings until the change)
for t, d in BELLS:
    for ratio, _, _ in BELL_PARTIALS:
        S.harm(t, d, BELL_ROOT + round(12 * np.log2(ratio)), 'bell')

S.check()


def render(wav=None):
    vn, og, ot, hs, cho, ti, bl, air = (tl.bus() for _ in range(8))
    for i, (t0, notes) in enumerate(S.phrases(VIOLIN)):
        S.place(vn, t0, bowed_phrase(notes, i), pan=0.12, gain=0.09)
    for t, d, m, part, role, w in S.notes:
        if part == 'organ tune':
            S.place(ot, t, pad_note(m, d - 0.02, int(t * 10), 'organ', release=0.15), pan=-0.1, gain=0.075)
    for t, d, m, k in ORG:
        S.place(og, t, pad_note(m, d - 0.03, int(t * 10) + k, 'organ', release=0.4), pan=(-0.35, 0.35, -0.15, 0.15)[k],
                gain=0.032)
    for t, d, m, k in PED:
        S.place(og, t, pad_note(m, d - 0.03, int(t * 10) + 7, 'organ', release=0.4), gain=0.06)
    for (t, s, m, v), r in zip(HARP, HRING):
        S.place(hs, t, string(m, r, v, int(t * 1000) + s, a=0.97, t60=1.8, tilt=0.5, noise=0.3, comb=0.06, top=11000,
                              rel=0.03), pan=-0.3 + 0.12 * s, gain=0.11)
    for t, d, m, k in CHOIRN:
        S.place(cho, t, choir_note(m, d - 0.05, 'ah', int(t * 10) + k), pan=(-0.4, 0.0, 0.4)[k], gain=0.045)
    for i, (t, m, v, d) in enumerate(TIMPS):
        S.place(ti, t, timp(m, v, i, d), pan=-0.2, gain=0.3)
    for j, (t, d) in enumerate(BELLS):
        S.place(bl, t, bell(BELL_ROOT, d, j, BELL_PARTIALS), gain=0.1 if j != 1 else 0.07)
    S.place(air, -0.4, thunder(0, 6.0), pan=-0.3, gain=0.18)
    S.place(air, 12 * BAR - 0.2, thunder(12, 5.0), pan=0.3, gain=0.12)
    for lb in (0, 2):
        S.place(air, lb * BAR - 0.3 * BAR, wind(lb, 2.6 * BAR), gain=0.06)
    hx = body(hs.x, [(500, 2, 0.3), (2500, 2, 0.25), (5000, 2, 0.15)], 90)
    vx = vn.x + pingpong(vn.x, 3 * S16, 0.25, 3, 3500) * 0.4
    stems = dict(violin=vx, organ_tune=ot.x, organ=og.x, harpsichord=hx, choir=cho.x, timpani=ti.x, bell=bl.x,
                 storm=air.x)
    send = dict(violin=0.45, organ_tune=0.55, organ=0.55, harpsichord=0.3, choir=0.5, timpani=0.35, bell=0.5,
                storm=0.2)
    return S.finish(stems, send, NAME, rt60=4.0, dark=6500, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
