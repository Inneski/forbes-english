# -*- coding: utf-8 -*-
"""The School Visit: Correction Test (A2–B1) — a 16:9 panel deck ("house
style 2") built from a one-page correction test Innes wrote for a student:
an author invited to talk about her book at a school, and the English she
produced about it.

Innes, 2026-10-02: *"make style 2 for this and take real names out"*. The
sheet named a real child; she is "my neighbour" throughout, and nothing
else in the deck identifies anyone.

Four parts, each opened by a divider (the plate whole) and a panel (the same
plate as a full-opacity column beside the instructions), sides alternating:
  1 Correct the mistakes   — 10 sentences, one per slide, typed whole
  2 Complete the sentences — 8 gaps, two rows a slide
  3 Ask the author         — 4 prompts in the learner's language → English
  4 Choose the expression  — 5 multiple choice
then results and the activation stage. 32 slides, EN/DE/ES.

Content decisions, so nobody re-litigates them against the sheet's key:
  * Every typed answer accepts the full stop, comma and contraction
    variants (`sentences()`), and every correct English the sheet's key
    did not list: "It rained here all day yesterday" (as well as "was
    raining"); "There is a generator in my house"; "I know nothing about
    the power cut"; "for explaining" and "in order to explain"; DOESN'T
    where the not-understanding is still true; "used to have"; MUCH for
    the two ANY/ANYTHING gaps. §7: a learner who is right and marked
    wrong is worse than one who is wrong and marked right.
  * Part 3's prompts are the only chrome written in the learner's
    language on purpose: in Spanish they are the sheet's own four lines,
    in English and German a child "wants to know …" — the task is the
    same (indirect → a direct question) and the key is unchanged.
  * MC 27's stem carried Spanish inside English; it is a translatable
    context line now, so the German deck does not quote Spanish.
  * Two-option multiple choice is the sheet's own format for 23–26 and
    is kept: the point is SAY/TELL and TO/FOR, a binary each time.

Art: Innes's 2026-10-02 renders from incoming/ ("screenprint texture,
minimal"), six of ten prepped into SchoolVisit/ by tools/prep-artwork.py.
Palette from plate-cover.jpg, --light, every row PASS.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_schoolvisit as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'school-visit-correction-test-a2-b1.html'
F = 'SchoolVisit'

E = I.T['en']

# py lesson-template/extract-palette.py SchoolVisit/plate-cover.jpg --light
# (2026-10-02, mountains under a pink moon; every row PASS)
PALETTE = """  --hero: url('%s/plate-cover.jpg');

  --void          : #d8d0ac;
  --surface       : #e1dcc4;
  --surface2      : #dcd5b8;
  --border        : #965e4a;
  --text          : #2a1711;
  --text-dim      : #5e3b2e;
  --accent        : #ad2d00;
  --accent-bright : #7a2000;
  --accent-dim    : #f06737;
  --secondary     : #4f6a6e;
  --contrast      : #075544;""" % F

# A panel is 548x720 out of a 16:9 source painted `cover`: it sees 42.6% of
# the width. `pos` picks the slice; set by eye from the contact sheet.
#   fix     the author at the board, pen raised, the class to her right
#   gaps    the author writing at her desk, sunlight across the page
#   ask     a boy turned to the author, the two of them in profile
#   choose  the author at the lectern on a pink wall, the class below
PIC = {1: 'plate-fix.jpg', 2: 'plate-gaps.jpg', 3: 'plate-ask.jpg',
       4: 'plate-choose.jpg'}
POS = {1: '14% 50%', 2: '28% 50%', 3: '10% 50%', 4: '50% 50%'}
SIDE = {1: 'left', 2: 'right', 3: 'left', 4: 'right'}
ACT_PIC = 'plate-act.jpg'


def sentences(*forms, end='.'):
    """Every accepted spelling of a typed sentence: with and without its
    final stop (or question mark), with and without its commas, and with
    straight or curly apostrophes — the engine's flatten() folds the last
    of those itself, but not punctuation. The first form is the one shown
    as "Answer: …"."""
    out = []
    for f in forms:
        bare = f.rstrip('.!?')
        for v in (bare + end, bare, bare.replace(',', '') + end,
                  bare.replace(',', '')):
            if v not in out:
                out.append(v)
    return '|'.join(out)


def neg(*forms, end='.'):
    """A sentence with a contracted negative, plus its full form."""
    full = []
    for f in forms:
        for a, b in (('don’t', 'do not'), ('didn’t', 'did not'),
                     ('doesn’t', 'does not'), ('I’m', 'I am'),
                     ('There’s', 'There is'), ('there’s', 'there is'),
                     ('What’s', 'What is')):
            if a in f and f.replace(a, b) not in forms:
                full.append(f.replace(a, b))
    return sentences(*(list(forms) + full), end=end)


