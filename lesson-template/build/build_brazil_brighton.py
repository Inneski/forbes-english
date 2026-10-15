# -*- coding: utf-8 -*-
"""Cold, Colder, the Coldest — From Brazil to Brighton (A1, adult, Brazilian).

House style 2 (the panel deck), 27 slides, EN / DE / ES / PT. Built
2026-10-15 from Innes's running notes of a 50-minute Preply trial class with
a Brazilian A1 learner living in Brighton. The notes are a transcript, not a
coursebook sheet, so the deck is built from what the class actually turned
up:

  * **Things the learner said she finds hard**: listening; "does" and
    "doesn't"; "of" ("I don't use of because I don't know how"); and a
    question about ARE ("My son's teachers are … Why use are?").
  * **What Innes taught on the spot**: cold / colder / the coldest, big /
    bigger / the biggest, expensive / more expensive / the most expensive,
    "one-syllable adjectives take -er and -est"; the Brighton accent (no R
    at the end of a word, an extra R before a vowel, the glottal stop).
  * **The vocabulary that came up**: lorry driver, van driver, taxi driver,
    chauffeur; the north of Scotland, the south of England; "How old is your
    son? — My son is 16 months."

None of the learner's own sentences, names or circumstances are on a slide.
The cast is new: Ana from Curitiba (the coldest state capital in Brazil —
true, and what "I live in the coldest city in Brazil" points at), her
husband Rafael, their son Theo, Rafael's cousin Lucas who found him a job,
and Callum, their teacher from the Black Isle. The visa threshold, the
penguin story and the Preply logistics in the notes are left out: none of
them is A1 language.

Stages and the defects each one answers:

  1. **I AM, he IS, they ARE** — the "why ARE?" question, and age with BE
     (Portuguese TEM 16 MESES; English IS 16 MONTHS OLD), which is the
     single most predictable Brazilian A1 error and the notes' own example.
  2. **Cold, colder, the coldest** — the four rules in one card each, plus
     THAN, plus GOOD → BETTER (Rafael's "the food is better"), and a sort.
  3. **Does he drive a taxi?** — the four driver jobs, then DO / DOES /
     DOESN'T with the -S that moves to DOES. The word-order task carries a
     spare DRIVES, which is wrong in every position.
  4. **How they talk in Brighton** — the three accent features as cards and
     one item. There is no audio; the spelling stands in for the sound.
  5. **Translate** — Português ⇄ English, the same direction-switch game as
     `build_possessive_adj.py`, written here for Portuguese. Six rows aim at
     exactly the transfer errors above: TER for age, MAIS FRIA QUE → COLDER
     THAN, DO BRASIL → IN Brazil after a superlative (the "of" problem from
     the other side), DOES at the front of a question, NÃO → DOESN'T.
     Accented letters may be typed bare (e → é, c → ç, a → ã …).

**Art — Innes, 2026-10-15: "pics are in plus extras and use the extras".**
Fourteen Midjourney plates in `BrazilBrighton/`, briefed in
docs/ARTWORK-brazil-brighton.md: four seafront renders (the brightest pier
view is the cover, `hero`; the others are `seafront-a/b/c`), two of Ana, four
of Scotland in winter, three of the homework kitchen and one street of
drivers. Every one is used. Within a stage the variants are dealt so that a
picture whose figure stands on the LEFT goes where the text does not: a
divider (full bleed), a panel's picture column, the centred results slide.
Questions, whose answers sit on the left, get a picture with its subject on
the right. `homework-3` shows a different, fair-haired learner, so it is on
the activation slide, which is about the learner, not about Ana.

Run from the repo root:  py lesson-template/build/build_brazil_brighton.py
"""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_brazil_brighton as I

TPL = 'lesson-template/lesson-template.html'
F = 'BrazilBrighton'
OUT = 'forbes-english-brazil-to-brighton-a1.html'
TITLE = 'Cold, Colder, the Coldest — From Brazil to Brighton (A1)'
SLOTS = ['hero', 'seafront-a', 'seafront-b', 'seafront-c', 'ana', 'ana-2',
         'cold', 'cold-2', 'cold-3', 'cold-4', 'drivers',
         'homework', 'homework-2', 'homework-3']
PIC = {s: '%s.jpg' % s for s in SLOTS}

E = I.T['en']

