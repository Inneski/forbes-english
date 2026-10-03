#!/usr/bin/env python3
"""The Last Night at the Grand Hotel — Mixed Tenses Voxel RPG (B1-B2).

    py lesson-template/build/build_grand_hotel.py

Rebuilds block-camp/grand-hotel-rpg.html from
lesson-template/build/rpg/grand-hotel-rpg/data.json — the text of the
standalone export Innes sent on 2026-10-03 (`Grand_Hotel_The_Last_Night.html`,
12 MB).

**A sixth kind of export** (rpg/README.md §2). One
`<script id="game-data" type="application/json">` block holding `pages` (30,
each with story, question, four options, a `why` line PER OPTION, the two
tenses it contrasts, an optional evidence `clue`, an optional story `choice`
and optional `variants` text chosen by an earlier choice), `guide` (18 tense
forms with the Sherpa Tensing route-map colours), `cast` (52) and `art` (30
pictures inline as base64 WebP, 1672x941, each with its own `object` and an
`x`/`y` centre). Read with a regex for the JSON block and `json.loads`; the
pictures were decoded from `art[*].src` and the rest saved as data.json
without them.

**The pictures were graded.** Innes: "can you grade the colours so the yellow
isnt so yellow". The plates came with a heavy amber cast — blue 40-58 levels
under red and green on the lobby, kitchen, survey and agreement plates. Each
was given a partial white balance in Lab: a* and b* pulled toward neutral by
55% of that plate's own midtone cast (a* at half strength), tapered off in the
highlights so the lamps and chandeliers stay warm and off in deep shadow, then
the yellow-orange hue band desaturated by 20%. A plate that was already
neutral (the cable car, the storm, the descent) barely moves, because the
correction is its own cast. The script is rpg/grand-hotel-rpg/grade.py.

The export's rules, kept exactly: 28 questions, +5 for a correct FIRST
answer, nothing for a wrong one and no lives — a mistake explains and the
story goes on. Five evidence questions (pages 5, 9, 15, 24, 26) are the
clues; a right first answer verifies one, and the engine's tiles count them.
Three story choices (pages 10, 19, 29) score nothing; the first two change
later text (`routeStory` on pages 22 and 23), and all three feed the ending:

    best      >= 23/28 right (115 pts), >= 4 clues, RESCUE first, PUBLIC
    middle    >= 17/28 right  (85 pts), >= 3 clues
    practice  otherwise

What the engine had to learn, all generic (README §6): `fb` as a list, one
line per option, since the export explains every option and that is better
teaching than one line for all four; `routeStory` on any scene, not only an
ending; `ladder`, an ending picked by score, tiles and routes together; and
'resolve' as the target of a story page, so the export's closing page "The
first morning" is read before the ending is decided.

What this builder changed, and why:

- **Every explanation rewritten in the house convention** — grammar forms in
  CAPS, cited words in double quotes, the answer as SUBJECT + FORM. The export
  wrote "Has been working emphasises…" in running lowercase.
- **Six answer keys were the longest option** (HOUSE-STYLE's hard gate). The
  key was trimmed on page 13 ("had already taken" -> "had taken"; the
  sentence keeps "already" in its meaning) and a distractor was replaced on
  pages 17, 19, 20, 22 and 27. Two of the new distractors are near misses —
  first half right, second half wrong (20, 27) — which is a better test of
  the contrast than the export's padding was.
- **Page 19's distractor "has tested / will have"** gave a blank that made no
  verb at all ("will have use"); replaced as part of the length fix.
- Hotspots: the export's `x`/`y` were right on 25 of 30 plates. Moved: the
  key (13), the power socket (21 — the export marked the scanner), the
  evidence paper (23 — it marked Alice's key), the lock light (24), the
  sealed envelope (28) and, on the descent, the cable car itself — the
  "handheld radio" the export named is not legible on the plate.
- The tense guide, the case notebook, the page map, the guest book, the
  teacher room and progress export/import are the export's own modal chrome;
  the engine has none of them and a Block Camp RPG does not carry them. The
  briefing's five cards are the guide condensed.

Pictures: block-camp/grand-hotel-rpg/NN_name.webp, 1672x941.
"""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'grand-hotel-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
PAGES = {p['id']: p for p in DATA['pages']}
LANGS = rpg.NINE


def T(en):
    return {'en': en}


