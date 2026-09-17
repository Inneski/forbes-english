#!/usr/bin/env python3
"""Turn generated artwork into the thirty-two 16:9 plates this RPG needs.

    py lesson-template/build/rpg/loch-ness-loop-rpg/prep-plates.py --list
    py lesson-template/build/rpg/loch-ness-loop-rpg/prep-plates.py incoming/lochness
    py lesson-template/build/rpg/loch-ness-loop-rpg/prep-plates.py one.png --as 09_q7_shore1.webp

Same tool as rpg/kraken-black-tide-rpg/prep-plates.py with one difference:
**this lesson's plates are 16:9, 1536 x 864**, not 3:2. Innes asked for 16:9
on the brief, and the engine takes it through `img_w`/`img_h` in the spec
(Wonderland: The Stolen Now is 1536 x 864 too). A 3:2 render is centre-cropped
to 16:9 — 80 px off the top and bottom of a 1536 x 1024 — so a picture model
that only does 3:2 (ChatGPT's) still works as long as the object and the
quiet half sit inside the middle band; IMAGES.md says so on every prompt.

  1. centre-crop to 16:9 and resize to 1536 x 864;
  2. WebP, walked down in quality until the file is under 200 KB;
  3. refuses a batch of the wrong length, and refuses to write the same
     picture under two names.

Requires Pillow.
"""
import hashlib
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
OUT = os.path.join(REPO, 'block-camp', 'loch-ness-loop-rpg')

W, H = 1536, 864
MAX_BYTES = 200 * 1024

PLATES = [
    '01_cover.webp',
    '02_q1_shop1.webp', '03_q2_shop2.webp', '04_q3_shop3.webp',
    '05_q4_shop4.webp', '06_q5_shop5.webp', '07_q6_shop6.webp',
    '08_choice1_dores.webp',
    '09_q7_shore1.webp', '10_q8_shore2.webp', '11_q9_shore3.webp', '12_q10_shore4.webp',
    '13_q7_hill1.webp', '14_q8_hill2.webp', '15_q9_hill3.webp', '16_q10_hill4.webp',
    '17_q11_pub1.webp', '18_q12_pub2.webp', '19_q13_pub3.webp',
    '20_choice2_pier.webp',
    '21_q14_deep1.webp', '22_q15_deep2.webp', '23_q16_deep3.webp',
    '24_q14_bay1.webp', '25_q15_bay2.webp', '26_q16_bay3.webp',
    '27_q17_back1.webp', '28_q18_back2.webp',
    '29_ending_master.webp', '30_ending_complete.webp',
    '31_ending_missing.webp', '32_ending_failed.webp',
]

SRC_EXT = ('.png', '.jpg', '.jpeg', '.webp')


def sources(args):
    out = []
    for a in args:
        p = os.path.abspath(a)
        if os.path.isdir(p):
            out += [os.path.join(p, f) for f in sorted(os.listdir(p))
                    if f.lower().endswith(SRC_EXT)]
        elif os.path.isfile(p):
            out.append(p)
        else:
            sys.exit('no such file or directory: %s' % a)
    return out


def crop_16x9(im):
    """Centre-crop to 16:9 before resizing; never squash."""
    im = im.convert('RGB')
    w, h = im.size
    if w * 9 > h * 16:                     # too wide
        new = int(round(h * 16 / 9))
        left = (w - new) // 2
        im = im.crop((left, 0, left + new, h))
    elif w * 9 < h * 16:                   # too tall (a 3:2 render lands here)
        new = int(round(w * 9 / 16))
        top = (h - new) // 2
        im = im.crop((0, top, w, top + new))
    return im.resize((W, H), Image.LANCZOS)


def write(im, dest):
    for q in (88, 84, 80, 76, 72, 68, 64, 60):
        im.save(dest, 'WEBP', quality=q, method=6)
        n = os.path.getsize(dest)
        if n <= MAX_BYTES:
            return n, q
    return None


def main(argv):
    if '--list' in argv:
        for i, p in enumerate(PLATES, 1):
            print('%2d  %s' % (i, p))
        return 0

    as_name = None
    if '--as' in argv:
        i = argv.index('--as')
        as_name = argv[i + 1]
        del argv[i:i + 2]
        if as_name not in PLATES:
            sys.exit('--as %s is not one of the thirty-two plates (--list)' % as_name)

    srcs = sources(argv)
    if not srcs:
        sys.exit(__doc__.strip().splitlines()[0] + '\n  (pass a folder, or a file with --as)')

    if as_name:
        if len(srcs) != 1:
            sys.exit('--as takes exactly one source, got %d' % len(srcs))
        targets = [as_name]
    else:
        if len(srcs) != len(PLATES):
            sys.exit('%d sources for %d plates. Name them in play order and pass the '
                     'whole set, or do one at a time with --as (see --list).'
                     % (len(srcs), len(PLATES)))
        targets = PLATES

    os.makedirs(OUT, exist_ok=True)
    seen, fails = {}, []
    for src, name in zip(srcs, targets):
        im = crop_16x9(Image.open(src))
        h = hashlib.sha1(im.tobytes()).hexdigest()
        if h in seen:
            fails.append('%s is the same picture as %s' % (name, seen[h]))
            continue
        seen[h] = name
        dest = os.path.join(OUT, name)
        got = write(im, dest)
        if not got:
            os.remove(dest)
            fails.append('%s will not go under 200 KB even at q60 — re-render it '
                         'with less fine texture' % name)
            continue
        n, q = got
        print('%-26s %4d KB  q%d  <- %s' % (name, n // 1024, q, os.path.basename(src)))

    missing = [p for p in PLATES if not os.path.exists(os.path.join(OUT, p))]
    if missing:
        print('\nstill missing %d of %d plates:\n  %s'
              % (len(missing), len(PLATES), '\n  '.join(missing)))
    if fails:
        print('\n' + '\n'.join(fails))
        return 1
    if not missing:
        print('\nall %d plates present in %s' % (len(PLATES), os.path.relpath(OUT, REPO)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
