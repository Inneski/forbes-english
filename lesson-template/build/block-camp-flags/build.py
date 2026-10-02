#!/usr/bin/env python3
"""Block Camp flags: an achievement record of the flags a learner has planted
on every camp of the climb and every station of the descent.

    py lesson-template/build/block-camp-flags/build.py            # write both
    py lesson-template/build/block-camp-flags/build.py --check    # exit 1 if stale

Innes, 2026-10-02: "Users need some kind of achievement record of flags
obtained from all the camps."

Writes two files:

  block-camp/camp-flags.js   from template.js - window.CampFlags: the flag
                             table, the rule, the record, the pixel sprite and
                             the route-map decorations. Loaded by camp-end.js
                             on every deck, by both route maps and by
                             flags.html.
  block-camp/flags.html      from template.html - "Your flags", the record
                             page: eighteen flags in two rows.

THE TABLE IS THE HUB'S. Camps, stations, names and colours are
block-camp-hub/build.py's CLIMB, DESCENT, CAMP and INK, imported the way the
quest and camp-nav builders import them, so the flags cannot disagree with the
hub cards, the quest or the deck buttons. (The two hand-kept route maps paint
camp 9 #6E0B24 and the Trial #46B0AB; the flags follow the hub, #d66d77 and
gold, like everything generated.) A camp or station appears only once its
deck exists, as on the hub.

THE RULE (template.js, PASS and GOLD):
  - a flag is planted when the camp's Part 1 (or the station's deck) reaches
    its Results slide with a score of 50% or more;
  - it carries a star when Part 2 does the same (camps with a Part 2 only:
    the flags with no Part 2 have no star slot at all);
  - it goes gold when Part 1 (or the station) scores 75% or more.
  Recorded at the Results slide, kept as the best score per deck, and latched:
  a later lower score, a deck rebuilt with more slides, or a Part 2 that lands
  later never takes a flag back. This is deliberately not the quest's "Camp
  pitched" badge (every part paged to the last slide, score-blind).

THE SAVE: the record lives in the learner's CampSave file under a new
top-level key, 'flags' = { pageId: {best, max, pct, plays, firstAt, lastAt,
pass, gold} }, written with CampSave.get/put. camp-save.js is not changed:
format v1 and MAGIC stay as they are, because twelve RPGs inline a copy of it
and a bump would wipe every save; the old copies keep unknown keys. So the
flags travel with the quest page's save code like the village's rangers do.
"""
import importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
HUB = os.path.join(REPO, 'lesson-template', 'build', 'block-camp-hub')
OUT_JS = os.path.join(REPO, 'block-camp', 'camp-flags.js')
OUT_HTML = os.path.join(REPO, 'block-camp', 'flags.html')

spec = importlib.util.spec_from_file_location('hub', os.path.join(HUB, 'build.py'))
hub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hub)

# The Trial has no camp of its own: gold, as on the hub card (build.py
# descent_cards), the quest and the deck buttons (block-camp-nav TRIAL).
TRIAL = ('#e8c04a', '#0b1a12')


def table():
    rows = []
    for n, name, slug, _l1, _l2 in hub.CLIMB:
        p1, p2 = 'blockcamp-%s' % slug, 'blockcamp-%s-2' % slug
        if not hub.present(p1 + '.html'):
            continue
        parts = [p1] + ([p2] if hub.present(p2 + '.html') else [])
        rows.append({'key': 'climb-%d' % n, 'line': 'climb', 'n': n, 'label': name,
                     'colour': hub.CAMP[n], 'ink': hub.INK[n], 'parts': parts,
                     'href': p1 + '.html', 'href2': (p2 + '.html') if len(parts) > 1 else None})
    for st, camp, name, slug, _lvl, _acc in hub.DESCENT:
        p = 'blockcamp-passive-%s' % slug
        if not hub.present(p + '.html'):
            continue
        colour, ink = (hub.CAMP[camp], hub.INK[camp]) if camp else TRIAL
        rows.append({'key': 'descent-%d' % st, 'line': 'descent', 'n': st, 'label': name,
                     'colour': colour, 'ink': ink, 'parts': [p], 'href': p + '.html',
                     'href2': None, 'trial': not camp})
    return rows