# ══════════════════════════════════════════════════════════════════════
#  PART 1 · correct the mistakes — (wrong, accepted, why key)
# ══════════════════════════════════════════════════════════════════════
FIX = [
    ('My neighbour wants that I give a presentation in English about my book at her school.',
     neg('My neighbour wants me to give a presentation in English about my book at her school',
         'My neighbour wants me to give a presentation about my book in English at her school'),
     'a1w'),
    ('My neighbour said me that the children might ask questions.',
     neg('My neighbour told me that the children might ask questions',
         'My neighbour told me the children might ask questions',
         'My neighbour said to me that the children might ask questions',
         'My neighbour said that the children might ask questions'),
     'a2w'),
    ('The synopsis of my book don’t have a problem.',
     neg('The synopsis of my book doesn’t have a problem',
         'There’s no problem with the synopsis of my book',
         'The synopsis of my book has no problem',
         'The synopsis of my book has no problems',
         'The synopsis of my book doesn’t have any problems',
         'The synopsis of my book doesn’t have any problem'),
     'a3w'),
    ('My neighbour read the book, but she no understand the content.',
     neg('My neighbour read the book, but she didn’t understand the content',
         'My neighbour read the book, but she doesn’t understand the content',
         'My neighbour read the book, but didn’t understand the content',
         'My neighbour has read the book, but she doesn’t understand the content'),
     'a4w'),
    ('She no understand this part of the book.',
     neg('She didn’t understand this part of the book',
         'She doesn’t understand this part of the book'),
     'a5w'),
    ('I wrote this paragraph for explain my idea.',
     sentences('I wrote this paragraph to explain my idea',
               'I wrote this paragraph for explaining my idea',
               'I wrote this paragraph in order to explain my idea'),
     'a6w'),
    ('I don’t know nothing about the power cut.',
     neg('I don’t know anything about the power cut',
         'I know nothing about the power cut'),
     'a7w'),
    ('I don’t watching nothing TV.',
     neg('I don’t watch TV',
         'I don’t watch anything on TV',
         'I don’t watch any TV',
         'I’m not watching TV',
         'I’m not watching anything on TV'),
     'a8w'),
    ('In my house have a generator.',
     neg('We have a generator in our house',
         'We have a generator in my house',
         'I have a generator in my house',
         'There’s a generator in my house',
         'There’s a generator in our house',
         'In my house there’s a generator',
         'In my house, there’s a generator',
         'My house has a generator',
         'Our house has a generator'),
     'a9w'),
    ('It was rain here all day yesterday.',
     sentences('It was raining here all day yesterday',
               'It rained here all day yesterday'),
     'a10w'),
]

# ══════════════════════════════════════════════════════════════════════
#  PART 2 · complete the sentences — slides of two rows
# ══════════════════════════════════════════════════════════════════════
GAPS = [
    [('When the kids start asking questions, I ______. <em>(sweat)</em>',
      ['will be sweating|’ll be sweating|will sweat|’ll sweat'], 'b11w'),
     ('When I was young, I ______ more time.',
      ['had|used to have'], 'b12w')],
    [('She might understand this part of my book when she ______ up.',
      ['grows|is grown|has grown|’s grown'], 'b13w'),
     ('My neighbour ______ her teacher whether they played games in class. <em>(ask)</em>',
      ['asked'], 'b14w')],
    [('We don’t watch ______ TV at home.',
      ['any|much'], 'b15w'),
     ('I don’t watch ______ on TV.',
      ['anything|much'], 'b16w')],
    [('There was a power ______ during the storm.',
      ['cut|outage|failure'], 'b17w'),
     ('My neighbour ______ me she wanted to read the book. <em>(say / tell)</em>',
      ['told|said to'], 'b18w')],
]
GAP_W = [230, 190, 190, 190]


# ══════════════════════════════════════════════════════════════════════
#  PART 3 · ask the author — (prompt key, accepted, why key)
# ══════════════════════════════════════════════════════════════════════
def _kids():
    out = []
    for who in ('kids', 'children'):
        for what in ('your book', 'the book', 'it'):
            out += ['Can %s read %s too' % (who, what),
                    'Can %s read %s as well' % (who, what),
                    'Can %s also read %s' % (who, what)]
    return out


ASK = [
    ('c1x', sentences('What inspired you to write your book',
                      'What inspired you to write the book',
                      'What inspired you to write it',
                      'What gave you the inspiration to write your book',
                      'What gave you the inspiration to write the book',
                      end='?'), 'c1w'),
    ('c2x', neg('What’s your book about', 'What’s the book about',
                'What is your book about', 'What is the book about',
                end='?'), 'c2w'),
    ('c3x', sentences(*_kids(), end='?'), 'c3w'),
    ('c4x', sentences('Why not', 'Why can’t they', 'Why can’t we', end='?'), 'c4w'),
]

