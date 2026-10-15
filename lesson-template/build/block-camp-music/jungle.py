#!/usr/bin/env python3
"""Block Camp soundtrack "Canopy" (Welcome to the Jungle RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is a voxel
jungle in the Past Continuous and the Past Simple: travellers who were
crossing the forest when something happened. So: the idiom of a jungle
adventure score - a marimba ostinato running in sixteenths, slit log drums
talking under it, shakers, a wooden flute carrying the tune, a French horn's
call when the adventure opens up, low strings, big frame drums, and the
forest itself: cicadas and birds. An original piece in that idiom: no
melody or progression is taken from any film or record.

E minor, 120 BPM, 4/4 (a sixteenth is exactly 6000 samples, a bar 2 s). One
chord a bar:

  intro  Em | Em | C  | D                     bars 0-3    cicadas, birds, the log drums; the
                                                          marimba and the flute come in
  A      Em | G  | C  | D  | Em | G | C | B   bars 4-11   the flute's tune over the marimba
  B      C  | D  | G  | Em | C  | D | B | B   bars 12-19  the horn's call, strings, big drums
  A'     Em | G  | C  | D  | Em | G | C | B   bars 20-27  the tune again
  break  Em | Em | C  | D                     bars 28-31  drums, marimba and the forest

The tune (flute, bar 4): B4 E5 G5~ A5 | B5~ A5 G5~ | E5 G5 C6~ | A5 F#5 D5~.

rpgkit.Song.check() proves the harmony at import (see rpgkit.py). The log
drums, the kick and the frame drums are tuned to each bar's chord.

Instruments (rpgkit.py): flute = flute_phrase; horn = brass_phrase('horn');
marimba = mallet('marimba'), damped when its note leaves the chord;
log drums; strings = pad_note('strings'); kick and frame drums; shakers;
cicadas; birds.
32 bars = 64 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/jungle.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from synthkit import Timeline, SR, hz, rng
from rpgkit import (Song, mallet, flute_phrase, brass_phrase, pad_note, log_drum, kick, frame_drum, shaker,
                    insects, bird, pingpong)

NAME = 'welcome-to-the-jungle'
tl = Timeline(bpm=120, bars=32)
CH = {'Em': {4, 7, 11}, 'G': {7, 11, 2}, 'C': {0, 4, 7}, 'D': {2, 6, 9}, 'B': {11, 3, 6}}
_A = ['Em', 'G', 'C', 'D', 'Em', 'G', 'C', 'B']
CHORDS = ['Em', 'Em', 'C', 'D'] + _A + ['C', 'D', 'G', 'Em', 'C', 'D', 'B', 'B'] + _A + ['Em', 'Em', 'C', 'D']
S = Song(tl, CH, CHORDS, [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ("A'", 20, 28), ('break', 28, 32)])
BAR, BEAT, S16, LOOP = S.BAR, S.BEAT, S.S16, S.LOOP

ROOT = {'Em': 52, 'G': 55, 'C': 48, 'D': 50, 'B': 47}
FIFTH = {'Em': 47, 'G': 50, 'C': 55, 'D': 45, 'B': 54}
KICK = {'Em': 28, 'G': 31, 'C': 36, 'D': 38, 'B': 35}
MARIMBA = {'Em': [52, 59, 64, 67, 71], 'G': [55, 59, 62, 67, 71], 'C': [52, 55, 60, 64, 67],
           'D': [50, 57, 62, 66, 69], 'B': [51, 54, 59, 63, 66]}
STRINGS = {'C': [48, 55, 64], 'D': [50, 57, 66], 'G': [43, 55, 59], 'Em': [40, 55, 59], 'B': [47, 54, 63]}

TUNE = [
    [(71, 4), (76, 4), (79, 6), (81, 2)],                   # Em  B E G~ A
    [(83, 6), (81, 2), (79, 8)],                            # G   B~ A G~
    [(76, 4), (79, 4), (84, 8)],                            # C   E G C~
    [(81, 4), (78, 4), (74, 8)],                            # D   A F# D~
    [(76, 4), (79, 4), (83, 6), (81, 2)],                   # Em  E G B~ A
    [(79, 6), (76, 2), (74, 8)],                            # G   G~ E D~
    [(72, 4), (76, 4), (79, 8)],                            # C   C E G~
    [(78, 6), (75, 2), (71, 8)],                            # B   F#~ D# B~
]
FLUTE = {2: [(0, 8), (79, 8)], 3: [(78, 16)]}
FLUTE.update({4 + k: row for k, row in enumerate(TUNE)})
FLUTE.update({20 + k: row for k, row in enumerate(TUNE)})
HORN = {
    12: [(67, 8), (72, 8)],                                 # C   G~ C~
    13: [(69, 8), (74, 8)],                                 # D   A~ D~
    14: [(71, 6), (74, 2), (79, 8)],                        # G   B~ D G~
    15: [(76, 12), (71, 4)],                                # Em  E~ B
    16: [(72, 8), (76, 4), (79, 4)],                        # C   C~ E G
    17: [(78, 8), (74, 4), (69, 4)],                        # D   F#~ D A
    18: [(71, 8), (75, 8)],                                 # B   B~ D#~
    19: [(78, 16)],                                         # B   F#~
}
S.tune(FLUTE, 'flute')
S.tune(HORN, 'horn')

PAT = [0, 2, 1, 3, 2, 4, 3, 2, 0, 2, 1, 3, 2, 4, 3, 1]


def marimba_notes():
    ev = []
    for lb in range(tl.bars):
        if lb < 2:
            continue
        v, t = MARIMBA[S.chord(lb)], lb * BAR
        for k, i in enumerate(PAT):
            ev.append((t + k * S16, i, v[i], 1.0 if k % 4 == 0 else 0.65))
    return sorted(ev)


MAR = marimba_notes()
MRING = [min(r, 0.45) for r in S.ring_out(MAR, 0.45)]
for (t, s, m, v), r in zip(MAR, MRING):
    S.harm(t, r, m, 'marimba')

LOGS = []                                                   # (t, midi, vel)
for lb in range(tl.bars):
    c, t = S.chord(lb), lb * BAR
    for pos, which, v in ((0, 'r', 1.0), (3, 'r', 0.6), (6, 'f', 0.8), (10, 'r', 0.7), (12, 'f', 0.6), (14, 'r', 0.5)):
        LOGS.append((t + pos * S16, ROOT[c] if which == 'r' else FIFTH[c], v))
def to_bar_end(t, d):
    """A drum's ring, stopped at the barline (the render damps it there too)."""
    return min(d, (int(t / BAR + 1e-9) + 1) * BAR - t)