# py lesson-template/extract-palette.py BrazilBrighton/hero.jpg --light
# (2026-10-15; every row PASS)
PALETTE = """  --hero: url('%s/hero.jpg');

  --void          : #d6c4ae;
  --surface       : #e0d4c6;
  --surface2      : #dbcbb9;
  --border        : #96624a;
  --text          : #2a1911;
  --text-dim      : #5e3d2e;
  --accent        : #9a3405;
  --accent-bright : #6c2200;
  --accent-dim    : #e86b31;
  --secondary     : #acc9d3;
  --contrast      : #085447;""" % F


# ── reading panels: English in every language ─────────────────────────
READ = {
    1: ['Hi! I’m <strong>Ana</strong>. I <strong>am</strong> from Curitiba, in the south '
        'of Brazil. Now I live in Brighton with my husband, Rafael, and our son, Theo. '
        'Theo <strong>is</strong> sixteen months old.',
        'My English teacher <strong>is</strong> Callum. He <strong>is</strong> from '
        'Scotland. Theo’s nursery teachers <strong>are</strong> very kind. '
        '<strong>They are</strong> quiet and friendly.'],
    2: ['Curitiba is <strong>the coldest</strong> big city in Brazil. But in winter, '
        'Brighton is <strong>colder than</strong> Curitiba!',
        'Rafael wants to live in Scotland. “The food is <strong>better</strong>!” he '
        'says. Ana laughs: “Scotland? It’s <strong>colder</strong> and '
        '<strong>more expensive</strong>!”'],
    3: ['Rafael’s cousin, Lucas, found him a job in Brighton. '
        '<em>“<strong>Does</strong> Rafael drive a taxi?”</em> — <em>“No, he '
        '<strong>doesn’t</strong>. He <strong>drives</strong> a van.”</em>',
        'Lucas <strong>doesn’t</strong> drive. He works in a hotel. '
        '<em>“<strong>Does</strong> he like Brighton?”</em> — <em>“Yes, he '
        '<strong>does</strong>!”</em>'],
}


def panel(n, eyebrow, pic, side='left', pos='78% 50%'):
    a, b = READ[n]
    return D.panel(eyebrow, E[eyebrow], 'p%dt' % n, E['p%dt' % n],
                   [(None, a), (None, b)], folder=F, pic=PIC[pic], side=side, pos=pos)


def divider(n, pic):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=PIC[pic])


def teach(title_key, eyebrow_key, items, bg, cols=None):
    """items: (English head, body key, English example). The six-item form,
    so the rule translates and the head and example stay English."""
    return D.teach(eyebrow_key, E[eyebrow_key], title_key, E[title_key],
                   [(None, h, bk, E[bk], None, ex) for h, bk, ex in items],
                   cols=cols, folder=F, bg=PIC[bg])


TEACH_BE = [('I → AM', 'tA1', '“I AM from Brazil.”'),
            ('he · she · it → IS', 'tA2', '“Theo IS sixteen months old.”'),
            ('you · we · they → ARE', 'tA3', '“Theo’s teachers ARE kind.”'),
            ('Age: BE, not HAVE', 'tA4', '“I AM 32.” · “How old IS your son?”')]
TEACH_CMP = [('short: + ER / THE + EST', 'tB1', 'cold → colder → the coldest'),
             ('one vowel + one consonant', 'tB2', 'big → bigger → the biggest'),
             ('long: MORE / THE MOST', 'tB3', 'expensive → more expensive → the most expensive'),
             ('GOOD is different', 'tB4', 'good → better → the best')]
TEACH_JOBS = [('lorry driver', 'jA1', '“He drives a lorry to Scotland.”'),
              ('van driver', 'jA2', '“Rafael is a van driver.”'),
              ('taxi driver', 'jA3', '“Call a taxi driver!”'),
              ('chauffeur', 'jA4', '“The chauffeur opens the door.”')]
TEACH_DOES = [('he · she · it + VERB-S', 'tC1', '“He DRIVES a van.”'),
              ('DOES + he · she · it + VERB?', 'tC2', '“DOES he DRIVE a taxi?”'),
              ('he · she · it + DOESN’T + VERB', 'tC3', '“He DOESN’T DRIVE a lorry.”'),
              ('I · you · we · they → DO / DON’T', 'tC4', '“DO you drive?” · “I DON’T drive.”')]
