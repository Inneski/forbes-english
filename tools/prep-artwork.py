#!/usr/bin/env python3
"""Prepare new artwork for a lesson: resize, convert, and refuse duplicates.

Midjourney hands you 3-7 MB PNGs at odd sizes, four variants of the same grid,
and no memory of what this site already ships. This does the three things that
have to happen before any of it reaches a lesson folder:

  1. **Resize and convert** to the house spec — 2000px wide, JPEG q85,
     optimised (HOUSE-STYLE.md §3). A 7 MB PNG becomes a ~300 KB JPEG.
     Never upscales; a source under --min-width is reported and skipped.

  2. **Reject duplicates**, twice over: against every image already in the
     repo, and against the rest of the incoming batch (Midjourney's four-up
     variants are near-identical by design). This is the check that was
     missing on 2026-09-04, when three "fresh" scenes were adopted into
     MinecraftB1/ that Tense Review and Past Modals were already using.

  3. **Flag what will not work** — an aspect ratio that is not 16:9, or a
     picture too dark for a light-theme deck.

Why it matters that step 1 happens BEFORE the commit: `.git` is already
~700 MB with no LFS, and git never forgets a blob. Thirty-four raw PNGs add
~150 MB permanently; the same thirty-four at house spec add ~10 MB.

Usage:
    python3 tools/prep-artwork.py <src>... --into TenseReview
    python3 tools/prep-artwork.py incoming/ --into TenseReview --dry-run
    python3 tools/prep-artwork.py incoming/ --into TenseReview \\
            --names hero,plain,scaffold,castle

    --into <dir>      destination lesson folder (created if absent)
    --names a,b,c     final basenames, in order, instead of <folder>-01.jpg
    --dry-run         report only, write nothing
    --force           write even the files flagged as duplicates
    --width N         long edge, default 2000
    --quality N       JPEG quality, default 85 (house range is 82-88)
    --min-width N     refuse a source narrower than this, default 1400
    --against <dir>   extra folders to check against (repeatable).
                      Default is every image in the repo, cached by mtime.

Requires Pillow. Hash cache lives in tools/.artwork-hashes.json (gitignored).
"""
import argparse
import json
import warnings
import os
import subprocess
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(HERE, '.artwork-hashes.json')
EXTS = ('.jpg', '.jpeg', '.png', '.webp')

warnings.filterwarnings('ignore', category=DeprecationWarning, module='PIL')
warnings.filterwarnings('ignore', category=UserWarning, module='PIL')

# One implementation of the hash, in tools/image-audit.py. Load it by path
# because the filename has a hyphen and is not importable as a module name.
_spec = importlib.util.spec_from_file_location(
    'image_audit', os.path.join(HERE, 'image-audit.py'))
image_audit = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(image_audit)
ahash, THRESH_SAME = image_audit.ahash, image_audit.THRESH_SAME

# 16:9 is 1.778. Anything outside this band letterboxes or crops on the deck.
AR_LO, AR_HI = 1.70, 1.86
# Mean luminance below this is too dark for a light-theme deck (HOUSE-STYLE §4).
DARK_BELOW = 90


def show(path):
    """Repo-relative where that reads better, absolute where it does not."""
    rel = os.path.relpath(path, ROOT)
    return path if rel.startswith('..') else rel


def dist(a, b):
    return bin(a ^ b).count('1')


def stats(path):
    """(width, height, mean luminance 0-255) without decoding at full size."""
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    with Image.open(path) as im:
        w, h = im.size
        im.draft('L', (64, 64))
        small = im.convert('L').resize((32, 32))
        px = list(small.get_flattened_data()
                  if hasattr(small, 'get_flattened_data') else small.getdata())
    return w, h, sum(px) / len(px)


def repo_images(extra):
    """Every image in the repo (maxdepth 2), plus any --against folders."""
    out = []
    try:
        found = subprocess.run(
            ['find', ROOT, '-maxdepth', '2', '-type', 'f',
             '-not', '-path', '*/.git/*', '-not', '-path', '*/node_modules/*'],
            capture_output=True, text=True, timeout=60).stdout.split('\n')
        out += [p for p in found if p.lower().endswith(EXTS)]
    except Exception as e:
        print(f"  ! could not scan the repo ({e}); checking --against only")
    for d in extra:
        for f in sorted(os.listdir(d)):
            if f.lower().endswith(EXTS):
                out.append(os.path.join(d, f))
    return sorted(set(out))


def load_cache():
    try:
        with open(CACHE) as f:
            return json.load(f)
    except Exception:
        return {}


def hashes_for(paths, cache):
    """ahash per path, cached on (size, mtime) so only new files are decoded."""
    out, fresh, misses = {}, 0, []
    for p in paths:
        try:
            st = os.stat(p)
        except OSError:
            continue
        key, stamp = os.path.relpath(p, ROOT), f"{st.st_size}:{int(st.st_mtime)}"
        hit = cache.get(key)
        if hit and hit.get('stamp') == stamp:
            out[p] = hit['hash']
        else:
            misses.append((p, key, stamp))
    if misses:
        print(f"  hashing {len(misses)} new or changed image(s)...", flush=True)
    for p, key, stamp in misses:
        try:
            h = ahash(p)
        except Exception:
            continue
        out[p] = h
        cache[key] = {'stamp': stamp, 'hash': h}
        fresh += 1
    if fresh:
        try:
            with open(CACHE, 'w') as f:
                json.dump(cache, f)
        except OSError:
            pass
    return out


