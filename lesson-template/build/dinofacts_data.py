# -*- coding: utf-8 -*-
"""Advanced Dinosaur Facts (C1) — the sixteen scored items.

Lifted from the scrolling `forbes-english-dinosaurs.html`. The palaeontology
is good and none of it changed. Four defects did:

1. **Option A was never the answer.** Keys sat at 1, 2, 1, 3, 2 across five
   questions — a learner who noticed could delete a quarter of every question.
   Spread across all four positions below.

2. **Two keys were the longest option by four characters or more** (Q1 by 5,
   Q4 by 4), which is what the ANSWERS gate fails on. Fixed by lengthening
   distractors, never by shortening a key: a shortened key just moves the tell.

3. **Every one of the five word banks listed the answer first.** Not "in gap
   order" — literally first, five times out of five. Alphabetised here.

4. **The reordering activity's five items were authored in the answer order**
   with `correctOrder: [0,1,2,3,4]`. The engine shuffles, so the screen was
   fine, but the source and any printed copy read as a key.

The timeline items were also far too long to sit in an `order` pool as
authored — each was a full sentence of forty words. They are labels now, with
the detail moved into the explanation where it belongs.
"""

# ── Activity 1: multiple choice ────────────────────────────────────────
MC_POS = [3, 0, 2, 1, 0]

_MC_RAW = [
    ("Recent palaeontological evidence suggests many theropod dinosaurs possessed "
     "protofeathers or full plumage. Which statement most accurately reflects current "
     "scientific consensus?",
     ["Widespread across coelurosaurs and probably other lineages, serving warmth "
      "and display",
      "Confined to true birds, appearing only after the K-Pg extinction, with no "
      "non-avian evidence",
      "Confirmed only in Archaeopteryx; no other fossil preserves integumentary "
      "structures",
      "Restricted to humid East Asian forests, never spreading to another continent"],
     "q1why"),

    ("The K-Pg extinction event around 66 million years ago wiped out the non-avian "
     "dinosaurs. What proportion of all Earth&rsquo;s species is estimated to have "
     "perished?",
     ["Approximately 75% of all species, affecting both terrestrial and marine "
      "ecosystems globally",
      "Approximately 25% of all species, with deep-ocean ecosystems left largely "
      "unaffected",
      "Approximately 50% of all species, concentrated primarily in equatorial "
      "terrestrial zones",
      "Approximately 95% of all species, the single most severe extinction in Earth&rsquo;s "
      "history"],
     "q2why"),

    ("Research into sauropod physiology suggests which factor most critically enabled "
     "their extraordinary body mass &mdash; in some species over 70 tonnes?",
     ["Hollow, air-filled vertebrae connected to an avian-style respiratory system that "
      "dramatically reduced skeletal mass",
      "Slow, reptilian metabolic rates paired with continuous feeding across sixteen or "
      "more hours daily",
      "A dual-pump circulatory system analogous to modern cetaceans, enabling efficient "
      "oxygen delivery to the extremities",
      "Specialised fermentation chambers extracting far more energy per kilogram of "
      "plant matter than any modern herbivore"],
     "q3why"),

    ("<em>Spinosaurus aegyptiacus</em> has been substantially reinterpreted since the "
     "Moroccan fossil discoveries. Which conclusion do palaeontologists now broadly "
     "accept about its lifestyle?",
     ["It was semi-aquatic, with dense bones for buoyancy control and a diet centred on "
      "large freshwater fish",
      "It was primarily nocturnal, hunting small mammals and lizards along arid "
      "riverbanks after dark",
      "It was a highly social apex predator that hunted in coordinated groups out "
      "across the open floodplains",
      "It inhabited open savannah and competed directly with the large titanosaur "
      "sauropods for feeding territory"],
     "q4why"),

    ("<em>T. rex</em> underwent explosive growth during adolescence. Studies of "
     "fossilised bone growth rings reveal roughly how much mass a juvenile gained per "
     "year at peak?",
     ["Approximately 600&ndash;700 kg per year, the fastest mass accumulation known in "
      "any terrestrial vertebrate",
      "Approximately 100&ndash;150 kg per year, comparable to the growth rate of large "
      "African elephants",
      "Approximately 300&ndash;400 kg per year, the fastest rate known among any "
      "Mesozoic theropod lineage yet described",
      "Approximately 900&ndash;1,000 kg per year, possible only in the oxygen-rich Late "
      "Cretaceous atmosphere"],
     "q5why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: the terminology gaps ───────────────────────────────────
FIB = [
    ("The study of dinosaur footprints, trackways and other trace fossils is called "
     "_______, and it reveals gait, speed and even social behaviour in species that "
     "left no skeleton in that region.",
     ["ichnology"], "f1why"),
    ("Many hadrosaurs had hollow cranial crests that worked as resonating chambers, "
     "producing low-frequency _______ communication, possibly audible across kilometres "
     "of dense Cretaceous vegetation.",
     ["infrasound"], "f2why"),
    ("Rather than the warm-blooded or cold-blooded dichotomy, bone isotope analysis "
     "suggests many dinosaurs were _______ &mdash; generating internal heat, but at "
     "rates between a true ectotherm and a full endotherm.",
     ["mesothermic"], "f3why"),
    ("The earliest unambiguous dinosaur fossils, including <em>Eoraptor</em> and "
     "<em>Herrerasaurus</em>, date to the _______ Age of the Late Triassic, about "
     "231&ndash;237 million years ago.",
     ["Carnian"], "f4why"),
    ("Palaeontologist Mary _______ controversially reported possible soft tissue, "
     "including collagen traces, from a 68-million-year-old <em>T. rex</em> femur.",
     ["Schweitzer"], "f5why"),
]

# alphabetised: the five answers were the first item of their own bank, five times
BANK = sorted(['ichnology', 'osteology', 'palynology', 'taphonomy', 'phylogenetics',
               'infrasound', 'ultrasound', 'echolocation',
               'mesothermic', 'poikilothermic', 'homeothermic', 'ectothermic',
               'Carnian', 'Norian', 'Rhaetian',
               'Schweitzer', 'Currie', 'Bakker'], key=str.lower)


# ── Activity 3: matching ───────────────────────────────────────────────
MATCH = [
    ('<em>Microraptor gui</em>',
     'Four-winged dromaeosaurid, thought to have glided between trees'),
    ('<em>Ankylosaurus</em>',
     'Tail club dense enough to fracture the bones of a large theropod'),
    ('<em>Epidexipteryx hui</em>',
     'Earliest dinosaur known to carry long ribbon-like display feathers'),
    ('<em>Pachycephalosaurus</em>',
     'Dome skull that withstood head-butting forces above 1,000 N'),
    ('<em>Therizinosaurus</em>',
     'Theropod that reversed to herbivory, with claws over a metre long'),
]


# ── Activity 4: the timeline ───────────────────────────────────────────
# labels, not the forty-word sentences the original tried to put in a chunk pool
TIMELINE = ['Eoraptor and Herrerasaurus, ~233 Ma',
            'Jurassic gigantism and Archaeopteryx, ~150 Ma',
            'Chicxulub impact and the K-Pg extinction, ~66 Ma',
            'Buckland describes Megalosaurus; Owen coins Dinosauria, 1824&ndash;1842',
            'Chinese feathered fossils and Schweitzer&rsquo;s soft tissue, 2000s']
