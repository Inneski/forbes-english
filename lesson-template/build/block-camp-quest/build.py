#!/usr/bin/env python3
"""Block Camp: The Quest — the overworld that turns the camp into one game.

    python3 lesson-template/build/block-camp-quest/build.py

Writes block-camp/quest.html (the game screen) plus the three files that make
it installable: block-camp/manifest.webmanifest, block-camp/sw.js and the two
icons in block-camp/quest-icons/. Nothing here is lesson content: the page
reads the learner's save file (block-camp/camp-save.js, which every RPG and
deck writes to) and draws the camp as a map — the climb, the descent and the
adventures — with each stop lit by how far they have got.

The camps, stations and adventures are the hub builder's own tables
(block-camp-hub/build.py: CAMP, CLIMB, DESCENT, ADVENTURES), imported, so a
new adventure added to the hub appears on the map on the next build without a
second list to keep in step. An adventure is hung off the camp whose tense it
teaches (its first grammar chip); one with no camp of its own — conditionals,
narrative tenses — hangs off the tower at the top.

The nav band and the Monocraft subset are the hub's, with the links rewritten
for a page that lives one directory down.
"""
import importlib.util, json, os, re, struct, sys, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
HUB = os.path.join(HERE, '..', 'block-camp-hub')
OUT_DIR = os.path.join(REPO, 'block-camp')

spec = importlib.util.spec_from_file_location('hub', os.path.join(HUB, 'build.py'))
hub = importlib.util.module_from_spec(spec); spec.loader.exec_module(hub)

def present(p): return os.path.exists(os.path.join(REPO, p))
def up(p): return '../' + p                      # a root-relative asset, seen from block-camp/
def unescape(s): return s.replace('&rsquo;', '’').replace('&mdash;', '—').replace('&ndash;', '–').replace('&amp;', '&')

# ---- the map data ---------------------------------------------------------
camps = []
for n, name, slug, l1, l2 in hub.CLIMB:
    parts = []
    if present(f'blockcamp-{slug}.html'):
        parts.append({'id': f'blockcamp-{slug}', 'href': up(f'blockcamp-{slug}.html'), 'label': 'Part 1', 'level': l1,
                      'access': 'free' if (n, 1) in hub.FREE_CLIMB else 'pro', 'img': up(f'BlockCamp/{slug}-1a.jpg')})
    if present(f'blockcamp-{slug}-2.html'):
        parts.append({'id': f'blockcamp-{slug}-2', 'href': up(f'blockcamp-{slug}-2.html'), 'label': 'Part 2', 'level': l2,
                      'access': 'pro', 'img': up(f'BlockCamp/{slug}-1b.jpg')})
    if parts:
        camps.append({'n': n, 'name': name, 'slug': slug, 'colour': hub.CAMP[n], 'ink': hub.INK[n], 'parts': parts})

stations = []
for st, camp, name, slug, lvl, acc in hub.DESCENT:
    if not present(f'blockcamp-passive-{slug}.html'): continue
    stations.append({'st': st, 'camp': camp, 'name': name, 'id': f'blockcamp-passive-{slug}', 'href': up(f'blockcamp-passive-{slug}.html'),
                     'colour': hub.CAMP[camp] if camp else '#e8c04a', 'ink': hub.INK[camp] if camp else '#0b1a12',
                     'level': lvl, 'access': acc, 'img': up(f'BlockCamp/passive-{st}-{slug}.jpg'), 'trial': not camp})

by_name = {name: n for n, name, *_ in hub.CLIMB}
by_name['Future Simple: Will'] = by_name['Future Simple']
adventures = []
for href, img, title, desc, gram, lvl, acc, tag in hub.ADVENTURES:
    if not present(href): continue
    pid = re.sub(r'\.html$', '', href.split('/')[-1])
    adventures.append({'id': pid, 'href': href.split('/', 1)[1] if href.startswith('block-camp/') else up(href),
                       'img': img.split('/', 1)[1] if img.startswith('block-camp/') else up(img),
                       'title': unescape(title), 'desc': unescape(desc), 'gram': list(gram), 'level': unescape(lvl), 'access': acc,
                       'camp': by_name.get(gram[0])})

