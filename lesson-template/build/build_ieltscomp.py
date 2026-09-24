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


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSCOMP')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Summary and <em>Sentence Completion</em>',
                'Where the word limit does the damage &mdash; answers come '
                'straight from the passage, spelling counts, and one word '
                'too many scores nothing',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Reading &middot; both modules'),
                 ('Count', '18 points')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'Three gaps, one instruction line, and the line '
                             'comes first',
                  [('t1ah', 'What you are given', 't1ab',
                    'A summary of part of the passage, or a set of separate '
                    'sentences, with gaps in them. The words that fill the '
                    'gaps are in the passage. The summary usually runs in '
                    'passage order, but it covers only a section &mdash; find '
                    'where that section starts and stay in it.', 't1an',
                    'Academic and General Training set it the same way. '
                    'Everything here applies to both.'),
                   ('t1bh', 'Read the instruction first', 't1bb',
                    '<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
                    'ONLY.</strong> The limit is printed above the gaps and '
                    'it is the first thing to read &mdash; before the summary, '
                    'before the passage. It decides what a correct answer '
                    'looks like before you have found one.', 't1bn',
                    'A hyphenated word is one word. A number is a number, not '
                    'a word. <em>The</em> is a word, and it counts.'),
                   ('t1ch', 'Sometimes there is a box', 't1cb',
                    'When the task gives you a list of words, A&ndash;H, you '
                    'choose from the list, not from the passage, and you '
                    'write the letter. The words might not be in the text at '
                    'all, and the list has more options than gaps.', 't1cn',
                    'Same skill underneath: find the place in the passage, '
                    'then check the grammar of the gap.')],
                  folder=F, bg=BG_SHAPE)

        + "".join(D.mc(i + 1, len(INSTRUCT), q, 'mcaEyebrow',
                       'Activity 1 &middot; Read the instruction', 'mcaTitle',
                       'What does the limit allow?',
                       folder=F, bg=BG_SHAPE, ctx=q.get('ctx'))
                  for i, q in enumerate(INSTRUCT))

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'The word is in the passage. Lift it.',
                  [('t2ah', 'Find the place by meaning', 't2ab',
                    'The summary does not repeat the passage; it paraphrases '
                    'everything <strong>around</strong> the gap. Match the '
                    'meaning of the sentence to find the right lines, then '
                    'read those lines for the one word the summary did not '
                    'change.', 't2an',
                    'A shared word tells you where to look. The gap word is '
                    'usually the one word that was not paraphrased.'),
                   ('t2bh', 'Then copy it, exactly', 't2bb',
                    'Same spelling, same form as printed. Do not make it '
                    'plural, do not change the tense, do not add an article '
                    'the summary already has. A correct idea in your own '
                    'words scores nothing, because the marker compares your '
                    'answer with the key, not with the passage.', 't2bn',
                    'If your word is not in the passage, it is not the '
                    'answer.'),
                   ('t2ch', 'The limit is a wall', 't2cb',
                    'Under NO MORE THAN TWO WORDS, a three-word answer scores '
                    'nothing however right it is. Not half a mark: nothing. '
                    'When an answer runs over, the extra word is almost '
                    'always an article or an adjective you did not need.',
                    't2cn',
                    'Write the answer, count it, then read the instruction '
                    'line again.')],
                  folder=F, bg=BG_COPY)

        + "".join(two_up(D.mc(i + 1, len(COPY), q, 'mcbEyebrow',
                       'Activity 2 &middot; Copy, do not paraphrase',
                       'mcbTitle', 'Which answer scores?',
                       folder=F, bg=BG_LIMIT, ctx=q.get('ctx')))
                  for i, q in enumerate(COPY))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'Predict the word before you look for it',
                  [('t3ah', 'Name the word class first', 't3ab',
                    'Read the summary sentence with the gap in it and decide '
                    'what it needs: a noun, a verb, an adjective, a number. A '
                    'gap after <em>the</em> or <em>a</em> wants a noun; a gap '
                    'after the subject wants a verb; a gap after '
                    '<em>lasted</em> or <em>cost</em> wants an amount.',
                    't3an',
                    'Decide this before you open the passage. Then you are '
                    'looking for one kind of word, not any word.'),
                   ('t3bh', 'The answer must read as English', 't3bb',
                    'Put your word in the gap and read the whole sentence. '
                    'Singular or plural, past or present: the summary '
                    'sentence decides, and the passage word usually already '
                    'fits, because the summary was written from it.', 't3bn',
                    'If the sentence does not read, you have the wrong form '
                    'or the wrong place.'),
                   ('t3ch', 'Spelling counts', 't3cb',
                    'Even in a copied word. Transfer it letter by letter and '
                    'check it against the passage. A word '
                    'you knew, copied wrongly, scores exactly what a word you '
                    'did not know would have.', 't3cn',
                    'Reading has no transfer time. Write on the answer sheet '
                    'as you go.')],
                  folder=F, bg=BG_FIT)

        + "".join(two_up(D.mc(i + 1, len(SHAPE), q, 'mccEyebrow',
                       'Activity 3 &middot; The gap has a shape',
                       'mccTitle', 'Which form fits the sentence?',
                       folder=F, bg=BG_FIT, ctx=q.get('ctx')))
                  for i, q in enumerate(SHAPE))

        + _keyed_sort(
            D.sort_slide(SORT_BINS, SORT_ITEMS,
                         'sortEyebrow', 'Activity 4 &middot; What the marker does',
                         'sortTitle', 'Sort the six answers',
                         'sortHint', 'Drag each one into a column &mdash; or '
                                     'click an item, then the column you want '
                                     'it in.',
                         'sortWhy', folder=F, bg=BG_FIT,
                         bin_keys=['sortBin1', 'sortBin2']))

        + D.results('resNext', 'You can fill them. Now set them &rarr;', folder=F)

        + D.activate('Set the gaps yourself', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs, with a short article each. Write a three-gap '
                     'summary of yours &mdash; four sentences, a word limit '
                     'above them &mdash; and swap. Your partner fills the gaps '
                     'from the article only; you mark as the examiner would: '
                     'passage word, within the limit, spelt as printed, or '
                     'nothing.',
                     ['Before filling any gap, say out loud what word class it '
                      'needs and which words in the sentence tell you so.',
                      'For every answer, point at the words in the article. An '
                      'answer you cannot point at is not accepted.',
                      'Find one gap in your partner&rsquo;s summary that two '
                      'passage words could fill, and rewrite the sentence so '
                      'only one can.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Take a passage you read this week and write a '
                     'four-sentence summary of it with three gaps, the word '
                     'limit stated above it. Then write the key: the exact '
                     'passage words for each gap, and one tempting wrong '
                     'answer with why it scores nothing.',
                     'NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting '
                     'wrong answer: …',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltscomp as I
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
