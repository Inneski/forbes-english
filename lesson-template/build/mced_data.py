# -*- coding: utf-8 -*-
"""Minecraft Trivia, the editorial cut &mdash; the thirty-two scored items.

Lifted from `forbes-english-minecraft-editorial.html`, the rust-and-cream
newspaper-styled B1 page that runs five activities down one column between
pixel-art illustration bands: six four-option trivia questions, six typed gap
sentences under written hints, six more gaps filled by dragging chips out of a
pooled word bank, seven Minecraft terms matched to seven surprising facts, and a
seven-step account of the road to the Ender Dragon to be put back into order.
All thirty-two survive here, and the page&rsquo;s own explanation for each is
reproduced verbatim at the foot of the file.

The shapes follow what the items are rather than what the page called them. The
first activity is `MC` because each question is a stem with four full-sentence
options and one key. The third activity joins it in the same `MC` list, because
although the page dragged chips it authored exactly four candidate answers for
each of its six sentences &mdash; the twenty-four chips in the bank are those six
private pools poured into one tray &mdash; so each item is a four-option choice
with a blank in the stem and nothing else. The second activity is the `FIB`,
with `FIB_BANK = None`, because it is genuinely typed free response: the page
offered no chips at all, only a written hint, and those hints are carried into
the stems as dim parentheticals because several of these facts &mdash; a
Y-coordinate, a push limit &mdash; are unguessable without them. The fourth is a
true `MATCH` and not a `SORT`, because its seven right-hand facts repeat nothing
and pair one to one. The fifth is `ORDER`, a single row of seven chunks, because
it is one narrative sequence scored a point per position rather than seven
separate judgements. Nothing on the page is a true/false or a many-to-few task,
so there is no `SORT` here.

Five defects were repaired. **The underwater-doors question, item six, had a key
that was the only long option**, at eighty-eight characters against eighty-five
for its nearest rival and seventy-seven for the shortest, which lets a learner
who knows nothing about doors pick it on shape alone; the buried-treasure
distractor is lengthened &mdash; never the key shortened &mdash; and stays the
same error it was, the belief that a placed block acts as a treasure detector.
**The sand-and-gravel item had two correct answers.** Its stem reads
&ldquo;placing a _____ or any other non-solid block&rdquo;, and redstone dust is
itself a non-solid block, so the stem certified its own distractor; redstone dust
becomes a stone slab, which learners take for a partial and therefore non-solid
block when it is in fact a solid support. **The zombie-villager cure had two
correct answers as well**, because the &ldquo;Notch Apple&rdquo; &mdash; the
enchanted golden apple &mdash; cures a Zombie Villager exactly as an ordinary
golden apple does; it becomes a Bottle of Honey, a real item that really does
clear one status effect, poison, and so is the mistake a learner actually makes.
**The Blaze gap accepted ungrammatical answers**: the sentence is
&ldquo;______ are the only source of Blaze Rods&rdquo; and the page marked
&ldquo;a blaze&rdquo; and &ldquo;blaze&rdquo; correct against a plural verb, so
only plural forms are accepted now. **The cat-taming gap accepted
&ldquo;raw cod&rdquo; and &ldquo;raw fish&rdquo;** although its stem already ends
in &ldquo;raw&rdquo;, which scores &ldquo;feed it raw raw cod&rdquo; as right,
and it accepted the bare &ldquo;fish&rdquo;, which its own explanation
contradicts by naming salmon as the other raw fish; the answer is now the cod
itself, spelled either way.

Three faults are recorded and left alone. The matching activity is largely a
memory test of activity one rather than of Minecraft: its Creeper, Gold Pickaxe
and Charged Creeper facts restate the keys of questions three, one and five
almost word for word, so a learner who read the earlier feedback can pair them
without knowing anything. The explanation for the cats question is garbled
&mdash; it says Creepers avoid cats &ldquo;because of the real-world hatred
between cats and cats&rsquo; natural predators&rdquo;, which is circular and
names no reason at all. And the explanation for the sand item describes a
mechanic that does not exist, inventing a &ldquo;floor check&rdquo; that a torch
supposedly satisfies; the item itself is sound, the prose under it is not.

The ordering activity fed seven whole sentences, sixty to a hundred and eight
characters each, into its chunk pool. Seven of those will not fit the stage
without shrinking the type, so the chunks below are short labels and the
sentences move into the explanation, as the sibling Minecraft deck did.

The English being taught is never translated: stems, options and chunks stay in
English in every language build, per house style.
"""

