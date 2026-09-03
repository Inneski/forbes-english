# -*- coding: utf-8 -*-
"""Dino-Craft Part 0: The Briefing (C1) — the scored content.

Lifted from the scrolling page that survived the merge with
`forbes-english-lesson (dinosoausrs c1).html`. All twenty-five scored items
are here. Four defects in the original are not:

1. **Four of the five multiple-choice keys sat at index 1** (1, 1, 1, 1, 3).
   Spread across the four positions below.

2. **The word bank was the answer key.** All five drag-and-drop answers came
   first, in slot order, followed by three decoys — so the bank could be read
   straight down without understanding a single discourse marker. It is
   alphabetised here, which `assert_bank_is_not_a_key` now enforces.

3. **One explanation named the option by letter** ("Option B is correct"),
   which is meaningless once the engine shuffles. It names the structure
   instead.

4. **Three of the five activities carried a single shared explanation** for
   the whole activity — one paragraph covering five drag-and-drop slots, one
   covering five matched pairs, one covering five reordered sentences. Every
   item now has its own, per house style §7.
"""

# ── Activity 1: multiple choice ────────────────────────────────────────
# key position per item: was 1,1,1,1,3 — no run of three, all four used
MC_POS = [2, 0, 3, 1, 0]

_MC_RAW = [
    ("A palaeontologist in a Minecraft museum exhibit says: <em>&ldquo;The "
     "Tyrannosaurus rex _______ an apex predator, capable of exerting bite forces "
     "that no other Cretaceous theropod could rival.&rdquo;</em> Which verb form "
     "indicates a general past truth?",
     ["was considered", "had been constituting", "has been constituting",
      "would have constituted"],
     "<strong>Was considered</strong> — the simple past passive is what English uses "
     "to state an accepted past fact or a scientific consensus. <em>Had been "
     "constituting</em> implies a continuous earlier state, <em>would have "
     "constituted</em> is hypothetical, and the present perfect continuous cannot "
     "describe a completed historical reality."),

    ("In a Minecraft server&rsquo;s in-game lore book, a player reads: <em>&ldquo;Had "
     "the Chicxulub asteroid not struck Earth, the dinosaurs _______ into countless "
     "new species.&rdquo;</em> Which form is grammatically correct?",
     ["might still have evolved", "might still evolve", "will have still evolved",
      "may still be evolving"],
     "<strong>Might still have evolved</strong> — an unreal past condition takes an "
     "unreal past result. <em>Might + have + past participle</em> is what carries "
     "counterfactual speculation about something that did not happen."),

    ("A Minecraft YouTuber narrates: <em>&ldquo;The Brachiosaurus&rsquo;s long neck is "
     "thought to be an evolutionary _______, allowing it to reach foliage that "
     "shorter-necked herbivores simply couldn&rsquo;t.&rdquo;</em> Which word fits at "
     "C1?",
     ["adaptation", "particularity", "modification", "characteristic"],
     "<strong>Adaptation</strong> is the precise term: in evolutionary biology it "
     "names a trait that evolved <em>because</em> it conferred an advantage. "
     "<em>Modification</em> and <em>characteristic</em> are plausible English and "
     "carry none of that specificity."),

    ("Which sentence uses a <strong>participle clause</strong> correctly to describe a "
     "player&rsquo;s action in a dinosaur-themed Minecraft map?",
     ["Having mined the amber block, the player discovered a velociraptor inside it.",
      "Having mined the amber block, the velociraptor was discovered inside it.",
      "After the player mined the amber block, a velociraptor was inside having been "
      "discovered.",
      "Once having mined the amber block, the velociraptor had been discovered by the "
      "player."],
     "A participle clause must share its subject with the main clause, so whoever did "
     "the mining has to be the subject of what follows &mdash; <strong>the player</strong>. "
     "Put the velociraptor there and the sentence says the velociraptor mined the "
     "block. That is a dangling participle, and it is the commonest way this structure "
     "goes wrong."),

    ("<em>&ldquo;The sheer _______ of the Argentinosaurus &mdash; estimated at over 70 "
     "tonnes &mdash; made it virtually impervious to attack.&rdquo;</em> Which word "
     "best fits?",
     ["magnitude", "dimension", "enormity", "proportions"],
     "<strong>Magnitude</strong> carries abstract scale, which is the register this "
     "sentence is in. <em>Enormity</em> in careful usage means moral gravity; "
     "<em>dimension</em> and <em>proportions</em> are more literal and land less "
     "heavily."),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: fill in the blank ──────────────────────────────────────
# (sentence, [accepted answers], why)
FIB = [
    ("The Minecraft biome guide explains: <em>&ldquo;Dinosaurs are widely believed to "
     "have been warm-blooded creatures, a theory that has gained considerable "
     "_______ in the palaeontological community.&rdquo;</em>",
     ["traction"],
     "<strong>Gain traction</strong> is a fixed collocation meaning to become more "
     "widely accepted. It belongs to academic and professional register, which is "
     "where this sentence sits."),

    ("A Minecraft server admin writes in the rules: <em>&ldquo;Any player found to be "
     "deliberately _______ the habitats of the dino NPCs will face an immediate "
     "ban.&rdquo;</em>",
     ["disrupting|destroying"],
     "<strong>Disrupting</strong> is the standard ecological collocation &mdash; it "
     "means interfering with a system that is working. <em>Destroying</em> is "
     "accepted here, but it says something stronger and less precise."),

    ("<em>&ldquo;The Pteranodon, often _______ referred to as a dinosaur, was in fact a "
     "flying reptile of the order Pterosauria &mdash; technically distinct from the "
     "dinosaur clade.&rdquo;</em>",
     ["erroneously|incorrectly|mistakenly"],
     "The adverb modifies <em>referred to</em> and marks the naming as inaccurate. "
     "<strong>Erroneously</strong> is the most formal of the three and the best fit "
     "for this register; <em>incorrectly</em> and <em>mistakenly</em> are also right."),

    ("In a Minecraft crafting guide: <em>&ldquo;Once you have _______ the dinosaur "
     "bones into powder, combine them with redstone dust to craft the revival "
     "serum.&rdquo;</em>",
     ["ground|crushed|processed"],
     "<strong>Ground</strong> is the past participle of <em>grind</em>, and "
     "<em>grind something into powder</em> is the idiom. <em>Crushed</em> is "
     "accepted, though grinding is specifically reduction by friction &mdash; which "
     "is what powder implies."),

    ("<em>&ldquo;The discovery of feathered dinosaur fossils in China in the 1990s "
     "fundamentally _______ our understanding of the link between birds and theropod "
     "dinosaurs.&rdquo;</em>",
     ["transformed|reshaped|revolutionised|revolutionized|altered|changed"],
     "<strong>Transformed</strong>, <em>reshaped</em> and <em>revolutionised</em> all "
     "carry the scale of a paradigm shift. <em>Altered</em> and <em>changed</em> are "
     "accepted but weaker &mdash; they would fit a small correction just as well."),
]


# ── Activity 3: the word bank (was drag & drop) ────────────────────────
DND = [
    ("The Minecraft modder claimed that dinosaurs, _______, would have been far more "
     "colourful than early palaeontologists had imagined.",
     ["contrary to popular belief"],
     "<strong>Contrary to popular belief</strong> introduces a correction to something "
     "widely assumed. It needs the assumption to exist first &mdash; which is why it "
     "opens so many science-writing sentences."),

    ("The velociraptor, _______ a turkey-sized predator, has been greatly exaggerated "
     "in size by Hollywood blockbusters.",
     ["in actual fact"],
     "<strong>In actual fact</strong> signals that what follows corrects the record. "
     "It is stronger than a bare <em>actually</em> and belongs in written register."),

    ("Crafting a saddle for the Stegosaurus proved _______ more complex than any recipe "
     "the player had previously attempted.",
     ["considerably"],
     "<strong>Considerably</strong> is one of the few adverbs that can intensify a "
     "comparative (<em>considerably more complex</em>). <em>Very</em> cannot do this "
     "job."),

    ("The ancient ruins biome was, _______, the only place where fossilised dinosaur "
     "eggs could spawn in the modpack.",
     ["by and large"],
     "<strong>By and large</strong> means generally, with exceptions allowed. It hedges "
     "the claim, which is why it sits between commas rather than at the front."),

    ("A herd of Triceratops had _______ the valley floor, leaving enormous three-toed "
     "impressions in the pixelated soil.",
     ["traversed"],
     "<strong>Traversed</strong> means crossed from one side to the other. Unlike the "
     "others in the bank it is a verb, so the auxiliary <em>had</em> before the gap "
     "already tells you which kind of word belongs here."),
]

# alphabetised, so the bank is a bank and not a key
BANK = sorted(['contrary to popular belief', 'in actual fact', 'considerably',
               'by and large', 'traversed', 'allegedly', 'regardless', 'presumably'])


# ── Activity 4: matching ───────────────────────────────────────────────
MATCH = [
    ('<em>Palaeontology</em>', 'The scientific study of prehistoric life through fossils'),
    ('<em>Apex predator</em>', 'A hunter at the top of its food chain, with no natural enemies'),
    ('<em>Herbivorous</em>', 'Feeding exclusively on plant matter'),
    ('<em>Cretaceous period</em>', 'The era from roughly 145 to 66 million years ago'),
    ('<em>Bipedal locomotion</em>', 'Movement using only two limbs to walk or run'),
]


# ── Activity 5: sentence building ──────────────────────────────────────
# (chunks, why)
ORDER = [
    (['It was not until', 'the discovery of the Archaeopteryx',
      'that scientists began to accept',
      'the evolutionary continuum between dinosaurs and modern birds.'],
     "<strong>It was not until X that Y</strong> is a cleft: the delay goes in the "
     "middle and the main clause is held to the end. Splitting <em>not until</em> from "
     "<em>that</em> breaks the frame."),

    (['The Minecraft modpack,', 'which had taken three years to develop,',
      'introduced a fully simulated Jurassic ecosystem',
      'complete with authentic predator-prey dynamics.'],
     "The non-defining relative clause sits inside its commas, directly after the noun "
     "it describes. Move it and it starts describing the ecosystem instead of the "
     "modpack."),

    (['Despite their fearsome reputation,', 'many large theropods are now believed',
      'to have subsisted primarily on carrion', 'rather than actively hunting live prey.'],
     "<em>Despite</em> sets up the contrast and has to come first. <strong>Believed to "
     "have + past participle</strong> is the reporting structure for a present belief "
     "about the past."),

    (['Having spawned in the Cretaceous biome,', 'the player quickly realised',
      'that conventional iron armour offered little protection',
      'against a charging Triceratops.'],
     "The participle clause comes first and its subject must be the subject of the main "
     "clause &mdash; <em>the player</em> spawned, and the player realised. This is the "
     "same rule the participle question tested."),

    (['The remarkable preservation of soft tissue', 'in amber-encased specimens',
      'has provided palaeontologists with unprecedented insight',
      'into the physiology of extinct species.'],
     "A long noun phrase carries the subject, and the verb cannot arrive until it is "
     "finished. <em>Provide someone with something</em> and <em>insight into</em> are "
     "both fixed."),
]
