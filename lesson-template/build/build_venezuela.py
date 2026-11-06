# -*- coding: utf-8 -*-
"""Used To & Be Used To — Venezuela Edition (B1). House style 2, the
benchmark build.

Rebuilt 2026-11-06 from the scrolling page of the same name (Innes: "find
other on forbes that are not house style and make them house style 2 ...
study the graphic composition of these as a benchmark"). It is the first
deck composed against the ENGHUB benchmark Innes supplied, and that deck
("How to Break Habits", B1-B2) teaches the same grammar, so its sequence is
followed closely: a top-five warmer, a field of speech bubbles, the rule as
pill-tab cards, one form per slide, a comparison of the two structures side
by side, and the speaking field again at the end, now with the target
language picked out in the accent.

Everything the old page taught is here: the two rule blocks with their
forms, all twelve example sentences with their notes, the comparison table,
all thirteen multiple-choice items. Added: two gap slides (six rows) and two
sentence builds, because the old page only ever asked the learner to
RECOGNISE the forms, plus the two discussion fields and the activation.

Fixed in the content, found in the audit (the old page shipped them):
  * Q2 "families used to cook everything with corn flour — a tradition passed
    down through many generations": a living tradition is still true, which
    is exactly what USED TO cannot say. Now a wood fire that gas replaced.
  * Q5 "the national team didn't use to qualify — they have still never
    reached the finals": DIDN'T USE TO implies that it happens now, and the
    clause after the dash says it does not. Now a team that has improved.
  * Q12 "farmers ___ rising before dawn": WERE USED TO was also correct as
    written. "today" makes ARE the only answer.
  * Q13's key built "many say they used to visit only in December", which
    says nothing, and a distractor built "used to only visit only". Rewritten
    so USED TO marks a pattern that has changed.
  * Example "visitors aren't used to eating such spicy food — Venezuelan
    cuisine can surprise foreigners": Venezuelan food is famously mild. Now
    arepas for breakfast.
  * Q6's distractor "were used to living" doubled the verb in the stem.
  * Q7's explanation said DIDN'T USE TO "would need a base verb, not -ing";
    there is no -ing in that sentence, it is a noun (THE NOISE).

Art: the only picture on disk is a 1200x671 library card, below the 1400px
floor, so every slot is a stand-in (tools/make_standin.py) with its brief
recorded for the shopping list (tools/standins.py). Drop the real plates in
Venezuela/ under the slot names and re-run; deck.plate() takes them over the
stand-ins without a code change. Re-derive the palette when the hero lands.

Run from the repo root:  py lesson-template/build/build_venezuela.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import deck as D
import i18n_venezuela as I
import make_standin

TPL = 'lesson-template/lesson-template.html'
F = 'Venezuela'
OUT = 'forbes-english-venezuela.html'
TITLE = 'Used To & Be Used To — Venezuela Edition (B1)'
E = I.T['en']

# Every picture the deck needs: cover, one per section, the two speaking
# fields, the activation. The brief is the shopping-list line for the real
# plate — an idea, not a scene (the Noma Bar rule in the revamp list).
ART = {
    'hero':   ('time', 'a hammock strung on a hacienda porch, the flat llanos beyond, one palm'),
    'warm':   ('quiz', 'a rotary telephone, a folded paper map and a stack of letters on a shelf: things people used to use'),
    'used':   ('music', 'an old valve radio on a windowsill with a harp leaning beside it, the joropo era'),
    'beused': ('mountain', 'a cable car climbing to a high Andean town, thin air, small houses on the slope'),
    'both':   ('build', 'a pair of worn rubber work boots beside a pair of new city shoes'),
    'talk':   ('talk', 'two figures in silhouette on a plaza bench under a mango tree, a speech bubble between them'),
    'act':    ('pair', 'two stools at a café counter with two small cups of cafecito'),
}
make_standin.ensure(F, ART, scheme='warm', deck=OUT)

# py lesson-template/extract-palette.py Venezuela/standin-hero.jpg --paper
# (2026-11-06; every row PASS). Re-derive from hero.jpg when it lands.
PALETTE_BODY = """
  --void          : #fcfbf9;
  --surface       : #f2eee5;
  --surface2      : #f7f5f0;
  --border        : #d0bc95;
  --text          : #231d13;
  --text-dim      : #595140;
  --accent        : #8f6003;
  --accent-bright : #694600;
  --accent-dim    : #e6d4b2;
  --secondary     : #3c9d92;
  --contrast      : #12697d;"""


