# -*- coding: utf-8 -*-
"""Lego Car Building (B2), Part II — rebuilt as a 16:9 deck.

`forbes-lego-b2-part2.html`, the second half of the B2 Lego car pair. All
fifteen scored items survive: five error-correction sentences with two faults
each, five transformations, five technical terms to match.

Part I is the vocabulary; this is what you do with it. The two share no items
and are meant to be taken in order.

What changed, beyond the format:

- **Error-correction item 2 was mis-keyed, and the key reversed the sentence.**
  The original read *he had to substitute the original wheels **with** a smaller
  alternative* and corrected *with* to *for* &mdash; but *substitute X for Y*
  means use X in place of Y, so the "corrected" version says he kept the
  original wheels. *Substitute with* is widely accepted anyway. Replaced with a
  preposition error that is unambiguously wrong: *depends **from***, the Romance
  carry-over, alongside an incompatibility the sentence already sets up.
- **Two transformation keys were markedly shorter than their distractors** —
  55 characters against 95, and 67 against 104. Short-is-the-answer gives the
  game away exactly as long-is-the-answer does, and it is not a defect
  `check-lesson.js` looks for. The distractors are tightened to sit within a few
  characters of the key, and each stays the error it was.
- **The matching dropdowns never consumed a definition.** All five carried the
  same five options, so the last item was free by elimination. `match()` takes
  each definition out of play as it is placed, so the fifth pair costs the same
  as the first.
- **It now teaches.** The original had no pre-question content at all: three
  activities and the rules only in the feedback. Three slides now cover the
  prepositions the tested verbs insist on, the two slips the error-correction
  section is built around (*to*/*too*, adjective/adverb), and the four
  transformation patterns.

One number changes. The old page scored an error-correction sentence as one
point for both of its blanks, giving fifteen; the deck engine counts every
input, so the same fifteen items are worth twenty. That is the more honest
count &mdash; a learner who fixes one fault of two has done half the work
&mdash; and nothing on the page claims otherwise.

Artwork is the existing `lego/` family; the cover is `lego-b2-scene-c.jpg`,
already this page's own image, so `library.html` needs no edit. The derived
palette is coral, against Part I's amber, so the pair reads as a pair without
reading as one lesson twice.

`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference. Every other token is `extract-palette.py` output unedited.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from legob2p2_data import MC, ERR, MATCH

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-lego-b2-part2.html'
F = 'lego'

# python3 lesson-template/extract-palette.py lego/lego-b2-scene-c.jpg
PALETTE = '''  --hero: url('%s/lego-b2-scene-c.jpg');

  --void          : #2a2f2a;
  --surface       : #121c12;
  --surface2      : #1a291a;
  --border        : #b94548;
  --text          : #f5f2f2;
  --text-dim      : #bfa3a4;
  --accent        : #ec787b;
  --accent-bright : #f7b4b6;
  --accent-dim    : #db2e32;
  --secondary     : #344e6b;
  --contrast      : #1ded83;''' % F

CHIPS = ['consists of', 'depends on', 'too&hellip; to&hellip;', 'only to',
         'despite', 'must', 'in sequence', 'incompatible with']

MC_BG = ['lego-b2-cube-2.jpg', 'lego-car-lineup.jpg', 'lego-b2-scene-a.jpg',
         'lego-car-chase-desert.jpg', 'lego-b2-cube-0.jpg']
ERR_BG = ['lego-car-chase-desert.jpg', 'lego-b2-cube-2.jpg', 'lego-b2-scene-a.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'LegoB2P2')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Lego Car Building <em>Part II</em>',
                'The prepositions verbs insist on, and four ways to say the same thing '
                'better',
                [('Level', 'B2 &middot; Upper-intermediate'),
                 ('Focus', 'Collocation &amp; sentence transformation'),
                 ('Count', '15 slides')])

        + D.teach('coEyebrow', 'Before the questions',
                  'coTitle', 'The verb chooses the preposition',
                  [('co1h', 'Fixed, and not negotiable', 'co1b',
                    'A mechanism <strong>consists of</strong> parts &mdash; never '
                    '<em>from</em>, never <em>in</em>. A fit <strong>depends on</strong> '
                    'tolerance, never <em>from</em>. There is no rule underneath these; '
                    'the verb simply takes one preposition.',
                    'co1n', '<em>Consist from</em> and <em>depend from</em> are the two '
                            'commonest carry-overs from Romance languages.'),
                   ('co2h', 'Two verbs that look alike', 'co2b',
                    'You <strong>replace</strong> one part <em>with</em> another, but '
                    'you <strong>substitute</strong> a new part <em>for</em> the old '
                    'one. The order reverses, and getting it wrong reverses the '
                    'sentence.',
                    'co2n', '<em>Substituted the wheels for smaller ones</em> means the '
                            'smaller ones went on.'),
                   ('co3h', 'Phrases that are learned whole', 'co3b',
                    'Components go on <strong>in sequence</strong>, work is done '
                    '<strong>in order</strong>, a part is <strong>in place</strong>. No '
                    'article, no plural, and no logic to appeal to.',
                    'co3n', 'These are the ones that make writing sound native or not, '
                            'and they are pure memory.')],
                  folder=F, bg='lego-b2-cube-0.jpg')

        + D.teach('grEyebrow', 'The two slips',
                  'grTitle', 'One letter, and one word class',
                  [('gr1h', '<em>To</em> and <em>too</em>', 'gr1b',
                    '<strong>Too</strong> with two <em>o</em>s means excessively: '
                    '<em>too rigid to absorb the impact</em>. <strong>To</strong> with '
                    'one is the infinitive marker or a preposition. The sentence usually '
                    'needs both, one after the other.',
                    'gr1n', '<em>Too X to Y</em>: the first is the degree, the second '
                            'belongs to the verb.'),
                   ('gr2h', 'Adjectives and adverbs', 'gr2b',
                    'An adjective describes a thing: <em>an <strong>inefficient</strong> '
                    'mechanism</em>. An adverb describes an action: <em>it turned '
                    '<strong>inefficiently</strong></em>. Ask what the word is attached '
                    'to.',
                    'gr2n', 'If it sits next to a verb, it needs the <em>-ly</em>. '
                            'Almost always.'),
                   ('gr3h', 'Where errors hide', 'gr3b',
                    'Both of these survive a read-through because the sentence still '
                    'makes sense. Proofreading for meaning will not find them; you have '
                    'to look at what each word is doing.',
                    'gr3n', 'This is why error correction is a separate skill from '
                            'writing.')],
                  folder=F, bg='lego-b2-scene-a.jpg')

        + D.teach('trEyebrow', 'Saying it again, better',
                  'trTitle', 'Four structures worth having',
                  [('tr1h', '<em>Too&hellip; to&hellip;</em>', 'tr1b',
                    '<em>So stiff that it was impossible to turn</em> becomes '
                    '<em><strong>too</strong> stiff <strong>to</strong> turn</em>. Nine '
                    'words become four and nothing is lost. The negative is built in '
                    '&mdash; do not add another.',
                    'tr1n', '<em>Too stiff to not turn</em> is the error this structure '
                            'invites.'),
                   ('tr2h', '<em>Only to&hellip;</em>', 'tr2b',
                    '<em>He worked for three hours <strong>only to</strong> discover a '
                    'mistake.</em> It marks an outcome that undoes the effort. Not just '
                    '&ldquo;and then&rdquo; &mdash; it carries the disappointment.',
                    'tr2n', 'Effort first, reversal second. The order is part of the '
                            'meaning.'),
                   ('tr3h', '<em>Despite</em> and <em>must</em>', 'tr3b',
                    '<strong>Despite</strong> takes a noun phrase, not a clause: '
                    '<em>despite its fragile appearance</em>, not <em>despite it '
                    'looked</em>. And <em>it is essential that you read</em> becomes '
                    '<em>you <strong>must</strong> read</em>.',
                    'tr3n', '<em>Despite of</em> does not exist. <em>In spite of</em> '
                            'does.')],
                  folder=F, bg='lego-car-lineup.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Activity 1 &middot; Transformation',
                       'mcTitle', 'Same meaning, new structure',
                       folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, part, None,
                        'errEyebrow', 'Activity 2 &middot; Error correction',
                        'errTitle', 'Two wrong words in each sentence',
                        folder=F, bg=ERR_BG[n], hint_key='errHint',
                        hint='Type the correction only. Each sentence has exactly two.',
                        width=165, size=17)
                  for n, part in enumerate([ERR[:2], ERR[2:4], ERR[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 3 &middot; The technical terms',
                  'matchTitle', 'Match the term to its definition',
                  'matchHint', 'Click a term, then click what it means.',
                  'matchWhy', folder=F, bg='lego-b2-cube-2.jpg')

        + D.results('resNext', 'You can fix it. Now report it &rarr;',
                    folder=F, bg='lego-b2-scene-c.jpg')

        + D.activate('Report the fault', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you built it and one of you is testing it, and it does not '
                     'work. Four minutes each, then swap.',
                     ['Describe a mechanism that failed, and say what it depends on that '
                      'was not there.',
                      'Explain something that took far longer than it should have '
                      '&mdash; and use <em>only to</em>.',
                      'Concede a fault and defend the design anyway. Start with '
                      '<em>despite</em>.',
                      'Give three instructions a builder must follow, and say why each '
                      'one matters.'],
                     'Writing &middot; 150&ndash;180 words',
                     'Write the fault report an engineer would file after testing a '
                     'prototype. Say what the mechanism consists of, what the failure '
                     'depended on, what was too weak to hold, and what must change '
                     'before the next build. Keep it factual and keep the collocations '
                     'right.',
                     'The drive assembly consists of…',
                     folder=F, bg='lego-car-chase-desert.jpg')
    )

    import i18n_legob2p2 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Lego Car Building — Part 2 (B2) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d error rows, %d pairs, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(ERR), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
