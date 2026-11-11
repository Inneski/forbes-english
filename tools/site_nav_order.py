# -*- coding: utf-8 -*-
"""One top menu bar, in one order, on every site page.

    py tools/site_nav_order.py          # apply (idempotent)
    py tools/site_nav_order.py --check  # exit 1 if any page is off the order

Innes, 2026-11-10: "RPG should be at top of landing page", then "menu bar
should be constant", with a screenshot of library.html's bar showing no RPGs.
Each site page carries its own copy of the bar, with its own classes, and on
every one RPGs had a "wide only" class, so at anything under ~1350px (or a
zoomed browser) it vanished. The order is now, on every page:

    RPGs · Level Check · Library · IELTS · Grammar · Block Camp ·
    Slide Decks · Work With Me · Sign In · (language) · Go Pro

RPGs leads and never steps out. The first pass moved RPGs' "wide only" class
onto Level Check to keep the link count per width; Innes, 2026-11-11, with a
zoomed Block Camp page: "why does level check drop here". So neither steps
out now: the main links (RPGs to Sign In, bar Slide Decks and Work With Me)
show at every desktop width, and only Slide Decks and Work With Me are wide
only. index.html's bar was reordered by hand (its classes and its fitRow
squeeze list differ) and is checked here, not edited. ielts.html's bar is
the one tools/build_hubs.py copies into the hubs, the IELTS routes and
rpg.html.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ['library.html', 'ielts.html', 'pricing.html', 'account.html', 'block-camp.html', 'block-camp-map.html',
         'block-camp/quest.html']
WIDE = ('nav-wide', 'fe-wide', 'tb-wide', 'wide')
A = r'<a\b[^>]*\bhref="(?:\.\./)?%s"[^>]*>[^<]*(?:<span[^>]*>[^<]*</span>)?[^<]*</a>'


def classes(tag):
    m = re.search(r'\bclass="([^"]*)"', tag)
    return m.group(1).split() if m else []


def with_classes(tag, cls):
    tag = re.sub(r'\s+class="[^"]*"', '', tag, count=1)
    return tag if not cls else tag.replace('<a ', '<a class="%s" ' % ' '.join(cls), 1)


def order(s):
    """The hrefs of the bar's links, in order, from the first bar that has RPGs."""
    rpg = re.search(A % r'rpg\.html', s)
    if not rpg:
        return None
    # library.html's bar is a <div>, not a <nav>: read from just before RPGs
    # to the Go Pro link, and treat any bar link in the lines before RPGs as
    # coming first
    go = re.search(A % r'pricing\.html', s[rpg.start():])
    before = s[max(0, rpg.start() - 400):rpg.start()]
    lead = re.findall(r'<a\b[^>]*\bhref="(?:\.\./)?((?:level-checker|library|ielts|grammar)\.html)"', before)
    bar = s[rpg.start():rpg.start() + (go.end() if go else 2000)]
    return lead + [re.sub(r'^\.\./', '', h) for h in re.findall(
        r'<a\b[^>]*\bhref="([^"]+)"[^>]*>[^<]*(?:<span[^>]*>[^<]*</span>)?[^<]*</a>', bar)
        if not h.endswith(('index.html', 'index.html#top'))]


def unwide(s, href):
    """Take the "wide only" class off the bar's link to href."""
    m = re.search(A % href, s)
    if m and any(c in WIDE for c in classes(m.group(0))):
        s = s[:m.start()] + with_classes(m.group(0), [c for c in classes(m.group(0)) if c not in WIDE]) + s[m.end():]
    return s


def fix(s):
    s = unwide(unwide(s, r'rpg\.html'), r'level-checker\.html')
    rpg = re.search(A % r'rpg\.html', s)
    lvl = re.search(A % r'level-checker\.html', s)
    lib = re.search(A % r'library\.html', s)
    assert rpg and lib, 'no RPGs or Library link'
    first = min(m.start() for m in (lvl, lib) if m)
    if rpg.start() < first:
        return s                                         # already leading
    tag = rpg.group(0)
    wide = [c for c in classes(tag) if c in WIDE]
    new_rpg = with_classes(tag, [c for c in classes(tag) if c not in WIDE])
    # cut RPGs (and the whitespace before it) out
    i = rpg.start()
    while i > 0 and s[i - 1] in ' \t':
        i -= 1
    if s[i - 1] == '\n':
        i -= 1
    s = s[:i] + s[rpg.end():]
    lvl = re.search(A % r'level-checker\.html', s)
    lib = re.search(A % r'library\.html', s)
    if lvl and lvl.start() < lib.start():
        if wide:
            s = s[:lvl.start()] + with_classes(lvl.group(0), classes(lvl.group(0)) + wide) + s[lvl.end():]
        at = lvl.start()
    else:
        # no Level Check in this bar: add one, wide only, between RPGs and Library
        pre = '../' if '"../library.html"' in lib.group(0) else ''
        lc = with_classes('<a href="%slevel-checker.html">Level Check</a>' % pre,
                          [c for c in classes(lib.group(0)) if c not in WIDE] + (wide or []))
        lc = re.sub(r'\s+aria-current="[^"]*"', '', lc)
        line_start = s.rfind('\n', 0, lib.start()) + 1
        indent = s[line_start:lib.start()]
        s = s[:lib.start()] + lc + ('\n' + indent if indent.strip() == '' else ' ') + s[lib.start():]
        at = lib.start()
    line_start = s.rfind('\n', 0, at) + 1
    indent = s[line_start:at]
    sep = ('\n' + indent) if indent.strip() == '' else ' '
    return s[:at] + new_rpg + sep + s[at:]


def main():
    check = '--check' in sys.argv
    bad = 0
    for p in PAGES + ['index.html']:
        path = os.path.join(ROOT, p)
        s = open(path, encoding='utf-8').read()
        if not check and p != 'index.html':
            t = fix(s)
            if t != s:
                open(path, 'w', encoding='utf-8', newline='').write(t)
                s = t
                print('  reordered', p)
        o = order(s)
        ok = bool(o) and o[0] == 'rpg.html' and 'level-checker.html' in o[:2]
        rpg = re.search(A % r'rpg\.html', s)
        lvl = re.search(A % r'level-checker\.html', s)
        ok = ok and not any(c in WIDE for c in classes(rpg.group(0)) + classes(lvl.group(0)))
        print('  %-4s %s: %s' % ('OK' if ok else 'FAIL', p, ' · '.join(h.split('.')[0] for h in (o or []))))
        bad += not ok
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
