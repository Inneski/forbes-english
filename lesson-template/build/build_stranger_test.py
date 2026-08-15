# -*- coding: utf-8 -*-
"""Stranger Things — the English test (A2–B1), rebuilt as a 16:9 deck.

Two files became one. `stranger-things-test.html` was a 22-item
autograded page; `stranger-things-test-german.html` was a printable
worksheet covering the same material with German prompts. They taught the
same words and the same three grammar points, one on screen and one on
paper, and neither was complete on its own: the screen version had no
teaching stage and no explanations, the paper version had the L1 → English
translation task that is the most valuable thing in either of them. The
deck keeps the union. The German file is retired to a redirect stub so
existing links still land; nothing learner-facing refers to either.

**The central problem: an L1 → English task has to translate.**
Everywhere else on this site the rule is that the English being taught
stays English in every language. Part 2 is the exception, and it has to
be: the task is "here is a word in your language, write the English", so
the *prompt* is content and the answer is the target. The prompts are the
ten `v*p` keys in `i18n_stranger_test.py` and they switch with the
selector — German sees `der Herbst`, Spanish `el otoño`. The answer is
the English word in all three.

**How the English case is handled.** "Translate into English" has no L1
for an English speaker, so the English layer substitutes the nearest
honest equivalent: a definition or picture-clue that identifies the word
without naming it — *"the season between summer and winter, when the
woods turn orange"* for **autumn**, *"you roll a heavy ball down a lane
to knock over ten pins"* for **bowling alley**. The learner still
produces the word from meaning; only the route to the meaning changes.
`assert_no_answer_is_shown` checks every clue against every accepted
answer *on its own slide*, in all three languages, so a clue can leak
neither the word it asks for nor its neighbour's. That check caught the
German prompt for the roller disco, which is the loanword *die
Rollerdisco* and handed the answer over intact; the prompt is now the
native compound *die Rollschuhdisco*.

**The German gloss was hardcoded inside the English stems.** Two items
in the interactive file carried `(= Blätter)` and `(= Schall)` in the
question text itself, which is invisible to a Spanish learner and wrong
for an English one. Both are gone; the gloss is the i18n prompt now.
`Schall` was also the wrong word — it means *sound*, not *scarf*, which
is *der Schal* with one l, as the paper worksheet correctly had it.

**Every key was the first option.** The interactive file did not shuffle:
options rendered in source order and the key was option 1 in 20 of 21
items. A learner who noticed could score 95% without reading a stem. The
fourteen multiple-choice keys here are spread across all four positions
([4, 3, 3, 4]) and the distribution is asserted at build time, on top of
the engine's runtime shuffle.

**Right and wrong said the same thing — which was nothing.** There were
no explanations anywhere in either file. The results screen printed a tick
or a cross and, when wrong, the correct string. Every one of the
twenty-eight scored points now carries its own reason, and each wrong
multiple-choice option says why *that* option is wrong, via a per-option
`data-explain` injected after `D.mc` — the fifth lesson to do it that way
rather than change a builder thirty decks share.

**There was no teaching stage at all.** Three grammar points were tested
— has/have, nor, present simple against continuous — and the whole of the
explanation was a one-line coloured banner above the first item of each
section, plus hints hidden behind a button. Fourteen language slides now
come before the questions that use them, and everything the banners and
hints said is in them.

**One item could not be answered from its stem.** *"Joyce is standing at
the edge of the photograph, not in the centre. She is ______ of the
picture"*, keyed to **on the right hand side** — but nothing in the stem
says which side, and *in the right hand corner* is also an edge. Only the
hidden hint ("not the left side!") carried the information. The stem now
names the side. The same section gained **in the foreground**, which
neither source file taught although both asked learners to describe a
picture.

**The nor rule as taught was wrong, and marked correct English wrong.**
The paper worksheet asked the learner to "correct the mistake" in *"I
don't like the Upside Down, or the Demogorgon"* — but `or` after a single
negative verb is standard English and there is no mistake in it. The
banner in the interactive file said the same thing: "after a negative
statement we use NOR — not OR". The two real environments for *nor* are
taught instead — the `neither … nor` pair, and *nor* opening a second
clause with the verb in front of the subject — and a slide says plainly
that `or` after a negative is good English, while `neither … or` and
`nor she does` are not.

**Three vocabulary items were conflated or mis-keyed.** The worksheet's
matching activity offered *"A plain / desert landscape"* as one option
for one description, so the two words could not be told apart; its own
vocabulary list asks for them separately. They are now taught as a
three-way contrast with **field** — flat, dry and enclosed are three
different properties — and the multiple-choice item that tests it says
the ground is green and there is no sand. The worksheet also had *das
Rollerdisco* (it is feminine) and the interactive file's Q6 offered
**scarfs** as a distractor for *leaves*, which is a real English plural.

Also carried over and fixed: the interactive file's `QUESTIONS` map, used
to print the review at the end, held shortened rewrites of several stems,
so the review showed the learner a question they had not been asked; the
progress bar counted 22 items while the score divided by 21; and the free
writing box's placeholder was *"I like hiking and walking in the forest
because…"*, which is the model answer to the paper worksheet's own
section 3a. No scored input in this deck carries a placeholder at all,
which the build asserts.

The free-writing question becomes the activation stage: a describe-and-
draw speaking task on the cover picture, plus a letter. 100–150 words
rather than the house 150–250, because this is an A2–B1 school lesson
whose sources asked for one sentence and for five.

Dark theme. The palette is pasted verbatim from
`extract-palette.py StrangerThings/hero.jpg` (measured median luminance
0.171, so no `--light`); every row of the contrast report PASSES, the
weakest being border-on-surface at 3.70:1 against a 1.25 floor. The hero
— a figure in a wood, a deer to the right, pale trunks behind, coral sky
— is also the picture the describing-a-picture part and the speaking task
are about, so the artwork does teaching work rather than decorating.
"""
import re
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
import i18n_stranger_test as I

