# -*- coding: utf-8 -*-
"""Nature agency vocabulary, Part 2 — rebuilt as a 16:9 deck.

Same filename, so the live URL does not change.

**It was not a lesson.** Fifty autograded items and no teaching content at
all: no rule box, no table, no worked example. Section 1 carried no hint
field on any of its seventeen items, so all eleven of its rules — including
the most useful thing in the file, the fixed pattern `swindle sb OUT OF
sth` — were learnable only by answering first and reading the mark. There
are now fourteen teaching slides in front of the questions. Section 1 is
taught as **eight confusable pairs plus a named method** (what the word
goes with, what follows it, who says it), because that is what the section
was secretly built on and never said.

**All seventeen Section 1 keys were index 0.** The runtime shuffle hid it,
but a static render inherited a 100% "always A" key. Worse, option B was
the sibling confusable in twelve of seventeen and C/D were filler, so
spotting the structure turned every item into a coin toss. The key is now
deranged across all four positions (4/4/4/5) and the sibling sits at every
possible offset from it; both distributions are asserted at build time, in
`assert_key_is_deranged`, so a later edit cannot quietly re-align them.
The two halves of each pair are also separated by at least four items —
previously they were adjacent, and six of seventeen items therefore
carried no independent information.

**Section 3 could not be lost.** `s3Score++` fired only on a correct
match; a wrong match flashed red for 550ms and cost nothing, and the exit
gate opened only at 16/16. Every learner who reached the results screen
scored exactly 16/16, so the reported percentage was `0.68 × real + 32`
and 41% real accuracy displayed as "Solid foundation". The shared match
engine in `deck.py` still has that property — it is thirty-odd shipped
lessons' worth of behaviour and changing it is a deliberate decision that
does not belong in one rebuild — so **Section 3 is now three `sort_slide`
activities binned by sense** instead. Sorting scores the first placement
only: put a word in the wrong box and the point is gone, which is what
makes the section losable.

**Right and wrong said the same thing.** All seventeen Section 1 items
ran `(isCorrect ? "Correct. " : "Not quite. ") + q.explanation` — the body
was byte-identical. Every distractor now carries its own `data-explain`,
so a learner who picks *swindle* where *defraud* was wanted is told about
`out of`, not re-told why *defraud* was right. Section 2's explanations
also used to restate their own pre-answer hint almost word for word
(100% content-word overlap on two items, ~60% mean); the hints now
scaffold recall (sense plus letter count) and the explanations carry
collocation, register and family information the hint did not.

**Eleven of seventeen Section 2 items rejected correct English.** There
was no alternatives array at all — `answer` was one string. `take into
consideration`, `complain`, `calm`, `attributes` and, worst of all,
`prefers` (standard British collective-noun agreement, which the item
itself depends on) were all marked wrong. Every gap now takes pipes, and
the collective-noun rule is taught before it is tested.

**Two facts were wrong.** Sand martins were nesting in "an old flint
quarry": they are obligate burrow-excavators that dig 50–100cm tunnels
into friable vertical faces, which flint — hard silica in chalk — cannot
provide. It is now **an old sand pit**. And *crane* was defined solely as
the lifting machine, two rows above *flock*, in a nature-conservation
lesson: the bird comes first here, and it is taught alongside the habitat
sense of *survey*, which the old file used five times while defining it
as land measurement only.

**The setting contradicted itself.** "Federal Agency for Nature
Conservation" is the official English name of Germany's Bundesamt für
Naturschutz, wrapped around bylaws, the Wildlife Act, licences,
roundabouts, car parks, visitor centres, a bird hide and reed warblers —
and the UK has no federal agencies. The institution is now the
**Wildlife and Countryside Agency**; `offense`→`offence`,
`bylaw`→`byelaw`, `memorize`→`memorise`.

Also fixed: nineteen words appeared only as distractors and were defined
nowhere, twelve of them Part 1 vocabulary — the deck now says on its
second slide that Part 1 comes first, and draws its distractors from
words this lesson itself teaches; the stem jargon (*the hide*, *cull*,
*byelaw*, *sand martin*) is glossed before the answer rather than
nowhere; the results bands told a Part 2 learner to revise "before moving
to Part 2"; the Section 1 results label read "Definitions"; and the deck
now has a logo, a hero, a derived palette, a German interface and an
activation stage, none of which existed.

Artwork: `NatureAgency2/hero-otter.jpg` on the cover and behind every
interior slide; `NatureAgency2/loch.jpg` behind the two scene-setting
slides and the results; `NatureAgency2/hide.jpg` behind the glossary,
under the definition of *the hide*; `NatureAgency2/shore.jpg` behind the
activation stage; `NatureAgency2/reeds.jpg` on the three section dividers. The two savanna illustrations that shipped in this
folder are of a different continent from every word in the lesson and are
not used.
"""
import random
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = '/home/claude/forbes-english/lesson-template/lesson-template.html'
OUT = '/home/claude/forbes-english/forbes-nature-agency-part2.html'
F = 'NatureAgency2'
BG2 = 'reeds.jpg'
# The loch: calm water, a clean band of sky, and the most empty space of the
# three, so it goes behind the text-heavy scene-setting slides and the results
# where the reeds' verticals fight the copy. The stone house on the far shore
# is a house — two storeys, two chimney stacks. It is NOT a bird hide, and
# nothing in this deck may caption it as one; the hide is taught in words.
BG3 = 'loch.jpg'
# A bird hide: timber box on stilts over the water, viewing shutters, walkway,
# reed bed. It sits behind the glossary slide, under the definition of *the
# hide* — the deck's highest-risk piece of jargon, because read as a verb the
# stem 'moving the hide further from the nest' collapses. This is the one
# background in the deck doing teaching work rather than atmosphere, and it
# earns it by actually depicting the thing. (loch.jpg does NOT: the structure
# on its far shore is a two-storey house.)
BG4 = 'hide.jpg'
# The wider shore — cabin, moored boat, waders. Atmosphere behind the
# activation stage. Nothing in it is captioned; nothing in it needs to be.
BG5 = 'shore.jpg'

# Derived mechanically from NatureAgency2/hero-otter.jpg:
#   python3 lesson-template/extract-palette.py NatureAgency2/hero-otter.jpg --light
# Every row of the contrast report PASSES. Light theme, so <html> also
# carries data-theme="light" — setting one without the other gives dark
# chrome on paper.
PALETTE = '''  --hero: url('%s/hero-otter.jpg');

  --void          : #d8beac;
  --surface       : #e1d0c4;
  --surface2      : #dcc6b8;
  --border        : #96684a;
  --text          : #2a1b11;
  --text-dim      : #5e412e;
  --accent        : #933a00;
  --accent-bright : #7a3000;
  --accent-dim    : #ee711f;
  --secondary     : #aec1c7;
  --contrast      : #07554e;''' % F

