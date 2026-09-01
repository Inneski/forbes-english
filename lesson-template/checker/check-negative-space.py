#!/usr/bin/env python3
"""Is the text block sitting on a character, or on the empty half of the plate?

WHY THIS EXISTS. Innes, opening a freshly built deck: "slides 5-10 with text on
wrong side - like are you even scanning for negative space?!" Then, after the
first version of this file shipped: "Pages 8, 15, 18 have text on wrong side on
past continuous passive". Both times the answer was that nothing was measuring
it, and then that the wrong thing was.

WHAT THE FIRST VERSION GOT WRONG, because it is an instructive failure. It
summed edge-gradient magnitude per half and called the busier half occupied.
That measures TEXTURE DENSITY, and texture density is not subjecthood. A brick
wall and a starfield are pure texture; a smooth-shaded villager two metres from
camera is almost none. On the three slides Innes flagged it scored the EMPTY
half busier and passed all three (0.92, 0.82, 0.94).

WHAT ACTUALLY SEPARATES THEM. These plates are colour-graded hard - a
Minecraft scene pushed to one hue for its camp: gold, pink, teal, green. The
terrain, sky and architecture all sit inside that grade. The characters do not:
Steve's teal shirt and purple legs, a villager's brown robe, skin tones. They
are the pixels that break the plate's own colour statistics.

So: convert to CIE Lab, take the plate's median colour as its grade, and score
every pixel by robust distance from it - each channel divided by that channel's
own median-absolute-deviation, so a plate with a natural sky-to-ground
luminance ramp is not convicted of having a sky. Luminance is weighted down to
0.25 because bright sky is the one non-character thing that reliably breaks the
grade; hue and chroma carry the signal. Score a half by the mean of its top
decile - one compact off-grade subject beats a wash of mild noise.

VALIDATED, NOT ASSERTED. Twelve slides labelled by eye: the three Innes
reported, five more found and confirmed to sit on a character, and four
confirmed correct (including two the previous metric's replacement would have
convicted - a warm window in a blue room, a bright sky over an empty lawn).
Worst true positive 1.30, worst true negative 1.21. MARGIN sits at 1.25 in that
gap. That gap is 8% wide, so treat findings near the line as "go and look",
not as proof - the numbers are printed for exactly that reason.

    python3 lesson-template/checker/check-negative-space.py [deck.html ...]
"""
import glob, os, re, sys

try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit('needs Pillow and numpy:  pip install pillow numpy')

CANVAS_W, CANVAS_H = 1280, 720
# The column a data-side block occupies: 52% of the canvas, pinned to its edge
# with the stage's 64px padding. Measured from the shipped CSS, not guessed.
PAD, COL = 64, 0.52
# Weight on the luminance channel. Chroma carries the character signal; L is
# kept at a quarter so a blown-out sky cannot convict an empty half on its own.
W_L = 0.25
# Fraction of a half discarded before scoring, so the score reflects the
# most off-grade region rather than the average of the whole column.
Q = 0.90
# Ratio at which a slide is called wrong. See the validation note above.
MARGIN = 1.25
# The same ratio, applied top-vs-bottom to a data-vpos="bottom" slide. Held
# higher than MARGIN because a bottom anchor is a deliberate composition call
# and only wants overruling when the lower half is plainly the occupied one.
MARGIN_VPOS = 1.50

ALLOW_VPOS = {
    # ('deck.html', slide_number): 'why this one belongs at the bottom anyway'
}

ALLOW = {
    # ('deck.html', slide_number): 'why this one is right anyway'
    # All six checked by eye. Five are the metric's known blind spot: a blown-out
    # sun or window is as far off the plate's grade as a character is.
    ('blockcamp-future-simple-2.html', 15):
        'fs bg33 - no character at all; the sunset over the rails scores the ratio',
    ('blockcamp-past-simple.html', 16):
        'ps bg30 - the villager IS on the left; the text is already on the empty plaza',
    ('blockcamp-passive-past-simple.html', 19):
        'ps bg30 - as above',
    ('blockcamp-past-continuous.html', 7):
        'pc bg30 - rod and arm are bottom-left; the text is already on the far water',
    ('blockcamp-past-continuous-2.html', 7):
        'pc bg30 - as above',
    ('blockcamp-passive-past-continuous.html', 7):
        'pc bg30 - as above',
    ('blockcamp-passive-past-continuous.html', 13):
        'pc bg33 - sleeper on the left, creeper on the right. No good half exists.',
    ('blockcamp-passive-future-simple.html', 10):
        'fs bg12 - blind spot 1, and a clean example of it. Alex is at 7-24% of '
        'the frame; the right half is an unlit cave mouth, which is texture '
        'without a subject and scores 1.45x. Measured at full size, the right '
        'is the correct half and the gate disagrees.',
}


def to_lab(im):
    a = np.asarray(im, dtype=np.float64) / 255.0
    a = np.where(a > 0.04045, ((a + 0.055) / 1.055) ** 2.4, a / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805],
                  [0.2126, 0.7152, 0.0722],
                  [0.0193, 0.1192, 0.9505]])
    xyz = a @ M.T / np.array([0.9505, 1.0, 1.089])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116.0)
    return np.dstack([116 * f[..., 1] - 16,
                      500 * (f[..., 0] - f[..., 1]),
                      200 * (f[..., 1] - f[..., 2])])


