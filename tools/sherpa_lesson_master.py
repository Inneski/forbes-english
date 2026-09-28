#!/usr/bin/env python3
"""The translators' master list for the Sherpa lesson pages.

    python tools/sherpa_lesson_master.py            # write lesson-template/sherpa-i18n/master.json
    python tools/sherpa_lesson_master.py --stats    # just count

Reads the per-page files from tools/sherpa_lesson_strings.js and folds them
into one list of unique English strings, each with a stable id, the kinds
it was guessed as, where it appears (a few samples) and on how many pages,
so each string is translated once and reads the same on every page. Camps
one and two are left out: they carry their own translation system
(I18N / sectionLang, per-section globes), which the new pages copy.

The shared interface strings (the globe menu, the quiz's own words, the
voice bar, the examples bar) are added under section "ui".
"""
import glob
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, 'lesson-template', 'sherpa-i18n')
OWN_SYSTEM = ('camp-one-present-continuous', 'camp-two-present-simple')
LANGS = ['de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']

# strings the page's script writes, and the controls around the lesson
UI = [
    ('Translate this section', 'aria-label of the globe button that translates one section'),
    ('Checkpoint {n} of {m}', 'quiz progress; keep {n} and {m}'),
    ('Score: {n}', 'quiz score; keep {n}'),
    ('Next checkpoint', 'quiz button'),
    ('Reach the summit', 'quiz button on the last question'),
    ('Climb again', 'button: restart the quiz'),
    ('Examples in', 'label before the language chips that show example translations'),
    ('Off', 'chip that switches example translations off'),
    ('Route map', 'link back to the course map'),
    ('Active voice', 'link from a passive lesson to its active twin'),
    ('Passive · finish this camp', 'locked link: the passive opens once this lesson is finished'),
    ('Show me anyway', 'link: open the locked passive lesson anyway'),
    ('No passive', 'label: this tense has no passive worth learning'),
    ('Finish this camp and its passive opens.', 'tooltip'),
    ('Nobody says the passive of this tense.', 'tooltip'),
]


def sid(en, svg=False):
    return hashlib.sha1(((u'svg:' if svg else u'') + en).encode('utf-8')).hexdigest()[:10]


def build():
    master = {}
    for f in sorted(glob.glob(os.path.join(DIR, '*.json'))):
        slug = os.path.basename(f)[:-5]
        if slug.startswith('_') or slug in OWN_SYSTEM:
            continue
        for it in json.load(io.open(f, encoding='utf-8'))['items']:
            k = sid(it['en'], it.get('svg'))
            m = master.setdefault(k, {'id': k, 'en': it['en'], 'svg': bool(it.get('svg')), 'kinds': [],
                                      'where': [], 'pages': []})
            if it['kind'] not in m['kinds']:
                m['kinds'].append(it['kind'])
            if slug not in m['pages']:
                m['pages'].append(slug)
            if len(m['where']) < 3 and it['where'] not in m['where']:
                m['where'].append(it['where'])
    for en, note in UI:
        k = sid('ui:' + en)
        master[k] = {'id': k, 'en': en, 'svg': False, 'kinds': ['chrome'], 'where': ['ui: ' + note], 'pages': ['*']}
    return sorted(master.values(), key=lambda m: (-len(m['pages']), m['en']))


def main():
    items = build()
    kinds = {}
    for m in items:
        k = m['kinds'][0] if len(m['kinds']) == 1 else 'mixed'
        kinds[k] = kinds.get(k, 0) + 1
    words = sum(len(m['en'].split()) for m in items)
    print('%d unique strings, %d words; %s' % (len(items), words, kinds))
    if '--stats' in sys.argv:
        return
    out = os.path.join(DIR, 'master.json')
    old = {}
    if os.path.exists(out):
        old = {m['id']: m for m in json.load(io.open(out, encoding='utf-8'))['items']}
    for m in items:                              # keep decisions and translations already made
        if m['id'] in old:
            for k in ('kind', 'tr', 'note'):
                if k in old[m['id']]:
                    m[k] = old[m['id']][k]
    io.open(out, 'w', encoding='utf-8', newline='\n').write(
        json.dumps({'langs': LANGS, 'items': items}, ensure_ascii=False, indent=1) + '\n')
    print('  ' + os.path.relpath(out, ROOT))


if __name__ == '__main__':
    main()
