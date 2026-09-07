#!/usr/bin/env python3
"""
Forbes English — The FireShield Pitch (B2)

Merges the three separate FireShield pages into one continuous lesson:

    fireshield-pitch-roleplay.html  -> Act I  — The Site Office
    fireshield-pitch-part2.html     -> Act II — The Framework
    fireshield-pitch-part3.html     -> Act III — The Conference

Why the merge changed the mechanics, not just the file count:

1. Parts 2 and 3 each opened by ASKING the learner how the previous part had
   ended, because a separate file cannot know. Four buttons, one of which the
   learner picks more or less at random. That recap picker is gone: the acts
   now hand their outcome forward, so what actually happened is what carries.

2. Trust now runs continuously across all three acts — eighteen months in one
   bar — and the OUTCOME is scored on trust earned against trust available,
   not on the absolute reading.

   This was not the first attempt. Re-basing the meter at each act boundary to
   the old recap values (85/60/45, then 90/65/45) looked faithful to the
   originals and was measurably wrong: simulating all 737,280 playthroughs put
   84% of them on the best ending and made the worst ending unreachable, because
   nine checkpoints all pay out positively, the meter clamps at 100, and Act III
   opened already above its own top threshold. A ratio cannot saturate, so the
   endings discriminate again. Re-run tools/simulate_fireshield.js after any
   change to a trust value.

3. Checkpoint trust is awarded ON THE FIRST ATTEMPT ONLY. In the originals a
   wrong answer simply sat there until you clicked the right one, so every
   learner banked every checkpoint point and the meter measured nothing but
   the story choices. First-try scoring makes the vocabulary carry weight.

4. The two catastrophic branches (overstating the fire rating in Act I,
   deflecting responsibility in Act II) still end the run — that consequence
   is the point — but they now offer a rewind to the decision, so a single
   bad click no longer locks the learner out of two thirds of the lesson.

5. Duplicate target items across the three parts were re-cut: 'trade off' and
   'reliable' each appeared twice, so Act II now teaches 'liability' and
   'accountable' in those slots.

6. The key was the FIRST option in 19 of the 20 checkpoints, inherited from
   all three originals — a learner could score full marks by always clicking
   the top button without reading. Options are now Fisher-Yates shuffled at
   render time AND deterministically pre-shuffled in the source, because
   check-lesson.js is explicit that an authored key-first order still leaks
   through print and PDF export.

7. It is a real 16:9 deck now: four slides on a 1280x720 stage, one scene per
   screen, using the template's own fitStage() centring. The branching never
   needed scrolling — it needed state. tools/fit_fireshield.js renders all 32
   scenes in all three languages and measures each against the canvas, because
   check-lesson.js can only measure whichever scene happens to be on screen.

Artwork: FireShield/*.jpg, cropped from the Midjourney originals uploaded in
6d6cbe9. Palette derived mechanically:

    python3 lesson-template/extract-palette.py FireShield/hero.jpg --light

Build:

    python3 lesson-template/build/build_fireshield.py
    node   tools/simulate_fireshield.js      # endings stay reachable
    node   tools/fit_fireshield.js           # every scene fits the canvas
    node   lesson-template/check-lesson.js fireshield-pitch.html
    python3 tools/seo.py                     # last, always
"""

import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D                      # shared — see CLAUDE.md, do not rewrite

TPL = "lesson-template/lesson-template.html"

OUT = "fireshield-pitch.html"

# --------------------------------------------------------------------------
# Palette — derived from FireShield/hero.jpg, --light. Every contrast row
# PASSes. Do not hand-edit; re-run extract-palette.py if the hero changes.
# --------------------------------------------------------------------------
PALETTE = {
    "void": "#d0c4b4",
    "surface": "#dcd4ca",
    "surface2": "#d5cbbe",
    "border": "#96664a",
    "text": "#2a1a11",
    "text-dim": "#5e402e",
    "accent": "#934618",
    "accent-bright": "#6d2f0b",
    "accent-dim": "#d18354",
    "secondary": "#161f24",
    "contrast": "#195c55",
}

# House rule 5 / §8: a language shows in the menu only if it defines every key
# English defines. Partial is a failure, not a work in progress.
LANGS = ("en", "de", "es")

# --------------------------------------------------------------------------
# Translation scope — HOUSE-STYLE §8, and deck.py's mc() confirms it: only the
# eyebrow and the title carry data-i18n there; the question stem, the options
# and the explanation carry none.
#
# So the app's chrome translates. The English being taught does NOT: the story
# prose, the choices Alex makes, the question stems, the options, the
# explanations and the ending text are the B2 reading input this lesson exists
# to deliver. Translating them would leave a learner reading Spanish and
# practising nothing. The activation stage follows the same line — the task
# instructions translate, the target-language chips do not.
# --------------------------------------------------------------------------
I18N = {
    "en": {
        "kicker": "Forbes English &middot; B2 &middot; Branching sales roleplay",
        "trustLabel": "Priya&rsquo;s trust",
        "briefing": "Briefing",
        "btnBegin": "Begin &rarr;",
        "btnStart": "Take the meeting",
        "btnContinue": "Continue",
        "btnNextAct": "Six months later &rarr;",
        "btnRewind": "Rewind to that decision",
        "btnRestart": "Play the whole thing again",
        "btnActivate": "Now use the language &rarr;",
        "carry": "Priya&rsquo;s trust now stands at",
        "langLabel": "Language",
        "actHeading": "Now use the language",
        "actChips": "Use at least three of these, in English:",
        "actSpeak": "🗣 Discussion",
        "actWrite": "✍️ Writing",
        "actWords": "words",
        "btnCopy": "Copy",
        "btnCopied": "Copied",
    },
    "de": {
        "kicker": "Forbes English &middot; B2 &middot; Verzweigtes Verkaufs-Rollenspiel",
        "trustLabel": "Priyas Vertrauen",
        "briefing": "Briefing",
        "btnBegin": "Beginnen &rarr;",
        "btnStart": "Zum Termin",
        "btnContinue": "Weiter",
        "btnNextAct": "Sechs Monate später &rarr;",
        "btnRewind": "Zu dieser Entscheidung zurück",
        "btnRestart": "Alles noch einmal spielen",
        "btnActivate": "Jetzt selbst anwenden &rarr;",
        "carry": "Priyas Vertrauen steht jetzt bei",
        "langLabel": "Sprache",
        "actHeading": "Jetzt selbst anwenden",
        "actChips": "Verwenden Sie mindestens drei davon, auf Englisch:",
        "actSpeak": "🗣 Diskussion",
        "actWrite": "✍️ Schreiben",
        "actWords": "Wörter",
        "btnCopy": "Kopieren",
        "btnCopied": "Kopiert",
    },
    "es": {
        "kicker": "Forbes English &middot; B2 &middot; Juego de rol de ventas ramificado",
        "trustLabel": "La confianza de Priya",
        "briefing": "Instrucciones",
        "btnBegin": "Empezar &rarr;",
        "btnStart": "Entrar a la reunión",
        "btnContinue": "Continuar",
        "btnNextAct": "Seis meses después &rarr;",
        "btnRewind": "Volver a esa decisión",
        "btnRestart": "Jugar todo otra vez",
        "btnActivate": "Ahora usa el idioma &rarr;",
        "carry": "La confianza de Priya ahora está en",
        "langLabel": "Idioma",
        "actHeading": "Ahora usa el idioma",
        "actChips": "Usa al menos tres de estas, en inglés:",
        "actSpeak": "🗣 Debate",
        "actWrite": "✍️ Escritura",
        "actWords": "palabras",
        "btnCopy": "Copiar",
        "btnCopied": "Copiado",
    },
}