# .q-ctx carries the pre-answer gloss of the field jargon in a stem. The
# template styles its halo but not its size, so the rule lives here.
#
# The sorting bins are filled with --inset, which on a light theme is
# almost nothing: over a detailed illustration the bin edges and their
# labels stopped reading. They get the card treatment instead — same
# translucency and blur, so the artwork still shows through.
CSS = ('.q-ctx { font-size: 16px; line-height: 1.5; font-style: italic; '
       'color: var(--text-dim); border-left: 2px solid var(--accent-dim); '
       'padding-left: 14px; margin-bottom: 14px; max-width: 76ch; }\n'
       '.sort-bin { background: color-mix(in srgb, var(--surface) 86%, '
       'transparent); backdrop-filter: blur(3px); '
       'border-color: color-mix(in srgb, var(--border) 90%, transparent); }\n')


# ── guards ─────────────────────────────────────────────────────────────
def assert_key_is_deranged(mc, label='MC'):
    """The two structural defects of the section this replaces.

    Every key was at index 0, and the sibling confusable was at index 1 in
    twelve of seventeen items. Both are distributions, not per-item facts,
    so both are measured across the whole section: the key must reach all
    four positions with no position starved, and the sibling must not sit
    at one offset from the key in more than 7 of 17 items."""
    n = len(mc)
    keys = [q['correct'] for q in mc]
    counts = [keys.count(i) for i in range(4)]
    assert min(counts) >= n // 4 - 1 and 0 not in counts, (
        '%s: the key is not deranged across all four positions (%s)' % (label, counts))
    offs = [(q['sib'] - q['correct']) % 4 for q in mc]
    assert 0 not in offs, '%s: an item marks its own key as the sibling' % label
    worst = max(offs.count(o) for o in (1, 2, 3))
    assert worst <= (n * 4) // 9, (
        '%s: the sibling confusable sits at the same offset from the key in '
        '%d of %d items — that is the "B is the near-miss" structure again'
        % (label, worst, n))
    return counts, [offs.count(o) for o in (1, 2, 3)]


def assert_pairs_are_separated(mc, gap=4, label='MC'):
    """A pair tested from both sides in adjacent items leaks its own key."""
    seen = {}
    for i, q in enumerate(mc):
        p = q.get('pair')
        if not p:
            continue
        if p in seen:
            assert i - seen[p] >= gap, (
                '%s: pair %r is tested at items %d and %d — too close; the '
                'first item hands over the second' % (label, p, seen[p] + 1, i + 1))
        seen[p] = i


def mc_slide(i, total, q, ek, e, tk, t, folder='', bg=None, ctx=None):
    """D.mc, plus a per-distractor explanation.

    The shared builder writes one explanation per slide, which is what
    produced identical feedback for right and wrong on all seventeen items
    of the section this replaces. Rather than change a builder thirty
    lessons share, the attribute is injected here: each wrong option says
    why *it* is wrong, and the key falls through to the slide's own
    `why`. The engine already prefers an option's own explanation."""
    html = D.mc(i, total, q, ek, e, tk, t, folder=folder, bg=bg, ctx=ctx)
    ex = q['opt_why']
    assert len(ex) == len(q['options']), 'opt_why must line up with options'
    assert ex[q['correct']] is None, 'the key takes the slide explanation'
    parts = html.split('<button class="opt"')
    out = [parts[0]]
    for n, chunk in enumerate(parts[1:]):
        attr = ' data-explain="%s"' % D.esc(ex[n]) if ex[n] else ''
        out.append('<button class="opt"%s%s' % (attr, chunk))
    return ''.join(out)


