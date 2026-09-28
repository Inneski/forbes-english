# -*- coding: utf-8 -*-
"""Contingency Plans & Trade-offs (C1), rebuilt as a 16:9 panel deck
("house style 2").

`contingency-trade-offs-vocab.html` was a 720px scrolling quiz: 28 multiple-
choice questions in three sections, then a 58-item glossary that only
appeared after the last question. Everything survives. The glossary is now
TAUGHT first, in three thematic stages of cards, before the test instead of
after it; each stage ends in a five-pair match on words the quiz never
tested, so every one of the 58 is either practised or tested.

**Style 2.** Art: six slot plates briefed in
docs/ARTWORK-contingency-trade-offs.md; until they exist this writes a
gitignored preview on the placeholders below. The four `Construction3/` plates (flat-vector site scenes: the
unfinished villa, the crane hook against a red sun, the tower crane in
cloud, the four-panel strip) each open a stage at full bleed and then own a
panel column beside that stage's introduction. Panels alternate sides.

**Content fixed in the rebuild** (learner-facing text never mentions it):
- Level: the page header said B2, the catalogue and the SEO say C1. C1.
- MC keys that were the only longest option (the checker's rule): moisture,
  firmness, arduous and persuasive; and the three items keyed "contingency
  plan" / "take for granted" against one-word options. Distractors
  lengthened or swapped for longer taught phrases ("post hoc review",
  "exaggerate the risk of"), keys untouched.
- "A 'trade-off' means ..." explained a noun for an item that tests the verb
  "trade off". The explanation now gives both.
- "We noticed a shortfall between production capacity and actual demand" —
  a shortfall is OF something, not between two things. Rewritten.
- "The delay was completely unintended" — no delay is ever intended, so the
  item tested nothing. Now an unintended side effect.
- "This building was never designed with insulation, so we need to retrofit
  a vapour barrier" — insulation is not a vapour barrier. Rewritten.
- "working in parallel , testing" had a stray space before the comma.
- Glossary: "compromised" gave only "settled a dispute", in a construction
  lesson where "a compromised structure" is the meaning learners meet;
  "conduct" gave only "lead or guide", not "conduct a survey"; "stuck" gave
  only the past of "stick" (pierce); "current" was just "present". Each now
  has both senses.
- Explanations: cited words in double quotes (house rule), not single.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_contingencytradeoffs as I

TPL = 'lesson-template/lesson-template.html'
LIVE = 'contingency-trade-offs-vocab.html'
PREVIEW = '_contingency-trade-offs-vocab.html'   # gitignored (leading underscore)
F = 'Construction3'

# Innes, 2026-09-27: "u will need artwork". The deck ships on the six plates
# briefed in docs/ARTWORK-contingency-trade-offs.md, one per slot. Until every
# one is on disk the builder writes the gitignored PREVIEW only, laid out on
# the four staged site pictures as placeholders — the Mixed Grammar precedent.
SLOTS = ('plate-cover', 'plate-plans', 'plate-site', 'plate-people',
         'plate-test', 'plate-act')
PLACEHOLDER = {'plate-cover': 'hero.jpg', 'plate-plans': 'a.jpg',
               'plate-site': 'hero.jpg', 'plate-people': 'b.jpg',
               'plate-test': 'c.jpg', 'plate-act': 'hero.jpg'}
READY = all(os.path.exists(os.path.join(F, s + '.jpg')) for s in SLOTS)
PIC = {s: (s + '.jpg') if READY else PLACEHOLDER[s] for s in SLOTS}
OUT = LIVE if READY else PREVIEW
HERO, SUN, CLOUD, STRIP = PIC['plate-cover'], PIC['plate-plans'], PIC['plate-people'], PIC['plate-test']
SITE, ACT = PIC['plate-site'], PIC['plate-act']

E = I.T['en']

# py lesson-template/extract-palette.py Construction3/plate-cover.jpg
PALETTE = """  --hero: url('%s/%s');

  --void          : #0b100e;
  --surface       : #131f1b;
  --surface2      : #1b2b26;
  --border        : #9a4d3b;
  --text          : #f5f2f2;
  --text-dim      : #bfa8a3;
  --accent        : #e67055;
  --accent-bright : #f3a290;
  --accent-dim    : #bd3f22;
  --secondary     : #31494e;
  --contrast      : #1dedb0;""" % (F, HERO)

