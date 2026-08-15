# -*- coding: utf-8 -*-
"""Make v Do — rebuilt as a deck.

The old page was a scrolling quiz: no hero, no logo, no slides, no activation
stage, its own font stack and an invented palette. Everything scored survives —
ten gap-fills, six collocation pairs, an eight-item sort and eight phrasal verbs
— but the rules now get taught before anything is graded, rather than appearing
only in post-answer feedback.

**Every key was at index 0** in the source — all six collocation pairs and all
eight phrasal verbs listed the correct option first, and the eight-item sort ran
make/do/make/do straight down. Neither the old page nor this deck exposes that
to a learner: the old page shuffled with `fisherYates`, and the deck template
shuffles `.opt` children on first view and the sort pool on build, both
deliberately ("so option order is never a tell"). So this was never a live
defect in either version, and deranging the source is hygiene rather than a
fix — it matters for a printed hand-out, for anyone reading the builder, and if
the engine's shuffle is ever removed. Done anyway:

    collocations  1 0 0 1 1 0
    phrasal verbs 2 0 3 1 0 3 1 2
    sort          M M D M D D M D

**The rules were only ever in the feedback.** The general make/produce
v do/perform split, the fixed expressions that break it, and the phrasal verbs
were all discoverable only by answering and reading the explanation — so the
one way to learn a rule was to get its item wrong. Four teaching slides now
carry them, and the phrasal verbs are grouped by particle rather than met one
at a time in a shuffled queue.

**Known loss, recorded rather than fixed:** the old page carried a German
explanation for all 24 explained items. `deck.py` writes per-item feedback into
a `data-explain` attribute, which `UI_I18N` does not reach — the switcher only
resolves `data-i18n` keys. So the German explanations cannot survive this
architecture, and only the interface is translated. Noted in HANDOFF; it wants
an engine change, not a per-lesson workaround.

Artwork: the supplied image is a 3376x1440 diptych with a hard seam at x=1688.
The left panel carries "MAKING. v DOING." set into it, which would fight the
deck's own cover title, so the cover takes the right panel (the Mustang, which
leaves clean space for type) and the lettered panel becomes the background on
the teaching slides, where it reinforces the split being taught.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'make-v-do.html'
F = 'MakeVDo'

# Derived: python3 lesson-template/extract-palette.py MakeVDo/hero.jpg
# Every row in the contrast report passes.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e090e;
  --surface       : #1c121c;
  --surface2      : #281a28;
  --border        : #8f3e54;
  --text          : #f5f2f3;
  --text-dim      : #bfa3ab;
  --accent        : #e05379;
  --accent-bright : #ef8ca6;
  --accent-dim    : #b1264c;
  --secondary     : #35496c;
  --contrast      : #1ded51;''' % F

# ── collocation pairs · keys deranged 1 0 0 1 1 0 ─────────────────────
CHOICE = [
    dict(stem='Which is correct?',
         options=['make business', 'do business'], correct=1,
         why='<strong>Do business.</strong> Business is treated as an activity you carry out, '
             'not a thing you produce &mdash; and it stays uncountable here.'),
    dict(stem='Which is correct?',
         options=['make a mistake', 'do a mistake'], correct=0,
         why='<strong>Make a mistake.</strong> One of the ones that breaks the rule: nobody '
             'produces a mistake on purpose, but the collocation is fixed.'),
    dict(stem='Which is correct?',
         options=['do the shopping', 'make the shopping'], correct=0,
         why='<strong>Do the shopping.</strong> Household activities take <em>do</em> &mdash; '
             'the shopping, the washing-up, the ironing.'),
    dict(stem='Which is correct?',
         options=['do money', 'make money'], correct=1,
         why='<strong>Make money.</strong> Money is a result you produce, through work or '
             'investment. This one follows the general rule cleanly.'),
    dict(stem='Which is correct?',
         options=['make exercise', 'do exercise'], correct=1,
         why='<strong>Do exercise.</strong> A physical activity you perform. Note that German '
             '<em>Sport machen</em> pulls learners straight to <em>make</em>.'),
    dict(stem='Which is correct?',
         options=['make a noise', 'do a noise'], correct=0,
         why='<strong>Make a noise.</strong> Noise is produced by an action &mdash; a result, '
             'so <em>make</em>. Same logic as <em>make a sound</em>.'),
]

# ── phrasal verbs · keys deranged 2 0 3 1 0 3 1 2 ─────────────────────
PV = [
    dict(stem='The raccoon knocked over the bin and ______ half our sandwiches.',
         options=['did without', 'made up for', 'made off with', 'did away with'], correct=2,
         why='<strong>Make off with something</strong> is to steal it and leave quickly.'),
    dict(stem='He was late again, so he bought coffee for the whole team to ______ it.',
         options=['make up for', 'make of', 'make off with', 'do up'], correct=0,
         why='<strong>Make up for something</strong> is to compensate for it.'),
    dict(stem='I really don&rsquo;t know what to ______ this cryptic email from the landlord.',
         options=['make up', 'do without', 'do up', 'make of'], correct=3,
         why='<strong>Make of someone or something</strong> is to have an opinion or reading of '
             'it. Almost always in a question: <em>what do you make of&hellip;?</em>'),
    dict(stem='The child ______ an elaborate story about a dragon eating his homework.',
         options=['did up', 'made up', 'made off with', 'did away with'], correct=1,
         why='<strong>Make something up</strong> is to invent it. Separable: '
             '<em>made it up</em>, not <em>made up it</em>.'),
    dict(stem='The council decided to ______ the outdated parking permits altogether.',
         options=['do away with', 'do without', 'make of', 'make up for'], correct=0,
         why='<strong>Do away with something</strong> is to abolish it. Formal, and it goes with '
             'rules, systems and institutions rather than objects.'),
    dict(stem='During the power cut, the whole street had to ______ hot water for two days.',
         options=['do away with', 'make up for', 'do up', 'do without'], correct=3,
         why='<strong>Do without something</strong> is to manage although you do not have it. '
             'Compare <em>do away with</em>, where you are the one removing it.'),
    dict(stem='After the long flight, she said she ______ a good night&rsquo;s sleep.',
         options=['could make up for', 'could do with', 'could do away with',
                  'could make off with'], correct=1,
         why='<strong>Could do with something</strong> is to want or need it. Idiomatic and '
             'always in the conditional &mdash; there is no <em>I do with a coffee</em>.'),
    dict(stem='They spent the whole summer ______ the old barn before turning it into a studio.',
         options=['making up', 'making off with', 'doing up', 'doing away with'], correct=2,
         why='<strong>Do something up</strong> is to renovate it. Also clothing: '
             '<em>do up your coat</em>.'),
]

# ── gap-fills · make or do ────────────────────────────────────────────
G = [
    ('I need to ______ a decision about my job.', ['make'],
     '<strong>Make a decision.</strong> A decision is a new result you produce.'),
    ('Can you help me ______ my homework?', ['do'],
     '<strong>Do homework.</strong> An activity you carry out, not an object you produce.'),
    ('She wants to ______ a cake for the party.', ['make'],
     '<strong>Make a cake.</strong> The clearest case of all: it did not exist before.'),
    ('He always tries to ______ his best in exams.', ['do'],
     '<strong>Do your best.</strong> Fixed &mdash; and it beats the rule, since a best effort '
     'sounds like something you produce.'),
    ('They always ______ a lot of noise at parties.', ['make'],
     '<strong>Make noise.</strong> Produced by an action, so <em>make</em>.'),
    ('We need to ______ some research before the meeting.', ['do'],
     '<strong>Do research.</strong> An activity. Note it is uncountable: '
     'not <em>a research</em>.'),
    ('I don&rsquo;t want to ______ another mistake.', ['make'],
     '<strong>Make a mistake.</strong> Fixed, and worth memorising as a pair with '
     '<em>do your best</em> &mdash; the two that break the rule in opposite directions.'),
    ('Let&rsquo;s ______ a plan for the weekend.', ['make'],
     '<strong>Make a plan.</strong> Something new you create.'),
    ('Could you ______ the washing-up, please?', ['do'],
     '<strong>Do the washing-up.</strong> Household task, like <em>do the shopping</em>.'),
    ('We always ______ progress when we plan carefully.', ['make'],
     '<strong>Make progress.</strong> Treated as a result being produced, so it takes '
     '<em>make</em> despite being abstract.'),
]

# ── sort · not the source's make/do/make/do alternation ───────────────
SORT = [('a plan', 0), ('a decision', 0), ('homework', 1), ('money', 0),
        ('research', 1), ('the washing-up', 1), ('a cake', 0), ('business', 1)]
BINS = ['make', 'do']

CHIPS = ['make a decision', 'do your best', 'make progress', 'do business',
         'make up for', 'do away with', 'could do with', 'do up']


def build():
    D.assert_no_key_is_longest(CHOICE, 'MakeVDo/collocation')
    D.assert_no_key_is_longest(PV, 'MakeVDo/phrasal')
    logo = D.logo_from(TPL)

    teach = (
        D.teach('t1e', 'The split, before anything is graded',
                't1t', 'One produces a thing. The other performs an activity.',
                [('t1ah', 'make &rarr; you produce something',
                  'A thing exists afterwards that did not exist before.',
                  't1an', '<em>make a cake &middot; make a plan &middot; make a decision &middot; '
                          'make money &middot; make noise &middot; make progress</em>'),
                 ('t1bh', 'do &rarr; you perform an activity',
                  'Work, tasks, chores, jobs. Nothing new is created.',
                  't1bn', '<em>do homework &middot; do research &middot; do the shopping &middot; '
                          'do the washing-up &middot; do exercise</em>'),
                 ('t1ch', 'The test',
                  'Ask: is there a <em>thing</em> at the end of it?',
                  't1cn', 'A cake, a plan, a decision &mdash; yes, so <em>make</em>. '
                          'Homework and research are things you <em>did</em>, not things you made.')],
                cols='1fr 1fr 1fr', folder=F, bg='lettering.jpg'),
        D.teach('t2e', 'The exceptions',
                't2t', 'Four that break the rule, and have to be learned',
                [('t2ah', 'make a mistake',
                  'Nobody produces a mistake deliberately.',
                  't2an', 'By the rule this should be <em>do</em>. It is not. Learn it as a phrase.'),
                 ('t2bh', 'do your best',
                  'A best effort sounds like something you produce.',
                  't2bn', 'It takes <em>do</em> anyway. The mirror image of '
                          '<em>make a mistake</em>.'),
                 ('t2ch', 'do business',
                  'Business feels like a thing; it behaves as an activity.',
                  't2cn', 'Also uncountable here &mdash; never <em>do a business</em>.'),
                 ('t2dh', 'do exercise',
                  'German <em>Sport machen</em> pulls you to <em>make</em>.',
                  't2dn', 'One of the most reliable first-language slips in this pair.')],
                cols='1fr 1fr 1fr 1fr', folder=F, bg='lettering.jpg'),
        D.teach('t3e', 'Phrasal verbs &middot; make',
                't3t', 'Four with <em>make</em>, grouped by particle',
                [('t3ah', 'make off with',
                  'To steal it and leave quickly.',
                  't3an', '<em>The raccoon made off with the sandwiches.</em>'),
                 ('t3bh', 'make up for',
                  'To compensate for something bad or missing.',
                  't3bn', '<em>He bought coffee to make up for being late.</em>'),
                 ('t3ch', 'make of',
                  'To have an opinion or reading of something.',
                  't3cn', 'Nearly always a question: <em>what do you make of it?</em>'),
                 ('t3dh', 'make up',
                  'To invent something untrue.',
                  't3dn', 'Separable: <em>made it up</em>, never <em>made up it</em>.')],
                cols='1fr 1fr 1fr 1fr', folder=F),
        D.teach('t4e', 'Phrasal verbs &middot; do',
                't4t', 'Four with <em>do</em> &mdash; and two that are easily swapped',
                [('t4ah', 'do away with',
                  'To abolish it. <em>You</em> remove it.',
                  't4an', 'Formal, and used of rules and systems rather than objects.'),
                 ('t4bh', 'do without',
                  'To manage although you do not have it.',
                  't4bn', 'The pair to watch: <em>do away with</em> is your choice, '
                          '<em>do without</em> is your circumstance.'),
                 ('t4ch', 'could do with',
                  'To want or need something.',
                  't4cn', 'Only in the conditional. There is no <em>I do with a coffee</em>.'),
                 ('t4dh', 'do up',
                  'To renovate &mdash; or to fasten.',
                  't4dn', '<em>doing up the barn</em>, and <em>do up your coat</em>.')],
                cols='1fr 1fr 1fr 1fr', folder=F),
    )

    slides = (
        D.cover(logo, 'Make <em>v</em> Do',
                'The rule that covers most of it, the handful that break it, '
                'and the phrasal verbs underneath',
                [('Level', 'B1 &middot; Intermediate'), ('Focus', 'Collocation &amp; phrasal verbs'),
                 ('Count', '26 slides')])
        + "".join(teach)
        + "".join(D.gap(n + 1, 4, rows, [], 'gapEyebrow', 'make or do',
                        'gapTitle', 'Complete the sentence', folder=F,
                        bg='lettering.jpg' if n % 2 else None, width=110, size=19)
                  for n, rows in enumerate([G[0:3], G[3:6], G[6:8], G[8:10]]))
        + "".join(D.mc(i + 1, len(CHOICE), q, 'colEyebrow', 'Which collocation?',
                       'colTitle', 'One of these is English', folder=F,
                       bg='lettering.jpg' if i % 3 == 2 else None)
                  for i, q in enumerate(CHOICE))
        + D.sort_slide(BINS, SORT, 'sortEyebrow', 'Sort',
                       'sortTitle', 'Which verb does each one take?',
                       'sortHint', 'Drag each expression into a box &mdash; or click the '
                                   'expression, then the box. A wrong first placement costs '
                                   'that item&rsquo;s point.',
                       'Six of these follow the rule. <em>Business</em> does not &mdash; it is an '
                       'activity that sounds like a thing, and it is the one worth remembering.',
                       folder=F)
        + "".join(D.mc(i + 1, len(PV), q, 'pvEyebrow', 'Phrasal verbs',
                       'pvTitle', 'Complete the sentence', folder=F,
                       bg='lettering.jpg' if i % 3 == 1 else None)
                  for i, q in enumerate(PV))
        + D.results('resNext', 'You know which verb. Now use them →')
        + D.activate('Say what you made and what you did', 'Use at least four:', CHIPS,
                     'Speaking &middot; in pairs',
                     'Last week, in detail. Your partner listens for a wrong collocation and stops you.',
                     ['Describe one decision you made and one task you did. Do not swap the verbs.',
                      'Tell your partner about something you had to do without.',
                      'Describe a mistake you made, and how you made up for it.',
                      'Name one thing at work or at school you would do away with.'],
                     'Writing &middot; 120&ndash;150 words',
                     'Write about a week when you were very busy: what you made, what you did, '
                     'and what you had to do without.',
                     'Last week — what I made and what I did')
    )

    import i18n_makevdo as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Make v Do — B1 | Forbes English', I)
    # The template ships --bg-opacity at 0.72, which suits a photographic hero.
    # This artwork is flat vector with a metre-high white wordmark in it, and at
    # 0.72 the "MAKING." and "DOING." letterforms competed with the slide titles
    # and swallowed the eyebrow line on the teaching slides.
    s = s.replace('  --bg-opacity: 0.72;', '  --bg-opacity: 0.34;', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    n = s.count('<section class="slide')
    print('wrote %s — %d <section class="slide" (checker header is authoritative), '
          '%d gap slides, %d collocations, 1 sort, %d phrasal verbs, %d bytes'
          % (OUT, n, 4, len(CHOICE), len(PV), len(s)))


if __name__ == '__main__':
    build()