def palette(hero_ref):
    return "  --hero: url('%s');\n%s" % (hero_ref, PALETTE_BODY)


# ── content ────────────────────────────────────────────────────────────
MC_A = [
    dict(stem='Angel Falls ___ the tallest waterfall in the world — and it still holds that record today.',
         options=['has always been', 'used to be', 'is used to be', 'would use to be'], correct=0, why='q1w'),
    dict(stem='Venezuelan families ___ cook over a wood fire — now most kitchens have a gas cooker.',
         options=['use to', 'used to', 'are used to', 'did used to'], correct=1, why='q2w'),
    dict(stem='The oil industry ___ employ hundreds of thousands of workers during the 1970s boom.',
         options=['was using to', 'used to', 'use to', 'used to being'], correct=1, why='q3w'),
    dict(stem='“___ the Orinoco River ___ look different in ancient times?” the professor asked.',
         options=['Did … use to', 'Used … to', 'Was … used to', 'Did … used to'], correct=0, why='q4w'),
    dict(stem='The national team ___ win many matches — but in recent years it has become far more competitive.',
         options=['used to not', 'not used to', 'didn’t use to', 'hasn’t used to'], correct=2, why='q5w'),
]
MC_B = [
    dict(stem='People from Mérida ___ living at high altitude — the thin air feels completely normal to them.',
         options=['used to', 'are used to', 'use to', 'were use to'], correct=1, why='q6w'),
    dict(stem='When he first moved to Caracas, he ___ the constant noise of the city — it kept him awake at night.',
         options=['didn’t use to', 'used to not hear', 'wasn’t used to', 'isn’t used to'], correct=2, why='q7w'),
    dict(stem='The oil engineers ___ working long offshore shifts — it had been their routine for over twenty years.',
         options=['used to work', 'were used to', 'are used to', 'got used to work'], correct=1, why='q8w'),
    dict(stem='After six months in Venezuela, the journalist finally ___ the intense afternoon heat.',
         options=['used to', 'was used to', 'got used to', 'is used to'], correct=2, why='q9w'),
    dict(stem='“___ your students ___ learning with so many different accents now?” the director asked.',
         options=['Are … used to', 'Do … use to', 'Were … used to', 'Did … use to'], correct=0, why='q10w'),
]
MC_C = [
    dict(stem='She ___ swim in Lake Maracaibo as a child, but now she ___ living far from the water.',
         options=['used to / is used to', 'was used to / used to', 'is used to / used to', 'used to / used to'],
         correct=0, why='q11w'),
    dict(stem='Farmers in the Llanos ___ getting up before dawn today — but in the 1960s many of them ___ have electricity.',
         options=['are used to / didn’t use to', 'used to / weren’t used to', 'get used to / used to not',
                  'were used to / didn’t use to'], correct=0, why='q12w'),
    dict(stem='Tourists from cold countries ___ such intense humidity, and many of them ___ come only in December — now they come all year.',
         options=['aren’t used to / used to', 'didn’t use to feel / are used to', 'aren’t used to / are used to',
                  'used to / are used to'], correct=0, why='q13w'),
]
for q in MC_A + MC_B + MC_C:
    q['stem'] = q['stem'].replace('___', '____')
D.assert_no_key_is_longest(MC_A + MC_B + MC_C)

APOS = lambda a: '|'.join(sorted({a, a.replace('’', "'"), a.replace("'", '’')}))
GAP_A = [
    ('I ______ (live) in Caracas, but now I live in Madrid.', ['used to live'], 'g1w'),
    ('We ______ (not / have) a car when I was a child — we went everywhere by bus.',
     [APOS('didn’t use to have') + '|did not use to have'], 'g2w'),
    ('______ you ______ (play) outside after school when you were young?', ['Did', 'use to play'], 'g3w'),
]
GAP_B = [
    ('My grandmother ______ (cook) for twelve people — she does it every Sunday, so it’s easy for her.',
     ['is used to cooking'], 'g4w'),
    ('When I first moved to Mérida, I ______ the cold mornings.',
     [APOS('wasn’t used to') + '|was not used to'], 'g5w'),
    ('At first the heat was terrible, but after a month we ______ used to it.', ['got'], 'g6w'),
]

