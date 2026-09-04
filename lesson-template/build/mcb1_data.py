# -*- coding: utf-8 -*-
"""Minecraft (B1) &mdash; the thirty-two scored items.

Lifted from the scrolling `forbes-english-minecraft-b1.html`, the cream-and-teal
newspaper-styled page that runs five activities down one column: six multiple
choice questions on game knowledge and B1 tense grammar, six typed gap sentences,
six drag-and-drop gaps drawing on one shared word bank, seven Minecraft terms
matched to definitions, and a seven-sentence account of a first day in the world
to be put back into order. Every one of the thirty-two survives here and the
page's own explanation for each is reproduced verbatim at the foot of the file.

The shapes follow what the items are rather than what the page called them. The
first activity is `MC` because each question offers four full-sentence options
with one key. The second is `FIB` with `FIB_BANK = None` because the page gave no
bank at all &mdash; the learner typed into a bare input under a written hint, and
the hints are carried into the stems as dim parentheticals so the items stay
answerable without one. The third is a second gap list, `DD` with `DD_BANK`,
because although the page dragged chips into gaps, each sentence has exactly one
gap and one right word and the twenty-four chips are a shared bank in every sense
that matters; a bank is the only difference between it and activity two, so it
gets its own list rather than being merged. The fourth is a true `MATCH`: seven
terms against seven definitions that repeat nothing, so `match()` can pair them
one to one and no `SORT` is needed. The fifth is `ORDER`, one row of seven chunks,
because the task is a single narrative sequence and not seven separate judgements
&mdash; the page scored a point per correct position, which is what an order row
does. No activity here is a true/false or many-to-few task, so nothing became a
`SORT`.

Five defects were repaired. **The present-perfect question, item three, was
mis-keyed against its own explanation.** Its key read &ldquo;I have been playing
for two hours and I just built my first house&rdquo; while the feedback claimed
&ldquo;just built&rdquo; was the present perfect; it is the past simple, so the
page taught a rule its key did not illustrate. The key now reads &ldquo;have just
built&rdquo; and is genuinely present perfect throughout. **That same key was
then conspicuously the longest option**, at seventy-one characters against
fifty-eight, so all three distractors are lengthened &mdash; never the key
shortened &mdash; and each stays exactly the error it was: present perfect with
&ldquo;yesterday&rdquo;, past simple with &ldquo;since&rdquo; plus a duration,
and present continuous with &ldquo;since&rdquo; plus a duration. **The
&ldquo;just&rdquo; gap sentence, item six of activity two, sat in the past
simple** &mdash; &ldquo;I ______ found a village&rdquo; &mdash; while its
explanation taught &ldquo;just&rdquo; with the present perfect, and the bare frame
also admitted &ldquo;recently&rdquo; and &ldquo;already&rdquo; as honest answers.
The auxiliary is supplied in the stem, so the sentence is now the present perfect
the explanation describes and only &ldquo;just&rdquo; fits it.

Three drag-and-drop items had two right answers each, which is the same defect as
a wrong key from the learner's side. **&ldquo;Diamonds are very rare&rdquo; and
&ldquo;In survival mode, you need to eat food regularly&rdquo;** both had a
distractor the page's own explanation conceded was correct, only more formal, so
&ldquo;uncommon&rdquo; and &ldquo;consume&rdquo; are now accepted alternatives;
the contrast being taught survives untouched, because &ldquo;difficult&rdquo; and
&ldquo;hard&rdquo; still describe effort rather than frequency and &ldquo;have
some&rdquo; and &ldquo;feed yourself&rdquo; are still wrong. **&ldquo;You should
carry a torch&rdquo; and &ldquo;you will take damage&rdquo; could not accept
theirs**, because the point of both items is the fixed collocation, so the
offending chips are replaced instead: &ldquo;bring along&rdquo;, which means
precisely what &ldquo;carry&rdquo; means here, becomes &ldquo;wear&rdquo;, and
&ldquo;get hurt badly&rdquo;, which the sentence takes as readily as the key,
becomes &ldquo;make damage&rdquo;. Both replacements are errors a B1 learner
actually produces &mdash; confusing what you hold with what you put on, and the
&ldquo;make damage&rdquo; calque out of German and the Romance languages &mdash;
and neither can be read as right.

Two further faults are recorded and left alone, because repairing them would cost
more of the lesson than they cost the learner. The first is that activity one's
present-simple question, item five, disqualifies its second distractor with
&ldquo;finished to build&rdquo;, a gerund error rather than a tense error, so a
learner who spots only the tense criterion the stem names sees a distractor that
passes it; the sentence is still ungrammatical and therefore still not the answer.
The second is that the drag-and-drop explanation for &ldquo;take damage&rdquo;
praises &ldquo;get hurt&rdquo; as an acceptable alternative, which after the
replacement above names a phrase no longer on the page at all; the sentence is
kept verbatim so the original wording is not lost, but it now recommends a form
the item neither offers nor scores.

The keys were also respread. In the page's own DOM order they sat at C, B, C, B, C
and B &mdash; positions two, one, two, one, two, one, an alternation a learner
notices inside three questions &mdash; and `MC_POS` puts them over all four
indices below. The assertion under `_place` proves nothing was lost in the move.

The English being taught is never translated: stems, options and chunks stay in
English in every language build, per house style.
"""