TEACH_ACC = [('No R at the end', 'tE1', 'car → “cah” · river → “rivuh”'),
             ('An extra R', 'tE2', 'I saw it → “I saw-R-it”'),
             ('The T disappears', 'tE3', 'water → “wa’er” · Brighton → “Brigh’on”')]

# ── multiple choice ────────────────────────────────────────────────────
MC_BE = [
    dict(stem='Theo’s nursery teachers ____ very kind.',
         options=['is', 'am', 'are', 'be'], correct=2, why='q1w'),
    dict(stem='“How old is your son?” — “He ____ sixteen months old.”',
         options=['has', 'is', 'have', 'are'], correct=1, why='q2w'),
]
MC_CMP = [
    dict(stem='In winter, Brighton is ____ than Curitiba.',
         options=['more cold', 'the coldest', 'most cold', 'colder'], correct=3, why='q3w'),
    dict(stem='Curitiba is ____ big city in Brazil.',
         options=['colder', 'the most cold', 'the coldest', 'most coldest'], correct=2,
         why='q4w'),
]
MC_DOES = [
    dict(stem='“____ your husband drive a taxi?”',
         options=['Is', 'Does', 'Do', 'Are'], correct=1, why='q5w'),
    dict(stem='Rafael ____ a lorry. He drives a van.',
         options=['doesn’t drive', 'don’t drive', 'doesn’t drives', 'isn’t drive'],
         correct=0, why='q6w'),
]
MC_ACC = [
    dict(ctx='c8', stem='water → “wa’er”', options=['R', 'W', 'T', 'D'], correct=2,
         why='q8w'),
]
for group in (MC_BE, MC_CMP, MC_DOES, MC_ACC):
    D.assert_no_key_is_longest(group)

# ── gap fill ───────────────────────────────────────────────────────────
GAP_BE = [('I ______ from Curitiba.', ['am'], 'g1w'),
          ('Rafael and Lucas ______ cousins.', ['are'], 'g2w'),
          ('Callum ______ from the north of Scotland.', ['is'], 'g3w')]
GAP_CMP = [('Brazil is ______ than Scotland. <span class="dim">(hot)</span>',
            ['hotter'], 'g4w'),
           ('Rafael says the food in Scotland is ______. <span class="dim">(good)</span>',
            ['better'], 'g5w'),
           ('London is ______ than Brighton. <span class="dim">(big)</span>',
            ['bigger'], 'g6w')]

# ── sort: -ER / -EST or MORE / MOST ────────────────────────────────────
SORT_ITEMS = [('cold', 0), ('expensive', 1), ('big', 0), ('beautiful', 1),
              ('hot', 0), ('difficult', 1), ('small', 0), ('interesting', 1),
              ('old', 0), ('famous', 1)]

# ── word order, each with a spare piece that fits nowhere ─────────────
ORDERS = [(['Does', 'Rafael', 'drive', 'a van?'], ['drives'], 'o1w')]

# ── translation: (Portuguese, English, more English, more Portuguese, why)
TR = [
    [('Eu sou do Brasil.', 'I am from Brazil.', ['I’m from Brazil.'],
      ['Sou do Brasil.'], 'tw1'),
     ('Meu filho tem dezesseis meses.', 'My son is sixteen months old.',
      ['My son is 16 months old.', 'My son is sixteen months.', 'My son is 16 months.'],
      ['O meu filho tem dezesseis meses.', 'Meu filho tem 16 meses.',
       'O meu filho tem 16 meses.'], 'tw2'),
     ('A Escócia é mais fria que o Brasil.', 'Scotland is colder than Brazil.', [],
      ['A Escócia é mais fria do que o Brasil.', 'Escócia é mais fria que o Brasil.',
       'Escócia é mais fria do que o Brasil.'], 'tw3')],
    [('Curitiba é a cidade mais fria do Brasil.', 'Curitiba is the coldest city in Brazil.',
      [], [], 'tw4'),
     ('Seu marido dirige um táxi?', 'Does your husband drive a taxi?', [],
      ['O seu marido dirige um táxi?', 'Seu marido dirige táxi?',
       'O seu marido dirige táxi?'], 'tw5'),
     ('Ele não dirige um caminhão.', 'He doesn’t drive a lorry.',
      ['He does not drive a lorry.', 'He doesn’t drive a truck.',
       'He does not drive a truck.'],
      ['Ele não dirige caminhão.'], 'tw6')],
]


