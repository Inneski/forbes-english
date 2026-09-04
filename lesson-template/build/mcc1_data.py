# -*- coding: utf-8 -*-
"""Minecraft (C1) &mdash; the thirty-one scored items.

Lifted from `forbes-english-minecraft-c1.html`, the dark blue and amber tabbed
page that runs five activities behind five tabs: six multiple choice questions on
C1 lexis and one tense contrast, six typed gap sentences on formal register, six
drag-and-drop gaps on collocation, seven Minecraft terms matched to definitions,
and a six-sentence account of the game&rsquo;s history to be put back into order.
Every one of the thirty-one survives here and the page&rsquo;s own explanation for
each is reproduced verbatim at the foot of the file.

The shapes follow what the items are rather than what the page called them. The
first activity is `MC` because each question offers four options with exactly one
key. The third activity is also `MC`, and is merged into the same list as items
seven to twelve, because although the page dragged chips into gaps, each sentence
carries its own set of four candidate phrases of which three are errors written
for that sentence alone &mdash; &ldquo;comply to&rdquo; is only wrong under
&ldquo;guidelines&rdquo;, &ldquo;capitalised at&rdquo; only wrong under
&ldquo;potential&rdquo; &mdash; so the distractors cannot be pooled into a bank
without losing the contrast each one teaches, and a stem with one blank and four
targeted options is a multiple choice question whatever the page calls it. The
second activity is `FIB`, six typed gaps with `FIB_BANK` supplying the six formal
words, because each frame has one gap and one intended word and the task is
lexical retrieval rather than choosing between prepared errors. The fourth is a
true `MATCH` and not a `SORT`: seven terms against seven definitions that repeat
nothing, so `match()` can pair them one to one. The fifth is `ORDER`, one row of
six chunks, because the task is a single argued sequence and not six separate
judgements &mdash; the page scored a point per correct position, which is what an
order row does. No activity here is a true/false or a many-to-few task, so nothing
became a `SORT`.

Seven defects were repaired. **Five keys were conspicuously the longest option on
their slide.** In activity one the spawn question&rsquo;s key ran ninety
characters against seventy-six, the biome question&rsquo;s one hundred and
sixty-three against one hundred and twenty-six, the iterative question&rsquo;s one
hundred and thirty-six against one hundred and three, the resource-acquisition
question&rsquo;s one hundred and fifty against one hundred and seven, and the
venture-forth question&rsquo;s one hundred and fourteen against ninety-one; a
learner could pass all five by measuring rather than reading. Every distractor is
lengthened &mdash; never a key shortened &mdash; and each stays exactly the error
it was: &ldquo;spawn&rdquo; used transitively for setting something up or
creating it, a biome reduced to a cosmetic skin, to a storage mechanic and to a
score multiplier the game does not have, &ldquo;iterative&rdquo; misapplied to
repeated complaints, to repetitive scenery and to an unpredictable blast, and
&ldquo;venture forth&rdquo; given the object it cannot take. **The
resource-acquisition question&rsquo;s second option did not contain the phrase the
stem asks about**: the stem says &ldquo;identify the sentence in which the phrase
resource acquisition is used most appropriately&rdquo; while the option read
&ldquo;Getting resources is the most basic activity a player does&rdquo;, which
uses no such phrase and could be struck out without reading it. It now uses the
phrase and fails on register instead, which is the criterion the stem actually
names. **Four of the six typed gaps admitted several honest answers while
accepting one.** &ldquo;Maintain a constant ______&rdquo; takes watchfulness and
alertness as readily as vigilance, &ldquo;______ deterministic&rdquo; takes
computationally and mathematically, and the bare frames for conduit and manipulate
take a dozen words each; the page nonetheless marked everything but its own word
wrong. `FIB_BANK` now supplies the six intended words, so the gaps are answerable
by choosing the collocation rather than by guessing the author&rsquo;s synonym,
and the near-synonyms the page&rsquo;s own explanations concede are still accepted
in the answer strings.

Three further faults are recorded and left alone. The past perfect continuous
question, item three, has two defensible answers: its own explanation admits that
&ldquo;were fortifying&rdquo; is &ldquo;plausible but less precise&rdquo;, and
with no past reference point in the stem beyond &ldquo;by dawn&rdquo; the past
continuous is not actually wrong, merely weaker. Item twelve is the same fault in
milder form &mdash; &ldquo;seized upon&rdquo; collocates perfectly well with
&ldquo;potential&rdquo;, so the item has a second answer its explanation never
addresses. And item seven&rsquo;s explanation recommends &ldquo;comply with&rdquo;
while noting it &ldquo;was not provided&rdquo;, which leaves the feedback teaching
a form the item neither offers nor scores. Repairing any of the three would cost
more of the lesson than it costs the learner.

The ordering activity&rsquo;s six chunks were whole sentences of between one
hundred and thirty and one hundred and eighty-five characters, which will not fit
a 1280x720 stage without shrinking the type, so they are short labels here and the
sentences move into the explanation; they are kept verbatim in a comment above
`ORDER` so nothing is lost.

The keys were also respread. In the page&rsquo;s own DOM order activity one sat at
B, B, C, B, C, A and activity three keyed the first chip of every pool, so eleven
of the twelve keys sat at index zero or one; `MC_POS` puts them over all four
indices below. The assertion under `_place` proves nothing was lost in the move.

The English being taught is never translated: stems, options and chunks stay in
English in every language build, per house style.
"""