# ── SECTION 1 — seventeen items, eight confusable pairs ────────────────
# `pair` groups the two halves of a pair so the separation guard can see
# them; `sib` is where the sibling confusable sits among the options.
S1 = [
    dict(pair='stress', correct=2, sib=0,
         stem='&ldquo;Don&rsquo;t be so <em>______</em> about the site visit '
              '&mdash; the assessor isn&rsquo;t going to bite,&rdquo; Priya '
              'laughed, handing Elena a coffee.',
         options=['stressful', 'slick', 'stressy', 'pithy'],
         why='<strong>Stressy</strong> describes a <em>person&rsquo;s</em> '
             'anxious manner, and it is informal &mdash; the register of a '
             'colleague handing you a coffee, never of a written report.',
         opt_why=[
             '<strong>Stressful</strong> describes the situation, not the '
             'person standing in it. A week is stressful; the officer running '
             'it is not.',
             '<strong>Slick</strong> means smoothly and effortlessly done, '
             'and often a shade too smoothly to trust. It says nothing about '
             'nerves.',
             None,
             '<strong>Pithy</strong> means short and forceful in the way '
             'something is <em>said</em>. It describes wording, not a mood.']),

    dict(pair='offence', correct=0, sib=3,
         ctx='A <strong>byelaw</strong> is a local rule made by a council or '
             'other public body and enforceable inside its own area.',
         stem='Repeat <em>______</em> caught illegally netting salmon now face '
              'much steeper fines under the new byelaw.',
         options=['offenders', 'assessors', 'philosophers', 'offences'],
         why='<strong>Offender</strong> is the person: the <em>-er</em> ending '
             'on a verb names the one who does it. Only a person can be '
             '<em>caught netting salmon</em>.',
         opt_why=[
             None,
             'An <strong>assessor</strong> values or judges something '
             'officially. The ending is right and the job is wrong.',
             '<strong>Philosophers</strong> study philosophy. The <em>-er</em> '
             'ending tells you the option is a person, not which person.',
             'An <strong>offence</strong> is the act itself. Acts cannot be '
             'caught in a river; the people committing them can.']),

    dict(pair='fraud', correct=3, sib=1,
         stem='Two contractors were prosecuted for trying to <em>______</em> '
              'the agency by billing for reeds that were never planted.',
         options=['revoke', 'swindle', 'entangle', 'defraud'],
         why='<strong>Defraud</strong> takes its victim straight after it '
             '&mdash; <em>defraud the agency</em>, and optionally <em>of</em> '
             'the money. Fake invoicing is the textbook case.',
         opt_why=[
             '<strong>Revoke</strong> cancels something you granted &mdash; a '
             'permit, a licence, a decision. It does not take a person as its '
             'object.',
             'The meaning is right and the pattern is not: you '
             '<strong>swindle</strong> somebody <em>out of</em> something. '
             'With nothing after the object, the sentence stops early.',
             '<strong>Entangle</strong> is physical &mdash; netting, fishing '
             'line, a young otter. A billing fraud tangles nobody.',
             None]),

    dict(pair='physic', correct=1, sib=2,
         stem='A <em>______</em> from the university joined the team to model '
              'how floodwater moves across the restored wetland.',
         options=['programmer', 'physicist', 'physician', 'optician'],
         why='<em>-ist</em> marks the specialist in a field of study. A '
             '<strong>physicist</strong> works on physics &mdash; here, the '
             'physics of moving water.',
         opt_why=[
             'A <strong>programmer</strong> writes the code. Somebody has to '
             'supply the physics the code is modelling.',
             None,
             'A <strong>physician</strong> is a medical doctor. Same stem, '
             '<em>-ian</em> ending, and an entirely different building.',
             'An <strong>optician</strong> tests eyesight and fits glasses. '
             'Another <em>-ian</em>, another practice.']),

    dict(pair='require', correct=0, sib=2,
         stem='The grant application lists several strict <em>______</em> that '
              'smaller conservation groups often struggle to meet.',
         options=['requirements', 'features', 'requirement', 'contributions'],
         why='<em>Several strict</em> forces the plural. '
             '<strong>Requirements</strong> is countable, and the determiner '
             'in front of it decides the form.',
         opt_why=[
             None,
             '<strong>Features</strong> are the distinctive attributes of '
             'something. A landscape has features; an application sets '
             'conditions.',
             'The singular takes a singular determiner: <em>a requirement</em>, '
             '<em>one requirement</em>. <em>Several strict requirement</em> is '
             'not English.',
             'A <strong>contribution</strong> is something given, usually '
             'money or effort. Conditions are met, not donated.']),

    dict(pair='mystery', correct=3, sib=0,
         stem='Local folklore gives the old yew grove a <em>______</em> '
              'quality, said to bring luck to anyone who plants a sapling '
              'there.',
         options=['mysterious', 'fraudulent', 'logical', 'mystical'],
         why='<strong>Mystical</strong> points at the spiritual &mdash; '
             'folklore, luck, ritual. That is what a grove <em>said to bring '
             'luck</em> has.',
         opt_why=[
             '<strong>Mysterious</strong> only means hard to explain. The '
             'folklore here is not puzzling; it is sacred.',
             '<strong>Fraudulent</strong> means obtained by deception. Nothing '
             'in the sentence is dishonest.',
             '<strong>Logical</strong> describes reasoning that follows. Luck '
             'from a sapling is the opposite of that.',
             None]),

    dict(pair='refuse', correct=1, sib=3,
         stem='After a third breach of the site&rsquo;s access rules, the '
              'agency chose to <em>______</em> the contractor&rsquo;s permit '
              'entirely.',
         options=['entangle', 'revoke', 'soothe', 'resist'],
         why='<strong>Revoke</strong> cancels something officially granted. '
             'Its objects are documents and decisions: a permit, a licence, '
             'an offer, consent.',
         opt_why=[
             '<strong>Entangle</strong> means to catch or twist up in '
             'something. A permit is paperwork, not netting.',
             None,
             '<strong>Soothe</strong> is to calm someone or something '
             'distressed. Nobody is calming the permit.',
             '<strong>Resist</strong> takes a force pulling at you &mdash; a '
             'temptation, pressure, an urge. A permit does not pull.']),

    dict(pair='logic', correct=2, sib=3,
         ctx='A <strong>hide</strong> is a small screened shelter that '
             'birdwatchers sit inside so they can watch without being seen.',
         stem='Priya&rsquo;s argument for moving the hide further from the '
              'nest was entirely <em>______</em>, even if it meant a longer '
              'walk for visitors.',
         options=['pithy', 'fraudulent', 'logical', 'legal'],
         why='<strong>Logical</strong> is about reasoning that holds together. '
             'Priya&rsquo;s case follows from what the birds need.',
         opt_why=[
             '<strong>Pithy</strong> would praise how briefly she put it, not '
             'whether the argument works.',
             '<strong>Fraudulent</strong> means obtained by deception. Nobody '
             'has accused Priya of anything.',
             None,
             '<strong>Legal</strong> is about what the law permits. Nobody '
             'suggested moving the hide broke a rule &mdash; only that it '
             'made a longer walk.']),

    dict(pair='stress', correct=3, sib=2,
         stem='Coordinating three field teams during the flood was the most '
              '<em>______</em> week of Elena&rsquo;s career so far.',
         options=['mysterious', 'slick', 'stressy', 'stressful'],
         why='<strong>Stressful</strong> describes the thing that causes the '
             'stress &mdash; a week, a job, a journey, a conversation.',
         opt_why=[
             '<strong>Mysterious</strong> means hard to explain. A hard week '
             'is not a puzzling one.',
             '<strong>Slick</strong> would say the week went smoothly, which '
             'is the opposite of what is meant.',
             '<strong>Stressy</strong> is informal and describes a '
             '<em>person&rsquo;s</em> manner. A week cannot be stressy; the '
             'officer running it can.',
             None]),

    dict(pair='teeth', correct=1, sib=0,
         stem='X-rays showed the trapped fox had fractured a <em>______</em>, '
              'one of the long pointed teeth used for gripping prey.',
         options=['incisor', 'canine', 'premolar', 'molar'],
         why='The <strong>canine</strong> is the long pointed tooth beside the '
             'incisors, enlarged in carnivores &mdash; a fox&rsquo;s gripping '
             'tooth.',
         opt_why=[
             'An <strong>incisor</strong> is a flat, chisel-edged front tooth '
             'for cutting, not gripping.',
             None,
             'A <strong>premolar</strong> sits behind the canine and shears '
             'rather than grips.',
             'A <strong>molar</strong> is a broad back tooth for grinding.']),

    dict(pair='mystery', correct=0, sib=1,
         stem='The sudden disappearance of the otters from the lower river '
              'remains <em>______</em>, and the agency has opened an inquiry.',
         options=['mysterious', 'mystical', 'pithy', 'slick'],
         why='<strong>Mysterious</strong> means hard to explain &mdash; which '
             'is exactly why an inquiry has been opened rather than a service '
             'held.',
         opt_why=[
             None,
             '<strong>Mystical</strong> would claim a spiritual explanation '
             'was intended. An inquiry says the opposite.',
             '<strong>Pithy</strong> describes wording that is short and '
             'forceful. A disappearance has no wording.',
             '<strong>Slick</strong> describes something done smoothly. The '
             'otters did not perform.']),

    dict(pair='logic', correct=2, sib=1,
         ctx='A <strong>cull</strong> is the licensed killing of part of a '
             'wild population, usually to control disease or numbers.',
         stem='Before the cull could go ahead, the agency needed '
              '<em>______</em> confirmation that the licence covered this '
              'specific site.',
         options=['fraudulent', 'logical', 'legal', 'mystical'],
         why='<strong>Legal</strong> here means <em>relating to the law</em>, '
             'not merely allowed: what is wanted is confirmation from lawyers '
             'about what the licence covers.',
         opt_why=[
             '<strong>Fraudulent</strong> means obtained by deception. The '
             'agency is asking for confirmation, not forging it.',
             '<strong>Logical</strong> is about reasoning. A licence is '
             'settled by a statute, not by an argument.',
             None,
             '<strong>Mystical</strong> belongs to folklore and ritual, not '
             'to a licensing question.']),

    dict(pair='physic', correct=1, sib=0,
         stem='The reserve keeps a list of the nearest <em>______</em> in case '
              'a ranger is injured on site.',
         options=['physicist', 'physician', 'optician', 'programmer'],
         why='A <strong>physician</strong> is a medical doctor. The '
             '<em>-ian</em> ending marks the practitioner of a practice: '
             'physician, optician, technician.',
         opt_why=[
             'A <strong>physicist</strong> studies physics. Same stem, '
             '<em>-ist</em> ending, and no use at all to an injured ranger.',
             None,
             'An <strong>optician</strong> fits glasses. Right ending, wrong '
             'emergency.',
             'A <strong>programmer</strong> writes software. The '
             '<em>-er</em> ending names a doer, not a doctor.']),

    dict(pair='fraud', correct=3, sib=1,
         stem='The elderly landowner realised too late that the so-called '
              '&lsquo;carbon consultant&rsquo; had tried to <em>______</em> '
              'him out of his grant money.',
         options=['soothe', 'defraud', 'entangle', 'swindle'],
         why='<em>Out of</em> is the giveaway. <strong>Swindle somebody out of '
             'something</strong> is a fixed pattern, and the money is what '
             'follows <em>out of</em>.',
         opt_why=[
             '<strong>Soothe</strong> means to calm someone. The consultant '
             'was not calming anybody.',
             '<strong>Defraud</strong> is the same crime in a different '
             'frame: <em>defraud somebody of something</em>, never <em>out '
             'of</em>.',
             '<strong>Entangle</strong> is physical. Grant money does not '
             'tangle.',
             None]),

    dict(pair='offence', correct=2, sib=1,
         stem='Removing eggs from a protected nest is a criminal '
              '<em>______</em> under the Wildlife and Countryside Act.',
         options=['requirement', 'offender', 'offence', 'contribution'],
         why='An <strong>offence</strong> is the act. Note the spelling: '
             '<em>offence</em> in British English, <em>offense</em> in '
             'American &mdash; while <em>offender</em> is the same on both '
             'sides.',
         opt_why=[
             'A <strong>requirement</strong> is a condition you must meet. '
             'The sentence is describing a crime, not a condition.',
             'An <strong>offender</strong> is the person. This would turn the '
             'act of removing eggs into a human being.',
             None,
             'A <strong>contribution</strong> is something given. Nothing is '
             'being donated here.']),

    dict(pair='refuse', correct=0, sib=1,
         stem='Rangers are trained to <em>______</em> the temptation to feed '
              'wildlife directly, however tame the animals seem.',
         options=['resist', 'revoke', 'entangle', 'memorise'],
         why='<strong>Resist</strong> takes something pulling at you: a '
             'temptation, pressure, an urge, arrest.',
         opt_why=[
             None,
             '<strong>Revoke</strong> cancels something granted. Nobody '
             'issued the ranger a temptation.',
             '<strong>Entangle</strong> means to catch up in something. The '
             'ranger is not being wrapped in anything.',
             '<strong>Memorise</strong> is to learn by heart. A temptation is '
             'felt, not learned.']),

    dict(pair='require', correct=3, sib=0,
         stem='Submitting a habitat survey is now a formal <em>______</em> '
              'before any building permit near the reserve can be approved.',
         options=['requirements', 'features', 'value', 'requirement'],
         why='<em>A formal</em> &mdash; a singular determiner takes the '
             'singular noun. One condition, named once.',
         opt_why=[
             'The plural needs a plural determiner: <em>several '
             'requirements</em>, <em>the requirements</em>. <em>A formal '
             'requirements</em> mixes the two.',
             '<strong>Features</strong> are distinctive attributes. A planning '
             'condition is not an attribute of the landscape.',
             '<strong>Value</strong> is worth expressed as a figure. Nothing '
             'is being priced here.',
             None]),
]