# Scene eyebrows — the one part of a scene that is chrome rather than content.
TAGS = {
    "sc1":   {"en": "Scene 1 — The Opening",
              "de": "Szene 1 — Der Einstieg",
              "es": "Escena 1 — La apertura"},
    "sc2":   {"en": "Scene 2 — The Objection",
              "de": "Szene 2 — Der Einwand",
              "es": "Escena 2 — La objeción"},
    "sc3":   {"en": "Scene 3 — The New Ask",
              "de": "Szene 3 — Die neue Forderung",
              "es": "Escena 3 — La nueva petición"},
    "sc4":   {"en": "Scene 4 — The Framework",
              "de": "Szene 4 — Der Rahmenvertrag",
              "es": "Escena 4 — El acuerdo marco"},
    "sc5":   {"en": "Scene 5 — The Conference",
              "de": "Szene 5 — Die Konferenz",
              "es": "Escena 5 — La conferencia"},
    "sc6":   {"en": "Scene 6 — The Distributor",
              "de": "Szene 6 — Der Händler",
              "es": "Escena 6 — El distribuidor"},
    "cpVocab": {"en": "Checkpoint — Vocabulary",
                "de": "Zwischenstopp — Wortschatz",
                "es": "Punto de control — Vocabulario"},
    "cpColl": {"en": "Checkpoint — Collocation and tense",
               "de": "Zwischenstopp — Kollokation und Zeitform",
               "es": "Punto de control — Colocación y tiempo verbal"},
    "cpPast": {"en": "Checkpoint — Past Continuous",
               "de": "Zwischenstopp — Past Continuous",
               "es": "Punto de control — Past Continuous"},
    "cpReg":  {"en": "Checkpoint — Register",
               "de": "Zwischenstopp — Register",
               "es": "Punto de control — Registro"},
    "endA1":  {"en": "End of Act I — Manchester",
               "de": "Ende von Akt I — Manchester",
               "es": "Fin del Acto I — Manchester"},
    "endA2":  {"en": "End of Act II — Leeds",
               "de": "Ende von Akt II — Leeds",
               "es": "Fin del Acto II — Leeds"},
    "endA3":  {"en": "End of Act III — Dublin",
               "de": "Ende von Akt III — Dublin",
               "es": "Fin del Acto III — Dublín"},
    "failCancel": {"en": "Ending — Contract Cancelled",
                   "de": "Ende — Vertrag gekündigt",
                   "es": "Final — Contrato cancelado"},
    "failDeal":   {"en": "Ending — Deal Off the Table",
                   "de": "Ende — Der Auftrag ist weg",
                   "es": "Final — El acuerdo se retira"},
    "failStory":  {"en": "Ending — Story Confirmed",
                   "de": "Ende — Die Geschichte bestätigt sich",
                   "es": "Final — La historia confirmada"},
}

# --------------------------------------------------------------------------
# Chrome strings
# --------------------------------------------------------------------------
UI = {
    "title": {"en": "The FireShield Pitch"},
    "kicker": {"en": "Forbes English &middot; B2 &middot; Branching sales roleplay"},
    "trust_label": {"en": "Priya&rsquo;s trust"},
    "briefing": {"en": "Briefing"},
    "start": {"en": "Take the meeting"},
    "continue": {"en": "Continue"},
    "next_act": {"en": "Six months later &rarr;"},
    "rewind": {"en": "Rewind to that decision"},
    "restart": {"en": "Play the whole thing again"},
    "to_activation": {"en": "Now use the language &rarr;"},
    "act_label": {"en": "Act"},
    "carry": {"en": "Priya\u2019s trust now stands at"},
}

INTRO = {
    "en": [
        "You are Alex Rowntree, a sales rep for Forbes Membranes. Over three "
        "meetings and eighteen months you have to sell FireShield HX — a "
        "fire-retardant vapour barrier — to a buyer who has been let down "
        "before, then keep her when a rival's product fails, then defend the "
        "whole story in public.",
        "Every choice moves Priya's trust. Vocabulary checkpoints move it too, "
        "but only if you get them right first time. Where you finish depends "
        "on what you actually did, not on how the last meeting is summarised.",
    ],
    "de": [
        "Sie sind Alex Rowntree, Vertriebsmitarbeiter bei Forbes Membranes. In "
        "drei Terminen über achtzehn Monate müssen Sie FireShield HX — eine "
        "flammhemmende Dampfsperre — an eine Einkäuferin verkaufen, die schon "
        "einmal enttäuscht wurde; sie halten, wenn das Produkt eines "
        "Konkurrenten versagt; und die ganze Geschichte öffentlich vertreten.",
        "Jede Entscheidung verändert Priyas Vertrauen. Die Wortschatz-Stopps "
        "auch — aber nur, wenn Sie sie beim ersten Versuch richtig lösen. Wo "
        "Sie landen, hängt davon ab, was Sie tatsächlich getan haben.",
    ],
    "es": [
        "Eres Alex Rowntree, comercial de Forbes Membranes. A lo largo de tres "
        "reuniones y dieciocho meses tienes que vender FireShield HX —una "
        "barrera de vapor ignífuga— a una compradora a la que ya le fallaron "
        "una vez, mantenerla cuando el producto de un rival falla, y después "
        "defender toda la historia en público.",
        "Cada decisión mueve la confianza de Priya. Los puntos de control de "
        "vocabulario también, pero solo si aciertas a la primera. Dónde acabas "
        "depende de lo que hiciste de verdad.",
    ],
}