# ── hotspots: [cx, cy, w, h] in % of the 1672x941 picture, panel side,
# vertical anchor, optional panel width %. Every plate here is a crowd scene
# with people on both sides, so the rule that decides is the object's: the
# panel goes on the side away from it. A panel grows 8 points with a gloss on.
HOT = {
    'intro':    ([12, 62, 16, 30], 'right', 'center'),       # the luggage trolley
    'arrival':  ([27, 32, 10, 24], 'right', 'center'),       # Sherpa Tensing, taking your bag
    'rules':    ([80, 80, 16, 12], 'left',  'center', 56),   # the old plans: a guide to the building's time
    'p2':       ([35, 71,  6, 10], 'right', 'center'),       # the brass reception bell
    'p3':       ([42, 60, 10, 22], 'right', 'center'),       # the brass annex key
    'p4':       ([55, 87,  9, 10], 'left',  'center', 42),   # the fallen silver tray
    'p5':       ([53, 55,  9, 18], 'left',  'center', 40),   # the photograph
    'p6':       ([29, 81, 12, 12], 'right', 'center'),       # the lift log
    'p7':       ([90, 76, 10, 16], 'left',  'center'),       # the covered meal tray
    'p8':       ([17, 62, 12, 22], 'right', 'center'),       # the security monitor
    'p9':       ([51, 85, 14, 10], 'right', 'center', 34),   # the torn log page
    'p10':      ([49, 61,  6, 10], 'right', 'center', 38),   # the envelope
    'ally':     ([49, 61,  6, 10], 'right', 'center', 38),
    'p11':      ([93, 76,  8, 16], 'left',  'center'),       # the garden lantern
    'p12':      ([50, 67, 14, 14], 'right', 'center', 34),   # the boat engine
    'p13':      ([92, 74,  8, 16], 'left',  'center'),       # the landing lantern
    'p14':      ([56, 76, 22, 14], 'left',  'center', 40),   # the unfolded floor plan
    'p15':      ([52, 83, 14, 10], 'left',  'center', 34),   # the tied archive folder
    'p16':      ([86, 72,  8, 14], 'left',  'center'),       # the archive clock
    'p17':      ([91, 72, 10, 18], 'left',  'center'),       # the emergency lantern
    'p18':      ([17, 70, 16, 26], 'right', 'center'),       # the station handwheel
    'p19':      ([30, 70, 13, 24], 'right', 'center'),       # the power socket
    'priority': ([30, 70, 13, 24], 'right', 'center'),
    'p20':      ([ 9, 26,  8, 16], 'right', 'center'),       # the green indicator lamp
    'p21':      ([60, 78, 18, 12], 'left',  'center', 40),   # the conflicting plans
    'p22':      ([44, 63,  8, 14], 'right', 'center', 40),   # the evidence paper
    'p23':      ([75, 64,  6, 10], 'left',  'center'),       # the green lock light
    'p24':      ([55, 78, 14, 10], 'left',  'center', 36),   # the signed agreement
    'p25':      ([62, 77,  8, 14], 'left',  'center', 44),   # the evidence camera
    'p26':      ([42, 62, 22, 28], 'right', 'center', 40),   # the security footage
    'p27':      ([36, 63,  8, 12], 'right', 'center', 42),   # the sealed envelope
    'p28':      ([82, 63,  8, 14], 'left',  'center'),       # the cable car going down
    'p29':      ([81, 50,  6, 14], 'left',  'center'),       # the microphone
    'announce': ([81, 50,  6, 14], 'left',  'center'),
    'p30':      ([45, 73, 10, 12], 'right', 'center', 40),   # the brass teapot
    'best':     ([55, 78, 14, 10], 'left',  'center', 36),   # the ownership register
    'middle':   ([62, 77,  8, 14], 'left',  'center', 44),   # Andreas, answering to Lestrade
    'practice': ([82, 63,  8, 14], 'left',  'center'),       # the cable car, one more night
}

