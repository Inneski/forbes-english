#!/usr/bin/env python3
"""ADD A LANGUAGE TO A DECK WITHOUT HAND-EDITING ESCAPED JAVASCRIPT.

Every deck already declares all ten languages in LANGS, and initLang() only
offers the ones whose UI_I18N block is complete:

    LANGS.filter(l => l.code === 'en' ||
                      Object.keys(UI_I18N[l.code] || {}).length >= enKeys)

So a language appears the moment its block has as many keys as English, and
never before. Nothing else has to change - no engine edit, no CSS, no build.
RTL is already handled (RTL_LANGS = ['ar']).

What stops this being easy is the quoting. The strings are HTML inside JS
string literals, so class="formula" has to be written class=\\"formula\\", and
getting that wrong kills the deck's JavaScript outright. That has happened
three times in one session, twice by hand and once inside a builder.

    python3 lesson-template/i18n_tool.py extract <deck.html> [lang]  > out.json
    python3 lesson-template/i18n_tool.py merge   <deck.html> <lang> <in.json>
    python3 lesson-template/i18n_tool.py status  [deck.html ...]

extract writes {key: value} with the HTML *unescaped*, so a translator sees
class="formula" and edits plain text. merge re-escapes on the way back in and
refuses to write a block that does not cover every English key - a partial
language would simply never show, which reads as "it did nothing".

The two function-valued keys (slideOf, wordCount) are carried across and must
be edited in the file by hand if a language needs different plural rules;
they are reported by merge so nobody forgets they exist.
"""
import json
import os
import re
import sys

RED, GRN, DIM = '\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[2m%s\x1b[0m'
KEY = re.compile(r'^\s{4}([A-Za-z0-9_]+):\s*(.*)$')


def block_spans(src, lang):
    """Every `  <lang>: { ... }` inside UI_I18N, as (start, end) byte ranges.

    THERE CAN BE MORE THAN ONE, and that is the trap. Each deck ships the
    eight unwritten languages as one-line stubs at the foot of the object:

        fr: {},
        it: {},

    A block written ABOVE one of those is silently overridden - a later key in
    an object literal wins - so the language stays empty, the switcher goes on
    hiding it, and the merge looks like it worked. That is why this returns a
    list and merge refuses to leave more than one behind.
    """
    start = src.find('const UI_I18N = {')
    if start < 0:
        raise SystemExit('no UI_I18N in this deck')
    spans = []
    for m in re.finditer(r'\n  %s: \{' % re.escape(lang), src[start:]):
        a = start + m.start()
        rest = src[start + m.end():]
        if rest.lstrip().startswith('}'):                    # one-line stub
            k = rest.index('}')
            b = start + m.end() + k + 1
            if src[b:b + 1] == ',':
                b += 1
        else:                                                 # a real block
            end = re.search(r'\n  \},?(?=\n)', rest)
            b = start + m.end() + end.end()
        spans.append((a, b))
    return spans


def block_span(src, lang):
    spans = block_spans(src, lang)
    return spans[-1] if spans else None


def parse(src, lang):
    """{key: (raw_js_value, is_function)} in file order."""
    span = block_span(src, lang)
    if not span:
        return {}
    body = src[span[0]:span[1]]
    out, cur, key = {}, [], None
    for line in body.split('\n')[1:]:
        m = KEY.match(line)
        if m:
            if key:
                out[key] = '\n'.join(cur).rstrip().rstrip(',')
            key, cur = m.group(1), [m.group(2)]
        elif key and line.strip() not in ('},', '}'):
            cur.append(line)
    if key:
        out[key] = '\n'.join(cur).rstrip().rstrip(',')
    return out


def js_to_text(raw):
    """A JS string literal -> the HTML a translator should see. None if it is
    not a plain string (an arrow function, say)."""
    raw = raw.strip()
    if not raw or raw[0] not in '"\'':
        return None
    q = raw[0]
    if not raw.endswith(q):
        return None
    return json.loads('"' + raw[1:-1].replace('\\\'', "'")
                      .replace('"', '\\"').replace('\\\\"', '\\"') + '"') \
        if q == "'" else json.loads(raw)


def text_to_js(text):
    """The HTML -> a double-quoted JS string literal, correctly escaped."""
    return json.dumps(text, ensure_ascii=False)


