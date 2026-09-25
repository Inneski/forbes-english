# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Test (Part 1), rebuilt as a 16:9 deck in house style 2.

`forbes-english-b1-mixed-grammar-test.html` was a 720px scrolling column:
Fraunces and Work Sans instead of the site's three faces, a hand-picked mint
palette over a coral desert hero, the hero boxed in a card, a logo lockup at
the superseded x=100/letter-spacing=8 geometry, twelve invented `--tense-*`
hexes that were all near-misses of `tense-palette.css`, no language switcher
at all — the `EN ↔ ES` badge was a CSS tooltip on six vocabulary words — and
no activation stage. The audit is `docs/PLAN-mixed-grammar-b1.md`.

All 35 scored items survive: 10 multiple choice, 8 reading gaps, 6 true/false,
5 sentence reorderings, 6 error corrections. Nothing pedagogical was dropped.

House style 2, not the washed hero
----------------------------------
Innes, 2026-09-25. The artwork is flat-vector Noma Bar, and the template's own
PANEL block says §5's washed hero "is wrong when the artwork is the point — a
flat-vector illustration dimmed by a quarter and covered by a card is neither
legible nor worth looking at". So each section opens with `D.divider()`
showing its picture whole, then a `D.panel()` carrying the instruction with
the same picture cropped to a 548px column at full opacity. The question
slides carry no `bg=`, and that does NOT leave them on flat --void: the
engine's `.bg-layer` paints `--hero` at 0.72 behind every slide that does not
paint its own background, and only panels and dividers do. So all 33
question slides sit on the COVER's wash (house rule 3) — measured on a local
render, 2026-09-25. That is why the cover brief asks for an empty middle: the
cover is the backdrop of most of the deck, not of one slide.

Panels alternate `side='right'` down the deck — "inverted panels", per the
template's own comment: it "stops a long deck reading as one template". On
45 slides that is structural. `build_twinpeaks2.py` is the other deck doing
this and was the reference.

Four content bugs fixed on the way through
------------------------------------------
Found in the old TEST_DATA, and live on the site until this build:

1. `ec6` marked *"the girl **that** is sitting there"* wrong while `tf6` in
   the same test taught that "that" can replace either. Now accepted.
2. `ec2` accepted only "I will call you", rejecting the commonest correct
   form, "I'll call you". `ec1` likewise rejected "She's lived here".
3. The engine's `flatten()` normalises case, quotes, dashes and whitespace
   but NOT trailing punctuation, so a learner typing the full sentence with
   its full stop was marked wrong. `sentences()` below expands every
   error-correction answer with and without it.
4. Section 4 shuffled single words. §7 wants an `order` chunked "at the
   joints you are teaching, never mid-phrase", so the five sentences are cut
   into phrases. Scoring is unchanged — `order` already scores one point for
   the whole sentence, which is what the old page did too.

True/false runs as `mc` with two options; there is no `tf` slide type. The
ANSWERS gate is satisfied either way, since "False" beats "True" by one
character and the gate needs both a 10% margin and four absolute characters.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_mixedgrammar1 as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-b1-mixed-grammar-test.html'
F = 'MixedGrammarPart1'

E = I.T['en']          # one source for the English; see the i18n docstring

# ── PALETTE — derived from the cover, every contrast row PASS ──────────
#   python3 lesson-template/extract-palette.py MixedGrammarPart1/hero.jpg --light
#
# The cover is `a_notepad_and_a_sharp_pencil_on_a_bare_desk…` 9ca3d7 #1, a
# notepad and pencil low on a pale desk under a pink wall: Innes's pick on
# 2026-09-25 from two stand-ins, because the cover the plan briefs (a pencil
# whose shadow curves into a question mark) has not been generated. When it
# is: prep it to hero.jpg, re-run the line above, paste over this block.
#
# Light, and measured rather than assumed: the hero's mean luminance is 182,
# and the dark derivation puts that pastel wall under a #0e0d09 canvas.
# --void lands at HSL lightness 0.761, the ~0.76 of §4a. assemble() derives
# data-theme from --void's luminance, so a dark block pasted here would
# silently flip the whole deck.
PALETTE = """  --hero: url('%s/hero.jpg');

  --void          : #d8c6ac;
  --surface       : #e1d6c4;
  --surface2      : #dccdb8;
  --border        : #965e4a;
  --text          : #2a1711;
  --text-dim      : #5e3b2e;
  --accent        : #a42a00;
  --accent-bright : #711d00;
  --accent-dim    : #ef612f;
  --secondary     : #72aab3;
  --contrast      : #075544;""" % F