# ── SECTION 2 — seventeen gaps, every one with accepted alternatives ───
# The section this replaces had no alternatives array at all: eleven of the
# seventeen keys rejected fully correct English, including `prefers`, which
# is standard British collective-noun agreement and the very rule the item
# is built on.
G = {}
G['cleavage'] = (
    'The geologist pointed out the natural ______ in the slate, where the '
    'rock splits cleanly along parallel planes.',
    ['cleavage|cleavages|foliation'],
    '<strong>Cleavage</strong> is a sharp division or split; in geology it is '
    'the tendency of a rock to break along flat parallel planes. '
    '<em>Foliation</em> is the geologist&rsquo;s wider term for the same '
    'fabric and is accepted here.')
G['account'] = (
    'Elena reminded the panel to take the drought forecast ______ before '
    'approving the irrigation plan.',
    ['into account|into consideration|on board'],
    'Four ways to say it, all usable in a briefing: <strong>take into '
    'account</strong>, <em>take into consideration</em>, <em>bear in '
    'mind</em>, <em>factor in</em>. Only <em>bear in mind</em> changes the '
    'verb, so it will not fit this gap.')
G['lectern'] = (
    'Director Bergmann set her notes on the ______ and began the annual '
    'funding briefing.',
    ['lectern|podium|rostrum|reading desk'],
    'A <strong>lectern</strong> is the stand the notes sit on. Strictly a '
    '<em>podium</em> is the raised platform the speaker stands on, but the '
    'two have merged in most English and both are accepted.')
G['rotunda'] = (
    'The exhibition on wetland birds is displayed inside the museum&rsquo;s '
    'domed ______.',
    ['rotunda|rotundas|round room'],
    'A <strong>rotunda</strong> is a round building or room, usually domed. '
    'The word is architectural: you will meet it on a floor plan far more '
    'often than in speech.')
G['soothe'] = (
    'Priya spoke in a low, steady voice to ______ the panicked swan before '
    'untangling it from the fishing line.',
    ['soothe|calm|quieten|settle'],
    '<strong>Soothe</strong> collocates with what hurts or frightens: soothe '
    'a burn, soothe a child, soothe nerves. <em>Calm</em> and <em>settle</em> '
    'do the same job here and are accepted.')
G['entangle'] = (
    'Loose netting left on the riverbank can easily ______ young otters.',
    ['entangle|trap|ensnare|tangle|snag|catch'],
    '<strong>Entangle</strong> is the word conservation reports use for '
    'wildlife caught in gear &mdash; hence <em>entanglement</em>, the noun on '
    'every incident form.')
G['gossip'] = (
    'By lunchtime, ______ about the surprise inspection had spread through '
    'every department in the building.',
    ['gossip|rumour|rumours|word|talk'],
    '<strong>Gossip</strong> is uncountable: <em>a lot of gossip</em>, never '
    '<em>a gossip</em> about something. It is also staff-room register &mdash; '
    'a report would say <em>unconfirmed reports</em>.')
G['value'] = (
    'The report tried to put a monetary ______ on the flood protection the '
    'wetlands provide each year.',
    ['value|worth|price|figure'],
    '<strong>Put a value on</strong> something is the fixed phrase. Note the '
    'preposition: a value is put <em>on</em> a thing, never <em>to</em> it.')
G['praise'] = (
    'The minister&rsquo;s visit ended with public ______ for the team&rsquo;s '
    'work on the otter reintroduction.',
    ['praise|recognition|acclaim|commendation'],
    '<strong>Praise</strong> is uncountable and takes <em>for</em>: '
    '<em>praise for the team</em>. <em>Commendation</em> is the formal '
    'equivalent and is what would appear in the minutes.')
G['grumble'] = (
    'A few of the older rangers still ______ about the new digital reporting '
    'system, though most have adapted by now.',
    ['grumble|complain|moan|grouse|gripe'],
    '<strong>Grumble</strong> is low-level and continuous rather than formal: '
    'you grumble <em>about</em> something. Lodging a complaint is a different '
    'act, and a different register.')
G['prefer'] = (
    'Given the choice, most of the survey team ______ early starts to avoid '
    'the midday heat.',
    ['prefer|prefers|favour|favours'],
    'Both verb forms are correct. British English lets a collective noun take '
    'a plural verb when you mean the individuals &mdash; <em>the team '
    'prefer</em> &mdash; and a singular when you mean the unit. Note also '
    '<strong>prefer A to B</strong>, never <em>prefer A than B</em>.')
