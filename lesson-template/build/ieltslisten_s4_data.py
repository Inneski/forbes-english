# -*- coding: utf-8 -*-
"""IELTS Listening Section 4 — the lecture.

The hardest section, and the one that is hardest for a reason candidates
usually misdiagnose. It is not the vocabulary and it is not the speed.

**There is no break.** Sections 1 to 3 pause halfway so you can read the next
set of questions. Section 4 runs straight through — one speaker, four or five
minutes, no pause, no second voice to interrupt and repeat. Lose your place
and there is nothing to grab hold of.

**And the answers are almost always note completion**, which means the words
come straight from the recording and the word limit is unforgiving: a right
answer written as three words where two were allowed scores nothing.

The script is an academic lecture on urban trees, and it is built around the
four things that actually lose marks at this end of the paper:

  1. **Signposting that tells you where you are.** *First* … *the second
     factor* … *finally*. These are the handholds, and a candidate who is not
     using them has nothing when they drift.
  2. **The aside.** A digression that lasts twenty seconds and contains no
     answers, placed exactly where a tiring candidate starts writing anything
     they hear.
  3. **A definition given in passing** — the term stated, then explained, with
     the explanation being the answer rather than the term.
  4. **A number revised upward** inside the same sentence, which is the
     Section 1 correction trap arriving at Section 4 speed.

The lecturer is British male — the fourth distinct voice across the four
sections, so a learner working through the route in order has met a spread
rather than the same speaker four times.
"""

# ── the recording ──────────────────────────────────────────────────────
TURNS = [
    ('narrator',
     'Section four. You will hear part of a lecture about the role of trees in '
     'cities. First, you have some time to look at questions one to ten.'),
    ('narrator', 'Now listen carefully and answer questions one to ten.'),

    ('gb_m2',
     'Good afternoon. Today I want to look at urban trees — not as decoration, '
     'which is how they were treated for most of the last century, but as '
     'infrastructure. And I want to give you three functions, in order of how '
     'well we can measure them.'),

    ('gb_m2',
     'First, and this is the one everybody knows, temperature. A mature street '
     'tree cools the air around it in two separate ways: by shading the '
     'surface underneath, and by transpiration — that is, releasing water '
     'vapour through the leaves, which takes heat out of the air as it '
     'evaporates. Transpiration is the one people forget, and in a dry city it '
     'does roughly half the work.'),

    ('gb_m2',
     'The figures here are good. A well-planted street in a European city runs '
     'about two degrees cooler than an unplanted one nearby. In some of the '
     'Australian measurements it is more — I have seen four quoted, though I '
     'would treat that as an upper bound rather than a typical figure.'),

    ('gb_m2',
     'The second factor is water. Trees intercept rainfall before it reaches '
     'the ground, and that matters enormously for drainage. The technical term '
     'is interception loss — the proportion of rain that never reaches the '
     'drain at all because it sits on the leaves and evaporates. For a mature '
     'canopy in a temperate climate that is somewhere between twenty and '
     'thirty per cent of a rainfall event.'),

    ('gb_m2',
     'Now, an aside, because somebody always asks. Yes, the roots do damage '
     'pavements, and yes, the repair bill is real. I have stood in council '
     'meetings where that single line ended the discussion. The honest answer '
     'is that the damage is species-specific and largely avoidable with the '
     'right planting pit, but that is a different lecture and I will not do it '
     'justice today.'),

    ('gb_m2',
     'Right. The third function, and the weakest evidence of the three, is air '
     'quality. Trees do trap particulates on their leaves. But the effect is '
     'small compared to the temperature effect, and there is a complication: '
     'a dense avenue of trees over a narrow street can trap polluted air at '
     'street level rather than letting it disperse. So the planting has to be '
     'designed, not simply maximised.'),

    ('gb_m2',
     'Finally, a word on cost, because this is where the argument is usually '
     'won or lost. Planting a single street tree in a British city costs '
     'around eight hundred pounds — no, I should be accurate, the last figure '
     'I saw was closer to twelve hundred once you include the first three '
     'years of watering. And it is the watering, not the planting, that most '
     'schemes fail to budget for.'),

    ('narrator',
     'That is the end of section four. You now have half a minute to check '
     'your answers.'),
]

AUDIO = 'section4.mp3'

# ── Questions 1-6 · note completion ────────────────────────────────────
# Straight from the recording, and the word limit is the point: every answer
# here is one or two words, which is what a real Section 4 note task allows.
NOTES_A = [
    ('Trees cool the air by shading and by ______',
     ['transpiration'],
     'Transpiration &mdash; and the lecturer defines it in the same breath, '
     '"releasing water vapour through the leaves". The definition is there to '
     'help; the answer is still the term.'),
    ('A planted street runs about ______ degrees cooler',
     ['2|two'],
     'Two in Europe. Four is quoted for Australia and immediately labelled an '
     '"upper bound rather than a typical figure" &mdash; a number said and '
     'then qualified is almost never the answer.'),
    ('Rain that never reaches the drain: ______ loss',
     ['interception'],
     '"The technical term is interception loss." He says <em>the technical '
     'term is</em>, which is the clearest possible flag that a word is about '
     'to be worth a mark.'),
]

NOTES_B = [
    ('Interception is ______ to thirty per cent of a rainfall event',
     ['20|twenty'],
     'Twenty to thirty. Both halves of a range get said; the gap tells you '
     'which one it wants by what is already printed beside it.'),
    ('Weakest evidence of the three: ______ quality',
     ['air'],
     'Air quality, and he grades it himself &mdash; "the weakest evidence of '
     'the three". A lecturer ranking his own points is handing you the '
     'structure.'),
    ('Cost per tree, including watering: £______',
     ['1200|1,200|twelve hundred'],
     'Twelve hundred. Eight hundred is said first and corrected inside the '
     'same sentence &mdash; "no, I should be accurate" &mdash; which is the '
     'Section 1 correction trap at Section 4 speed.'),
]

NOTES_BANK = []

# ── Questions 7-10 · multiple choice ───────────────────────────────────
MC = [
    dict(stem='How does the lecturer want trees to be thought of?',
         options=['As infrastructure rather than as decoration.',
                  'As decoration rather than as infrastructure.',
                  'As a cost that cities should try to reduce.',
                  'As a replacement for drainage in a city.'],
         correct=0, why='p1why'),

    dict(stem='What complication does he raise about air quality?',
         options=['Particulates are washed off the leaves by rain.',
                  'Dense trees can trap polluted air in a street.',
                  'The leaves absorb less pollution than expected.',
                  'Measuring the effect needs specialist equipment.'],
         correct=1, why='p2why'),

    dict(stem='What does he say about roots damaging pavements?',
         options=['It is a myth that councils repeat to save money.',
                  'It is the strongest argument against street trees.',
                  'It is real, but avoidable with the right planting.',
                  'It is a problem only in older European cities.'],
         correct=2, why='p3why'),

    dict(stem='Which cost do schemes most often fail to budget for?',
         options=['The price of buying the young tree originally.',
                  'The repair of pavements damaged by the roots.',
                  'The cost of designing where the trees will go.',
                  'The watering of the tree in its first few years.'],
         correct=3, why='p4why'),
]
