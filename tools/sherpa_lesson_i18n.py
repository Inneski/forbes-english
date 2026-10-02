#!/usr/bin/env python3
"""Translations on every Sherpa lesson page, in the camp one pattern.

    node   tools/sherpa_lesson_strings.js        # 1. collect each page's text
    python tools/sherpa_lesson_master.py         # 2. fold it into the translators' master list
    python tools/sherpa_lesson_i18n.py --merge   # 3a. fold translators' and reviewers' files into the master
    python tools/sherpa_lesson_i18n.py           # 3. inject the translations and the runtime
    python tools/sherpa_lesson_i18n.py --check   #    exit 1 unless every language is complete and sound
    python tools/sherpa_lesson_i18n.py --pseudo  #    inject "[de] ..." stand-ins, to test coverage
    node   tools/sherpa_lesson_i18n_check.js     # 4. measure it in a browser, every page, every language

Innes, 2026-09-26: "you have to be more thorough in your translation work -
still some important text has nothing". With a language on, eight of the
nine descents had no translation at all, and the other fifteen pages only
translated ten example sentences each; camps one and two alone carried a
real system: a globe on each section (English line, translation beneath),
the quiz's own words translated. This puts that system on the other 23
pages, in the course's nine languages (de es fr it pt ru ar zh ja).

WHAT IS TRANSLATED follows HOUSE-STYLE section 8: the page's own
explanations, headings, notes, hints and captions ("chrome") get a line
beneath them from the section's globe; example sentences stay English and
show a translation under them from the "Examples in" bar (which the
descents now get); the English being taught (conjugation tables, grammar
forms, signal-word lists, quiz stems and options) is left alone. The kinds
are in lesson-template/sherpa-i18n/master.json, decided per string.

The runtime (tools/sherpa_lesson_i18n_runtime.js) matches text, not keys:
each block's English, whitespace collapsed, looks itself up. So the quiz,
which rewrites its hint and feedback as the learner goes, is translated
again as it changes, without touching the quiz's code.
"""
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, 'lesson-template', 'sherpa-i18n')
RUNTIME = os.path.join(ROOT, 'tools', 'sherpa_lesson_i18n_runtime.js')
OWN_SYSTEM = ('camp-one-present-continuous', 'camp-two-present-simple',
              'the-climb')  # the game carries its own ten-language strings (lesson-template/build/sherpa-climb)
START, END = '<!-- SHERPA-LESSON-I18N:start -->', '<!-- SHERPA-LESSON-I18N:end -->'
FENCE = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sherpa_lesson_master as M                      # noqa: E402

CSS = """
/* the camp one pattern (tools/sherpa_lesson_i18n.py) */
.lang-globe-wrap{position:relative;display:inline-block;margin:6px 0 4px;}
.hero .lang-globe-wrap{margin-top:10px;}
.lang-globe-btn{width:30px;height:30px;padding:0;border-radius:50%;border:1px solid var(--accent-light);background:var(--accent-lighter);font-size:16px;line-height:1;display:inline-flex;align-items:center;justify-content:center;cursor:pointer;transition:background .15s ease,border-color .15s ease;}
.lang-globe-btn:hover{border-color:var(--accent);}
.lang-globe-btn.active{background:var(--accent);border-color:var(--accent);}
.lang-menu{position:absolute;top:36px;left:0;z-index:30;min-width:180px;background:var(--card);border:1px solid var(--accent-light);border-radius:10px;box-shadow:0 10px 28px rgba(43,15,29,0.16);padding:5px;}
.lang-menu[hidden]{display:none;}
.lang-menu button{display:block;width:100%;text-align:left;background:none;border:none;padding:7px 10px;border-radius:6px;cursor:pointer;font-family:var(--sherpa-font,'Inter',sans-serif);font-size:14px;font-weight:600;color:var(--ink);}
.lang-menu button:hover{background:var(--accent-lighter);}
.lang-menu button.selected{color:var(--accent-dark);background:var(--accent-lighter);}
.i18n-inline{display:block;margin-top:4px;padding-left:8px;border-left:1px solid var(--accent-light);font-size:.92em;font-style:italic;font-weight:400;letter-spacing:normal;text-transform:none;color:var(--accent-dark);}
.i18n-inline[dir="rtl"]{text-align:right;padding-left:0;padding-right:8px;border-left:0;border-right:1px solid var(--accent-light);}
.tr-bar{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 26px;font-family:var(--sherpa-font,'Inter',sans-serif);font-size:13.5px;color:var(--ink-soft);}
.tr-bar .tr-label{letter-spacing:.06em;text-transform:uppercase;font-weight:700;font-size:12px;}
.tr-bar button{font:inherit;font-weight:600;border:1px solid var(--accent-light);background:var(--card);color:var(--ink-soft);padding:5px 11px;border-radius:999px;cursor:pointer;}
.tr-bar button:hover{color:var(--ink);}
.tr-bar button.on{background:var(--accent);color:var(--on-accent,#fff);border-color:var(--accent);}
.ex-tr{display:block;margin-top:8px;padding-top:7px;border-top:1px dashed var(--accent-light);font-style:normal;font-size:.95em;opacity:.92;}
.ex-tr[dir="rtl"]{text-align:right;}
"""


