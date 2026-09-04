# -*- coding: utf-8 -*-
"""Lego Car Building (B2) — the fifteen scored items.

Lifted from the scrolling `forbes-lego-b2.html`, a Lego-Technic-themed
vocabulary lesson in brick red and blueprint blue that teaches the language of
design, engineering and the build process. Three activities, five items each:
five multiple choice on single words in context (align, differential gear,
orientation, structural integrity, retrofit), five typed gap-fills on technical
nouns and adjectives drawn from an eight-word bank, and five drag-and-drop gaps
on the phrasal verbs and hyphenated verbs a builder actually uses. All fifteen
survive, sentence for sentence, and the page's own explanation for every one of
them is reproduced at the foot of this file.

One item is repaired. **Multiple choice question 1's key was conspicuously the
longest option.** "To position something so it lines up correctly" ran forty-six
characters against a longest distractor of thirty-eight, an eight-character lead
that a learner can see without reading a word of it — the tell the ANSWERS gate
fails on, and it is worth more here than anywhere else because the item is the
first one in the lesson. The key is untouched, because shortening a key only
moves the tell onto whichever option is longest next. The three distractors are
lengthened into fuller versions of the same three errors: taking a component
apart is now taking it apart "again and rebuild it", the adhesive distractor
becomes joining "two separate parts together", and reinforcing a joint becomes
reinforcing "a weak joint by adding extra bricks". All three are still what a
B2 learner reaches for when they guess at *align* from the build context, and
the four options now sit within four characters of one another.

The keys were also respread. In DOM order they sat at index 2, 1, 2, 1, 3 —
never at index 0 across five questions, and alternating third-second-third-
second for the first four, so a learner who noticed could delete a quarter of
every item unread. MC_POS puts them over all four positions below, and the
assertion under `_place` proves nothing was lost in the move.

The gap answers are widened. The page lowercased the typed string and compared
it with `===` against one accepted form, so a learner who wrote "load bearing"
with the vocabulary exactly right was marked wrong; the hyphenated answers now
carry their spaced and run-together spellings pipe-separated inside one string,
here and in the drag-and-drop, which the deck accepts as typed input.

Both banks are kept and both are sorted case-insensitively. The page printed
the eight FITB words as coloured chips inside an SVG and the seven drag chips in
a bank row, and in neither case was the order the gap order to begin with, so
sorting costs nothing and guarantees it. Neither bank runs in gap order after
sorting — FIB answers land at bank positions 6, 5, 1, 4, 3 and DND answers at
3, 6, 4, 0, 1 — so both survive as real banks rather than dropping to None.

One defect is recorded and left alone, because the deck format makes it moot.
The printed A/B/C/D letters are out of sequence on questions 3, 4 and 5: the
letters were hand-shuffled to disguise the key position but the DOM order was
not, so question 3 reads A, C, B, D down the page, question 4 reads D, A, C, B
and question 5 reads B, D, A, C. On the page this is merely odd; in a deck the
letters are generated from the option index, so the mismatch cannot survive the
rebuild and there is nothing to carry across.
"""

# ── Activity 1: multiple choice ────────────────────────────────────────
# original key positions in DOM order: [2, 1, 2, 1, 3] — never index 0
MC_POS = [0, 2, 1, 3, 1]

