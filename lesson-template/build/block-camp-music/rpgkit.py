"""Shared score and instruments for the RPG soundtracks composed on 2026-10-15:
fistful.py, frostbound.py, blocula.py, kraken.py, yellow_road.py, jungle.py.

The five earlier RPG tracks (last_bounty.py and the rest) each carry their own
copy of the score machinery and the instruments. These six share one: a Song
holds the changes, every note the score sounds, and the same harmony proof as
last_bounty.py's check(); the instruments are last_bounty.py's (Karplus-Strong
strings, the continuous voice engine, the choir, the bell, the timpani, the
wind) plus the families the new idioms need (flute, reed, bowed string,
brass, organ, string pad, mallets, frame and log drums, woodblock, triangle,
surf, birds, insects, thunder).

A Song's check(), the rule every track here passes before it renders:
  - every lead note on beat 1 or 3, or a beat or longer, is a tone of every
    chord it sounds over;
  - every accompaniment note ('harm': bass, pads, plucks, pitched percussion)
    is a tone of every chord it spans;
  - no two notes sounding together sit 1, 11 or 13 semitones apart, and no
    two long ones (a lead note of a beat or more, or any harm note) a
    semitone or a major seventh apart in any octave.
Notes are entered with the span they really sound for, so a plucked string
that rings across a barline is checked against the next chord too.
"""
import sys
import numpy as np
from scipy.signal import lfilter
from synthkit import SR, hz, rng, lp1, hp1, lp, hp, bp, adsr, pingpong, make_ir, reverb, finish  # noqa: F401