# ── the 28 questions. Options are the English being taught and are not
# glossed (HOUSE-STYLE §8). `fb` is one line per option, in option order.
# CHANGED marks an option this builder replaced (see the docstring).
Q = {
    2: (['called / had called', 'has called / called', 'is calling / calls', 'calls / is calling'], 3, [
        'Both forms are past. The sentence is about a routine and about this moment, so it needs present forms.',
        'HAS CALLED is a result and CALLED is a finished past event. Neither says "every evening" or "right now".',
        'This swaps the meanings. A routine takes the simple form, THE OWNER + CALLS; an action in progress takes the continuous.',
        '"Every evening" is a routine: THE OWNER + CALLS. "Right now" is an action in progress: SOMEONE + IS CALLING.']),
    3: (['had seen / has been giving', 'was seeing / gives', 'has seen / gave', 'saw / has just given'], 3, [
        'HAD SEEN needs an earlier past point, and HAS BEEN GIVING is an ongoing activity, not one handover.',
        'One sighting is SAW, not WAS SEEING. GIVES is a routine, not one new handover.',
        '"Yesterday" is a finished time, so SAW, not HAS SEEN. GAVE loses the link to now: we have the key.',
        '"Yesterday" is a finished time: LESTRADE + SAW. A recent action with a result now: THE COUNT + HAS JUST GIVEN.']),
    4: (['was singing / went', 'had sung / have gone', 'sang / were going', 'has sung / go'], 0, [
        'The song was in progress: ZOMBIELLA + WAS SINGING. The blackout interrupted it: THE LIGHTS + WENT out.',
        'HAD SUNG means the song was already over, but she was still singing. HAVE GONE links to now.',
        'SANG makes the whole song one event, and WERE GOING makes the sudden blackout a long background action.',
        'HAS SUNG and GO are present forms. The story is at 20:05, in the past.']),
    5: (['was leaving / have gone', 'has left / went', 'had already left / went', 'leaves / were going'], 2, [
        'WAS LEAVING puts him in the middle of leaving, and HAVE GONE links to now, not to 20:05.',
        'HAS LEFT looks from now. Here we look back from 20:05, a finished past point.',
        'The earlier event: ANDREAS + HAD ALREADY LEFT. The later event: THE LIGHTS + WENT out. His 20:10 story is false.',
        'LEAVES is a present routine. We are putting two finished past events in order.']),
    6: (['worked / was replacing', 'has worked / has been replacing', 'has been working / has replaced', 'is working / replaced'], 2, [
        'WORKED makes the work finished, and WAS REPLACING does not count three finished fuses.',
        'HAS WORKED is possible, but HAS BEEN REPLACING is activity, not three finished results.',
        '"Since seven" and still working: ZOMBITO + HAS BEEN WORKING. Three finished results: HE + HAS REPLACED.',
        'IS WORKING cannot take "since seven", and REPLACED loses the link to now in "so far".']),
    7: (['has known / has been checking', 'knew / had checked', 'has been knowing / checked', 'is knowing / checks'], 0, [
        '"Know" is a state, so the simple form: HUDSON + HAS KNOWN. Activity up to now: KIT + HAS BEEN CHECKING.',
        'KNEW and HAD CHECKED move both facts into the past, but she still knows him and Kit is still checking.',
        '"Know" is a state verb, so not HAS BEEN KNOWING. CHECKED says the checking is finished.',
        '"Know" is a state verb, so not IS KNOWING. CHECKS is a routine, not tonight\'s activity.']),
    8: (['arrived / had entered', 'was arriving / enters', 'has arrived / has entered', 'had arrived / entered'], 0, [
        'The later point: THE COUNT + ARRIVED. The earlier event: ANDREAS + HAD ENTERED.',
        'ENTERS is present. We are telling the whole sequence in the past.',
        'Both events have finished clock times, 20:02 and 20:04, so not HAS + past participle.',
        'This puts HAD on the later event. The earlier one, the entry at 20:02, takes HAD ENTERED.']),
    9: (['repaired / has checked', 'had been repairing / was checking', 'has been repairing / is checking', 'was repairing / had checked'], 1, [
        'REPAIRED does not measure "for over an hour", and HAS CHECKED links to now, not to the alarm.',
        'Activity up to a past event: ZOMBITO + HAD BEEN REPAIRING. In progress at that moment: HE + WAS CHECKING.',
        'These forms look from now. Our point of view is the alarm at 20:05, in the past.',
        'HAD CHECKED says the checking was already finished, but he was still doing it.']),
    10: (['copies / is', 'was copying / had been', 'copied / has been', 'has copied / was'], 2, [
        'COPIES is a habit, and IS cannot carry "since then".',
        'WAS COPYING is not one finished event, and HAD BEEN stops at a past point, not now.',
        '"Yesterday" is a finished time: ALICE + COPIED. A state from then to now: SHE + HAS BEEN.',
        'HAS COPIED does not go with "yesterday", and WAS does not reach now.']),
    11: (['are visiting / have been', 'had visited / go', 'have visited / went', 'visited / have gone'], 2, [
        'ARE VISITING is happening now, and HAVE BEEN does not go with "last Tuesday".',
        'GO turns the dated visit into a present routine.',
        'Experience up to now: THE SISTERS + HAVE VISITED. One finished, dated visit: THEY + WENT.',
        'HAVE GONE does not go with the finished time "last Tuesday".']),
    12: (['has been repairing / has found', 'was repairing / had searched', 'has repaired / has been searching', 'repairs / searched'], 2, [
        'HAS BEEN REPAIRING does not say the repair is done, and HAS FOUND says the search succeeded.',
        'WAS REPAIRING leaves the repair in the past and unfinished, but the search is still going on now.',
        'A finished result: MARA + HAS REPAIRED. Effort that goes on to now: LIA + HAS BEEN SEARCHING.',
        'REPAIRS is a routine, and SEARCHED says the search is over.']),
    13: (['has taken / gives', 'was taking / had given', 'takes / has given', 'had taken / was giving'], 3, [   # key trimmed
        'HAS TAKEN looks from now, not from the moment Brannan arrived.',
        'The guests were already inside, so not WAS TAKING. Vass was in the middle of giving, so not HAD GIVEN.',
        'Present forms cannot tell this past sequence.',
        'Before Brannan arrived: TULLOCH + HAD TAKEN. In progress while he checked: VASS + WAS GIVING.']),
    14: (['used to / is used to', 'would / has used to', 'was using to / uses to', 'is used to / used to'], 0, [
        'A past habit that has ended: USED TO + verb. Something familiar now: BE USED TO + -ING.',
        'WOULD can describe a past habit, but HAS USED TO is not English.',
        'WAS USING TO and USES TO are not English forms.',
        'This swaps them. IS USED TO needs a noun or -ING, and "used to working" is not the past-habit pattern.']),
    15: (['was / locks', 'is / has locked', 'had been / is locking', 'has been / had locked'], 3, [
        'WAS does not carry the locked state up to now, and LOCKS is a routine.',
        'IS cannot carry "since eight", and HAS LOCKED does not place the locking before Cat came.',
        'HAD BEEN stops at a past point, and IS LOCKING is happening now.',
        'A state up to now: THE DOOR + HAS BEEN locked. Before a past event: SOMEONE + HAD LOCKED it.']),
    16: (['will have checked / will be closing', 'has been checking / closed', 'will be checking / will have closed', 'checks / has closed'], 2, [
        'This swaps them: the checking is in progress at 23:30, and the closing is complete by midnight.',
        'HAS BEEN CHECKING and CLOSED look from now and from the past, not from future times.',
        'In progress at a future time: THE REGISTRAR + WILL BE CHECKING. Complete by a deadline: SHE + WILL HAVE CLOSED.',
        'CHECKS is a routine, and HAS CLOSED is a result now, not by midnight.']),
    17: (['was going to fall / carried', 'has fallen / am carrying', 'falls / have carried', 'is going to fall / will carry'], 3, [   # [0] CHANGED
        'WAS GOING TO FALL looks back from the past, and CARRIED is past. We need a prediction and an offer now.',
        'HAS FALLEN says the fall has happened, but the beam is still bending.',
        'FALLS is a general fact or a timetable, and HAVE CARRIED looks back.',
        'Evidence you can see: IT + IS GOING TO FALL. An offer made now: I + WILL CARRY.']),
    18: (['is leaving / has met', 'left / will have met', 'has left / meets', 'leaves / is meeting'], 3, [
        'HAS MET says the meeting has already happened.',
        'LEFT is past, and WILL HAVE MET looks back from a later time.',
        'HAS LEFT is a result now, not tonight\'s timetable.',
        'A timetable: THE LAST CAR + LEAVES. A confirmed arrangement: JAX + IS MEETING.']),
    19: (['has tested / will have', 'will have tested / has to', 'will be testing / is going to', 'had been testing / was going to'], 2, [   # [3] CHANGED
        'HAS TESTED is a result now, and WILL HAVE + "use" is not a verb form.',
        'WILL HAVE TESTED makes the test finished by eleven, and HAS TO is a duty, not his plan.',
        'In progress at a future moment: ZOMBITO + WILL BE TESTING. A plan already made: HE + IS GOING TO use.',
        'HAD BEEN TESTING looks back from the past, and WAS GOING TO is an old plan that may not happen.']),
    20: (['will have been working / will have repaired', 'will have been working / will have been repairing',
          'will be working / has repaired', 'will work / is repairing'], 0, [   # [1] CHANGED
        'Duration up to a future time: ZOMBITO + WILL HAVE BEEN WORKING. Complete by a deadline: HE + WILL HAVE REPAIRED.',
        'The first half is right, but WILL HAVE BEEN REPAIRING measures effort. It does not say the repair is finished.',
        'WILL BE WORKING does not measure the five hours, and HAS REPAIRED looks from now.',
        'WILL WORK does not add up five hours by midnight, and IS REPAIRING is happening now.']),
    21: (['will / arranges', 'was going to / had arranged', 'is going to / has arranged', 'has been going to / was arranging'], 1, [
        'WILL and ARRANGES look forward from now, not back to his plan.',
        'A plan in the past: ANDREAS + WAS GOING TO close. Finished before the discovery: HE + HAD ARRANGED.',
        'IS GOING TO and HAS ARRANGED look from now. We are looking back from the past.',
        'HAS BEEN GOING TO is not English, and WAS ARRANGING leaves the arrangement unfinished.']),
    22: (['was repaired / is being copied', 'is being repaired / has been copied', 'is repaired / was being copied',
          'has been repairing / has been copying'], 1, [   # [3] CHANGED
        'WAS REPAIRED is finished and past, and IS BEING COPIED says the copy is not finished.',
        'Work going on now: THE LOCK + IS BEING REPAIRED. A finished result now: THE SURVEY + HAS BEEN COPIED.',
        'IS REPAIRED is a state or a routine, and WAS BEING COPIED does not say the copy is finished.',
        'These are active forms: they make the lock and the survey do the repairing and the copying.']),
    23: (['has turned / opened', 'will turn / open', 'turns / will open', 'turned / have opened'], 2, [
        'OPENED is past, so it is no longer an instruction about what we will do.',
        'After WHEN, for the future, use the present simple: WHEN THE LIGHT + TURNS, not WILL TURN.',
        'After WHEN, the present simple: THE LIGHT + TURNS. The main clause: WE + WILL OPEN.',
        'TURNED and HAVE OPENED are past and present perfect. Neither gives a future instruction.']),
    24: (['were signing / has signed', 'had signed / is signing', 'signed / had signed', 'have signed / signs'], 2, [
        'WERE SIGNING leaves the signing unfinished, and HAS SIGNED looks from now.',
        'IS SIGNING puts Blocula\'s signature in progress now, but the document is old.',
        '"Last month" is a finished time: THE STAFF + SIGNED. Before the later offer: BLOCULA + HAD SIGNED.',
        '"Last month" needs the past simple, and SIGNS is present.']),
    25: (['has entered / is waiting', 'entered / had been waiting', 'enters / has waited', 'had entered / was waiting'], 1, [
        'These forms look from now, not from 20:04.',
        'The past point: BLOCULA + ENTERED. Activity up to that point: ANDREAS + HAD BEEN WAITING.',
        'Present forms take the sequence out of the finished past.',
        'The Count\'s entry is the reference point, so ENTERED. The waiting started earlier and went on until then: HAD BEEN WAITING.']),
    26: (['has never locked / locked', 'is never locking / had locked', 'had never locked / is locking', 'never locks / has locked'], 0, [
        'Experience up to now: HE + HAS NEVER LOCKED. One dated event at 20:07: HE + LOCKED.',
        'IS NEVER LOCKING is not the form for life experience, and HAD LOCKED needs another past point.',
        'IS LOCKING is happening now, but the camera recorded a finished event.',
        'NEVER LOCKS is a habit, and a finished clock time takes the past simple, not HAS LOCKED.']),
    27: (['will have been waiting / will have given', 'will wait / will be giving',
          'will have been waiting / will be giving', 'has waited / gave'], 0, [   # [2] CHANGED
        'Duration up to 23:50: THE ASSISTANT + WILL HAVE BEEN WAITING. Complete by 23:55: JAX + WILL HAVE GIVEN.',
        'WILL WAIT does not measure the hour, and WILL BE GIVING leaves the handover in progress.',
        'The first half is right, but WILL BE GIVING leaves the handover in progress at 23:55, not complete.',
        'HAS WAITED and GAVE look from now and from the past, not from the future deadlines.']),
    28: (['arrives / will register', 'arrived / would register', 'had arrived / would have registered', 'will arrive / registers'], 0, [
        'A real future possibility: IF + JAX + ARRIVES, then THE REGISTRAR + WILL REGISTER.',
        'ARRIVED / WOULD REGISTER makes the situation imaginary. Tonight it is a real possibility.',
        'HAD ARRIVED / WOULD HAVE REGISTERED is about an unreal past, but the journey is still happening.',
        'After IF, for the future, use the present simple, not WILL ARRIVE.']),
    29: (['was giving / had checked', 'has been giving / checks', 'has given / is checking', 'gives / checked'], 2, [
        'Both forms are past. We need a result now and a check happening now.',
        'HAS BEEN GIVING is a long activity, not one handover, and CHECKS is a routine.',
        'A finished handover with a result now: JAX + HAS GIVEN. In progress now: THE REGISTRAR + IS CHECKING.',
        'GIVES is a routine, and CHECKED makes the check finished and past.']),
}

