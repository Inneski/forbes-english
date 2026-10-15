#!/usr/bin/env python3
"""Block Camp soundtrack "Fistful of Lies" (A Fistful of Lies RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is a voxel
western in the Past Simple: a frontier town where everyone tells a story
about what happened, and not every story is true. Last Bounty (its sister
western) has the standoff; this one has the town - the idiom of a comic
frontier score: a harmonica with a wink in it, a banjo rolling, boom-chick
bass and guitar, a fiddle for the tall tale, clip-clop woodblocks, a shaker
and a jaw harp's "boing" for every lie that lands. An original piece in that
idiom: no melody or progression is taken from any film or record.

D major, 90 BPM, 4/4 (a sixteenth is exactly 8000 samples, a bar 2.667 s).
One chord a bar:

  intro  D  | D | G | A                       bars 0-3    the jaw harp, a harmonica call, strums
  A      D  | G | D | A | D | G | A | D       bars 4-11   the harmonica tune over banjo and
                                                          boom-chick, the clip-clop
  B      Bm | G | D | A | Bm | G | E | A      bars 12-19  the fiddle's tall tale, the shaker
  A'     D  | G | D | A | D | C | G | A       bars 20-27  the tune again; the C (the flat
                                                          seventh) is the lie, with a boing

The tune (harmonica, bar 4): A4 D5 F#5~ E5 | G5~ E5 D5 | F#5 D5 A4 | C#5 E5 A5~ G5.

rpgkit.Song.check() proves the harmony at import (see rpgkit.py). The jaw
harp drones on the root of its bar.

Instruments (rpgkit.py): harmonica = reed_phrase('harmonica'); fiddle =
bowed_phrase; banjo = Karplus-Strong, bright and short through a drum-head
body; guitar = Karplus-Strong strums; bass = a plucked low string; jaw
harp; woodblocks; shaker.
28 bars = 74.67 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/fistful.py [--wav preview.wav] [--stems]
"""
import sys
from synthkit import Timeline
from rpgkit import (Song, string, body, reed_phrase, bowed_phrase, jaw_harp, woodblock, shaker, pingpong)

NAME = 'fistful-of-lies'
tl = Timeline(bpm=90, bars=28)
CH = {'D': {2, 6, 9}, 'G': {7, 11, 2}, 'A': {9, 1, 4}, 'Bm': {11, 2, 6}, 'E': {4, 8, 11}, 'C': {0, 4, 7}}
CHORDS = (['D', 'D', 'G', 'A'] +
          ['D', 'G', 'D', 'A', 'D', 'G', 'A', 'D'] +
          ['Bm', 'G', 'D', 'A', 'Bm', 'G', 'E', 'A'] +
          ['D', 'G', 'D', 'A', 'D', 'C', 'G', 'A'])
S = Song(tl, CH, CHORDS, [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ("A'", 20, 28)])
BAR, BEAT, S16, LOOP = S.BAR, S.BEAT, S.S16, S.LOOP

BASS = {'D': (38, 45), 'G': (43, 50), 'A': (45, 40), 'Bm': (47, 42), 'E': (40, 47), 'C': (36, 43)}
GTR = {'D': [50, 57, 62, 66], 'G': [55, 59, 62, 67], 'A': [52, 57, 61, 64], 'Bm': [50, 54, 59, 62],
       'E': [52, 56, 59, 64], 'C': [52, 55, 60, 64]}
BANJO = {'D': [62, 66, 69, 74], 'G': [62, 67, 71, 74], 'A': [61, 64, 69, 73], 'C': [60, 64, 67, 72]}
JAW = {0: 50, 2: 55, 25: 48}                                # bar -> the root it drones on

_A = {
    0: [(69, 4), (74, 4), (78, 6), (76, 2)],                # D   A D F#~ E
    1: [(79, 6), (76, 2), (74, 8)],                         # G   G~ E D~
    2: [(78, 4), (74, 4), (69, 8)],                         # D   F# D A~
    3: [(73, 4), (76, 4), (81, 6), (79, 2)],                # A   C# E A~ G
    4: [(78, 6), (76, 2), (74, 8)],                         # D   F#~ E D~
    5: [(71, 4), (74, 4), (79, 8)],                         # G   B D G~
    6: [(81, 6), (79, 2), (76, 4), (73, 4)],                # A   A~ G E C#
    7: [(74, 12), (0, 4)],                                  # D   D~
}
HARMONICA = {
    0: [(0, 8), (69, 4), (74, 4)],                          # D   .. A D
    1: [(78, 16)],                                          # D   F#~
    2: [(0, 8), (74, 8)],                                   # G   .. D~
    3: [(76, 8), (73, 8)],                                  # A   E~ C#~
}
HARMONICA.update({4 + k: row for k, row in _A.items()})
HARMONICA.update({20 + k: _A[k] for k in range(5)})
HARMONICA.update({
    25: [(72, 4), (76, 4), (79, 8)],                        # C   C E G~   (the lie)
    26: [(79, 6), (74, 2), (71, 8)],                        # G   G~ D B~
    27: [(73, 4), (76, 4), (69, 8)],                        # A   C# E A~
})
FIDDLE = {
    12: [(78, 8), (74, 4), (71, 4)],                        # Bm  F#~ D B
    13: [(79, 6), (81, 2), (83, 8)],                        # G   G~ A B~
    14: [(81, 8), (78, 4), (74, 4)],                        # D   A~ F# D
    15: [(76, 6), (78, 2), (81, 8)],                        # A   E~ F# A~
    16: [(83, 6), (81, 2), (78, 8)],                        # Bm  B~ A F#~
    17: [(79, 8), (74, 4), (71, 4)],                        # G   G~ D B
    18: [(76, 6), (78, 2), (80, 8)],                        # E   E~ F# G#~
    19: [(81, 8), (76, 4), (73, 4)],                        # A   A~ E C#
}
S.tune(HARMONICA, 'harmonica')
S.tune(FIDDLE, 'fiddle')


