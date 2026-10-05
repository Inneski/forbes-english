# -*- coding: utf-8 -*-
"""Ten languages for the eleven hand-written IELTS decks.

Innes, 2026-10-05: "some ielts is not translated into all the languages —
fix this now." The fourteen builder decks had carried ten languages since
2026-09-24 (`ielts_langs.py`); these eleven, which arrived as finished HTML
with no builder, were still English and German — below even the EN/DE/ES
minimum of 2026-09-04 — and seven of them showed every explanation in
English whatever the menu said. HANDOFF had parked the choice between
"translate in place" and "write eleven builders" since 09-12. This is the
in-place route, made repeatable: the deck's `UI_I18N` lives in JSON files
beside this script, and the script writes it back.

    py lesson-template/build/ielts_hand_i18n.py extract <deck.html>|all
    py lesson-template/build/ielts_hand_i18n.py inject  <deck.html>|all
    py lesson-template/build/ielts_hand_i18n.py status  [<deck.html>|all]

`extract` reads the deck's `UI_I18N`, writes `ielts_hand/<slug>/en.json`
(always, from the deck) and `de.json` (only if absent — a translator may
have added to it), and `content.json`: the keys a translator has to write,
which is English minus the chrome that `chrome_i18n.CHROME` and
`ielts_langs.TAIL_MORE` already carry in every language. It also turns every
literal `data-explain="A sentence…"` in the slides into a key (`x07b`: slide
7, second explanation) with the sentence registered under `en`, so that
explanations translate with the rest of the deck, and gives the three decks
whose `feedback()` could not look a key up (Parts 4, 5, 6) the `explainOf`
resolver the others already had. It then injects, filling the new keys from
English for German only, so the live behaviour (German chrome, English
explanations) is unchanged until the German arrives.

`inject` rebuilds the `const UI_I18N = {...};` block from the JSON files: en,
then each language that is COMPLETE (every English key present, after the
chrome overlay), in the deck's own `LANGS` order; a language with any key
missing is written `{}` and named, because HOUSE-STYLE §8 says partial is a
failure — the menu offers it and it falls back to English halfway down.
`status` reports the same without writing.

Translators write `<slug>/<code>.json` with the keys of `content.json`. The
conventions (register per language, what stays English, Arabic `<bdi>`) are
in `ielts_hand/TRANSLATING.md`. Keys the translator does not need (buttons,
score chip, results messages, ledger labels) are overlaid from CHROME when
the deck's English equals CHROME's English — a deck-specific `resNext` or
`actSpeakKind` is content, and the translator sees it in `content.json`.

The eleven decks are not generated, so this is a half-step, not a builder:
the slides, the engine and the artwork are still edited in the HTML. But a
wording fix in any language is now a JSON edit and an `inject`, and nothing
is retyped into eleven files.
"""
import html
import json
import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chrome_i18n import CHROME            # noqa: E402
from ielts_langs import LANGS, TAIL_MORE  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
DATA = os.path.join(HERE, 'ielts_hand')

DECKS = [
    'forbes-english-ielts-academic-writing-part1.html',
    'forbes-english-ielts-academic-writing-part1b.html',
    'forbes-english-ielts-writing-lab-part2.html',
    'forbes-english-ielts-writing-lab-part2b.html',
    'forbes-english-ielts-model-answers-part4.html',
    'forbes-english-ielts-outweigh-part5.html',
    'forbes-english-ielts-two-questions-part6.html',
    'forbes-english-ielts-intro-overview-part7.html',
    'forbes-english-ielts-line-graph-part8.html',
    'forbes-english-ielts-listening-part9.html',
    'forbes-english-ielts-speaking-part1-2.html',
    # The three scrolling pages (not decks; rule 1 still broken, see HANDOFF)
    # were given the same LANGS / UI_I18N / #langSelect shape on 2026-10-05 so
    # that this script could carry their ten languages too. Their JSON was
    # written from the page's own EN/DE dictionaries by hand, not extracted.
    'forbes-english-ielts-writing-studio-part3.html',
    'forbes-english-ielts-bar-charts-c1.html',
    'forbes-english-ielts-maps-and-data-c1.html',
]

