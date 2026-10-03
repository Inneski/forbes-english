"""Which soundtrack each Block Camp page plays, and the one place that writes
the <script> tag for it.

block-camp/music/loops.json maps a track name to its loop points, [start, end]
in seconds; synthkit.finish() (and lakeside.py) keep it current. TRACK maps a
page to a track. set_music() replaces whatever camp-music tag a page carries
with the right one, or removes it.

Why a helper and not a hand edit: camp 9 (lesson-template/camp/build_camp.py)
and the nine descent stations (lesson-template/descent/build_descent.py) are
built from a published Part I deck used as a chassis, copied tail and all. A
rebuild used to inherit the chassis's music (Past Perfect would have played
Past Simple's "Lakeside") and its CLIP SUBTITLES block (a CC menu for clips it
does not have). Both builders now call set_music() and strip_clip_subs().

    py lesson-template/build/block-camp-music/deck_music.py          # wire every page in TRACK
    py lesson-template/build/block-camp-music/deck_music.py --check  # report pages that differ
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
LOOPS = os.path.join(ROOT, 'block-camp', 'music', 'loops.json')

# page (repo-relative) -> track name in block-camp/music/<name>.m4a
TRACK = {
    'blockcamp-present-simple.html': 'present-simple',
    'blockcamp-present-simple-2.html': 'present-simple',
    'blockcamp-present-continuous.html': 'present-continuous',
    'blockcamp-present-continuous-2.html': 'present-continuous',
    'blockcamp-past-simple.html': 'past-simple',
    'blockcamp-past-simple-2.html': 'past-simple',
    'blockcamp-past-continuous.html': 'past-continuous',
    'blockcamp-past-continuous-2.html': 'past-continuous',
    'blockcamp-going-to.html': 'going-to',
    'blockcamp-going-to-2.html': 'going-to',
    'blockcamp-future-simple.html': 'future-simple',
    'blockcamp-future-simple-2.html': 'future-simple',
    'blockcamp-present-perfect.html': 'present-perfect',
    'blockcamp-present-perfect-2.html': 'present-perfect',
    'blockcamp-present-perfect-continuous.html': 'present-perfect-continuous',
    'blockcamp-present-perfect-continuous-2.html': 'present-perfect-continuous',
    'blockcamp-past-perfect.html': 'past-perfect',
    'blockcamp-passive-present-simple.html': 'passive-present-simple',
    'blockcamp-passive-present-continuous.html': 'passive-present-continuous',
    'blockcamp-passive-past-simple.html': 'passive-past-simple',
    'blockcamp-passive-past-continuous.html': 'passive-past-continuous',
    'blockcamp-passive-going-to.html': 'passive-going-to',
    'blockcamp-passive-future-simple.html': 'passive-future-simple',
    'blockcamp-passive-present-perfect.html': 'passive-present-perfect',
    'blockcamp-passive-trial.html': 'passive-trial',
    'blockcamp-passive-past-perfect.html': 'passive-past-perfect',
    # the hub, block-camp.html: its own theme (theme.py)
    'block-camp.html': 'block-camp-theme',
    # the two route maps: one mountain-flute atmosphere (summit.py)
    'block-camp-map.html': 'route-map',
    'block-camp-descent-map.html': 'route-map',
    # The Last Night at the Grand Hotel, the first RPG with a soundtrack
    # (grand_hotel.py). Innes, 2026-10-03: "add some fitting music".
    'block-camp/grand-hotel-rpg.html': 'grand-hotel',
}

# Sherpa Tensing (the Himalayan tense climb, built by build_sherpa.py): the
# route maps' mountain flute on every page. Innes, 2026-10-01: "the music on
# block-camp-descent-map would be good on sherpa tensing".
import glob as _glob
for _f in sorted(_glob.glob(os.path.join(ROOT, 'sherpa-tensing*.html'))):
    TRACK[os.path.basename(_f)] = 'route-map'

MUSIC_TAG = re.compile(r'\n?<script src="[^"]*camp-music\.js"[^>]*></script>')
NAV_TAG = re.compile(r'<script src="([^"]*)camp-nav\.js"[^>]*></script>')
SUBS = re.compile(r'<!-- CLIP SUBTITLES -->.*?<!-- /CLIP SUBTITLES -->\n?', re.S)


def loops():
    try:
        return json.load(open(LOOPS, encoding='utf-8'))
    except FileNotFoundError:
        return {}


def prefix_for(page):
    """block-camp/ as seen from the page: 'block-camp/' from the root decks,
    '' from the RPGs, which live in block-camp/ themselves."""
    rel = os.path.relpath(os.path.join(ROOT, 'block-camp'), os.path.dirname(os.path.join(ROOT, page)))
    return '' if rel == '.' else rel.replace(os.sep, '/') + '/'


def music_tag(page):
    name = TRACK.get(page)
    lp = loops().get(name) if name else None
    if not name or not lp or not os.path.exists(os.path.join(ROOT, 'block-camp', 'music', name + '.m4a')):
        return ''
    p = prefix_for(page)
    # Six decimals, not %g: a loop of 67.166667 s written as 67.1667 puts the
    # seam 1.6 samples off and the loop ticks every lap.
    fmt = lambda x: ('%.6f' % x).rstrip('0').rstrip('.')
    return (f'<script src="{p}camp-music.js" data-track="{p}music/{name}.m4a" '
            f'data-loop="{fmt(lp[0])} {fmt(lp[1])}" defer></script>')


def set_music(html, page):
    """Remove any camp-music tag, then put this page's in: after camp-nav.js
    in a deck, before </body> in an RPG (which inlines its other scripts)."""
    html = MUSIC_TAG.sub('', html)
    tag = music_tag(page)
    if not tag:
        return html
    m = NAV_TAG.search(html)
    if m:
        return html[:m.end()] + '\n' + tag + html[m.end():]
    i = html.rfind('</body>')
    if i < 0:
        raise SystemExit(f'{page}: nowhere to put the music tag')
    return html[:i] + tag + '\n' + html[i:]


def strip_clip_subs(html):
    """A chassis's subtitle layer is for ITS clips. A page with none drops it."""
    if 'data-clip=' in html:
        return html
    return SUBS.sub('', html)


def main():
    check = '--check' in sys.argv
    bad = 0
    for page in sorted(TRACK):
        path = os.path.join(ROOT, page)
        s = open(path, encoding='utf-8', newline='').read()
        out = set_music(s, page)
        if out != s:
            if check:
                print('DIFFERS', page); bad += 1
            else:
                open(path, 'w', encoding='utf-8', newline='').write(out); print('wired', page, '->', TRACK[page])
        if not music_tag(page):
            print('NO TRACK YET', page, TRACK[page])
    if check:
        print('PASS' if not bad else f'{bad} page(s) differ')
        return 1 if bad else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
