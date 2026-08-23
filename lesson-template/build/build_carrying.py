# -*- coding: utf-8 -*-
"""Carrying the Load (C1) — new lesson, built to the deck house style.

Source is a Liane Davey blog post Innes supplied on dealing with a co-worker
who does not pull their weight. Nothing from it is reproduced: the four-rung
escalation model and the behaviour/impact/question unit are the ideas kept,
and every paragraph, every example script and every distractor here is
written fresh. The names in the examples are new for the same reason.

Four Black Isler office illustrations came with the brief. The widest — the
row of profiles in coral, cream and slate — is the cover and drives the
palette; the other three rotate as per-section backgrounds.

The one thing worth carrying forward: this lesson's whole subject is the
difference between a sentence that reports behaviour and a sentence that
assigns a motive, so the ANATOMY section's four options are a closed set
shown on every item. That set had to be length-balanced by hand — with
"Interpretation" naturally the longest label, the key leaked on two items
until the four labels were rewritten to 33–36 characters.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'carrying-the-load-c1.html'
F = 'CarryingTheLoad'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e0c09;
  --surface       : #1c1712;
  --surface2      : #29221a;
  --border        : #a36352;
  --text          : #f5f2f2;
  --text-dim      : #bfa9a3;
  --accent        : #e1907a;
  --accent-bright : #f1bfb2;
  --accent-dim    : #ca5535;
  --secondary     : #8ba6af;
  --contrast      : #1dedb5;''' % F

# ── reading: five slides, two cards each ───────────────────────────────
READING = [
    ('r1Title', 'The cost of silence',
     'An uneven workload rarely announces itself. It accumulates &mdash; a deadline absorbed here, a weekend surrendered there, a plan rewritten at midnight because the version that finally arrived was unusable.',
     'The colleague taking up the slack says nothing: partly politeness, partly a suspicion that complaining would look petty. Resentment that is never spoken does not fade. It hardens, and arrives later as an accusation rather than a request.'),
    ('r2Title', 'Posture before words',
     'It is vanishingly unlikely that your colleague wakes up hunting for fresh ways to let the team down. Far more often they are drowning: under-skilled for the task, over-committed elsewhere, or working to priorities nobody has reconciled with yours.',
     'Assuming struggle rather than malice is not naivety. It is tactical. A conversation that opens from curiosity gets you an explanation. One that opens from a verdict gets you a defence.'),
    ('r3Title', 'The unit of feedback',
     'Three moving parts. State the behaviour as a camera would have recorded it: what was agreed, what arrived, when. Name the impact on you, concretely and in the first person. Then hand the conversation over with a real question.',
     '&ldquo;We agreed the draft would reach me on Tuesday; it came at four on Friday. To hold my own deadline I worked Saturday, and I was frustrated about that. What happened at your end?&rdquo;'),
    ('r4Title', 'Feedback about the feedback',
     'Often you have done all of that and it went nowhere: a shrug, a counter-example, a list of other people who were also late. That deflection is itself a behaviour, and it takes the same three parts.',
     '&ldquo;When I raised the delay, you named three colleagues, and we never got to your part. I&rsquo;m not yet confident this won&rsquo;t happen again. What will you do differently?&rdquo;'),
    ('r5Title', 'Counsel, not rescue',
     'Only now does the manager belong in it. Bring a pattern rather than an anecdote, show what you have already tried, and ask for advice rather than intervention. You keep ownership; they acquire a problem they can no longer claim not to know about.',
     'If they still do nothing, the formula points somewhere new: the manager&rsquo;s behaviour, the manager&rsquo;s impact, the manager&rsquo;s question to answer. Past that, the decision is about what the imbalance costs you, and for how long.'),
]

RUNGS = [
    ('rung1Title', 'You do not skip a rung', [
        ('Rung 1 &middot; Direct feedback',
         'To the colleague, once, calmly. Behaviour, impact, question &mdash; and then you stop talking.',
         'Most attempts fail here, because the question at the end is really an accusation.'),
        ('Rung 2 &middot; Feedback about the feedback',
         'If rung 1 was deflected, the deflection becomes the behaviour you describe. Same three parts, new subject.',
         'Some people start delivering the moment every miss is followed by a calm, specific conversation.'),
    ]),
    ('rung2Title', 'And if the rung above gives way', [
        ('Rung 3 &middot; Bring in your leader',
         'A pattern with dates, what you already tried, and a request for counsel rather than rescue.',
         '&ldquo;How would you approach it from here?&rdquo; keeps the problem yours.'),
        ('Rung 4 &middot; Feedback to your leader',
         'If nothing changes, the manager&rsquo;s inaction is now the behaviour. Name it, state its cost, ask what they will do.',
         'Past rung 4 there is no fifth conversation &mdash; only a decision about what this costs you.'),
    ]),
]

ANATOMY_REF = [
    ('The three that belong',
     'Behaviour is what a camera recorded. Impact is what it cost you, in the first person. A request says what you want to happen next, and by when.',
     'All three can be checked against the world. None of them is a claim about the other person.'),
    ('The one that does not',
     'Interpretation assigns a motive: &ldquo;clearly doesn&rsquo;t care&rdquo;, &ldquo;isn&rsquo;t taking this seriously&rdquo;.',
     'Hedging it does not rescue it. &ldquo;It feels as though you don&rsquo;t care&rdquo; is the same verdict in a softer coat.'),
]

GRAMMAR_REF = [
    ('Clefts put the point first',
     '<em>What frustrates me is&hellip;</em> and <em>It&rsquo;s the timing that&hellip;</em> both move the important half of the sentence to the front and leave the person out of it.',
     'You are foregrounding a problem, not a culprit.'),
    ('Nominalisation and the passive create distance',
     '<em>There has been a pattern of late handovers</em> makes the behaviour the subject. <em>The plan was delivered late</em> removes the actor entirely.',
     'Use both to describe a fact. Neither is a way of avoiding one.'),
]

PHRASES = [
    ('ph1Title', 'Carrying, and being seen to carry', [
        ('take up the slack &middot; cover the gap',
         'Do the work someone else left undone, usually quietly and usually at your own cost.',
         '<em>For two months I took up the slack while he caught up.</em>'),
        ('pull your weight &middot; step up',
         '<em>Pull your weight</em> is doing your fair share. <em>Step up</em> is starting to take proper responsibility.',
         'Both are almost always used in the negative, or as a demand.'),
    ]),
    ('ph2Title', 'Deflecting, escalating, owning', [
        ('deflect &middot; turn a blind eye',
         'To <em>deflect</em> is to turn an accusation away from yourself. To <em>turn a blind eye</em> is to ignore something deliberately.',
         'The second is what a manager does when rung 3 fails.'),
        ('escalate &middot; retain ownership',
         '<em>Escalate</em> moves an issue up a level. <em>Retain ownership</em> means it is still your problem while it travels.',
         'Asking for counsel rather than rescue is how you do both at once.'),
    ]),
]

# ── section 1: comprehension ───────────────────────────────────────────
CHECK = [
    dict(stem='Why, according to the text, does the person absorbing the extra work usually stay quiet?',
         options=['They assume that their line manager has already noticed the imbalance.',
                  'They are afraid that raising it would make them look petty.',
                  'They have been told that workload is not something they may discuss.',
                  'They believe the imbalance will eventually correct itself in time.'],
         correct=1,
         why='They say nothing &ldquo;partly out of politeness and partly out of a suspicion that complaining would look petty&rdquo;. Nothing in the text supports the other three.'),
    dict(stem='What does the writer mean by saying that unspoken resentment &ldquo;hardens&rdquo;?',
         options=['It eventually comes out as an accusation rather than as a request.',
                  'It turns into a formal complaint against the colleague involved.',
                  'It spreads outward and infects the rest of the immediate team.',
                  'It causes the person&rsquo;s own work to deteriorate over time.'],
         correct=0,
         why='&ldquo;It hardens, and arrives later as an accusation rather than a request.&rdquo; Hardening is about the <em>form</em> the complaint finally takes, not about who else hears it.'),
    dict(stem='The writer calls assuming struggle rather than malice &ldquo;tactical&rdquo;. Why tactical rather than simply kind?',
         options=['Because the majority of colleagues genuinely are overloaded at work.',
                  'Because it protects you if the conversation is repeated to others later.',
                  'Because it changes the kind of response that you get back.',
                  'Because managers expect peers to be generous with one another.'],
         correct=2,
         why='&ldquo;A conversation that opens from curiosity gets you an explanation. One that opens from a verdict gets you a defence.&rdquo; The mindset is chosen for its effect, not for its virtue.'),
    dict(stem='What does it mean to state the behaviour &ldquo;as a camera would have recorded it&rdquo;?',
         options=['Keep written evidence of every single exchange that you have.',
                  'Repeat the colleague&rsquo;s own words back to them, verbatim.',
                  'Describe the situation from the whole team&rsquo;s point of view.',
                  'Describe only what was observable, adding no interpretation.'],
         correct=3,
         why='A camera records what was agreed, what arrived and when. It cannot record a motive &mdash; so motives stay out of the sentence.'),
    dict(stem='Why is the impact on you &ldquo;the one thing your colleague cannot dispute&rdquo;?',
         options=['Because it has been recorded in the project plan already.',
                  'Because your manager has confirmed it independently of you.',
                  'Because it concerns the deadline rather than the person.',
                  'Because it is your own experience, not a claim about them.'],
         correct=3,
         why='They can argue about whose fault the delay was. They cannot tell you that you did not work on Saturday, or that you were not frustrated.'),
    dict(stem='Which part of the feedback formula does the writer treat as the most fragile?',
         options=['That the question at the end is a genuinely open one.',
                  'That the impact is named in the first person, concretely.',
                  'That the tone of the conversation stays calm throughout.',
                  'That the conversation happens soon after the event itself.'],
         correct=0,
         why='&ldquo;Everything hangs on that final question actually being a question&rdquo; &mdash; that is, not an accusation with a question mark on the end.'),
    dict(stem='When the feedback is met with a list of other people who were also late, the writer&rsquo;s advice is to:',
         options=['accept that the delay was genuinely shared, and then move on.',
                  'put the concern in writing so that there is a record of it.',
                  'treat the deflection itself as a behaviour and feed it back.',
                  'take the issue to your own manager on the very same day.'],
         correct=2,
         why='&ldquo;That deflection is itself a behaviour, and it takes the same three parts.&rdquo; The formula is applied a second time, to the response rather than to the delay.'),
    dict(stem='Why ask a manager for advice rather than for intervention?',
         options=['Because managers rarely act when they are asked to directly.',
                  'Because it keeps ownership with you while still making them aware.',
                  'Because it avoids having to name the colleague who is involved.',
                  'Because advice is much easier to put in writing afterwards.'],
         correct=1,
         why='&ldquo;You keep ownership; they acquire a problem they can no longer claim not to know about.&rdquo; Rescue hands the problem over; counsel does not.'),
]

# ── section 2: anatomy. One closed set of four, shown on every item.
# Labels balanced to 33-36 characters so the key never leaks by length.
ANAT_OPTS = ['Behaviour &mdash; what a camera recorded',
             'Impact &mdash; what it actually cost me',
             'Interpretation &mdash; a motive I assigned',
             'Request &mdash; what I want to happen next']

ANATOMY = [
    ('&ldquo;The plan was due on Tuesday and reached me at four o&rsquo;clock on Friday.&rdquo;', 0,
     'Agreed date, actual date, nothing else. Pure observable behaviour &mdash; and nothing in it can be argued with.'),
    ('&ldquo;I ended up working through Saturday to hold my own deadline.&rdquo;', 1,
     'The cost to you: concrete, first person, and not disputable. This is the sentence that carries the whole conversation.'),
    ('&ldquo;It feels as though this project simply isn&rsquo;t a priority for you.&rdquo;', 2,
     '&ldquo;It feels as though&rdquo; softens the wording, but the content is still a verdict on their motives. Hedging an interpretation does not convert it into an observation.'),
    ('&ldquo;What could we change so that the handover lands on time next month?&rdquo;', 3,
     'Forward-looking and open. It asks for a change instead of describing the past.'),
    ('&ldquo;You clearly have no respect for other people&rsquo;s schedules.&rdquo;', 2,
     '&ldquo;Clearly&rdquo; is the giveaway. Nothing was observed here; a motive was assigned and then presented as obvious.'),
    ('&ldquo;I&rsquo;ve had to rebuild the delivery schedule twice this quarter.&rdquo;', 1,
     'Again the consequence landing on the speaker. Note the first person and the countable detail &mdash; <em>twice</em>, <em>this quarter</em>.'),
    ('&ldquo;In four of the last six handovers, the file arrived after the agreed date.&rdquo;', 0,
     'A pattern, but still recorded behaviour: dates and counts, no motive. This is the sentence a manager can act on.'),
    ('&ldquo;Can you tell me by Thursday which parts you&rsquo;ll need help with?&rdquo;', 3,
     'A specific, dated ask. Requests carry a deadline; complaints do not.'),
]

# ── section 3: escalation ──────────────────────────────────────────────
ESCALATE = [
    dict(ctx='A colleague&rsquo;s deliverable has arrived three days late for the first time. You are opening the conversation.',
         stem='Which opening does the writer&rsquo;s model support?',
         options=['&ldquo;Everyone on the team has noticed that the plan came in late again this month.&rdquo;',
                  '&ldquo;We&rsquo;d agreed Tuesday and it reached me Friday. I had to move two other pieces of work. What happened?&rdquo;',
                  '&ldquo;I really don&rsquo;t want to make a thing of this at all, but the plan was a little bit late.&rdquo;',
                  '&ldquo;Is everything all right at the moment? You have seemed to be struggling with all of this for quite a while now.&rdquo;'],
         correct=1,
         why='Behaviour, impact, question &mdash; in that order, with no interpretation. The others hide behind the team, minimise the point until it disappears, or diagnose the person.'),
    dict(ctx='You have given that feedback. Your colleague immediately names two other people who held them up.',
         stem='What is the most useful next move?',
         options=['&ldquo;So what you&rsquo;re saying is that it wasn&rsquo;t really your fault at all, then.&rdquo;',
                  'Say nothing further about it for the moment, and instead raise the whole thing with your own manager quietly on the same afternoon.',
                  '&ldquo;You&rsquo;ve named two people who were involved, and we still haven&rsquo;t got to your part. What will you do differently?&rdquo;',
                  '&ldquo;That is exactly the sort of excuse that I was expecting to hear from you today.&rdquo;'],
         correct=2,
         why='This is rung 2: the deflection is named as behaviour, then the conversation is handed back with a question. Going to the manager the same afternoon skips a rung.'),
    dict(ctx='You want the conversation to produce an explanation rather than a defence.',
         stem='Which closing question does that?',
         options=['&ldquo;Why is it that you always leave absolutely everything until the very last minute?&rdquo;',
                  '&ldquo;Am I right in thinking that you simply didn&rsquo;t get round to doing it at all?&rdquo;',
                  '&ldquo;Do you honestly think that what happened here was in any way acceptable?&rdquo;',
                  '&ldquo;What happened at your end?&rdquo;'],
         correct=3,
         why='The other three are accusations wearing question marks. Only one of them can be answered without first defending yourself &mdash; and being short is exactly what makes it open.'),
    dict(ctx='Two rounds of direct feedback have changed nothing. You are taking it to your manager for the first time.',
         stem='Which framing keeps ownership with you?',
         options=['&ldquo;I&rsquo;ve raised it twice directly and I&rsquo;m stuck. How would you approach it from here?&rdquo;',
                  '&ldquo;I need you to speak to her about this, because I have completely run out of patience.&rdquo;',
                  '&ldquo;I thought that you ought to know she has been letting the whole team down lately.&rdquo;',
                  '&ldquo;Everyone else in the team feels exactly the same way about this as I do.&rdquo;'],
         correct=0,
         why='Counsel, not rescue. The other three hand the problem over, editorialise about the person, or recruit an anonymous crowd to make the case.'),
    dict(ctx='You are deciding what to bring into that first conversation with your manager.',
         stem='Which material makes the case strongest?',
         options=['A description of how demoralised the rest of the team has slowly become.',
                  'One vivid, detailed account of the single worst instance so far.',
                  'A pattern across several projects, with dates and the feedback already given.',
                  'An explanation of the reasons that you personally think your colleague behaves this way.'],
         correct=2,
         why='Bring a pattern rather than an anecdote, and show that you have already tried. Dates travel between conversations; adjectives do not.'),
    dict(ctx='A month has passed. Nothing has changed and your manager has not mentioned it since.',
         stem='What does the model suggest you do?',
         options=['Go over the manager&rsquo;s head and take the matter to their own director.',
                  'Stop covering the gap and let a deadline fail so the problem becomes visible.',
                  'Wait until the end of the quarter and then raise the whole thing again.',
                  'Give the manager the same feedback: behaviour, impact, and a question.'],
         correct=3,
         why='The formula does not change when the audience does. Inaction is a behaviour, and it can be described exactly like a late file.'),
    dict(ctx='You are writing that line to your manager now.',
         stem='Which version is feedback rather than accusation?',
         options=['&ldquo;I raised this a month ago and haven&rsquo;t seen a change. I don&rsquo;t think I can solve it alone &mdash; how can you help us?&rdquo;',
                  '&ldquo;You have basically ignored this for a month, which I think says a fair amount.&rdquo;',
                  '&ldquo;Perhaps you could mention it to her at some point over the next few weeks, if you do happen to get the chance at all.&rdquo;',
                  '&ldquo;I assume that you have decided that this isn&rsquo;t really worth dealing with.&rdquo;'],
         correct=0,
         why='Behaviour, impact, question. Two of the others read a motive into the silence; the third is so vague that it asks for nothing at all.'),
    dict(ctx='You have now given feedback at every level, and nothing has moved.',
         stem='How does the writer frame what is left?',
         options=['The team should raise the issue collectively at the next department meeting.',
                  'The remaining question is what the imbalance costs you, and for how long.',
                  'The relationship is beyond repair and should now be formalised through HR.',
                  'The feedback has failed, so the behaviour must be documented in writing.'],
         correct=1,
         why='&ldquo;The decision is about what the imbalance costs you, and for how long.&rdquo; The last step is a decision about yourself, not another conversation.'),
]

# ── section 4: vocabulary ──────────────────────────────────────────────
WORDS = [
    dict(stem='For two months I quietly ______ the slack while he caught up on everything else.',
         options=['gave up', 'took up', 'held up', 'made up'], correct=1,
         why='<strong>Take up the slack</strong> = do the work someone else has left undone. The other three are real phrasal verbs, but none of them collocates with <em>the slack</em>.'),
    dict(stem='He ______ every piece of feedback by pointing at somebody else&rsquo;s delays.',
         options=['deferred', 'deducted', 'deflected', 'reflected'], correct=2,
         why='To <strong>deflect</strong> is to turn an accusation away from yourself. <em>Defer</em> is to postpone; <em>reflect</em> is to think, or to throw light back.'),
    dict(stem='I wanted to keep you ______ the loop before this turns into a bigger problem.',
         options=['in', 'on', 'at', 'through'], correct=0,
         why='Fixed expression: <strong>keep someone in the loop</strong>. <em>On the line</em> and <em>at the helm</em> exist, but mean something else entirely.'),
    dict(stem='Managers who ______ a blind eye to poor performance end up owning it themselves.',
         options=['close', 'pass', 'keep', 'turn'], correct=3,
         why='The idiom is <strong>turn a blind eye (to something)</strong> &mdash; to ignore deliberately. It never takes <em>close</em> or <em>keep</em>.'),
    dict(stem='She hasn&rsquo;t delivered on a single ______ she made in that meeting.',
         options=['committee', 'commission', 'commitment', 'commencement'], correct=2,
         why='A <strong>commitment</strong> is something you have promised to do. Note the collocation as well: you <em>deliver on</em> a commitment.'),
    dict(stem='Only once you have ______ the direct options is it fair to escalate.',
         options=['expired', 'expelled', 'expanded', 'exhausted'], correct=3,
         why='<strong>Exhaust your options</strong> = use every one of them before moving on. The others share the prefix but nothing else.'),
    dict(stem='An uneven workload slowly ______ the trust inside a team.',
         options=['corrodes', 'collides', 'consoles', 'collapses'], correct=0,
         why='<strong>Corrode</strong> is the writer&rsquo;s metaphor: damage from the inside, gradually. <em>Collapse</em> is sudden, and does not take an object here.'),
    dict(stem='I would far rather he ______ up than have me rewrite his section every month.',
         options=['stepped', 'stood', 'put', 'brought'], correct=0,
         why='<strong>Step up</strong> = start taking proper responsibility. <em>Stand up</em> and <em>put up</em> would both need objects, and mean other things.'),
    dict(stem='If nothing changes at your level, you can ______ the issue to your line manager.',
         options=['accelerate', 'alleviate', 'allocate', 'escalate'], correct=3,
         why='To <strong>escalate</strong> is to move an issue up a level of authority. <em>Alleviate</em> is to ease something; <em>allocate</em> is to assign it.'),
    dict(stem='Asking for advice rather than rescue lets you ______ ownership of the problem.',
         options=['detain', 'retain', 'refrain', 'contain'], correct=1,
         why='<strong>Retain ownership</strong> = keep it. <em>Detain</em> holds a person; <em>refrain</em> means hold back from doing something.'),
]

# ── section 5: grammar ─────────────────────────────────────────────────
FORM = [
    dict(stem='______ frustrates me is having to rebuild the schedule twice in one quarter.',
         options=['That', 'Which', 'It', 'What'], correct=3,
         why='A <strong>what-cleft</strong>: <em>What</em> + verb + <em>is</em> + the real point. <em>That</em> and <em>which</em> need an antecedent, and <em>It frustrates me is</em> has no grammatical shape at all.'),
    dict(stem='______ the timing of the handover that causes the problem, not the quality of the work.',
         options=['It&rsquo;s', 'There&rsquo;s', 'That&rsquo;s', 'What&rsquo;s'], correct=0,
         why='An <strong>it-cleft</strong>: <em>It is X that&hellip;</em> Used here to move the point off the person and onto one variable.'),
    dict(stem='&ldquo;You ______ me on Monday that the plan was going to slip.&rdquo;',
         options=['can have told', 'could have told', 'could tell', 'could have been telling'], correct=1,
         why='<strong>could have + past participle</strong> criticises a missed opportunity. <em>Could tell</em> describes ability; <em>can have told</em> is not used in affirmative sentences.'),
    dict(stem='Which sentence describes a pattern without putting the person on trial?',
         options=['Late handovers are apparently something of a speciality of yours.',
                  'You have made a habit of missing more or less every single deadline.',
                  'There has been a pattern of late handovers this quarter.',
                  'You are constantly handing your work over to me later than agreed.'], correct=2,
         why='<strong>Nominalisation</strong> makes the behaviour the subject instead of the person. The others all begin from <em>you</em>, and two of them are sarcastic as well.'),
    dict(stem='&ldquo;If the draft ______ on Tuesday, I ______ at the weekend.&rdquo;',
         options=['arrived / wouldn&rsquo;t work',
                  'had arrived / wouldn&rsquo;t have worked',
                  'would arrive / hadn&rsquo;t worked',
                  'has arrived / wouldn&rsquo;t have worked'], correct=1,
         why='A <strong>third conditional</strong> &mdash; an unreal past. <em>had</em> + past participle in the if-clause, <em>would have</em> + past participle in the result.'),
    dict(stem='You are fairly sure it will happen again, but you want to leave the door open. Which line does that?',
         options=['You will obviously just go and do exactly the same thing again next month.',
                  'I&rsquo;m not yet confident that this won&rsquo;t happen again.',
                  'This is definitely going to happen for a fourth time, exactly as before.',
                  'I know for an absolute fact that nothing at all is going to change here.'], correct=1,
         why='<em>Not yet confident</em> hedges twice &mdash; a negative plus <em>yet</em> &mdash; so the point survives without a verdict attached to it.'),
    dict(stem='&ldquo;The plan ______ three working days after the agreed date.&rdquo;',
         options=['was delivering', 'delivered', 'was delivered', 'has delivering'], correct=2,
         why='The <strong>passive</strong> removes the actor from the sentence, which is what you want when you are describing a fact rather than blaming a person.'),
    dict(stem='You told your manager: &ldquo;I gave her feedback twice.&rdquo; Writing it up afterwards: &ldquo;I explained that I ______ her feedback twice.&rdquo;',
         options=['had given', 'have given', 'was giving', 'would give'], correct=0,
         why='<strong>Backshift</strong> in reported speech: past simple in the original becomes past perfect after a past reporting verb.'),
    dict(stem='______ has the plan arrived on the date we agreed.',
         options=['No sooner', 'Never before that', 'Not once', 'Hardly ever it'], correct=2,
         why='<strong>Negative inversion</strong> for emphasis: <em>Not once</em> + auxiliary + subject. <em>No sooner</em> needs a <em>than</em>-clause; the other two are not grammatical.'),
    dict(stem='Which closing question is genuinely open rather than an instruction in disguise?',
         options=['Can you just make absolutely sure that it does not happen again next time?',
                  'You will get it over to me on time next month, though, won&rsquo;t you?',
                  'Don&rsquo;t you think that it is about time the two of us sorted this out?',
                  'What would need to change for the next handover to land on time?'], correct=3,
         why='The first three are a command, a tag question demanding agreement, and a rhetorical question. Only the last one can be answered with new information.'),
]

# Five, not six: a sixth chip pushed the row past the 1150px content width and
# the last two clipped at the canvas edge. The row does not wrap.
CHIPS = ['take up the slack', 'turn a blind eye', 'escalate', 'retain ownership',
         'not yet confident that&hellip;']


def build():
    for label, group in (('CHECK', CHECK), ('ESCALATE', ESCALATE),
                         ('WORDS', WORDS), ('FORM', FORM)):
        D.assert_no_key_is_longest(group, label)
    D.assert_no_key_is_longest(
        [dict(options=ANAT_OPTS, correct=c) for _, c, _ in ANATOMY], 'ANATOMY')

    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Carrying the <em>Load</em>',
                'What to say to the colleague who does not pull their weight &mdash; and what to say next when saying it once does not work',
                [('Level', 'C1 &middot; Business English'),
                 ('Focus', 'Feedback &amp; escalation'),
                 ('Count', 'COUNT slides')])

        + "".join(D.teach('readEyebrow', 'Reading', key, title,
                          [(None, 'The claim', a, None, None),
                           (None, 'What follows from it', b, None, None)],
                          folder=F, bg='bg02.jpg' if n % 2 else None)
                  for n, (key, title, a, b) in enumerate(READING))

        + "".join(D.teach('rungEyebrow', 'The four rungs', key, title,
                          [(None, h, b, None, note) for h, b, note in cards],
                          folder=F, bg='bg03.jpg')
                  for key, title, cards in RUNGS)

        + "".join(D.mc(i + 1, len(CHECK), q, 'ckEyebrow', 'Comprehension',
                       'ckTitle', 'Did you read it closely?', folder=F,
                       bg='bg02.jpg' if i % 4 == 1 else None)
                  for i, q in enumerate(CHECK))

        + D.teach('anRefEyebrow', 'Before you sort', 'anRefTitle',
                  'Four jobs a sentence can do',
                  [(None, h, b, None, note) for h, b, note in ANATOMY_REF],
                  folder=F, bg='bg04.jpg')

        + "".join(D.mc(i + 1, len(ANATOMY),
                       dict(stem=stem, options=ANAT_OPTS, correct=c, why=why),
                       'anEyebrow', 'Anatomy',
                       'anTitle', 'What is this line actually doing?', folder=F,
                       bg='bg04.jpg' if i % 4 == 2 else None)
                  for i, (stem, c, why) in enumerate(ANATOMY))

        + "".join(D.mc(i + 1, len(ESCALATE), q, 'esEyebrow', 'Escalate',
                       'esTitle', 'Choose the move', folder=F,
                       bg='bg03.jpg' if i % 4 == 0 else None, ctx=q['ctx'])
                  for i, q in enumerate(ESCALATE))

        + "".join(D.teach('phEyebrow', 'The language of the imbalance', key, title,
                          [(None, h, b, None, note) for h, b, note in cards],
                          folder=F, bg='bg02.jpg')
                  for key, title, cards in PHRASES)

        + "".join(D.mc(i + 1, len(WORDS), q, 'woEyebrow', 'Words',
                       'woTitle', 'One word fits the collocation', folder=F,
                       bg='bg04.jpg' if i % 5 == 3 else None)
                  for i, q in enumerate(WORDS))

        + D.teach('grEyebrow', 'Before the grammar', 'grTitle',
                  'Two ways to take yourself out of the sentence',
                  [(None, h, b, None, note) for h, b, note in GRAMMAR_REF],
                  folder=F, bg='bg03.jpg')

        + "".join(D.mc(i + 1, len(FORM), q, 'foEyebrow', 'Form',
                       'foTitle', 'Grammar under pressure', folder=F,
                       bg='bg02.jpg' if i % 5 == 2 else None)
                  for i, q in enumerate(FORM))

        + D.results('resNext', 'You can spot the sentence. Now say it out loud &rarr;',
                    folder=F, bg='bg04.jpg')

        + D.activate('Have the conversation', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you is the colleague, one is you. Swap after the second prompt &mdash; the deflection is harder to do well than it looks.',
                     ['Deliver round one: behaviour a camera saw, impact on you, one question. Nothing else.',
                      'Deflect. Name two other people and a system problem, and sound entirely reasonable doing it.',
                      'Feed back the deflection, in under forty seconds, without raising your voice or your eyebrows.',
                      'Brief the manager in three sentences: the pattern with numbers, what you tried, the question you want answered.',
                      'A month on, nothing has changed. Give the manager feedback without once assigning them a motive.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the message you would send your manager after two rounds of direct feedback have failed. Pattern with dates, impact in the first person, what you already tried, one open question &mdash; and no interpretation of anyone&rsquo;s motives.',
                     'Hi … — I wanted to flag something before the next cycle rather than after it.',
                     folder=F, bg='bg03.jpg')
    )

    import i18n_carrying as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Carrying the Load — C1', I, langs=('en', 'de'))
    n = s.count('<section class="slide')
    # The chip has to say the number the checker reports, and the checker
    # counts one fewer than the raw section count (the cover is not a stop).
    s = s.replace('COUNT slides', '%d slides' % (n - 1))
    s = s.replace("chipCount: \"58 slides\"", 'chipCount: "%d slides"' % (n - 1))
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d sections, %d scored (%d check, %d anatomy, %d escalate, '
          '%d words, %d form), %d bytes'
          % (OUT, n, len(CHECK) + len(ANATOMY) + len(ESCALATE) + len(WORDS) + len(FORM),
             len(CHECK), len(ANATOMY), len(ESCALATE), len(WORDS), len(FORM), len(s)))


if __name__ == '__main__':
    build()