TPL = '/home/claude/forbes-english/lesson-template/lesson-template.html'
OUT = '/home/claude/forbes-english/stranger-things-test.html'
STUB = '/home/claude/forbes-english/stranger-things-test-german.html'
F = 'StrangerThings'
E = I.T['en']
HERO = 'hero.jpg'

# Derived mechanically from StrangerThings/hero.jpg:
#   python3 lesson-template/extract-palette.py StrangerThings/hero.jpg
# Pasted verbatim. Dark theme — the hero's median luminance is 0.171 —
# and every row of the contrast report PASSES (text on surface 15.85:1,
# the weakest row, border on surface, 3.70:1 against a 1.25 floor).
PALETTE = '''  --hero: url('%s/%s');

  --void          : #0a0d0a;
  --surface       : #151a13;
  --surface2      : #1e261c;
  --border        : #b85545;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #ec8777;
  --accent-bright : #f7bcb3;
  --accent-dim    : #db442d;
  --secondary     : #5e7a84;
  --contrast      : #1deda5;''' % (F, HERO)

# The Part 2 row: a prompt from the language layer, an arrow, a box. The
# prompt is the only piece of learner-facing content on this site that is
# meant to change with the selector, so it gets a class of its own rather
# than borrowing the stem's styling.
CSS = ('.v-prompt { font-weight: 600; color: var(--accent-bright); }\n'
       '.v-arrow { color: var(--text-dim); margin: 0 12px; '
       'font-family: var(--font-mono); }\n'
       '[data-type="gap"] .gap-row .q-stem { line-height: 1.45; }\n')

VROW = ('<span class="v-prompt" data-i18n="%s">%s</span>'
        '<span class="v-arrow">&rarr;</span> ______')


# ── guards ─────────────────────────────────────────────────────────────
def assert_key_is_deranged(mc, label='MC'):
    """The key was option 1 in 20 of the 21 items of the file this replaces.

    A per-item fact cannot express what is wrong with that, so it is
    measured as a distribution across every multiple-choice item in the
    deck: all four positions used, none starved."""
    n = len(mc)
    keys = [q['correct'] for q in mc]
    counts = [keys.count(i) for i in range(4)]
    assert 0 not in counts, (
        '%s: position(s) %s never carry the key (%s)'
        % (label, [i for i, c in enumerate(counts) if not c], counts))
    assert max(counts) - min(counts) <= max(1, n // 5), (
        '%s: the key distribution is lopsided (%s)' % (label, counts))
    return counts


def _visible(chunk):
    chunk = re.sub(r'<div class="act-target".*?</div>', '', chunk, flags=re.S)
    chunk = re.sub(r'data-explain="[^"]*"', '', chunk)
    return re.sub(r'<[^>]+>', ' ', chunk).lower()


def assert_no_answer_is_shown(html):
    """Nothing may reveal an answer before it is given.

    Two halves, and the second is stricter than the version this
    inherits from `build_geo.py`. The first is blunt: no scored input
    carries a `placeholder` at all — the file this replaces put the model
    answer in one. The second checks every accepted spelling of every
    answer on a gap slide against the *whole* of that slide's visible
    text, not just against its own row. Two rows per slide is the shape
    of Part 2, so a clue that leaks its neighbour's word is exactly as
    bad as one that leaks its own, and a per-row check would not see it.

    `data-explain` is excluded because it is written into the page only
    after marking, and a word bank would be excluded by design — there
    is none here, because a bank turns a production task back into
    recognition."""
    for m in re.finditer(r'<input[^>]*class="gap"[^>]*>', html):
        assert 'placeholder' not in m.group(0), \
            'a gap input carries a placeholder: %s' % m.group(0)[:120]

    n = 0
    for slide in re.findall(r'<section class="slide"[^>]*data-type="gap".*?'
                            r'</section>', html, re.S):
        chunks = slide.split('<div class="card gap-row"')
        answers = []
        for chunk in chunks[1:]:
            found = re.findall(r'data-answer="([^"]+)"', chunk)
            # One gap per row, always: checkGaps marks the FIRST .gap in
            # each row while maxScore counts every .gap on the slide, so a
            # second input inside one row creates a point nobody can score.
            assert len(found) == 1, 'one gap per row, or scoring loses one'
            answers += found[0].split('|')
        text = _visible(slide)
        for alt in answers:
            assert alt.lower() not in text, (
                'the accepted answer %r is readable on the slide that asks '
                'for it' % alt)
        n += len(chunks) - 1
    return n


