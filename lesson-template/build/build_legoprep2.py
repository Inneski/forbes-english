# -*- coding: utf-8 -*-
"""LEGO Prepositions & Phrasal Verbs — Part 2 (B2) — rebuilt as a 16:9 deck.

`forbes-english-lego-lesson-part2.html` was a five-tab scrolling quiz with no
teaching content at all — every rule lived only in the per-answer feedback,
the exact gap already flagged against both Lego B2 decks in
`docs/HANDOFF.md`. All 27 scored items survive unchanged in substance: 6
multiple-choice, 5 fill-in-the-blank, 6 true/false, 5 matching pairs, 5
error-correction (already multiple choice on the old page, so nothing to
convert there).

What changed, beyond the format:

- **Three teaching slides now exist.** None did. They cover exactly the
  traps the 27 items test: literal vs idiomatic phrasal verbs, prepositions
  that are fixed rather than logical, and near-identical forms that mean
  different things (`apart from` / `take apart`, `sort out` / the invented
  `sort away`).
- **True/false becomes six two-option multiple-choice slides.** There is no
  dedicated true/false slide type in the shared engine, and a two-option MC
  is exactly what the tab already was — the True/False choice is a UI label,
  not part of the English being taught, so it is never translated (see the
  `exam1`/`exam2` builders for the same convention).
- **The old score was 27; the deck score is also 27.** Every FITB row and
  every TF/EC item is one point each here, same as the page it replaces —
  unlike the Lego Car Building pair, nothing on the old page bundled two
  answers into one point, so there is no re-count to report.

Artwork is the lesson's own `LegoPart2/` pair: the dice brick is the hero,
the brick wall becomes the background on the slides below. The derived
palette is a dark pink/red, mechanically pulled from the hero — never
hand-picked.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from legoprep2_data import MC, FITB, FITB_BANK, TF, MATCH, EC

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lego-lesson-part2.html'
F = 'LegoPart2'

# python3 lesson-template/extract-palette.py LegoPart2/lego-dice-brick.jpg
PALETTE = '''  --hero: url('%s/lego-dice-brick.jpg');

  --void          : #0f1417;
  --surface       : #182026;
  --surface2      : #1f2a32;
  --border        : #8d4351;
  --text          : #f5f2f2;
  --text-dim      : #bfa3a9;
  --accent        : #dd5973;
  --accent-bright : #ed90a3;
  --accent-dim    : #b02b45;
  --secondary     : #053151;
  --contrast      : #1ded60;''' % F

CHIPS = ['fall off', 'sell out', 'get round to', 'look forward to',
         'take apart', 'sort out', 'impact of']

WALL = 'lego-brick-wall.jpg'


def build():
    D.assert_no_key_is_longest(MC, 'LegoPrep2-MC')
    D.assert_no_key_is_longest(EC, 'LegoPrep2-EC')
    D.assert_bank_is_not_a_key(FITB_BANK, [a[0] for _, a, _ in FITB])
    logo = D.logo_from(TPL)

    tf_mc = [dict(stem=sentence, options=['True', 'False'],
                  correct=0 if is_true else 1, why=why)
             for sentence, is_true, why in TF]

    slides = (
        D.cover(logo, 'LEGO Prepositions &amp; Phrasal Verbs <em>Part 2</em>',
                'Fixed prepositions, idiomatic particles, and the '
                'lookalikes that trip B2 learners up',
                [('Level', 'B2 &middot; Upper-intermediate'),
                 ('Focus', 'Prepositions &amp; phrasal verbs'),
                 ('Count', '27 questions')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'One particle, more than one meaning',
                  [('t1ah', 'The same particle, two different jobs', 't1ab',
                    'A LEGO set can <strong>sell out</strong> (no stock left) '
                    'or be <strong>sold off</strong> (sold cheap to clear '
                    'it) &mdash; one letter of difference, unrelated '
                    'meanings.', 't1an',
                    'Never assume a phrasal verb means what its parts '
                    'suggest.'),
                   ('t1bh', 'Idiomatic, not physical', 't1bb',
                    '<strong>Get round to</strong> something has nothing to '
                    'do with going around anything &mdash; it means finally '
                    'finding the time. The literal image is gone; only the '
                    'idiom is left.', 't1bn',
                    'This is why phrasal verbs are learned as whole units, '
                    'not built from their pieces.'),
                   ('t1ch', 'One verb, two senses', 't1cb',
                    '<strong>Make out</strong> can mean to understand '
                    '("make out why") or to discern a shape at a distance. '
                    'Context decides which.', 't1cn',
                    'A dictionary entry with three numbered senses is '
                    'normal for a phrasal verb &mdash; a single English '
                    'verb rarely has that many.')],
                  folder=F)

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title', 'Some prepositions are simply fixed',
                  [('t2ah', 'No other choice', 't2ab',
                    'You <strong>look forward to</strong> something &mdash; '
                    'never <em>forward for</em>, never <em>forward '
                    'about</em>. The preposition is part of the phrase, not '
                    'a free slot.', 't2an',
                    'If a fixed phrase feels swappable, that feeling is '
                    'wrong.'),
                   ('t2bh', 'Location prepositions are precise', 't2bb',
                    'Something sits <strong>at the bottom</strong> of a '
                    'box, not <em>in the bottom</em>. <em>At</em> marks a '
                    'specific point; <em>in</em> suggests a contained area '
                    '&mdash; the wrong one still sounds like English, which '
                    'is what makes it easy to miss.', 't2bn',
                    'The same applies to <em>the impact of</em> something '
                    '&mdash; never <em>impact in</em>.'),
                   ('t2ch', 'A line, not a scatter', 't2cb',
                    '<strong>Alongside</strong> a street means following '
                    'its length, in a continuous row. <strong>In '
                    'between</strong> means alternating positions. They '
                    'describe different shapes, not the same idea twice.',
                    't2cn', 'Picture the arrangement before choosing the '
                            'preposition.')],
                  folder=F, bg=WALL)

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'Lookalikes that are not the same word',
                  [('t3ah', '<em>Apart from</em> vs <em>take apart</em>',
                    't3ab',
                    '<strong>Take apart</strong> is the phrasal verb: you '
                    'take a model apart to sort the pieces. '
                    '<strong>Apart from</strong> is a preposition meaning '
                    '"except for". Neither can stand in for the other.',
                    't3an', 'If you can replace it with "except for" and '
                            'the sentence still works, it is the '
                            'preposition, not the phrasal verb.'),
                   ('t3bh', 'A particle that does not exist', 't3bb',
                    '<strong>Sort out</strong> means to organise something. '
                    'There is no <em>sort away</em>, no <em>sort off</em> '
                    '&mdash; swapping the particle does not give you a '
                    'rarer synonym, it gives you an error.', 't3bn',
                    'When in doubt, the particle that exists is usually '
                    'the only one that does.'),
                   ('t3ch', 'A verb that needs someone doing it', 't3cb',
                    '<strong>Run out of</strong> needs an active subject: '
                    '"the store <strong>ran out of</strong> stock" &mdash; '
                    'not "the stock <em>was run out of</em>". Passive '
                    'grammar and a phrasal verb do not always combine.',
                    't3cn', 'Say who is doing the running out.')],
                  folder=F, bg=WALL)

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'Choose the preposition or phrasal verb',
                       folder=F, bg=None if i % 2 else WALL)
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, rows, FITB_BANK,
                        'fEyebrow', 'Activity 2 &middot; Fill in the blank',
                        'fTitle', 'Complete each sentence from the word bank',
                        folder=F, hint_key='fHint',
                        hint='Use each expression from the bank once at '
                             'most.')
                  for n, rows in enumerate([FITB[:2], FITB[2:4], FITB[4:]]))

        + "".join(D.mc(i + 1, len(tf_mc), q, 'tfEyebrow',
                       'Activity 3 &middot; True or false',
                       'tfTitle', 'Is the underlined phrase used correctly?',
                       folder=F, bg=None if i % 2 else WALL)
                  for i, q in enumerate(tf_mc))

        + D.match(MATCH, 'matchEyebrow', 'Activity 4 &middot; Building &amp; progress',
                  'matchTitle', 'Match the phrasal verb to its definition',
                  'matchHint', 'Click a phrase, then click what it means.',
                  'matchWhy', folder=F, bg=WALL)

        + "".join(D.mc(i + 1, len(EC), q, 'ecEyebrow',
                       'Activity 5 &middot; Error correction',
                       'ecTitle', 'Find the correct replacement',
                       folder=F, bg=None if i % 2 else WALL)
                  for i, q in enumerate(EC))

        + D.results('resNext', 'You can recognise it. Now use it &rarr;',
                    folder=F)

        + D.activate('Explain the build', 'Use at least three:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you is the LEGO instructor, one is a new '
                     'builder who keeps making mistakes. Four minutes '
                     'each, then swap.',
                     ['Explain a mistake a beginner always makes, and say '
                      'what they should do instead.',
                      'Describe a set that <em>sold out</em> immediately, '
                      'and one you are <em>looking forward to</em>.',
                      'Tell your partner to <em>sort out</em> their pieces '
                      'before they <em>take</em> anything <em>apart</em>.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write a short guide for a new LEGO club member: what '
                     'they must do before starting a build, one mistake '
                     'they should avoid, and what to do if a piece is '
                     'missing. Use at least three of the expressions above.',
                     'Before you start, make sure you…',
                     folder=F, bg=WALL)
    )

    import i18n_legoprep2 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'LEGO Prepositions &amp; Phrasal Verbs — Part 2 (B2) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d TF, %d pairs, %d EC, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FITB),
             len(TF), len(MATCH), len(EC), len(s)))


if __name__ == '__main__':
    build()