# --------------------------------------------------------------------------
# Scenes
#
# type: story      — narrative + choices, each carrying a trust delta
#       checkpoint — narrative + question; trust awarded on first try only
#       interlude  — act boundary; tiers pick the outcome prose and the trust
#                    carried into the next act
#       ending     — terminal. 'rewind' marks a recoverable failure branch.
# --------------------------------------------------------------------------
SCENES = {

    # ------------------------------------------------------------------ Act I
    "a1_open": {
        "type": "story", "act": 1, "bg": "act1",
        "tag": {"en": "Scene 1 — The Opening"},
        "narrative": {"en":
            "Meridian Construction's site office, Manchester. Priya Shah greets you "
            "with a firm handshake and the look of someone who has heard enough sales "
            "pitches to last a lifetime. Her last supplier caused a <i>shortfall</i> "
            "that cost her three weeks of work. You have twenty minutes."},
        "choices": [
            {"label": {"en": "Lead with the technical specifications and test data"},
             "next": "a1_tech", "trust": 0},
            {"label": {"en": "Ask about the problems she has had with suppliers before"},
             "next": "a1_consult", "trust": 10},
            {"label": {"en": "Open with a 15% discount if she signs today"},
             "next": "a1_shortfall", "trust": -10},
        ],
    },

    "a1_tech": {
        "type": "checkpoint", "act": 1, "bg": "act1",
        "tag": {"en": "Checkpoint — Collocation and tense"},
        "narrative": {"en":
            "You open your laptop and start talking through fire ratings and moisture "
            "permeability figures. Priya cuts in: &lsquo;Before I look at numbers — has "
            "this actually been tested on a live site, or just in a lab?&rsquo;"},
        "question": {"en": "Which sentence is correct?"},
        "options": {"en": [
            "We made a full test on three sites last year.",
            "We did a full test on three sites last year.",
            "We are making a full test on three sites last year."]},
        "correct": 1,
        "explain": {"en":
            "&lsquo;Do a test&rsquo; is the natural collocation — &lsquo;make a "
            "test&rsquo; is a common but incorrect translation — and the finished "
            "action needs Past Simple."},
        "trustOnCorrect": 10, "next": "a1_shortfall",
    },

    "a1_consult": {
        "type": "checkpoint", "act": 1, "bg": "act1",
        "tag": {"en": "Checkpoint — Past Continuous"},
        "narrative": {"en":
            "Priya's shoulders drop slightly. &lsquo;Our last supplier promised weekly "
            "deliveries. For two months ___ fine — then the shipments just stopped and "
            "we lost three weeks of work.&rsquo;"},
        "question": {"en": "Which fits the gap?"},
        "options": {"en": ["we were coping", "we coped", "we have been coping"]},
        "correct": 0,
        "explain": {"en":
            "Past Continuous (&lsquo;we were coping&rsquo;) sets the ongoing background "
            "situation that the Past Simple event (&lsquo;the shipments stopped&rsquo;) "
            "interrupted."},
        "trustOnCorrect": 10, "next": "a1_shortfall",
    },

    "a1_shortfall": {
        "type": "checkpoint", "act": 1, "bg": "act1",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "Priya leans back. &lsquo;Here is my real problem — I have a ___ of about "
            "400 square metres between what my current supplier can deliver this month "
            "and what the schedule needs. Your competitor, Northline, is offering "
            "something similar for 8% less.&rsquo;"},
        "question": {"en": "Which word fits the gap?"},
        "options": {"en": ["shortfall", "trade-off", "contingency plan", "threshold"]},
        "correct": 0,
        "explain": {"en":
            "A &lsquo;shortfall&rsquo; is exactly this — the gap between what is needed "
            "and what is actually available."},
        "trustOnCorrect": 5, "next": "a1_objection",
    },

    "a1_objection": {
        "type": "story", "act": 1, "bg": "act1",
        "tag": {"en": "Scene 2 — The Objection"},
        "narrative": {"en":
            "Priya is waiting for your answer, and the Northline quote is face-up on "
            "the desk between you."},
        "choices": [
            {"label": {"en": "Offer a small trial installation on one wing before she commits to the full order"},
             "next": "a1_trial", "trust": 5},
            {"label": {"en": "Match Northline's price on the spot"},
             "next": "a1_match", "trust": -5},
            {"label": {"en": "Tell her FireShield HX has a fire rating well beyond what it is actually certified for"},
             "next": "end_lie1", "trust": -30},
        ],
    },

    "a1_trial": {
        "type": "checkpoint", "act": 1, "bg": "act1",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "&lsquo;One wing, fully documented, before you commit to the rest — no risk "
            "to your schedule if it does not perform.&rsquo; Priya raises an eyebrow, "
            "interested."},
        "question": {"en": "Which word best describes what you have just proposed?"},
        "options": {"en": ["a trial", "a precedent", "an assumption", "a concession"]},
        "correct": 0,
        "explain": {"en":
            "A &lsquo;trial&rsquo; is a small-scale test of performance or suitability "
            "before full commitment — exactly what you have offered."},
        "trustOnCorrect": 10, "next": "a1_close",
    },

    "a1_match": {
        "type": "checkpoint", "act": 1, "bg": "act1",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You agree to match Northline's price. Your regional manager will not be "
            "pleased, but Priya nods slowly."},
        "question": {"en": "Matching the price on the spot is really a ___ between margin and winning the contract."},
        "options": {"en": ["trade-off", "shortfall", "precaution", "requirement"]},
        "correct": 0,
        "explain": {"en":
            "A &lsquo;trade-off&rsquo; is exchanging one thing of value (margin) for "
            "another (the contract) — exactly what is happening here."},
        "trustOnCorrect": 5, "next": "a1_close",
    },

    "a1_close": {
        "type": "checkpoint", "act": 1, "bg": "act1",
        "tag": {"en": "Checkpoint — Register"},
        "narrative": {"en":
            "Before you leave, you draft a short follow-up email confirming next steps. "
            "You want it convincing, without sounding pushy."},
        "question": {"en": "Which word describes writing convincingly, using reasoning rather than pressure?"},
        "options": {"en": ["persuasive", "exaggerated", "arduous", "compromised"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Persuasive&rsquo; means effective at convincing through reasoning — "
            "the register you want here, as opposed to exaggerating or pressuring."},
        "trustOnCorrect": 10, "next": "int1",
    },

    "int1": {
        "type": "interlude", "act": 1,
        "tag": {"en": "End of Act I — Manchester"},
        "tiers": [
            {"min": 0.78,
             "title": {"en": "The trial wing performs exactly as promised."},
             "body": {"en":
                "Priya signs Meridian's entire tower order and tells two other site "
                "managers to call you directly. You did not win her with a number; you "
                "won her by removing her risk."}},
            {"min": 0.45,
             "title": {"en": "The trial wing does the job."},
             "body": {"en":
                "Priya signs the order for the tower, but she stays polite and reserved "
                "rather than warm. The product is proven. The relationship is not."}},
            {"min": 0.0,
             "title": {"en": "Priya signs, relieved to have matched the competitor's price."},
             "body": {"en":
                "The order goes through, but your margin is razor-thin, and she still "
                "mentions Northline every time you call. You bought the contract instead "
                "of earning it."}},
        ],
        "next": "a2_open",
    },

    # ----------------------------------------------------------------- Act II
    "a2_open": {
        "type": "story", "act": 2, "bg": "act2",
        "tag": {"en": "Scene 3 — The New Ask"},
        "narrative": {"en":
            "Six months on. Meridian's regional director wants a framework agreement "
            "covering five new sites in Leeds — ten times the size of the original "
            "order. But a rival's membrane failed on a nearby site last month: mould "
            "appeared behind the cladding, and every supplier is under suspicion. Priya "
            "calls you: &lsquo;Before anyone signs anything, I need to know FireShield "
            "HX will not do the same thing.&rsquo;"},
        "choices": [
            {"label": {"en": "Offer to walk the failed site with her and compare installation methods"},
             "next": "a2_walk", "trust": 10},
            {"label": {"en": "Send a written assurance that your product is completely safe"},
             "next": "a2_assure", "trust": -10},
            {"label": {"en": "Suggest bringing in an independent third-party auditor"},
             "next": "a2_adhoc", "trust": 5},
        ],
    },

    "a2_walk": {
        "type": "checkpoint", "act": 2, "bg": "act2",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You and Priya inspect the failed site together. The membrane itself looks "
            "intact, but the fixing points show damp staining."},
        "question": {"en": "Which word describes water present in small quantity within a material or on a surface?"},
        "options": {"en": ["moisture", "threshold", "firmness", "precaution"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Moisture&rsquo; is water diffused in small quantity within a solid "
            "or condensed on a surface — exactly what is staining the fixing points."},
        "trustOnCorrect": 10, "next": "a2_resilient",
    },

    "a2_assure": {
        "type": "checkpoint", "act": 2, "bg": "act2",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "Your email lands — all confidence, no evidence. Priya replies within the "
            "hour: &lsquo;That is not really an answer.&rsquo;"},
        "question": {"en": "Priya felt your email offered reassurance with no evidence. Which word describes that?"},
        "options": {"en": ["an assumption", "a precaution", "a requirement", "a trade-off"]},
        "correct": 0,
        "explain": {"en":
            "An &lsquo;assumption&rsquo; is something accepted as true without proof — "
            "exactly what an unsupported reassurance amounts to."},
        "trustOnCorrect": 5, "next": "a2_resilient",
    },

    "a2_adhoc": {
        "type": "checkpoint", "act": 2, "bg": "act2",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "Priya likes the idea of independent verification, but wants to know it will "
            "not drag on for months."},
        "question": {"en": "Which phrase describes something arranged for a specific purpose, as needed, without a long-term structure?"},
        "options": {"en": ["ad hoc", "post hoc", "homogeneous", "in perpetuity"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Ad hoc&rsquo; describes something set up for a specific purpose as "
            "it is needed, rather than as a permanent structure."},
        "trustOnCorrect": 10, "next": "a2_resilient",
    },

    "a2_resilient": {
        "type": "checkpoint", "act": 2, "bg": "act2",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "The audit confirms it: the rival's failure was caused by poor installation "
            "trapping moisture behind the membrane, not by a flaw in the material. "
            "Still, the regional director is nervous about signing a five-site agreement "
            "while that story is circulating."},
        "question": {"en": "Which word means &lsquo;able to withstand or recover quickly from difficult conditions&rsquo; — exactly what you need your reputation to be?"},
        "options": {"en": ["resilient", "hazardous", "monotonous", "agitated"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Resilient&rsquo; describes the ability to recover from damage or "
            "difficulty — the quality your reputation needs here."},
        "trustOnCorrect": 5, "next": "a2_objection",
    },

    "a2_objection": {
        "type": "story", "act": 2, "bg": "act2",
        "tag": {"en": "Scene 4 — The Framework"},
        "narrative": {"en":
            "The director puts a number on the table: a five-site framework, but only if "
            "you can guarantee installation quality, not just material quality."},
        "choices": [
            {"label": {"en": "Propose a phased rollout — one site first, as a monitored pilot, before the rest"},
             "next": "a2_pilot", "trust": 10},
            {"label": {"en": "Offer to cover the retrofit cost on the failed site yourself, as goodwill, even though it was not your product"},
             "next": "a2_liability", "trust": 5},
            {"label": {"en": "Push back and say installation quality is not Forbes' responsibility"},
             "next": "end_deflect", "trust": -30},
        ],
    },

    "a2_pilot": {
        "type": "checkpoint", "act": 2, "bg": "act2",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "&lsquo;One site, fully monitored, before the rest&rsquo; — the director "
            "likes that it limits their risk without questioning your product."},
        "question": {"en": "Which word means &lsquo;a condition that must be met&rsquo;?"},
        "options": {"en": ["requirement", "assumption", "threshold", "shortfall"]},
        "correct": 0,
        "explain": {"en":
            "A &lsquo;requirement&rsquo; is a condition that must be met — here, the "
            "monitoring the director insists on."},
        "trustOnCorrect": 10, "next": "a2_close",
    },

    "a2_liability": {
        "type": "checkpoint", "act": 2, "bg": "act2",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You offer to help cover the retrofit cost on the failed site, even though "
            "it was not your product that failed. Your finance director asks, carefully, "
            "whether you have just admitted something."},
        "question": {"en": "Which word describes legal responsibility for a cost or a fault?"},
        "options": {"en": ["liability", "requirement", "precaution", "shortfall"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Liability&rsquo; is legal responsibility for something, especially a "
            "cost — which is why paying for a failure that was not yours has to be "
            "worded as goodwill, not as an admission."},
        "trustOnCorrect": 5, "next": "a2_close",
    },

    "a2_close": {
        "type": "checkpoint", "act": 2, "bg": "act2",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You draft the final proposal for the five-site framework. The director's "
            "one real fear is that nobody will own the outcome if a site goes wrong."},
        "question": {"en": "Which word describes being required to explain and take responsibility for your actions?"},
        "options": {"en": ["accountable", "affordable", "monotonous", "provisional"]},
        "correct": 0,
        "explain": {"en":
            "To be &lsquo;accountable&rsquo; is to be required to explain and answer for "
            "what you do — the assurance the director is actually buying."},
        "trustOnCorrect": 10, "next": "int2",
    },

    "int2": {
        "type": "interlude", "act": 2,
        "tag": {"en": "End of Act II — Leeds"},
        "tiers": [
            {"min": 0.78,
             "title": {"en": "The regional director signs the full framework."},
             "body": {"en":
                "Priya becomes the go-to reference for Forbes Membranes across the "
                "North West, and FireShield HX becomes the preferred spec for Meridian's "
                "entire regional pipeline."}},
            {"min": 0.45,
             "title": {"en": "The director agrees to the monitored pilot site."},
             "body": {"en":
                "The rest of the framework stays pending the results. Real progress, and "
                "Priya is on your side — but the big number is still six months away."}},
            {"min": 0.0,
             "title": {"en": "The director signs only the original, already-disputed site."},
             "body": {"en":
                "The wider framework is shelved. Priya privately tells you she pushed for "
                "more, but trust from the first deal had not recovered enough to carry a "
                "bigger ask."}},
        ],
        "next": "a3_open",
    },

    # ---------------------------------------------------------------- Act III
    "a3_open": {
        "type": "story", "act": 3, "bg": "act3",
        "tag": {"en": "Scene 5 — The Conference"},
        "narrative": {"en":
            "A year later, Dublin. Meridian's parent company has put you on stage in "
            "front of fifty construction buyers, with a rep from Kavanagh — the "
            "distributor you want — in the front row. Somewhere in the room is a trade "
            "journalist who has read about the mould story."},
        "choices": [
            {"label": {"en": "Open with the independent audit results and safety data"},
             "next": "a3_data", "trust": 5},
            {"label": {"en": "Open with Priya's story from Meridian, told in her own words"},
             "next": "a3_story", "trust": 10},
            {"label": {"en": "Address the mould story directly, before anyone can ask"},
             "next": "a3_headon", "trust": 8},
        ],
    },

    "a3_data": {
        "type": "checkpoint", "act": 3, "bg": "act3",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You lead with numbers: fire ratings, permeability figures, third-party "
            "sign-off. Heads nod, but nobody looks moved yet."},
        "question": {"en": "Which word fits: &lsquo;The safety audit was ___ by an independent inspector, not by us.&rsquo;"},
        "options": {"en": ["conducted", "persuaded", "provoked", "located"]},
        "correct": 0,
        "explain": {"en":
            "To &lsquo;conduct&rsquo; is to carry out or organise — an audit is "
            "conducted, and saying who conducted it is what gives the result its "
            "independence."},
        "trustOnCorrect": 10, "next": "a3_provoke",
    },

    "a3_story": {
        "type": "checkpoint", "act": 3, "bg": "act3",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You tell the room about Priya's original hesitation, the trial wing, and "
            "the way the relationship grew. A few buyers lean forward."},
        "question": {"en": "Which word means &lsquo;convince someone to do something&rsquo; — what a good story does better than a spreadsheet?"},
        "options": {"en": ["persuade", "provoke", "startle", "reassess"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Persuade&rsquo; is convincing someone through reasoning, evidence or "
            "emotion — a customer story does this more naturally than raw data."},
        "trustOnCorrect": 10, "next": "a3_provoke",
    },

    "a3_headon": {
        "type": "checkpoint", "act": 3, "bg": "act3",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "&lsquo;Some of you will have heard about a membrane failure on a site near "
            "one of ours,&rsquo; you say. &lsquo;Let us talk about it before you "
            "ask.&rsquo; The room goes quiet, then attentive."},
        "question": {"en": "Which word fits: &lsquo;A membrane installed incorrectly can become ___ over time — ours passed every follow-up inspection.&rsquo;"},
        "options": {"en": ["hazardous", "affordable", "monotonous", "homogeneous"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Hazardous&rsquo; means risky or dangerous. Naming the real risk "
            "honestly, then showing it did not apply to you, is what earns credibility."},
        "trustOnCorrect": 10, "next": "a3_provoke",
    },

    "a3_provoke": {
        "type": "checkpoint", "act": 3, "bg": "act3",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "In the Q&amp;A the journalist stands up: &lsquo;Is it not true that a "
            "Forbes membrane failed just months ago?&rsquo; It is not true — it was a "
            "rival's — and every eye in the room is on you."},
        "question": {"en": "Which word describes what her question is really trying to do?"},
        "options": {"en": ["provoke", "persuade", "reassess", "conduct"]},
        "correct": 0,
        "explain": {"en":
            "To &lsquo;provoke&rsquo; is to deliberately cause a reaction — she is "
            "testing whether you will get flustered on stage, not asking for facts."},
        "trustOnCorrect": 5, "next": "a3_objection",
    },

    "a3_objection": {
        "type": "story", "act": 3, "bg": "act3",
        "tag": {"en": "Scene 6 — The Distributor"},
        "narrative": {"en":
            "Afterwards, Kavanagh's rep finds you by the coffee stand. &lsquo;Honestly, "
            "your product looks the same as everything else on the market, and it is a "
            "lot cheaper to stay with our current supplier.&rsquo;"},
        "choices": [
            {"label": {"en": "Offer a five-year performance guarantee at a small additional cost"},
             "next": "a3_guarantee", "trust": 10},
            {"label": {"en": "Match the competitor's price to win the listing"},
             "next": "a3_afford", "trust": -5},
            {"label": {"en": "Tell her your product has never failed, anywhere, ever"},
             "next": "end_lie3", "trust": -30},
        ],
    },

    "a3_guarantee": {
        "type": "checkpoint", "act": 3, "bg": "act3",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "&lsquo;A written guarantee, backed by the audit you saw today. No extra "
            "risk on your side.&rsquo; She is listening properly now."},
        "question": {"en": "Which word describes a measure taken in advance to prevent something unpleasant — which is what a guarantee is, for her?"},
        "options": {"en": ["precaution", "requirement", "assumption", "trade-off"]},
        "correct": 0,
        "explain": {"en":
            "A &lsquo;precaution&rsquo; is arranged in advance to prevent a problem — "
            "the guarantee protects her against exactly the risk she is worried about."},
        "trustOnCorrect": 10, "next": "a3_close",
    },

    "a3_afford": {
        "type": "checkpoint", "act": 3, "bg": "act3",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You agree to match the competitor's number. It makes the listing easier for "
            "her to justify internally, and you already know what it does to your margin."},
        "question": {"en": "Matching the price makes the offer more ___, at the cost of your margin."},
        "options": {"en": ["affordable", "reliable", "persuasive", "accountable"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Affordable&rsquo; means reasonably priced. You have made the offer "
            "cheaper — a different lever from proving the product is worth the money."},
        "trustOnCorrect": 5, "next": "a3_close",
    },

    "a3_close": {
        "type": "checkpoint", "act": 3, "bg": "act3",
        "tag": {"en": "Checkpoint — Vocabulary"},
        "narrative": {"en":
            "You send Kavanagh a follow-up proposal for national distribution across "
            "Ireland — confident, not pushy. Eighteen months of work comes down to one "
            "quality the reader has to believe in."},
        "question": {"en": "Which word describes something that can be trusted to work well, every time?"},
        "options": {"en": ["reliable", "exaggerated", "provisional", "agitated"]},
        "correct": 0,
        "explain": {"en":
            "&lsquo;Reliable&rsquo; means dependable. After a public question about a "
            "past failure, this is the single word the whole proposal has to earn."},
        "trustOnCorrect": 10, "next": "final",
    },

    # -------------------------------------------------------------- Endings
    "final": {
        "type": "interlude", "act": 3, "final": True,
        "tag": {"en": "End of Act III — Dublin"},
        "tiers": [
            {"min": 0.85,
             "title": {"en": "Kavanagh commits to carrying FireShield HX right across Ireland."},
             "body": {"en":
                "The trade press runs a follow-up piece — not about the mould story, but "
                "about how Forbes handled it. Within a year FireShield HX is the "
                "reference case other suppliers get compared against. You never once "
                "claimed more than you could prove."}},
            {"min": 0.62,
             "title": {"en": "Kavanagh agrees to carry the product across the Dublin region."},
             "body": {"en":
                "Six months of sales data will decide whether it goes national. A real "
                "foothold in a new market — but the bigger win is still conditional."}},
            {"min": 0.38,
             "title": {"en": "Kavanagh places a modest first order."},
             "body": {"en":
                "The competitor's product stays on the shelves alongside yours. You are "
                "in the market, but you have not won it, and the next order is far from "
                "guaranteed."}},
            {"min": 0.0,
             "title": {"en": "Kavanagh takes the meeting, and nothing else."},
             "body": {"en":
                "No order, no listing, and a polite promise to keep you on file. "
                "Eighteen months of discounting bought you a seat in the room and no "
                "reason for anyone to choose you."}},
        ],
    },

    "end_lie1": {
        "type": "ending", "act": 1, "bg": "end", "rewind": "a1_objection",
        "tag": {"en": "Ending — Contract Cancelled"},
        "title": {"en": "Three weeks into installation, Meridian's fire safety consultant flags the discrepancy."},
        "body": {"en":
            "The certification does not match what you claimed. The contract is "
            "cancelled on the spot, and word travels fast around the Manchester "
            "construction scene. There is no Act II — but you can go back and take "
            "that decision again."},
    },

    "end_deflect": {
        "type": "ending", "act": 2, "bg": "end", "rewind": "a2_objection",
        "tag": {"en": "Ending — Deal Off the Table"},
        "title": {"en": "&lsquo;That is not the answer I needed to hear.&rsquo;"},
        "body": {"en":
            "The director ends the call within a minute of you deflecting "
            "responsibility. Meridian issues a tender for all five sites the following "
            "week, and Forbes is not on the list of invited suppliers."},
    },

    "end_lie3": {
        "type": "ending", "act": 3, "bg": "end", "rewind": "a3_objection",
        "tag": {"en": "Ending — Story Confirmed"},
        "title": {"en": "&lsquo;Never failed, anywhere, ever?&rsquo; the journalist repeats, pen already moving."},
        "body": {"en":
            "The trade press runs a story questioning Forbes' honesty rather than its "
            "product. Kavanagh's rep stops returning your calls, and the Dublin "
            "expansion is quietly shelved."},
    },
}

