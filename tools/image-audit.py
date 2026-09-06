#!/usr/bin/env python3
"""Find repeated artwork across lessons.

Three passes, cheapest first:

  1. MD5        — byte-identical copies of the same file under two names.
  2. dhash + colour — a 256-bit gradient hash (which way brightness steps,
                  not how bright) plus an 8x8 RGB signature. A pair counts as
                  the same picture only when BOTH agree.
  3. data-bg    — how many distinct pictures each deck actually shows, and how
                  many times each one repeats.

Run pass 1 and 2 over any candidate artwork BEFORE adopting it into a lesson
folder. On 2026-09-04 three "fresh" scenes were pulled from Downloads into
MinecraftB1/ that turned out to be the same pictures Tense Review and Past
Modals were already using, under different Midjourney filenames.

**Why not an average hash.** The first version of this tool used a 16x16 ahash
and it was worthless on this site's artwork, which is flat minimalist
illustration: a wide gradient sky over a dark horizontal mass, over and over.
Measured on 2026-09-06 against six known-identical pairs and four confirmed
false positives:

    metric     true duplicates   false positives
    ahash            0 - 4            4 - 20      <- overlapping, useless
    dhash            2 - 6           98 - 107
    colour         0.2 - 2.3        130 - 181

ahash rated a boat on open water and a figure on a road at sunset as distance
4 — closer than two genuine crops of the same picture. It throws away colour
and encodes only "is this pixel above the mean", which for this style is the
same answer everywhere. dhash and colour each separate the two classes by an
order of magnitude, so both are required to agree.

Usage:
    python3 tools/image-audit.py <folder-or-image> [more...]
    python3 tools/image-audit.py --decks <lesson.html> [more...]

Needs Pillow.
"""
import sys, os, re, glob, hashlib, itertools, collections

# Measured margins are enormous (see the table above), so these sit in the gap
# rather than near either class.
THRESH_SAME, THRESH_LOOK = 12, 24   # dhash bits
THRESH_COLOUR = 20                  # mean per-channel RGB distance, 0-765


def images(args):
    out = []
    for a in args:
        if os.path.isdir(a):
            for ext in ('jpg', 'jpeg', 'png', 'webp'):
                out += sorted(glob.glob(os.path.join(a, '*.' + ext)))
        elif os.path.isfile(a):
            out.append(a)
    return out


def _data(im):
    return list(im.get_flattened_data() if hasattr(im, 'get_flattened_data')
                else im.getdata())


def dhash(path, s=16):
    """Gradient hash: which way brightness steps, not how bright it is."""
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    px = _data(Image.open(path).convert('L').resize((s + 1, s)))
    bits = 0
    for i, (r, c) in enumerate((r, c) for r in range(s) for c in range(s)):
        if px[r * (s + 1) + c] > px[r * (s + 1) + c + 1]:
            bits |= 1 << i
    return bits


def colour_sig(path, s=8):
    """8x8 RGB thumbnail. ahash discards colour entirely; this is why it failed."""
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    return _data(Image.open(path).convert('RGB').resize((s, s)))


def colour_dist(a, b):
    return sum(abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])
               for x, y in zip(a, b)) / len(a)


def signature(path):
    """Both halves. A pair is the same picture only when both agree."""
    return {'d': dhash(path), 'c': colour_sig(path)}


def compare(sa, sb):
    return bin(sa['d'] ^ sb['d']).count('1'), colour_dist(sa['c'], sb['c'])


def same(sa, sb):
    d, c = compare(sa, sb)
    return d <= THRESH_SAME and c <= THRESH_COLOUR


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
            H[p] = signature(p)
        except Exception as e:
            print(f"   skip {p}: {e}")
    pairs = []
    for a, b in itertools.combinations(sorted(H), 2):
        d, c = compare(H[a], H[b])
        if d <= THRESH_LOOK and c <= THRESH_COLOUR:
            pairs.append((d, c, a, b))
    print(f"\nNEAR-DUPLICATE PAIRS (dhash <= {THRESH_SAME} and colour "
          f"<= {THRESH_COLOUR} is the same picture):")
    if not pairs:
        print("   none")
    for d, c, a, b in sorted(pairs):
        mark = "SAME  " if d <= THRESH_SAME else "check "
        print(f"   {mark}d={d:3d} col={c:5.1f}  {a}\n                        {b}")


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
