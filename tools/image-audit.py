#!/usr/bin/env python3
"""Find repeated artwork across lessons.

Three passes, cheapest first:

  1. MD5        — byte-identical copies of the same file under two names.
  2. ahash      — a 256-bit 16x16 average hash. Distance <= 20 means the same
                  picture (a re-encode, a resize, or a slightly different crop);
                  <= 42 means "look at it before you trust it".
  3. data-bg    — how many distinct pictures each deck actually shows, and how
                  many times each one repeats.

Run pass 1 and 2 over any candidate artwork BEFORE adopting it into a lesson
folder. On 2026-09-04 three "fresh" scenes were pulled from Downloads into
MinecraftB1/ that turned out to be the same pictures Tense Review and Past
Modals were already using, under different Midjourney filenames.

Usage:
    python3 tools/image-audit.py <folder-or-image> [more...]
    python3 tools/image-audit.py --decks <lesson.html> [more...]

Needs Pillow.
"""
import sys, os, re, glob, hashlib, itertools, collections

THRESH_SAME, THRESH_LOOK = 20, 42


def images(args):
    out = []
    for a in args:
        if os.path.isdir(a):
            for ext in ('jpg', 'jpeg', 'png', 'webp'):
                out += sorted(glob.glob(os.path.join(a, '*.' + ext)))
        elif os.path.isfile(a):
            out.append(a)
    return out


def ahash(path):
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(path).convert('L').resize((16, 16))
    px = list(im.get_flattened_data() if hasattr(im, 'get_flattened_data') else im.getdata())
    avg = sum(px) / len(px)
    return sum(1 << i for i, v in enumerate(px) if v > avg)


def audit_images(paths):
    seen = collections.defaultdict(list)
    for p in paths:
        seen[hashlib.md5(open(p, 'rb').read()).hexdigest()].append(p)
    dupes = [v for v in seen.values() if len(v) > 1]
    print(f"== {len(paths)} images, {len(seen)} distinct files ==")
    if dupes:
        print("\nBYTE-IDENTICAL:")
        for v in dupes:
            print("   " + "\n   = ".join(v))

    H = {}
    for p in paths:
        try:
            H[p] = ahash(p)
        except Exception as e:
            print(f"   skip {p}: {e}")
    pairs = []
    for a, b in itertools.combinations(sorted(H), 2):
        d = bin(H[a] ^ H[b]).count('1')
        if d <= THRESH_LOOK:
            pairs.append((d, a, b))
    print(f"\nNEAR-DUPLICATE PAIRS (<= {THRESH_SAME} is the same picture):")
    if not pairs:
        print("   none")
    for d, a, b in sorted(pairs):
        mark = "SAME  " if d <= THRESH_SAME else "check "
        print(f"   {mark}d={d:3d}  {a}\n              {b}")


def audit_decks(files):
    for f in files:
        s = open(f, encoding='utf-8', errors='replace').read()
        bgs = [b for b in re.findall(r'data-bg="([^"]+)"', s) if 'folder/other' not in b]
        n = len(re.findall(r'<section class="slide', s))
        c = collections.Counter(bgs)
        print(f"\n## {f} — {n} slides, {len(bgs)} with a background, "
              f"{len(c)} distinct pictures")
        for img, k in c.most_common():
            print(f"   {k:3d}x  {img}" + ("   <-- repeated" if k > 1 else ""))


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    if args[0] == '--decks':
        audit_decks(args[1:])
    else:
        audit_images(images(args))
