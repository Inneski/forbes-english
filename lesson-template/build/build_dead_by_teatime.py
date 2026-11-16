# -*- coding: utf-8 -*-
"""Dead by Teatime (B1) — a zombie-comedy RPG, built like The Scarlet Star.

Innes, 2026-11-15: "Do a similar story to Shaun of the Dead RPG", with
present modals of obligation and advice (MUST, MUSTN'T, HAVE TO, DON'T HAVE
TO, SHOULD) and relative clauses, art by ChatGPT. Then, on a first build in
house style 1: "You should copy Scarlet Star vibe not house style". So this
is the Scarlet Star machine and look, as `build_verdict.py` builds it: a
branch-flow deck on the house template (nodes, `data-goto`, a ledger in the
deck bar, gated endings), each slide on its own full-bleed plate.

Neither grammar strand had a story deck of its own: the inventory taken that
day found conditionals in six stories and reported speech in four, and these
two in none.

It is an ORIGINAL story in the genre, not a retelling: its own town
(Lowfield), its own people (Gaz, Nan and her bat Geoffrey, Priya the
paramedic, Colin and his survival manual, Mr Bell's corner shop), its own
refuge (Lowfield Lanes, the bowling alley you have the keys to) and its own
jokes. No film title, character, place or scene is borrowed.

  trunk     Act I     q01–q04                         the alert, the flat
  hub       Act II    stops A (q05–q08), B (q09–q12), C (q13–q16) in any
                      order; each checkpoint carries its stop (data-clue),
                      and Lowfield Lanes opens only with all three
  trunk     Act III   q17 q18                         the bowling alley
  fork      Act IV    back yard q19  |  front doors q20
  trunk               q21–q25                         the long night
  trunk     Act V     q26, then the decision
  endings   the bus (needs Nerve left) | wait for the army | run alone
  25 MC on every route: 12 modals and 12 relative clauses in the trunk and
  the stops, and the fork's arm is one of each (q19 relatives, q20 modals),
  so every route is 13/12 one way or the other (the build asserts it).

**Action.** Innes, 2026-11-16, on the first draft: "Why is there zero zombie
fighting in this?" It had none: the group hid, barricaded and kept quiet.
Six scenes are fights now (the stairs, the ambulance, the till, the glass
giving way at 2 a.m., the claw machine, the car park at dawn): slapstick
knockdowns with a cricket bat, bowling balls, a newspaper, never gore. The
grammar items did not move, except q10 (WHOSE) and q21 (THAT), rewritten
with their scenes. ACTION lists the six plates re-briefed for them.

**Art.** ChatGPT/Codex, a detailed graphic-novel look (Innes chose it over
the first brief's flat print), each plate
painted with its subject on the RIGHT and the left half empty for the text
(the Reasonable Doubt lesson: text must never land on a face). Briefed in
docs/CHATGPT-DEAD-BY-TEATIME-ART-BRIEF.md; drop folder incoming/dead-by-teatime/;
plates go through prep-artwork.py to DeadByTeatime/<slot>.jpg. Until every
plate in PLATES is there, this writes the gitignored preview
`_dead-by-teatime-rpg.html` on Scarlet Star stand-ins with the Scarlet Star
palette. With every plate in, it stops and asks for PALETTE_LIVE from
`extract-palette.py DeadByTeatime/hero.jpg`, then writes `dead-by-teatime-rpg.html`.

Run from the repo root:  py lesson-template/build/build_dead_by_teatime.py
"""
import importlib
import itertools
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D  # noqa: E402
import i18n_dead_by_teatime as I  # noqa: E402
from chrome_i18n import CHROME  # noqa: E402

TPL = 'lesson-template/lesson-template.html'
OUT = 'dead-by-teatime-rpg.html'
PREVIEW = '_dead-by-teatime-rpg.html'
F = 'DeadByTeatime'
DROP = os.path.join('incoming', 'dead-by-teatime')
TITLE = 'Dead by Teatime (B1) | Forbes English'
E = dict(CHROME['en'], **I.T['en'])
NERVE = 5

PALETTE_LIVE = None   # from: py lesson-template/extract-palette.py DeadByTeatime/hero.jpg

PALETTE_PREVIEW = '''  --hero: url('Sherlock/hero.jpg');

  --void          : #090c0e;
  --surface       : #12181c;
  --surface2      : #1c292d;
  --border        : #a84a3f;
  --text          : #f5f2f2;
  --text-dim      : #bfa6a3;
  --accent        : #e97264;
  --accent-bright : #f5a89f;
  --accent-dim    : #cd3624;
  --secondary     : #07466d;
  --contrast      : #1ded9f;'''

# ── the narrative, glossed. key -> English; DE/ES in i18n_dead_by_teatime_<code>.N ──
N = {
    'brief': 'Lowfield, a quiet town outside London. Monday, 7:40 a.m. Your phone shows forty missed calls '
             'and one emergency alert. Something is wrong with the neighbours. You are the assistant manager '
             'of Lowfield Lanes, the bowling alley, and you have the only set of keys. Your task: get your '
             'people there before dark.',
    'streets': 'Lowfield is quiet in the wrong way. There are three stops to make before the bowling alley. '
               'In what order?',
    'lanes': 'The bowling alley glows at the end of the high street. You unlock the doors: eight lanes, a '
             'snack bar, a claw machine full of soft toys, and a glass front that was never designed to keep '
             'anything out.',
    'noise': 'Midnight. The lights flicker and go out. The generator in the back yard has stopped, and the '
             'shapes outside are coming closer to the glass. Two ideas, and no time to try both.',
    'dawn': 'Morning. The radio says the army is clearing the town street by street. The shapes outside are '
            'slower in daylight. In the car park stands the minibus of the Over-70s Bowling League, and Nan '
            'has the keys. Of course she does.',
    'end-bus': 'You fight your way across the car park with a cricket bat, two bowling balls and a very thick '
               'book. Then Nan drives the minibus down the middle of the high street at nine miles an hour. '
               'Gaz’s hand is fine. Geoffrey has a dent. At the edge of town, a soldier waves you through.',
    'end-wait': 'You stay behind the snack-bar fridge until the army arrives on Thursday. Everyone survives, '
                'mostly on crisps. Nan says she has had worse Christmases.',
    'end-solo': 'You slip out of the back door alone. You are faster, yes. But the storeroom key is in your '
                'pocket, and the people you left behind cannot get to the food.',
}