# The six labels the template reads that CHROME does not carry for every
# language. The seven added languages come from ielts_langs.TAIL_MORE; these
# three are the values the builder decks use (i18n_ieltsp3.py and siblings).
TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'", 'glossShow': "'Translate'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'", 'glossShow': "'Übersetzen'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'", 'glossShow': "'Traducir'"},
}
for _c, _d in TAIL_MORE.items():
    TAIL[_c] = {k: _d[k] for k in ('branchLocked', 'glossHide', 'glossShow')}


def slug(deck):
    base = os.path.basename(deck)
    return re.sub(r'^forbes-english-ielts-', '', base)[:-len('.html')]


def deck_path(deck):
    return deck if os.path.isabs(deck) else os.path.join(ROOT, deck)


# ── A small JS object scanner ──────────────────────────────────────────────
# UI_I18N is a JS object literal: strings in three quote styles, arrow
# functions with template literals, block comments between entries. A regex
# cannot read it; this walks it.

def skip_string(s, i):
    q = s[i]
    i += 1
    n = len(s)
    while i < n:
        c = s[i]
        if c == '\\':
            i += 2
            continue
        if c == q:
            return i + 1
        if q == '`' and s.startswith('${', i):
            depth = 0
            while i < n:
                if s[i] in '\'"`' and not (s[i] == '`' and depth == 0):
                    i = skip_string(s, i)
                    continue
                if s[i] == '{':
                    depth += 1
                elif s[i] == '}':
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                i += 1
            continue
        i += 1
    raise ValueError('unterminated string')


def skip_comment(s, i):
    if s.startswith('/*', i):
        return s.index('*/', i) + 2
    if s.startswith('//', i):
        j = s.find('\n', i)
        return len(s) if j < 0 else j
    return i


def match_brace(s, i):
    """s[i] == '{'; return the index of its closing brace."""
    depth = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c in '\'"`':
            i = skip_string(s, i)
            continue
        if c == '/' and (s.startswith('/*', i) or s.startswith('//', i)):
            i = skip_comment(s, i)
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('unbalanced braces')


def scan_value(s, i):
    depth = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c in '\'"`':
            i = skip_string(s, i)
            continue
        if c == '/' and (s.startswith('/*', i) or s.startswith('//', i)):
            i = skip_comment(s, i)
            continue
        if c in '{[(':
            depth += 1
        elif c in '}])':
            depth -= 1
        elif c == ',' and depth == 0:
            return i
        i += 1
    return n


KEY_RE = re.compile(r'''([A-Za-z_$][\w$]*|'[^']*'|"[^"]*")\s*:''')


def split_entries(body):
    """Top-level `key: value` pairs of an object body (no outer braces)."""
    out = []
    i, n = 0, len(body)
    while i < n:
        while i < n:
            if body[i].isspace() or body[i] == ',':
                i += 1
            elif body.startswith('/*', i) or body.startswith('//', i):
                i = skip_comment(body, i)
            else:
                break
        if i >= n:
            break
        m = KEY_RE.match(body, i)
        if not m:
            raise ValueError('cannot read a key at: %r' % body[i:i + 60])
        key = m.group(1).strip('\'"')
        i = m.end()
        j = scan_value(body, i)
        out.append((key, body[i:j].strip()))
        i = j
    return out


_ESC = {'n': '\n', 't': '\t', 'r': '\r', 'b': '\b', 'f': '\f', 'v': '\v', '0': '\0'}


