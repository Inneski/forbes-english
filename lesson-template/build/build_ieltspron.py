# -*- coding: utf-8 -*-
"""IELTS Pronunciation & fluency (C1), built as a 16:9 deck.

The third step on `ielts-speaking.html`, and the second of the two cards that
route had been showing as disabled with nothing behind them. Its own copy made
the argument for the lesson: "A quarter of the marks sits on pronunciation and
most candidates never practise it deliberately."

The deck is built around the misconception that makes that practice not happen.
Candidates hear "pronunciation" and think "accent", decide the accent is not
going to change in the weeks before the test, and skip the criterion. But the
public descriptors score intelligibility, control of the features that carry
meaning, and the effort the listener has to make. An accent costs nothing. Flat
stress, a break in the middle of a noun phrase and a filler inside a phrase all
cost something, and all three are fixable in an afternoon.

Three sections — stress, thought groups, pausing and repair — then a sorting
task that puts the whole misconception on one slide: six habits, two columns,
"costs you marks" against "costs you nothing". The accent goes in the free
column. That slide is the lesson.

Six pictures, one per section: a microphone in an empty room for the cover,
pendant lamps at unequal heights for stress, a shelf of clustered objects for
thought groups, an empty chair and a glass set down for the pause, a tiled wall
for the drills, and two chairs with a stopwatch for the activation stage.

English, German and Spanish all complete.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltspron_data import (STRESS, CHUNK, PAUSE, ALL,
                            SORT_BINS, SORT_ITEMS, SORT_WHY)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-pronunciation.html'
F = 'ielts-pronunciation'

# python3 lesson-template/extract-palette.py ielts-pronunciation/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0f1517;
  --surface       : #182125;
  --surface2      : #202c31;
  --border        : #b2aba0;
  --text          : #f5f4f2;
  --text-dim      : #bfb4a3;
  --accent        : #eadfce;
  --accent-bright : #d2c6c6;
  --accent-dim    : #cab492;
  --secondary     : #364851;
  --contrast      : #35c0d4;''' % F

# The chips are the moves, not phrases: this is the one deck on the route whose
# target language is a way of saying things rather than a set of expressions.
CHIPS = ['thought groups', 'content-word stress', 'pause at the joins',
         'no filler inside a phrase', 'paraphrase, do not stop',
         'RECord / reCORD']

BG_STRESS, BG_CHUNK, BG_PAUSE, BG_SORT = ('bg02.jpg', 'bg03.jpg',
                                          'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSPRON')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Pronunciation <em>&amp; Fluency</em>',
                'A quarter of the marks, and the quarter nobody practises: '
                'stress, chunking, and the pause that reads as thinking',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Speaking &middot; all three parts'),
                 ('Count', '18 points')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'It is not an accent test. It never was.',
                  [('t1ah', 'What is actually scored', 't1ab',
                    'The descriptors ask how easily you can be understood, '
                    'whether you control the features that carry meaning, and '
                    'how much effort the listener has to make. Sounding '
                    'British is on none of those lists.', 't1an',
                    'Candidates lose marks here for flat stress far more often '
                    'than for an accent.'),
                   ('t1bh', 'Stress marks the meaning', 't1bb',
                    'English puts the beat on the words that carry the point '
                    'and lets the rest run light. Flatten that and every word '
                    'arrives with equal weight, so the listener has to work '
                    'out the point unaided.', 't1bn',
                    'Two syllables, two words: <em>RECord</em> is the noun, '
                    '<em>reCORD</em> is the verb.'),
                   ('t1ch', 'Six sentences, six words', 't1cb',
                    '&ldquo;I didn&rsquo;t say she stole the money&rdquo; '
                    'means six different things depending on which word takes '
                    'the beat. The words never change; only the stress does.',
                    't1cn',
                    'Try it aloud on each of the six. Every version denies '
                    'something different.')],
                  folder=F, bg=BG_STRESS)

        + "".join(D.mc(i + 1, len(STRESS), q, 'mcaEyebrow',
                       'Activity 1 &middot; Where the beat falls', 'mcaTitle',
                       'Stress, and what moves when it moves',
                       folder=F, bg=BG_STRESS, ctx=q.get('ctx'))
                  for i, q in enumerate(STRESS))

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'Speech arrives in groups, not in words',
                  [('t2ah', 'The thought group', 't2ab',
                    'Fluent English comes in short runs of words said as one '
                    'unit, with a small break between them. The break is not a '
                    'hesitation &mdash; it is the punctuation of spoken '
                    'language.', 't2an',
                    'Roughly three to seven words is the natural size of a '
                    'group.'),
                   ('t2bh', 'The boundary carries meaning', 't2bb',
                    'Move the break and you move the sense. The group boundary '
                    'is doing the same job a comma does on the page, and '
                    'putting it in the wrong place misleads the listener in '
                    'the same way.', 't2bn',
                    'Read a written sentence aloud and the commas usually show '
                    'you where the groups end.'),
                   ('t2ch', 'Inside a group, keep going', 't2cb',
                    'A break inside a group is the one that reads as trouble: '
                    'pausing in the middle of a noun phrase tells the examiner '
                    'you have lost the word, not that you are weighing an '
                    'idea.', 't2cn',
                    'Pause at the joins, not inside the pieces.')],
                  folder=F, bg=BG_CHUNK)

        + "".join(D.mc(i + 1, len(CHUNK), q, 'mcbEyebrow',
                       'Activity 2 &middot; Thought groups', 'mcbTitle',
                       'Where speech breaks, and why it matters',
                       folder=F, bg=BG_CHUNK, ctx=q.get('ctx'))
                  for i, q in enumerate(CHUNK))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'The pause, and what you put in it',
                  [('t3ah', 'Silence is allowed', 't3ab',
                    'A short silence at the end of a group reads as thinking. '
                    'The same length of silence in the middle of a phrase '
                    'reads as a search for a word. The pause is not the '
                    'problem &mdash; its position is.', 't3an',
                    'Two seconds at a join is unremarkable. Two seconds inside '
                    'a phrase is audible.'),
                   ('t3bh', 'Fillers are worse than silence', 't3bb',
                    '<em>Errrm</em> and a repeated first word draw attention '
                    'to the trouble. A clean break does not. If you need a '
                    'moment, take it quietly &mdash; or say that you are '
                    'taking it.', 't3bn',
                    '<em>That is a good question, actually</em> buys the same '
                    'time and costs nothing.'),
                   ('t3ch', 'Talk around the word you lost', 't3cb',
                    'If the word will not come, describe what the thing does '
                    'and keep the turn. Paraphrase is scored under Lexical '
                    'Resource; stopping dead is scored under Fluency, and not '
                    'kindly.', 't3cn',
                    'Never stop to ask the examiner for a word. They will not '
                    'give you one.')],
                  folder=F, bg=BG_PAUSE)

        + "".join(D.mc(i + 1, len(PAUSE), q, 'mccEyebrow',
                       'Activity 3 &middot; Pausing and repair', 'mccTitle',
                       'Thinking, or stalling?', folder=F, bg=BG_PAUSE,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(PAUSE))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow',
                       'Activity 4 &middot; What the criterion actually scores',
                       'sortTitle', 'Sort the six habits',
                       'sortHint', 'Drag each one into a column &mdash; or '
                                   'click an item, then the column you want '
                                   'it in.',
                       SORT_WHY, folder=F, bg=BG_SORT,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can hear it. Now say it &rarr;', folder=F)

        + D.activate('Say it, and be followed', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs, with the long-turn card from Part 2. Read your '
                     'partner a four-line answer, deliberately flat, then read '
                     'it again in thought groups with the beat on the content '
                     'words. Your partner says what changed.',
                     ['Say &ldquo;I didn&rsquo;t say she stole the '
                      'money&rdquo; six times, one beat each. Your partner '
                      'names what you denied.',
                      'Take a Part 3 question and answer it in groups of three '
                      'to seven words, pausing only at the joins.',
                      'Have your partner interrupt with a word you do not '
                      'know. Talk around it and keep the turn &mdash; no '
                      'stopping, no asking.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write out a two-minute answer, then mark it up: a slash '
                     'at every group boundary and capitals on the word that '
                     'takes the beat in each group. Read it back and check the '
                     'beats land where the meaning is.',
                     'The place I would recommend / is a small town…',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltspron as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Pronunciation & Fluency (C1) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    # The engine scores each sort chip separately, so the deck is out of
    # 18: twelve items plus the six habits on the sorting slide. The cover
    # chip has to match what the results slide prints, or the learner
    # arrives at a score out of a number the cover never mentioned.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