# ── the questions. (node, eyebrow, title, story, stem, [key, wrong, wrong], why, picture, strand) ──
# strand: 'm' modals, 'r' relative clauses. Grammar tokens in CAPS, cited
# words in double quotes (the house rule).
Q = [
    # Act I · the flat
    ('q01', 'Act I · the alert', 'An emergency alert.',
     '7:40 a.m. Your phone buzzes: EMERGENCY ALERT. Stay indoors. Lock your doors. Gaz reads it out with his '
     'mouth full of toast.',
     'Everyone ___ stay indoors until further notice.',
     ['must', 'must to', 'musts'],
     'MUST + base verb, with no TO and no -S: “must stay”. MUST is the same for every subject.',
     'alert', 'm'),
    ('q02', 'Act I · the door', 'Somebody is scratching.',
     'Something is scratching at the front door. Gaz reaches for the handle. The alert said: do not open your '
     'door to anyone.',
     'Gaz, you ___ open that door!',
     ['mustn’t', 'don’t have to', 'shouldn’t to'],
     'MUSTN’T: it is forbidden. DON’T HAVE TO only means it isn’t necessary, and that is not what the alert '
     'says. SHOULD never takes TO.',
     'door', 'm'),
    ('q03', 'Act I · the news', 'The news at eight.',
     'On TV, a very calm newsreader explains the new rules. A red banner runs along the bottom of the screen: '
     'BITTEN? GO TO HOSPITAL.',
     'Which sentence is correct?',
     ['Anyone who has been bitten must go to hospital.', 'Anyone which has been bitten must go to hospital.',
      'Anyone who he has been bitten must go to hospital.'],
     'ANYONE is a person, so WHO (or THAT). WHICH is for things. WHO is already the subject, so there is no '
     'HE as well.',
     'news', 'r'),
    ('q04', 'Act I · the plan', 'Gaz has a plan.',
     'Gaz announces his plan: go back to bed until it is all over. You have a better idea. Nan lives alone, '
     'and she isn’t answering her phone.',
     'We ___ check on Nan before we do anything else.',
     ['should', 'should to', 'ought'],
     'SHOULD + base verb gives advice: “should check”. There is no TO after SHOULD. OUGHT needs TO: “ought to '
     'check”.',
     'plan', 'm'),

    # Stop A · Nan's house
    ('q05', 'Stop A · Nan’s house', 'Nan opens the door.',
     'Nan is waiting in the hall with her cricket bat. She calls it Geoffrey. Monsters or no monsters, her '
     'house has rules.',
     '“In this house, you ___ wipe your feet. Even today.”',
     ['have to', 'has to', 'having to'],
     'HAVE TO with I, YOU, WE, THEY; HAS TO with HE, SHE, IT. A house rule is an obligation from outside you: '
     '“you have to wipe your feet”.',
     'nan', 'm'),
    ('q06', 'Stop A · the tablets', 'Nan’s tablets.',
     'Nan won’t leave without her heart tablets. They are in the bathroom upstairs, and something up there '
     'is moving.',
     'Her tablets, ___ she takes every morning, are upstairs.',
     ['which', 'that', 'who'],
     'Extra information between commas: WHICH for things, and never THAT after a comma. WHO is for people.',
     'tablets', 'r'),
    ('q07', 'Stop A · the stairs', 'Duck!',
     'You go up for the tablets. On the landing, something in a dressing gown turns round and lurches at you. '
     'Nan is right behind you with Geoffrey, already swinging.',
     '“You ___ stand there, love. Duck!”',
     ['shouldn’t', 'don’t should', 'shouldn’t to'],
     'SHOULDN’T + base verb: advice not to do something. The negative is SHOULDN’T, never DON’T SHOULD, and '
     'there is no TO.',
     'stairs', 'm'),
    ('q08', 'Stop A · checkpoint', 'Nan is coming with you.',
     'You come down with the tablets. Nan has packed a bag: biscuits, a torch, Geoffrey. She asks if she needs '
     'her big winter coat. It is June.',
     'Choose the reply that means it is NOT necessary.',
     ['You don’t have to bring it, Nan.', 'You mustn’t bring it with you, Nan.', 'You don’t must bring it, Nan.'],
     'Stop A is complete. DON’T HAVE TO: it isn’t necessary, so Nan can choose. MUSTN’T would forbid it, and '
     'MUST has no DON’T form.',
     'coat', 'm'),

    # Stop B · the ambulance station
    ('q09', 'Stop B · the ambulance station', 'Where is Priya?',
     'The ambulance station is empty, apart from a man in a dressing gown. He has seen Priya. You and Priya '
     'were together for three years.',
     'Priya is the paramedic ___ you used to go out with.',
     ['who', 'which', 'whose'],
     'WHO for a person. WHICH is for things, and WHOSE is for possession. THAT also works here, and so does no '
     'pronoun at all.',
     'station', 'r'),
    ('q10', 'Stop B · the car park', 'Not a paramedic any more.',
     'In the car park, one ambulance has its back doors open. Something in a green uniform is climbing out, '
     'arms first. You grab the door and push.',
     'Slam it on the one ___ arms are reaching out!',
     ['whose', 'who', 'who his'],
     'WHOSE + noun shows possession: his arms, so “whose arms”. WHO would need a verb next (“who is reaching '
     'out”), and never WHO + HIS.',
     'ambulance', 'r'),
    ('q11', 'Stop B · a note', 'A note on the door.',
     'On the door of the back room there is a note in Priya’s handwriting: IN HERE. KNOCK THREE TIMES IF YOU '
     'ARE HUMAN.',
     'The back room is the place ___ Priya is hiding.',
     ['where', 'which', 'who'],
     'A place where something happens takes WHERE: “the place where she is hiding”. WHICH alone needs a '
     'preposition at the end: “the place which she is hiding in”.',
     'note', 'r'),
    ('q12', 'Stop B · checkpoint', 'Meet Colin.',
     'Priya opens the door. Behind her stands a tall man in a camping hat, holding a book called Surviving '
     'Anything. “This is Colin,” she says.',
     'Which sentence describes him correctly?',
     ['Colin, whose book has an answer for everything, smiles.',
      'Colin, that has a book for everything, smiles at you.',
      'Colin, who his book has an answer for everything, smiles.'],
     'Stop B is complete. Extra information goes between commas: “, WHOSE book …,”. After a comma, never THAT; '
     'and WHOSE replaces WHO + HIS.',
     'colin', 'r'),

    # Stop C · Bell's corner shop
    ('q13', 'Stop C · Bell’s corner shop', 'Open, as always.',
     'Mr Bell’s corner shop is open. Of course it is. Mr Bell stands behind the counter under a new sign: '
     'CASH ONLY. NO BITING.',
     'Mr Bell runs the shop ___ sells everything from batteries to birthday cards.',
     ['which', 'where', 'who'],
     'The shop does the selling, so it is the subject: WHICH or THAT. WHERE needs a new subject: “the shop '
     'where you can buy batteries”.',
     'shop', 'r'),
    ('q14', 'Stop C · the list', 'One basket.',
     'You have ten minutes and one basket. Gaz wants crisps. Nan wants tea. You want the torch batteries Mr '
     'Bell keeps behind the counter.',
     'Which sentence is correct?',
     ['We need the batteries Bell keeps behind the counter.',
      'We need the batteries Bell keeps them behind the counter.',
      'We need the batteries who Bell keeps behind the counter.'],
     'The pronoun can go when a new subject follows it: “the batteries (that) Bell keeps”. Don’t repeat the '
     'object with THEM, and WHO is only for people.',
     'list', 'r'),
    ('q15', 'Stop C · the till', 'Mr Bell stays.',
     'A customer at the till groans and lunges across the counter. Mr Bell flattens him with a rolled-up '
     'newspaper and goes back to his crossword. He will not leave.',
     '“Somebody ___ look after the shop.”',
     ['has to', 'have to', 'must to'],
     'SOMEBODY is singular, like HE or SHE, so HAS TO: “somebody has to look after it”. MUST never takes TO.',
     'till', 'm'),
    ('q16', 'Stop C · checkpoint', 'Advice from the counter.',
     'Mr Bell gives you some advice for the road: stay in the middle of the street, and don’t run. They notice '
     'running.',
     'Report his advice correctly.',
     ['He says we shouldn’t run.', 'He says we don’t should run.', 'He says we shouldn’t to run.'],
     'Stop C is complete. SHOULDN’T + base verb: advice. The negative is never DON’T SHOULD, and SHOULD never '
     'takes TO.',
     'advice', 'm'),

    # Act III · Lowfield Lanes
    ('q17', 'Act III · the storeroom', 'One lock that works.',
     'Colin opens his book. “Rule one: secure the entrances.” For once he is right. Only one door in the '
     'building locks from the inside.',
     'The storeroom is the only room ___.',
     ['we can lock from the inside', 'which we can lock it from inside', 'where we can lock it from inside'],
     'The room is the object of LOCK, so the pronoun can go: “the room (that) we can lock”. Don’t add IT as '
     'well; the relative already stands for the room.',
     'storeroom', 'r'),
    ('q18', 'Act III · house rules', 'Colin’s rules.',
     'Colin writes rules on the scoreboard in capital letters. Rule four: NO NOISE AFTER DARK. Gaz asks if '
     'that includes talking.',
     '“We ___ shout, but we don’t have to whisper.”',
     ['mustn’t', 'don’t have to', 'haven’t to'],
     'MUSTN’T: forbidden, so no shouting. DON’T HAVE TO: not necessary, so whispering is optional. HAVEN’T TO '
     'is not English.',
     'scoreboard', 'm'),

    # Act IV · the fork
    ('q19', 'Act IV · the back yard', 'The generator.',
     'Priya comes with you. The generator needs a key, and the key is in Colin’s pocket. Colin is asleep on '
     'lane three.',
     'Get the key from the man ___ asleep on lane three.',
     ['who is', 'which is', 'whose is'],
     'WHO for a person, and here it is the subject: “the man who is asleep”. WHOSE always needs a noun after '
     'it: “the man whose key we need”.',
     'generator', 'r'),
    ('q20', 'Act IV · the front doors', 'The barricade.',
     'You and Gaz drag the snack-bar fridge across the glass doors. After one metre, Gaz wants a break.',
     '“We can’t stop now. We ___ finish this before they get in.”',
     ['have to', 'don’t have to', 'should to'],
     'HAVE TO: the situation makes it necessary. DON’T HAVE TO means the opposite. SHOULD never takes TO.',
     'barricade', 'm'),

    # Act IV · the long night
    ('q21', 'Act IV · 2 a.m.', 'The glass gives way.',
     'At 2 a.m. the glass cracks and three of them push through the gap. Gaz grabs a bowling ball from the '
     'rack and looks at you: which one first?',
     'Aim at the one ___ is closest to Nan!',
     ['that', 'where', 'whose'],
     'The one closest to Nan is the subject of IS, so THAT (or WHO). WHERE is for places, and WHOSE always '
     'needs a noun after it.',
     'bowling', 'r'),
    ('q22', 'Act IV · first aid', 'Priya takes charge.',
     'The last one goes down on lane one. Gaz shows you a small bite on his hand. “It was a crisp packet,” he '
     'says. “Probably.” Priya cleans it and gives him three instructions.',
     'Which instruction is advice, not a rule?',
     ['You should drink some water.', 'You mustn’t touch the bandage.', 'You have to keep your hand up.'],
     'SHOULD gives advice: a good idea. MUSTN’T and HAVE TO are rules, with no choice. Priya uses all three, '
     'and Gaz follows none of them.',
     'firstaid', 'm'),
    ('q23', 'Act IV · 3 a.m.', 'A noise in the dark.',
     'At 3 a.m. the claw machine starts playing its little song. Something is moving inside the glass box, '
     'behind the soft toys.',
     'The noise comes from the machine ___ Gaz once won a pink rabbit.',
     ['where', 'which', 'who'],
     'A place where something happened takes WHERE, meaning “in which”. WHICH alone would need IN at the end: '
     '“the machine which Gaz won a rabbit in”.',
     'claw', 'r'),
    ('q24', 'Act IV · the manual', 'No chapter on this.',
     'Colin flips through his book. There is no chapter on claw machines. For the first time, he asks you what '
     'to do.',
     '“Do we ___ open it?” Colin asks.',
     ['have to', 'must', 'should to'],
     'A question with HAVE TO uses DO: “Do we have to open it?” MUST makes its question without DO: “Must we '
     'open it?” SHOULD never takes TO.',
     'manual', 'm'),
    ('q25', 'Act IV · the claw machine', 'It’s only Mr Bell.',
     'The claw machine bursts open and a zombie in a bowling shirt falls out, with Mr Bell right behind it. '
     'He knocks it flat with his bag of cash. “Shop’s closed,” he says.',
     'Which sentence is correct?',
     ['Mr Bell, who we thought was at the shop, climbs out.',
      'Mr Bell, that we thought was at the shop, climbs out.',
      'Mr Bell, who we thought he was at the shop, climbs out.'],
     'Extra information about a named person: commas + WHO, never THAT. Don’t repeat the subject: WHO already '
     'stands for Mr Bell, so no HE.',
     'bell', 'r'),

    # Act V · morning
    ('q26', 'Act V · the decision', 'Make the call.',
     'Six of them stand between the doors and the minibus, slow in the daylight. Nan raises Geoffrey. Colin '
     'raises his book. Everyone looks at you.',
     'Which sentence gives the group clear advice?',
     ['We should leave now, while they are slow.', 'We should to leave now, while they are slow.',
      'We don’t should leave now, while it’s light.'],
     'SHOULD + base verb: “should leave”. It is advice, not an order: you want the group to agree with you.',
     'minibus', 'm'),
]

