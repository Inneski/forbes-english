"""The Climb — every word the learner reads, in English.

Innes, 2026-10-02: "an interactive game for sherpa tensing to practice the
tenses and scale the mountain, it will have a continuity of characters and
narrative but not very much narrative, mainly question to question".

So: thirteen camps up the route map's ascent, one tense each, eight lines per
camp, then the summit push (one line per tense). The narrative is the speaker
on each line and one or two lines on arriving at and leaving a camp. Nothing
else.

THE CAST (new: the course has no recurring characters; the art rule is "no
faces", so they are drawn from behind)
    Tensing  the guide. The course's name made a person. Gives the tip and the
             arrival/leaving lines; never speaks a quiz line. No pronoun is
             ever used for Tensing.
    Myra     the planner (called Ana until Innes renamed her, 2026-10-03): the schedule, the forecast, what happens next.
    Otto     the old hand: stories of climbs he has done before.
    Sam      first big climb: what is happening, what he has done so far.
    Navya    base camp radio. (Called Doris until Innes renamed her, 2026-10-03;
             camp four's own example is "Doris has just made coffee".)
    Momo     the yak, at base camp with Navya ("he"). A running joke, never a
             speaker.
Every radio line, Navya's or the team's, ends "Over."

THE STORY'S FACTS (two reviews found the story contradicting itself; keep
these true when you change a line)
    One camp a day. Day one, at camp one by the lake, is a Tuesday; camp four
    is Friday; camp thirteen is day thirteen; the summit is the morning of day
    fourteen ("nearly two weeks" in tents). The summit push starts at four in
    the morning; the sun rises at ten to six; they are on top by ten and
    heading down by two.
    The ridge is crossed at camp six (the storm); the glacier at camp nine;
    the hut is found locked at camp ten and opened at camp eleven.
    Otto first climbed in 1987, climbed THIS mountain in 1998 (the last peak in
    the valley), has known Tensing nearly twenty years, and next June will have
    been climbing for forty. Navya has known Otto twenty years. Sam is going to
    meet his sister in Kathmandu after the climb; the plane home leaves on the
    20th.

ITEM SHAPE
    id      'c<camp>-<n>' or 's-<n>' (summit). Stable: saves and the review
            list key on it.
    kind    'choose' — three options, key first here (the page shuffles them,
                       Fisher-Yates); 'type' — one gap, typed; 'spot' — which
                       tense is the [bracketed] form? options are camp numbers.
                       A camp's spot line may mark ANOTHER camp's tense (the
                       contrast the camp teaches); its options must include
                       the camp's own tense. A spot answer that is always the
                       camp you are standing in tests nothing.
    who     a CAST key.         via   optional: 'radio', 'diary', 'note'.
    text    the English line. One gap '_____' (two for a question, filled by
            an option written 'Are ... using'). The cue goes in brackets last.
    answer  what fills the gap(s): the corrected line shows it in bold.
    options choose: three strings, key first. spot: three camp numbers, key first.
    accept  type: every genuinely right answer. The page expands contractions
            on both sides ('ll / will, n't / not, 's / is / has, 'd / had /
            would), folds shall / shan't to will / won't, ignores case, curly
            quotes and a final full stop, so list only answers that differ in
            words: another tense that also fits, GOING TO beside WILL, an
            adverb in another place, a particle ("packed up").
    fb      ONE line, shown after every answer, right or wrong. Grammar tokens
            in CAPS, cited words in "double quotes" (the house rule — see
            build_lost_yellow_road.py). Translated: it is a meaning, not a
            pattern, so it is glossed; CAPS tokens stay English in every gloss.
    camp    summit items only: which tense the line tests.
A camp dict may also carry 'side': 'left' | 'right' to overrule the side of
the scene the card sits on (build.py measures the quieter half).

THE RULE THE REVIEWS ENFORCED: a learner who is right must never be marked
wrong, in British or American English, spoken or written. A distractor that a
fluent speaker could say in that context is a defect, however textbook-wrong
it looks ("I'm going to carry it for you" as an offer; "I didn't drink coffee
at home"). Two adversarial passes (2026-10-02) changed 75 of the first draft's
117 items; their reasoning is in the commit message.

Learner-facing English is A2 at camps 1-3 and 5-7, B1 at 4, 8 and 9, B2 at
10-12, C1 at 13 — the camps' own levels. Narrative lines model the camp's tense
(Innes on the RPGs: "the description must match the questions"), and must not
hand over an answer from the same camp; **bold** marks the form in them.
"""

CAST = {
    'tensing': {'name': 'Tensing', 'role': 'the guide'},
    'ana':     {'name': 'Myra',     'role': 'the planner'},
    'otto':    {'name': 'Otto',    'role': 'the old hand'},
    'sam':     {'name': 'Sam',     'role': 'first big climb'},
    'doris':   {'name': 'Navya',   'role': 'base camp radio'},
}
VIA = {'radio': 'on the radio', 'diary': 'diary', 'note': 'note'}

INTRO = [
    {'who': 'tensing', 'en': "I'm Tensing, your guide. Thirteen camps to the top, and one tense at each camp."},
    {'who': 'tensing', 'en': "Every line the team says has a gap. Fill it, and we climb."},
    {'who': 'tensing', 'en': "Miss one, and the rope holds: you read why, and that line comes back before we leave the camp."},
]