# ── the seven pictures ─────────────────────────────────────────────────
# One per section plus the cover. Each appears twice: whole on its divider,
# cropped to a column on its panel. POS picks which vertical slice the panel
# takes: a panel is 548x720 out of a 16:9 source painted `cover`, so it sees
# 42.6% of the width, and 'P% 50%' puts the window's left edge at P x 0.574
# of it. (The divider gets the same value but has ~6px of slack, so there it
# is a no-op.) Set by eye from renders of each crop, 2026-09-25:
#
#   1  the clip, all three ticks, and the pencil on the unticked fourth row
#   2  the alarm clock whole, both bells — Elena's alarm, at about eight
#   3  the padlock, with the key's teeth coming in at the edge
#   4  the tipped-over box and the cards it spilled
#   5  the hammer and the screwdrivers; the tools sit low, so the right-hand
#      end is the only slice with any height in it
PIC = {
    1: 's1-clipboard.jpg',
    2: 's2-clock.jpg',
    3: 's3-key-padlock.jpg',
    4: 's4-index-cards.jpg',
    5: 's5-tool-roll.jpg',
}
ACT_PIC = 'activate-notepad.jpg'
POS = {
    1: '52% 50%',
    2: '85% 50%',
    3: '78% 50%',
    4: '62% 50%',
    5: '85% 50%',
}


def panel(n, stage, side='left'):
    """A section's instruction panel: two paragraphs beside its picture."""
    return D.panel('e%d' % stage, E['e%d' % stage], 's%dt' % n, E['s%dt' % n],
                   [('s%da' % n, E['s%da' % n]),
                    ('s%db' % n, E['s%db' % n], 'dim')],
                   folder=F, pic=PIC[stage], side=side, pos=POS.get(stage))


def divider(n):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=PIC[n], pos=POS.get(n))


def sentences(*forms):
    """Every accepted spelling of a corrected sentence, with and without the
    final full stop.

    The engine's flatten() folds case, curly quotes, dashes and runs of
    whitespace, but it does not strip terminal punctuation — so "…for five
    years." and "…for five years" are two different answers and both have to
    be listed. §7: a learner who is right and marked wrong is worse than one
    who is wrong and marked right."""
    out = []
    for f in forms:
        stripped = f.rstrip('.!?')
        for v in (stripped, stripped + '.'):
            if v not in out:
                out.append(v)
    return '|'.join(out)


# ══════════════════════════════════════════════════════════════════════
#  SECTION 1 · ten sentences, ten grammar points
# ══════════════════════════════════════════════════════════════════════
# Options are never translated: they ARE the English being tested. The key
# sits at a different index each time, and never as the longest option —
# check-lesson.js measures both. This set came over from the old page
# unchanged, because it already passed: only one key ('was cooking', 11) is
# the longest option at all, by one character over 'am cooking'.
MC = [
    dict(stem='Listen! Someone ______ at the door. <em>(knock)</em>',
         options=['knocks', 'is knocking', 'knocked', 'was knocking'],
         correct=1, why='q1w'),
    dict(stem='While I ______ dinner, the phone rang. <em>(cook)</em>',
         options=['cook', 'was cooking', 'cooks', 'am cooking'],
         correct=1, why='q2w'),
    dict(stem='She ______ in Madrid since 2019. <em>(live)</em>',
         options=['lives', 'lived', 'has lived', 'is living'],
         correct=2, why='q3w'),
    dict(stem='I think Brazil ______ the tournament. <em>(win)</em>',
         options=['is winning', 'won', 'wins', 'will win'],
         correct=3, why='q4w'),
    dict(stem='This is ______ film I’ve seen this year. <em>(good)</em>',
         options=['the goodest', 'the better', 'more good', 'the best'],
         correct=3, why='q5w'),
    dict(stem='You ______ wear a seatbelt in this country — it’s the law.',
         options=['might', 'could', 'would', 'must'],
         correct=3, why='q6w'),
    dict(stem='If it ______ tomorrow, we’ll cancel the picnic. <em>(rain)</em>',
         options=['will rain', 'rained', 'would rain', 'rains'],
         correct=3, why='q7w'),
    dict(stem='If I ______ more free time, I would learn to paint. <em>(have)</em>',
         options=['have', 'will have', 'has', 'had'],
         correct=3, why='q8w'),
    dict(stem='This bridge ______ in 1889. <em>(build)</em>',
         options=['built', 'has built', 'builds', 'was built'],
         correct=3, why='q9w'),
    dict(stem='The woman ______ lives next door is a doctor.',
         options=['which', 'whose', 'where', 'who'],
         correct=3, why='q10w'),
]