ORDER = ['q01', 'q02', 'q03', 'q04', 'streets',
         'q05', 'q06', 'q07', 'q08', 'streets',
         'q09', 'q10', 'q11', 'q12', 'streets',
         'q13', 'q14', 'q15', 'q16', 'streets',
         'lanes', 'q17', 'q18', 'noise',
         'q19', 'q21', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'dawn', 'q26', 'decision']
NEXT = {a: b for a, b in zip(ORDER, ORDER[1:]) if a.startswith('q')}
STOPS = {'q08': 'nan', 'q12': 'priya', 'q16': 'bell'}   # a checkpoint closes its stop
SECTIONS = [['q01', 'q02', 'q03', 'q04'], ['q05', 'q06', 'q07', 'q08'], ['q09', 'q10', 'q11', 'q12'],
            ['q13', 'q14', 'q15', 'q16'], ['q17', 'q18'], ['q19'], ['q20'],
            ['q21', 'q22', 'q23', 'q24', 'q25'], ['q26']]
GOLD = 'time>=1'
SLOTS = [1, 2, 0, 2, 0, 1, 0, 1, 2]

# headword (English, never translated) and example; the meaning is lab<n> in T
LAB = [
    ('MUST / MUSTN’T + VERB', 'You mustn’t open the door.'),
    ('HAVE TO / HAS TO + VERB', 'Nan has to take her tablets.'),
    ('DON’T HAVE TO + VERB', 'You don’t have to whisper.'),
    ('SHOULD / SHOULDN’T + VERB', 'You shouldn’t run.'),
    ('WHO · WHICH · THAT', 'the man who lives next door · the van that won’t start'),
    ('WHERE · WHOSE', 'the shop where Nan buys tea · the man whose book has the answers'),
    ('(THAT) LEFT OUT', 'the bat (that) Nan keeps by the door'),
    (', WHO … , · , WHICH … ,', 'Gaz, who never runs, ran.'),
]