# (headword, definition key) per card slide, three per stage row
VOCAB = {
    1: [('contingency plan', 'g_contingency'), ('ad hoc', 'g_adhoc'),
        ('post hoc', 'g_posthoc'), ('in parallel', 'g_parallel'),
        ('trade off', 'g_tradeoff'), ('shortfall', 'g_shortfall')],
    2: [('unintended', 'g_unintended'), ('actual', 'g_actual'),
        ('current', 'g_current'), ('requirement', 'g_requirement'),
        ('assumption', 'g_assumption'), ('reassess', 'g_reassess')],
    3: [('threshold', 'g_threshold'), ('precaution', 'g_precaution'),
        ('reliable', 'g_reliable'), ('primarily', 'g_primarily'),
        ('delay', 'g_delay'), ('trial', 'g_trial')],
    4: [('moisture', 'g_moisture'), ('firmness', 'g_firmness'),
        ('dense', 'g_dense'), ('homogeneous', 'g_homogeneous'),
        ('resilient', 'g_resilient'), ('fire-retardant', 'g_fireretardant')],
    5: [('mouldy', 'g_mouldy'), ('hazardous', 'g_hazardous'),
        ('width', 'g_width'), ('retrofit', 'g_retrofit'),
        ('remove', 'g_remove'), ('take off', 'g_takeoff')],
    6: [('chain', 'g_chain'), ('carpet', 'g_carpet'), ('stuck', 'g_stuck'),
        ('locate', 'g_locate'), ('audible', 'g_audible'),
        ('appropriate', 'g_appropriate')],
    7: [('deserve', 'g_deserve'), ('tell', 'g_tell'),
        ('take for granted', 'g_granted'), ('concern', 'g_concern'),
        ('concerns', 'g_concerns'), ('competitor', 'g_competitor')],
    8: [('exhaustion', 'g_exhaustion'), ('arduous', 'g_arduous'),
        ('monotonous', 'g_monotonous'), ('manageable', 'g_manageable'),
        ('agitated', 'g_agitated'), ('nightmare', 'g_nightmare')],
    9: [('startle', 'g_startle'), ('provoke', 'g_provoke'),
        ('exaggerate', 'g_exaggerate'), ('persuade', 'g_persuade'),
        ('persuasive', 'g_persuasive'), ('opinion', 'g_opinion')],
    10: [('compromised', 'g_compromised'), ('affordable', 'g_affordable'),
         ('advert', 'g_advert'), ('conduct', 'g_conduct')],
}
assert sum(len(v) for v in VOCAB.values()) == 58

# Words the quiz never tests, practised here instead.
MATCH = {
    1: [('precaution', 'a step taken in advance to prevent trouble'),
        ('reliable', 'can be trusted to work well'),
        ('primarily', 'mainly'),
        ('trial', 'a test of performance or suitability'),
        ('assumption', 'something believed without proof')],
    2: [('dense', 'closely compacted'),
        ('mouldy', 'affected by mould'),
        ('hazardous', 'dangerous'),
        ('audible', 'able to be heard'),
        ('locate', 'find the exact position of')],
    3: [('monotonous', 'boring and repetitive'),
        ('manageable', 'possible without too much difficulty'),
        ('agitated', 'visibly troubled or nervous'),
        ('startle', 'give a sudden shock'),
        ('exaggerate', 'make something sound bigger than it is')],
}