# ── the three story choices: (scene id, after page, title, line, routes).
# A route is (name, consequence, ROUTE). Points: none — the export's own rule.
CHOICES = {
    10: ('ally', 'Choose your partner',
         'Zombiella or Alice. Whoever you do not choose stays with the frightened guests.',
         [('Trust Zombiella · find the payment', 'Her receipt will expose how the distraction was arranged.', 'ZOMBIELLA'),
          ('Trust Alice · trace the copied key', 'Her key record will show who asked for access to the annex.', 'ALICE')]),
    19: ('priority', 'What gets power first?',
         'The damaged circuit can power one of them at a time.',
         [('The lock · get Blocula out first', 'Protect the owner. The document can be scanned after the rescue.', 'RESCUE'),
          ('The scanner · protect the agreement first', 'Secure an early copy, but leave Blocula in the cold for longer.', 'SCANNER')]),
    29: ('announce', 'How will you handle the truth?',
         'The registrar is reading. The whole hotel is waiting for you to speak.',
         [('Tell the whole staff · share the evidence', "Give everyone the facts and a voice in the hotel's future.", 'PUBLIC'),
          ('Arrange a private settlement first', 'Seek a quieter deal with management before making an announcement.', 'PRIVATE')]),
}
ROUTE_KEY = {'zombiella': 'ZOMBIELLA', 'alice': 'ALICE', 'people': 'RESCUE', 'paper': 'SCANNER'}

