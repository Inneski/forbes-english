#!/usr/bin/env python3
"""Pull the text and pictures out of a standalone RPG export.

    python3 lesson-template/build/rpg/extract_standalone.py <export.html> <slug>

The exports Innes sends (the "Sherpa Yellow" / "Cybervoxel" generator: one
HTML file, 3–5 MB, every picture inlined as base64, the whole game in a
`window.*_GAME_DATA = {...}` object) are the raw material for a Block Camp
RPG, never the published page. This script:

  * writes every picture to `block-camp/<slug>/<name>.webp` — the names the
    export used, which are already numbered (01_cover.webp, 02_q1_….webp);
  * writes the game object minus the pictures to
    `lesson-template/build/rpg/<slug>/data.json`, which is what the lesson's
    builder reads;
  * prints one line per scene — id, picture, position, kind — which is the
    list you fill the hotspot table from (README.md §3).

It does not pick hotspots, write the rules briefing or the feedback lines:
those are the builder's job, because they need a person to look at the
pictures and know the grammar. Copy build_lost_yellow_road.py and edit it.
"""
import base64, json, os, re, struct, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))


def webp_size(b):
    if b[12:16] == b'VP8X':
        return int.from_bytes(b[24:27], 'little') + 1, int.from_bytes(b[27:30], 'little') + 1
    if b[12:16] == b'VP8 ':
        return struct.unpack('<H', b[26:28])[0] & 0x3fff, struct.unpack('<H', b[28:30])[0] & 0x3fff
    return None


def main(src, slug):
    s = open(src, encoding='utf-8').read()
    m = re.search(r'window\.(\w+_GAME_DATA)\s*=\s*(\{.*?\});?\s*</script>', s, re.S)
    if not m:
        raise SystemExit('no window.*_GAME_DATA object in %s — is this a generator export?' % src)
    data = json.loads(m.group(2))
    img_dir = os.path.join(REPO, 'block-camp', slug)
    os.makedirs(img_dir, exist_ok=True)
    sizes = set()
    for name, uri in data.pop('images', {}).items():
        b = base64.b64decode(uri.split(',', 1)[1])
        open(os.path.join(img_dir, name), 'wb').write(b)
        sizes.add(webp_size(b))
    print('%s: %d pictures -> block-camp/%s/  sizes %s' % (m.group(1), len(os.listdir(img_dir)), slug, sorted(sizes, key=str)))
    if sizes - {(1536, 1024)}:
        print('  ! not 3:2 at 1536x1024 — pass img_w/img_h in the spec so the hotspots land')
    out_dir = os.path.join(HERE, slug)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'data.json')
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('text -> %s' % os.path.relpath(out, REPO))
    print('langs in export:', [k for k in data.get('ui', {}) if k != 'off'])
    print('\nscenes (fill HOT from a gridded contact sheet):')
    for sid, sc in data.get('scenes', {}).items():
        kind = 'choice' if 'choices' in sc else 'question'
        print('  %-14s %-32s %-7s %s%s' % (sid, sc.get('image'), sc.get('position'), kind,
                                           '  relic' if sc.get('relic') else ''))
    for key, e in data.get('endings', {}).items():
        print('  %-14s %-32s %-7s ending' % ('end_' + key, e.get('image'), ''))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