CHIPS = ['must', 'mustn’t', 'have to', 'don’t have to', 'should', 'who', 'which', 'where', 'whose']

# every route: the three stops in any order, either arm of the fork
STOP_RUNS = [['q05', 'q06', 'q07', 'q08'], ['q09', 'q10', 'q11', 'q12'], ['q13', 'q14', 'q15', 'q16']]
PATHS = [['q01', 'q02', 'q03', 'q04'] + sum(order, []) + ['q17', 'q18', arm, 'q21', 'q22', 'q23', 'q24', 'q25', 'q26']
         for order in itertools.permutations(STOP_RUNS) for arm in ('q19', 'q20')]

# The plates: slot -> (the Scarlet Star picture that stands in for it in the
# preview, what ChatGPT is asked to paint). The full prompts are in
# docs/CHATGPT-DEAD-BY-TEATIME-ART-BRIEF.md, generated from this table.
PLATES = {
    'hero': ('hero', 'Five friends and a grandmother with a cricket bat, silhouetted in front of a glowing '
                     'bowling-alley sign at dusk'),
    'brief': ('pov', 'A phone glowing on a bedside table at dawn: forty missed calls and an emergency alert'),
    'how': ('compass', 'A bowling ball and a cricket bat crossed like a coat of arms'),
    'cast': ('faces', 'Six heads in a row, in profile: a young man, a sleepy flatmate, a grandmother, a '
                      'paramedic, a tall man in a camping hat, an old shopkeeper'),
    'toolkit': ('case', 'A cork board with a pinned notice, a whistle and a torch hanging beside it'),
    'alert': ('teatin', 'A man on a sofa with toast in his mouth, staring at his phone'),
    'door': ('door', 'A front door with a shadowy shape behind its frosted glass; a hand on the handle'),
    'news': ('window', 'A television in a dark living room: a calm newsreader and a red warning banner'),
    'plan': ('study', 'A duvet pulled over a head; a hand holding car keys beside it'),
    'nan': ('celeste', 'A small grandmother in a hallway holding a cricket bat like a sword'),
    'tablets': ('body', 'A bathroom cabinet, half open, a box of tablets inside; a shadow on the tiles'),
    'stairs': ('stairs', 'A grandmother on a narrow staircase swinging her cricket bat at a slow zombie in a dressing gown on the landing; YOU ducking below the swing'),
    'coat': ('celeste-shadow', 'A grandmother with a packed bag and an enormous winter coat'),
    'streets': ('street', 'An empty high street, one shopping trolley rolling on its own'),
    'station': ('platform', 'An empty ambulance station; a man in a dressing gown in the doorway'),
    'ambulance': ('carriage', 'A zombie in a green paramedic uniform climbing out of the back doors of an ambulance, arms first; YOU slamming one door on it, blue lights flashing'),
    'note': ('museum', 'A handwritten note taped to a closed door, a hand raised to knock'),
    'colin': ('holmes-celeste', 'A tall man in a camping hat holding a survival manual, a woman paramedic beside him'),
    'shop': ('bar', 'A tiny corner shop at night, the old owner behind the counter, a hand-written sign above him'),
    'list': ('table', 'A shopping basket: crisps, a box of tea, torch batteries'),
    'till': ('moriarty', 'An old shopkeeper flattening a lunging zombie customer with a rolled-up newspaper across his shop counter, completely unbothered'),
    'advice': ('rails', 'An empty street at dusk, a dotted line running down its middle'),
    'lanes': ('chase', 'A bowling alley at night: eight lanes, a neon sign, a glass front'),
    'storeroom': ('chase-steps', 'A storeroom door with one heavy bolt, lit by a torch'),
    'scoreboard': ('chase-fire', 'A tall thin man in a camping hat writing on a glowing bowling scoreboard'),
    'noise': ('standoff', 'The bowling alley in darkness, shapes pressed against the glass doors'),
    'generator': ('chase-stairs', 'A generator in a back yard at night, lit by a torch'),
    'barricade': ('chase-alley', 'Two people pushing a drinks fridge across glass doors'),
    'bowling': ('chase-fire', 'Inside a bowling alley at night: cracked glass doors, three zombies pushing through, the flatmate hurling a bowling ball down the lane at them, the grandmother with her bat, the paramedic with a fire extinguisher'),
    'firstaid': ('celeste-eyes', 'A paramedic bandaging a hand by torchlight'),
    'claw': ('pursued', 'A claw machine glowing in the dark, something moving behind the soft toys'),
    'manual': ('moriarty-face', 'A worried man flipping through a survival book'),
    'bell': ('chase-alley', 'An old shopkeeper climbing out of a glowing claw machine behind a zombie in a bowling shirt, knocking it flat with a bag of cash'),
    'dawn': ('rails', 'Morning light across a car park and a white minibus'),
    'minibus': ('carriage', 'At dawn the whole group fights across a car park to a white minibus: the grandmother swinging her bat, the tall man swinging his thick book, slow zombies all round'),
    'decision': ('table', 'Six people round the end of a bowling lane, all looking at you'),
    'endbus': ('street', 'A white minibus driving slowly down the middle of a high street at sunrise'),
    'endwait': ('study', 'The group asleep among crisp packets behind a barricaded fridge'),
    'endsolo': ('pursued', 'One figure alone on an empty street at dawn'),
    'act': ('compass', 'A notice taped to the inside of a glass door, the group behind it, morning light'),
}


