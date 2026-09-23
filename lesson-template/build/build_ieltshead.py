# -*- coding: utf-8 -*-
"""IELTS Reading: Matching Headings (C1), built as a 16:9 deck.

The second Reading lesson on the route, after True / False / Not Given. The
hub card on `ielts-reading.html` set the brief: "The type that does not run
in passage order, so the technique is different: read for what the paragraph
is doing rather than what it is about, and leave the headings that fit two
paragraphs until last." The deck is those three clauses in order:

  1. THE SHAPE OF THE TASK — more headings than paragraphs, the one type
     that jumps, and the trap of reading the list before the paragraph.
  2. FUNCTION OVER TOPIC — a heading names what the paragraph is DOING; the
     topic sentence moves around; a repeated word is bait.
  3. ORDER OF ATTACK — sure ones first, cross it out once used, a heading
     that fits two paragraphs goes last and is decided by elimination.

Twelve items in three activities, four options each — every option a
heading, so they are all short and the length gate had to be satisfied by
lengthening distractors word by word. A sort of six SIGNALS closes the
scored part: three marks of the heading that fits the whole paragraph
against the three ways a decoy looks right.

Six pictures, one per idea. A long row of numbered mailboxes under an empty
sky is the list of headings waiting for paragraphs; an empty frame on a wall
with the picture leaning below it is function against topic — the frame is
what the paragraph does, the picture is what it is about; a box of index
cards knocked over is the passage with no order to lean on; a jigsaw with
one gap and two nearly identical pieces is the heading that fits twice; and
a single coat on a long row of hooks closes it on the activation stage.

English, German and Spanish all complete.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltshead_data import (MAIN, FUNCTION, ATTACK, ALL,
                            SORT_BINS, SORT_ITEMS, SORT_WHY)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-reading-headings.html'
F = 'ielts-reading-headings'

# python3 lesson-template/extract-palette.py ielts-reading-headings/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090e09;
  --surface       : #121c12;
  --surface2      : #1a281a;
  --border        : #d4a77f;
  --text          : #f5f3f2;
  --text-dim      : #bfb0a3;
  --accent        : #f8dbc1;
  --accent-bright : #d2c6c6;
  --accent-dim    : #ebab73;
  --secondary     : #9db6b3;
  --contrast      : #1dedeb;''' % F

# The target language of this deck is a set of moves, not a set of phrases —
# which is why the chips read as instructions. English in every gloss: they are
# what the learner says to themselves in the exam room.
CHIPS = ['function, not topic', 'a detail is not a heading', 'sure ones first',
         'two-fit goes last', 'cross it out', 'too general fails']

BG_SHAPE, BG_FUNCTION, BG_ORDER, BG_TWOFIT = ('bg02.jpg', 'bg03.jpg',
                                              'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSHEAD')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Matching <em>Headings</em>',
                'A Reading task that does not run in passage order '
                '&mdash; so the technique is different',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Reading &middot; both modules'),
                 ('Count', '18 points')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'More headings than paragraphs, and no order to '
                             'lean on',
                  [('t1ah', 'The shape of the task', 't1ab',
                    'A list of headings numbered i, ii, iii, and a passage '
                    'with paragraphs lettered A to G. Each paragraph takes '
                    'one heading. There are always more headings than '
                    'paragraphs, so two or three are never used &mdash; and '
                    'they are written to be tempting.', 't1an',
                    'Seven paragraphs, ten headings, three decoys. That is '
                    'the usual arithmetic.'),
                   ('t1bh', 'A type that jumps', 't1bb',
                    'Most question types follow the passage. This one, like '
                    'Matching Information, does not: heading i can belong to '
                    'paragraph F, and the order of the list tells you nothing '
                    'about where to look. Answering four tells you nothing '
                    'about the fifth.', 't1bn',
                    'It usually comes first on its passage, before the '
                    'questions that do run in order.'),
                   ('t1ch', 'Read the paragraph before the list', 't1cb',
                    'The trap is to read ten headings first and then hunt '
                    'for them in the text &mdash; ten ideas in your head, all '
                    'looking for a home. Read paragraph A, say in your own '
                    'words what it is about, and only then look at the list '
                    'for the heading that says the same.', 't1cn',
                    'Your own summary first, the list second. Every time.')],
                  folder=F, bg=BG_SHAPE)

        + "".join(D.mc(i + 1, len(MAIN), q, 'mcaEyebrow',
                       'Activity 1 &middot; The main idea', 'mcaTitle',
                       'Read the paragraph. Which heading covers all of it?',
                       folder=F, bg=BG_SHAPE, ctx=q.get('ctx'))
                  for i, q in enumerate(MAIN))

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'Ask what the paragraph is doing, not what it '
                             'is about',
                  [('t2ah', 'Function over topic', 't2ab',
                    'Two paragraphs can share a topic and do different jobs '
                    'with it: one introduces a problem, the next gives an '
                    'example, a third weighs two views, a fourth proposes a '
                    'fix. The heading names the job. A heading that only '
                    'names the topic fits half the passage.', 't2an',
                    'Introducing, illustrating, comparing, warning, '
                    'proposing. Five verbs cover most of what a paragraph '
                    'does.'),
                   ('t2bh', 'The topic sentence moves around', 't2bb',
                    'It is usually first, and the people who write these '
                    'tests know you know that. A paragraph can open with an '
                    'example and state its point at the end, or bury it in '
                    'the middle after a concession. Read to the last '
                    'sentence before you decide.', 't2bn',
                    'A heading that matches only the first sentence is the '
                    'commonest wrong answer on the paper.'),
                   ('t2ch', 'A repeated word is bait', 't2cb',
                    'If a heading uses a word that sits in the paragraph, be '
                    'suspicious. The right heading paraphrases: it says what '
                    'the paragraph means in words the paragraph did not '
                    'use. The wrong ones are built from its vocabulary, so '
                    'that a candidate scanning for words finds them.', 't2cn',
                    'Matching a word takes a second. Matching an idea takes '
                    'a sentence. Spend the sentence.')],
                  folder=F, bg=BG_FUNCTION)

        + "".join(D.mc(i + 1, len(FUNCTION), q, 'mcbEyebrow',
                       'Activity 2 &middot; What is it doing?', 'mcbTitle',
                       'Name the job, not the subject',
                       folder=F, bg=BG_FUNCTION, ctx=q.get('ctx'))
                  for i, q in enumerate(FUNCTION))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'Sure ones first, cross it out, two-fit goes '
                             'last',
                  [('t3ah', 'Do the certain ones first', 't3ab',
                    'Some paragraphs have one obvious heading. Take them, '
                    'whatever letter they carry. Every certain match '
                    'shortens the list for the ones you are not sure of, and '
                    'the hardest paragraph is often decided by what is left '
                    'rather than by what it says.', 't3an',
                    'Do not work A to G. Work easy to hard.'),
                   ('t3bh', 'Cross it out once used', 't3bb',
                    'Each heading is used once. Strike it off the list the '
                    'moment you commit to it, and strike off the paragraph '
                    'too. A list that still shows ten headings with two '
                    'paragraphs to go is asking you to reconsider every '
                    'decision you have already made.', 't3bn',
                    'Pencil, not memory. Under time you will forget which '
                    'you have used.'),
                   ('t3ch', 'When a heading fits two paragraphs', 't3cb',
                    'Leave it. Do the rest, and come back with the list '
                    'shorter. Then ask of each paragraph: does this heading '
                    'cover the whole of it, or just one sentence? One of the '
                    'two has a better heading elsewhere, and elimination '
                    'decides what reading could not.', 't3cn',
                    'Too general and too specific both fail. The right '
                    'heading fits the paragraph and fits nothing else.')],
                  folder=F, bg=BG_ORDER)

        + "".join(D.mc(i + 1, len(ATTACK), q, 'mccEyebrow',
                       'Activity 3 &middot; Order of attack', 'mccTitle',
                       'Which move, and which heading?',
                       folder=F, bg=BG_TWOFIT, ctx=q.get('ctx'))
                  for i, q in enumerate(ATTACK))

        # The explanation goes through its i18n key so it translates with
        # the rest of the slide; SORT_WHY in the data module is the English
        # of that key, kept there so the data file reads whole.
        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', 'Activity 4 &middot; Right heading, or '
                                      'trap?',
                       'sortTitle', 'Sort the six signals',
                       'sortHint', 'Drag each one into a column &mdash; or '
                                   'click an item, then the column you want '
                                   'it in.',
                       'sortWhy', folder=F, bg=BG_TWOFIT,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can match them. Now write them &rarr;',
                    folder=F)

        + D.activate('Write the headings yourself', 'Use at least three:',
                     CHIPS, 'Discussion &middot; in pairs',
                     'In pairs, with any article to hand. One of you writes '
                     'a heading for each paragraph, then adds two extra '
                     'headings that fit nothing &mdash; one that repeats a '
                     'word from the text, one that is too general. Shuffle '
                     'the list, swap, and match. Then argue every match.',
                     ['Whoever matches must say what each paragraph is doing '
                      '&mdash; introducing, comparing, warning &mdash; before '
                      'naming its heading.',
                      'For each decoy, say which paragraph it was written to '
                      'tempt you towards, and what gives it away.',
                      'Find one heading in your partner&rsquo;s set that fits '
                      'two paragraphs, and rewrite it so that it fits only '
                      'one.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Take a passage of three paragraphs and write a heading '
                     'for each. Under every heading, quote the one sentence '
                     'that proves it is the main idea, and say in a line why '
                     'the heading covers the whole paragraph rather than '
                     'that sentence alone.',
                     'Paragraph A — heading: … The sentence that proves it: …',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltshead as I
    assert I.T['en']['sortWhy'] == SORT_WHY, 'sortWhy drifted from SORT_WHY'
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Reading: Matching Headings (C1) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    # Twelve items plus the six signals on the sorting slide: the engine scores
    # a sort per chip, so the cover chip has to say 18, not 13.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
