# -*- coding: utf-8 -*-
"""Managing Risk (C1/C2) — builder.

Asked for as "risk management C1/C2 with Spanish and German support". No
existing lesson covered it, so this is a new build rather than a conversion,
and the eleven flat-vector illustrations supplied with the request are its own
art family: hero plus ten per-slide backgrounds, one palette derived from the
hero, nothing borrowed from another lesson.

The subject. "Risk management" could be project risk, insurance, or health and
safety; this is the corporate/enterprise register — the language of a risk
review, a register entry and an escalation email. It sits alongside
forbes-c1-negotiation and forbes-escalating-a-complaint-c1 rather than
duplicating either: negotiation is about moving another party, escalation is
about routing a problem upward, and this is about naming and grading a thing
that has not happened yet.

Six teaching points, each chosen because C1/C2 learners get it wrong in a way
that costs them credibility rather than marks:

  1. hazard / risk / exposure / issue are four different words. The commonest
     error is calling something a risk after it has already happened.
  2. the three preposition patterns — a risk OF the event, a risk TO the thing
     threatened, AT RISK OF the outcome. Fixed, and routinely crossed over.
  3. the four responses — treat, transfer, tolerate, terminate — and the fact
     that only the last one eliminates anything.
  4. calibration: "may well" raises probability, "might just" lowers it, and a
     stack of downtoners removes the information the reader needed.
  5. appetite / tolerance / capacity, which boards distinguish and learners
     collapse into one word.
  6. the passive: honest for an event whose agent is genuinely unknown,
     evasive for a decision or a future action, because those have people
     attached.

Shape: cover → 6 teach → 2 sort → 2 gap → 1 match → 2 order → 8 mc → results
→ activate. The engine scores a sort per item and a gap per input, not per
slide, so the fifteen question slides are worth more than fifteen points.

Level. Innes asked for C1/C2. The body is pitched C1 and four items are the
C2 stretch: the litotes question, the downtoner-stack question, the
appetite/capacity distinction and the passive-ownership question. A confident
C1 group can do the whole thing; the last two multiple-choice items are where
a C2 group earns its level.

Three things worth knowing before changing anything here.

* The palette is the verbatim output of

      python3 lesson-template/extract-palette.py RiskManagement/hero.jpg

  Every row of its contrast report reads PASS. Swapping the hero is a one-line
  change to HERO plus a re-run of that script and this builder; never hand-tune
  a channel.

* Every option's data-explain rides on the mc(explains=…) argument and the
  key's slot is None on purpose — the key is explained by the slide-level
  feedback, so a learner who picks a distractor is told what is wrong with
  their answer rather than what was right about someone else's.

* The distractors on the register questions were written LONG on purpose.
  House style §12 warns that a lesson about register walks into the
  key-is-longest defect every time, because the professional phrasing genuinely
  is the more elaborate one. Q8 is the clearest case: the honest line is the
  shortest of the four, and the three evasive ones had to be padded to match
  so that "pick the long one" is not a strategy.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-risk-management-c1-c2.html'

# One art family, supplied with the request. The hero is the Jenga tower with
# a hand steadying it — the only image in the set that depicts a risk and a
# mitigation in the same frame, which is why it is the cover rather than one
# of the two skyline shots.
F = 'RiskManagement'
HERO = 'hero.jpg'

# Mechanically derived — the verbatim output of
#     python3 lesson-template/extract-palette.py RiskManagement/hero.jpg
# Contrast report: PASS on all eight rows, the tightest being border on
# surface at 3.97:1 against a 1.25 floor. Never hand-pick a value in here.
PALETTE = '''  --hero: url('%s/%s');

  --void          : #100f0b;
  --surface       : #1e1b15;
  --surface2      : #2a261d;
  --border        : #b16648;
  --text          : #f5f3f2;
  --text-dim      : #bfaba3;
  --accent        : #e99776;
  --accent-bright : #f4b398;
  --accent-dim    : #d65e2d;
  --secondary     : #93a0a0;
  --contrast      : #1dedc4;''' % (F, HERO)


# ── teaching slides ────────────────────────────────────────────────────
# (eyebrow_key, eyebrow, title_key, title, cards, background)
# Cards are deck.teach's five-item form: (head_key, head, body, note_key,
# note). head_key is None throughout — the term and its English definition are
# the target language and must not translate; the note underneath is
# commentary about the term, so it does.
TEACH = [
    ('t1Eyebrow', 'The four words that get swapped',
     't1Title', '<em>Hazard</em>, <em>risk</em>, <em>exposure</em>, <em>issue</em>',
     [(None, 'hazard',
       'The thing that could do the damage: a sole supplier, an unpatched server, a currency.',
       't1n1', 'It exists whether or not it ever reaches you.'),
      (None, 'risk',
       'Likelihood combined with impact. Always future, always uncertain.',
       't1n2', 'The moment it becomes certain, it stops being a risk.'),
      (None, 'exposure',
       'How much of you sits in its path: &euro;4m, three sites, 60% of revenue.',
       't1n3', 'A quantity, not a judgement.'),
      (None, 'issue',
       'A risk that has already materialised. It has an owner and a fix.',
       't1n4', 'Calling it a risk after the fact sounds like hoping.')],
     'scrutiny.jpg'),

    ('t2Eyebrow', 'Three fixed patterns',
     't2Title', '<em>a risk of</em>, <em>a risk to</em>, <em>at risk of</em>',
     [(None, 'a risk <strong>of</strong> —',
       'names the event: <em>a risk of slippage, of contamination, of a strike</em>.',
       't2n1', 'Ask yourself: what is the event?'),
      (None, 'a risk <strong>to</strong> —',
       'names what is threatened: <em>a risk to margin, to the schedule, to our licence</em>.',
       't2n2', 'Ask yourself: what gets hurt?'),
      (None, '<strong>at risk of</strong> —',
       'promotes the threatened thing: <em>the launch is at risk of slipping</em>.',
       't2n3', 'Use it when the thing threatened matters more than the risk does.'),
      (None, 'all three',
       '<em>There is a risk <strong>of</strong> a strike; it is a risk <strong>to</strong> the launch, which is now <strong>at risk of</strong> slipping.</em>',
       't2n4', 'All three, in the order a reader expects them.')],
     'plaza.jpg'),

    ('t3Eyebrow', 'The four responses',
     't3Title', 'What you can actually do about a risk',
     [(None, 'treat',
       'Reduce the likelihood, the impact, or both: <em>mitigate, control, hedge</em>.',
       't3n1', 'Before controls it is <em>inherent risk</em>; what is left after them is <em>residual risk</em>.'),
      (None, 'transfer',
       'Move the financial consequence: insurance, an indemnity, a fixed-price contract.',
       't3n2', 'The event still happens. Only the bill moves.'),
      (None, 'tolerate',
       'Accept it consciously and say so: <em>we are accepting this within appetite</em>.',
       't3n3', 'Tolerating is a decision on the record. Ignoring is not.'),
      (None, 'terminate',
       'Stop doing the thing. The only response that removes the risk itself.',
       't3n4', 'The only response that can honestly use <em>eliminate</em>.')],
     'boardroom.jpg'),

    ('t4Eyebrow', 'Calibration',
     't4Title', 'Saying how likely it is, without hiding it',
     [(None, 'raising it',
       '<em>may well</em> &middot; <em>stands to</em> &middot; <em>a distinct possibility</em> &middot; <em>all but certain</em>',
       't4n1', '<em>We may well breach the covenant</em> is a warning, not a maybe.'),
      (None, 'lowering it',
       '<em>might just</em> &middot; <em>a remote possibility</em> &middot; <em>an outside chance</em> &middot; <em>conceivably</em>',
       't4n2', '<em>Might just</em> is weaker than <em>might</em>, not stronger.'),
      (None, 'litotes',
       '<em>not inconceivable</em> &middot; <em>a not insignificant exposure</em> &middot; <em>far from ideal</em>',
       't4n3', 'Understatement a C2 reader hears as emphasis &mdash; and a B2 reader may miss entirely.')],
     'cliff.jpg'),

    ('t5Eyebrow', 'Three words a board does not confuse',
     't5Title', 'Appetite, tolerance, capacity',
     [(None, 'risk appetite',
       'How much risk you <em>choose</em> to take in pursuit of a return. A statement of intent.',
       't5n1', 'Chosen deliberately, and minuted.'),
      (None, 'risk tolerance',
       'The acceptable variation around that appetite before someone has to act.',
       't5n2', 'A threshold that obliges someone to act, not a preference.'),
      (None, 'risk capacity',
       'The most you could absorb and still survive. A fact about the balance sheet.',
       't5n3', 'Not chosen. You can exceed your capacity once.')],
     'outlook.jpg'),

    ('t6Eyebrow', 'Register',
     't6Title', 'What the passive may hide &mdash; and what it may not',
     [(None, 'legitimate',
       '<em>The control was bypassed on 14 March.</em> The event is established; the agent is genuinely not yet known.',
       't6n1', 'Honest work: reporting what happened before you can say who.'),
      (None, 'evasive',
       '<em>It was felt that the review could be deferred.</em> A decision, with nobody attached to it.',
       't6n2', 'A decision with no decider, so there is nobody to ask.'),
      (None, 'the test',
       'Can a reader ask a person about this sentence? <em>Mistakes were made</em> &rarr; <em>we got the supplier assessment wrong</em>.',
       't6n3', 'If you know who, and the sentence hides them, that is the tell.')],
     'stakeholders.jpg'),
]


# ── sorting ────────────────────────────────────────────────────────────
# The first sort is four matched pairs: the same four stories on either side
# of the event. That is the point of it — the vocabulary and the tense both
# change at the moment the probability resolves, and a learner who sorts by
# topic rather than by tense will get exactly half of it right.
SORTS = [
    dict(bins=['Still a risk', 'Already an issue'],
         title_key='sortTitleA', title='Still ahead of you, or already landed?',
         hint_key='sortHintA',
         hint='Click a line, then the box it belongs in. Each pair is the same story on either side of the event.',
         items=[('Sterling could fall further before we settle in March.', 0),
                ('Sterling fell nine per cent and we settled at the lower rate.', 1),
                ('If the second auditor resigns, we lose our quorum.', 0),
                ('The second auditor resigned on Friday and we have no quorum.', 1),
                ('The regulator is consulting on a rule that would ban the additive.', 0),
                ('The additive was banned with effect from 1 July.', 1),
                ('Heavy rain is forecast for the week of the pour.', 0),
                ('The pour flooded and the slab has to be recut.', 1)],
         why='A risk is a probability with a date in the future; an issue is a fact with an owner. '
             'These are four stories told twice, and the grammar moves with them: <strong>could</strong>, '
             '<strong>if</strong> and <strong>is forecast</strong> on one side, simple past and present '
             'perfect on the other.'),

    dict(bins=['Treat', 'Transfer', 'Tolerate', 'Terminate'],
         title_key='sortTitleB', title='Which of the four responses is this?',
         hint_key='sortHintB',
         hint='Click a line, then the box it belongs in. One of these boxes takes actions that change nothing about the event itself.',
         items=[('Add a second qualified supplier in another jurisdiction.', 0),
                ('Install the patch and shorten the review cycle to weekly.', 0),
                ('Move to a fixed-price contract so the contractor carries the overrun.', 1),
                ('Take out political-risk cover on the shipment.', 1),
                ('Accept the exposure, minute the decision, and review it in June.', 2),
                ('Note it as within appetite and take no further action for now.', 2),
                ('Withdraw from the market and close the entity.', 3),
                ('Stop selling the product line altogether.', 3)],
         why='<strong>Treat</strong> changes the odds or the damage. <strong>Transfer</strong> moves the bill '
             'without moving the event &mdash; insurance does not stop the fire. <strong>Tolerate</strong> is a '
             'recorded decision, which is why both of its lines mention minuting or appetite. '
             '<strong>Terminate</strong> is the only one that removes the risk, and it does so by removing '
             'the activity.'),
]


# ── gap fill ───────────────────────────────────────────────────────────
# Both banks are alphabetised rather than built from the answers, which is what
# stops a bank being an answer key (house style §12, BANK gate). Three of the
# six chips on each slide are decoys.
BANK_A = ['against', 'at', 'beyond', 'of', 'to', 'within']
BANK_B = ['eliminate', 'escalate', 'mitigate', 'terminate', 'tolerate', 'transfer']

GAPS = [
    dict(bank=BANK_A, title_key='gapTitleA', title='Complete the pattern',
         hint_key='gapHintA', hint='One word per gap. Three of the six are not needed.',
         width=110,
         rows=[('There is a serious risk ______ contamination if the seal fails.',
                ['of'], '<strong>Of</strong> names the event that might occur.'),
               ('That is a risk ______ our licence to operate, not merely to margin.',
                ['to'], '<strong>To</strong> names what is threatened &mdash; here, the licence.'),
               ('On current volumes the fund is ______ risk of breaching its mandate.',
                ['at'], '<strong>At risk of</strong> is fixed, and it puts the threatened thing in subject position.')],
         why=None),

    dict(bank=BANK_B, title_key='gapTitleB', title='Complete the response',
         hint_key='gapHintB',
         hint='One verb per gap. Three of the six are not needed &mdash; and two of those three are the ones people reach for by mistake.',
         width=170,
         rows=[('Insurance does not stop the fire &mdash; it can only ______ the cost to the underwriter.',
                ['transfer'], '<strong>Transfer</strong> moves the financial consequence. The fire still burns.'),
               ('A second supplier will ______ the impact without removing the hazard.',
                ['mitigate'], '<strong>Mitigate</strong> reduces likelihood or impact, and always leaves residual risk.'),
               ('The board chose to ______ the exposure and minute the decision.',
                ['tolerate'], '<strong>Tolerate</strong> is an accepted risk on the record &mdash; which is exactly what minuting it does.')],
         why=None),
]


# ── matching ───────────────────────────────────────────────────────────
# Definitions are held to a similar length for the same reason MC options are:
# length must not leak the pairing.
MATCH = [
    ('risk appetite', 'how much risk you choose to take in pursuit of a return'),
    ('risk tolerance', 'the acceptable variation before someone is obliged to act'),
    ('risk capacity', 'the most you could absorb and still remain solvent'),
    ('residual risk', 'what is left once the agreed controls are working'),
    ('exposure', 'the quantity of you that sits in the hazard&rsquo;s path'),
    ('risk transfer', 'moving the financial consequence, never the event'),
]


# ── ordering ───────────────────────────────────────────────────────────
ORDERS = [
    dict(title_key='ordTitleA', title='Flagging it early',
         hint_key='ordHintA', hint='Click the parts in order. Soft delivery, hard content.',
         items=['I want to flag early', 'that the November launch',
                'is at risk of slipping', 'and that on current evidence',
                'a six-week delay', 'is a distinct possibility'],
         why='The delivery is soft &mdash; <strong>I want to flag early</strong> &mdash; and the content is not. '
             '<strong>At risk of</strong> puts the launch in subject position, and <strong>a distinct '
             'possibility</strong> commits to a probability instead of retreating into <em>possibly some slight '
             'delay</em>.'),

    dict(title_key='ordTitleB', title='A register entry',
         hint_key='ordHintB', hint='Click the parts in order: cause, event, consequence.',
         items=['Because the additive is under consultation', 'there is a risk',
                'that it will be banned before Q3',
                'which would cost us two production lines', 'and a quarter of our volume'],
         why='A register entry names the <strong>cause</strong>, the <strong>event</strong> and the '
             '<strong>consequence</strong>, in that order. Drop the cause and nobody can act on it; drop the '
             'consequence and nobody will.'),
]


# ── multiple choice ────────────────────────────────────────────────────
# Key positions are 0, 2, 1, 3, 0, 2, 1, 3 — deliberately spread, because the
# KEYS gate reads the authored order and a run of identical indices is a
# pattern a learner can find even though the engine shuffles at runtime.
QUESTIONS = [
    dict(stem='The regulator banned the additive last Thursday. In Monday&rsquo;s report, this is now &mdash;',
         options=['an issue: it has happened and needs an owner',
                  'a risk: it could affect next quarter&rsquo;s volume',
                  'a hazard: it sits outside our direct control',
                  'an exposure: it covers two production lines'],
         correct=0,
         explains=[None,
                   'It has already happened, so the probability has resolved. It stopped being a risk on Thursday.',
                   'The consultation was the hazard. Once the ban took effect you are past hazard language.',
                   'Exposure is the quantity in the path &mdash; two lines. The ban is the event, not the amount.'],
         why='When the probability resolves, the vocabulary changes with it. An issue has an owner and a fix; '
             'a risk has a likelihood and a date.',
         bg='window.jpg'),

    dict(stem='Which sentence uses all three <em>risk</em> patterns correctly?',
         options=['There is a risk to a strike, which is a risk of the launch; the launch is on risk of slipping.',
                  'There is a risk for a strike, which is a risk at the launch; the launch is in risk of slipping.',
                  'There is a risk of a strike, which is a risk to the launch; the launch is at risk of slipping.',
                  'There is a risk at a strike, which is a risk for the launch; the launch is of risk to slipping.'],
         correct=2,
         explains=['<strong>Risk of</strong> names the event and <strong>risk to</strong> names what is threatened. This reverses them, and <em>on risk of</em> is not English.',
                   '<em>A risk for</em> and <em>a risk at</em> exist in other senses but not this one, and the fixed phrase is <strong>at risk of</strong>, never <em>in risk of</em>.',
                   None,
                   'All three are wrong. The pattern does not vary: <strong>a risk of</strong> the event, <strong>a risk to</strong> what is threatened, <strong>at risk of</strong> the outcome.'],
         why='<strong>Of</strong> names the event, <strong>to</strong> names what is threatened, and '
             '<strong>at risk of</strong> promotes the threatened thing to subject. None of the three is '
             'interchangeable with another.',
         bg='exposure.jpg'),

    dict(stem='The team has added a second supplier in another jurisdiction. Accurately, this &mdash;',
         options=['eliminates the risk of any supply disruption',
                  'mitigates the impact but leaves a residual risk',
                  'transfers the exposure to the second supplier',
                  'tolerates the risk while the board reviews it'],
         correct=1,
         explains=['Only stopping the activity eliminates a risk. Both suppliers could still fail on the same day.',
                   None,
                   'Transfer moves a financial consequence by contract or insurance. A second supplier changes the odds.',
                   'Tolerating is a recorded decision to accept. Adding a supplier is an action, so it is treatment.'],
         why='<strong>Mitigate</strong> reduces likelihood or impact and always leaves <strong>residual '
             'risk</strong>. Only <strong>terminate</strong> removes a risk, and only by removing the activity.',
         bg='boardroom.jpg'),

    dict(stem='You believe a covenant breach is now more likely than not. Which sentence says so?',
         options=['We might just breach the covenant this quarter.',
                  'We could conceivably breach it later this quarter.',
                  'There is an outside chance of a breach this quarter.',
                  'We may well breach the covenant this quarter.'],
         correct=3,
         explains=['<strong>Might just</strong> is weaker than <em>might</em>. It marks a bare possibility, not a probability above half.',
                   '<strong>Conceivably</strong> concedes only that something is imaginable. It sits near the bottom of the scale.',
                   '<strong>An outside chance</strong> is a long shot &mdash; what you say when you are hoping, not when you are warning.',
                   None],
         why='<strong>May well</strong> puts the probability above evens and is heard as a warning. The other '
             'three all lower it, and one of them is what people reach for when they want to be able to say '
             'afterwards that they did mention it.',
         bg='cliff.jpg'),

    dict(stem='&ldquo;We could absorb a &euro;40m loss and still meet our obligations.&rdquo; This is a statement of &mdash;',
         options=['risk capacity, which is a fact about the balance sheet',
                  'risk appetite, which is a choice the board has made',
                  'risk tolerance, which is the band around that choice',
                  'risk exposure, which is the amount currently at stake'],
         correct=0,
         explains=[None,
                   'Appetite is what you are willing to take. This sentence says nothing about willingness, only about survival.',
                   'Tolerance is the variation allowed before someone must act. This is the outer wall, not the band inside it.',
                   'Exposure is what is at stake right now. The &euro;40m here is what could be absorbed, not what is committed.'],
         why='<strong>Capacity</strong> is a fact you can exceed only once; <strong>appetite</strong> is chosen '
             'and <strong>tolerance</strong> is the band around it. Boards get into trouble when a statement of '
             'capacity is minuted as appetite.',
         bg='outlook.jpg'),

    dict(stem='Which line belongs in a risk register, where every entry needs an owner?',
         options=['It was felt that the seal did not require re-testing.',
                  'Arrangements are being made for the seal to be re-tested.',
                  'Ravi Shah will re-test the seal before the 9 May pour.',
                  'The seal will be re-tested at some point before the pour.'],
         correct=2,
         explains=['<em>Felt</em> by whom? The verb has no subject, so there is nobody to ask and nothing to chase.',
                   'The passive hides the agent of a future action, which is exactly where a register needs a name.',
                   None,
                   'The action is named but the actor and the date are not, and <em>at some point</em> is not a date anyone can miss.'],
         why='The passive is honest when it reports an event whose agent you genuinely do not know. It is '
             'evasive when it describes a decision or a future action, because both of those always have a '
             'person attached.',
         bg='stakeholders.jpg'),

    dict(stem='A CFO writes: <em>the exposure is not insignificant.</em> A C2 reader takes this to mean &mdash;',
         options=['the exposure is small but has not yet been quantified',
                  'the exposure is large, said with deliberate understatement',
                  'the exposure is moderate and sits within the agreed tolerance',
                  'the exposure is uncertain and the figure is still moving'],
         correct=1,
         explains=['Litotes never means <em>small</em>. Denying the negative asserts the positive, and usually asserts it strongly.',
                   None,
                   '<em>Not insignificant</em> is not a middle value. The construction is emphasis dressed as caution.',
                   'Nothing here is about uncertainty. The writer is confident about the size and understated about saying it.'],
         why='Denying the opposite &mdash; <strong>not insignificant</strong>, <strong>far from ideal</strong>, '
             '<strong>not inconceivable</strong> &mdash; asserts the positive and adds weight to it. It is a C2 '
             'habit that a B2 reader can take at face value, which is sometimes exactly why it is used.',
         bg='scrutiny.jpg'),

    dict(stem='You know the slab must be recut, adding six weeks. Which line flags it without misleading?',
         options=['There may possibly be some slight impact on the programme arising from the pour.',
                  'The pour was not entirely successful and the programme is currently under review.',
                  'Some minor remedial work is anticipated, and we will of course keep you updated.',
                  'The pour has failed. Recutting adds six weeks; I want to agree a revised date.'],
         correct=3,
         explains=['Every word is a downtoner: <em>may</em>, <em>possibly</em>, <em>some</em>, <em>slight</em>. Stacked, they remove the information the reader needed.',
                   '<em>Not entirely successful</em> is litotes used to shrink rather than to emphasise, and <em>under review</em> gives no date and no number.',
                   '<em>Minor</em> is a judgement the reader is entitled to make for themselves, and <em>keep you updated</em> defers the only thing they need.',
                   None],
         why='Soften the <strong>delivery</strong> &mdash; <em>I want to flag early</em> &mdash; and never the '
             '<strong>content</strong>. The reader needs the fact, the number and the ask; hedging any of the '
             'three buys you a week and costs you the next conversation.',
         bg='downside.jpg'),
]

# The phrases the activation stage expects to hear. Target language, so they
# stay in English in all three switcher languages.
CHIPS = ['a risk of &middot; a risk to', 'at risk of', 'mitigate the impact',
         'transfer the exposure', 'within appetite', 'residual risk',
         'may well', 'a distinct possibility']

SPEAK = [
    'You own the cobalt exposure: cause, event, consequence, then one recommended response and one you rejected.',
    'Finance director: the recommendation costs &euro;2m a year. Push back using <em>appetite</em>, <em>tolerance</em> and <em>capacity</em>.',
    'The event has now happened. Same room &mdash; every risk is now an issue. Redo it in ninety seconds.',
    'Argue the other side: when is <em>tolerate</em> the professional answer rather than the lazy one?',
]


def build():
    D.assert_no_key_is_longest(QUESTIONS, 'Risk')
    for g in GAPS:
        D.assert_bank_is_not_a_key(g['bank'], [r[1][0] for r in g['rows']])

    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Managing <em>Risk</em>',
                'Naming exposure, grading it, owning it and acting on it &mdash; without overstating what you know or hiding what you do',
                [('Level', 'C1&ndash;C2 &middot; Enterprise risk'),
                 ('Focus', 'Precision, calibration and ownership'),
                 ('Count', 'NSLIDES slides')])

        + "".join(D.teach(ek, e, tk, t, cards, folder=F, bg=bg)
                  for ek, e, tk, t, cards, bg in TEACH)

        + D.sort_slide(SORTS[0]['bins'], SORTS[0]['items'],
                       'sortEyebrow', 'Before you open your mouth',
                       SORTS[0]['title_key'], SORTS[0]['title'],
                       SORTS[0]['hint_key'], SORTS[0]['hint'], SORTS[0]['why'],
                       folder=F, bg='downside.jpg')

        + D.sort_slide(SORTS[1]['bins'], SORTS[1]['items'],
                       'sortEyebrow', 'Before you open your mouth',
                       SORTS[1]['title_key'], SORTS[1]['title'],
                       SORTS[1]['hint_key'], SORTS[1]['hint'], SORTS[1]['why'],
                       folder=F, bg='site.jpg')

        + "".join(D.gap(i + 1, len(GAPS), g['rows'], g['bank'],
                        'gapEyebrow', 'The grammar of risk',
                        g['title_key'], g['title'],
                        hint=g['hint'], hint_key=g['hint_key'], why=g['why'],
                        width=g['width'], folder=F,
                        bg=('plaza.jpg' if i == 0 else 'site.jpg'))
                  for i, g in enumerate(GAPS))

        + D.match(MATCH, 'matEyebrow', 'Precision',
                  'matTitle', 'Match the term to what it actually means',
                  'matHint',
                  'Six terms, six definitions. Three of them are routinely used as if they were interchangeable; they are not.',
                  'Appetite is chosen, tolerance is the band around it, and capacity is a fact about what you could '
                  'survive. <strong>Residual risk</strong> is what your controls leave behind &mdash; there is always '
                  'some, and a register that shows none is a register nobody has finished.',
                  folder=F, bg='scrutiny.jpg')

        + "".join(D.order(o['items'], 'ordEyebrow', 'Build the sentence',
                          o['title_key'], o['title'],
                          o['hint_key'], o['hint'], o['why'],
                          folder=F, bg=('window.jpg' if i == 0 else 'exposure.jpg'))
                  for i, o in enumerate(ORDERS))

        + "".join(D.mc(i + 1, len(QUESTIONS), q,
                       'qEyebrow', 'Choose the version that survives being forwarded',
                       'qTitle', 'Which one would you actually write?',
                       explains=q['explains'], folder=F, bg=q['bg'])
                  for i, q in enumerate(QUESTIONS))

        + D.results('resNext', 'Recognising the register is the easy half. Now say it to a sponsor &rarr;',
                    folder=F, bg='outlook.jpg')

        + D.activate('Now run the risk review', 'Use at least four:', CHIPS,
                     'Discussion &middot; in threes',
                     'Ten minutes. One chairs, one owns the risk, one is the finance director who signs the decision.',
                     SPEAK,
                     'Writing &middot; 180&ndash;220 words',
                     'Write the escalation email to the sponsor. Name the cause, the event and the consequence; calibrate the probability instead of hedging it; give the response you recommend and the one you rejected; end with a named owner and a date.',
                     'I want to flag early that…',
                     folder=F, bg='boardroom.jpg')
    )

    import i18n_risk as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Managing Risk: Exposure, Calibration and Ownership (C1/C2)',
                   I, langs=('en', 'de', 'es'))

    # The chip has to say the number the checker reports, and the raw section
    # count is one higher than that — the template's authoring comment contains
    # the string '<section class="slide' too. NSLIDES is patched in all three
    # languages as well as on the cover itself, or the number changes the
    # moment a learner touches the switcher.
    n = s.count('<section class="slide') - 1
    s = s.replace('NSLIDES', str(n))
    open(OUT, 'w', encoding='utf-8').write(s)

    sort_pts = sum(len(x['items']) for x in SORTS)
    gap_pts = sum(len(g['rows']) for g in GAPS)
    print('wrote %s — %d slides, %d scored (%d sort, %d gap, %d match, %d order, '
          '%d mc), %d bytes'
          % (OUT, n, sort_pts + gap_pts + len(MATCH) + len(ORDERS) + len(QUESTIONS),
             sort_pts, gap_pts, len(MATCH), len(ORDERS), len(QUESTIONS), len(s)))


if __name__ == '__main__':
    build()