def bg(pic, preview):
    if preview:
        return ' data-bg="Sherlock/%s.jpg"' % PLATES[pic][0]
    return ' data-bg="%s/%s.jpg"' % (F, pic)


def cont(to, key='btnContinue'):
    return ('        <div style="margin-top:18px">\n'
            '          <button class="btn btn-solid" data-goto="%s" data-i18n="%s">%s</button>\n'
            '        </div>\n' % (to, key, E[key]))


def head(eyebrow, title, eyebrow_key=None, title_key=None):
    ek = ' data-i18n="%s"' % eyebrow_key if eyebrow_key else ''
    tk = ' data-i18n="%s"' % title_key if title_key else ''
    return ('      <div class="slide-head"><div>\n'
            '        <div class="eyebrow"%s>%s</div>\n'
            '        <h2 class="slide-title"%s>%s</h2>\n'
            '      </div></div>\n' % (ek, eyebrow, tk, title))


def section(node, kind, act, body, pic=None, preview=False):
    return ('\n    <section class="slide" data-type="%s" data-node="%s" data-act="%s"%s>\n%s'
            '    </section>\n' % (kind, node, act, bg(pic, preview) if pic else '', body))


def gl(key, cls='prose'):
    return '<p class="%s gloss" data-tr="%s">%s</p>' % (cls, key, N[key])


def say(key):
    """A speaking prompt: an instruction, so translated in place (data-i18n)."""
    return '<p class="prose dim" style="margin-top:12px" data-i18n="%s">%s</p>' % (key, E[key])


def teach(node, act, ek, tk, inner, to, pic, preview):
    body = (head(E[ek], E[tk], ek, tk) +
            '      <div class="slide-body" style="position:relative">\n        %s\n' % inner +
            (cont(to) if to else '') + '      </div>\n')
    return section(node, 'teach', act, body, pic, preview)


