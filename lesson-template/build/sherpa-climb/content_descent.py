"""The Descent — every word the learner reads, in English (the passive voice).

Innes, 2026-10-05: "Then we make the descent and we need drama, the yak saves
the day on a severe weather rescue mission".

The same cast as The Climb (content.py), going DOWN the route map's descent:
nine passive stops, summit to ground, then "Home to base camp", one line per
passive. More story than the climb (a storm, an accident, a rescue), still
question to question: two lines on arriving at a stop, one on leaving.

THE STORY (keep it true when you change a line)
    Day 14, after the summit. Navya radios a storm warning.
    The storm is forecast for TONIGHT (Navya, the intro).
    Camp 12  the race: the camp taken down, every bag loaded, by six.
    Camp 10  the hut on the way down: its door torn off by the wind, the food
             eaten by birds, the stove taken by the other team (the one that
             cut the steps on the way up). Otto's hat and the spare tent are
             blown away in the night; the team keeps its other tents.
    Camp 7   morning, the radio: the pass will be closed at noon; porters will
             meet them at the lake; no helicopter will be sent. "We'll be
             lowered down the ice wall one at a time. Me last." (Otto)
    Camp 6   the ice wall: Otto, going last, was being lowered when the rope
             jammed; he was swung against the ice and landed on one foot; his
             ankle was being strapped up as the light went.
    Camp 5   Otto can't walk, and the porters never came (they were turned
             back by the snow below camp five). Navya: "You're going to be
             fetched, and I know exactly who by": Momo is sent up.
    Camp 4   the whiteout. Otto has been carried between two of them since
             dawn. Something big with horns has been seen on the ridge: Momo,
             who found them by the smell of Sam's two-week-old socks (The
             Climb, c13-7). Otto is lifted onto Momo's back.
    Camp 3   that night they tell it: led down by a yak, Otto carried all
             afternoon (singing). Momo's dinner: Sam's socks.
    Camp 2   how it works: every yak here is trained for nights like this.
    Camp 1   by the lake, just above base camp: a stretcher is being brought
             up, Otto's ankle is being checked by the doctor, Momo is being
             cheered and brushed by the porters.
    Base camp (the finale): the whole story, once more, one passive at a time.
    Momo is the passive's natural agent ("Otto was carried down BY Momo").

WHAT THE PASSIVE NEEDS FROM THE ITEMS (from the descent pages' own defects,
scratchpad research 2026-10-05):
  * no verb that works both ways in a gap (close, open, break, crack, freeze,
    melt, flood, move, tear, rip, blow away, sink, collapse, change, widen,
    clear, reopen): "the rope broke" and "the rope was broken" are both right;
  * every tense pinned by its own time words (by six / when we got there /
    right now / since lunchtime / last night);
  * typed answers accept the GET passive where a speaker would use it
    ("got lifted"), and any other tense that is genuinely right;
  * BE USED TO is never a cue (ambiguous with the passive of USE);
  * HAS BEEN BEING / WILL BE BEING + participle is never a key (the route
    map's own note: native speakers avoid them).

Shapes are content.py's (read its docstring): CAMPS are the stops in play
order, 'n' is the twin camp, 'storm' 0-3 sets the snow, 'alt' comes from
content.py by twin. Ids 'd<n>-<k>', finale 'r-<k>'. CHROME overrides the
climb's interface English for this game.
"""
import importlib.util as _ilu
import os as _os

_spec = _ilu.spec_from_file_location('_climb', _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'content.py'))
_climb = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_climb)
CAST = _climb.CAST          # the same people: keys ana / doris show as Myra / Navya
VIA = _climb.VIA

CHROME = {
    'title': ('The Descent', "the game's name, the page title; stays English like The Climb"),
    'kicker': ('Passive game', 'small label above the title'),
    'lead': ('Come down the mountain with Tensing and the team. Every camp on the way down is one passive, and a storm is coming.',
             'the line under the title. Tensing is a name'),
    'startOne': ('Start at camp twelve', 'main button: the descent starts at camp twelve, just below the summit'),
    'continueTop': ('Continue: home to base camp', 'main button when every camp is done and only the finale is left'),
    'momo': ('And Momo, the yak at base camp. Remember him.', 'line under the team; Momo is a name and the hero of the descent'),
    'chooseHow': ('The way down has no locks either: start at whichever camp you need.', 'under "Choose a camp"'),
    'mapAria': ('The mountain at night, with a diamond for each passive on the way down. Every camp is also listed here.',
                'aria-label of the descent map'),
    'summitRow': ('Home to base camp · all nine passives', 'the last row of the camp list: the finale'),
    'summitPush': ('Home to base camp', 'the finale, as a heading and a chip'),
    'summitAlt': ('Home to base camp · {alt} m', 'the finale heading with its altitude; keep {alt}'),
    'readFirst': ('Read the lesson first', 'link from a stop to its passive lesson page'),
    'right': ('Right. Down you go.', 'verdict after a right answer (the climb says "Up you go")'),
    'onTo': ('Down to camp {n}', 'button to the next camp on the way down; keep {n}'),
    'onTop': ('On to base camp', 'button from the last camp to the finale'),
    'summitH': ('Base camp', 'heading of the end screen'),
    'seeClimb': ('See your descent', 'end screen, first step: button to the scores'),
    'yourClimb': ('Your descent', 'end screen, second step: heading over the scores'),
    'climbAgain': ('Down again', 'end screen: play the descent again'),
    'wayDown': ('Play The Climb', 'end screen link to the other game, The Climb (stays English)'),
}

