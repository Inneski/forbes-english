# -*- coding: utf-8 -*-
"""The Design Pitch — rebuilt as a deck.

The old page ran three activities down one scroll and carried a live scoring
bug: the badge counted out of 17 while the real maximum was 24, so the number
changed meaning between the middle of the lesson and the end. The deck engine
counts its own scored elements, so that whole class of mistake is gone.

Two content decisions worth recording. The twelve-phrase sorting exercise
became a reference slide plus a matching exercise on what each phrase actually
does — sorting into three buckets tested recognition of a category label, not
of the language. And five of the seven multiple-choice keys were the longest
option on their slide, which on a lesson about persuasive phrasing is close to
fatal: the more considered wording genuinely is the longer one, so length was
a free answer key. Every distractor was lengthened to match.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from pitch_mc import MC

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lesson-2.html'
F = 'DesignPitch'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e0c09;
  --surface       : #1c1912;
  --surface2      : #28241b;
  --border        : #845546;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #d77759;
  --accent-bright : #e9a48e;
  --accent-dim    : #a64b2f;
  --secondary     : #f1ecd0;
  --contrast      : #1dedba;''' % F

# ── The phrasebook, kept whole from the old sorting exercise ────────────
OPENERS = ['The concept stems from&hellip;', 'What we set out to explore&hellip;',
           'At the heart of this proposal&hellip;', 'The driving idea was&hellip;']
CONCEPT = ['rooted in contrast', 'a spatial tension between',
           'conceptually driven by', 'an honest expression of']
FEEDBACK = ['That&rsquo;s a useful point &mdash;', 'We can absolutely revisit&hellip;',
            'Could you say more about&hellip;', 'That feedback helps us refine&hellip;']

# ── Vocabulary gaps: the verbs the lesson actually teaches ──────────────
GAPS = [
    ('We need to ______ the tactility of the object &mdash; it is central to the concept.',
     ['foreground'],
     'To <strong>foreground</strong> something is to bring it to prominence. Borrowed from visual arts theory and now standard in design talk.'),
    ('The materiality is in direct ______ with the landscape: timber and rammed earth echo the site.',
     ['dialogue'],
     '<strong>In dialogue with</strong> implies a two-way relationship. <em>Influenced by</em> only runs one way, which is weaker.'),
    ('We would like to ______ those budget constraints as an opportunity to simplify the concept.',
     ['reframe'],
     'To <strong>reframe</strong> is to present a problem in a new light &mdash; without dismissing the concern that raised it.'),
    ('Rather than ______ to a conventional corridor plan, we organised the spaces around a void.',
     ['defaulting'],
     '<strong>Defaulting to</strong> names the convention you are departing from. Naming it is what makes the departure read as a decision.'),
    ('The concept grew out of a ______ between public access and private contemplation.',
     ['tension'],
     'A <strong>tension</strong> is the engine of a design narrative: two things that pull against each other, which the building then resolves.'),
]
BANK = sorted(['foreground', 'dialogue', 'reframe', 'defaulting', 'tension',
               'articulate', 'precedent', 'threshold'])

MATCH = [
    ('grew directly out of', 'Says where an idea came from, and implies it was necessary'),
    ('we chose to connect', 'Marks a decision as deliberate rather than accidental'),
    ('is in direct dialogue with', 'Describes a two-way relationship with the context'),
    ('we would like to reframe', 'Turns a constraint into an opportunity, politely'),
    ('an attempt to make', 'Claims ambition without overpromising the result'),
]

CHIPS = ['grew out of', 'a tension between', 'rather than defaulting to',
         'in dialogue with', 'to foreground', 'to reframe', 'a strong direction']


def build():
    D.assert_no_key_is_longest(MC, 'Design Pitch')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    def col(head_key, head, items):
        return (head_key, head,
                "<br>".join('&ldquo;%s&rdquo;' % p for p in items), None, None)

    slides = (
        D.cover(logo,
                'The Design <em>Pitch</em>',
                'Language, narrative and persuasion &mdash; how designers make an idea land',
                [('Level', 'B2 &middot; Professional communication'),
                 ('Focus', 'Design &amp; creative pitching'),
                 ('Count', '15 slides')])
        + D.teach('narrEyebrow', 'Before anything else',
                  'narrTitle', 'A pitch is an argument, not a description',
                  [('n1h', '1 &middot; The tension',
                    'Every good narrative starts from two things that pull against each other &mdash; <em>public access and private contemplation</em>, <em>weight and lightness</em>.',
                    'n1b', 'Without a tension there is nothing for the building to resolve, and nothing for you to say.'),
                   ('n2h', '2 &middot; The decision',
                    'Name the convention, then depart from it: <em>rather than defaulting to a corridor plan&hellip;</em>',
                    'n2b', 'Departing from a norm you have not named reads as ignorance. Naming it reads as judgement.'),
                   ('n3h', '3 &middot; The translation',
                    'Turn the abstract idea into something the client can picture: <em>its edges blur into the terrain</em>.',
                    'n3b', 'If a non-specialist cannot repeat your idea back, you have described the drawing, not the concept.')],
                  folder=F, bg='podium.jpg')
        + D.teach('phraseEyebrow', 'The phrasebook',
                  'phraseTitle', 'Twelve phrases, in the three places you need them',
                  [col('pcol1', 'Starting a narrative', OPENERS),
                   col('pcol2', 'Describing a concept', CONCEPT),
                   col('pcol3', 'Responding to feedback', FEEDBACK)],
                  folder=F, bg='pair.jpg')
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'In the room',
                       'qTitle', 'Which one lands?', folder=F, ctx=q['ctx'],
                       bg=['sun.jpg', None, 'podium.jpg', None, 'pair.jpg', None, 'sun.jpg'][i])
                  for i, q in enumerate(MC))
        + "".join(
            D.gap(n + 1, 2, part, BANK, 'gapEyebrow', 'The working verbs',
                  'gapTitle', 'The words that do the lifting', folder=F,
                  hint_key='gapHint',
                  hint='These five words carry most of a design pitch. Type the one that belongs.')
            for n, part in enumerate([GAPS[:3], GAPS[3:]]))
        + D.match(MATCH, 'matchEyebrow', 'What the phrase is doing',
                  'matchTitle', 'Five moves from a real pitch',
                  'matchHint', 'Click a phrase, then click what it does.',
                  'Notice that none of these describes the building. They describe the speaker&rsquo;s relationship to the idea, to the site, or to the client — which is what a pitch is actually made of.',
                  folder=F, bg='growth.jpg')
        + D.results('resNext', 'Recognising the language is half of it. Now pitch something →')
        + D.activate('Pitch it', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in threes',
                     'One designer, two clients. The clients must interrupt at least twice.',
                     ['Open on the tension your concept resolves. Two sentences, no specification.',
                      'A client says it does not fit their brand. Respond without defending the work.',
                      'A client cuts the budget by a fifth. Reframe it in front of them.',
                      'Close by naming what this is a direction for, not a solution to.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the opening of a pitch for a building you know well. Start from the tension.',
                     'The concept grew out of&hellip;')
    )
    import i18n_pitch as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'The Design Pitch — B2', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, bank positions %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH),
             pos, len(s)))


if __name__ == '__main__':
    build()