# --------------------------------------------------------------------------
# Activation stage — house rule 6. Speaking and writing, both live, under a
# strip of the language the lesson actually taught.
# --------------------------------------------------------------------------
TARGET_LANGUAGE = ["shortfall", "trade-off", "trial", "requirement", "precaution",
                   "assumption", "liability", "accountable", "moisture", "resilient",
                   "hazardous", "persuade", "provoke", "conduct an audit", "ad hoc",
                   "reliable", "affordable"]

ACTIVATION = {
    "speaking": {
        "en": [
            "You are Alex. Priya asks you point-blank whether FireShield HX could "
            "fail the way the rival's product did. You cannot say &lsquo;no&rsquo; "
            "and you cannot say &lsquo;yes&rsquo;. Answer her out loud, in under a "
            "minute.",
            "Your competitor is 8% cheaper and your buyer has said so. Argue for "
            "the higher price without once calling your product &lsquo;better&rsquo; "
            "— talk about risk, liability, and what a failure would actually cost "
            "her.",
            "A journalist asks you a question built on a false premise, in public. "
            "Correct the premise without sounding defensive, and take the room with "
            "you.",
        ],
        "de": [
            "Sie sind Alex. Priya fragt Sie direkt, ob FireShield HX genauso "
            "versagen könnte wie das Konkurrenzprodukt. Sie können weder "
            "&lsquo;nein&rsquo; noch &lsquo;ja&rsquo; sagen. Antworten Sie laut, in "
            "unter einer Minute.",
            "Der Wettbewerber ist 8% günstiger, und Ihre Kundin hat das gesagt. "
            "Begründen Sie den höheren Preis, ohne Ihr Produkt ein einziges Mal "
            "&lsquo;besser&rsquo; zu nennen — sprechen Sie über Risiko, Haftung und "
            "die tatsächlichen Kosten eines Schadens.",
            "Eine Journalistin stellt Ihnen öffentlich eine Frage, die auf einer "
            "falschen Annahme beruht. Korrigieren Sie die Annahme, ohne defensiv zu "
            "wirken, und nehmen Sie den Saal mit.",
        ],
        "es": [
            "Eres Alex. Priya te pregunta sin rodeos si FireShield HX podría fallar "
            "igual que el producto del rival. No puedes decir &lsquo;no&rsquo; ni "
            "puedes decir &lsquo;sí&rsquo;. Respóndele en voz alta, en menos de un "
            "minuto.",
            "Tu competidor es un 8% más barato y tu compradora lo ha dicho. Defiende "
            "el precio más alto sin llamar ni una sola vez &lsquo;mejor&rsquo; a tu "
            "producto: habla de riesgo, de responsabilidad y de lo que le costaría "
            "un fallo.",
            "Una periodista te hace en público una pregunta basada en una premisa "
            "falsa. Corrige la premisa sin sonar a la defensiva, y llévate a la sala "
            "contigo.",
        ],
    },
    "writing_brief": {
        "en":
            "Priya has emailed asking, in writing, for reassurance about the mould "
            "story before her director will sign. Write the reply in English. Give "
            "evidence rather than assurance, name what you will be accountable for, "
            "and propose a concrete next step. 150&ndash;250 words.",
        "de":
            "Priya hat Ihnen geschrieben und bittet schriftlich um eine Zusicherung "
            "zur Schimmel-Geschichte, bevor ihr Direktor unterschreibt. Schreiben "
            "Sie die Antwort auf Englisch. Liefern Sie Belege statt Beteuerungen, "
            "benennen Sie, wofür Sie geradestehen, und schlagen Sie einen konkreten "
            "nächsten Schritt vor. 150&ndash;250 Wörter.",
        "es":
            "Priya te ha escrito pidiendo por escrito garantías sobre la historia "
            "del moho antes de que su director firme. Escribe la respuesta en "
            "inglés. Da pruebas en lugar de promesas, di de qué te haces "
            "responsable y propón un siguiente paso concreto. 150&ndash;250 "
            "palabras.",
    },
}

