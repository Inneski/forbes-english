# Whole-script critic findings

## [BLOCKER] provost + reef3

Friday runs backwards. `provost` says "Regatta Week starts on Friday" (Friday is ahead). An hour later on the REEF branch, `reef3` says "Forty were here until Friday morning" and the correct answer is "since Friday" (Friday is behind). Chapter 4 `night1` then says Regatta Week is happening. A REEF player meets both statements within minutes of each other; the only reading that saves it is that day 1 IS Friday, which makes "has been empty since Friday" nonsense on a Friday afternoon.

**Fix:** Move the seal colony off Friday and off cave3's Tuesday. reef3 clue: "The last seal lies alone on the rock. Forty were here on Monday morning." correct: "since Monday"; wrong1: "for Monday"; wrong2 unchanged. Explanation: "A point in time takes SINCE: SINCE Monday. A length of time takes FOR: FOR two weeks."

## [BLOCKER] sound + cave1 + cave4 + wreck1

Quinn and the Selkie are in two places on the CAVES branch. `sound` puts you aboard the Selkie with Quinn and Hoy ("Choose where the Selkie searches first"). `cave1` then says "Quinn's boat is not at the mouth" and the correct answer is "Quinn has already gone into the cave ahead of you" — so the boat you just arrived on has vanished and its skipper has overtaken you. `cave4` has him leaving in the inflatable, and `wreck1` opens with "The Selkie stops above the Morag", a boat nobody has been aboard for four scenes.

**Fix:** cave1 clue: "Quinn's punt is tied off at the mouth. The storm lantern shows wet oar marks." (the Selkie is left outside with Hoy; Quinn rowed in). cave4 story: "The cave is filling fast. Quinn is aboard again, wet through. He runs the inflatable out to the waiting Selkie."

## [BLOCKER] all 25 explanations (drift…last)

The explanation style is split down the group seams. Chapter 1 (drift, bell, provost, hoy, jar, shed), the whole CAVES branch and all three wreck scenes write grammar tokens in lower case ("has + taken", "have never + seen", "Been is there and back"). The REEF branch, the CORRY branch, the NIGHT branch and Chapter 5 write them in CAPS with quoted forms ("ALREADY goes between HAS and MARKED", "\"Went\" is a past simple form"). Every player crosses at least one seam. The house rule and the most recent shipped RPG (frankenstein-green-prometheus-rpg: "The negative uses BE, not DO: he + ISN'T + going to + leave") are CAPS.

**Fix:** Convert the thirteen lower-case explanations to CAPS tokens. e.g. drift: "Present Perfect for a past event with a result now: HAS + TAKEN. THE SEA is singular, and TOOK is Past Simple." wreck1: "BEEN is there and back; GONE is still away. She is here. WENT is not a past participle." Also normalise the tense names — CAPS-group writes "past simple form" (corry1) where everyone else writes "Past Simple".

## [BLOCKER] barrels (against last)

Two defects in one item. (a) The distractor "threw" is correct English — "Hoy threw two barrels over the side today" is standard; the learner is being marked wrong for an acceptable sentence, which is the distractor-is-also-correct class that cost this repo eight preposition items. (b) It makes the last two questions of the game the same question: `barrels` is has thrown / threw and `last` is has come loose / came loose, back to back, both Present Perfect vs Past Simple, and slot 18 already owns that contrast. "threw" is also the only five-character option in a field of ten- and eleven-character ones.

**Fix:** Move the gap onto the time expression, which is what slot 17 is for. prompt: "Hoy has thrown two barrels over the side ___." correct: "today"; wrong1: "yesterday"; wrong2: "at six this morning". explanation: "TODAY is not finished, so Present Perfect fits. YESTERDAY and AT SIX are finished times: they need Past Simple."

## [BLOCKER] briefing card 3 (against jar) and card 1 (against drift)

The chart hands over two answers before the game starts. Card 3 reads "I HAVE NEVER seen one." and `jar`'s correct option is "I have never seen one this big." — the same string plus two words. Card 1 reads "The loch HAS taken them." and `drift`'s correct option is "The sea has taken them." — same verb, same object, same shape. The briefing is on screen immediately before question 1.

