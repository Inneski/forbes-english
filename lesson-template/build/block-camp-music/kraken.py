#!/usr/bin/env python3
"""Block Camp soundtrack "Black Tide" (The Kraken: A Tale of the Deep RPG).

Innes, 2026-10-05: "add soundtracks to the RPGs". The game is a West
Highland sea story in the Present Perfect: a fishing village, a black tide,
and something vast that has risen from the deep. So: the idiom of a
Highland sea score - a low whistle carrying a slow air over a clarsach
(the Highland harp), a pipe drone and the surf, gulls; then the deep wakes:
a solo fiddle high and wide, a French horn's long line under it, a choir,
timpani and a bodhran, and a sub-bass swell that is the thing itself. An
original piece in that idiom: no melody or progression is taken from any
film or record.

E minor (aeolian), 72 BPM, 4/4 (a sixteenth is exactly 10000 samples, a bar
3.333 s). One chord a bar:

  intro  Em | Em | D  | Em                    bars 0-3    surf, gulls, the drone; the deep swells
  A      Em | G  | D  | Em | C | G | D | D    bars 4-11   the air on the low whistle, the harp,
                                                          low strings, the bodhran walking
  B      C  | D  | Em | Bm | C | D | Em | Em  bars 12-19  the deep: fiddle, horn, choir "ah",
                                                          timpani, the swell
  outro  C  | D  | Em | Em                    bars 20-23  the whistle comes home to E; the drone

The air (whistle, bar 4): E4 G4 B4~ A4 | B4~ A4 G4 | F#4 A4 D5~ B4 | B4 G4 E4~.

rpgkit.Song.check() proves the harmony at import (see rpgkit.py). The
bodhran and the swell are tuned to each bar's root.

Instruments (rpgkit.py): low whistle = flute_phrase(low=True); clarsach =
Karplus-Strong, bright wire-ish strings through a small box; fiddle =
bowed_phrase; horn = brass_phrase('horn'); strings = pad_note('strings');
drone = pad_note('drone'); choir = choir_note('ah'); bodhran = frame_drum;
timpani; swell = a low sine and its octave; surf; gulls.
24 bars = 80 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/kraken.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from synthkit import Timeline, SR, hz, rng, adsr, lp
from rpgkit import (Song, string, body, flute_phrase, bowed_phrase, brass_phrase, choir_note, pad_note,
                    frame_drum, timp, surf, bird, pingpong)

NAME = 'kraken'
tl = Timeline(bpm=72, bars=24)
CH = {'Em': {4, 7, 11}, 'G': {7, 11, 2}, 'D': {2, 6, 9}, 'C': {0, 4, 7}, 'Bm': {11, 2, 6}}
CHORDS = (['Em', 'Em', 'D', 'Em'] +
          ['Em', 'G', 'D', 'Em', 'C', 'G', 'D', 'D'] +
          ['C', 'D', 'Em', 'Bm', 'C', 'D', 'Em', 'Em'] +
          ['C', 'D', 'Em', 'Em'])
S = Song(tl, CH, CHORDS, [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ('outro', 20, 24)])
BAR, BEAT, S16, LOOP = S.BAR, S.BEAT, S.S16, S.LOOP

ROOT = {'Em': 40, 'G': 43, 'D': 38, 'C': 36, 'Bm': 35}
HARP = {'Em': [40, 47, 52, 55, 59, 64], 'G': [43, 50, 55, 59, 62, 67], 'D': [38, 45, 50, 57, 62, 66],
        'C': [36, 43, 48, 55, 60, 64], 'Bm': [35, 42, 47, 54, 59, 62]}
STRINGS = {'Em': [40, 47, 55, 59], 'G': [43, 50, 55, 59], 'D': [38, 45, 54, 57], 'C': [36, 43, 52, 55],
           'Bm': [35, 42, 50, 54]}
CHOIR = {'Em': [64, 67, 71], 'G': [62, 67, 71], 'D': [62, 66, 69], 'C': [64, 67, 72], 'Bm': [62, 66, 71]}
TIMP = {'Em': 40, 'G': 43, 'D': 38, 'C': 36, 'Bm': 47}

WHISTLE = {
    4: [(64, 4), (67, 4), (71, 6), (69, 2)],                # Em  E G B~ A
    5: [(71, 6), (69, 2), (67, 8)],                         # G   B~ A G~
    6: [(66, 4), (69, 4), (74, 6), (71, 2)],                # D   F# A D~ B
    7: [(71, 4), (67, 4), (64, 8)],                         # Em  B G E~
    8: [(64, 4), (67, 4), (72, 6), (74, 2)],                # C   E G C~ D
    9: [(71, 6), (69, 2), (67, 4), (62, 4)],                # G   B~ A G D
    10: [(66, 6), (64, 2), (62, 8)],                        # D   F#~ E D~
    11: [(69, 8), (66, 4), (62, 4)],                        # D   A~ F# D
    20: [(72, 8), (67, 8)],                                 # C   C~ G~
    21: [(69, 8), (66, 8)],                                 # D   A~ F#~
    22: [(64, 16)],                                         # Em  E~
}
FIDDLE = {
    12: [(76, 8), (79, 4), (84, 4)],                        # C   E~ G C
    13: [(81, 8), (78, 4), (74, 4)],                        # D   A~ F# D
    14: [(79, 6), (81, 2), (76, 8)],                        # Em  G~ A E~
    15: [(78, 8), (74, 4), (71, 4)],                        # Bm  F#~ D B
    16: [(79, 4), (76, 4), (72, 4), (76, 4)],               # C   G E C E
    17: [(78, 6), (76, 2), (74, 8)],                        # D   F#~ E D~
    18: [(71, 4), (76, 4), (79, 8)],                        # Em  B E G~
    19: [(83, 12), (79, 4)],                                # Em  B~ G
}
HORN = {
    12: [(64, 16)], 13: [(66, 16)], 14: [(67, 16)], 15: [(66, 16)],
    16: [(64, 16)], 17: [(62, 8), (66, 8)], 18: [(64, 16)], 19: [(59, 16)],
}
S.tune(WHISTLE, 'whistle')
S.tune(FIDDLE, 'fiddle')
S.tune(HORN, 'horn')

PAD = S.held(lambda lb: STRINGS[S.chord(lb)] if S.section(lb) != 'intro' else None, 'strings')
DRONE = S.held(lambda lb: [ROOT[S.chord(lb)], ROOT[S.chord(lb)] + 7] if S.section(lb) in ('intro', 'outro') else None, 'drone')
CHOIRN = S.held(lambda lb: CHOIR[S.chord(lb)] if S.section(lb) == 'B' else None, 'choir')
SWELL = S.held(lambda lb: [ROOT[S.chord(lb)] - 12] if lb in (0, 1, 3, 12, 13, 14, 18, 19) else None, 'swell')

ARP = [0, 1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5]                  # twelve plucks a bar: a lilting triplet feel


def harp_plucks():
    ev = []
    for lb in range(tl.bars):
        sec, v = S.section(lb), HARP[S.chord(lb)]
        t = lb * BAR
        if sec in ('A', 'outro'):
            for k, s in enumerate(ARP):
                ev.append((t + k * BAR / 12, s, v[s], 0.9 if k % 3 == 0 else 0.6))
        elif sec == 'B':
            for j, s in enumerate(range(6)):
                ev.append((t + j * 0.04, s, v[s], 0.75))
    return sorted(ev)


HARPS = harp_plucks()
HRING = S.ring_out(HARPS, 3.0)
for (t, s, m, v), r in zip(HARPS, HRING):
    S.harm(t, r, m, 'harp')

BODHRAN = []                                                # (t, midi or None for a rim tap, vel)
for lb in range(tl.bars):
    sec = S.section(lb)
    if sec in ('A', 'B'):
        r = ROOT[S.chord(lb)]
        pat = ((0, 1.0), (6, 0.55), (8, 0.8), (14, 0.5)) if sec == 'A' else \
              ((0, 1.0), (3, 0.5), (6, 0.7), (8, 0.9), (11, 0.5), (12, 0.6), (14, 0.7))
        for pos, v in pat:
            BODHRAN.append((lb * BAR + pos * S16, r + 12, v))
        for pos in (2, 4, 10):
            BODHRAN.append((lb * BAR + pos * S16, None, 0.35))
for t, m, v in BODHRAN:
    if m:
        S.harm(t, 0.3, m, 'bodhran')
TIMPS = [(lb * BAR, TIMP[S.chord(lb)]) for lb in range(12, 20)] + [(19 * BAR + 2 * BEAT, 40)]
for t, m in TIMPS:
    S.harm(t, min(BAR, (np.floor(t / BAR) + 1) * BAR - t), m, 'timpani')

S.check()


def swell(m, dur, seed):
    n = int((dur + 0.6) * SR); t = np.arange(n) / SR
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.5 * np.sin(4 * np.pi * f * t) + 0.15 * np.sin(6 * np.pi * f * t)
    env = np.sin(np.pi * np.clip(t / (dur + 0.5), 0, 1)) ** 1.5
    return x * env


def render(wav=None):
    wh, fd, hn, hp_, st, dr, cho, sw, bo, ti, sea, gull = (tl.bus() for _ in range(12))
    for i, (t0, notes) in enumerate(S.phrases(WHISTLE)):
        S.place(wh, t0, flute_phrase(notes, i, breath=0.7, low=True, vib_c=14), pan=-0.1, gain=0.095)
    for i, (t0, notes) in enumerate(S.phrases(FIDDLE)):
        S.place(fd, t0, bowed_phrase(notes, i), pan=0.15, gain=0.1)
    for i, (t0, notes) in enumerate(S.phrases(HORN)):
        S.place(hn, t0, brass_phrase(notes, i, 'horn'), pan=-0.25, gain=0.045)
    for (t, s, m, v), r in zip(HARPS, HRING):
        S.place(hp_, t, string(m, r, v, int(t * 1000) + s, a=0.88, t60=4.5, tilt=0.85, noise=0.2, comb=0.14, top=8500),
                pan=0.35 - 0.12 * s, gain=0.15)
    for t, d, m, k in PAD:
        S.place(st, t, pad_note(m, d - 0.05, int(t * 10) + k, 'strings', attack=1.0, release=0.6),
                pan=(-0.3, 0.3, -0.15, 0.15)[k], gain=0.065)
    for t, d, m, k in DRONE:
        S.place(dr, t, pad_note(m, d - 0.05, int(t * 10) + k, 'drone', release=0.5), pan=(-0.2, 0.2)[k], gain=0.03)
    for t, d, m, k in CHOIRN:
        S.place(cho, t, choir_note(m, d - 0.05, 'ah', int(t * 10) + k), pan=(-0.4, 0.0, 0.4)[k], gain=0.04)
    for j, (t, d, m, k) in enumerate(SWELL):
        S.place(sw, t, swell(m, d, j), gain=0.16)
    for i, (t, m, v) in enumerate(BODHRAN):
        S.place(bo, t, frame_drum(i, f0=hz(m) if m else 110, vel=v, open_=m is not None), pan=0.1, gain=0.3)
    for i, (t, m) in enumerate(TIMPS):
        S.place(ti, t, timp(m, 0.85, i, min(BAR, (np.floor(t / BAR) + 1) * BAR - t)), pan=-0.15, gain=0.3)
    for lb in range(tl.bars):
        sec = S.section(lb)
        if sec in ('intro', 'outro') or lb % 2 == 0:
            S.place(sea, lb * BAR - 0.3 * BAR, surf(lb, 1.6 * BAR), gain=0.09 if sec in ('intro', 'outro') else 0.045)
        if sec in ('intro', 'outro'):
            r = rng('gulls', lb)
            for q in sorted(r.choice(8, 2, replace=False)):
                S.place(gull, lb * BAR + q * 2 * S16 + r.uniform(0, 0.1), bird(lb * 10 + int(q), 'gull'),
                        pan=r.uniform(-0.7, 0.7), gain=0.02)
    hx = body(hp_.x, [(400, 2.5, 0.35), (1800, 2, 0.2)], 70)
    whx = wh.x + pingpong(wh.x, 3 * S16, 0.3, 4, 3200) * 0.5
    stems = dict(whistle=whx, fiddle=fd.x, horn=hn.x, harp=hx, strings=st.x, drone=dr.x, choir=cho.x, swell=sw.x,
                 bodhran=bo.x, timpani=ti.x, surf=sea.x, gulls=gull.x)
    send = dict(whistle=0.5, fiddle=0.45, horn=0.4, harp=0.35, strings=0.35, drone=0.3, choir=0.5, swell=0.1,
                bodhran=0.25, timpani=0.35, surf=0.2, gulls=0.5)
    return S.finish(stems, send, NAME, rt60=3.2, dark=7500, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