# --------------------------------------------------------------------------
def t(node, lang="en"):
    """Pull a language string, falling back to English."""
    if isinstance(node, dict):
        return node.get(lang, node.get("en", ""))
    return node


def preshuffle(key, options, correct):
    """Move the key out of first position in the SOURCE, deterministically.

    The engine shuffles at render time, but check-lesson.js is explicit that
    the authored order still leaks through print and PDF export. 19 of these
    20 checkpoints were authored key-first, inherited from the three original
    files, so a learner reading a printout could score full marks by always
    taking the top option.

    Seeded on the scene key so a rebuild is byte-identical.
    """
    import random
    rng = random.Random("fireshield:" + key)
    order = list(range(len(options)))
    rng.shuffle(order)
    return [options[i] for i in order], order.index(correct)


_TAG_BY_EN = {v["en"]: k for k, v in TAGS.items()}


def tag_key(scene):
    """Scene eyebrows are chrome, so they carry an i18n key rather than text."""
    en = scene.get("tag", {}).get("en", "")
    if en not in _TAG_BY_EN:
        raise KeyError("no TAGS entry for eyebrow %r — add one so it translates" % en)
    return _TAG_BY_EN[en]


def js_scenes(lang="en"):
    """Emit the scene graph as a JS object literal for one language."""
    import json
    out = {}
    for key, s in SCENES.items():
        o = {"type": s["type"], "act": s.get("act"), "tagKey": tag_key(s)}
        if s.get("bg"):
            o["bg"] = s["bg"]
        if s["type"] == "story":
            o["narrative"] = t(s["narrative"], lang)
            o["choices"] = [{"label": t(c["label"], lang), "next": c["next"],
                             "trust": c["trust"]} for c in s["choices"]]
        elif s["type"] == "checkpoint":
            o["narrative"] = t(s["narrative"], lang)
            o["question"] = t(s["question"], lang)
            opts, corr = preshuffle(key, t(s["options"], lang), s["correct"])
            o["options"] = opts
            o["correct"] = corr
            o["explain"] = t(s["explain"], lang)
            o["trustOnCorrect"] = s["trustOnCorrect"]
            o["next"] = s["next"]
        elif s["type"] == "interlude":
            o["tiers"] = [{"min": x["min"],
                           "title": t(x["title"], lang), "body": t(x["body"], lang)}
                          for x in s["tiers"]]
            if s.get("next"):
                o["next"] = s["next"]
            if s.get("final"):
                o["final"] = True
        elif s["type"] == "ending":
            o["title"] = t(s["title"], lang)
            o["body"] = t(s["body"], lang)
            if s.get("rewind"):
                o["rewind"] = s["rewind"]
        out[key] = o
    return json.dumps(out, ensure_ascii=False, indent=1)


def js_i18n():
    """UI_I18N = chrome strings + scene eyebrows, per language.

    §8: the switcher is built from this at runtime and skips any language
    whose key count is short of English, so a half-done pass is never offered.
    """
    import json
    table = {}
    for lang in LANGS:
        row = dict(I18N[lang])
        for key, forms in TAGS.items():
            if lang in forms:
                row[key] = forms[lang]
        for i, para in enumerate(INTRO.get(lang, [])):
            row["intro%d" % i] = para
        for i, prompt in enumerate(ACTIVATION["speaking"].get(lang, [])):
            row["speak%d" % i] = prompt
        if lang in ACTIVATION["writing_brief"]:
            row["writeBrief"] = ACTIVATION["writing_brief"][lang]
        table[lang] = row
    return json.dumps(table, ensure_ascii=False, indent=1)