# (stem, options, correct) — the old page's 28, audited; why = q<n>w
MC = [
    # Section 1: meaning -> word
    ("Which word means “do something, or show qualities, worthy of reward or punishment”?",
     ['deserve', 'persuade', 'reassess', 'conduct'], 0),
    ("Which phrase describes two things “occurring at the same time and having some connection”?",
     ['ad hoc', 'post hoc', 'in parallel', 'current'], 2),
    ("Which phrase means “a plan that can be followed if an original plan is not possible”?",
     ['post hoc review', 'requirement', 'contingency plan', 'assumption'], 2),
    ("Which word means “not planned or meant”?",
     ['unintended', 'ad hoc', 'hazardous', 'actual'], 0),
    ('In poker, which word describes an unconscious action that betrays an attempted deception?',
     ['concern', 'precaution', 'tell', 'threshold'], 2),
    ("Which phrase means “exchange something of value, especially as part of a compromise”?",
     ['trade off', 'take off', 'retrofit', 'remove'], 0),
    ("Which word means “a deficit of something required or expected”?",
     ['threshold', 'requirement', 'shortfall', 'delay'], 2),
    ("Which phrase means “after the event”?",
     ['post hoc', 'ad hoc', 'in parallel', 'primarily'], 0),
    ("Which phrase means “specifically as needed”, with no fixed plan?",
     ['post hoc', 'ad hoc', 'current', 'actual'], 1),
    ("Which word means “existing in fact, as contrasted with what was intended or expected”?",
     ['actual', 'current', 'reliable', 'resilient'], 0),
    ("Which word means “add a component to something that didn’t have it when it was made”?",
     ['remove', 'take off', 'retrofit', 'trade off'], 2),
    ("Which phrase means “fail to appreciate someone or something because of overfamiliarity”?",
     ['take for granted', 'reassess', 'contingency plan', 'assumption'], 0),
    # Section 2: word -> meaning
    ('What does “moisture” mean?',
     ['A solid, almost unyielding surface or structure that resists pressure',
      'Water or liquid present in small quantity, in a solid or on a surface',
      'A substance or treatment that slows or stops the spread of fire',
      'Closely compacted in substance, with very little space inside it'], 1),
    ('What does “firmness” mean?',
     ['The quality of having a solid, almost unyielding surface or structure',
      'The ability to withstand or recover quickly from difficult conditions',
      'The risk or danger something poses to health and safety on a site',
      'How wide something is, measured from one side across to the other'], 0),
    ('What does “resilient” mean?',
     ['Something that can be trusted to work well',
      'Able to withstand or recover quickly from difficult conditions',
      'Able to be organised or completed without too much difficulty',
      'Involving strenuous effort; difficult and tiring'], 1),
    ('What does “threshold” mean?',
     ['A measure taken in advance to prevent something unpleasant',
      'The intensity that must be exceeded for a reaction to occur',
      'A deficit of something required or expected',
      'Something that is necessary'], 1),
    ('What does “homogeneous” mean?',
     ['Of the same kind; alike', 'Closely compacted in substance',
      'Something that can be trusted to work well',
      'Another business offering a similar product'], 0),
    ('What does “exhaustion” mean?',
     ['Feeling or appearing troubled or nervous',
      'A state of extreme physical or mental fatigue',
      'Cause a person to feel sudden shock or alarm',
      'A frightening or unpleasant dream'], 1),
    ('What does “arduous” mean?',
     ['Boring and repetitive, with nothing new from one day to the next',
      'Able to be organised or completed without too much difficulty',
      'Involving or requiring strenuous effort; difficult and tiring',
      'Risky or dangerous, especially to the people who do the work'], 2),
    ('What does “persuasive” mean?',
     ['Good at persuading someone through reasoning or temptation',
      'A view or judgement formed about something, not based on fact',
      'Convince someone to do something they had not planned to do',
      'Consider or assess again, in the light of new information'], 0),
    # Section 3: complete the sentence
    ('Before we finalise the design, we need a ______ in case the new adhesive fails testing.',
     ['contingency plan', 'post hoc review', 'assumption', 'requirement'], 0),
    ('The discolouration was completely ______ — nobody meant the new coating to stain the wall.',
     ['unintended', 'ad hoc', 'hazardous', 'actual'], 0),
    ('Production fell 2,000 units short of demand this quarter, a ______ we will have to explain.',
     ['shortfall', 'threshold', 'tell', 'opinion'], 0),
    ('The membrane needs good ______ so it holds its shape under load.',
     ['firmness', 'moisture', 'width', 'exhaustion'], 0),
    ('This building was put up without a vapour barrier, so we need to ______ one.',
     ['retrofit', 'remove', 'take off', 'trade off'], 0),
    ('Please ______ the old tape before applying the new adhesive.',
     ['remove', 'retrofit', 'take for granted', 'reassess'], 0),
    ('The two teams are working ______, testing the coating and the substrate at the same time.',
     ['in parallel', 'post hoc', 'ad hoc', 'primarily'], 0),
    ("Don’t ______ this partnership — check in with the client regularly.",
     ['take for granted', 'exaggerate the risk of', 'reassess', 'deserve'], 0),
]
assert len(MC) == 28
SECTIONS = [(1, 0, 12), (2, 12, 20), (3, 20, 28)]


