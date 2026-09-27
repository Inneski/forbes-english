# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Test, Part 2, rebuilt as a 16:9 deck in house style 2.

The sibling of `build_mixedgrammar1.py`, built the same way so the two parts
of one test read as a pair: each section opens on its picture whole
(`D.divider()`), then the same picture cropped to a full-opacity column beside
the instructions (`D.panel()`), then its questions. Panels alternate sides.
The question slides carry no `bg=`, so they sit on the COVER's wash (house
rule 3) — which is why the cover has to be calm in the middle.

`forbes-english-b1-mixed-grammar-test-part2.html` was the same 720px scrolling
column as Part 1: Fraunces and Work Sans, a hand-picked palette, the hero in a
card, a Spanish-only hover glossary, no language switcher, no activation.

Art: the desert family, as `docs/PLAN-mixed-grammar-b1.md` §5 gives it — one
style per deck, Noma Bar for Part 1, the American desert roadside for Part 2.
The hero is the gas station already in the repo (renamed hero.jpg); the six
plates are Innes's 09-24 renders from incoming/.

Content: all 35 scored items, from the audit `19b39ed` made of the old page for
the editorial builder (`build_mixed_b1.py`, which this supersedes). Its fixes
carry over, and its English, German and Spanish explanations are ported into
`i18n_mixedgrammar2.py` — they already follow the house rule: grammar forms
in CAPS, cited words in double quotes.

  * The story said Diego had "forgotten his passport at his parents' house".
    FORGET does not take a place; LEAVE does.
  * It said he had "already checked in online" a week before the flight,
    which no airline allows. He has chosen his seat.
  * Error correction 6 was an error nobody makes ("whose car was stolen it").
    It is a doubled possessive now, "whose his car", which learners do make.
  * Accepted answers were too narrow: "had recommended", "is going to fly",
    "might miss", "I'd buy", "the money" are all right and were marked wrong.
    Story gap 1 also takes HAS TRAVELLED: "has travelled every summer, but
    this year…" is good English, and the explanation says so.
  * A typed correction without its full stop, or without its comma, was
    marked wrong. `sentences()` accepts both.

Titles name the scene, never the grammar or the answer. Part 1 shipped with
"If it rains" over an item whose key was "rains"; that is fixed there too.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_mixedgrammar2 as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-b1-mixed-grammar-test-part2.html'
F = 'MixedGrammarPart2'

E = I.T['en']          # one source for the English; see the i18n docstring

# ── PALETTE — derived from the cover, every contrast row PASS ──────────
#   python3 lesson-template/extract-palette.py MixedGrammarPart2/hero.jpg --light
#
# Light, measured: the hero's mean luminance is 148, a pale dusk sky over a
# dark station, and the dark derivation puts that sky under a #121410
# canvas. --void lands at HSL lightness 0.761, the ~0.76 of §4a.
PALETTE = """  --hero: url('%s/hero.jpg');

  --void          : #d8ccac;
  --surface       : #e1dac4;
  --surface2      : #dcd2b8;
  --border        : #965d4a;
  --text          : #2a1711;
  --text-dim      : #5e3a2e;
  --accent        : #a53c19;
  --accent-bright : #80280c;
  --accent-dim    : #d77f62;
  --secondary     : #a3bcc1;
  --contrast      : #136350;""" % F

