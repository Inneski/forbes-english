#!/usr/bin/env python3
"""Sailing the Seas: calm arcade music, a seamless loop.

    py lesson-template/build/sailing_music.py   # writes sailing-the-seas-of-grammar/music.m4a

Innes, 2026-10-01: "just make some arcade style calming music" (in place of
the sea, gulls and foghorn). An original chiptune in D major at 80 (a beat is exactly 36000 samples, so
every repeat lands on the same samples): a pulse
lead with delayed vibrato and a dotted echo, a thin 12.5% pulse arpeggio, a
triangle bass, and hats you can barely hear. 16 bars:

    A   Dmaj7  Bm7   Gmaj7  Asus4   Dmaj7  F#m7  Gmaj7  Asus4
    B   Bm7    Gmaj7 Dmaj7  A       Em7    Gmaj7 Asus4  Asus4

Rendered periodically with the Block Camp synth kit (synthkit.py): every
event is placed from bar mod 16, so echoes and reverb cross the seam as on a
real repeat, and the seam is measured. Played by block-camp/camp-music.js;
build_sailing.py reads the loop points from music.json.
"""
import json, os, subprocess, sys
import numpy as np
import imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'block-camp-music'))
import synthkit as K                                     # noqa: E402

SR, PAD = K.SR, K.PAD
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
DST = os.path.join(ROOT, 'sailing-the-seas-of-grammar', 'music.m4a')
BARS = 16
tl = K.Timeline(80, BARS, pre=2, post=1, tail=5.0)
B = tl.beat

CH = {'Dmaj7': [50, 62, 66, 69, 73], 'Bm7': [47, 59, 62, 66, 69], 'Gmaj7': [43, 59, 62, 66, 67],
      'Asus4': [45, 57, 62, 64, 69], 'F#m7': [42, 61, 64, 66, 69], 'A': [45, 57, 61, 64, 69],
      'Em7': [40, 59, 62, 64, 67]}
PROG = ['Dmaj7', 'Bm7', 'Gmaj7', 'Asus4', 'Dmaj7', 'F#m7', 'Gmaj7', 'Asus4',
        'Bm7', 'Gmaj7', 'Dmaj7', 'A', 'Em7', 'Gmaj7', 'Asus4', 'Asus4']   # the held D would rub a C#
D5, E5, Fs5, G5, A5, B5, Cs5, D6, A4, B4 = 74, 76, 78, 79, 81, 83, 73, 86, 69, 71
_ = None
TUNE = [
    [(Fs5, 1.5), (E5, .5), (D5, 1), (A4, 1)], [(B4, 1.5), (D5, .5), (Fs5, 2)],
    [(G5, 1), (Fs5, 1), (D5, 1), (B4, 1)], [(A4, 3), (_, 1)],
    [(Fs5, 1.5), (A5, .5), (B5, 1), (A5, 1)], [(Fs5, 1), (E5, 1), (Cs5, 1), (E5, 1)],
    [(D5, 1), (B4, 1), (D5, 1), (G5, 1)], [(E5, 3), (_, 1)],
    [(D6, 1.5), (B5, .5), (A5, 1), (Fs5, 1)], [(G5, 1.5), (Fs5, .5), (D5, 2)],
    [(Fs5, 1), (A5, 1), (D6, 1), (A5, 1)], [(B5, 2), (A5, 2)],
    [(G5, 1.5), (Fs5, .5), (E5, 1), (B4, 1)], [(D5, 1), (Fs5, 1), (B5, 1), (A5, 1)],
    [(A5, 2), (G5, 1), (E5, 1)], [(D5, 3), (_, 1)],
]


def lead(m, dur):
    n = int((dur + 0.25) * SR); t = np.arange(n) / SR
    vib = 1 + 0.006 * np.sin(2 * np.pi * 5.2 * t) * np.clip((t - 0.18) / 0.25, 0, 1)
    x = K.pulse(K.hz(m) * vib, n, 0.25) * 0.6 + K.tri(K.hz(m) * vib, n) * 0.5
    env = K.adsr(n, 0.008, 0.25, 0.7, 0.18, dur * 0.92)
    return K.lp(x * env, 3600)


def arp(m, dur):
    n = int((dur + 0.08) * SR)
    return K.lp(K.pulse(K.hz(m), n, 0.125) * K.perc(n, 0.003, 0.16), 3000)


def bass(m, dur):
    n = int((dur + 0.1) * SR)
    return K.tri(K.hz(m), n) * K.adsr(n, 0.01, 0.3, 0.8, 0.08, dur * 0.9)


def hat(seed):
    n = int(0.05 * SR)
    return K.hp(K.rng('hat', seed).standard_normal(n), 7000) * K.perc(n, 0.001, 0.012)


lead_bus, arp_bus, low_bus = tl.bus(), tl.bus(), tl.bus()
for bar in tl.bars_range():
    b = bar % BARS
    t0 = bar * tl.bar
    ch = CH[PROG[b]]
    t = t0
    for m, beats in TUNE[b]:
        if m is not None:
            lead_bus.add(t, lead(m, beats * B), 0.0, 0.42)
        t += beats * B
    up = ch[1:] + [ch[1] + 12, ch[2] + 12, ch[3] + 12]   # up and down the chord in eighths
    pat = up[:4] + up[4:6] + up[2:4][::-1]
    for k, m in enumerate(pat):
        arp_bus.add(t0 + k * B / 2, arp(m + 12, B / 2), -0.45 if k % 2 else 0.45, 0.12)
    low_bus.add(t0, bass(ch[0] - 12 + 12, 2 * B), 0, 0.5)
    low_bus.add(t0 + 2 * B, bass(ch[0] + (7 if b % 2 else 12) - 12, 2 * B), 0, 0.42)
    for k in range(4):
        low_bus.add(t0 + k * B + B / 2, hat((b, k)), 0.3 if k % 2 else -0.3, 0.05)

lx = lead_bus.x
echo = K.pingpong(lx, 0.75 * B, 0.38, 6, 2500)           # a dotted-eighth echo, darkening
ir = K.make_ir(2.2, dark=3500, seed=3)
mix = lx + echo * 0.45 + arp_bus.x + low_bus.x
mix = mix + K.reverb(lx * 0.6 + arp_bus.x, ir) * 0.25

# out: the loop with PAD seconds of real continuation either side (an AAC
# encoder's priming then never lands on the seam), the seam measured.
mix = K.hp1(mix, 30)
a, b = tl.smp(-PAD), tl.smp(tl.loop + PAD)
out = mix[a:b]
out = out * (10 ** (-18 / 20) / np.sqrt(np.mean(out ** 2)))
out = 0.95 * np.tanh(out / 0.95)
i0, i1, k = tl.smp(0) - a, tl.smp(tl.loop) - a, int(PAD * SR)
seam = float(np.abs(out[i1:i1 + k] - out[i0:i0 + k]).max())
assert seam < 1e-3, 'the loop is not periodic (%.4f)' % seam
pcm = (np.clip(out, -1, 1) * 32767).astype('<i2').tobytes()
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-',
                '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', DST], input=pcm, check=True)
loop = [PAD, round(PAD + tl.loop, 6)]
json.dump({'loop': loop}, open(os.path.join(os.path.dirname(DST), 'music.json'), 'w'), indent=1)
print('music.m4a: %.1f s, loop %g .. %g, seam %.5f, peak %.2f, %d KB'
      % (len(out) / SR, loop[0], loop[1], seam, np.abs(out).max(), os.path.getsize(DST) // 1024))
