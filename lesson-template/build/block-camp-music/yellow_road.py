#!/usr/bin/env python3
"""Block Camp soundtrack "Yellow Road" (The Lost Yellow Road RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is Oz in a
block-built world, in the Past Continuous: a yellow road that has gone
missing, and travellers who were doing something when it happened. So: the
idiom of a storybook march - a celesta tune skipping along the bricks, a
clarinet for the travellers' song, a tuba oompah, pizzicato strings on the
off-beats, brushed snare, woodblock footsteps, a triangle, and a piccolo
an octave over the tune when it comes round again. An original piece in
that idiom: no melody or progression is taken from any film or record.

F major, 100 BPM, 4/4 (a sixteenth is exactly 7200 samples, a bar 2.4 s).
One chord a bar:

  intro  F  | F | C  | C7                     bars 0-3    the celesta's call, the oompah starts
  A      F  | Dm| Gm | C7 | F  | Bb | C7 | F  bars 4-11   the celesta tune, woodblock steps
  B      Bb | F | Gm | C  | Am | Dm | G7 | C7 bars 12-19  the clarinet's song
  A'     F  | Dm| Gm | C7 | F  | Bb | C7 | F  bars 20-27  the tune again, piccolo on top
  tag    Bb | F | C  | C7                     bars 28-31  the clarinet walks it home

The tune (celesta, bar 4): C5 F5 A5 G5 F5 | D5~ C5 A4~ | Bb4 D5 G5~ F5 | E5~ D5 C5~.

rpgkit.Song.check() proves the harmony at import (see rpgkit.py). The
celesta's notes are damped at their written length so what is checked is
what sounds; the triangle (on A) is struck only over F.

Instruments (rpgkit.py): celesta = mallet('celesta'); clarinet =
reed_phrase('clarinet'); piccolo = flute_phrase an octave up; tuba =
brass_phrase('tuba'); pizzicato = Karplus-Strong, short and soft; brushed
snare; woodblocks; triangle.
32 bars = 76.8 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/yellow_road.py [--wav preview.wav] [--stems]
"""
import sys
from synthkit import Timeline
from rpgkit import (Song, string, body, mallet, reed_phrase, flute_phrase, brass_phrase, snare, woodblock, triangle,
                    pingpong)

NAME = 'lost-yellow-road'
tl = Timeline(bpm=100, bars=32)
CH = {'F': {5, 9, 0}, 'Dm': {2, 5, 9}, 'Gm': {7, 10, 2}, 'C7': {0, 4, 7, 10}, 'C': {0, 4, 7}, 'Bb': {10, 2, 5},
      'Am': {9, 0, 4}, 'G7': {7, 11, 2, 5}}
_A = ['F', 'Dm', 'Gm', 'C7', 'F', 'Bb', 'C7', 'F']
CHORDS = (['F', 'F', 'C', 'C7'] + _A + ['Bb', 'F', 'Gm', 'C', 'Am', 'Dm', 'G7', 'C7'] + _A + ['Bb', 'F', 'C', 'C7'])
S = Song(tl, CH, CHORDS, [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ("A'", 20, 28), ('tag', 28, 32)])
BAR, BEAT, S16, LOOP = S.BAR, S.BEAT, S.S16, S.LOOP

TUBA = {'F': (41, 48), 'Dm': (38, 45), 'Gm': (43, 38), 'C7': (36, 43), 'C': (36, 43), 'Bb': (46, 41),
        'Am': (45, 40), 'G7': (43, 38)}
PIZZ = {'F': [53, 57, 60, 65], 'Dm': [50, 57, 62, 65], 'Gm': [55, 58, 62, 67], 'C7': [52, 58, 60, 64],
        'C': [52, 55, 60, 64], 'Bb': [53, 58, 62, 65], 'Am': [52, 57, 60, 64], 'G7': [53, 55, 59, 62]}

