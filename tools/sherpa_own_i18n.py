#!/usr/bin/env python3
"""Camps one and two keep their own translation system; bring it to the course's nine.

    python tools/sherpa_own_i18n.py            # add pt, ar, ja from the translators' files
    python tools/sherpa_own_i18n.py --check    # exit 1 unless every language has every key

Their pages carry an I18N table (en, de, it, es, pl, zh, fr, ru) and a globe on each
section offering those. The course's languages are de es fr it pt ru ar zh ja, so
Portuguese, Arabic and Japanese were missing (Polish, which only these two pages
have, stays). This adds the three tables (from lesson-template/sherpa-i18n/work/
own-<page>.out.json, written by the translation workflow), puts them in the globe
menus, and sets an Arabic translation line right to left.

Fixed on the way (2026-09-26): on camp two the frequency words and time expressions
(signal1li1-6, signal2li2-5) were one language along in the table, so a German
learner saw Italian under "never (0%)"; they were rotated back by hand, see the
commit.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, 'lesson-template', 'sherpa-i18n', 'work')
PAGES = ['camp-one-present-continuous', 'camp-two-present-simple']
ADD = [('pt', 'PT &middot; Portugu&ecirc;s'), ('ar', 'AR &middot; &#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577;'),
       ('ja', 'JA &middot; &#26085;&#26412;&#35486;')]
NINE = ['de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']


def blocks(s):
    start = s.index('var I18N = {')
    return start, list(re.finditer(r'^  (\w+): \{\n(.*?)\n  \}', s[start:], re.S | re.M))


def keys_of(body):
    """Every key, including several on one line (signal1li1 ... signal1li6 share lines on
    camp two: reading only the first per line left them out of pt/ar/ja, and the check too)."""
    return re.findall(r'(?<![\w"])(\w+)\s*:\s*"', body)


def js_block(code, table, order):
    lines = ['    %s: %s' % (k, json.dumps(table[k], ensure_ascii=False)) for k in order if k in table]
    return '  %s: {\n%s\n  }' % (code, ',\n'.join(lines))


def apply(slug):
    p = os.path.join(ROOT, 'sherpa-tensing-%s.html' % slug)
    s = io.open(p, encoding='utf-8').read()
    out = json.load(io.open(os.path.join(WORK, 'own-%s.out.json' % slug), encoding='utf-8'))
    # rewrite this tool's own blocks rather than skip a page that has them
    for code, _ in ADD:
        s = re.sub(r',\n  %s: \{\n.*?\n  \}(?=,\n  \w+: \{|\n\};)' % code, '', s, count=1, flags=re.S)
    start, bl = blocks(s)
    en_keys = keys_of(bl[0].group(2))
    missing = {code: [k for k in en_keys if k not in out[code]] for code, _ in ADD}
    for code, ks in missing.items():
        if ks:
            sys.exit('! %s: the %s translations lack %s' % (slug, code, ks[:5]))
    add = ''.join(',\n' + js_block(code, out[code], en_keys) for code, _ in ADD)
    last = bl[-1]
    at = start + last.end()
    s = s[:at] + add + s[at:]
    # the globe menus
    for code, label in reversed(ADD):          # each goes straight after ru: reversed keeps pt, ar, ja
        if '{ code: "%s"' % code not in s:
            s = re.sub(r'(\n  \{ code: "ru", label: "[^"]*" \})',
                       lambda m: m.group(1) + ',\n  { code: "%s", label: "%s" }' % (code, label), s, count=1)
    # an Arabic line reads right to left
    if 'sub.setAttribute("dir", "rtl")' not in s:
        s = s.replace('    sub.className = "i18n-inline";\n',
                      '    sub.className = "i18n-inline";\n    if (lang === "ar") { sub.setAttribute("dir", "rtl"); sub.style.textAlign = "right"; }\n', 1)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(s)


def check():
    bad = []
    for slug in PAGES:
        s = io.open(os.path.join(ROOT, 'sherpa-tensing-%s.html' % slug), encoding='utf-8').read()
        start, bl = blocks(s)
        en = set(keys_of(bl[0].group(2)))
        have = {m.group(1): set(keys_of(m.group(2))) for m in bl}
        for code in NINE:
            if code not in have:
                bad.append('%s: no %s table' % (slug, code))
            elif en - have[code]:
                bad.append('%s: %s lacks %d keys, e.g. %s' % (slug, code, len(en - have[code]), sorted(en - have[code])[:3]))
            if '{ code: "%s"' % code not in s:
                bad.append('%s: %s not in the globe menu' % (slug, code))
    for b in bad:
        print('FAIL ' + b)
    print('PASS' if not bad else 'FAIL: %d' % len(bad))
    return bad


def main():
    if '--check' in sys.argv:
        sys.exit(1 if check() else 0)
    for slug in PAGES:
        apply(slug)
        print('  sherpa-tensing-%s.html' % slug)
    sys.exit(1 if check() else 0)


if __name__ == '__main__':
    main()
