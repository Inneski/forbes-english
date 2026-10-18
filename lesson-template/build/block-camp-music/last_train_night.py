#!/usr/bin/env python3
"""Block Camp soundtrack "Night Line" (The Last Train Home RPG, its first track).

Innes, 2026-10-18: "last train home should have music - like vangelis". The
page already had last_train.py's driving synthwave; this is the Blade
Runner idiom instead, and the page now opens on it, with the synthwave one
press of the track switch away. The game: a cybervoxel megacity at night,
the last train dead after a gig, lockdown coming, a walk across the city
under the drones and the rain to a tower before the checkpoints seal. So:
the end-titles side of Vangelis rather than the blues - a sequenced pulse
running in sixteenths like a train on the rails, huge CS-80 brass chords
bending into pitch, a brass lead that swells and leans on its notes, a
gated snare in a vast hall, rain, a station chime, a train horn far off,
and a glass bell when the city goes quiet. An original piece in that idiom:
nothing is taken from the film's score.

F# minor (the synthwave's key, so the two tracks are one game), 68.57 BPM -
rainfall.py's tempo, a beat exactly 42000 samples, a bar 3.5 s - with the
pulse in sixteenths (0.22 s, a train's rhythm). One chord a bar:

  intro  F#m | F#m | D   | C#                       bars 0-3    rain, the chime, the horn, pads swelling
  A      F#m | D   | Bm  | C# | F#m | D  | E  | C#   bars 4-11   the pulse; the brass tune; drums from bar 8
  B      D   | E   | C#m | F#m| Bm  | D  | C#sus4 | C#  bars 12-19  the tune again, warmer, the pads at their widest
  outro  F#m | D   | Bm  | C#                       bars 20-23  drums out, the pulse filtered down, the bell

The tune (brass, bar 4): F#4 C#5 F#5~ | A5~ F#5 | F#5~ D5 B4~ | C#5~ E#5.

rpgkit.Song.check() proves the harmony at import (see rpgkit.py): the pulse,
the drone, the kick, the chime and the horn are chord tones of their bars,
the tune's long and strong notes are too, and nothing rubs a semitone.

Instruments: pads = rainfall.py's cs80() (bending in, the filter opening over
a second); drone = rainfall.py's drone(); the pulse = a polyBLEP saw and a
square an octave up through a low-pass whose cutoff rides the loop (shut in
the intro and outro, open in B), each note plucked by its own envelope; the
brass lead = rpgkit's voice engine driving two detuned saws through a filter
that opens as the note swells; the bell = rainfall.py's glass_phrase(); kick
tuned to the root, a snare in a 4.5 s hall; rain = rainfall.py's
grains; the chime = vibes; the horn = a three-note chord of reedy saws,
low-passed, drifting a few cents as it passes.
24 bars = 84 s, a seamless loop (see synthkit.py).

    py lesson-template/build/block-camp-music/last_train_night.py [--wav preview.wav] [--stems]
"""
import sys
import numpy as np
from synthkit import SR, Timeline, hz, rng, lp, lp1, hp, adsr, pingpong
from rpgkit import Song, voice_phrase, mallet, kick, snare
import rainfall
from rainfall import blep_saw, cs80, drone, glass_phrase, rain_grain, thunder, CHUNK

NAME = 'last-train-night'
BEAT = rainfall.BEAT
tl = Timeline(bpm=60 / BEAT, bars=24, pre=6, post=1)
CH = {'F#m': {6, 9, 1}, 'D': {2, 6, 9}, 'Bm': {11, 2, 6}, 'C#': {1, 5, 8}, 'E': {4, 8, 11}, 'C#m': {1, 4, 8},
      'C#sus4': {1, 6, 8}}
CHORDS = (['F#m', 'F#m', 'D', 'C#'] +
          ['F#m', 'D', 'Bm', 'C#', 'F#m', 'D', 'E', 'C#'] +
          ['D', 'E', 'C#m', 'F#m', 'Bm', 'D', 'C#sus4', 'C#'] +
          ['F#m', 'D', 'Bm', 'C#'])
S = Song(tl, CH, CHORDS, [('intro', 0, 4), ('A', 4, 12), ('B', 12, 20), ('outro', 20, 24)])
BAR, S16, LOOP = S.BAR, S.S16, S.LOOP
assert abs(S16 - rainfall.S16) < 1e-12               # glass_phrase() counts in rainfall's sixteenths

ROOT = {'F#m': 42, 'D': 38, 'Bm': 35, 'C#': 37, 'E': 40, 'C#m': 37, 'C#sus4': 37}
FIFTH = {c: ROOT[c] + 7 for c in ROOT}
PAD = {'F#m': [54, 61, 66, 69], 'D': [54, 57, 62, 66], 'Bm': [54, 59, 62, 66], 'C#': [53, 56, 61, 65],
       'E': [56, 59, 64, 68], 'C#m': [56, 61, 64, 68], 'C#sus4': [54, 56, 61, 66]}