def assert_prompts_never_give_the_answer(groups):
    """The i18n half of the same rule, run over every language.

    Part 2's prompts are the one piece of content on this site that is
    supposed to change with the selector, so checking the built HTML only
    checks English. Each group is (i18n keys visible on the slide,
    accepted answers on that slide); every key is resolved in every
    language and checked against every answer. This is what caught the
    German prompt for the roller disco: German really does say *die
    Rollerdisco*, which contains the answer whole."""
    bad = []
    for lang, table in I.T.items():
        for keys, answers in groups:
            text = ' '.join(_visible(table[k]) for k in keys)
            for a in answers:
                if a.lower() in text:
                    bad.append((lang, a, keys))
    assert not bad, ('a prompt or hint contains its own answer: %s'
                     % bad[:4])


def mc_slide(i, total, q, ek, tk, folder='', bg=None):
    """D.mc, plus a per-distractor explanation.

    The shared builder writes one explanation per slide, which is what
    makes right and wrong identical. Rather than change a builder thirty
    lessons share, the attribute is injected here — the fifth lesson to
    do it this way: each wrong option says why *it* is wrong and the key
    falls through to the slide's own `why`. The engine already prefers an
    option's own explanation."""
    html = D.mc(i, total, q, ek, E[ek], tk, E[tk], folder=folder, bg=bg)
    ex = q['opt_why']
    assert len(ex) == len(q['options']), 'opt_why must line up with options'
    assert ex[q['correct']] is None, 'the key takes the slide explanation'
    assert all(x for n, x in enumerate(ex) if n != q['correct']), \
        'every distractor needs its own explanation'
    parts = html.split('<button class="opt"')
    out = [parts[0]]
    for n, chunk in enumerate(parts[1:]):
        attr = ' data-explain="%s"' % D.esc(ex[n]) if ex[n] else ''
        out.append('<button class="opt"%s%s' % (attr, chunk))
    return ''.join(out)


def teach(ek, tk, cards, cols=None, bg=None):
    """cards: list of (head_key_or_None, body_html, note_key_or_None)."""
    return D.teach(ek, E[ek], tk, E[tk],
                   [(hk, E[hk] if hk else '', body, nk, E[nk] if nk else None)
                    for hk, body, nk in cards],
                   cols=cols, folder=F, bg=bg)


# ══ PART 1 — describing a picture ══════════════════════════════════════
# Keys at 2, 0, 3, 1. Q4 could not be answered from its own stem in the
# file this replaces; the stem now names the side. "in the foreground"
# is new: neither source taught it, though both asked for descriptions.
PIC = [
    dict(correct=2,
         stem='A figure stands among the trees, far away and half hidden by '
              'shadow. It is standing ______ of the picture.',
         options=['in the middle', 'in the foreground', 'in the background',
                  'in the bottom left-hand corner'],
         why='Furthest from you, behind everything else. <em>In the '
             'background</em> answers how far away something is, never which '
             'side it is on.',
         opt_why=[
             'The middle is between the other things, at the same distance as '
             'they are. This figure is behind them &mdash; far away and half '
             'hidden is the clue.',
             'The foreground is the part closest to you, at the very front of '
             'the picture. This figure is as far from you as it can be.',
             None,
             'A corner names a small piece of the edge, and it needs two '
             'words: bottom, then left. Nothing in the stem puts the figure '
             'at an edge.']),

    dict(correct=0,
         stem='Mike is comforting Eleven in the photograph. Which sentence '
              'describes what you can see?',
         options=['He has a hand on her shoulder.',
                  'He has a hand in her shoulder.',
                  'He has a shoulder on her hand.',
                  'He has a hand on the shoulder.'],
         why='A hand rests <strong>on</strong> a shoulder, and English names '
             'whose shoulder it is: <strong>her</strong> shoulder.',
         opt_why=[
             None,
             '<em>In</em> a shoulder would put the hand inside it. Anything '
             'resting on a surface takes <strong>on</strong>.',
             'That swaps the two nouns round. The shoulder is the thing being '
             'touched, so it is the one that follows <em>on</em>.',
             'Grammatical, but English uses a possessive for body parts when '
             'we know whose they are. <em>The shoulder</em> sounds as though '
             'it belongs to nobody.']),

    dict(correct=3,
         stem='Dustin is standing between Lucas and Mike in the group photo. '
              'He is ______.',
         options=['in the background', 'in the foreground',
                  'on the right-hand side', 'in the middle'],
         why='Between the other two, so there is something on each side of '
             'him. That is exactly what <em>in the middle</em> means.',
         opt_why=[
             'That would put him behind Lucas and Mike. <em>Between</em> puts '
             'him at the same distance from you as they are.',
             'That would put him in front of the other two, closest to you. '
             'He is level with them, not ahead of them.',
             'That names one side of the photo. With a boy on each side of '
             'him, he is not on a side at all.',
             None]),

    dict(correct=1,
         stem='Nancy is not in the centre of the photograph. She is at the '
              'edge, next to the window on the right. She is ______.',
         options=['in the middle', 'on the right-hand side',
                  'in the background', 'in the bottom left-hand corner'],
         why='At the edge and on the right, so the phrase has to name a side. '
             'Note the hyphen: <strong>right-hand</strong> side.',
         opt_why=[
             'The stem rules this out in its first six words: she is not in '
             'the centre.',
             None,
             'That says how far away she is, not which side she is on, and '
             'the stem has already told you the side.',
             'A corner is where two edges meet, and this one is on the left. '
             'She is by the window on the right.']),
]