G['gig'] = (
    'Tomas plays bass in a local band and had a ______ the same night as the '
    'reserve&rsquo;s open evening.',
    ['gig|concert|show|booking|performance'],
    '<strong>Gig</strong> is informal and has spread well beyond music: a '
    'freelancer talks about <em>gigs</em> and the <em>gig economy</em>. In a '
    'written report it would be <em>a performance</em> or <em>a booking</em>.')
G['optician'] = (
    'After struggling to read the tiny print on the survey forms, Tomas '
    'finally booked an appointment with the ______.',
    ['optician|optometrist|opticians'],
    'In the UK the high-street <strong>optician</strong> both tests eyes and '
    'fits glasses; <em>optometrist</em> is the precise term for the one who '
    'tests, and is accepted. Compare the <em>-ian</em> family: physician, '
    'technician.')
G['wheelchair'] = (
    'The new boardwalk was widened so that visitors using a ______ could '
    'reach the bird hide without difficulty.',
    ['wheelchair|wheelchairs'],
    'One word, no hyphen. The preposition matters in reports: a visitor '
    '<em>uses</em> or <em>is in</em> a <strong>wheelchair</strong> &mdash; '
    '<em>confined to</em> is dated and is avoided in agency writing.')
G['roundabout'] = (
    'Turn left at the ______ just past the visitor centre, and the car park '
    'is on your right.',
    ['roundabout|mini-roundabout|junction'],
    '<strong>Roundabout</strong> is British; American English says '
    '<em>traffic circle</em> or <em>rotary</em>. As an adjective the same '
    'word means indirect: <em>a roundabout way of saying it</em>.')
G['people'] = (
    'Nobody would call Tomas a ______ &mdash; he would rather spend the day '
    'alone counting reed warblers than lead a school tour.',
    ['people person|people-person|social animal'],
    'A <strong>people person</strong> is fixed and always plural in its first '
    'half: never <em>a person person</em>. Informal, like most compliments '
    'about personality.')
G['features'] = (
    'The site survey noted several unusual landscape ______, including an old '
    'sand pit now used by nesting sand martins.',
    ['features|attributes|elements|characteristics'],
    '<strong>Features</strong> are the distinctive parts of something: '
    '<em>landscape features</em>, <em>design features</em>. Note the sand pit '
    '&mdash; sand martins dig their tunnels into soft sand and fine gravel, '
    'which is why a colony turns up in a worked-out pit and never in hard '
    'rock.')

# ── SECTION 3 — sixteen field terms, sorted by sense ───────────────────
# `sort` scores the first placement only, so this section can be lost.
S3_REF = [
    ('s3a', 'Sixteen field terms &mdash; 1 of 4', [
        ('ignite', 'to catch fire, or to set something alight &mdash; '
                   '<em>dry reed will ignite in seconds</em>'),
        ('matchstick', 'the wooden stem of a match &mdash; <em>the sapling '
                       'snapped like a matchstick</em>'),
        ('crane', 'the tall grey bird, <em>Grus grus</em> &mdash; and, off '
                  'the reserve, the lifting machine'),
        ('flock', 'a group of birds of one kind together &mdash; <em>a flock '
                  'of lapwings over the marsh</em>')]),
    ('s3b', 'Sixteen field terms &mdash; 2 of 4', [
        ('survey', 'to examine and record an area &mdash; <em>the site survey '
                   'noted several features</em>'),
        ('density', 'how tightly packed something is &mdash; <em>nest density '
                    'fell by a third</em>'),
        ('memorise', 'to learn something by heart &mdash; <em>rangers '
                     'memorise the byelaw numbers</em>'),
        ('philosophers', 'people who study philosophy &mdash; <em>the '
                         'philosophers of the Enlightenment</em>')]),
    ('s3c', 'Sixteen field terms &mdash; 3 of 4', [
        ('opposite', 'on the other side of something, facing it &mdash; '
                     '<em>the hide is opposite the reed bed</em>'),
        ('removed', 'of a cousin: separated by so many generations &mdash; '
                    '<em>a first cousin once removed</em>'),
        ('fraudulent', 'obtained or done by deception &mdash; <em>a '
                       'fraudulent expenses claim</em>'),
        ('slick', 'smoothly and efficiently done, sometimes too smoothly '
                  '&mdash; <em>a slick presentation</em>')]),
    ('s3d', 'Sixteen field terms &mdash; 4 of 4', [
        ('spark', 'a small fiery particle &mdash; and, as a verb, to trigger: '
                  '<em>it sparked an inquiry</em>'),
        ('pithy', 'short, and forceful with it &mdash; <em>a pithy summary of '
                  'the objection</em>'),
        ('destiny', 'what the future holds for someone &mdash; <em>the '
                    'destiny of the reserve</em>'),
        ('ebb and flow', 'a repeating pattern of decline and growth &mdash; '
                         '<em>the ebb and flow of visitor numbers</em>')]),
]

S3_SORTS = [
    ('s3s1', 'Which field does the word belong to?',
     ['Fire and burning', 'Birds', 'Ground and measurement'],
     [('ignite', 0), ('matchstick', 0), ('crane', 1), ('flock', 1),
      ('survey', 2), ('density', 2)],
     'On a reserve, <strong>crane</strong> is the bird long before it is the '
     'machine &mdash; <em>Grus grus</em>, one of Europe&rsquo;s conservation '
     'successes &mdash; and a <strong>flock</strong> of them is what you '
     'count. <strong>Survey</strong> and <strong>density</strong> are both '
     'measurement: you survey a site, then report the density of nests in it.'),
    ('s3s2', 'Which field does the word belong to?',
     ['The mind', 'Position and relation', 'Deception'],
     [('memorise', 0), ('philosophers', 0), ('opposite', 1), ('removed', 1),
      ('fraudulent', 2), ('slick', 2)],
     '<strong>Removed</strong> is a relation word, not a movement word: '
     '<em>a first cousin once removed</em> is a step down the family tree. '
     '<strong>Slick</strong> sits with <strong>fraudulent</strong> because '
     'its edge is suspicion &mdash; a slick operator is smooth enough to '
     'worry you.'),
    ('s3s3', 'Short and sudden, or slow and repeating?',
     ['Short and sudden', 'Slow and repeating'],
     [('spark', 0), ('pithy', 0), ('destiny', 1), ('ebb and flow', 1)],
     '<strong>Spark</strong> and <strong>pithy</strong> are both about brevity '
     'with force behind it &mdash; a spark starts something, a pithy remark '
     'lands. <strong>Destiny</strong> and <strong>ebb and flow</strong> both '
     'look along a long timeline, one towards a fixed end and one round a '
     'cycle.'),
]