def divider(n, pic, pos=None):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=pic, pos=pos)


def intro(n, pic, side, pos):
    return D.panel('e%d' % n, E['e%d' % n], 'p%dt' % n, E['p%dt' % n],
                   [('p%da' % n, E['p%da' % n]), ('p%db' % n, E['p%db' % n], 'dim')],
                   folder=F, pic=pic, side=side, pos=pos)


def quiz_intro(s, pic, side, pos):
    return D.panel('e4', E['e4'], 'qt%d' % s, E['qt%d' % s],
                   [('q%di' % s, E['q%di' % s]), ('qInfo', E['qInfo'], 'dim')],
                   folder=F, pic=pic, side=side, pos=pos)


def cards(eb, n):
    items = VOCAB[n]
    return D.teach(eb, E[eb], 'vt%d' % n, E['vt%d' % n],
                   [(None, w, k, E[k], None, None) for w, k in items],
                   cols='1fr 1fr 1fr')


def match(eb, n):
    return D.match(MATCH[n], eb, E[eb], 'mt', E['mt'], 'matchHint', E['matchHint'],
                   'matchWhy')


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest([dict(options=o, correct=c) for _, o, c in MC])

    quiz = []
    for s, a, b in SECTIONS:
        quiz.append(quiz_intro(s, STRIP,
                               ['left', 'right', 'left'][s - 1],
                               ['8% 50%', '55% 50%', '97% 50%'][s - 1]))
        for i in range(a, b):
            stem, opts, c = MC[i]
            quiz.append(D.mc(i + 1, len(MC),
                             dict(stem=stem, options=opts, correct=c, why='q%dw' % (i + 1)),
                             'e4', E['e4'], 'qt%d' % s, E['qt%d' % s]))

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        divider(1, SUN),
        intro(1, SUN, 'left', '35% 50%'),
        cards('e1', 1), cards('e1', 2), cards('e1', 3),
        match('e1', 1),

        divider(2, SITE),
        intro(2, SITE, 'right', '14% 50%'),
        cards('e2', 4), cards('e2', 5), cards('e2', 6),
        match('e2', 2),

        divider(3, CLOUD),
        intro(3, CLOUD, 'left', '72% 50%'),
        cards('e3', 7), cards('e3', 8), cards('e3', 9), cards('e3', 10),
        match('e3', 3),

        divider(4, STRIP),
    ] + quiz + [
        D.results(),
        D.activate(E['actTitle'], E['actUse'],
                   ['contingency plan', 'trade-off', 'shortfall', 'ad hoc',
                    'precaution', 'reassess', 'take for granted'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=ACT),
    ])

    n = slides.count('<section class="slide')
    assert ('%d slides' % n) == E['chipCount'], (n, E['chipCount'])
    langs = tuple(c for c in I.LANGS if c in I.T)
    D.assemble(TPL, OUT, slides, PALETTE, 'Contingency Plans &amp; Trade-offs (C1) | Forbes English',
               I, langs=langs)
    print('wrote %s — %d slides, %s%s' % (OUT, n, ','.join(langs),
          '' if READY else ' (PREVIEW: plates missing, see docs/ARTWORK-contingency-trade-offs.md)'))


if __name__ == '__main__':
    build()