# ══ PART 2 — L1 into English ═══════════════════════════════════════════
# Ten items, two per slide, no word bank: a bank would turn a production
# task back into recognition and would hand over half the section.
# (prompt key, canonical + accepted spellings, why)
VOCAB = [
    ('v1p', 'autumn|the autumn|fall|the fall',
     'British English says <strong>autumn</strong>, American English says '
     '<strong>the fall</strong>. Both are right, and both are accepted here.'),
    ('v2p', 'leaves|the leaves',
     'One <strong>leaf</strong>, two <strong>leaves</strong> &mdash; the f '
     'turns into ves, as in <em>half &rarr; halves</em>.'),
    ('v3p', 'scarf|a scarf|the scarf',
     'One <strong>scarf</strong>, two <strong>scarves</strong>: the same f '
     '&rarr; ves change again.'),
    ('v4p', 'bright',
     '<strong>Bright</strong> is about how much light there is. Its opposite '
     'is <em>dim</em>, and a bright colour is a strong, clear one.'),
    ('v5p', 'bowling alley|a bowling alley|the bowling alley|bowling-alley',
     'Two words. The <em>alley</em> is the long polished lane the ball runs '
     'down, and the place takes its name from it.'),
    ('v6p', 'rollerdisco|a rollerdisco|the rollerdisco|roller disco|'
            'a roller disco|the roller disco|roller-disco',
     'Usually written as one word. <em>Roller disco</em> and '
     '<em>roller-disco</em> are accepted too.'),
    ('v7p', 'desert|a desert|the desert',
     'One s in the middle. <em>Dessert</em>, with two, is what you eat after '
     'dinner &mdash; a spelling worth being careful with.'),
    ('v8p', 'plain|a plain|the plain|plains|the plains',
     'A <strong>plain</strong> is flat, wide and open. That says nothing '
     'about how dry it is.'),
    ('v9p', 'field|a field|the field|meadow|a meadow|the meadow',
     'A <strong>field</strong> has a boundary round it. <em>Meadow</em> '
     '&mdash; grass rather than crops &mdash; is accepted as well.'),
    ('v10p', 'rusty|rust-coloured|rust coloured|rust-colored|rust colored',
     'From <em>rust</em>, the reddish-brown coating iron gets in the wet. '
     '<em>Rust-coloured</em> is accepted as well.'),
]
VOCAB_HINTS = ['h1', 'h2', 'h3', 'h4', 'h5']