def build(lang="en"):
    p = PALETTE
    title = t(UI["title"], lang)
    logo = D.logo_from(TPL)
    # Anything translatable carries data-i18n; anything without it will never
    # translate (HOUSE-STYLE §8 — the usual cause of a stubbornly English button).
    intro_ps = "\n        ".join(
        f'<p data-i18n="intro{i}">{x}</p>' for i, x in enumerate(INTRO["en"]))
    speak = "\n          ".join(
        f'<li data-i18n="speak{i}">{x}</li>'
        for i, x in enumerate(ACTIVATION["speaking"]["en"]))
    # Target-language chips stay English by rule — no data-i18n on them.
    chips = "\n          ".join(f'<span class="chip">{html.escape(c)}</span>'
                               for c in TARGET_LANGUAGE)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} (B2) | Forbes English</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{{
    --void:{p['void']};
    --surface:{p['surface']};
    --surface2:{p['surface2']};
    --border:{p['border']};
    --text:{p['text']};
    --text-dim:{p['text-dim']};
    --accent:{p['accent']};
    --accent-bright:{p['accent-bright']};
    --accent-dim:{p['accent-dim']};
    --secondary:{p['secondary']};
    --contrast:{p['contrast']};

    /* Every layout constant gets ONE property. The same bug class has bitten
       this repo twice: a media query moves one hardcoded value and leaves
       three others behind. (CLAUDE.md, "things that have bitten us") */
    --slide-w:1280px;
    --slide-h:720px;
    --pad:44px;
    --bar-h:58px;
    --card-r:14px;
    --bg-wash:0.13;
  }}
  *{{box-sizing:border-box;}}
  html,body{{height:100%;}}
  body{{
    margin:0; background:var(--void); color:var(--text);
    font-family:'Inter',sans-serif; line-height:1.55;
    overflow:hidden;                    /* house rule 1: a deck never scrolls */
  }}

  /* The stage is pinned top-left and centred arithmetically in fitStage().
     Do NOT reintroduce place-items:center on .stage-wrap — an item wider than
     its track aligns to start, not overflowed both sides, which put every
     deck off the right edge below 1280px. */
  .stage-wrap{{position:fixed; inset:0; overflow:hidden;}}
  .stage{{
    position:absolute; left:0; top:0;
    width:var(--slide-w); height:var(--slide-h);
    transform-origin:top left; overflow:hidden;
    background:var(--void);
    box-shadow:0 24px 80px rgba(0,0,0,.45);
  }}

  /* Act artwork, swapped rather than pasted as a box (house rule 5b). */
  .bg-layer{{
    position:absolute; inset:0; z-index:0;
    background-image:var(--act-bg,none); background-size:cover;
    background-position:center; opacity:var(--bg-wash);
    transition:background-image .45s ease, opacity .45s ease;
  }}

  .slide{{
    position:absolute; inset:0; z-index:1; display:none;
    flex-direction:column; padding:var(--pad);
  }}
  .slide.is-active{{display:flex; animation:slide-in .32s ease both;}}
  @keyframes slide-in{{from{{opacity:0; transform:translateY(10px);}}
                       to{{opacity:1; transform:none;}}}}
  @media (prefers-reduced-motion:reduce){{
    .slide.is-active{{animation:none;}}
    .trust-fill{{transition:none;}}
  }}

  .fe-logo{{width:152px; height:auto; display:block;}}
  .fe-logo-mark{{color:var(--logo-mark, var(--accent));}}
  .fe-logo-word{{fill:var(--secondary);}}
  .slide[data-type="cover"] .fe-logo{{width:232px;}}

  /* ── COVER ── */
  .slide[data-type="cover"]{{
    padding:0; justify-content:flex-end;
    background:url('FireShield/hero.jpg') center/cover no-repeat;
  }}
  /* A pseudo-element, not a child: check-lesson.js sums the heights of a
     slide's direct children, so an absolutely-positioned scrim div reads as
     720px of extra stack and the cover "overflows" by exactly one canvas. */
  .slide[data-type="cover"]::before{{
    content:''; position:absolute; inset:0;
    background:linear-gradient(100deg, var(--surface) 4%, transparent 66%);
    opacity:.9;
  }}
  .cover-inner{{
    position:relative; z-index:1; padding:var(--pad);
    display:flex; flex-direction:column; align-items:flex-start;
    justify-content:center; height:100%; max-width:660px; gap:2px;
  }}
  .cover-title{{
    font-family:'Fraunces',serif; font-size:58px; font-weight:700;
    line-height:1.04; letter-spacing:-.015em; color:var(--secondary);
    margin:22px 0 0;
  }}
  .cover-sub{{font-size:18px; color:var(--text-dim); margin-top:14px;
    letter-spacing:.03em; font-weight:600;}}
  .cover-meta{{display:flex; gap:9px; margin-top:24px; flex-wrap:wrap;}}

  /* ── TOP BAR ── */
  .deck-bar{{
    flex:none; height:var(--bar-h); display:flex; align-items:center;
    gap:22px; margin-bottom:18px;
  }}
  .deck-bar .fe-logo{{width:104px;}}
  .trust{{flex:1; min-width:0;}}
  .trust-label{{
    display:flex; justify-content:space-between; font-size:11px;
    text-transform:uppercase; letter-spacing:.1em; font-weight:700;
    color:var(--text-dim); margin-bottom:5px;
  }}
  .trust-track{{
    height:8px; background:var(--void); border:1px solid var(--border);
    border-radius:6px; overflow:hidden;
  }}
  .trust-fill{{height:100%; background:var(--accent); width:50%;
    transition:width .45s cubic-bezier(.4,0,.2,1);}}
  .act-pips{{
    display:flex; gap:14px; margin-top:6px; font-size:10.5px;
    text-transform:uppercase; letter-spacing:.12em; font-weight:700;
    color:var(--text-dim);
  }}
  .act-pips span{{opacity:.32;}}
  .act-pips span.on{{opacity:1; color:var(--accent-bright);}}
  .langbar{{display:flex; align-items:center; gap:8px; flex:none;}}
  .langbar label{{font-size:10.5px; text-transform:uppercase;
    letter-spacing:.1em; font-weight:700; color:var(--text-dim);}}
  .langbar select{{
    font-family:'Inter',sans-serif; font-size:13px; font-weight:600;
    color:var(--text); background:var(--surface);
    border:1.5px solid var(--border); border-radius:8px; padding:5px 9px;
    cursor:pointer;
  }}
  .langbar select:focus{{outline:2px solid var(--accent); outline-offset:1px;}}

  /* ── SCENE BODY ── */
  .body{{flex:1; min-height:0; display:flex; flex-direction:column;}}
  .card{{
    background:var(--surface); border:1px solid var(--border);
    border-radius:var(--card-r); padding:26px 30px; flex:1; min-height:0;
    display:flex; flex-direction:column; justify-content:center;
  }}
  /* A checkpoint reads left, answers right — one screen, no scrolling. */
  .card.two-col{{
    display:grid; grid-template-columns:1.02fr 1fr; gap:30px;
    align-items:center;
  }}
  .col{{min-width:0; display:flex; flex-direction:column;}}
  .tag{{
    font-family:'Fraunces',serif; font-size:12px; text-transform:uppercase;
    letter-spacing:.11em; color:var(--accent-bright); font-weight:700;
    margin-bottom:12px; flex:none;
  }}
  .narrative{{font-size:18.5px; line-height:1.55; margin:0 0 14px;}}
  .narrative i{{color:var(--accent-bright); font-style:italic;}}
  .q-stem{{font-size:19px; font-weight:700; margin:2px 0 14px;
    line-height:1.4;}}

  .choice-btn, .opt{{
    display:block; width:100%; text-align:left; background:var(--surface2);
    border:1.5px solid var(--border); border-radius:10px;
    padding:12px 15px; margin-bottom:9px; font-size:16.5px;
    font-family:'Inter',sans-serif; cursor:pointer; color:var(--text);
    line-height:1.4; transition:border-color .15s, background .15s;
  }}
  .choice-btn{{font-size:17px;}}
  .choice-btn:hover, .opt:hover:not(:disabled){{
    border-color:var(--accent); background:var(--void);
  }}
  .opt:disabled{{cursor:default;}}
  .opt.correct{{border-color:var(--contrast); color:var(--contrast);
    font-weight:700;}}
  .opt.wrong{{border-color:var(--accent-bright); color:var(--accent-bright);
    opacity:.6; text-decoration:line-through;}}

  .feedback{{
    margin-top:10px; padding:12px 14px; border-radius:9px; font-size:15px;
    line-height:1.5; display:none; border-left:4px solid var(--contrast);
    background:var(--surface2);
  }}
  .feedback.show{{display:block;}}

  .btn{{
    align-self:flex-start; margin-top:14px; background:var(--secondary);
    color:var(--surface); border:none; padding:11px 24px; border-radius:24px;
    font-size:15px; font-weight:700; cursor:pointer;
    font-family:'Inter',sans-serif; flex:none;
  }}
  .btn:hover{{background:var(--accent-bright);}}
  .btn.ghost{{background:transparent; color:var(--accent-bright);
    border:1.5px solid var(--border);}}
  .btn.ghost:hover{{background:var(--surface2);}}
  .btn[disabled]{{opacity:.32; pointer-events:none;}}
  .btn-row{{display:flex; gap:10px; align-items:center;}}

  /* ── INTERLUDE / ENDING ── */
  .interlude{{border-left:5px solid var(--accent); justify-content:center;}}
  .interlude h2{{
    font-family:'Fraunces',serif; font-size:30px; line-height:1.2;
    margin:6px 0 14px; color:var(--secondary); max-width:22ch;
  }}
  .interlude .narrative{{max-width:60ch; font-size:19px;}}
  .carry{{
    margin-top:16px; padding-top:12px; border-top:1px solid var(--border);
    font-size:12px; color:var(--text-dim); font-weight:700;
    text-transform:uppercase; letter-spacing:.06em; max-width:40ch;
  }}
  .carry b{{color:var(--accent-bright); font-size:17px;}}

  /* ── ACTIVATION (house rule 6) ── */
  .act-head{{flex:none;}}
  .act-head h2{{font-family:'Fraunces',serif; font-size:26px; margin:0;
    color:var(--secondary);}}
  .chips{{flex:none; margin:10px 0 14px;}}
  .chips-intro{{font-size:11px; color:var(--text-dim); font-weight:700;
    text-transform:uppercase; letter-spacing:.08em; margin-bottom:7px;}}
  .chip{{
    display:inline-block; background:var(--surface2);
    border:1px solid var(--border); border-radius:999px; padding:3px 11px;
    margin:0 5px 5px 0; font-size:13px; color:var(--accent-bright);
    font-weight:600;
  }}
  .tracks{{flex:1; min-height:0; display:grid;
    grid-template-columns:1fr 1fr; gap:26px;}}
  .track{{min-width:0; display:flex; flex-direction:column; min-height:0;}}
  .track h3{{font-family:'Fraunces',serif; font-size:17px; margin:0 0 9px;
    color:var(--secondary); flex:none;}}
  .track ol{{margin:0; padding-left:19px; font-size:15px; line-height:1.5;}}
  .track li{{margin-bottom:9px;}}
  .brief{{margin:0 0 10px; font-size:15px; line-height:1.5;}}
  textarea{{
    flex:1; min-height:0; width:100%; padding:12px; border-radius:9px;
    border:1.5px solid var(--border); background:var(--surface2);
    color:var(--text); font-family:'Inter',sans-serif; font-size:15px;
    line-height:1.55; resize:none;
  }}
  textarea:focus{{outline:2px solid var(--accent); outline-offset:1px;}}
  .writing-foot{{display:flex; align-items:center; gap:12px; margin-top:8px;
    flex:none;}}
  .writing-foot .btn{{margin-top:0;}}
  .counter{{font-size:13px; color:var(--text-dim); font-weight:700;}}
  .counter.ok{{color:var(--contrast);}}

  /* A textarea's value does not print, so the PDF gets a mirror of it. */
  .print-mirror{{display:none;}}
  @media print{{
    body{{overflow:visible;}}
    .stage-wrap{{position:static; display:block;}}
    .stage{{position:static; transform:none !important;
      width:1280px; height:auto; overflow:visible; box-shadow:none;}}
    .slide{{position:static; display:flex !important; page-break-after:always;
      height:720px;}}
    .bg-layer,.deck-bar,.btn,.langbar{{display:none !important;}}
    .print-mirror{{display:block; white-space:pre-wrap; font-size:14px;}}
    textarea{{display:none;}}
  }}
