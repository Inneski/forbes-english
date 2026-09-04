# -*- coding: utf-8 -*-
"""Tense Review — Minecraft Edition (B2) — the thirty scored items.

Lifted from the scrolling `tense-review-minecraft.html`: six multiple choice,
seven gaps in a streamer's live commentary, five grammar claims to judge, six
collocations to match and six sentences to repair. All thirty survive.

Three defects fixed on the way across:

- **Every multiple-choice key was the longest option**, on four of six
  questions, because the answer was always the longest tense name and the
  distractors were the short ones. A learner who never read a stem could take
  four of the six points. Each question gains a fourth option that is longer
  than or equal to the key — and each of those is a real error, not padding:
  `would have been exploring` is the mixed-conditional slip, `has been
  building` the present-for-past slip.
- **The keys sat at A, B or C with C never used twice in a row** — but with
  three options the floor is a third. Four options and a spread across all
  four positions puts it at a quarter.
- **Error correction item 5 had no error in it.** The rubric said every
  sentence contained one, the feedback then said "the sentence is correct as
  written!", and a learner who trusted the rubric lost the point for being
  right. The sentence now carries a genuine Past Perfect Continuous error and
  the rubric is honest again. Judging a correct sentence is a real skill, and
  it is what Activity 3 is for — it should not be smuggled into an exercise
  that promises the opposite.

The twelve-tense chip rail at the top of the original page is gone. It named
the tenses and taught none of them; the three opening slides now do the work
it was standing in for.
"""

# ── Activity 1: multiple choice ────────────────────────────────────────
MC_POS = [0, 2, 1, 3, 2, 0]