def plucks():
    """(t, string id, midi, vel, kind) for bass, guitar and banjo."""
    ev = []
    for lb in range(tl.bars):
        sec, c = S.section(lb), S.chord(lb)
        t = lb * BAR
        r, f = BASS[c]
        ev += [(t, 'b', r, 1.0, 'bass'), (t + 8 * S16, 'b', f, 0.85, 'bass')]
        if sec == 'intro':
            for j, m in enumerate(GTR[c]):
                ev.append((t + j * 0.03, 'g%d' % j, m, 0.6, 'gtr'))
            continue
        for h in (4, 12):                                   # the chick
            for j, m in enumerate(GTR[c]):
                ev.append((t + h * S16 + j * 0.008, 'g%d' % j, m, 0.7, 'gtr'))
        if sec in ('A', "A'"):                              # a forward roll in sixteenths
            v = BANJO[c]
            for k, s in enumerate([0, 1, 3, 0, 1, 3, 0, 3, 1, 2, 3, 1, 2, 3, 1, 3]):
                ev.append((t + k * S16, 'j%d' % s, v[s], 0.85 if k % 4 == 0 else 0.6, 'banjo'))
    return sorted(ev)


PLUCKS = plucks()
_ring_cap = {'bass': 1.3, 'gtr': 0.3, 'banjo': 0.45}
PRING = [min(r, _ring_cap[e[4]]) for e, r in zip(PLUCKS, S.ring_out(PLUCKS, 1.3))]
for (t, s, m, v, kind), r in zip(PLUCKS, PRING):
    S.harm(t, r, m, kind)
for lb, m in JAW.items():
    S.harm(lb * BAR + (0 if lb != 25 else 8 * S16), 0.9, m, 'jaw harp')

S.check()


def render(wav=None):
    hm, fd, bj, gt, bs, jw, wb, sh = (tl.bus() for _ in range(8))
    for i, (t0, notes) in enumerate(S.phrases(HARMONICA)):
        S.place(hm, t0, reed_phrase(notes, i, 'harmonica'), pan=-0.08, gain=0.075)
    for i, (t0, notes) in enumerate(S.phrases(FIDDLE)):
        S.place(fd, t0, bowed_phrase(notes, i), pan=0.12, gain=0.085)
    for (t, s, m, v, kind), r in zip(PLUCKS, PRING):
        seed = int(t * 1000) + m
        if kind == 'bass':
            S.place(bs, t, string(m, r, v, seed, a=0.55, t60=2.0, tilt=1.4, noise=0.05, comb=0.22, top=2400, rel=0.05),
                    gain=0.28)
        elif kind == 'gtr':
            S.place(gt, t, string(m, r, v, seed, a=0.85, t60=1.5, tilt=0.9, noise=0.25, comb=0.15, top=7000, rel=0.03),
                    pan=0.3, gain=0.14)
        else:
            S.place(bj, t, string(m, r, v, seed, a=0.95, t60=0.9, tilt=0.6, noise=0.3, comb=0.08, top=10000, rel=0.03),
                    pan=-0.35, gain=0.13)
    for lb, m in JAW.items():
        S.place(jw, lb * BAR + (0 if lb != 25 else 8 * S16), jaw_harp(m, 0.9, lb), pan=0.2, gain=0.09)
    for lb in range(tl.bars):
        sec = S.section(lb)
        if sec != 'intro':                                  # clip-clop
            for k, pos in enumerate((0, 3, 4, 7, 8, 11, 12, 15)):
                S.place(wb, lb * BAR + pos * S16, woodblock(lb * 16 + pos, 1050 if k % 2 == 0 else 1350,
                                                            1.0 if pos % 4 == 0 else 0.7), pan=0.4, gain=0.06)
        if sec == 'B':
            for pos in range(0, 16, 2):
                acc = 1.0 if pos % 4 == 2 else 0.6
                S.place(sh, lb * BAR + pos * S16, shaker(lb * 16 + pos, acc), pan=-0.4, gain=0.08 * acc)
    bjx = body(bj.x, [(600, 1.5, 0.4), (2200, 1.5, 0.3)], 120)
    gtx = body(gt.x, [(110, 2.2, 0.4), (230, 2.5, 0.3)], 80)
    hmx = hm.x + pingpong(hm.x, 3 * S16, 0.22, 3, 3500) * 0.35
    stems = dict(harmonica=hmx, fiddle=fd.x, banjo=bjx, guitar=gtx, bass=bs.x, jaw=jw.x, woodblock=wb.x, shaker=sh.x)
    send = dict(harmonica=0.3, fiddle=0.35, banjo=0.2, guitar=0.2, bass=0.05, jaw=0.2, woodblock=0.15, shaker=0.2)
    return S.finish(stems, send, NAME, rt60=1.8, dark=8000, wet=0.4, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
