# -*- coding: utf-8 -*-
"""Must & Have To — VfB Stuttgart (B1), rebuilt as a 16:9 deck.

    py lesson-template/build/build_vfb_musthaveto.py      (python3 on Linux)

`must-have-to-vfb-stuttgart.html` was a hand-built scrolling page in its own
CSS (Barlow Condensed, Crimson Pro, Share Tech Mono; an Arial-set logo), with
Spanish glossed inline and no language switcher. Same content, same URL,
brought up to house style. EN + DE + ES.

**What was broken in the old page, and is fixed here**

- **The results panel could never open.** `TOTAL = 19`, but the page has 18
  scored items (6 + 5 + 3 + 4). `showScore()` fired at `answered >= TOTAL`,
  which never happened. The hero chip also said "19 Questions".
- **Exercise 1's Check button marked Exercise 4.** `checkFill()` selected
  every `input.fi[data-answer]` on the page, which includes the four
  error-correction boxes, so it scored them blank, locked them, and
  `checkErrors()` then skipped them as already checked. Exercise 4 could not
  be answered by anyone who did Exercise 1 first.
- **The apostrophe normalisation was a no-op** (`replace(/'/g,"'")`, straight
  to straight), so `mustn’t` typed on a phone keyboard scored wrong, and each
  gap took exactly one spelling: `must not` for `mustn't` scored wrong too.
  The engine flattens curly quotes; every gap lists its accepted forms.
- **The answer was printed on the options.** Every multiple-choice key
  carried an emoji its distractors did not (🚫 ✅ 📋 💪), and Q5 labelled
  its three options ❌ ❌ ✅. Two keys were also the longest option.
- **Four items marked correct English wrong** — defect 6 of the recurring
  pattern. In positive present sentences MUST and HAVE TO overlap, and the
  old page scored the "internal vs external" tendency as if it were a rule:
    * gap 2, *"We ___ press from the first minute"*, accepted only
      `have to`; *We must press* is equally good English. Now third person
      (*our striker ___ press*), which tests HAS TO, and accepts MUST too.
    * gap 4, *"I ___ score in the next game. I feel it"*, accepted only
      `must`. Now accepts `have to` as well, and the explanation says why
      MUST is the more natural choice rather than the only one.
    * MC 3 asked which fits a rulebook that *"says all clubs must
      register players"* and marked *"VfB must register…"* wrong — the stem
      itself used MUST for the rule. Replaced by a question-form item on the
      same transfer deadline: DOES + SUBJECT + HAVE TO, which has one answer.
    * MC 4 marked *"He feels VfB have to win the title"* wrong. Now asks
      why the coach says MUST, with distractors that are wrong for hard
      reasons (forbidden = MUSTN'T, optional = DON'T HAVE TO, past = HAD TO).
- **Gap 5 had two defensible answers.** *"The top scorer ___ play in the cup
  game — the coach will rest him"*: a player the coach is resting is not
  allowed to play, so MUSTN'T is arguable. Now *"It's only a friendly … he
  can rest if his legs are tired"*, which leaves only DOESN'T HAVE TO.
- **Rules were taught only in the feedback** (defect 4): no -S on MUST, no
  TO after it, DO / DOES in HAVE TO questions and DIDN'T + HAVE were all
  tested (MC 5, the builder, errors 1–2) and never taught. They are the third
  teaching slide now.
- **The word builder lost its point in conversion — so the engine grew
  decoys.** The old builder dealt a spare word or two (*have, can / must /
  must, has*), and choosing between them was the exercise. The template's
  order slide had no spare pieces, so it now takes optional `data-decoys`
  (lesson-template.html, deck.order). Each decoy is wrong in every position:
  *has to* beside *Does | the captain | have to* rather than *must*, because
  *Must the captain take the penalty?* is correct English and the engine
  would mark it wrong. A build that uses a decoy is marked when Check is
  pressed even if it is short: *VfB | had to | play | extra time.* is four
  pieces of five, and before the engine learned this, Check did nothing for
  exactly the learner who fell into the trap.

**Content decisions**

- **No quotes put in real people's mouths.** The old page had Sebastian
  Hoeneß and Deniz Undav saying things they never said, on a paid page, and
  "Season 2024/25" was already out of date. They are *the coach* and *our
  striker* now; the club stays. The Cannstatter Kurve and the MHPArena were
  only in the old page's correct-answer toasts, which the engine does not
  have.
- **E3's "because of Cannstatter Volksfest"** asserted a fixture fact about
  the club that nobody here could vouch for, in front of learners who live
  next to the Wasen. Dropped; the sentence tests the tense and needs no
  reason.
- **The cheat sheet and the danger box are folded into the three teaching
  slides**, which carry every row of both: the four forms, "the Stuttgart
  test" (MUSTN'T leave the pitch / DON'T HAVE TO leave it at half-time), the
  golden rule, and "MUST has no past". A recap after the questions would
  have repeated them word for word.
- **MUST's second meaning** (deduction — the old card's "Undav must be the
  most clinical striker") is kept as a note on the MUST card, flagged as a
  conclusion rather than an obligation. It is not tested; nor was it before.
- The per-item hints (*"Hint: It is forbidden by the rules 🚫
  (prohibición)"*) named the answer's category before the learner read the
  sentence. The sentence already carries that meaning; the hint's content is
  in each item's explanation, which now translates. Exercise 4's hints did
  more than that — *"Type the correct past form"* is what ruled out
  *played* — so its instruction names the forms instead ("using the right
  form of MUST or HAVE TO"), and E3's box covers *must* alone, so *played*
  cannot fit it.

**Adversarial review, 2026-09-25** (four reviewers, one skeptic each; what
survived):

- Correct English that was marked wrong: *need to* in E2, *needed to* in
  E3, *mustn't* in gap 2 (the rewrite had lost the old clause that pinned the
  positive; "we need an early goal" does that now). NEED forms and *have got
  to* are accepted wherever they fit.
- Tells: MC3's key was the only longest option by one letter (*have* vs
  *has*); MC1's key was the only option not starting "Players"; MC4's key
  said "nobody is ordering him", which is the soft internal/external
  tendency stated as fact.
- The third teaching slide printed two build-it answers word for word
  (`check-teach-leak.js` agreed); its examples are new sentences now. "MUST
  never takes DO" was tested (MC3, E2) and taught only in feedback; it is on
  the MUST card.
- Gap 1 said *players* may not handle the ball; goalkeepers may, in their
  own area. *Outfield players*.
- The activation dropped its own role-play on prompt 3, gave the new signing
  nothing to say, and never required a HAVE TO question. Rewritten so each
  prompt requires a form: MUSTN'T, DO I HAVE TO…?, DON'T HAVE TO, HAD TO.
- The results message printed `&mdash;` literally: the template wrote
  #scoreMsg with textContent. Fixed in the template (innerHTML), with a
  gate — see HANDOFF for the fifteen other decks that still carry it.
- Refuted, left alone: the subs warm-up item (it names no moment in play,
  and "if you prefer" rules out MUSTN'T); quoting "he, she and it" (the house
  reference builder does not).

**Artwork.** Ten of fourteen Midjourney renders Innes dropped in
`incoming/` on 2026-09-25 — two prompts, "Stuttgart football minimalist
vector illustration" (16:9) and "VfB Stuttgart Noma Bar style" (2.34:1, so
they crop at the sides; every one used here keeps its subject inside the
crop). One picture per section, per HOUSE-STYLE §5c:

    hero     ball on the pitch under a low sun     cover, library card
    strike   striker mid-volley                    teach 1 · two ways to say it
    corner   corner flag and floodlight            teach 2 · the negative trap
    sprint   runner through a diagonal of light    teach 3 · the forms
    dusk     player walking the ball out at dusk   activity 1 · gap fill
    legs     Noma Bar legs and ball, red on red    activity 2 · choose
    dribble  Noma Bar dribble                      activity 3 · build it
    boots    boots and ball, close                 activity 4 · the mistakes
    arena    Noma Bar stadium                      results
    stadium  ground, crowd and trees               activation

The four not used (two near-duplicate dribblers, a runner cut off by the
crop, a close-up of boots) and one rejected after a look at the rendered deck
are in `incoming/_previous/vfb-stuttgart/`. The reject was the Noma Bar kick:
its goalpost sits at 88% of the source width, exactly where the 16:9 crop
falls, so every multiple-choice slide showed a white strip down its right
edge that read as a rendering fault. `vfb-stuttgart/player-dribble.jpg`,
the old page's only picture, was referenced by nothing after the
rebuild and is removed from the tree (it stays in history).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import deck as D

ROOT = os.path.dirname(os.path.dirname(HERE))
TPL = os.path.join(ROOT, 'lesson-template', 'lesson-template.html')
OUT = os.path.join(ROOT, 'must-have-to-vfb-stuttgart.html')
F = 'vfb-stuttgart'

# py lesson-template/extract-palette.py vfb-stuttgart/hero.jpg --light
# Every row PASS (text on surface 12.12, accent on surface 4.66). The light
# theme because the hero is a bright coral sky, and because the derivation
# lands the accent on #b81000 — the club's own red, out of its own picture.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #d8c5ac;
  --surface       : #e1d5c4;
  --surface2      : #dccdb8;
  --border        : #96514a;
  --text          : #2a1311;
  --text-dim      : #5e322e;
  --accent        : #b81000;
  --accent-bright : #850b00;
  --accent-dim    : #f15142;
  --secondary     : #1d3b49;
  --contrast      : #075536;''' % F

# The seven forms the old page's Exercise 1 offered, grouped positives then
# negatives. Not alphabetical: that order lists slide 2's answers in gap
# order, which is what assert_bank_is_not_a_key exists to refuse.
BANK = ['must', 'had to', 'has to', 'have to', "mustn't", "don't have to",
        "doesn't have to"]

# Accepted spellings. The engine flattens curly apostrophes and case; every
# genuinely right answer is listed, so a learner is never marked wrong for
# correct English (HOUSE-STYLE §7).
NO_NEED = "don't have to|do not have to|needn't|need not|don't need to|do not need to"
NO_NEED_3 = ("doesn't have to|does not have to|needn't|need not|doesn't need to"
             "|does not need to")
BANNED = ("mustn't|must not|can't|cannot|can not|aren't allowed to"
          "|are not allowed to")

GAPS = [
    ("Outfield players ______ handle the ball deliberately &mdash; it&rsquo;s "
     "strictly against the Laws of the Game.",
     [BANNED], 'g1why'),
    ("The coach&rsquo;s orders are clear: our striker ______ press the "
     "goalkeeper from the first minute &mdash; we need an early goal.",
     ['has to|must|has got to|needs to'], 'g2why'),
    ("The club told the unused subs: &lsquo;You ______ warm up on the pitch "
     "&mdash; use the tunnel if you prefer.&rsquo;",
     [NO_NEED], 'g3why'),
    ("After the defeat, our striker said: &lsquo;I ______ score in the next "
     "game. I can feel it &mdash; the fans deserve it.&rsquo;",
     ['must|have to|have got to|need to'], 'g4why'),
    ("It&rsquo;s only a friendly, so our top scorer ______ play &mdash; he can "
     "rest if his legs are tired.",
     [NO_NEED_3], 'g5why'),
    ("Last season, VfB ______ play three matches in six days because of "
     "postponed fixtures.",
     ['had to|needed to'], 'g6why'),
]

# ctx / stem split per deck.mc(): the situation or the question translates,
# the English under test does not.
MC = [
    dict(ctx='What does this sentence mean?', ctx_key='mcMean',
         stem='&ldquo;VfB players <strong>mustn&rsquo;t</strong> wear jewellery '
              'during a match.&rdquo;',
         options=["Players don't need to wear jewellery during a match.",
                  "Players probably won't wear any jewellery in a match.",
                  "Players aren't allowed to wear jewellery in a match.",
                  "Players can decide for themselves about jewellery."],
         correct=2, why='mc1why'),
    dict(ctx='What does this sentence mean?', ctx_key='mcMean',
         stem='&ldquo;The reserve goalkeeper <strong>doesn&rsquo;t have '
              'to</strong> play tonight.&rdquo;',
         options=["He isn't allowed to play tonight, so he won't.",
                  "He isn't required to play tonight, but he might.",
                  "He definitely won't be playing in tonight's game.",
                  "He has been told he must stay on the bench tonight."],
         correct=1, why='mc2why'),
    dict(ctx='The transfer window closes on Friday. Which question is correct?',
         ctx_key='mc3ctx', stem='',
         options=["Does the club must register players by Friday?",
                  "Does the club has to register players by Friday?",
                  "Does the club have to registers players by Friday?",
                  "Does the club have to register players by Friday?"],
         correct=3, why='mc3why'),
    dict(ctx='Why does the coach say MUST here?', ctx_key='mc4ctx',
         stem='&ldquo;We <strong>must</strong> win the title this season '
              '&mdash; I really believe it.&rdquo;',
         options=["It comes from him — it's how he personally feels.",
                  "It's forbidden, so he's warning the players not to.",
                  "It's about last season, when they nearly won it.",
                  "It's optional — they can win it if they want to."],
         correct=0, why='mc4why'),
    dict(ctx='Which sentence is correct English?', ctx_key='mc5ctx', stem='',
         options=['The striker musts score more goals.',
                  'The striker must to score more goals.',
                  'The striker must score more goals.',
                  'The striker must scores more goals.'],
         correct=2, why='mc5why'),
]

# (chunks in answer order, decoys, hint key, why key). Each decoy is wrong
# wherever it goes — see deck.order. The hint holds the meaning as an English
# paraphrase inside a translated frame, so the learner still works from
# English to English.
ORDER = [
    (['VfB players', "mustn't", 'foul', 'inside the box.'], ["don't have to"],
     'o1hint', 'o1why'),
    (['Does', 'the captain', 'have to', 'take', 'the penalty?'], ['has to'],
     'o2hint', 'o2why'),
    (['VfB', "didn't", 'have to', 'play', 'extra time.'], ['had to'],
     'o3hint', 'o3why'),
]

# Error correction as gap rows: the wrong sentence, then the same sentence
# with a box where the mistake was. "Change as little as you can" is the
# criterion, so a rewrite with CAN'T is not a correction of MUST NOT TO.
FIX = [
    ("&#10007; VfB players <strong>must not to enter</strong> the referee&rsquo;s "
     "dressing room at half-time.<br>"
     "&#10003; VfB players ______ the referee&rsquo;s dressing room at half-time.",
     ["must not enter|mustn't enter"], 'e1why'),
    ("&#10007; Does the new signing <strong>musts</strong> attend the "
     "pre-season press conference?<br>"
     "&#10003; Does the new signing ______ attend the pre-season press "
     "conference?",
     ['have to|need to'], 'e2why'),
    ("&#10007; Last month, Stuttgart <strong>must</strong> play four away "
     "games in a row.<br>"
     "&#10003; Last month, Stuttgart ______ play four away games in a row.",
     ['had to|needed to'], 'e3why'),
    ("&#10007; The veteran player <strong>mustn&rsquo;t</strong> retire &mdash; "
     "it&rsquo;s his own decision and nobody is forcing him.<br>"
     "&#10003; The veteran player ______ retire &mdash; it&rsquo;s his own "
     "decision and nobody is forcing him.",
     [NO_NEED_3], 'e4why'),
]

CHIPS = ['must', "mustn't", 'have to', 'has to', "don't have to",
         "doesn't have to", 'had to', "didn't have to"]


def build(count_chip):
    D.assert_no_key_is_longest(MC, 'VfB MC')
    for n in range(0, len(GAPS), 2):
        D.assert_bank_is_not_a_key(BANK, [a[0] for _, a, _ in GAPS[n:n + 2]])
    logo = D.logo_from(TPL)
    import i18n_vfb_musthaveto as I
    en = I.T['en']

    def teach(prefix, bg):
        # Six-item cards: the rule travels with its heading into DE and ES,
        # while the English examples inside it stay English (§8).
        cards = [('%s%dh' % (prefix, n), en['%s%dh' % (prefix, n)],
                  '%s%db' % (prefix, n), en['%s%db' % (prefix, n)],
                  '%s%dn' % (prefix, n), en['%s%dn' % (prefix, n)])
                 for n in (1, 2)]
        return D.teach(prefix + 'Eyebrow', en[prefix + 'Eyebrow'],
                       prefix + 'Title', en[prefix + 'Title'], cards,
                       folder=F, bg=bg)

    slides = (
        D.cover(logo, en['coverTitle'], en['coverSub'],
                [('Level', en['chipLevel']), ('Focus', en['chipFocus']),
                 ('Count', count_chip)])

        + teach('ta', 'strike.jpg')
        + teach('tb', 'corner.jpg')
        + teach('tc', 'sprint.jpg')

        + "".join(D.gap(n + 1, 3, GAPS[2 * n:2 * n + 2], BANK,
                        'gapEyebrow', en['gapEyebrow'], 'gapTitle', en['gapTitle'],
                        folder=F, bg='dusk.jpg', hint_key='gapHint',
                        hint=en['gapHint'], width=175, size=19)
                  for n in range(3))

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow', en['mcEyebrow'],
                       'mcTitle', en['mcTitle'], folder=F, bg='legs.jpg',
                       ctx=q['ctx'], ctx_key=q['ctx_key'])
                  for i, q in enumerate(MC))

        + "".join(D.order(items, 'ordEyebrow', en['ordEyebrow'] + ' &middot; %d / 3' % (i + 1),
                          'ordTitle', en['ordTitle'], hk, en[hk], why,
                          folder=F, bg='dribble.jpg', decoys=decoys)
                  for i, (items, decoys, hk, why) in enumerate(ORDER))

        + "".join(D.gap(n + 1, 2, FIX[2 * n:2 * n + 2], None,
                        'fixEyebrow', en['fixEyebrow'], 'fixTitle', en['fixTitle'],
                        folder=F, bg='boots.jpg', hint_key='fixHint',
                        hint=en['fixHint'], width=175, size=18)
                  for n in range(2))

        + D.results('resNext', en['resNext'], folder=F, bg='arena.jpg')

        + D.activate(en['actTitle'], en['actUse'], CHIPS,
                     en['actSpeakKind'], en['actSpeakBrief'],
                     [en['actSpeak%d' % n] for n in range(1, 4)],
                     en['actWriteKind'], en['actWriteBrief'],
                     en['actPlaceholder'], folder=F, bg='stadium.jpg')
    )

    # mc() only puts a stem in the markup; an empty one would leave a blank
    # 25px line under the question, so drop it where the ctx IS the question.
    slides = slides.replace('        <p class="q-stem"></p>\n', '')

    # D.order puts its hint in .order-hint, the mono uppercase label meant for
    # "click the parts in order". Here the hint is the item itself — an
    # English paraphrase to rebuild — and in capitals it both shouts and
    # erases the CAPS that mark the forms. So it becomes the slide's context
    # line, and the generic instruction goes back underneath as the label.
    for i in range(1, 4):
        k = 'o%dhint' % i
        a = '<p class="order-hint" data-i18n="%s">%s</p>' % (k, en[k])
        assert a in slides, k
        slides = slides.replace(a,
            '<p class="q-ctx" style="margin-bottom:14px" data-i18n="%s">%s</p>\n'
            '        <p class="order-hint" data-i18n="orderHint">%s</p>'
            % (k, en[k], en['orderHint']), 1)

    # The order eyebrow was built with its counter inside the English text,
    # which would translate away. Put the counter outside the key, as mc()
    # and gap() do.
    for i in range(3):
        slides = slides.replace(
            '<div class="eyebrow" data-i18n="ordEyebrow">%s &middot; %d / 3</div>'
            % (en['ordEyebrow'], i + 1),
            '<div class="eyebrow"><span data-i18n="ordEyebrow">%s</span> '
            '&middot; %d / 3</div>' % (en['ordEyebrow'], i + 1), 1)

    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Must &amp; Have To — VfB Stuttgart (B1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    return s


if __name__ == '__main__':
    import i18n_vfb_musthaveto as I
    s = build(I.T['en']['chipCount'])
    n = s.count('<section class="slide') - 1   # the template's own marker is the +1
    print('wrote %s — %d slides, %d gaps, %d MC, %d order, %d fixes, %d bytes'
          % (os.path.basename(OUT), n, len(GAPS), len(MC), len(ORDER), len(FIX), len(s)))
