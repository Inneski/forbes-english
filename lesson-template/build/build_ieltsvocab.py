# -*- coding: utf-8 -*-
"""IELTS Vocabulary: Lexical Resource (C1), built as a 16:9 deck.

The last disabled card on `ielts.html`, and its own copy set the brief: "Topic
banks that feed Speaking and Task 2 at once, since Lexical Resource is a
quarter of the marks in both. Words you have to use, not words you have to
read."

So the deck is built against the belief that costs candidates the most here —
that this criterion rewards rare words. It does not. The public descriptors ask
for less common lexis used with PRECISION and FLEXIBILITY, and they penalise
inaccuracy by name, which means a reach-and-miss scores below a plain word that
lands. What actually moves the band is three things, and they are the three
sections:

  1. **precision** — the near-miss costs more than the plain word, and a
     memorised "band 9 phrase" is audible because it sits apart from the
     English around it;
  2. **collocation** — the unit that gets scored is the pairing. You *conduct*
     research and *reach* a decision; there is *heavy traffic* and *heavy
     fighting* but never *heavy sunshine*, and no rule predicts it, which is
     why a notebook entry has to be a phrase and not a word;
  3. **paraphrase** — the one skill Speaking Part 3 and Task 2 both pay for,
     and the reason a topic bank is built by idea rather than alphabetically:
     a word filed under an idea arrives with an argument attached.

The sorting slide is the lesson in one screen. Six habits, two columns, and
the impressive-feeling ones — memorising phrase lists, reaching for a thesaurus
word, echoing the question — are all in the column that pays nothing.

Six pictures, one per section: a card-index cabinet for the cover, gauge blocks
for precision, interlocking blocks for collocation, two differently shaped
vessels holding the same volume for paraphrase, a wall of labelled drawers for
the bank, and a desk with an open notebook to close.

English, German and Spanish all complete.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltsvocab_data import (PRECISION, COLLOCATION, PARAPHRASE, ALL,
                             SORT_BINS, SORT_ITEMS, SORT_WHY)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-lexical-resource.html'
F = 'ielts-vocabulary'

# python3 lesson-template/extract-palette.py ielts-vocabulary/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #10110f;
  --surface       : #1c1e19;
  --surface2      : #262922;
  --border        : #a18a7e;
  --text          : #f5f3f2;
  --text-dim      : #bfaca3;
  --accent        : #deb9a7;
  --accent-bright : #eac3b0;
  --accent-dim    : #c0866a;
  --secondary     : #a4bab6;
  --contrast      : #2edbc0;

  /* This deck's backgrounds are the brightest and busiest on the IELTS route —
     a wall of pale drawers behind the sorting slide. At the house default of
     0.68 the order hint measured 4.33:1 against the lightest patch under it,
     which is below AA. Raised per deck, exactly as the template's note says to
     do, and re-measured in the page rather than by eye. */
  --plate: 0.82;''' % F

# Collocations, not single words — which is the deck's own argument. English in
# every gloss: the pairing is the thing being learnt.
CHIPS = ['conduct research', 'reach a decision', 'draw a conclusion',
         'heavy traffic', 'tackle congestion', 'ease the pressure']

BG_PRECISION, BG_COLLOC, BG_PARA, BG_BANK = ('bg02.jpg', 'bg03.jpg',
                                             'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSVOCAB')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Lexical <em>Resource</em>',
                'A quarter of the marks in Speaking and in Task 2, and it is '
                'not the quarter that rewards rare words',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Speaking &amp; Writing Task 2'),
                 ('Count', '18 points')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'It does not reward rare words. It never has.',
                  [('t1ah', 'What the descriptors ask for', 't1ab',
                    '<em>Less common</em> vocabulary, used with '
                    '<strong>precision</strong> and <strong>flexibility</strong>. '
                    'Two of those three words are about accuracy, and '
                    'inaccuracy is penalised by name.', 't1an',
                    'Rarity with a miss scores below plainness with a hit. '
                    'Every time.'),
                   ('t1bh', 'The near-miss costs more than the plain word',
                    't1bb',
                    'A candidate who writes <em>ameliorate the traffic</em> '
                    'has reached for a rare verb and attached it to the wrong '
                    'object. The examiner sees the reach and the miss. '
                    '<em>Ease the traffic</em> is plain, right, and scores '
                    'higher.', 't1bn',
                    'Reach for the word you are sure of, then stretch once you '
                    'are certain of the fit.'),
                   ('t1ch', 'Memorised phrases are audible', 't1cb',
                    'Band 9 phrase lists sit apart from the answer around '
                    'them, and examiners are trained to hear exactly that. A '
                    'learnt phrase in a plain answer marks the plain answer as '
                    'the real one.', 't1cn',
                    'It is the mismatch that gives it away, not the phrase '
                    'itself.')],
                  folder=F, bg=BG_PRECISION)

        + "".join(D.mc(i + 1, len(PRECISION), q, 'mcaEyebrow',
                       'Activity 1 &middot; Precision, not rarity', 'mcaTitle',
                       'What is actually being marked?',
                       folder=F, bg=BG_PRECISION, ctx=q.get('ctx'))
                  for i, q in enumerate(PRECISION))

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'The unit is the pairing, not the word',
                  [('t2ah', 'The noun chooses the verb', 't2ab',
                    'You <em>conduct</em> research, <em>reach</em> a decision '
                    'and <em>draw</em> a conclusion. None of those verbs is '
                    'rare; all three are fixed, and none of them is the one a '
                    'dictionary gives you for the noun.', 't2an',
                    '<em>Make research</em> and <em>do a decision</em> are the '
                    'two this costs most often.'),
                   ('t2bh', 'And the adjective', 't2bb',
                    '<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy '
                    'losses</em>, <em>heavy fighting</em> &mdash; but never '
                    '<em>heavy sunshine</em>. The adjective is chosen by the '
                    'noun, and no rule predicts which.', 't2bn',
                    'Which is why they are learnt whole, in the phrase, rather '
                    'than derived.'),
                   ('t2ch', 'So write the phrase, not the word', 't2cb',
                    'A notebook entry of one word plus a translation gives you '
                    'a word you cannot use. An entry of the phrase it lives in '
                    'gives you something you can say tomorrow.', 't2cn',
                    '<em>Tackle congestion</em> is worth ten times '
                    '<em>congestion = [your language]</em>.')],
                  folder=F, bg=BG_COLLOC)

        + "".join(D.mc(i + 1, len(COLLOCATION), q, 'mcbEyebrow',
                       'Activity 2 &middot; Words that travel together',
                       'mcbTitle', 'Which pairing does English use?',
                       folder=F, bg=BG_COLLOC, ctx=q.get('ctx'))
                  for i, q in enumerate(COLLOCATION))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'Paraphrase is the skill that pays twice',
                  [('t3ah', 'Both papers score it', 't3ab',
                    'Speaking Part 3 and Writing Task 2 carry the same '
                    'criterion. The work you do on saying one idea three ways '
                    'is marked in both rooms, which is the best return on '
                    'revision time in the whole exam.', 't3an',
                    'It is also what Reading tests, from the other side.'),
                   ('t3bh', 'Reword the question, do not copy it', 't3bb',
                    'Words lifted straight from the prompt are not counted as '
                    'your vocabulary. An opening that restates the question in '
                    'your own terms is scored; one that repeats it is not.',
                    't3bn',
                    'Change the grammar, not just the nouns: <em>should '
                    'museums be free</em> becomes <em>whether entry should '
                    'cost anything</em>.'),
                   ('t3ch', 'Build the bank by idea', 't3cb',
                    'A topic bank sorted alphabetically gives you words. '
                    'Sorted by idea &mdash; congestion, ageing, automation '
                    '&mdash; each word arrives with an argument already '
                    'attached, which is what you are short of under time.',
                    't3cn',
                    'Ten ideas with three phrases each beats a hundred words '
                    'with none.')],
                  folder=F, bg=BG_PARA)

        + "".join(D.mc(i + 1, len(PARAPHRASE), q, 'mccEyebrow',
                       'Activity 3 &middot; Saying it another way', 'mccTitle',
                       'Paraphrase, and the bank behind it',
                       folder=F, bg=BG_PARA, ctx=q.get('ctx'))
                  for i, q in enumerate(PARAPHRASE))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow',
                       'Activity 4 &middot; Where the revision time should go',
                       'sortTitle', 'Sort the six habits',
                       'sortHint', 'Drag each one into a column &mdash; or '
                                   'click an item, then the column you want '
                                   'it in.',
                       SORT_WHY, folder=F, bg=BG_BANK,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can spot it. Now build it &rarr;', folder=F)

        + D.activate('Build one page of the bank', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs. Take one topic &mdash; congestion, ageing, '
                     'automation, tourism. Five minutes to build a page '
                     'together: three ideas, and for each idea two phrases '
                     'rather than two words. Then argue the topic for two '
                     'minutes using only what is on your page.',
                     ['Every phrase on the page must be a pairing &mdash; a '
                      'verb with its noun, or an adjective with its noun. No '
                      'bare words.',
                      'Your partner stops you whenever you use a word that is '
                      'not on the page, and you have to say it again using one '
                      'that is.',
                      'Take one idea and say it three ways: plainly, formally, '
                      'and as you would say it to a friend.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Take a Task 2 question and write the opening paragraph '
                     'twice: once repeating the question wording, once '
                     'rewording it properly. Then underline in the second one '
                     'every phrase you would count as your own vocabulary, and '
                     'say how many there are.',
                     'Whether entry to museums should cost anything…',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltsvocab as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Lexical Resource: Vocabulary That Scores (C1) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
