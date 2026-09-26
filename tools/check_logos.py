# -*- coding: utf-8 -*-
"""Every page draws the Forbes English logo the standard way, or fails here.

    python3 tools/check_logos.py            # every tracked page; exit 1 on a FAIL
    python3 tools/check_logos.py a.html ... # just these

The standard, since 2026-09-26: the "Forbes" trace with ENGLISH beneath it at
exactly the wordmark's width. Three accepted forms:

  lesson   ENGLISH as <text textLength=...> in DM Sans 600, inside the SVG
           that holds the trace (hand-built lessons; see HOUSE-STYLE.md).
  chrome   the same with class fe-logo-en / tb-logo-en, Barlow Condensed 800
           (library, index, pricing, the hubs' top band, Block Camp).
  deck     lesson-template.html's .fe-logo: <text class="fe-logo-word"> with
           the template's tracking, shown only once DM Sans has loaded.

What fails is what the 2026-09-26 sweep removed: ENGLISH as its own <span> or
<div> under the wordmark (its width then depends on a font and a tracking
value, and drifted on ~100 pages); ENGLISH as SVG text with hand-set
letter-spacing and no textLength; "Forbes" typed as text instead of the trace;
an FE monogram standing in for the logo.

level-checker.html's masthead is exempt: it takes the level's typeface on
purpose. A page with no logo at all is not this check's business.
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACE = 'c-58 -10 -226 -34'            # a run of the wordmark's first path
EXEMPT = {('level-checker.html', 'fe-logo-sub')}

SVG = re.compile(r'<svg\b[^>]*>(?:(?!</svg>).)*?</svg>', re.S)
EN_TEXT = re.compile(r'<text\b([^>]*)>\s*ENGLISH\s*</text>')
EN_AFTER = re.compile(r'\s*(?:<div class="[\w-]*(?:rule|divider)[\w-]*"></div>\s*)?'
                      r'<(span|div)\b[^>]*class="([\w -]+)"[^>]*>\s*(?i:english)\s*</\1>', re.S)


def pages():
    out = subprocess.run(['git', 'ls-files', '*.html'], cwd=ROOT, capture_output=True, text=True).stdout
    return [p for p in out.splitlines()
            if not p.startswith(('lesson-template/', 'docs/', '.claude/', 'FORBES ENGLISH/', 'CGPT cleaned/'))
            and not os.path.basename(p).startswith('_')]


def check(path):
    s = open(os.path.join(ROOT, path), encoding='utf-8', errors='replace').read()
    name = os.path.basename(path)
    faults = []
    for m in SVG.finditer(s):
        svg = m.group(0)
        if TRACE not in svg:
            if re.search(r'<text\b[^>]*>\s*F(?:E|<tspan[^>]*>E</tspan>)\s*</text>', svg):
                faults.append('FE monogram in place of the logo')
            elif re.search(r'<text\b[^>]*>\s*Forbes\s*</text>', svg) and 'ENGLISH' in svg:
                faults.append('"Forbes" set as text, not the wordmark trace')
            continue
        t = EN_TEXT.search(svg)
        if t:
            a = t.group(1)
            if 'textLength=' in a or 'fe-logo-word' in a or re.search(r'class="word"', a):
                continue
            faults.append('ENGLISH is SVG text with hand-set tracking (no textLength)')
            continue
        after = EN_AFTER.match(s, m.end())
        if after:
            if (name, after.group(2).split()[0]) in EXEMPT:
                continue
            faults.append('ENGLISH is a separate <%s class="%s"> under the wordmark' % (after.group(1), after.group(2)))
    return faults


def main(argv):
    targets = argv or pages()
    bad = 0
    for p in targets:
        f = check(p)
        if f:
            bad += 1
            for x in sorted(set(f)):
                print('FAIL  %s  %s' % (p, x))
    print('%d page(s) checked, %d with a non-standard logo' % (len(targets), bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
