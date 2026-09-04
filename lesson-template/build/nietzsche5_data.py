# -*- coding: utf-8 -*-
"""Nietzsche on Film — C1 Vocabulary, Part V — the fifteen scored items.

Lifted from the scrolling `nietzsche-film-vocab-c1-part5.html`. The premise is
a retrospective at the Berlin festival and the learner is the artistic
director; the fifteen multiple-choice items run film-criticism terminology,
professional collocation, register and connotation, industry phrasal verbs and
idioms, and word formation. Every stem and option is kept as written apart from
the two items named below. The page's own explanation text is not in this
module — it belongs in the i18n layer, and `why` here is a key string only. The
free-writing task (the festival blurb) is not a scored item and is not carried.

Three defects, two of them content:

1. **The answer key was a metronome.** From Q5 onward it ran c, b, d, a and
   then repeated, four times without a break — a learner who spotted it after
   two cycles could answer the last six questions without reading them.
   MC_POS below spreads the keys over all four positions with no period.

2. **Q6 was mis-keyed.** The stem's own evidence is "no major studio had taken
   that risk on a period biographical film" — that is the definition of
   *unprecedented*, never-done-before, and it says nothing about the decision
   opening new artistic territory, which is what *groundbreaking* claims. The
   page keyed *groundbreaking* and then argued for it on collocational feel
   against the evidence in its own sentence. Re-keyed to *unprecedented*;
   *groundbreaking* stays as a distractor, where it is a good one.

3. **Q15 was broken twice over.** It sat in the word-formation section but its
   key, "with consummate restraint," is a collocation, not a derived form of
   anything — the root given was the noun *restraint* and the answer was that
   same noun plus an adjective. Worse, its feedback opened by admitting "all
   four options are grammatically possible," which makes the item unscoreable:
   a learner who picks "with restraint" is marked wrong for a correct answer.
   Replaced with a genuine derivation item on the same root *restrain*, keying
   the adjective *restrained* against three plausible wrong derivations
   (*restraining*, *restraint*, *restrictive*). The film-criticism register of
   the surrounding page is kept.
"""

MC_POS = [2, 0, 3, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 2, 0]

