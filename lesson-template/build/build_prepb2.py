# -*- coding: utf-8 -*-
"""Advanced Prepositions (B2) — rebuilt as a 16:9 deck.

`b2_prepositions_advanced_lesson.html` was a scrolling four-section quiz. Like
its B1 sibling it carried no teaching content at all — every rule lived only
in the per-answer feedback, so the learner met the rule after getting the item
wrong. It had no hero either, which is why `library.html` greyed it out:
`comingSoon(l)` is `!LESSON_IMAGES[l.file]`.

All 28 items survive in count, and all but one in substance: the
`congratulate` item had `for` on its option list, and "congratulate someone
for something" is attested English, so `for` was swapped for the inert
`with`. See `prepb2_data.py`.

- **Four teaching slides now exist. None did.** One per section: the for/to
  purpose split, the fixed idiomatic phrases, the advanced verb and adjective
  pairs, and the three-part prepositional phrasal verbs.
- **The Spanish was unaccented and is now correct.** The old page carried a
  short `es:` note on every item — "proposito", "espanol", "razon", "exito",
  "solucion" — with the diacritics stripped throughout. The deck's Spanish is
  a full translation of each explanation, accented, and it keeps what the old
  note was actually good at: naming the Spanish structure a learner would map
  onto the English one.
- **German is new.** The page was English with a Spanish footnote.

Artwork is `PrepositionsB2/` — a figure climbing a wide staircase through
layered levels, which is the register this half of the lesson works in. Six
pictures: the hero on the cover and results, one backdrop per activity, and one
for the activation stage. Part 2 has its own folder and shares none of them.
The palette is derived from `PrepositionsB2/hero.jpg` with `--light`; every
contrast row PASSes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from prepb2_data import PURPOSE, IDIOM, DEPENDENT, PHRASAL, ALL

TPL = 'lesson-template/lesson-template.html'
OUT = 'b2_prepositions_advanced_lesson.html'
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

CHIPS = ['in terms of', 'on behalf of', 'in spite of', 'on the verge of',
         'at the expense of', 'for the sake of', 'put up with',
         'come up with', 'stand up for']

# One backdrop per activity — the same staircase at four other moments. Part 2
# runs the business-people set instead and shares no picture with this deck;
# what holds the pair together is the palette, which both derive from a
# staircase hero.
BG_PURPOSE, BG_IDIOM, BG_DEP, BG_PHRASAL = ('bg05.jpg', 'bg02.jpg',
                                            'bg03.jpg', 'bg04.jpg')

# Its own picture for the activation stage — see build_prepb1.py for why the
# densest slide in the deck does not share the cover's. Calmest of the two
# remaining staircases over that footprint: 9.16 edge energy against 10.86.
BG_ACT = 'bg06.jpg'


def build():
    D.assert_no_key_is_longest(ALL, 'PrepB2')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Advanced <em>Prepositions</em>',
                'Purpose, fixed phrases, dependent pairs and the phrasal '
                'verbs that carry them',
                [('Level', 'B2 &middot; Upper-intermediate'),
                 ('Focus', 'Prepositions'),
                 ('Count', '28 questions')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'Purpose: what a thing is for, why a person acts',
                  [('t1ah', 'For + noun or -ing', 't1ab',
                    '<strong>For</strong> names the <em>function</em> of a '
                    'thing. Boots made <em>for walking</em>, an account '
                    '<em>for paying fees</em>, a cream <em>for reducing '
                    'lines</em>.', 't1an',
                    'What follows is a noun or an <em>-ing</em> form, never '
                    'a bare infinitive.'),
                   ('t1bh', 'To + infinitive', 't1bb',
                    '<strong>To</strong> gives the <em>reason</em> a person '
                    'does something. He saved for a year <em>to buy a '
                    'van</em>; she '
                    'she took the early train <em>to avoid the queues</em>.',
                    't1bn',
                    '<em>In order to</em> is the same thing, one register '
                    'up. There is no <em>in order for</em> to match it.'),
                   ('t1ch', 'The test that works', 't1cb',
                    'Read what comes after the gap, not who the subject '
                    'is. <em>For</em> takes a noun or an <em>-ing</em> '
                    'form; <em>to</em> takes a bare infinitive. That test '
                    'never fails.', 't1cn',
                    'What the gap describes is the function of a thing, or '
                    'the goal of an action &mdash; a person can be the '
                    'subject of either.')],
                  folder=F, bg=BG_PURPOSE)

        + "".join(D.mc(i + 1, len(PURPOSE), q, 'mcaEyebrow',
                       'Activity 1 &middot; Purpose', 'mcaTitle',
                       'For, or to?', folder=F, bg=BG_PURPOSE)
                  for i, q in enumerate(PURPOSE))

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'Fixed phrases: the preposition is not a slot',
                  [('t2ah', 'The whole phrase is the word', 't2ab',
                    '<em>In terms of</em>, <em>on behalf of</em>, <em>in '
                    'spite of</em> &mdash; these are single items of '
                    'vocabulary that happen to be three words long. Nothing '
                    'inside them is chosen.', 't2an',
                    'Learn them whole, the way you learn <em>however</em> '
                    'or <em>nevertheless</em>.'),
                   ('t2bh', 'Bookended by prepositions', 't2bb',
                    'Most take one preposition at each end: <em>on</em> the '
                    'verge <em>of</em>, <em>at</em> the expense <em>of</em>, '
                    '<em>for</em> the sake <em>of</em>. Drop either and the '
                    'phrase stops working.', 't2bn',
                    'The gap is usually the first one, because the second '
                    'is almost always <em>of</em>.'),
                   ('t2ch', 'They mark register', 't2cb',
                    'This set belongs to formal and written English &mdash; '
                    'reports, speeches, meetings. Using them is part of '
                    'sounding B2 rather than B1.', 't2cn',
                    '<em>In spite of</em> and <em>despite</em> mean the '
                    'same; <em>despite</em> takes no <em>of</em>.')],
                  folder=F, bg=BG_IDIOM)

        + "".join(D.mc(i + 1, len(IDIOM), q, 'mcbEyebrow',
                       'Activity 2 &middot; Fixed phrases', 'mcbTitle',
                       'Complete the expression', folder=F, bg=BG_IDIOM)
                  for i, q in enumerate(IDIOM))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'Verbs and adjectives that come with a preposition',
                  [('t3ah', 'Same idea, different preposition', 't3ab',
                    'You <em>accuse</em> someone <em>of</em> something but '
                    '<em>blame</em> someone <em>for</em> it. The meanings '
                    'are close; the prepositions are not '
                    'interchangeable.', 't3an',
                    'This is the pair that catches people out most often at '
                    'B2.'),
                   ('t3bh', 'Three that take a person and a thing', 't3bb',
                    '<em>Prevent</em> someone <em>from</em> doing it, '
                    '<em>congratulate</em> someone <em>on</em> it, '
                    '<em>succeed in</em> doing it. Each has exactly one '
                    'preposition.', 't3bn',
                    '<em>Succeed in</em> and <em>prevent from</em> are both '
                    'followed by <em>-ing</em>, never an infinitive.'),
                   ('t3ch', 'What things are made of', 't3cb',
                    '<em>Consist of</em> lists the parts; <em>specialise '
                    'in</em> names the field. <em>Consist of</em> has no '
                    'passive &mdash; nothing "is consisted of".', 't3cn',
                    '<em>Comprise</em> means the same as <em>consist of</em> '
                    'and takes no preposition at all.')],
                  folder=F, bg=BG_DEP)

        + "".join(D.mc(i + 1, len(DEPENDENT), q, 'mccEyebrow',
                       'Activity 3 &middot; Dependent pairs', 'mccTitle',
                       'Which preposition does the word take?', folder=F, bg=BG_DEP)
                  for i, q in enumerate(DEPENDENT))

        + D.teach('t4Eyebrow', 'Before you start',
                  't4Title', 'Phrasal verbs where the preposition is the meaning',
                  [('t4ah', 'Three words, one verb', 't4ab',
                    '<em>Look up to</em>, <em>look down on</em>, <em>put up '
                    'with</em>, <em>come up with</em>. The whole string is '
                    'the verb; no part of it can be changed or '
                    'moved.', 't4an',
                    'The object always comes after the entire phrase: put '
                    'up with <em>the noise</em>.'),
                   ('t4bh', 'The direction carries the meaning', 't4bb',
                    'Look <em>up to</em> someone is to admire them; look '
                    '<em>down on</em> someone is to think yourself above '
                    'them. One particle apart, opposite in '
                    'meaning.', 't4bn',
                    'The literal image survives here, which makes this pair '
                    'unusually easy to remember.'),
                   ('t4ch', 'Nothing to work out', 't4cb',
                    '<em>Get away with</em> is to escape consequences, '
                    '<em>stand up for</em> is to defend, <em>cut down on</em> '
                    'is to reduce. None of these is recoverable from the '
                    'parts.', 't4cn',
                    'These are the ones that make speech sound natural, so '
                    'they are worth the memorising.')],
                  folder=F, bg=BG_PHRASAL)

        + "".join(D.mc(i + 1, len(PHRASAL), q, 'mcdEyebrow',
                       'Activity 4 &middot; Phrasal verbs', 'mcdTitle',
                       'Finish the phrasal verb', folder=F, bg=BG_PHRASAL)
                  for i, q in enumerate(PHRASAL))

        + D.results('resNext', 'You can spot it. Now use it &rarr;', folder=F)

        + D.activate('Make the case', 'Use at least three:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'A department is being cut. One of you speaks for the '
                     'staff, the other for management. Five minutes each '
                     'side, then swap roles and argue the opposite.',
                     ['Speak <em>on behalf of</em> your team and say what '
                      'the decision would cost, <em>in terms of</em> morale '
                      'as well as money.',
                      'Concede one point &mdash; something you have had to '
                      '<em>put up with</em> &mdash; then <em>come up '
                      'with</em> an alternative.',
                      'Argue that the saving comes <em>at the expense of</em> '
                      'something the company cannot afford to lose.'],
                     'Writing &middot; 180&ndash;250 words',
                     'Write the email your side sends afterwards: what was '
                     'agreed, what remains open, and what you are asking for '
                     'next. It goes to people who were not in the room, so '
                     'nothing can be left implied. Use at least three of the '
                     'expressions above.',
                     'Following this morning’s meeting…',
                     folder=F, bg=BG_ACT)
    )

    import i18n_prepb2 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Advanced Prepositions (B2) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d questions, %d bytes'
          % (OUT, s.count('<section class="slide'), len(ALL), len(s)))


if __name__ == '__main__':
    build()
