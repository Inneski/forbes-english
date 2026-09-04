# -*- coding: utf-8 -*-
"""Lego Car Building &mdash; Part 2 (B2) &mdash; the fifteen scored items.

Lifted from the scrolling `forbes-lego-b2-part2.html`, the second half of the
Lego-Technic lesson in brick red and blueprint blue, where the vocabulary of
part one is put under pressure. Three activities, five items each: five error
corrections on preposition collocation and word form, five sentence
transformations driven by a supplied phrase, and five technical terms matched to
their definitions. All fifteen survive and the page's own explanation for every
one of them is reproduced at the foot of this file.

The error corrections change shape rather than substance. The page asked for two
typed words per item, the wrong one and its replacement, and awarded the point
only when both were right. A deck gap row does the same work more honestly: each
sentence below carries two `______` markers and two answers, both of which must
land, so the item still costs two correct pieces of knowledge. The blanks fall
where the page underlined, so the learner supplies the collocation instead of
diagnosing it, and each sentence reads naturally with both blanks filled.

One error-correction item is thrown out. **Item two was mis-keyed.** Its sentence
had a builder substitute the original wheels *with* a smaller alternative and its
key rewrote *with* to *for* &mdash; but *substitute X for Y* means use X in place
of Y, so the corrected sentence says the smaller alternative was swapped out in
favour of the wheels it was meant to replace, the exact reverse of the story the
sentence tells. *Substitute with* is widely accepted in any case, which leaves an
item whose supposed error is defensible and whose key is wrong. It is replaced by
a genuinely broken preposition in the same register and the same workshop: the
steering assembly *depends on* a precise fit, where the error a B2 learner
actually produces is *depends from*, a straight carry-over from Romance. That key
admits only *on* or *upon*, so there is nothing left to argue about. The
incompatible-axle framing is kept, because it was the good half of the item.

Two transformation keys are lengthened by proxy. **Questions three and five had
keys markedly shorter than their longest distractor** &mdash; fifty-five
characters against ninety-five, and sixty-seven against a hundred and four. A key
that is conspicuously the shortest option gives the item away exactly as a key
that is conspicuously the longest one does, and both keys are the tight,
idiomatic transformation the exercise is teaching, so shortening them further is
impossible and lengthening them would spoil them. The distractors are tightened
instead. Question three's padded clauses (&ldquo;so turning it smoothly was
something impossible to do&rdquo;, &ldquo;but it was still possible to turn it
with enough effort&rdquo;) contract to the same three errors stated plainly, and
question five's loses its trailing justifications. Every distractor stays
grammatical and stays the mistake it was: wrong adjective, reversed meaning,
swapped adjectives on three; perfect modal, continuous modal, contradicted
instruction on five. All four options now sit within a handful of characters.

The keys are also respread. In DOM order they sat at positions two, two, four,
one and three, which is not a pattern a learner can exploit but is not a spread
either, and MC_POS puts them over all four indices below. The assertion under
`_place` proves nothing was lost in the move.

One defect is recorded and left alone, because the deck format makes it moot. The
five matching dropdowns each carried the same five definitions and never removed
one that had been used, so a learner who answered the first four correctly had no
decision left to make on the fifth: load capacity was free by elimination, and
the activity was really worth four points, not five. The deck's `match()` builds
its grid from the pairs and consumes each definition as it is placed, so the
final term is a real question there and nothing needs changing in the data.
"""

# ── Activity 1: error correction, as two-blank gap rows ────────────────
# Each row: the page's sentence with the underlined words blanked, both
# answers required. Item 2 is the replacement described above.
ERR = [
    ("The instructions advised builders to start ______ the chassis and work "
     "their way upwards, attaching each component ______ sequence.",
     ["from|with", "in"], "e1why"),

    ("He was frustrated to discover that the rear axle was ______ with the new "
     "wheel design, since the whole steering assembly depends ______ a precise "
     "fit between the hub and the pin.",
     ["incompatible", "on|upon"], "e2why"),

    ("The gear mechanism consists ______ three interlocking cogs, each ______ "
     "rotational force to the drive shaft at a controlled ratio.",
     ["of", "transmitting"], "e3why"),

    ("Despite following the instructions ______, she found that the steering "
     "column was slightly off-centre, which caused the vehicle to turn ______ "
     "on tight bends.",
     ["precisely|exactly", "inefficiently"], "e4why"),

    ("The designer had to reconsider the suspension layout after ______ that "
     "the current setup was ______ rigid to absorb the impact of uneven "
     "terrain effectively.",
     ["realising|realizing", "too"], "e5why"),
]


# ── Activity 2: sentence transformation ────────────────────────────────
# original key positions in DOM order: [2, 2, 4, 1, 3] (1-based)
MC_POS = [2, 3, 0, 3, 1]

