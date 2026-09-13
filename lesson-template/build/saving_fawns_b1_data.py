# -*- coding: utf-8 -*-
"""Saving Fawns from the Mower (B1) — the 28 scored MC items + 12 sort pairs.

Lifted from the pre-deck scrolling page (`saving-fawns-mower-b1.html`),
which had already been through two rounds of fixes this session before the
rebuild:

1. **Every one of the 28 keys was authored at index 0.** Fixed once by
   shuffling position only, which did not fix the real defect (below), then
   properly by rewriting the short distractors so the correct option is no
   longer a length tell. Both fixes are carried over verbatim — nothing
   further to do here.
2. **Reading comprehension questions have no blank**, so per `deck.mc`'s
   stem_key convention they translate whole (the original page's `deQ` did
   this too, just with hand-rolled i18n). Vocabulary-in-context and Grammar
   Focus sentences keep a blank and stay English per house style §8 — the
   original's `deQ` on those was translating the test sentence itself, which
   is not carried over.

Word Sorting has no dedicated slide type in the deck engine (only
cover/teach/mc/gap/match/order/discuss/results/activate). Reframed as a
`match` slide: term = the English word, definition = its category name. Only
the category name is glossed per-language (deck.match's own rule) — the
words being sorted are what the activity tests, so they never translate.
"""

READING = [
    dict(stem="Why does staying still not help a fawn near a mowing machine?",
         options=["Fawns are simply too weak in the very first days of their life to stand up and run away quickly.",
                  "Fawns can hear the sound of the machine clearly but usually choose to ignore the noise completely.",
                  "Farmers always walk carefully across the whole field looking for fawns before they start the machine.",
                  "Staying still hides a fawn from animals like foxes, but a machine cannot see it at all — moving or not."],
         correct=3, why='r1why', stem_key='r1stem'),
    dict(stem="Why do drone teams fly early in the morning?",
         options=["Because fawns are usually only awake and moving in the early morning hours.",
                  "Because farmers in this region always choose to cut their fields in the morning.",
                  "Because the ground is cool then, so the camera can easily see a fawn's warm body.",
                  "Because it is generally much easier and safer to fly a small drone in the dark."],
         correct=2, why='r2why', stem_key='r2stem'),
    dict(stem="What happens to a fawn after the team finds it?",
         options=["It is taken away to a special animal hospital and cared for there for several long weeks.",
                  "It is left exactly where it was found, and the farmer simply drives carefully around it.",
                  "It is moved by the team to a completely different field, far away from the first one.",
                  "It is covered with a box or branches nearby until the mowing is finished, then let go again."],
         correct=3, why='r3why', stem_key='r3stem'),
    dict(stem="Why do rescue teams wear gloves?",
         options=["Because fawns are known to bite the rescuers' hands when they feel frightened.",
                  "Because wearing gloves outdoors is simply a safety rule set by the local government.",
                  "Because the mother deer might reject her baby if it smells like a human.",
                  "Because the thermal camera only works correctly when the team wears gloves."],
         correct=2, why='r4why', stem_key='r4stem'),
    dict(stem="Who works together in this rescue project, according to the text?",
         options=["Only the local farmers and a small team of animal doctors.",
                  "Only officials who work for the regional government.",
                  "Only the private companies that build and sell the drones.",
                  "Farmers, hunters, drone pilots, and volunteers."],
         correct=3, why='r5why', stem_key='r5stem'),
    dict(stem="What German word does the text use for an accidental fawn death caused by mowing?",
         options=["Waldsterben", "Tierschutz", "Feldjagd", "Mähtod"],
         correct=3, why='r6why', stem_key='r6stem'),
    dict(stem="What do farmers do to help the rescue team, according to the text?",
         options=["They personally pay the full cost of all of the team's drone equipment.",
                  "They fly the drones themselves instead of leaving that job to the volunteers.",
                  "They tell the team when they plan to cut a field, so the team can check it first.",
                  "They are the ones who release the fawns back into the field after mowing ends."],
         correct=2, why='r7why', stem_key='r7stem'),
    dict(stem="According to the text, how many fawns can a region save in one year with good teamwork?",
         options=["About ten.", "Exactly one hundred.", "Many thousands.", "A few hundred thousand."],
         correct=2, why='r8why', stem_key='r8stem'),
]