# ══ PART 3 — the word that fits ════════════════════════════════════════
# Keys at 0, 3, 1, 2. These are the pairs the sources let learners confuse:
# a plain against a desert, an alley against a rink, rusty against bright.
FIT = [
    dict(correct=0,
         stem='A torch was ______ the dark tunnel, and the kids could finally '
              'see the way ahead.',
         options=['shining through', 'showing through', 'burning through',
                  'shining under'],
         why='<strong>Shine through</strong> is light passing from one side '
             'all the way to the other &mdash; a torch in a tunnel, sunlight '
             'in a wood, a lamp behind a curtain.',
         opt_why=[
             None,
             '<em>Show through</em> is used of something faintly visible '
             'behind a surface, like ink on thin paper. It is not what a '
             'torch does.',
             '<em>Burn through</em> means to make a hole by burning. A torch '
             'gives light, not fire.',
             '<em>Under</em> would put the light beneath the tunnel. It '
             'travels along it and out of the far end, which is '
             '<em>through</em>.']),

    dict(correct=3,
         stem='It stretches away flat and empty in every direction, but the '
              'grass is green and there is no sand anywhere. It is a vast '
              '______.',
         options=['desert', 'forest', 'meadow', 'plain'],
         why='A <strong>plain</strong> is flat, wide and open. Flat and dry '
             'are two different properties, and only one of them is in the '
             'stem.',
         opt_why=[
             'A desert is dry, and the stem says the grass is green and there '
             'is no sand. Being flat does not make land dry.',
             'A forest is full of trees, which is not something that '
             'stretches away flat and empty.',
             'A meadow is a small grassy field with a boundary round it, not '
             'something running in every direction as far as you can see.',
             None]),

    dict(correct=1,
         stem='Billy hands you a heavy ball and points down a polished lane '
              'at ten pins. You are at the ______.',
         options=['rollerdisco', 'bowling alley', 'sports field',
                  'roller rink'],
         why='<strong>Bowling alley</strong>. The lane itself is the alley, '
             'and the whole place takes its name from it.',
         opt_why=[
             'At a rollerdisco you skate to music. Nobody hands you a heavy '
             'ball there, and there are no pins.',
             None,
             'A sports field is outdoors and has grass on it. A polished lane '
             'is indoors.',
             'A roller rink is the floor you skate on. Still skating, still '
             'no ball and no pins.']),

    dict(correct=2,
         stem='Everything in the Upside Down looked old and decayed, the '
              'colour of iron left out in the rain for years. It had a ______ '
              'colour.',
         options=['bright', 'golden', 'rusty', 'plain'],
         why='<strong>Rusty</strong> is the reddish-brown of iron left in the '
             'wet, and it carries the idea of decay with it. That is why it '
             'fits this place and a simple colour word would not.',
         opt_why=[
             'Bright is about how much light there is rather than about '
             'colour, and this place is described as old and decayed.',
             'Golden is warm and shining. Rust is dull and reddish-brown '
             '&mdash; the opposite feeling.',
             None,
             '<em>Plain</em> as an adjective means simple, or without a '
             'pattern. It does not name a colour at all.']),
]

# ══ PART 4 — has or have ═══════════════════════════════════════════════
# Gaps rather than multiple choice: with a closed set of three forms the
# options carry no information, and the point is producing the -s.
# (hint key, [(sentence, answers, why), …])
HAVE = [
    ('h6', [
        ('The man ______ a remote control in his hand.', 'has',
         '<em>The man</em> is he, and he, she and it always take the -s form.'),
        ('Mike and Dustin ______ bikes, and they ride everywhere on them.',
         'have',
         'Two names joined by <em>and</em> are they. The sentence even says '
         '<em>they</em> in its second half.'),
    ]),
    ('h7', [
        ('The Demogorgon ______ no face at all.', 'has',
         'One creature, so it is <em>it</em> &mdash; and it takes the -s '
         'form, however strange the creature happens to be.'),
        ('We ______ a plan to close the gate.', 'have',
         '<em>We</em> takes the plain form. Only he, she and it get the -s.'),
    ]),
]

# ══ PART 5 — nor ═══════════════════════════════════════════════════════
# Keys at 3, 0. The rule as the sources stated it was wrong; see the
# docstring. These two items test the pair and the inversion, which are
# the two places nor actually belongs.
NOR = [
    dict(correct=3,
         stem='Will is neither in Hawkins ______ in the Upside Down. Nobody '
              'knows where he is.',
         options=['or', 'and', 'not', 'nor'],
         why='<strong>Neither</strong> and <strong>nor</strong> travel as a '
             'pair. Once you have written <em>neither</em>, the second half '
             'has to be <em>nor</em>.',
         opt_why=[
             '<em>Neither &hellip; or</em> is the one combination that is '
             'always wrong. <em>Or</em> pairs with <em>either</em>.',
             '<em>And</em> adds two true things together, and <em>neither</em> '
             'has already made both of them untrue.',
             'That would be two negatives in a row. <em>Neither</em> is '
             'already doing the negating.',
             None]),

    dict(correct=0,
         stem='Hopper does not believe the story, ______',
         options=['nor does Joyce.', 'nor Joyce does.', 'or does Joyce.',
                  'nor Joyce believes.'],
         why='After <strong>nor</strong> the verb comes in front of the '
             'subject &mdash; <em>nor does Joyce</em>. It is the word order '
             'of a question.',
         opt_why=[
             None,
             'The right word, the wrong order. <em>Nor</em> pulls the verb in '
             'front of the subject: <em>nor does Joyce</em>.',
             '<em>Or</em> cannot open a clause of its own like this. A second '
             'negative clause after a comma takes <em>nor</em>.',
             'Once <em>does</em> is doing the work the main verb goes back to '
             'its plain form &mdash; and it still has to follow the '
             'inversion.']),
]

