# -*- coding: utf-8 -*-
"""IELTS Reading: Summary and Sentence Completion (C1), built as a 16:9 deck.

The second Reading deck, after True / False / Not Given. Its card on
`ielts-reading.html` names the lesson: "Where the word limit does the damage.
Answers come straight from the passage, spelling counts, and 'no more than
two words' means a three-word answer scores nothing however right it is."
So this is technique again, and the deck is built on one fact:

  **The marker compares your answer with the key. Not with the passage, not
  with your meaning.** A right idea in different words, a right word in the
  wrong form, a right phrase one word over the limit: each is understanding
  the text and scoring nothing for it.

Three teaching sections, twelve items and a sort:

  1. the shape of the task — the instruction line first, what counts as a
     word, and the box-of-options variant where the words are not in the
     text;
  2. copy, do not paraphrase — find the place by meaning, lift the word as
     printed, and the limit is a wall;
  3. the gap has a shape — predict the word class before looking, read the
     finished sentence, and spelling counts even in a copied word.

The sorting slide sorts ANSWERS, not rules: six things a candidate might
write, into what the marker does with them. Every item on the right is a way
of being right and getting nothing.

Six pictures, one per idea. A sheet of paper with three windows cut out is
the gaps; a metal stencil beside the shape it left is the copy; a parcel that
will not go through the letterbox is the word limit; a brass key against a
padlock whose teeth do not match is the grammar fit; and a pencil sharpened
to a point, shavings beside it, closes it.

Ten languages, all complete (`ielts_langs.LANGS`), the sort items included:
they are answers a candidate might write, described, not the English under test, so
they carry `data-i18n` keys that this builder adds after `sort_slide()`.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltscomp_data import (INSTRUCT, COPY, SHAPE, ALL,
                            SORT_BINS, SORT_ITEMS, SORT_WHY)
import i18n_ieltscomp as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-reading-completion.html'
F = 'ielts-reading-completion'

# python3 lesson-template/extract-palette.py ielts-reading-completion/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #121410;
  --surface       : #1e2219;
  --surface2      : #292e22;
  --border        : #a97b5e;
  --text          : #f5f3f2;
  --text-dim      : #bfaea3;
  --accent        : #e2ad8b;
  --accent-bright : #eeb794;
  --accent-dim    : #ca7a47;
  --secondary     : #98b4b0;
  --contrast      : #1dedda;''' % F

# The target language of this deck is a set of moves, not a set of phrases —
# which is why the chips read as instructions. English in every gloss: they are
# what the learner says to themselves in the exam room.
CHIPS = ['read the limit first', 'copy, not paraphrase', 'predict the class',
         'a number = one', 'spelling counts', 'hyphen = one word']

BG_SHAPE, BG_COPY, BG_LIMIT, BG_FIT = ('bg02.jpg', 'bg03.jpg',
                                       'bg04.jpg', 'bg05.jpg')

# A passage excerpt, a limit, a summary line and four answers fit the canvas at rest, but
# once a learner answers, the explanation and the "Answer:" line push the
# slide 23-24px past the bottom edge. check-lesson only measures slides
# unanswered, so it never saw it. Two options a row buys back two rows.
# Activity 3 was measured first; Activity 2 overflowed by the same 23px in
# German and Spanish only, which the first measurement missed because the
# checker's language switch did nothing (fixed in answered-overflow.js).
def two_up(html):
    return html.replace('<div class="opts">', '<div class="opts two-up">')


BG_ACT = 'bg06.jpg'


def _keyed_sort(html):
    """Give each sort item a UI_I18N key so it translates with the deck.

    `sort_slide()` writes the items bare. On this deck they are descriptions
    of answers ("Three words when the limit is two"), not English under test,
    and a German learner should read them in German. The engine moves the
    spans into the pool rather than cloning them, so a `data-i18n` on the
    span survives initialisation and `applyLang()` finds it."""
    for n, (text, b) in enumerate(SORT_ITEMS, 1):
        bare = '<span class="sort-item" data-bin="%d">%s</span>' % (b, text)
        keyed = ('<span class="sort-item" data-bin="%d" data-i18n="sort%d">'
                 '%s</span>' % (b, n, text))
        assert bare in html, 'sort item %d not found in slide' % n
        html = html.replace(bare, keyed, 1)
    return html

# Every English string on the slides is read from the i18n module, so the
# HTML and UI_I18N.en cannot drift apart. Until 2026-09-24 they were written
# out twice, and a correction to one copy would have missed the other.
E = I.T['en']


def card(p):
    """The six-item teach card for prefix p ('t1a', 't1b', …), from E."""
    return (p + 'h', E[p + 'h'], p + 'b', E[p + 'b'], p + 'n', E[p + 'n'])


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSCOMP')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_SHAPE)

        + "".join(D.mc(i + 1, len(INSTRUCT), q, 'mcaEyebrow', E['mcaEyebrow'],
                       'mcaTitle', E['mcaTitle'],
                       folder=F, bg=BG_SHAPE, ctx=q.get('ctx'))
                  for i, q in enumerate(INSTRUCT))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_COPY)

        + "".join(two_up(D.mc(i + 1, len(COPY), q, 'mcbEyebrow',
                              E['mcbEyebrow'], 'mcbTitle', E['mcbTitle'],
                              folder=F, bg=BG_LIMIT, ctx=q.get('ctx')))
                  for i, q in enumerate(COPY))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_FIT)

        + "".join(two_up(D.mc(i + 1, len(SHAPE), q, 'mccEyebrow',
                              E['mccEyebrow'], 'mccTitle', E['mccTitle'],
                              folder=F, bg=BG_FIT, ctx=q.get('ctx')))
                  for i, q in enumerate(SHAPE))

        + _keyed_sort(
            D.sort_slide(SORT_BINS, SORT_ITEMS,
                         'sortEyebrow', E['sortEyebrow'],
                         'sortTitle', E['sortTitle'],
                         'sortHint', E['sortHint'],
                         'sortWhy', folder=F, bg=BG_FIT,
                         bin_keys=['sortBin1', 'sortBin2']))

        + D.results('resNext', 'You can fill them. Now set them &rarr;', folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Reading: Summary and Sentence Completion (C1) | '
                   'Forbes English',
                   I, langs=LANGS)
    # Twelve items plus the six answers on the sorting slide: the engine scores
    # a sort per chip, so the cover chip has to say 18, not 13.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
