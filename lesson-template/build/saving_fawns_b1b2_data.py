# -*- coding: utf-8 -*-
"""Saving Fawns from the Mower (B1-B2) — the 28 scored MC items + 12 sort pairs.

Sibling of `saving_fawns_b1_data.py` — same rescue-network topic, a
different article and a harder register (B2 vocabulary: deterrent device,
casualty, camouflage). Shares the Animal Welfare art set but is a distinct
question bank, not a re-skin.

Every one of the 28 keys was authored at index 0 on the source scrolling
page, same defect as the B1 sibling before its fix — corrected here before
the rebuild rather than carried over.
"""

READING = [
    dict(stem="Why does a fawn's freezing instinct fail against farm machinery?",
         options=["Because fawns are physically too weak in the first days of their life to move "
                  "away at all.",
                  "Because farmers deliberately walk every single field looking carefully for "
                  "hidden fawns before they ever start cutting it.",
                  "Because fawns can hear the approaching machine coming but simply choose to "
                  "ignore the noise.",
                  "Because staying still, which hides it from predators, doesn't help it avoid a "
                  "machine that simply cuts through the grass."],
         correct=3, why='r1why', stem_key='r1stem'),
    dict(stem="According to the text, when do drone teams usually fly over the fields, and why?",
         options=["At night, because the article describes fawns as being most active after dark.",
                  "Any time of day at all, because the article specifically says that the exact "
                  "timing genuinely doesn't really matter much.",
                  "Midday, because the article says bright sunlight helps the thermal cameras "
                  "work best.",
                  "Early morning, because the temperature difference between a fawn's body and "
                  "the cool ground is easiest to detect then."],
         correct=3, why='r2why', stem_key='r2stem'),
    dict(stem="What happens to a fawn once a drone pilot finds it?",
         options=["It's taken away to a wildlife rescue centre and cared for there for several "
                  "long weeks.",
                  "It's moved by the ground team to a completely different field, quite far away "
                  "from where it was originally found.",
                  "It's simply left exactly in place, and the farmer mows very carefully all "
                  "the way around it.",
                  "It's temporarily covered or fenced off nearby until mowing is finished, then "
                  "released close to where it was found."],
         correct=3, why='r3why', stem_key='r3stem'),
    dict(stem="Why do rescue teams avoid touching fawns with bare hands?",
         options=["Because fawns are known to become aggressive and bite when they feel frightened.",
                  "Because local hunting law strictly forbids touching any wild animal by hand.",
                  "Because gloves are said to help keep the thermal camera's readings accurate.",
                  "Because a doe may reject a fawn that smells of humans after it has been handled."],
         correct=3, why='r4why', stem_key='r4stem'),
    dict(stem="Who is involved in the rescue network described in the article?",
         options=["Only the farmers themselves and a small team of local veterinarians.",
                  "Only government wildlife agencies working with regional park rangers.",
                  "Only the private companies that manufacture and sell the drones.",
                  "Farmers, hunters, drone pilots, and volunteer conservationists."],
         correct=3, why='r5why', stem_key='r5stem'),
    dict(stem="What German term does the article mention for an unnecessary fawn death caused by mowing?",
         options=["Waldsterben", "Tierschutz", "Feldjagd", "Mähtod"],
         correct=3, why='r6why', stem_key='r6stem'),
    dict(stem="What role does the farmer play in the network described?",
         options=["Personally flying the drones over their own fields every morning.",
                  "Paying for all of the network's expensive thermal imaging cameras.",
                  "Releasing the fawns back into the field once mowing is fully complete.",
                  "Announcing mowing dates in advance so a rescue team can be organised."],
         correct=3, why='r7why', stem_key='r7stem'),
    dict(stem="According to the article, how many fawns can a well-organised regional network relocate in a single season?",
         options=["Exactly one hundred.", "Several dozen.", "Several hundred thousand.", "Several thousand."],
         correct=3, why='r8why', stem_key='r8stem'),
]