def tiles(rows, line):
    """The static markup of one row of flags. The sprite slot is filled at
    runtime (camp-flags.js draws it); the text and the links are here so the
    page reads without script."""
    out = []
    for r in rows:
        if r['line'] != line:
            continue
        what = 'Camp %d' % r['n'] if line == 'climb' else ('Station %d' % r['n'])
        links = '<a class="pt" href="../%s">%s</a>' % (r['href'], 'Part 1' if r['href2'] else 'Open')
        if r['href2']:
            links += '<a class="pt" href="../%s">Part 2</a>' % r['href2']
        out.append(
            '<li class="fl locked" data-key="%s" style="--c:%s;--ci:%s">'
            '<span class="art" aria-hidden="true"></span>'
            '<span class="no mono">%s</span>'
            '<span class="nm">%s</span>'
            '<span class="st">Not planted yet</span>'
            '<span class="bs"></span>'
            '<span class="pts">%s</span></li>'
            % (r['key'], r['colour'], r['ink'], what.upper(), r['label'], links))
    return '\n      '.join(out)


def render():
    rd = lambda d, n: open(os.path.join(d, n), encoding='utf-8').read()
    rows = table()
    data = json.dumps(rows, ensure_ascii=False, separators=(',', ':'))
    js = rd(HERE, 'template.js').replace('{{TABLE}}', data)

    nav = rd(HUB, 'nav.html')
    nav = re.sub(r'href="(?!https?:|mailto:|#|\.\./)([^"]+)"', r'href="../\1"', nav)
    nav = re.sub(r'src="(?!https?:|data:|\.\./)([^"]+)"', r'src="../\1"', nav)
    nav = nav.replace('href="../block-camp.html" aria-current="page"', 'href="../block-camp.html"')
    n_climb = sum(r['line'] == 'climb' for r in rows)
    n_desc = sum(r['line'] == 'descent' for r in rows)
    n_star = sum(1 for r in rows if len(r['parts']) > 1)
    html = (rd(HERE, 'template.html')
            .replace('{{MONOCRAFT}}', rd(HUB, 'monocraft.css'))
            .replace('{{NAV}}', nav)
            .replace('{{CLIMB}}', tiles(rows, 'climb'))
            .replace('{{DESCENT}}', tiles(rows, 'descent'))
            .replace('{{N_CLIMB}}', str(n_climb))
            .replace('{{N_DESCENT}}', str(n_desc))
            .replace('{{N_STAR}}', str(n_star))
            .replace('{{N_ALL}}', str(len(rows))))
    return js, html, rows


def main():
    js, html, rows = render()
    pairs = ((OUT_JS, js), (OUT_HTML, html))
    if '--check' in sys.argv:
        stale = []
        for path, text in pairs:
            try:
                cur = open(path, encoding='utf-8', newline='').read()
            except OSError:
                cur = None
            if cur != text:
                stale.append(os.path.relpath(path, REPO))
        if stale:
            print('STALE: ' + ', '.join(stale) + ' - run lesson-template/build/block-camp-flags/build.py')
            sys.exit(1)
        print('OK: camp-flags.js and flags.html match the hub tables (%d flags)' % len(rows))
        return
    for path, text in pairs:
        open(path, 'w', encoding='utf-8', newline='\n').write(text)
    print('wrote block-camp/camp-flags.js and block-camp/flags.html - %d climb, %d descent flags'
          % (sum(r['line'] == 'climb' for r in rows), sum(r['line'] == 'descent' for r in rows)))


if __name__ == '__main__':
    main()