# ── Activities 1 and 3: language and context, collocation and register ─
# ORIGINAL key positions, in the page's DOM order: activity one ran
# [1, 1, 2, 1, 2, 0] and activity three keyed element zero of every pool,
# [0, 0, 0, 0, 0, 0] — eleven of twelve at index zero or one. Respread:
MC_POS = [2, 0, 3, 3, 1, 0, 2, 1, 3, 0, 2, 1]

# (stem, [options with the KEY FIRST], why-key)
_MC_RAW = [
    ("In the context of Minecraft, which sentence best demonstrates the "
     "correct use of the verb <strong>to spawn</strong>?",
     ["Upon entering a new biome, hostile mobs may spawn automatically if "
      "lighting levels are low.",
      "The explorers decided to spawn their camp near the river delta before "
      "the light failed.",
      "She worked hard to spawn a reputation for excellence among the other "
      "builders on the server.",
      "The architect chose to spawn a bold new aesthetic into the facade of "
      "the building she designed."],
     "q1why"),

    ("Which of the following most accurately describes the concept of a "
     "Minecraft <strong>biome</strong> using formal register?",
     ["A biome constitutes a distinct geographical region within the game "
      "world, characterised by specific climate conditions, terrain features, "
      "and endemic flora and fauna.",
      "A biome is a randomly selected decorative backdrop applied to the "
      "visual surface of the world map, altering its colours without changing "
      "anything a player can dig through.",
      "A biome functions as a temporary protected zone in which players may "
      "store the resources they have collected, sheltered from interference "
      "by mobs while they are logged out.",
      "A biome refers to the scoring multiplier the game applies whenever "
      "players successfully navigate hazardous terrain, rewarding them in "
      "proportion to the danger survived."],
     "q2why"),

    ("A player writes: &ldquo;We _____ our base overnight, resulting in a "
     "formidable defensive perimeter by dawn.&rdquo; Which <strong>verb "
     "phrase</strong> best completes the sentence at C1 level?",
     ["had been fortifying",
      "did build up",
      "were fortifying",
      "have been building"],
     "q3why"),

    ("Which of the following sentences uses the word <strong>iterative</strong> "
     "correctly in relation to Minecraft game development?",
     ["Minecraft&rsquo;s development followed an iterative process, with "
      "frequent updates refining gameplay mechanics based on community "
      "feedback.",
      "The iterative complaints from players eventually forced the developers "
      "to shut the servers down without any warning at all whatsoever.",
      "Players consistently found the iterative landscape of the Nether biome "
      "particularly disorienting whenever they attempted to explore it alone.",
      "The iterative nature of the creeper&rsquo;s explosion made it a "
      "thoroughly unreliable tool for mining resources at any real depth."],
     "q4why"),

    ("Identify the sentence in which the phrase <strong>resource "
     "acquisition</strong> is used most appropriately for an academic essay "
     "about Minecraft&rsquo;s economic mechanics.",
     ["Resource acquisition constitutes the foundational economic behaviour "
      "underpinning all subsequent crafting and technological progression "
      "within the game.",
      "Resource acquisition is basically when you go round collecting loads of "
      "wood and stone and stuff so that you can make things with it later on "
      "in the game.",
      "Resource acquisition is pretty much the most basic thing that a player "
      "ever does in Minecraft, and honestly it never really stops being "
      "important.",
      "Players must do resource acquisition first, before they are ever "
      "allowed to craft any of the new items or to build structures anywhere."],
     "q5why"),

    ("Which sentence correctly uses the phrase <strong>to venture "
     "forth</strong> in a Minecraft context?",
     ["Players must venture forth into unexplored territories to gather rare "
      "materials unavailable near the spawn point.",
      "The game requires players to venture forth their entire inventory "
      "before they may enter a new dimension on foot.",
      "Builders venture forth complex architectural blueprints to the server "
      "owner prior to commencing any construction.",
      "To venture forth a server of their own, administrators must first "
      "configure port forwarding on their home router."],
     "q6why"),

    ("Players who engage in multiplayer servers must _____ established "
     "community guidelines to avoid being permanently banned.",
     ["adhere to", "comply to", "sustain at", "conform at"],
     "q7why"),

    ("The modding community has _____ the base game&rsquo;s content, "
     "introducing thousands of user-generated features.",
     ["substantially augmented", "hugely increased up", "very much widened",
      "greatly expanded over"],
     "q8why"),

    ("The Ender Dragon is widely _____ the game&rsquo;s primary antagonist, "
     "despite the absence of a conventional narrative arc.",
     ["regarded as", "considered to", "viewed for", "known by"],
     "q9why"),

    ("Speedrunners often _____ obscure game mechanics and glitches to "
     "complete the campaign in record time.",
     ["exploit", "misuse", "abuse", "leverage"],
     "q10why"),

    ("The game&rsquo;s _____ terrain ensures that no two worlds are "
     "identical, contributing to virtually limitless replayability.",
     ["procedurally generated", "randomly constructed", "digitally assembled",
      "computationally rendered"],
     "q11why"),

    ("Many educators have _____ Minecraft&rsquo;s creative potential as a "
     "pedagogical tool, incorporating it into STEM curricula worldwide.",
     ["harnessed", "exploited", "seized upon", "capitalised at"],
     "q12why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: complete the passage ───────────────────────────────────
# One gap, one intended word, typed. The page gave no bank and no hint and
# accepted only its own synonyms; the bank below is the repair.
FIB = [
    ('The game&rsquo;s survival mode requires players to maintain a constant '
     '______ against environmental hazards and hostile entities that emerge '
     'after nightfall.',
     ['vigilance|watchfulness|alertness'], 'g1why'),

    ('Minecraft&rsquo;s open-ended structure has been widely ______ for '
     'fostering creativity, problem-solving, and collaborative skills among '
     'players of all ages.',
     ['lauded|praised|acclaimed'], 'g2why'),

    ('The Redstone system serves as the game&rsquo;s primary ______ for '
     'complex mechanical engineering, enabling players to construct elaborate '
     'automated contraptions.',
     ['conduit|mechanism|means'], 'g3why'),

    ('Critics have argued that the game&rsquo;s procedurally generated worlds '
     'are, to a certain extent, ______ deterministic, despite appearing '
     'random to the casual observer.',
     ['algorithmically|computationally'], 'g4why'),

    ('The cultural ______ of Minecraft extends far beyond gaming, permeating '
     'education, architecture, and digital art communities worldwide.',
     ['resonance|impact|significance'], 'g5why'),

    ('By allowing players to ______ individual voxels within the game world, '
     'Minecraft grants an unprecedented degree of environmental agency.',
     ['manipulate|modify|alter'], 'g6why'),
]

# Sorted case-insensitively; the gap answers fall at 5, 2, 1, 0, 4, 3,
# which is not gap order and therefore not an answer key.
FIB_BANK = [
    'algorithmically', 'conduit', 'lauded', 'manipulate', 'resonance',
    'vigilance',
]


# ── Activity 4: match the terms ────────────────────────────────────────
# A real MATCH, not a SORT: seven terms, seven definitions, none repeated.
# The seven definitions ran 74 to 111 characters and the slide overflowed by
# 37px. They are trimmed to the defining clause; every one still models the
# register the lesson teaches — a noun phrase, a formal verb, and no "is when"
# anywhere — which is what they are here for.
MATCH = [
    ('Redstone',
     'An in-game mineral functioning as an electrical conductor'),
    ('Biome',
     'A distinct region with its own climate, terrain and biodiversity'),
    ('Procedural generation',
     'Algorithmic creation of content from rules rather than by hand'),
    ('Voxel',
     'A three-dimensional pixel: one unit of volume in a grid'),
    ('Mob',
     'A generic term for any autonomous entity in the game world'),
    ('The Nether',
     'A hostile parallel dimension reached through an obsidian portal'),
    ('Speedrunning',
     'Completing a game as fast as possible, often exploiting glitches'),
]



# ── Activity 5: reorder the sentences ──────────────────────────────────
# One sequence, six chunks. The page fed six whole sentences into the pool,
# running 130 to 185 characters each; six of those will not fit a 1280x720
# stage without shrinking the type, which the house style forbids. They are
# short labels here and the sentences belong in the explanation. Verbatim:
#   1. "Minecraft was originally developed by Markus Persson, known as
#      'Notch', and released in 2011 under the auspices of Mojang Studios."
#   2. "Despite its deceptively simple visual aesthetic, the game conceals a
#      layer of considerable technical depth, particularly in its Redstone
#      circuitry system."
#   3. "This system enables players to construct functioning logic gates,
#      automated farms, and even rudimentary computers within the game's voxel
#      environment."
#   4. "Consequently, Minecraft has transcended its origins as a sandbox game
#      to become a recognised educational platform, employed in schools across
#      more than 100 countries."
#   5. "Its enduring cultural relevance is perhaps best evidenced by the fact
#      that, as of 2024, it remains the best-selling video game in history,
#      with over 300 million copies sold."
#   6. "Scholars in the fields of digital humanities and educational technology
#      continue to explore the pedagogical implications of open-world,
#      player-driven learning environments such as this."
ORDER = [
    (['Notch released Minecraft in 2011',
      'Simple graphics hide technical depth',
      'Redstone builds logic gates and farms',
      'Consequently, schools in 100+ countries',
      'Best-selling game ever: 300m copies',
      'Scholars study open-world learning'], 'o1why'),
]


# ORIGINAL EXPLANATIONS —
# q1: 'To spawn' in gaming means for entities to appear or be generated in the game world. Option B correctly uses it in a gaming context: mobs appearing under specific environmental conditions. The other options use 'spawn' metaphorically or incorrectly.
# q2: Option B uses precise formal language: 'constitutes,' 'characterised by,' 'endemic,' and 'terrain features.' This accurately mirrors how 'biome' is defined in both ecology and game design. The other options either misrepresent the concept or use incorrect register.
# q3: 'Had been fortifying' is the past perfect continuous, expressing an ongoing action completed before a specific past moment ('by dawn'). This is the most grammatically precise choice for a C1 context. 'Were fortifying' is plausible but less precise about completion.
# q4: 'Iterative' means involving repetition of a process to achieve progressive improvements. Option B correctly applies this to software development: repeated cycles of updates based on feedback. The other options misapply the word in gaming contexts where it has no technical meaning.
# q5: Option C employs formal academic register with precise vocabulary: 'constitutes,' 'foundational,' 'underpinning,' and 'technological progression.' This is consistent with C1+ academic writing. The other options use informal, vague, or grammatically awkward constructions inappropriate for formal analysis.
# q6: 'To venture forth' is an intransitive phrasal verb meaning to go out boldly, especially into unknown territory. Option A uses it correctly: players moving into unexplored areas. The other options incorrectly use it as a transitive verb, treating it as if it takes an object.
# q7: 'Adhere to' is the correct collocation with 'guidelines' or 'rules.' 'Comply with' is also correct but was not provided. 'Comply to' and 'conform at' are incorrect prepositional combinations.
# q8: 'Substantially augmented' is the most precise and formal collocation. 'Augmented' means increased or enlarged, and 'substantially' is an appropriate C1-level adverb. The other options contain redundant prepositions or less precise vocabulary.
# q9: 'Regarded as' is the standard collocation when identifying something's role or classification. 'Considered to be' is also correct, but 'considered to' alone is incomplete. The other prepositions are incorrect with these verbs.
# q10: In gaming contexts, 'exploit' is the precise technical term for using game mechanics — especially unintended ones — to one's advantage. While 'leverage' is close, it lacks the technical connotation of using glitches. 'Misuse' and 'abuse' carry negative moral connotations not appropriate here.
# q11: 'Procedurally generated' is the established technical term in game design for content created algorithmically according to rules. This is the standard industry collocation and would be expected in any formal discussion of Minecraft's design.
# q12: 'Harnessed' collocates correctly with 'potential' (to harness potential) and carries a positive, purposeful connotation — ideal in educational contexts. 'Capitalised on' would also work, but 'capitalised at' is incorrect. 'Exploited' has a negative connotation unsuitable here.
# g1: 'Vigilance' (noun) collocates naturally with 'maintain' and means watchful alertness. 'Awareness' is possible but less formal; 'attention' doesn't collocate with 'maintain' in this context.
# g2: 'Lauded' means praised highly, typically in a formal or written context. 'Praised' and 'acclaimed' are also accepted. Avoid informal alternatives like 'loved' or 'liked' at C1 level.
# g3: 'Conduit' metaphorically means a channel or means through which something is transmitted. It collocates well with 'serves as' and conveys technical precision. 'Mechanism' is also accepted.
# g4: 'Algorithmically' is the correct adverb form here, modifying 'deterministic.' The sentence uses sophisticated hedging ('to a certain extent') and technical vocabulary, consistent with C1 academic writing.
# g5: 'Resonance' means the quality of evoking or suggesting images, memories, and emotions, used metaphorically here. It collocates well with 'cultural' and conveys depth of influence. 'Impact' is a simpler but acceptable alternative.
# g6: 'Manipulate' means to handle or control (something) with skill. In technical game design contexts, it precisely conveys deliberate, skilled alteration of discrete units. 'Modify' and 'alter' are simpler but accepted alternatives.
# m1: (none)
# m2: (none)
# m3: (none)
# m4: (none)
# m5: (none)
# m6: (none)
# m7: (none)
# o1: (none)


# WHAT THIS LESSON TEACHES —
#
# REGISTER. The spine of the lesson is the gap between how a gamer talks and how
# an academic writes about games, and half the items are decided on register
# alone. The formal frame is built from a small set of high-value verbs and
# nouns the learner is expected to produce: a thing "constitutes" something
# rather than "is" it, a region is "characterised by" its features, a behaviour
# "underpins" what follows, a system "serves as" a channel for something, a
# structure has been "widely lauded for" doing something. Set against these are
# the informal moves that disqualify an option at C1 — vague quantifiers ("wood
# and stone and stuff"), the discourse marker "basically" and "honestly", the
# defining relative opened with "is when", and the empty verb in "do resource
# acquisition" where the phrase needs no verb at all. The teaching point is that
# an academic sentence is not a formal-sounding word dropped into a casual
# frame: the whole clause has to change.
#
# COLLOCATION AND DEPENDENT PREPOSITIONS. Six fixed pairings carry activity
# three, each with its near-miss written out. You adhere to guidelines (and
# comply with them, never comply to them, and never conform at them); something
# is regarded as a thing or considered to be one, but never viewed for or known
# by it; you substantially augment content rather than increase it up or expand
# it over; you harness potential, and you may capitalise on it but never at it.
# Two items turn on connotation rather than grammar: exploit is the neutral
# technical verb for using a game mechanic, while misuse and abuse import a
# moral judgement the sentence does not want, and harness is positive where
# exploited would insult the teachers it describes. Two more turn on which term
# a field has actually fixed: procedurally generated is the industry term for
# rule-driven content, against randomly constructed and computationally
# rendered, which describe nothing in particular.
#
# LEXIS. Around a dozen C1 words are taught in use rather than in isolation: to
# spawn (intransitive, of entities appearing under conditions — the item exists
# to stop the learner using it transitively for "set up" or "create"); to
# venture forth (intransitive phrasal verb, to go out boldly into the unknown,
# and it takes no object); iterative (repeated cycles that progressively refine
# something, a software word, not a synonym for repetitive or unpredictable);
# vigilance maintained against a hazard; a conduit as a metaphorical channel;
# cultural resonance; to manipulate discrete units; algorithmically
# deterministic, with the hedge "to a certain extent" attached. The seven
# matched terms give the topic vocabulary — Redstone as an in-game electrical
# conductor, biome, procedural generation, voxel, mob, the Nether, speedrunning
# — and each definition is itself a model of the formal register above.
#
# GRAMMAR. One tense contrast, item three: the past perfect continuous ("had
# been fortifying") for an action that ran up to and was finished by a stated
# past moment ("by dawn"), against the past continuous ("were fortifying"),
# which gives the action no endpoint, against the present perfect continuous
# ("have been building"), which cannot be used with a past time frame at all,
# and against the non-form "did build up". Elsewhere the grammar is at phrase
# level: transitivity in the spawn and venture-forth items, adverb formation in
# "algorithmically deterministic", and the passive plus adverb frame "has been
# widely lauded for" in the second gap.
#
# DISCOURSE. The ordering activity teaches how an argued paragraph about a
# subject is built: origin and date first, then a "despite" concession that
# introduces the technical claim, then "this system", a demonstrative reference
# that can only follow the sentence naming it, then "consequently" for the
# educational result, then the evidence sentence ("is perhaps best evidenced by
# the fact that"), and finally the widening move to what scholars make of it.
# Those five signals — a concessive opener, a demonstrative reference chain,
# consequently, an evidence formula, and a closing generalisation — are the
# transferable content, and they are worth pulling out of the paragraph and
# naming.