EX_A = [  # label key, English sentence, note key
    ('xA1l', 'Venezuela <strong>used to be</strong> one of the wealthiest countries in Latin America.', 'xA1n'),
    ('xA2l', 'Tourists <strong>used to flock</strong> to Angel Falls from every corner of the world.', 'xA2n'),
    ('xA3l', 'Families <strong>used to gather</strong> on Sundays to make arepas from scratch together.', 'xA3n'),
    ('xA4l', 'The country <strong>used to export</strong> more crude oil than almost any other nation on Earth.', 'xA4n'),
    ('xA5l', 'Children <strong>didn’t use to watch</strong> so much television — they played outside until dark.', 'xA5n'),
    ('xA6l', 'Joropo music <strong>used to fill</strong> the airwaves every evening across the whole country.', 'xA6n'),
]
EX_B = [
    ('xB1l', 'People from Mérida <strong>are used to living</strong> at high altitude — the thin air feels normal to them.', 'xB1n'),
    ('xB2l', 'Oil workers <strong>were used to spending</strong> long shifts offshore, far from their families in Maracaibo.', 'xB2n'),
    ('xB3l', 'Visitors <strong>aren’t used to eating</strong> arepas for breakfast — but after a week they love them.', 'xB3n'),
    ('xB4l', '“<strong>Are</strong> you <strong>used to driving</strong> on mountain roads?” she asked the new guide from the city.', 'xB4n'),
    ('xB5l', 'After years in Caracas, he <strong>got used to dealing</strong> with the sudden tropical rainstorms.', 'xB5n'),
    ('xB6l', 'She <strong>is used to hearing</strong> salsa from the neighbours every Friday night — it no longer bothers her.', 'xB6n'),
]

SURVEY = [('writing letters', 1), ('buying a newspaper', 2), ('using a phone box', 3),
          ('renting films from a video shop', 4), ('printing holiday photos', 5)]

TALK_1 = [
    'What is one thing you did every day as a child?',
    'Which habit from your childhood do you still have?',
    'What feels normal to you now that felt strange at first?',
    'Is it harder to start a good habit or to stop a bad one?',
    'What did your town look like twenty years ago?',
    'What did you have to learn when you started a new job or school?',
]
TALK_2 = [
    'What is something you <strong>used to do</strong> as a child that you don’t do any more?',
    '<strong>Are you used to</strong> the weather where you live, or did it take time to <strong>get used to</strong>?',
    'What food <strong>did</strong> your family <strong>use to</strong> eat on special days?',
    'What <strong>are you used to doing</strong> every morning before work or class?',
    'Is there anything you will never <strong>get used to</strong>? Why?',
    'What <strong>used to be</strong> in your street that isn’t there now?',
    'Is it easier to <strong>get used to</strong> change when you are young, or older?',
    'What <strong>didn’t</strong> you <strong>use to</strong> like that you like now?',
]

ORDERS = [
    (['Did', 'you', 'use to', 'walk', 'to school?'], ['used to'], 'o1w'),
    (['She', 'isn’t', 'used to', 'driving', 'on mountain roads.'], ['drive'], 'o2w'),
]


# ── slide helpers ──────────────────────────────────────────────────────
def examples(title_key, eyebrow_key, rows):
    cards = "\n          ".join(
        '<div class="card" style="padding:18px 22px">'
        '<span class="chip" style="background:var(--void);font-size:11px" data-i18n="%s">%s</span>'
        '<p class="prose" style="margin-top:10px;font-size:18px;line-height:1.45">%s</p>'
        '<p class="prose dim" style="margin-top:6px;font-size:15.5px;line-height:1.4" data-i18n="%s">%s</p>'
        '</div>' % (lk, E[lk], sent, nk, E[nk]) for lk, sent, nk in rows)
    return '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols cols-3" style="gap:16px">
          %s
        </div>
      </div>
    </section>
