#!/usr/bin/env python3
"""ChatGPT's export of the Kraken saga -> data.json + the plates.

    py lesson-template/build/rpg/kraken-saga/extract-export.py [export.html]

**A sixth kind of export, and the second shape this saga has arrived in.**
rpg/README.md section 2 names three (Oz, Wonderland, patched-DATA) and
docs/HANDOFF-rpg.md section 3 adds "a script written here first", which is what
this is: STORY.md and IMAGES.md were written in this repo on 2026-09-12 and
ChatGPT was asked for the pictures and the hotspot boxes only.

The first return (2026-09-17) was a *saved web page* - `kraken.htm` plus a
`kraken_files/` folder - whose plates were not in it at all and had to be
fetched from a login-gated host. The second (2026-09-22) is one 39 MB HTML file
with everything inlined: `window.KRAKEN` (the text), `window.KRAKEN_SPOTS` (one
[cx, cy] per picture) and `window.KRAKEN_ASSETS` (79 base64 WebPs). This reads
either, because the three globals are the same shape in both.

**What the second return changed, all of it verified by diffing against the
data.json the published page was built from:**

  - Every plate redrawn at 1672x941, which is 16:9. They were 3:2, and a 3:2
    plate in a 16:9 window loses a sixth of its height to `object-fit:cover`,
    so the page had been letterboxing them. At 16:9 it fills the frame.
  - Twenty new `insert_*` plates feeding a new `panels` field on fourteen
    scenes: each reading page gets its own picture and its own label ("THE
    SCENE", "YOU HEAR", "THE BELL"). Where a scene has `panels`, the export is
    choosing the pages and the builder must not split the text itself.
  - The twenty-one prompts that used to arrive as `** "..."` with the
    speaker's name missing now carry it. repair_speaker() in the builder stays
    as a guard rather than a workaround.
  - Six scenes genuinely rewritten, 2.11 most heavily.
  - Two of fifty-five hotspot centres moved.

`FIXES` below is the one place this repo edits the export's English. Each entry
asserts its old text is present, so a re-export that changes the line fails
loudly here instead of silently dropping the correction.

Plates are written to kraken-black-tide-rpg/ at 1536x864 WebP under 200 KB -
the engine inlines nothing and the browser fetches one file per scene, so the
export's 200-590 KB originals would be 27 MB of page weight. `00_home.webp` is
Innes's own cover and is never in the export; it is left alone.
"""
import base64, io, json, os, re, sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
SLUG = 'kraken-black-tide-rpg'

DEFAULT_SRC = os.path.join(os.path.expanduser('~'), 'Downloads',
                           'KRAKEN_The_Black_Tide_Complete (5).html')
SRC = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC

TITLE = 'THE KRAKEN: A TALE OF THE DEEP'
HOME = '00_home.webp'
W, H = 1536, 864                 # 16:9, the ratio the plates now come in
MAX_BYTES = 200 * 1024
DEFAULT_BOX = (12.0, 16.0)       # spots give a centre only; the builder overrides

# Corrections to the export's English, applied at extract time so they survive
# a re-extract. (scene id, field, old fragment, new fragment).
FIXES = [
    ('1.3', 'dialogue',
     'Regatta Week is four hundred visitors and every bed in the village."',
     'Regatta Week is four hundred visitors and every bed in the village is occupied."'),
]


def grab(s, var):
    """`window.X = {...};` -> the JSON literal, found by matching brackets
    rather than by regex: the assets object is 39 MB of base64 and a greedy
    pattern over it is not worth waiting for."""
    m = re.search(r'window\.%s\s*=\s*' % re.escape(var), s)
    if not m:
        raise SystemExit('no `window.%s =` in %s' % (var, SRC))
    i = start = m.end()
    depth, instr, esc = 0, False, False
    backslash = chr(92)
    while i < len(s):
        c = s[i]
        if instr:
            if esc:
                esc = False
            elif c == backslash:
                esc = True
            elif c == '"':
                instr = False
        else:
            if c == '"':
                instr = True
            elif c in '{[':
                depth += 1
            elif c in '}]':
                depth -= 1
                if depth == 0:
                    return json.loads(s[start:i + 1])
        i += 1
    raise SystemExit('unterminated %s literal' % var)


def prep(raw, path):
    """Centre-crop to 16:9, resize, and walk quality down until it fits."""
    im = Image.open(io.BytesIO(raw)).convert('RGB')
    w, h = im.size
    if w / h > W / H:
        nw = int(h * W / H)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    elif w / h < W / H:
        nh = int(w * H / W)
        im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize((W, H), Image.LANCZOS)
    for q in range(88, 47, -4):
        im.save(path, 'WEBP', quality=q, method=6)
        if os.path.getsize(path) <= MAX_BYTES:
            return q
    return q


def main():
    if not os.path.exists(SRC):
        raise SystemExit('no export at %s' % SRC)
    s = io.open(SRC, encoding='utf-8', errors='replace').read()
    K = grab(s, 'KRAKEN')
    spots = grab(s, 'KRAKEN_SPOTS')
    assets = grab(s, 'KRAKEN_ASSETS')
    scenes = K['scenes']

    for sid, field, old, new in FIXES:
        cur = scenes[sid][field]
        if old not in cur:
            raise SystemExit('FIX for %s.%s no longer applies; its text has '
                             'changed in the export:\n  %r' % (sid, field, cur[:160]))
        scenes[sid][field] = cur.replace(old, new)
    print('applied %d correction(s) to the export text' % len(FIXES))

    art = os.path.join(REPO, SLUG)
    os.makedirs(art, exist_ok=True)
    for name, uri in sorted(assets.items()):
        raw = base64.b64decode(uri.split(',', 1)[1] if ',' in uri else uri)
        q = prep(raw, os.path.join(art, name))
        if q <= 52:
            print('  %-28s squeezed to q=%d' % (name, q))
    print('%d plates -> %s/ at %dx%d' % (len(assets), SLUG, W, H))
    if not os.path.exists(os.path.join(art, HOME)):
        raise SystemExit('%s/%s is missing - it is Innes\'s cover, not the '
                         'export\'s, and nothing here recreates it' % (SLUG, HOME))

    out = {'saga': TITLE, 'home': HOME, 'workingTitle': K['title'],
           'imgW': W, 'imgH': H, 'chapters': [], 'scenes': {}}

    for part in K['parts']:
        ids = list(part['sequence'])
        for sid in list(ids):
            for ch in scenes.get(sid, {}).get('choices', []) or []:
                for step in ch['path']:
                    if step not in ids:
                        ids.append(step)

        out['chapters'].append(
            {'part': part['number'], 'title': part['title'], 'label': part['label'],
             'lead': part['lead'], 'cover': part['cover'], 'items': part['items'],
             'rules': part['rules'], 'endings': part['endings'],
             'sequence': part['sequence']})

        for sid in ids:
            sc = dict(scenes[sid])
            cx, cy = spots[str(sc['picture'])]
            sc['hot'] = [round(cx * 100, 1), round(cy * 100, 1), *DEFAULT_BOX]
            sc['chapter'] = part['number']
            out['scenes'][sid] = sc

        q = sum(1 for sid in ids if scenes[sid]['kind'] in ('CCQ', 'GRAMMAR'))
        p = sum(1 for sid in ids if scenes[sid].get('panels'))
        print('part %d %-12s %2d scenes, %2d questions, %2d with authored panels'
              % (part['number'], part['title'], len(ids), q, p))

    with open(os.path.join(HERE, 'data.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')
    print('data.json - %d scenes, %d chapters' % (len(out['scenes']), len(out['chapters'])))


if __name__ == '__main__':
    main()