BRASS = {
    4: [(66, 4), (73, 4), (78, 8)],                         # F#m  F# C# F#~
    5: [(81, 12), (78, 4)],                                 # D    A~ F#
    6: [(78, 6), (74, 2), (71, 8)],                         # Bm   F#~ D B~
    7: [(73, 12), (77, 4)],                                 # C#   C#~ E#
    8: [(78, 8), (81, 8)],                                  # F#m  F#~ A~
    9: [(86, 8), (81, 4), (78, 4)],                         # D    D~ A F#
    10: [(83, 8), (80, 4), (76, 4)],                        # E    B~ G# E
    11: [(77, 8), (73, 8)],                                 # C#   E#~ C#~
    12: [(69, 4), (74, 4), (78, 8)],                        # D    A D F#~
    13: [(76, 12), (71, 4)],                                # E    E~ B
    14: [(73, 8), (68, 8)],                                 # C#m  C#~ G#~
    15: [(69, 16)],                                         # F#m  A~
    16: [(66, 4), (71, 4), (74, 8)],                        # Bm   F# B D~
    17: [(78, 8), (74, 8)],                                 # D    F#~ D~
    18: [(73, 8), (66, 8)],                                 # C#sus4  C#~ F#~
    19: [(65, 16)],                                         # C#   E#~
}
BELL = {
    20: [(78, 4), (81, 4), (85, 8)],                        # F#m  F# A C#~
    21: [(81, 8), (78, 8)],                                 # D    A~ F#~
    22: [(74, 8), (78, 8)],                                 # Bm   D~ F#~
    23: [(77, 16)],                                         # C#   E#~
}
S.tune(BRASS, 'brass')
S.tune(BELL, 'bell')

PADS = S.held(lambda lb: PAD[S.chord(lb)], 'pads')
DRONE = S.held(lambda lb: [ROOT[S.chord(lb)]], 'drone')

STEP = [0, 12, 0, 7, 0, 12, 7, 12]                         # the pulse, twice a bar
PULSE = []                                                  # (t, midi, vel)
for lb in range(tl.bars):
    if lb < 2:
        continue
    r = ROOT[S.chord(lb)] + 12
    for k in range(16):
        PULSE.append((lb * BAR + k * S16, r + STEP[k % 8], 1.0 if k % 4 == 0 else 0.7))
for t, m, v in PULSE:
    S.harm(t, S16 * 0.9, m, 'pulse')

KICKS, SNARES = [], []
for lb in range(8, 20):
    for q in (0, 2):
        KICKS.append((lb * BAR + q * 4 * S16, ROOT[S.chord(lb)] - 12))
    for q in (1, 3):
        SNARES.append(lb * BAR + q * 4 * S16)
for t, m in KICKS:
    S.harm(t, 0.3, m, 'kick')
CHIME = [(0.0, 78), (0.45, 81), (0.9, 85)]                  # the station chime: F# A C#
for t, m in CHIME:
    S.harm(t, 1.6, m, 'chime')
HORN = (2 * BAR + 0.4, 2.6, [62, 66, 69])                   # far off, over the D bar
for m in HORN[2]:
    S.harm(HORN[0], HORN[1], m, 'horn')

S.check()


# ── instruments ─────────────────────────────────────────────────────────────
def brass_lead(notes, seed):
    """A CS-80 brass lead: two saws 6 cents apart and a sub-octave, bending
    up into each fresh note, the filter opening as the note swells."""
    ph, g, fr = voice_phrase(notes, f_vib=5.0, vib_c=16, glide_hz=10, scoop_c=90, attack=0.18, release=0.6, dip=0.3)
    n = len(ph)
    r = rng('brass', seed)
    x = (0.5 * blep_saw(fr * 2 ** (-6 / 1200), n, r.random()) + 0.5 * blep_saw(fr * 2 ** (6 / 1200), n, r.random())
         + 0.3 * np.sin(ph / 2))
    sw = lp1(g, 3)                                          # a slow swell: the "aftertouch"
    fc = (500 + 3800 * sw ** 1.4)[::CHUNK]
    return rainfall.tv_lp(x, fc, 1.2) * g