INTRO = [
    {'who': 'tensing', 'en': "We made it to the top. Now the hard part: getting down."},
    {'who': 'doris', 'via': 'radio', 'en': "Base camp here. A big storm **has been forecast** for tonight. Get down fast. Over."},
    {'who': 'tensing', 'en': "On the way down, it's not who did it. It's what **was done**."},
]

CAMPS = [
    # ------------------------------------------------------------------ 12  future perfect passive  C1
    {
        'n': 12, 'storm': 0,
        'arrive': [
            {'who': 'ana', 'en': "By six tonight, this camp **will have been taken** down and every bag **will have been loaded**."},
            {'who': 'tensing', 'en': "Then we go. The storm won't wait for anyone."},
        ],
        'tip': "Done before a time in the future, with the doer left out: WILL HAVE BEEN + PAST PARTICIPLE. BY + a time is the deadline; BY + a person (or the snow) is the doer.",
        'items': [
            {'id': 'd12-1', 'kind': 'choose', 'who': 'ana',
             'text': "By the time the storm arrives, we _____ off this ridge by Tensing. (lead)",
             'answer': 'will have been led', 'options': ['will have been led', 'will have been lead', 'will have led'],
             'fb': '"By the time the storm arrives" = done before then, and BY TENSING is the doer: WILL HAVE BEEN + PAST PARTICIPLE. LEAD → LED.'},
            {'id': 'd12-2', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "By tomorrow night, the whole team _____ safely to base camp. I promise. Over. (bring)",
             'answer': 'will have been brought', 'options': ['will have been brought', 'will have been bringed', 'will have brought'],
             'fb': 'The team does not bring; it is brought: WILL HAVE BEEN + PAST PARTICIPLE. BRING → BROUGHT.'},
            {'id': 'd12-3', 'kind': 'type', 'who': 'ana',
             'text': "Go and sleep, Sam. By the time you wake up, every rope _____ twice. (already / check)",
             'answer': 'will already have been checked',
             'accept': ['will already have been checked', 'will have already been checked', 'will have been checked already',
                        'will have been checked', 'will already have got checked', 'will have already got checked',
                        'will already have gotten checked', 'will have already gotten checked', 'is going to have already been checked'],
             'fb': '"By the time you wake up" = done before then: WILL + ALREADY + HAVE BEEN + CHECKED.'},
            {'id': 'd12-4', 'kind': 'choose', 'who': 'sam',
             'text': "_____ the tents _____ before it gets dark? (pack)",
             'answer': 'Will ... have been packed', 'options': ['Will ... have been packed', 'Will ... has been packed', 'Will ... have been pack'],
             'fb': 'A question about a future deadline: WILL + subject + HAVE BEEN + PAST PARTICIPLE?'},
            {'id': 'd12-5', 'kind': 'spot', 'who': 'otto',
             'text': "By the time the snow reaches us, the worst of the ridge [will have been crossed].",
             'answer': 12, 'options': [12, 7, 10],
             'fb': 'WILL HAVE BEEN + CROSSED, done before a future moment: future perfect passive.'},
            {'id': 'd12-6', 'kind': 'choose', 'who': 'ana',
             'text': "By six, Tensing _____ every peg out of the ice. (pull)",
             'answer': 'will have pulled', 'options': ['will have pulled', 'will have been pulled', 'will has pulled'],
             'fb': 'Tensing does the pulling, so this one is active: WILL HAVE + PAST PARTICIPLE. A passive needs BEEN, and the thing as the subject.'},
            {'id': 'd12-7', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "The forecast says that by midnight, the lower path _____ by snow. Over. (cover)",
             'answer': 'will have been covered',
             'accept': ['will have been covered', 'will be covered', 'is going to have been covered', 'is going to be covered',
                        'will get covered', 'is going to get covered', 'will have got covered', 'will have gotten covered',
                        'will have been completely covered', 'will be completely covered'],
             'fb': '"by midnight" = done before then: WILL HAVE BEEN + COVERED. BY SNOW is what does it.'},
            {'id': 'd12-8', 'kind': 'choose', 'who': 'otto',
             'text': "The hut _____ by the time we get there, so we'll light the stove ourselves. (not / heat)",
             'answer': "won't have been heated", 'options': ["won't have been heated", "won't have been heat", "won't has been heated"],
             'fb': "Not done before a future moment: WON'T HAVE BEEN + PAST PARTICIPLE."},
        ],
        'done': {'who': 'tensing', 'en': "Packs on. By tonight, every footprint up here **will have been buried**."},
    },
    # ------------------------------------------------------------------ 10  past perfect passive  B2
    {
        'n': 10, 'storm': 1,
        'arrive': [
            {'who': 'otto', 'en': "When we reached the hut, the door **had been torn** off by the wind."},
            {'who': 'sam', 'en': "And our food **had been eaten**! By birds, I hope."},
        ],
        'tip': "Done before a past moment, doer left out: HAD BEEN + PAST PARTICIPLE. Find the later past first.",
        'items': [
            {'id': 'd10-1', 'kind': 'choose', 'who': 'ana',
             'text': "When we got back to the ledge, our spare rope _____ under a metre of snow. (bury)",
             'answer': 'had been buried', 'options': ['had been buried', 'had buried', 'had been bury'],
             'fb': '"When we got back" is the later past; the snow came first: HAD BEEN + PAST PARTICIPLE.'},
            {'id': 'd10-2', 'kind': 'choose', 'who': 'otto',
             'text': "By the time we arrived, the stove _____ by the other team. (take)",
             'answer': 'had been taken', 'options': ['had been taken', 'had been took', 'has been taken'],
             'fb': '"By the time we arrived" looks back from the past: HAD BEEN + PAST PARTICIPLE. TAKE → TAKEN.'},
            {'id': 'd10-3', 'kind': 'type', 'who': 'sam', 'via': 'diary',
             'text': "When we found Otto's hat this morning, it _____ two hundred metres by the wind. (blow)",
             'answer': 'had been blown',
             'accept': ['had been blown', 'had been blown away', 'had got blown', 'had gotten blown', 'had got blown away',
                        'had gotten blown away', 'had already been blown', 'had already been blown away'],
             'fb': 'Before we found it, BY THE WIND: HAD BEEN + PAST PARTICIPLE. BLOW → BLOWN.'},
            {'id': 'd10-4', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "_____ the radio _____ before the storm hit? It's your only line to me. Over. (charge)",
             'answer': 'Had ... been charged', 'options': ['Had ... been charged', 'Has ... been charged', 'Had ... been charge'],
             'fb': 'A question about before a past moment: HAD + subject + BEEN + PAST PARTICIPLE?'},
            {'id': 'd10-5', 'kind': 'spot', 'who': 'otto',
             'text': "We [were roped] together by Tensing, so nobody fell far.",
             'answer': 3, 'options': [3, 10, 7],
             'fb': 'WERE + ROPED: events told in order, then "so". Past simple passive; camp ten would be HAD BEEN ROPED.'},
            {'id': 'd10-6', 'kind': 'choose', 'who': 'sam',
             'text': "Whatever it was, it _____ the night before we arrived. (happen)",
             'answer': 'had happened', 'options': ['had happened', 'had been happened', 'was happened'],
             'fb': 'HAPPEN takes no object, so it has no passive: HAD + HAPPENED.'},
            {'id': 'd10-7', 'kind': 'type', 'who': 'ana',
             'text': "By the time the wind dropped, our spare tent _____ halfway to camp nine. (carry)",
             'answer': 'had been carried',
             'accept': ['had been carried', 'had already been carried', 'had got carried', 'had gotten carried',
                        'had been carried away', 'had already got carried', 'had already gotten carried'],
             'fb': '"By the time the wind dropped" is the later past: HAD BEEN + CARRIED.'},
            {'id': 'd10-8', 'kind': 'choose', 'who': 'otto',
             'text': "I knew that part was dangerous. I _____ about the ice by Tensing. (warn)",
             'answer': 'had been warned', 'options': ['had been warned', 'had warned', 'had been warn'],
             'fb': 'Warned before I knew: HAD BEEN + PAST PARTICIPLE. BY TENSING is the doer.'},
        ],
        'done': {'who': 'sam', 'en': "Nobody slept. By dawn, snow **had been blown** in through every crack."},
    },
    # ------------------------------------------------------------------ 7  future simple passive  B1
    {
        'n': 7, 'storm': 2,
        'arrive': [
            {'who': 'doris', 'via': 'radio', 'en': "The pass **will be closed** at noon. After that, you're on your own. Over."},
            {'who': 'tensing', 'en': "Then we go now. Anyone who falls behind **will be roped** to me."},
        ],
        'tip': "Promises, notices and predictions, doer left out: WILL BE + PAST PARTICIPLE.",
        'items': [
            {'id': 'd7-1', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Don't worry. You _____ at the lake by two of our porters. Over. (meet)",
             'answer': 'will be met', 'options': ['will be met', 'will be meet', 'will meet'],
             'fb': 'A promise, and the porters do the meeting: WILL BE + PAST PARTICIPLE. MEET → MET.'},
            {'id': 'd7-2', 'kind': 'choose', 'who': 'ana',
             'text': "No helicopter _____ in this wind. It's too dangerous. (send)",
             'answer': 'will be sent', 'options': ['will be sent', 'will send', 'will be send'],
             'fb': 'A helicopter does not send; it is sent: WILL BE + PAST PARTICIPLE. SEND → SENT.'},
            {'id': 'd7-3', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "Your families _____ tonight that you are safe. Over. (tell)",
             'answer': 'will be told',
             'accept': ['will be told', 'are going to be told', 'are being told', 'will get told', 'are going to get told', 'are getting told'],
             'fb': 'A promise, doer left out: WILL BE + TOLD.'},
            {'id': 'd7-4', 'kind': 'choose', 'who': 'sam',
             'text': "_____ Otto's bag _____ by someone else? He's got the radio too. (carry)",
             'answer': 'Will ... be carried', 'options': ['Will ... be carried', 'Will ... be carry', 'Will ... carried'],
             'fb': 'A question about the future, doer at the end: WILL + subject + BE + PAST PARTICIPLE?'},
            {'id': 'd7-5', 'kind': 'spot', 'who': 'ana',
             'text': "The ropes [are going to be fixed] before we start down the ice.",
             'answer': 5, 'options': [5, 7, 12],
             'fb': 'ARE GOING TO BE + FIXED: already planned. Going-to passive, not camp seven.'},
            {'id': 'd7-6', 'kind': 'choose', 'who': 'otto',
             'text': "The lower path _____ until tomorrow, so we'll take the ice wall. (not / dig out)",
             'answer': "won't be dug out", 'options': ["won't be dug out", "won't dug out", "won't be dig out"],
             'fb': "Not done in the future, doer left out: WON'T BE + PAST PARTICIPLE. DIG → DUG."},
            {'id': 'd7-7', 'kind': 'type', 'who': 'ana',
             'text': "Everything heavy _____ here, and we'll come back for it in spring. (leave)",
             'answer': 'will be left',
             'accept': ['will be left', 'is going to be left', 'is being left', 'will have to be left', 'is going to have to be left', 'will get left'],
             'fb': 'Decided now, doer left out: WILL BE + LEFT.'},
            {'id': 'd7-8', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "This time you'll be called by _____, not by the weather station. Noon. Over.",
             'answer': 'us', 'options': ['us', 'we', 'our'],
             'fb': 'After BY comes the object form: US, not WE.'},
        ],
        'done': {'who': 'otto', 'en': "Right. We**'ll be lowered** down the ice wall one at a time. Me last."},
    },
    # ------------------------------------------------------------------ 6  past continuous passive  B2
    {
        'n': 6, 'storm': 3,
        'arrive': [
            {'who': 'ana', 'en': "Otto went last, like he said. Halfway down the ice wall, the rope jammed."},
            {'who': 'sam', 'en': "He **was being swung** against the ice like a bell. Then it gave, and he landed on one foot."},
        ],
        'tip': "In the middle of being done when something else happened: WAS / WERE + BEING + PAST PARTICIPLE.",
        'items': [
            {'id': 'd6-1', 'kind': 'type', 'who': 'sam',
             'text': "Otto _____ down the ice wall when the torch went out. (lower)",
             'answer': 'was being lowered', 'accept': ['was being lowered', 'was getting lowered', 'was lowering'],
             'fb': 'In the middle of it when the torch went out: WAS + BEING + LOWERED.'},
            {'id': 'd6-2', 'kind': 'choose', 'who': 'ana',
             'text': "While his ankle _____, Otto kept making jokes. (strap up)",
             'answer': 'was being strapped up', 'options': ['was being strapped up', 'was strapping up', 'were being strapped up'],
             'fb': 'The ankle does not strap itself: WAS + BEING + PAST PARTICIPLE. One ankle: WAS.'},
            {'id': 'd6-3', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "I couldn't hear you. My radio _____ when you called. Over. (repair)",
             'answer': 'was being repaired', 'options': ['was being repaired', 'was repairing', 'was been repaired'],
             'fb': 'In the middle of it when you called: WAS + BEING + PAST PARTICIPLE. BEEN is for the perfect.'},
            {'id': 'd6-4', 'kind': 'choose', 'who': 'otto',
             'text': "_____ the rope _____ properly when it jammed, or did it just catch on the ice? (hold)",
             'answer': 'Was ... being held', 'options': ['Was ... being held', 'Was ... been held', 'Were ... being held'],
             'fb': 'A question about a moment in the past: WAS + subject + BEING + PAST PARTICIPLE?'},
            {'id': 'd6-5', 'kind': 'spot', 'who': 'ana',
             'text': "The rope [had been checked] twice, but it still jammed.",
             'answer': 10, 'options': [10, 6, 12],
             'fb': 'HAD BEEN + CHECKED: done before the moment it jammed. Past perfect passive, not camp six.'},
            {'id': 'd6-6', 'kind': 'choose', 'who': 'sam',
             'text': "Two of our bags _____ towards the edge by the wind as we came down. (drag)",
             'answer': 'were being dragged', 'options': ['were being dragged', 'was being dragged', 'were dragging'],
             'fb': 'In progress as we came down, and two bags: WERE + BEING + PAST PARTICIPLE.'},
            {'id': 'd6-7', 'kind': 'choose', 'who': 'ana',
             'text': "It wasn't Sam's fault. The rope _____ by anyone at that point; it just caught on the ice. (not / pull)",
             'answer': "wasn't being pulled", 'options': ["wasn't being pulled", "weren't being pulled", "wasn't pulling"],
             'fb': "Not in progress at that moment, and one rope: WASN'T + BEING + PAST PARTICIPLE."},
            {'id': 'd6-8', 'kind': 'choose', 'who': 'otto',
             'text': "Everything was chaos. Snow _____ into our faces the whole time. (throw)",
             'answer': 'was being thrown', 'options': ['was being thrown', 'was been thrown', 'was being threw'],
             'fb': 'The background of the story: WAS + BEING + PAST PARTICIPLE. THROW → THROWN.'},
        ],
        'done': {'who': 'sam', 'en': "As the light went, Otto **was being wrapped** in every jacket we had."},
    },
    # ------------------------------------------------------------------ 5  going-to passive  B1
    {
        'n': 5, 'storm': 3,
        'arrive': [
            {'who': 'ana', 'via': 'radio', 'en': "Navya, Otto can't walk and the porters haven't come. We**'re going to be snowed in** up here. Over."},
            {'who': 'doris', 'via': 'radio', 'en': "Not tonight you're not. You**'re going to be fetched**, and I know exactly who by. Over."},
        ],
        'tip': "Already decided, or you can see it coming, doer left out: AM / IS / ARE + GOING TO BE + PAST PARTICIPLE.",
        'items': [
            {'id': 'd5-1', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Listen. Momo _____ up to you tonight. He knows the path. Over. (send)",
             'answer': 'is going to be sent', 'options': ['is going to be sent', 'is going to send', 'is going be sent'],
             'fb': 'Already decided, and Momo is not the sender: IS + GOING TO BE + SENT. Keep the TO.'},
            {'id': 'd5-2', 'kind': 'choose', 'who': 'sam',
             'text': "Look at that sky! We _____ in here by the snow. (trap)",
             'answer': 'are going to be trapped', 'options': ['are going to be trapped', 'are going to trap', 'are going to be trap'],
             'fb': 'You can see it coming: ARE + GOING TO BE + PAST PARTICIPLE.'},
            {'id': 'd5-3', 'kind': 'type', 'who': 'ana',
             'text': "It's decided: Otto's pack _____ between the three of us. (share)",
             'answer': 'is going to be shared',
             'accept': ['is going to be shared', 'will be shared', 'is being shared', 'is going to get shared', 'is to be shared'],
             'fb': '"It\'s decided" = a plan, doer left out: IS + GOING TO BE + SHARED.'},
            {'id': 'd5-4', 'kind': 'choose', 'who': 'otto',
             'text': "_____ I _____ down by a yak? Seriously? (carry)",
             'answer': 'Am ... going to be carried', 'options': ['Am ... going to be carried', 'Do ... going to be carried', 'Am ... going to carried'],
             'fb': 'A question about the plan: AM + I + GOING TO BE + PAST PARTICIPLE? Not DO.'},
            {'id': 'd5-5', 'kind': 'spot', 'who': 'doris', 'via': 'radio',
             'text': "Momo [will be given] a big bag of carrots when he gets back. Over.",
             'answer': 7, 'options': [7, 5, 2],
             'fb': 'WILL BE + GIVEN: a promise. Future simple passive, not GOING TO.'},
            {'id': 'd5-6', 'kind': 'choose', 'who': 'ana',
             'text': "Look how fast it's falling. Our tracks _____ under the snow by morning. (hide)",
             'answer': 'are going to be hidden', 'options': ['are going to be hidden', 'are going to be hide', 'is going to be hidden'],
             'fb': '"Look how fast it\'s falling" = you can see it coming, and "tracks" is plural: ARE + GOING TO BE + PAST PARTICIPLE. HIDE → HIDDEN.'},
            {'id': 'd5-7', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "The old path _____ with flags until spring, so Momo will find his own way. Over. (not / be going to / mark)",
             'answer': "isn't going to be marked", 'accept': ["isn't going to be marked", "isn't going to get marked"],
             'fb': "Already decided, negative: ISN'T + GOING TO BE + MARKED."},
            {'id': 'd5-8', 'kind': 'choose', 'who': 'sam',
             'text': "Momo _____ by the wind at all. Yaks love storms! (not / bother)",
             'answer': "isn't going to be bothered", 'options': ["isn't going to be bothered", "doesn't going to be bothered", "isn't going to bothered"],
             'fb': "You can see it coming, negative: ISN'T + GOING TO BE + PAST PARTICIPLE. Not DOESN'T."},
        ],
        'done': {'who': 'tensing', 'en': "At first light we go on, Otto between us. We**'re going to be found**. We have to be."},
    },
    # ------------------------------------------------------------------ 4  present perfect passive  B1
    {
        'n': 4, 'storm': 3,
        'arrive': [
            {'who': 'ana', 'via': 'radio', 'en': "Navya, Otto **has been carried** between two of us since dawn, and now something **has been seen** on the ridge. Something big, with horns. Over."},
            {'who': 'doris', 'via': 'radio', 'en': "Then stay where you are. That's Momo, and he**'s** never **been beaten** by a storm. Over."},
        ],
        'tip': "Done, with a line to now, doer left out: HAS / HAVE BEEN + PAST PARTICIPLE.",
        'items': [
            {'id': 'd4-1', 'kind': 'choose', 'who': 'sam',
             'text': "Listen! Momo's bell _____! He's right above us! (just / hear)",
             'answer': 'has just been heard', 'options': ['has just been heard', 'has just heard', 'have just been heard'],
             'fb': 'Moments ago, with the news now, and one bell: HAS + JUST + BEEN + PAST PARTICIPLE.'},
            {'id': 'd4-2', 'kind': 'choose', 'who': 'sam',
             'text': "We _____ by smell! Momo followed my two-week-old socks! (find)",
             'answer': 'have been found', 'options': ['have been found', 'have found', 'has been found'],
             'fb': 'Done, with the result now, and "we": HAVE BEEN + PAST PARTICIPLE. FIND → FOUND.'},
            {'id': 'd4-3', 'kind': 'type', 'who': 'otto',
             'text': "The path _____ since lunchtime, so Momo is finding his own way. (bury)",
             'answer': 'has been buried',
             'accept': ['has been buried', 'has got buried', 'has gotten buried', 'has been getting buried', 'has been completely buried', 'has completely been buried'],
             'fb': '"since lunchtime", up to now: HAS BEEN + BURIED.'},
            {'id': 'd4-4', 'kind': 'choose', 'who': 'otto',
             'text': "_____ the straps on Momo _____ yet? I'm not falling off a yak. (check)",
             'answer': 'Have ... been checked', 'options': ['Have ... been checked', 'Have ... checked', 'Has ... been checked'],
             'fb': 'A question about up to now, and "straps": HAVE + subject + BEEN + PAST PARTICIPLE?'},
            {'id': 'd4-5', 'kind': 'spot', 'who': 'sam',
             'text': "Momo [was sent] up by Navya last night.",
             'answer': 3, 'options': [3, 4, 6],
             'fb': 'WAS + SENT with "last night": a finished time. Past simple passive, not camp four.'},
            {'id': 'd4-6', 'kind': 'choose', 'who': 'ana',
             'text': "Two of our tents _____ since we got here. (damage)",
             'answer': 'have been damaged', 'options': ['have been damaged', 'have damaged', 'have been damage'],
             'fb': '"since we got here", up to now: HAVE BEEN + PAST PARTICIPLE.'},
            {'id': 'd4-7', 'kind': 'type', 'who': 'ana',
             'text': "Otto's ankle _____ again since lunchtime, so it's much better now. (strap up)",
             'answer': 'has been strapped up',
             'accept': ['has been strapped up', 'has been strapped', 'has got strapped up', 'has gotten strapped up'],
             'fb': '"since lunchtime", and the result is here now: HAS BEEN + STRAPPED UP.'},
            {'id': 'd4-8', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "I _____ by the weather station: the storm will end tonight. Over. (tell)",
             'answer': 'have been told', 'options': ['have been told', 'have told', 'has been told'],
             'fb': 'News with a line to now, and "I": HAVE BEEN + PAST PARTICIPLE. TELL → TOLD.'},
        ],
        'done': {'who': 'otto', 'en': "I**'ve been lifted** onto a yak. Nearly forty years of climbing, and this is how I go home."},
    },
    # ------------------------------------------------------------------ 3  past simple passive  B1
    {
        'n': 3, 'storm': 2,
        'arrive': [
            {'who': 'ana', 'en': "In the whiteout, we **were led** down by a yak. Nobody **was lost**."},
            {'who': 'sam', 'en': "And Otto **was carried** all afternoon on Momo's back. He sang the whole time."},
        ],
        'tip': "Finished, doer left out or put back with BY: WAS / WERE + PAST PARTICIPLE.",
        'items': [
            {'id': 'd3-1', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "How _____ you _____ in all that snow? Over. (find)",
             'answer': 'were ... found', 'options': ['were ... found', 'was ... found', 'were ... find'],
             'fb': 'A question about a finished event, and "you": WERE + "you" + PAST PARTICIPLE?'},
            {'id': 'd3-2', 'kind': 'choose', 'who': 'sam',
             'text': "The way down _____ by Momo, not by us! (choose)",
             'answer': 'was chosen', 'options': ['was chosen', 'was choosed', 'were chosen'],
             'fb': 'Finished, BY MOMO is the point, and one way: WAS + PAST PARTICIPLE. CHOOSE → CHOSEN.'},
            {'id': 'd3-3', 'kind': 'type', 'who': 'otto',
             'text': "This morning, I _____ onto Momo's back by Tensing and Sam. (lift)",
             'answer': 'was lifted', 'accept': ['was lifted', 'got lifted', 'was lifted up', 'got lifted up', 'was carefully lifted'],
             'fb': '"This morning" is finished, and the doers come after BY: WAS + LIFTED.'},
            {'id': 'd3-4', 'kind': 'choose', 'who': 'ana',
             'text': "The bridge over the stream _____ in 1998, the year Otto first came here. (build)",
             'answer': 'was built', 'options': ['was built', 'was build', 'has been built'],
             'fb': '"in 1998" = a finished time: WAS + PAST PARTICIPLE. BUILD → BUILT.'},
            {'id': 'd3-5', 'kind': 'spot', 'who': 'sam',
             'text': "Momo [is called] the hero of the valley now.",
             'answer': 2, 'options': [2, 3, 1],
             'fb': 'IS + CALLED: how things are now. Present simple passive, not camp three.'},
            {'id': 'd3-6', 'kind': 'choose', 'who': 'otto',
             'text': "My ankle _____ by a rock, not by the rope. (hurt)",
             'answer': 'was hurt', 'options': ['was hurt', 'was hurted', 'hurt'],
             'fb': 'Finished, with the cause after BY: WAS + HURT. HURT never changes.'},
            {'id': 'd3-7', 'kind': 'type', 'who': 'ana',
             'text': "The porters _____ back by the snow below camp five. That's why Momo came. (turn)",
             'answer': 'were turned back', 'accept': ['were turned back', 'got turned back', 'had been turned back'],
             'fb': 'A finished event, and "porters": WERE + TURNED BACK.'},
            {'id': 'd3-8', 'kind': 'choose', 'who': 'sam',
             'text': "It all _____ so fast. One minute, whiteout; the next minute, Momo! (happen)",
             'answer': 'happened', 'options': ['happened', 'was happened', 'were happened'],
             'fb': 'HAPPEN takes no object, so it has no passive: just HAPPENED.'},
        ],
        'done': {'who': 'tensing', 'en': "That night, Momo **was given** the best dinner on the mountain: Sam's socks."},
    },
    # ------------------------------------------------------------------ 2  present simple passive  A2
    {
        'n': 2, 'storm': 1,
        'arrive': [
            {'who': 'ana', 'via': 'radio', 'en': "Navya, how does a yak find people in a whiteout? Over."},
            {'who': 'doris', 'via': 'radio', 'en': "Every yak here **is trained** for nights like that. And Momo **is** never **told** the way. He just knows. Over."},
        ],
        'tip': "Facts, routines and how things are done, doer left out: AM / IS / ARE + PAST PARTICIPLE.",
        'items': [
            {'id': 'd2-1', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Momo _____ twice a day, morning and evening. Over. (feed)",
             'answer': 'is fed', 'options': ['is fed', 'is feed', 'are fed'],
             'fb': 'A routine, and Momo is one yak: IS + PAST PARTICIPLE. FEED → FED.'},
            {'id': 'd2-2', 'kind': 'choose', 'who': 'ana',
             'text': "Rescues like this _____ by radio from base camp. (organise)",
             'answer': 'are organised', 'options': ['are organised', 'are organise', 'is organised'],
             'fb': 'How things are done, and "rescues" is plural: ARE + PAST PARTICIPLE.'},
            {'id': 'd2-3', 'kind': 'type', 'who': 'sam',
             'text': "Every winter, the yaks _____ down in the valley. (keep)",
             'answer': 'are kept', 'accept': ['are kept', 'get kept', 'are always kept', 'are usually kept'],
             'fb': '"Every winter" = a routine, and "yaks": ARE + KEPT.'},
            {'id': 'd2-4', 'kind': 'choose', 'who': 'otto',
             'text': "_____ yaks ever _____ that high in a storm? (see)",
             'answer': 'Are ... seen', 'options': ['Are ... seen', 'Do ... seen', 'Are ... see'],
             'fb': 'A question about what usually happens: ARE + subject + PAST PARTICIPLE? Not DO.'},
            {'id': 'd2-5', 'kind': 'spot', 'who': 'doris', 'via': 'radio',
             'text': "A bed [is being made up] for Otto right now. Over.",
             'answer': 1, 'options': [1, 2, 4],
             'fb': 'IS BEING + MADE UP with "right now": happening now. Present continuous passive, not camp two.'},
            {'id': 'd2-6', 'kind': 'choose', 'who': 'ana',
             'text': "In this valley, yaks _____ by everyone. (love)",
             'answer': 'are loved', 'options': ['are loved', 'are love', 'is loved'],
             'fb': 'A general fact, and "yaks": ARE + PAST PARTICIPLE.'},
            {'id': 'd2-7', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "Hot soup _____ at base camp every night at seven. It always has been. Over. (serve)",
             'answer': 'is served', 'accept': ['is served', 'gets served', 'is always served', 'is usually served'],
             'fb': '"every night" = a routine: IS + SERVED.'},
            {'id': 'd2-8', 'kind': 'choose', 'who': 'sam',
             'text': "Cheese _____ from yak milk up here. It's delicious! (make)",
             'answer': 'is made', 'options': ['is made', 'is make', 'makes'],
             'fb': 'How things are done: IS + PAST PARTICIPLE. MAKE → MADE, and FROM for what it is made of.'},
        ],
        'done': {'who': 'sam', 'en': "Momo's bell **is heard** before he is seen. Best sound in the world."},
    },
    # ------------------------------------------------------------------ 1  present continuous passive  B1
    {
        'n': 1, 'storm': 0,
        'arrive': [
            {'who': 'doris', 'via': 'radio', 'en': "I can see you through the telescope! A stretcher **is being brought** up to meet you. Over."},
            {'who': 'sam', 'en': "And Momo **is being cheered** by the porters coming up the path!"},
        ],
        'tip': "Being done right now, doer left out: AM / IS / ARE + BEING + PAST PARTICIPLE.",
        'items': [
            {'id': 'd1-1', 'kind': 'choose', 'who': 'ana',
             'text': "Look! A big pot of soup _____ for us down there! (make)",
             'answer': 'is being made', 'options': ['is being made', 'is making', 'is been made'],
             'fb': '"Look!" = happening now, and soup does not make itself: IS + BEING + PAST PARTICIPLE.'},
            {'id': 'd1-2', 'kind': 'choose', 'who': 'ana', 'via': 'radio',
             'text': "Navya, Otto's ankle _____ by the doctor right now. Over. (check)",
             'answer': 'is being checked', 'options': ['is being checked', 'is checking', 'is been checked'],
             'fb': '"right now", done by the doctor: IS + BEING + PAST PARTICIPLE. BEEN is for the perfect.'},
            {'id': 'd1-3', 'kind': 'type', 'who': 'sam',
             'text': "Listen! Our names _____ on the radio in Kathmandu! (read out)",
             'answer': 'are being read out',
             'accept': ['are being read out', 'are being read', 'are getting read out', 'are being read out loud', 'are being read aloud'],
             'fb': '"Listen!" = happening now: ARE + BEING + READ OUT.'},
            {'id': 'd1-4', 'kind': 'choose', 'who': 'otto',
             'text': "Why _____ I still _____? I can almost walk now. (carry)",
             'answer': 'am ... being carried', 'options': ['am ... being carried', 'do ... being carried', 'am ... been carried'],
             'fb': 'A question about right now: AM + I + BEING + PAST PARTICIPLE? Not DO.'},
            {'id': 'd1-5', 'kind': 'spot', 'who': 'ana',
             'text': "Otto's ankle [was strapped up] at the ice wall.",
             'answer': 3, 'options': [3, 10, 1],
             'fb': 'WAS + STRAPPED UP: finished in the past. Past simple passive, not camp one.'},
            {'id': 'd1-6', 'kind': 'choose', 'who': 'sam',
             'text': "Momo _____ by two of the porters at the moment, and he loves it. (brush)",
             'answer': 'is being brushed', 'options': ['is being brushed', 'is brushing', 'is been brushed'],
             'fb': '"at the moment", and the porters are doing it to Momo: IS + BEING + PAST PARTICIPLE.'},
            {'id': 'd1-7', 'kind': 'type', 'who': 'ana',
             'text': "Right now we _____ down to base camp by Momo. (lead)",
             'answer': 'are being led', 'accept': ['are being led', 'are getting led'],
             'fb': '"Right now", BY MOMO: ARE + BEING + LED. LEAD → LED.'},
            {'id': 'd1-8', 'kind': 'choose', 'who': 'sam',
             'text': "Momo _____ any more. Otto's on the stretcher now. (not / ride)",
             'answer': "isn't being ridden", 'options': ["isn't being ridden", "isn't being rode", "aren't being ridden"],
             'fb': 'Not happening now, and Momo is one yak: ISN\'T + BEING + PAST PARTICIPLE. RIDE → RIDDEN.'},
        ],
        'done': {'who': 'tensing', 'en': "Base camp, just below. Every one of us **is being brought** home."},
    },
]

