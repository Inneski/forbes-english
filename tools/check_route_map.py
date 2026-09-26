#!/usr/bin/env python3
"""Check the Sherpa Tensing route map against the catalogue and its readers.

`sherpa-tensing-route-map.html` is hand-maintained (there is no builder), and
it states things that live elsewhere: which lessons are free, their levels,
how many there are, and which lesson opens which. It is also a data source:
`lesson-template/build/build_sherpa.py` reads the tense colours off it with a
regex, and `lesson-template/apply_soften.py` / `soften_family.py` rewrite
them. This checks both directions, so a catalogue change or a careless edit
shows up as a line of output instead of a wrong badge nobody notices.

    python tools/check_route_map.py              # exit 1 if anything is wrong
    python tools/check_route_map.py <copy.html>  # check a copy instead

`tools/build_hubs.py` runs the same check (warn-only) on every hub build,
because that is when a catalogue change is most likely to have happened.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'sherpa-tensing-route-map.html')
FAMILY = 'sherpa-tensing-'
MAP = 'sherpa-tensing-route-map.html'

_UNITS = ('zero one two three four five six seven eight nine ten eleven twelve thirteen '
          'fourteen fifteen sixteen seventeen eighteen nineteen').split()
_TENS = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()
WORD = {w: i for i, w in enumerate(_UNITS)}
for t, tw in enumerate(_TENS, 2):
    WORD[tw] = t * 10
    for u in range(1, 10):
        WORD['%s-%s' % (tw, _UNITS[u])] = t * 10 + u


def _lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _attr(tag, name):
    m = re.search(r'\s%s="([^"]*)"' % re.escape(name), tag)
    return m.group(1) if m else None


def rows_of(s):
    """Every list row: (kind, file, opening tag, inner html), attribute order free."""
    out = []
    for m in re.finditer(r'(<a\s[^>]*\bclass="(camp|desc|off)-row\b[^"]*"[^>]*>)(.*?)</a>', s, re.S):
        out.append((m.group(2), _attr(m.group(1), 'href'), m.group(1), m.group(3)))
    return out


def check(rows, page=PAGE):
    """Return a list of problems (empty when the page agrees with everything)."""
    s = open(page, encoding='utf-8').read()
    cat = {r['file']: r for r in rows if r['file'].startswith(FAMILY) and r['file'] != MAP}
    free = {f for f, r in cat.items() if r.get('access') != 'pro'}
    bad = []

    listed = rows_of(s)
    if len(listed) < 20:
        return ['only %d list rows found: has the markup changed? (the check reads '
                '<a class="camp-row|desc-row|off-row" href=...>)' % len(listed)]
    files = [f for _, f, _, _ in listed]

    # every lesson in the family has exactly one row in the lists
    for f in sorted(set(cat) - set(files)):
        bad.append('%s is in the catalogue but has no row on the route map' % f)
    for f in sorted(set(files) - set(cat)):
        bad.append('%s has a row on the route map but is not in the catalogue' % f)
    for f in sorted({f for f in files if files.count(f) > 1}):
        bad.append('%s has %d rows' % (f, files.count(f)))
    for f in files:
        if not os.path.exists(os.path.join(ROOT, f)):
            bad.append('%s is linked but the file does not exist' % f)

    # each row's Free badge and level agree with the catalogue
    for kind, f, tag, inner in listed:
        if f not in cat:
            continue
        badge = bool(re.search(r'class="[^"]*\btag-free\b', inner))
        if badge != (f in free):
            bad.append('%s: page says %s, catalogue says %s' % (
                f, 'Free' if badge else 'Pro', cat[f].get('access')))
        lvl = re.search(r'<span class="lvl"[^>]*>([^<]+)</span>', inner)
        if not lvl or lvl.group(1) != cat[f].get('level'):
            bad.append('%s: level %s on the page, %s in the catalogue' % (
                f, lvl.group(1) if lvl else 'missing', cat[f].get('level')))

    # the counts in the hero and the free line add up
    kinds = [k for k, _, _, _ in listed]
    want = {'camps up': kinds.count('camp'), 'passives down': kinds.count('desc'),
            'off the route': kinds.count('off'), 'free': len(free)}
    got = dict((lab.strip(), int(n)) for n, lab in re.findall(
        r'<li[^>]*><b>(\d+)</b>\s*(?:<span[^>]*>)?([a-z ]+)(?:</span>)?</li>', s))
    for lab, n in want.items():
        if got.get(lab) != n:
            bad.append('hero count "%s" says %s, the lists say %d' % (lab, got.get(lab), n))
    pro = re.search(r'<strong>(\w+) lessons? (?:is|are) free[^<]*</strong>.*?Pro opens the other ([\w-]+)', s, re.S)
    if not pro:
        bad.append('the free/Pro line is missing')
    else:
        a, b = WORD.get(pro.group(1).lower()), WORD.get(pro.group(2).lower())
        if a != len(free) or b != len(cat) - len(free):
            bad.append('free/Pro line says %s free and %s Pro; the catalogue says %d and %d' % (
                pro.group(1), pro.group(2), len(free), len(cat) - len(free)))

    # the colour key build_sherpa.py reads: 13 rows, row colour = its ascent dot,
    # and every descent dot (and descent row) in its twin camp's colour
    key = re.findall(r'href="(%s[a-z0-9-]+\.html)" style="background:(#[0-9A-Fa-f]{6});color:(#[0-9A-Fa-f]{6})' % FAMILY, s)
    if len(key) != 13:
        bad.append('build_sherpa.py reads %d colour-key rows off the map, not 13' % len(key))
    for f, bg, ink in key:
        if contrast(bg, ink) < 4.5:
            bad.append('%s: row text %s on %s is %.2f:1, under 4.5' % (f, ink, bg, contrast(bg, ink)))
    dots = dict((f, c.upper()) for c, f in re.findall(
        r'data-color="(#[0-9A-Fa-f]{6})" data-href="(%s[a-z0-9-]+\.html)"' % FAMILY, s))
    by_num = {}
    for kind, f, tag, inner in listed:
        if kind == 'camp':
            num = re.search(r'<span class="camp-num">(\d+)</span>', inner)
            bg = re.search(r'background:(#[0-9A-Fa-f]{6})', _attr(tag, 'style') or '')
            if num and bg:
                by_num[int(num.group(1))] = bg.group(1).upper()
                if dots.get(f) != bg.group(1).upper():
                    bad.append('%s: row colour %s, ascent dot %s' % (f, bg.group(1), dots.get(f)))
    descs = [(f, tag) for kind, f, tag, _ in listed if kind == 'desc']
    if sum(1 for f in dots if '-descent-' in f) != 9:
        bad.append('the descent map has %d live dots, not 9' % sum(1 for f in dots if '-descent-' in f))
    for f, tag in descs:
        twin, c = _attr(tag, 'data-camp'), re.search(r'--c:(#[0-9A-Fa-f]{6})', _attr(tag, 'style') or '')
        want_c = by_num.get(int(twin)) if twin and twin.isdigit() else None
        if not c or c.group(1).upper() != want_c:
            bad.append('%s: list colour %s, its camp %s is %s' % (f, c.group(1) if c else None, twin, want_c))
        if dots.get(f) != want_c:
            bad.append('%s: map dot %s, its camp %s is %s (build_sherpa.py asserts this)'
                       % (f, dots.get(f), twin, want_c))

    # the contour background: text on the paper must still clear 4.5:1 where
    # the darkest line crosses it. A stroke thinner than a pixel covers only
    # part of one, so a line's darkest point is its opacity x its width
    # (capped at 1), composited onto the paper. Labels with a paper halo
    # (text-shadow in --paper) never touch a line and are measured on paper.
    tile = re.search(r'background-image:url\("([^"]+\.svg)"\)', s)
    deep = re.search(r'--paper-deep:(#[0-9A-Fa-f]{6})', s)
    if tile:
        svg_path = os.path.join(ROOT, tile.group(1).replace('%20', ' '))
        if not os.path.exists(svg_path):
            bad.append('background tile %s does not exist' % tile.group(1))
        else:
            svg = open(svg_path, encoding='utf-8').read()
            stroke = re.search(r'stroke="(#[0-9A-Fa-f]{6})"', svg)
            lines = [(float(o), float(w)) for o, w in re.findall(
                r'<path stroke-opacity="([0-9.]+)" stroke-width="([0-9.]+)"', svg)]
            tok = dict(re.findall(r'(--[a-z-]+):(#[0-9A-Fa-f]{6})', s))
            if not stroke or not lines:
                bad.append('could not read the contour tile\'s stroke colour and opacities')
            elif '--paper' in tok:
                a, p = max(o * min(1.0, w) for o, w in lines), tok['--paper']
                # the paper darkens towards the foot of the page: measure the darker end
                if deep and _lum(deep.group(1)) < _lum(p):
                    p = deep.group(1).upper()
                mix = '#' + ''.join('%02X' % round(int(stroke.group(1)[i:i + 2], 16) * a
                                                   + int(p[i:i + 2], 16) * (1 - a)) for i in (1, 3, 5))
                halo = re.search(r'\.kicker[^{]*\{text-shadow:[^}]*var\(--paper\)', s)
                for name in ('--accent-text', '--ink-soft', '--ink'):
                    against = p if (name == '--accent-text' and halo) else mix
                    if name in tok and contrast(tok[name], against) < 4.5:
                        bad.append('%s %s is %.2f:1 %s' % (
                            name, tok[name], contrast(tok[name], against),
                            'on the paper' if against == p else 'where a contour line (%s) crosses it' % mix))
                if '.kicker{color:var(--accent-text);}' not in s:
                    bad.append('.kicker is not on --accent-text, the shade measured against the contours')
                # older rules that set a grey by hex on text that sits on the paper
                for rule, col in re.findall(r'\.(teach-row|legend|map-how|lead)\{[^}]*?color:(#[0-9A-Fa-f]{6})', s):
                    if contrast(col, mix) < 4.5:
                        bad.append('.%s text %s is %.2f:1 where a contour line crosses it' % (rule, col, contrast(col, mix)))

    # no free lesson may be locked behind Pro lessons only: a free learner
    # could never open it (used to sat behind camp 3 until 2026-09-25)
    slug = lambda f: f[len(FAMILY):-5]
    back = {slug(f): f for f in cat}
    pair = dict(re.findall(r'"(descent-[a-z0-9-]+)":\s*\["(camp-[a-z0-9-]+)"', s))
    gates = []
    for sel, cond in re.findall(r'gate\(\'a\[href\*="(cloud-[a-z0-9-]+)"\][^\']*\',\s*(.*?),\s*\n', s):
        gates.append((sel, cond))
    if len(pair) != 9 or len(gates) != 3:
        bad.append('could not read the lock rules (PAIR %d of 9, gate() %d of 3)' % (len(pair), len(gates)))
    for d, c in pair.items():
        if back.get(d) in free and back.get(c) not in free:
            bad.append('%s is free but only opens after %s, which is Pro' % (d, c))
    for sel, cond in gates:
        pre = re.findall(r'done\("([a-z0-9-]+)"\)', cond)
        via_descent = 'descents' in cond          # "any one descent" includes the free one
        if back.get(sel) in free and not via_descent and not any(back.get(x) in free for x in pre):
            bad.append('%s is free but only opens after %s, all Pro' % (sel, ', '.join(pre) or cond))
    return bad


def report(rows, source=None):
    """Warn-only, for build_hubs.py. Never stops the build."""
    try:
        bad = check(rows)
    except Exception as e:                       # noqa: BLE001
        print('  ! route map check skipped: %s' % e)
        return []
    src = ' (catalogue from %s)' % source if source else ''
    if bad:
        print('  ! sherpa-tensing-route-map.html disagrees with the catalogue%s:' % src)
        for b in bad:
            print('      ' + b)
    else:
        print('  sherpa-tensing-route-map.html: lists, badges, counts and locks agree%s' % src)
    return bad


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import seo
    rows, source = seo.lessons(write_cache=False)
    bad = check(rows, *(sys.argv[1:2]))
    for b in bad:
        print('FAIL ' + b)
    print('%s: %d problem(s) (catalogue from %s)' % (
        'PASS' if not bad else 'FAIL', len(bad), source))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
