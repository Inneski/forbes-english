"""Splice new languages into a Block Camp deck's word bank, glosses and gloss CSS.

    python3 lesson-template/bank_merge.py <deck.html> <dir>

<dir> holds bw_XX.json (object keyed by the exact English strings, same key
set as the deck's es bank) and sup_XX.json (array of gloss strings in document
order, one per es/de gloss pair) for each language code XX in NEW.

Three edits, each verified before the file is written:
  1. BW_TR word bank: add each language, keys in es order, all present.
  2. Inline glosses: after each <span class="sup" data-lang="de"> span, add one
     span per new language, same markup, text HTML-escaped.
  3. Gloss CSS: every rule whose selector targets .sup[data-lang="es"|"de"] is
     regenerated for all gloss languages. The data-boxw width knob is a layout
     decision per language and is left alone.

Written for blockcamp-present-simple.html on 2026-09-03; the other decks share
the markup, so this should carry them once their JSON exists. Refuses to write
if any count is off - every count is asserted against the deck.
"""
import io, re, json, html, os, sys

DECK = sys.argv[1]
SRC = sys.argv[2]
NEW = ['fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']
GLOSS_LANGS = ['es', 'de'] + NEW
NBSP = chr(160)

s = io.open(DECK, encoding='utf-8', newline='').read()
assert chr(13) not in s, 'deck has CR characters; refusing'

# ---- 1. word bank -------------------------------------------------------
m = re.search(r'(<script>window\.BW_TR=)(\{.*?\})(;</script>)', s, re.S)
d = json.loads(m.group(2))
es_keys = list(d['es'].keys())
n_keys = len(es_keys)
for L in NEW:
    p = os.path.join(SRC, 'bw_%s.json' % L)
    t = json.load(io.open(p, encoding='utf-8'))
    assert set(t.keys()) == set(es_keys), (L, set(t) ^ set(es_keys))
    d[L] = {k: t[k].replace(NBSP, ' ') for k in es_keys}
    for k, v in d[L].items():
        assert v.strip() and '<' not in v and '>' not in v, (L, k, v)
new_json = json.dumps(d, ensure_ascii=False)
s = s[:m.start(2)] + new_json + s[m.end(2):]

# ---- 2. inline glosses --------------------------------------------------
de_pat = re.compile(r'<span class="sup" data-lang="de"><b>DE</b><span>.*?</span></span>', re.S)
sites = list(de_pat.finditer(s))
n_sites = len(sites)
assert n_sites, 'no German gloss spans found'
sups = {}
for L in NEW:
    p = os.path.join(SRC, 'sup_%s.json' % L)
    sups[L] = [x.replace(NBSP, ' ') for x in json.load(io.open(p, encoding='utf-8'))]
    assert len(sups[L]) == n_sites, (L, len(sups[L]), n_sites)
    for x in sups[L]:
        assert x.strip() and '<' not in x and '>' not in x, (L, x)
out, last = [], 0
for i, mm in enumerate(sites):
    out.append(s[last:mm.end()])
    last = mm.end()
    for L in NEW:
        out.append('<span class="sup" data-lang="%s"><b>%s</b><span>%s</span></span>'
                   % (L, L.upper(), html.escape(sups[L][i], quote=False)))
out.append(s[last:])
s = ''.join(out)

# ---- 3. gloss CSS -------------------------------------------------------
rule_pat = re.compile(r'((?::root\[lang="(?:es|de)"\][^{}]*?)(?:,\s*:root\[lang="(?:es|de)"\][^{}]*?)*)\s*\{([^}]*)\}')
count = 0
def gen(match):
    global count
    sel, body = match.group(1), match.group(2)
    if '.sup[data-lang=' not in sel:
        return match.group(0)          # the data-boxw width knob: leave it
    parts = [p.strip() for p in sel.split(',')]
    tmpl = [p for p in parts if 'lang="es"' in p]
    assert tmpl, sel
    for p in parts:
        assert ('lang="es"' in p) or ('lang="de"' in p), sel
    new = []
    for L in GLOSS_LANGS:
        for t in tmpl:
            new.append(t.replace('"es"', '"%s"' % L))
    count += 1
    return ',\n'.join(new) + ' {' + body + '}'
s = rule_pat.sub(gen, s)
assert count, 'no es/de gloss rules found'

# ---- verify and write ---------------------------------------------------
for L in NEW:
    n = len(re.findall(r'<span class="sup" data-lang="%s">' % L, s))
    assert n == n_sites, (L, n, n_sites)
    assert len(re.findall(r':root\[lang="%s"\] \.sup\[data-lang="%s"\]' % (L, L), s)) == 1, L
d2 = json.loads(re.search(r'<script>window\.BW_TR=(\{.*?\});</script>', s, re.S).group(1))
assert all(len(d2[L]) == n_keys for L in GLOSS_LANGS), {L: len(d2[L]) for L in GLOSS_LANGS}
io.open(DECK, 'w', encoding='utf-8', newline='').write(s)
print('merged: bank %s x %d keys, %d glosses x %d languages, %d css rules generalised'
      % (sorted(d2.keys()), n_keys, n_sites, len(NEW), count))
