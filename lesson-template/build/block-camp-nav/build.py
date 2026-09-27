#!/usr/bin/env python3
"""Builds block-camp/camp-nav.js - the route-map button and the next-camp
button on every Block Camp deck - from template.js plus the route below.

    py lesson-template/build/block-camp-nav/build.py            # write it
    py lesson-template/build/block-camp-nav/build.py --check    # exit 1 if stale

Innes, 2026-09-27: "we need a navigational button on each level back to the
main camp at all times and to the next camp once you finish each camp".
template.js says what the two buttons do and why they sit where they do; this
file decides where they go.

THE ROUTE IS THE HUB'S. The order of the camps, their names and their colours
are block-camp-hub/build.py's CLIMB, DESCENT, CAMP and INK, imported the way
the quest builder imports them, so the hub, the overworld and these buttons
cannot disagree about which camp comes next or what colour it is. A deck
appears here only once its page exists, like a card on the hub.

THE NEXT CAMP IS THE NEXT STOP ON THE MAP. Both parts of camp N lead to camp
N+1's Part 1 - the stop the route map links - because Part 2 is already one
click away in the deck bar, and the free path through the line runs through
the Part 1s. The top of the climb leads into the descent, station 9; the end
of the descent leads to the adventures on the hub.

ACCESS IS THE CATALOGUE'S, not a table here. It is read from lesson-meta.json,
the file the Worker builds its gate pages from, so the padlock on a button
says what the click will actually meet. The hub once hardcoded Free/Pro by
hand and contradicted the paywall for days (checker/check-access.py tells
that story). When a Block Camp lesson's access changes, seo.py rewrites
lesson-meta.json; re-run this and commit block-camp/camp-nav.js with it -
--check fails until you do.
"""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
OUT = os.path.join(REPO, 'block-camp', 'camp-nav.js')

spec = importlib.util.spec_from_file_location(
    'hub', os.path.join(REPO, 'lesson-template', 'build', 'block-camp-hub', 'build.py'))
hub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hub)

MAPS = {'climb': 'block-camp-map.html', 'descent': 'block-camp-descent-map.html'}
# After station 17 there is no next camp: the next thing in Block Camp is the
# adventures, on the hub. Gold, the colour the Trial and the hub's own
# buttons wear.
END = {'href': 'block-camp.html#adventures', 'colour': '#e8c04a', 'ink': '#0b1a12'}
TRIAL = ('#e8c04a', '#0b1a12')


def catalogue():
    """{file: access} from lesson-meta.json, the Worker's own list. A deck
    too new to have a row is treated as Pro: a padlock that turns out not
    to be needed costs less than a free-looking link to a paywall."""
    path = os.path.join(REPO, 'lesson-meta.json')
    meta = json.load(open(path, encoding='utf-8'))
    return {f: (row.get('access') or 'pro') for f, row in meta.items()}


def route():
    acc = catalogue()
    climb, descent = [], []
    for n, name, slug, _l1, _l2 in hub.CLIMB:
        for part, f in ((1, 'blockcamp-%s.html' % slug), (2, 'blockcamp-%s-2.html' % slug)):
            if hub.present(f):
                climb.append(dict(file=f, line='climb', n=n, part=part, name=name,
                                  colour=hub.CAMP[n], ink=hub.INK[n]))
    for st, camp, name, slug, _lvl, _acc in hub.DESCENT:
        f = 'blockcamp-passive-%s.html' % slug
        if hub.present(f):
            colour, ink = (hub.CAMP[camp], hub.INK[camp]) if camp else TRIAL
            descent.append(dict(file=f, line='descent', n=st, name=name, colour=colour, ink=ink))

    firsts = [d for d in climb if d['part'] == 1]
    decks = {}
    for d in climb:
        later = [c for c in firsts if c['n'] > d['n']]
        d['next'] = later[0] if later else (descent[0] if descent else None)
    for i, d in enumerate(descent):
        d['next'] = descent[i + 1] if i + 1 < len(descent) else None
    for d in climb + descent:
        key = d['file'][:-len('.html')]
        entry = {'href': d['file'], 'line': d['line'], 'n': d['n'], 'name': d['name'],
                 'colour': d['colour'], 'ink': d['ink'], 'access': acc.get(d['file'], 'pro'),
                 'next': d['next']['file'][:-len('.html')] if d['next'] else 'end'}
        if 'part' in d:
            entry['part'] = d['part']
        decks[key] = entry
    return {'maps': MAPS, 'end': END, 'decks': decks}


def render():
    tpl = open(os.path.join(HERE, 'template.js'), encoding='utf-8').read()
    r = route()
    # One deck per line, so a change to one camp is a one-line diff.
    lines = ['{',
             '    "maps": %s,' % json.dumps(r['maps']),
             '    "end": %s,' % json.dumps(r['end']),
             '    "decks": {']
    keys = list(r['decks'])
    for i, k in enumerate(keys):
        lines.append('      %s: %s%s' % (json.dumps(k), json.dumps(r['decks'][k]),
                                          ',' if i < len(keys) - 1 else ''))
    lines += ['    }', '  }']
    assert tpl.count('{{ROUTE}}') == 1
    return tpl.replace('{{ROUTE}}', '\n'.join(lines)), r


if __name__ == '__main__':
    js, r = render()
    if '--check' in sys.argv:
        have = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
        if have != js:
            print('FAIL block-camp/camp-nav.js is stale - run '
                  'py lesson-template/build/block-camp-nav/build.py and commit it')
            sys.exit(1)
        print('PASS block-camp/camp-nav.js matches template.js and the catalogue (%d decks)'
              % len(r['decks']))
        sys.exit(0)
    open(OUT, 'w', encoding='utf-8', newline='\n').write(js)
    for k, d in r['decks'].items():
        print('  %-44s -> %-44s %s' % (k, d['next'], d['access']))
    print('wrote block-camp/camp-nav.js (%d decks)' % len(r['decks']))
