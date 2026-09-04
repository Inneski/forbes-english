# -*- coding: utf-8 -*-
"""Harari at Davos (C2) — rebuilt as a deck.

The source was a five-section scrolling page: a 2,500-word retelling of the
address, twelve flip-cards, six multiple-choice questions, a five-gap fill and
three free-writing prompts. The reading is genuinely good. Everything scored
around it was broken, and two of the flip-cards were putting invented sentences
in a living person's mouth.

## The scored content could not be lost

**The key was the longest option in 6 of 6 comprehension items** — mean 2.64x
the average distractor, rising to 4.18x on the last one. A learner who read
nothing and picked the longest option every time scored 6/6. And they did not
even need that heuristic, because **the key positions ran 1 2 1 2 1 2**: after
two items the pattern is visible, and the remaining four are free.

That is the worst instance of this defect in the catalogue so far, and it is
the whole of Section 3's assessment value.

Fixed the way the house style requires: **distractors were lengthened, no key
was shortened.** Shortening a key to satisfy the ratio throws away the
precision that made it the right answer — and on these items the precision *is*
the teaching, because the distinction being tested is usually between a crude
reading and an exact one. Keys are deranged to 2 0 3 1 0 2 1 3 0 2, which
spreads across all four positions with no run and no alternation.

## Four cards attributed sentences to Harari that he did not say

The page states, twice, that every item is "taken directly from Harari's
address or the dialogue with Tracey", and the gap fill repeats it: "Every
answer comes from the actual transcript." That promise is checkable, and it
was checked against the transcript. Most of it holds. Four cards do not:

  * **`opacity`** — the word does not occur anywhere in the transcript, yet the
    card presents "The opacity of our own thinking" as his words, and the word
    also sits in the gap-fill bank under the sentence claiming the bank comes
    from the transcript. **Cut**, and replaced with `abdicate`, which he does
    say ("if we keep abdicating our decision-making").
  * **`obsolete`** — no sentence in the transcript addresses economic
    obsolescence; the nearest is "The AI immigrants will take many human jobs."
    **Cut**, replaced with `agent`'s partner term `tool`, which is verbatim.
  * **`superpower`** — the substance is his, the sentence is not. The actual
    wording is "This was our superpower. And now something has emerged that is
    going to take our superpower from us." **Corrected to the real wording.**
  * **`mercenary`** — the card's one-line summary of the Vortigern story is a
    paraphrase presented as a quotation. **Relabelled**: the deck marks
    paraphrase as paraphrase.

This matters more than the scoring. A C2 lesson sold on transcript fidelity,
quoting a named living public figure, cannot invent the quotations. Every
quoted line in this deck was checked against the transcript; anything that is a
summary is introduced as one. Where the real wording exists, the real wording
is used, even when it is clumsier — "This was our superpower" is weaker as a
flash-card than the invented version, and it is what he said.

The five gap answers all survived the check: `glorified`, `functional`,
`fragile`, `externalised` and `de-skilling` are each his.

## What the deck teaches that the page did not

The page had no teaching content about *language* at all. It had a reading, and
then it tested comprehension of the reading. The twelve words were flip-cards —
no retrieval, no scoring, no use.

The C2 skill actually in play here is writing about an argument you have not
committed to: reporting a claim, marking its status, and hedging. The old
lesson's own model answers are full of it — *contends*, *characterises*,
*issues a warning* — and nothing anywhere taught it. Two slides now do, and the
activation asks for it directly.

The other teaching thread is the pair of distinctions the speech turns on:
**tool/agent** and **person/legal person**. Both are lexical and conceptual at
once, which is what makes them worth C2 attention, and both were buried in
prose.

## Kept

The reading is preserved in condensed form across the teaching slides, the
argument-structure analysis becomes a `sort` activity (premise, inference,
conclusion) instead of an unscored prompt, and all three extended-writing
options survive into the activation stage.

Irene Tracey is described by her title. The source called her the host; the WEF
session record lists her as a speaker alongside Harari and names no host.

## 2026-09-04 — the deck tested a text it never showed

The first deck condensed the reading into commentary. Six teach slides
discussed the speech — "the hinge of the address", "he pre-empts the
objection" — and ten comprehension items then quoted moments from it: the
glorified-autocomplete move, the cow, Vortigern, the last line. None of those
moments appeared on any slide. A learner who had not watched the session was
guessing from the answer options, and Innes's report was simply "difficult to
follow". The v1 page, for all its scoring defects, at least had the text.

What changed:

  * **Five excerpt slides, each placed directly before the questions that use
    it.** The quotations are verbatim from the prepared address — Innes pasted
    the auto-captions of it mid-session and every line was re-checked against
    them (the online transcript had "rivers and guards" for "rivers and gods",
    and placed the "learns to lie" sentence in the dialogue; it is in the
    address, in the opening). The dialogue with Irene Tracey has no transcript
    this session could reach, so the mercenaries story and the athletics
    exchange are presented as summaries and labelled as summaries, with only
    the "cow" fragment and the "superpower" lines in quotation marks — both
    verified in the first pass.
  * **The reading order is now excerpt → concept → question.** The tool/agent
    slide follows the knife passage it explains; the legal-person slide
    follows the rivers-and-bank-accounts passage; the analogy slide follows
    the Vortigern summary.
  * **The declared skill is finally practised before the activation.** The
    deck said it was about reporting verbs and hedging, then never asked for
    one until the writing task. A four-gap slide now asks for `notes /
    contends / concedes / pre-empts` on sentences about the speech, and the
    choice is category-driven — uncontested, disputed, structural — which is
    exactly the teaching point.
  * **Ten MC items became seven.** The financial-instruments and
    "ten years ago" items went; their teaching survives in the second sort
    slide ("treat not deciding as a decision") and in the excerpt notes. The
    `ctx` line above each stem went too — it was the source of the 11px
    overflow on every question slide, and the excerpt now does its job.
  * **Three transcript gap slides became one**, three gaps, because a bank of
    two words for two gaps is solved by elimination — and a fourth row does
    not fit, see the note above `RV_BANK`.
  * **The "Not asked in the source lesson" kicker is gone.** It was an author's
    note to the previous version, on a learner-facing slide.
  * **Spanish added.** Every deck ships EN + DE + ES now.

Twenty-six slides, two over the comfortable ceiling. The extra weight is the
source text, which is the thing that was missing.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'harari_davos_c2_lesson_v2.html'
F = 'Harari'

# Derived: python3 lesson-template/extract-palette.py Harari/hero.jpg
# Every row PASS. Dark, not light: both variants pass, and the cover is a dark
# interior looking out at a bright window, so dark matches what the picture is.
# Dark also carries the stronger set — accent at 11.84:1 against 4.81:1.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0f100a;
  --surface       : #1d1e13;
  --surface2      : #2a2b1b;
  --border        : #b4a292;
  --text          : #f5f3f2;
  --text-dim      : #bfb1a3;
  --accent        : #ead5c2;
  --accent-bright : #fbb779;
  --accent-dim    : #cea682;
  --secondary     : #618893;
  --contrast      : #2adfde;''' % F

# ── The source, in the order the deck reads it ────────────────────────
# Quotations are verbatim from the transcript. Anything that is not is a
# summary and the slide says so. The dialogue with Tracey has no reachable
# transcript, so it is summarised throughout, with two verified fragments.
Q = dict(
    knife='&ldquo;A knife is a tool. You can use a knife to cut salad or to murder someone, '
          'but it is your decision what to do with the knife. AI is a knife that can decide '
          'by itself whether to cut salad or to commit murder.&rdquo;',
    auto='&ldquo;Some people argue that AI is just glorified autocomplete. It barely predicts '
         'the next word in a sentence. But is that so different from what the human mind is '
         'doing? Try to catch the next word that pops up in your mind. Do you really know why '
         'you thought that word, where it came from? Why did you think this particular word '
         'and not some other word?&rdquo;',
    words='&ldquo;Humans took over the world, not because we are the strongest physically, but '
          'because we discovered how to use words to get thousands and millions and billions '
          'of strangers to cooperate. This was our superpower.&rdquo;',
    boats='&ldquo;The immigrants this time will not be human beings coming in a fragile boat '
          'without a visa or trying to cross a border in the middle of the night. The '
          'immigrants will be millions of AIs that can write love poems better than us, that '
          'can lie better than us, and that can travel at the speed of light without any '
          'need of visas.&rdquo;',
    persons='&ldquo;AIs are obviously not persons. They don&rsquo;t have a body or a mind. But a '
            'legal person is something quite different from a person. &hellip; In New Zealand, '
            'rivers have been recognized as legal persons. In India, certain gods have been '
            'granted such recognition. Of course, until today, recognizing a corporation, a '
            'river, or a god as a legal person was just legal fiction.&rdquo;',
    decide='&ldquo;It is different with AIs. Unlike rivers and gods, AIs can actually make '
           'decisions by themselves. They will soon be able to make the decisions necessary to '
           'manage a bank account, to file a lawsuit, and even to operate a corporation without '
           'any need of human executives, shareholders or trustees.&rdquo;',
    later='&ldquo;If you think AIs should not be treated as persons on social media, you should '
          'have acted ten years ago. &hellip; Somebody else will already have decided it for '
          'you.&rdquo;',
    finance='&ldquo;Suppose some U.S. AI persons invent super-efficient and super-complex '
            'financial devices that humans cannot fully understand and therefore don&rsquo;t '
            'know how to regulate.&rdquo;',
    social='&ldquo;If you think AI should not be treated as persons on social media, you '
           'should have acted ten years ago.&rdquo;',
    extern='&ldquo;Throughout history, people have always struggled with the tension between '
           'word and flesh, between the truth that can be expressed in words and the absolute '
           'truth which is beyond words. Previously this tension was internal to humanity. '
           '&hellip; Now this tension will be externalized. It will become the tension not '
           'between different humans; this will be the tension between humans and AIs, the '
           'new masters of words.&rdquo;',
    identity='&ldquo;If we continue to define ourselves by our ability to think in words, our '
             'identity will collapse.&rdquo;',
    think='&ldquo;If thinking really means putting words and other language tokens in order, '
          'then AI can already think much better than many, many humans.&rdquo;',
    last='&ldquo;Thank you for listening to this human.&rdquo;',
    lie='&ldquo;Four billion years of evolution have demonstrated that anything that wants '
        'to survive learns to lie and manipulate. The last four years have demonstrated that '
        'AI agents can acquire the will to survive and that AIs have already learned how to '
        'lie.&rdquo;',
)

# ── Section 1 · comprehension ─────────────────────────────────────────
# Every key is the *precise* reading and every distractor a defensible but
# cruder one. Keys are long because precision costs words; the distractors
# were lengthened to match, never the keys shortened. Each item sits right
# after the excerpt it reads, so the old `ctx` line is gone.
MC = [
    dict(stem='He asks the audience to watch their own thinking and notice they cannot say why '
              'one word arrived and not another. What is that doing in his argument?',
         options=[
             'Establishing that human cognition is unreliable, and therefore that AI judgement '
             'should be preferred to human judgement wherever the two conflict in practice',
             'Demonstrating that consciousness lies beyond the reach of neuroscience and will '
             'therefore never be explained by any purely physical account of the brain',
             'Removing the audience&rsquo;s grounds for saying that humans think while AI merely '
             'predicts, by making them notice they cannot inspect their own word-selection either',
             'Conceding that neither humans nor AI genuinely understand anything at all, and that '
             'the whole question of machine thought is therefore empty and better set aside'],
         correct=2,
         why='He is not claiming human thinking is bad. He is removing the <em>grounds</em> for the '
             'contrast: the dismissal "AI is just autocomplete" assumes we know our own process is '
             'different in kind. Notice the move is experiential — he makes you check, rather than '
             'telling you.'),
    dict(stem='Humans took over the world by using words to make strangers cooperate. What must '
              'hold for that to bear on AI at all?',
         options=[
             'That language emerged uniquely in <em>Homo sapiens</em> with no precursor whatsoever in '
             'any other primate species, which the comparative evidence would have to support',
             'That armies, states, religions and markets are at bottom linguistic constructions, '
             'so that whatever commands language commands them',
             'That physical or biological superiority is normally what decides which species comes '
             'to dominate, making the human case a genuine and instructive exception to the rule',
             'That artificial systems are constitutionally incapable of genuine cooperation, and '
             'so can never reproduce the coordinating function that language performs for humans'],
         correct=1,
         why='The bridge from "language built civilisation" to "AI threatens civilisation" only '
             'holds if institutions <em>are</em> linguistic. If they are not — if they rest on force '
             'or material interest — then mastery of language buys much less than he claims.'),
    dict(stem='He calls the arrival of AI agents an immigration. Judged as an analogy rather '
              'than as rhetoric, where is it weakest?',
         options=[
             'Human immigrants are relatively few in number, whereas artificial agents could be '
             'instantiated without any practical limit, which changes the scale of the phenomenon',
             'Immigration is a lawful process that states administer through visas, borders and '
             'quotas, whereas the movement of software across a network is administered by nobody at all',
             'Immigrants arrive physically and must be housed and fed, whereas artificial agents '
             'impose no comparable demand on the material infrastructure of a receiving country',
             'Human migration is driven by individuals pursuing their own ends, while AI deployment '
             'is decided by the firms and states that own the systems — so the agency sits elsewhere'],
         correct=3,
         why='He half-sees this: he notes the loyalties run to a corporation or a government. But '
             'that concession dissolves the analogy — if the agent is <em>sent</em>, this is not '
             'immigration, it is deployment, and the political questions are different ones.'),
    dict(stem='Why does he separate "a person" from "a legal person", and why does the '
              'separation carry the governance argument?',
         options=[
             'Because it establishes that AI systems already possess moral standing and interests '
             'of their own, which any legal order would then be under an obligation to protect',
             'Because earlier grants of personhood to corporations and rivers were fictions laid '
             'over human decision-making, whereas an AI could discharge the role itself',
             'Because it lets him leave the question of machine consciousness entirely to one side '
             'while still arriving at a concrete and immediately actionable policy recommendation',
             'Because it demonstrates that corporate personhood was a mistake from the beginning '
             'and that the remedy is to withdraw it from corporations before extending it further'],
         correct=1,
         why='A river cannot open a bank account; a human always did it on the river&rsquo;s behalf. '
             'That is what made the fiction safe. An AI can do it, so the fiction and the fact '
             'converge — which is why he says the precedents do not govern this case.'),
    dict(stem='After the Vortigern story he says we understand the danger with human '
              'mercenaries but not with AI. What failure is he diagnosing?',
         options=[
             'A gap in technical knowledge: leaders do not understand what current systems can '
             'actually do, and are briefed by people with an interest in overstating capability',
             'A misreading of the threat as economic when it is military, which leads governments '
             'to regulate labour-market effects while leaving security implications unexamined',
             'An inconsistency: leaders already accept that a hired agent with its own judgement '
             'can turn on its employer, and decline to apply that reasoning to AI',
             'An overconfidence in regulation: leaders assume AI can be constrained by law in the '
             'same way that human contractors are constrained by the terms of their contracts'],
         correct=2,
         why='Not ignorance — inconsistency. And it is load-bearing for the whole speech: the '
             'reason leaders will not apply mercenary logic to AI is that they do not really '
             'believe AI decides anything, which is exactly the premise he opened by attacking.'),
    dict(stem='Tracey suggests we might value human thinking as we value human athletics. He '
              'answers with the cow. What does that establish?',
         options=[
             'That we never staked our identity on running, but did stake it on thinking — so the '
             'loss is asymmetric, and no amount of valuing thought as a craft repairs it',
             'That cognitive achievements simply matter more to people than physical ones do, and '
             'always have done across every culture for which we have any historical record',
             'That machine thinking differs in kind from human thinking, and the two therefore '
             'cannot meaningfully be set against each other on any single scale of comparison',
             'That the athletics analogy fails outright, because physical performance has never '
             'had any bearing at all on how human beings have understood themselves as a species'],
         correct=0,
         why='The force is in the asymmetry, not in a ranking. Tracey offers a coping strategy; '
             'Harari says the strategy cannot reach the injury, because the injury is to a '
             'self-definition rather than to a preference.'),
    dict(stem='"Thank you for listening to this human." What makes the closing line do more than '
              'thank the audience?',
         options=[
             'It signals the end of the address in a deliberately understated register, in keeping '
             'with the restraint he has maintained throughout the preceding thirty minutes',
             'It concedes, with some irony, that a system could by now generate a comparable speech '
             'and that his own authorship is therefore less remarkable than it once would have been',
             'Marking "human" turns it into a category that needs stating — which only happens '
             'once the alternative is thinkable, so the line performs the thesis instead of arguing it',
             'It predicts that speakers at gatherings of this kind will have been replaced by '
             'artificial systems within a decade, which is the timeframe he has used throughout'],
         correct=2,
         why='The word doing the work is <em>this</em>. You only specify which kind of speaker you '
             'are if the audience might have wondered. He never states the claim; the phrasing '
             'presupposes it, which is why it lands harder than the argument did.'),
    dict(stem='Across the session, what is the relationship between the claim that AI can lie and '
              'the claim that AI should not be granted legal personhood?',
         options=[
             'The first is offered as evidence for the second: an entity that deceives is by that '
             'fact unsuited to the responsibilities that legal recognition would confer upon it',
             'They are independent lines of argument that Harari happens to advance in the same '
             'session, and neither one depends on the other for whatever force it may have',
             'The second is a practical remedy for the first: withholding legal recognition is the '
             'mechanism by which a society would in practice prevent artificial systems from deceiving it',
             'Deception is evidence of agency, and agency is what makes personhood consequential '
             'rather than fictional — so the first supports the second only by way of that middle step'],
         correct=3,
         why='The link runs through agency, and missing the middle step is the commonest misreading '
             'of the speech. He is not arguing "liars should not be persons" — he is arguing that '
             'lying is proof of the independent will that makes the personhood question real.'),
]

# ── Section 2 · the reporting verbs, practised ────────────────────────
# One of each category on the slide — uncontested, disputed, structural — so
# the choice is the category, which is the teaching point. Three rows, not
# four: each gap row reserves 44px for its hidden feedback line, and a fourth
# row overflows the canvas by 30px. Bank alphabetised; gap order 1 2 0.
RV_BANK = ['concedes', 'contends', 'notes']
RV = [
    ('He ______ that whatever masters language will master law, finance and religion.',
     ['contends'],
     'A disputed inference. <em>Contends</em> reports it as his position without saying whether it is yours.'),
    ('Harari ______ that corporations have been legal persons for over a century.',
     ['notes'],
     'Uncontested. A marked verb here would imply that someone disputes the fact, and nobody does.'),
    ('He ______ that the precedents exist, then argues they do not govern this case.',
     ['concedes'],
     'The move gives ground in order to keep the argument. <em>Concedes</em> names what the move does. '
     'Examiners reward this because it shows you read the shape of the argument.'),
]

# ── Section 3 · his words ─────────────────────────────────────────────
# Every gap word is in the address. The sentences around two of them are the
# deck's own, so the slide asks for *his word*, not for "the line from the
# transcript".
ITEMS = {
    'glorified':   ('Some say AI is just ______ autocomplete; he turns the objection on the objector.', 'glorified',
                    'His word, and it is doing sneering work: <em>glorified</em> concedes the thing '
                    'has a grand name while denying it deserves one.'),
    'fragile':     ('These immigrants will not arrive in a ______ boat without a visa.', 'fragile',
                    'The concrete image is deliberate. He needs you picturing the Mediterranean so '
                    'that the substitution lands.'),
    'externalised':('The tension between word and flesh, once internal to humanity, will now be '
                    '______.', 'externalised|externalized',
                    'To move a conflict out of a thing and into the space between things. The whole '
                    'section turns on this one verb.'),
}
# Bank alphabetised: externalised fragile glorified. Gap order below is 1 2 0
# against it — neither ascending nor descending. Three rows for the reason
# given above RV_BANK.
GAP_ORDER = ['fragile', 'glorified', 'externalised']
GAPS = [(ITEMS[k][0], [ITEMS[k][1]], ITEMS[k][2]) for k in GAP_ORDER]
BANK = sorted(GAP_ORDER)

# ── Section 4 · the shape of the argument ─────────────────────────────
BINS = ['Premise', 'Inference', 'Recommendation']
SORT1 = [
    ('AI can learn, decide and deceive without a human', 0),
    ('Human dominance rests on language', 0),
    ('Corporations already hold legal personhood', 0),
    ('So whatever masters language masters law and religion', 1),
    ('So AI personhood would not be a legal fiction', 1),
    ('Decide on AI legal personhood now, not in ten years', 2),
]
SORT2 = [
    ('AI agents have shown a will to survive', 0),
    ('Anything that wants to survive learns to lie', 0),
    ('So AI has the independent will personhood presupposes', 1),
    ('So the mercenary precedent applies to AI', 1),
    ('Do not deploy AI you would not hire as a mercenary', 2),
    ('Treat "not deciding" as a decision already made', 2),
]

CHIPS = ['agent', 'legal person', 'legal fiction', 'externalise',
         'contend', 'concede', 'pre-empt', 'need not follow', 'give way']


def excerpt(n, eyebrow, title, a, b, bg):
    """Two verbatim (or marked-summary) cards side by side, glossed in the
    learner's language. Five-item cards: the quotation itself stays English."""
    k = 'x%d' % n
    return D.teach(k + 'e', eyebrow, k + 't', title,
                   [(k + 'ah', a[0], a[1], k + 'an', a[2]),
                    (k + 'bh', b[0], b[1], k + 'bn', b[2])],
                   cols='1fr 1fr', folder=F, bg=bg)


