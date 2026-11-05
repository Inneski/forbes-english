# -*- coding: utf-8 -*-
"""Who Was First in Space? (C1) — a new deck from a magazine feature.

Source: "Why Yuri Gagarin wasn't the first in space – and who beat him to it",
by the literary historian Vladimir Brljak (6 March 2026), pasted by Innes on
2026-11-05 with the illustration of two balloonists in a gondola as the hero.

The article is an argument, not a report, which is what makes it C1: it lays
out the practical and scientific definitions of where space begins, concedes
that they are useful, and then makes a case for a third, cultural one — the
first astronaut is whoever first saw the blue sky turn black. So the deck
teaches the reading, the vocabulary of limits and records, the writer's own
grammar of emphasis (ONLY + time/place + inversion: "Only in the 17th century
did scientists begin…"), and the moves of the argument (concede, build the
case, land a verdict). The activation asks the learner to make that kind of
case themselves.

Decisions:

1. **The article is retold, not reproduced.** It is a copyrighted feature, so
   the four reading slides are a summary in new words, carrying the facts,
   the figures and a handful of short quotes from the pilots. Every point the
   questions test is in the retelling.

2. **Light theme, blue accent.** The hero is a flat coral field, bright and
   airy, which is the §4a case; the palette is extract-palette.py --light
   --accent-hue 200, unedited (Innes wanted blue, not the default coral-red).

3. **Artwork: one picture, five sections.** §5c wants a background per
   section. Only the hero arrived, so every section slot falls back to the
   hero until its plate exists in FirstInSpace/. Drop the plates in
   incoming/first-in-space/, run prep-artwork.py with the SLOT names, re-run
   this builder: the swap is automatic, nothing else to edit.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import deck as D
import i18n_firstinspace as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'first-in-space-c1.html'
F = 'FirstInSpace'
E = I.T['en']

# One plate per section (HOUSE-STYLE §5c). A missing plate means the slide
# shows the hero, which the engine does when data-bg is absent.
SLOTS = ('bg-sky', 'bg-records', 'bg-only', 'bg-case', 'bg-act')
os.makedirs(os.path.join('incoming', 'first-in-space'), exist_ok=True)


def bg(slot):
    return slot + '.jpg' if os.path.exists(os.path.join(F, slot + '.jpg')) else None


SKY, REC, ONLY, CASE, ACT = (bg(s) for s in SLOTS)

# py lesson-template/extract-palette.py FirstInSpace/hero.jpg --light --accent-hue 200
# (2026-11-05, every row PASS). Innes asked for blue instead of the coral-red
# the tool picks by default; 200deg is the plates' slate-blue (median ~185)
# pushed a little toward blue so it reads as blue, not teal.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #d8b5ac;
  --surface       : #e1cac4;
  --surface2      : #dcbeb8;
  --border        : #4a7d96;
  --text          : #11212a;
  --text-dim      : #2e4e5e;
  --accent        : #005d8b;
  --accent-bright : #004c71;
  --accent-dim    : #18a6ee;
  --secondary     : #f29681;
  --contrast      : #9c0d22;''' % F

# The reading: a retelling, in English in every build.
R1A = ('Two numbers are usually quoted. The FAI puts the edge of space at '
       '<strong>100 km</strong>: the Kármán line. US government and military bodies draw '
       'it at 50 miles, about 80 km. Both mark roughly where the air becomes too thin '
       'for wings or balloons to hold anything up.')
R1B = ('The Oxford English Dictionary says space is what lies <strong>beyond Earth’s '
       'atmosphere</strong>. But the atmosphere reaches far further than was once assumed: '
       'its last atoms only disappear about 630,000 km out, beyond the Moon and well past '
       'anywhere a human has been.')
R2A = ('For centuries most Europeans assumed the blue day sky simply <em>was</em> space. '
       'Night, they thought, was just Earth’s shadow, hiding a bright blue universe for a '
       'few hours. Scientists began to picture a black universe in the 17th century, but '
       'the blue one survived in the popular mind until the Space Age.')
R2B = ('So there is a third way to define space: historical and cultural. On this view, '
       'the first astronaut is the first person who climbed high enough to <strong>watch '
       'the sky turn black</strong>, and saw with their own eyes that the old bright cosmos '
       'had been an illusion.')
R3A = ('Albert Stevens and Orvil Anderson rose to 22.1 km in a sealed gondola. They could '
       'just make out the curve of the Earth. Above them, they radioed, the sky was '
       '“very dark indeed”, but it could still be called blue.')
R3B = ('At 23.2 km in 1956, Malcolm Ross and Lee Lewis became the first to see the sky '
       'overhead as <strong>black</strong>, before a faulty valve brought them down early. '
       'A year later David Simons spent over 24 hours up there, among stars that no '
       'longer twinkled.')
R4A = ('Rocket planes had reached these heights first. But William Bridgeman, at 24.2 km '
       'in 1951, admitted he had been “too damn busy” to look. Iven Kincheloe went far '
       'higher in 1956, yet saw a blue-black sky for only a few seconds.')
R4B = ('In 1960 Joseph Kittinger jumped from a balloon at 31.3 km and called the sky above '
       'him “very hostile”. In 2021 William Shatner crossed the Kármán line, and said the '
       'real moment was watching the blue go by. A number, says the writer, is an idea; '
       'the vanishing sky is felt.')

# (stem, options, correct index, explanation key). Keys spread over positions.
MC = [
    dict(stem='Why does the writer call the 100 km and 80 km limits &ldquo;arbitrary&rdquo;?',
         options=['they were set by experts who could not agree',
                  'they suit aircraft, not a definition of space',
                  'they have been measured wrongly for decades',
                  'they were fixed before anyone flew that high'],
         correct=1, why='q1why'),
    dict(stem='By the dictionary&rsquo;s definition, has anyone been to space yet?',
         options=['yes, anyone who has crossed the Kármán line',
                  'yes, the Apollo 13 crew set a record there',
                  'no, the dictionary gives no real definition',
                  'no, nobody has gone past the last of the air'],
         correct=3, why='q2why'),
    dict(stem='Before the 17th century, most Europeans believed night was caused by ______.',
         options=['Earth&rsquo;s shadow hiding a blue universe',
                  'the sky turning black above the clouds',
                  'the sun moving out into the black of space',
                  'dust in the air blocking out the sunlight'],
         correct=0, why='q3why'),
    dict(stem='What did the Explorer II crew report in 1935?',
         options=['a sky so black that the stars had stopped twinkling',
                  'a clear view of the black void beyond the atmosphere',
                  'a very dark sky that could nonetheless be called blue',
                  'no colour at all, because their windows had frozen'],
         correct=2, why='q4why'),
    dict(stem='Why does William Bridgeman not count as the first, in the writer&rsquo;s view?',
         options=['he never went as high as the balloonists',
                  'he was too busy flying to look at the sky',
                  'he flew at night, so the sky was black anyway',
                  'his plane&rsquo;s windows only faced the ground'],
         correct=1, why='q5why'),
    dict(stem='Why does the writer mention William Shatner?',
         options=['to show celebrities can now reach space easily',
                  'to prove the Kármán line is the right definition',
                  'to compare his flight with Gagarin&rsquo;s orbit',
                  'to show that seeing the sky go black still matters'],
         correct=3, why='q6why'),
]

VOCAB = [
    dict(stem='In 1956 Kincheloe flew the X-2 to an ______ 38.5 km. Nobody had ever been so high.',
         options=['undistinguished', 'unprecedented', 'unremarkable', 'inconsequential'],
         correct=1, why='v1why'),
    dict(stem='A faulty valve forced Ross and Lewis to come down ______, after only a few minutes at the top.',
         options=['provisionally', 'conventionally', 'prematurely', 'intermittently'],
         correct=2, why='v2why'),
]

STANCE = [
    dict(stem=E['s1stem'],
         options=['Admittedly, Gagarin orbited Earth, but the balloonists saw it first.',
                  'Clearly, Gagarin orbited Earth, and so he was the first in space.',
                  'Obviously, the balloonists were first, and Gagarin simply followed.',
                  'Without doubt, Gagarin was first, whatever the balloonists saw.'],
         correct=0, why='s1why'),
    dict(stem='&ldquo;In my book, their claim is at least as good as Gagarin&rsquo;s.&rdquo; The writer is ______.',
         options=['citing a book about the history of flight',
                  'giving a personal but firm verdict',
                  'admitting that Gagarin was first after all',
                  'saying the evidence is all in a book'],
         correct=1, why='s2why'),
]

GAPS = [
    [('Only in 1956 ______ anyone actually see the sky overhead turn black.',
      ['did|could'], 'gp1why'),
     ('Only above about 20 km ______ the sky begin to darken properly.',
      ['does|did'], 'gp2why')],
    [('Only inside a sealed gondola ______ a human survive at that height.',
      ['can|could'], 'gp3why'),
     ('Only around 630,000 km from Earth ______ there no atoms of air at all.',
      ['are|were'], 'gp4why')],
]
BANK = ['are', 'is', 'did', 'has', 'does', 'was', 'can', 'do']

MATCH = [
    ('arbitrary', 'decided by choice, not by any real principle'),
    ('a benchmark', 'a point of reference used to judge others'),
    ('within touching distance', 'extremely close to achieving something'),
    ('a feat', 'something difficult done with skill or courage'),
    ('humbled', 'made aware of how small or limited you are'),
]

CHIPS = ['Only then did …', 'a good case can be made that', 'I would still argue that',
         'it seems absurd to argue that', 'in my book', 'arbitrary', 'a benchmark',
         'unprecedented', 'within touching distance']


def build():
    D.assert_no_key_is_longest(MC, 'FirstInSpace MC')
    D.assert_no_key_is_longest(VOCAB, 'FirstInSpace vocab')
    D.assert_no_key_is_longest(STANCE, 'FirstInSpace stance')
    flat = [a for part in GAPS for _, aa, _ in part for a in aa]
    pos = D.assert_bank_is_not_a_key(BANK, flat)
    logo = D.logo_from(TPL)

    def read(n, title, ah, a, bh, b):
        k = 'r%d' % n
        return D.teach('readEyebrow%d' % n, E['readEyebrow%d' % n], k + 'Title', title,
                       [(k + 'ah', ah, None, a, None, None),
                        (k + 'bh', bh, None, b, k + 'n', E[k + 'n'])],
                       folder=F, bg=SKY)

    def card(h, b, n):
        return (h, E[h], b, E[b], n, E[n] if n else None)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('leadEyebrow', E['leadEyebrow'], 'leadTitle', E['leadTitle'],
                  [card('l1h', 'l1b', None), card('l2h', 'l2b', None),
                   card('l3h', 'l3b', None)], folder=F, bg=SKY)

        + read(1, E['r1Title'], E['r1ah'], R1A, E['r1bh'], R1B)
        + read(2, E['r2Title'], E['r2ah'], R2A, E['r2bh'], R2B)
        + read(3, E['r3Title'], E['r3ah'], R3A, E['r3bh'], R3B)
        + read(4, E['r4Title'], E['r4ah'], R4A, E['r4bh'], R4B)

        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', E['qEyebrow'], 'qTitle', E['qTitle'],
                       folder=F, bg=SKY)
                  for i, q in enumerate(MC))

        + D.teach('wordsEyebrow', E['wordsEyebrow'], 'wordsTitle', E['wordsTitle'],
                  [card('w1h', 'w1b', 'w1n'), card('w2h', 'w2b', 'w2n'),
                   card('w3h', 'w3b', 'w3n')], folder=F, bg=REC)
        + D.match(MATCH, 'matchEyebrow', E['matchEyebrow'], 'matchTitle', E['matchTitle'],
                  'matchHint', E['matchHint'], 'matchWhy', folder=F, bg=REC)
        + "".join(D.mc(i + 1, len(VOCAB), q, 'vEyebrow', E['vEyebrow'], 'vTitle', E['vTitle'],
                       folder=F, bg=REC)
                  for i, q in enumerate(VOCAB))

        + D.teach('gramEyebrow', E['gramEyebrow'], 'gramTitle', E['gramTitle'],
                  [card('g1h', 'g1b', 'g1n'), card('g2h', 'g2b', 'g2n'),
                   card('g3h', 'g3b', 'g3n')], folder=F, bg=ONLY)
        + "".join(D.gap(n + 1, len(GAPS), part, BANK, 'gapEyebrow', E['gapEyebrow'],
                        'gapTitle', E['gapTitle'], folder=F, bg=ONLY,
                        hint_key='gapHint', hint=E['gapHint'])
                  for n, part in enumerate(GAPS))
        + D.order(['Only', 'in the 17th century', 'did scientists', 'begin to imagine',
                   'a black universe'],
                  'orderEyebrow', E['orderEyebrow'], 'orderTitle', E['orderTitle'],
                  'orderHint', E['orderHint'], 'ordWhy', folder=F, bg=ONLY,
                  decoys=['scientists did'])

        + D.teach('argEyebrow', E['argEyebrow'], 'argTitle', E['argTitle'],
                  [card('a1h', 'a1b', 'a1n'), card('a2h', 'a2b', 'a2n'),
                   card('a3h', 'a3b', 'a3n')], folder=F, bg=CASE)
        + D.mc(1, 2, STANCE[0], 'sEyebrow', E['sEyebrow'], 'sTitle', E['sTitle'],
               folder=F, bg=CASE, stem_key='s1stem')
        + D.mc(2, 2, STANCE[1], 'sEyebrow', E['sEyebrow'], 'sTitle', E['sTitle'],
               folder=F, bg=CASE)

        + D.results('resNext', E['resNext'], folder=F, bg=ACT)
        + D.activate(E['actTitle'], E['actUse'], CHIPS, E['actSpeakKind'], E['actSpeakBrief'],
                     [E['actSpeak%d' % n] for n in (1, 2, 3, 4)],
                     E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                     folder=F, bg=ACT)
    )

    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Who Was First in Space? (C1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    missing = [x for x in SLOTS if not bg(x)]
    print('wrote %s — %d bytes, bank positions %s' % (OUT, len(s), pos))
    print('plates missing (hero shown instead): %s' % (', '.join(missing) or 'none'))


if __name__ == '__main__':
    build()