''' % (eyebrow_key, E[eyebrow_key], title_key, E[title_key], cards)


def mcs(qs, start, total, ek, slot, side=None):
    # q['why'] is a UI_I18N key, so the explanation translates (RESOLVE gate).
    return [D.art(D.mc(start + n, total, q, ek, E[ek], 'mcT', E['mcT']), F, slot, side=side)
            for n, q in enumerate(qs)]


def gap(rows, ek, hint_key):
    # Full width, no picture: three rows each grow an explanation line when
    # answered, and beside a picture they wrapped and ran 44-96px off the
    # canvas (answered-overflow.js, en/de/es). The slide budget wins.
    return D.gap(1, 1, [(s, a, w) for s, a, w in rows], None, ek, E[ek], 'gapT', E['gapT'],
                 hint=E[hint_key], hint_key=hint_key, size=21)


def b(key):
    return [(k, E[k]) for k in key]


def slides():
    cover, hero_ref = D.hs2_cover(D.logo_from(TPL), E['coverTitle'], E['coverSub'],
                                  [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                                   ('Count', E['chipCount'])], F)
    s = [cover]

    # ── warm-up: the benchmark's opening pair ──────────────────────────
    s.append(D.art(D.survey('eW', E['eW'], 'svT', E['svT'], None,
                            'Name something people <strong>used to</strong> do every week that most people don’t do any more.',
                            SURVEY, hint=('svHint', E['svHint'])), F, 'warm', side='left'))
    s.append(D.art(D.bubbles('eT', E['eT'], 'tk1T', E['tk1T'], [(None, p) for p in TALK_1], cols=3),
                   F, 'talk'))

    # ── stage 1 · used to ──────────────────────────────────────────────
    s.append(D.rules('eR', E['eR'], 'rAt', E['rAt'], [
        ('I used to + verb', b(['rA1', 'rA2', 'rA3']),
         'Venezuela <strong>used to export</strong> more oil than almost any other country.'),
        ('I didn’t use to + verb', b(['rA4']),
         'Children <strong>didn’t use to watch</strong> so much television.'),
        ('Did you use to + verb?', b(['rA5']),
         '<strong>Did</strong> your family <strong>use to make</strong> arepas on Sundays?'),
    ]))
    s.append(examples('xAt', 'eX', EX_A))
    s += mcs(MC_A, 1, 5, 'e1', 'used')
    s.append(gap(GAP_A, 'e1', 'gHintA'))

    # ── stage 2 · be used to ───────────────────────────────────────────
    s.append(D.rules('eR', E['eR'], 'rBt', E['rBt'], [
        ('be used to + -ing', b(['rB1', 'rB2', 'rB3']),
         'People from Mérida <strong>are used to living</strong> at high altitude.'),
        ('be used to + noun', b(['rB4']),
         'He <strong>wasn’t used to</strong> the noise of the city.'),
        ('get used to', b(['rB5']),
         'After a month, she <strong>got used to</strong> the heat.'),
    ]))
    s.append(examples('xBt', 'eX', EX_B))
    s += mcs(MC_B, 1, 5, 'e2', 'beused', side='left')
    s.append(gap(GAP_B, 'e2', 'gHintB'))

    # ── stage 3 · side by side ─────────────────────────────────────────
    s.append(D.rules('eR', E['eR'], 'rCt', E['rCt'], [
        ('used to + base verb', b(['rC1', 'rC2', 'rC3']),
         'She <strong>used to wake up</strong> at 5 a.m. to catch the bus to Caracas.'),
        ('be used to + -ing', b(['rC4', 'rC5', 'rC6']),
         'She <strong>is used to waking up</strong> early — she has always lived in the countryside.'),
    ]))
    s += mcs(MC_C, 1, 3, 'e3', 'both')
    for items, dec, why in ORDERS:
        s.append(D.art(D.order(items, 'e3', E['e3'], 'orderT', E['orderT'], 'orderHint',
                               E['orderHint'], why, decoys=dec), F, 'both', side='left'))

    # ── speaking, results, activation ──────────────────────────────────
    s.append(D.bubbles('eT', E['eT'], 'tk2T', E['tk2T'], [(None, p) for p in TALK_2], cols=4))
    s.append(D.results())
    chips = ['got used to', 'didn’t use to', 'used to', 'Did … use to',
             'getting used to', 'is used to']
    s.append(D.art(D.activate(E['actTitle'], E['actUse'], chips, 'Speaking', E['actSpeakBrief'],
                              [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                              E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder']),
                   F, 'act'))
    return "".join(s), hero_ref


def build():
    s, hero_ref = slides()
    D.assemble(TPL, OUT, s, palette(hero_ref), TITLE, I, langs=('en', 'de', 'es'), style='hs2')
    n = s.count('<section class="slide')
    print('wrote %s — %d slides' % (OUT, n))


if __name__ == '__main__':
    build()
