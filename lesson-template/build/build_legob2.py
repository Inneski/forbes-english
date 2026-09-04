# -*- coding: utf-8 -*-
"""Lego Car Building (B2), Part I — rebuilt as a 16:9 deck.

`forbes-lego-b2.html`, the anchor of the B2 Lego car strand and third of the
nine Lego pages off the scrolling format. All fifteen scored items survive:
five multiple choice on engineering terms, five gaps from a word bank, five
phrasal-verb gaps.

What changed, beyond the format:

- **The options never moved.** They were static HTML rendered in DOM order, so
  the key sat at position three, two, three, two and four across five
  questions and never first. Dealt fresh in `legob2_data.py`, and the template
  shuffles them again on every load. A related oddity goes with it: the printed
  A/B/C/D letters were out of sequence on questions three, four and five,
  because someone hand-shuffled the letters and left the DOM alone. The deck
  generates its letters from position, so it cannot happen here.
- **Question one's key was the longest option** by eight characters. The
  distractors are longer now, and each is still the same real error: taking it
  apart, gluing it, reinforcing it.
- **The gaps took one spelling.** Hyphens and spacings are accepted both ways
  now &mdash; `load-bearing` and `load bearing`, `fine-tune` and `fine tune`.
- **It now teaches.** The original's three section intros were task
  instructions; every definition lived in the feedback after the answer. Three
  slides now cover the design vocabulary as pairs that are easy to confuse
  (blueprint/prototype, modular/iterative, load-bearing/tolerance), the phrasal
  verbs in the order you would actually use them, and the habit the whole
  activity one depends on &mdash; reading what a term rules out, because every
  distractor here is a near-synonym.

Both word banks are sorted case-insensitively and checked against
`assert_bank_is_not_a_key`, so neither hands the answers over in gap order.

Artwork is the existing `lego/` family, and the cover is `lego-car-lineup.jpg`,
already this page's own image, so `library.html` needs no edit. The derived
palette is amber, which keeps it apart from Part II's coral.

`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference. Every other token is `extract-palette.py` output unedited.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from legob2_data import MC, FIB, FIB_BANK, DND, DND_BANK

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-lego-b2.html'
F = 'lego'

# python3 lesson-template/extract-palette.py lego/lego-car-lineup.jpg
PALETTE = '''  --hero: url('%s/lego-car-lineup.jpg');

  --void          : #2e2f28;
  --surface       : #1b1c12;
  --surface2      : #27291a;
  --border        : #6f522e;
  --text          : #f5f4f2;
  --text-dim      : #bfb3a3;
  --accent        : #db8b28;
  --accent-bright : #ebad60;
  --accent-dim    : #8b591c;
  --secondary     : #5295a5;
  --contrast      : #1ddded;''' % F

CHIPS = ['lay out', 'cross-reference', 'snap into place', 'troubleshoot',
         'fine-tune', 'load-bearing', 'a modular design', 'the next iteration']

MC_BG = ['lego-car-chase-desert.jpg', 'lego-b2-scene-c.jpg', 'lego-b2-cube-1.jpg',
         'lego-b2-scene-a.jpg', 'lego-b2-cube-2.jpg']
FIB_BG = ['lego-b2-cube-1.jpg', 'lego-car-chase-desert.jpg', 'lego-b2-scene-a.jpg']
DND_BG = ['lego-b2-scene-c.jpg', 'lego-b2-cube-2.jpg', 'lego-car-chase-desert.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'LegoB2')
    D.assert_bank_is_not_a_key(FIB_BANK, [a[0] for _, a, _ in FIB])
    D.assert_bank_is_not_a_key(DND_BANK, [a[0] for _, a, _ in DND])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Lego Car Building <em>Part I</em>',
                'The words engineers actually use, and why the near-synonym is always '
                'wrong',
                [('Level', 'B2 &middot; Upper-intermediate'),
                 ('Focus', 'Design &amp; engineering vocabulary'),
                 ('Count', '17 slides')])

        + D.teach('deEyebrow', 'Before the questions',
                  'deTitle', 'Words for the thing before the thing',
                  [('de1h', '<em>Prototype</em> and <em>blueprint</em>', 'de1b',
                    'A <strong>blueprint</strong> is the plan on paper. A '
                    '<strong>prototype</strong> is the first one you actually build, '
                    'made to be tested and thrown away. One is a drawing, the other is '
                    'an object.',
                    'de1n', 'You draw a blueprint, you build a prototype. The verbs do '
                            'not swap.'),
                   ('de2h', '<em>Modular</em> and <em>iterative</em>', 'de2b',
                    '<strong>Modular</strong> describes the thing: built from '
                    'self-contained sections you can replace one at a time. '
                    '<strong>Iterative</strong> describes the process: build, test, '
                    'change, build again.',
                    'de2n', 'A modular design makes an iterative process cheap. They are '
                            'not the same idea.'),
                   ('de3h', '<em>Load-bearing</em> and <em>tolerance</em>', 'de3b',
                    'A <strong>load-bearing</strong> part holds weight the rest depends '
                    'on. <strong>Tolerance</strong> is how much error a fit will accept '
                    'before it stops working &mdash; the gap between good enough and '
                    'not.',
                    'de3n', 'Both come from real engineering, and both are used '
                            'unchanged in everyday B2 English.')],
                  folder=F, bg='lego-b2-cube-1.jpg')

        + D.teach('pvEyebrow', 'The register',
                  'pvTitle', 'Phrasal verbs are the technical ones here',
                  [('pv1h', 'Before you start', 'pv1b',
                    '<strong>Lay out</strong> the pieces &mdash; spread them where you '
                    'can see them. <strong>Cross-reference</strong> the diagram with the '
                    'parts list &mdash; check one against the other. Both are '
                    'preparation, and both are separable.',
                    'pv1n', '<em>Lay them out</em>, <em>cross-reference it against</em> '
                            '&mdash; the object can sit inside.'),
                   ('pv2h', 'While you build', 'pv2b',
                    'Pieces <strong>snap into</strong> place. When one does not, you '
                    '<strong>troubleshoot</strong> the problem &mdash; work through it '
                    'in order until you find the cause.',
                    'pv2n', '<em>Troubleshoot</em> is one word and takes a direct '
                            'object. Not <em>troubleshoot for</em>.'),
                   ('pv3h', 'At the end', 'pv3b',
                    'You <strong>fine-tune</strong> the mechanism: small adjustments to '
                    'something that already works. Not repair, not redesign &mdash; the '
                    'last five per cent.',
                    'pv3n', 'If it is broken you fix it. You only fine-tune something '
                            'already close.')],
                  folder=F, bg='lego-b2-scene-a.jpg')

        + D.teach('prEyebrow', 'The C1 habit at B2',
                  'prTitle', 'The distractor is the near-synonym',
                  [('pr1h', 'Read what the word rules out', 'pr1b',
                    '<em>Align</em> is about position, not connection, so gluing and '
                    'reinforcing are both wrong however sensible they sound. Each of '
                    'these words says one thing and excludes the rest.',
                    'pr1n', 'Ask what the word does <em>not</em> mean. That is usually '
                            'faster.'),
                   ('pr2h', '<em>Orientation</em> is direction, not place', 'pr2b',
                    'A beam in the wrong <strong>orientation</strong> is in the right '
                    'position and facing the wrong way. Wrong length, wrong colour and '
                    'unattached are three different errors with three different names.',
                    'pr2n', 'Position, orientation, dimension, colour &mdash; four '
                            'properties, four words.'),
                   ('pr3h', '<em>Retrofit</em> has a time built into it', 'pr3b',
                    'To <strong>retrofit</strong> is to add something <em>after</em> the '
                    'thing was finished. Rebuilding it, or leaving it alone, or '
                    'stripping a feature out are all different actions.',
                    'pr3n', 'The word carries a sequence. That is what makes it '
                            'precise.')],
                  folder=F, bg='lego-b2-cube-2.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'What does the term actually mean?',
                       folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, part, FIB_BANK,
                        'fibEyebrow', 'Activity 2 &middot; The design vocabulary',
                        'fibTitle', 'One word fits each gap',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='Eight words in the bank, five gaps. The three left over '
                             'are the near-misses.',
                        width=185, size=17)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + "".join(D.gap(n + 1, 3, part, DND_BANK,
                        'dndEyebrow', 'Activity 3 &middot; The phrasal verbs',
                        'dndTitle', 'Complete the instruction',
                        folder=F, bg=DND_BG[n], hint_key='dndHint',
                        hint='Seven phrases in the bank, five gaps. Two belong to no gap '
                             'here.',
                        width=200, size=17)
                  for n, part in enumerate([DND[:2], DND[2:4], DND[4:]]))

        + D.results('resNext', 'You have the words. Now build with them &rarr;',
                    folder=F, bg='lego-car-lineup.jpg')

        + D.activate('Talk through the build', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you designed it, the other has to build it from your '
                     'description alone. Four minutes each, then swap.',
                     ['Describe how you would prepare a complex build before touching a '
                      'single piece.',
                      'Explain a mechanism you understand &mdash; gears, hinges, '
                      'suspension &mdash; to someone who does not.',
                      'Something in your build does not fit. Talk your partner through '
                      'troubleshooting it.',
                      'Describe a design you would call modular, and say what that buys '
                      'you.'],
                     'Writing &middot; 150&ndash;180 words',
                     'Write the design note that goes with a prototype. Say what the '
                     'blueprint specified, which parts are load-bearing, where the '
                     'tolerances are tight, and what the next iteration will change. '
                     'Write it for an engineer, not a customer.',
                     'The first prototype was laid out from the blueprint on…',
                     folder=F, bg='lego-car-chase-desert.jpg')
    )

    import i18n_legob2 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Lego Car Building (B2) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d phrasal, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(DND), len(s)))


if __name__ == '__main__':
    build()
