# -*- coding: utf-8 -*-
"""The topic map: which grammar point (or skill) each lesson is about.

Nothing in the catalogue says what a lesson teaches. `lessons.json` has a
title, a level and a file, and the library's own shelving is a set of
regexes in `library.html` that a Python script cannot call. This module is
the one place that knowledge lives in a form both `tools/seo.py` and
`tools/build_hubs.py` can read.

Why it exists at all: a search for "present perfect exercises B1" has to
land on *something*, and a lesson called "Block Camp — Present Perfect 1b:
How Long, And From When" is not it. The hub page for the topic is. Each
topic here becomes one page (`<slug>.html`), listing every lesson on that
point by level, under a few hundred words that actually explain the
grammar — which is the part a search engine can rank.

The classifier is regex-over-title-and-filename, like the library's, plus
`OVERRIDES` for titles that say nothing about their grammar ("Champions
League", "Grammar Atelier"). A topic's `pattern` is matched against the
lowercased title and the lowercased filename joined by a space. When you
add a lesson whose title is opaque, add it to OVERRIDES; when you add a
topic, give it a slug that is a real search phrase, and check the slug
does not collide with a folder or file already in the root.
"""
import re

# ── the topics ─────────────────────────────────────────────────────────
# slug, name (as printed on a page), short (what page_title appends),
# pattern, exclude (a pattern that vetoes the match), and the page copy.
#
# The copy is the point. Every paragraph is a plain statement about the
# grammar that a learner could act on and an answer engine could quote —
# the form, what it is for, and the mistake that gives the level away.
TOPICS = [
    dict(slug='present-simple', name='Present Simple', short='Present Simple',
         pattern=r'present simple|present-simple|present_simple',
         exclude=r'passive',
         group='Tenses', order=1,
         h1='Present <em>Simple</em>',
         desc='Present Simple English lessons from A1 to B1: habits, facts, timetables and states, with the third-person -s, questions with do/does, and time signals like always, usually and never.',
         intro=[
             'The Present Simple is the tense for things that are generally true: habits, routines, facts, and states that do not change from moment to moment. <em>I build. She builds. Water boils at 100 degrees. The train leaves at six.</em>',
             'The form is the base verb, with one exception that every learner meets on day one: <strong>he, she and it take -s</strong> (<em>he builds</em>, <em>she watches</em>, <em>it goes</em>). Questions and negatives use <em>do</em> or <em>does</em>, and the main verb goes back to its base form: <em>Does she build?</em>, not <em>Does she builds?</em>',
             'Its time signals are frequency words &mdash; <em>always, usually, often, sometimes, rarely, never</em> &mdash; and phrases like <em>every day</em> and <em>on Mondays</em>. Timetables and schedules also take the Present Simple even when they are about the future: <em>the match starts at eight</em>.',
             'The mistake to watch for is using it for something happening right now. <em>I work</em> is a fact about your life; <em>I am working</em> is what you are doing at this moment. That contrast is the whole of the next lesson.',
         ]),
    dict(slug='present-continuous', name='Present Continuous', short='Present Continuous',
         pattern=r'present continuous|present-continuous',
         exclude=r'passive|present simple vs',
         group='Tenses', order=2,
         h1='Present <em>Continuous</em>',
         desc='Present Continuous English lessons from A1 to B1: what is happening now, temporary situations, plans that are already arranged, and the difference from the Present Simple.',
         intro=[
             'The Present Continuous describes an action in progress: happening now, around now, or as a temporary situation. <em>She is building a wall. I am staying with friends this week. They are working on it.</em>',
             'The form is <strong>am / is / are + verb-ing</strong>. Because the auxiliary is <em>be</em>, questions are made by inversion (<em>Is she building?</em>) and negatives with <em>not</em> (<em>She isn&rsquo;t building</em>). There is no <em>do</em> anywhere in it.',
             'It also carries fixed future arrangements &mdash; <em>I am meeting her on Friday</em> &mdash; and, with <em>always</em>, an irritated habit: <em>He is always losing his keys</em>. Time signals: <em>now, at the moment, today, this week, these days, still</em>.',
             'State verbs resist it. <em>Know, want, like, believe, need, own</em> describe a condition rather than an activity, so <em>I know</em> is right and <em>I am knowing</em> is not. The exception list is short, and the lessons here drill it.',
         ]),
    dict(slug='past-simple', name='Past Simple', short='Past Simple',
         pattern=r'past simple|past-simple|past_simple|penguins_past',
         exclude=r'passive',
         group='Tenses', order=3,
         h1='Past <em>Simple</em>',
         desc='Past Simple English lessons from A1 to B2: finished actions at a finished time, regular -ed and the irregular verbs, questions and negatives with did, and how it differs from the Present Perfect.',
         intro=[
             'The Past Simple is for an action that started and finished in the past, at a time that is stated or understood. <em>We built the wall yesterday. She left at six. The war ended in 1945.</em>',
             'Regular verbs add <strong>-ed</strong>; irregular verbs have to be learned (<em>go &rarr; went, build &rarr; built, see &rarr; saw</em>). Questions and negatives use <strong>did</strong>, and the main verb returns to its base form: <em>Did you go?</em> and <em>I didn&rsquo;t go</em>, never <em>didn&rsquo;t went</em>.',
             'Time signals point at a finished time: <em>yesterday, last week, in 2019, two hours ago, when I was a child</em>. Any of those words in the sentence rules out the Present Perfect.',
             'The contrast every B1 learner has to master is Past Simple against Present Perfect. <em>I lost my keys</em> is a past event; <em>I have lost my keys</em> says they are still lost now. Several lessons below are built on exactly that line.',
         ]),
    dict(slug='past-continuous', name='Past Continuous', short='Past Continuous',
         pattern=r'past continuous|past-continuous',
         exclude=r'passive',
         group='Tenses', order=4,
         h1='Past <em>Continuous</em>',
         desc='Past Continuous English lessons from A1 to B1: an action in progress in the past, interrupted by a Past Simple event, with while, when and as.',
         intro=[
             'The Past Continuous sets a scene: an action that was in progress at a moment in the past. <em>At nine o&rsquo;clock I was working. It was raining when we arrived.</em>',
             'The form is <strong>was / were + verb-ing</strong>. It rarely stands alone. Its usual job is background for a Past Simple event that cuts across it: <em>I was crossing the road when a car hit me</em>. The long action takes the continuous; the short one that interrupts it takes the simple.',
             'The signals are <em>while</em> and <em>as</em> for the long action, <em>when</em> for the short one, and a clock time for the moment of the scene: <em>at midnight, at that moment, all evening</em>.',
             'The mistake is using it for a sequence of finished events. <em>I was waking up, I was having breakfast and I was leaving</em> is wrong; those are three completed actions in order, and they take the Past Simple.',
         ]),
    dict(slug='present-perfect', name='Present Perfect', short='Present Perfect',
         pattern=r'present perfect|present-perfect|perfect vs simple|perfect-vs-simple',
         exclude=r'present perfect continuous|present-perfect-continuous|passive',
         group='Tenses', order=5,
         h1='Present <em>Perfect</em>',
         desc='Present Perfect English lessons from A1 to B2: past actions with a present result, life experience with ever and never, unfinished time with since and for, and the difference from the Past Simple.',
         intro=[
             'The Present Perfect connects the past to now. It is used for a past action whose result matters in the present (<em>I have lost my keys</em> &mdash; they are still lost), for experience in a life that is still going on (<em>She has been to Japan</em>), and for something that began in the past and continues (<em>We have lived here since 2015</em>).',
             'The form is <strong>have / has + past participle</strong>: the third column of the irregular verb table (<em>gone, built, seen</em>), or <em>-ed</em> for regular verbs. Questions invert <em>have</em>: <em>Have you finished?</em>',
             'Its time signals are open or unfinished: <em>ever, never, already, yet, just, so far, today, this week, since, for</em>. The moment a finished time appears &mdash; <em>yesterday, in 2019, ago</em> &mdash; the sentence switches to the Past Simple.',
             '<em>Since</em> takes a point (<em>since Monday</em>); <em>for</em> takes a length (<em>for three days</em>). <em>Been</em> means went and came back; <em>gone</em> means still away. The lessons here drill each of these lines separately before mixing them.',
         ]),
    dict(slug='present-perfect-continuous', name='Present Perfect Continuous', short='Present Perfect Continuous',
         pattern=r'present perfect continuous|present-perfect-continuous',
         exclude=r'passive',
         group='Tenses', order=6,
         h1='Present Perfect <em>Continuous</em>',
         desc='Present Perfect Continuous English lessons at B1: have been doing, for how long, and activities whose effects you can still see, against the Present Perfect Simple.',
         intro=[
             'The Present Perfect Continuous is about duration and activity rather than result. <em>I have been building this wall for three hours</em> says how long the activity has been going on, and it may not be finished; <em>I have built the wall</em> says it is done.',
             'The form is <strong>have / has been + verb-ing</strong>. It answers <em>How long?</em> and it explains present evidence: <em>You&rsquo;re covered in mud &mdash; have you been digging?</em>',
             'Time signals: <em>for, since, how long, all day, lately, recently</em>. State verbs stay in the simple form: <em>I have known her for years</em>, not <em>I have been knowing</em>.',
             'The choice against the Present Perfect Simple is the whole difficulty. Count the results and you want the simple (<em>I have written three emails</em>); measure the time and you want the continuous (<em>I have been writing emails all morning</em>).',
         ]),
    dict(slug='past-perfect', name='Past Perfect', short='Past Perfect',
         pattern=r'past perfect|past-perfect',
         exclude=r'passive',
         group='Tenses', order=7,
         h1='Past <em>Perfect</em>',
         desc='Past Perfect English lessons at B1 and B2: had done for the earlier of two past events, with by the time, before, after and already, plus the Past Perfect Continuous.',
         intro=[
             'The Past Perfect is the past of the past. When a story is already in the Past Simple and you need to reach further back, <em>had + past participle</em> does it: <em>When we arrived, the film had started.</em> The arriving is past; the starting is earlier still.',
             'It is only needed when the order matters and is not obvious. <em>I had breakfast and left</em> is fine in the Past Simple because the order is clear. <em>By the time I got there, she had left</em> needs the Past Perfect because the two events are being compared.',
             'Signals: <em>by the time, before, after, already, until, as soon as</em>, and reported thoughts and speech (<em>He said he had seen it</em>). The continuous form, <em>had been doing</em>, gives the earlier action duration: <em>She had been waiting for an hour when the bus came.</em>',
             'The mistake is overuse: putting everything old in the Past Perfect. It marks the earlier of two events, and once that is established the story drops back into the Past Simple.',
         ]),
    dict(slug='future-tenses', name='Future Tenses', short='Future Tenses',
         pattern=r'future simple|future-simple|going to|going-to|\bwill\b|future continuous|future perfect|future-perfect|future you',
         exclude=r'passive',
         group='Tenses', order=8,
         h1='The <em>Future</em>: will, going to and beyond',
         desc='Future tense English lessons from A1 to C1: will for decisions and predictions, going to for plans and evidence, the Present Continuous for arrangements, and the Future Continuous and Future Perfect.',
         intro=[
             'English has no single future tense. It has several ways of talking about the future, and the choice says how sure you are and whether a plan already exists.',
             '<strong>Will</strong> is for a decision made at the moment of speaking (<em>I&rsquo;ll get it</em>), a prediction based on opinion (<em>I think it will rain</em>), and promises and offers. <strong>Going to</strong> is for a plan you already have (<em>We&rsquo;re going to build a bigger one</em>) and a prediction based on evidence you can see (<em>Look at those clouds &mdash; it&rsquo;s going to rain</em>).',
             'The <strong>Present Continuous</strong> covers fixed arrangements with a time and place (<em>I&rsquo;m meeting her at six</em>). Above B1 come the <strong>Future Continuous</strong> for an action in progress at a future moment (<em>This time tomorrow I&rsquo;ll be flying</em>) and the <strong>Future Perfect</strong> for something finished before a future point (<em>By Friday we&rsquo;ll have finished</em>).',
             'The classic mistake is <em>will</em> for a plan that was made earlier. If the decision already exists, it is <em>going to</em>; if you are deciding as you speak, it is <em>will</em>. The Block Camp and Sherpa Tensing lessons below drill exactly that line.',
         ]),
    dict(slug='passive-voice', name='Passive Voice', short='Passive Voice',
         pattern=r'passive',
         group='Grammar', order=10,
         h1='The <em>Passive</em> Voice',
         desc='Passive voice English lessons from A2 to C1: be + past participle in every tense, when to leave out the agent, by-phrases, and the causative have something done.',
         intro=[
             'The passive puts the thing that receives the action at the front of the sentence, because that is what the sentence is about. <em>The bridge was built in 1932</em> is about the bridge; whoever built it is either unknown, obvious or unimportant.',
             'The form is <strong>be + past participle</strong>, and it is <em>be</em> that carries the tense: <em>is built, is being built, was built, has been built, will be built, is going to be built</em>. The participle never changes.',
             'The agent, when it is worth naming, comes after <em>by</em>: <em>The novel was written by a teenager.</em> Most passives have no agent at all, which is the point of them: processes, rules, news and science are written this way because the doer does not matter.',
             'Above B1 comes the causative &mdash; <em>I had my car repaired</em> &mdash; where you arrange for someone else to do something. The Sherpa Tensing descent and Block Camp II below take the passive through every tense in the same order the active forms were taught.',
         ]),
    dict(slug='modal-verbs', name='Modal Verbs', short='Modal Verbs',
         pattern=r'\bmodal|\bmust\b|have to|\bshould\b|might vs|deduction|regrets',
         group='Grammar', order=11,
         h1='Modal <em>Verbs</em>',
         desc='Modal verb English lessons from A2 to B2: must, have to, should, can, could, might and may for obligation, advice, ability and possibility, and the past modals should have and must have.',
         intro=[
             'Modal verbs add an attitude to the main verb: how necessary, how likely, how allowed. <em>Must, have to, should, can, could, may, might, will, would.</em> They take the base verb with no <em>to</em> (<em>you must go</em>), they do not take <em>-s</em> for he and she, and they make questions by inversion.',
             '<strong>Obligation:</strong> <em>must</em> is the speaker&rsquo;s own rule; <em>have to</em> is a rule from outside. <em>Mustn&rsquo;t</em> forbids; <em>don&rsquo;t have to</em> means there is no need &mdash; and confusing those two is the most common modal error in every language group.',
             '<strong>Advice</strong> is <em>should</em>. <strong>Possibility</strong> runs from <em>might</em> and <em>may</em> to <em>could</em>, and <strong>deduction</strong> uses <em>must</em> for near-certainty and <em>can&rsquo;t</em> for its opposite: <em>She must be at home; the lights are on.</em>',
             'Past modals add <em>have + past participle</em>: <em>should have called</em> (a regret), <em>must have left</em> (a deduction about the past), <em>could have won</em> (a missed possibility). Those are B2 material and have their own lessons below.',
         ]),
    dict(slug='prepositions', name='Prepositions', short='Prepositions',
         pattern=r'preposition',
         group='Grammar', order=12,
         h1='<em>Prepositions</em>',
         desc='Preposition English lessons from A2 to C1: in, on and at for time and place, dependent prepositions after verbs and adjectives, and the advanced pairs that separate B2 from C1.',
         intro=[
             'Prepositions are short words that fix a relationship: where, when, how, and for what. <em>In, on, at, by, for, with, from, to, about.</em> There are few of them and no rule covers all their uses, which is why they are learned in chunks rather than as a table.',
             'The place and time set is the A2 core. <strong>At</strong> a point (<em>at the door, at six</em>), <strong>on</strong> a surface or a day (<em>on the table, on Monday</em>), <strong>in</strong> a space or a period (<em>in the box, in June, in 2020</em>). The exceptions &mdash; <em>at night, at the weekend, in the morning</em> &mdash; are the part that has to be memorised.',
             'From B1 the work moves to dependent prepositions: the one a particular verb or adjective demands. <em>Depend on, interested in, good at, afraid of, responsible for.</em> The preposition is part of the word and goes with it everywhere.',
             'At C1 the pairs get fine: <em>in time</em> against <em>on time</em>, <em>made of</em> against <em>made from</em>, <em>compared to</em> against <em>compared with</em>. The lessons below put those choices inside stories &mdash; a crime file, a presidency, a small town with a lot of secrets &mdash; so the chunk is remembered with its context.',
         ]),
    dict(slug='gerunds-and-infinitives', name='Gerunds and Infinitives', short='Gerunds &amp; Infinitives',
         pattern=r'gerund|infinitive|sailing the seas',
         exclude=r'going to|going-to',
         group='Grammar', order=13,
         h1='Gerunds and <em>Infinitives</em>',
         desc='Gerund and infinitive English lessons at B1: verbs followed by -ing, verbs followed by to, the ones that take both with a change of meaning, and gerunds as subjects and after prepositions.',
         intro=[
             'When one verb follows another, the second one takes a form: the gerund (<em>-ing</em>) or the infinitive (<em>to + verb</em>). Which one depends on the first verb, and there is no rule that predicts it &mdash; only patterns, and a list.',
             '<strong>Gerund:</strong> after <em>enjoy, finish, avoid, mind, suggest, keep, practise</em>, after every preposition (<em>good at swimming, before leaving</em>), and as the subject of a sentence (<em>Smoking is banned</em>).',
             '<strong>Infinitive:</strong> after <em>want, decide, hope, plan, promise, agree, refuse, manage</em>, after adjectives (<em>happy to help</em>), and to give a reason (<em>I went out to buy milk</em>).',
             'A few verbs take both with a change in meaning. <em>Stop smoking</em> means you quit; <em>stop to smoke</em> means you paused for a cigarette. <em>Remember doing</em> is a memory; <em>remember to do</em> is a task. Those pairs are where the lessons below spend most of their time.',
         ]),
    dict(slug='conditionals', name='Conditionals', short='Conditionals',
         pattern=r'conditional|if-clauses|castle of if|castle-of-if',
         group='Grammar', order=14,
         h1='<em>Conditionals</em>',
         desc='Conditional English lessons from B1 to C2: zero, first, second and third conditionals, mixed conditionals, and if-clauses in business and argument.',
         intro=[
             'A conditional sentence has an <em>if</em>-clause and a result, and the tense in each half says how real the condition is.',
             '<strong>Zero:</strong> <em>if + present, present</em> for things that are always true (<em>If you heat ice, it melts</em>). <strong>First:</strong> <em>if + present, will</em> for a real possibility (<em>If it rains, we&rsquo;ll stay in</em>). <strong>Second:</strong> <em>if + past, would</em> for something unreal or unlikely now (<em>If I had the money, I would buy it</em>). <strong>Third:</strong> <em>if + past perfect, would have</em> for an unreal past (<em>If you had called, I would have come</em>).',
             'The <em>if</em>-clause never takes <em>will</em> or <em>would</em>: <em>If it will rain</em> is the error that gives a B1 speaker away. Mixed conditionals join a past condition to a present result (<em>If I had studied, I would be a doctor now</em>) and are C1 territory.',
             'In business and debate the conditionals are the language of negotiation and consequence: <em>If you order five hundred, we can drop the price. Had we known, we would have acted sooner.</em> The lessons below use them that way.',
         ]),
    dict(slug='used-to', name='Used To and Be Used To', short='Used To',
         pattern=r'used to|used-to',
         group='Grammar', order=15,
         h1='<em>Used to</em> and <em>be used to</em>',
         desc='Used to English lessons at A2 and B1: used to + verb for past habits that have stopped, be used to + -ing for what is familiar, and get used to for what is becoming familiar.',
         intro=[
             'Three phrases that look alike and mean different things. <strong>Used to + verb</strong> is a past habit or state that is no longer true: <em>I used to smoke. There used to be a cinema here.</em> Its negative and question forms use <em>did</em>: <em>I didn&rsquo;t use to like coffee. Did you use to play?</em>',
             '<strong>Be used to + -ing</strong> (or a noun) means accustomed to: something is familiar and no longer difficult. <em>I&rsquo;m used to getting up early.</em> <strong>Get used to</strong> is the process of becoming accustomed: <em>You&rsquo;ll get used to the noise.</em>',
             'The difference is in the verb form after <em>to</em>. <em>Used to work</em> is a past habit; <em>used to working</em> is a present familiarity. One letter, opposite meanings.',
         ]),
    dict(slug='phrasal-verbs', name='Phrasal Verbs and Collocations', short='Phrasal Verbs',
         pattern=r'phrasal verb|take.{0,3}put|make.{0,3}do|make-v-do',
         group='Grammar', order=16,
         h1='Phrasal Verbs and <em>Collocations</em>',
         desc='Phrasal verb English lessons from A2 to B2: take, put, make and do, separable and inseparable verbs, and the collocations native speakers reach for.',
         intro=[
             'A phrasal verb is a verb plus a particle whose meaning is not the sum of its parts. <em>Put off</em> is postpone; <em>take up</em> is start a hobby; <em>give up</em> is stop. They are the everyday register of spoken English, and formal single-word equivalents (<em>postpone, commence, cease</em>) sound stiff in conversation.',
             'Some are separable: the object can go between the verb and particle, and a pronoun must (<em>put it off</em>, never <em>put off it</em>). Some are inseparable (<em>look after her</em>). Dictionaries mark which is which; the lessons here drill the common ones until the choice is automatic.',
             'Collocations are the same idea one step wider: <em>make a decision</em> but <em>do the shopping</em>, <em>take a photo</em> but <em>put on weight</em>. There is no logic to learn, only pairs to remember, and the fastest way to remember them is in a story where they do work.',
         ]),
    dict(slug='tense-review', name='Tense Review and Grammar Tests', short='Tense Review',
         pattern=r'tense review|all tenses|mixed grammar|grammar test|grammar court|grammar jail|grammar atelier|route map|route-map|the trial|test prep|time signals',
         group='Tenses', order=9,
         h1='Tense <em>Review</em> and Grammar Tests',
         desc='English tense review lessons and grammar tests from A1 to C1: every tense side by side, the time signals that choose between them, and scored tests that show which lesson to go back to.',
         intro=[
             'Once the tenses have been taught one at a time, the real work is choosing between them at speed. These lessons put several side by side and make the learner pick: <em>I lived</em> or <em>I have lived</em>, <em>I was doing</em> or <em>I did</em>, <em>will</em> or <em>going to</em>.',
             'The fastest route through that choice is the time signal. <em>Yesterday</em> forces the Past Simple; <em>since</em> forces the Present Perfect; <em>while</em> sets up a Past Continuous; <em>by the time</em> reaches for the Past Perfect. The Time Signals series below is built on that principle, one tense per lesson, for A1 upwards.',
             'The tests are scored and the score is diagnostic: each wrong answer names the tense it belongs to, so a class knows which lesson to revisit. The <a href="level-checker.html">free Level Checker</a> does the same thing adaptively in six questions a level.',
         ]),
    dict(slug='business-english', name='Business English', short='Business English',
         pattern=r'business|negotiat|talking with clients|meetings?\b|professional speaking|dailies review|workplace|decision-making|contingency|fireshield|design pitch|product strategy|product speaking|construction|contracts?\b|refinery|turnaround|energy|geoscience|emails|feedback that lands|escalating|carrying the load|risk management|risk-management|presentations?\b|pitch|e-?commerce|architectural|interior design|vapour|membrane|impostor|self-improvement|ten-year bet|the docket|koolhaas|koolhas|harari|geopolitics',
         group='Skills', order=20,
         h1='Business <em>English</em>',
         desc='Business English lessons from B1 to C2: meetings, negotiation, presentations, emails, feedback, client conversations and the vocabulary of construction, energy, architecture and design.',
         intro=[
             'Business English is not a separate grammar. It is the same tenses and modals pointed at a different job: getting a decision, holding a room, softening a refusal, escalating a complaint without burning the relationship.',
             'The lessons here are built around the situations that professionals actually meet &mdash; a status meeting, a pitch, a negotiation that stalls, an email chain that has gone cold, a colleague who is not pulling their weight &mdash; and the language is taught as phrases that do a job, not as vocabulary lists. Most end in a role-play, because the point is to produce the language under pressure, not to recognise it.',
             'Several are written for a specific industry: construction contracts and site presentations, refinery turnarounds, energy project management, geoscience, architecture and interior design. The grammar inside them is general; the vocabulary is the vocabulary of that trade.',
             'Levels run from B1 (talking about your product, talking with clients) through B2 (negotiation, meetings, business conditionals) to C1 and C2 (managing risk, decision-making under uncertainty, executive role-plays).',
         ]),
    dict(slug='ielts', name='IELTS Academic', short='IELTS',
         pattern=r'ielts', page='ielts.html',
         group='Skills', order=21, h1='', desc='', intro=[]),
    # The catch-all. Anything that is in no grammar topic and is not IELTS
    # is a vocabulary or topic lesson — football, hiking, dinosaurs, film —
    # and "football vocabulary B1" is a search someone actually types.
    dict(slug='english-vocabulary', name='Vocabulary and Topic Lessons', short='Vocabulary',
         pattern=None,
         group='Skills', order=22,
         h1='English <em>Vocabulary</em>, by Topic',
         desc='English vocabulary lessons from A1 to C2 built around a subject — football, skiing, hiking, Minecraft, Lego, film, nature, food, architecture — with the words taught in context and used in a speaking task.',
         intro=[
             'Vocabulary sticks when it does a job. A list of forty sports words is forgotten by Friday; the same words met inside a match report, argued over in a role-play and then used to describe your own weekend are still there a month later. Every lesson here is built that way: a subject the class actually cares about, the words it needs, and a task that forces them out.',
             'The subjects are the ones Innes&rsquo;s students brought to class &mdash; football and the Champions League, skiing, mountain biking, tennis, water polo, hiking, dinosaurs, Minecraft and Lego, film and television, food, travel, nature and conservation, architecture. The level is set by the language, not the subject: there is A1 food and C1 conservation.',
             'Each deck teaches the words with a picture and a definition, checks them with a sort or a gap-fill, and finishes with speaking &mdash; a description, a discussion or a role-play &mdash; because a word you have said out loud under a little pressure is a word you own.',
         ]),
]

