#!/usr/bin/env python3
"""Turn Midjourney output into the thirty-two plates this RPG needs.

    py lesson-template/build/rpg/kraken-black-tide-rpg/prep-plates.py --list
    py lesson-template/build/rpg/kraken-black-tide-rpg/prep-plates.py incoming/kraken
    py lesson-template/build/rpg/kraken-black-tide-rpg/prep-plates.py one.png --as 09_q7_reef1.webp

`tools/prep-artwork.py` is the deck tool: 16:9, 2000px, JPEG. An RPG plate is
a different animal — 3:2, 1536x1024, WebP, under 200 KB, because the engine
inlines nothing and the browser loads every scene's picture as a file. So this
does the three things that spec needs and nothing else:

  1. **Centre-crop to 3:2 and resize to 1536x1024.** Midjourney at --ar 3:2
     comes back close but not exact, and a plate that is not exactly 3:2 puts
     every hotspot percentage out by the difference.
  2. **WebP, walked down in quality until the file is under 200 KB.** Starts
     at 88 and steps to 60; anything that still will not fit is reported
     rather than written, because a 300 KB plate on a thirty-two plate game is
     three megabytes of page weight nobody asked for.
  3. **Refuses a batch that is not the right length, and refuses to overwrite
     a plate with a picture it has already seen** — Midjourney hands you four
     near-identical variants of the same grid and two of them landing as two
     different scenes is the defect that threw away a whole export.

Requires Pillow.
"""
import hashlib
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
OUT = os.path.join(REPO, 'block-camp', 'kraken-black-tide-rpg')

W, H = 1536, 1024
MAX_BYTES = 200 * 1024

# play order, and the only names the builder will look for. The briefing
# screen reuses 07_q6_shed.webp, so there is no plate of its own for it.
PLATES = [
    '01_cover.webp',
    '02_q1_drift.webp', '03_q2_bell.webp', '04_q3_provost.webp',
    '05_q4_hoy.webp', '06_q5_jar.webp', '07_q6_shed.webp',
    '08_choice1_sound.webp',
    '09_q7_reef1.webp', '10_q8_reef2.webp', '11_q9_reef3.webp', '12_q10_reef4.webp',
    '13_q7_cave1.webp', '14_q8_cave2.webp', '15_q9_cave3.webp', '16_q10_cave4.webp',
    '17_q11_wreck1.webp', '18_q12_wreck2.webp', '19_q13_wreck3.webp',
    '20_choice2_decision.webp',
    '21_q14_corry1.webp', '22_q15_corry2.webp', '23_q16_corry3.webp',
    '24_q14_night1.webp', '25_q15_night2.webp', '26_q16_night3.webp',
    '27_q17_barrels.webp', '28_q18_last.webp',
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


def crop_3x2(im):
    """Centre-crop to 3:2 before resizing. Squashing a 16:9 render to 3:2
    instead would stretch every face in the game by 12%."""
    im = im.convert('RGB')
    w, h = im.size
    if w * 2 > h * 3:                      # too wide
        new = int(round(h * 3 / 2))
        left = (w - new) // 2
        im = im.crop((left, 0, left + new, h))
    elif w * 2 < h * 3:                    # too tall
        new = int(round(w * 2 / 3))
        top = (h - new) // 2
        im = im.crop((0, top, w, top + new))
    return im.resize((W, H), Image.LANCZOS)


def write(im, dest):
    """Walk the quality down until it fits. Returns (bytes, quality) or None."""
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
        im = crop_3x2(Image.open(src))
        # the duplicate check is on the CROPPED pixels, not the source file:
        # two Midjourney variants differ in bytes and not in what they show.
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