# ══════════════════════════════════════════════════════════════════════
#  SECTION 2 · Elena's week — eight gaps over four slides
# ══════════════════════════════════════════════════════════════════════
# §6: "A reading passage with eight gaps becomes four slides of two." The
# passage itself is read whole on a panel first, with the answers shown, so
# the learner meets it as a text before meeting it as a test.
GAP = [
    [('Elena usually ______ at seven o’clock, but this morning she ______ '
      'because her alarm didn’t ring. <em>(get up / oversleep)</em>',
      ['gets up', 'overslept'], 'g1w')],
    [('She ______ in this apartment for almost three years now. '
      '<em>(live)</em>', ['has lived|’s lived|has been living'], 'g2aw'),
     ('Last night, while she ______ a book, her neighbour knocked on the '
      'door. <em>(read)</em>', ['was reading'], 'g2bw')],
    [('Tomorrow, Elena ______ her sister for lunch — they’ve already booked '
      'a table. <em>(meet)</em>', ['is meeting|’s meeting'], 'g3aw'),
     ('If the weather ______ nice this weekend, they’ll go to the coast. '
      '<em>(be)</em>', ['is|’s'], 'g3bw')],
    [('If the weather is nice, they ______ to the coast afterwards. '
      '<em>(go)</em>', ['will go|’ll go'], 'g4aw'),
     ('The new restaurant serves ______ fresh seafood. '
      '<em>(a lot of / much)</em>', ['a lot of|much|lots of'], 'g4bw')],
]
# The first slide carries two gaps in one row, so it needs its explanations
# per gap rather than per row — the row is teaching two different tenses and
# one shared explanation can only make one of the two points (§7).
GAP1_EXPLAINS = ['g1aw', 'g1bw']

# ══════════════════════════════════════════════════════════════════════
#  SECTION 3 · six rules, four true and two myths
# ══════════════════════════════════════════════════════════════════════
TF = [
    ('We use the Present Perfect with a specific finished time, like '
     '‘yesterday’ or ‘in 2010’.', False, 't1w'),
    ('‘Must’ and ‘have to’ can both express obligation, but only ‘have to’ '
     'has a past form (‘had to’).', True, 't2w'),
    ('In the First Conditional, we use ‘will’ in the if-clause.', False, 't3w'),
    ('Superlative adjectives are usually preceded by ‘the’.', True, 't4w'),
    ('The passive voice is formed with the verb ‘to be’ + past participle.',
     True, 't5w'),
    ('We use ‘who’ for people and ‘which’ for things in relative clauses.',
     True, 't6w'),
]

# ══════════════════════════════════════════════════════════════════════
#  SECTION 4 · chunked at the joints, never mid-phrase
# ══════════════════════════════════════════════════════════════════════
ORDER = [
    (['This house', 'was built', 'in 1990.'], 'o1w'),
    (['The man', 'who lives next door', 'is friendly.'], 'o2w'),
    (['Where', 'did you go', 'yesterday?'], 'o3w'),
    (['If I were rich,', 'I’d travel', 'the world.'], 'o4w'),
    (['This one is', 'much bigger', 'than that one.'], 'o5w'),
]

# ══════════════════════════════════════════════════════════════════════
#  SECTION 5 · one error each, and every right answer accepted
# ══════════════════════════════════════════════════════════════════════
EC = [
    ('She has lived here since five years.',
     sentences('She has lived here for five years',
               'She has lived here for 5 years',
               'She’s lived here for five years',
               "She's lived here for five years"), 'ec1w'),
    ('If I will have time, I will call you.',
     sentences('If I have time, I will call you',
               'If I have time I will call you',
               'If I have time, I’ll call you',
               "If I have time, I'll call you",
               "If I have time I'll call you"), 'ec2w'),
    ('This song is more better than the last one.',
     sentences('This song is better than the last one'), 'ec3w'),
    ('The letter was wrote by my grandmother.',
     sentences('The letter was written by my grandmother'), 'ec4w'),
    ('I have many money in my wallet.',
     sentences('I have much money in my wallet',
               'I have a lot of money in my wallet'), 'ec5w'),
    # 'That' is accepted here because tf6, four sections earlier in this same
    # test, teaches that it can replace either. The old page marked it wrong.
    ('The girl which is sitting there is my cousin.',
     sentences('The girl who is sitting there is my cousin',
               'The girl that is sitting there is my cousin'), 'ec6w'),
]


