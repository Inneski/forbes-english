#!/usr/bin/env python3
"""Audit a translations directory before it ever reaches a built page.

    python3 lesson-template/build/rpg/check_translations.py <slug>/translations [data.json]

`check-glosses.js` measures the same defect class on a finished Blocula-style
page: a gloss carrying a neighbouring language's writing system, a gloss with
none of its own script, a blank gloss, a gloss left identical to its English.
It cannot read an rpg.py page (no `const LANGS`) and it cannot run at all
until a page exists — by which point a bad gloss has already been built in.

This runs the same rules over the `<lang>.json` files themselves, so a
translation pass is checkable the moment it is written, plus three rules that
belong to this stage:

  * every language file holds exactly the same set of English keys;
  * a prompt whose English has a ___ keeps the ___ in every gloss (that blank
    is the question — a gloss that silently fills it in gives the answer away);
  * pass `data.json` and it also reports which learner-facing strings in the
    lesson have no entry at all, which is what `validate()` would refuse on.

Exit 0 = clean, 1 = findings. Coincidences are real: a proper name, a French
kicker that genuinely matches its English, Chinese and Japanese that share
their kanji. Those come out as ADVISORY and do not fail the run.
"""
import json, os, re, sys

LANGS = ('es', 'de', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')

CYR, ARAB = r'Ѐ-ӿ', r'؀-ۿݐ-ݿ'
HAN, KANA = r'一-鿿㐀-䶿', r'぀-ヿ'
HANGUL, GREEK, HEB = r'가-힯', r'Ͱ-Ͽ', r'֐-׿'
LAT = r'A-Za-zÀ-ɏ'
_LATIN = dict(bad=(CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB), needs=LAT)
RULES = {l: _LATIN for l in ('es', 'de', 'fr', 'it', 'pt')}
RULES['ru'] = dict(bad=(ARAB, HAN, KANA, HANGUL, HEB), needs=CYR)
RULES['ar'] = dict(bad=(CYR, HAN, KANA, HANGUL, GREEK, HEB), needs=ARAB)
RULES['zh'] = dict(bad=(CYR, ARAB, HANGUL, HEB), needs=HAN)
RULES['ja'] = dict(bad=(CYR, ARAB, HANGUL, HEB), needs=HAN + KANA)

TEXT_KEYS = ('k', 'act', 'title', 'story', 'clue', 'mission', 'prompt',
             'fb', 'explanation', 'note', 'label', 'small', 'start', 'eyebrow')


def load(d):
    out = {}
    for l in LANGS:
        p = os.path.join(d, l + '.json')
        if os.path.isfile(p):
            out[l] = json.load(open(p, encoding='utf-8'))
    return out


def lesson_strings(path):
    """Every learner-facing English string in an extracted data.json."""
    found = []
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in TEXT_KEYS and isinstance(v, str) and v.strip():
                    found.append(v.strip())
                elif k in TEXT_KEYS and isinstance(v, dict) and isinstance(v.get('en'), str):
                    found.append(v['en'].strip())
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(json.load(open(path, encoding='utf-8')))
    return found


def main(d, data_json=None):
    tables = load(d)
    if not tables:
        raise SystemExit('no <lang>.json files in %s' % d)
    errs, warn = [], []

    keysets = {l: set(t) for l, t in tables.items()}
    union = set().union(*keysets.values())
    for l, ks in keysets.items():
        for missing in sorted(union - ks):
            errs.append(('MISSING KEY', l, missing, ''))

    for l, table in tables.items():
        r = RULES[l]
        for en, s in table.items():
            if not isinstance(s, str) or not s.strip():
                errs.append(('EMPTY', l, en, '')); continue
            if s.strip() == en.strip() and re.search(r'[A-Za-z]{4}', s):
                warn.append(('IDENTICAL TO EN', l, en, 'a proper name?'))
            for rng in r['bad']:
                m = re.search('[' + rng + ']+', s)
                if m:
                    errs.append(('FOREIGN SCRIPT', l, en, 'contains %r' % m.group(0)))
            if (not re.search('[' + r['needs'] + ']', s)
                    and s.strip() != en.strip()
                    and re.sub(r'[\s\d\W_]', '', s, flags=re.U)):
                errs.append(('WRONG SCRIPT', l, en, 'no %s characters at all' % l))
            if '___' in en and '___' not in s:
                errs.append(('BLANK LOST', l, en, s))
            if '___' not in en and '___' in s:
                errs.append(('BLANK ADDED', l, en, s))

    if data_json:
        want = set(lesson_strings(data_json))
        for s in sorted(want - union):
            errs.append(('UNTRANSLATED STRING', '-', s, 'in the lesson, not in the table'))
        stale = sorted(union - want)
        if stale:
            warn.append(('UNUSED', '-', '%d entries' % len(stale),
                         'in the table, not in the lesson: ' + '; '.join(s[:40] for s in stale[:4])))

    n = len(union)
    show = lambda rows: [print('  %-20s %-3s %s\n%s%s' % (k, l, en[:78], ' ' * 25, extra[:110]))
                         for k, l, en, extra in rows]
    if warn:
        print('\n%d advisory (check each is a real coincidence):\n' % len(warn)); show(warn)
    if not errs:
        print('\nPASS  %s — %d strings x %d languages, no script, coverage or blank-slot defects'
              % (d, n, len(tables)))
        return 0
    print('\nFAIL  %s — %d defect(s)\n' % (d, len(errs))); show(errs)
    return 1


if __name__ == '__main__':
    if not 2 <= len(sys.argv) <= 3:
        raise SystemExit(__doc__.strip().splitlines()[2].strip())
    sys.exit(main(*sys.argv[1:]))
