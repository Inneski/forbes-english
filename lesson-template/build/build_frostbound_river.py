#!/usr/bin/env python3
"""Frostbound: The River Remembers — Present Simple frozen-north RPG (A1-A2).

    python3 lesson-template/build/build_frostbound_river.py

Rebuilds block-camp/frostbound-river-rpg.html from
lesson-template/build/rpg/frostbound-river-rpg/data.json — the text of the
standalone export Innes sent on 2026-09-14, pulled out by
rpg/extract_scene_array.py.

**A fifth kind of export** (rpg/README.md §2). The Oz kind turned inside out:
no `window.*_GAME_DATA` and no `images` map, just a flat `const SCENES=[...]`
array where every scene carries its own picture inline on an `image` key. It
does carry two things no earlier export did — a per-scene `object` naming the
glowing thing the plate was drawn around, and a `target` giving that object's
centre in picture percent — so the hotspot hunt started from the author's own
answer rather than a guess. Every box below was still read off a gridded
contact sheet; the widths are this file's work, because no export knows how
wide a translated panel gets.

What the export did not have, and this builder writes: the rules briefing, the
nine languages, and the panel width on every scene. What it had and keeps: 5
points a question, 2-or-4 points a story choice, and three endings chosen by
score alone — 64+, 40-63, below 40.

**The stems on five questions were rewritten, and that is the point of the
rebuild.** Innes asked whether a game can run on the present simple alone when
the pictures all show a single moment. It can, and this export's distractors
made it safe by accident: not one of them is a well-formed present continuous,
so a learner who knows that tense could never pick it. The risk was in the
stems. The briefing says the present simple is for habits, repeated actions and
facts, and then five questions asked about a one-off action happening in front
of the reader — "The ice ___ under our boots", where any competent speaker says
IS CRACKING. The rule was taught and then broken by its own answer key. Each of
the five now carries a frequency or generalising context (ALWAYS, BEFORE EVERY
CROSSING, IN AN EMERGENCY) so the present simple is the only natural reading,
and the grammar target of each — third-person -S, consonant + Y to -IES, -SH to
-ES, the plural base form — is untouched. They are marked REWRITTEN below.

The note on the briefing names the other half of the seam: the story itself is
narrated in the present simple, the way a film synopsis is. A learner who meets
present simple vs continuous later should not find this lesson contradicting it.

**Nine distractors were replaced too.** The export leaned on aux+base forms no
learner produces — "is hear", "is whisper", "is reveal" — which reduce a
four-option item to a two-option one. Each is now a real A1 error: the base form
with a singular subject, a doubled marker ("does hears"), a bare -ING with no
auxiliary, an over-applied -ES spelling, or DO/DOES against a plural subject.
The key is dealt across all four slots (5/4/3/5 of 17) and is never the longest
option; `_check_answer_key` enforces both.

Three engine additions this export needed, all generic and in rpg/rpg.py
(README §9): `bands` — an ending picked by score alone; `points` on a route;
and the fourth answer key, since the engine bound only 1-3 and the key here is
in slot 4 on five of the twelve questions.

Pictures: block-camp/frostbound-river-rpg/NN_id.webp, 1536x864 (16:9), as
exported — so the spec passes img_w/img_h.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'frostbound-river-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = {s['id']: s for s in json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))}
LANGS = rpg.NINE

# ── hotspots: [cx, cy, w, h] in % of the 1536x864 picture, then panel side,
# vertical anchor, optional panel width %.
#
# The export's `target` centre was accurate on all 26 plates and is kept; the
# sizes and every width are read off the contact sheets. A panel is 46% of the
# frame by default and grows 8 points the moment a gloss language is on, so a
# left panel reaches x=56 in English and x=64 translated. Objects between 56
# and 64 are the reason so many scenes below carry a narrower width: this art
# puts its characters centre-right and its lit object further right still.
HOT = {
    'intro':        ([76, 49, 13, 26], 'left',  'center'),       # the ice crystal on its pedestal
    'rules':        ([78, 70, 22, 18], 'left',  'center', 56),   # the open field guide; wide, five cards
    'voice':        ([90, 63,  9, 20], 'left',  'center', 40),   # the ice bell by the cracked window
    'crossroads':   ([84, 65,  9, 18], 'left',  'center', 52),   # the compass medallion on the trail marker
    'ridge':        ([22, 65, 18, 26], 'right', 'center'),       # the brass rope anchor driven into the ice
    'forest':       ([81, 65, 10, 22], 'left',  'center'),       # the leaf stone
    'wind':         ([76, 76, 12, 18], 'left',  'center', 42),   # the stone spiral marker
    'spirit_choice':([77, 75, 11, 18], 'left',  'center', 52),   # the blue ember
    'fire':         ([22, 58, 15, 18], 'right', 'center'),       # the little fire spirit
    'giants':       ([76, 75, 18, 16], 'left',  'center'),       # the water-filled footprint
    'camp':         ([73, 55,  9, 14], 'left',  'center'),       # the family pendant in their hands
    'truth_choice': ([93, 50, 11, 20], 'left',  'center', 52),   # the diamond compass in the pillar
    'sea':          ([29, 48, 11, 18], 'right', 'center'),       # the ice rein at the horse's chest
    'memory':       ([75, 53, 13, 26], 'left',  'center', 42),   # the memory crystal
    'records':      ([73, 73, 14, 12], 'left',  'center'),       # the brass brush on the ledge
    'oath':         ([21, 73, 11, 16], 'right', 'center'),       # the broken silver seal
    'truth':        ([67, 60, 16, 28], 'left',  'center', 42),   # the cracked floodgate wheel
    'dam_choice':   ([86, 66, 15, 14], 'left',  'center', 52),   # the signal horn on the parapet
    'rescue':       ([10, 23, 17, 30], 'right', 'center'),       # the warning bell
    'break_dam':    ([86, 72, 14, 12], 'left',  'center'),       # the gate key on the safe ledge
    'wave':         ([86, 70, 12, 18], 'left',  'center', 42),   # the waypoint stone
    # The one scene whose object and whose faces are on the same side. Eira and
    # Lina stand centre (x 58-80) and the lantern is at x 23, so a right panel
    # covers the sisters and a left panel covers the lantern. The rule that
    # binds is the object's (README §3), so the panel goes right and the ice
    # shield — the action the scene is about — stays in view on the left.
    'bridge':       ([23, 61, 12, 18], 'right', 'center'),       # the bridge lantern
    'peace':        ([82, 69, 12, 18], 'left',  'center', 42),   # the blue flower through the snow
    'guardian':     ([84, 64, 13, 22], 'left',  'center', 42),   # the joined-diamond crest
    'rebuild':      ([83, 74, 16, 14], 'left',  'center', 42),   # the builder's hammer on the toolbox
    'rekindle':     ([76, 64, 12, 20], 'left',  'center', 42),   # the hope lantern on the rock
}

# ── the twelve-question path: options, key and the line under every answer.
# `stem` overrides the export's question where it was rewritten (see docstring).
# Options are the English being taught and are never glossed (HOUSE-STYLE §8).
Q = {
    'voice': dict(
        opts=['hearing', 'hears', 'hear', 'does hears'], answer=1,
        fb='"Every night" is a repeated action, so the present simple. Eira is "she": add -S. '
           'EIRA + HEARS. "Does hears" marks the verb twice.'),
    'ridge': dict(   # REWRITTEN. Was "The ice ___ under our boots" — one crack, happening now.
        stem='Bram ___ the rope before every crossing.',
        opts=['check', 'checking', 'checks', 'checkes'], answer=2,
        fb='"Before every crossing" is a habit. Bram is "he": BRAM + CHECKS. '
           '-ES goes after -S, -SH, -CH, -X and -O, not after "check".'),
    'forest': dict(
        opts=['whisper', 'whispers', 'whispering', 'does whisper'], answer=0,
        fb='"The trees" is "they", so the verb takes no -S: THE TREES + WHISPER. '
           'DOES belongs with "he", "she" or "it".'),
    'wind': dict(  # REWRITTEN. "show THEM the way" asked about the one moment in the
                   # plate; "show TRAVELLERS the way" asks what the spirit does for
                   # anyone, which is the only reading the present simple wants.
        stem='___ the wind spirit show travellers the way?',
        opts=['Is', 'Are', 'Do', 'Does'], answer=3,
        fb='A present simple question is DO / DOES + SUBJECT + BASE VERB. '
           '"The wind spirit" is "it": DOES + THE WIND SPIRIT + SHOW.'),
    'fire': dict(
        opts=["don't", "doesn't", "isn't", "aren't"], answer=1,
        fb='The negative is DOESN\'T + BASE VERB with "he", "she" or "it". '
           'Nim is "he": NIM + DOESN\'T + TOUCH. "Isn\'t" would need no verb after it.'),
    'giants': dict(
        opts=["don't", "isn't", 'not', "doesn't"], answer=0,
        fb='"The giants" is "they", so DON\'T + BASE VERB: THE GIANTS + DON\'T + SLEEP. '
           'English needs DO or DOES in front of "not" here.'),
    'camp': dict(  # REWRITTEN. Was "Eira and Lina ___ a memory of their mother" — the
                   # sixth stem of the same defect, and the one the first pass missed:
                   # SHARE was read as stative and it is not, so the picture's ARE
                   # SHARING was the natural answer. Innes caught it on the live page
                   # and supplied the fix. A shared mother is permanent, so the
                   # continuous is not merely unlikely here, it is ungrammatical.
        stem='Eira and Lina ___ the same mother.',
        opts=['sharing', 'does share', 'shares', 'share'], answer=3,
        fb='Two people make "they": EIRA AND LINA + SHARE. A permanent fact takes the '
           'present simple. No -S and no DOES with a plural subject.'),
    'sea': dict(
        opts=['Does', 'Do', 'Is', 'Are'], answer=0,
        fb='Eira is "she", so the question word is DOES: DOES + EIRA + NEED. '
           'The verb after DOES stays in the base form.'),
    'memory': dict(
        opts=['remembers', 'remembering', 'do remember', 'remember'], answer=0,
        fb='"The river" is one thing — "it": THE RIVER + REMEMBERS. '
           'DO goes with "I", "you", "we" and "they".'),
    'records': dict(  # REWRITTEN. Was "Lina ___ the carved pictures carefully" — happening in the plate.
        stem='Lina always ___ old carvings carefully.',
        opts=['studys', 'studying', 'study', 'studies'], answer=3,
        fb='"Always" is a habit, so the present simple. After a CONSONANT + Y, '
           'the Y becomes -IES: STUDY becomes STUDIES.'),
    'oath': dict(
        opts=['does reveals', 'reveals', 'reveal', 'revealing'], answer=2,
        fb='"The old records" is plural — "they": THE RECORDS + REVEAL. '
           'No -S, and never DOES + a verb that already has -S.'),
    'truth': dict(
        opts=['block', 'blocks', 'blocking', 'do block'], answer=1,
        fb='"The dam" is one thing — "it": THE DAM + BLOCKS. '
           'A fact that stays true takes the present simple.'),
    'rescue': dict(  # REWRITTEN. Was "Bram ___ supplies to the safe path" — one trip, in the plate.
        stem='In an emergency, Bram ___ supplies to high ground.',
        opts=['carrys', 'carrying', 'carry', 'carries'], answer=3,
        fb='"In an emergency" describes what always happens. Bram is "he", and '
           'after a CONSONANT + Y the Y becomes -IES: CARRY becomes CARRIES.'),
    'break_dam': dict(
        opts=["aren't", "don't", "doesn't", "isn't"], answer=2,
        fb='Lina is "she": LINA + DOESN\'T + NEED. '
           '"Need" is the base form — the -S has moved onto DOESN\'T.'),
    'wave': dict(   # REWRITTEN. Was "The water ___ toward Northmere" — one wave, right now.
        stem='A free river always ___ toward the sea.',
        opts=['rush', 'rushes', 'rushing', 'do rush'], answer=1,
        fb='"Always" plus a general truth takes the present simple. '
           'After -SH the ending is -ES: RUSH becomes RUSHES.'),
    'bridge': dict(  # REWRITTEN. Was "Eira and Lina ___ together to protect the town".
        stem='Eira and Lina always ___ together.',
        opts=['work', 'working', 'does work', 'works'], answer=0,
        fb='Two people make "they", so the base verb: EIRA AND LINA + WORK. '
           'The -S form belongs to one person.'),
    'peace': dict(
        opts=["doesn't", "don't", "isn't", "aren't"], answer=3,
        fb='BE is the exception: it needs no DO or DOES. '
           '"The spirits" is "they": THE SPIRITS + AREN\'T + angry.'),
}

# ── the four story choices. `desc` is the export's own consequence line, moved
# in front of the choice: a route card exists to tell the player what a road
# costs before they take it, and a hidden 4-against-2 is a trap, not a lesson.
ROUTES = {
    'crossroads': [
        ('Take the ice ridge together', 'You check the rope and keep the group together.', 'ridge', 'RIDGE', 4),
        ('Enter the forest trail', 'The shortcut saves time, but the mist hides the path.', 'forest', 'FOREST', 2),
    ],
    'spirit_choice': [
        ('Calm the frightened fire spirit', "A gentle approach earns the spirit's trust.", 'fire', 'FIRE', 4),
        ('Follow the stone giants', 'Their footsteps reveal a route to the river.', 'giants', 'GIANTS', 2),
    ],
    'truth_choice': [
        ('Cross the sea with Eira', 'You brave the waves to follow the voice.', 'sea', 'SEA', 2),
        ('Study the river records with Lina', 'You gather evidence before acting.', 'records', 'RECORDS', 4),
    ],
    'dam_choice': [
        ('Warn the town before breaking the dam', 'Your warning gives families time to reach high ground.',
         'rescue', 'WARNING', 4),
        ('Break the dam immediately', 'The forest is freed quickly; Eira must face a stronger emergency.',
         'break_dam', 'BREAK', 2),
    ],
}

# where each question goes next; the export routed right and wrong answers to
# the same scene and the chance counter was never the penalty here (README §9)
NEXT = {'voice': 'crossroads', 'ridge': 'wind', 'forest': 'wind', 'wind': 'spirit_choice',
        'fire': 'camp', 'giants': 'camp', 'camp': 'truth_choice', 'sea': 'memory',
        'memory': 'truth', 'records': 'oath', 'oath': 'truth', 'truth': 'dam_choice',
        'rescue': 'wave', 'break_dam': 'wave', 'wave': 'bridge', 'bridge': 'peace',
        'peace': 'resolve'}


# ── the export closed two endings on "clear commands" and "practise your
# commands", which it inherited from a spell-casting frame. Nothing in this
# lesson is an imperative; the last line of a lesson should name what the
# learner actually did.
ENDING_STORY = {
    'guardian': 'The flood turns safely into the empty fjord. Northmere stands, the forest is free, '
                'and the sisters become a bridge between two peoples. Your careful choices and clear '
                'grammar protect both homes.',
    'rekindle': 'The spirits lead the travellers to safety. The river is free, but the town needs a '
                'long recovery. Eira and Lina begin again, one careful step at a time. Practise the '
                '-S forms and return for a stronger ending.',
}


def T(en):
    return {'en': en}


# ── the rules briefing. Nothing in the export; this is the lesson.
# A card carrying a PATTERN keeps its English in every gloss (the engine hides a
# translation identical to its English); a card carrying a MEANING is glossed.
RULES_SCENE = {
    'kind': 'rules', 'img': DATA['rules']['image'],
    'k': T('YOUR FIELD GUIDE · HOW THE GRAMMAR WORKS'),
    'title': T('WORDS HAVE POWER'),
    # No story line. Five cards, a note and a button already reach the foot of
    # the panel, and the Spanish briefing scrolled 95px (check-rpg-panels.js
    # `tight`); the lead-in said what the note says, so it is the line to lose.
    'rules': [
        {'name': T('I · YOU · WE · THEY'), 'form': T('The base verb, with no ending. · The spirits sleep.')},
        {'name': T('HE · SHE · IT'), 'form': T('Add -S. · Eira hears the voice.')},
        {'name': T('SPELLING OF THE -S FORM'), 'form': T('rush → rushes · study → studies · go → goes')},
        {'name': T('NEGATIVE'), 'form': T("DON'T / DOESN'T + BASE VERB · Nim doesn't touch the flames.")},
        {'name': T('QUESTION'), 'form': T('DO / DOES + SUBJECT + BASE VERB · Does the spirit show the way?')},
    ],
    # The briefing is the longest panel in the lesson and the Spanish ran 129px
    # past it (check-rpg-panels.js). Cut here rather than shrinking the type or
    # widening past 56% — rpg/README.md §1.
    'note': T('Habits, repeated actions and facts — look for ALWAYS, EVERY NIGHT or NEVER. '
              'The story is told in the present simple too, the way a film is described: '
              '"She opens the window. She hears a voice."'),
    'button': T('Follow the voice'),
    'next': 'voice',
}

LABELS = {
    # there is no chance counter in this game: a wrong answer costs the points
    # and nothing else, so the default "-1 CHANCE" would name a badge that the
    # HUD does not show
    'wrong': T('NO POINTS'),
    'progress': T('CHALLENGES'),
    'help': T('click the glowing object or ENTER to read · ESC hide · 1-4 choose · '
              'L language · S sound · F fullscreen'),
}


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def build():
    intro = DATA['intro']
    scenes = {
        'intro': place('intro', {
            'kind': 'intro', 'img': intro['image'],
            'k': T('FROSTBOUND · A PRESENT SIMPLE RPG'),
            'title': T('THE RIVER REMEMBERS'),
            'story': T(intro['story']),
            'rules': [T('PRESENT SIMPLE'), T('12 CHALLENGES'), T('3 ENDINGS')],
            'start': T('Begin the journey'),
            'small': T('12 grammar challenges · 4 branching choices · 3 endings'),
            'next': 'rules'}),
        'rules': place('rules', dict(RULES_SCENE)),
    }

    for sid, s in DATA.items():
        if sid in ('intro', 'rules'):
            continue
        base = {'img': s['image'], 'k': T(s['chapter']), 'title': T(s['title']), 'story': T(s['story'])}
        if s['kind'] == 'quiz':
            q = Q[sid]
            base.update({
                'kind': 'question',
                'prompt': T(q.get('stem', s['question'])),
                'opts': [{'en': o} for o in q['opts']],
                'answer': q['answer'], 'points': 5,
                'fb': T(q['fb']), 'next': NEXT[sid]})
        elif s['kind'] == 'choice':
            base['kind'] = 'choice'
            base['routes'] = [{'name': T(n), 'desc': T(d), 'target': t, 'route': r, 'points': p}
                              for n, d, t, r, p in ROUTES[sid]]
        else:                                  # the three endings
            base['kind'] = 'ending'
            if sid in ENDING_STORY:
                base['story'] = T(ENDING_STORY[sid])
        scenes[sid] = place(sid, base)

    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'Frostbound: The River Remembers — Present Simple Frozen North RPG (A1-A2)',
        'description': 'An interactive A1-A2 English lesson from Forbes English: Frostbound: '
                       'The River Remembers — Present Simple Frozen North RPG (A1-A2).',
        'langs': LANGS,
        # camp 1, Present Simple, on the Block Camp route map — and the one
        # camp colour that was already this lesson's palette
        'accent': '#7A93B5', 'accent_ink': '#06111f',
        'deep': '#061024', 'panel': 'rgba(6,16,36,.88)',
        'labels': LABELS,
        'start': 'intro', 'scenes': scenes,
        # `bands` decides the ending; these are the engine's fallback keys and
        # are never reached while bands are set
        'endings': {'master': 'guardian', 'complete': 'rebuild',
                    'missing': 'rebuild', 'failed': 'rekindle'},
        'bands': [(64, 'guardian'), (40, 'rebuild'), (0, 'rekindle')],
        # 12 questions x 5 + 4 choices x up to 4 = 76, and the export's own
        # thresholds, kept exactly
        'max': 76, 'points': 5, 'tiles': 0, 'chances': 0, 'complete_score': 40,
        'total': 12,
        'img_w': 1536, 'img_h': 864,
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
