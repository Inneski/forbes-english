#!/usr/bin/env python3
"""BLOCK CAMP HARDCODES A FACT THE DATABASE OWNS.

Innes made Past Simple 1a free on 2026-09-02. The database row changed,
library.html's grid changed (it reads `access` live from Supabase through
sb-client.js), the crawlable index changed, the gate page stopped being
built, and the deck's JSON-LD flipped isAccessibleForFree to true.

The Block Camp hub still said Pro, because its Free/Pro tag is typed into
block-camp.html by hand, once per thumbnail. Nothing linked the two, so the
front page of the whole line contradicted the paywall for as long as nobody
happened to look at it - and it reports as "it still says pro", not as an
error.

IT HAPPENED AGAIN, AND THIS GATE DID NOT SEE IT. On 2026-09-15 e709bfc freed
five more camp 1a decks and eight Time Signals references. The hub had been
rebuilt dark in the meantime; this gate's pattern no longer matched a single
card, so it printed "this gate is now blind" and nobody ran it. For twelve
days the hub said Pro on thirteen free lessons, the quest padlocked five, and
the route map padlocked six - Past Simple 1a since 09-03, because the fix
then went into the hub and not the map. Innes found none of it: it surfaced
on 2026-09-27 when the deck's new next-camp button (block-camp-nav) read the
catalogue and disagreed with the map beside it.

So the gate now holds EVERY Block Camp page that says Free or Pro to the
catalogue - lesson-meta.json, the file the Worker builds its gate pages from:

  hub     block-camp.html's cards      (built; fix = rebuild block-camp-hub)
  quest   block-camp/quest.html's data (built; fix = rebuild block-camp-quest)
  nav     block-camp/camp-nav.js       (built; fix = rebuild block-camp-nav)
  map     block-camp-map.html's locks  (HAND-KEPT; fix = this script, --fix)

The three builders read access through block-camp-hub/build.py's access(), so
a rebuild puts them right. The route map is hand-kept HTML, so --fix sets its
padlocks - the stop, the lesson panel and the phone list - from the catalogue.

    py lesson-template/checker/check-access.py          # report, exit 1 on any disagreement
    py lesson-template/checker/check-access.py --fix    # also repair the route map

Run it whenever an access flag moves. It fails, rather than passing, when it
finds nothing to check on a page: a gate that goes blind must say so.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
META = os.path.join(ROOT, 'lesson-meta.json')
CACHE = os.path.join(ROOT, 'tools', 'lessons.json')
HUB = os.path.join(ROOT, 'block-camp.html')
QUEST = os.path.join(ROOT, 'block-camp', 'quest.html')
NAV = os.path.join(ROOT, 'block-camp', 'camp-nav.js')
MAP = os.path.join(ROOT, 'block-camp-map.html')

RED, GRN, DIM = '\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[2m%s\x1b[0m'

# A hub card: its href, then everything up to its closing tag, where the
# Free / Pro chip is.
HUB_CARD = re.compile(r'<a class="card"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)
# Any link on the route map to a deck, with its attributes and its content.
MAP_LINK = re.compile(r'<a ([^>]*?)href="(blockcamp-[^"]+\.html)"([^>]*)>(.*?)</a>', re.S)
LOCK = ('<span class="lock" aria-hidden="true"></span>'
        '<span class="sr">, subscribers only</span>')


def catalogue():
    meta = json.load(open(META, encoding='utf-8'))
    return {f: row['access'] for f, row in meta.items() if row.get('access')}


def page(href, base=''):
    """A link as the catalogue keys it: repo-relative, no fragment. The RPGs
    live in block-camp/ and are keyed with the folder; the quest page sits in
    that folder, so its links to decks climb out with ../."""
    href = href.split('#')[0]
    if href.startswith('../'):
        return href[3:]
    return base + href


def hub(real):
    out = []
    for href, body in HUB_CARD.findall(open(HUB, encoding='utf-8').read()):
        shown = 'free' if 'chip-free' in body else 'pro' if 'chip-pro' in body else None
        out.append((page(href), shown))
    return out


def quest(real):
    src = open(QUEST, encoding='utf-8').read()
    m = re.search(r'^const MAP = (.*);$', src, re.M)
    if not m:
        return []
    data, out = json.loads(m.group(1)), []
    for c in data['camps']:
        out += [(page(p['href'], 'block-camp/'), p['access']) for p in c['parts']]
    out += [(page(s['href'], 'block-camp/'), s['access']) for s in data['stations']]
    out += [(page(a['href'], 'block-camp/'), a['access']) for a in data['adventures']]
    return out


def nav(real):
    src = open(NAV, encoding='utf-8').read()
    return [(page(href), acc) for href, acc in
            re.findall(r'"href": "([^"]+)", [^\n]*?"access": "(free|pro)"', src)]


def map_links():
    src = open(MAP, encoding='utf-8').read()
    return src, list(MAP_LINK.finditer(src))


def route_map(real):
    _, links = map_links()
    out = []
    for m in links:
        attrs, body = m.group(1) + m.group(3), m.group(4)
        panel = 'class=' not in attrs          # the lesson panel's Part 1 / Part 2 / Open links
        marked = 'data-pro' in attrs and (not panel or 'class="lock"' in body)
        out.append((m.group(2), 'pro' if marked else 'free'))
    return out


def fix_map(real):
    """Set every padlock on the route map from the catalogue. Stops and phone
    rows carry data-pro (their CSS draws the lock); a panel link carries
    data-pro plus the lock and the screen-reader words."""
    src, links = map_links()
    out, last, n = [], 0, 0
    for m in links:
        attrs1, f, attrs2, body = m.groups()
        pro = real.get(f) == 'pro'
        a1 = re.sub(r'\s*data-pro="1"', '', attrs1)
        a2 = re.sub(r'\s*data-pro="1"', '', attrs2)
        text = body.replace(LOCK, '')
        panel = 'class=' not in attrs1 + attrs2
        if pro:
            if panel:
                a2, text = ' data-pro="1"' + a2, text + LOCK
            else:
                a1 = re.sub(r'(class="[^"]+")', r'\1 data-pro="1"', a1, count=1)
        new = '<a %shref="%s"%s>%s</a>' % (a1, f, a2, text)
        n += new != m.group(0)
        out.append(src[last:m.start()] + new)
        last = m.end()
    out.append(src[last:])
    new_src = ''.join(out)
    if new_src != src:
        open(MAP, 'w', encoding='utf-8', newline='\n').write(new_src)
    return n


def report(name, pairs, real):
    if not pairs:
        print('    ' + RED % 'FAIL', '%-6s nothing found to check - has the markup changed? '
                                    'This part of the gate is blind.' % name)
        return 1
    bad = [(f, s, real.get(f)) for f, s in pairs if real.get(f) != s]
    for f, shown, truth in bad:
        print('    ' + RED % 'FAIL', '%-6s %-44s says %-5s the catalogue says %s'
              % (name, f, shown, truth or 'nothing (no row)'))
    if not bad:
        print('    ' + GRN % 'PASS', '%-6s %d marker(s) agree with the catalogue' % (name, len(pairs)))
    return 1 if bad else 0


def main():
    real = catalogue()
    if '--fix' in sys.argv:
        n = fix_map(real)
        print('\n  --fix: %d link(s) on the route map re-marked' % n)
    print('\n  BLOCK CAMP FREE / PRO AGAINST lesson-meta.json')
    fails = sum(report(name, fn(real), real) for name, fn in
                (('hub', hub), ('quest', quest), ('nav', nav), ('map', route_map)))
    # The offline cache seo.py falls back to in a cloud session. If it
    # disagrees, a cloud run of seo.py would put the old access back.
    try:
        cache = {r['file']: r.get('access') for r in json.load(open(CACHE, encoding='utf-8'))}
        drift = sorted(f for f in real if f.startswith('blockcamp-') and cache.get(f) not in (None, real[f]))
        for f in drift:
            print('    ' + DIM % ('warn   tools/lessons.json says %s for %s' % (cache[f], f)))
    except (OSError, ValueError):
        pass
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