def mc(q, preview):
    """A question is one slide, as on the Scarlet Star: the scene (glossed),
    the stem, the options and the feedback, on its own plate."""
    node, eyebrow, title, story, stem, opts, why, pic, _ = q
    key = opts[0]
    nxt = NEXT[node]
    clue = ' data-clue="%s"' % STOPS[node] if node in STOPS else ''
    sec = next(s for s in SECTIONS if node in s)
    n = sec.index(node) + 1
    # The engine shuffles, but check-lesson's KEYS gate reads the source, so
    # the key is dealt round the letters too: 1 2 0 2 0 1 …, never three alike.
    slot = SLOTS[[x[0] for x in Q].index(node) % len(SLOTS)]
    dealt = list(opts[1:])
    dealt.insert(slot, key)
    buttons = []
    for o in dealt:
        if o == key:
            buttons.append('<button class="opt" data-correct data-dp="1"%s data-goto="%s">%s</button>' % (clue, nxt, o))
        else:
            buttons.append('<button class="opt" data-time="-1"%s data-goto="%s">%s</button>' % (clue, nxt, o))
    N['q-' + node] = story
    # Eyebrow, title, an instruction stem and the explanation are chrome:
    # they translate (QT). A gap stem is the English being taught: it does not.
    gap = '___' in stem
    for code, d in I.T.items():
        e, t, s, w = (eyebrow, title, None if gap else stem, why) if code == 'en' else I.QT[code][node]
        d['qe' + node] = e + (' · ' + I.OF[code] % (n, len(sec)) if len(sec) > 1 else '')
        d['qt' + node], d['qw' + node] = t, w
        if s:
            d['qs' + node] = s
    E.update((k, I.T['en'][k]) for k in ('qe' + node, 'qt' + node, 'qw' + node))
    act = eyebrow.split(' · ')[0]
    stem_html = ('        <p class="q-stem">%s</p>\n' % stem if gap else
                 '        <p class="q-stem" data-i18n="qs%s">%s</p>\n' % (node, stem))
    # Short options sit two to a row, as on the Scarlet Star; sentences take a row each.
    two = ' two-up' if max(len(o) for o in opts) <= 30 else ''
    body = (head(E['qe' + node], title, 'qe' + node, 'qt' + node) +
            '      <div class="slide-body">\n'
            '        <p class="q-ctx gloss" data-tr="q-%s" style="margin-bottom:16px">%s</p>\n' % (node, story) +
            stem_html +
            '        <div class="opts%s">\n          %s\n        </div>\n' % (two, '\n          '.join(buttons)) +
            # Continue sits beside the feedback, not under it: under a two-line
            # explanation it met the deck bar (Reasonable Doubt, same fix).
            '        <div style="display:flex;gap:16px;align-items:flex-start">\n'
            '          <p class="feedback" style="flex:1" data-explain="qw%s"></p>\n' % node +
            '          <button class="btn btn-solid" style="flex:none;margin-top:8px" data-action="branch-continue" '
            'data-i18n="btnContinue" hidden>%s</button>\n'
            '        </div>\n      </div>\n' % E['btnContinue'])
    return section(node, 'mc', act, body, pic, preview)


def choices(rows):
    """Choice rows, stacked: (label key, body key or None, goto, require)."""
    out = '        <div style="margin-top:14px">\n'
    for k, bk, to, req in rows:
        out += ('          <div class="card choice-row">\n'
                '            <p class="prose"><strong data-i18n="%s">%s</strong>%s</p>\n'
                '            <button class="btn btn-solid choice" data-goto="%s"%s data-i18n="btnChoose">%s</button>\n'
                '          </div>\n' % (k, E[k], '<br><span data-i18n="%s">%s</span>' % (bk, E[bk]) if bk else '',
                                       to, ' data-require="%s"' % req if req else '', E['btnChoose']))
    return out + '        </div>\n'


EXTRA = '''<style>
/* Dead by Teatime: a choice is a row, what it is on the left, its button on the right. */
.choice-row { display: flex; align-items: center; gap: 16px; padding: 12px 18px; }
.choice-row + .choice-row { margin-top: 10px; }
.choice-row .prose { flex: 1; font-size: 18px; line-height: 1.4; }
.choice-row .btn { flex: none; }
/* A question slide carries its scene, the scene's translation, the stem,
   three options and the feedback: options a little tighter than a quiz's. */
.slide[data-type="mc"] .opts { gap: 8px; }
.slide[data-type="mc"] .opt { padding-top: 9px; padding-bottom: 9px; }
.slide[data-type="mc"] .q-stem { margin-top: 18px; margin-bottom: 12px; }
</style>
<script>
/* The deck bar's act label is written from data-act, which is English; it
   reads its own language key instead, and again when the language changes. */
function actLabel() {
  const a = slides[idx].dataset.act || '';
  const k = 'act' + a.replace(/[^A-Za-z]/g, '');
  if (!a || UI_I18N.en[k] == null) return;
  ['deckCount', 'phoneCount'].forEach(id => { const el = document.getElementById(id); if (el) el.textContent = t(k); });
}
slideHooks.push(actLabel);
document.addEventListener('change', e => { if (e.target.matches('select')) setTimeout(actLabel, 0); });
</script>
'''


