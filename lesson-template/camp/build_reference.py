#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build past-perfect-time-signals.html - the ninth 41-scene grammar reference.

The "Time Signals" family (claude/time-signals-pages.md) is a 1920x1080 stage,
41 sections, one scene each, Pixelify Sans / Silkscreen embedded, an ES/DE
support bar and nothing else. This takes past-simple-time-signals.html as the
SHELL - its fonts, stylesheet, chrome and script, verbatim - swaps the family's
tan for the past perfect's maroon, and fills the 41 sections from the Memory
Vault content Innes supplied (extracted to content.json / quiz.json).

Two things the Vault had that the family did not:

  * the font. The Vault embedded a 101-glyph "Minecraft Regular" with a broken
    capital A and no accents; everything non-ASCII fell back to Arial. The
    shell's Pixelify Sans and Silkscreen carry the whole Latin range, so the
    ES/DE lines render in the same face as the English for the first time.
  * ten MEMORY SHARD questions. Kept - as click-to-answer buttons in the
    family's own style, with a SHARDS counter in the nav bar. The family shell
    has no score, so the small script for it is added here.

    python3 lesson-template/camp/build_reference.py
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SHELL = os.path.join(ROOT, 'past-simple-time-signals.html')
OUT = os.path.join(ROOT, 'past-perfect-time-signals.html')
FOLDER = 'past-perfect-time-signals'
CONTENT = json.load(open(os.path.join(HERE, 'reference-content.json'), encoding='utf-8'))
QUIZ = {int(k): v for k, v in json.load(open(os.path.join(HERE, 'reference-quiz.json'), encoding='utf-8')).items()}

# ── the family's colour slots, remapped for the maroon page ─────────────
# The shell paints with six hexes. Every one is swapped, none is added.
COLOURS = {
    '#130F0B': '#12060A',   # page and stage ground - darkened maroon
    '#19130E': '#1A0A0C',   # the 8-way pixel outline behind every glyph
    '#4C3C2F': '#4C2A31',   # chrome borders
    '#DCC7B4': '#E6CDD2',   # chrome text
    '#B08968': '#D66D77',   # chrome accent: the past perfect's ink (COLOUR-RULES: the
                            # route-map maroon #6E0B24 lifted in Lab until it reads)
    '#1F1711': '#1F0A0E',   # text on the pressed accent button
}
TITLE = '#55C1FF'           # h2 colour - the family's blue, kept ("every deck needs blue")
TURN = '#7FE046'            # YOUR TURN green, family-wide
GOLD = '#FFD65A'            # the question line on a shard slide