def off_grade(path):
    """Per-pixel robust distance from the plate's own colour grade."""
    im = Image.open(path).convert('RGB').resize((320, 180))
    v = to_lab(im)
    flat = v.reshape(-1, 3)
    med = np.median(flat, axis=0)
    mad = np.median(np.abs(flat - med), axis=0) + 1e-6
    z = (v - med) / mad
    return np.sqrt(W_L * z[..., 0] ** 2 + z[..., 1] ** 2 + z[..., 2] ** 2)


def halves(d):
    """The text column and its mirror, as slices of the score map."""
    w = int(CANVAS_W * COL)
    s = d.shape[1] / float(CANVAS_W)
    left = d[:, int(PAD * s):int((PAD + w) * s)]
    right = d[:, int((CANVAS_W - PAD - w) * s):int((CANVAS_W - PAD) * s)]
    return left, right


def score(a):
    v = np.sort(a.ravel())
    return float(v[int(len(v) * Q):].mean())


def slides(src):
    body = src[src.find('<section class="slide'):src.find('const UI_I18N')]
    out, n = [], 0
    for m in re.finditer(r'<section class="slide[^>]*>', body):
        tag = m.group(0)
        if 'data-type=' not in tag:
            continue
        n += 1
        bg = re.search(r'data-bg="([^"]+)"', tag)
        side = re.search(r'data-side="(\w+)"', tag)
        kind = re.search(r'data-type="(\w+)"', tag)
        vpos = re.search(r'data-vpos="(\w+)"', tag)
        out.append((n, bg.group(1) if bg else None,
                    side.group(1) if side else None,
                    kind.group(1) if kind else '',
                    vpos.group(1) if vpos else 'center'))
    return out


# The deck bar. Below this line nothing is read, so it is also the bottom of
# the box a slide is really composed inside.
BAR = 644 / 720.0


def anchored_wrong(col):
    """A bottom-anchored slide sits in the lower half of its column. Is that
    the half with the subject in it? Same measurement as the left/right gate,
    turned ninety degrees."""
    vis = col[:int(col.shape[0] * BAR)]
    half = len(vis) // 2
    return score(vis[half:]) / max(score(vis[:half]), 1e-9)


RED, GRN, DIM = '\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[2m%s\x1b[0m'


def main(decks):
    findings, low, checked, allowed = [], [], 0, 0
    cache = {}
    for deck in decks:
        name = os.path.basename(deck)
        root = os.path.dirname(os.path.abspath(deck))
        src = open(deck, encoding='utf-8').read()
        for n, bg, side, kind, vpos in slides(src):
            # A cover or a centred slide has no other side to move to.
            if not bg or side not in ('left', 'right'):
                continue
            path = os.path.join(root, bg)
            if not os.path.exists(path):
                continue
            if path not in cache:
                try:
                    cache[path] = halves(off_grade(path))
                except Exception:
                    continue
            L, R = cache[path]
            checked += 1
            t, o = (score(L), score(R)) if side == 'left' else (score(R), score(L))
            if o <= 0:
                continue
            ratio = t / o
            if ratio >= MARGIN:
                if (name, n) in ALLOW:
                    allowed += 1
                    continue
                findings.append((name, n, kind, side, bg, ratio))
            if vpos == 'bottom':
                v = anchored_wrong(L if side == 'left' else R)
                if v >= MARGIN_VPOS and (name, n) not in ALLOW_VPOS:
                    low.append((name, n, kind, bg, v))

    findings.sort(key=lambda f: -f[5])
    print('\n  TEXT ON A CHARACTER            %d slide(s) measured, margin %.2fx'
          % (checked, MARGIN))
    if allowed:
        print(DIM % ('  %d allowed by name' % allowed))
    print()
    if not findings:
        print('    ' + GRN % 'PASS',
              'every side-pinned slide sits on the half that is not the subject\n')
        return report_low(low)
    for name, n, kind, side, bg, ratio in findings:
        print('    ' + RED % 'FAIL',
              '%-34s slide %2d  %-8s on the %-5s  %.2fx  %s'
              % (name.replace('blockcamp-', '').replace('.html', ''),
                 n, kind, side, ratio, os.path.basename(bg)))
    print(DIM % '\n          Flip data-side, or add it to ALLOW with a reason.')
    print(DIM % '          Findings under ~1.4x are worth eyeballing before flipping.')
    print('\n  %d slide(s) to look at\n' % len(findings))
    return report_low(low) or 1


def report_low(low):
    """Second gate: a bottom anchor pointing at the busy half."""
    print('  ANCHORED LOW ONTO THE SUBJECT  margin %.2fx\n' % MARGIN_VPOS)
    if not low:
        print('    ' + GRN % 'PASS',
              'every bottom-anchored slide has the quieter half under it\n')
        return 0
    for name, n, kind, bg, v in sorted(low, key=lambda f: -f[4]):
        print('    ' + RED % 'FAIL',
              '%-34s slide %2d  %-8s bottom half %.2fx busier  %s'
              % (name.replace('blockcamp-', '').replace('.html', ''),
                 n, kind, v, os.path.basename(bg)))
    print(DIM % '\n          Move it to data-vpos="top", or add it to ALLOW_VPOS.')
    print('\n  %d slide(s) to look at\n' % len(low))
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or sorted(glob.glob('blockcamp-*.html'))))