DATA = {'camps': camps, 'stations': stations, 'adventures': adventures}

# ---- the icons: a pixel tent, written without PIL ---------------------------
TENT = """
................
................
.......G........
......GG........
......G.........
......G.........
.....YYY........
....YYYYY.......
...YYYYYYY......
..YYYYYYYYY.....
.YYYYYDDYYYY....
YYYYYDDDDYYYYY..
gggggggggggggggg
gggggggggggggggg
................
................""".strip('\n').split('\n')
PAL = {'.': (20, 48, 31, 255), 'G': (232, 192, 74, 255), 'Y': (232, 192, 74, 255), 'D': (11, 26, 18, 255), 'g': (35, 74, 51, 255)}

def png(size):
    n = len(TENT); k = size // n
    rows = []
    for y in range(size):
        line = bytearray([0])
        src = TENT[min(n - 1, y // k)]
        for x in range(size):
            line += bytes(PAL[src[min(n - 1, x // k)]])
        rows.append(bytes(line))
    raw = b''.join(rows)
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))

# ---- assemble --------------------------------------------------------------
def build():
    rd = lambda d, n: open(os.path.join(d, n), encoding='utf-8').read()
    nav = rd(HUB, 'nav.html')
    nav = re.sub(r'href="(?!https?:|mailto:|#|\.\./)([^"]+)"', r'href="../\1"', nav)
    nav = re.sub(r'src="(?!https?:|data:|\.\./)([^"]+)"', r'src="../\1"', nav)
    nav = nav.replace('href="../block-camp.html" aria-current="page"', 'href="../block-camp.html"')
    page = (rd(HERE, 'template.html')
            .replace('{{MONOCRAFT}}', rd(HUB, 'monocraft.css'))
            .replace('{{NAV}}', nav)
            .replace('{{DATA}}', json.dumps(DATA, ensure_ascii=False, separators=(',', ':')))
            .replace('{{N_CAMPS}}', str(len(camps))).replace('{{N_STATIONS}}', str(len(stations))).replace('{{N_ADV}}', str(len(adventures))))
    out = os.path.join(OUT_DIR, 'quest.html')
    open(out, 'w', encoding='utf-8', newline='\n').write(page)

    icons = os.path.join(OUT_DIR, 'quest-icons'); os.makedirs(icons, exist_ok=True)
    for size in (192, 512):
        open(os.path.join(icons, f'icon-{size}.png'), 'wb').write(png(size))
    manifest = {
        'name': 'Block Camp: The Quest', 'short_name': 'Block Camp', 'id': '/block-camp/quest.html',
        'start_url': 'quest.html', 'scope': '/block-camp/', 'display': 'standalone', 'orientation': 'any',
        'background_color': '#14301f', 'theme_color': '#14301f',
        'description': 'The English tense journey as a game: climb the camps, clear the adventures, collect every tile.',
        'icons': [{'src': 'quest-icons/icon-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'},
                  {'src': 'quest-icons/icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any maskable'}]}
    open(os.path.join(OUT_DIR, 'manifest.webmanifest'), 'w', encoding='utf-8', newline='\n').write(json.dumps(manifest, indent=2) + '\n')
    # the worker: network first, cache as fallback, scoped to block-camp/ so
    # it can never serve a stale copy of anything outside the game
    open(os.path.join(OUT_DIR, 'sw.js'), 'w', encoding='utf-8', newline='\n').write(rd(HERE, 'sw.js'))
    print('wrote block-camp/quest.html — %d camps, %d stations, %d adventures; manifest, sw.js, 2 icons'
          % (len(camps), len(stations), len(adventures)))

if __name__ == '__main__':
    build()