VOCAB = [
    dict(stem="A newborn ___ has almost no scent, which normally protects it from predators.",
         options=["fawn", "hunter", "doe", "drone"], correct=0, why='v1why'),
    dict(stem="The mother deer, or ___, will search for her baby after it has been moved.",
         options=["volunteer", "farmer", "doe", "fawn"], correct=2, why='v2why'),
    dict(stem="Freezing completely still is a natural ___, not something the animal has to learn.",
         options=["network", "casualty", "camouflage", "instinct"], correct=3, why='v3why'),
    dict(stem="Farmers usually ___ their fields in early summer, once the grass has grown tall enough.",
         options=["donate", "relocate", "spot", "mow"], correct=3, why='v4why'),
    dict(stem="A large ___ can cut through a field far faster than any traditional method.",
         options=["scarecrow", "thermal imaging camera", "deterrent device", "combine harvester"],
         correct=3, why='v5why'),
    dict(stem="A ___ detects body heat instead of light, so a warm animal appears as a bright shape on screen.",
         options=["long-range GPS device", "portable deterrent device", "handheld weather sensor",
                  "thermal imaging camera"],
         correct=3, why='v6why'),
    dict(stem="Many rescue teams now use a ___ to search fields from above before mowing begins.",
         options=["drone", "combine harvester", "scent", "barrier"], correct=0, why='v7why'),
    dict(stem="The person flying it, called the ___, needs training and a steady hand at dawn.",
         options=["conservationist", "drone pilot", "hunter", "farmer"], correct=1, why='v8why'),
    dict(stem="Most people who search fields for fawns are ___ — nobody pays them for their early mornings.",
         options=["inspectors", "contractors", "employees", "volunteers"], correct=3, why='v9why'),
    dict(stem="Once the fawn has been found, the next step is to ___ it safely out of the mower's path.",
         options=["evolve", "donate", "announce", "relocate"], correct=3, why='v10why'),
]

GRAMMAR = [
    dict(stem="Every spring, thousands of fawns ___ hidden in fields across the countryside.",
         options=["have find", "were found", "find", "are found"], correct=3, why='g1why'),
    dict(stem="The fawn ___ with bare hands, to avoid leaving a human scent.",
         options=["is not touched", "does not touch", "was not touch", "has not touched"],
         correct=0, why='g2why'),
    dict(stem="Mowing dates ___ by farmers several days in advance.",
         options=["are announced", "announce", "were announcing", "has announced"],
         correct=0, why='g3why'),
    dict(stem="The thermal cameras ___ by volunteer drone pilots, not bought by the rescue organisation.",
         options=["donate", "have donate", "was donated", "are donated"], correct=3, why='g4why'),
    dict(stem="If a drone pilot ___ a fawn early in the morning, the rescue team ___ time to act "
              "before mowing starts.",
         options=["spot / has", "spotted / would have", "spots / would have", "spots / will have"],
         correct=3, why='g5why'),
    dict(stem="If nobody ___ the field first, many fawns ___ the mowing season.",
         options=["checked / wouldn't survive", "check / don't survive", "checks / don't survive",
                  "checks / won't survive"],
         correct=3, why='g6why'),
    dict(stem="The doe ___ her fawn if it ___ of humans.",
         options=["would reject / smelled", "rejects / will smell", "will reject / smell",
                  "will reject / smells"],
         correct=3, why='g7why'),
    dict(stem="Rescue teams ___ wear gloves when handling a fawn — it's an essential precaution.",
         options=["needn't", "might", "could", "must"], correct=3, why='g8why'),
    dict(stem="Farmers ___ report their mowing dates by law, but responsible farmers do it anyway.",
         options=["are strictly forbidden to", "are not required to", "would be wise not to",
                  "are simply unable to"], correct=1, why='g9why'),
    dict(stem="You ___ approach a resting fawn calmly and quietly — sudden movement can cause it "
              "to bolt into danger.",
         options=["needn't", "must", "can't", "should"], correct=3, why='g10why'),
]

# (word, category key) — category labels + translations live in the builder
SORT_PAIRS = [
    ("farmer", "people"), ("hunter", "people"), ("drone pilot", "people"),
    ("drone", "equipment"), ("thermal imaging camera", "equipment"), ("deterrent device", "equipment"),
    ("fawn", "animals"), ("doe", "animals"), ("hare", "animals"),
    ("mow", "actions"), ("spot", "actions"), ("release", "actions"),
]

CATEGORY_LABEL = {
    'people': 'People & Roles',
    'equipment': 'Equipment',
    'animals': 'Animals',
    'actions': 'Actions & Process',
}
