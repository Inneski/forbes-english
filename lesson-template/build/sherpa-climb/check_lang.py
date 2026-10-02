#!/usr/bin/env python3
"""Check one translation file without building the page.

    py lesson-template/build/sherpa-climb/check_lang.py de       # or es fr it pt ru ar zh ja

Reads i18n/strings.json (written by build.py: every English string and a note
on where it is used) and i18n/<lang>.json, and prints what build.py would
refuse: missing strings, stale keys, and the problems() it checks (a CAPS token
lost, a {placeholder} changed, an odd number of ** marks). Exit 1 on any.

It writes nothing, so several translators can run it at once; build.py itself
rewrites the page, and two of those at once would race.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # noqa: E402  (build.py runs nothing on import)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in build.LANGS:
        raise SystemExit('usage: check_lang.py <%s>' % '|'.join(build.LANGS))
    lang = sys.argv[1]
    en = json.load(io.open(os.path.join(HERE, 'i18n', 'strings.json'), encoding='utf-8'))
    tr = json.load(io.open(os.path.join(HERE, 'i18n', lang + '.json'), encoding='utf-8'))
    have = {k: v for k, v in tr.items() if isinstance(v, str) and v.strip()}
    missing = [s for s in en if s not in have]
    stale = [k for k in tr if k not in en]
    bad = []
    for s in en:
        if s in have:
            bad += ['%r: %s' % (s[:70], b) for b in build.problems(s, have[s])]
    out = sys.stdout
    for s in missing:
        out.write('missing: %s\n' % s[:90].encode('ascii', 'backslashreplace').decode())
    for k in stale:
        out.write('stale key (not an English string the page uses): %s\n' % k[:90].encode('ascii', 'backslashreplace').decode())
    for b in bad:
        out.write('problem: %s\n' % b.encode('ascii', 'backslashreplace').decode())
    ok = not (missing or stale or bad)
    out.write('%s: %s %d/%d translated, %d stale, %d problem(s)\n' % (
        'PASS' if ok else 'FAIL', lang, len(en) - len(missing), len(en), len(stale), len(bad)))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