</style>
</head>
<body>

<div class="stage-wrap">
<div class="stage" id="stage">
  <div class="bg-layer" id="bgLayer"></div>

  <!-- 0 — cover: landscape hero, stacked lockup, title over it (rule 2) -->
  <section class="slide" data-type="cover">
    <div class="cover-inner">
      {logo}
      <h1 class="cover-title">{title}</h1>
      <p class="cover-sub" data-i18n="kicker">{I18N['en']['kicker']}</p>
      <div class="cover-meta">
        <span class="chip">B2</span>
        <span class="chip">Forbes Membranes</span>
        <span class="chip">3 acts</span>
      </div>
      <button class="btn" id="coverBtn" data-i18n="btnBegin">{I18N['en']['btnBegin']}</button>
    </div>
  </section>

  <!-- 1 — briefing -->
  <section class="slide" data-type="teach">
    <div class="deck-bar">
      {logo}
      <div class="trust"></div>
      <div class="langbar">
        <label for="langSel" data-i18n="langLabel">{I18N['en']['langLabel']}</label>
        <select id="langSel" aria-label="Language"></select>
      </div>
    </div>
    <div class="body"><div class="card">
      <div class="tag" data-i18n="briefing">{I18N['en']['briefing']}</div>
      <div class="narrative">
        {intro_ps}
      </div>
      <button class="btn" id="startBtn" data-i18n="btnStart">{I18N['en']['btnStart']}</button>
    </div></div>
  </section>

  <!-- 2 — the roleplay itself; the engine renders one scene at a time here -->
  <section class="slide" data-type="scene">
    <div class="deck-bar">
      {logo}
      <div class="trust">
        <div class="trust-label">
          <span data-i18n="trustLabel">{I18N['en']['trustLabel']}</span>
          <span id="trustNum">50</span>
        </div>
        <div class="trust-track"><div class="trust-fill" id="trustFill"></div></div>
        <div class="act-pips" id="actPips">
          <span data-act="1">I &middot; Manchester</span>
          <span data-act="2">II &middot; Leeds</span>
          <span data-act="3">III &middot; Dublin</span>
        </div>
      </div>
    </div>
    <div class="body" id="gameArea"></div>
  </section>

  <!-- 3 — activation: speaking and writing, both live (rule 6) -->
  <section class="slide" data-type="activate">
    <div class="act-head">
      <h2 data-i18n="actHeading">{I18N['en']['actHeading']}</h2>
    </div>
    <div class="chips">
      <div class="chips-intro" data-i18n="actChips">{I18N['en']['actChips']}</div>
      {chips}
    </div>
    <div class="tracks">
      <div class="track">
        <h3 data-i18n="actSpeak">{I18N['en']['actSpeak']}</h3>
        <ol>
          {speak}
        </ol>
      </div>
      <div class="track">
        <h3 data-i18n="actWrite">{I18N['en']['actWrite']}</h3>
        <p class="brief" data-i18n="writeBrief">{ACTIVATION['writing_brief']['en']}</p>
        <textarea id="writing" aria-label="Writing task"></textarea>
        <div class="print-mirror" id="writingMirror"></div>
        <div class="writing-foot">
          <span class="counter" id="counter">0 {I18N['en']['actWords']}</span>
          <button class="btn ghost" id="copyBtn" data-i18n="btnCopy">{I18N['en']['btnCopy']}</button>
        </div>
      </div>
    </div>
  </section>

</div>
</div>

<script>
const SCENES = {js_scenes(lang)};
const UI_I18N = {js_i18n()};
const BG = {{
  cover:"FireShield/bg-intro.jpg", act1:"FireShield/bg-act1.jpg",
  act2:"FireShield/bg-act2.jpg",   act3:"FireShield/bg-act3.jpg",
  end:"FireShield/bg-end.jpg"
}};

/* ── i18n ──
   §8: offer a language only if it defines every key English defines. A
   half-done pass stays in the table and is simply not listed. */
const LANG_NAMES = {{en:"English", de:"Deutsch", es:"Espa\\u00f1ol"}};
let LANG = "en";
function T(k){{
  const row = UI_I18N[LANG] || {{}};
  return (row[k] !== undefined ? row[k] : UI_I18N.en[k]);
}}
function completeLangs(){{
  const need = Object.keys(UI_I18N.en).length;
  return Object.keys(UI_I18N).filter(l => Object.keys(UI_I18N[l]).length >= need);
}}

/* ── Stage ── */
const stage = document.getElementById("stage");
const slides = [...document.querySelectorAll(".slide")];
let idx = 0;

