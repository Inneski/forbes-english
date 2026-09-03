# -*- coding: utf-8 -*-
"""Football Vocabulary (B1) — the fourteen scored items.

Lifted verbatim from the pre-deck scrolling page, which is also where the
Argentina edition's identical copy came from. Two things were changed and
both were defects:

1. **Every one of the fourteen keys was authored at index 0.** The old page
   shuffled at runtime, so it never showed as A-A-A-A on screen, but it
   leaks straight through print and PDF export, and it is the exact defect
   the KEYS gate was written for after fifteen other lessons had it. Keys
   are now spread across the four positions by a fixed pattern with no run
   of three, so the source reads the way the screen does.

2. The Spanish gloss on each item (`es: "Referee = arbitro"`) had nowhere to
   go in a deck, because `data-explain` takes one string. It is now carried
   as a per-item UI_I18N key, so the gloss reaches a Spanish learner in the
   Spanish build and nobody else sees a stray Spanish word in an English
   explanation. Nothing was dropped.

The English being taught is never translated — stems and options stay in
English in every language, per house style §8.
"""

# key position per item: no run of three, all four letters used
KEY_POS = [1, 3, 0, 2, 1, 2, 3, 0, 2, 1, 3, 0, 1, 3]

# (stem, [options with the key FIRST], why-key)
_RAW = [
    ("The ______ blew the whistle to stop the match after a dangerous tackle.",
     ["referee", "striker", "substitute", "captain"], "q1why"),
    ("She scored a fantastic ______ from outside the penalty area.",
     ["goal", "corner", "offside", "foul"], "q2why"),
    ("The defender committed a ______ inside the box and gave away a penalty.",
     ["foul", "pass", "save", "cross"], "q3why"),
    ("The player received a ______ for a reckless tackle and was sent off immediately.",
     ["red card", "yellow card", "throw-in", "clean sheet"], "q4why"),
    ("The linesman raised his flag because the striker was in an ______ position.",
     ["offside", "onside", "corner", "save"], "q5why"),
    ("The ______ is the forward whose main job is to score goals close to the "
     "opponent&rsquo;s goal.",
     ["striker", "goalkeeper", "midfielder", "referee"], "q6why"),
    ("The ______ dived to his left and saved the penalty kick.",
     ["goalkeeper", "winger", "defender", "coach"], "q7why"),
    ("When the attacker&rsquo;s shot went out over the goal line, the defending "
     "team took a ______.",
     ["goal kick", "corner", "throw-in", "penalty"], "q8why"),
    ("The ball rolled out over the touchline, so the away team took a ______ to "
     "restart play.",
     ["throw-in", "corner", "kick-off", "free kick"], "q9why"),
    ("The winger managed to ______ past two defenders before crossing the ball "
     "into the box.",
     ["dribble", "tackle", "save", "block"], "q10why"),
    ("The goalkeeper kept a ______, which means the opposing team failed to "
     "score all game.",
     ["clean sheet", "own goal", "hat-trick", "red card"], "q11why"),
    ("Because the score was level after ninety minutes, the teams played ______ "
     "to find a winner.",
     ["extra time", "half-time", "injury time", "kick-off"], "q12why"),
    ("With ten minutes left, the coach made a ______ to bring on a faster player.",
     ["substitution", "formation", "possession", "counterattack"], "q13why"),
    ("It was a costly mistake when the defender accidentally scored an ______ "
     "under pressure.",
     ["own goal", "equaliser", "winner", "hat-trick"], "q14why"),
]


def _place(options, pos):
    """Move the key (authored first) to `pos`, keeping distractor order."""
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [
    dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
    for (stem, opts, why), pos in zip(_RAW, KEY_POS)
]

assert [q["options"][q["correct"]] for q in MC] == [r[1][0] for r in _RAW], \
    "reordering lost a key"