# THE SLIDE COUNTER READS BACKWARDS IN ARABIC. "5 / 22" is three bidi runs -
# a number, a neutral separator, a number - so an RTL paragraph reorders them
# and the learner sees "22 / 5". Found by rendering the deck bar, not by
# reading the JSON: every structural check passes, because the string IS
# "5 / 22". The score chip escapes it only because "0/28" has no spaces and
# stays one run.
#
# U+2066 LEFT-TO-RIGHT ISOLATE ... U+2069 POP DIRECTIONAL ISOLATE pins the run
# without affecting anything around it. Applied here rather than asked of the
# translator, because it is a rendering fact about Arabic, not a translation
# choice, and it has to hold for every deck.
ISOLATE_LANGS = ('ar',)


def rtl_isolate(lang, fn):
    if lang not in ISOLATE_LANGS or '\\u2066' in fn:
        return fn
    return fn.replace('`${a} / ${b}`', '`\\u2066${a} / ${b}\\u2069`')


def cmd_extract(deck, lang):
    src = open(deck, encoding='utf-8').read()
    vals = parse(src, lang)
    if not vals:
        raise SystemExit('deck has no %r block' % lang)
    out = {}
    for k, raw in vals.items():
        t = js_to_text(raw)
        out[k] = t if t is not None else {'__function__': raw}
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


def cmd_merge(deck, lang, path):
    src = open(deck, encoding='utf-8').read()
    en = parse(src, 'en')
    new = json.load(open(path, encoding='utf-8'))

    missing = [k for k in en if k not in new]
    extra = [k for k in new if k not in en]
    if missing:
        print('  ' + RED % 'REFUSED', '%d key(s) missing - a short block never '
              'appears in the switcher:' % len(missing))
        for k in missing[:12]:
            print('      ' + k)
        if len(missing) > 12:
            print('      ' + DIM % ('... and %d more' % (len(missing) - 12)))
        return 1
    if extra:
        print('  ' + DIM % ('ignoring %d key(s) English does not have: %s'
                            % (len(extra), ', '.join(extra[:6]))))

    lines = ['  %s: {' % lang]
    fns = []
    for k in en:                                  # English order, always
        v = new[k]
        if isinstance(v, dict) and '__function__' in v:
            lines.append('    %s: %s,' % (k, rtl_isolate(lang, v['__function__'])))
            fns.append(k)
        else:
            lines.append('    %s: %s,' % (k, text_to_js(v)))
    lines[-1] = lines[-1].rstrip(',')
    block = '\n'.join(lines) + '\n  },'

    spans = block_spans(src, lang)
    if spans:
        # Write into the LAST one - it is the one the browser would have used -
        # and delete any earlier duplicate, so nothing can shadow it again.
        a, b = spans[-1]
        src = src[:a] + '\n' + block + src[b:]
        for a, b in reversed(spans[:-1]):
            trimmed = src[:a] + src[b:]
            src = trimmed
        what = 'replaced' if len(spans) == 1 else \
            'replaced (and removed %d shadowing stub(s))' % (len(spans) - 1)
    else:                                          # insert after English
        ens = block_span(src, 'en')
        src = src[:ens[1]] + '\n' + block + src[ens[1]:]
        what = 'added'

    left = len(block_spans(src, lang))
    if left != 1:
        print('  ' + RED % 'REFUSED', 'that would leave %d %r blocks in '
              'UI_I18N; the file is not written' % (left, lang))
        return 1
    open(deck, 'w', encoding='utf-8').write(src)
    print('  ' + GRN % 'OK', '%s %r on %s - %d keys' % (what, lang, deck, len(en)))
    if fns:
        print('  ' + DIM % ('carried over unchanged, check the plural rules: '
                            + ', '.join(fns)))
    return 0


def cmd_status(decks):
    print('\n  UI_I18N COVERAGE')
    print('  %-42s %s' % ('deck', 'complete languages'))
    for d in decks:
        src = open(d, encoding='utf-8').read()
        en = len(parse(src, 'en'))
        done = [l for l in ('de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')
                if len(parse(src, l)) >= en > 0]
        name = os.path.basename(d).replace('blockcamp-', '').replace('.html', '')
        print('  %-42s en+%s %s' % (name, ','.join(done) if done else '(none)',
                                    DIM % ('%d keys' % en)))
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == 'extract':
        cmd_extract(a[1], a[2] if len(a) > 2 else 'en')
    elif a[0] == 'merge':
        sys.exit(cmd_merge(a[1], a[2], a[3]))
    elif a[0] == 'status':
        sys.exit(cmd_status(a[1:] or sorted(
            __import__('glob').glob('blockcamp-*.html'))))
    else:
        raise SystemExit(__doc__)