for t, m, v in LOGS:
    S.harm(t, to_bar_end(t, 0.3), m, 'log drum')

KICKS = []
for lb in range(tl.bars):
    if S.section(lb) != 'intro':
        for pos in (0, 6, 8, 11) if S.section(lb) != 'break' else (0, 8):
            KICKS.append((lb * BAR + pos * S16, KICK[S.chord(lb)]))
for t, m in KICKS:
    S.harm(t, to_bar_end(t, 0.25), m, 'kick')
DRUMS = [(lb * BAR + pos * S16, ROOT[S.chord(lb)] - 12, v)
         for lb in range(12, 20) for pos, v in ((0, 1.0), (4, 0.6), (8, 0.9), (10, 0.5), (12, 0.7), (14, 0.6))]
for t, m, v in DRUMS:
    S.harm(t, to_bar_end(t, 0.3), m, 'frame drum')
PAD = S.held(lambda lb: STRINGS[S.chord(lb)] if S.section(lb) == 'B' else None, 'strings')

S.check()


def damp(sig, d, fade=0.02):
    n = int((d + fade) * SR)
    sig = sig[:n].copy()
    k = int(fade * SR)
    sig[-k:] *= np.linspace(1, 0, k)
    return sig


def render(wav=None):
    fl, hn, mr, lg, st, kk, dr, sh, fo = (tl.bus() for _ in range(9))
    for i, (t0, notes) in enumerate(S.phrases(FLUTE)):
        S.place(fl, t0, flute_phrase(notes, i, breath=0.75, vib_c=16), pan=-0.1, gain=0.08)
    for i, (t0, notes) in enumerate(S.phrases(HORN)):
        S.place(hn, t0, brass_phrase(notes, i, 'horn'), pan=0.15, gain=0.065)
    for (t, s, m, v), r in zip(MAR, MRING):
        S.place(mr, t, mallet(m, int(t * 1000), 'marimba', v, ring=r), pan=-0.3 + 0.15 * s, gain=0.09)
    for i, (t, m, v) in enumerate(LOGS):
        S.place(lg, t, damp(log_drum(m, i, v), to_bar_end(t, 0.3)), pan=0.35 if m == ROOT[S.chord_at(t)] else 0.5, gain=0.12)
    for t, d, m, k in PAD:
        S.place(st, t, pad_note(m, d - 0.05, int(t * 10) + k, 'strings', attack=0.4), pan=(-0.3, 0.0, 0.3)[k],
                gain=0.06)
    for i, (t, m) in enumerate(KICKS):
        S.place(kk, t, damp(kick(i, 0.9, hz(m)), to_bar_end(t, 0.25)), gain=0.3)
    for i, (t, m, v) in enumerate(DRUMS):
        S.place(dr, t, damp(frame_drum(i, hz(m), v), to_bar_end(t, 0.3)), pan=(-0.3, 0.3)[i % 2], gain=0.25)
    for lb in range(tl.bars):
        sec, t = S.section(lb), lb * BAR
        if sec in ('A', "A'", 'break'):
            for pos in range(16):
                acc = 1.0 if pos % 4 == 2 else 0.55
                S.place(sh, t + pos * S16, shaker(lb * 16 + pos, acc), pan=0.4 if pos % 2 else -0.4, gain=0.06 * acc)
        if sec in ('intro', 'break') and lb % 2 == 0:
            S.place(fo, t - 0.2 * BAR, insects(lb, 2.4 * BAR)[:, None].repeat(2, 1) * [1.0, 0.7], gain=0.03)
        r = rng('birds', lb)
        for q in sorted(r.choice(8, 2 if sec in ('intro', 'break') else 1, replace=False)):
            S.place(fo, t + q * 2 * S16 + r.uniform(0, 0.1), bird(lb * 10 + int(q), 'chirp' if r.random() < 0.7 else 'trill'),
                    pan=r.uniform(-0.8, 0.8), gain=0.025)
    flx = fl.x + pingpong(fl.x, 3 * S16, 0.3, 4, 4000) * 0.45
    stems = dict(flute=flx, horn=hn.x, marimba=mr.x, logs=lg.x, strings=st.x, kick=kk.x, drums=dr.x, shakers=sh.x,
                 forest=fo.x)
    send = dict(flute=0.45, horn=0.4, marimba=0.25, logs=0.2, strings=0.35, kick=0.05, drums=0.25, shakers=0.2,
                forest=0.4)
    return S.finish(stems, send, NAME, rt60=2.4, dark=8000, wet=0.45, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