# ══ PART 6 — now, or always? ═══════════════════════════════════════════
# Keys at 1, 2, 0, 3. The first and last are the same verb in its two
# senses, which is the distinction the sources asserted but never drew.
NOW = [
    dict(correct=1,
         stem='The government agents ______ when they arrive at the lab. '
              'Nobody is smiling.',
         options=['are looking very serious', 'look very serious',
                  'looks very serious', 'is looking very serious'],
         why='Here <strong>look</strong> means <em>seem</em>, which is a '
             'state and not an action. States take the present simple, and '
             '<em>the agents</em> is plural, so there is no -s.',
         opt_why=[
             '<em>Are looking</em> would mean they are pointing their eyes at '
             'something at this moment. Looking serious is how they seem.',
             None,
             'The -s form belongs to he, she or it. <em>The agents</em> is '
             'they.',
             'Two problems at once: <em>is</em> does not go with a plural '
             'subject, and a state verb does not take the -ing form.']),

    dict(correct=2,
         stem='The two agents meet. Right now, at this very moment, they '
              '______.',
         options=['shake each other&rsquo;s hands',
                  'shakes each other&rsquo;s hands',
                  'are shaking each other&rsquo;s hands',
                  'are shake each other&rsquo;s hands'],
         why='It is happening as you watch, so English uses <strong>be + '
             '-ing</strong>: <em>are shaking</em>.',
         opt_why=[
             'The present simple would mean they do this every time they '
             'meet. The stem says right now, at this very moment.',
             'The same problem, and the -s as well: <em>the two agents</em> '
             'is they.',
             None,
             'The <em>be</em> is there but the -ing is missing. <em>Be</em> '
             'and <em>-ing</em> always come as a set.']),

    dict(correct=0,
         stem='The kids look at the forest. &ldquo;______ a lot of trees '
              'here,&rdquo; says Mike, &ldquo;we will never find him.&rdquo;',
         options=['There are', 'There is', 'They are', 'It is'],
         why='<strong>Trees</strong> is plural, and the verb agrees with what '
             'follows <em>there</em>, not with <em>there</em> itself.',
         opt_why=[
             None,
             'The verb agrees with what comes after it, and <em>a lot of '
             'trees</em> is plural.',
             '<em>They are</em> points back at something already mentioned. '
             'Mike is naming the trees for the first time.',
             'Singular, and it too points at something already known. '
             'Neither half fits a first mention of many trees.']),

    dict(correct=3,
         stem='Dustin ______ the map right now. He has it open on the table '
              'in front of him.',
         options=['looks at', 'does look at', 'looking at', 'is looking at'],
         why='<strong>Look at</strong> is an action you can watch happening, '
             'so it takes <strong>be + -ing</strong>. Compare <em>they look '
             'serious</em>, which is a state.',
         opt_why=[
             'The present simple would make it a habit. The stem says right '
             'now, with the map open in front of him.',
             'That is the emphatic present simple, used to insist something '
             'is true &mdash; not to say it is happening at this moment.',
             'The -ing is there but the <em>be</em> is missing. English needs '
             'both halves: <em>is looking</em>.',
             None]),
]

ALL_MC = PIC + FIT + NOR + NOW

# The activation strip. `check-lesson.js`'s BANK gate walks every
# `.bank-chip` on the page, and the activation chips are bank chips — so
# a strip that happens to list gap answers in gap order reads to the gate
# as an answer key, even though it sits after the results slide and after
# every gap has been marked. Phrases rather than bare headwords is better
# production practice anyway, and it keeps the chips off the answers.
ACT_CHIPS = ['in the foreground', 'in the middle', 'in the background',
             'on the right-hand side', 'a hand on her shoulder',
             'the autumn leaves', 'a rusty colour', 'shining through',
             'a scarf', 'a bowling alley']


def assert_chips_are_not_a_key(chips, answers):
    """The BANK gate, run at build time so it fails here and says why."""
    pos = [chips.index(a) for a in answers if a in chips]
    assert not (len(pos) >= 2 and all(x < y for x, y in zip(pos, pos[1:]))), (
        'the activation chips list gap answers in gap order (%s)' % pos)