def _bare(s):
    """é → e, ç → c, ã → a: a keyboard with no Portuguese layout."""
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def _expand(sentences, portuguese):
    """Every spelling a right answer might be typed in. The engine already
    ignores case, spacing and curly-vs-straight apostrophes."""
    out = []

    def add(s):
        if s not in out:
            out.append(s)
    for s in sentences:
        forms = [s]
        if not portuguese:
            for a, b in (('I am', 'I’m'),):
                forms += [f.replace(a, b) for f in forms if a in f and b not in s]
        else:
            forms += [_bare(f) for f in forms if _bare(f) != f]
        for f in forms:
            add(f)
            add(f.rstrip('.?!'))
    assert not any('|' in s for s in out)
    return '|'.join(D.esc(s) for s in out)


def translate(n, rows, total, pic):
    body = []
    for pt, en, more_en, more_pt, why in rows:
        ans_en = _expand([en] + more_en, portuguese=False)
        ans_pt = _expand([pt] + more_pt, portuguese=True)
        body.append('''<div class="card gap-row tr-row" data-src-pt="%s" data-src-en="%s" style="padding:12px 18px">
          <p class="q-stem" style="margin-bottom:0;font-size:22px"><span class="tr-src">%s</span> <span class="tr-arrow" aria-hidden="true">→</span> <input class="gap tr-in" data-answer="%s" data-ans-en="%s" data-ans-pt="%s" aria-label="translation" autocomplete="off" spellcheck="false"></p>
          <p class="feedback" data-explain="%s"></p>
        </div>''' % (D.esc(pt), D.esc(en), pt, ans_en, ans_en, ans_pt, why))
    return '''
    <section class="slide" data-type="gap" data-translate%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="e5">%s</span> &middot; %d / %d</div>
        <h2 class="slide-title" data-i18n="trT">%s</h2>
      </div>
        <div class="tr-toggle" role="group" aria-label="Translation direction">
          <button type="button" class="tr-dir is-on" data-dir="pt-en" aria-pressed="true">Português → English</button>
          <button type="button" class="tr-dir" data-dir="en-pt" aria-pressed="false">English → Português</button>
        </div>
      </div>
      <div class="slide-body">%s
        %s
        <div style="margin-top:10px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
''' % (D._bg(F, PIC[pic]), E['e5'], n, total, E['trT'],
       # The switch is explained once, on the first slide: the second one
       # needs the room for its three explanations once it is answered.
       ('\n        <p class="prose dim" style="margin-bottom:6px;font-size:16px" '
        'data-i18n="trHint">%s</p>' % E['trHint']) if n == 1 else '',
       "\n        ".join(body))


# The translate kit from build_possessive_adj.py, with Portuguese in place of
# German. The switch is global, so a learner who picks English → Português
# keeps it on the next slide; a checked slide is locked, because swapping the
# answer set after marking would rewrite history.
TRANSLATE_KIT = '''
    <style>
      .tr-toggle { display:inline-flex; flex:none; gap:0; margin:0; border:2px solid var(--accent);
                   border-radius:999px; overflow:hidden; }
      .tr-dir { font:700 17px/1 'DM Sans',sans-serif; padding:10px 20px; border:0; cursor:pointer;
                background:transparent; color:var(--accent); }
      .tr-dir.is-on { background:var(--accent); color:var(--void); }
      .tr-dir:disabled { cursor:default; opacity:.55; }
      .tr-row .tr-src { font-weight:700; }
      .tr-row .tr-arrow { color:var(--accent); font-weight:700; }
      .tr-row input.tr-in { width:470px; font-size:21px; }
    </style>
    <script>
    (function () {
      var dir = 'pt-en';
      function apply(slide) {
        if (slide.querySelector('.tr-in:disabled')) return;   // already marked
        slide.querySelectorAll('.tr-dir').forEach(function (b) {
          var on = b.dataset.dir === dir;
          b.classList.toggle('is-on', on);
          b.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
        slide.querySelectorAll('.tr-row').forEach(function (r) {
          var src = r.querySelector('.tr-src'), g = r.querySelector('.tr-in');
          var from = dir === 'pt-en' ? 'pt' : 'en', to = dir === 'pt-en' ? 'en' : 'pt';
          if (src.textContent !== r.getAttribute('data-src-' + from)) g.value = '';
          src.textContent = r.getAttribute('data-src-' + from);
          src.lang = from;
          g.lang = to;
          g.dataset.answer = g.getAttribute('data-ans-' + to);
        });
      }
      document.addEventListener('click', function (e) {
        var b = e.target.closest('.tr-dir');
        if (b && !b.disabled) {
          dir = b.dataset.dir;
          document.querySelectorAll('.slide[data-translate]').forEach(apply);
          return;
        }
        var c = e.target.closest('.slide[data-translate] [data-action="check"]');
        if (c) c.closest('.slide').querySelectorAll('.tr-dir')
                .forEach(function (x) { x.disabled = true; });
      }, true);
    })();
    </script>
'''