**Fix:** Change both examples to verbs the eighteen items never use. Card 1: "The tide HAS turned. The lamps HAVE burned all night." Card 3: "HAVE you EVER touched one? I HAVE NEVER been so close." (Card 4's "Hoy HAS JUST arrived. Baird HAS ALREADY refused." is fine — it narrates the chapter without printing an answer string.)

## [BLOCKER] endings master / missing / failed (against provost, night1, cover)

Three endings resolve a harbour closure that never happens anywhere in the script. The cover says "The Provost will not close the harbour", `provost` says Baird will not close the water, `night1` says "Baird keeps the water open". Then `master` says "At noon Baird lifts the order" — an order nobody issued — and `missing` and `failed` say "The harbour stays shut" / "The harbour is shut".

**Fix:** The scene graph is fixed, so fix the endings. master: "…At noon Baird sends the fleet out himself, and the boats go back on the water." missing: "…The harbour stays empty. Read the chart again and take the boat out." failed: "…No boat leaves the pier, and the story is not over."

## [BLOCKER] bell + cave2

The same item twice in different words, on the CAVES path. `bell` (slot 2, negative) is correct "They haven't come back." / wrong "They haven't came back." `cave2` (slot 8, YET) is correct "has not come back yet" / wrong "has not came back yet". Same verb, same negative, same participle error. Slot 8 is supposed to be paying for YET, and half of it is re-running slot 2.

**Fix:** Change cave2's verb and let YET carry the item. prompt unchanged; correct: "has not turned up yet"; wrong1: "has not turned up still"; wrong2: "has not turn up yet". Clue must stop pre-answering it: "The dinghy lamp burns on its hook, and both oars are shipped."

## [WARNING] reef2

The named grammar point never decides the answer. Options are "has not spoken" / "has spoken" / "has not speaking". The clue says "Quinn stares at it and stays silent", so "has spoken" is eliminated by the story, and "has not speaking" by surface shape. A learner who has no idea that YET needs a negative still scores. cave2, the parallel slot-8 item, does test it properly.

**Fix:** Make the wrong option a real YET error that the story cannot eliminate: correct "has not spoken"; wrong1 "did not speak"; wrong2 "has not spoke". Explanation: "YET needs the Present Perfect negative: HAS NOT + SPOKEN. Past Simple cannot take YET."

## [WARNING] answer key, all 25 items

In every one of the twenty-five items the correct option is never the longest of the three — it is shortest or tied-shortest thirteen times and never strictly longest. "Never pick the longest" is a free elimination on all eighteen questions, and it survives whatever order the builder shuffles them into. Combined with the fact that one distractor is a past-simple-for-participle error in thirteen of the eighteen items on a given path, several questions can be solved by surface shape alone.

**Fix:** Make the correct option the longest in at least four items. Worked examples: reef3 correct "since Monday morning" against "for Monday morning" and "since two weeks"; cave4 correct "have been in here for two hours now" against "have been in here since two hours"; corry2 wrong2 shortened to "The biggest thing I ever seen." so the correct option is longest.

## [WARNING] drift + reef1 + wreck3 (against corry1 / night1)

Subject agreement is the eliminable distractor in five of the eighteen items on a path — drift wrong1 "The sea have taken them", reef1 wrong2 "have already marked", wreck3 wrong2 "have sunk right here", plus corry1 and night1, whose whole slot (14) it is. Slot 1 and slot 14 end up testing the same thing in the same frame: singular noun + HAVE + participle, and singular noun + HAVE/HAS + past simple.

**Fix:** Leave agreement decisive only at corry1 and night1. drift wrong1 → "The sea has taked them." (over-regularised participle, matching the slot's stated point). reef1 wrong2 → "has already mark". wreck3 wrong2 → "has sank right here".

## [WARNING] jar + corry2

The same beat and the same verb twice, and every player gets both. `jar` is "I have never seen one this big." (slot 5) and `corry2` is "The biggest thing I have ever seen." (slot 15) — both are a character reacting to size with EVER/NEVER + SEEN. Ten questions apart, it reads as the writer reaching for the same line twice.

**Fix:** Keep the superlative line at corry2 and change the verb at jar: correct "I have never held one this big."; wrong1 "I haven't never held one this big."; wrong2 "I have never hold one this big." Explanation: "NEVER already means not at any time, so HAVE stays positive: HAVE NEVER + HELD. HELD, not HOLD."

## [WARNING] reef4

Two problems. "has fishing" is not a real B1 learner error — it is nonsense, which bible rule 2 forbids. And the prompt hands the learner "for thirty years" ready-made, so slot 10 (FOR + a period) is never actually chosen on the REEF path; the item ends up re-testing slot 1's HAS + participle. cave4, the parallel item, does make the learner pick FOR over SINCE and AGO.

**Fix:** wrong2 → "has fish" (bare verb after HAS, a genuine error, parallel to "has not speak"). If you want slot 10 to bite on both branches, move the marker into the options: prompt "Quinn has fished these waters ___." correct "for forty years", wrong1 "since forty years", wrong2 "forty years ago".

## [WARNING] reef4 + wreck3 + night2

Quinn's age does not add up across branches. reef4 says he has fished these waters for thirty years; wreck3 puts the Morag on the bottom twenty-eight years ago in 1998, with Quinn one of eleven crew in the water; night2 says he started fishing here at fourteen. That makes him forty-four now and sixteen on the night of the sinking, which sits badly against the bible's "old creel fisherman" with a lifetime's grudge. A REEF-then-WATCH player gets both numbers.

**Fix:** reef4 prompt → "Quinn ___ these waters for forty years." Forty years from fourteen makes him fifty-four now and twenty-six in 1998 — a crewman, and an old man today.

## [WARNING] drift + cave2

"Nobody is aboard." appears verbatim in both, and both scenes are the same reveal: a small boat found with its crew gone. A CAVES player gets the identical sentence and the identical beat at question 1 and question 8. There is also a wider tic — five sentences in one playthrough open with Nobody (drift, cave2 story, cave2 clue "nobody answers when you call", wreck2 "Nobody believed me", corry2 "Nobody speaks").

**Fix:** cave2 story: "Deep in the caves a dinghy turns slowly against the wall, half full of water. The thwart is empty." Vary at least two of the remaining Nobody openings.

## [WARNING] drift + shed

The bitten barrel is revealed twice in Chapter 1, five questions apart. drift's clue already says "The yellow barrel in the stern is chewed through"; shed's clue then plays it as the discovery — "bitten clean through the middle" — and shed's whole beat (Quinn turning a barrel round, you reaching for the radio) depends on it being new information. "clean through" also turns up again at reef2 ("cut clean through, edge to edge").

**Fix:** Hold the damage back at drift: clue → "The yellow barrel in the stern hangs by a stub of rope. Both coats are aboard." Then shed's bitten barrel lands as the reveal it is written to be, and reef2 keeps "clean through" to itself.

## [WARNING] sound + cave1…cave4

Hoy disappears for a quarter of the game on the CAVES branch. The route card promises "Hoy has the sonar ready. Choose where the Selkie searches first", and then four consecutive scenes mention only Quinn and you; she reappears at wreck1 putting on a mask. The sonar, the thing the choice was sold on, is never used on that branch at all.

**Fix:** Put her in the chamber scene: cave3 story → "The passage opens into a chamber. Hoy lights a dry ledge of heaped shells and smashed creels." And soften the route card: sound story → "Past the harbour mouth the channel divides. Hoy has the sonar ready. Choose where you search first."

## [WARNING] decision (WATCH route note) + night1

The route note sells the harbour choice on "The regatta boats are lit. Two hundred people on the water." The scene it leads into says the opposite one screen later: night1's clue is "a line of moored boats, every one of them empty" and its correct answer is "Every skipper in the harbour has come ashore." The stake the player chose evaporates.

**Fix:** WATCH note → "Two hundred people ashore, and the whole fleet moored and lit." The moored, lit, empty boats are then what night1 shows, and the people are on the quay where the player is.

## [WARNING] corry1 + night3

The two branch-final scenes are written as the same moment. corry1's clue is "The rope on the capstan is tight. Something below is pulling." night3's story is "A rope runs tight from the deck down into black water." The plates differ (whirlpool capstan by day, pontoon cleat by night), but the text is the same sentence, and a player who replays to take the other branch reads it twice.

**Fix:** Push corry1's wording onto the drum and the load, not the tightness: clue → "The rope is smoking round the iron drum. Something below is taking it." Leave night3 as the bar-tight rope.

## [WARNING] cave2 + night2

"still burning" describes a single small lamp over dark water in both — cave2's clue ("The dinghy lamp is still burning") and night2's story ("one small light is still burning"). One is on the CAVES branch, the other on the WATCH branch, so a replayer meets the same image and the same two words on the second run.

**Fix:** night2 story → "…Far out on the black water one small light still shows." The masthead lamp plate is unaffected.

## [WARNING] briefing (five cards)

The chart does not cover three things the questions actually test. (a) The contracted negative HASN'T / HAVEN'T + participle is never modelled, yet bell, reef2 and cave2 test it and five distractors across the game are built on it — card 4's "Nobody HAS left YET" is a positive verb form, not a negative. (b) BEEN vs GONE is a whole slot (wreck1) with no card, and the note's "not HAS GONE" is the only place GONE appears, used for a different purpose. (c) The unfinished time period (barrels: today) has no card; the note gives only the finished-time half of the contrast.

**Fix:** Card 2 carries the negative without losing result-now: "The coastguard HASN'T come, so the boats stay in." Card 1 carries been/gone alongside the form: "Hoy HAS BEEN down to the wreck. Quinn HAS GONE out to the Corry." Extend the note: "A finished time takes the PAST SIMPLE: the boat WENT out at six. TODAY and THIS WEEK are not finished, so they keep the Present Perfect."

## [WARNING] barrels

The panel contradicts itself on the count. The story has Hoy throwing the third barrel over the rail right now; the clue says "Two barrels float behind. The yellow barrel is next" — so the third is simultaneously going over and still to come. (The prompt's "two barrels … today" is the only part that is consistent.)

**Fix:** clue → "The day is not over. Two barrels float behind the boat." Drop "The yellow barrel is next." — the plate already has a barrel going over the rail.

## [WARNING] barrels + endings complete / failed

The last run happens twice at different times of day. `barrels` is daylight — "The day is not over", "today". `master` ends at noon, which fits. But `complete` says "By morning the loch is quiet" and `failed` opens at "Dawn" with the lifeboat "out since two", both of which read as a night action ending the following morning.

**Fix:** complete → "…By evening the loch is quiet." failed can keep dawn if the search runs overnight, but say so: "…The lifeboat has been out since dark. Nobody has found anything."

## [WARNING] bell + provost

The same error type in consecutive questions, with the same closing rule in both explanations. bell wrong1 is "They don't have come back." and provost wrong1 is "Do you have called the coastguard?" — both do-support with the perfect — and both explanations end on "the auxiliary is have, never do" / "Never use do as the auxiliary." Question 3 teaches nothing question 2 did not.

**Fix:** bell wrong1 → "They not have come back." (a real B1 omission error), and end its explanation on the participle instead: "Negative Present Perfect: HAVE NOT + COME. The negative needs the auxiliary HAVE, and CAME is Past Simple."

## [WARNING] cover + drift + bell

The missing-boat arithmetic does not close. The cover says the sea has taken two boats; drift brings one boat back in to the pier with two coats aboard; bell then rings "over two empty spaces" and counts the boats twice. If the drifted boat is in, only one berth should be empty — as written there are three boats in play and two crews accounted for.

**Fix:** Drop the number from bell's clue and let the title carry it: "The brass bell rings over the empty berths, and no engine answers from the Sound." Or keep the count and leave the creel boat adrift in the bay rather than alongside: drift story → "A creel boat turns in the bay with its rope trailing. The thwarts are empty."

