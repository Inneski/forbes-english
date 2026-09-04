# -*- coding: utf-8 -*-
"""Past Modals in Minecraft (B2) — the fifteen scored items.

Lifted from the scrolling `forbes-english-past-modals-minecraft.html`. Five
multiple choice, five gap-fills and five matched pairs, all kept.

One defect: **option A was never the answer.** Keys sat at 1, 2, 3, 2, 2 across
five questions, so a learner who noticed could delete a quarter of every item
unread. Spread across all four positions below. No key was the longest option,
which is unusual for this library and worth noting rather than assuming.

The page also disagreed with itself about level — the header chip said B1, the
`<title>` and the catalogue row both say B2. B2 wins; the modals here
(needn't have, the deduction/possibility split) are not B1 grammar.
"""

# ── Activity 1: multiple choice ────────────────────────────────────────
MC_POS = [3, 0, 2, 1, 0]

_MC_RAW = [
    ("Alex fell into lava and lost all her diamonds. Her friend said: <em>&ldquo;You "
     "_____ put your diamonds in a chest before going mining in the Nether.&rdquo;</em>",
     ["should have put", "must have put", "might have put", "could have put"],
     "m1why"),
    ("Steve found a hidden underground base. He thought: <em>&ldquo;Someone _____ built "
     "this &mdash; there are torches everywhere and the walls are too smooth to be "
     "natural.&rdquo;</em>",
     ["must have built", "needn&rsquo;t have built", "should have built",
      "could have built"],
     "m2why"),
    ("The creeper exploded near Mia&rsquo;s house, but it didn&rsquo;t break the walls. "
     "She said: <em>&ldquo;That explosion _____ destroyed everything &mdash; I was very "
     "lucky.&rdquo;</em>",
     ["could have destroyed", "might have destroyed", "should have destroyed",
      "must have destroyed"],
     "m3why"),
    ("Leo spent three hours collecting wood before realising he was in Creative Mode. "
     "His teammate laughed: <em>&ldquo;You _____ bothered &mdash; you can just spawn "
     "anything!&rdquo;</em>",
     ["needn&rsquo;t have bothered", "might not have bothered",
      "shouldn&rsquo;t have bothered", "mustn&rsquo;t have bothered"],
     "m4why"),
    ("Nobody saw who broke the community bridge overnight. One player suggested: "
     "<em>&ldquo;It _____ been a griefer &mdash; they were online late last "
     "night.&rdquo;</em>",
     ["might have", "could have", "must have", "should have"],
     "m5why"),
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
    ("The Ender Dragon appeared suddenly and destroyed the village. We _______ prepared "
     "better defences before entering The End.",
     ["should have"], "f1why"),
    ("Nobody found the buried treasure chest &mdash; but Alex had the map! She _______ "
     "found it easily if she had followed the coordinates.",
     ["could have"], "f2why"),
    ("Steve walked back from the mine for twenty minutes. He _______ walked &mdash; he "
     "had a horse tied up outside the mine entrance.",
     ["needn't have|neednt have|need not have"], "f3why"),
    ("There are footprints all around the stolen chest. The thief _______ been nearby "
     "just a few minutes ago.",
     ["must have"], "f4why"),
    ("Nobody knows what happened to the lost village. The flood _______ caused the "
     "damage, or perhaps it was an earthquake.",
     ["might have"], "f5why"),
]

# The original showed the same hint under every gap ("should / must / could /
# might / needn't + have"). As a bank it is the five answers and nothing else,
# which is the word-bank-is-a-key defect wearing a different hat, so there is
# no bank here — the forms are taught on the slide before instead.
BANK = None


# ── Activity 3: matching ───────────────────────────────────────────────
MATCH = [
    ('&ldquo;I <strong>must have</strong> left my pickaxe at the village.&rdquo;',
     'A confident deduction from evidence'),
    ('&ldquo;You <strong>should have</strong> built the walls higher.&rdquo;',
     'Criticism of what was not done'),
    ('&ldquo;She <strong>needn&rsquo;t have</strong> crafted all those arrows.&rdquo;',
     'It was done, and it was unnecessary'),
    ('&ldquo;That skeleton <strong>might have</strong> dropped a rare bow.&rdquo;',
     'An uncertain guess about the past'),
    ('&ldquo;You <strong>could have</strong> used the Elytra to cross.&rdquo;',
     'It was possible, and it did not happen'),
]
