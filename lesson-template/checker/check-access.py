#!/usr/bin/env python3
"""THE HUB HARDCODES A FACT THE DATABASE OWNS.

Innes made Past Simple 1a free on 2026-09-02. The database row changed,
library.html's grid changed (it reads `access` live from Supabase through
sb-client.js), the crawlable index changed, the gate page stopped being
built, and the deck's JSON-LD flipped isAccessibleForFree to true.

The Block Camp hub still said Pro, because its Free/Pro tag is typed into
block-camp.html by hand, once per thumbnail. Nothing linked the two, so the
front page of the whole line contradicted the paywall for as long as nobody
happened to look at it - and it reports as "it still says pro", not as an
error.

This gate compares every hardcoded tag on the hub against the access column,
read from tools/lessons.json (the same cache seo.py falls back to, kept in
step with Supabase by hand). Run it whenever an access flag moves.

    python3 lesson-template/checker/check-access.py

Exits non-zero on any disagreement.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HUB = os.path.join(ROOT, 'block-camp.html')
CACHE = os.path.join(ROOT, 'tools', 'lessons.json')

RED, GRN, DIM = '\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[2m%s\x1b[0m'

# One card: the anchor's href, then the title and the tag block inside it.
CARD = re.compile(
    r'<a[^>]*href="([^"]*blockcamp-[^"]+\.html)"[^>]*>.*?'
    r'<h3 class="mini-title">(.*?)</h3><div class="tags">(.*?)</div>', re.S)


def main():
    hub = open(HUB, encoding='utf-8').read()
    access = {r['file']: r['access'] for r in json.load(open(CACHE, encoding='utf-8'))}

    cards = CARD.findall(hub)
    if not cards:
        print('  ' + RED % 'FAIL', 'no Block Camp cards found on the hub - has the '
                                  'markup changed? This gate is now blind.')
        return 1

    findings, missing = [], []
    for href, title, tags in cards:
        f = href.split('/')[-1]
        shown = 'free' if '>Free<' in tags else 'pro' if '>Pro<' in tags else None
        real = access.get(f)
        if real is None:
            missing.append(f)
        elif shown is None:
            findings.append((f, 'no Free/Pro tag at all', real))
        elif shown != real:
            findings.append((f, 'hub says %s' % shown, real))

    print('\n  THE HUB AGAINST THE ACCESS COLUMN   %d card(s)' % len(cards))
    if findings:
        for f, said, real in findings:
            print('    ' + RED % 'FAIL', '%-44s %s, the database says %s'
                  % (f.replace('blockcamp-', '').replace('.html', ''), said, real))
    else:
        print('    ' + GRN % 'PASS', 'every hardcoded tag matches the access column')

    if missing:
        print('\n  ' + DIM % 'NOT IN THE CACHE (add them, or the gate cannot see them)')
        for f in missing:
            print('    ' + DIM % ('  ' + f))

    return 1 if findings or missing else 0


if __name__ == '__main__':
    sys.exit(main())