def decode_js_string(lit):
    """A JS string literal → Python str; anything else → None."""
    if not lit or lit[0] not in '\'"':
        return None
    q = lit[0]
    if lit[-1] != q:
        return None
    s, i, out = lit[1:-1], 0, []
    while i < len(s):
        c = s[i]
        if c == '\\':
            i += 1
            e = s[i]
            if e in _ESC:
                out.append(_ESC[e])
                i += 1
            elif e == 'x':
                out.append(chr(int(s[i + 1:i + 3], 16)))
                i += 3
            elif e == 'u':
                if s[i + 1] == '{':
                    k = s.index('}', i)
                    out.append(chr(int(s[i + 2:k], 16)))
                    i = k + 1
                else:
                    out.append(chr(int(s[i + 1:i + 5], 16)))
                    i += 5
            elif e == '\n':
                i += 1
            else:
                out.append(e)
                i += 1
        else:
            out.append(c)
            i += 1
    return ''.join(out)


def encode_js_string(s):
    return "'" + (s.replace('\\', '\\\\').replace("'", "\\'")
                   .replace('\r', '').replace('\n', '\\n')
                   .replace('</script', '<\\/script')) + "'"


def to_json_value(raw):
    s = decode_js_string(raw)
    return s if s is not None else {'js': raw}


def to_js(value):
    if isinstance(value, dict):
        return value['js']
    return encode_js_string(value)


def find_block(src):
    m = re.search(r'const UI_I18N = \{', src)
    if not m:
        raise ValueError('no UI_I18N block')
    a = m.start()
    close = match_brace(src, m.end() - 1)
    b = close + 1
    if src[b:b + 1] == ';':
        b += 1
    return a, b


def read_langs(src):
    a, b = find_block(src)
    body = src[a + len('const UI_I18N = {'):b - 1 - (1 if src[b - 1] == ';' else 0)]
    langs = OrderedDict()
    for code, raw in split_entries(body):
        if not raw.startswith('{'):
            raise ValueError('language %s is not an object' % code)
        d = OrderedDict()
        for k, v in split_entries(raw[1:-1]):
            d[k] = to_json_value(v)     # a repeated key keeps its last value
        langs[code] = d
    return langs


def deck_lang_codes(src):
    m = re.search(r'const LANGS = \[(.*?)\];', src, re.S)
    codes = re.findall(r"code:\s*'([a-z]{2})'", m.group(1)) if m else list(LANGS)
    return codes


# ── Chrome overlay ─────────────────────────────────────────────────────────

def _same(a, b):
    if isinstance(a, dict) or isinstance(b, dict):
        ra = a['js'] if isinstance(a, dict) else encode_js_string(a)
        rb = b['js'] if isinstance(b, dict) else encode_js_string(b)
        return re.sub(r'\s+', '', ra) == re.sub(r'\s+', '', rb)
    return a == b


def chrome_value(code, key, en):
    """The shared translation of `key` for `code`, or None if the deck's
    English is not the shared English (then it is content)."""
    if key in TAIL.get('en', {}) and key in TAIL.get(code, {}):
        if _same(en[key], to_json_value(TAIL['en'][key])):
            return to_json_value(TAIL[code][key])
    c_en = CHROME['en'].get(key)
    c_l = CHROME.get(code, {}).get(key)
    if c_en is not None and c_l is not None and _same(en[key], to_json_value(c_en)):
        return to_json_value(c_l)
    return None


def content_keys(en, codes):
    """Keys a translator must write: those no shared source covers for
    every non-English language of the deck."""
    out = []
    for k in en:
        if all(chrome_value(c, k, en) is not None for c in codes if c != 'en'):
            continue
        out.append(k)
    return out


# ── JSON files ─────────────────────────────────────────────────────────────

def folder(deck):
    return os.path.join(DATA, slug(deck))


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding='utf-8') as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write('\n')


# ── Explanations → keys ────────────────────────────────────────────────────