# Titles that say nothing about their grammar, mapped by file to the topic
# slugs they belong under. Regexes above still run; this adds to them.
OVERRIDES = {
    'champions_league_english.html': [],                # football vocabulary; no grammar hub
    'top-gear-skiing-lesson.html': ['past-simple'],
    'forbes-english-golf-lesson.html': ['past-simple', 'present-perfect'],
    'mtb-perfect-vs-simple.html': ['past-simple', 'present-perfect'],
    'forbes-english-lesson (2).html': ['conditionals', 'business-english'],
    'forbes-english-lesson-curious incident.html': ['conditionals'],
    'geopolitics-english-class.html': ['conditionals'],
    'forbes-english-lesson-TopGear.html': ['passive-voice'],
    'forbes-english-lego-passive-active.html': ['passive-voice'],
    'active_passive_refinery_lesson.html': ['passive-voice', 'business-english'],
    'active_passive_refinery_quiz_part2.html': ['passive-voice', 'business-english'],
    'vw_grammar_atelier_final.html': ['tense-review'],
    'full_grammar_test.html': ['tense-review'],
    'forbes-english-b1-mixed-grammar-test.html': ['tense-review'],
    'forbes-english-b1-mixed-grammar-test-part2.html': ['tense-review'],
    'nietzsche-grammar-test.html': ['tense-review'],
    'nietzsche-grammar-test-part2.html': ['tense-review'],
    'nietzsche-grammar-test-part3.html': ['tense-review'],
    'stranger-things-test.html': ['tense-review'],
    'forbes-english-b2-lesson.html': ['tense-review'],
    'tense-review-minecraft.html': ['tense-review'],
    'forbes-english-venezuela.html': ['used-to'],
    'taekwondo-regrets.html': ['modal-verbs'],
    'thornwick-deduction.html': ['modal-verbs'],
    'minecraft-lesson.html': ['modal-verbs'],
    'blockcamp-passive-trial.html': ['passive-voice'],
    'sherpa-tensing-cloud-causative.html': ['passive-voice'],
    'sherpa-tensing-route-map.html': ['tense-review'],
    'harry-quebert-b2.html': [],
    'forbes-english-lesson-2.html': ['business-english'],
    'forbes-english-speaking-2.html': ['business-english'],
    'forbes-gap-fill.html': ['business-english'],
    'forbes-english-lesson (talking with clients).html': ['business-english'],
    'forbes-english-lesson (flow).html': ['business-english'],
    'forbes-english-lesson (data).html': ['business-english'],
    'forbes-english-lesson-managing energy.html': ['business-english'],
    'forbes-english-negotiating part2.html': ['business-english'],
    'forbes-english-meetings.html': ['business-english'],
    'forbes-roleplay-reddit-french-TEST-p3.html': ['business-english'],
    'forbes-dnd-rpg.html': ['business-english'],
    'forbes-dnd-rpg-part2.html': ['business-english'],
    'forbes-english-ukraine-presentations-c1.html': ['business-english'],
    'ukraine-reconstruction-lesson.html': ['business-english'],
    'forbes-ukraine-presentations-c1.html': ['business-english'],
    'forbes-english-architecture-c1 (1).html': ['business-english'],
    'forbes-english-construction-presentations.html': ['business-english'],
    'forbes-interior-design-c1.html': ['business-english'],
    'interior-design-vocabulary.html': ['business-english'],
    'forbes-architectural-vocabulary.html': ['business-english'],
    'forbes-architectural-vocabulary-part2.html': ['business-english'],
    'reading-the-elevation-c1.html': ['business-english'],
    'reading-a-room-cafe-kowloon.html': ['business-english'],
    'forbes_english_lesson.html': ['business-english'],
    'forbes-geoscience-phrases.html': ['business-english'],
    'fireshield-pitch.html': ['business-english'],
    'workplace-roleplay-live.html': ['business-english'],
    'feedback-that-lands.html': ['business-english'],
    'dailies-review-feedback.html': ['business-english'],
    'contingency-trade-offs-vocab.html': ['business-english'],
    'Forbes English - Decision-Making Under Uncertainty.html': ['business-english'],
    'Forbes English - Product Strategy & Market Research Speaking (2).html': ['business-english'],
    'forbes-english-product-speaking.html': ['business-english'],
    'forbes-english-emails calls part3.html': ['business-english'],
    'forbes-escalating-a-complaint-c1.html': ['business-english'],
    'carrying-the-load-c1.html': ['business-english'],
    'forbes-risk-management-c1-c2.html': ['business-english'],
    'forbes-construction-contracts.html': ['business-english'],
    'vapour-barriers-lesson.html': ['business-english'],
    'forbes-english-the-ten-year-bet-C1.html': ['business-english'],
    'forbes-english-the-docket-b2.html': ['business-english'],
    'koolhas & Lamb.html': ['business-english'],
    'fashion_english_exercises (2).html': ['business-english'],
    'fashion_english_exercises.html': ['business-english'],
    'eintracht-gerunds-lesson.html': ['gerunds-and-infinitives'],
    'lesson1_gerunds_football.html': ['gerunds-and-infinitives'],
    'forbes-english-tennis-present-perfect-a2.html': ['present-perfect'],
    'forbes-english-present-perfect-lego-b1.html': ['present-perfect'],
    'present-simple-vs-continuous.html': ['present-simple', 'present-continuous'],
    'forbes-english-modal-verbs-B1.html': ['modal-verbs'],
    'forbes-english-b1-modal-verbs-fire-brigade.html': ['modal-verbs'],
    'english_firefighter_v3.html': ['modal-verbs'],
    'german_firefighter_happy.html': ['modal-verbs'],
    'must-have-to-lego-polish.html': ['modal-verbs'],
    'must-have-to-vfb-stuttgart.html': ['modal-verbs'],
    'forbes-english-past-modals-minecraft.html': ['modal-verbs'],
    'block-camp/dracula-castle-of-if.html': ['conditionals', 'passive-voice'],
    'block-camp/long-way-home-rpg.html': ['tense-review', 'past-simple', 'past-continuous', 'past-perfect'],
}