# ── the seven pictures ─────────────────────────────────────────────────
# A panel is 548x720 out of a 16:9 source painted `cover`: it sees 42.6% of
# the width, and 'P% 50%' puts the window's left edge at P x 0.574 of it.
# Set by eye from renders of each crop, 2026-09-25:
#
#   1  the arrow sign pointing back across the road, and the pickup
#   2  the moka pot and the cups on the sill, sun behind — Diego's morning
#   3  the figure standing where the sunlit lane and the shadowed one split
#   4  the locomotive and its line of coloured cars, parts in an order
#   5  the man on the ladder straightening the crooked shutter
PIC = {
    1: 's1-crossroads.jpg',
    2: 's2-window.jpg',
    3: 's3-fork.jpg',
    4: 's4-siding.jpg',
    5: 's5-shutter.jpg',
}
ACT_PIC = 'activate-tailgate.jpg'
POS = {
    1: '92% 50%',
    2: '20% 50%',
    3: '50% 50%',
    4: '75% 50%',
    5: '88% 50%',
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
    """Every accepted spelling of a corrected sentence: with and without the
    final full stop, and with and without its commas.

    The engine's flatten() folds case, curly quotes, dashes and runs of
    whitespace, but not punctuation — so "…a house." and "…a house" are two
    answers, and so are "If I had money, I'd…" and "If I had money I'd…".
    §7: a learner who is right and marked wrong is worse than one who is
    wrong and marked right. The first form is the one shown as "Answer: …"."""
    out = []
    for f in forms:
        bare = f.rstrip('.!?')
        for v in (bare, bare + '.', bare.replace(',', ''),
                  bare.replace(',', '') + '.'):
            if v not in out:
                out.append(v)
    return '|'.join(out)


# ══════════════════════════════════════════════════════════════════════
#  SECTION 1 · ten new sentences, ten grammar points
# ══════════════════════════════════════════════════════════════════════
# Options are never translated: they ARE the English being tested. The key
# is never the longest option by the gate's measure, and sits at a different
# index each time (the engine shuffles at runtime as well).
MC = [
    dict(stem='Be quiet! The baby ______. <em>(sleep)</em>',
         options=['sleeps', 'is sleeping', 'slept', 'was sleeping'],
         correct=1, why='q1w'),
    dict(stem='The lights went out while we ______ a film. <em>(watch)</em>',
         options=['were watching', 'watch', 'watches', 'are watching'],
         correct=0, why='q2w'),
    dict(stem='They ______ each other for ten years now. <em>(know)</em>',
         options=['know', 'knew', 'have known', 'are knowing'],
         correct=2, why='q3w'),
    dict(stem='I promise I ______ you tomorrow. <em>(help)</em>',
         options=['am helping', 'will help', 'helped', 'help'],
         correct=1, why='q4w'),
    dict(stem='Of all the cities I’ve visited, Tokyo is ______. <em>(busy)</em>',
         options=['busier', 'more busy', 'the most busiest', 'the busiest'],
         correct=3, why='q5w'),
    dict(stem='You ______ smoke in here — it’s strictly forbidden.',
         options=['mustn’t', 'might not', 'don’t have to', 'wouldn’t'],
         correct=0, why='q6w'),
    dict(stem='If you ______ the instructions, the machine won’t break. <em>(follow)</em>',
         options=['will follow', 'followed', 'follow', 'would follow'],
         correct=2, why='q7w'),
    dict(stem='If she ______ taller, she could join the team. <em>(be)</em>',
         options=['is', 'will be', 'has been', 'were'],
         correct=3, why='q8w'),
    dict(stem='The Mona Lisa ______ by Leonardo da Vinci. <em>(paint)</em>',
         options=['painted', 'was painted', 'paints', 'has painted'],
         correct=1, why='q9w'),
    dict(stem='The book ______ I’m reading is fascinating.',
         options=['who', 'where', 'which', 'whose'],
         correct=2, why='q10w'),
]
# The one word a B1 learner may not have, glossed on the slide that needs it
# — "strictly forbidden" is what decides between MUSTN'T and DON'T HAVE TO.
MC_GLOSS = {6: 'q6g'}

# ══════════════════════════════════════════════════════════════════════
#  SECTION 2 · Diego's trip — eight gaps over three slides of two rows
# ══════════════════════════════════════════════════════════════════════
# The passage is read whole on a panel first, WITH ITS GAPS, so the learner
# meets it as a text before meeting it as a test. (Part 1's first version
# printed the answers on that panel, one slide before the questions.)
GAP = [
    [('Diego ______ <em>(travel)</em> to Italy every summer, but this year '
      'he’s trying something different.',
      ['travels|has travelled|has traveled|’s travelled|’s traveled'], 'g1aw'),
     ('Last month, he ______ <em>(book)</em> a flight to Lisbon after a friend '
      '______ <em>(recommend)</em> it.',
      ['booked', 'recommended|had recommended|’d recommended'], 'g1bw')],
    [('He ______ <em>(never / visit)</em> Portugal before, so he’s very '
      'excited.', ['has never visited|’s never visited'], 'g2aw'),
     ('Last week, while he ______ <em>(pack)</em> his suitcase, he realised '
      'he’d left his passport at his parents’ house.', ['was packing'], 'g2bw')],
    [('Next Friday, Diego ______ <em>(fly)</em> from Madrid to Lisbon — '
      'he’s already chosen his seat.',
      ['is flying|’s flying|is going to fly|’s going to fly'], 'g3aw'),
     ('If the flight ______ <em>(be)</em> delayed, he ______ <em>(miss)</em> '
      'his hotel check-in time.',
      ['is|’s', 'will miss|’ll miss|is going to miss|’s going to miss|'
                'might miss|could miss|may miss'], 'g3bw')],
]

# ══════════════════════════════════════════════════════════════════════
#  SECTION 3 · six rules, four true and two myths
# ══════════════════════════════════════════════════════════════════════
# English, like Part 1's: the learner judges a rule about English, stated in
# English. The explanation after it translates.
TF = [
    ('The Present Continuous can describe a future arrangement, like '
     '“I’m flying to Rome on Monday.”', True, 't1w'),
    ('“Mustn’t” and “don’t have to” mean the same thing.', False, 't2w'),
    ('In the second conditional we often use “were” instead of “was” after '
     'I, he, she and it.', True, 't3w'),
    ('Two-syllable adjectives always take “more”, never “-er”.', False, 't4w'),
    ('The passive of “People speak English here” is “English is spoken '
     'here.”', True, 't5w'),
    ('“Whose” is used to talk about possession.', True, 't6w'),
]

# ══════════════════════════════════════════════════════════════════════
#  SECTION 4 · chunked at the joints, never mid-phrase
# ══════════════════════════════════════════════════════════════════════
# Each cut is where the grammar is: the auxiliary that inverts in a
# question, the relative clause as one block, the two halves of a
# conditional. Capitals and the final stop leave exactly one order.
ORDER = [
    (['Was', 'this painting', 'painted', 'by a famous artist?'], 'o1w'),
    (['The restaurant', 'where we had dinner', 'was excellent.'], 'o2w'),
    (['How long', 'have', 'you', 'lived here?'], 'o3w'),
    (['If he', 'had more time,', 'he would', 'exercise every day.'], 'o4w'),
    (['The more', 'you practise,', 'the better', 'you become.'], 'o5w'),
]

# ══════════════════════════════════════════════════════════════════════
#  SECTION 5 · one error each, and every right answer accepted
# ══════════════════════════════════════════════════════════════════════
EC = [
    ('I am agreeing with you completely.',
     sentences('I agree with you completely',
               'I completely agree with you',
               'I agree completely with you'), 'ec1w'),
    ('She is married with a doctor.',
     sentences('She is married to a doctor',
               'She’s married to a doctor'), 'ec2w'),
    ('If I would have money, I would buy a house.',
     sentences('If I had money, I would buy a house',
               'If I had money, I’d buy a house',
               'If I had the money, I would buy a house',
               'If I had the money, I’d buy a house'), 'ec3w'),
    ('This exercise is more easy than the last one.',
     sentences('This exercise is easier than the last one'), 'ec4w'),
    ('The email was sent for the manager yesterday.',
     sentences('The email was sent by the manager yesterday'), 'ec5w'),
    ('This is the man whose his car was stolen.',
     sentences('This is the man whose car was stolen'), 'ec6w'),
]


def build():
    logo = D.logo_from(TPL)
    n_mc, n_tf, n_gap, n_ec = len(MC), len(TF), len(GAP), len(EC)

    def mc_slide(i, q):
        g = MC_GLOSS.get(i + 1)
        return D.mc(i + 1, n_mc, q, 'e1', E['e1'],
                    'q%dt' % (i + 1), E['q%dt' % (i + 1)],
                    ctx=E[g] if g else None, ctx_key=g)

    slides = "".join(
        [
            D.cover(logo, E['coverTitle'], E['coverSub'],
                    [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                     ('Count', E['chipCount'])]),

            # ── section 1 · multiple choice ────────────────────────────
            divider(1),
            panel(1, 1),
        ] + [mc_slide(i, q) for i, q in enumerate(MC)] + [
            # ── section 2 · Diego's trip ───────────────────────────────
            divider(2),
            panel(2, 2, side='right'),
            D.panel('e2', E['e2'], 'storyT', E['storyT'],
                    [('storyA', E['storyA']), ('storyB', E['storyB'], 'dim')],
                    folder=F, pic=PIC[2], side='left', pos=POS.get(2)),
        ] + [
            D.gap(i + 1, n_gap, rows, None, 'e2', E['e2'],
                  'g%dt' % (i + 1), E['g%dt' % (i + 1)],
                  hint=E['g%dh' % (i + 1)], hint_key='g%dh' % (i + 1),
                  width=150)
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
                       ['I’m flying', 'if it rains', 'mustn’t', 'don’t have to',
                        'was …-ing', 'have known', 'the best', 'whose'],
                       'Speaking', E['actSpeakBrief'],
                       [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                       E['actWriteKind'], E['actWriteBrief'],
                       E['actPlaceholder'],
                       folder=F, bg=ACT_PIC),
        ])

    # The count on the cover chip is typed in three languages; make a
    # mismatch fail here rather than on the live page.
    n = slides.count('<section class="slide')     # the cover is "slide is-active"
    for code in I.T:
        assert I.T[code]['chipCount'].split()[0] == str(n), (
            'chipCount in %s says %s, the deck has %d slides'
            % (code, I.T[code]['chipCount'], n))

    D.assemble(TPL, OUT, slides, PALETTE,
               'B1 Mixed Grammar Test — Part 2', I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides' % (OUT, n))


if __name__ == '__main__':
    build()
