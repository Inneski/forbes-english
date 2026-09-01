# -*- coding: utf-8 -*-
"""The Social Edge (C2) — builder.

Asked for as "make forbes english C2 class with spanish and german support"
against Bright Simons's essay *The Social Edge of Intelligence* (The Ideas
Letter 62, 16 April 2026). New build, not a conversion: nothing on the site
teaches the language of written argument at C2, and the two nearest decks are
not close. forbes-risk-management-c1-c2 owns calibration and hedging;
forbes-ai-productive-struggle-c1 owns AI as a classroom subject. This one owns
the moves an argumentative essay makes — and deliberately leaves calibration
alone so the two do not overlap.

The subject is the essay's *language*, not its opinions. The learner does not
have to agree that AI is thinning its own substrate; they have to be able to
report the claim without signing it, concede the other side before turning,
and choose between seven verbs of decline that are not synonyms.

Six teaching points, each chosen because it is where a strong B2/C1 writer
stops sounding like the source text:

  1. nominalisation — packing a clause into a noun phrase so it can be the
     subject of the next claim, and the actor it costs you.
  2. the verbs of decline as a scale, not a synonym set: thin, narrow,
     converge, attenuate, erode, degrade, collapse.
  3. reporting verbs carry a verdict. *Argues* reports; *establishes* signs;
     *declines to examine* is a critique, said politely.
  4. concession and pivot — the strongest version of the other side, then one
     sentence that turns.
  5. conditional chains and inversion: if … and if … then; *were it to*.
  6. metaphor as argument: a live metaphor makes a claim you can dispute, and
     an extended one has to stay inside its own frame.

Shape: cover -> 6 teach -> 2 sort -> 2 gap -> 1 match -> 2 order -> 8 mc ->
results -> activate = 24 slides. The engine scores a sort per item and a gap
per input, so the fifteen question slides are worth well over fifteen points.

Level. C2 throughout rather than C1 with a stretch. The discriminations are
fine-grained on purpose — converge against erode, *declines to examine*
against *appears to have overlooked* — because that is what separates C2 from
a confident C1 who can already read the essay.

Three things worth knowing before changing anything here.

* THE PALETTE IS PROVISIONAL. The five illustrations supplied with the
  request never reached the build sandbox as files, so the palette below is
  the verbatim output of extract-palette.py run on RiskManagement/outlook.jpg
  — a plate from the same flat-vector family, chosen because its composition
  (large slate field, coral secondary, dark figures) matches this hero's. The
  family is mechanically stable: four plates from it were measured and the
  accent moved by three points across all four. The moment SocialEdge/hero.jpg
  exists, re-derive and rebuild:

      python3 lesson-template/extract-palette.py SocialEdge/hero.jpg
      # paste over PALETTE below
      python3 lesson-template/build/build_socialedge.py
      node   lesson-template/check-lesson.js forbes-social-edge-c2.html
      python3 tools/seo.py

  Nothing else in this file depends on the artwork.

* Every option's data-explain rides on mc(explains=...) and the key's slot is
  None on purpose: a learner who picks a distractor is told what is wrong with
  their own answer, not what was right about someone else's.

* The distractors were written LONG on purpose. House style §12 warns that a
  lesson about register walks into the key-is-longest defect every time,
  because the more careful phrasing genuinely is the more elaborate one. Q4 is
  the clearest case: the concede-then-pivot key is a two-clause sentence, so
  all three distractors were padded to match it rather than the key trimmed.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-social-edge-c2.html'

# One art family, five plates, supplied with the request. The hero is the row
# of profiles that ends in a machine head — the only image in the set that
# carries the essay's own argument (a lineage of minds, and what is standing at
# the end of it), which is why it is the cover rather than the bar or the
# typing room.
F = 'SocialEdge'
HERO = 'hero.jpg'
BG_WATCH = 'watchers.jpg'      # the crowd in hats and dark glasses
BG_BAR = 'barroom.jpg'         # the bar at dusk: the spaces between people
BG_TYPE = 'typewriters.jpg'    # the row of chimps at typewriters
BG_NIGHT = 'nightshift.jpg'    # terminals under a low sun

# PROVISIONAL — see the docstring. Verbatim output of
#     python3 lesson-template/extract-palette.py RiskManagement/outlook.jpg
# Contrast report: PASS on every row, text on surface 15.90:1, text-dim on
# surface 7.97:1. Never hand-pick a value in here; re-derive it instead.
PALETTE = '''  --hero: url('%s/%s');

  --void          : #0a0d0e;
  --surface       : #141a1b;
  --surface2      : #1c2527;
  --border        : #b86c54;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #eb9f87;
  --accent-bright : #f6bcaa;
  --accent-dim    : #d8633e;
  --secondary     : #3a5762;
  --contrast      : #1dedbb;''' % (F, HERO)


# ── teaching slides ────────────────────────────────────────────────────
# (eyebrow_key, eyebrow, title_key, title, cards, background)
# deck.teach's five-item form: (head_key, head, body, note_key, note). The
# head and the body are the target language and carry no data-i18n; the note
# underneath is commentary about it, so it translates.
TEACH = [
    ('t1Eyebrow', 'Density, and what it costs',
     't1Title', 'Nominalisation: turning a claim into a thing',
     [(None, 'the automation of thought',
       'A whole clause &mdash; <em>people stop thinking for themselves</em> &mdash; packed into a noun phrase.',
       't1n1', 'Once it is a noun, it can be the subject of your next sentence.'),
      (None, 'cognitive offloading',
       'Naming a mechanism so that it can be measured, cited and argued with: <em>knowledge collapse</em>, <em>model collapse</em>.',
       't1n2', 'Naming the thing is the first move in owning the argument about it.'),
      (None, 'individual gain, collective loss',
       'The essay&rsquo;s whole thesis in four words, because both halves are nouns.',
       't1n3', 'A nominalised pair is what makes a claim quotable.'),
      (None, 'the price',
       '<em>The elimination of interaction-dense work</em> has nobody eliminating anything.',
       't1n4', 'Same tell as the passive: ask who did it, and see whether the sentence can answer.')],
     BG_WATCH),

    ('t2Eyebrow', 'Seven verbs, one scale',
     't2Title', 'The vocabulary of decline is not a synonym set',
     [(None, 'thin &middot; thin out',
       'Fewer of them, less densely: <em>junior roles thin out</em>, <em>the substrate is allowed to thin</em>.',
       't2n1', 'About how many there are, never about quality.'),
      (None, 'narrow &middot; converge',
       'The range shrinks; the things inside it become alike: <em>collectively, they had converged</em>.',
       't2n2', '<em>Converge</em> is about similarity and can never mean <em>fewer</em>.'),
      (None, 'erode &middot; attenuate',
       'Worn away from outside; weakened as a signal: <em>a slow attenuation of the substrate</em>.',
       't2n3', '<em>Erode</em> takes surfaces and institutions; <em>attenuate</em> takes signals and effects.'),
      (None, 'degrade &middot; collapse',
       'Quality falls; the structure goes entirely: <em>models collapse when trained on their own output</em>.',
       't2n4', '<em>Collapse</em> is the end state. The other six are the road to it.')],
     BG_TYPE),

    ('t3Eyebrow', 'Reporting, or agreeing',
     't3Title', 'The verb you choose is a verdict',
     [(None, 'neutral',
       '<em>argues</em> &middot; <em>writes</em> &middot; <em>observes</em> &middot; <em>reports</em> &middot; <em>frames it as</em>',
       't3n1', 'You have reported the claim. You have not signed it.'),
      (None, 'endorsing',
       '<em>establishes</em> &middot; <em>demonstrates</em> &middot; <em>shows</em> &middot; <em>quantifies</em>',
       't3n2', 'Use one of these and you have agreed. That is a decision, not a style.'),
      (None, 'limiting',
       '<em>assumes</em> &middot; <em>concedes</em> &middot; <em>declines to examine</em> &middot; <em>comes closest to acknowledging</em>',
       't3n3', 'These name what the source did not do &mdash; the sharpest tool in a critique.'),
      (None, 'distancing',
       '<em>reaches for a phrase</em> &middot; <em>is typically framed as</em> &middot; <em>I suspect mere rhetorical flourish</em>',
       't3n4', 'You describe the move rather than accepting the fact.')],
     BG_BAR),

    ('t4Eyebrow', 'The shape of an argument',
     't4Title', 'Concede properly, then turn once',
     [(None, 'concede first',
       '<em>Yes, scaling matters, architecture matters, and compute matters.</em>',
       't4n1', 'Give the strongest version of the other side. A weak concession reads as a trick.'),
      (None, 'pivot once',
       '<em>But none of these will continue to deliver if the social substrate is allowed to thin.</em>',
       't4n2', 'One sentence, and it carries the essay. Two pivots and the reader stops believing either.'),
      (None, 'the false agreement',
       '<em>So far, so on message. But when the researchers examined the full body of stories&hellip;</em>',
       't4n3', 'Set the consensus up in its own words, then break it with the evidence.'),
      (None, 'correct the cause',
       '<em>It is smarter not because the architecture changed but because the civilization did.</em>',
       't4n4', 'You accept the fact and reassign its reason. Far harder to answer than a flat denial.')],
     BG_WATCH),

    ('t5Eyebrow', 'Premises and payoff',
     't5Title', 'Conditional chains, and the inverted form',
     [(None, 'if &hellip; and if &hellip; then',
       '<em>If capability depends on social complexity &mdash; and if deployment reduces it &mdash; then the technology undermines itself.</em>',
       't5n1', 'Two premises, one conclusion. The dashes hold the second premise open.'),
      (None, 'inversion',
       '<em>Were the substrate to thin further&hellip;</em> &middot; <em>Should the springs dry up&hellip;</em> &middot; <em>Had the tails survived&hellip;</em>',
       't5n2', 'Formal, and it front-loads the condition. No <em>if</em>, and never <em>if &hellip; would</em>.'),
      (None, 'the thought experiment',
       '<em>Suppose you could travel to Egypt in 3000 BC&hellip; The result would be a system capable of&hellip;</em>',
       't5n3', '<em>Suppose</em> sets it up and <em>would</em> runs to the end of it, without ever slipping into <em>will</em>.'),
      (None, 'where the hedge goes',
       '<em>Their compound effect may be catastrophic</em> &mdash; hedged conclusion, unhedged premises.',
       't5n4', 'Hedge the conclusion. Hedge the premises too and you have argued nothing.')],
     BG_NIGHT),

    ('t6Eyebrow', 'Figurative language that argues',
     't6Title', 'A live metaphor makes a claim you can dispute',
     [(None, 'substrate',
       'What a thing grows on: <em>the social substrate</em>, <em>the springs feeding the reservoir</em>.',
       't6n1', 'It chooses the frame: intelligence as a crop, not as a machine.'),
      (None, 'inheritance',
       '<em>Inheritances, if consumed without reinvestment, eventually run out.</em>',
       't6n2', 'An extended metaphor has to stay inside one frame: consume, reinvest, run out.'),
      (None, 'borrowed precision',
       '<em>a tragedy of the commons</em> &middot; <em>the tails of the distribution</em> &middot; <em>a fossil of social interaction</em>',
       't6n3', 'Taken from a field that defines it. It must survive being read literally.'),
      (None, 'live or dead',
       '<em>a doom-spiral</em> is nearly dead; <em>the springs feeding it are drying up</em> is alive.',
       't6n4', 'A live metaphor advances the argument. A dead one is just a word you reached for.')],
     BG_TYPE),
]


# ── sorting ────────────────────────────────────────────────────────────
# Both sorts are three-bin, three-each. Two bins would let a learner score
# half of it by coin toss, and the discrimination that matters here is
# three-way: reporting is not endorsing, and neither is critique.
SORTS = [
    dict(bins=['Reports the claim', 'Signs the claim', 'Marks what the source missed'],
         title_key='sortTitleA', title='Reporting it, or agreeing with it?',
         hint_key='sortHintA',
         hint='Click a line, then the box it belongs in. Every line is about somebody else&rsquo;s work &mdash; the question is what the verb commits the writer to.',
         items=[('Hutchins wrote that the symbol system is a model with the human removed.', 0),
                ('Shumailov and colleagues published a paper with a blunt title.', 0),
                ('Altman frames society itself as a form of advanced intelligence.', 0),
                ('Tomasello&rsquo;s work establishes that cognition diverged through collaboration.', 1),
                ('Dunbar&rsquo;s hypothesis quantifies the link between neocortex and group size.', 1),
                ('They demonstrated that recursive training degrades a model.', 1),
                ('Aschenbrenner assumes that scaling is the primary constraint.', 2),
                ('Amodei does not consider that the training data may be degrading.', 2),
                ('The industry has largely declined to examine this dependency.', 2)],
         why='<strong>Wrote</strong>, <strong>published</strong> and <strong>frames&nbsp;as</strong> report a claim and leave you free of it. '
             '<strong>Establishes</strong>, <strong>quantifies</strong> and <strong>demonstrated</strong> sign it: use one and you have agreed in '
             'print. <strong>Assumes</strong>, <strong>does not consider</strong> and <strong>declines to examine</strong> are the critique, and '
             'they are polite precisely because they name the omission instead of the person.'),

    dict(bins=['Concedes', 'Pivots', 'Corrects the cause'],
         title_key='sortTitleB', title='Which move is the sentence making?',
         hint_key='sortHintB',
         hint='Click a line, then the box it belongs in. One box accepts the fact and changes only the reason given for it.',
         items=[('The trajectory has a compelling internal logic.', 0),
                ('Yes, scaling matters, architecture matters, and compute matters.', 0),
                ('So far, so on message: a familiar story about intelligent machines.', 0),
                ('But the results of a team in the UK should give us pause.', 1),
                ('But across the full body of stories, the picture became murky.', 1),
                ('But none of it delivers if the social substrate is allowed to thin.', 1),
                ('It is smarter not because the architecture changed but because the world did.', 2),
                ('The reservoir is not draining so much as the springs are drying up.', 2),
                ('The intelligence was never individual: it was forged between people.', 2)],
         why='A <strong>concession</strong> states the other side at full strength and in its own words. A <strong>pivot</strong> introduces the '
             'evidence that breaks it, and there should be one. A <strong>cause correction</strong> does something harder: it accepts the fact and '
             'reassigns the reason &mdash; <em>not because X but because Y</em>, <em>not A so much as B</em>, <em>never P: Q</em>. An opponent can '
             'answer a denial. Reassigning the cause leaves them agreeing with you about what happened.'),
]


# ── gap fill ───────────────────────────────────────────────────────────
# Both banks are alphabetised rather than built from the answers, which is
# what stops a bank being an answer key (house style §12, BANK gate). The
# first bank is given in base forms and the sentences need them inflected —
# a C2 demand, and it is stated in the hint.
BANK_A = ['attenuate', 'collapse', 'converge', 'degrade', 'erode', 'narrow', 'thin']
BANK_B = ['attenuation', 'collapse', 'commons', 'convergence',
          'homogenisation', 'offloading', 'redundancy']

GAPS = [
    dict(bank=BANK_A, title_key='gapTitleA', title='Choose the verb that is actually true',
         hint_key='gapHintA',
         hint='One verb per gap, in the right form. Four of the seven are not needed &mdash; and two of those four are the ones people reach for by mistake.',
         width=150,
         rows=[('Each writer was lifted; collectively, their stories had ______ on one shape.',
                ['converged'],
                '<strong>Converge</strong> is about similarity, not quantity. Nothing was lost here &mdash; the stories became alike, which is a different complaint and the essay&rsquo;s actual one.'),
               ('Over successive generations the distribution ______ and the rare formulations go first.',
                ['narrows'],
                '<strong>Narrow</strong> takes a range, a distribution, a gap. The tails are the edges of it, so they are what a narrowing removes.'),
               ('If those interactions become rarer, the intelligence that depends on them will ______.',
                ['degrade'],
                '<strong>Degrade</strong> is a fall in quality over time, which is the claim. <em>Collapse</em> would promise a sudden and total failure that the essay is careful not to predict.')],
         why=None),

    dict(bank=BANK_B, title_key='gapTitleB', title='Pack the clause into a noun phrase',
         hint_key='gapHintB',
         hint='One noun per gap. Four of the seven are not needed. Each sentence says the same thing twice &mdash; once as a clause, once as a noun.',
         width=210,
         rows=[('Writers converge on the same shapes: the ______ of creative output.',
                ['homogenisation|homogenization'],
                'The noun for <em>everything becomes the same</em>. Both spellings are current; the essay uses the <em>-z-</em> one.'),
               ('Public knowledge gets worse; Peterson calls this knowledge ______.',
                ['collapse'],
                'A compound noun does the work of a whole finding: <em>knowledge collapse</em>, <em>model collapse</em>. That is what makes it citable.'),
               ('The substrate weakens slowly: a slow ______ of the thing AI feeds on.',
                ['attenuation'],
                'The noun from <em>attenuate</em>. Note what has vanished with the verb &mdash; there is no longer anyone attenuating anything.')],
         why=None),
]


# ── matching ───────────────────────────────────────────────────────────
# Definitions are held to a similar length for the same reason MC options
# are: length must not leak the pairing.
MATCH = [
    ('a tragedy of the commons', 'each actor gains by a move that leaves everyone worse off'),
    ('model collapse', 'output narrows once a system is trained on what it produced'),
    ('cognitive offloading', 'handing a mental job to a tool the moment one is available'),
    ('tacit knowledge', 'what can only be picked up by doing the work beside someone'),
    ('the Social Edge Paradox', 'a technology thinning the very thing that it feeds on'),
    ('convex leadership', 'a payoff whose upside grows faster than its downside falls'),
]


# ── ordering ───────────────────────────────────────────────────────────
ORDERS = [
    dict(title_key='ordTitleA', title='The argument in one sentence',
         hint_key='ordHintA', hint='Click the parts in order: two premises, then what follows from them.',
         items=['If the capability of a model', 'depends on the social complexity of human language',
                'and if its deployment reduces that complexity',
                'then the technology is quietly undermining', 'the conditions for its own advancement'],
         why='<strong>If &hellip; and if &hellip; then</strong> is the whole essay. Both premises land before the conclusion is '
             'named, so a reader who wants to disagree has to say which premise is wrong &mdash; which is exactly the '
             'argument you want to have. Put the conclusion first and it reads as an assertion with reasons bolted on.'),

    dict(title_key='ordTitleB', title='Concede, then turn',
         hint_key='ordHintB', hint='Click the parts in order. The concession is real and it comes first.',
         items=['Scaling matters, architecture matters', 'and compute matters',
                'but none of these will keep delivering', 'if the social substrate',
                'is allowed to thin'],
         why='The concession is given in the other side&rsquo;s own vocabulary and at full strength &mdash; three things, not one '
             'grudging clause &mdash; and then a single <strong>but</strong> turns it. <em>Is allowed to thin</em> closes it on a '
             'passive that is doing honest work: nobody in particular is thinning it, which is the point of the paradox.'),
]


# ── multiple choice ────────────────────────────────────────────────────
# Key positions are 0, 2, 1, 3, 0, 2, 3, 1 — deliberately spread, because the
# KEYS gate reads the authored order and a run of identical indices is a
# pattern a learner can find even though the engine shuffles at runtime.
QUESTIONS = [
    dict(stem='You are summarising Aschenbrenner&rsquo;s framework and you do not accept it. Which verb reports the claim without signing it?',
         options=['Aschenbrenner assumes that scaling is the primary constraint on capability.',
                  'Aschenbrenner establishes that scaling is the primary constraint on capability.',
                  'Aschenbrenner demonstrates that scaling is the primary constraint on capability.',
                  'Aschenbrenner has proven that scaling is the primary constraint on capability.'],
         correct=0,
         explains=[None,
                   '<strong>Establishes</strong> means the case is now settled. Write it and you have agreed with him in print.',
                   '<strong>Demonstrates</strong> vouches for the evidence as well as the claim. You are lending him your own credibility.',
                   '<strong>Has proven</strong> is the strongest endorsement in the set and the hardest to withdraw from later.'],
         why='<strong>Assumes</strong> reports the claim and marks it as unexamined in the same word &mdash; which is a critique, not a '
             'discourtesy. The other three all sign it. That choice is made once per sentence and it is not a matter of style.',
         bg=BG_TYPE),

    dict(stem='A board paper reads: <em>the elimination of interaction-dense roles is now under way.</em> What has the nominalisation cost?',
         options=['It states the scale of the change but not the timing that was agreed',
                  'It states the decision but not the cost that has been attached to it',
                  'It states the change but not who decided on it',
                  'It states the outcome but not the evidence that was put behind it'],
         correct=2,
         explains=['The timing is in fact there &mdash; <em>now under way</em>. What is missing is a person, not a date.',
                   'Cost is not what a nominalisation removes. Turning a verb into a noun removes its subject.',
                   None,
                   'Evidence is missing from most board papers. This sentence has a more specific hole in it than that.'],
         why='<em>Eliminate</em> needs somebody to do the eliminating; <em>the elimination</em> does not. That is exactly why the noun '
             'is chosen, and it is the same tell as the evasive passive: ask whether a reader could put a name to the sentence.',
         bg=BG_BAR),

    dict(stem='Independent judges rated each story higher, yet the stories resembled one another more. Which verb describes that, exactly?',
         options=['The stories had eroded, because the range was worn away at its edges.',
                  'The stories had converged, because they had become more alike.',
                  'The stories had attenuated, because the signal in them had weakened.',
                  'The stories had collapsed, because the structure of them had gone.'],
         correct=1,
         explains=['<strong>Erode</strong> takes a surface or an institution and removes material from it. Nothing here was removed.',
                   None,
                   '<strong>Attenuate</strong> weakens a signal or an effect. These stories were rated as stronger, not weaker.',
                   '<strong>Collapse</strong> is total and sudden. It is the end of the scale, and the finding is at the start of it.'],
         why='<strong>Converge</strong> is the only one of the seven that means <em>become similar</em>. The finding is precisely that '
             'quality went up while variety went down &mdash; individual gain, collective loss &mdash; and no verb of loss or weakening says that.',
         bg=BG_NIGHT),

    dict(stem='Which opening concedes the strongest version of the other side before it turns?',
         options=['Of course there is something in the scaling argument, up to a point, and nobody would deny it outright.',
                  'Scaling has its defenders, and no doubt they have their reasons, though the reasons are rarely given.',
                  'People keep saying that scaling is the only thing that matters, which is obviously far too simple a view.',
                  'Scaling matters, architecture matters and compute matters. But none of it delivers if the substrate thins.'],
         correct=3,
         explains=['<em>Up to a point</em> takes back most of what the concession appeared to give, and a reader hears it.',
                   'The subordinate clause turns the concession into an accusation before any evidence has arrived.',
                   'This restates the other side in a form nobody holds, which is the definition of a straw man.',
                   None],
         why='A concession is worth making only at full strength and in the other side&rsquo;s own vocabulary &mdash; three things named, no '
             'qualifier smuggled in. Then <strong>one</strong> pivot. Concede weakly and the pivot has nothing to push against.',
         bg=BG_WATCH),

    dict(stem='The essay calls AI&rsquo;s capability an <em>inheritance</em>. Which sentence keeps that metaphor doing work?',
         options=['Inheritances, if they are consumed without reinvestment, eventually run out.',
                  'Inheritances, if they are not properly leveraged, will fail to scale upward.',
                  'Inheritances, if they are left unmonitored, will drift out of alignment.',
                  'Inheritances, if they are not maintained, gradually corrode from within.'],
         correct=0,
         explains=[None,
                   '<em>Leverage</em> and <em>scale</em> come from finance and engineering. Two frames in one sentence, and the reader feels the seam.',
                   '<em>Drift out of alignment</em> is machinery, or else AI safety. An estate does not have an alignment.',
                   '<em>Corrode</em> belongs to metal. Money is spent, not rusted, and the mixed image costs the sentence its force.'],
         why='An extended metaphor has to stay inside one frame. The estate frame gives you <em>consume</em>, <em>reinvest</em>, '
             '<em>run out</em>, <em>squander</em> &mdash; and each of those is a claim about AI you could dispute. Reach outside the frame and '
             'the metaphor stops arguing and starts decorating.',
         bg=BG_BAR),

    dict(stem='Put into the formal inverted form: <em>If the substrate were to thin any further, the frontier would stall.</em>',
         options=['Would the substrate thin any further, the frontier would then be stalling.',
                  'If the substrate would thin any further, the frontier would stall as well.',
                  'Were the substrate to thin any further, the frontier would stall.',
                  'Had the substrate thinned any further, the frontier would have stalled.'],
         correct=2,
         explains=['English inverts <em>were</em>, <em>had</em> and <em>should</em> in conditionals. It does not invert <em>would</em>.',
                   '<em>If &hellip; would</em> in the same clause is the commonest conditional error there is, at every level.',
                   None,
                   'That is the third conditional. It moves the whole claim into a past that did not happen.'],
         why='<strong>Were &hellip; to</strong> is the inversion of the second conditional and it front-loads the condition, which is why formal '
             'argument likes it. Only three words invert: <em>were</em>, <em>had</em> and <em>should</em>.',
         bg=BG_NIGHT),

    dict(stem='Each model in the chain is smarter than the last. Which sentence assigns the cause the way the essay does?',
         options=['The models improve because each generation is trained on a far larger corpus of raw text.',
                  'The models improve because the architecture is refined between one epoch and the next one.',
                  'The models improve because a great deal more compute is thrown at each training run.',
                  'The models improve not because the architecture changed but because the civilization did.'],
         correct=3,
         explains=['The thought experiment holds the corpus size argument still: it is the same architecture reading a different world.',
                   'This is the reading the essay is written against. The architecture is explicitly unchanged along the chain.',
                   'Compute is one of the three things conceded in the pivot, and conceding it is not the same as crediting it.',
                   None],
         why='<strong>Not because X but because Y</strong> concedes the observation and reassigns its cause. It is the hardest move to answer, '
             'because your opponent already agrees with you about what happened and now has to argue about why.',
         bg=BG_WATCH),

    dict(stem='You want to say, politely and precisely, that a paper never asked a question it should have. Which line does that?',
         options=['The paper is unfortunately rather silent on the social origins of the data it scales.',
                  'The paper declines to examine the social origins of the data it scales.',
                  'The paper appears to have entirely overlooked the social origins of the data it scales.',
                  'The paper says almost nothing at all about the social origins of the data it scales.'],
         correct=1,
         explains=['<em>Silent on</em> suggests the authors had nothing to say. Your claim is that they had, and did not.',
                   None,
                   '<em>Overlooked</em> imputes carelessness. That is an accusation about the authors rather than about the argument.',
                   '<em>Says almost nothing</em> measures quantity. A paper can say a great deal and still never ask the question.'],
         why='<strong>Declines to examine</strong> says the writer could have looked and chose not to. It is the sharpest of the four and the '
             'easiest to defend, because it describes the shape of the argument instead of the state of mind of its author.',
         bg=BG_TYPE),
]

# The phrases the activation stage expects to hear. Target language, so they
# stay in English in all three switcher languages.
CHIPS = ['thin &middot; narrow &middot; converge', 'cognitive offloading',
         'X declines to examine Y', 'not because &hellip; but because &hellip;',
         'were it to &hellip;', 'yes, X matters &mdash; but &hellip;',
         'a tragedy of the commons', 'consumed without reinvestment']

SPEAK = [
    'You chair the operating committee. Argue against a 30% cut to entry-level hiring on the pipeline, not on sentiment.',
    'Take the other side: the tacit-knowledge argument is what every incumbent says to protect headcount.',
    'Report Doshi and Hauser&rsquo;s finding in three sentences, without signing any of it.',
    'Your CTO calls the substrate argument unfalsifiable. Concede the strongest version of that, then pivot once.',
]


def build():
    D.assert_no_key_is_longest(QUESTIONS, 'SocialEdge')
    for g in GAPS:
        D.assert_bank_is_not_a_key(g['bank'], [r[1][0] for r in g['rows']])

    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'The <em>Social Edge</em>',
                'Reading an argument that runs against the consensus &mdash; and building one: nominalisation, stance, concession and the metaphors that carry a claim',
                [('Level', 'C2 &middot; Argument &amp; abstraction'),
                 ('Focus', 'Reporting, conceding, correcting the cause'),
                 ('Count', 'NSLIDES slides')])

        + "".join(D.teach(ek, e, tk, t, cards, folder=F, bg=bg)
                  for ek, e, tk, t, cards, bg in TEACH)

        + D.sort_slide(SORTS[0]['bins'], SORTS[0]['items'],
                       'sortEyebrow', 'Whose claim is it?',
                       SORTS[0]['title_key'], SORTS[0]['title'],
                       SORTS[0]['hint_key'], SORTS[0]['hint'], SORTS[0]['why'],
                       folder=F, bg=BG_NIGHT)

        + D.sort_slide(SORTS[1]['bins'], SORTS[1]['items'],
                       'sortEyebrow', 'Whose claim is it?',
                       SORTS[1]['title_key'], SORTS[1]['title'],
                       SORTS[1]['hint_key'], SORTS[1]['hint'], SORTS[1]['why'],
                       folder=F, bg=BG_BAR)

        + "".join(D.gap(i + 1, len(GAPS), g['rows'], g['bank'],
                        'gapEyebrow', 'Precision under pressure',
                        g['title_key'], g['title'],
                        hint=g['hint'], hint_key=g['hint_key'], why=g['why'],
                        width=g['width'], folder=F,
                        bg=(BG_TYPE if i == 0 else BG_WATCH))
                  for i, g in enumerate(GAPS))

        + D.match(MATCH, 'matEyebrow', 'The named things',
                  'matTitle', 'Match the term to what it actually names',
                  'matHint',
                  'Six coinages, six definitions. Every one of them is a whole finding compressed into a noun phrase &mdash; which is why they travel.',
                  'Each of these is nominalisation doing its job: a mechanism named once and then argued about by name. '
                  '<strong>Model collapse</strong> and <strong>knowledge collapse</strong> are deliberately built to rhyme with each other; '
                  '<strong>the Social Edge Paradox</strong> is the essay claiming its own term, which is how a framework gets cited.',
                  folder=F, bg=BG_BAR)

        + "".join(D.order(o['items'], 'ordEyebrow', 'Build the argument',
                          o['title_key'], o['title'],
                          o['hint_key'], o['hint'], o['why'],
                          folder=F, bg=(BG_NIGHT if i == 0 else BG_WATCH))
                  for i, o in enumerate(ORDERS))

        + "".join(D.mc(i + 1, len(QUESTIONS), q,
                       'qEyebrow', 'Choose the version that survives being quoted back',
                       'qTitle', 'Which one would you actually write?',
                       explains=q['explains'], folder=F, bg=q['bg'])
                  for i, q in enumerate(QUESTIONS))

        + D.results('resNext', 'Recognising the moves is the easy half. Now make one of these arguments out loud &rarr;',
                    folder=F, bg=BG_NIGHT)

        + D.activate('Now argue it', 'Use at least four:', CHIPS,
                     'Discussion &middot; in threes',
                     'Twelve minutes. One proposes the cut, one opposes it, one has to summarise both positions fairly at the end.',
                     SPEAK,
                     'Writing &middot; 180&ndash;220 words',
                     'Write the one-page note to your board opposing a 30% cut to entry-level roles. Concede the cost case in full before you turn; name the mechanism, not the mood; keep one metaphor inside its own frame; close with what you would measure in twelve months.',
                     'Yes, the cost case is sound. But&hellip;',
                     folder=F, bg=BG_BAR)
    )

    import i18n_socialedge as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'The Social Edge: Argument, Stance and Abstraction (C2)',
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