ENDINGS = {
    'best': ('25_agreement', 'The hotel belongs to everyone', [
        "The registrar confirms the agreement before midnight. Your timeline and your documents leave no gap "
        "for Andreas to use. Lestrade takes him down the mountain under guard.",
        "At dawn, Elizabeth reads the staff's names from the ownership register. Mrs Hudson says shareholders "
        "can still wash dishes. Zombiella starts a song; this time, nobody has paid her to keep singing.",
        "You protected Blocula first and gave the whole staff a voice. The hotel reopens as a staff-run business."]),
    'middle': ('26_confrontation', 'A future under negotiation', [
        "The agreement reaches the registrar, and your evidence is strong enough to stop a quiet takeover. "
        "Some details need a second check, but the sale is suspended. Andreas must answer to Lestrade.",
        "The staff keep their jobs while Elizabeth and the Count work through the remaining questions. "
        "By breakfast, a handwritten notice replaces the closing sign: OPEN — PLEASE BE PATIENT."]),
    'practice': ('29_descent', 'One more night', [
        "Blocula is safe, Andreas is detained, and the agreement has reached the village. But the evidence has too "
        "many uncertain details for registration tonight. The registrar orders a review of the sale. "
        "The hotel stays open for now.",
        'Holmes asks you to sit beside the fire. "We know what happened. Now we must learn to explain when." '
        "You completed the rescue. Review the tense contrasts and come back to secure the staff's future."]),
}
# the middle ending's last line depends on the road taken — the export's own
# three notes, in its own order of precedence (first key in the route wins)
MIDDLE_NOTE = {
    'SCANNER': 'The early scan helped, but leaving Blocula in the cold cost trust. Victor reminds you that '
               'the best plan protects people as well as papers.',
    'PRIVATE': 'Your private settlement keeps the hotel open, but the staff want a full meeting before they '
               'trust the new arrangement.',
    'PUBLIC': 'The central case is sound. A clearer timeline would have made the transfer immediate.',
}