# ── the score ───────────────────────────────────────────────────────────────
class Song:
    def __init__(self, tl, ch, chords, sections):
        """ch: name -> set of pitch classes; chords: one name a bar;
        sections: [(name, first bar, bar after the last)]."""
        self.tl, self.CH, self.CHORDS, self.SECTIONS = tl, ch, chords, sections
        self.BAR, self.BEAT, self.S16, self.LOOP, self.BARS = tl.bar, tl.beat, tl.s16, tl.loop, tl.bars
        assert len(chords) == tl.bars, (len(chords), tl.bars)
        assert abs(self.S16 * SR - round(self.S16 * SR)) < 1e-6, 'a sixteenth must be a whole number of samples'
        self.notes = []

    def section(self, lb):
        lb %= self.BARS
        return next(n for n, a, b in self.SECTIONS if a <= lb < b)

    def chord(self, lb):
        return self.CHORDS[lb % self.BARS]

    def chord_at(self, t):
        return self.CHORDS[int(np.floor(t / self.BAR + 1e-9)) % self.BARS]

    # entering notes
    def tune(self, tune, part):
        """tune: {loop bar: [(midi, sixteenths), ...]} summing to 16 a bar, 0 = rest."""
        for lb, row in tune.items():
            assert sum(d for _, d in row) == 16, (part, lb, row)
            pos = 0
            for m, d in row:
                if m:
                    self.notes.append((lb * self.BAR + pos * self.S16, d * self.S16, m, part, 'lead', d * self.S16))
                pos += d

    def harm(self, t, d, m, part):
        self.notes.append((t, d, m, part, 'harm', d))

    def phrases(self, tune):
        """A tune split at its rests: [(t0, [(t from t0, d, midi), ...])]."""
        notes = []
        for lb, row in tune.items():
            pos = 0
            for m, d in row:
                if m:
                    notes.append((lb * self.BAR + pos * self.S16, d * self.S16, m))
                pos += d
        out = []
        for s, d, m in sorted(notes):
            if out and abs(out[-1][0] + out[-1][1][-1][0] + out[-1][1][-1][1] - s) < 1e-6:
                out[-1][1].append((s - out[-1][0], d, m))
            else:
                out.append((s, [(0.0, d, m)]))
        return out

    def held(self, voicing, part, bars=None):
        """Sustained voices (pads, drones): voicing(lb) -> list of midi, one per
        voice, or None for silence. A voice holds across the barline while its
        note stays. Enters the notes and returns [(t, d, midi, voice index)]."""
        bars = list(range(self.BARS)) if bars is None else bars
        out = []
        width = max(len(voicing(lb) or []) for lb in bars)
        for k in range(width):
            cur = None
            for lb in range(self.BARS):
                v = voicing(lb) if lb in bars else None
                m = v[k] if v and k < len(v) else None
                if m is None:
                    if cur:
                        out.append(cur); cur = None
                    continue
                if cur and cur[2] == m and abs(cur[0] + cur[1] - lb * self.BAR) < 1e-9:
                    cur[1] += self.BAR
                else:
                    if cur:
                        out.append(cur)
                    cur = [lb * self.BAR, self.BAR, m, k]
            if cur:
                out.append(cur)
        out = [tuple(c) for c in out]
        for t, d, m, k in out:
            self.harm(t, d, m, part)
        return out

    def ring_out(self, events, cap):
        """events [(t, string, midi, ...)]: how long each pluck sounds - until its
        string is plucked again (around the loop) or the chord changes to one
        it is not in (the fretting hand lets go), at most `cap` seconds."""
        by = {}
        for i, e in enumerate(events):
            by.setdefault(e[1], []).append(i)
        ring = [0.0] * len(events)
        for s, idx in by.items():
            idx.sort(key=lambda i: events[i][0])
            for j, i in enumerate(idx):
                t = events[i][0]
                nxt = events[idx[(j + 1) % len(idx)]][0]
                gap = (nxt - t) % self.LOOP or self.LOOP
                dur = min(gap, cap)
                tc = (np.floor(t / self.BAR + 1e-9) + 1) * self.BAR
                while tc < t + dur:
                    if events[i][2] % 12 not in self.CH[self.chord_at(tc)]:
                        dur = tc - t
                        break
                    tc += self.BAR
                ring[i] = dur
        return ring

    # the proof
    def check(self):
        bad, eps = [], 1e-6
        BAR, BEAT, LOOP = self.BAR, self.BEAT, self.LOOP

        def chords_over(t, d):
            out, tc = [self.chord_at(t)], (np.floor(t / BAR + 1e-9) + 1) * BAR
            while tc < t + d - eps:
                out.append(self.chord_at(tc)); tc += BAR
            return out

        def long_(n):
            t, d, m, part, role, w = n
            return role != 'lead' or w >= BEAT - eps or abs(t / (2 * BEAT) - round(t / (2 * BEAT))) < 1e-6

        for n in self.notes:
            t, d, m, part, role, w = n
            if long_(n):
                for c in chords_over(t, d if role != 'lead' else w):
                    if m % 12 not in self.CH[c]:
                        bad.append((part, round(t / BAR, 3), m, c, 'not a chord tone'))
        ev = sorted(self.notes + [(n[0] - LOOP,) + n[1:] for n in self.notes] + [(n[0] + LOOP,) + n[1:] for n in self.notes])
        for i, a in enumerate(ev):
            if not 0 <= a[0] < LOOP:
                continue
            for b in ev[i + 1:]:
                if b[0] >= a[0] + a[1] - eps:
                    break
                if b[0] + b[1] <= a[0] + eps:
                    continue
                iv = abs(a[2] - b[2])
                if iv in (1, 11, 13) or (long_(a) and long_(b) and iv % 12 in (1, 11)):
                    bad.append((a[3], round(a[0] / BAR, 3), a[2], b[3], round(b[0] / BAR, 3), b[2], 'rub'))
        print('lines vs chords:', 'every long or strong note is a chord tone, nothing rubs' if not bad else bad[:20])
        assert not bad, 'a wrong note (listed above)'

    # rendering
    def place(self, bus, t, sig, pan=0.0, gain=1.0):
        """An event of the loop, added on every lap the timeline holds."""
        tl = self.tl
        for k in (-1, 0, 1):
            tt = t + k * self.LOOP
            if tt + len(sig) / SR > -tl.pre * self.BAR and tt < (self.BARS + tl.post) * self.BAR + 1:
                bus.add(tt, sig, pan, gain)

    def finish(self, stems, send, name, rt60=2.6, dark=7000, wet=0.5, wav=None):
        hall = make_ir(rt60, dark=dark, seed=31, pre=0.03)
        stems = dict(stems)
        stems['reverb'] = reverb(sum(stems[k] * send.get(k, 0.0) for k in stems), hall) * wet
        mix = sum(stems.values())
        if '--stems' in sys.argv:
            self.stem_report(stems, mix)
        return finish(self.tl, mix, name, wav=wav)

    def stem_report(self, stems, mix):
        """Per stem: A-weighted level (dB re the mix) by section, the biggest
        top-octave jump against its 99.9th percentile, and its 6-8 kHz and
        8 kHz+ energy (dB of the mix)."""
        tl, BAR = self.tl, self.BAR
        i0, N = tl.smp(0), int(round(self.LOOP * SR))
        secs = self.SECTIONS

        def aw(f):
            f2 = np.asarray(f, float) ** 2
            return 12194 ** 2 * f2 ** 2 / ((f2 + 20.6 ** 2) * np.sqrt((f2 + 107.7 ** 2) * (f2 + 737.9 ** 2)) * (f2 + 12194 ** 2)) * 10 ** 0.1

        def lev(x):
            X = np.fft.rfft(x.mean(1)); f = np.fft.rfftfreq(len(x), 1 / SR)
            return np.sum(np.abs(X) ** 2 * aw(f) ** 2) / len(x) ** 2

        def seg(x, a, b):
            return x[i0 + int(a * BAR * SR):i0 + int(b * BAR * SR)]

        refs = [lev(seg(mix, a, b)) for _, a, b in secs]

        def band(x, lo, hi):
            X = np.fft.rfft(x[i0:i0 + N].mean(1)); f = np.fft.rfftfreq(N, 1 / SR)
            return np.sum(np.abs(X[(f >= lo) & (f < hi)]) ** 2)

        tot = band(mix, 0, SR)
        print('stem (dBA re mix) ' + ' '.join(f'{s:>8s}' for s, _, _ in secs) + '   click      6-8k   8k+')
        for k, v in stems.items():
            row = [10 * np.log10(lev(seg(v, a, b)) / r + 1e-12) for (_, a, b), r in zip(secs, refs)]
            h = np.abs(np.diff(hp(v.mean(1), 6000)[i0:i0 + N]))
            ratio = h.max() / (np.percentile(h, 99.9) + 1e-12)
            hf = [10 * np.log10(band(v, lo, hi) / tot + 1e-12) for lo, hi in ((6000, 8000), (8000, SR))]
            print(f'{k:15s}   ' + ' '.join(f'{r:8.1f}' for r in row) + f'   {ratio:5.1f}x   {hf[0]:6.1f} {hf[1]:6.1f}')