BY_SLUG = {t['slug']: t for t in TOPICS}
_LEVEL_ORDER = ['A1', 'A1-A2', 'A2', 'A2-C1', 'B1', 'B1-B2', 'B2', 'C1', 'C1-C2', 'C2']


def topics_for(row):
    """The topic slugs a catalogue row belongs to, in TOPICS order."""
    hay = ('%s %s' % (row.get('title') or '', row.get('file') or '')).lower()
    hay = hay.replace('—', ' ').replace('–', ' ')
    found = set(OVERRIDES.get(row.get('file'), []))
    for t in TOPICS:
        if t['pattern'] and re.search(t['pattern'], hay) and not (
                t.get('exclude') and re.search(t['exclude'], hay)):
            found.add(t['slug'])
    if not found:
        found.add('english-vocabulary')
    return [t['slug'] for t in TOPICS if t['slug'] in found]


def title_has_topic(title, slug):
    """Does the printed title already say this topic? Decides whether
    page_title() should append it. Matched against the title alone,
    without the filename, and without OVERRIDES."""
    t = BY_SLUG[slug]
    hay = (title or '').lower().replace('—', ' ').replace('–', ' ')
    return bool(t['pattern'] and re.search(t['pattern'], hay))


def hub_url(slug):
    """Where a topic's page lives. Most are generated; IELTS already has a
    hand-built route page and keeps it."""
    return BY_SLUG[slug].get('page') or '%s.html' % slug