# The finale: home to base camp, the whole story once more, one line per passive.
SUMMIT = {
    'n': 'summit', 'alt': 2950, 'top': 2800, 'storm': 0,
    'arrive': [
        {'who': 'doris', 'en': "Welcome home! The coffee **has been made** and Momo **has been fed**. Now sit down and tell me everything."},
    ],
    'tip': "Every passive is BE in some tense + PAST PARTICIPLE. Find the tense of BE.",
    'items': [
        {'id': 'r-1', 'camp': 12, 'kind': 'choose', 'who': 'doris',
         'text': "By tomorrow, your story _____ to every climber in Nepal! (tell)",
         'answer': 'will have been told', 'options': ['will have been told', 'will have told', 'will has been told'],
         'fb': '"By tomorrow" = done before then: WILL HAVE BEEN + PAST PARTICIPLE. Camp twelve.'},
        {'id': 'r-2', 'camp': 10, 'kind': 'choose', 'who': 'sam',
         'text': "When we got to the hut, our food _____ by birds. (eat)",
         'answer': 'had been eaten', 'options': ['had been eaten', 'had eaten', 'had been ate'],
         'fb': 'Before we got there: HAD BEEN + PAST PARTICIPLE. EAT → EATEN. Camp ten.'},
        {'id': 'r-3', 'camp': 7, 'kind': 'type', 'who': 'ana',
         'text': "Next year, a new hut _____ on the ledge. I promise. (will / build)",
         'answer': 'will be built', 'accept': ['will be built', 'will get built'],
         'fb': 'A promise about next year, doer left out: WILL BE + BUILT. Camp seven.'},
        {'id': 'r-4', 'camp': 6, 'kind': 'choose', 'who': 'otto',
         'text': "I _____ down the ice wall when the rope jammed. (lower)",
         'answer': 'was being lowered', 'options': ['was being lowered', 'were being lowered', 'was been lowered'],
         'fb': 'In the middle of it when the rope jammed, and "I": WAS + BEING + PAST PARTICIPLE. Camp six.'},
        {'id': 'r-5', 'camp': 5, 'kind': 'choose', 'who': 'doris',
         'text': "Look at Momo's face. He _____ a medal, and he knows it! (give)",
         'answer': 'is going to be given', 'options': ['is going to be given', 'is going to give', 'is going be given'],
         'fb': 'You can see it coming: IS + GOING TO BE + PAST PARTICIPLE. Camp five.'},
        {'id': 'r-6', 'camp': 4, 'kind': 'choose', 'who': 'sam',
         'text': "My socks _____ by Momo. All of them. (eat)",
         'answer': 'have been eaten', 'options': ['have been eaten', 'have eaten', 'has been eaten'],
         'fb': 'Done, and the result is here now (no socks): HAVE BEEN + PAST PARTICIPLE. Camp four.'},
        {'id': 'r-7', 'camp': 3, 'kind': 'type', 'who': 'otto',
         'text': "Two days ago, I _____ down a mountain by a yak. Nobody will believe me. (carry)",
         'answer': 'was carried', 'accept': ['was carried', 'got carried'],
         'fb': '"Two days ago" is finished, BY A YAK: WAS + CARRIED. Camp three.'},
        {'id': 'r-8', 'camp': 2, 'kind': 'choose', 'who': 'doris',
         'text': "Here, every climber _____ a hot drink on arrival. (hand)",
         'answer': 'is handed', 'options': ['is handed', 'is hand', 'hands'],
         'fb': 'How things are done here: IS + PAST PARTICIPLE. Camp two.'},
        {'id': 'r-9', 'camp': 1, 'kind': 'spot', 'who': 'doris',
         'text': "A cake [is being baked] for Momo right now.",
         'answer': 1, 'options': [1, 2, 5],
         'fb': 'IS BEING + BAKED, "right now": present continuous passive. Camp one.'},
    ],
    'done': {'who': 'tensing', 'en': "We **were saved** by a yak. Write that in your diary, Sam."},
}

OUTRO = [
    {'who': 'sam', 'via': 'diary', 'en': "Day seventeen, Kathmandu. Otto **has been taken** to hospital. He's fine. My sister **has been told** everything."},
    {'who': 'otto', 'via': 'note', 'en': "Nearly forty years of climbing, and I **was carried** off a mountain by a yak. I'm going to need a better story."},
    {'who': 'doris', 'via': 'radio', 'en': "Momo **has been given** a medal. He ate it. Over."},
]
