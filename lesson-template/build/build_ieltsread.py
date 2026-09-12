# -*- coding: utf-8 -*-
"""IELTS Reading: True / False / Not Given (C1), built as a 16:9 deck.

The Reading card on `ielts.html` had been disabled since the route was split,
and its own copy chose this lesson: "True/False/Not Given first, because that
is where the most marks are lost — and it is technique, not vocabulary, that
recovers them." So this is technique, and the deck is built on one distinction:

  **FALSE means the passage contradicts the statement. NOT GIVEN means the
  passage is silent.** The test is whether you can put your finger on a line.
  If you are reasoning — "well, it must be" — the answer is Not Given, and
  reasoning feels like understanding, which is exactly why it costs so much.

Four teaching sections, twelve items and a sort:

  1. the shape of the paper, including the trap that Reading has **no**
     transfer time where Listening has ten minutes;
  2. FALSE against NOT GIVEN;
  3. answering from the passage rather than from what you know;
  4. the qualifier that decides it — absolutes, hedges, comparatives.

The sorting slide does not sort verdicts, which would be four more items. It
sorts the SIGNALS: three things that point to FALSE against three that point
to NOT GIVEN, and every one on the right is a way of reaching a verdict
without a line to point at.

Six pictures, one per section. The three stacks of paper are the three
passages; two doorways, one shut and one opening onto flat darkness, are False
and Not Given; a book in a pool of light with everything beyond it unlit is
the passage against the world; a balance almost but not quite level is the
qualifier; and the clock over a bare desk closes it.

English, German and Spanish all complete.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltsread_data import (VERDICT, WORLD, QUALIFY, ALL,
                            SORT_BINS, SORT_ITEMS, SORT_WHY)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-reading-tfng.html'
F = 'ielts-reading'

# python3 lesson-template/extract-palette.py ielts-reading/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0c0c0b;
  --surface       : #191915;
  --surface2      : #24241e;
  --border        : #ac7766;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #e4a794;
  --accent-bright : #efb19d;
  --accent-dim    : #cc6e50;
  --secondary     : #87a1aa;
  --contrast      : #1decba;''' % F

# The target language of this deck is a set of moves, not a set of phrases —
# which is why the chips read as instructions. English in every gloss: they are
# what the learner says to themselves in the exam room.
CHIPS = ['point at the line', 'contradicts = FALSE', 'silent = NOT GIVEN',
         'most &ne; all', 'may excludes nothing', 'paraphrase, not words']

BG_SHAPE, BG_VERDICT, BG_WORLD, BG_QUALIFY = ('bg02.jpg', 'bg03.jpg',
                                              'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSREAD')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'True, False, <em>Not Given</em>',
                'The question type that loses the most marks on the Reading '
                'paper &mdash; and the one that technique, not vocabulary, '
                'gets back',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Reading &middot; both modules'),
                 ('Count', '18 points')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'Sixty minutes, three passages, no time at the end',
                  [('t1ah', 'The shape of the paper', 't1ab',
                    'Three passages, forty questions, sixty minutes. Roughly '
                    'twenty minutes each, and the third is usually the hardest '
                    '&mdash; so a passage that runs long is borrowing from the '
                    'one that needs it most.', 't1an',
                    'Academic and General Training differ in the texts, not in '
                    'the technique. Everything here applies to both.'),
                   ('t1bh', 'No transfer time. None.', 't1bb',
                    'Listening gives you ten minutes at the end to copy your '
                    'answers across. <strong>Reading does not.</strong> Write '
                    'on the answer sheet as you go, because the invigilator '
                    'stops you on the hour with whatever is on it.', 't1bn',
                    'Answers left on the question paper score nothing. It is '
                    'the single cheapest way to lose marks on this paper.'),
                   ('t1ch', 'The questions follow the text', 't1cb',
                    'Most question types run in passage order, this one '
                    'included. Answer four and you know roughly where the '
                    'fifth is &mdash; you never have to search the whole '
                    'passage twice.', 't1cn',
                    'Matching Headings and Matching Information are the '
                    'exceptions. They jump around.')],
                  folder=F, bg=BG_SHAPE)

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'False and Not Given are not the same answer',
                  [('t2ah', 'FALSE: the passage says otherwise', 't2ab',
                    'There is a sentence in the text that '
                    '<strong>contradicts</strong> the statement. You can put '
                    'your finger on it. If someone asked you to prove the '
                    'statement wrong, you would point at that line.', 't2an',
                    'A number that disagrees, a date that does not match, an '
                    '"only" against a "several" &mdash; all contradictions.'),
                   ('t2bh', 'NOT GIVEN: the passage is silent', 't2bb',
                    'The text neither says it nor denies it. The statement may '
                    'well be true out in the world; the passage simply does '
                    'not go there.', 't2bn',
                    'Not Given is not a punishment for missing something. It '
                    'is a real answer, and roughly a third of them are.'),
                   ('t2ch', 'The test is one question', 't2cb',
                    '<strong>Can I point at the sentence?</strong> If yes, the '
                    'answer is True or False depending on what it says. If you '
                    'are reasoning &mdash; &ldquo;well, it must be&rdquo; '
                    '&mdash; the answer is Not Given.', 't2cn',
                    'Reasoning feels like understanding, which is exactly why '
                    'it costs so many marks here.')],
                  folder=F, bg=BG_VERDICT)

        + "".join(D.mc(i + 1, len(VERDICT), q, 'mcaEyebrow',
                       'Activity 1 &middot; False, or Not Given?', 'mcaTitle',
                       'Read the passage. Then read the statement.',
                       folder=F, bg=BG_VERDICT, ctx=q.get('ctx'))
                  for i, q in enumerate(VERDICT))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'Answer from the passage, never from what you know',
                  [('t3ah', 'Your knowledge is the trap', 't3ab',
                    'A statement can be perfectly true in the world and still '
                    'Not Given in the text. The examiner is not asking whether '
                    'it is true. They are asking what this passage says.',
                    't3an',
                    'This is why candidates score worse on topics they know '
                    'well.'),
                   ('t3bh', 'TRUE means the text says it', 't3bb',
                    'Said in different words, almost always. The passage will '
                    'not repeat the statement; it will paraphrase it. Matching '
                    'meaning is the skill &mdash; matching words is a habit to '
                    'break.', 't3bn',
                    '<em>Attendance fell sharply after 1990</em> and <em>far '
                    'fewer people came in the years that followed</em> are '
                    'the same claim with no word in common.'),
                   ('t3ch', 'Word-matching fails both ways', 't3cb',
                    'The same words can sit in a sentence that says the '
                    'opposite, and a sentence with no shared words at all can '
                    'state the claim exactly. Shared vocabulary tells you '
                    'where to look, never what to answer.', 't3cn',
                    'Use the repeated word to find the line. Then read the '
                    'line.')],
                  folder=F, bg=BG_WORLD)

        + "".join(D.mc(i + 1, len(WORLD), q, 'mcbEyebrow',
                       'Activity 2 &middot; The passage, not the world',
                       'mcbTitle', 'What does this text actually say?',
                       folder=F, bg=BG_WORLD, ctx=q.get('ctx'))
                  for i, q in enumerate(WORLD))

        + D.teach('t4Eyebrow', 'Before you start',
                  't4Title', 'One word decides a third of these',
                  [('t4ah', 'Absolutes', 't4ab',
                    '<em>All</em>, <em>every</em>, <em>never</em>, '
                    '<em>only</em>. A passage that says <em>most</em> makes a '
                    'statement saying <em>all</em> FALSE &mdash; the two '
                    'cannot both hold, and that is a contradiction you can '
                    'point at.', 't4an',
                    '<em>Most islanders</em> against <em>every islander</em> '
                    'is a False, not a Not Given.'),
                   ('t4bh', 'Hedges', 't4bb',
                    '<em>May</em>, <em>might</em>, <em>is thought to</em>, '
                    '<em>suggests</em>. A hedged passage does not deny a '
                    'confident statement &mdash; it just never makes it. That '
                    'shape is usually Not Given.', 't4bn',
                    'The difference from an absolute: <em>most</em> excludes '
                    '<em>all</em>, but <em>may</em> excludes nothing.'),
                   ('t4ch', 'Comparatives need both sides', 't4cb',
                    '<em>Wetter than</em>, <em>the largest</em>, <em>more '
                    'common than</em>. Check that the passage actually '
                    'compares the same two things &mdash; a text about one of '
                    'them cannot support a claim about the pair.', 't4cn',
                    'A passage naming one figure and a statement ranking two '
                    'is a Not Given every time.')],
                  folder=F, bg=BG_QUALIFY)

        + "".join(D.mc(i + 1, len(QUALIFY), q, 'mccEyebrow',
                       'Activity 3 &middot; The word that decides it',
                       'mccTitle', 'Most, all, may, never',
                       folder=F, bg=BG_QUALIFY, ctx=q.get('ctx'))
                  for i, q in enumerate(QUALIFY))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', 'Activity 4 &middot; What tips you which way',
                       'sortTitle', 'Sort the six signals',
                       'sortHint', 'Drag each one into a column &mdash; or '
                                   'click an item, then the column you want '
                                   'it in.',
                       SORT_WHY, folder=F, bg=BG_QUALIFY,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can call it. Now prove it &rarr;', folder=F)

        + D.activate('Prove it from the text', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs, with any passage you have to hand &mdash; a '
                     'news article will do. One of you writes four statements '
                     'about it: one true, one false, two not given. Swap, '
                     'answer, and then defend each verdict by reading out the '
                     'line you based it on. No line, no FALSE.',
                     ['Whoever answers must say which sentence decided it, out '
                      'loud, before the verdict is accepted.',
                      'For every NOT GIVEN, say what the passage would have '
                      'had to contain for the answer to be FALSE instead.',
                      'Find one statement in your partner&rsquo;s set that you '
                      'could argue either way, and rewrite it so that it '
                      'cannot be.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Take one passage and write three statements about it '
                     '&mdash; one TRUE, one FALSE, one NOT GIVEN &mdash; then '
                     'write the answer key, naming for each one the exact '
                     'sentence that decides it, or saying plainly that no '
                     'sentence does.',
                     'Statement 1 (TRUE): … The line that decides it: …',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltsread as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Reading: True, False, Not Given (C1) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    # Twelve items plus the six signals on the sorting slide: the engine scores
    # a sort per chip, so the cover chip has to say 18, not 13.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