function fitStage(){{
  const s = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
  // Centre explicitly. Relying on the wrapper to centre an oversized child is
  // what put the stage off-screen on every viewport under 1280px wide.
  const x = (window.innerWidth  - 1280 * s) / 2;
  const y = (window.innerHeight -  720 * s) / 2;
  stage.style.transform = `translate(${{x}}px, ${{y}}px) scale(${{s}})`;
}}
addEventListener("resize", fitStage);
fitStage();

function show(n){{
  idx = Math.max(0, Math.min(slides.length - 1, n));
  slides.forEach((s, i) => s.classList.toggle("is-active", i === idx));
}}

/* ── Scoring ──
   Trust is EARNED against trust AVAILABLE, per act and overall. An absolute
   running total saturates at 100 and stops discriminating — 84% of simulated
   playthroughs reached the best ending under that scheme, and the worst was
   unreachable. A ratio cannot saturate.

   The bar the learner watches is the same number, so the meter can never
   disagree with the ending it leads to. PRIOR smooths the first few clicks. */
const PRIOR = 20;
let log = [], current = "a1_open", missed = false;

function record(act, delta, max){{ log.push({{act:act, delta:delta, max:max}}); }}
function totals(act){{
  const rows = act ? log.filter(r => r.act === act) : log;
  let got = 0, max = 0;
  for (const r of rows){{ got += r.delta; max += r.max; }}
  return {{got: got, max: max}};
}}
function ratio(act){{
  const t = totals(act);
  return t.max <= 0 ? 0 : Math.max(0, Math.min(1, t.got / t.max));
}}
function meter(){{
  const t = totals(null);
  const v = (t.got + PRIOR / 2) / (t.max + PRIOR);
  return Math.round(100 * Math.max(0, Math.min(1, v)));
}}

/* Fisher-Yates. The authored options put the key first in 19 of 20
   checkpoints — inherited from the three originals — so a learner could score
   full marks by always clicking the top button without reading. Shuffling at
   render time is what makes the key move. */
function shuffled(options, correct){{
  const a = options.map((text, i) => ({{text: text, key: i === correct}}));
  for (let i = a.length - 1; i > 0; i--){{
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }}
  return a;
}}

const area = document.getElementById("gameArea");
const bgLayer = document.getElementById("bgLayer");

function paint(){{
  const trust = meter();
  document.getElementById("trustFill").style.width = trust + "%";
  document.getElementById("trustNum").textContent = trust;
  const act = SCENES[current] ? SCENES[current].act : 1;
  document.querySelectorAll("#actPips span").forEach(s => {{
    s.classList.toggle("on", Number(s.dataset.act) === act);
  }});
  const bg = SCENES[current] && SCENES[current].bg;
  if (bg && BG[bg]) bgLayer.style.setProperty("--act-bg", `url('${{BG[bg]}}')`);
}}

function startGame(){{
  log = []; current = "a1_open"; missed = false;
  show(2); paint(); render();
}}
function go(next){{ current = next; paint(); render(); }}

function render(){{
  const s = SCENES[current];

  if (s.type === "story"){{
    area.innerHTML = `<div class="card">
      <div class="tag">${{T(s.tagKey)}}</div>
      <p class="narrative">${{s.narrative}}</p>
      <div id="choiceBox"></div></div>`;
    const box = document.getElementById("choiceBox");
    const best = Math.max.apply(null, s.choices.map(x => x.trust));
    s.choices.forEach(c => {{
      const b = document.createElement("button");
      b.className = "choice-btn"; b.innerHTML = c.label;
      b.addEventListener("click", () => {{ record(s.act, c.trust, best); go(c.next); }});
      box.appendChild(b);
    }});
  }}

  else if (s.type === "checkpoint"){{
    missed = false;
    area.innerHTML = `<div class="card two-col">
      <div class="col">
        <div class="tag">${{T(s.tagKey)}}</div>
        <p class="narrative">${{s.narrative}}</p>
        <p class="q-stem">${{s.question}}</p>
      </div>
      <div class="col">
        <div id="optsBox"></div>
        <div class="feedback" id="feedbackBox"></div>
        <button class="btn" id="nextBtn" disabled>${{T("btnContinue")}}</button>
      </div></div>`;
    const box = document.getElementById("optsBox");
    shuffled(s.options, s.correct).forEach(o => {{
      const b = document.createElement("button");
      b.className = "opt"; b.textContent = o.text;
      b.addEventListener("click", () => {{
        if (o.key){{
          document.querySelectorAll("#optsBox .opt").forEach(x => x.disabled = true);
          b.classList.add("correct");
          /* First attempt only — a retry earns the explanation, not the trust. */
          record(s.act, missed ? 0 : s.trustOnCorrect, s.trustOnCorrect);
          paint();
          const fb = document.getElementById("feedbackBox");
          fb.innerHTML = s.explain; fb.classList.add("show");
          const nb = document.getElementById("nextBtn");
          nb.disabled = false;
          nb.addEventListener("click", () => go(s.next));
        }} else {{
          missed = true;
          b.classList.add("wrong"); b.disabled = true;
        }}
      }});
      box.appendChild(b);
    }});
  }}

  else if (s.type === "interlude"){{
    const r = s.final ? ratio(null) : ratio(s.act);
    const tier = s.tiers.find(t => r >= t.min) || s.tiers[s.tiers.length - 1];
    area.innerHTML = `<div class="card interlude">
      <div class="tag">${{T(s.tagKey)}}</div>
      <h2>${{tier.title}}</h2>
      <p class="narrative">${{tier.body}}</p>
      <div class="carry">${{T("carry")}}: <b>${{meter()}}</b></div>
      <button class="btn" id="nextBtn">${{s.final ? T("btnActivate") : T("btnNextAct")}}</button>
      </div>`;
    document.getElementById("nextBtn").addEventListener("click", () => {{
      if (s.final){{
        bgLayer.style.setProperty("--act-bg", `url('${{BG.end}}')`);
        show(3); return;
      }}
      go(s.next);
    }});
  }}

  else if (s.type === "ending"){{
    area.innerHTML = `<div class="card interlude">
      <div class="tag">${{T(s.tagKey)}}</div>
      <h2>${{s.title}}</h2>
      <p class="narrative">${{s.body}}</p>
      <div class="btn-row">
        ${{s.rewind ? `<button class="btn" id="rewindBtn">${{T("btnRewind")}}</button>` : ""}}
        <button class="btn ghost" id="restartBtn">${{T("btnRestart")}}</button>
      </div></div>`;
    if (s.rewind){{
      document.getElementById("rewindBtn").addEventListener("click", () => {{
        log.pop();               /* un-take it; the meter follows the log */
        go(s.rewind);
      }});
    }}
    document.getElementById("restartBtn").addEventListener("click", startGame);
  }}
}}

/* ── Activation ── */
const ta = document.getElementById("writing");
const counter = document.getElementById("counter");
const mirror = document.getElementById("writingMirror");
function countWords(){{
  const n = ta.value.trim() ? ta.value.trim().split(/\\s+/).length : 0;
  counter.textContent = n + " " + T("actWords");
  counter.classList.toggle("ok", n >= 150 && n <= 250);
  mirror.textContent = ta.value;
}}
ta.addEventListener("input", countWords);
document.getElementById("copyBtn").addEventListener("click", async () => {{
  try {{
    await navigator.clipboard.writeText(ta.value);
    const b = document.getElementById("copyBtn");
    b.textContent = T("btnCopied");
    setTimeout(() => b.textContent = T("btnCopy"), 1400);
  }} catch (e) {{ ta.select(); }}
}});

function applyI18n(){{
  document.documentElement.lang = LANG;
  document.querySelectorAll("[data-i18n]").forEach(el => {{
    el.innerHTML = T(el.dataset.i18n);
  }});
  countWords();
  if (idx === 2 && area.children.length) render();
}}

(function initLang(){{
  const sel = document.getElementById("langSel");
  const langs = completeLangs();
  if (langs.length < 2){{ sel.closest(".langbar").hidden = true; return; }}
  langs.forEach(l => {{
    const o = document.createElement("option");
    o.value = l; o.textContent = LANG_NAMES[l] || l;
    sel.appendChild(o);
  }});
  sel.value = LANG;
  sel.addEventListener("change", () => {{ LANG = sel.value; applyI18n(); }});
}})();

document.getElementById("coverBtn").addEventListener("click", () => show(1));
document.getElementById("startBtn").addEventListener("click", startGame);
bgLayer.style.setProperty("--act-bg", `url('${{BG.cover}}')`);
show(0);
</script>

</body>
</html>
"""


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    path = os.path.join(root, OUT)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(build("en"))
    n_scenes = len(SCENES)
    print(f"wrote {OUT}  ({n_scenes} nodes, langs={','.join(LANGS)})")
