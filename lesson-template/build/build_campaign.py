# -*- coding: utf-8 -*-
"""The Monthly Review (B2) — reporting a campaign in English. New build.

Asked for on 2026-09-16 for a named student: team lead and project manager at
a digital marketing agency — Google and Meta advertising, website projects,
branding, analytics, and client and partner communication. He wants meetings,
presentations, business trips, conferences and everyday professional English,
and above all to feel confident speaking *spontaneously*: explaining ideas and
strategies, discussing projects, using the vocabulary of his own trade.

That is four lessons, not one, so this is the first and the one only he needs.
The site already carries the neighbouring ground — forbes-english-meetings
(open answer practice), the design pitch, talking with clients, emails and
follow-ups, escalating a complaint, C1 negotiation — and none of them touches
campaign performance. Nothing here duplicates those.

The situation is the one that recurs in his week: the monthly review call with
a client. It carries all four of his stated needs at once. He has to present
numbers (analytics), explain what happened and why (spontaneous explanation),
propose what to do next (strategy), and answer a question he did not prepare
for (the confidence problem, stated directly).

Six teaching points, each chosen because an agency professional gets it wrong
in a way that costs credibility rather than marks:

  1. the four patterns of change — rise BY an amount, rise TO a level, FROM x
     TO y, up ON a comparison period. *Increased on 12%* and *increased with
     12%* are the two commonest errors in this register and they land in the
     first sentence of every report he gives.
  2. cause versus coincidence. *Driven by* and *down to* assert a mechanism;
     *coincided with* and *in line with* assert timing only. Claiming the
     first when you only have the second is the fastest way to lose a
     client's trust, and it is invisible to the speaker.
  3. the metric pairs that get collapsed in English even by people who hold
     them apart in their own language: reach/impressions, CTR/conversion
     rate, CPC/CPA/ROAS, spend/budget.
  4. saying it went badly, professionally: *came in under target*, *that one
     is on us*, *that sat with the platform* — owning a miss in a sentence
     the client can forward.
  5. proposing rather than deciding. *I'd suggest we* leaves the decision
     with the client; *we should* and *we're going to* take it away. He is a
     team lead, so he does both, and the difference is not obvious in English.
  6. buying two seconds when asked something unprepared. This is the answer
     to "I want to feel more confident speaking spontaneously": *off the top
     of my head*, *let me come back to you on that*, *that's a fair question*.
     Fluency here is a holding phrase, not a faster brain.

Shape: cover -> 6 teach -> 1 sort -> 2 gap -> 1 match -> 2 order -> 8 mc ->
results -> activate. 22 slides. The engine scores a sort per item and a gap
per input, so the fourteen question slides are worth more than fourteen
points.

Level. B2, and deliberately not C1: the neighbouring business decks on this
site are already C1/C2, and this student needs the everyday register to be
automatic before the elaborate one is worth teaching.

Languages: English, German, Spanish and **Croatian**, which the student
actually speaks and which the site had never carried. See i18n_campaign.py's
docstring for the three shared files that had to learn the language.

Three notes before changing anything here.

* The palette is the verbatim output of

      python3 lesson-template/extract-palette.py CampaignReview/hero.jpg --light

  Light theme, because the art family is pale blue and cream — HOUSE-STYLE
  §4a: forcing bright artwork into the dark theme is what produces muddy
  interiors. Every row of the contrast report reads PASS.

* The artwork is PLACEHOLDER, chosen from incoming/ on Innes's instruction
  ("choose any images from incoming for now, we can replace them later").
  It is one coherent flat-vector family in a single palette, one picture per
  section per HOUSE-STYLE §5c, and each was picked for what it depicts: a
  ruler for measurement, interlocking cogs for cause, numbered mailboxes for
  reach, a departure board mid-flip for the moment before you have the words.
  Swapping any of them is a one-line change to the bg name plus a re-run;
  swapping the hero also means re-running extract-palette.

  Four of them were swapped for a different Midjourney variant of the SAME
  subject after measuring, not after looking. On a light deck the text is dark
  ink, so a background failure is a dark MASS under a text run rather than a
  bright one — the opposite of the dark-theme case HOUSE-STYLE §5 describes,
  and a blanket wash bump is the wrong lever because a void-based wash on a
  light deck lightens the whole picture toward the flat, washed-out look §4a
  warns about (0.45 alpha was needed, which is far past that). The fix is
  per-image. Measured against the real ink rectangles pulled off the rendered
  page, the first cut had thirteen text runs under 3.5:1, eight of them on the
  original cogs variant whose black gear sat directly under the eyebrow, title
  and stem. cogs, cards and stencil moved to the variant of the same picture
  whose subject sits LOW, and the activation's departure-board platform became
  the sharpened pencil, which was the only good closer that keeps its top two
  thirds open. Nothing is now under 3.5:1.

  Two remain worth knowing about if the art is replaced. bulb.jpg clears at
  3.52:1 on the context line and desk.jpg at 3.48:1 on the hint — the first is
  a hair over the floor and the second a hair under it, both inside the margin
  the text-shadow halo covers, and neither has a better variant in the batch.
  Replace either one and re-measure rather than assuming.

* Every MC stem here carries a stem_key and translates, which is the opposite
  of the grammar decks. The stems are all "which sentence …?" prompts with no
  blank in them, so nothing under test is translated — the options stay
  English in all three languages. Same for the ctx lines: the *situation* is
  scaffolding he has to read before the item is answerable at all.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-campaign-review-b2.html'

F = 'CampaignReview'
HERO = 'hero.jpg'

# Mechanically derived — the verbatim output of
#     python3 lesson-template/extract-palette.py CampaignReview/hero.jpg --light
# Contrast report: PASS on all eight rows, the tightest being border on
# surface at 3.33:1 against a 1.25 floor. Never hand-pick a value in here.
PALETTE = '''  --hero: url('%s/%s');

  --void          : #d8beac;
  --surface       : #e1d0c4;
  --surface2      : #dcc6b8;
  --border        : #96634a;
  --text          : #2a1911;
  --text-dim      : #5e3e2e;
  --accent        : #953e12;
  --accent-bright : #6e2907;
  --accent-dim    : #d87a4b;
  --secondary     : #577170;
  --contrast      : #0f4d44;''' % (F, HERO)


# ── teaching slides ────────────────────────────────────────────────────
# (eyebrow_key, eyebrow, title_key, title, cards, background)
# Cards are deck.teach's SIX-item form — (head_key, head, body_key, body,
# note_key, note) — because this deck ships three languages and the five-item
# form would leave the rule text in English under a translated heading
# (CLAUDE.md, standing constraints). head_key is None throughout: the heading
# is the English pattern itself and must not travel.
TEACH = [
    ('t1Eyebrow', 'The first sentence of every report',
     't1Title', 'Four patterns for a number that moved',
     [(None, 'rise / fall <strong>by</strong>',
       't1b1', 'The <em>size</em> of the move: <em>CPA fell by 14%</em>.',
       't1n1', 'Never <em>fell with 14%</em>, never <em>fell on 14%</em>.'),
      (None, 'rise / fall <strong>to</strong>',
       't1b2', 'The <em>level</em> it ended at: <em>CTR rose to 3.1%</em>.',
       't1n2', 'One says how far it moved, the other where it stopped.'),
      (None, '<strong>from</strong> &hellip; <strong>to</strong> &hellip;',
       't1b3', 'Both ends: <em>from &euro;38 to &euro;32 in three weeks</em>.',
       't1n3', 'Use it when the starting point is the point.'),
      (None, 'up / down <strong>on</strong>',
       't1b4', 'The comparison: <em>spend is up 11% on last month</em>.',
       't1n4', 'Also <em>month on month</em>, <em>year on year</em>, <em>versus Q2</em>.')],
     'ruler.jpg'),

    ('t2Eyebrow', 'The claim you can defend',
     't2Title', 'Cause, coincidence, or not yet known',
     [(None, 'driven by &middot; down to',
       't2b1', 'You are asserting a mechanism. Say it when you can show one.',
       't2n1', 'The client is entitled to ask <em>how do you know?</em>'),
      (None, 'coincided with &middot; in line with',
       't2b2', 'You are asserting timing, and nothing more than timing.',
       't2n2', 'Honest, and it survives someone explaining it differently.'),
      (None, 'we put it down to',
       't2b3', 'Your reading, marked as yours. A judgement, offered as one.',
       't2n3', 'The <em>we</em> is doing real work here. Keep it.'),
      (None, 'it&rsquo;s too early to say',
       't2b4', 'A complete answer &mdash; if you add when you <em>will</em> know.',
       't2n4', 'Without a date it sounds like avoiding the question.')],
     'cogs.jpg'),

    ('t3Eyebrow', 'Four pairs people collapse in English',
     't3Title', 'The metrics, said precisely',
     [(None, 'reach &middot; impressions',
       't3b1', 'Reach counts <em>people</em>. Impressions count <em>times shown</em>.',
       't3n1', 'Impressions are always the bigger number of the two.'),
      (None, 'CTR &middot; conversion rate',
       't3b2', 'Clicks per impression; then actions per visit. Two stages.',
       't3n2', 'High CTR and low CVR is a landing-page conversation.'),
      (None, 'CPC &middot; CPA &middot; ROAS',
       't3b3', 'Cost of a click, cost of a customer, revenue per unit spent.',
       't3n3', 'Only the last is a ratio: <em>a 4x ROAS</em>, not <em>4%</em>.'),
      (None, 'spend &middot; budget',
       't3b4', 'Budget is allocated, spend is gone. <em>Pacing</em> is the gap.',
       't3n4', '<em>We are pacing ahead</em> means it will run out early.')],
     'mailboxes.jpg'),

    ('t4Eyebrow', 'Bad news, first, in one sentence',
     't4Title', 'Saying it missed without sounding careless',
     [(None, 'name the miss',
       't4b1', '<em>We came in under target on conversions</em> &mdash; the number, plainly.',
       't4n1', 'Careful: under <em>budget</em> is good news, under <em>target</em> is not.'),
      (None, 'say where it sat',
       't4b2', '<em>That one&rsquo;s on us.</em> &middot; <em>That sat with the platform.</em>',
       't4n2', 'Either is fine. Having no answer is not.'),
      (None, 'then the fix',
       't4b3', '<em>We caught it on day seven and it is corrected.</em>',
       't4n3', 'A miss with a date and a fix stops being an argument.')],
     'cards.jpg'),

    ('t5Eyebrow', 'Who decides',
     't5Title', 'Proposing without taking the decision',
     [(None, 'I&rsquo;d suggest we &hellip;',
       't5b1', 'A proposal. It leaves the decision with the person paying.',
       't5n1', 'The safest opener when they have to sign it off.'),
      (None, 'we&rsquo;re going to &hellip;',
       't5b2', 'A decision already taken. You are informing, not asking.',
       't5n2', 'Correct for your own team. Risky with a client.'),
      (None, 'the verbs',
       't5b3', '<em>shift</em> &middot; <em>scale back</em> &middot; <em>pause</em> &middot; <em>hold off on</em> &middot; <em>double down on</em>',
       't5n3', '<em>Shift budget out of X and into Y</em> is the fixed pattern.'),
      (None, 'ask for time',
       't5b4', '<em>I&rsquo;d give it another fortnight before we judge it.</em>',
       't5n4', 'A date turns &ldquo;wait&rdquo; into a plan.')],
     'bulb.jpg'),

    ('t6Eyebrow', 'The question you did not prepare for',
     't6Title', 'Two seconds, bought properly',
     [(None, 'off the top of my head',
       't6b1', 'Gives a figure and flags it as approximate, in four words.',
       't6n1', 'Then <em>but let me confirm that</em>. Always finish it.'),
      (None, 'let me come back to you',
       't6b2', 'Declines to guess and promises the answer. Add <em>by this afternoon</em>.',
       't6n2', 'A promise with no time on it is not a promise.'),
      (None, 'that&rsquo;s a fair question',
       't6b3', 'Buys the two seconds and sounds candid rather than stalling.',
       't6n3', 'Follow it with <em>the honest answer is</em> &mdash; then answer.'),
      (None, 'can I check one thing first?',
       't6b4', 'Turns a guess into a checked answer, conceding nothing.',
       't6n4', 'Better than silence. Silence reads as not knowing.')],
     'board.jpg'),
]


# ── sorting ────────────────────────────────────────────────────────────
# Three bins, three lines each, and every line describes a real movement in
# the numbers. What is being sorted is how much the sentence CLAIMS to know
# about why — teaching point 2, and the one a learner cannot hear themselves
# getting wrong.
SORT = dict(
    bins=['Claims a cause', 'Claims only timing', 'Claims nothing yet'],
    bin_keys=['sortBin1', 'sortBin2', 'sortBin3'],
    title_key='sortTitle', title='How much does the sentence claim to know?',
    hint_key='sortHint',
    hint='Click a line, then the box it belongs in. Every line is about a real movement in the numbers &mdash; what changes is how much it claims about the reason.',
    items=[('The uplift was driven by the new landing page.', 0),
           ('That drop is down to the budget running out on the 24th.', 0),
           ('We put the weekend dip down to the checkout being offline.', 0),
           ('The uplift coincided with the launch of the new landing page.', 1),
           ('The drop came in the same week the budget ran out.', 1),
           ('The weekend dip was in line with the checkout outage.', 1),
           ('It is too early to say what is behind the uplift.', 2),
           ('We have not isolated the cause of the drop yet.', 2),
           ('I would want another fortnight before I called that a trend.', 2)],
    why='The middle column is the one that survives being questioned. <strong>Driven by</strong> and '
        '<strong>down to</strong> assert a mechanism, so the client may reasonably ask to see it; '
        '<strong>coincided with</strong> and <strong>in line with</strong> assert only that two things '
        'happened together, which is usually all you can show. <strong>We put it down to</strong> sits '
        'between them &mdash; a reading, marked as yours.')


# ── gap fill ───────────────────────────────────────────────────────────
# Both banks are alphabetised rather than built from the answers, which is
# what stops a bank being an answer key (HOUSE-STYLE §12, BANK gate). Three of
# the six chips on each slide are decoys, and on the second slide all three
# decoys are real phrases taught two slides earlier — a decoy the lesson has
# never mentioned teaches nothing when it is rejected.
BANK_A = ['at', 'by', 'in', 'of', 'on', 'to']
BANK_B = ['double', 'hold', 'pause', 'roll', 'scale', 'shift']

GAPS = [
    dict(bank=BANK_A, title_key='gapTitleA', title='Complete the movement',
         hint_key='gapHintA', hint='One word per gap. Three of the six are not needed.',
         width=110, bg='desk.jpg',
         rows=[('Cost per acquisition fell ______ fourteen per cent in the second half of the month.',
                ['by'],
                '<strong>By</strong> gives the size of the move. <em>Fell with</em> and <em>fell on</em> are the two errors this pattern attracts.'),
               ('Click-through rate rose ______ 3.1 per cent, its best figure since March.',
                ['to'],
                '<strong>To</strong> gives the level it reached. <em>Rose by 3.1%</em> would mean something different &mdash; and larger.'),
               ('Spend is up eleven per cent ______ last month on the same budget.',
                ['on'],
                '<strong>On</strong> names the period you are comparing with: <em>up on last month</em>, <em>down on Q2</em>.')],
         why=None),

    dict(bank=BANK_B, title_key='gapTitleB', title='Complete the proposal',
         hint_key='gapHintB',
         hint='One verb per gap. Three of the six are not needed &mdash; and all three are real phrases from this lesson.',
         width=140, bg='stencil.jpg',
         rows=[('I&rsquo;d suggest we ______ a fifth of the budget out of display and into search.',
                ['shift'],
                '<strong>Shift &hellip; out of &hellip; and into &hellip;</strong> is the fixed pattern for moving money between channels.'),
               ('We&rsquo;re going to ______ back the Meta spend until the creative is refreshed.',
                ['scale'],
                '<strong>Scale back</strong> is a reduction, not a stop. <em>Pause</em> would mean switching it off entirely.'),
               ('I&rsquo;d ______ off on a decision until we have a full fortnight of data.',
                ['hold'],
                '<strong>Hold off on</strong> asks for time before deciding. It needs a date after it, or it sounds like avoidance.')],
         why=None),
]


# ── matching ───────────────────────────────────────────────────────────
# Definitions are held to a similar length for the same reason MC options
# are: length must not leak the pairing.
MATCH = [
    ('impressions', 'the number of times it was shown, repeats included'),
    ('reach', 'the number of separate people who saw it at least once'),
    ('click-through rate', 'clicks counted as a share of the times it was shown'),
    ('conversion rate', 'the share of visits that ended in the action you wanted'),
    ('cost per acquisition', 'what you paid, on average, for one of those actions'),
    ('return on ad spend', 'revenue earned for every euro the campaign spent'),
]


# ── ordering ───────────────────────────────────────────────────────────
ORDERS = [
    dict(title_key='ordTitleA', title='Headline first',
         hint_key='ordHintA',
         hint='Click the parts in order. The client hears the conclusion before the detail.',
         items=['Before I take you through the numbers,', 'the headline is',
                'that cost per acquisition came down,', 'conversions did not,',
                'and I think I know why.'],
         why='A review that builds to its conclusion makes the client wait for it, and they stop waiting. '
             '<strong>Before I take you through the numbers, the headline is &hellip;</strong> is the move: the '
             'result in one sentence, then the evidence. It also lets you say the bad half yourself.'),

    dict(title_key='ordTitleB', title='A proposal they can say no to',
         hint_key='ordHintB',
         hint='Click the parts in order: the evidence, the proposal, the size of it, then the date.',
         items=['On what we have so far', 'I&rsquo;d suggest we shift',
                'about a fifth of the budget', 'out of display and into search,',
                'and look at it again', 'in two weeks.'],
         why='<strong>I&rsquo;d suggest we</strong> leaves the decision where it belongs, <strong>about a '
             'fifth</strong> is a size they can argue with, and <strong>look at it again in two weeks</strong> '
             'is what makes it a proposal rather than a request to stop worrying about it.'),
]


# ── multiple choice ────────────────────────────────────────────────────
# Every distractor is the length of the key and wrong for a reason this deck
# teaches. Q5, Q6 and Q8 are where that work went: the professional answer
# genuinely is the longer one in this register, so the distractors were padded
# to match rather than the keys trimmed (HOUSE-STYLE §12).
QUESTIONS = [
    dict(stem_key='q1Stem', stem='Which sentence reports the size of the movement correctly?',
         options=['Cost per acquisition decreased with fourteen per cent over the month.',
                  'Cost per acquisition decreased by fourteen per cent over the month.',
                  'Cost per acquisition decreased on fourteen per cent over the month.',
                  'Cost per acquisition decreased of fourteen per cent over the month.'],
         correct=1,
         explains=['<em>Decrease with</em> is the calque most European languages produce here. English does not use it.',
                   None,
                   '<em>On</em> introduces the period you are comparing with, not the size: <em>down on last month</em>.',
                   '<em>Of</em> works after the noun &mdash; <em>a decrease of 14%</em> &mdash; but never after the verb.'],
         why='After the <strong>verb</strong>, the size of a move takes <strong>by</strong>. After the '
             '<strong>noun</strong> it takes <em>of</em>: <em>a decrease of fourteen per cent</em>. Both are '
             'right; they are not interchangeable.',
         bg='ruler.jpg'),

    dict(ctx_key='q2Ctx', ctx='Click-through rate was 2.4% in June. It is 3.1% now.',
         stem_key='q2Stem', stem='Which sentence states that accurately?',
         options=['Click-through rate has risen by 3.1 per cent since the middle of June.',
                  'Click-through rate has risen on 3.1 per cent since the middle of June.',
                  'Click-through rate has risen to 3.1 per cent since the middle of June.',
                  'Click-through rate has risen from 3.1 per cent since the middle of June.'],
         correct=2,
         explains=['<strong>By</strong> is the size of the move, which here is 0.7 points &mdash; not 3.1.',
                   '<strong>On</strong> takes a period, not a level: <em>up on June</em>, never <em>up on 3.1%</em>.',
                   None,
                   '<strong>From</strong> marks where it started, so this says it began at 3.1 and left.'],
         why='<strong>To</strong> names the level it reached. Both prepositions are available and they say '
             'different things: <em>risen by 0.7 points, to 3.1 per cent</em> says the whole thing at once.',
         bg='ruler.jpg'),

    dict(ctx_key='q3Ctx', ctx='The campaign was shown 840,000 times, to 210,000 different people.',
         stem_key='q3Stem', stem='Which sentence reports that correctly?',
         options=['We reached 840,000 people and recorded 210,000 impressions in total.',
                  'We recorded 840,000 impressions and reached 210,000 people in total.',
                  'We reached 840,000 impressions across 210,000 people in total.',
                  'We recorded 840,000 people and reached 210,000 impressions in total.'],
         correct=1,
         explains=['Reversed. Reach counts people, so it cannot be the larger of the two numbers here.',
                   None,
                   'You do not <em>reach</em> an impression. Reach takes people; impressions are recorded.',
                   'Both verbs are attached to the wrong noun, and the two numbers are the wrong way round.'],
         why='<strong>Impressions</strong> count how many times it was shown and <strong>reach</strong> counts '
             'how many people saw it, so impressions are always the bigger number. One divided by the other is '
             '<strong>frequency</strong> &mdash; here, four times each.',
         bg='mailboxes.jpg'),

    dict(ctx_key='q4Ctx',
         ctx='Conversions rose 20% in the week a competitor&rsquo;s site was down. You have no other evidence.',
         stem_key='q4Stem', stem='Which sentence can you defend if the client asks how you know?',
         options=['The rise was driven by our competitor being offline for most of that week.',
                  'The rise coincided with our competitor being offline for most of that week.',
                  'The rise was down to our competitor being offline for most of that week.',
                  'The rise was caused by our competitor being offline for most of that week.'],
         correct=1,
         explains=['<strong>Driven by</strong> asserts a mechanism. You have the timing and nothing else.',
                   None,
                   '<strong>Down to</strong> is the same claim in a more casual register. Still a claim.',
                   '<strong>Caused by</strong> is the strongest of the four and the hardest to withdraw.'],
         why='<strong>Coincided with</strong> claims only that two things happened together, which is exactly '
             'what you can show. To go further, mark it as your reading: <em>we put it down to</em> &mdash; not '
             '<em>it was down to</em>.',
         bg='cogs.jpg'),

    dict(ctx_key='q5Ctx', ctx='The client asks whether the new creative is working. It has been live four days.',
         stem_key='q5Stem', stem='Which answer is both honest and useful?',
         options=['It&rsquo;s working &mdash; the first four days are already up on the old creative.',
                  'It&rsquo;s too early to say &mdash; I&rsquo;d give it another ten days before we judge it.',
                  'I couldn&rsquo;t tell you yet; we will have to wait and see how it develops.',
                  'It&rsquo;s not working, so I&rsquo;d pull it and go back to the previous version.'],
         correct=1,
         explains=['Four days is not a result. If it reverses next week you have to take this back.',
                   None,
                   'Honest, but it hands the decision back with no date on it. <em>Wait and see</em> is not a plan.',
                   'The same four days, read the other way. A conclusion either way is premature here.'],
         why='<strong>It&rsquo;s too early to say</strong> is a complete professional answer <em>only</em> when '
             'you add when you will know. Without the date it is indistinguishable from not wanting to answer.',
         bg='cogs.jpg'),

    dict(ctx_key='q6Ctx', ctx='Your team used the wrong audience for a week. The client will see it in the numbers.',
         stem_key='q6Stem', stem='Which sentence would you say first?',
         options=['That one&rsquo;s on us: the audience was set wrong, and we caught it on day seven.',
                  'There were some issues with the audience setup during the week in question.',
                  'The audience appears to have been set incorrectly at some point during the week.',
                  'Mistakes were made in the audience setup and they have all been corrected now.'],
         correct=0,
         explains=[None,
                   '<em>Some issues</em> names nothing and nobody, and the client already has the numbers.',
                   '<em>Appears to have been</em> distances you from a fact you know for certain.',
                   'The agentless passive with no owner. The client&rsquo;s next question is who.'],
         why='Say it before they find it, name where it sat, and give the date you caught it. <strong>That '
             'one&rsquo;s on us</strong> costs you far less than three sentences a client has to decode &mdash; '
             'and it closes the subject instead of opening it.',
         bg='cards.jpg'),

    dict(ctx_key='q7Ctx', ctx='You want to move budget between channels. The client has to sign it off.',
         stem_key='q7Stem', stem='Which sentence leaves the decision with them?',
         options=['We should shift a fifth of the display budget across to search this week.',
                  'I&rsquo;d suggest we shift a fifth of the display budget across to search.',
                  'We&rsquo;re shifting a fifth of the display budget across to search this week.',
                  'A fifth of the display budget has to be shifted across to search soon.'],
         correct=1,
         explains=['<em>We should</em> is a recommendation that sounds like an instruction, and it assumes the answer.',
                   None,
                   '<em>We&rsquo;re shifting</em> announces a decision already taken. Correct internally, risky here.',
                   'Passive with no agent: nobody is asking, nobody is deciding, and nobody owns it.'],
         why='<strong>I&rsquo;d suggest we</strong> is the register for anything the other person signs off. '
             'Keep <em>we&rsquo;re going to</em> for your own team, where announcing the decision is your job.',
         bg='bulb.jpg'),

    dict(ctx_key='q8Ctx', ctx='Mid-call, the client asks for a figure you do not have in front of you.',
         stem_key='q8Stem', stem='Which reply keeps your credibility?',
         options=['Off the top of my head it&rsquo;s about eight euros, but let me confirm that.',
                  'I think it was somewhere around eight euros, more or less, when I last saw it.',
                  'I don&rsquo;t have that in front of me at the moment, I&rsquo;m afraid &mdash; sorry.',
                  'It&rsquo;s eight euros &mdash; and I&rsquo;ll double-check and correct that if I&rsquo;m wrong.'],
         correct=0,
         explains=[None,
                   'Two hedges and no commitment. It gives a number and takes it back in the same breath.',
                   'Honest, but it closes the door: no figure, no promise, and nothing for them to work with.',
                   'States it as fact and hedges afterwards. If it is wrong, the correction is what they remember.'],
         why='<strong>Off the top of my head</strong> marks the figure as approximate <em>before</em> you say it, '
             'and <strong>let me confirm that</strong> puts a next step on it. Four words of framing is the '
             'difference between sounding unprepared and sounding like someone who knows their own numbers.',
         bg='board.jpg'),
]


# The phrases the activation stage expects to hear. Target language, so they
# stay in English in all three switcher languages.
CHIPS = ['rose by &middot; rose to', 'up 11% on last month', 'coincided with',
         'it&rsquo;s too early to say', 'came in under target',
         'that one&rsquo;s on us', 'I&rsquo;d suggest we&hellip;',
         'off the top of my head']

SPEAK = [
    'Open the review with the headline in two sentences: what moved, which way, by how much. No slides.',
    'Client: &ldquo;So why did conversions drop?&rdquo; You have the timing and no cause. Answer without inventing one.',
    'Client: &ldquo;What was last week&rsquo;s CPA?&rdquo; You do not have it. Answer, promise, keep the call moving.',
    'Propose moving a fifth of the budget. Leave the decision with them, and put a date on the review.',
]


def build():
    D.assert_no_key_is_longest(QUESTIONS, 'Campaign')
    for g in GAPS:
        D.assert_bank_is_not_a_key(g['bank'], [r[1][0] for r in g['rows']])

    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'The Monthly <em>Review</em>',
                'Reporting a campaign in English &mdash; the numbers, the reason, the proposal, and the question you did not prepare for',
                [('Level', 'B2 &middot; Agency &amp; client reporting'),
                 ('Focus', 'Performance language and thinking on your feet'),
                 ('Count', 'NSLIDES slides')])

        + "".join(D.teach(ek, e, tk, t, cards, folder=F, bg=bg)
                  for ek, e, tk, t, cards, bg in TEACH)

        + D.sort_slide(SORT['bins'], SORT['items'],
                       'sortEyebrow', 'Before you say why',
                       SORT['title_key'], SORT['title'],
                       SORT['hint_key'], SORT['hint'], SORT['why'],
                       folder=F, bg='pegboard.jpg', bin_keys=SORT['bin_keys'])

        + "".join(D.gap(i + 1, len(GAPS), g['rows'], g['bank'],
                        'gapEyebrow', 'The grammar of the report',
                        g['title_key'], g['title'],
                        hint=g['hint'], hint_key=g['hint_key'], why=g['why'],
                        width=g['width'], folder=F, bg=g['bg'])
                  for i, g in enumerate(GAPS))

        + D.match(MATCH, 'matEyebrow', 'Precision',
                  'matTitle', 'Match the metric to what it actually counts',
                  'matHint',
                  'Six terms, six definitions. Four of them are routinely used as if they were interchangeable; none of them are.',
                  'Impressions count showings and reach counts people, so <strong>impressions &divide; reach</strong> '
                  'is frequency. CTR and conversion rate measure two different stages, which is why a campaign can '
                  'be excellent at one and hopeless at the other.',
                  folder=F, bg='jigsaw.jpg')

        + "".join(D.order(o['items'], 'ordEyebrow', 'Build the sentence',
                          o['title_key'], o['title'],
                          o['hint_key'], o['hint'], o['why'],
                          folder=F, bg='windows.jpg')
                  for o in ORDERS)

        + "".join(D.mc(i + 1, len(QUESTIONS), q,
                       'qEyebrow', 'On the call',
                       'qTitle', 'Which one would you actually say?',
                       ctx=q.get('ctx'), ctx_key=q.get('ctx_key'),
                       stem_key=q['stem_key'],
                       explains=q['explains'], folder=F, bg=q['bg'])
                  for i, q in enumerate(QUESTIONS))

        + D.results('resNext', 'Recognising the right sentence is the easy half. Now run the call &rarr;',
                    folder=F, bg='frame.jpg')

        + D.activate('Now run the review', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs',
                     'Twelve minutes, then swap. One runs the monthly review; one is the client who has not read the deck and interrupts.',
                     SPEAK,
                     'Writing &middot; 160&ndash;200 words',
                     'Write the follow-up email that goes out after the call. Headline first; two numbers with the movement stated correctly; one thing that went wrong and where it sat; one proposal with a review date. Nothing the client has to scroll to find.',
                     'Thanks for your time this morning. The headline is…',
                     folder=F, bg='pencil.jpg')
    )

    import i18n_campaign as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'The Monthly Review: Reporting a Campaign in English (B2)',
                   I, langs=('en', 'de', 'es', 'hr'))

    # The chip has to say the number the checker reports, and the raw section
    # count is one higher than that — the template's authoring comment contains
    # the string '<section class="slide' too. NSLIDES is patched in all three
    # languages as well as on the cover itself, or the number changes the
    # moment a learner touches the switcher.
    n = s.count('<section class="slide') - 1
    s = s.replace('NSLIDES', str(n))
    open(OUT, 'w', encoding='utf-8', newline='').write(s)

    gap_pts = sum(len(g['rows']) for g in GAPS)
    print('wrote %s — %d slides, %d scored (%d sort, %d gap, %d match, %d order, '
          '%d mc), %d bytes'
          % (OUT, n,
             len(SORT['items']) + gap_pts + len(MATCH) + len(ORDERS) + len(QUESTIONS),
             len(SORT['items']), gap_pts, len(MATCH), len(ORDERS), len(QUESTIONS),
             len(s)))


if __name__ == '__main__':
    build()