ACT = lambda n: 'ACT I' if n <= 10 else 'ACT II' if n <= 20 else 'ACT III'

# ── the briefing. Nothing like it in the export beyond an 18-card modal guide;
# these five cards are that guide condensed, one row per time. A card carrying
# a PATTERN keeps its English in every gloss; its name is glossed.
RULES = [
    ('PRESENT · NOW, AND UP TO NOW', 'CHECKS · IS CHECKING · HAS CHECKED · HAS BEEN CHECKING'),
    ('PAST · LOOKING BACK', 'CHECKED · WAS CHECKING · HAD CHECKED · HAD BEEN CHECKING'),
    ('FUTURE · LOOKING AHEAD', 'WILL CHECK · WILL BE CHECKING · WILL HAVE CHECKED · WILL HAVE BEEN CHECKING'),
    ('PLANS, HABITS AND THE PASSIVE', 'IS GOING TO CHECK · USED TO CHECK · IS USED TO CHECKING · IS BEING CHECKED · HAS BEEN CHECKED'),
]
RULES_NOTE = ('SIMPLE: the whole event. CONTINUOUS, BE + -ING: in progress. PERFECT, HAVE + PAST PARTICIPLE: '
              'looking back from a point in time. In every question, read the time word first — "yesterday", '
              '"since seven", "by midnight".')