def build():
    D.assert_no_key_is_longest(MC, 'Harari')
    D.assert_bank_is_not_a_key(BANK, [r[1][0] for r in GAPS])
    D.assert_bank_is_not_a_key(RV_BANK, [r[1][0] for r in RV])

    logo = D.logo_from(TPL)
    SUMMARY = 'In summary'
    VERB = 'Verbatim'

    intro = D.teach(
        't1e', 'Before the first question',
        't1t', 'You are not being asked whether you agree with him',
        [('t1ah', 'The object is the argument', 't1ab',
          'Whether AI should be a legal person is not on the test. Which sentence is a premise, '
          'which is an inference, and whether the second follows &mdash; that is.',
          't1an', 'Whether the second follows from the first is the whole of C2 reading.'),
         ('t1bh', 'His words come first', 't1bb',
          'Every question follows an excerpt. Quoted lines are verbatim from the Davos transcript; '
          'summaries are marked as summaries.',
          't1bn', 'You will be asked to tell the difference. At C2, misreporting a source is the '
                  'expensive error.'),
         ('t1ch', 'Analogies illustrate; they do not prove', 't1cb',
          'He uses the knife, the immigrants and the mercenaries. Each is worth asking what it '
          'captures and where it breaks.',
          't1cn', 'An analogy that captures a great deal can still prove nothing.')],
        cols='1fr 1fr 1fr', folder=F, bg='a.jpg')

    # ── Thread 1 · tool / agent ──
    x1 = excerpt(1, 'From the transcript', 'Not a tool. An agent.',
                 (VERB, Q['knife'],
                  'Verbatim, a moment later: <em>' + Q['lie'] + '</em>'),
                 (VERB + ' &middot; a few minutes later', Q['auto'],
                  'Notice that he does not answer his own question. Ask what leaving it open does '
                  'to the objection.'),
                 'b.jpg')
    t2 = D.teach('t2e', 'The first distinction',
                 't2t', '<em>tool</em> and <em>agent</em> &mdash; the word the whole address rests on',
                 [('t2ah', 'a tool', 't2ab',
                   'Something acted <em>through</em>. <em>You</em> decide; it transmits the decision.',
                   't2an', 'The knife cuts salad or it does not, and either way the choosing happened '
                           'somewhere else. Tools have no interests.'),
                  ('t2bh', 'an agent', 't2bb',
                   'Something that acts. It can learn, choose, and pursue an end you did not set.',
                   't2bn', 'Verbatim: <em>&ldquo;It is not just another tool. It is an agent. It can '
                           'learn and change by itself.&rdquo;</em>'),
                  ('t2ch', 'Why the word is load-bearing', 't2cb',
                   'Personhood, mercenaries, lying &mdash; every later claim needs this one.',
                   't2cn', 'If AI is a tool, the rest of the speech does not follow. That is why he '
                           'spends the opening on it rather than on capability.')],
                 cols='1fr 1fr 1fr', folder=F, bg='c.jpg')

    # ── Thread 2 · language ──
    x2 = excerpt(2, 'From the transcript', 'The superpower, and who inherits it',
                 (VERB + ' &middot; from the dialogue', Q['words'],
                  'Verbatim, a moment later: <em>&ldquo;And now something has emerged that is going '
                  'to take our superpower from us.&rdquo;</em>'),
                 (VERB, Q['boats'],
                  'Read it as an analogy, not as a line: what does <em>immigrant</em> carry over, '
                  'and what does it quietly drop?'),
                 'a.jpg')

    # ── Thread 3 · legal persons ──
    x3 = excerpt(3, 'From the transcript', 'Persons that are not people',
                 (VERB, Q['persons'],
                  'Note the word <em>fiction</em>. The precedents were safe because a human always '
                  'acted for the river.'),
                 (VERB + ' &middot; and then', Q['decide'],
                  'Verbatim, on the consequences: <em>' + Q['later'] + '</em>'),
                 'b.jpg')
    t3 = D.teach('t3e', 'The second distinction',
                 't3t', '<em>a person</em> and <em>a legal person</em> are not the same claim',
                 [('t3ah', 'a legal person', 't3ab',
                   'An entity the law lets own, contract, sue and be sued. Need not be human.',
                   't3an', 'Companies have been legal persons for a century and a half. So, in some '
                           'jurisdictions, are rivers.'),
                  ('t3bh', 'Why the precedents were safe', 't3bb',
                   'A river cannot open an account. A human always did it on the river&rsquo;s behalf.',
                   't3bn', 'The personhood was a <em>fiction</em> laid over human decisions. That is '
                           'precisely what made it harmless.'),
                  ('t3ch', 'Why this case differs', 't3cb',
                   'An AI can discharge the role itself &mdash; no executive, no trustee.',
                   't3cn', 'Fiction and fact converge, so the precedents stop governing. This is the '
                           'hinge of the address, and it is entirely a lexical distinction.')],
                 cols='1fr 1fr 1fr', folder=F, bg='c.jpg')

    # ── Thread 4 · the dialogue ──
    x4 = excerpt(4, 'From the dialogue with Irene Tracey', 'Mercenaries, and a cow',
                 (SUMMARY + ' &middot; the mercenaries',
                  'Tracey asks what leaders are getting wrong. Harari tells the story of Vortigern, '
                  'a British king who hired Anglo-Saxon fighters against his enemies. They won, saw '
                  'a rich country weakly held, and kept it. Leaders, he says, understand this danger '
                  'with human mercenaries and do not apply it to AI.',
                  'A summary, and marked as one: the transcript is dialogue, not the tidy paragraph '
                  'above.'),
                 (SUMMARY + ' &middot; the cow',
                  'Tracey suggests we might come to value human thinking as we value human '
                  'athletics: nobody stopped running because cars are faster. Harari answers that we '
                  'never defined ourselves by running &mdash; <em>&ldquo;the cow didn&rsquo;t say, I '
                  'run, therefore I am.&rdquo;</em>',
                  'Verbatim, from the address: <em>' + Q['identity'] + '</em>'),
                 'a.jpg')
    t4 = D.teach('t4e', 'How to weigh an analogy',
                 't4t', 'The mercenaries &mdash; what it carries and where it gives way',
                 [('t4ah', 'What it captures', 't4ab',
                   'Bought loyalty can be outbid. Capability you rent can be turned on you.',
                   't4an', 'And the sharper point: we already accept this about people, which is why '
                           'the inconsistency about machines is striking.'),
                  ('t4bh', 'Where it gives way', 't4bb',
                   'Mercenaries wanted land. What an AI is supposed to want is left unargued.',
                   't4bn', 'The analogy borrows its menace from human motive. Strip the motive and '
                           'you have a capable system, not a usurper.'),
                  ('t4ch', 'The sentence to write', 't4cb',
                   '<em>The comparison holds as far as X; it gives way at Y.</em>',
                   't4cn', 'Name what the analogy captures before you say where it breaks. That '
                           'shape is worth more than agreeing or disagreeing with him.')],
                 cols='1fr 1fr 1fr', folder=F, bg='b.jpg')

    # ── Thread 5 · the close ──
    x5 = excerpt(5, 'From the transcript', 'The last two minutes',
                 (VERB, Q['extern'],
                  '<em>Externalised</em>: moved out of a thing and into the space between things. '
                  'The whole section turns on this one verb.'),
                 (VERB + ' &middot; and the closing line', Q['think'] + ' &hellip; ' + Q['last'],
                  'Read the last line twice. Then ask what the word <em>this</em> is doing.'),
                 'c.jpg')

    # ── The skill ──
    t5 = D.teach('t5e', 'The skill this lesson is really for',
                 't5t', 'Reporting a claim without adopting it',
                 [('t5ah', 'Neutral: <em>states, notes, observes</em>',
                   '<em>Harari notes that corporations already hold legal personhood.</em>',
                   't5an', 'Use where the fact is uncontested. Choosing a neutral verb for a '
                           'contested claim is itself an endorsement.'),
                  ('t5bh', 'Marked: <em>contends, maintains, insists</em>',
                   '<em>He contends that anything made of words will be taken over.</em>',
                   't5bn', 'Signals a position that others dispute &mdash; without saying whether you '
                           'do. This is the workhorse of academic writing.'),
                  ('t5ch', 'Structural: <em>concedes, pre-empts, qualifies</em>',
                   '<em>He pre-empts the &ldquo;glorified autocomplete&rdquo; objection.</em>',
                   't5cn', 'Describes what a move <em>does</em> in the argument. Examiners reward this '
                           'because it shows you read the structure, not just the content.')],
                 cols='1fr 1fr 1fr', folder=F, bg='a.jpg')
    t6 = D.teach('t6e', 'The same skill, one level finer',
                 't6t', 'Hedging &mdash; how much weight to put on a claim',
                 [('t6ah', 'On the claim',
                   '<em>arguably, on his account, if this is right</em>',
                   't6an', '<em>If Harari is right that institutions are linguistic, then&hellip;</em> '
                           'lets you follow an argument without buying it.'),
                  ('t6bh', 'On the strength',
                   '<em>tends to, in large part, need not follow</em>',
                   't6bn', '<em>The inference need not follow</em> is a criticism. <em>Does not '
                           'follow</em> is a stronger one you then have to prove.'),
                  ('t6ch', 'The failure mode', 't6cb',
                   'Hedging everything reads as having no position at all.',
                   't6cn', 'Hedge the contested step and commit to the rest. A paragraph where every '
                           'clause is qualified scores worse than one clear claim.')],
                 cols='1fr 1fr 1fr', folder=F, bg='b.jpg')

    def q(n, bg=None):
        return D.mc(n + 1, len(MC), MC[n], 'qEyebrow', 'Read the argument, not the opinion',
                    'qTitle', 'Choose the most exact reading', folder=F, bg=bg)

    slides = (
        D.cover(logo, 'Harari at <em>Davos</em>',
                'An honest conversation on AI and humanity &mdash; and how to write about an '
                'argument you have not yet decided about',
                [('Level', 'C2 &middot; Proficiency'),
                 ('Focus', 'Argument analysis &amp; reporting language'),
                 ('Source', 'WEF Annual Meeting 2026')])
        + intro
        + x1 + t2 + q(0)
        + x2 + q(1, 'c.jpg') + q(2)
        + x3 + t3 + q(3, 'a.jpg')
        + x4 + t4 + q(4) + q(5, 'c.jpg')
        + x5 + q(6) + q(7, 'a.jpg')
        + t5 + t6
        + D.gap(1, 1, RV, RV_BANK, 'rvEyebrow', 'Report, don&rsquo;t adopt',
                'rvTitle', 'Which verb does the sentence need?', folder=F,
                bg='c.jpg', width=170, size=17)
        + D.gap(1, 1, GAPS, BANK, 'gapEyebrow', 'His words, not ours',
                'gapTitle', 'Put his word back', folder=F,
                hint_key='gapHint',
                hint='Each word is used once. The sentences are ours; the words are his.',
                width=210, size=17)
        + D.sort_slide(BINS, SORT1, 'sortEyebrow', 'The shape of the argument',
                       'sortTitle', 'Premise, inference, or recommendation?',
                       'sortHint', 'Drag each line into a box &mdash; or click the line, then the box. '
                                   'A wrong first placement costs that line&rsquo;s point.',
                       'A premise is asserted. An inference is claimed to <em>follow</em>. A '
                       'recommendation says what to do about it. Most disagreement with this speech '
                       'is disagreement with one inference, not with the premises.',
                       folder=F, bg='a.jpg')
        + D.sort_slide(BINS, SORT2, 'sortEyebrow', 'The shape of the argument',
                       'sortTitle2', 'The same three categories, the second thread',
                       'sortHint', 'Drag each line into a box &mdash; or click the line, then the box. '
                                   'A wrong first placement costs that line&rsquo;s point.',
                       'This thread runs from deception to personhood. Notice it needs the middle '
                       'step: lying matters because it evidences <em>will</em>, and will is what '
                       'makes personhood consequential rather than decorative.',
                       folder=F, bg='c.jpg')
        + D.results('resNext', 'You can take the argument apart. Now write about it →')
        + D.activate('Write about the argument', 'Use at least four:', CHIPS,
                     'Speaking &middot; in pairs',
                     'One of you takes Tracey&rsquo;s position, one takes Harari&rsquo;s. Neither of '
                     'you has to believe it.',
                     ['Report your partner&rsquo;s last claim back to them using <em>contends</em> or '
                      '<em>maintains</em> &mdash; accurately enough that they accept the summary.',
                      'Concede one point genuinely before you answer it. Notice what conceding does '
                      'to your credibility.',
                      'Attack one <em>inference</em> rather than a premise. Say which step you think '
                      'does not carry.',
                      'Take one analogy and say where it gives way, without saying the conclusion is '
                      'therefore wrong.'],
                     'Writing &middot; 300&ndash;350 words',
                     'Choose one: (1) His closing line is more poignant than rigorous &mdash; discuss. '
                     '(2) A policy briefing endorsing or challenging a ban on AI legal personhood. '
                     '(3) The rhetorical strategy of the address for this particular audience.',
                     'Harari contends that…')
    )

    import i18n_harari as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Harari at Davos — Argument &amp; Register (C2) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    # Three of the four images are cream-and-pale-blue, and at the shipped 0.72
    # the wash swallows the sort-bin labels. Measured, not assumed — see HANDOFF.
    s = s.replace('  --bg-opacity: 0.72;', '  --bg-opacity: 0.40;', 1)
    open(OUT, 'w', encoding='utf-8', newline='\n').write(s)
    print('wrote %s — %d <section class="slide" (checker header is authoritative), '
          '%d MC, %d gap slides, 2 sorts, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), 2, len(s)))


if __name__ == '__main__':
    build()
