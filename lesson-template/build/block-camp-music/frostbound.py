#!/usr/bin/env python3
"""Block Camp soundtrack "Frostbound" (Frostbound: The River Remembers RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is the frozen
north in the Present Simple: a river that remembers, a village that lives by
its routines through the long winter. So: the idiom of a Nordic folk score -
a willow flute calling over a frozen valley, a kantele (the plucked
zither) rippling in eighths, a low string section holding the ground like
ice, a solo fiddle for the river's memory, a frame drum's heartbeat, a
wordless "oo" choir, ice chimes and the wind. An original piece in that
idiom: no melody or progression is taken from any film or record.

A minor (aeolian), 80 BPM, 4/4 (a sixteenth is exactly 9000 samples, a bar
3 s). One chord a bar:

  intro  Am | Am | G  | Am                    bars 0-3    wind, ice chimes, the flute's call,
                                                          the low strings
  A      Am | C  | G  | Am | F | C | G | G    bars 4-11   the flute's tune over the kantele
  B      F  | G  | Am | Em | F | G | Am | Am  bars 12-19  the fiddle, high and long; the choir,
                                                          the frame drum
  outro  F  | G  | Am | Am                    bars 20-23  the flute comes down to A; chimes

The hook (flute, bar 4): A4 C5 E5~ D5 | E5~ D5 C5 | B4 D5 G5~ E5 | C5 D5 C5 A4.

rpgkit.Song.check() proves the harmony at import (see rpgkit.py). The frame
drum is tuned to the root of each bar; the chimes play chord tones and are
damped at the barline.

Instruments (rpgkit.py): willow flute = flute_phrase; kantele =
Karplus-Strong strings, bright, long, through a small box; fiddle =
bowed_phrase; strings = pad_note('strings'); choir = choir_note('oo');
chimes = mallet('glock'); frame drum; wind.
24 bars = 72 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/frostbound.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from synthkit import Timeline, rng
from rpgkit import (Song, string, body, flute_phrase, bowed_phrase, choir_note, pad_note, mallet,
                    frame_drum, wind, pingpong)

NAME = 'frostbound-river'
tl = Timeline(bpm=80, bars=24)
CH = {'Am': {9, 0, 4}, 'C': {0, 4, 7}, 'G': {7, 11, 2}, 'F': {5, 9, 0}, 'Em': {4, 7, 11}}
CHORDS = (['Am', 'Am', 'G', 'Am'] +
          ['Am', 'C', 'G', 'Am', 'F', 'C', 'G', 'G'] +
          ['F', 'G', 'Am', 'Em', 'F', 'G', 'Am', 'Am'] +
          ['F', 'G', 'Am', 'Am'])
S = Song(tl, CH, CHORDS, [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ('outro', 20, 24)])
BAR, BEAT, S16, LOOP = S.BAR, S.BEAT, S.S16, S.LOOP

ROOT = {'Am': 45, 'C': 48, 'G': 43, 'F': 41, 'Em': 40}
STRINGS = {'Am': [45, 52, 57, 60], 'C': [48, 55, 60, 64], 'G': [43, 50, 55, 59], 'F': [41, 48, 53, 57],
           'Em': [40, 47, 55, 59]}
KANTELE = {'Am': [45, 52, 57, 60, 64, 69], 'C': [48, 55, 60, 64, 67, 72], 'G': [43, 50, 55, 59, 62, 67],
           'F': [41, 48, 53, 57, 60, 65], 'Em': [40, 47, 52, 55, 59, 64]}
CHOIR = {'Am': [60, 64, 69], 'C': [60, 64, 67], 'G': [59, 62, 67], 'F': [60, 65, 69], 'Em': [59, 64, 67]}

FLUTE = {
    0: [(0, 8), (76, 8)],                                   # Am  .. E~
    1: [(81, 4), (76, 12)],                                 # Am  A E~
    2: [(0, 4), (74, 4), (79, 8)],                          # G   .. D G~
    3: [(76, 16)],                                          # Am  E~
    4: [(69, 4), (72, 4), (76, 6), (74, 2)],                # Am  A C E~ D
    5: [(76, 6), (74, 2), (72, 8)],                         # C   E~ D C~
    6: [(71, 4), (74, 4), (79, 6), (76, 2)],                # G   B D G~ E
    7: [(72, 4), (74, 2), (72, 2), (69, 8)],                # Am  C D C A~
    8: [(69, 4), (72, 4), (77, 8)],                         # F   A C F~
    9: [(76, 6), (74, 2), (72, 4), (67, 4)],                # C   E~ D C G
    10: [(71, 6), (69, 2), (74, 8)],                        # G   B~ A D~
    11: [(74, 4), (71, 4), (67, 8)],                        # G   D B G~
    20: [(77, 8), (72, 8)],                                 # F   F~ C~
    21: [(74, 8), (71, 8)],                                 # G   D~ B~
    22: [(69, 16)],                                         # Am  A~
}
FIDDLE = {
    12: [(81, 8), (77, 4), (79, 2), (77, 2)],               # F   A~ F G F
    13: [(79, 8), (74, 4), (71, 4)],                        # G   G~ D B
    14: [(72, 6), (74, 2), (76, 8)],                        # Am  C~ D E~
    15: [(79, 8), (76, 8)],                                 # Em  G~ E~
    16: [(77, 6), (79, 2), (81, 8)],                        # F   F~ G A~
    17: [(83, 8), (79, 4), (74, 4)],                        # G   B~ G D
    18: [(81, 12), (79, 2), (76, 2)],                       # Am  A~ G E
    19: [(76, 4), (72, 4), (69, 8)],                        # Am  E C A~
}
S.tune(FLUTE, 'flute')
S.tune(FIDDLE, 'fiddle')

PAD = S.held(lambda lb: STRINGS[S.chord(lb)], 'strings')
CHOIRN = S.held(lambda lb: CHOIR[S.chord(lb)] if S.section(lb) == 'B' else None, 'choir')

ARP = [0, 2, 3, 4, 5, 4, 3, 2]


def kantele_plucks():
    ev = []
    for lb in range(tl.bars):
        sec, v = S.section(lb), KANTELE[S.chord(lb)]
        t = lb * BAR
        if sec in ('A', 'outro'):
            for k, s in enumerate(ARP):
                ev.append((t + 2 * k * S16, s, v[s], 0.95 if k == 0 else 0.7))
        elif sec == 'B':                                    # a spread chord on 1 and 3
            for h in (0, 8):
                for j, s in enumerate(range(6)):
                    ev.append((t + h * S16 + j * 0.03, s, v[s], 0.6))
        elif lb >= 2:
            for j, s in enumerate(range(6)):
                ev.append((t + j * 0.06, s, v[s], 0.5))
    return sorted(ev)


KANT = kantele_plucks()
KRING = S.ring_out(KANT, 2.8)
for (t, s, m, v), r in zip(KANT, KRING):
    S.harm(t, r, m, 'kantele')

DRUM = []                                                   # (t, midi, vel): the heartbeat, tuned to the root
for lb in range(tl.bars):
    if S.section(lb) in ('B', 'outro'):
        r = ROOT[S.chord(lb)]
        for pos, v in ((0, 1.0), (3, 0.5), (8, 0.85), (11, 0.45)):
            if S.section(lb) == 'outro' and pos % 8:
                continue
            DRUM.append((lb * BAR + pos * S16, r, v))
for t, m, v in DRUM:
    S.harm(t, 0.35, m, 'drum')

CHIMES = []                                                 # (t, midi, ring)
for lb in range(tl.bars):
    if S.section(lb) in ('intro', 'outro'):
        r = rng('chimes', lb)
        tones = [m for m in range(84, 97) if m % 12 in CH[S.chord(lb)]]
        for pos in sorted(r.choice(range(0, 14, 2), 3, replace=False)):
            t = lb * BAR + pos * S16
            ring = min(1.6, (lb + 1) * BAR - t)
            CHIMES.append((t, int(r.choice(tones)), ring))
for t, m, ring in CHIMES:
    S.harm(t, ring, m, 'chimes')

S.check()


def render(wav=None):
    fl, fd, kt, st, cho, dr, ch, air = (tl.bus() for _ in range(8))
    for i, (t0, notes) in enumerate(S.phrases(FLUTE)):
        S.place(fl, t0, flute_phrase(notes, i, breath=0.6), pan=-0.1, gain=0.085)
    for i, (t0, notes) in enumerate(S.phrases(FIDDLE)):
        S.place(fd, t0, bowed_phrase(notes, i), pan=0.15, gain=0.08)
    for (t, s, m, v), r in zip(KANT, KRING):
        S.place(kt, t, string(m, r, v, int(t * 1000) + s, a=0.9, t60=4.0, tilt=0.8, noise=0.25, comb=0.12, top=9000),
                pan=-0.4 + 0.15 * s, gain=0.16)
    for t, d, m, k in PAD:
        S.place(st, t, pad_note(m, d - 0.05, int(t * 10) + k, 'strings', attack=0.9, release=0.6), pan=(-0.3, 0.3, -0.15, 0.15)[k],
                gain=0.07)
    for t, d, m, k in CHOIRN:
        S.place(cho, t, choir_note(m, d - 0.05, 'oo', int(t * 10) + k), pan=(-0.4, 0.0, 0.4)[k], gain=0.04)
    for t, m, v in DRUM:
        S.place(dr, t, frame_drum(int(t * 100), f0=float(440 * 2 ** ((m - 69) / 12)), vel=v), pan=0.05, gain=0.32)
    for i, (t, m, ring) in enumerate(CHIMES):
        S.place(ch, t, mallet(m, i, 'glock', 0.8, ring), pan=(-0.5, 0.5)[i % 2], gain=0.05)
    for lb in range(0, tl.bars, 2):
        S.place(air, lb * BAR - 0.5 * BAR, wind(lb, 3 * BAR, lo=500, span=1400),
                gain=0.07 if S.section(lb) in ('intro', 'outro') else 0.04)
    kx = body(kt.x, [(320, 2.5, 0.4), (1200, 2, 0.2), (3500, 1.5, 0.15)], 80)
    flx = fl.x + pingpong(fl.x, 3 * S16, 0.3, 4, 3500) * 0.5
    stems = dict(flute=flx, fiddle=fd.x, kantele=kx, strings=st.x, choir=cho.x, drum=dr.x, chimes=ch.x, wind=air.x)
    send = dict(flute=0.5, fiddle=0.45, kantele=0.3, strings=0.35, choir=0.5, drum=0.3, chimes=0.6, wind=0.3)
    return S.finish(stems, send, NAME, rt60=3.4, dark=8000, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
