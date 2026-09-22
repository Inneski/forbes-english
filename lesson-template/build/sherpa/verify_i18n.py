# -*- coding: utf-8 -*-
"""Check one sherpa/i18n/<slug>.json against its page. Exit 1 on any fault.

    py lesson-template/build/sherpa/verify_i18n.py camp-03

What it refuses:
  * a German or Spanish block missing a key, or carrying a key English lacks
  * an English override outside the authored set (cover line, activation)
  * a translation that changed a quoted English example: anything inside
    "…" in the English string must appear verbatim in the translation
  * a translation identical to the English on a string with 4+ words
    (the target-language forms are copied, prose is not)
  * chips: fewer than 4 or more than 8, or not plain English strings
  * a quiz fix that drops the key, changes the option count, or still leaves
    the key the longest option by 4+ characters
  * an activation string left empty, or a placeholder carrying an entity
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import build_sherpa as B   # noqa: E402

AUTHORED = {'coverSub', 'actTitle', 'actUse', 'actSpeakBrief', 'actSpeak1', 'actSpeak2',
            'actSpeak3', 'actWriteKind', 'actWriteBrief', 'actPlaceholder'}
LANGS = ('de', 'es')


def quoted(s):
    # pair the quotes in sequence, THEN drop the short ones — filtering by
    # length inside the regex let a short "It" go unmatched and paired every
    # later closing quote with the next opening one
    return [q for q in re.findall(r'"([^"]*)"', html.unescape(re.sub(r'<[^>]+>', '', s))) if len(q) >= 6]


def words(s):
    return len(re.findall(r'\w+', re.sub(r'<[^>]+>', '', s)))


def verify(slug):
    faults = []
    c = json.load(open(os.path.join(B.CONTENT, slug + '.json'), encoding='utf-8'))
    p = os.path.join(B.I18N, slug + '.json')
    if not os.path.exists(p):
        return ['no file %s' % p]
    A = json.load(open(p, encoding='utf-8'))
    EN = B.en_strings(c)
    over = A.get('en', {})
    bad = [k for k in over if k not in AUTHORED]
    if bad:
        faults.append('en overrides keys outside the authored set: %s' % bad)
    for k in AUTHORED:
        if not over.get(k):
            faults.append('en.%s is missing or empty' % k)
    EN.update({k: v for k, v in over.items() if k in AUTHORED})
    if '&' in over.get('actPlaceholder', '') and re.search(r'&[a-z#0-9]+;', over['actPlaceholder']):
        faults.append('actPlaceholder carries an HTML entity; it is set as plain text')
    keys = set(EN) - {'chipCount'}
    for lang in [l for l in B.ALL_LANGS if l != 'en' and (l in LANGS or l in A)]:
        tr = A.get(lang)
        if not isinstance(tr, dict):
            faults.append('%s: block missing' % lang)
            continue
        missing = sorted(keys - set(tr))
        extra = sorted(set(tr) - keys - {'chipCount'})
        if missing:
            faults.append('%s: missing %d keys: %s' % (lang, len(missing), missing[:15]))
        if extra:
            faults.append('%s: %d keys English does not have: %s' % (lang, len(extra), extra[:10]))
        for k in keys & set(tr):
            v = tr[k]
            if not isinstance(v, str) or not v.strip():
                faults.append('%s.%s is empty' % (lang, k))
                continue
            for q in quoted(EN[k]):
                if q not in html.unescape(re.sub(r'<[^>]+>', '', v)):
                    faults.append('%s.%s changed the quoted English example: "%s"' % (lang, k, q[:50]))
            # a table cell may legitimately be an English form or sentence
            # ("They was waiting." under "Not this"); only prose keys are
            # held to the still-English test
            is_cell = re.search(r'_ch\d+t\d+c\d+$', k)
            if v.strip() == EN[k].strip() and words(EN[k]) >= 4 and not re.search(r' \+ ', EN[k]) and not is_cell and not EN[k].strip().startswith('"') and k != 'actPlaceholder':
                faults.append('%s.%s is still English: %s' % (lang, k, EN[k][:50]))
    chips = A.get('chips')
    if not isinstance(chips, list) or not 4 <= len(chips) <= 8 or not all(isinstance(x, str) and x.strip() for x in chips):
        faults.append('chips: need 4-8 plain English strings, got %r' % (chips,))
    for n, fix in (A.get('quiz') or {}).items():
        q = c['quiz'][int(n) - 1]
        opts = fix.get('options')
        if not opts or len(opts) != len(q['options']):
            faults.append('quiz %s: options must be a list of %d' % (n, len(q['options'])))
            continue
        if q['correct'] not in opts:
            faults.append('quiz %s: the key %r is gone' % (n, q['correct']))
            continue
        L = [len(html.unescape(re.sub(r'<[^>]+>', '', o))) for o in opts]
        k = L[opts.index(q['correct'])]
        if k == max(L) and L.count(max(L)) == 1 and k - sorted(L)[-2] >= 4:
            faults.append('quiz %s: the key is still the longest by %d' % (n, k - sorted(L)[-2]))
        if len(set(o.lower() for o in opts)) != len(opts):
            faults.append('quiz %s: duplicate options' % n)
    # every longest-key item must have a fix
    for n, q in enumerate(c['quiz'], 1):
        L = [len(html.unescape(re.sub(r'<[^>]+>', '', o))) for o in q['options']]
        k = L[q['options'].index(q['correct'])]
        if k == max(L) and L.count(max(L)) == 1 and k - sorted(L)[-2] >= 4 and str(n) not in (A.get('quiz') or {}):
            faults.append('quiz %d keys the longest option and has no fix' % n)
    return faults


if __name__ == '__main__':
    rc = 0
    for slug in sys.argv[1:] or B.slugs():
        f = verify(slug)
        if f:
            rc = 1
            print('%s: %d fault(s)' % (slug, len(f)))
            for x in f:
                print('   - ' + x)
        else:
            print('%s: OK' % slug)
    sys.exit(rc)