# ── plucked strings (last_bounty.py's) ──────────────────────────────────────
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


def _pick(N, f, tilt, noise, comb, seed, top):
    kk = np.arange(1, int(max(2, min(60, top / f))) + 1)[:, None]
    ph = np.arange(N) / N
    exc = (kk ** -tilt * np.sin(2 * np.pi * kk * ph)).sum(0)
    exc /= np.abs(exc).max()
    exc += noise * lp1(np.random.default_rng(seed).uniform(-1, 1, N), min(top, 9000)) * np.sin(np.pi * np.arange(N) / N)
    k = max(1, int(comb * N))
    exc[k:] -= 0.5 * exc[:-k]
    return exc / np.abs(exc).max()


def string(m, ring, vel, seed, a=0.8, t60=3.0, tilt=0.9, noise=0.15, comb=0.18, top=6000, rel=0.06):
    """A Karplus-Strong string, damped `ring` s after the pluck."""
    f = hz(m)
    N, c, den = ks_setup(f, a, t60)
    exc = _pick(N, f, tilt, noise, comb, seed, top)
    n = int((ring + rel + 0.01) * SR)
    x = np.zeros(n); x[:min(N, n)] = exc[:min(N, n)] * vel
    y = lfilter([1.0, c], den, x)
    y[:48] *= np.linspace(0, 1, 48)
    t = np.arange(n) / SR
    return y * np.clip((ring + rel - t) / rel, 0, 1)


def body(x, res, hp_hz=70):
    """A soundbox: x plus band-passed copies, res = [(fc, q, gain)]."""
    y = x.copy()
    for fc, q, g in res:
        y = y + g * bp(x, fc, q)
    return hp1(y, hp_hz)