def generated():
    """The topics build_hubs.py writes a page for."""
    return [t for t in TOPICS if not t.get('page')]


def level_key(level):
    return _LEVEL_ORDER.index(level) if level in _LEVEL_ORDER else 99


def level_span(rows):
    """'A1 to B2' from a set of rows, for a hub's eyebrow and description."""
    lv = sorted({r.get('level') for r in rows if r.get('level')}, key=level_key)
    if not lv:
        return ''
    lo = lv[0].split('-')[0]
    hi = lv[-1].split('-')[-1]
    return lo if lo == hi else '%s to %s' % (lo, hi)


def members(rows, images, coming_soon):
    """{slug: [row, ...]} for every finished lesson, sorted by level then
    title. `coming_soon` is seo.coming_soon, passed in so this module does
    not import seo (seo imports this)."""
    out = {t['slug']: [] for t in TOPICS}
    for r in rows:
        if coming_soon(r, images):
            continue
        for slug in topics_for(r):
            out[slug].append(r)
    for slug in out:
        out[slug].sort(key=lambda r: (level_key(r.get('level')),
                                      r.get('access') == 'pro',
                                      (r.get('title') or '').lower()))
    return out


def hero(rows, images):
    """A hub's share image: the first free lesson's hero, else the first
    lesson's. Returns a site-relative path or None."""
    for r in rows:
        if r.get('access') != 'pro' and images.get(r['file']):
            return '/' + images[r['file']]
    for r in rows:
        if images.get(r['file']):
            return '/' + images[r['file']]
    return None


# What seo.py needs to give each hub page a title, description, priority and
# hero: the same tuple shape as its PAGES table. The hero is the picture of
# the first free lesson on the topic, chosen at build time — see build_hubs.
def hub_pages():
    out = {'grammar.html': (
        'English Grammar by Topic: Tenses, Modals, Passive, Prepositions',
        'Every Forbes English grammar lesson sorted by topic and level — '
        'the tenses, modal verbs, the passive, prepositions, conditionals, '
        'gerunds and infinitives — each with the rule explained and the '
        'lessons that drill it.', 0.9)}
    for t in generated():
        out[hub_url(t['slug'])] = (
            '%s: English lessons and exercises' % t['name'], t['desc'], 0.8)
    return out
