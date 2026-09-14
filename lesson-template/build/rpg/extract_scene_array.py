#!/usr/bin/env python3
"""Pull the text and pictures out of a `const SCENES=[...]` RPG export.

    python3 lesson-template/build/rpg/extract_scene_array.py <export.html> <slug>

The fifth kind of export (Frostbound: The River Remembers, 2026-09-14). It is
the Oz kind turned inside out: instead of one `window.*_GAME_DATA` object with
a separate `images` map, the whole game is a flat `const SCENES=[...]` array
and every scene carries its own picture inline as a `data:image/webp` URI on
an `image` key, with the prompt that made it on `art` and the same text again
on `alt`.

There is no `window.*` global and no `images` map, so `extract_standalone.py`
finds nothing. This script:

  * writes every scene's picture to `block-camp/<slug>/NN_<id>.webp`, numbered
    in array order — the export gives the pictures no names of their own;
  * writes the scenes minus the base64 to
    `lesson-template/build/rpg/<slug>/data.json`;
  * prints one line per scene — id, picture, kind, the object the export
    names — which is the list you fill the hotspot table from (README §3).

The export's `object` key is a gift the Oz kind does not give: it names the
glowing thing the art was drawn around, so the hotspot hunt starts from a
name rather than a guess. It still needs eyes for the coordinates.
"""
import base64, json, os, re, struct, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))


def webp_size(b):
    if b[12:16] == b'VP8X':
        return int.from_bytes(b[24:27], 'little') + 1, int.from_bytes(b[27:30], 'little') + 1
    if b[12:16] == b'VP8 ':
        return struct.unpack('<H', b[26:28])[0] & 0x3fff, struct.unpack('<H', b[28:30])[0] & 0x3fff
    if b[12:16] == b'VP8L':
        n = int.from_bytes(b[21:25], 'little')
        return (n & 0x3fff) + 1, ((n >> 14) & 0x3fff) + 1
    return None


def array_after(s, i):
    """Slice the bracket-balanced array literal starting at s[i] == '['."""
    depth, instr, esc, j = 0, False, False, i
    while j < len(s):
        c = s[j]
        if instr:
            if esc:
                esc = False
            elif c == chr(92):
                esc = True
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True
        elif c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                return s[i:j + 1]
        j += 1
    raise SystemExit('unbalanced SCENES array')


def main(src, slug):
    s = open(src, encoding='utf-8').read()
    m = re.search(r'const\s+SCENES\s*=\s*\[', s)
    if not m:
        raise SystemExit('no `const SCENES=[` in %s — try extract_standalone.py' % src)
    scenes = json.loads(array_after(s, m.end() - 1))
    img_dir = os.path.join(REPO, 'block-camp', slug)
    os.makedirs(img_dir, exist_ok=True)
    sizes = set()
    for n, sc in enumerate(scenes, 1):
        uri = sc.pop('image', '')
        if not uri.startswith('data:image/'):
            raise SystemExit('scene %s has no inline picture' % sc.get('id'))
        b = base64.b64decode(uri.split(',', 1)[1])
        name = '%02d_%s.webp' % (n, sc['id'])
        open(os.path.join(img_dir, name), 'wb').write(b)
        sc['image'] = name
        sizes.add(webp_size(b))
    print('SCENES: %d pictures -> block-camp/%s/  sizes %s' % (len(scenes), slug, sorted(sizes, key=str)))
    if sizes - {(1536, 1024)}:
        print('  ! not 3:2 at 1536x1024 — pass img_w/img_h in the spec so the hotspots land')
    out_dir = os.path.join(HERE, slug)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'data.json')
    json.dump(scenes, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('text -> %s' % os.path.relpath(out, REPO))
    print('\nscenes (fill HOT from a gridded contact sheet):')
    for sc in scenes:
        print('  %-14s %-26s %-7s %-6s object: %s' % (
            sc['id'], sc['image'], sc.get('side'), sc.get('kind'), sc.get('object')))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