# ── continuous voices (last_bounty.py's engine) ─────────────────────────────
def voice_phrase(notes, f_vib=5.6, vib_c=22, glide_hz=26, scoop_c=55, attack=0.03, release=0.07, dip=0.18):
    """A monophonic line through notes [(t, d, midi)] (t from the phrase
    start): glides, a dip between tied notes, a close at rests, vibrato
    growing on long notes. Returns (phase, gain, f)."""
    total = notes[-1][0] + notes[-1][1]
    n = int((total + release + 0.05) * SR)
    f = np.full(n, hz(notes[0][2])); g = np.zeros(n); vw = np.zeros(n); sc = np.zeros(n)
    for j, (t, d, m) in enumerate(notes):
        a, b = int(round(t * SR)), int(round((t + d) * SR))
        tt = np.arange(n - a) / SR
        tied = j + 1 < len(notes) and abs(notes[j + 1][0] - (t + d)) < 1e-6
        fresh = j == 0 or abs(notes[j - 1][0] + notes[j - 1][1] - t) > 1e-6
        f[a:] = hz(m)
        env = np.minimum(1, tt / attack) if fresh else 1 - dip * np.exp(-tt / 0.04)
        if not tied:
            g[a:] = np.maximum(g[a:], env * np.clip((d + release - tt) / release, 0, 1))
        else:
            g[a:b] = env[:b - a]
        vw[a:b] = np.clip((tt[:b - a] - 0.22) / 0.5, 0, 1) * (1.0 if d > 0.45 else 0.25)
        sc[a:b] += -(scoop_c if fresh else scoop_c * 0.3) * np.exp(-tt[:b - a] / 0.045)
    k = np.exp(-2 * np.pi * glide_hz / SR)
    f = lfilter([1 - k], [1, -k], f - f[0]) + f[0]
    t = np.arange(n) / SR
    cents = sc + vib_c * lp1(vw, 8) * np.sin(2 * np.pi * f_vib * t + 0.4 * np.sin(2 * np.pi * 0.31 * t))
    fr = f * 2 ** (cents / 1200)
    return 2 * np.pi * np.cumsum(fr) / SR, lp1(g, 60), fr


def _additive(ph, fr, amps, top=11000):
    """sum_k amps(k) sin(k ph), each partial faded out as it nears `top`."""
    x = np.zeros(len(ph))
    K = int(top / max(fr.min(), 30))
    for k in range(1, K + 1):
        a = amps(k)
        if a:
            x += a * np.clip((top - k * fr) / 1500, 0, 1) * np.sin(k * ph)
    return x


def flute_phrase(notes, seed, breath=0.5, f_vib=5.0, vib_c=18, low=False):
    """A wooden flute (or a low whistle, low=True): near-sine, a little second
    and third harmonic, chiff at each fresh note, breath."""
    ph, g, fr = voice_phrase(notes, f_vib=f_vib, vib_c=vib_c, glide_hz=28, scoop_c=45, attack=0.04)
    n = len(ph)
    z = rng('flute', seed).standard_normal(n)
    tone = np.sin(ph) + (0.18 if low else 0.1) * np.sin(2 * ph) + 0.05 * np.sin(3 * ph)
    air = lp1(z, 160) * np.sin(ph) * 1.6 + hp1(lp(z, 9000), 2500) * 0.12 + bp(z, 6500, 1.3) * 0.12
    return (tone + air * breath) * g


def reed_phrase(notes, seed, kind='clarinet'):
    """A reed: clarinet (odd harmonics, woody), harmonica (all harmonics, a
    bright free reed, a breathy wobble), chanter (a nasal, piping double reed)."""
    if kind == 'clarinet':
        ph, g, fr = voice_phrase(notes, f_vib=5.2, vib_c=8, glide_hz=35, scoop_c=25, attack=0.035)
        x = _additive(ph, fr, lambda k: (k ** -1.0 if k % 2 else 0.12 * k ** -1.3), top=9000)
        x = x + 0.4 * bp(x, 1500, 1.4) + 0.2 * bp(x, 3000, 2)
    elif kind == 'harmonica':
        ph, g, fr = voice_phrase(notes, f_vib=6.0, vib_c=30, glide_hz=50, scoop_c=80, attack=0.025)
        x = _additive(ph, fr, lambda k: k ** -0.75 * (1.3 if k == 2 else 1.0), top=10000)
        x = x + 0.7 * bp(x, 1700, 1.3) + 0.35 * bp(x, 3800, 2)
    else:                                                   # chanter
        ph, g, fr = voice_phrase(notes, f_vib=0.1, vib_c=0, glide_hz=120, scoop_c=0, attack=0.012, dip=0.6)
        x = _additive(ph, fr, lambda k: k ** -0.55, top=9500)
        x = x + 0.8 * bp(x, 1250, 1.5) + 0.5 * bp(x, 2700, 2.2)
    x = lp(hp1(x, 180), 9000, 0.6)
    z = rng('reed', kind, seed).standard_normal(len(ph))
    air = bp(z, 2200, 0.8) * 0.06 + hp1(z, 6000) * 0.015
    return (x / (np.abs(x).max() + 1e-9) + air) * g