# A word being NAMED takes inverted commas, in every language (house style
# 8.24). These are the named words per slide, applied to meaning and practice.
QUOTE = {
    6: ['Had'], 7: ['had'], 12: ['Went', 'had', 'gone'], 13: ['Been', 'be'],
    14: ['Had repaired'], 15: ['had not'], 16: ['Hadn’t', 'hadn’t', 'had not'],
    18: ['had'], 20: ['had'], 21: ['By the time'], 22: ['Before'], 23: ['After'],
    25: ['Already', 'already'], 26: ['Just'], 27: ['Never', 'never'], 29: ['Yet'],
}
# ...and the YOUR TURN line names a word on these slides only - on slide 12
# 'had' is part of the sentence to correct, not a word being named.
QUOTE_PRACTICE = {16, 25, 27}
# Copy corrections to the supplied text.
FIX = {
    (1, 'kicker_en'): 'B1 GRAMMAR GUIDE',
    (1, 'kicker_es'): 'GUÍA DE GRAMÁTICA B1',
    (1, 'kicker_de'): 'GRAMMATIK-GUIDE B1',
    (2, 'kicker_es'): 'LA CÁMARA DE LA MEMORIA',
    # the two longest slides ran off the bottom in German; trimmed to fit
    (40, 'example_en'): 'The allay crossed the line first. Laura arrived later.',
    (40, 'example_es'): 'El allay cruzó primero la meta. Laura llegó después.',
    (40, 'example_de'): 'Der Allay überquerte zuerst das Ziel. Laura kam später an.',
    (40, 'meaning_en'): 'Which sentence makes the order clear?',
    (40, 'meaning_es'): '¿Qué oración aclara el orden?',
    (40, 'meaning_de'): 'Welcher Satz macht die Reihenfolge klar?',
    (41, 'example_en'): 'By the time Dale arrived, Laura had opened the vault.',
    (41, 'example_es'): 'Cuando Dale llegó, Laura ya había abierto la cámara.',
    (41, 'example_de'): 'Als Dale ankam, hatte Laura das Archiv bereits geöffnet.',
    (41, 'meaning_en'): 'Tell the story in six sentences.',
    (41, 'meaning_es'): 'Cuenta la historia en seis oraciones.',
    (41, 'meaning_de'): 'Erzähle die Geschichte in sechs Sätzen.',
    (41, 'practice_en'): 'Shards: 8–10 Vault Master · 5–7 Keeper · 0–4 again.',
    (41, 'practice_es'): 'Fragmentos: 8–10 Maestro · 5–7 Guardián · 0–4 otra vez.',
    (41, 'practice_de'): 'Scherben: 8–10 Meister · 5–7 Hüter · 0–4 noch einmal.',
    (41, 'form_en'): 'HAD + PAST PARTICIPLE → PAST SIMPLE',
    (41, 'form_es'): 'HAD + PARTICIPIO PASADO → PAST SIMPLE',
    (41, 'form_de'): 'HAD + PAST PARTICIPLE → PAST SIMPLE',
    (40, 'title_en'): 'CHOOSE THE SENTENCE',
    (40, 'form_en'): 'EARLIER: PAST PERFECT · LATER: PAST SIMPLE',
    (40, 'form_es'): 'ANTES: PAST PERFECT · DESPUÉS: PAST SIMPLE',
    (40, 'form_de'): 'FRÜHER: PAST PERFECT · SPÄTER: PAST SIMPLE',
}


def quote_named(text, words):
    for w in words:
        text = re.sub(r'(?<![\w‘])%s(?![\w’])' % re.escape(w), '‘%s’' % w, text)
    return text


def esc(t):
    t = html.escape(t, quote=False)
    # the family keeps the last two words together so a line never ends on
    # one orphaned word
    parts = t.rsplit(' ', 1)
    return '&nbsp;'.join(parts) if len(parts) == 2 and len(t) > 24 else t


OUTLINE = ('text-shadow:-3px 0px 0 %(o)s,3px 0px 0 %(o)s,0px -3px 0 %(o)s,0px 3px 0 %(o)s,'
           '-3px -3px 0 %(o)s,3px -3px 0 %(o)s,-3px 3px 0 %(o)s,3px 3px 0 %(o)s,0 0 10px %(o)s')
OUTLINE4 = OUTLINE.replace('3px', '4px').replace('10px', '14px')
NOLIG = "font-variant-ligatures:none;font-feature-settings:'liga' 0,'clig' 0,'dlig' 0,'calt' 0"
O = {'o': COLOURS['#19130E']}


def sup(es, de, right):
    rev = ';flex-direction:row-reverse' if right else ''
    def one(code, text):
        return ('<span class="sup" data-lang="%s"><div style="display:flex;align-items:baseline;gap:14px%s">'
                '<span style="font:400 28px Silkscreen,monospace;color:#FFFFFF;%s;%s">%s</span>'
                '<span style="font:400 30px/1.18 \'Pixelify Sans\',monospace;color:#D9D9D9;%s;%s">%s</span>'
                '</div></span>' % (code, rev, OUTLINE % O, NOLIG, code.upper(), OUTLINE % O, NOLIG, esc(text)))
    return one('es', es) + one('de', de)