CAMPS = [
    # ------------------------------------------------------------------ 1  present continuous  A2   (day 1, a Tuesday)
    {
        'n': 1, 'alt': 3000,
        'arrive': [
            {'who': 'tensing', 'en': "Camp one, by the lake. The sun **is coming** up and the team **is getting** ready."},
            {'who': 'doris', 'via': 'radio', 'en': "Base camp here. I**'m watching** you through the telescope. Wave! Over."},
        ],
        'tip': "Now, around now, or already arranged: AM / IS / ARE + VERB-ING.",
        'items': [
            {'id': 'c1-1', 'kind': 'choose', 'who': 'sam',
             'text': "After the climb I _____ my sister in Kathmandu. It's all arranged! (meet)",
             'answer': 'am meeting', 'options': ['am meeting', 'was meeting', 'am meet'],
             'fb': '"It\'s all arranged" = a fixed plan: AM + VERB-ING.'},
            {'id': 'c1-2', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Base camp here. Momo _____ my breakfast! Over. (always / eat)",
             'answer': 'is always eating', 'options': ['is always eating', 'eats always', 'always is eating'],
             'fb': 'An annoying habit: IS + ALWAYS + VERB-ING.'},
            {'id': 'c1-3', 'kind': 'type', 'who': 'otto',
             'text': "Shh! Tensing _____ to the weather report. (listen)",
             'answer': 'is listening', 'accept': ['is listening'],
             'fb': '"Shh!" = it is happening now: IS + LISTENING.'},
            {'id': 'c1-4', 'kind': 'choose', 'who': 'ana',
             'text': "_____ you _____ the big map right now? I need it. (use)",
             'answer': 'Are ... using', 'options': ['Are ... using', 'Do ... use', 'Did ... use'],
             'fb': '"right now" in a question: ARE + you + VERB-ING?'},
            {'id': 'c1-5', 'kind': 'spot', 'who': 'doris', 'via': 'radio',
             'text': "The wind [is getting] stronger up there. Take care. Over.",
             'answer': 1, 'options': [1, 2, 6],
             'fb': 'IS + GETTING: a change that is happening now. Present continuous.'},
            {'id': 'c1-6', 'kind': 'choose', 'who': 'ana',
             'text': "Sam _____ in Otto's tent this week. His own tent is broken. (stay)",
             'answer': 'is staying', 'options': ['is staying', 'stays', 'is stay'],
             'fb': '"this week" = for now, not for ever: IS + VERB-ING.'},
            {'id': 'c1-7', 'kind': 'type', 'who': 'sam', 'via': 'diary',
             'text': "Day one. Right now Otto and Myra _____ breakfast, and I'm starving! (cook)",
             'answer': 'are cooking', 'accept': ['are cooking'],
             'fb': '"Right now" = in the middle of it: ARE + COOKING.'},
            {'id': 'c1-8', 'kind': 'choose', 'who': 'sam',
             'text': "I _____! It's just the wind in my eyes. (not / cry)",
             'answer': 'am not crying', 'options': ['am not crying', 'not crying', 'am not cry'],
             'fb': 'Not happening now: AM + NOT + VERB-ING. Keep both AM and -ING.'},
        ],
        'done': {'who': 'tensing', 'en': "Good. Packs on. We **are leaving** the lake now."},
    },
    # ------------------------------------------------------------------ 2  present simple  A2
    {
        'n': 2, 'alt': 3400,
        'arrive': [
            {'who': 'tensing', 'en': "Camp two, at the foot of the rock. The river **runs** east, and the sun **rises** behind that peak."},
            {'who': 'otto', 'en': "Some things **never change**. That's why I **like** this place."},
        ],
        'tip': "Facts, habits and timetables: VERB, or VERB + -S / -ES after he / she / it. Questions and negatives: DO / DOES.",
        'items': [
            {'id': 'c2-1', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Momo _____ fifteen kilos of grass a day, and he's still hungry! Over. (eat)",
             'answer': 'eats', 'options': ['eats', 'eat', 'is eat'],
             'fb': 'A habit, and Momo is "he": VERB + -S.'},
            {'id': 'c2-2', 'kind': 'choose', 'who': 'otto',
             'text': "Water _____ at a lower temperature up here. (boil)",
             'answer': 'boils', 'options': ['boils', 'boil', 'is boils'],
             'fb': 'A fact about the world, and water is "it": VERB + -S. No IS.'},
            {'id': 'c2-3', 'kind': 'type', 'who': 'ana',
             'text': "On every climb, Tensing _____ the sky first and then wakes the team. (watch)",
             'answer': 'watches', 'accept': ['watches'],
             'fb': '"On every climb" = a habit, one thing after another. One person, and WATCH ends in -CH: VERB + -ES.'},
            {'id': 'c2-4', 'kind': 'choose', 'who': 'sam',
             'text': "_____ you usually _____ this early, Tensing? (get up)",
             'answer': 'Do ... get up', 'options': ['Do ... get up', 'Are ... get up', 'Does ... get up'],
             'fb': '"usually" = a habit. A question with "you": DO + you + BASE VERB?'},
            {'id': 'c2-5', 'kind': 'spot', 'who': 'doris', 'via': 'radio',
             'text': "Sorry about the noise. The radio [isn't working] properly today. Over.",
             'answer': 1, 'options': [1, 2, 6],
             'fb': "ISN'T + WORKING with \"today\": a problem for now, not a fact about the radio. Present continuous."},
            {'id': 'c2-6', 'kind': 'choose', 'who': 'ana',
             'text': "Our plane home _____ at 6:40 on the 20th. We can't miss it! (leave)",
             'answer': 'leaves', 'options': ['leaves', 'is leave', 'leaving'],
             'fb': 'A timetable: somebody else set the time. VERB + -S.'},
            {'id': 'c2-7', 'kind': 'type', 'who': 'sam',
             'text': "I _____ coffee at home. I only drink it on mountains! (not / drink)",
             'answer': "don't drink", 'accept': ["don't drink", 'never drink'],
             'fb': "A habit, negative, with \"I\": DON'T + BASE VERB."},
            {'id': 'c2-8', 'kind': 'choose', 'who': 'otto',
             'text': "Tensing _____ lost, even in thick fog. (never / get)",
             'answer': 'never gets', 'options': ['never gets', 'never get', "doesn't never get"],
             'fb': "NEVER is already negative: NEVER + VERB + -S, with no DOESN'T."},
        ],
        'done': {'who': 'ana', 'en': "Tensing **wakes** everyone at five. The path **starts** behind the big rock."},
    },
    # ------------------------------------------------------------------ 3  past simple  A2
    {
        'n': 3, 'alt': 3800,
        'arrive': [
            {'who': 'tensing', 'en': "Camp three. We **left** the river at seven and **walked** all day."},
            {'who': 'sam', 'en': "I **saw** an eagle! It **flew** right over us."},
        ],
        'tip': "Finished, at a time that is stated or clear: PAST FORM (-ED, or the irregular form). Questions and negatives: DID + BASE VERB.",
        'items': [
            {'id': 'c3-1', 'kind': 'choose', 'who': 'otto',
             'text': "In 1998 I _____ this mountain with my brother. (climb)",
             'answer': 'climbed', 'options': ['climbed', 'have climbed', 'climb'],
             'fb': '"In 1998" = a finished, stated time: PAST FORM, -ED.'},
            {'id': 'c3-2', 'kind': 'choose', 'who': 'sam',
             'text': "We _____ to the top of the pass at four o'clock. (get)",
             'answer': 'got', 'options': ['got', 'getted', 'have got'],
             'fb': '"at four o\'clock" = a stated time. GET is irregular: GOT.'},
            {'id': 'c3-3', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "Momo _____ your sunglasses yesterday. He stood on them. Sorry! Over. (break)",
             'answer': 'broke', 'accept': ['broke'],
             'fb': '"yesterday" = finished time. BREAK is irregular: BROKE.'},
            {'id': 'c3-4', 'kind': 'choose', 'who': 'ana',
             'text': "_____ you _____ the water bottles before we left? (fill)",
             'answer': 'Did ... fill', 'options': ['Did ... fill', 'Did ... filled', 'Have ... fill'],
             'fb': '"before we left" = finished time: DID + you + BASE VERB? One past form is enough.'},
            {'id': 'c3-5', 'kind': 'spot', 'who': 'sam',
             'text': "My legs [are aching] after yesterday's walk.",
             'answer': 1, 'options': [1, 3, 6],
             'fb': 'ARE + ACHING: happening now, even with "yesterday" in the line. Present continuous, not camp three.'},
            {'id': 'c3-6', 'kind': 'choose', 'who': 'sam', 'via': 'diary',
             'text': "Day three. I _____ well last night. Otto snores! (not / sleep)",
             'answer': "didn't sleep", 'options': ["didn't sleep", "didn't slept", 'not slept'],
             'fb': "\"last night\", negative: DIDN'T + BASE VERB. Never DIDN'T + SLEPT."},
            {'id': 'c3-7', 'kind': 'type', 'who': 'ana',
             'text': "This morning we _____ at a little lake for breakfast. (stop)",
             'answer': 'stopped', 'accept': ['stopped', 'stopped off'],
             'fb': 'STOP → STOPPED: one syllable ending in one vowel + one consonant, so double the last letter before -ED.'},
            {'id': 'c3-8', 'kind': 'choose', 'who': 'otto',
             'text': "We _____ so tired last night that we went to bed at eight. (be)",
             'answer': 'were', 'options': ['were', 'was', 'did be'],
             'fb': '"we" + BE in the past: WERE. Not WAS, and never DID BE.'},
        ],
        'done': {'who': 'sam', 'en': "I **walked** fourteen kilometres, and I **didn't complain** once!"},
    },
    # ------------------------------------------------------------------ 4  present perfect  B1   (day 4: Friday)
    {
        'n': 4, 'alt': 4200,
        'arrive': [
            {'who': 'tensing', 'en': "Camp four. We**'ve climbed** twelve hundred metres since the lake."},
            {'who': 'sam', 'en': "And my legs **have** never **worked** so hard!"},
        ],
        'tip': "A past with a line to now, and no finished time stated: HAVE / HAS + PAST PARTICIPLE.",
        'items': [
            {'id': 'c4-1', 'kind': 'choose', 'who': 'sam',
             'text': "I _____ this high before. It's amazing! (never / be)",
             'answer': 'have never been', 'options': ['have never been', 'had never been', 'have never be'],
             'fb': 'All your life up to now: HAVE + NEVER + PAST PARTICIPLE. BE → BEEN.'},
            {'id': 'c4-2', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Base camp here. I _____ some fresh coffee. Pity you're not here! Over. (just / make)",
             'answer': 'have just made', 'options': ['have just made', 'has just made', 'have just make'],
             'fb': 'Moments ago, and still hot: HAVE + JUST + PAST PARTICIPLE. MAKE → MADE.'},
            {'id': 'c4-3', 'kind': 'type', 'who': 'ana',
             'text': "We _____ on this mountain since Tuesday, and the sky is still blue. (be)",
             'answer': 'have been', 'accept': ['have been'],
             'fb': '"since Tuesday" = from then up to now: HAVE + BEEN.'},
            {'id': 'c4-4', 'kind': 'choose', 'who': 'sam',
             'text': "_____ you ever _____ a yak, Otto? (ride)",
             'answer': 'Have ... ridden', 'options': ['Have ... ridden', 'Have ... rode', 'Has ... ridden'],
             'fb': '"ever" = at any time up to now: HAVE + you + PAST PARTICIPLE? RIDE → RIDDEN.'},
            {'id': 'c4-5', 'kind': 'spot', 'who': 'ana',
             'text': "We [left] the lake on Tuesday, and we haven't stopped since.",
             'answer': 3, 'options': [3, 4, 6],
             'fb': 'LEFT with "on Tuesday": a finished, stated time. Past simple, not camp four.'},
            {'id': 'c4-6', 'kind': 'choose', 'who': 'ana',
             'text': "Otto isn't here. He _____ to look at the ice. (go)",
             'answer': 'has gone', 'options': ['has gone', 'has been', 'has went'],
             'fb': 'He is there now and not back yet: HAS GONE. HAS BEEN would mean he went and came back.'},
            {'id': 'c4-7', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "I _____ Otto for twenty years, and he still tells the same jokes. Over. (know)",
             'answer': 'have known', 'accept': ['have known'],
             'fb': '"for twenty years" and still true: HAVE + PAST PARTICIPLE. KNOW → KNOWN.'},
            {'id': 'c4-8', 'kind': 'choose', 'who': 'ana',
             'text': "Otto _____ this pile of stones here two years ago, and it's still standing! (build)",
             'answer': 'built', 'options': ['built', 'has built', 'has build'],
             'fb': '"two years ago" = a finished, stated time: PAST FORM, which sends you back to camp three. BUILD → BUILT.'},
        ],
        'done': {'who': 'ana', 'en': "We**'ve done** the easy part. From here the path gets steeper."},
    },
    # ------------------------------------------------------------------ 5  going to  A2
    {
        'n': 5, 'alt': 4600,
        'arrive': [
            {'who': 'ana', 'en': "Here's the plan. Tomorrow we**'re going to cross** the meadow, and then we**'re going to climb** the ridge."},
            {'who': 'tensing', 'en': "Look at those clouds. It**'s going to rain** tonight."},
        ],
        'tip': "A plan already made, or a future you can see coming: AM / IS / ARE + GOING TO + BASE VERB. A plan that didn't happen: WAS / WERE GOING TO.",
        'items': [
            {'id': 'c5-1', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Oh no! Momo _____ in the river! Over. (fall)",
             'answer': 'is going to fall', 'options': ['is going to fall', 'going to fall', 'is going fall'],
             'fb': 'She can see it coming: IS + GOING TO + BASE VERB. Keep IS, and keep TO.'},
            {'id': 'c5-2', 'kind': 'choose', 'who': 'ana',
             'text': "I've decided. We _____ at six, before the sun gets hot. (leave)",
             'answer': 'are going to leave', 'options': ['are going to leave', 'are going to leaving', 'going to leave'],
             'fb': 'A decision already made: ARE + GOING TO + BASE VERB. No -ING after TO.'},
            {'id': 'c5-3', 'kind': 'type', 'who': 'otto',
             'text': "I _____ a big dinner tonight. I've brought everything for it! (be going to / cook)",
             'answer': 'am going to cook', 'accept': ['am going to cook', 'am going to be cooking'],
             'fb': '"I" + a plan you have prepared for: AM + GOING TO + BASE VERB.'},
            {'id': 'c5-4', 'kind': 'choose', 'who': 'sam',
             'text': "_____ we _____ ropes on the ridge? (be going to / need)",
             'answer': 'Are ... going to need', 'options': ['Are ... going to need', 'Do ... going to need', 'Are ... going to needing'],
             'fb': 'A question about what is coming: ARE + we + GOING TO + BASE VERB? Not DO.'},
            {'id': 'c5-5', 'kind': 'spot', 'who': 'sam', 'via': 'radio',
             'text': "Don't worry, Navya. I'm sure Momo [will be] fine. Over.",
             'answer': 7, 'options': [7, 5, 9],
             'fb': 'WILL + BE after "I\'m sure": an opinion about the future. Future simple, not going to.'},
            {'id': 'c5-6', 'kind': 'choose', 'who': 'ana',
             'text': "We _____ stop for lunch on the ridge tomorrow. It's too cold up there. (not / be going to)",
             'answer': "aren't going to", 'options': ["aren't going to", "don't going to", "aren't go to"],
             'fb': "A plan not to do it: AREN'T + GOING TO + BASE VERB. Not DON'T."},
            {'id': 'c5-7', 'kind': 'type', 'who': 'ana',
             'text': "Sam _____ his mum from the top. He promised her! (be going to / phone)",
             'answer': 'is going to phone', 'accept': ['is going to phone', 'is going to be phoning'],
             'fb': 'A plan already made: IS + GOING TO + PHONE.'},
            {'id': 'c5-8', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "I _____ call you at nine, but the radio was dead. Over. (be going to)",
             'answer': 'was going to', 'options': ['was going to', 'am going to', 'will'],
             'fb': 'A plan that did not happen: WAS + GOING TO, then "but".'},
        ],
        'done': {'who': 'tensing', 'en': "Rest now. Tomorrow **is going to be** a long day."},
    },
    # ------------------------------------------------------------------ 6  past continuous  A2
    {
        'n': 6, 'alt': 5000,
        'arrive': [
            {'who': 'otto', 'en': "What a day! We **were crossing** the ridge when the storm hit."},
            {'who': 'sam', 'en': "I **was holding** the rope so tightly that my hands **were shaking**."},
        ],
        'tip': "The background, or an action in progress when something happened: WAS / WERE + VERB-ING.",
        'items': [
            {'id': 'c6-1', 'kind': 'choose', 'who': 'sam',
             'text': "I _____ my lunch when the hail started, and I never finished it. (eat)",
             'answer': 'was eating', 'options': ['was eating', 'were eating', 'ate'],
             'fb': 'In the middle of it, then cut off: WAS + VERB-ING ... WHEN + PAST FORM.'},
            {'id': 'c6-2', 'kind': 'choose', 'who': 'ana',
             'text': "At three o'clock we _____ still _____ up the ridge. (climb)",
             'answer': 'were ... climbing', 'options': ['were ... climbing', 'was ... climbing', 'were ... climb'],
             'fb': '"At three o\'clock" = in the middle of it. "we" takes WERE + VERB-ING.'},
            {'id': 'c6-3', 'kind': 'type', 'who': 'otto',
             'text': "We _____ when the wind broke one of the tent poles. (sleep)",
             'answer': 'were sleeping', 'accept': ['were sleeping', 'had been sleeping', 'were asleep', 'were all asleep', 'were fast asleep', 'were still asleep', 'were all sleeping', 'were still sleeping'],
             'fb': 'The long action, cut by a short one: WERE + VERB-ING ... WHEN + PAST FORM.'},
            {'id': 'c6-4', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Sorry, I _____. Can you say that again? Over. (not / listen)",
             'answer': "wasn't listening", 'options': ["wasn't listening", "weren't listening", "didn't listening"],
             'fb': "Not in the middle of listening at that moment: WASN'T + VERB-ING."},
            {'id': 'c6-5', 'kind': 'spot', 'who': 'ana',
             'text': "While Sam was taking photos, a rock [fell] past him.",
             'answer': 3, 'options': [3, 6, 10],
             'fb': 'FELL: the short event that cut in. Past simple. WAS TAKING is the background.'},
            {'id': 'c6-6', 'kind': 'choose', 'who': 'ana',
             'text': "Why _____ you _____ so close to the edge when the storm started? (stand)",
             'answer': 'were ... standing', 'options': ['were ... standing', 'was ... standing', 'did ... stood'],
             'fb': '"you" + an action already in progress: WERE + you + VERB-ING?'},
            {'id': 'c6-7', 'kind': 'type', 'who': 'otto',
             'text': "We _____ dinner when the wind blew the stove over, so we ate the rest cold. (cook)",
             'answer': 'were cooking', 'accept': ['were cooking', 'had been cooking'],
             'fb': '"ate the rest cold" = it was not finished: WERE + VERB-ING ... WHEN + PAST FORM.'},
            {'id': 'c6-8', 'kind': 'choose', 'who': 'sam',
             'text': "I _____ where the path was, so I stayed close to Tensing. (not / know)",
             'answer': "didn't know", 'options': ["didn't know", "wasn't knowing", "didn't knew"],
             'fb': "KNOW is a state verb: no -ING. DIDN'T + BASE VERB."},
        ],
        'done': {'who': 'sam', 'en': "That night the stars **were shining** and Otto **was singing** in his tent."},
    },
    # ------------------------------------------------------------------ 7  future simple (will)  A2
    {
        'n': 7, 'alt': 5400,
        'arrive': [
            {'who': 'ana', 'en': "Nobody knows what the weather **will do** up here."},
            {'who': 'tensing', 'en': "Stay close to me and you**'ll be** fine."},
        ],
        'tip': "Decided now, offered, promised, or just what you think: WILL + BASE VERB. Offers as questions: SHALL I ...? After WHEN and IF: the present.",
        'items': [
            {'id': 'c7-1', 'kind': 'choose', 'who': 'otto',
             'text': "Your bag looks heavy, Sam. I _____ it for you. (carry)",
             'answer': "'ll carry", 'options': ["'ll carry", "'ll to carry", 'carry'],
             'fb': "An offer, decided as you speak: WILL ('LL) + BASE VERB. No TO after WILL."},
            {'id': 'c7-2', 'kind': 'choose', 'who': 'ana',
             'text': "I think Sam _____ the top. He's stronger than he looks. (reach)",
             'answer': 'will reach', 'options': ['will reach', 'will reaches', 'wills reach'],
             'fb': '"I think" + your opinion of the future: WILL + BASE VERB. No -S after WILL.'},
            {'id': 'c7-3', 'kind': 'type', 'who': 'sam',
             'text': "Sorry! I promise I _____ my boots outside the tent again. (not / leave)",
             'answer': "won't leave", 'accept': ["won't leave", 'am not going to leave', 'will never leave', "won't ever leave", 'am never going to leave', "won't be leaving", 'am not leaving'],
             'fb': "A promise: WON'T (= WILL NOT) + BASE VERB."},
            {'id': 'c7-4', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "You're breaking up. _____ I call you back in five minutes? Over.",
             'answer': 'Shall', 'options': ['Shall', 'Does', 'Am'],
             'fb': 'Offering to do something: SHALL + I + BASE VERB?'},
            {'id': 'c7-5', 'kind': 'spot', 'who': 'otto',
             'text': "Look at the ice on that slope. Somebody [is going to fall].",
             'answer': 5, 'options': [5, 7, 9],
             'fb': 'IS GOING TO + FALL: you can see it coming. Going to, not camp seven.'},
            {'id': 'c7-6', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Call me when you _____ at the hut. Over. (arrive)",
             'answer': 'arrive', 'options': ['arrive', 'will arrive', 'arrived'],
             'fb': 'After WHEN, the future takes the present: WHEN you ARRIVE, not WHEN you WILL ARRIVE.'},
            {'id': 'c7-7', 'kind': 'type', 'who': 'otto',
             'text': "The stove _____. I've tried five times! (will / not / start)",
             'answer': "won't start", 'accept': ["won't start"],
             'fb': "Something that refuses to work: WON'T + BASE VERB."},
            {'id': 'c7-8', 'kind': 'choose', 'who': 'sam',
             'text': "_____ the weather _____ better tomorrow, Tensing? (get)",
             'answer': 'Will ... get', 'options': ['Will ... get', 'Will ... gets', 'Does ... gets'],
             'fb': 'A question about the future: WILL + subject + BASE VERB?'},
        ],
        'done': {'who': 'tensing', 'en': "The clouds are building. We**'ll see** what the morning brings."},
    },
    # ------------------------------------------------------------------ 8  present perfect continuous  B1
    {
        'n': 8, 'alt': 5800,
        'arrive': [
            {'who': 'tensing', 'en': "Look at the tracks behind us. We**'ve been climbing** since dawn."},
            {'who': 'sam', 'en': "And my feet **have been hurting** for hours."},
        ],
        'tip': "How long, up to now, or an activity that explains what you can see now: HAVE / HAS + BEEN + VERB-ING.",
        'items': [
            {'id': 'c8-1', 'kind': 'choose', 'who': 'sam',
             'text': "We _____ since six this morning, and I need a rest! (walk)",
             'answer': 'have been walking', 'options': ['have been walking', 'had been walking', 'are walking'],
             'fb': '"since six this morning", up to now: HAVE + BEEN + VERB-ING. Not ARE + VERB-ING.'},
            {'id': 'c8-2', 'kind': 'choose', 'who': 'ana',
             'text': "Your hands are black, Otto! _____ you _____ the stove again? (fix)",
             'answer': 'Have ... been fixing', 'options': ['Have ... been fixing', 'Had ... been fixing', 'Has ... been fixing'],
             'fb': 'Black hands now are the evidence: HAVE + you + BEEN + VERB-ING?'},
            {'id': 'c8-3', 'kind': 'type', 'who': 'sam', 'via': 'diary',
             'text': "Day eight. It _____ since lunchtime, and everything I own is wet. (snow)",
             'answer': 'has been snowing', 'accept': ['has been snowing', 'has snowed'],
             'fb': '"since lunchtime", up to now: HAS + BEEN + SNOWING.'},
            {'id': 'c8-4', 'kind': 'choose', 'who': 'ana',
             'text': "How long _____ you _____ Otto, Tensing? Twenty years? (know)",
             'answer': 'have ... known', 'options': ['have ... known', 'have ... been knowing', 'do ... know'],
             'fb': 'KNOW is a state verb, so no -ING: HAVE + you + KNOWN. That is camp four, not camp eight.'},
            {'id': 'c8-5', 'kind': 'spot', 'who': 'doris', 'via': 'radio',
             'text': "Good news: Momo [has stopped] chewing the radio cable. Over.",
             'answer': 4, 'options': [4, 8, 3],
             'fb': 'HAS + STOPPED: a result you can see now. Present perfect, not camp eight.'},
            {'id': 'c8-6', 'kind': 'choose', 'who': 'otto',
             'text': "I _____ three cups of tea since we stopped. (drink)",
             'answer': 'have drunk', 'options': ['have drunk', 'have been drinking', 'drink'],
             'fb': '"three cups" is a number, a result: HAVE + PAST PARTICIPLE (camp four). DRINK → DRUNK.'},
            {'id': 'c8-7', 'kind': 'type', 'who': 'ana',
             'text': "Otto _____ the same song for an hour. Please make him stop! (sing)",
             'answer': 'has been singing', 'accept': ['has been singing', 'has sung'],
             'fb': 'An activity that has gone on up to now: HAS + BEEN + SINGING.'},
            {'id': 'c8-8', 'kind': 'choose', 'who': 'sam',
             'text': "We _____ very well lately. The tent is too cold. (not / sleep)",
             'answer': "haven't been sleeping", 'options': ["haven't been sleeping", "hadn't been sleeping", "haven't been slept"],
             'fb': "\"lately\", up to now, negative: HAVEN'T + BEEN + VERB-ING."},
        ],
        'done': {'who': 'tensing', 'en': "We**'ve been climbing** for eleven hours. Tonight, we rest."},
    },
    # ------------------------------------------------------------------ 9  future continuous  B1
    {
        'n': 9, 'alt': 6200,
        'arrive': [
            {'who': 'ana', 'en': "Tomorrow morning we**'ll be crossing** the glacier."},
            {'who': 'doris', 'via': 'radio', 'en': "And I**'ll be drinking** coffee in the sun. Over."},
        ],
        'tip': "In progress at a time in the future, already in the plan, or a guess about now: WILL BE + VERB-ING.",
        'items': [
            {'id': 'c9-1', 'kind': 'choose', 'who': 'ana',
             'text': "At six tomorrow morning we _____ up the ice field. (walk)",
             'answer': 'will be walking', 'options': ['will be walking', 'will being walking', 'will be walk'],
             'fb': '"At six tomorrow morning" = in the middle of it at that time: WILL BE + VERB-ING.'},
            {'id': 'c9-2', 'kind': 'choose', 'who': 'sam',
             'text': "_____ you _____ the big stove tonight? I need to boil some water. (use)",
             'answer': 'Will ... be using', 'options': ['Will ... be using', 'Will ... be use', 'Are ... use'],
             'fb': 'A polite way to ask about plans: WILL + you + BE + VERB-ING?'},
            {'id': 'c9-3', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "This time tomorrow the wind _____ hard again, so leave early. Over. (blow)",
             'answer': 'will be blowing', 'accept': ['will be blowing', 'is going to be blowing'],
             'fb': '"This time tomorrow" = in the middle of it then: WILL BE + BLOWING.'},
            {'id': 'c9-4', 'kind': 'choose', 'who': 'otto',
             'text': "Don't call Navya now. She _____ lunch. (have)",
             'answer': "'ll be having", 'options': ["'ll be having", "'ll having", "'s be having"],
             'fb': "A confident guess about now: WILL ('LL) BE + VERB-ING."},
            {'id': 'c9-5', 'kind': 'spot', 'who': 'sam',
             'text': "Tomorrow at noon we [will be standing] on the north ridge.",
             'answer': 9, 'options': [9, 7, 12],
             'fb': 'WILL BE + STANDING: in progress at a future time. Future continuous.'},
            {'id': 'c9-6', 'kind': 'choose', 'who': 'ana',
             'text': "The forecast comes at six. I _____ by seven, I promise. (know)",
             'answer': 'will know', 'options': ['will know', 'will be knowing', 'know'],
             'fb': 'KNOW is a state verb: plain WILL + KNOW, never WILL BE KNOWING.'},
            {'id': 'c9-7', 'kind': 'type', 'who': 'sam',
             'text': "At midnight tonight I _____, so please don't wake me! (sleep)",
             'answer': 'will be sleeping', 'accept': ['will be sleeping', 'am going to be sleeping', 'will be asleep', 'am going to be asleep'],
             'fb': '"At midnight tonight" = in the middle of it then: WILL BE + SLEEPING.'},
            {'id': 'c9-8', 'kind': 'choose', 'who': 'ana', 'via': 'radio',
             'text': "Don't worry if you can't reach us tomorrow morning, Navya. We _____ the radio. Over. (not / use)",
             'answer': "won't be using", 'options': ["won't be using", "won't be use", "aren't be using"],
             'fb': "Not in progress at that future time: WON'T BE + VERB-ING."},
        ],
        'done': {'who': 'tensing', 'en': "Early night, everyone. At four tomorrow we**'ll be walking** on ice."},
    },
    # ------------------------------------------------------------------ 10  past perfect  B2
    {
        'n': 10, 'alt': 6600,
        'arrive': [
            {'who': 'otto', 'en': "When we got here, another team **had** already **cut** steps in the ice. Look: we can use them."},
            {'who': 'sam', 'en': "Before this trip I **had never been** above four thousand metres."},
        ],
        'tip': "The earlier of two past events, seen from the later one, or a past that did not happen (IF ...): HAD + PAST PARTICIPLE.",
        'items': [
            {'id': 'c10-1', 'kind': 'choose', 'who': 'ana',
             'text': "By the time we reached the ledge, the other team _____. (leave)",
             'answer': 'had left', 'options': ['had left', 'has left', 'left'],
             'fb': '"By the time we reached" is the later past. Earlier still: HAD + PAST PARTICIPLE.'},
            {'id': 'c10-2', 'kind': 'choose', 'who': 'otto',
             'text': "When you first met Momo, _____ you ever _____ a yak before? (see)",
             'answer': 'had ... seen', 'options': ['had ... seen', 'have ... seen', 'had ... saw'],
             'fb': 'Before that past moment, as a question: HAD + you + EVER + PAST PARTICIPLE?'},
            {'id': 'c10-3', 'kind': 'type', 'who': 'otto',
             'text': "By the time I got back to the tent, someone _____ all my chocolate. There wasn't a piece left! (eat)",
             'answer': 'had eaten', 'accept': ['had eaten', 'had already eaten', 'had been eating'],
             'fb': 'It happened before I got back: HAD + PAST PARTICIPLE. EAT → EATEN.'},
            {'id': 'c10-4', 'kind': 'choose', 'who': 'sam',
             'text': "Otto said he _____ his glasses, but they were on his head all the time! (lose)",
             'answer': 'had lost', 'options': ['had lost', 'has lost', 'had lose'],
             'fb': 'Reported speech moves back: "I\'ve lost them" → he said he HAD LOST them.'},
            {'id': 'c10-5', 'kind': 'spot', 'who': 'ana',
             'text': "We found the hut at last, but someone [had locked] the door.",
             'answer': 10, 'options': [10, 3, 11],
             'fb': 'HAD + LOCKED: done before we found the hut. Past perfect.'},
            {'id': 'c10-6', 'kind': 'choose', 'who': 'sam',
             'text': "It was the first time I _____ on a glacier. (walk)",
             'answer': 'had walked', 'options': ['had walked', 'have walked', 'had walk'],
             'fb': '"It was the first time" looks back from a past moment: HAD + PAST PARTICIPLE.'},
            {'id': 'c10-7', 'kind': 'type', 'who': 'ana',
             'text': "We _____ anything since breakfast, so by dinner we were starving. (not / eat)",
             'answer': "hadn't eaten", 'accept': ["hadn't eaten"],
             'fb': "Nothing up to that past moment: HADN'T + PAST PARTICIPLE."},
            {'id': 'c10-8', 'kind': 'choose', 'who': 'otto',
             'text': "If we _____ earlier, we would have reached the hut before the storm. (start)",
             'answer': 'had started', 'options': ['had started', 'would start', 'started'],
             'fb': 'A past that did not happen: IF + HAD + PAST PARTICIPLE.'},
        ],
        'done': {'who': 'sam', 'en': "By the time we got the stove going, the sun **had** already **gone** down."},
    },
    # ------------------------------------------------------------------ 11  past perfect continuous  B2
    {
        'n': 11, 'alt': 7000,
        'arrive': [
            {'who': 'ana', 'en': "We **had been shivering** outside for an hour when Tensing finally got the hut door open."},
            {'who': 'otto', 'en': "And it **had been snowing** all day. My beard was frozen!"},
        ],
        'tip': "How long something had been going on before a past moment, or the activity behind a past state: HAD BEEN + VERB-ING.",
        'items': [
            {'id': 'c11-1', 'kind': 'choose', 'who': 'sam',
             'text': "My legs were shaking because I _____ uphill all afternoon. (climb)",
             'answer': 'had been climbing', 'options': ['had been climbing', 'have been climbing', 'was been climbing'],
             'fb': 'A long activity behind a past state: HAD BEEN + VERB-ING.'},
            {'id': 'c11-2', 'kind': 'choose', 'who': 'ana',
             'text': "How long _____ you _____ when the rescue team found you, Otto? (wait)",
             'answer': 'had ... been waiting', 'options': ['had ... been waiting', 'have ... been waiting', 'had ... been wait'],
             'fb': 'How long, up to a past moment: HAD + you + BEEN + VERB-ING?'},
            {'id': 'c11-3', 'kind': 'type', 'who': 'otto',
             'text': "When the helicopter came, I _____ in the snow for two days. (sit)",
             'answer': 'had been sitting', 'accept': ['had been sitting', 'had sat', 'had been sat'],
             'fb': '"for two days" up to a past moment: HAD BEEN + SITTING.'},
            {'id': 'c11-4', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "Momo was soaking wet when I found him. He _____ in the river all morning! Over. (play)",
             'answer': 'had been playing', 'options': ['had been playing', 'has been playing', 'had been played'],
             'fb': 'The activity behind what she found: HAD BEEN + VERB-ING.'},
            {'id': 'c11-5', 'kind': 'spot', 'who': 'sam', 'via': 'diary',
             'text': "My eyes were sore. I [had been staring] at the snow all day.",
             'answer': 11, 'options': [11, 10, 8],
             'fb': 'HAD BEEN + STARING: a long activity before a past moment. Past perfect continuous.'},
            {'id': 'c11-6', 'kind': 'choose', 'who': 'ana',
             'text': "By lunchtime yesterday, Otto _____ four cups of tea. (drink)",
             'answer': 'had drunk', 'options': ['had drunk', 'had been drinking', 'has drunk'],
             'fb': '"four cups" is a number, a result: HAD + PAST PARTICIPLE (camp ten). DRINK → DRUNK.'},
            {'id': 'c11-7', 'kind': 'type', 'who': 'ana',
             'text': "When the snow finally stopped, it _____ for eleven hours. (fall)",
             'answer': 'had been falling', 'accept': ['had been falling', 'had fallen'],
             'fb': '"for eleven hours" up to a past moment: HAD BEEN + FALLING.'},
            {'id': 'c11-8', 'kind': 'choose', 'who': 'sam',
             'text': "Before we reached the hut, I _____ well for days. (not / sleep)",
             'answer': "hadn't been sleeping", 'options': ["hadn't been sleeping", "haven't been sleeping", "wasn't been sleeping"],
             'fb': "Negative, up to a past moment: HADN'T + BEEN + VERB-ING."},
        ],
        'done': {'who': 'otto', 'en': "We **had been dreaming** about that hut for days. It was perfect."},
    },
    # ------------------------------------------------------------------ 12  future perfect  B2
    {
        'n': 12, 'alt': 7400,
        'arrive': [
            {'who': 'ana', 'en': "By ten the day after tomorrow, we**'ll have reached** the top."},
            {'who': 'tensing', 'en': "And by two we **will have started** down. The mountain doesn't wait."},
        ],
        'tip': "Finished before a time in the future, or a confident guess about now: WILL HAVE + PAST PARTICIPLE. Look for BY. After BY THE TIME: the present.",
        'items': [
            {'id': 'c12-1', 'kind': 'choose', 'who': 'ana',
             'text': "We _____ the last ridge by dark, so pack a head torch. (not / cross)",
             'answer': "won't have crossed", 'options': ["won't have crossed", "won't have cross", "won't has crossed"],
             'fb': "Not done by a future time: WON'T HAVE + PAST PARTICIPLE."},
            {'id': 'c12-2', 'kind': 'choose', 'who': 'doris', 'via': 'radio',
             'text': "By the time you get back, I _____ your favourite dinner. Over. (make)",
             'answer': 'will have made', 'options': ['will have made', 'will have make', 'have made'],
             'fb': '"By the time you get back" = done before then: WILL HAVE + PAST PARTICIPLE.'},
            {'id': 'c12-3', 'kind': 'type', 'who': 'sam',
             'text': "By the end of this trip, I _____ more than a hundred kilometres! (walk)",
             'answer': 'will have walked', 'accept': ['will have walked', 'am going to have walked'],
             'fb': 'A total reached by a future time: WILL HAVE + WALKED.'},
            {'id': 'c12-4', 'kind': 'choose', 'who': 'ana',
             'text': "Hurry up, Sam! By the time you _____ your bag, we will have left! (pack)",
             'answer': 'pack', 'options': ['pack', 'packed', 'will pack'],
             'fb': 'After BY THE TIME, the future takes the present: you PACK, not you WILL PACK.'},
            {'id': 'c12-5', 'kind': 'spot', 'who': 'otto',
             'text': "By 1998 I [had climbed] every other peak in this valley.",
             'answer': 10, 'options': [10, 12, 4],
             'fb': 'HAD + CLIMBED with "By 1998": done before a past point. Past perfect, not camp twelve.'},
            {'id': 'c12-6', 'kind': 'choose', 'who': 'sam',
             'text': "Tensing _____ the weather report by now. Let's ask. (check)",
             'answer': 'will have checked', 'options': ['will have checked', 'is going to check', 'will check'],
             'fb': 'A confident guess about now: WILL HAVE + PAST PARTICIPLE, with "by now".'},
            {'id': 'c12-7', 'kind': 'type', 'who': 'sam', 'via': 'note',
             'text': "Mum, by the time you read this postcard, I _____ home! (already / fly)",
             'answer': 'will already have flown', 'accept': ['will already have flown', 'will have already flown', 'will have flown', 'am going to have already flown', 'am going to have flown', 'will already have flown back', 'will have already flown back', 'will have flown back'],
             'fb': '"by the time you read this" = done before then: WILL + ALREADY + HAVE + PAST PARTICIPLE. FLY → FLOWN.'},
            {'id': 'c12-8', 'kind': 'choose', 'who': 'sam', 'via': 'radio',
             'text': "_____ Momo _____ all the grass at base camp by the time we get back, Navya? Over. (eat)",
             'answer': 'Will ... have eaten', 'options': ['Will ... have eaten', 'Will ... has eaten', 'Has ... eaten'],
             'fb': 'A question about a future deadline: WILL + subject + HAVE + PAST PARTICIPLE?'},
        ],
        'done': {'who': 'tensing', 'en': "By sunset tomorrow we **will have reached** camp thirteen. Rest well."},
    },
    # ------------------------------------------------------------------ 13  future perfect continuous  C1
    {
        'n': 13, 'alt': 7800,
        'arrive': [
            {'who': 'sam', 'en': "By the time we reach the top, we**'ll have been living** in tents for nearly two weeks."},
            {'who': 'tensing', 'en': "Last camp. By ten tomorrow we**'ll have been moving** for six hours, so eat well tonight."},
        ],
        'tip': "How long it will have gone on by a future point: WILL HAVE BEEN + VERB-ING. It needs a length of time.",
        'items': [
            {'id': 'c13-1', 'kind': 'choose', 'who': 'sam',
             'text': "How long _____ we _____ by the time we reach the top? (walk)",
             'answer': 'will ... have been walking', 'options': ['will ... have been walking', 'will ... have been walked', 'have ... been walking'],
             'fb': 'How long, up to a future point: WILL + we + HAVE BEEN + VERB-ING?'},
            {'id': 'c13-2', 'kind': 'choose', 'who': 'ana',
             'text': "By next June, Otto _____ mountains for forty years. (climb)",
             'answer': 'will have been climbing', 'options': ['will have been climbing', 'will have been climbed', 'will be climbing'],
             'fb': '"for forty years" up to a future point: WILL HAVE BEEN + VERB-ING.'},
            {'id': 'c13-3', 'kind': 'type', 'who': 'doris', 'via': 'radio',
             'text': "Momo started eating at nine. By noon he _____ for three hours! Over. (eat)",
             'answer': 'will have been eating', 'accept': ['will have been eating', 'is going to have been eating'],
             'fb': '"for three hours" up to a future point: WILL HAVE BEEN + EATING.'},
            {'id': 'c13-4', 'kind': 'choose', 'who': 'ana',
             'text': "By the end of this trip, Tensing _____ teams up this mountain four times this year. (guide)",
             'answer': 'will have guided', 'options': ['will have guided', 'will have been guiding', 'will be guiding'],
             'fb': '"four times" is a number, a result: WILL HAVE + PAST PARTICIPLE (camp twelve).'},
            {'id': 'c13-5', 'kind': 'spot', 'who': 'sam',
             'text': "By sunrise we [will have reached] the summit snowfield.",
             'answer': 12, 'options': [12, 13, 9],
             'fb': 'WILL HAVE + REACHED: done by a future time, with no length of time. Future perfect, not camp thirteen.'},
            {'id': 'c13-6', 'kind': 'choose', 'who': 'otto',
             'text': "Next month I _____ Tensing for twenty years. (know)",
             'answer': 'will have known', 'options': ['will have known', 'will have been knowing', 'will be knowing'],
             'fb': 'KNOW is a state verb: WILL HAVE + KNOWN, never BEEN KNOWING.'},
            {'id': 'c13-7', 'kind': 'type', 'who': 'sam',
             'text': "By the time we get home, I _____ these socks for two weeks! (wear)",
             'answer': 'will have been wearing', 'accept': ['will have been wearing', 'will have worn', 'am going to have been wearing', 'am going to have worn'],
             'fb': '"for two weeks" up to a future point: WILL HAVE BEEN + WEARING.'},
            {'id': 'c13-8', 'kind': 'choose', 'who': 'ana', 'via': 'radio',
             'text': "Don't worry, Navya. When the bus comes, we _____ for long. Over. (not / wait)",
             'answer': "won't have been waiting", 'options': ["won't have been waiting", "haven't been waiting", "won't have been wait"],
             'fb': "Not long, up to a future moment: WON'T HAVE BEEN + VERB-ING."},
        ],
        'done': {'who': 'tensing', 'en': "Sleep now. By sunrise tomorrow we**'ll have been walking** for two hours."},
    },
]