def bowed_phrase(notes, seed, kind='violin'):
    """A bowed string: a sawtooth-like spectrum through a body (violin, or a
    cello with its resonances an octave down), vibrato that moves the
    partials across them, bow noise, bow-change dips."""
    lo = kind == 'cello'
    ph, g, fr = voice_phrase(notes, f_vib=5.4 if not lo else 5.0, vib_c=20, glide_hz=22, scoop_c=30,
                             attack=0.08 if not lo else 0.11, release=0.12, dip=0.3)
    x = _additive(ph, fr, lambda k: k ** -1.0, top=10000 if not lo else 6000)
    res = ([(280, 3, 0.8), (480, 3, 0.9), (2800, 1.5, 1.2), (4200, 2.5, 0.4)] if not lo
           else [(140, 3, 0.9), (240, 3, 0.8), (1400, 1.4, 0.6)])
    x = body(x, res, 90 if not lo else 50)
    x = lp(x, 8500 if not lo else 4500)
    z = rng('bow', kind, seed).standard_normal(len(ph))
    noise = bp(z, 3500 if not lo else 1800, 1.0) * 0.05
    return (x / (np.abs(x).max() + 1e-9) + noise) * g


def brass_phrase(notes, seed, kind='horn'):
    """Brass brightening as it swells: a French horn (dark, round) or a tuba (low, short)."""
    ph, g, fr = voice_phrase(notes, f_vib=5.0, vib_c=10 if kind == 'horn' else 4, glide_hz=30, scoop_c=40,
                             attack=0.06 if kind == 'horn' else 0.03, release=0.1)
    s = (0.9 if kind == 'horn' else 1.1) - 0.45 * g
    top = 5000 if kind == 'horn' else 3000
    x = np.zeros(len(ph))
    for k in range(1, int(top / fr.min()) + 1):
        x += k ** -0.6 * np.exp(-(k - 1) * s) * np.clip((top - k * fr) / 800, 0, 1) * np.sin(k * ph)
    x = x + 0.5 * bp(x, 500 if kind == 'horn' else 250, 1.2)
    return lp(hp1(x, 40), 6000) * g


VOWELS = {'mm': [(260, 120, 1.0), (1900, 400, 0.04)],
          'oo': [(330, 120, 1.0), (760, 160, 0.55), (2400, 300, 0.06)],
          'ah': [(700, 150, 1.0), (1150, 180, 0.7), (2600, 300, 0.22), (3400, 400, 0.08)],
          'eh': [(530, 120, 1.0), (1850, 200, 0.6), (2500, 300, 0.25)]}


def choir_note(m, dur, vowel, seed, attack=0.6, release=0.6, singers=3):
    """last_bounty.py's choir: three singers on one note, harmonics through vowel formants."""
    n = int((dur + release + 0.05) * SR); t = np.arange(n) / SR
    r = rng('choir', seed)
    F = VOWELS[vowel]
    x = np.zeros(n)
    for v, cents in enumerate((-8, -1, 7)[:singers]):
        f0 = hz(m) * 2 ** (cents / 1200)
        vib = 1 + 0.0032 * np.sin(2 * np.pi * (4.7 + 0.35 * v) * t + r.uniform(0, 6.3)) * np.clip((t - 0.4) / 0.8, 0, 1)
        ph = 2 * np.pi * np.cumsum(f0 * vib) / SR
        for k in range(1, int(min(60, 7500 / f0)) + 1):
            fk = k * f0
            a = k ** -0.7 * (0.03 + sum(gn * np.exp(-((fk - fc) / bw) ** 2) for fc, bw, gn in F))
            x += a * np.sin(k * ph + r.uniform(0, 6.3))
    z = r.standard_normal(n)
    x += 0.6 * bp(z, F[0][0] * 1.6, 1.5) * 0.2 + hp1(lp1(z, 12000), 5000) * 0.05
    return x / singers * adsr(n, attack, 0.4, 0.88, release, dur)