def slides():
    # pics: one per question, so a stage can deal its picture variants.
    mc = lambda qs, ek, tk, pics: [
        D.mc(i + 1, len(qs), q, ek, E[ek], tk, E[tk], folder=F, bg=PIC[pics[i]],
             ctx=E[q['ctx']] if 'ctx' in q else None, ctx_key=q.get('ctx'))
        for i, q in enumerate(qs)]
    # Not in teaching order: the BANK gate reads activation chips as a word
    # bank, and teaching order is the gap order.
    chips = ['better', 'doesn’t', 'colder than', 'are', 'the most', 'does', 'is',
             'the coldest', 'am']
    return "".join([
        D.cover(D.logo_from(TPL), E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        # ── stage 1 · I AM, he IS, they ARE ────────────────────────────
        divider(1, 'ana'),
        panel(1, 'e1', 'ana-2', pos='24% 50%'),
        teach('tAt', 'eR', TEACH_BE, 'ana', cols='1fr 1fr'),
        D.gap(1, 1, GAP_BE, None, 'e1', E['e1'], 'gapT', E['gapT'], folder=F,
              bg=PIC['ana'], hint=E['gapHint1'], hint_key='gapHint1', size=24),
    ] + mc(MC_BE, 'e1', 'mcT', ['ana', 'ana']) + [

        # ── stage 2 · cold, colder, the coldest ────────────────────────
        divider(2, 'cold-3'),
        panel(2, 'e2', 'cold-2', side='right', pos='72% 50%'),
        teach('tBt', 'eR', TEACH_CMP, 'cold', cols='1fr 1fr'),
    ] + mc(MC_CMP, 'e2', 'mcT', ['cold', 'cold-2']) + [
        D.gap(1, 1, GAP_CMP, None, 'e2', E['e2'], 'gapT', E['gapT'], folder=F,
              bg=PIC['cold'], hint=E['gapHint2'], hint_key='gapHint2', size=24),
        D.sort_slide([E['binA'], E['binB']], SORT_ITEMS, 'e2', E['e2'],
                     'sortT', E['sortT'], 'sortHint', E['sortHint'], 'sortWhy',
                     bin_keys=['binA', 'binB'], folder=F, bg=PIC['cold-4']),

        # ── stage 3 · does he drive a taxi? ────────────────────────────
        divider(3, 'drivers'),
        panel(3, 'e3', 'drivers'),
        teach('jAt', 'eV', TEACH_JOBS, 'drivers', cols='1fr 1fr'),
        teach('tCt', 'eR', TEACH_DOES, 'drivers', cols='1fr 1fr'),
    ] + mc(MC_DOES, 'e3', 'mcT', ['drivers', 'drivers']) + [
        D.order(items, 'e3', E['e3'], 'orderT', E['orderT'], 'orderHint',
                E['orderHint'], why, folder=F, bg=PIC['drivers'], decoys=dec)
        for items, dec, why in ORDERS
    ] + [

        # ── stage 4 · the Brighton accent, back on the seafront
        teach('tEt', 'e4', TEACH_ACC, 'seafront-b'),
    ] + mc(MC_ACC, 'e4', 'mc4T', ['seafront-a']) + [

        # ── stage 5 · translate ────────────────────────────────────────
        TRANSLATE_KIT,
    ] + [translate(i + 1, r, len(TR), pic)
         for i, (r, pic) in enumerate(zip(TR, ['homework', 'homework-2']))] + [
        D.results(folder=F, bg=PIC['seafront-c']),
        D.activate(E['actTitle'], E['actUse'], chips, 'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=PIC['homework-3']),
    ])


def build():
    s = slides()
    D.assemble(TPL, OUT, s, PALETTE, TITLE, I, langs=('en', 'de', 'es', 'pt'))
    print('wrote %s — %d slides' % (OUT, s.count('<section class="slide')))


if __name__ == '__main__':
    build()