# (stem, [options with the key FIRST], why-key)
_MC_RAW = [
    ("<strong>Original:</strong> &ldquo;It was impossible to complete the build "
     "without a pair of tweezers for the smallest parts.&rdquo;<br><br>Using: "
     "<em>&hellip;could not be completed&hellip;</em>",
     ["The build could not be completed without a pair of tweezers for the "
      "smallest parts.",
      "The build could not be completed because it was impossible to find a "
      "pair of tweezers.",
      "The build could not be completed, even though tweezers were available "
      "for the small parts.",
      "The build could not be completed if the tweezers were used on the "
      "smallest parts only."],
     "q1why"),

    ("<strong>Original:</strong> &ldquo;He spent three hours assembling the "
     "engine block before he noticed a mistake.&rdquo;<br><br>Using: "
     "<em>&hellip;only to discover&hellip;</em>",
     ["He spent three hours assembling the engine block, only to discover that "
      "he had made a mistake.",
      "He spent three hours on the engine block, and eventually he was able to "
      "discover his mistake.",
      "He only discovered the engine block mistake after spending more than "
      "three hours on it later.",
      "He had only been working for three hours when he discovered the engine "
      "had been assembled wrongly."],
     "q2why"),

    ("<strong>Original:</strong> &ldquo;The steering mechanism was so stiff "
     "that it was impossible to turn smoothly.&rdquo;<br><br>Using: "
     "<em>&hellip;too&hellip; to&hellip;</em>",
     ["The steering mechanism was too stiff to turn smoothly.",
      "The steering mechanism was too difficult to turn smoothly.",
      "The steering mechanism was too stiff, yet it turned smoothly.",
      "The steering mechanism was too smooth to be turned stiffly."],
     "q3why"),

    ("<strong>Original:</strong> &ldquo;Although the model looked fragile, it "
     "proved to be extremely durable.&rdquo;<br><br>Using: "
     "<em>&hellip;despite&hellip;</em>",
     ["Despite its fragile appearance, the model proved to be extremely "
      "durable.",
      "Despite looking fragile, the model did not manage to prove that it was "
      "especially durable.",
      "Despite the model being durable, it also had a very fragile exterior "
      "that was extremely delicate.",
      "Despite the fact it was fragile, the model did not prove to be "
      "particularly durable in testing."],
     "q4why"),

    ("<strong>Original:</strong> &ldquo;It is essential that all builders read "
     "the instructions carefully before starting.&rdquo;<br><br>Using: "
     "<em>&hellip;must&hellip;</em>",
     ["All builders must read the instructions carefully before starting.",
      "All builders must have read the instructions before they started.",
      "All builders must be reading the instructions once they have started.",
      "All builders must read the instructions, though starting first is fine."],
     "q5why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 3: terms and definitions ──────────────────────────────────
MATCH = [
    ("torque",
     "The rotational force that causes an object to turn around an axis"),
    ("camber",
     "The angle at which a wheel is tilted relative to the vertical plane"),
    ("gear ratio",
     "The comparison of speeds between two meshing gears"),
    ("suspension",
     "A system that absorbs shock and maintains contact with the ground"),
    ("load capacity",
     "The maximum weight a structural element can safely support"),
]


# ORIGINAL EXPLANATIONS —
# q1: Option B preserves the exact meaning of the original using the passive form "could not be completed" — the condition (needing tweezers) remains unchanged.
# q2: "Only to discover" expresses a disappointing or surprising outcome after effort — perfectly capturing the frustration of finding a mistake after three hours of work.
# q3: "Too + adjective + to + infinitive" is a concise structure meaning "so [adjective] that it was impossible to [verb]." Option C captures this perfectly.
# q4: "Despite + noun phrase" replaces "Although + clause." Option D correctly converts "its fragile appearance" into the noun phrase following "despite," keeping the meaning intact.
# q5: "It is essential that + subject + base verb" transforms directly into "subject + must + base verb" — both express strong obligation. Option B is accurate and unmodified.
# e1: The error was "on". The correct preposition is in: "in sequence." The phrase in sequence is a fixed collocation meaning in the correct order.
# e2: The error was "with". The verb substitute collocates with for, not with: "substitute the original wheels for a smaller alternative." Note: replace takes with — a common confusion.
# e3: The error was "from". The verb consist always takes the preposition of: "consists of three interlocking cogs." This is a fixed collocation with no exceptions.
# e4: The error was "inefficient" (adjective). It modifies the verb turn, so an adverb is needed: inefficiently. Adverbs modify verbs; adjectives modify nouns.
# e5: The error was "to" (preposition/infinitive marker). The correct word is too (adverb of degree): "too rigid to absorb…" — meaning excessively rigid. This is a very common spelling confusion.
# m1: torque → The rotational force that causes an object to turn around an axis. In Lego Technic, torque is what makes the wheels spin — generated by the motor or manually turning a gear.
# m2: camber → The angle at which a wheel is tilted relative to the vertical plane. Negative camber (top of wheel tilting inward) improves cornering grip on racing cars.
# m3: gear ratio → The comparison of speeds between two meshing gears. A 3:1 ratio means the output gear turns once for every three turns of the input gear — trading speed for torque.
# m4: suspension → A system that absorbs shock and maintains tyre contact with the ground. In Lego Technic cars, suspension is built using spring elements and pivot joints.
# m5: load capacity → The maximum weight a structural element can safely support. Engineers calculate load capacity for chassis and axle beams to ensure the model doesn't buckle.