def row(label, text, colour, es, de, right, size='40px'):
    return ('<div style="display:flex;align-items:baseline;gap:24px;flex-wrap:wrap">'
            '<span style="font:700 34px \'Pixelify Sans\',monospace;color:#FFFFFF;letter-spacing:2px;min-width:250px;%s;%s">%s</span>'
            '<span style="font:500 %s/1.35 \'Pixelify Sans\',monospace;color:%s;flex:1 1 0;min-width:0;%s;%s">%s</span></div>'
            % (OUTLINE % O, NOLIG, label, size, colour, OUTLINE % O, NOLIG, esc(text))
            + sup(es, de, right))


def section(s):
    n = s['n']
    right = 'pos-right' in s['cls']
    d = {k: s[k] for k in s if k.endswith(('_en', '_es', '_de'))}
    for (sn, key), v in FIX.items():
        if sn == n:
            d[key] = v
    for slot in ('meaning', 'practice'):
        if slot == 'practice' and n not in QUOTE_PRACTICE:
            continue
        for lang in ('en', 'es', 'de'):
            d['%s_%s' % (slot, lang)] = quote_named(d['%s_%s' % (slot, lang)], QUOTE.get(n, []))
    q = QUIZ.get(n)
    label = html.escape(re.sub(r'\s+', ' ', d['title_en']).title() if n > 1 else 'Past Perfect')
    col = ('display:flex;flex-direction:column;justify-content:flex-start;gap:%s;padding:%s 90px 92px;'
           'max-width:1150px;box-sizing:border-box' % ('10px' if q else '16px', '110px' if n == 1 else '56px'))
    if right:
        col += ';align-items:flex-end;text-align:right;margin-left:auto'
    out = ['<section data-label="%s" data-screen-label="%02d %s"%s>' % (label, n, label, ' data-quiz="%d"' % n if q else ''),
           '<img draggable="false" alt="" src="%s/bg%02d.jpg" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover">' % (FOLDER, n),
           '<div style="position:absolute;inset:0;background:%s26"></div>' % COLOURS['#130F0B'],
           '<div style="position:absolute;inset:0;%s">' % col,
           '<div style="font:700 34px \'Pixelify Sans\',monospace;color:#FFFFFF;letter-spacing:3px;%s;%s">%s</div>'
           % (OUTLINE % O, NOLIG, esc(d['kicker_en'])) + sup(d['kicker_es'], d['kicker_de'], right)]
    if n == 1:
        out.append('<h1 style="font:700 104px/1 \'Pixelify Sans\',monospace;white-space:nowrap;color:%s;margin:0;%s;%s">Past Perfect</h1>'
                   % (TITLE, OUTLINE4 % O, NOLIG) + sup('Pluscuamperfecto', 'Plusquamperfekt', right))
        out.append('<h2 style="font:700 58px/1.1 \'Pixelify Sans\',monospace;letter-spacing:4px;color:#FFFFFF;margin:0;%s;%s">THE MEMORY VAULT</h2>'
                   % (OUTLINE4 % O, NOLIG) + sup('LA CÁMARA DE LA MEMORIA', 'DAS ERINNERUNGSARCHIV', right))
    else:
        t = d['title_en']
        t = t if t.isupper() and len(t) <= 12 else t.capitalize() if t.isupper() else t
        out.append('<h2 style="font:700 %s/1.06 \'Pixelify Sans\',monospace;color:%s;margin:0;%s;%s">%s</h2>'
                   % ('92px' if len(t) <= 19 else '72px', TITLE, OUTLINE4 % O, NOLIG, esc(t))
                   + sup(d['title_es'], d['title_de'], right))
    # meaning, then example - the family's order (what it means, then the line)
    out.append('<p style="font:600 %s/1.28 \'Pixelify Sans\',monospace;color:%s;margin:0;%s;%s">%s</p>'
               % ('40px' if q else '44px', GOLD if q else '#FFFFFF', OUTLINE % O, NOLIG, esc(d['meaning_en'])) + sup(d['meaning_es'], d['meaning_de'], right))
    if n > 1:
        out.append('<p style="font:600 %s/1.28 \'Pixelify Sans\',monospace;color:#FFFFFF;margin:0;%s;%s">%s</p>'
                   % ('44px' if q else '50px', OUTLINE % O, NOLIG, esc(d['example_en'])) + sup(d['example_es'], d['example_de'], right))
    if q:
        out.append('<div class="choices" style="display:flex;flex-direction:column;gap:10px;%s">' % ('align-items:flex-end' if right else 'align-items:flex-start'))
        for i, c in enumerate(q):
            out.append('<button class="choice" data-key="%d"><span class="k">%s</span>'
                       '<span style="display:flex;flex-direction:column;gap:4px;%s"><span>%s</span>%s</span></button>'
                       % (1 if c['key'] else 0, 'AB'[i], 'align-items:flex-end' if right else '', html.escape(c['en']),
                          sup(c['es'], c['de'], right)))
        out.append('<div class="verdict" aria-live="polite"></div></div>')
    tail = [row('FORM', d['form_en'], '#FFFFFF', d['form_es'], d['form_de'], right, '34px' if q else '40px')]
    if not q:
        tail.append(row('YOUR TURN', d['practice_en'], TURN, 'TU TURNO: ' + d['practice_es'], 'DU BIST DRAN: ' + d['practice_de'], right))
    out.append('<div style="margin-top:auto;display:flex;flex-direction:column;gap:10px;%s">%s</div>'
               % ('align-items:flex-end;' if right else '', ''.join(tail)))
    out.append('</div>\n</section>')
    return '\n'.join(out)