# The summit push: one line per tense, in route order. 'camp' = the tense tested.
SUMMIT = {
    'n': 'summit', 'alt': 8000, 'top': 8350,
    'arrive': [
        {'who': 'tensing', 'en': "The summit push. You**'ve met** every tense on the way up. Now they all come at once."},
    ],
    'tip': "Read the whole line before you answer: the time words (NOW, SINCE, BY, WHEN) decide the tense.",
    'items': [
        {'id': 's-1', 'camp': 1, 'kind': 'choose', 'who': 'sam',
         'text': "Listen! Somebody _____ my name. (shout)",
         'answer': 'is shouting', 'options': ['is shouting', 'shouts', 'has shouted'],
         'fb': '"Listen!" = it is happening now: IS + VERB-ING. Camp one.'},
        {'id': 's-2', 'camp': 2, 'kind': 'choose', 'who': 'ana',
         'text': "At this time of year the sun _____ at ten to six. (rise)",
         'answer': 'rises', 'options': ['rises', 'rise', 'rose'],
         'fb': 'A regular fact, and the sun is "it": VERB + -S. Camp two.'},
        {'id': 's-3', 'camp': 3, 'kind': 'type', 'who': 'otto',
         'text': "I _____ my first mountain in 1987. (climb)",
         'answer': 'climbed', 'accept': ['climbed'],
         'fb': '"in 1987" = a finished, stated time: PAST FORM. Camp three.'},
        {'id': 's-4', 'camp': 4, 'kind': 'choose', 'who': 'sam',
         'text': "Look up, Otto! I _____ so many stars in my life! (never / see)",
         'answer': 'have never seen', 'options': ['have never seen', 'has never seen', 'had never seen'],
         'fb': '"in my life", up to now: HAVE + NEVER + PAST PARTICIPLE. Camp four.'},
        {'id': 's-5', 'camp': 5, 'kind': 'choose', 'who': 'doris', 'via': 'radio',
         'text': "There are big black clouds over base camp. It _____ rain. Over.",
         'answer': 'is going to', 'options': ['is going to', 'will to', 'is going'],
         'fb': 'You can see it coming: IS + GOING TO + BASE VERB. Camp five.'},
        {'id': 's-6', 'camp': 6, 'kind': 'choose', 'who': 'ana',
         'text': "Sam _____ his lunch when the hail started, so he never finished it. (eat)",
         'answer': 'was eating', 'options': ['was eating', 'ate', 'has eaten'],
         'fb': 'In the middle of lunch when the hail came: WAS + VERB-ING. Camp six.'},
        {'id': 's-7', 'camp': 7, 'kind': 'spot', 'who': 'ana',
         'text': "I think the wind [will drop] after sunrise.",
         'answer': 7, 'options': [7, 5, 9],
         'fb': 'WILL + DROP after "I think": just what you think will happen. Camp seven.'},
        {'id': 's-8', 'camp': 8, 'kind': 'choose', 'who': 'sam',
         'text': "I'm so tired. We _____ since four this morning. (climb)",
         'answer': 'have been climbing', 'options': ['have been climbing', 'had been climbing', 'are climbing'],
         'fb': '"since four this morning", up to now: HAVE BEEN + VERB-ING. Camp eight.'},
        {'id': 's-9', 'camp': 9, 'kind': 'choose', 'who': 'ana',
         'text': "This time next week we _____ at home in the warm. (sit)",
         'answer': 'will be sitting', 'options': ['will be sitting', 'will have sat', 'will sitting'],
         'fb': 'In the middle of it at a future time: WILL BE + VERB-ING. Camp nine.'},
        {'id': 's-10', 'camp': 10, 'kind': 'type', 'who': 'otto',
         'text': "When we reached the top in 1998, the clouds _____ and the sky was completely empty. (already / clear)",
         'answer': 'had already cleared', 'accept': ['had already cleared', 'had cleared already', 'had already cleared away', 'had cleared away already'],
         'fb': 'Earlier than "we reached": HAD + ALREADY + PAST PARTICIPLE. Camp ten.'},
        {'id': 's-11', 'camp': 11, 'kind': 'choose', 'who': 'ana',
         'text': "Otto's face was red because he _____ the heavy bag for hours. (carry)",
         'answer': 'had been carrying', 'options': ['had been carrying', 'has been carrying', 'is carrying'],
         'fb': 'A long activity behind a past state: HAD BEEN + VERB-ING. Camp eleven.'},
        {'id': 's-12', 'camp': 12, 'kind': 'choose', 'who': 'doris', 'via': 'radio',
         'text': "By the time you're back, the snow at base camp _____. Over. (melt)",
         'answer': 'will have melted', 'options': ['will have melted', 'would have melted', 'has melted'],
         'fb': 'Done before you are back: WILL HAVE + PAST PARTICIPLE. Camp twelve.'},
        {'id': 's-13', 'camp': 13, 'kind': 'type', 'who': 'sam',
         'text': "In ten minutes we _____ for thirteen whole days! (climb)",
         'answer': 'will have been climbing', 'accept': ['will have been climbing', 'will have climbed', 'are going to have been climbing', 'are going to have climbed'],
         'fb': '"for thirteen whole days" up to a future point: WILL HAVE BEEN + VERB-ING. Camp thirteen.'},
    ],
    'done': {'who': 'tensing', 'en': "We**'ve made** it. Look down: every camp is behind us."},
}

OUTRO = [
    {'who': 'sam', 'en': "I**'ve never felt** so tired, or so happy."},
    {'who': 'otto', 'en': "Nearly forty years, and the view still **takes** my breath away."},
    {'who': 'doris', 'via': 'radio', 'en': "Congratulations, everyone! Bad news, though: Momo **has eaten** your cake. Over."},
]
# Three lines, not five: with six speakers the summit card scrolled on a phone
# (the no-scroll gate in test_climb.js), and Innes asked for "not very much narrative".