def pad_note(m, dur, seed, kind='strings', attack=None, release=0.5):
    """A sustained note: 'strings' (three detuned saws, dark, a slow bow),
    'organ' (a pipe organ: principal, octave, twelfth, fifteenth, a little
    mixture, a slow tremulant) or 'drone' (a reedy bagpipe-like drone)."""
    n = int((dur + release + 0.05) * SR); t = np.arange(n) / SR
    r = rng('pad', kind, seed)
    f = hz(m)
    x = np.zeros(n)
    if kind == 'strings':
        for cents in (-9, 0, 8):
            fv = f * 2 ** (cents / 1200) * (1 + 0.003 * np.sin(2 * np.pi * r.uniform(4.6, 5.4) * t + r.uniform(0, 6.3)))
            ph = 2 * np.pi * np.cumsum(fv) / SR
            for k in range(1, int(min(40, 7000 / f)) + 1):
                x += k ** -1.1 * np.sin(k * ph + r.uniform(0, 6.3))
        x = lp(x, 2600); a = attack or 0.5
    elif kind == 'organ':
        ph = 2 * np.pi * f * t * (1 + 0.0015 * np.sin(2 * np.pi * 6.2 * t))
        for k, a_ in ((1, 1.0), (2, 0.7), (3, 0.35), (4, 0.35), (6, 0.12), (8, 0.12)):
            if k * f < 9000:
                x += a_ * np.sin(k * ph + r.uniform(0, 6.3))
        x *= 1 + 0.12 * np.sin(2 * np.pi * 6.2 * t)
        z = r.standard_normal(n)
        x += 0.05 * bp(z, min(4 * f, 6000), 2) * np.clip(1 - t / 0.08, 0, 1)        # the pipe's chiff
        a = attack or 0.05
    else:                                                   # drone
        ph = 2 * np.pi * f * t
        for k in range(1, int(min(30, 6000 / f)) + 1):
            x += k ** -0.7 * np.sin(k * ph + r.uniform(0, 6.3))
        x = x + 0.6 * bp(x, 900, 1.6)
        a = attack or 0.3
    x /= np.abs(x).max() + 1e-9
    return x * adsr(n, a, 0.3, 0.9, release, dur)


# ── mallets and pitched percussion ──────────────────────────────────────────
MALLETS = {   # (partial ratio, amp, tau)
    'marimba': [(1, 1.0, 0.5), (3.93, 0.25, 0.09), (9.2, 0.06, 0.02)],
    'glock':   [(1, 1.0, 1.4), (2.76, 0.25, 0.4), (5.4, 0.12, 0.15)],
    'celesta': [(1, 1.0, 0.9), (2, 0.25, 0.4), (3, 0.06, 0.15)],
    'vibes':   [(1, 1.0, 1.6), (4, 0.18, 0.3), (10, 0.03, 0.05)],
}


def mallet(m, seed, kind='marimba', vel=1.0, ring=None):
    f = hz(m); P = MALLETS[kind]
    dur = ring or 4 * P[0][2]
    n = int((dur + 0.05) * SR); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * r_ * t) * np.exp(-t / tau) for r_, a, tau in P if f * r_ < 16000)
    z = np.random.default_rng(seed).standard_normal(n)
    x = x + 0.15 * bp(z, min(f * 4, 9000), 1.5) * np.exp(-t / 0.003)
    return x * np.minimum(1, t / 0.0008) * vel * np.clip((dur - t) / 0.05, 0, 1)


def bell(root, ring, seed, partials):
    """A bell on `root`, partials [(ratio, amp, tau)], stopped `ring` s after the strike."""
    f = hz(root); n = int((ring + 0.4) * SR); t = np.arange(n) / SR
    x = np.zeros(n); r = rng('bell', seed)
    for ratio, a, tau in partials:
        x += a * np.sin(2 * np.pi * f * ratio * (1 + 0.0009 * r.uniform(-1, 1)) * t + r.uniform(0, 6.3)) * np.exp(-t / tau)
    z = r.standard_normal(n)
    x += 0.3 * bp(z, 2400, 1.0) * np.exp(-t / 0.006)
    return x * np.minimum(1, t / 0.0015) * np.clip((ring - t) / 0.35, 0, 1)


