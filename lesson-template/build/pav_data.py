# -*- coding: utf-8 -*-
"""Active & Passive Voice, LEGO edition (B1) — the twenty scored items.

Lifted from the scrolling `forbes-english-lego-passive-active.html`, a Lego-themed
drill on the passive: seven multiple choice, six gap-fills, five active sentences to
pair with their passive equivalents and two jumbled passive sentences to rebuild.
The grammar is sound and the sentences are kept as the page wrote them.

The two rebuild items were the page's drag-and-drop activity, and they are ORDER
here rather than being folded into anything else. They are word-order tasks with no
gap and no pair, so neither FIB nor MATCH could hold them; they were already a
separate card ("Word Order 1 of 2") sitting under the matching grid, and they stay
one. The pairing activity is a real MATCH and not a SORT: its five right-hand cells
are five distinct passive sentences, one per left-hand active sentence, so match()
can pair them one to one.

BANK is None. The page offered no word bank for the gaps and needs none, because the
verb sits in brackets after each gap; a bank of the six answers would be the key laid
out flat. The chunk pools for the two rebuild items live inside ORDER itself.

Two things are fixed. **Every key sat at C, C, B, B, B, D, C** — never at A, and
never in the first position across seven questions, so a learner who noticed could
delete a quarter of every item unread. MC_POS respreads them over all four positions.
**Multiple choice question 5's key was the only long option**, seventy-six characters
against a sixty-four-character longest distractor, which is the tell the ANSWERS gate
fails on. The three distractors are lengthened and the key is untouched, since a
shortened key only moves the tell: hiding the founder's name is now stated as
deliberate concealment, the unknown-doer distractor becomes a claim that nobody has
ever discovered who founded the company, and the formality distractor is pushed to
"in every context". All three remain errors a B1 learner really makes.

The gap answers are widened. The page lowercased the typed string and compared it
with `===` against one accepted form, so a learner who wrote "'s been assembled" with
the grammar exactly right was marked wrong. Gap one now carries its contraction and
its apostrophe-less spelling pipe-separated inside one string; the other five have no
contracted form a learner would type.

Two fields of the original have no home in these shapes and are folded or dropped.
Each gap carried a tense hint in a yellow chip ("Present perfect passive"), and
without it the gaps are genuinely ambiguous — "the set ______ (assemble) by fans"
admits three tenses — so the hint moves inside the bracket cue after a ·.
The multiple choice context lines ("Think about whether the subject performs or
receives the action") are dropped: they steer rather than disambiguate, and every
stem stands without them.

Everything else found wrong is recorded below and left alone. The page scores
twenty-two, not twenty: seven plus six plus five is eighteen, and the two rebuilds
pay two points each. The header, the ring and the final card all say twenty, and
`pct=score/20` drives a stroke-dashoffset that goes negative above twenty, so a
strong learner overfills the ring and reads "22 out of 20". Restarting is worse:
`mnx.onclick` hides `#match-box` with `box.style.display='none'` and `restart()`
never restores it, so on a second run the matching grid is invisible and its five
points are unreachable. Multiple choice question 6 has two defensible keys: it asks
for the present perfect passive and the intended key is "New Lego themes have been
introduced", but "Lego's headquarters have been located in Billund" is that form too,
and the explanation dismisses it on meaning ("a stative verb") rather than on form.
Question 3's fourth option, the verb phrase "was designed", is not a candidate agent
at all and reads as filler, while its third option, "Denmark", is a fragment of the
key. The matching grid costs nothing for a wrong guess and the last pair is scored
automatically once four are placed, so five points can be brute-forced. The stored
explanations name option letters ("Option C uses 'was released'"), which no longer
line up once MC_POS moves the keys; they are reproduced verbatim at the foot of this
file for reference and the i18n copy should drop the letters.
"""

# ── Activity 1: multiple choice ────────────────────────────────────────
# original key positions: C, C, B, B, B, D, C  (2, 2, 1, 1, 1, 3, 2) — never A
MC_POS = [2, 0, 3, 1, 0, 2, 3]