def keyify(src, en):
    """Literal data-explain sentences in the slide markup become keys."""
    cut = src.index('const UI_I18N = {')
    cut = src.rfind('<script', 0, cut)
    head, tail = src[:cut], src[cut:]
    sections = [m.start() for m in re.finditer(r'<section class="slide', head)]
    added = OrderedDict()
    seen = {}
    counters = {}

    def repl(m):
        val = m.group(1)
        if not re.search(r'\s', val) or val in en:
            return m.group(0)
        text = html.unescape(val)
        if text in seen:
            return 'data-explain="%s"' % seen[text]
        n = sum(1 for s in sections if s < m.start())
        counters[n] = counters.get(n, 0) + 1
        key = 'x%02d%s' % (n, 'abcdefghijklmnopqrstuvwxyz'[counters[n] - 1])
        while key in en or key in added:
            counters[n] += 1
            key = 'x%02d%s' % (n, 'abcdefghijklmnopqrstuvwxyz'[counters[n] - 1])
        seen[text] = key
        added[key] = text
        return 'data-explain="%s"' % key

    head = re.sub(r'data-explain="([^"]*)"', repl, head)
    return head + tail, added


RESOLVER = '''
/* An explanation may be written straight into data-explain, which is what most
   of the library does, or given as a UI_I18N key so that it translates with
   the rest of the deck. Resolve a key; pass literal text through untouched.
   A literal explanation is a sentence and can never collide with a key name,
   so this is safe on every existing lesson. */
const explainOf = v => (v && typeof v === 'string' && typeof UI_I18N.en[v] === 'string')
  ? t(v) : v;
'''


def patch_resolver(src):
    """Parts 4, 5 and 6 read data-explain raw; give them the resolver the
    other decks have, at the three places an explanation is read."""
    a = 'const reason = ownExplain || el.dataset.explain;'
    b = "const why = fb.dataset.explain ? ' ' + fb.dataset.explain : '';"
    if 'explainOf' in src or a not in src:
        return src, False          # already resolves keys (its own way)
    anchor = '  ? UI_I18N[currentLang][k] : UI_I18N.en[k];\n'
    if anchor not in src:
        raise ValueError('cannot find t() to anchor explainOf')
    src = src.replace(anchor, anchor + RESOLVER, 1)
    if b not in src:
        raise ValueError('fillFeedback() is not in the shape this patch expects')
    src = src.replace(a, 'const reason = explainOf(ownExplain || el.dataset.explain);', 1)
    src = src.replace(b, "const why = explainOf(fb.dataset.explain) ? ' ' + explainOf(fb.dataset.explain) : '';", 1)
    return src, True


# ── Validation ─────────────────────────────────────────────────────────────

TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)')


def tag_profile(s):
    prof = {}
    for close, name in TAG_RE.findall(s):
        name = name.lower()
        if name == 'bdi':
            continue
        k = ('/' if close else '') + name
        prof[k] = prof.get(k, 0) + 1
    return prof


def check_value(code, key, en_v, v):
    """Warnings for one translated string against its English."""
    w = []
    if isinstance(en_v, dict) or isinstance(v, dict):
        if not (isinstance(en_v, dict) and isinstance(v, dict)):
            w.append('%s.%s: function/string mismatch' % (code, key))
        return w
    if tag_profile(en_v) != tag_profile(v):
        w.append('%s.%s: HTML tags differ from English' % (code, key))
    if key.endswith('Svg') and en_v.count('<text') != v.count('<text'):
        w.append('%s.%s: <text> count differs' % (code, key))
    if (v == en_v and len(v) > 24 and ' ' in v and re.search(r'[a-z]{3,}', v)):
        w.append('%s.%s: identical to English' % (code, key))
    if code == 'ar':
        # Text only: an SVG's attribute quotes are not quoted English.
        s = re.sub(r'<bdi\b[^>]*>[\s\S]*?</bdi>', '￼', v)
        s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
        if re.search(r'“[^”]*[A-Za-z][^”]*”', s) or re.search(r'"[^"]*[A-Za-z][^"]*"', s):
            w.append('%s.%s: quoted English outside <bdi>' % (code, key))
    return w


# ── Commands ───────────────────────────────────────────────────────────────