QUIZ_CSS = """
/* --- memory shards: ten click-to-answer slides ------------------------ */
.choice{display:flex;align-items:baseline;gap:22px;font:500 36px/1.25 'Pixelify Sans',monospace;color:#FFFFFF;
  background:%(ground)sD9;border:3px solid %(accent)s99;padding:10px 22px;cursor:pointer;text-align:left;max-width:1000px;
  %(nolig)s}
.choice .k{font:400 26px Silkscreen,monospace;color:%(accent)s;min-width:34px}
.choice .sup span{font-size:26px!important;line-height:1.15!important}
.choice .sup span:first-child{font-size:22px!important}
.choice:hover{border-color:%(accent)s}
.choice.hit{border-color:%(turn)s;background:#0F2A18E6}
.choice.miss{border-color:%(accent)s;background:#3A0C16E6;color:#E6CDD2}
.choice[disabled]{cursor:default}
.verdict{font:400 22px Silkscreen,monospace;color:%(turn)s;letter-spacing:1px;min-height:28px}
.verdict.miss{color:%(accent)s}
#shards{font:400 13px Silkscreen,monospace;color:%(text)s;min-width:110px;text-align:center}
""" % dict(ground=COLOURS['#130F0B'], accent=COLOURS['#B08968'], turn=TURN, text=COLOURS['#DCC7B4'], nolig=NOLIG)

QUIZ_JS = """
<script>
(function(){
  /* MEMORY SHARDS. One answer per slide, ten slides, a lit shard for each
     right one. Nothing is stored: the count is for this read-through. */
  var lit = 0, total = document.querySelectorAll('section[data-quiz]').length;
  var shards = document.getElementById('shards');
  function paint(){ shards.textContent = 'SHARDS ' + lit + ' / ' + total; }
  document.querySelectorAll('section[data-quiz]').forEach(function(sec){
    var btns = sec.querySelectorAll('.choice'), v = sec.querySelector('.verdict');
    btns.forEach(function(b){
      b.addEventListener('click', function(){
        if (sec.dataset.done) return;
        sec.dataset.done = '1';
        var ok = b.dataset.key === '1';
        b.classList.add(ok ? 'hit' : 'miss');
        btns.forEach(function(x){ x.disabled = true; if (x !== b && x.dataset.key === '1') x.classList.add('hit'); });
        if (ok) lit++;
        v.textContent = ok ? 'CORRECT · +1 MEMORY SHARD' : 'NOT YET · THE GREEN ONE IS THE FORM';
        v.classList.toggle('miss', !ok);
        paint();
      });
    });
  });
  paint();
})();
</script>
"""