_MC_RAW = [
    ("Which sentence is in the <strong>passive voice</strong>?",
     ["The new Lego model was released last Tuesday.",
      "The designer sketched a new Lego set overnight.",
      "Children built a huge Lego castle in the park.",
      "Lego engineers tested the bricks for flexibility."],
     "q1why"),

    ("Choose the correct <strong>passive</strong> transformation of: "
     "<em>&ldquo;Millions of children buy Lego sets every year.&rdquo;</em>",
     ["Lego sets are bought by millions of children every year.",
      "Lego sets were bought by millions of children every year.",
      "Millions of children are buying Lego sets every year.",
      "Every year, children will buy millions of Lego sets."],
     "q2why"),

    ("What is the <strong>agent</strong> in: <em>&ldquo;The Lego Technic set was "
     "designed by a team in Denmark.&rdquo;</em>",
     ["A team in Denmark",
      "The Lego Technic set",
      "Denmark",
      "The verb phrase &ldquo;was designed&rdquo;"],
     "q3why"),

    ("Which sentence uses the <strong>passive voice correctly</strong>?",
     ["The Lego bricks were sorted by colour before assembly.",
      "The Lego bricks were sort by colour before assembly.",
      "The Lego bricks was sorted by colour before assembly.",
      "The Lego bricks sorted by colour before assembly."],
     "q4why"),

    # distractors lengthened so the key is no longer the sole longest option
    ("Why might a writer use the <strong>passive</strong> here? <em>&ldquo;Lego was "
     "founded in Denmark in 1932.&rdquo;</em>",
     ["Because the founder&rsquo;s identity is less important than the company&rsquo;s "
      "history.",
      "Because the writer is deliberately hiding the founder&rsquo;s name from the "
      "reader.",
      "Because nobody has ever managed to discover who actually founded the company.",
      "Because the passive voice is always more formal than the active in every "
      "context."],
     "q5why"),

    ("Select the sentence in the <strong>present perfect passive</strong>.",
     ["New Lego themes have been introduced every year for decades.",
      "More than 400 billion Lego bricks are produced each year.",
      "The Lego Movie had been watched by millions globally.",
      "Lego&rsquo;s headquarters have been located in Billund for decades."],
     "q6why"),

    ("Identify the <strong>mistake</strong> in: <em>&ldquo;A limited-edition set was "
     "been launched at the toy fair.&rdquo;</em>",
     ["Both &ldquo;was&rdquo; and &ldquo;been&rdquo; are used together, which is "
      "incorrect.",
      "The past participle &ldquo;launched&rdquo; should be &ldquo;launching&rdquo;.",
      "The subject needs to be changed to the plural form.",
      "The agent phrase introduced by &ldquo;by&rdquo; is missing at the end."],
     "q7why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: the verb-form gaps ─────────────────────────────────────
# the page's yellow tense chip is folded into the bracket cue after a &middot;
FIB = [
    ("The famous Lego Millennium Falcon set ______ (assemble &middot; present perfect "
     "passive) by fans in over 80 countries.",
     ["has been assembled|'s been assembled|s been assembled"],
     "g1why"),

    ("Every year, more than 75 billion Lego elements ______ (manufacture &middot; "
     "present simple passive) at factories in Denmark and Hungary.",
     ["are manufactured"], "g2why"),

    ("The instructions for the Lego Eiffel Tower set ______ (write &middot; present "
     "simple passive) in 13 different languages.",
     ["are written"], "g3why"),

    ("The original Lego brick design ______ (patent &middot; simple past passive) in "
     "Denmark in 1958.",
     ["was patented"], "g4why"),

    ("Before the new range ______ (launch &middot; simple past passive), extensive "
     "safety testing had been carried out on every piece.",
     ["was launched"], "g5why"),

    ("The Lego Ideas programme allows fans to submit designs that might ______ (turn "
     "into &middot; passive infinitive: be + past participle) an official set.",
     ["be turned into"], "g6why"),
]

# No bank. The lemma is given in brackets after every gap, so the task is to inflect
# a verb the learner already has, not to choose a word; six answers laid out would be
# the key.
BANK = None


# ── Activity 3: active → passive matching ──────────────────────────────
# a real MATCH, not a SORT: five left-hand actives, five distinct right-hand passives
MATCH = [
    ("Ole Kirk Christiansen founded Lego in 1932.",
     "Lego was founded by Ole Kirk Christiansen in 1932."),
    ("Engineers test every Lego brick for quality.",
     "Every Lego brick is tested for quality by engineers."),
    ("The company releases new themed sets each year.",
     "New themed sets are released each year by the company."),
    ("A Danish toy designer created the classic minifigure.",
     "The classic minifigure was created by a Danish toy designer."),
    ("Fans have built an enormous Lego model of Big Ben.",
     "An enormous Lego model of Big Ben has been built by fans."),
]


# ── Activity 4: rebuild the passive sentence ───────────────────────────
# the page's two drag-and-drop items, kept as their own activity (chunks, why)
ORDER = [
    (["Lego", "City", "has", "been", "sold", "in", "over", "50", "countries"],
     "o1why"),

    (["The", "instruction", "booklet", "was", "translated", "into", "15",
      "languages"], "o2why"),
]


# GRAMMAR REFERENCE —
# The pre-question card teaches the passive in four blocks.
#
# 1. THE TWO VOICES. Active = Subject → Verb → Object; the subject *performs* the
# action; the most common voice in English, direct and clear. Example: "Lego
# releases new sets every year." Passive = Subject + be + past participle; the
# subject *receives* the action, and the agent (the doer) may be omitted or
# introduced with "by". Example: "New sets are released every year (by Lego)."
#
# 2. THE TRANSFORMATION, three mechanical steps. (a) The object becomes the new
# subject. (b) The verb becomes be + past participle, in the tense of the original
# verb. (c) The old subject becomes "by + agent", which is optional. Worked example:
# active "Ole Kirk Christiansen founded Lego in 1932." → passive "Lego was founded by
# Ole Kirk Christiansen in 1932."
#
# 3. THE TENSE TABLE, six rows (tense | active | passive form):
#   Present Simple      | Lego makes bricks.        | is/are + made
#   Past Simple         | They built a castle.      | was/were + built
#   Present Perfect     | She has tested the set.   | has/have + been + tested
#   Past Perfect        | He had launched it.       | had + been + launched
#   Modal (will/can…)   | You can assemble it.      | can + be + assembled
#   Passive Infinitive  | —                         | to be + past participle
#
# 4a. WHEN TO USE THE PASSIVE, four points: the doer is unknown ("The brick was
# dropped."); the doer is obvious or unimportant; to focus on the result rather than
# the person; in formal or scientific writing.
#
# 4b. COMMON MISTAKES, four points: using "was been" instead of "was" or "has been";
# wrong agreement ("The bricks was made" ✗); forgetting "by" when the agent matters;
# using the wrong past participle form.


# ORIGINAL EXPLANATIONS —
# q1: Option C uses 'was released' — the subject (the Lego model) receives the action. The other three all have subjects actively performing their verbs, making them active voice.
# q2: The active is present simple, so the passive uses 'are bought.' The object (Lego sets) becomes the subject. Option A is past tense (incorrect), and B is present continuous active.
# q3: The agent is introduced by 'by' and tells us who did the action. Here, 'a team in Denmark' designed the set — they are the agent.
# q4: Option B is correct: 'were sorted' — plural 'were' agrees with 'bricks', and 'sorted' is the past participle. A has a spelling error, C uses singular 'was', and D omits the auxiliary verb 'be'.
# q5: Writers use the passive to shift focus onto what happened rather than who did it. The key facts are Lego's founding year and country. Saying the passive is 'always' more formal is an oversimplification.
# q6: Option D — 'have been introduced' — is present perfect passive. A is present simple passive. B is past perfect passive. C uses a stative verb describing a state rather than a completed action.
# q7: 'Was been' is the error — you cannot combine simple past 'was' with 'been'. Use 'was launched' (simple past passive) or 'has been launched' (present perfect passive). Omitting the agent is perfectly acceptable.
# g1: Present perfect passive: 'has been assembled.' The set (subject) receives the action; present perfect shows a completed action with present relevance.
# g2: Present simple passive: 'are manufactured.' Plural 'are' agrees with 'elements', and the passive shows the elements receive the action.
# g3: 'Are written' — present simple passive. 'Instructions' is plural, so use 'are' + the past participle 'written'.
# g4: Simple past passive: 'was patented.' The design is singular and the event happened at a specific past time (1958), so use 'was' + past participle.
# g5: 'Was launched' — simple past passive. The main clause uses past perfect, showing testing happened before the launch. Simple past is correct for the 'before' clause.
# g6: After a modal ('might'), use the passive infinitive: be + past participle. 'Might be turned into' — the design receives the action.
# m1: (none)
# m2: (none)
# m3: (none)
# m4: (none)
# m5: (none)
# d1: Present perfect passive: Subject (Lego City) + has been + past participle (sold) + place phrase.
# d2: Simple past passive: Subject + was + past participle (translated) + prepositional phrase.