def build():
    key_spread = assert_key_is_deranged(ALL_MC, 'all multiple choice')
    for label, group in (('Part 1', PIC), ('Part 3', FIT), ('Part 5', NOR),
                         ('Part 6', NOW)):
        D.assert_no_key_is_longest(group, label)

    # The i18n half of "nothing shows the answer": every prompt and hint
    # on a gap slide, in every language, against the answers on it.
    groups = []
    for n in range(5):
        pair = VOCAB[2 * n:2 * n + 2]
        groups.append((['a2E', 'a2T', VOCAB_HINTS[n]] + [k for k, _, _ in pair],
                       [a for _, ans, _ in pair for a in ans.split('|')]))
    for hk, rows in HAVE:
        groups.append((['a4E', 'a4T', hk],
                       [a for _, ans, _ in rows for a in ans.split('|')]))
    assert_prompts_never_give_the_answer(groups)
    assert_chips_are_not_a_key(
        ACT_CHIPS,
        [a.split('|')[0] for _, a, _ in VOCAB]
        + [a for _, rows in HAVE for _, a, _ in rows])

    logo = D.logo_from(TPL)
    S = [D.cover(logo, E['coverTitle'], E['coverSub'],
                 [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                  ('Time', E['chipTime']), ('Count', E['chipCount'])])]

    # ── 2. orientation ──
    S += [teach('tOrient', 'oT', [
        ('oa', 'Six parts. Each one opens with the language it is about to '
               'test, so read those slides before you start answering.', None),
        ('ob', 'Fourteen questions to choose from and fourteen boxes to type '
               'into. Ten of the boxes ask you to produce a word from its '
               'meaning alone.', 'on')], cols='1fr 1fr')]

    # ── 3-4. describing a picture ──
    S += [teach('tPic', 'p1T', [
        ('p1a', 'The part of the picture closest to you, right at the front. '
                '<em>There is a deer in the foreground.</em>', None),
        ('p1b', 'Between the other things, with something on each side. '
                '<em>A boy is standing in the middle.</em>', None),
        ('p1c', 'Furthest away, behind everything else. <em>Tall trees rise '
                'in the background.</em>', 'p1n')], cols='1fr 1fr 1fr')]

    S += [teach('tPic', 'p2T', [
        ('p2a', 'One side of the picture rather than the centre. <em>The deer '
                'is on the right-hand side.</em>', None),
        ('p2b', 'Where two edges meet. Name them in this order: top or '
                'bottom, then left or right.', None),
        ('p2c', 'For people touching: <em>he has a hand on her shoulder</em>. '
                'English says whose shoulder it is.', 'p2n')],
        cols='1fr 1fr 1fr')]

    S += [mc_slide(i + 1, len(PIC), q, 'a1E', 'a1T', folder=F)
          for i, q in enumerate(PIC)]

    # ── 9-12. the words ──
    S += [teach('tVocab', 'v1T', [
        ('v1a', 'The season between summer and winter. British English: '
                '<strong>autumn</strong>. American English: <strong>the '
                'fall</strong>.', None),
        ('v1b', 'One <strong>leaf</strong>, two <strong>leaves</strong>. '
                '<em>The leaves fell from the trees like orange snow.</em>',
         None),
        ('v1c', 'You wind it round your neck against the cold. One '
                '<strong>scarf</strong>, two <strong>scarves</strong>.',
         'v1n')], cols='1fr 1fr 1fr')]

    S += [teach('tVocab', 'v2T', [
        ('v2a', 'The reddish-brown of old iron left out in the rain. '
                '<em>Everything down there had a rusty colour.</em>', None),
        ('v2b', 'Giving out a lot of light. <em>The lab lights were so bright '
                'they hurt her eyes.</em> Opposite: <strong>dim</strong>.',
         None),
        ('v2c', 'Light from one side passing all the way to the other. <em>A '
                'torch was shining through the tunnel.</em>', 'v2n')],
        cols='1fr 1fr 1fr')]

    S += [teach('tVocab', 'v3T', [
        ('v3a', 'You roll a heavy ball down a polished lane to knock over ten '
                'pins. Strike, spare, gutter ball.', None),
        ('v3b', 'You put on roller skates and go round and round to music. '
                'Friday night in Hawkins.', 'v3n')], cols='1fr 1fr')]

    S += [teach('tVocab', 'v4T', [
        ('v4a', 'A wide area of flat land with no hills. <em>The Upside Down '
                'looks like a vast plain.</em>', None),
        ('v4b', 'So dry that almost nothing grows: sand, bare rock, no '
                'water.', None),
        ('v4c', 'A piece of land with a hedge or a fence round it, where '
                'crops grow or animals graze.', 'v4n')], cols='1fr 1fr 1fr')]

    # ── 13. how Part 2 works ──
    S += [teach('tTask', 'tkT', [
        ('tka', 'A clue beside each box: a short definition in English, or '
                'the same word in your own language if you pick one from the '
                'menu at the top of the screen.', None),
        ('tkb', 'The English word, typed into the box. One word, or two where '
                'English needs two. <em>A</em> and <em>the</em> in front of '
                'it are fine either way.', 'tkn')], cols='1fr 1fr')]

    # ── 14-18. Part 2, two rows per slide, one gap per row ──
    for n in range(5):
        pair = VOCAB[2 * n:2 * n + 2]
        rows = [(VROW % (k, E[k]), [ans], why) for k, ans, why in pair]
        S += [D.gap(n + 1, 5, rows, None, 'a2E', E['a2E'], 'a2T', E['a2T'],
                    folder=F, hint=E[VOCAB_HINTS[n]],
                    hint_key=VOCAB_HINTS[n], width=210, size=19)]

    # ── 19-22. Part 3 ──
    S += [mc_slide(i + 1, len(FIT), q, 'a3E', 'a3T', folder=F)
          for i, q in enumerate(FIT)]

    # ── 23-24. has and have ──
    S += [teach('tGram', 'g1T', [
        ('g1a', '<em>The man has a remote control. Eleven has powers. The '
                'Demogorgon has no face.</em>', None),
        ('g1b', '<em>I have a torch. We have a plan. Mike and Dustin have '
                'bikes.</em>', 'g1n')], cols='1fr 1fr')]

    S += [teach('tGram', 'g2T', [
        ('g2a', 'The -s is already inside <strong>has</strong>. <em>He '
                'haves</em> does not exist in English at all.', None),
        ('g2b', 'British English often adds <em>got</em>: <em>he has got a '
                'torch</em> means the same as <em>he has a torch</em>, and '
                'the -s stays where it was.', 'g2n')], cols='1fr 1fr')]

    for n, (hk, rows) in enumerate(HAVE, 1):
        S += [D.gap(n, len(HAVE), [(s, [a], w) for s, a, w in rows], None,
                    'a4E', E['a4E'], 'a4T', E['a4T'], folder=F,
                    hint=E[hk], hint_key=hk, width=120, size=21)]

    # ── 27-28. nor ──
    S += [teach('tGram', 'g3T', [
        ('g3a', 'The pair always travels together. <em>Will is neither in '
                'Hawkins nor in the Upside Down.</em>', None),
        ('g3b', 'Opening a second negative clause. <em>She does not watch '
                'television, nor does she listen to the radio.</em>', 'g3n')],
        cols='1fr 1fr')]

    S += [teach('tGram', 'g4T', [
        ('g4a', '<em>I do not like the Upside Down or the Demogorgon.</em> '
                'One verb, two things after it &mdash; and this is correct '
                'English.', None),
        ('g4b', '<em>I like neither the Upside Down nor the Demogorgon</em>, '
                'or <em>I do not like the Upside Down, nor do I like the '
                'Demogorgon.</em>', 'g4n')], cols='1fr 1fr')]

    S += [mc_slide(i + 1, len(NOR), q, 'a5E', 'a5T', folder=F)
          for i, q in enumerate(NOR)]

    # ── 31-32. now or always ──
    S += [teach('tGram', 'g5T', [
        ('g5a', '<em>The two agents are shaking hands. Eleven is closing the '
                'gate.</em>', None),
        ('g5b', 'look, seem, know, like, want, believe, own. <em>The agents '
                'look very serious. Eleven knows where the gate is.</em>',
         'g5n')], cols='1fr 1fr')]

    S += [teach('tGram', 'g6T', [
        ('g6a', '<em>There is a torch on the table. There is a deer in the '
                'foreground.</em>', None),
        ('g6b', '<em>There are a lot of trees here. There are two people in '
                'the picture.</em>', 'g6n')], cols='1fr 1fr')]

    S += [mc_slide(i + 1, len(NOW), q, 'a6E', 'a6T', folder=F)
          for i, q in enumerate(NOW)]

    # ── results and activation ──
    S += [D.results(),
          D.activate(E['actTitle'], E['actUse'],
                     ACT_CHIPS,
                     'Discussion &middot; in pairs', E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'])]
    return S, key_spread


# The retired worksheet. Relative, with the extension: every link on this
# site is built from the filename (`library.html` sets `a.href = l.file`)
# and the host serves `.html` paths, so an extensionless `/stranger-things-test`
# would 404 and the stub would fail at the one job it has.
STUB_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="0; url=stranger-things-test.html">
<link rel="canonical" href="stranger-things-test.html">
<title>Stranger Things — the English Test</title>
</head>
<body style="font-family:system-ui,sans-serif;background:#0a0d0a;color:#f5f2f2;
             display:grid;place-items:center;min-height:100vh;margin:0;
             text-align:center;padding:24px">
<p>This test now lives at
   <a href="stranger-things-test.html" style="color:#ec8777">forbesenglish.com/stranger-things-test.html</a>.</p>
</body>
</html>
'''


if __name__ == '__main__':
    slides, key_spread = build()
    body = "".join(slides)
    n = body.count('<section class="slide')
    body = body.replace('NN slides', '%d slides' % n)
    I.T['en']['chipCount'] = '%d slides' % n
    I.T['de']['chipCount'] = '%d Folien' % n
    I.T['es']['chipCount'] = '%d diapositivas' % n

    s = D.assemble(TPL, OUT, body, PALETTE,
                   'Stranger Things — the English Test', I,
                   langs=('en', 'de', 'es'))
    s = s.replace('</style>\n</head>', CSS + '</style>\n</head>', 1)
    assert 'data:image' not in s, 'a base64 blob survived into the build'
    points = assert_no_answer_is_shown(s)
    for gone in ('= Blätter', '= Schall', 'Schall', 'hiking and walking'):
        assert gone not in s, 'a hardcoded gloss survived: %r' % gone
    open(OUT, 'w', encoding='utf-8').write(s)

    open(STUB, 'w', encoding='utf-8').write(STUB_HTML)

    print('wrote %s — %d bytes, %d slides' % (OUT, len(s), n))
    print('wrote %s — redirect stub' % STUB)
    print('MC key positions A/B/C/D: %s' % key_spread)
    assert points == len(VOCAB) + 4, 'expected %d gaps, counted %d' % (
        len(VOCAB) + 4, points)
    print('scored points: %d multiple choice + %d gaps = %d'
          % (len(ALL_MC), points, len(ALL_MC) + points))