LABELS = {
    'tiles': T('CLUES'),
    'relic': T('CLUE VERIFIED · +{p} POINTS'),
    # no lives in this game: a wrong answer costs the points and nothing else
    'wrong': T('NO POINTS'),
    'progress': T('TIME CHECKS'),
    'help': T('click the glowing object or ENTER to read · ESC hide · 1-4 answer · '
              'L language · S sound · F fullscreen'),
}


def pages_of(text, limit=60):
    """The export's paragraphs, dealt onto panel pages of up to ~`limit` words.
    A paragraph is never split; a long one gets a page of its own."""
    out, cur = [], []
    for para in [p.strip() for p in text.split('\n') if p.strip()]:
        if cur and len(' '.join(cur + [para]).split()) > limit:
            out.append(' '.join(cur)); cur = []
        cur.append(para)
    if cur:
        out.append(' '.join(cur))
    return [T(p) for p in out]


def place(sid, scene, img):
    hot, pos, v = HOT[sid][:3]
    scene.update({'img': img + '.webp', 'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def build():
    p1 = PAGES[1]
    paras = [l.strip() for l in p1['story'].split('\n') if l.strip()]
    scenes = {
        'intro': place('intro', {
            'kind': 'intro',
            'k': T('FORBES ENGLISH · A BLOCK CAMP MYSTERY'),
            'title': T('THE LAST NIGHT AT THE GRAND HOTEL'),
            'story': T(' '.join(paras[:2])),
            'rules': [T('MIXED TENSES'), T('28 TIME CHECKS'), T('5 CLUES'), T('3 ENDINGS')],
            'start': T('Start the night shift'),
            'small': T('5 points for a right first answer · a wrong answer explains, and the story goes on'),
            'next': 'arrival'}, p1['art']),
        # the cover's third paragraph, on a page of its own: the cover ran to
        # the ceiling of its panel in English before any gloss was added
        'arrival': place('arrival', {
            'kind': 'story',
            'k': T('ACT I · 19:30 · THE MOUNTAIN ROAD'),
            'title': T('Who to trust'),
            'story': T(paras[2]),
            'button': T('Check in'),
            'next': 'rules'}, p1['art']),
        'rules': place('rules', {
            'kind': 'rules',
            'k': T('BEFORE THE NIGHT SHIFT · HOW THE TENSES WORK'),
            'title': T("SHERPA TENSING'S TENSE GUIDE"),
            'rules': [{'name': T(n), 'form': T(f)} for n, f in RULES],
            'note': T(RULES_NOTE),
            'button': T('Go to reception'),
            'next': 'p2'}, PAGES[14]['art']),
    }

    for n in range(2, 30):
        p = PAGES[n]
        opts, ans, fb = Q[n]
        sid = 'p%d' % n
        nxt = CHOICES[n][0] if n in CHOICES else ('p%d' % (n + 1) if n < 29 else 'p30')
        s = {
            'kind': 'question',
            'k': T('%s · %s · %s' % (ACT(n), p['time'], p['place'].upper())),
            'title': T(p['title']),
            'story': pages_of(p['story']),
            'prompt': T(p['question']),
            'opts': [{'en': o} for o in opts],
            'answer': ans, 'points': 5,
            'fb': [T(f) for f in fb],
            'next': nxt,
        }
        if p['clue']:
            c = p['clue']
            s['relic'] = True
            s['fbRight'] = s['fbWrong'] = T('NOTEBOOK · %s. %s' % (c['title'].upper(), c['text']))
        if p['variants']:
            v = p['variants']
            s['routeStory'] = {ROUTE_KEY[k]: T(t) for k, t in v.items() if k != 'key'}
        scenes[sid] = place(sid, s, p['art'])
        if n in CHOICES:
            cid, title, line, routes = CHOICES[n]
            scenes[cid] = place(cid, {
                'kind': 'choice',
                'k': T('STORY DECISION · NO POINTS'),
                'title': T(title), 'story': T(line),
                'routes': [{'name': T(a), 'desc': T(b), 'route': r, 'target': 'p%d' % (n + 1) if n < 29 else 'p30'}
                           for a, b, r in routes],
            }, p['art'])

    p30 = PAGES[30]
    scenes['p30'] = place('p30', {
        'kind': 'story',
        'k': T('00:01 → DAWN · THE GRAND HOTEL'),
        'title': T(p30['title']),
        'story': T(' '.join(l.strip() for l in p30['story'].split('\n'))),
        'button': T('Hear the midnight result'),
        'next': 'resolve'}, p30['art'])
    for eid, (img, title, paras) in ENDINGS.items():
        e = {'kind': 'ending', 'k': T('THE FIRST MORNING · ENDING'), 'title': T(title),
             'story': [T(x) for x in paras]}
        if eid == 'middle':
            e['routeStory'] = {k: T(v) for k, v in MIDDLE_NOTE.items()}
        scenes[eid] = place(eid, e, img)

    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'The Last Night at the Grand Hotel — Mixed Tenses Voxel RPG (B1-B2)',
        'description': 'An interactive B1-B2 English lesson from Forbes English: The Last Night at the '
                       'Grand Hotel — Mixed Tenses Voxel RPG (B1-B2).',
        'langs': LANGS,
        # mixed tenses has no single camp: the hub's gold (README §1)
        'accent': '#e8c04a', 'accent_ink': '#1a1200',
        'deep': '#120c04', 'panel': 'rgba(16,12,8,.88)',
        'labels': LABELS,
        'page_clues': True,
        'start': 'intro', 'scenes': scenes,
        # the ladder decides; these keys are for the camp save (master =
        # best, failed = the try-again ending) and the engine's fallback
        'endings': {'master': 'best', 'complete': 'middle', 'missing': 'practice', 'failed': 'practice'},
        'ladder': [
            {'min': 115, 'tiles': 4, 'route': ['RESCUE', 'PUBLIC'], 'ending': 'best'},
            {'min': 85, 'tiles': 3, 'ending': 'middle'},
            {'ending': 'practice'},
        ],
        'max': 140, 'points': 5, 'tiles': 5, 'chances': 0, 'complete_score': 85,
        'total': 28,
        'img_w': 1672, 'img_h': 941,
    }


def strings(spec):
    """Every English string the page shows, in order, for the translators."""
    out = []
    def walk(o, skip=False):
        if isinstance(o, dict):
            if 'en' in o and isinstance(o['en'], str):
                if not skip and o['en'] not in out:
                    out.append(o['en'])
                return
            for k, v in o.items():
                walk(v, skip or k == 'opts')
        elif isinstance(o, list):
            for v in o:
                walk(v, skip)
    walk(spec['labels']); walk(spec['scenes'])
    return out


if __name__ == '__main__':
    if '--strings' in sys.argv:
        json.dump(strings(build()), sys.stdout, ensure_ascii=False, indent=0)
    else:
        rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