def load_master():
    return {m['id']: m for m in json.load(io.open(os.path.join(DIR, 'master.json'), encoding='utf-8'))['items']}


def kind_of(m):
    if 'kind' in m:
        return m['kind']
    ks = [k for k in m['kinds'] if k != '?']
    return ks[0] if len(ks) == 1 and len(m['kinds']) == 1 else '?'


def page_langs(slug, master):
    """The languages this page can offer: those in which every string it needs, and every
    interface string, is translated. HOUSE-STYLE section 8: a half-done language is never
    offered, it would fall back to English halfway down the screen."""
    items = json.load(io.open(os.path.join(DIR, slug + '.json'), encoding='utf-8'))['items']
    need = [master[M.sid(it['en'], it.get('svg'))] for it in items
            if M.sid(it['en'], it.get('svg')) in master and kind_of(master[M.sid(it['en'], it.get('svg'))]) in ('chrome', 'example')]
    need += [m for m in master.values() if m['pages'] == ['*']]
    return [l for l in M.LANGS if all(m.get('tr', {}).get(l) for m in need)]


def page_data(slug, master, pseudo=False):
    items = json.load(io.open(os.path.join(DIR, slug + '.json'), encoding='utf-8'))['items']
    langs = M.LANGS if pseudo else page_langs(slug, master)
    data = {'langs': langs, 't': {}, 'x': {}, 's': {}, 'ui': {}}
    missing = [l for l in M.LANGS if l not in langs]

    def row(m):
        tr = m.get('tr', {})
        if pseudo:
            return ['[%s] %s' % (l, tr.get(l) or m['en']) for l in langs]
        return [tr.get(l, '') for l in langs]

    for it in items:
        m = master.get(M.sid(it['en'], it.get('svg')))
        if not m:
            continue
        k = kind_of(m)
        if k == 'keep' or (k == '?' and not pseudo):
            continue
        # by occurrence, not by string: the same sentence can be an example in one place
        # and quiz feedback in another ("Happen takes no object..." on descent ten)
        if it.get('svg'):
            if k != 'chrome':
                continue
            bucket = 's'
        elif it['where'].startswith('quiz'):
            bucket = 't'                                  # hints and feedback: the globe's
        else:
            bucket = 'x' if (it['kind'] == 'example' or k == 'example') else 't'
        data[bucket][m['en']] = row(m)
    for m in master.values():
        if m['pages'] == ['*']:
            data['ui'][m['en']] = row(m)
    return data, missing


def block(data):
    runtime = io.open(RUNTIME, encoding='utf-8').read()
    payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return (START + '\n<style id="sherpa-lesson-i18n">' + CSS + '</style>\n'
            + '<script type="application/json" id="sherpa-i18n-data">' + payload + '</script>\n'
            + '<script>\n' + runtime + '</script>\n' + END + '\n')


TAG = re.compile(r'</?([a-z0-9]+)\b[^>]*>', re.I)
CAPS = re.compile(r'\b[A-Z][A-Z\'’]+(?:\s+[A-Z][A-Z\'’]+)+\b|\b[A-Z]{3,}\b')