def build():
    D.assert_no_key_is_longest(S1, 'Section 1')
    key_spread, sib_spread = assert_key_is_deranged(S1, 'Section 1')
    assert_pairs_are_separated(S1, 4, 'Section 1')

    logo = D.logo_from(TPL)
    S = [D.cover(logo, 'The Wildlife and <em>Countryside</em> Agency',
                 'Vocabulary in the field, Part 2 — eight confusable pairs, '
                 'seventeen briefings and sixteen terms',
                 [('Level', 'C1 &middot; Part 2 of 2'),
                  ('Focus', 'Word choice &amp; register'),
                  ('Count', 'NN slides')])]

    # ── front matter: the setting, the prerequisite, the jargon ──
    S += [D.teach('b1E', 'Before you begin', 'b1T', 'Six weeks in',
                  [('b1ah', 'Where you are',
                    'Elena Voss is a field officer at the Wildlife and '
                    'Countryside Agency. She has sat in on a fraud '
                    'investigation, learned which permits can be revoked, and '
                    'discovered that Tomas would rather count reed warblers '
                    'than make small talk.',
                    None, None),
                   ('b1bh', 'Part 1 comes first',
                    'This is the second half of a two-part set. Part 1 teaches '
                    'the words that turn up here as wrong options &mdash; '
                    '<em>reconcile</em>, <em>prevalent</em>, <em>ersatz</em>, '
                    '<em>assessor</em>, <em>domineering</em> and eight more.',
                    'b1bn', 'You can take this part on its own, but you will '
                    'be choosing between a word you have been taught and a '
                    'word you have not. Part 1 removes that guesswork.')],
                  folder=F, bg=BG3)]

    # One card in a two-column grid, so the right half of the slide stays
    # clear and the hide in the artwork is actually visible next to its own
    # definition. The image is mirrored for this: the structure was on the
    # left, exactly where the card sits, and the tree that came with it was
    # sitting behind the title.
    S += [D.teach('bhE', 'Before you begin', 'bhT',
                  'The hide',
                  [(None, 'a noun, not a verb',
                    'A <strong>hide</strong> is a small screened shelter that '
                    'birdwatchers sit inside so they can watch without being '
                    'seen &mdash; often a timber box on stilts at the edge of '
                    'the water, with shutters to look through. Later on you '
                    'will read about <em>moving the hide further from the '
                    'nest</em>. That is this building being moved, not anyone '
                    'concealing anything.', None, None)],
                  cols='1fr 1fr', folder=F, bg=BG4)]

    S += [D.teach('b2E', 'Before you begin', 'b2T',
                  'Four words the briefings assume you know',
                  [(None, 'the hide',
                    'a small screened shelter that birdwatchers sit inside so '
                    'they can watch without being seen &mdash; a noun here, '
                    'never the verb', None, None),
                   (None, 'a cull',
                    'the licensed killing of part of a wild population, '
                    'usually to control disease or numbers', None, None),
                   (None, 'a byelaw',
                    'a local rule made by a council or other public body and '
                    'enforceable inside its own area', None, None),
                   (None, 'a sand martin',
                    'a small brown-and-white migrant that digs nest tunnels '
                    'into soft vertical sand faces, often in worked-out pits',
                    'b2n', 'All four appear inside question stems later on. '
                    'They are glossed here so that no item is testing whether '
                    'you happen to know the jargon.')],
                  cols='1fr 1fr', folder=F, bg=BG3)]

    # ── fourteen teaching slides ──
    TP = ('tpE', 'Confusable pairs')
    TF = ('tfE', 'Field language')
    S += [
        D.teach(TP[0], TP[1], 't1T', 'Three questions that separate a pair',
                [('t1ah', '1 &middot; What does it go with?',
                  'You <strong>revoke</strong> a permit. You '
                  '<strong>resist</strong> a temptation. Neither verb will '
                  'take the other&rsquo;s object.', None, None),
                 ('t1bh', '2 &middot; What follows it?',
                  '<strong>defraud</strong> sb <em>of</em> sth &middot; '
                  '<strong>swindle</strong> sb <em>out of</em> sth', None, None),
                 ('t1ch', '3 &middot; Who says it?',
                  '<em>stressy</em>, <em>a gig</em>, <em>a grumble</em> &mdash; '
                  'spoken. <em>anxious</em>, <em>a performance</em>, <em>a '
                  'concern</em> &mdash; written.',
                  't1cn', 'Every pair ahead yields to one of these three. Ask '
                  'them in order: what it goes with, what follows it, who '
                  'says it.')], folder=F),

        D.teach(TP[0], TP[1], 't2T', 'stressy / stressful',
                [(None, 'stressy',
                  'informal, and about a <strong>person&rsquo;s manner</strong>: '
                  '<em>don&rsquo;t be so stressy about it</em>', None, None),
                 (None, 'stressful',
                  'about the <strong>situation</strong> that causes it: '
                  '<em>the most stressful week of her career</em>',
                  't2n', 'This pair turns on register as much as sense. '
                  '<em>Stressy</em> belongs in the staff room; a written '
                  'report says <em>anxious</em>.')], folder=F),

        D.teach(TP[0], TP[1], 't3T', 'physician / physicist',
                [('t3ah', '-ian &rarr; the practitioner',
                  'phys<strong>ician</strong> &middot; opt<strong>ician</strong> '
                  '&middot; techn<strong>ician</strong>', None, None),
                 ('t3bh', '-ist &rarr; the specialist, -er &rarr; the doer',
                  'phys<strong>icist</strong> &middot; biolog<strong>ist</strong> '
                  '&nbsp;|&nbsp; programm<strong>er</strong> &middot; '
                  'offend<strong>er</strong> &middot; assess<strong>or</strong>',
                  't3n', 'All three endings name a <em>person</em>, so the '
                  'ending alone will not choose for you &mdash; but it does '
                  'tell you the option is a person and not an act. A physician '
                  'treats you; a physicist models your floodwater.')],
                folder=F),

        D.teach(TP[0], TP[1], 't4T', 'offence / offender',
                [('t4ah', 'the act',
                  'a criminal <strong>offence</strong> &middot; to commit an '
                  'offence &middot; an offence under the Act', None, None),
                 ('t4bh', 'the person',
                  'a repeat <strong>offender</strong> &middot; first-time '
                  'offenders &middot; offenders face steeper fines',
                  't4n', 'British English spells the act <em>offence</em>; '
                  'American English spells it <em>offense</em>. The person is '
                  '<em>offender</em> on both sides of the Atlantic. This '
                  'lesson is British throughout.')], folder=F),

        D.teach(TP[0], TP[1], 't5T', 'mystical / mysterious',
                [(None, 'mystical',
                  'spiritual, sacred, beyond ordinary explanation: <em>a '
                  'mystical quality</em>, <em>mystical traditions</em>',
                  None, None),
                 (None, 'mysterious',
                  'simply hard to explain: <em>a mysterious '
                  'disappearance</em>, <em>a mysterious phone call</em>',
                  't5n', 'A quick test. If somebody has opened an inquiry, the '
                  'thing is <em>mysterious</em>. If somebody has lit a candle, '
                  'it is <em>mystical</em>.')], folder=F),

        D.teach(TP[0], TP[1], 't6T', 'defraud / swindle &mdash; what follows',
                [(None, 'defraud sb (of sth)',
                  '<em>They tried to <strong>defraud</strong> the agency.</em> '
                  '&middot; <em>He <strong>defrauded</strong> her <strong>of'
                  '</strong> £40,000.</em>', None, None),
                 (None, 'swindle sb out of sth',
                  '<em>He tried to <strong>swindle</strong> the landowner '
                  '<strong>out of</strong> his grant.</em> Never <em>swindle '
                  'him of</em>.',
                  't6n', 'Same crime, different frame. <em>Out of</em> is the '
                  'single most reliable signal that <em>swindle</em> is the '
                  'verb wanted: it is the pattern that decides, not the '
                  'meaning.')], folder=F),

        D.teach(TP[0], TP[1], 't7T', 'One root, four slots',
                [(None, 'verb',
                  '<strong>defraud</strong> &mdash; <em>to defraud the '
                  'agency</em>', None, None),
                 (None, 'noun',
                  '<strong>fraud</strong> &mdash; <em>a fraud '
                  'investigation</em>; <strong>fraudster</strong> &mdash; the '
                  'person', None, None),
                 (None, 'adjective',
                  '<strong>fraudulent</strong> &mdash; <em>a fraudulent '
                  'claim</em>, <em>fraudulently obtained</em>',
                  't7n', 'The verb, the noun and the adjective are each '
                  'tested in a different section of this lesson. Knowing the '
                  'family lets you move between them inside a sentence '
                  'instead of reaching for the one form you remember.')],
                folder=F),

        D.teach(TP[0], TP[1], 't8T', 'legal / logical',
                [(None, 'legal',
                  'to do with the law: <em>legal advice</em>, <em>legal '
                  'confirmation</em>, <em>a legal requirement</em>',
                  None, None),
                 (None, 'logical',
                  'to do with reasoning: <em>a logical argument</em>, <em>the '
                  'logical next step</em>',
                  't8n', 'A decision can be legal and not logical, or logical '
                  'and not legal. Ask which authority the sentence is '
                  'appealing to: a statute, or an argument.')], folder=F),

        D.teach(TP[0], TP[1], 't9T', 'a requirement / several requirements',
                [('t9ah', 'the determiner decides',
                  '<em><strong>a</strong> formal requirement</em> &middot; '
                  '<em>several strict <strong>requirements</strong></em>',
                  None, None),
                 ('t9bh', 'and a collective noun takes either',
                  '<em>the survey team <strong>prefer</strong> early '
                  'starts</em> &middot; <em>the team <strong>is</strong> '
                  'small</em>',
                  't9n', 'British English lets a collective noun take a plural '
                  'verb when you mean the individuals in it &mdash; <em>the '
                  'team prefer</em>, <em>the panel disagree</em>, <em>the '
                  'government are divided</em>. Both forms are correct; the '
                  'meaning shifts.')], folder=F),

        D.teach(TP[0], TP[1], 't10T', 'revoke / resist',
                [('t10ah', 'revoke + something you granted',
                  'a permit &middot; a licence &middot; consent &middot; an '
                  'offer &middot; a decision', None, None),
                 ('t10bh', 'resist + something pulling at you',
                  'a temptation &middot; pressure &middot; the urge to help '
                  '&middot; arrest &middot; change',
                  't10n', 'Two verbs of refusal separated entirely by what '
                  'follows them. Nothing grants you a temptation, and no '
                  'permit pulls.')], folder=F),

        D.teach(TF[0], TF[1], 't11T', 'Report English and staff-room English',
                [('t11ah', 'in the staff room',
                  '<em>stressy</em> &middot; <em>a gig</em> &middot; '
                  '<em>gossip</em> &middot; <em>grumble</em> &middot; <em>a '
                  'people person</em> &middot; <em>slick</em>', None, None),
                 ('t11bh', 'in the written report',
                  '<em>anxious</em> &middot; <em>a performance</em> &middot; '
                  '<em>unconfirmed reports</em> &middot; <em>raise '
                  'concerns</em> &middot; <em>works well with the public</em> '
                  '&middot; <em>efficient</em>',
                  't11n', 'Nothing in the left-hand column is wrong English. '
                  'All of it is wrong in a document a landowner&rsquo;s '
                  'solicitor may read. Knowing a word is not the same as '
                  'knowing where it goes.')], folder=F),

        D.teach(TF[0], TF[1], 't12T', 'Four teeth, front to back',
                [(None, 'incisor',
                  'flat and chisel-edged, at the front &mdash; for cutting',
                  None, None),
                 (None, 'canine',
                  'long and pointed, beside the incisors &mdash; for gripping '
                  'and tearing', None, None),
                 (None, 'premolar',
                  'behind the canine &mdash; for holding and shearing',
                  None, None),
                 (None, 'molar',
                  'broad, at the back &mdash; for grinding',
                  't12n', 'Carnivores carry the enlarged canine, which is the '
                  'tooth the trapped fox had fractured. Three of these four '
                  'turn up as wrong options and are worth knowing on sight.')],
                cols='1fr 1fr', folder=F),

        D.teach(TF[0], TF[1], 't13T', 'crane, flock, survey',
                [(None, 'crane',
                  'first the <strong>bird</strong>: <em>Grus grus</em>, tall, '
                  'grey and trumpeting. Then, off the reserve, the lifting '
                  'machine.', None, None),
                 (None, 'flock',
                  'a group of birds of one kind, feeding or travelling '
                  'together: <em>a flock of forty cranes</em>', None, None),
                 (None, 'survey',
                  'to examine and record an area: <em>a habitat survey</em>, '
                  '<em>the site survey noted several features</em>',
                  't13n', 'Two of these have a second meaning that arrives '
                  'first for most learners &mdash; the machine, and land '
                  'measurement. On a reserve it is the bird and the habitat '
                  'sense that are in use.')], folder=F),

        D.teach(TF[0], TF[1], 't14T', 'Taking it into account',
                [('t14ah', 'four ways to say it',
                  'take sth <strong>into account</strong> &middot; take sth '
                  '<strong>into consideration</strong> &middot; '
                  '<strong>bear</strong> sth <strong>in mind</strong> &middot; '
                  '<strong>factor</strong> sth <strong>in</strong>',
                  None, None),
                 ('t14bh', 'spark and ignite',
                  '<strong>spark</strong> (n) a fiery particle; (v) to '
                  'trigger: <em>the disappearance sparked an inquiry</em>. '
                  '<strong>ignite</strong>: to catch fire, or to set alight.',
                  't14n', 'The four phrases on the left are interchangeable in '
                  'a briefing. <em>Spark</em> is the one that has quietly '
                  'become a verb about causes rather than about fire &mdash; '
                  'and that is now its commonest use in a report.')],
                folder=F),
    ]

    # ── Section 1 ──
    S += [D.teach('d1E', 'Section 1 of 3', 'd1T', 'Word choice',
                  [(None, 'Seventeen sentences from Elena&rsquo;s six weeks, '
                    'each missing one word.',
                    'Eight of the pairs you have just seen are tested here, '
                    'from both directions. For each item, ask the three '
                    'questions in order: what does the word go with, what '
                    'follows it, and who is speaking?',
                    'd1n', 'The options are shuffled every time the deck '
                    'loads, so the letters mean nothing. Read all four before '
                    'you choose.')], folder=F, bg=BG2)]
    S += [mc_slide(i + 1, len(S1), q, 's1E', 'Section 1 &middot; Word choice',
                   's1T', 'Choose the word that fits', folder=F,
                   ctx=q.get('ctx'))
          for i, q in enumerate(S1)]

    # ── Section 2 ──
    S += [D.teach('d2E', 'Section 2 of 3', 'd2T', 'Complete the briefing',
                  [(None, 'Seventeen gaps, typed from memory.',
                    'Each gap accepts every answer that is genuinely correct '
                    'English, not one string. Where two words do the same job '
                    'here, both are marked right.',
                    'd2n', 'The line above each sentence gives you the sense '
                    'and the length. Press Enter, or use Check, to mark the '
                    'slide.')], folder=F, bg=BG2)]

    GAPS = [
        ('g1', [G['cleavage']], 'g1h',
         'A sharp division or split, used of rock structure &mdash; 8 letters, '
         'begins with c.', 200),
        ('g2', [G['account']], 'g2h',
         'Two words completing the idiom &ldquo;to consider something alongside '
         'other factors&rdquo;.', 250),
        ('g3', [G['lectern'], G['rotunda']], 'g3h',
         'First: a tall stand with a sloping top for a speaker&rsquo;s notes '
         '&mdash; 7 letters. Second: a round, domed room &mdash; 7 letters, '
         'begins with r.', 200),
        ('g4', [G['soothe'], G['entangle']], 'g4h',
         'First: to gently calm a frightened animal &mdash; 6 letters, begins '
         'with s. Second: to catch and twist something up in something else '
         '&mdash; 8 letters.', 200),
        ('g5', [G['gossip'], G['value']], 'g5h',
         'First: casual, unconfirmed talk about other people &mdash; 6 letters. '
         'Second: what something is worth, as a figure &mdash; 5 letters.', 200),
        ('g6', [G['praise'], G['grumble']], 'g6h',
         'First: warm approval expressed openly &mdash; 6 letters. Second: to '
         'complain in a low-level, bad-tempered way &mdash; 7 letters.', 200),
        ('g7', [G['prefer'], G['gig']], 'g7h',
         'First: to like one option better than another &mdash; watch the '
         'agreement after a collective noun. Second: informal &mdash; a public '
         'performance, 3 letters.', 200),
        ('g8', [G['optician']], 'g8h',
         'The high-street professional who tests eyesight and fits glasses '
         '&mdash; 8 letters, and one of the <em>-ian</em> family.', 220),
        ('g9', [G['wheelchair']], 'g9h',
         'A chair fitted with wheels, used by people who cannot walk unaided '
         '&mdash; one word, 10 letters.', 220),
        ('g10', [G['roundabout']], 'g10h',
         'A road junction where traffic circles a central island &mdash; 10 '
         'letters, and thoroughly British.', 220),
        ('g11', [G['people']], 'g11h',
         'A two-word phrase for somebody who enjoys and is good at dealing '
         'with others.', 250),
        ('g12', [G['features']], 'g12h',
         'The distinctive parts or aspects of something &mdash; plural noun, '
         '8 letters.', 220),
    ]
    total_g = len(GAPS)
    for n, (key, rows, hk, hint, width) in enumerate(GAPS, 1):
        S += [D.gap(n, total_g, rows, None, 's2E',
                    'Section 2 &middot; Complete the briefing', 's2T',
                    'Type the missing word', folder=F, hint=hint, hint_key=hk,
                    width=width, size=18)]

    # ── Section 3 ──
    S += [D.teach('d3E', 'Section 3 of 3', 'd3T', 'Sixteen field terms',
                  [(None, 'Read the sixteen, then sort them by sense.',
                    'Each term is glossed with an example on the four slides '
                    'that follow. After that you place every word in the box '
                    'its meaning belongs to.',
                    'd3n', 'The first box you choose for a word is the one '
                    'that scores. Put it in the wrong box and the point is '
                    'gone, so read before you place.')], folder=F, bg=BG2)]
    for key, title, cards in S3_REF:
        S += [D.teach('s3rE', 'Section 3 &middot; The terms', key + 'T', title,
                      [(None, w, d, None, None) for w, d in cards],
                      cols='1fr 1fr', folder=F)]

    # The authored order of the chips is shuffled with a fixed seed so that
    # the source never prints the sixteen terms in the order the reference
    # slides introduce them. The engine shuffles again at runtime.
    rng = random.Random(11)
    for key, title, bins, items, why in S3_SORTS:
        shuffled = items[:]
        rng.shuffle(shuffled)
        S += [D.sort_slide(bins, shuffled, 's3E', 'Section 3 &middot; Sort by '
                           'sense', key + 'T', title, key + 'h',
                           'Click a word, then click the box it belongs in. '
                           'The first box you choose is the one that counts.',
                           why, folder=F)]

    # ── results and activation ──
    S += [D.results(),
          D.activate('The permit letter', 'Use at least four:',
                     ['take into account', 'swindle sb out of sth',
                      'revoke a permit', 'a criminal offence',
                      'resist the temptation', 'a habitat survey',
                      'bear in mind', 'a repeat offender'],
                     'Discussion &middot; in pairs',
                     'A landowner has just been told his access permit is '
                     'being revoked after a third breach.',
                     ['One of you is the field officer. Deliver the decision, '
                      'name the byelaw and hold the line when he pushes back.',
                      'Swap roles. This time the landowner says a consultant '
                      'swindled him out of the grant that paid for the work. '
                      'Take that into account &mdash; without reversing the '
                      'decision.',
                      'Both: your draft newsletter says the team were '
                      '<em>stressy</em> about the inspection and that Tomas '
                      'had a <em>gig</em>. Argue the register, item by item, '
                      'and agree a written version.'],
                     'Writing &middot; 150&ndash;250 words',
                     'Write the site note that goes to the landowner&rsquo;s '
                     'solicitor: what the breach was, which byelaw applies, '
                     'and what happens next. Report register throughout '
                     '&mdash; nothing from the staff room.',
                     'Following the site visit of 14 March, the Agency has '
                     'revoked …')]
    return S, key_spread, sib_spread