def pulse_note(m, v, cut, seed):
    n = int(0.35 * SR); t = np.arange(n) / SR
    r = rng('pulse', seed)
    x = 0.7 * blep_saw(hz(m), n, r.random()) + 0.3 * np.sign(np.sin(2 * np.pi * hz(m + 12) * t + r.random()))
    env = np.minimum(1, t / 0.002) * np.exp(-t / 0.09)
    fc = cut * (0.35 + 0.65 * np.exp(-t / 0.05))
    out = np.empty(n)
    for i in range(0, n, CHUNK):
        out[i:i + CHUNK] = lp(x[max(0, i - 2000):i + CHUNK], fc[i], 2.0)[-len(x[i:i + CHUNK]):]
    return out * env * v * np.clip((S16 * 0.9 - t) / 0.02 + 1, 0, 1)


def cutoff(lb):
    """The pulse's filter across the loop: shut in the intro, opening through
    A, widest in B, closing again in the outro (and so back into the intro)."""
    return {'intro': 500 + 150 * lb, 'A': 900 + 120 * (lb - 4), 'B': 2400,
            'outro': 2400 - 450 * (lb - 19)}[S.section(lb)]


def horn(ms, dur, seed):
    n = int((dur + 0.5) * SR); t = np.arange(n) / SR
    r = rng('horn', seed)
    x = np.zeros(n)
    for m in ms:
        f = hz(m) * (1 + 0.004 * np.sin(2 * np.pi * t / (dur * 2)))     # a slow drift as it passes
        x += blep_saw(f, n, r.random()) + 0.5 * blep_saw(f * 1.003, n, r.random())
    x = lp(lp(x, 1400, 0.9), 1800)
    return x * adsr(n, 0.25, 0.3, 0.85, 0.5, dur)


def render(wav=None):
    pads, drn, pul, brs, bell, kk, sn, rain, fx = (tl.bus() for _ in range(9))
    for t, d, m, k in PADS:
        S.place(pads, t, cs80(m, d - 0.1, 2400 if S.section(int(t / BAR)) == 'B' else 1700, (int(t * 10), k)),
                pan=(-0.5, 0.5, -0.2, 0.2)[k], gain=0.05)
    for t, d, m, k in DRONE:
        S.place(drn, t, drone(m, d - 0.1, int(t * 10)), gain=0.13)
    for i, (t, m, v) in enumerate(PULSE):
        S.place(pul, t, pulse_note(m, v, cutoff(int(t / BAR + 1e-9)), i), pan=0.15 * (1 if i % 2 else -1), gain=0.12)
    for i, (t0, notes) in enumerate(S.phrases(BRASS)):
        S.place(brs, t0, brass_lead(notes, i), pan=0.05, gain=0.075)
    for t0, notes in S.phrases(BELL):
        mel, pos = [], 0.0
        for t, d, m in notes:                               # back to (midi, sixteenths) for glass_phrase
            if t > pos + 1e-9:
                mel.append((0, round((t - pos) / S16)))
            mel.append((m, round(d / S16))); pos = t + d
        S.place(bell, t0, glass_phrase(mel), pan=-0.15, gain=0.09)
    for i, (t, m) in enumerate(KICKS):
        S.place(kk, t, kick(i, 1.0, hz(m))[:int(0.32 * SR)] * np.linspace(1, 0, int(0.32 * SR)) ** 0.3, gain=0.6)
    for i, t in enumerate(SNARES):
        x = snare(i, 1.0)
        S.place(sn, t, x, pan=0.0, gain=0.22)
    for lb in range(tl.bars):                             # two-bar grains a bar apart: the power sums flat
        S.place(rain, lb * BAR, rain_grain(lb), gain=0.035)
    S.place(fx, BAR + 0.5, thunder(1, 7.0), gain=0.35)
    for j, (t, m) in enumerate(CHIME):
        S.place(fx, t, mallet(m, j, 'vibes', 0.9, ring=1.6), pan=0.3, gain=0.07)
    S.place(fx, HORN[0], horn(HORN[2], HORN[1], 0), pan=-0.45, gain=0.03)
    stems = dict(pads=pads.x, drone=drn.x, pulse=pul.x + pingpong(pul.x, 3 * S16, 0.25, 3, 2500) * 0.35,
                 brass=brs.x + pingpong(brs.x, 3 * S16, 0.3, 4, 3000) * 0.5, bell=bell.x + pingpong(bell.x, 3 * S16, 0.35, 4, 4000) * 0.5,
                 kick=kk.x, snare=sn.x, rain=rain.x, fx=fx.x)
    send = dict(pads=0.55, drone=0.1, pulse=0.25, brass=0.6, bell=0.6, kick=0.1, snare=0.9, rain=0.1, fx=0.5)
    return S.finish(stems, send, NAME, rt60=4.5, dark=6500, wet=0.6, wav=wav)


if __name__ == '__main__':
    render(sys.argv[sys.argv.index('--wav') + 1] if '--wav' in sys.argv else None)