def main():
    src = open(SHELL, encoding='utf-8').read()
    head, rest = src.split('<body', 1)
    body_open = '<body' + rest[:rest.find('>') + 1]
    rest = rest[rest.find('>') + 1:]
    stage_i = rest.find('<div id="viewport"><div id="stage">')
    stage_j = rest.rfind('</section>') + len('</section>')
    before, after = rest[:stage_i], rest[stage_j:]

    # 1. colours, everywhere in the shell
    for a, b in COLOURS.items():
        head = head.replace(a, b)
        before = before.replace(a, b)
        after = after.replace(a, b)
    # 2. head: title, description, drop the old SEO block (seo.py / the row
    #    writes the right one), keep the family's meta shape
    # Keep the FENCE (empty) so seo.inject() replaces it: the family head also
    # carries four hand-written og: tags after <title>, and an unfenced page
    # with og: tags is one inject() refuses to touch.
    head = re.sub(r'<!-- SEO:start -->.*?<!-- SEO:end -->', '<!-- SEO:start -->\n<!-- SEO:end -->', head, flags=re.S)
    head = re.sub(r'<title>[^<]*</title>', '<title>Past Perfect: Time Signals (Minecraft ed.) (B1) | Forbes English</title>', head)
    desc = ('A B1 grammar reference for the past perfect: the earlier of two past actions, had + third form, '
            'questions and negatives, and the time signals - across 41 scenes with ten memory-shard checks. '
            'Spanish and German support available.')
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % desc, head)
    head = head.replace('<meta property="og:title" content="Past Simple: Time Signals">',
                        '<meta property="og:title" content="Past Perfect: Time Signals">')
    head = head.replace('<meta property="og:description" content="A1 grammar reference — present perfect time signals.">',
                        '<meta property="og:description" content="B1 grammar reference — past perfect time signals.">')
    head = head.replace('past-simple-time-signals/bg01.jpg', FOLDER + '/bg18.jpg')
    head = head.replace('</style>', QUIZ_CSS + '</style>')
    # 3. the nav bar gains the shard counter
    after = after.replace('<span id="count">01 / 41</span>',
                          '<span id="shards">SHARDS 0 / 10</span>\n  <span id="count">01 / 41</span>')
    after = after.replace('</script>\n</body>', '</script>' + QUIZ_JS + '</body>')

    sections = '\n'.join(section(s) for s in CONTENT)
    out = head + body_open + before + '<div id="viewport"><div id="stage">\n' + sections + '\n' + after

    # SEO block from a synthetic row, same route as the camp decks
    sys.path.insert(0, HERE)
    from build_camp import seo
    out = seo(out, dict(row=dict(file='past-perfect-time-signals.html',
                                 title='Past Perfect: Time Signals (Minecraft ed.)',
                                 level='B1', access='pro', deck=False, video=False,
                                 created_at='2026-09-04T00:00:00+00:00', sort_order=None),
                        card=FOLDER + '/bg18.jpg'))
    open(OUT, 'w', encoding='utf-8', newline='\n').write(out)
    n_sec = len(re.findall(r'<section ', out))
    n_img = len(re.findall(r'<img ', out))
    assert n_sec == 41 and n_img == 41, (n_sec, n_img)
    assert 'data:image' not in out
    print('built %s  %.0f KB  %d sections' % (OUT, os.path.getsize(OUT) / 1024, n_sec))


if __name__ == '__main__':
    main()