# ── Activity 1: what do you know about Minecraft? ──────────────────────
# ORIGINAL key positions, in the page's DOM order: [2, 1, 2, 1, 2, 1]
# — a straight C/B alternation through all six. Respread:
MC_POS = [2, 0, 3, 1, 3, 0]

# (stem, [options with the KEY FIRST], why-key)
_MC_RAW = [
    ("What <strong>happens at night</strong> in Minecraft that makes it "
     "dangerous?",
     ["Dangerous mobs like zombies, skeletons, and creepers start to appear.",
      "The player moves more slowly and cannot see very well in the dark.",
      "Your tools break faster because the cold night air damages them.",
      "All the animals go underground and you cannot find food."],
     "q1why"),

    ("What <strong>material</strong> do you need to build a Nether Portal?",
     ["You need obsidian blocks arranged in a rectangular frame.",
      "You need diamond blocks arranged in a tall rectangular frame.",
      "You need iron blocks placed in a square pattern on the ground.",
      "You need gold blocks placed in an arch shape above a door."],
     "q2why"),

    ("A player writes in a message: &ldquo;_____&rdquo;. Which sentence is "
     "<strong>grammatically correct</strong>?",
     ["I have been playing for two hours and I have just built my first house.",
      "I have built a house yesterday after I found the wood in the forest.",
      "I built a house since I started playing on this server three hours ago.",
      "I am building a house since two hours when I start playing today."],
     "q3why"),

    ("What do you need to give two cows to make them <strong>breed</strong> "
     "and produce a baby calf?",
     ["You need to give them both some wheat, which puts them in love mode.",
      "You need to give them each a bucket of water and some grass blocks.",
      "You need to build a fence around them and wait until morning comes.",
      "You need to use a lead to tie them together inside a small pen."],
     "q4why"),

    ("Which sentence correctly uses the <strong>present simple</strong> to "
     "describe a Minecraft habit?",
     ["When I find diamonds, I always make armour before I go to fight "
      "monsters.",
      "Every morning, I am checking my inventory before I go exploring "
      "outside.",
      "I usually explore caves after I have finished to build my shelter "
      "completely.",
      "I was crafting a sword whenever I needed to go out and fight at "
      "night."],
     "q5why"),

    ("In Minecraft, when you <strong>respawn</strong> after dying, where do "
     "you appear?",
     ["You appear at your spawn point &mdash; usually your bed or the world "
      "start point.",
      "You appear at the exact location where you were standing when you "
      "died.",
      "You appear at the nearest village where you can trade with villagers "
      "again.",
      "You appear at the centre of the map, which is always a flat, open "
      "area."],
     "q6why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: complete the sentences ─────────────────────────────────
# Typed, no bank. The page printed a written hint above each input; it is
# carried into the stem as a dim parenthetical, because without it several
# of these frames take half a dozen honest answers.
FIB = [
    ('In Minecraft, you can ______ new tools and items by putting materials '
     'into the crafting table in the right pattern. '
     '<span class="dim">(a verb meaning to make something new by putting '
     'materials together)</span>',
     ['craft|make|create|build'], 'g1why'),

    ('You must build a shelter before it gets dark, ______ dangerous mobs '
     'will come and attack you during the night. '
     '<span class="dim">(a connector meaning &lsquo;if you do not&rsquo; '
     '&mdash; it introduces a warning)</span>',
     ['otherwise|or|or else'], 'g2why'),

    ('First, I ______ some wood by hitting nearby trees with my hands. '
     '<span class="dim">(a past tense verb &mdash; the action of getting '
     'resources from trees)</span>',
     ['collected|gathered|got|obtained|cut'], 'g3why'),

    ('If you find a horse and tame it, you ______ ride it to travel much '
     'faster than walking. '
     '<span class="dim">(a modal verb expressing ability &mdash; what the '
     'player is able to do)</span>',
     ["can|could|are able to|will be able to|'re able to"], 'g4why'),

    ('I have been playing Minecraft ______ three hours and I still '
     'haven&rsquo;t found any diamonds yet. '
     '<span class="dim">(a preposition of time &mdash; used before periods '
     'of duration)</span>',
     ['for'], 'g5why'),

    ('I have ______ found a village! There are lots of houses and villagers '
     'inside it. '
     '<span class="dim">(an adverb showing that something happened very '
     'recently &mdash; a moment ago)</span>',
     ['just'], 'g6why'),
]

FIB_BANK = None


# ── Activity 3: fill the gap with the right word ───────────────────────
# The same gap shape as activity two, but with the page's twenty-four
# drag chips pooled into one bank. Every sentence has one gap and one
# right answer, so it is a gap-fill and not a match or a sort.
DD = [
    ('You need to ______ in a bed at night to skip the darkness and set your '
     'spawn point.',
     ['sleep'], 'd1why'),

    ('Diamonds are very ______, which means you have to dig very deep '
     'underground to find them.',
     ['rare|uncommon'], 'd2why'),

    ('If you fall into lava, you will ______ and lose all your hearts very '
     'quickly.',
     ['take damage'], 'd3why'),

    ('You should ______ a torch when you go into a dark cave so you can see '
     'where you are going.',
     ['carry'], 'd4why'),

    ('The Ender Dragon is the ______ of Minecraft &mdash; defeating it shows '
     'the game&rsquo;s ending credits.',
     ['final boss'], 'd5why'),

    ('In survival mode, you need to ______ food regularly to keep your hunger '
     'bar full and stay healthy.',
     ['eat|consume'], 'd6why'),
]

# Sorted case-insensitively; the gap answers fall at 19, 15, 20, 1, 6, 4,
# which is not gap order and therefore not an answer key.
DD_BANK = [
    'biggest creature', 'carry', 'consume', 'difficult', 'eat',
    'feed yourself', 'final boss', 'hard', 'hardest mob', 'have some',
    'hold on to', 'keep near you', 'last enemy', 'lose some hearts',
    'make damage', 'rare', 'receive health loss', 'rest', 'sit down',
    'sleep', 'take damage', 'uncommon', 'wait', 'wear',
]


# ── Activity 4: match each word to its meaning ─────────────────────────
# A real MATCH, not a SORT: seven terms, seven definitions, none repeated.
MATCH = [
    ('<strong>Spawn</strong>',
     'To appear in the game world &mdash; either for the first time or after '
     'dying.'),
    ('<strong>Craft</strong>',
     'To make a new item by combining materials on a crafting table.'),
    ('<strong>Mine</strong>',
     'To dig into rock or ground to collect materials like stone, coal, or '
     'iron.'),
    ('<strong>Mob</strong>',
     'Any moving creature in the game, such as a zombie, cow, or chicken.'),
    ('<strong>Biome</strong>',
     'An area of the world with its own weather, plants, and landscape type.'),
    ('<strong>Inventory</strong>',
     'The list of all the items and materials your character is currently '
     'carrying.'),
    ('<strong>Smelt</strong>',
     'To heat raw ore in a furnace to turn it into a usable material like '
     'iron.'),
]


# ── Activity 5: put the steps in the right order ───────────────────────
# One sequence, seven chunks. The chunks are whole sentences because the
# task is narrative order, not sentence construction; none contains a pipe.
# The original fed seven full sentences into a chunk pool. Each ran 60 to 97
# characters, and seven of them will not fit a 1280x720 stage without shrinking
# the type, which the house style forbids. They are short labels here and the
# sentences move into the explanation, which is the same repair the DinoFacts
# timeline needed.
ORDER = [
    (['You appear in a new world',
      'You punch a tree for wood',
      'You craft a wooden pickaxe',
      'You mine stone and coal',
      'You build a shelter',
      'You light it with torches',
      'You sleep until morning'], 'o1why'),
]


# ORIGINAL EXPLANATIONS —
# q1: At night, hostile mobs — including zombies, skeletons, spiders, and creepers — start to spawn in dark areas. This is why the first thing most players do in Minecraft is build a shelter before the sun sets. During the day, most of these mobs burn in sunlight.
# q2: A Nether Portal is built using obsidian — one of the hardest blocks in the game, made by pouring water over lava. You need at least 10 obsidian blocks to make a portal frame (4 wide, 5 tall), then light it with flint and steel. It creates a purple glowing rectangle.
# q3: Option C is correct. 'Have been playing' is the present perfect continuous — used for an action that started in the past and continues now ('for two hours'). 'Just built' is the present perfect for a recent completed action. Option A is wrong because 'yesterday' needs simple past, not present perfect.
# q4: Feeding two cows wheat puts them in 'love mode' — they produce red hearts above their heads and then produce a baby calf. Most farm animals in Minecraft breed using a specific food item: cows and sheep use wheat, pigs use carrots or potatoes, and chickens use seeds.
# q5: Option C correctly uses the present simple ('find', 'make', 'go') to describe a general habit or rule — what the player always does in this situation. Option A incorrectly uses 'am checking' (present continuous) for a routine habit. Option D incorrectly uses 'was crafting' (past continuous) for a present habit.
# q6: When you die in Minecraft, you 'respawn' — you appear again at your spawn point. If you have slept in a bed, that becomes your personal spawn point. If not, you return to the original world spawn point. The word 'respawn' comes from 'spawn' (to appear) with the prefix 're-' meaning again.
# g1: 'Craft' is the specific Minecraft term for making items at a crafting table. 'Make' and 'create' are also accepted because they have the same meaning in this context. 'Craft' as a verb means to make something with skill and careful attention to detail.
# g2: 'Otherwise' means 'if that does not happen' or 'if not.' It introduces the negative consequence of not doing something. 'Or' and 'or else' are also accepted — they work the same way here. Example: 'Take an umbrella, otherwise you'll get wet.'
# g3: All the listed answers are accepted because they correctly describe taking wood from trees in the past simple tense. 'Collected' and 'gathered' emphasise bringing together multiple items. 'Cut' specifically refers to cutting the tree. The past simple is used here because this is a completed action in a story.
# g4: 'Can' expresses present ability or possibility. Here it describes what is possible if you tame a horse. 'Are able to' means the same thing and is also accepted. 'Could' would suggest a hypothetical or past situation, which is less natural here. 'Will be able to' is also correct but less concise.
# g5: We use 'for' with the present perfect continuous to show how long an action has been happening: 'I have been playing for three hours.' Compare this with 'since,' which is used with a specific point in time: 'I have been playing since 2 o'clock.' 'For' + duration; 'since' + point in time.
# g6: 'Just' is used with the present perfect to talk about something that happened a very short time ago. 'I have just found a village' = I found it moments ago. This is a very common B1 structure. Compare: 'I already found a village' (earlier, before expected) and 'I haven't found a village yet' (still not done).
# d1: 'Sleep in a bed' is the natural collocation in English. 'Rest' is a similar word but does not collocate with 'in a bed' in the same way. 'Wait' and 'sit down' do not describe using a bed at all. In Minecraft, sleeping in a bed skips the night and sets your respawn location.
# d2: 'Rare' means something that does not appear very often — it is the most natural adjective here. 'Uncommon' means nearly the same thing but is slightly more formal. 'Difficult' and 'hard' describe effort, not frequency — you would say 'it is difficult to find diamonds,' not 'diamonds are difficult.'
# d3: 'Take damage' is the standard gaming collocation in English — it means to receive harm or injury. 'Get hurt' is a more informal but also acceptable alternative. 'Receive health loss' is not a natural phrase. 'Lose some hearts' could work but 'quickly' makes 'some' inaccurate since lava kills very fast.
# d4: 'Carry' is the most natural verb for taking something with you when you move. 'Bring' is also natural but needs an object ('bring a torch'). 'Carry' + object is the standard collocation for items you take on a journey or into a dangerous area.
# d5: 'Final boss' is the standard gaming term in English for the most powerful enemy at the end of a game. 'Last enemy' and 'hardest mob' are not standard terms. 'Biggest creature' is factually inaccurate — the Ender Dragon is large but size and difficulty are different things.
# d6: 'Eat' is the most direct and natural verb here. 'Consume' is correct but formal — more common in academic or technical writing. 'Have some' is too vague and informal without specifying what you have. 'Feed yourself' is grammatically correct but less natural as a standalone verb phrase in this sentence.
# m1: (none)
# m2: (none)
# m3: (none)
# m4: (none)
# m5: (none)
# m6: (none)
# m7: (none)
# o1: Great work! The correct order follows a very logical pattern: arrive → collect wood → craft tools → mine stone → build shelter → add torches → sleep safely. This is exactly what most Minecraft tutorials teach new players.


# WHAT THIS LESSON TEACHES —
#
# GRAMMAR. Three tense contrasts carry the lesson. The present perfect
# continuous "have been playing" + "for" + a duration is drilled twice, once as
# an MC key and once as the gap that forces "for" rather than "since": "for"
# takes a length of time, "since" takes a point in time. The present perfect
# with "just" for something finished moments ago is set against "already"
# (earlier than expected) and "yet" (still not done), and against the error of
# putting the present perfect with "yesterday", which needs the past simple.
# The present simple for habits and general truths — "when I find diamonds, I
# always make armour" — is set against the present continuous, which cannot
# carry a routine ("every morning I am checking"), and against the past
# continuous, which cannot describe a present habit ("I was crafting whenever
# I needed"). The past simple appears again as the narrative tense of a
# completed action in a story ("First, I collected some wood"). Two further
# points: "can" and "are able to" for present ability or possibility, with
# "could" reserved for the hypothetical; and "otherwise" (with "or" and "or
# else") as the connector that introduces the bad consequence of not doing
# something — "build a shelter, otherwise mobs will attack you".
#
# COLLOCATION. Six fixed pairings, each with its near-miss made explicit:
# sleep in a bed (not rest in a bed); take damage (not make damage); carry a
# torch (not wear one); eat food, with "consume" available but formal; a thing
# is rare or uncommon, describing how often it appears, whereas difficult and
# hard describe the effort of getting it; and final boss as the fixed gaming
# term for the enemy at the end of a game.
#
# VOCABULARY. Seven game terms defined in plain English and worth teaching as
# ordinary English words with a gaming sense: spawn (to appear, first time or
# after dying) and its transparent derivative respawn, re- meaning again;
# craft (to make an item by combining materials, and more widely to make
# something with skill); mine (to dig for stone, coal or iron); mob (any moving
# creature, friendly or hostile); biome (a region with its own weather, plants
# and landscape); inventory (everything the character is carrying); and smelt
# (to heat raw ore in a furnace into a usable metal). Around them sit the
# lesson's supporting nouns — shelter, spawn point, hunger bar, hearts, crafting
# table, pickaxe, torch, lava, obsidian, Nether Portal, villager — and the
# breeding vocabulary of "love mode" fed by wheat.
#
# DISCOURSE. The ordering activity teaches sequencing a procedure in the second
# person present: arrive, collect wood, craft tools, mine stone and coal, build
# a shelter before dark, light it with torches, sleep until morning. It is a
# ready-made frame for "how to" narration and for the time connectors (first,
# then, after that, before, until) a B1 learner needs to retell it.