def sources(args_src):
    out = []
    for a in args_src:
        if os.path.isdir(a):
            out += [os.path.join(a, f) for f in sorted(os.listdir(a))
                    if f.lower().endswith(EXTS)]
        elif os.path.isfile(a):
            out.append(a)
        else:
            print(f"  ! not found: {a}")
    return out


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('src', nargs='*')
    ap.add_argument('--into')
    ap.add_argument('--names')
    ap.add_argument('--width', type=int, default=2000)
    ap.add_argument('--quality', type=int, default=85)
    ap.add_argument('--min-width', type=int, default=1400)
    ap.add_argument('--against', action='append', default=[])
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('-h', '--help', action='store_true')
    a = ap.parse_args()

    if a.help or not a.src or not a.into:
        print(__doc__)
        return 0 if a.help else 1

    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow is required:  pip install pillow --break-system-packages")
    Image.MAX_IMAGE_PIXELS = None

    src = sources(a.src)
    if not src:
        print("Nothing to do — no images in the source.")
        return 1

    dest = a.into if os.path.isabs(a.into) else os.path.join(ROOT, a.into)
    names = [n.strip() for n in a.names.split(',')] if a.names else None
    if names and len(names) != len(src):
        sys.exit(f"--names has {len(names)} entries for {len(src)} images.")

    print(f"== {len(src)} source image(s) -> {a.into}/ "
          f"at {a.width}px q{a.quality} ==\n")

    cache = load_cache()
    existing_paths = [p for p in repo_images(a.against)
                      if os.path.abspath(p) not in {os.path.abspath(s) for s in src}]
    existing = hashes_for(existing_paths, cache)
    incoming = hashes_for(src, cache)
    print()

    # Decide on every file first, so a --dry-run says exactly what a real run does.
    plan, kept_hashes = [], []
    for i, p in enumerate(src):
        try:
            w, h, lum = stats(p)
        except Exception as e:
            plan.append((p, None, f"SKIP  unreadable ({e})", []))
            continue
        hv, notes, verdict = incoming.get(p), [], None

        if hv is not None:
            match = min(((dist(hv, existing[q]), q) for q in existing),
                        default=(999, None))
            if match[0] <= THRESH_SAME:
                verdict = f"SKIP  already in the repo as {show(match[1])} (d={match[0]})"
            else:
                twin = min(((dist(hv, k), n) for k, n in kept_hashes), default=(999, None))
                if twin[0] <= THRESH_SAME:
                    verdict = f"SKIP  same picture as {twin[1]} earlier in this batch (d={twin[0]})"

        if w < a.min_width:
            # Also a note, so --force never writes an under-size file silently
            # when a duplicate verdict got there first.
            notes.append(f"only {w}px wide, house minimum is {a.min_width}")
            verdict = verdict or f"SKIP  only {w}px wide, house minimum is {a.min_width}"
        ar = w / h if h else 0
        if not (AR_LO <= ar <= AR_HI):
            notes.append(f"aspect {ar:.2f}, not 16:9 — it will crop on the deck")
        if lum < DARK_BELOW:
            notes.append(f"mean luminance {lum:.0f} — too dark for a light-theme deck")

        out_name = (names[i] if names else f"{os.path.basename(dest)}-{i + 1:02d}")
        if not out_name.lower().endswith('.jpg'):
            out_name += '.jpg'
        if verdict and not a.force:
            plan.append((p, None, verdict, notes))
        else:
            plan.append((p, os.path.join(dest, out_name),
                         ("FORCED " + verdict) if verdict else "write", notes))
            if hv is not None:
                kept_hashes.append((hv, out_name))

    writes = [r for r in plan if r[1]]
    if writes and not a.dry_run:
        os.makedirs(dest, exist_ok=True)

    saved_in = saved_out = 0
    for p, out, verdict, notes in plan:
        label = os.path.basename(p)
        if not out:
            print(f"  {verdict}\n        {label}")
        else:
            before = os.path.getsize(p)
            if a.dry_run:
                print(f"  would write  {show(out)}"
                      f"   ({before // 1024} KB source)")
            else:
                with Image.open(p) as im:
                    im = im.convert('RGB')
                    w, h = im.size
                    if w > a.width:
                        im = im.resize((a.width, round(a.width * h / w)),
                                       Image.LANCZOS)
                    im.save(out, 'JPEG', quality=a.quality, optimize=True)
                after = os.path.getsize(out)
                saved_in += before
                saved_out += after
                print(f"  wrote  {show(out)}"
                      f"   {before // 1024} KB -> {after // 1024} KB")
            if verdict != "write":
                print(f"        {verdict}")
        for n in notes:
            print(f"        ! {n}")

    skipped = len(plan) - len(writes)
    print(f"\n{len(writes)} written, {skipped} skipped.")
    if saved_in:
        print(f"{saved_in // 1024} KB -> {saved_out // 1024} KB "
              f"({100 - saved_out * 100 // saved_in}% smaller).")
    if writes and not a.dry_run:
        print(f"\nNext: point the builder's BG lists at the new names, re-run it, "
              f"then check-lesson.js, then tools/seo.py.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
