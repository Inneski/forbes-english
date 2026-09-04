# -*- coding: utf-8 -*-
"""Advanced Dinosaur Facts (C1) — rebuilt as a 16:9 deck.

`forbes-english-dinosaurs.html`, the last genuinely dinosaur lesson still on
the old scrolling format. All sixteen scored items survive: five multiple
choice, five terminology gaps, five matched pairs and the timeline.

The palaeontology was good and none of it changed. What changed:

- **It now teaches.** Three opening slides, and they are not filler — the
  lesson tests a vocabulary *system* it never explained. The `-ology` stems
  (ichno-, osteo-, palyno-, tapho-), the `-thermic` family (ecto-, endo-,
  meso-, homeo-, poikilo-) and how to read a scientific claim for its
  precision. Every distractor in the deck is a near-miss inside one of those
  three systems, which is only fair once the system has been shown.
- **Key positions, two over-long keys, five answer-first word banks and a
  pre-sorted timeline** — all in `dinofacts_data.py`.
- **The timeline items were forty-word sentences** being fed to a chunk pool.
  They are short labels now and the detail moved to the explanation.

Artwork: six illustrations from Innes's Downloads — the coral-and-slate
family, distinct from the muted teal set Part 0 took, so the two dinosaur
lessons do not look like the same deck twice. Palette rotated to the teal
that is in the water and the silhouettes: the honest derivation returns a
pale coral, which is the sky, so the UI disappeared into the cover.

`--void` is the one value here that is NOT the tool's output. Innes asked for
the interior slides to sit on grey rather than near-black, so the derived
canvas is lifted while every other token stays as derived. It is the canvas
only: the cover shows its hero at full opacity and is untouched, and the cards
still use the derived `--surface`, so the contrast between card and canvas is
what carries the layout. Body text still measures about 12:1 on it.
**A rebuild will not revert this — but re-deriving the palette would, so lift
it again if you re-run extract-palette.py.**
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from dinofacts_data import MC, FIB, BANK, MATCH, TIMELINE

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-dinosaurs.html'
F = 'DinoFacts'

# python3 lesson-template/extract-palette.py DinoFacts/hero.jpg \
#            --accent-hue=175 --accent-sat=0.65
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #2d3335;
  --surface       : #12191c;
  --surface2      : #1a2429;
  --border        : #6bb8b1;
  --text          : #f2f5f5;
  --text-dim      : #a3bfbd;
  --accent        : #9eebe4;
  --accent-bright : #14d7c7;
  --accent-dim    : #58d5cb;
  --secondary     : #eaaa9f;
  --contrast      : #f04ca9;''' % F

CHIPS = ['the evidence suggests', 'broadly accepted', 'thought to have been',
         'ichnology', 'mesothermic', 'infrasound', 'pneumatised',
         'consensus', 'contested', 'it now appears that']

MC_BG = ['feather.jpg', 'cliffs.jpg', 'plain.jpg', 'forest.jpg', 'crest.jpg']
FIB_BG = ['forest.jpg', 'crest.jpg', 'cliffs.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'DinoFacts')
    D.assert_bank_is_not_a_key(BANK, [a[0] for _, a, _ in FIB])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'The Hidden World of <em>Dinosaurs</em>',
                'Advanced palaeontology, the words the field uses, and the facts that '
                'refuse to sit still',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Academic vocabulary &amp; precision'),
                 ('Count', '16 slides')])

        + D.teach('ologyEyebrow', 'Before the questions',
                  'ologyTitle', 'What each -ology actually studies',
                  [('ol1h', 'Reading the stem', 'ol1b',
                    '<strong>Ichno-</strong> is a track, <strong>osteo-</strong> a bone, '
                    '<strong>palyno-</strong> pollen, <strong>tapho-</strong> a burial. '
                    'The stem names the evidence; <em>-ology</em> just means the study '
                    'of it.',
                    'ol1n', 'Guess the stem and you can usually guess the field. That is '
                            'the whole trick.'),
                   ('ol2h', 'Why it matters here', 'ol2b',
                    '<strong>Ichnology</strong> reads footprints, so it recovers '
                    'behaviour &mdash; herding, speed, hunting &mdash; from animals whose '
                    'bones were never found in that place at all.',
                    'ol2n', '<strong>Taphonomy</strong> asks a different question: not '
                            'what lived, but how it came to be preserved.'),
                   ('ol3h', 'The near-miss is the distractor', 'ol3b',
                    '<strong>Phylogenetics</strong> reconstructs relatedness, not '
                    'fossils. In a question about footprints it is plausible, adjacent '
                    'and wrong &mdash; which is exactly what a good distractor is.',
                    'ol3n', 'At C1 the wrong answer is rarely absurd. It is usually the '
                            'neighbouring term.')],
                  folder=F, bg='plain.jpg')

        + D.teach('thermEyebrow', 'One suffix, five answers',
                  'thermTitle', 'How an animal makes, or fails to make, heat',
                  [('th1h', 'The two you know', 'th1b',
                    'An <strong>ectotherm</strong> takes its heat from outside; an '
                    '<strong>endotherm</strong> generates its own. Lizard and mammal, '
                    'roughly.',
                    'th1n', '<em>Cold-blooded</em> and <em>warm-blooded</em> are the '
                            'everyday words for these two.'),
                   ('th2h', 'The one in the middle', 'th2b',
                    'A <strong>mesotherm</strong> generates heat but runs between the two '
                    'rates. It is how a dinosaur can grow at 600 kg a year without a '
                    'mammal&rsquo;s appetite.',
                    'th2n', 'Tuna and some sharks do it today, which is how the idea was '
                            'testable at all.'),
                   ('th3h', 'The two about stability', 'th3b',
                    '<strong>Homeothermic</strong> means holding a steady temperature; '
                    '<strong>poikilothermic</strong> means letting it vary. That is a '
                    'different question from where the heat comes from.',
                    'th3n', 'So an animal can be ectothermic and homeothermic at once. '
                            'The pairs are not opposites.')],
                  folder=F, bg='forest.jpg')

        + D.teach('claimEyebrow', 'The skill being tested',
                  'claimTitle', 'Read the claim, not the topic',
                  [('cl1h', 'The number carries the answer', 'cl1b',
                    '<em>75%</em> and <em>95%</em> are not rounding. One is the K-Pg '
                    'event, the other is the Permian-Triassic. A distractor often differs '
                    'from the key by a single figure.',
                    'cl1n', 'When two options differ only in a number, the number '
                            '<em>is</em> the question.'),
                   ('cl2h', 'Watch the scope word', 'cl2b',
                    '<em>Exclusively</em>, <em>only</em>, <em>never</em>, <em>confined '
                    'to</em> &mdash; an absolute makes a claim far easier to falsify, and '
                    'science rarely writes them.',
                    'cl2n', 'A hedge (<em>likely</em>, <em>possibly</em>, <em>broadly '
                            'accept</em>) is usually the safer bet.'),
                   ('cl3h', 'Plausible is not the same as accepted', 'cl3b',
                    'Every distractor here is something a reasonable person might '
                    'believe. The question asks what the field currently '
                    '<em>accepts</em>, which is a narrower thing than what sounds '
                    'sensible.',
                    'cl3n', '<em>Most accurately reflects consensus</em> is doing real '
                            'work in that stem.')],
                  folder=F, bg='cliffs.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow', 'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'What does the evidence actually support?',
                       folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, part, BANK,
                        'fibEyebrow', 'Activity 2 &middot; The exact term',
                        'fibTitle', 'The word the field would use',
                        folder=F, bg=FIB_BG[n],
                        hint_key='fibHint',
                        hint='Eighteen words in the bank; five gaps. The near-misses are '
                             'there on purpose.',
                        width=200, size=18)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 3 &middot; Five that break the rules',
                  'matchTitle', 'Match the animal to what makes it strange',
                  'matchHint', 'Click a name, then click what characterises it.',
                  'matchWhy', folder=F, bg='feather.jpg')

        + D.order(TIMELINE, 'ordEyebrow', 'Activity 4 &middot; The timeline',
                  'ordTitle', 'Put the milestones in order',
                  'ordHint', 'Click a card to place it, click a placed card to take it '
                             'back.',
                  'ordWhy', folder=F, bg='crest.jpg')

        + D.results('resNext', 'You can read the evidence. Now present it &rarr;',
                    folder=F, bg='hero.jpg')

        + D.activate('Present the strange fact', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you presents, the other is the sceptical colleague who asks '
                     'for the evidence. Four minutes each, then swap.',
                     ['Explain to a non-specialist why &ldquo;warm-blooded or '
                      'cold-blooded&rdquo; is the wrong question for a dinosaur.',
                      'Your colleague says feathers prove dinosaurs could fly. Correct '
                      'the inference without dismissing them.',
                      'Argue what ichnology can tell us that a skeleton cannot &mdash; '
                      'and be specific about what it cannot.',
                      'Present the Schweitzer soft-tissue finding, and hedge it as '
                      'carefully as the evidence deserves.'],
                     'Writing &middot; 200&ndash;250 words',
                     'Write the short &ldquo;current thinking&rdquo; box for a museum '
                     'panel on one of these: dinosaur metabolism, feather evolution, or '
                     'Spinosaurus. State what is established, mark what is contested, and '
                     'give a visitor no false certainty.',
                     'The evidence now broadly supports&hellip;',
                     folder=F, bg='plain.jpg')
    )

    import i18n_dinofacts as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Advanced Dinosaur Facts | C1 | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d timeline, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(MATCH),
             len(TIMELINE), len(s)))


if __name__ == '__main__':
    build()