def problems(m, text, lang):
    out = []
    if m.get('kind') == 'example':
        return out                     # an example's translation is shown as plain text
    if sorted(TAG.findall(m['en'])) != sorted(TAG.findall(text)):
        out.append('tags differ')
    for ph in re.findall(r'\{\w+\}', m['en']):
        if ph not in text:
            out.append('placeholder %s lost' % ph)
    plain = re.sub(r'<[^>]+>', ' ', m['en'])
    if plain.strip().isupper():
        return out                     # an all-caps label ("UNFINISHED TIME") is translated whole
    for tok in CAPS.findall(plain):
        if tok not in text:
            out.append('grammar token "%s" not kept in English' % tok)
    return out


def merge():
    """Fold the translators' files (work/tr-<lang>-<k>.json) and the reviewers' corrections
    (work/review-<lang>.json, applied last) into master.json's "tr"."""
    path = os.path.join(DIR, 'master.json')
    doc = json.load(io.open(path, encoding='utf-8'))
    by = {m['id']: m for m in doc['items']}
    counts = {}
    for l in M.LANGS:
        got = {}
        for f in sorted(glob.glob(os.path.join(DIR, 'work', 'tr-%s-*.json' % l))):
            got.update(json.load(io.open(f, encoding='utf-8')))
        rv = os.path.join(DIR, 'work', 'review-%s.json' % l)
        fixes = json.load(io.open(rv, encoding='utf-8')) if os.path.exists(rv) else {}
        got.update(fixes)
        # hand fixes, applied last so no later merge undoes them (work/fixes.json: {lang: {id: text}})
        hand = os.path.join(DIR, 'work', 'fixes.json')
        if os.path.exists(hand):
            got.update(json.load(io.open(hand, encoding='utf-8')).get(l, {}))
        n = 0
        for i, t in got.items():
            if i in by and isinstance(t, str) and t.strip():
                by[i].setdefault('tr', {})[l] = t.strip()
                n += 1
        counts[l] = (n, len(fixes))
    io.open(path, 'w', encoding='utf-8', newline='\n').write(json.dumps(doc, ensure_ascii=False, indent=1) + '\n')
    for l, (n, f) in counts.items():
        print('  %s  %4d translations, %3d reviewer corrections' % (l, n, f))


def remove():
    """Take the block off every page (a rollback, or before committing test stand-ins)."""
    for p in sorted(glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html'))):
        src = io.open(p, encoding='utf-8').read()
        new = FENCE.sub('', src)
        if new != src:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
            print('  removed from ' + os.path.basename(p))


def main():
    if '--merge' in sys.argv:
        return merge()
    if '--remove' in sys.argv:
        return remove()
    check, pseudo = '--check' in sys.argv, '--pseudo' in sys.argv
    master = load_master()
    bad = []
    pending = {}
    if check:
        for m in master.values():
            if kind_of(m) == 'keep':
                continue
            for l in M.LANGS:
                t = m.get('tr', {}).get(l)
                if not t:
                    pending[l] = pending.get(l, 0) + 1    # not offered until complete: reported, not failed
                    continue
                for p in problems(m, t, l):
                    bad.append('%s %s: %s' % (l, p, m['en'][:60]))
        und = [m['en'][:50] for m in master.values() if kind_of(m) == '?']
        if und:
            bad.append('%d strings with no decided kind, e.g. %s' % (len(und), und[:3]))
    for p in sorted(glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html'))):
        slug = os.path.basename(p)[len('sherpa-tensing-'):-5]
        if slug in OWN_SYSTEM or slug == 'route-map':
            continue
        src = io.open(p, encoding='utf-8').read()
        data, missing = page_data(slug, master, pseudo)
        b = block(data)
        new = FENCE.sub(lambda m: b, src, count=1) if FENCE.search(src) else src.replace('</body>', b + '</body>', 1)
        if check:
            if new != src and not pseudo:
                bad.append('%s: block missing or stale' % slug)
        elif new != src:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
            print('  %-44s %3d to translate, %3d examples, %2d labels; offers %s%s' % (
                slug, len(data['t']), len(data['x']), len(data['s']), ' '.join(data['langs']),
                ('  (pending: %s)' % ' '.join(missing)) if missing else ''))
    for x in bad[:60]:
        print('FAIL ' + x)
    if check:
        if pending:
            print('pending (not offered until complete): ' + ', '.join('%s %d strings' % kv for kv in sorted(pending.items())))
        print('PASS' if not bad else 'FAIL: %d problem(s)' % len(bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
