#!/usr/bin/env python3
"""Which catalogued lessons are still scrolling pages, and what artwork do they own?

Regenerates the measurement behind `docs/ART-SHOPPING-LIST.md`. Reads only what is
in git — no network, no Supabase — so it gives the same answer in a cloud session
as on Innes's machine.

    python3 tools/audit-artwork.py              # the summary table
    python3 tools/audit-artwork.py --blocked    # the lessons with no usable image
    python3 tools/audit-artwork.py --topups     # the ones with 1-4, for the §5c check
    python3 tools/audit-artwork.py --json       # everything, machine-readable

A lesson is a DECK if it has `<section class="slide` and `fitStage`; an RPG if it
carries a `window.*_GAME_DATA`. Sherpa Tensing, the Block Camp time-signals pages,
Sailing the Seas and the .pptx deck-viewers are deliberately not decks and are
excluded from the scrolling count.

Artwork is found three ways — images the page references, the folder its
`LESSON_IMAGES` card points at, and any root artwork folder whose name matches the
lesson slug — and "usable" means at least 1400px wide (HOUSE-STYLE §3).

`FORBES ENGLISH/` and `HOUSE STYLE/` are excluded from name matching. They are brand
and reference dumps, and matching `forbes-english-*` against `FORBES ENGLISH/` makes
eighteen lessons look supplied when they own nothing.
"""
import argparse, json, os, re, struct, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_HERO_W = 1400
SKIP_WALK = {'.git', 'node_modules', 'lesson-template', 'tools', 'docs', '.claude',
             'block-camp', 'incoming'}
SKIP_MATCH = {'FORBES ENGLISH', 'HOUSE STYLE', 'LibraryCards', 'BlockCamp',
              'BlockCampDescent', 'minecraft'}
NOT_A_DECK = re.compile(r'sherpa-tensing|-time-signals|sailing-the-seas|deck-viewer'
                        r'|future-simple-will|going-to-infinitive|block-camp')
IMG_REF = re.compile(
    r'''(?:src|href)\s*=\s*["']([^"']+\.(?:jpg|jpeg|png|webp))["']'''
    r'''|url\(\s*['"]?([^)'"]+\.(?:jpg|jpeg|png|webp))'''
    r'''|data-bg\s*=\s*["']([^"']+)["']''', re.I)


def img_size(path):
    """(width, height) from the file header. None if it cannot be read."""
    try:
        with open(path, 'rb') as f:
            head = f.read(32)
            if head[:8] == b'\x89PNG\r\n\x1a\n':
                return struct.unpack('>II', head[16:24])
            if head[:2] == b'\xff\xd8':
                f.seek(2)
                while True:
                    b = f.read(1)
                    if not b:
                        return None
                    if b != b'\xff':
                        continue
                    while b == b'\xff':
                        b = f.read(1)
                    m = b[0]
                    if m in (0xd8, 0xd9) or 0xd0 <= m <= 0xd7:
                        continue
                    ln = struct.unpack('>H', f.read(2))[0]
                    if 0xc0 <= m <= 0xcf and m not in (0xc4, 0xc8, 0xcc):
                        h, w = struct.unpack('>HH', f.read(5)[1:5])
                        return w, h
                    f.seek(ln - 2, 1)
    except Exception:
        return None
    return None


def norm(s):
    return re.sub(r'[^a-z0-9]+', '', s.lower())


def scan_folders():
    out = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        rel = '' if rel == '.' else rel
        if rel.split(os.sep)[0] in SKIP_WALK:
            dirnames[:] = []
            continue
        imgs = [f for f in filenames if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        if imgs:
            out[rel] = [(f, img_size(os.path.join(dirpath, f))) for f in sorted(imgs)]
    return out


def lesson_images():
    lib = open(os.path.join(ROOT, 'library.html'), encoding='utf-8').read()
    return dict(re.findall(r'"([^"]+\.html)":\s*"([^"]+)"', lib[lib.index('LESSON_IMAGES'):]))


def audit():
    cat = json.load(open(os.path.join(ROOT, 'tools/lessons.json'), encoding='utf-8'))
    folders = scan_folders()
    cards = lesson_images()
    usable = {k: [f for f, s in v if s and s[0] >= MIN_HERO_W] for k, v in folders.items()}
    match_pool = {k: norm(k) for k in folders if k and os.sep not in k and k not in SKIP_MATCH}

    rows = []
    for e in cat:
        path = os.path.join(ROOT, e['file'])
        if not os.path.exists(path):
            rows.append(dict(e, kind='missing'))
            continue
        src = open(path, encoding='utf-8', errors='replace').read()
        if 'GAME_DATA' in src or e['file'].startswith('block-camp/'):
            kind = 'rpg'
        elif re.search(r'<section class="slide', src) and 'fitStage' in src:
            kind = 'deck'
        elif NOT_A_DECK.search(e['file']):
            kind = 'not-a-deck family'
        elif re.search(r'<section class="slide', src):
            kind = 'deck?'
        else:
            kind = 'scroll'

        dirs, refs = set(), []
        for m in IMG_REF.finditer(src):
            u = (m.group(1) or m.group(2) or m.group(3) or '').lstrip('/')
            if not u or u.startswith(('http', 'data:')):
                continue
            if os.path.exists(os.path.join(ROOT, u)):
                refs.append(u)
                if os.path.dirname(u) not in ('', 'LibraryCards'):
                    dirs.add(os.path.dirname(u))
        card = cards.get(e['file'])
        if card and os.path.dirname(card) not in ('', 'LibraryCards'):
            dirs.add(os.path.dirname(card))
        slug = norm(e['file'].rsplit('.', 1)[0])
        for k, n in match_pool.items():
            if len(n) >= 5 and (n in slug or slug in n):
                dirs.add(k)

        pool = sorted({(d, f) for d in dirs for f in usable.get(d, [])})
        pool += [(os.path.dirname(u), os.path.basename(u)) for u in refs
                 if (img_size(os.path.join(ROOT, u)) or (0, 0))[0] >= MIN_HERO_W
                 and os.path.dirname(u) not in dirs]
        rows.append(dict(e, kind=kind, card=card, dirs=sorted(dirs),
                         usable=sorted(set(pool)), n=len(set(pool))))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--blocked', action='store_true', help='lessons with no usable image')
    ap.add_argument('--topups', action='store_true', help='scrolling lessons with 1-4 images')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    rows = audit()
    if args.json:
        json.dump(rows, sys.stdout, indent=1)
        return

    scroll = [r for r in rows if r['kind'] == 'scroll']
    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1

    if args.blocked or args.topups:
        lo, hi = (0, 0) if args.blocked else (1, 4)
        sel = [r for r in scroll if lo <= r['n'] <= hi]
        for r in sorted(sel, key=lambda r: (r['level'] or '', r['file'])):
            art = r['card'] or '-'
            print(f"{r['level'] or '?':<6} {r['access']:<5} {r['file']:<58} "
                  f"usable={r['n']:<3} {art}")
        print(f"\n{len(sel)} lessons")
        return

    print(f"catalogued lessons        {len(rows)}")
    for k in sorted(kinds):
        print(f"  {k:<24} {kinds[k]}")
    print("\nscrolling lessons by usable artwork (>=%dpx wide)" % MIN_HERO_W)
    for label, lo, hi in [('none', 0, 0), ('one', 1, 1), ('two to four', 2, 4),
                          ('five or more', 5, 10 ** 6)]:
        print(f"  {label:<14} {sum(1 for r in scroll if lo <= r['n'] <= hi)}")


if __name__ == '__main__':
    main()
