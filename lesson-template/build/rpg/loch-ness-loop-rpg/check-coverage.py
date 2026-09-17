#!/usr/bin/env python3
"""Every string in strings.json has a gloss in every language, and nothing else.

    py lesson-template/build/rpg/loch-ness-loop-rpg/check-coverage.py

`check_translations.py` (one directory up) measures script purity, blanks and
key-set agreement across the nine files, but its coverage pass reads a
data.json through TEXT_KEYS that do not include a briefing card's `text`, an
ending's `text`, the cover `lead`, a route `label` or the builder's chrome —
exactly the strings validate() will refuse on at build time. This reads the
list render-story.py wrote from the assembled data instead, which is the
complete set, and reports per language: missing, extra, and any gloss that
lost a `___`, lost a CAPS token the English carries, or is identical to its
English when it should not be.

Exit 0 clean, 1 with findings.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = ('es', 'de', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')
CAPS = re.compile(r'\b[A-Z][A-Z-]{2,}\b')
# CAPS tokens that are chrome, not target lexis, and are expected to be translated
CHROME_CAPS = {'CHAPTER', 'ROUTE', 'CHOICE', 'THE', 'AND', 'PHOTO', 'PHOTOS', 'TAKEN', 'POINTS',
               'RIDE', 'AGAIN', 'BEFORE', 'YOU', 'SET', 'OFF', 'CORRECT', 'CHANCES', 'SHOP',
               'SHORE', 'ROAD', 'HIGH', 'FORT', 'AUGUSTUS', 'PIER', 'CASTLE', 'BAY', 'NORTH',
               'SIDE', 'DORES', 'LOCH', 'NESS', 'LOOP', 'RPG', 'BIKE', 'PARTS'}


def main():
    want = json.load(open(os.path.join(HERE, 'strings.json'), encoding='utf-8'))
    tdir = os.path.join(HERE, 'translations')
    bad, n_ok = [], 0
    for lang in LANGS:
        p = os.path.join(tdir, lang + '.json')
        if not os.path.exists(p):
            bad.append('%s: no translations/%s.json' % (lang, lang)); continue
        t = json.load(open(p, encoding='utf-8'))
        for s in want:
            if s not in t:
                bad.append('%s: MISSING  %r' % (lang, s[:70])); continue
            g = t[s]
            if not isinstance(g, str) or not g.strip():
                bad.append('%s: EMPTY    %r' % (lang, s[:70])); continue
            if ('___' in s) != ('___' in g):
                bad.append('%s: BLANK    %r -> %r' % (lang, s[:50], g[:50]))
            # a VOCAB explanation's CAPS target words are the English being
            # taught and travel into the gloss unchanged
            for tok in set(CAPS.findall(s)) - CHROME_CAPS:
                if len(tok) >= 3 and tok not in g and s.upper() != s:
                    bad.append('%s: CAPS LOST %s in %r' % (lang, tok, s[:60]))
            if g.strip() == s.strip() and re.search(r'[a-z]{4}', s):
                bad.append('%s: IDENTICAL %r' % (lang, s[:70]))
        for s in t:
            if s not in want:
                bad.append('%s: EXTRA    %r' % (lang, s[:70]))
        n_ok += 1
    if bad:
        print('\n'.join(bad))
        print('\n%d findings' % len(bad))
        return 1
    print('PASS  %d strings x %d languages, complete' % (len(want), n_ok))
    return 0


if __name__ == '__main__':
    sys.exit(main())