# ══════════════════════════════════════════════════════════════════════
#  PART 4 · choose the right expression
# ══════════════════════════════════════════════════════════════════════
# Options are never translated: they ARE the English being tested. Keys sit
# at different indexes; the engine shuffles at runtime as well.
MC = [
    dict(stem='“She ______ me about the presentation.”',
         options=['said', 'told'], correct=1, why='m1w'),
    dict(stem='“She ______ that the book was interesting.”',
         options=['said', 'told'], correct=0, why='m2w'),
    dict(stem='“I used a picture ______ the idea.”',
         options=['for explain', 'to explain'], correct=1, why='m3w'),
    dict(stem='“This diagram is useful ______ how the generator works.”',
         options=['for explaining', 'for explain'], correct=0, why='m4w'),
    dict(stem=E['m5s'],
         options=['In our house have a generator.',
                  'This is a generator in our house.',
                  'We have a generator in our house.'],
         correct=2, why='m5w'),
]


def divider(n):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=PIC[n], pos=POS[n])


def panel(n):
    return D.panel('e%d' % n, E['e%d' % n], 's%dt' % n, E['s%dt' % n],
                   [('s%da' % n, E['s%da' % n]),
                    ('s%db' % n, E['s%db' % n], 'dim')],
                   folder=F, pic=PIC[n], side=SIDE[n], pos=POS[n])


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest(MC)

    slides = "".join(
        [
            D.cover(logo, E['coverTitle'], E['coverSub'],
                    [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                     ('Count', E['chipCount'])]),

            # ── part 1 · correct the mistakes ─────────────────────────
            divider(1), panel(1),
        ] + [
            D.gap(i + 1, len(FIX),
                  [('<em>%s</em><br>______' % wrong, [answers], why)],
                  None, 'e1', E['e1'], 'a%dt' % (i + 1), E['a%dt' % (i + 1)],
                  hint=E['aHint'], hint_key='aHint', width=560, size=18)
            for i, (wrong, answers, why) in enumerate(FIX)
        ] + [
            # ── part 2 · complete the sentences ───────────────────────
            divider(2), panel(2),
        ] + [
            D.gap(i + 1, len(GAPS), rows, None, 'e2', E['e2'],
                  'b%dt' % (i + 1), E['b%dt' % (i + 1)],
                  hint=E['bHint'], hint_key='bHint', width=GAP_W[i])
            for i, rows in enumerate(GAPS)
        ] + [
            # ── part 3 · ask the author ───────────────────────────────
            divider(3), panel(3),
        ] + [
            D.gap(i + 1, 2,
                  [('<em data-i18n="%s">%s</em><br>______' % (xk, E[xk]),
                    [answers], why)
                   for xk, answers, why in ASK[i * 2:i * 2 + 2]],
                  None, 'e3', E['e3'], 'c%dt' % (i + 1), E['c%dt' % (i + 1)],
                  hint=E['cHint'], hint_key='cHint', width=520, size=18)
            for i in range(2)
        ] + [
            # ── part 4 · choose the right expression ──────────────────
            divider(4), panel(4),
        ] + [
            D.mc(i + 1, len(MC), q, 'e4', E['e4'],
                 'm%dt' % (i + 1), E['m%dt' % (i + 1)],
                 ctx=E['m5x'] if i == 4 else None,
                 ctx_key='m5x' if i == 4 else None,
                 stem_key='m5s' if i == 4 else None)
            for i, q in enumerate(MC)
        ] + [
            # ── results, then activation (§10b) ───────────────────────
            D.results(),
            D.activate(E['actTitle'], E['actUse'],
                       ['wants me to', 'told me that', 'said that',
                        'didn’t understand', 'to explain', 'anything',
                        'We have …', 'was raining', 'will be sweating',
                        'asked her whether'],
                       'Speaking', E['actSpeakBrief'],
                       [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                       E['actWriteKind'], E['actWriteBrief'],
                       E['actPlaceholder'],
                       folder=F, bg=ACT_PIC),
        ])

    # The count on the cover chip is typed in three languages; make a
    # mismatch fail here rather than on the live page.
    n = slides.count('<section class="slide')
    for code in I.T:
        assert I.T[code]['chipCount'].split()[0] == str(n), (
            'chipCount in %s says %s, the deck has %d slides'
            % (code, I.T[code]['chipCount'], n))

    langs = tuple(c for c in I.LANGS if c in I.T)
    D.assemble(TPL, OUT, slides, PALETTE,
               'The School Visit: Correction Test (A2–B1) | Forbes English',
               I, langs=langs)
    print('wrote %s — %d slides, %s' % (OUT, n, ','.join(langs)))


if __name__ == '__main__':
    build()
