# -*- coding: utf-8 -*-
"""Active & Passive Voice, Lego edition (B1) — rebuilt as a 16:9 deck.

`forbes-english-lego-passive-active.html`, second of the nine Lego pages off
the scrolling format. All twenty scored items survive: seven multiple choice,
six gaps, five transformations to match and two sentences to rebuild.

The page's grammar reference was the best pre-teaching in the Lego set — two
voices, the three mechanical steps, a six-row tense table, when to use the
passive, and a common-mistakes panel — and it is the raw material for the
three opening slides rather than something that had to be invented. What
changed:

- **The keys never sat at A.** Positions ran C, C, B, B, B, D, C across seven
  questions, and the options were rendered in fixed order against `q.c`, so
  nothing moved at runtime either. Dealt across all four positions in
  `pav_data.py`, and the template shuffles them again on every load.
- **Question five's key was the only long option** — 76 characters against a
  64-character longest distractor, on an item about *why* a writer chooses the
  passive, where the reasoning is the whole point. The distractors are longer
  now, and each of the three is a real belief learners hold: that the passive
  conceals, that it is always more formal, that nobody knows the founder.
- **The gaps took one spelling each**, compared with `===`. Contractions and
  apostrophe-less forms are accepted now.
- **The explanations named option letters.** With the positions dealt fresh and
  shuffled at runtime, a letter means nothing; every explanation names the
  language instead, which is what it should have done from the start.

Three defects in the old page are simply gone with it, and are recorded here
because they were live: it scored twenty-two items while the header, the ring
and the final card all said twenty, which drove the progress ring's dashoffset
negative; `restart()` never restored the matching grid, so a second run lost
five of the points; and the matching activity cost nothing for a wrong guess
and awarded the last pair by elimination.

Artwork is the existing `lego/` family. The cover is `lego-b2-cube-1.jpg`,
already this page's own image, so `library.html` needs no edit. The palette is
the dark derivation, which also keeps this deck apart from Present Perfect with
Lego — the other Lego deck, drawn from the same folder and built light.
`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference; every other token is `extract-palette.py` output unedited.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from pav_data import MC, FIB, MATCH, ORDER

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lego-passive-active.html'
F = 'lego'

# python3 lesson-template/extract-palette.py lego/lego-b2-cube-1.jpg
PALETTE = '''  --hero: url('%s/lego-b2-cube-1.jpg');

  --void          : #2b2f33;
  --surface       : #182126;
  --surface2      : #1f2b32;
  --border        : #b04357;
  --text          : #f5f2f2;
  --text-dim      : #bfa3a8;
  --accent        : #ea6f85;
  --accent-bright : #f6abb8;
  --accent-dim    : #d72746;
  --secondary     : #053048;
  --contrast      : #1ded64;''' % F

CHIPS = ['was made', 'is kept', 'has been used', 'can be seen',
         'by the designer', 'it was decided', 'are believed to', 'was given to me']

MC_BG = ['lego-b2-scene-a.jpg', 'lego-b2-cube-2.jpg', 'lego-b2-scene-c.jpg',
         'lego-b2-cube-0.jpg', 'lego-b2-scene-b.jpg', 'lego-b2-cube-2.jpg',
         'lego-b2-scene-a.jpg']
FIB_BG = ['lego-b2-cube-0.jpg', 'lego-b2-scene-c.jpg', 'lego-b2-cube-2.jpg']
ORD_BG = ['lego-b2-scene-b.jpg', 'lego-b2-cube-0.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'PassiveActive')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Active &amp; <em>Passive</em>',
                'Who did it, who it was done to, and when English decides not to say',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'The passive voice'),
                 ('Count', '19 slides')])

        + D.teach('voEyebrow', 'Before the questions',
                  'voTitle', 'Two voices, one event',
                  [('vo1h', 'Active: the subject acts', 'vo1b',
                    'Subject, verb, object. <em>Lego <strong>releases</strong> new sets '
                    'every year.</em> The subject does the releasing, and this is the '
                    'ordinary way English puts a sentence together.',
                    'vo1n', 'Direct, short, and the right default. The passive is the '
                            'marked choice.'),
                   ('vo2h', 'Passive: the subject receives', 'vo2b',
                    '<strong>Be</strong> + past participle. <em>New sets <strong>are '
                    'released</strong> every year.</em> The subject is on the receiving '
                    'end, and the doer can be named with <em>by</em> or left out '
                    'entirely.',
                    'vo2n', 'Same event, different thing in the spotlight.'),
                   ('vo3h', 'Three steps to turn one into the other', 'vo3b',
                    'The object becomes the subject; the verb becomes <em>be</em> + past '
                    'participle <strong>in the original tense</strong>; the old subject '
                    'becomes <em>by</em> + agent, and that part is optional.',
                    'vo3n', '<em>Ole Kirk Christiansen founded Lego</em> &rarr; <em>Lego '
                            'was founded by Ole Kirk Christiansen</em>.')],
                  folder=F, bg='lego-b2-cube-1.jpg')

        + D.teach('tnEyebrow', 'The mechanism',
                  'tnTitle', '<em>Be</em> carries the tense, always',
                  [('tn1h', 'The simple tenses', 'tn1b',
                    'Present: <em>Lego makes bricks</em> &rarr; <em>bricks <strong>are '
                    'made</strong></em>. Past: <em>they built a castle</em> &rarr; <em>a '
                    'castle <strong>was built</strong></em>. Only <em>be</em> moves; the '
                    'participle never changes.',
                    'tn1n', '<em>Is / are</em> for the present, <em>was / were</em> for '
                            'the past.'),
                   ('tn2h', 'The perfect tenses', 'tn2b',
                    '<em>She has tested the set</em> &rarr; <em>the set <strong>has been '
                    'tested</strong></em>. <em>He had launched it</em> &rarr; <em>it '
                    '<strong>had been launched</strong></em>. The perfect keeps its '
                    'auxiliary and adds <em>been</em>.',
                    'tn2n', '<em>Has been</em>, <em>had been</em> &mdash; two words, and '
                            'both are needed.'),
                   ('tn3h', 'Modals and the infinitive', 'tn3b',
                    'After a modal, <em>be</em> stays bare: <em>you can assemble it</em> '
                    '&rarr; <em>it <strong>can be assembled</strong></em>. The passive '
                    'infinitive is <em>to be</em> + past participle: <em>designs that '
                    'might <strong>be turned into</strong> sets</em>.',
                    'tn3n', 'A modal never takes <em>been</em>. <em>Can been '
                            'assembled</em> is not English.')],
                  folder=F, bg='lego-b2-scene-c.jpg')

        + D.teach('whEyebrow', 'Why bother',
                  'whTitle', 'When the passive is the better sentence',
                  [('wh1h', 'When nobody knows who', 'wh1b',
                    '<em>The brick <strong>was dropped</strong>.</em> If the doer is '
                    'unknown, or obvious, or beside the point, the active forces you to '
                    'invent a subject. The passive lets you leave it out.',
                    'wh1n', 'It is not evasion. Often it is simply the only honest '
                            'sentence available.'),
                   ('wh2h', 'When the result is the news', 'wh2b',
                    'Reports, labels, instructions and science put the thing first: '
                    '<em>the design <strong>was patented</strong> in 1958</em>. The '
                    'patent office is not what the sentence is about.',
                    'wh2n', 'This is why formal writing uses it so much &mdash; and why '
                            'it can sound cold.'),
                   ('wh3h', 'The three mistakes', 'wh3b',
                    'Never <em>was been</em> &mdash; it is either <em>was</em> or '
                    '<em>has been</em>. Agree with the new subject: <em>the bricks '
                    '<strong>were</strong> made</em>. And use the participle, not the '
                    'past: <em>was <strong>written</strong></em>, not <em>was '
                    'wrote</em>.',
                    'wh3n', 'Every one of these comes from forgetting that <em>be</em> '
                            'is the verb doing the work.')],
                  folder=F, bg='lego-b2-cube-0.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'Read the voice', folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, part, None,
                        'fibEyebrow', 'Activity 2 &middot; The exact form',
                        'fibTitle', 'Put the verb into the passive',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='The verb and the tense are both given. Contractions are '
                             'accepted.',
                        width=185, size=17)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 3 &middot; The transformation',
                  'matchTitle', 'Match the active to its passive',
                  'matchHint', 'Click an active sentence, then click its passive.',
                  'matchWhy', folder=F, bg='lego-b2-scene-a.jpg')

        + "".join(D.order(chunks, 'ordEyebrow',
                          'Activity 4 &middot; Sentence building',
                          'ordTitle', 'Build the passive sentence',
                          'ordHint', 'Click a chunk to place it, click a placed chunk '
                                     'to take it back.',
                          why, folder=F, bg=ORD_BG[n])
                  for n, (chunks, why) in enumerate(ORDER))

        + D.results('resNext', 'You can build it. Now decide when to use it &rarr;',
                    folder=F, bg='lego-b2-cube-1.jpg')

        + D.activate('Write the museum label', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you is a museum guide, the other a visitor who keeps asking '
                     '&ldquo;but who actually did it?&rdquo;. Three minutes each, then '
                     'swap.',
                     ['Describe how something in the room was made, without saying who '
                      'made it.',
                      'Your partner asks who is responsible. Answer twice: once naming '
                      'the agent, once leaving it out.',
                      'Explain a rule at your school or workplace using the passive '
                      'three times.',
                      'Tell the story of an object you own &mdash; where it was made, '
                      'when it was given to you, what has been done to it since.'],
                     'Writing &middot; 120&ndash;150 words',
                     'Write the label a museum would put beside a famous object. Say '
                     'when it was made, what it was made from, how it has been used and '
                     'where it is kept now. Name an agent only where the reader would '
                     'actually want to know.',
                     'This model was built in…',
                     folder=F, bg='lego-b2-scene-b.jpg')
    )

    import i18n_pav as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Active &amp; Passive Voice (LEGO ed.) | B1 | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d order, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(MATCH),
             len(ORDER), len(s)))


if __name__ == '__main__':
    build()