if __name__ == '__main__':
    import i18n_nature2

    slides, key_spread, sib_spread = build()
    body = "".join(slides)
    # The loch behind the results slide — the calmest of the three, and the
    # score ring needs the quietest background in the deck.
    body = body.replace('<section class="slide" data-type="results">',
                        '<section class="slide" data-type="results" '
                        'data-bg="%s/%s">' % (F, BG3), 1)
    # The wider shore behind the activation stage.
    body = body.replace('<section class="slide" data-type="activate">',
                        '<section class="slide" data-type="activate" '
                        'data-bg="%s/%s">' % (F, BG5), 1)
    n = body.count('<section class="slide')
    body = body.replace('NN slides', '%d slides' % n)
    i18n_nature2.T['en']['chipCount'] = '%d slides' % n
    i18n_nature2.T['de']['chipCount'] = '%d Folien' % n

    s = D.assemble(TPL, OUT, body, PALETTE,
                   'Wildlife and Countryside Agency — Vocabulary, Part 2',
                   i18n_nature2)
    s = s.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)
    s = s.replace('</style>\n</head>', CSS + '</style>\n</head>', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes, %d slides' % (OUT, len(s), n))
    print('Section 1 key positions A/B/C/D: %s' % key_spread)
    print('Section 1 sibling offset from key (+1/+2/+3): %s' % sib_spread)