# ── Activities 1 and 3: the trivia questions ───────────────────────────
# ORIGINAL key positions, in the page's DOM order: activity one sat at
# [2, 2, 1, 2, 1, 1] — C, C, B, C, B, B, never once A or D — and activity
# three keyed its drag pools at [0, 0, 0, 0, 0, 0], the right chip first
# in every array. Respread over all four indices:
MC_POS = [1, 3, 0, 2, 0, 3, 2, 1, 3, 0, 2, 1]

# (stem, [options with the KEY FIRST], why-key)
_MC_RAW = [
    ("Which pickaxe has the <strong>fastest mining speed</strong> in "
     "Minecraft, even though most players never use it for that?",
     ["The Gold Pickaxe, despite having the lowest durability of all.",
      "The Diamond Pickaxe, due to its superior material quality.",
      "The Netherite Pickaxe, because it upgrades all diamond stats.",
      "The Iron Pickaxe, as a balanced all-round tool for mining."],
     "q1why"),

    ("What happens if you try to <strong>sleep in a bed</strong> while in "
     "the Nether or the End?",
     ["The bed explodes violently, dealing significant damage to you and "
      "nearby blocks.",
      "You skip to the next in-game morning as normal, saving your spawn "
      "point.",
      "Nothing happens &mdash; beds cannot be placed in those dimensions at "
      "all.",
      "You are immediately teleported back to your original spawn point in "
      "the Overworld."],
     "q2why"),

    ("The Creeper was <strong>originally created</strong> as a result of "
     "which mistake by Minecraft&rsquo;s creator?",
     ["A pig model that had its height and width values accidentally swapped "
      "around.",
      "A failed zombie skin that was accidentally given the wrong AI "
      "behaviour code.",
      "An error in the tree-generation code that produced a walking plant mob "
      "instead.",
      "A test version of the skeleton that was given the wrong attack "
      "animation data."],
     "q3why"),

    ("Which of the following mobs are <strong>scared away</strong> by tamed "
     "cats in Minecraft?",
     ["Creepers and Phantoms, who will avoid getting close to a player&rsquo;s "
      "tamed cat.",
      "Zombies and Skeletons, who will not approach a player with a cat "
      "nearby.",
      "Endermen and Husks, who flee from cats in a 10-block radius around "
      "them.",
      "Spiders and Cave Spiders, who detect and run from cats using their web "
      "sense."],
     "q4why"),

    ("What do you get when a <strong>lightning bolt</strong> strikes a "
     "Creeper during a thunderstorm?",
     ["A Charged Creeper, whose explosion radius and damage are roughly "
      "doubled in size.",
      "A Wither Creeper, which generates a harmful wither effect when it "
      "explodes near you.",
      "A Storm Creeper, which splits into two smaller creepers when it "
      "finally explodes near you.",
      "An Electric Creeper, which can be ridden by the player using a saddle "
      "after the strike."],
     "q5why"),

    ("Why would an experienced player <strong>carry doors</strong> in their "
     "inventory while exploring underwater?",
     ["Placing a door underwater creates an air pocket that lets the player "
      "breathe temporarily.",
      "Doors can be placed to create a temporary crafting station anywhere "
      "while underwater.",
      "Doors deal double damage to Drowned and Guardians when used as a melee "
      "weapon.",
      "A door placed on the ocean floor reveals the location of any hidden "
      "buried treasure chests nearby."],
     "q6why"),

    ("You can ride a saddled pig in Minecraft, but to control its direction "
     "you must hold a _____ &mdash; otherwise it wanders wherever it chooses.",
     ["carrot on a stick",
      "golden carrot rod",
      "lead with a carrot",
      "fishing rod bait"],
     "q7why"),

    ("A lightning bolt striking a pig transforms it into a _____, which will "
     "then be hostile if attacked but otherwise ignores the player.",
     ["zombie piglin",
      "charged pig mob",
      "nether pig form",
      "undead pig zombie"],
     "q8why"),

    ("Milk, obtained by right-clicking a cow with a bucket, removes all "
     "active _____ from the player &mdash; including both positive and "
     "negative ones.",
     ["status effects",
      "health and hunger",
      "potion buff timers",
      "inventory item slots"],
     "q9why"),

    ("The rarest naturally generated biome in Minecraft is the _____, which "
     "can only appear in very specific conditions where a jungle borders a "
     "swamp hills biome.",
     ["Modified Jungle Edge",
      "Mushroom Field Shore",
      "Eroded Badlands Plateau",
      "Deep Frozen Ocean"],
     "q10why"),

    ("Curing a Zombie Villager requires hitting it with a Splash Potion of "
     "Weakness and then feeding it a _____, after which it slowly reverts "
     "back into a normal villager.",
     ["Golden Apple",
      "Bottle of Honey",
      "Enchanted Glistering Melon",
      "Regular Golden Carrot"],
     "q11why"),

    ("Sand and gravel are gravity-affected blocks, but placing a _____ or any "
     "other non-solid block directly beneath them will prevent them from "
     "falling.",
     ["torch",
      "wooden plank",
      "glass block",
      "stone slab"],
     "q12why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: complete the Minecraft facts ───────────────────────────
# Typed, no bank at all. The page printed a written hint above each bare
# input; it is carried into the stem as a dim parenthetical, because a
# Y-coordinate and a piston push limit are not recoverable from the frame.
FIB = [
    ('After the 1.18 update, the optimal level to mine for diamonds changed '
     'from Y=11 to Y=______, because the update significantly deepened the '
     'underground world. '
     '<span class="dim">(a negative whole number &mdash; the new peak '
     'diamond level)</span>',
     ['-58|minus 58|negative 58|&minus;58'], 'g1why'),

    ('A standard piston can push up to ______ blocks in one activation '
     '&mdash; if you add a 13th block, it won&rsquo;t move at all. '
     '<span class="dim">(a number &mdash; the maximum a piston will '
     'shift)</span>',
     ['12|twelve'], 'g2why'),

    ('Players throw an ______ into the air to find the nearest stronghold, '
     'which contains the End Portal. '
     '<span class="dim">(a three-word item name, crafted from Blaze Powder '
     'and an Ender Pearl)</span>',
     ['Eye of Ender|eye of ender|Ender Eye|Eye of the Ender'], 'g3why'),

    ('______ are the only source of Blaze Rods, which are an essential '
     'ingredient for crafting Eyes of Ender. '
     '<span class="dim">(a plural mob name &mdash; found only inside Nether '
     'Fortresses)</span>',
     ['Blazes|blazes|Blaze mobs|blaze mobs'], 'g4why'),

    ('You need exactly ______ bookshelves surrounding your enchanting table '
     'to unlock level 30 enchantments, which is the maximum. '
     '<span class="dim">(a number &mdash; how many bookshelves reach the top '
     'level)</span>',
     ['15|fifteen'], 'g5why'),

    ('To tame a stray cat in Minecraft, you must slowly approach it and feed '
     'it raw ______ or raw salmon. '
     '<span class="dim">(a common fish &mdash; the other one cats will '
     'accept)</span>',
     ['cod|codfish'], 'g6why'),
]

FIB_BANK = None


# ── Activity 4: match the Minecraft facts ──────────────────────────────
# A real MATCH and not a SORT: seven terms, seven facts, no right-hand
# value repeated, so every pairing is one to one.
# The seven facts ran 79 to 89 characters and the slide overflowed by 48px.
# Trimmed to the defining clause. Every one keeps its frame — a passive or a
# change verb, then "by" plus an -ing form, then the condition — because that
# frame is what the slide is teaching, and the trailing detail was not.
MATCH = [
    ('Creeper',
     'Was created by accident: a pig model with its values swapped'),
    ('Gold Pickaxe',
     'Mines faster than any other, despite the lowest durability'),
    ('Sponge',
     'Can only be obtained by defeating an Elder Guardian'),
    ('Phantom',
     'Only begins spawning after three nights without sleep'),
    ('Notch Apple',
     'Was removed from crafting and is now found only in loot chests'),
    ('Turtle Helmet',
     'Provides Water Breathing for 10 seconds when worn'),
    ('Charged Creeper',
     'Created when lightning strikes one, doubling its blast radius'),
]



# ── Activity 5: put the steps in order ─────────────────────────────────
# One sequence, seven chunks, no pipes and nothing over forty-five
# characters; the page's own sentences ran to a hundred and eight and are
# recorded in the explanation instead.
ORDER = [
    (['Gather wood, stone and food',
      'Mine iron, then diamonds',
      'Build a Nether Portal',
      'Kill Blazes for Blaze Rods',
      'Craft Eyes of Ender',
      'Find the stronghold portal',
      'Defeat the Ender Dragon'], 'o1why'),
]


# ORIGINAL EXPLANATIONS —
# q1: Gold has the highest mining speed of any pickaxe material — faster even than netherite — but it can only mine up to iron-tier blocks and has very low durability. Most players overlook it because they assume higher-tier materials are always better in every way.
# q2: Beds explode in the Nether and the End because those dimensions have no concept of a day/night cycle. This explosive property is so powerful that experienced speedrunners deliberately use beds as weapons against the Ender Dragon — dealing massive damage with each explosion.
# q3: Notch (Markus Persson) has confirmed that the Creeper was created when he accidentally flipped the height and width values of a pig model — making it stand upright and tall instead of being low and wide. The resulting creature was so unsettling that he kept it in the game and gave it an explosive attack.
# q4: Cats repel Creepers and Phantoms — Creepers because of the real-world hatred between cats and cats' natural predators, and Phantoms because they are supposedly frightened of cats. This makes tamed cats genuinely useful in survival mode, not just decorative companions.
# q5: A lightning strike transforms a Creeper into a Charged Creeper — identifiable by a blue electrical aura. Its explosion is approximately twice as powerful as a normal Creeper. This also makes it unique: a mob killed by a Charged Creeper explosion drops its head as a collectible item.
# q6: In Minecraft, placing a door in a water column creates an air pocket immediately in front of it, allowing players to refill their breath bar without surfacing. This was a well-known survival trick before dedicated underwater breathing tools like the Turtle Helmet and Conduit were added to the game.
# q7: A carrot on a stick is crafted from a fishing rod and a carrot. It attracts the pig and lets you steer it. Each use slowly degrades the item. The same item can also be used to attract pigs without riding them, since they follow the carrot.
# q8: When lightning strikes a pig, it transforms into a Zombie Piglin. Zombie Piglins are neutral in the Overworld — they won't attack unless provoked. If you attack one, however, all nearby Zombie Piglins will become hostile simultaneously, which can be very dangerous.
# q9: Drinking milk is the quickest way to cure negative effects like Poison or Wither — but it also removes beneficial ones like Strength or Speed. This double-edged nature requires careful timing, particularly during boss fights or when you've just taken a strength potion before battle.
# q10: The Modified Jungle Edge biome is so rare that many players who have explored millions of blocks have never seen one. It requires an exact biome adjacency — jungle next to swamp hills — which almost never happens in world generation. Even Mushroom Islands, which feel rare, are more common.
# q11: The curing process takes 2–5 minutes, during which the Zombie Villager shakes and makes conversion sounds. Once cured, it returns as a regular villager — and importantly, it gives heavily discounted trades as a thank-you. Curing multiple villagers is one of the best ways to get cheap items.
# q12: When a gravity block like sand or gravel has a non-solid block (air-space item) beneath it, the game checks for a solid surface and finds none — but the presence of a non-solid placed block like a torch acts as a 'floor' check. This is used to hold sand in place while building or to create interesting structural tricks.
# g1: The 1.18 'Caves and Cliffs' update extended the world depth downwards, making Y=-58 the new peak diamond level. Diamond ore becomes more frequent the deeper you go — right up to the bedrock layer. Many veteran players still instinctively dig to Y=11 from old habit.
# g2: The piston push limit of 12 is a fundamental constraint in Redstone engineering. Any contraption involving moving columns, flying machines, or extending bridges must stay within this limit. If the chain of pushable blocks exceeds 12, the piston simply does nothing.
# g3: Eyes of Ender float towards the nearest stronghold when thrown, then either fall to the ground (to be picked up again) or occasionally shatter. You need 12 of them to fill all End Portal frames and open the portal. Finding a stronghold without them is theoretically possible but extremely slow.
# g4: Blazes are hostile flying mobs that spawn in Nether Fortresses. They shoot fireballs and are immune to fire damage. Each killed Blaze drops 0–1 Blaze Rods, which are used to make Blaze Powder — a key ingredient in both Eyes of Ender and brewing potions.
# g5: Bookshelves must be placed one block away from the enchanting table, with nothing blocking the line between them. Each bookshelf increases the maximum enchantment level available. At 15 bookshelves, you unlock the highest possible enchantments, such as Efficiency V or Protection IV.
# g6: Cats are found near villages and witch huts. Because they are skittish, you must crouch and move slowly towards them while holding raw fish. Feeding them raw cod or raw salmon tames them over time. Tamed cats bring gifts each morning and scare away both Creepers and Phantoms.
# m1: (none)
# m2: (none)
# m3: (none)
# m4: (none)
# m5: (none)
# m6: (none)
# m7: (none)
# o1: The complete path: survive → mine resources → enter the Nether → collect Blaze Rods → craft Eyes of Ender → find the stronghold → defeat the Ender Dragon.
# o1 chunks, as the page wrote them before they were shortened to labels:
# o1 step 1: Collect wood, stone, and food to survive the first night and create basic tools.
# o1 step 2: Mine underground to gather iron and eventually diamonds for better armour and tools.
# o1 step 3: Build a Nether Portal out of obsidian and travel to the Nether dimension.
# o1 step 4: Find a Nether Fortress and kill Blazes to collect the Blaze Rods they drop.
# o1 step 5: Kill Endermen to collect Ender Pearls, then combine them with Blaze Powder to craft Eyes of Ender.
# o1 step 6: Throw Eyes of Ender to locate a stronghold underground, then fill all 12 End Portal frames to open the portal.
# o1 step 7: Enter the End, destroy the healing crystals on the obsidian pillars, and defeat the Ender Dragon.

# WHAT THIS LESSON TEACHES —
# The content is Minecraft trivia, but the language load is real and consistent,
# and it is what the three slides should teach.
#
# 1. Lexis. A game-and-systems word field the learner must hold across all five
# activities: mob, spawn and respawn, biome, stronghold, portal, dimension, the
# Overworld and the Nether and the End, ore and vein, durability, mining speed,
# explosion radius, status effect, gravity-affected block, loot chest,
# enchantment and enchanting table, brewing, taming and breeding, saddle, splash
# potion, conduit. Two morphology points sit inside it: the re- prefix (respawn,
# revert back) and compound premodifiers written as one noun chunk — iron-tier
# blocks, gravity-affected blocks, a 10-block radius, a day/night cycle, a
# well-known survival trick. Numbers and measurements carry meaning throughout,
# so the typed activity drills reading and writing them exactly: a negative
# Y-coordinate, "up to 12 blocks", "exactly 15 bookshelves", "three or more
# nights", "for 10 seconds", "0–1 rods", "2–5 minutes".
#
# 2. Grammar. Change-of-state and result verbs are the spine: transform X into Y,
# turn into, become, be created when, revert back into, be identifiable by. They
# appear as often in the passive as the active — was created, can only be
# obtained, was removed, is transformed, when worn by the player — so the passive
# for facts and rules is teachable straight off the page, including the reduced
# relative ("a mob killed by a Charged Creeper explosion"). Rules of the game are
# stated as zero and first conditionals side by side: "if you add a 13th block,
# it won't move", "if you attack one, all nearby piglins will become hostile",
# "if you fall into lava, you will take damage", against the timeless "beds
# explode in the Nether because those dimensions have no day/night cycle".
# Relative clauses do the discriminating work in the multiple choice, where four
# options differ only in the clause hung off the noun, and all three pronouns are
# in play — who for mobs treated as animate, which for items and events, whose
# for the possessed property ("whose explosion radius is doubled"). Concession
# and contrast run underneath the trivia and are worth an explicit slide: despite
# + -ing, even though, although, but, "faster even than netherite". Gerunds after
# prepositions and after certain verbs recur — despite having, avoid getting
# close, without surfacing, begins spawning, requires hitting — as do purpose
# infinitives ("throw an Eye of Ender to find the nearest stronghold") and modals
# of ability, permission and necessity (can only mine, must slowly approach, you
# need to eat, you should carry).
#
# 3. Skills. The multiple choice trains a single reading sub-skill: four long,
# grammatically identical options that differ by one proposition, so the learner
# must scan for the distinguishing clause rather than recognise a keyword. The
# matching activity models definition English and is worth mining for the frames
# themselves — "Was created by accident, a pig model with its values swapped",
# "Can only be obtained by defeating an Elder Guardian", "Only begins spawning
# once the player has…", "Provides X when worn by the player" — which are the
# patterns a learner needs to define any term in their own field. The typed gaps
# test productive spelling and exact form under a hint that names the word class,
# so they double as a dictionary-skills exercise. The ordering activity is
# process description and sequencing: seven steps in a chain where each depends
# on the last, the natural home for first, then, after that, once you have, and
# finally, and the obvious speaking follow-on is to have the learner narrate the
# whole road to the Ender Dragon from the seven labels alone.