# (stem, [options with the key FIRST], why-key)
_MC_RAW = [
    ("The instruction manual told builders to <strong>align</strong> the axle "
     "with the chassis before attaching the wheels. What does <em>align</em> "
     "mean here?",
     ["To position something so it lines up correctly",
      "To take a component apart again and rebuild it",
      "To join two separate parts together using adhesive",
      "To reinforce a weak joint by adding extra bricks"],
     "q1why"),

    ("The Lego Technic set features a <strong>differential gear</strong>, which "
     "allows the outer wheels to rotate faster when cornering. What is the "
     "primary function of this mechanism?",
     ["It compensates for the difference in wheel speed during turns",
      "It increases the engine&rsquo;s overall horsepower output",
      "It locks both rear wheels to prevent them from spinning",
      "It converts rotational force into linear movement efficiently"],
     "q2why"),

    ("After spending six hours on the build, she realised she had placed a beam "
     "in the wrong <strong>orientation</strong>. What does this tell us?",
     ["She had placed the piece facing the wrong direction or angle",
      "She had selected the incorrect colour of brick for that section",
      "She had forgotten to attach the piece to the main chassis frame",
      "She had used a beam that was too long for that specific position"],
     "q3why"),

    ("The finished model had excellent <strong>structural integrity</strong>, "
     "meaning it could withstand rough handling without falling apart. Which "
     "sentence best paraphrases this?",
     ["The model was robust and held together even under physical stress",
      "The model looked very realistic because of its detailed colouring",
      "The model was easy to disassemble and rebuild from scratch quickly",
      "The model was very lightweight due to the minimal number of pieces"],
     "q4why"),

    ("He decided to <strong>retrofit</strong> the model by adding working LED "
     "headlights after he had already completed the build. What does "
     "<em>retrofit</em> imply?",
     ["To add a new feature to something that was already completed",
      "To build an entirely new version of the same model from scratch",
      "To follow the original instructions without making any changes",
      "To remove a feature that was included in the original design"],
     "q5why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: the gaps ───────────────────────────────────────────────
FIB = [
    ("Before producing the final set, the engineers built a ______ to test "
     "whether all the pieces worked together as intended.",
     ["prototype"], "g1why"),

    ("The chassis used a ______ design, meaning each section could be built and "
     "replaced independently without affecting the rest of the model.",
     ["modular"], "g2why"),

    ("She checked the ______ carefully before starting the build, noting every "
     "step, measurement, and part number in the diagram.",
     ["blueprint|blue print"], "g3why"),

    ("The central beam was a ______ element &mdash; without it, the entire "
     "frame would collapse under the weight of the other components.",
     ["load-bearing|load bearing|loadbearing"], "g4why"),

    ("Designers use an ______ process, refining the model through repeated "
     "testing and adjustment cycles before approving the final version.",
     ["iterative"], "g5why"),
]

# The page's eight-word chip bank, alphabetised. Its printed order was
# prototype, assemble, load-bearing, tolerance, blueprint, compatibility,
# iterative, modular — not gap order, and not sorted either.
FIB_BANK = sorted(['prototype', 'assemble', 'load-bearing', 'tolerance',
                   'blueprint', 'compatibility', 'iterative', 'modular'],
                  key=str.lower)


# ── Activity 3: the phrasal-verb gaps ──────────────────────────────────
DND = [
    ("Always ______ all the pieces before you start building so that you can "
     "spot missing parts immediately.",
     ["lay out|layout"], "d1why"),

    ("When a wheel doesn&rsquo;t fit properly, you should ______ the problem by "
     "checking the axle alignment first.",
     ["troubleshoot|trouble-shoot|trouble shoot"], "d2why"),

    ("The bricks are designed to ______ place with a satisfying click, "
     "confirming a secure connection.",
     ["snap into"], "d3why"),

    ("Experienced builders always ______ the diagram with the parts list to "
     "avoid assembly errors.",
     ["cross-reference|cross reference|crossreference"], "d4why"),

    ("Once the basic structure was complete, she began to ______ the steering "
     "mechanism for smoother movement.",
     ["fine-tune|fine tune|finetune"], "d5why"),
]

# The page's seven drag chips, alphabetised. Their printed order was follow,
# fine-tune, snap into, lay out, cross-reference, troubleshoot, step-by-step.
DND_BANK = sorted(['follow', 'fine-tune', 'snap into', 'lay out',
                   'cross-reference', 'troubleshoot', 'step-by-step'],
                  key=str.lower)


# ORIGINAL EXPLANATIONS —
# q1: Align means to position or arrange things so they are in the correct relative position — here, lining up the axle with the chassis.
# q2: A differential gear allows each wheel to rotate at a different speed, which is essential when a vehicle turns, as the outer wheels travel a longer distance.
# q3: Orientation refers to the direction or angle in which something is positioned — placing a beam the wrong way round is an orientation error.
# q4: Structural integrity refers to a structure's ability to remain intact under stress or load — so a model with good structural integrity is strong and durable.
# q5: To retrofit means to add a new feature or component to an existing finished product. Here, the LEDs were added after the original build was complete.
# g1: Answer: prototype — A prototype is a first working model built to test and evaluate a concept before final production begins.
# g2: Answer: modular — A modular design is one where individual sections are self-contained and interchangeable, making maintenance and modification easier.
# g3: Answer: blueprint — A blueprint is a detailed technical plan or diagram used as a guide during construction or manufacturing.
# g4: Answer: load-bearing — A load-bearing element is a structural component that supports the weight of other parts of a construction.
# g5: Answer: iterative — An iterative process involves repeated cycles of testing and refinement, each cycle improving on the last.
# d1: To lay out means to spread everything out in an organised manner before starting a task — a key preparation step.
# d2: To troubleshoot means to identify and solve problems systematically — essential when something doesn't work as expected.
# d3: Snap into place describes the action of a piece clicking firmly and securely into its correct position.
# d4: To cross-reference means to check one source of information against another to confirm accuracy.
# d5: To fine-tune means to make small, precise adjustments to improve performance — here, refining the steering mechanism.