VOCAB = [
    dict(stem="A baby deer is called a ___.",
         options=["fawn", "hunter", "doe", "drone"], correct=0, why='v1why'),
    dict(stem="The mother deer, or ___, looks for her baby after it has been moved.",
         options=["volunteer", "farmer", "doe", "fawn"], correct=2, why='v2why'),
    dict(stem="Staying completely still is a natural ___, not something learned.",
         options=["group", "network", "camera", "instinct"], correct=3, why='v3why'),
    dict(stem="Farmers usually ___ their fields in early summer.",
         options=["donate", "relocate", "spot", "mow"], correct=3, why='v4why'),
    dict(stem="A big ___ can cut a whole field very fast.",
         options=["scarecrow", "thermal imaging camera", "combine harvester", "glove"],
         correct=2, why='v5why'),
    dict(stem="A ___ can see heat, not normal light.",
         options=["pair of night vision goggles", "long-range GPS tracking device",
                  "portable weather sensor unit", "thermal imaging camera"],
         correct=3, why='v6why'),
    dict(stem="Many teams now use a ___ to search fields from above.",
         options=["drone", "combine harvester", "glove", "smell"], correct=0, why='v7why'),
    dict(stem="The person flying it is called the ___.",
         options=["volunteer", "drone pilot", "hunter", "farmer"], correct=1, why='v8why'),
    dict(stem="Most helpers are ___ — nobody pays them.",
         options=["employees", "students", "police", "volunteers"], correct=3, why='v9why'),
    dict(stem="After they find a fawn, the team will ___ it, close to the same spot.",
         options=["donate", "photograph", "relocate", "announce"], correct=2, why='v10why'),
]

GRAMMAR = [
    dict(stem="Every spring, many fawns ___ in fields.",
         options=["have find", "were found", "find", "are found"], correct=3, why='g1why'),
    dict(stem="The fawn ___ with bare hands, to keep it safe.",
         options=["is not touched", "was not touch", "has not touched", "does not touch"],
         correct=0, why='g2why'),
    dict(stem="Mowing dates ___ by farmers before the work starts.",
         options=["are announced", "has announced", "were announcing", "announce"],
         correct=0, why='g3why'),
    dict(stem="The cameras ___ by volunteer drone pilots, not bought by the organisation.",
         options=["donate", "have donate", "was donated", "are donated"], correct=3, why='g4why'),
    dict(stem="If a pilot ___ a fawn early, the team ___ time to help before mowing starts.",
         options=["spotted / would have", "spots / would have", "spots / will have", "spot / has"],
         correct=2, why='g5why'),
    dict(stem="If nobody ___ the field first, some fawns ___ the mowing.",
         options=["checked / wouldn't survive", "checks / won't survive",
                  "check / don't survive", "checks / don't survive"],
         correct=1, why='g6why'),
    dict(stem="The mother ___ her fawn if it ___ of humans.",
         options=["would reject / smelled", "will reject / smell",
                  "will reject / smells", "rejects / will smell"],
         correct=2, why='g7why'),
    dict(stem="Rescue teams ___ wear gloves — it's an important rule.",
         options=["needn't", "could", "might", "must"], correct=3, why='g8why'),
    dict(stem="Farmers ___ report their mowing dates by law, but many do it anyway.",
         options=["mustn't", "are not able to", "don't have to", "shouldn't"], correct=2, why='g9why'),
    dict(stem="You ___ approach a fawn calmly — sudden movement can scare it.",
         options=["needn't", "must", "should", "can't"], correct=2, why='g10why'),
]

# (word, category key) — category labels + translations live in the builder
SORT_PAIRS = [
    ("farmer", "people"), ("hunter", "people"), ("drone pilot", "people"),
    ("drone", "equipment"), ("thermal imaging camera", "equipment"), ("gloves", "equipment"),
    ("fawn", "animals"), ("doe", "animals"), ("hare", "animals"),
    ("mow", "actions"), ("spot", "actions"), ("release", "actions"),
]

CATEGORY_LABEL = {
    'people': 'People & Roles',
    'equipment': 'Equipment',
    'animals': 'Animals',
    'actions': 'Actions & Process',
}
