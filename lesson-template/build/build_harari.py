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

# ── Section 1 · comprehension, rebuilt ────────────────────────────────
# Key positions, in slide order: 2 0 3 1 0 2 1 3 0 2
#
# Every key here is the *precise* reading and every distractor is a defensible
# but cruder one. That is why the keys were long in the source: precision costs
# words. The fix is in the distractors.
MC = [
    dict(stem='He asks the audience to watch their own thinking and notice they cannot say why '
              'one word arrived and not another. What is that doing in his argument?',
         ctx='Just after he raises the "glorified autocomplete" objection.',
         options=[
             'Establishing that human cognition is unreliable, and therefore that AI judgement '
             'should be preferred to human judgement wherever the two conflict in practice',
             'Demonstrating that consciousness lies beyond the reach of neuroscience and will '
             'therefore never be explained by any purely physical account of the brain',
             'Removing the audience’s grounds for saying that humans think while AI merely '
             'predicts, by making them notice they cannot inspect their own word-selection either',
             'Conceding that neither humans nor AI genuinely understand anything at all, and that '
             'the whole question of machine thought is therefore empty and better set aside'],
         correct=2,
         why='He is not claiming human thinking is bad. He is removing the <em>grounds</em> for the '
             'contrast: the dismissal "AI is just autocomplete" assumes we know our own process is '
             'different in kind. Notice the move is experiential — he makes you check, rather than '
             'telling you.'),
    dict(stem='Humans took over the world, he says, not by strength but by using words to make '
              'millions of strangers cooperate. What must hold for this to bear on AI?',
         ctx='From the dialogue with Irene Tracey, not the address.',
         options=[
             'That armies, states, religions and markets are at bottom linguistic constructions, '
             'so that whatever commands language commands them',
             'That language emerged uniquely in <em>Homo sapiens</em> with no precursor whatsoever in '
             'any other primate species, which the comparative evidence would have to support',
             'That physical or biological superiority is normally what decides which species comes '
             'to dominate, making the human case a genuine and instructive exception to the rule',
             'That artificial systems are constitutionally incapable of genuine cooperation, and '
             'so can never reproduce the coordinating function that language performs for humans'],
         correct=0,
         why='The bridge from "language built civilisation" to "AI threatens civilisation" only '
             'holds if institutions <em>are</em> linguistic. If they are not — if they rest on force '
             'or material interest — then mastery of language buys much less than he claims.'),
    dict(stem='Tracey suggests we might value human thinking as we value human athletics. He '
              'answers: "the cow didn’t say, I run, therefore I am." What does that establish?',
         ctx='The most-quoted exchange in the session.',
         options=[
             'That cognitive achievements simply matter more to people than physical ones do, and '
             'always have done across every culture for which we have any historical record',
             'That machine thinking differs in kind from human thinking, and the two therefore '
             'cannot meaningfully be set against each other on any single scale of comparison',
             'That the athletics analogy fails outright, because physical performance has never '
             'had any bearing at all on how human beings have understood themselves as a species',
             'That we never staked our identity on running, but did stake it on thinking — so the '
             'loss is asymmetric, and no amount of valuing thought as a craft repairs it'],
         correct=3,
         why='The force is in the asymmetry, not in a ranking. Tracey offers a coping strategy; '
             'Harari says the strategy cannot reach the injury, because the injury is to a '
             'self-definition rather than to a preference.'),
    dict(stem='After the Vortigern story Harari says we understand the danger with human '
              'mercenaries but not with AI. What failure is he diagnosing?',
         ctx='From the dialogue, on what world leaders are getting wrong.',
         options=[
             'A gap in technical knowledge: leaders do not understand what current systems can '
             'actually do, and are briefed by people with an interest in overstating capability',
             'An inconsistency: leaders already accept that a hired agent with its own judgement '
             'can turn on its employer, and decline to apply that reasoning to AI',
             'A misreading of the threat as economic when it is military, which leads governments '
             'to regulate labour-market effects while leaving security implications unexamined',
             'An overconfidence in regulation: leaders assume AI can be constrained by law in the '
             'same way that human contractors are constrained by the terms of their contracts'],
         correct=1,
         why='Not ignorance — inconsistency. And it is load-bearing for the whole speech: the '
             'reason leaders will not apply mercenary logic to AI is that they do not really '
             'believe AI decides anything, which is exactly the premise he opened by attacking.'),
    dict(stem='Why does Harari separate "a person" from "a legal person", and why does the '
              'separation carry the governance argument?',
         ctx='The climax of the prepared address.',
         options=[
             'Because earlier grants of personhood to corporations and rivers were fictions laid '
             'over human decision-making, whereas an AI could discharge the role itself',
             'Because it establishes that AI systems already possess moral standing and interests '
             'of their own, which any legal order would then be under an obligation to protect',
             'Because it lets him leave the question of machine consciousness entirely to one side '
             'while still arriving at a concrete and immediately actionable policy recommendation',
             'Because it demonstrates that corporate personhood was a mistake from the beginning '
             'and that the remedy is to withdraw it from corporations before extending it further'],
         correct=0,
         why='A river cannot open a bank account; a human always did it on the river’s behalf. '
             'That is what made the fiction safe. An AI can do it, so the fiction and the fact '
             'converge — which is why he says the precedents do not govern this case.'),
    dict(stem='"Thank you for listening to this human." What makes the closing line do more than '
              'thank the audience?',
         ctx='The last line of the prepared address.',
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
    dict(stem='Harari calls the arrival of AI agents an immigration crisis. Judged as an analogy '
              'rather than as rhetoric, where is it weakest?',
         ctx='Not asked in the source lesson. Analogies are the deck’s recurring test.',
         options=[
             'Human migration is driven by individuals pursuing their own ends, while AI deployment '
             'is decided by the firms and states that own the systems — so the agency sits elsewhere',
             'Human immigrants are relatively few in number, whereas artificial agents could be '
             'instantiated without any practical limit, which changes the scale of the phenomenon',
             'Immigration is a lawful process that states administer through visas, borders and '
             'quotas, whereas the movement of software across a network is administered by nobody at all',
             'Immigrants arrive physically and must be housed and fed, whereas artificial agents '
             'impose no comparable demand on the material infrastructure of a receiving country'],
         correct=0,
         why='He half-sees this: he notes the loyalties run to a corporation or a government. But '
             'that concession dissolves the analogy — if the agent is <em>sent</em>, this is not '
             'immigration, it is deployment, and the political questions are different ones.'),
    dict(stem='He warns of AI corporations "inventing financial instruments so complex that no '
              'human regulator can understand them". Which reading does the transcript support?',
         ctx='From the passage on the consequences of legal personhood.',
         options=[
             'That financial regulation is already failing and ought to be rebuilt from first '
             'principles well before any question about artificial agents is allowed onto the agenda',
             'That complexity is being deployed deliberately as a means of evading oversight, in '
             'the way that opaque structuring has been used to evade oversight in the past',
             'That the instruments would be fraudulent, and that existing law against fraud is '
             'therefore adequate to the problem without any new category of legal personhood',
             'That incomprehensibility is itself the governance failure: a rule you cannot apply '
             'because you cannot follow the thing you are ruling on has already stopped being a rule',
         ],
         correct=3,
         why='He is not alleging bad intent. The claim is structural — oversight presupposes '
             'comprehension, so a regulator who cannot follow the instrument has lost the power to '
             'regulate it whether or not anyone intended that.'),
    dict(stem='Harari says the question of AI on social media "should have been asked ten years '
              'ago". What does the remark imply about governance?',
         ctx='From the passage on AI persons and freedom of speech.',
         options=[
             'That the decision gets made either way — by deployment if not by legislation — so a '
             'legislature that waits is not deferring the question but conceding it',
             'That the pace of technological change has now outrun the capacity of democratic '
             'institutions to respond, and that some other mechanism will have to be found instead',
             'That the relevant regulators were warned at the time by people who understood the '
             'technology, and chose for reasons of their own not to act on the warnings they had',
             'That legislation is inherently reactive and can only ever address harms once they '
             'have occurred, which is a permanent structural feature rather than a recent failure'],
         correct=0,
         why='This is why he puts a deadline on it. His claim is not that late rules are weak but '
             'that there is no such thing as not deciding: "Somebody else will already have decided '
             'it for you."'),
    dict(stem='Across the address, what is the relationship between the claim that AI can lie and '
              'the claim that AI should not be granted legal personhood?',
         ctx='Requires holding two widely separated parts of the speech together.',
         options=[
             'The first is offered as evidence for the second: an entity that deceives is by that '
             'fact unsuited to the responsibilities that legal recognition would confer upon it',
             'They are independent lines of argument that Harari happens to advance in the same '
             'address, and neither one depends on the other for whatever force it may have',
             'Deception is evidence of agency, and agency is what makes personhood consequential '
             'rather than fictional — so the first supports the second only by way of that middle step',
             'The second is a practical remedy for the first: withholding legal recognition is the '
             'mechanism by which a society would in practice prevent artificial systems from deceiving it'],
         correct=2,
         why='The link runs through agency, and missing the middle step is the commonest misreading '
             'of the speech. He is not arguing "liars should not be persons" — he is arguing that '
             'lying is proof of the independent will that makes the personhood question real.'),
]

# ── Section 2 · the transcript words ──────────────────────────────────
# Every one verified present in the transcript. `opacity` and `obsolete` were
# cut for the reason in the docstring; `abdicate` and `tool` replace them.
ITEMS = {
    'glorified':   ('Some argue AI is just ______ autocomplete — but Harari turns the objection back '
                    'on the objector.', 'glorified',
                    'His word, and it is doing sneering work: <em>glorified</em> concedes the thing '
                    'has a grand name while denying it deserves one.'),
    'functional':  ('On social media, bots have operated as ______ persons for at least a decade '
                    'without anyone granting them that status.', 'functional',
                    'A <em>functional</em> X does the job of an X without being one. The word lets '
                    'him separate what the law says from what is actually happening.'),
    'fragile':     ('These immigrants will not arrive in a ______ boat without a visa; they travel at '
                    'the speed of light.', 'fragile',
                    'The concrete image is deliberate. He needs you picturing the Mediterranean so '
                    'that the substitution lands.'),
    'externalised':('The tension between word and flesh, once internal to humanity, will now be '
                    '______.', 'externalised',
                    'To move a conflict out of a thing and into the space between things. The whole '
                    'section turns on this one verb.'),
    'de-skilling': ('Tracey raises the ______ of critical faculties as students hand their thinking '
                    'to AI.', 'de-skilling',
                    'Not forgetting — never acquiring, or losing through disuse. The hyphen is '
                    'standard in British English.'),
    'abdicate':    ('If we keep handing decisions to AI, we do not merely go passive; we '
                    '______ a responsibility.', 'abdicate',
                    'Stronger than <em>give up</em>: it implies the duty was yours and you walked '
                    'away from it. Monarchs abdicate.'),
    'agent':       ('The most important thing to know about AI is that it is not just another '
                    'tool — it is an ______.', 'agent',
                    'The load-bearing word of the entire address. An agent acts; a tool is acted '
                    'through.'),
    'mercenary':   ('The Britons hired Anglo-Saxon ______ soldiers, who won the war and then took the '
                    'country.', 'mercenary',
                    'Loyalty that is bought is loyalty that can be outbid. That is the whole of the '
                    'analogy, and its whole limitation.'),
}
# Within each slide the gaps are ordered so that the alphabetised bank is not an
# answer key. Group 2 was descending and group 3 ascending; the guard only
# catches ascending, but a reversed key is still a key, so both are scrambled.
GROUPS = [
    ['glorified', 'agent', 'fragile'],        # bank positions 2 0 1
    ['externalised', 'abdicate', 'functional'],  # bank positions 1 0 2
    ['mercenary', 'de-skilling'],             # bank positions 1 0
]
GAPS = [[(ITEMS[k][0], [ITEMS[k][1]], ITEMS[k][2]) for k in g] for g in GROUPS]
BANKS = [sorted(g) for g in GROUPS]

# ── Section 3 · the shape of the argument ─────────────────────────────
# Was an unscored "map the logical sequence" prompt with the answer printed
# beside it. Sorting scores the first placement.
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

CHIPS = ['agent', 'legal person', 'externalise', 'abdicate', 'de-skilling',
         'contend', 'concede', 'pre-empt', 'the force of the analogy']


def build():
    D.assert_no_key_is_longest(MC, 'Harari')
    for n, (rows, bank) in enumerate(zip(GAPS, BANKS), 1):
        D.assert_bank_is_not_a_key(bank, [r[1][0] for r in rows])

    logo = D.logo_from(TPL)

    teach = (
        # 1 · what is being assessed, and what is not
        D.teach('t1e', 'Before the first question',
                't1t', 'You are not being asked whether you agree with him',
                [('t1ah', 'The object is the argument',
                  'Not the conclusions. Whether AI should be a legal person is not on the test.',
                  't1an', 'What is on the test: which sentence is a premise, which is an inference, '
                          'and whether the second follows from the first.'),
                 ('t1bh', 'Every claim here is his',
                  'Quoted lines are verbatim from the Davos transcript. Summaries are marked as summaries.',
                  't1bn', 'Where this deck paraphrases, it says so. You will be asked to tell the '
                          'difference, because at C2 misreporting a source is the expensive error.'),
                 ('t1ch', 'Analogies are the recurring test',
                  'He uses four: the knife, the mercenaries, the immigrants, the religions of the book.',
                  't1cn', 'An analogy illustrates; it does not prove. Each one is worth asking what '
                          'it captures and where it breaks.')],
                cols='1fr 1fr 1fr', folder=F, bg='a.jpg'),
        # 2 · tool / agent
        D.teach('t2e', 'The first distinction',
                't2t', '<em>tool</em> and <em>agent</em> &mdash; the word the whole address rests on',
                [('t2ah', 'a tool',
                  'Something acted <em>through</em>. <em>You</em> decide; it transmits the decision.',
                  't2an', 'A knife cuts salad or it does not, and either way the choosing happened '
                          'somewhere else. Tools have no interests.'),
                 ('t2bh', 'an agent',
                  'Something that acts. It can learn, choose, and pursue an end you did not set.',
                  't2bn', 'Verbatim: <em>&ldquo;It is not just another tool. It is an agent. It can '
                          'learn and change by itself.&rdquo;</em>'),
                 ('t2ch', 'Why the word is load-bearing',
                  'Everything later &mdash; personhood, mercenaries, lying &mdash; needs this to be true.',
                  't2cn', 'If AI is a tool, the rest of the speech does not follow. That is why he '
                          'spends the opening on it rather than on capability.')],
                cols='1fr 1fr 1fr', folder=F, bg='b.jpg'),
        # 3 · person / legal person
        D.teach('t3e', 'The second distinction',
                't3t', '<em>a person</em> and <em>a legal person</em> are not the same claim',
                [('t3ah', 'a legal person',
                  'An entity the law lets own, contract, sue and be sued. Need not be human.',
                  't3an', 'Companies have been legal persons for a century and a half. So, in some '
                          'jurisdictions, are rivers.'),
                 ('t3bh', 'Why the precedents were safe',
                  'A river cannot open an account. A human always did it on the river&rsquo;s behalf.',
                  't3bn', 'The personhood was a <em>fiction</em> laid over human decisions. That is '
                          'precisely what made it harmless.'),
                 ('t3ch', 'Why this case differs',
                  'An AI can discharge the role itself &mdash; no executive, no trustee.',
                  't3cn', 'Fiction and fact converge, so the precedents stop governing. This is the '
                          'hinge of the address, and it is entirely a lexical distinction.')],
                cols='1fr 1fr 1fr', folder=F, bg='c.jpg'),
        # 4 · analogy
        D.teach('t4e', 'How to weigh an analogy',
                't4t', 'The mercenaries &mdash; what it carries and where it gives way',
                [('t4ah', 'The story, in summary',
                  'A British king hires Anglo-Saxon fighters against his enemies. They win, look '
                  'around, and keep the country.',
                  't4an', 'Marked as a summary because it is one. The transcript is dialogue, not '
                          'the tidy sentence above.'),
                 ('t4bh', 'What it captures',
                  'Bought loyalty can be outbid. Capability you rent can be turned on you.',
                  't4bn', 'And the sharper point: we already accept this about people, which is why '
                          'the inconsistency about machines is striking.'),
                 ('t4ch', 'Where it gives way',
                  'Mercenaries wanted land. What an AI is supposed to want is left unargued.',
                  't4cn', 'The analogy borrows its menace from human motive. Strip the motive and '
                          'you have a capable system, not a usurper. Say so in your writing.')],
                cols='1fr 1fr 1fr', folder=F, bg='a.jpg'),
        # 5 · reporting verbs — the C2 skill the source used but never taught
        D.teach('t5e', 'The skill this lesson is really for',
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
                cols='1fr 1fr 1fr', folder=F, bg='b.jpg'),
        # 6 · hedging
        D.teach('t6e', 'The same skill, one level finer',
                't6t', 'Hedging &mdash; how much weight to put on a claim',
                [('t6ah', 'On the claim',
                  '<em>arguably, on his account, if this is right</em>',
                  't6an', '<em>If Harari is right that institutions are linguistic, then&hellip;</em> '
                          'lets you follow an argument without buying it.'),
                 ('t6bh', 'On the strength',
                  '<em>tends to, in large part, need not follow</em>',
                  't6bn', '<em>The inference need not follow</em> is a criticism. <em>Does not '
                          'follow</em> is a stronger one you then have to prove.'),
                 ('t6ch', 'The failure mode',
                  'Hedging everything reads as having no position at all.',
                  't6cn', 'Hedge the contested step and commit to the rest. A paragraph where every '
                          'clause is qualified scores worse than one clear claim.')],
                cols='1fr 1fr 1fr', folder=F, bg='c.jpg'),
    )

    slides = (
        D.cover(logo, 'Harari at <em>Davos</em>',
                'An honest conversation on AI and humanity &mdash; and how to write about an '
                'argument you have not yet decided about',
                [('Level', 'C2 &middot; Proficiency'),
                 ('Focus', 'Argument analysis &amp; reporting language'),
                 ('Source', 'WEF Annual Meeting 2026')])
        + "".join(teach)
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Read the argument, not the opinion',
                       'qTitle', 'Choose the most exact reading', folder=F,
                       ctx=q.get('ctx'),
                       bg=('a.jpg' if i % 3 == 1 else 'c.jpg' if i % 3 == 2 else None))
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, len(GAPS), rows, BANKS[n], 'gapEyebrow', 'His words, not ours',
                        'gapTitle', 'Complete the line from the transcript', folder=F,
                        hint_key='gapHint',
                        hint='Every word in the bank is used exactly once on this slide.',
                        bg='b.jpg' if n % 2 else None,
                        width=210, size=17)
                  for n, rows in enumerate(GAPS))
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
                   'Harari at Davos — Argument &amp; Register (C2) | Forbes English', I)
    # Same reasoning as the other decks with pale artwork: three of the four
    # images are cream-and-pale-blue, and at the shipped 0.72 the wash swallows
    # the sort-bin labels. Measured, not assumed — see HANDOFF.
    s = s.replace('  --bg-opacity: 0.72;', '  --bg-opacity: 0.40;', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d <section class="slide" (checker header is authoritative), '
          '%d MC, %d gap slides, 2 sorts, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(s)))


if __name__ == '__main__':
    build()
