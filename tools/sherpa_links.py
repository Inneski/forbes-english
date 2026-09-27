#!/usr/bin/env python3
"""A way home from every Sherpa page.

    python tools/sherpa_links.py            # link the wordmark on every lesson page
    python tools/sherpa_links.py --check    # exit 1 if a page lacks either link

Innes, 2026-09-26: "should be links to main page on every page in sherpa". The
lesson pages had one way out, the "Route map" button; their wordmark was plain
text. Now, as on the route map itself, "Forbes English" links to the site's front
page (index.html), and "Sherpa Tensing" links to the course's own main page, the
route map. Both keep their look: the name in its colours, "Forbes English" in the
page's text accent.
"""
import glob
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND_OLD = '<div class="brand">Sherpa <span>Tensing</span></div>'
BRAND_NEW = ('<div class="brand"><a href="sherpa-tensing-route-map.html" style="color:inherit;text-decoration:none">'
             'Sherpa <span>Tensing</span></a></div>')
SUB_OLD = '<div class="sub">Forbes English &middot; a route up the tenses</div>'
SUB_NEW = ('<div class="sub"><a href="index.html" style="color:var(--accent-dark);text-decoration:none;font-weight:600;">'
           'Forbes English</a> &middot; a route up the tenses</div>')


def pages():
    return sorted(p for p in glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html'))
                  if not p.endswith('sherpa-tensing-route-map.html'))


def main():
    check = '--check' in sys.argv
    bad = []
    for p in pages():
        name = os.path.basename(p)
        src = io.open(p, encoding='utf-8').read()
        new = src.replace(BRAND_OLD, BRAND_NEW, 1).replace(SUB_OLD, SUB_NEW, 1)
        if BRAND_NEW not in new or SUB_NEW not in new:
            bad.append('%s: wordmark not in the expected form, links not added' % name)
            continue
        if check:
            if new != src:
                bad.append('%s: wordmark links missing' % name)
        elif new != src:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
            print('  ' + name)
    for b in bad:
        print('FAIL ' + b)
    if check:
        print('PASS: %d pages link home and to the route map' % len(pages()) if not bad else 'FAIL: %d' % len(bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
