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

House style 1 (2026-11-09, Innes: "comeback ride is the new house style
1 - adhere to its rules"; HOUSE-STYLE §000), through hs1.py, the reference
builder's machinery lifted into a module. Art: seven Midjourney renders from
2026-11-09 (picks in PLATES below), the hero cut out for the cover. One plate
per question is owed (QA/QB/QC/O below, briefs beside each): until a plate
lands its slide shows the texture field, and the build prints what is owed.

Run from the repo root:  py lesson-template/build/build_venezuela.py
"""
r"""(The house style 2 notes, kept for the record: the first rebuild was the
HS2 benchmark deck, on stand-ins.)

Run from the repo root:  py lesson-template/build/build_venezuela.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import deck as D
import hs1
import i18n_venezuela as I

TPL = 'lesson-template/lesson-template.html'
F = 'Venezuela'
OUT = 'forbes-english-venezuela.html'
TITLE = 'Used To & Be Used To — Venezuela Edition (B1)'
E = I.T['en']

# House style 1 plates: <slot>.jpg in Venezuela/, whole renders with the
# subject centred. Picks from the 2026-11-09 grids: hero 0, warm 0, used 3
# (the small guitar reads as a cuatro), beused 3, both 2, talk 0, act 3.
# POP: which subjects break out of their frame (tools/pop_plate.py), checked
# by eye on the built slides.
POP = {
    'beused': (None, 'square'),
    'both': (None, 'free'),
    'talk': (None, 'free'),
}
# The hacienda hero is a scene with no one object in it, so the cover pops
# out the radio and cuatro instead (the joropo era: what people used to do).
K = hs1.Deck(F, pop=POP, cover_slot='used', title_px=64, cover_w=44)   # DE/ES subtitles run three lines

# One plate per question, owed. Briefs for Midjourney (his style images,
# --stylize 200; HOUSE-STYLE §000 rule 2), one per slot, subject centred:
QA = [('qa-falls', 'Angel Falls dropping off a flat-topped tepui into the jungle'),
      ('qa-fire', 'a clay pot on a wood fire in a village kitchen, a gas cooker in the corner'),
      ('qa-oil', 'oil derricks on Lake Maracaibo in the 1970s boom, workers in hard hats'),
      ('qa-river', 'the wide Orinoco river winding through rainforest, one canoe'),
      ('qa-football', 'a football team in burgundy shirts celebrating a goal')]
QB = [('beused', 'the Merida cable car: in hand'),
      ('qb-night', 'a man lying awake in a city flat at night, car lights through the blinds'),
      ('qb-rig', 'an offshore oil platform at dusk, a worker on the deck'),
      ('qb-heat', 'a journalist with a notebook fanning herself in hot afternoon sun'),
      ('qb-class', 'a language classroom, students with headphones, a teacher at the board')]
QC = [('qc-lake', 'a girl swimming in a lake at sunset, stilt houses behind'),
      ('qc-dawn', 'a farmer leading cattle across the flat llanos at dawn, an oil lamp'),
      ('qc-humid', 'two tourists in sun hats wilting in tropical humidity under palms')]
O = [('o-school', 'a child with a satchel walking to school along a dusty road'),
     ('o-road', 'a small car on a winding mountain road with hairpin bends')]


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


def mcs(qs, start, total, ek, slots):
    # q['why'] is a UI_I18N key, so the explanation translates (RESOLVE gate).
    return [K.frame(D.mc(start + n, total, q, ek, E[ek], 'mcT', E['mcT']), slot,
                    text=(q['stem'], q['options']))
            for n, (q, (slot, _brief)) in enumerate(zip(qs, slots))]


def gap(rows, ek, hint_key):
    # Full width, no picture: three rows each grow an explanation line when
    # answered, and beside a picture they wrapped and ran 44-96px off the
    # canvas (answered-overflow.js, en/de/es). The slide budget wins.
    return D.gap(1, 1, [(s, a, w) for s, a, w in rows], None, ek, E[ek], 'gapT', E['gapT'],
                 hint=E[hint_key], hint_key=hint_key, size=21)


def b(key):
    return [(k, E[k]) for k in key]


def slides():
    s = [K.cover(E)]

    # ── warm-up: the benchmark's opening pair ──────────────────────────
    s.append(K.frame(D.survey('eW', E['eW'], 'svT', E['svT'], None,
                              'Name something people <strong>used to</strong> do every week that most people don’t do any more.',
                              SURVEY, hint=('svHint', E['svHint'])), 'warm'))
    s.append(K.frame(K.talk('eT', 'tk1T', TALK_1, E), 'talk'))

    # ── stage 1 · used to ──────────────────────────────────────────────
    K.stage()
    s.append(D.rules('eR', E['eR'], 'rAt', E['rAt'], [
        ('I used to + verb', b(['rA1', 'rA2', 'rA3']),
         'Venezuela <strong>used to export</strong> more oil than almost any other country.'),
        ('I didn’t use to + verb', b(['rA4']),
         'Children <strong>didn’t use to watch</strong> so much television.'),
        ('Did you use to + verb?', b(['rA5']),
         '<strong>Did</strong> your family <strong>use to make</strong> arepas on Sundays?'),
    ]))     # three rule cards: no room for a picture (texture field)
    s.append(examples('xAt', 'eX', EX_A))
    s += mcs(MC_A, 1, 5, 'e1', QA)
    s.append(gap(GAP_A, 'e1', 'gHintA'))

    # ── stage 2 · be used to ───────────────────────────────────────────
    K.stage()
    s.append(D.rules('eR', E['eR'], 'rBt', E['rBt'], [
        ('be used to + -ing', b(['rB1', 'rB2', 'rB3']),
         'People from Mérida <strong>are used to living</strong> at high altitude.'),
        ('be used to + noun', b(['rB4']),
         'He <strong>wasn’t used to</strong> the noise of the city.'),
        ('get used to', b(['rB5']),
         'After a month, she <strong>got used to</strong> the heat.'),
    ]))     # three rule cards: no room for a picture
    s.append(examples('xBt', 'eX', EX_B))
    s += mcs(MC_B, 1, 5, 'e2', QB)
    s.append(gap(GAP_B, 'e2', 'gHintB'))

    # ── stage 3 · side by side ─────────────────────────────────────────
    K.stage()
    s.append(K.frame(D.rules('eR', E['eR'], 'rCt', E['rCt'], [
        ('used to + base verb', b(['rC1', 'rC2', 'rC3']),
         'She <strong>used to wake up</strong> at 5 a.m. to catch the bus to Caracas.'),
        ('be used to + -ing', b(['rC4', 'rC5', 'rC6']),
         'She <strong>is used to waking up</strong> early — she has always lived in the countryside.'),
    ]), 'both'))
    s += mcs(MC_C, 1, 3, 'e3', QC)
    for (items, dec, why), (slot, _brief) in zip(ORDERS, O):
        s.append(K.frame(D.order(items, 'e3', E['e3'], 'orderT', E['orderT'], 'orderHint',
                                 E['orderHint'], why, decoys=dec), slot))

    # ── speaking, results, activation ──────────────────────────────────
    K.stage()
    s.append(K.frame(K.talk('eT', 'tk2T', TALK_2, E), 'act'))
    s.append(K.frame(D.results(), 'hero'))
    chips = ['got used to', 'didn’t use to', 'used to', 'Did … use to',
             'getting used to', 'is used to']
    # the activation's two panels need the full width
    s.append(D.activate(E['actTitle'], E['actUse'], chips, 'Speaking', E['actSpeakBrief'],
                        [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                        E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder']))
    return "".join(s)


def build():
    body = slides()
    n = body.count('<section class="slide')
    for c in ('en', 'de', 'es'):
        assert str(n) in I.T[c]['chipCount'], '%s chipCount %r, deck has %d' % (c, I.T[c]['chipCount'], n)
    K.assemble(OUT, body, TITLE, I, ('en', 'de', 'es'))


if __name__ == '__main__':
    build()