def build_slides(preview):
    logo = D.logo_from(TPL)
    by = {q[0]: q for q in Q}

    def m(node):
        return mc(by[node], preview)

    def tc(*a):
        return teach(*a, preview)

    s = []
    cover = D.cover(logo, E['coverTitle'], E['coverSub'],
                    [('Level', E['chipLevel']), ('Focus', E['chipFocus']), ('Count', E['chipCount'])])
    cover = cover.replace('data-type="cover"', 'data-type="cover" data-node="cover" data-act=""', 1)
    s.append(cover.replace('data-action="next"', 'data-goto="how"', 1))

    pre = E['actBefore']
    s.append(section('how', 'teach', pre,
                     head(E['howEyebrow'], E['howTitle'], 'howEyebrow', 'howTitle') +
                     '      <div class="slide-body">\n        <div class="cols cols-3">\n' +
                     ''.join('          <div class="card"><p class="prose"><strong data-i18n="%s">%s</strong><br>'
                             '<span data-i18n="%sBody">%s</span></p></div>\n'
                             % (k, E[k], k, E[k + 'Body']) for k in ('howDp', 'howTime', 'howClues')) +
                     '        </div>\n'
                     '        <p class="prose dim" style="margin-top:16px" data-i18n="howAloud">%s</p>\n'
                     % E['howAloud'] + cont('brief') + '      </div>\n', 'how', preview))
    s.append(tc('brief', pre, 'briefEyebrow', 'briefTitle', '<div class="card">%s</div>' % gl('brief'), 'cast', 'brief'))
    s.append(section('cast', 'teach', pre,
                     head(E['castEyebrow'], E['castTitle'], 'castEyebrow', 'castTitle') +
                     '      <div class="slide-body">\n        <div class="cols cols-3" style="gap:12px">\n' +
                     ''.join('          <div class="card" style="padding:14px 18px"><p class="prose" style="font-size:17px;line-height:1.4">'
                             '<strong data-i18n="cast%d">%s</strong><br>'
                             '<span class="dim" data-i18n="cast%dBody">%s</span></p></div>\n'
                             % (i, E['cast%d' % i], i, E['cast%dBody' % i]) for i in range(1, 7)) +
                     '        </div>\n' + cont('toolkit') + '      </div>\n', 'cast', preview))

    def forms(lo, hi):
        return '<div class="card" style="padding:16px 22px">%s</div>' % ''.join(
            '<p class="prose" style="font-size:17px;line-height:1.45;margin-top:%dpx">'
            '<strong style="font-size:13px;letter-spacing:.04em">%s</strong><br>%s · '
            '<span class="dim" data-i18n="lab%d">%s</span></p>'
            % (0 if i == lo else 12, h, ex, i, E['lab%d' % i])
            for i, (h, ex) in enumerate(LAB, 1) if lo <= i <= hi)
    s.append(tc('toolkit', pre, 'labEyebrow1', 'labTitle1', forms(1, 4), 'toolkit2', 'toolkit'))
    s.append(tc('toolkit2', pre, 'labEyebrow2', 'labTitle2', forms(5, 8), 'q01', 'toolkit'))

    s += [m('q01'), m('q02'), m('q03'), m('q04')]
    s.append(tc('streets', 'Act II', 'hubEyebrow', 'hubTitle',
                gl('streets') + '\n' +
                choices([('stopA', 'stopABody', 'q05', None), ('stopB', 'stopBBody', 'q09', None),
                         ('stopC', 'stopCBody', 'q13', None)]) +
                '        <div style="margin-top:16px">\n'
                '          <button class="btn btn-solid" data-goto="lanes" data-require="clues>=3" '
                'data-i18n="btnHead">%s</button>\n'
                '        </div>\n' % E['btnHead'], None, 'streets'))
    for run in STOP_RUNS:
        s += [m(n) for n in run]

    s.append(tc('lanes', 'Act III', 'lanesEyebrow', 'lanesTitle',
                '<div class="card">%s%s</div>' % (gl('lanes'), say('sayLanes')), 'q17', 'lanes'))
    s += [m('q17'), m('q18')]
    s.append(tc('noise', 'Act IV', 'forkEyebrow', 'forkTitle',
                gl('noise') + '\n' +
                choices([('routeBack', None, 'q19', None), ('routeFront', None, 'q20', None)]) +
                '        <p class="prose dim" style="margin-top:14px;font-size:18px" '
                'data-i18n="explainFirst">%s</p>\n' % E['explainFirst'], None, 'noise'))
    s += [m('q19'), m('q20'), m('q21'), m('q22'), m('q23'), m('q24'), m('q25')]
    s.append(tc('dawn', 'Act V', 'dawnEyebrow', 'dawnTitle',
                '<div class="card">%s%s</div>' % (gl('dawn'), say('sayDawn')), 'q26', 'dawn'))
    s.append(m('q26'))
    s.append(tc('decision', 'Ending', 'decisionEyebrow', 'decisionTitle',
                choices([('voteBus', 'voteBusBody', 'end-bus', GOLD),
                         ('voteWait', 'voteWaitBody', 'end-wait', None),
                         ('voteSolo', 'voteSoloBody', 'end-solo', None)]), None, 'decision'))

    def ending(k, revisit):
        K_ = k.capitalize()
        inner = '<div class="card">%s%s</div>' % (gl('end-' + k), say('say' + K_))
        body = (head(E['end' + K_], E['end%sTitle' % K_], 'end' + K_, 'end%sTitle' % K_) +
                '      <div class="slide-body" style="position:relative">\n        %s\n' % inner +
                '        <div style="margin-top:18px;display:flex;gap:10px">\n'
                '          <button class="btn btn-solid" data-goto="results" data-i18n="btnContinue">%s</button>\n'
                % E['btnContinue'] +
                ('          <button class="btn" data-goto="decision" data-i18n="btnRevisit">%s</button>\n'
                 % E['btnRevisit'] if revisit else '') +
                '        </div>\n      </div>\n')
        return section('end-' + k, 'teach', 'Ending', body, 'end' + k, preview)
    s += [ending('bus', False), ending('wait', True), ending('solo', True)]

    results = D.results(next_key='resRoute', next_text=E['resRoute'])
    results = results.replace('data-type="results"', 'data-type="results" data-node="results" data-act="Ending"%s'
                              % bg('hero', preview), 1)
    i = results.rindex('      </div>\n    </section>')
    s.append(results[:i] + cont('activate', 'resNext') + results[i:])

    act = D.activate(E['actTitle'], E['actUse'], CHIPS, 'Speaking', E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'])
    act = act.replace('data-type="activate"', 'data-type="activate" data-node="activate" data-act="Activation"%s'
                      % bg('act', preview), 1)
    s.append(act.replace('data-action="restart"', 'data-action="restart" data-goto="how"', 1))
    return ''.join(s)


def gates(slides, preview):
    """The checks a branching deck needs that check-lesson.js does not make."""
    D.assert_no_key_is_longest([dict(options=q[5], correct=0) for q in Q], 'MC')
    nodes = re.findall(r'data-node="([^"]+)"', slides)
    assert len(nodes) == len(set(nodes)), 'duplicate node'
    gotos = set(re.findall(r'data-goto="([^"]+)"', slides))
    missing = gotos - set(nodes)
    assert not missing, 'data-goto to no node: %s' % missing
    orphans = set(nodes) - gotos - {'cover'}
    assert not orphans, 'orphan nodes: %s' % orphans
    for p in PATHS:
        assert len(p) == 25, ('questions on a path', len(p))
        strands = [next(q[8] for q in Q if q[0] == n) for n in p]
        assert abs(strands.count('m') - strands.count('r')) <= 1, ('strand balance', strands.count('m'))
    for node, clue in STOPS.items():
        sec = re.search(r'data-node="%s".*?</section>' % node, slides, re.S).group(0)
        assert sec.count('data-clue="%s"' % clue) == 3, node
    assert slides.count('data-clue=') == 9
    for q in Q:
        assert q[7] in PLATES, 'no brief for plate %s' % q[7]
        assert q[6].count('“') == q[6].count('”'), q[0]
        assert len(set(q[5])) == 3, q[0]
    used = set(re.findall(r'data-bg="%s/([^"]+)\.jpg"' % F, slides)) if not preview else set()
    if not preview:
        assert used | {'hero'} >= set(PLATES) - {'hero'}, 'plates never shown: %s' % (set(PLATES) - used)
        # live: no two linked slides share a picture
        pic = dict(re.findall(r'data-node="([^"]+)"[^>]*?data-bg="([^"]+)"', slides))
        for node, body in re.findall(r'data-node="([^"]+)"(.*?)</section>', slides, flags=re.S):
            for to in set(re.findall(r'data-goto="([^"]+)"', body)):
                assert not (node in pic and to in pic and pic[node] == pic[to]), (node, to, pic[node])
    for p in set(re.findall(r'data-bg="([^"]+)"', slides)):
        assert os.path.exists(p), 'missing plate %s' % p
    for k in N:
        assert '’' not in k


def narrative_tr(langs):
    out = {}
    for c in langs[1:]:
        mod = importlib.import_module('i18n_dead_by_teatime_%s' % c)
        nk = set(N) - set(mod.N)
        assert not nk, '%s glosses missing: %s' % (c, sorted(nk))
        extra = set(mod.N) - set(N)
        assert not extra, '%s glosses for nothing: %s' % (c, sorted(extra))
        out[c] = mod.N
    return 'const NARRATIVE_TR = ' + json.dumps(out, ensure_ascii=False, indent=1) + ';\n'


BRIEF = 'docs/CHATGPT-DEAD-BY-TEATIME-ART-BRIEF.md'

STYLE = ('Detailed graphic-novel illustration, cinematic lighting, dusk blues against bowling-alley neon pink '
         'and warm lamp light, fine ink texture. ACTION COMEDY, never gory: the fights are slapstick knockdowns '
         'with whatever is to hand (a cricket bat, bowling balls, a rolled-up newspaper, a fire extinguisher, a '
         'thick book), with no blood and no wounds; the undead are shabby, grey-faced and slow, funny rather than '
         'frightening. 16:9 landscape. Put the action in the RIGHT half of the picture and keep the LEFT half '
         'calm and dark, because slide text sits there. No words, letters, numbers, logos or signatures anywhere '
         'in the image. Invented faces only: no resemblance to any real actor or public figure.')

ACTION = ('stairs', 'ambulance', 'till', 'bowling', 'bell', 'minibus')   # 2026-11-16: the fights, re-briefed

CAST = ('The same people in every picture: YOU, late twenties, short dark hair, a red bowling-alley polo shirt; '
        'GAZ, your flatmate, messy fair hair, grey hoodie, always half asleep; NAN, a tiny grandmother with a '
        'white perm, a lilac cardigan and a cricket bat; PRIYA, a paramedic in a dark green uniform, black '
        'ponytail; COLIN, very tall and thin, beige camping hat, khaki vest with many pockets, a thick book; '
        'MR BELL, an old bald shopkeeper with round glasses and a brown shop coat. The town is LOWFIELD, a '
        'small English commuter town: terraced houses, a high street, a 1980s bowling alley called Lowfield Lanes.')


def write_brief():
    """The ChatGPT brief, generated from PLATES so the two never drift apart."""
    rows = ['# Dead by Teatime: artwork brief for ChatGPT', '',
            'Generated by `py lesson-template/build/build_dead_by_teatime.py --brief`; edit PLATES in the '
            'builder, not this file.', '',
            '## How to use it', '',
            '1. Start one ChatGPT conversation and paste **The style** and **The people** below as the first '
            'message, with: "Keep this style and these people for every picture I ask for in this chat."',
            '2. Then ask for each picture by pasting its line, one picture per message.',
            '3. Save each picture as the file name shown (`hero.png`, `brief.png` …) in '
            '`incoming/dead-by-teatime/`. The folder already exists on this machine.',
            '4. Run `/publish`, or tell Claude the pictures are in. The deck builds itself from them.', '',
            '## The style', '', STYLE, '', '## The people', '', CAST, '',
            '## The pictures (%d)' % len(PLATES), '']
    rows[rows.index('## The style'):rows.index('## The style')] = [
        '## Redo these six: the fights (2026-11-16)', '',
        'The story now has zombie fighting. These six replace the fight-free pictures of the same name '
        '(`bowling.png` is new and replaces `bite.png`, which is no longer used). Same style, same people; paste '
        'each line as its own message.', ''] + [
        '- **`%s.png`**: %s.' % (slot, PLATES[slot][1]) for slot in ACTION] + ['']
    for n, (slot, (_, subject)) in enumerate(PLATES.items(), 1):
        rows.append('%d. **`%s.png`**: %s.' % (n, slot, subject))
    rows += ['', 'The deck is playable now on stand-in pictures; each real one replaces its stand-in on the '
             'next build. Every slot above must be filled before the page goes live.', '']
    open(BRIEF, 'w', encoding='utf-8', newline='\n').write('\n'.join(rows))
    print('wrote', BRIEF)


def build():
    os.makedirs(DROP, exist_ok=True)       # the drop folder exists whenever the builder runs
    have = [p for p in PLATES if os.path.exists(os.path.join(F, p + '.jpg'))]
    preview = len(have) < len(PLATES)
    if not preview and PALETTE_LIVE is None:
        sys.exit('Every plate is in %s/. Run extract-palette.py %s/hero.jpg, paste its block '
                 'into PALETTE_LIVE, and run again.' % (F, F))
    slides = build_slides(preview)
    gates(slides, preview)
    n = slides.count('<section class="slide')
    langs = tuple(c for c in I.LANGS if c in I.T)
    out = PREVIEW if preview else OUT
    s = D.assemble(TPL, out, slides, PALETTE_PREVIEW if preview else PALETTE_LIVE, TITLE, I, langs=langs)
    s = s.replace('<body>', '<body data-flow="branch" data-start="cover" data-time="%d">' % NERVE, 1)
    s = s.replace('const UI_I18N = {', narrative_tr(langs) + 'const UI_I18N = {', 1)
    s = s.replace('</body>', EXTRA + '</body>', 1)
    open(out, 'w', encoding='utf-8', newline='').write(s)
    print('wrote %s — %d slides, %s%s' % (out, n, ','.join(langs),
                                          ' (PREVIEW: %d of %d plates in %s/)' % (len(have), len(PLATES), F)
                                          if preview else ''))


if __name__ == '__main__':
    if '--brief' in sys.argv:
        write_brief()
    else:
        build()