def assemble(deck, write=True, fill_en=(), quiet=False):
    path = deck_path(deck)
    with open(path, encoding='utf-8') as f:
        src = f.read()
    codes = deck_lang_codes(src)
    fold = folder(deck)
    en = load_json(os.path.join(fold, 'en.json'))
    if en is None:
        raise SystemExit('%s: no en.json — run extract first' % slug(deck))
    need = content_keys(en, codes)
    save_json(os.path.join(fold, 'content.json'),
              OrderedDict((k, en[k]) for k in need))

    out = OrderedDict([('en', en)])
    report = OrderedDict()
    warnings = []
    for code in codes:
        if code == 'en':
            continue
        tr = load_json(os.path.join(fold, code + '.json')) or OrderedDict()
        extra = [k for k in tr if k not in en]
        full = OrderedDict()
        filled = []
        for k in en:
            if k in tr:
                full[k] = tr[k]
            else:
                cv = chrome_value(code, k, en)
                if cv is not None:
                    full[k] = cv
                elif code in fill_en:
                    full[k] = en[k]
                    filled.append(k)
        missing = [k for k in en if k not in full]
        for k in full:
            if k in tr:
                warnings += check_value(code, k, en[k], full[k])
        if missing:
            out[code] = OrderedDict()
            report[code] = 'MISSING %d (%s%s)' % (len(missing), ', '.join(missing[:6]),
                                                   '…' if len(missing) > 6 else '')
        else:
            out[code] = full
            note = 'complete'
            if filled:
                note += ', %d filled from English' % len(filled)
            if not tr:
                note = 'absent'
                out[code] = OrderedDict()
            report[code] = note
        if extra:
            warnings.append('%s: %d keys not in English, dropped: %s' % (code, len(extra), ', '.join(extra[:5])))

    lines = ['const UI_I18N = {']
    for code, d in out.items():
        if not d:
            lines.append('  %s: {},' % code)
            continue
        lines.append('  %s: {' % code)
        items = list(d.items())
        for i, (k, v) in enumerate(items):
            lines.append('    %s:%s%s' % (k, to_js(v), ',' if i < len(items) - 1 else ''))
        lines.append('  },')
    lines[-1] = lines[-1].rstrip(',')
    lines.append('};')
    block = '\n'.join(lines)

    a, b = find_block(src)
    new = src[:a] + block + src[b:]
    if write and new != src:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(new)
    if not quiet:
        print('%s  (%d keys, %d for translators)' % (slug(deck), len(en), len(need)))
        for code, note in report.items():
            print('   %-3s %s' % (code, note))
        for w in warnings:
            print('   ! ' + w)
    return report, warnings


def extract(deck):
    path = deck_path(deck)
    with open(path, encoding='utf-8') as f:
        src = f.read()
    langs = read_langs(src)
    en = langs['en']
    src, added = keyify(src, en)
    en.update(added)
    src, patched = patch_resolver(src)
    fold = folder(deck)
    save_json(os.path.join(fold, 'en.json'), en)
    de_path = os.path.join(fold, 'de.json')
    if not os.path.exists(de_path) and langs.get('de'):
        save_json(de_path, langs['de'])
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(src)
    print('%s: %d explanations keyed%s' % (slug(deck), len(added),
                                           ', explainOf added' if patched else ''))
    assemble(deck, write=True, fill_en=('de',))


def status(decks):
    for deck in decks:
        assemble(deck, write=False)


def main(argv):
    flags = [a for a in argv[1:] if a.startswith('--')]
    args = [a for a in argv[1:] if not a.startswith('--')]
    if not args or args[0] not in ('extract', 'inject', 'status'):
        print(__doc__)
        return 2
    cmd = args[0]
    targets = args[1:] or ['all']
    decks = DECKS if targets == ['all'] else targets
    # --fill-de: keep German complete by filling keys it lacks from English
    # (the pre-translation state, so nothing regresses while the German is
    # being written). Never for any other language.
    fill = ('de',) if '--fill-de' in flags else ()
    if cmd == 'extract':
        for d in decks:
            extract(d)
    elif cmd == 'inject':
        for d in decks:
            assemble(d, write=True, fill_en=fill)
    else:
        status(decks)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
