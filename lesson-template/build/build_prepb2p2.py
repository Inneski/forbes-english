# -*- coding: utf-8 -*-
"""Advanced Prepositions (B2) — Part 2 — rebuilt as a 16:9 deck.

`b2_prepositions_advanced_lesson_part2.html` was the third of the three
scrolling preposition quizzes, and the worst offender of the set: no teaching
content, no hero, and the correct answer written first in **all 28 items**
without a single exception. See `prepb2p2_data.py` for what was done about
that and why it was not merely cosmetic.

All 28 scored items survive unchanged in substance and in count.

- **Four teaching slides now exist. None did.** One per section: the
  rise/increase/fall prepositions that carry statistics, the second set of
  fixed phrases, the second set of dependent pairs, and the phrasal verbs for
  handling, recovering and delaying.
- **The Spanish was unaccented and is now correct** — the old `es:` notes read
  "disminucion", "comparacion", "situacion dificil", "perdida". Every one is a
  real word in Spanish with the accent on.
- **German is new.**

Part 1 and this share `PrepositionsB2/hero.jpg` and therefore share a derived
palette: Innes asked for one world across the pair. They remain two lessons at
two URLs, because that is what students have bookmarked.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from prepb2p2_data import TRENDS, IDIOM, DEPENDENT, PHRASAL, ALL

TPL = 'lesson-template/lesson-template.html'
OUT = 'b2_prepositions_advanced_lesson_part2.html'
F = 'PrepositionsB2'

# python3 lesson-template/extract-palette.py PrepositionsB2/hero.jpg --light
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #d8c3ac;
  --surface       : #e1d3c4;
  --surface2      : #dccbb8;
  --border        : #966f4a;
  --text          : #2a1d11;
  --text-dim      : #5e452e;
  --accent        : #8e4c0d;
  --accent-bright : #653304;
  --accent-dim    : #db883b;
  --secondary     : #162630;
  --contrast      : #165f60;''' % F

CHIPS = ['a rise in', 'an increase of', 'fall by', 'compared to',
         'with regard to', 'in charge of', 'under control', 'deal with',
         'fall behind']

# The same three backdrops Part 1 uses, in reverse order: the pair shares a
# world on Innes's instruction, but a learner doing both back to back should
# not feel they are repeating a deck. Part 4 falls back to the hero.
BG_TRENDS, BG_IDIOM, BG_DEP = 'bg04.jpg', 'bg03.jpg', 'bg02.jpg'


def build():
    D.assert_no_key_is_longest(ALL, 'PrepB2P2')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Advanced Prepositions <em>Part 2</em>',
                'The prepositions that carry figures, formal phrases and '
                'everyday phrasal verbs',
                [('Level', 'B2 &middot; Upper-intermediate'),
                 ('Focus', 'Prepositions'),
                 ('Count', '28 questions')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'Talking about figures: three words, three jobs',
                  [('t1ah', 'In, of, by', 't1ab',
                    'A rise <em>in</em> demand names <em>what</em> is '
                    'growing. An increase <em>of</em> eight percent gives '
                    'the <em>size</em>. Costs dropping <em>by</em> a fifth '
                    'gives the size of the <em>change</em>.', 't1an',
                    'All three can appear in one sentence, each doing a '
                    'different job.'),
                   ('t1bh', 'From here to there', 't1bb',
                    '<strong>From X to Y</strong> marks the two ends of a '
                    'change &mdash; membership rose <em>from</em> 500 '
                    '<em>to</em> over 800. The starting point comes first.',
                    't1bn',
                    'Use it when both numbers matter; use <em>by</em> when '
                    'only the gap between them does.'),
                   ('t1ch', 'Comparing and qualifying', 't1cb',
                    '<em>Compared to</em> sets two things side by side. '
                    '<em>A shortage of</em> names what is missing. <em>With '
                    'regard to</em> narrows to one aspect.', 't1cn',
                    '<em>With regard to</em> is formal and singular &mdash; '
                    'never <em>with regards to</em>, which is a sign-off.')],
                  folder=F, bg=BG_TRENDS)

        + "".join(D.mc(i + 1, len(TRENDS), q, 'mcaEyebrow',
                       'Activity 1 &middot; Trends and quantity', 'mcaTitle',
                       'Which preposition carries the figure?', folder=F, bg=BG_TRENDS)
                  for i, q in enumerate(TRENDS))

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'More fixed phrases, and the trap inside them',
                  [('t2ah', 'The <em>in</em> family', 't2ab',
                    '<em>In charge of</em>, <em>in favour of</em>, <em>in '
                    'return for</em>, <em>in addition to</em>. Four phrases '
                    'that all open with <em>in</em> &mdash; which is why '
                    'the first half is rarely the difficult part.', 't2an',
                    'If the phrase describes a role or a position, the odds '
                    'favour <em>in</em>.'),
                   ('t2bh', 'States, not places', 't2bb',
                    '<em>Out of the question</em>, <em>under control</em>, '
                    '<em>beyond doubt</em>. Each describes a condition '
                    'something is in, and none of them is literal.', 't2bn',
                    '<em>Beyond</em> means past the point where it could be '
                    'argued &mdash; the same <em>beyond</em> as in '
                    '<em>beyond repair</em>.'),
                   ('t2ch', 'The tail is not always <em>of</em>', 't2cb',
                    'In charge <em>of</em>, in favour <em>of</em>, but in '
                    'return <em>for</em> and in addition <em>to</em>. '
                    'Learning the opening preposition is only half the '
                    'phrase.', 't2cn',
                    'This is why they are memorised whole rather than by '
                    'rule.')],
                  folder=F, bg=BG_IDIOM)

        + "".join(D.mc(i + 1, len(IDIOM), q, 'mcbEyebrow',
                       'Activity 2 &middot; Fixed phrases', 'mcbTitle',
                       'Complete the expression', folder=F, bg=BG_IDIOM)
                  for i, q in enumerate(IDIOM))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'More dependent pairs, including one real trap',
                  [('t3ah', 'When <em>to</em> is not an infinitive', 't3ab',
                    'You <em>object to</em> something, and that <em>to</em> '
                    'is a preposition &mdash; so a verb after it takes '
                    '<em>-ing</em>. Residents objected <em>to</em> the road '
                    '<em>being built</em>, never <em>to be built</em>.',
                    't3an',
                    'The same trap sits inside <em>look forward to</em> and '
                    '<em>be used to</em>.'),
                   ('t3bh', 'Trusting and mentioning', 't3bb',
                    '<em>Rely on</em> someone to do something. <em>Refer '
                    'to</em> something in a speech or a text. Both fixed, '
                    'neither negotiable.', 't3bn',
                    '<em>Refer to</em> also means "look something up", with '
                    'the same preposition.'),
                   ('t3ch', 'Leaving, gaining, boasting', 't3cb',
                    'You <em>resign from</em> a post and <em>benefit '
                    'from</em> a scheme &mdash; both take <em>from</em>. You '
                    '<em>boast about</em> something, and <em>excuse</em> '
                    'someone <em>for</em> it.', 't3cn',
                    'Two verbs sharing a preposition is the exception here, '
                    'not the rule.')],
                  folder=F, bg=BG_DEP)

        + "".join(D.mc(i + 1, len(DEPENDENT), q, 'mccEyebrow',
                       'Activity 3 &middot; Dependent pairs', 'mccTitle',
                       'Which preposition does the word take?', folder=F, bg=BG_DEP)
                  for i, q in enumerate(DEPENDENT))

        + D.teach('t4Eyebrow', 'Before you start',
                  't4Title', 'Handling, recovering, delaying, bumping into',
                  [('t4ah', 'Both take <em>with</em>', 't4ab',
                    'You <em>deal with</em> a problem and you <em>cope '
                    'with</em> pressure. <em>Deal with</em> is about solving '
                    'it; <em>cope with</em> is about surviving it.', 't4an',
                    'A manager deals with a conflict. The team copes with '
                    'the workload.'),
                   ('t4bh', 'Getting past it, or putting it off', 't4bb',
                    '<em>Get over</em> something is to recover from it '
                    'emotionally. <em>Put off</em> something is to postpone '
                    'it &mdash; and it is the decision, not the person, that '
                    'gets put off.', 't4bn',
                    '<em>Put someone off</em> exists too, and means to '
                    'discourage them. Different verb.'),
                   ('t4ch', 'By chance, or behind', 't4cb',
                    '<em>Come across</em> a thing and <em>run into</em> a '
                    'person &mdash; both mean by chance, but one is for '
                    'objects and one is for people. <em>Fall behind</em> is '
                    'to slip back against a plan.', 't4cn',
                    'You come across a photo; you run into an old teacher.')],
                  folder=F)

        + "".join(D.mc(i + 1, len(PHRASAL), q, 'mcdEyebrow',
                       'Activity 4 &middot; Phrasal verbs', 'mcdTitle',
                       'Finish the phrasal verb', folder=F)
                  for i, q in enumerate(PHRASAL))

        + D.results('resNext', 'You can spot it. Now use it &rarr;', folder=F)

        + D.activate('Present the figures', 'Use at least three:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you presents this quarter&rsquo;s results to the '
                     'board; the other is a board member who does not accept '
                     'them. Four minutes each, then swap.',
                     ['Describe one number that went up and one that went '
                      'down, using <em>a rise in</em>, <em>an increase '
                      'of</em> and <em>fall by</em> correctly.',
                      'Say how this quarter looks <em>compared to</em> the '
                      'last, and what you are still <em>in charge of</em> '
                      'fixing.',
                      'Push back: ask what is being done about the one '
                      'figure that is not yet <em>under control</em>.'],
                     'Writing &middot; 180&ndash;250 words',
                     'Write the paragraph that opens the quarterly report: '
                     'what rose, what fell, by how much, and what you are '
                     'doing about the one figure that is behind. Use at '
                     'least three of the expressions above.',
                     'In the three months to September…',
                     folder=F)
    )

    import i18n_prepb2p2 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Advanced Prepositions (B2) — Part 2 | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d questions, %d bytes'
          % (OUT, s.count('<section class="slide'), len(ALL), len(s)))


if __name__ == '__main__':
    build()