def timp(m, v, seed, ring):
    f = hz(m); n = int((ring + 0.12) * SR); t = np.arange(n) / SR
    bend = np.cumsum(1 + 0.012 * np.exp(-t / 0.08)) / SR
    x = np.zeros(n)
    for r_, a, tau in ((1, 1, 1.1), (1.5, 0.45, 0.6), (1.99, 0.3, 0.45), (2.44, 0.14, 0.3), (2.98, 0.08, 0.22)):
        x += a * np.sin(2 * np.pi * f * r_ * bend) * np.exp(-t / tau)
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.45 * lp(z, 400) * np.exp(-t / 0.02) + 0.08 * hp(z, 3000) * np.exp(-t / 0.004)
    return x * np.minimum(1, t / 0.002) * v * np.clip((ring - t) / min(0.1, ring / 2), 0, 1)


def frame_drum(seed, f0=90, vel=1.0, open_=True):
    """A frame drum or bodhran: a low membrane thud (open) or a rim tap."""
    n = int(0.5 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    if open_:
        f = f0 * (1 + 0.25 * np.exp(-t / 0.02))
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16) + 0.3 * lp(z, 900) * np.exp(-t / 0.015)
    else:
        x = bp(z, 2200, 1.4) * np.exp(-t / 0.012) + 0.3 * np.sin(2 * np.pi * f0 * 3.1 * t) * np.exp(-t / 0.03)
    x += 0.15 * hp(z, 5000) * np.exp(-t / 0.002)
    return x * np.minimum(1, t / 0.0006) * vel


def log_drum(m, seed, vel=1.0):
    """A slit log drum: a short, hollow, pitched knock."""
    f = hz(m); n = int(0.45 * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.12) + 0.3 * np.sin(2 * np.pi * 2.8 * f * t) * np.exp(-t / 0.03)
    z = np.random.default_rng(seed).standard_normal(n)
    x += 0.25 * bp(z, 1500, 1.2) * np.exp(-t / 0.006)
    return x * np.minimum(1, t / 0.0006) * vel


def kick(seed, vel=1.0, f0=55):
    n = int(0.5 * SR); t = np.arange(n) / SR
    f = f0 * (1 + 1.5 * np.exp(-t / 0.03))
    z = np.random.default_rng(seed).standard_normal(n)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.22) + 0.2 * lp(z, 2000) * np.exp(-t / 0.005)
    return x * np.minimum(1, t / 0.0005) * vel


def snare(seed, vel=1.0, brush=False):
    n = int(0.3 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    if brush:
        return (hp(lp(z, 9000), 2500) * np.minimum(1, t / 0.01) * np.exp(-t / 0.06)) * vel
    x = 0.6 * np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.04) + bp(z, 4500, 0.7) * np.exp(-t / 0.08)
    return x * np.minimum(1, t / 0.0005) * vel


def shaker(seed, acc=1.0):
    n = int(0.09 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    return (hp(lp(z, 9500), 4200) + 1.2 * bp(z, 7000, 1.6)) * np.minimum(1, t / 0.006) * np.exp(-t / (0.018 + 0.012 * acc))


def woodblock(seed, f=1100, vel=1.0):
    n = int(0.12 * SR); t = np.arange(n) / SR
    z = np.random.default_rng(seed).standard_normal(n)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.025) + 0.5 * bp(z, f * 2.6, 3) * np.exp(-t / 0.01)
    return x * np.minimum(1, t / 0.0004) * vel


def triangle(seed, m=105, ring=1.2):
    f = hz(m); n = int(ring * SR); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * r_ * t) * np.exp(-t / tau) for r_, a, tau in ((1, 1, 0.8), (2.76, 0.4, 0.4), (5.2, 0.2, 0.2)))
    z = np.random.default_rng(seed).standard_normal(n)
    return (x + 0.3 * hp(z, 6000) * np.exp(-t / 0.002)) * np.minimum(1, t / 0.0004) * np.clip((ring - t) / 0.1, 0, 1)


def jaw_harp(m, dur, seed):
    """A jaw harp 'boing': a buzzy drone on m whose formant sweeps up and back."""
    f = hz(m); n = int((dur + 0.1) * SR); t = np.arange(n) / SR
    ph = 2 * np.pi * f * t
    x = sum(k ** -0.4 * np.sin(k * ph) for k in range(1, int(8000 / f)))
    fc = 700 + 1700 * np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 2
    y = np.zeros(n); CH_ = 480
    for i in range(0, n, CH_):
        y[i:i + CH_] = bp(x[max(0, i - 2000):i + CH_], fc[i], 5)[-len(x[i:i + CH_]):]
    return y * np.minimum(1, t / 0.004) * np.exp(-t / (dur * 0.7)) * np.clip((dur - t) / 0.05 + 1, 0, 1)


