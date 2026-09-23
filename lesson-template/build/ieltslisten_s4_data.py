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

REVISED 2026-09-23 (IELTS audit): ten note gaps in the order they are heard,
as a real Section 4 is (the four multiple-choice items were answered from the
first sentence, the middle and the end, which cannot work once the recording
plays while the learner answers). The aside is no longer described as "no
answers at all": it holds one (Question 6), and "believe him and rest" was
advice to stop listening. "On a hot day" replaces "in a dry city", where
trees transpire least. The lecturer contracts; the narrator does not.
"""

# ── the recording ──────────────────────────────────────────────────────
TURNS = [
    ('narrator',
     'Section four. You will hear part of a lecture about the role of trees in '
     'cities. First, you have some time to look at questions one to ten.'),
    ('pause', 15),
    ('narrator', 'Now listen carefully and answer questions one to ten.'),

    ('gb_m2',
     "Good afternoon. Today I want to look at urban trees — not as decoration, "
     "which is how they were treated for most of the last century, but as "
     "infrastructure. And I want to give you three functions, in order of how "
     "well we can measure them."),

    ('gb_m2',
     "First, and this is the one everybody knows, temperature. A mature street "
     "tree cools the air around it in two separate ways: by shading the "
     "surface underneath, and by transpiration — that is, releasing water "
     "vapour through the leaves, which takes heat out of the air as it "
     "evaporates. Transpiration is the one people forget, and on a hot day "
     "it does roughly half the work."),

    ('gb_m2',
     "The figures here are good. A well-planted street in a European city runs "
     "about two degrees cooler than an unplanted one nearby. In some of the "
     "Australian measurements it's more — I've seen four quoted, though I'd "
     "treat that as an upper bound rather than a typical figure."),

    ('gb_m2',
     "The second factor is water. Trees intercept rainfall before it reaches "
     "the ground, and that matters enormously for drainage. The technical term "
     "is interception loss — the proportion of rain that never reaches the "
     "drain at all because it sits on the leaves and evaporates. For a mature "
     "canopy in a temperate climate that's somewhere between twenty and "
     "thirty per cent of a rainfall event."),

    ('gb_m2',
     "Now, an aside, because somebody always asks. Yes, the roots do damage "
     "pavements, and yes, the repair bill is real. I've stood in council "
     "meetings where that single line ended the discussion. The honest answer "
     "is that the damage is species-specific and largely avoidable with the "
     "right planting pit, but that's a different lecture and I won't do it "
     "justice today."),

    ('gb_m2',
     "Right. The third function, and the weakest evidence of the three, is air "
     "quality. Trees do trap particulates on their leaves. But the effect is "
     "small compared to the temperature effect, and there's a complication: a "
     "dense avenue of trees over a narrow street can trap polluted air at "
     "street level rather than letting it disperse. So the planting has to be "
     "designed, not simply maximised."),

    ('gb_m2',
     "Finally, a word on cost, because this is where the argument is usually "
     "won or lost. Planting a single street tree in a British city costs "
     "around eight hundred pounds — no, I should be accurate, the last figure "
     "I saw was closer to twelve hundred once you include the first three "
     "years of watering. And it's the watering, not the planting, that most "
     "schemes fail to budget for."),

    ('narrator',
     'That is the end of section four. You now have half a minute to check '
     'your answers.'),
]

AUDIO = 'section4.mp3'

# ── Questions 1-10 · note completion, in the order they are heard ──────
# A real Section 4 is ten note gaps that follow the lecture. This deck had six
# gaps and then four multiple-choice items whose answers came from the first
# sentence, the middle and the end, so once the recording played while the
# learner answered (2026-09-23) nobody could follow the order. The four points
# those items tested are note lines now, in sequence; the word limit is still
# the point, and every answer is one word or a number.
NOTES = [
    ('Urban trees should be treated as ______, not decoration',
     ['infrastructure'],
     'Infrastructure, in the first sentence: the thesis the whole lecture is '
     'built to support.'),
    ('Trees cool the air by shading and by ______',
     ['transpiration'],
     'Transpiration, defined in the same breath as "releasing water vapour '
     'through the leaves". The answer is the term, not the definition.'),
    ('A planted street runs about ______ degrees cooler',
     ['2|two'],
     'Two, for Europe. Four is quoted for Australia and called an "upper '
     'bound" at once &mdash; a figure that gets qualified is not the answer.'),
    ('Rain that never reaches the drain: ______ loss',
     ['interception'],
     '"The technical term is interception loss" &mdash; the clearest flag '
     'there is that a word is worth a mark.'),
    ('Interception is ______ to thirty per cent of a rainfall event',
     ['20|twenty'],
     'Twenty to thirty. What is printed beside the gap shows which half of '
     'the range it wants.'),
    ('Root damage is largely avoidable with the right planting ______',
     ['pit'],
     'Pit, inside the aside the lecturer flags as a digression. An aside is '
     'off the main argument, not empty.'),
    ('Weakest evidence of the three: ______ quality',
     ['air'],
     'Air quality, and the lecturer grades it himself &mdash; "the weakest '
     'evidence of the three". A lecturer ranking his own points is handing you '
     'the structure.'),
    ('A dense avenue over a narrow street can ______ polluted air',
     ['trap'],
     'Trap. The complication comes straight after the claim it limits '
     '&mdash; trees trap particulates, and they can trap the polluted air '
     'too. Same verb, opposite effect.'),
    ('Cost per tree, including watering: £______',
     ['1200|1,200'],
     'Twelve hundred. Eight hundred is said first and corrected inside the '
     'same sentence &mdash; "no, I should be accurate" &mdash; which is the '
     'Section 1 correction trap at Section 4 speed.'),
    ('Most schemes fail to budget for the ______',
     ['watering'],
     'Watering &mdash; "the watering, not the planting". The last line of a '
     'lecture is where it lands its point, and the contrast is said in the '
     'same breath.'),
]

NOTES_BANK = []

# Two a slide. Four rows run past the canvas once the explanations show, and
# three ran 12px past in Spanish once the explanations translated (measured
# 2026-09-23). HOUSE-STYLE §6: more slides, not smaller type.
NOTES_SLIDES = [NOTES[i:i + 2] for i in range(0, len(NOTES), 2)]