_MC_RAW = [

    # ── Section I: Film Criticism Terminology ────────────────────────
    ("The reviewer praised the director&rsquo;s control of _____ &mdash; the "
     "precise arrangement of every visual element within the frame: the "
     "actors&rsquo; positioning, the set design, the lighting, and the costumes.",
     ["mise-en-scène", "cinematography", "production design", "blocking"],
     "q1why"),

    ("The Wagner leitmotif plays whenever Nietzsche remembers his former friend. "
     "This music exists only on the film&rsquo;s soundtrack &mdash; the "
     "characters cannot hear it. It is _____ music.",
     ["non-diegetic", "diegetic", "ambient", "synchronous"],
     "q2why"),

    ("Some critics felt the film sacrificed _____ for spectacle: the "
     "19th-century Turin streets looked too clean, the costumes too pristine, "
     "and Nietzsche too healthy &mdash; none of it felt historically believable.",
     ["verisimilitude", "continuity", "authenticity", "realism"],
     "q3why"),

    # ── Section II: Precise Collocations ─────────────────────────────
    ("After three years of post-production disputes, the studio finally _____ "
     "the film for release last autumn.",
     ["greenlit", "authorised", "permitted", "validated"],
     "q4why"),

    ("The film went significantly over budget, and the producers had to seek "
     "additional funding _____ the eleventh hour to avoid shutting down the "
     "production.",
     ["at", "in", "on", "during"],
     "q5why"),

    ("The director&rsquo;s decision to cast an unknown actor in the lead role "
     "was considered _____ &mdash; no major studio had taken that risk on a "
     "period biographical film with a €40 million budget.",
     ["unprecedented", "groundbreaking", "unparalleled", "pioneering"],
     "q6why"),

    # ── Section III: Register & Connotation ──────────────────────────
    ("A Frankfurter Allgemeine critic writes of the film: &ldquo;Despite its "
     "ambitions, <em>Thus Spake Nietzsche</em> is ultimately a _____ work "
     "&mdash; it imitates the surface of its influences without understanding "
     "them.&rdquo;",
     ["ersatz", "derivative", "imitative", "unoriginal"],
     "q7why"),

    ("In the official press release, the studio announced that the director "
     "would _____ from the project due to creative differences, and that a "
     "replacement would be named shortly.",
     ["withdraw", "walk away", "bail out", "quit"],
     "q8why"),

    ("The performance by the lead actor was widely described as _____ &mdash; a "
     "word that suggests the performance will be studied, referenced, and "
     "judged against for generations to come.",
     ["definitive", "memorable", "outstanding", "powerful"],
     "q9why"),

    # ── Section IV: Phrasal Verbs & Idioms in Context ────────────────
    ("The production designer warned the director that if the budget was cut "
     "any further, they would have to _____ several key set pieces that were "
     "central to the visual identity of the film.",
     ["do away with", "cut down on", "put off", "get rid of"],
     "q10why"),

    ("In the pitch meeting, the executive producer made it clear that the "
     "studio would not _____ any further delays &mdash; the film had to be "
     "delivered to the festival by March 1st, without exception.",
     ["countenance", "put up with", "stand for", "go along with"],
     "q11why"),

    ("When asked about the film&rsquo;s controversial ending, the director said "
     "she had deliberately _____ easy resolutions, preferring to leave the "
     "audience with the discomfort Nietzsche himself lived with.",
     ["eschewed", "avoided", "shunned", "refrained from"],
     "q12why"),

    # ── Section V: Word Formation in Context ─────────────────────────
    ("Critics debated whether the film&rsquo;s _____ of Nietzsche as a tragic "
     "romantic figure was historically responsible or dangerously misleading. "
     "<em>(ROOT: portray)</em>",
     ["portrayal", "portraying", "portrayal&rsquo;s", "portrait"],
     "q13why"),

    ("The film&rsquo;s score was praised for its _____ use of Wagner&rsquo;s "
     "motifs &mdash; stripped of their nationalist associations and reworked "
     "into something quietly devastating. <em>(ROOT: evoke)</em>",
     ["evocative", "evocating", "evocational", "evoked"],
     "q14why"),

    ("The lead actor&rsquo;s _____ performance in the closing scenes &mdash; "
     "barely a raised voice, barely a gesture &mdash; was singled out by every "
     "major broadsheet as the finest work of his career. <em>(ROOT: restrain)</em>",
     ["restrained", "restraining", "restraint", "restrictive"],
     "q15why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ORIGINAL EXPLANATIONS — the page's own feedback text, kept as source
# material for the i18n module. Not used at runtime.
#
# q1: Mise-en-scène (French: "placing on stage") is the overarching term for everything visible within the frame as a composed whole: setting, lighting, costume, actor placement, and movement. Cinematography refers specifically to camera work and lighting technique. Blocking refers only to actor and camera movement planning. Production design covers sets and visual environment alone.
# q2: Non-diegetic sound exists outside the story world — only the audience hears it (a film score, voiceover narration). Diegetic sound exists within the story world and could theoretically be heard by the characters (a piano playing in a room, a gunshot). The distinction is fundamental in film sound theory.
# q3: Verisimilitude (from Latin verum similis — "like the truth") is the quality of seeming true or real within the conventions of the work — it is the preferred critical term over "realism," which implies a specific artistic movement. Authenticity is a broader cultural/ethical concept. Continuity refers specifically to visual consistency between shots, not believability. At C1, distinguishing verisimilitude from realism is essential.
# q4: To greenlight a project (past: greenlit) is the standard industry collocation for giving official approval for a film to proceed — used specifically in the film and television business. "Authorised," "permitted," and "validated" are all technically possible but sound like a bureaucratic document, not a film industry professional speaking.
# q5: "At the eleventh hour" is a fixed idiomatic expression meaning at the last possible moment — the preposition is always "at." It comes from the Biblical parable of labourers hired at the last hour of the working day. At C1, mastery of fixed prepositional phrases in professional idioms is expected.
# q6: Groundbreaking collocates naturally with creative or artistic decisions that open new territory — it carries a sense of innovation and courage. Unprecedented means "never done before" but is more formal and statistical. Unparalleled means "without equal" — a matter of quality, not novelty. Pioneering is close but more commonly used of people or movements, not single decisions.
# q7: Ersatz (borrowed from German into English) means a poor or inferior substitute — it carries a connotation of something that pretends to be the real thing. In intellectual criticism, "ersatz" implies fraudulence, not just lack of originality. It is the most precisely contemptuous of the four. Derivative is common but softer — merely derived from something else. Imitative is neutral and descriptive. Unoriginal is the most mundane register.
# q8: Withdraw is the correct formal register for a press release — neutral, professional, and non-judgmental. Walk away is informal and implies a degree of choice or principle. Bail out is informal/colloquial with a connotation of abandonment or cowardice. Quit is informal and slightly blunt. Register matching is a core C1 skill: the right word in the wrong register is still the wrong word.
# q9: Definitive means the best, most authoritative version — the standard by which all others will be measured. "The definitive Hamlet." It carries a sense of finality and critical consensus. Memorable simply means unforgettable. Outstanding means very good but not uniquely authoritative. Powerful describes emotional impact, not canonical status.
# q10: Do away with means to abolish or eliminate entirely — the strongest and most definitive of the options. It conveys that something is being removed permanently and decisively, which fits the severity of losing "key set pieces." Cut down on means to reduce (not eliminate). Put off means to postpone. Get rid of is correct in meaning but too informal for the professional register of this sentence.
# q11: Countenance (formal verb: to accept or permit something to happen) is the most precise fit for a formal professional ultimatum — it implies a refusal to permit or sanction. Put up with and stand for mean to tolerate — both slightly less formal and more personal in tone. Go along with means to agree or cooperate, which changes the meaning — it implies acceptance of an ongoing arrangement, not tolerance of a delay.
# q12: Eschewed is the most precisely elevated choice — it means deliberately abstained from, often for principled reasons. It is the word a director speaking at a festival Q&A or to a quality broadsheet journalist would reach for. Avoided is neutral and too general. Shunned implies emotional rejection or social avoidance. Refrained from is correct but imposes self-restraint rather than artistic principle.
# q13: Portrayal is the correct nominalisation of "portray" — meaning the act or manner of depicting someone. Portraying is a gerund (verb form as noun) — grammatically possible but stylistically weaker in formal criticism. Portrait is a related noun but refers to a likeness (painting or photograph), not an act of representation in a film. Portrayal's is incorrectly possessivised here.
# q14: Evocative is the correct adjectival form — meaning tending to bring strong feelings, memories, or associations to mind. The suffix -ative forms adjectives from verbs: evoke → evocative, communicate → communicative, demonstrate → demonstrative. "Evocating" does not exist. "Evocational" is not a standard English form. "Evoked" is a past participle — grammatically possible as a modifier but changes the meaning to "having been evoked" rather than "capable of evoking."
# q15: (replaced — no original)