def build():
    logo = D.logo_from(TPL)
    n_mc, n_tf, n_gap, n_ec = len(MC), len(TF), len(GAP), len(EC)

    slides = "".join(
        [
            D.cover(logo, E['coverTitle'], E['coverSub'],
                    [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                     ('Count', E['chipCount'])]),

            # ── section 1 · multiple choice ────────────────────────────
            divider(1),
            panel(1, 1),
        ] + [
            D.mc(i + 1, n_mc, q, 'e1', E['e1'],
                 'q%dt' % (i + 1), E['q%dt' % (i + 1)])
            for i, q in enumerate(MC)
        ] + [
            # ── section 2 · Elena's week ───────────────────────────────
            divider(2),
            panel(2, 2, side='right'),
            D.panel('e2', E['e2'], 'storyT', E['storyT'],
                    [('storyA', E['storyA']), ('storyB', E['storyB'], 'dim')],
                    folder=F, pic=PIC[2], side='left', pos=POS.get(2)),
        ] + [
            D.gap(i + 1, n_gap, rows, None, 'e2', E['e2'],
                  'g%dt' % (i + 1), E['g%dt' % (i + 1)],
                  hint=E['gapHint'], hint_key='gapHint', width=150)
            for i, rows in enumerate(GAP)
        ] + [
            # ── section 3 · true or false ──────────────────────────────
            divider(3),
            panel(3, 3, side='right'),
        ] + [
            D.mc(i + 1, n_tf,
                 dict(stem=stmt, options=['True', 'False'],
                      correct=0 if ok else 1, why=why),
                 'e3', E['e3'], 't%dt' % (i + 1), E['t%dt' % (i + 1)],
                 ctx=E['tfStem'], ctx_key='tfStem')
            for i, (stmt, ok, why) in enumerate(TF)
        ] + [
            # ── section 4 · build the sentence ─────────────────────────
            divider(4),
            panel(4, 4),
        ] + [
            D.order(items, 'e4', E['e4'], 'o%dt' % (i + 1), E['o%dt' % (i + 1)],
                    'orderHint', E['orderHint'], why)
            for i, (items, why) in enumerate(ORDER)
        ] + [
            # ── section 5 · find the mistake ───────────────────────────
            divider(5),
            panel(5, 5, side='right'),
        ] + [
            D.gap(i + 1, n_ec,
                  [('<em>%s</em><br>______' % wrong, [answers], why)],
                  None, 'e5', E['e5'],
                  'ec%dt' % (i + 1), E['ec%dt' % (i + 1)],
                  hint=E['ecHint'], hint_key='ecHint', width=560, size=18)
            for i, (wrong, answers, why) in enumerate(EC)
        ] + [
            # ── results, then activation ───────────────────────────────
            # §10b: activation comes AFTER the results and is the last thing
            # the learner sees. The old page had no activation stage at all.
            D.results(),
            D.activate(E['actTitle'], E['actUse'],
                       ['has lived / for', 'was …-ing when', 'is meeting',
                        'if + present, will', 'was built', 'who / which',
                        'much / many', 'the best'],
                       'Speaking', E['actSpeakBrief'],
                       [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                       E['actWriteKind'], E['actWriteBrief'],
                       E['actPlaceholder'],
                       folder=F, bg=ACT_PIC),
        ])

    # The two-gap first reading slide teaches two tenses in one row, so each
    # input carries its own data-explain, appended after the row's. See §7.
    first = slides.index('data-type="gap"')
    head, tail = slides[:first], slides[first:]
    for key in GAP1_EXPLAINS:
        tail = tail.replace('<input class="gap" data-answer=',
                            '<input class="gap" data-explain="%s" data-answer='
                            % key, 1)
    slides = head + tail

    D.assemble(TPL, OUT, slides, PALETTE,
               'B1 Mixed Grammar Test', I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides' % (OUT, slides.count('<section class="slide')))


if __name__ == '__main__':
    build()