# ── atmosphere ──────────────────────────────────────────────────────────────
def wind(seed, dur, lo=380, span=900):
    """A gust: band-passed noise whose centre rises and falls, stereo."""
    n = int(dur * SR); u = np.arange(n) / n
    r = rng('wind', seed)
    env = np.sin(np.pi * u) ** 2 * (0.7 + 0.3 * np.sin(2 * np.pi * (u * r.uniform(1.5, 2.5) + r.random())))
    out = np.zeros((n, 2)); CH_ = 960
    for ch in range(2):
        z = r.standard_normal(n); y = np.empty(n); zi = np.zeros(2)
        for i in range(0, n, CH_):
            fc = lo + span * env[i] ** 1.3
            w = 2 * np.pi * fc / SR; q = 0.9; al = np.sin(w) / (2 * q); c = np.cos(w)
            b = np.array([al, 0, -al]); a = np.array([1 + al, -2 * c, 1 - al])
            y[i:i + CH_], zi = lfilter(b / a[0], a / a[0], z[i:i + CH_], zi=zi)
        out[:, ch] = y * env + hp1(lp1(z, 7000), 3000) * env ** 2 * 0.08
    return out


def surf(seed, dur):
    """One wave: a swell of low noise, a break, a long hiss pulling back over shingle."""
    n = int(dur * SR); u = np.arange(n) / n
    r = rng('surf', seed)
    out = np.zeros((n, 2))
    env = np.where(u < 0.45, (u / 0.45) ** 2, np.exp(-(u - 0.45) / 0.18))
    for ch in range(2):
        z = r.standard_normal(n)
        out[:, ch] = lp(z, 500) * env + hp(lp1(z, 9000), 1800) * env ** 1.5 * 0.35 * (u > 0.4)
    return out * np.sin(np.pi * u)[:, None] ** 0.3


def bird(seed, kind='chirp'):
    """One bird call: 'chirp' (a quick rising sweep, repeated), 'trill', 'gull' (a falling mew)."""
    r = rng('bird', kind, seed)
    if kind == 'gull':
        dur = 0.55; n = int(dur * SR); t = np.arange(n) / SR
        f = 1500 - 700 * (t / dur) ** 0.7 + 60 * np.sin(2 * np.pi * 22 * t)
        ph = 2 * np.pi * np.cumsum(f) / SR
        x = np.sin(ph) + 0.4 * np.sin(2 * ph) + 0.25 * np.sin(3 * ph)
        return x * np.sin(np.pi * t / dur) ** 0.5 * 0.6
    reps = r.integers(2, 5) if kind == 'chirp' else 1
    out = []
    for k in range(reps):
        dur = r.uniform(0.06, 0.12) if kind == 'chirp' else r.uniform(0.5, 0.9)
        n = int(dur * SR); t = np.arange(n) / SR
        f0 = r.uniform(2800, 4200)
        f = f0 * (1 + 0.35 * t / dur) if kind == 'chirp' else f0 * (1 + 0.12 * np.sin(2 * np.pi * r.uniform(18, 26) * t))
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / dur) ** 1.5
        out += [x, np.zeros(int(r.uniform(0.04, 0.09) * SR))]
    return np.concatenate(out)


def insects(seed, dur):
    """Cicadas: a band of high noise pulsed fast, swelling and fading."""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    r = rng('insects', seed)
    z = r.standard_normal(n)
    am = (0.5 + 0.5 * np.sin(2 * np.pi * r.uniform(35, 55) * t)) ** 3
    return bp(z, r.uniform(5200, 6800), 4) * am * np.sin(np.pi * u) ** 1.2


def thunder(seed, dur=5.0):
    n = int(dur * SR); t = np.arange(n) / SR
    r = rng('thunder', seed)
    z = r.standard_normal(n)
    env = np.minimum(1, t / 0.08) * np.exp(-t / (dur / 3.5)) * (0.6 + 0.4 * lp1(np.abs(r.standard_normal(n)), 6) * 4)
    return lp(z, 260) * env + 0.15 * bp(z, 1200, 0.7) * np.exp(-t / 0.3)