TUNE = [
    [(72, 4), (77, 4), (81, 4), (79, 2), (77, 2)],          # F   C F A G F
    [(74, 6), (72, 2), (69, 8)],                            # Dm  D~ C A~
    [(70, 4), (74, 4), (79, 6), (77, 2)],                   # Gm  Bb D G~ F
    [(76, 6), (74, 2), (72, 8)],                            # C7  E~ D C~
    [(72, 4), (77, 4), (81, 4), (84, 4)],                   # F   C F A C
    [(82, 6), (81, 2), (77, 8)],                            # Bb  Bb~ A F~
    [(79, 4), (76, 4), (72, 4), (70, 4)],                   # C7  G E C Bb
    [(69, 4), (72, 4), (77, 8)],                            # F   A C F~
]
CELESTA = {0: [(0, 8), (72, 4), (77, 4)], 1: [(81, 16)], 2: [(0, 8), (79, 8)], 3: [(76, 8), (70, 8)]}
CELESTA.update({4 + k: row for k, row in enumerate(TUNE)})
CELESTA.update({20 + k: row for k, row in enumerate(TUNE)})
PICCOLO = {20 + k: [(m + 12 if m else 0, d) for m, d in row] for k, row in enumerate(TUNE)}
CLARINET = {
    12: [(74, 6), (72, 2), (70, 8)],                        # Bb  D~ C Bb~
    13: [(69, 4), (72, 4), (77, 8)],                        # F   A C F~
    14: [(79, 6), (77, 2), (74, 8)],                        # Gm  G~ F D~
    15: [(72, 4), (76, 4), (79, 8)],                        # C   C E G~
    16: [(76, 6), (74, 2), (72, 8)],                        # Am  E~ D C~
    17: [(69, 4), (74, 4), (77, 8)],                        # Dm  A D F~
    18: [(79, 4), (77, 4), (74, 4), (71, 4)],               # G7  G F D B
    19: [(72, 4), (76, 4), (79, 4), (82, 4)],               # C7  C E G Bb
    28: [(77, 8), (74, 8)],                                 # Bb  F~ D~
    29: [(72, 8), (69, 8)],                                 # F   C~ A~
    30: [(67, 8), (72, 8)],                                 # C   G~ C~
    31: [(70, 8), (76, 8)],                                 # C7  Bb~ E~
}
S.tune(CELESTA, 'celesta')
S.tune(PICCOLO, 'piccolo')
S.tune(CLARINET, 'clarinet')

OOMPAH, PZ = [], []
for lb in range(tl.bars):
    c, t = S.chord(lb), lb * BAR
    r, f = TUBA[c]
    OOMPAH += [(t, 6 * S16, r), (t + 8 * S16, 6 * S16, f)]
    for h in (4, 12):
        for j, m in enumerate(PIZZ[c]):
            PZ.append((t + h * S16 + j * 0.006, 'p%d' % j, m, 0.8 if h == 4 else 0.7))
for t, d, m in OOMPAH:
    S.harm(t, d, m, 'tuba')
PZRING = [min(r, 0.35) for r in S.ring_out(PZ, 0.35)]
for (t, s, m, v), r in zip(PZ, PZRING):
    S.harm(t, r, m, 'pizzicato')
TRI = [lb * BAR for lb in (4, 8, 20, 24)]                   # over F only: the triangle rings on A
for t in TRI:
    S.harm(t, 1.2, 105, 'triangle')

S.check()


def render(wav=None):
    ce, pc, cl, tb, pz, sn, wb, tr = (tl.bus() for _ in range(8))
    for t, d, m, part, role, w in S.notes:
        if part == 'celesta':
            S.place(ce, t, mallet(m, int(t * 100), 'celesta', 0.9, ring=d + 0.05), pan=-0.15, gain=0.09)
    for i, (t0, notes) in enumerate(S.phrases(PICCOLO)):
        S.place(pc, t0, flute_phrase(notes, i, breath=0.3, vib_c=12), pan=0.2, gain=0.035)
    for i, (t0, notes) in enumerate(S.phrases(CLARINET)):
        S.place(cl, t0, reed_phrase(notes, i, 'clarinet'), pan=0.1, gain=0.075)
    for i, (t, d, m) in enumerate(OOMPAH):
        S.place(tb, t, brass_phrase([(0.0, d * 0.8, m)], i, 'tuba'), pan=-0.05, gain=0.13)
    for (t, s, m, v), r in zip(PZ, PZRING):
        S.place(pz, t, string(m, r, v, int(t * 1000) + m, a=0.6, t60=0.8, tilt=1.2, noise=0.08, comb=0.3, top=4000,
                              rel=0.04), pan=0.3, gain=0.17)
    for lb in range(tl.bars):
        sec, t = S.section(lb), lb * BAR
        if sec != 'intro':
            for h in (4, 12):
                S.place(sn, t + h * S16, snare(lb * 16 + h, 0.8, brush=True), pan=0.15, gain=0.09)
        if sec in ('A', "A'"):                              # footsteps on the bricks
            for pos in range(0, 16, 2):
                S.place(wb, t + pos * S16, woodblock(lb * 16 + pos, 1200 if pos % 4 == 0 else 1550,
                                                     1.0 if pos % 4 == 0 else 0.6), pan=-0.35, gain=0.045)
    for i, t in enumerate(TRI):
        S.place(tr, t, triangle(i, 105, 1.2), pan=0.45, gain=0.04)
    cex = ce.x + pingpong(ce.x, 3 * S16, 0.25, 3, 5000) * 0.35
    pzx = body(pz.x, [(250, 2, 0.3), (900, 2, 0.15)], 80)
    stems = dict(celesta=cex, piccolo=pc.x, clarinet=cl.x, tuba=tb.x, pizzicato=pzx, snare=sn.x, woodblock=wb.x,
                 triangle=tr.x)
    send = dict(celesta=0.4, piccolo=0.35, clarinet=0.35, tuba=0.1, pizzicato=0.25, snare=0.2, woodblock=0.15,
                triangle=0.4)
    return S.finish(stems, send, NAME, rt60=1.9, dark=8500, wet=0.45, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