_MC_RAW = [
    ('&ldquo;By the time the Ender Dragon respawns, the player _____ the outer '
     'islands for over three in-game days.&rdquo;',
     ['will have been exploring', 'will be exploring', 'has been exploring',
      'would have been exploring'],
     'q1why'),
    ('&ldquo;When the Creeper exploded, she _____ a fully enchanted diamond '
     'sword &mdash; it was completely destroyed.&rdquo;',
     ['had been carrying', 'carried', 'has been carrying',
      'would have been carrying'],
     'q2why'),
    ('&ldquo;Speedrunners _____ the world record dozens of times since the 1.16 '
     'Nether update changed routing strategies.&rdquo;',
     ['have broken', 'were breaking', 'had broken', 'have been breaking'],
     'q3why'),
    ('&ldquo;While he _____ a Nether portal, a Ghast destroyed it with a '
     'fireball from behind.&rdquo;',
     ['was building', 'built', 'had built', 'has been building'],
     'q4why'),
    ('&ldquo;The Warden _____ to vibrations and sniffing &mdash; it '
     'doesn&rsquo;t rely on sight at all.&rdquo;',
     ['responds', 'is responding', 'has responded', 'had responded'],
     'q5why'),
    ('&ldquo;By the time the stream ends tonight, I _____ on this redstone '
     'contraption for nine hours straight.&rdquo;',
     ['will have been working', 'will be working', 'have been working',
      'would have been working'],
     'q6why'),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: the streamer's commentary ──────────────────────────────
# The bracketed tense name and infinitive stay in the stem. They are the
# scaffold the original page carried as a colour-coded legend, and without
# them a seven-gap monologue has seven right answers per gap.
FIB = [
    ('&ldquo;OK chat, so &mdash; as you can see, I ______ for diamonds all '
     'morning and I still haven&rsquo;t found a single vein.&rdquo; '
     '<span class="dim">(present perfect continuous &middot; mine)</span>',
     ["have been mining|'ve been mining|ve been mining"], 'g1why'),
    ('&ldquo;Last night, before I logged off, I ______ the entire skeleton of '
     'the farm.&rdquo; '
     '<span class="dim">(past perfect simple &middot; build)</span>',
     ["had built|had already built|'d built|'d already built"], 'g2why'),
    ('&ldquo;So when I logged back in this morning, the structure ______ '
     'already there.&rdquo; '
     '<span class="dim">(past simple &middot; be)</span>',
     ['was'], 'g3why'),
    ('&ldquo;I actually think this world ______ my longest hardcore run '
     'ever.&rdquo; '
     '<span class="dim">(going to &middot; be)</span>',
     ["is going to be|'s going to be|s going to be"], 'g4why'),
    ('&ldquo;If the next 50 days go well, I ______ on this seed for almost 100 '
     'days by the time I beat the dragon.&rdquo; '
     '<span class="dim">(future perfect continuous &middot; play)</span>',
     ["will have been playing|'ll have been playing|ll have been playing"],
     'g5why'),
    ('&ldquo;While I ______ the Wither, I need someone in chat to track my '
     'health.&rdquo; '
     '<span class="dim">(present continuous &middot; fight)</span>',
     ["am fighting|'m fighting|m fighting"], 'g6why'),
    ('&ldquo;Last time I ______ I was on half a heart until it was nearly too '
     'late.&rdquo; '
     '<span class="dim">(past simple &middot; not realise)</span>',
     ["didn't realise|didnt realise|did not realise|didn't realize"
      "|didnt realize|did not realize"], 'g7why'),
]


# ── Activity 3: is the sentence sound? ─────────────────────────────────
SORT_BINS = ['Correct as written', 'Contains a tense error']

SORT = [
    ('Villagers <em>trade</em> using emeralds as currency.', 0),
    ('She <em>has been crafting</em> a beacon since she found the first '
     'Wither skull.', 0),
    ('By the end of Update Aquatic, Mojang <em>had already introduced</em> '
     'dolphins and shipwrecks.', 0),
    ('He was mining diamonds when a Creeper <em>was exploding</em> next to '
     'him.', 1),
    ('I <em>have visited</em> the End last year and defeated the dragon.', 1),
]


# ── Activity 4: the collocations ───────────────────────────────────────
MATCH = [
    ('to <strong>spawn</strong>', 'to appear in the world at a set location'),
    ('to <strong>grind</strong>',
     'to repeat a task for a long time to gain resources or XP'),
    ('a <strong>biome</strong>',
     'a region with its own terrain, climate and mobs'),
    ('to <strong>aggro</strong> a mob',
     'to make a passive or neutral mob turn hostile'),
    ('a <strong>redstone contraption</strong>',
     'a circuit-driven device that automates an action'),
    ('to <strong>speedrun</strong>',
     'to finish a game as fast as possible on an optimised route'),
]


# ── Activity 5: repair the sentence ────────────────────────────────────
# Each row shows the wrong form and asks for the right one. The original
# underlined the error in red and asked for "only the correct verb form",
# which is what these do.
EC = [
    ('&ldquo;Endermen <strong>are becoming</strong> hostile only when a player '
     'makes direct eye contact with them.&rdquo;<br>'
     'Replace <em>are becoming</em> with ______',
     ['become'], 'e1why'),
    ('&ldquo;By the time Notch <strong>has released</strong> the full game in '
     '2011, the beta had already attracted millions of players.&rdquo;<br>'
     'Replace <em>has released</em> with ______',
     ['released'], 'e2why'),
    ('&ldquo;At the time of writing, Minecraft <strong>sold</strong> over 300 '
     'million copies across all platforms.&rdquo;<br>'
     'Replace <em>sold</em> with ______',
     ['has sold'], 'e3why'),
    ('&ldquo;When the player <strong>will enter</strong> the Deep Dark, the '
     'Warden begins to detect nearby vibrations.&rdquo;<br>'
     'Replace <em>will enter</em> with ______',
     ['enters'], 'e4why'),
    ('&ldquo;The developers <strong>work</strong> on the Caves &amp; Cliffs '
     'update for over a year when they announced a split release.&rdquo;<br>'
     'Replace <em>work</em> with ______',
     ['had been working|had worked'], 'e5why'),
    ('&ldquo;While the Wither <strong>has destroyed</strong> the surrounding '
     'blocks, the player managed to place a bed and skip the night.&rdquo;<br>'
     'Replace <em>has destroyed</em> with ______',
     ['was destroying'], 'e6why'),
]
