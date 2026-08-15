# -*- coding: utf-8 -*-
"""Impostor Syndrome — Advanced English (C1), for Japanese learners.

Rebuild of impostor_syndrome_advanced_JP.html, a seven-step scrolling
lesson. Same filename, so the live URL does not change. English and
Japanese, because this lesson is written for Japanese learners and
already carried Japanese throughout.

The audit found this lesson's comprehension quiz to be, in effect,
unanswerable and simultaneously trivial. Both at once.

**Trivial:** all seven keys were the longest option, at roughly twice the
mean distractor length, and the key was never A and never D — the answer
array was literally [2,1,1,1,2,2,1]. A learner who never opened the text
could pick the long middle option seven times and score 7/7.

**Unanswerable:** two of those seven asked about text that is not in the
passage. Q5 asked what "the scientist who documented laboratory problems"
was evidence for — the words *scientist*, *laboratory* and *equipment*
appear nowhere in the reading. Q6 asked what the author implied by the
phrase "there is often no threshold of accomplishment that puts these
feelings to rest", and *threshold* likewise occurs zero times. The cause
is visible in the sibling file `impostor_syndrome_lesson.html`: the
passage was cut down from a longer script and the questions, one
vocabulary card, a discourse-marker row and a phrase-bank entry were all
left pointing at the removed material. Q3 was worse than either — its
premise ("why does positive feedback often fail to relieve impostor
feelings") contradicts the passage, which *recommends* collecting
positive feedback, and its supporting quotation was invented.

Those three are rewritten against sentences the passage actually
contains, testing the same skills: evidence-function, vocabulary in
context, and inference.

Other defects fixed here:

- **No wrong-answer feedback existed anywhere in the lesson.** The
  handler swapped a two-word prefix onto one shared explanation string,
  so right and wrong learners read identical text. Same for all four
  collocation items.
- **All five error-correction explanations were dead data** —
  `errorData[].note` was authored and never rendered. Five rules tested,
  zero taught. The grader then dumped all five answers in gap order on
  the first wrong submission, and each input's placeholder was the error
  word itself.
- **Wrong predictions rendered in a green success panel** — a duplicated
  `style` attribute and a hard-coded `ok` class that the handler never
  swapped.
- **The nominalisation check could not fail:** it passed on the substring
  "many people", which appears in the prompt sentence.
- **Only 7 items in the whole lesson were scored.** Fourteen other
  gradeable responses fed nothing. Vocabulary, hedging, collocations,
  discourse markers and error correction are all scored here.

Factual corrections:

- *imposterism* was described as "preferred in academic literature over
  'syndrome'". The term the literature actually prefers is **impostor
  phenomenon** (Clance & Imes 1978).
- A vocabulary example cited "Clance's longitudinal study traced
  imposterism across twenty years of academic careers." No such study
  exists. Replaced.
- The passage's claim that impostorism "isn't necessarily tied to
  depression, anxiety, or self-esteem" is stated as settled; Bravata et
  al. (2020) report consistent associations with both anxiety and
  depression. Hedged, and the disagreement is taught rather than hidden —
  in a lesson whose own grammar section is about hedging, an unhedged
  contested claim was the wrong thing to model.
- "Most surefire way" is likewise the strongest claim in the text and is
  now marked as the text's claim rather than a finding.
- Angelou's "eleven books" is the video script's figure and undercounts
  her; the passage no longer turns on a number.

Japanese corrections:

- **偽物症候群 is not a term.** It was coined for this page. The standard
  Japanese is **インポスター症候群**.
- **Target-language content had been translated into Japanese** in two
  places — the closing quotation, which lost the very hedge it was there
  to exemplify, and two rows of the discourse-marker table. The English
  being taught stays in English; only instructions and chrome translate.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'impostor_syndrome_advanced_JP.html'
F = 'Impostor'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090e0a;
  --surface       : #121c14;
  --surface2      : #1a281d;
  --border        : #576871;
  --text          : #f2f4f5;
  --text-dim      : #a3b5bf;
  --accent        : #6aa3c4;
  --accent-bright : #99c4dc;
  --accent-dim    : #417491;
  --secondary     : #f27868;
  --contrast      : #e4717e;

  /* the hero is blue edge to edge and the accent is drawn from
     it, so the Forbes mark was vanishing into its own artwork.
     House style names --contrast as the switch for this. */
  --logo-mark     : var(--contrast);''' % F

CSS = (
    '/* the passage is read once and then referred back to from seven\n'
    '   comprehension slides, so it gets a solid card rather than the\n'
    '   translucent one. */\n'
    '.card.read-text { background: #12181c; }\n'
    '.jp { font-size: 15px; color: var(--text-dim); }\n'
)

# ── vocabulary ────────────────────────────────────────────────────────
# (word, part, English definition, note-key, en note, ja note)
VOCAB = [
    ('fraudulence', 'n',
     'The unwarranted conviction that you have fooled others into '
     'overestimating you.',
     'v1', 'a sense of ~ &middot; pervasive ~ &middot; feelings of ~',
     '偽物感。「自分は他人をだましている」という根拠のない確信。<br>'
     'コロケーション: a sense of ~ / feelings of ~'),
    ('accolade', 'n',
     'An award or public honour, especially one given by an authoritative '
     'body.',
     'v2', 'receive / garner / merit an ~ &middot; a prestigious ~',
     '称賛、栄誉、受賞。権威ある団体から与えられるもの。<br>'
     'コロケーション: garner / receive an ~'),
    ('unwarranted', 'adj',
     'Not justified by the facts. Used of beliefs that contradict the '
     'evidence.',
     'v3', '~ concern / fear / criticism &middot; entirely ~',
     '根拠のない、不当な。事実に反する思い込みについて使う。<br>'
     'コロケーション: ~ fear / criticism'),
    ('pervasive', 'adj',
     'Present throughout something; affecting nearly every part or member.',
     'v4', '~ influence / culture / feeling &middot; remain ~',
     '広く浸透した、蔓延している。ラテン語 pervadere（通り抜ける）から。<br>'
     'コロケーション: ~ influence / feeling'),
    ('disproportionate', 'adj',
     'Larger or smaller than is reasonable or just, relative to something '
     'else.',
     'v5', '~ impact / burden / effect &middot; ~ly affect',
     '不均衡な、過度の。何かと比べて不当に大きい（小さい）こと。<br>'
     'コロケーション: ~ burden / impact'),
    ('pluralistic ignorance', 'n',
     'When everyone in a group privately doubts a norm but assumes the '
     'others accept it.',
     'v6', 'perpetuate / reinforce / overcome ~',
     '多元的無知。全員が内心では疑っているのに、他の人は納得していると'
     '思い込んでいる状態。'),
    ('impostor phenomenon', 'n',
     'The academic term for this experience — self-doubt, fear of exposure, '
     'and crediting success to luck.',
     'v7', 'experience / study the ~',
     'インポスター現象。学術文献で用いられる正式な用語（Clance &amp; Imes '
     '1978）。「症候群」という語は病気を連想させるため避けられる。'),
    ('surefire', 'adj',
     'Certain to work. Informal, and unusually strong for academic prose.',
     'v8', '~ way / method / solution',
     '確実な、間違いのない。くだけた語で、学術的な文章では珍しく強い断定。'),
    ('banish', 'v',
     'To get rid of something permanently. Normally used of people; here, '
     'of a feeling.',
     'v9', '~ doubt / fear &middot; ~ from one\'s mind',
     '追い払う、永久に消し去る。本来は人に使う語を、ここでは感情に'
     '比喩的に用いている。'),
    ('spiral (into)', 'v',
     'To get progressively and rapidly worse, in a self-reinforcing cycle.',
     'v10', '~ into crisis / failure &middot; a downward ~',
     '悪循環に陥る、螺旋状に悪化する。下向きの渦の比喩で、勢いと'
     '抜け出しにくさの両方を含む。'),
    ('susceptible (to)', 'adj',
     'Likely to be affected by something; not immune to it.',
     'v11', 'be ~ to pressure / criticism / influence',
     '〜の影響を受けやすい。必ず to + 名詞が続く。日本語話者が'
     '前置詞を落としやすい語。'),
    ('downplay', 'v',
     'To present something as less important than it really is. Opposite: '
     'overstate.',
     'v12', '~ the risk / the significance / a role',
     '軽く見る、過小評価する。反対語は overstate。'),
]

VOCAB_GAPS = [
    ('No ______, however prestigious, seemed able to quiet his self-doubt.',
     ['accolade'],
     '<strong>Accolade</strong> — an award or public honour. Note the '
     'concessive <em>however prestigious</em> sitting inside the noun '
     'phrase; that is a C1 pattern worth copying.'),
    ('The committee concluded that her fear of being exposed was entirely '
     '______.', ['unwarranted'],
     '<strong>Unwarranted</strong> — not justified by the facts. '
     '<em>Entirely unwarranted</em> is the standard intensifier.'),
    ('The ______ nature of self-doubt across professions suggests a '
     'structural cause.', ['pervasive'],
     '<strong>Pervasive</strong> — present throughout. Used here '
     'attributively before <em>nature</em>, which is how it most often '
     'appears in academic prose.'),
    ('Even the most confident people are ______ to situational self-doubt.',
     ['susceptible'],
     '<strong>Susceptible to</strong> — the preposition is obligatory. '
     '「〜に対して」の to を落とさないこと。'),
    ('Unaddressed, the anxiety can ______ into a conviction that exposure is '
     'inevitable.', ['spiral'],
     '<strong>Spiral into</strong> — to worsen progressively. The metaphor '
     'carries both momentum and difficulty of escape.'),
    ('To call it a syndrome is to ______ how universal it is.', ['downplay'],
     '<strong>Downplay</strong> — to make something seem less important. '
     'This is the sentence the passage itself uses.'),
]

VOCAB_MATCH = [
    ('fraudulence', 'The conviction that you have fooled others'),
    ('pluralistic ignorance', 'Everyone privately doubts; each assumes the rest do not'),
    ('disproportionate', 'Unfairly large or small relative to something else'),
    ('banish', 'To drive out permanently'),
    ('surefire', 'Certain to work &mdash; informal, and unusually strong'),
    ('impostor phenomenon', 'The term the research literature actually uses'),
]

# ── the passage ───────────────────────────────────────────────────────
# Eight paragraphs, one per slide. Two edits of substance: the Angelou
# sentence no longer turns on a book count that undercounts her, and the
# depression/anxiety claim is hedged, because Bravata et al. (2020) report
# consistent associations and the unhedged version was the one sentence in
# the lesson that modelled exactly the overstatement Step 5 teaches
# against.
PARAS = [
    ('p1', 'Even after publishing book after book and winning several of the '
     'most prestigious awards in American letters, Maya Angelou could not '
     'escape the nagging doubt that she had not really earned her '
     'accomplishments. Albert Einstein described himself in similar terms — '
     'as an "involuntary swindler" whose work did not deserve the attention '
     'it received.',
     'p1n', '<em>nagging</em>: persistently troubling, refusing to go away. '
     '<em>involuntary</em>: not by choice; a <em>swindler</em> deceives '
     'people for gain.',
     'nagging = 頭から離れない。involuntary swindler = 意図せずして人を'
     'だましている者。'),
    ('p2', 'Accomplishments at that level are rare, but the feeling of '
     'fraudulence is extremely common. Why can so many of us not shake the '
     'feeling that we have not earned what we have, or that our ideas are '
     'not worth other people\'s attention?',
     'p2n', '<em>shake a feeling</em>: to rid yourself of an unwanted '
     'emotion. Compare <em>shake off a cold</em>. A very common collocation '
     'and an easy one to miss.',
     'shake a feeling = 感情を振り払う。shake off a cold と同じ用法。'),
    ('p3', 'The psychologist Pauline Rose Clance was the first to study this '
     'unwarranted sense of insecurity. Working as a therapist, she noticed '
     'that many of her undergraduate patients shared one concern: despite '
     'high grades, they did not believe they deserved their places at the '
     'university. Some believed their acceptance had been an admissions '
     'error.',
     'p3n', '<em>admissions error</em>: a mistake in the enrolment process. '
     'The students feared their acceptance was accidental rather than '
     'earned.',
     'admissions error = 入学選考のミス。「自分は間違って合格した」という'
     '思い込み。'),
    ('p4', 'With her colleague Suzanne Imes, Clance first studied the '
     'impostor phenomenon in female college students and faculty, '
     'establishing pervasive feelings of fraudulence in that group. It has '
     'since been found across gender, race, age and a wide range of '
     'occupations, though it may be more prevalent among, and '
     'disproportionately affect, underrepresented or disadvantaged groups.',
     'p4n', 'Read the hedging in the last clause: <em>may be</em>, not '
     '<em>is</em>. Step 5 comes back to this sentence — it is the model for '
     'the whole grammar section.',
     '最後の節の may be に注目。is ではない。第5部でこの文をもう一度扱う。'),
    ('p5', 'To call it a syndrome is to downplay how universal it is. It is '
     'not a disease or an abnormality, though research does find it '
     'associated with anxiety and low mood. People who are highly skilled '
     'tend to assume everyone else is equally skilled, and that assumption '
     'can spiral into a feeling that they do not deserve the accolades and '
     'opportunities they receive.',
     'p5n', '<em>To call X is to Y</em> is a concessive pattern worth '
     'stealing. Note also that the original of this passage said '
     'impostorism "isn\'t necessarily tied to depression or anxiety" — '
     'later work (Bravata et al., 2020) reports consistent associations, so '
     'the claim is softened here.',
     '"To call X is to Y" は使える譲歩表現。なお元の文は「うつや不安とは'
     '関係ない」と断定していたが、後の研究では関連が報告されている。'),
    ('p6', 'Everyone is susceptible to pluralistic ignorance: we each doubt '
     'ourselves privately but believe we are alone in doing so, because no '
     'one else says it out loud. Since it is hard to know how hard our peers '
     'work, how difficult they find a task, or how much they doubt '
     'themselves, there is no easy way to dismiss the feeling that we are '
     'the least capable person in the room.',
     'p6n', 'This paragraph is the answer to one of the comprehension '
     'questions. Read it twice.',
     'この段落は読解問題の答えに直結する。二度読むこと。'),
    ('p7', 'Intense feelings of this kind stop people sharing good ideas, or '
     'applying for jobs and programmes where they would do well. The text\'s '
     'own strongest claim is that the most surefire way to fight impostor '
     'feelings is to talk about them. Even hearing that a mentor has felt '
     'the same thing can help; so, sometimes, can simply learning that there '
     'is a name for it.',
     'p7n', '<em>surefire</em> is informal and unusually strong. Notice how '
     'far it sits from the careful <em>may be</em> of paragraph 4 — the same '
     'author, two very different levels of commitment.',
     'surefire は口語的で断定が強い。第4段落の may be との落差に注目。'),
    ('p8', 'Once you are aware of the phenomenon, you can work against it by '
     'collecting and revisiting positive feedback about yourself. We may '
     'never be able to banish these feelings entirely, but we can have open '
     'conversations about academic and professional difficulty — and be '
     'franker about some simple truths: <em>you have talent, you are '
     'capable, and you belong.</em>',
     'p8n', 'The closing line stays in English. In the previous version of '
     'this lesson it had been translated into Japanese, which removed the '
     'thing it was there to demonstrate.',
     '最後の一文は英語のまま。旧版では日本語に訳されており、'
     '示すべきものが消えていた。'),
]

# ── comprehension ─────────────────────────────────────────────────────
# Every option is written to a comparable length. In the original, all
# seven keys were the longest option by roughly 2x, and the key was never
# A and never D.
COMP = [
    dict(stem='Why does the author open with Maya Angelou and Albert Einstein?',
         options=[
             'To show that impostor feelings survive achievement of any kind, '
             'in any field',
             'To suggest that impostor feelings are largely confined to the '
             'unusually famous',
             'To establish the author&rsquo;s credibility by citing two very '
             'well-known names',
             'To contrast the literary temperament with the scientific one, '
             'in passing'],
         correct=0,
         why='Two figures from opposite fields, both at the top of them. The '
             'pairing forecloses the objection <em>if I were really any good, '
             'I would not feel this way</em>. It is an argument about '
             '<strong>range</strong>, not about fame.'),
    dict(stem='Why does the author object to the word <em>syndrome</em>?',
         options=[
             'Because it frames as a rare illness something the text says is '
             'near-universal',
             'Because the term was coined before the necessary research had '
             'been carried out',
             'Because medical vocabulary excludes readers with no training in '
             'psychology',
             'Because it carries the implication that the condition cannot be '
             'treated at all'],
         correct=0,
         why='"To call it a syndrome is to <strong>downplay how universal it '
             'is</strong>." The objection is to the connotation of '
             'abnormality — not to the accuracy of the research or the '
             'accessibility of the word.'),
    # Rewritten. The original asked why positive feedback "often fails to
    # relieve impostor feelings" and quoted a sentence that is not in the
    # text — while the passage in fact recommends collecting it.
    dict(stem='Paragraph 8 recommends collecting and revisiting positive '
              'feedback. What does that advice assume about the problem?',
         options=[
             'That the belief survives the evidence, so the evidence has to be '
             'deliberately revisited',
             'That people are simply not given enough praise, so the supply '
             'of it has to be increased',
             'That praise works only when it comes from a person the receiver '
             'already respects',
             'That the feelings are best removed altogether before any real '
             'work can be done'],
         correct=0,
         why='The advice only makes sense if the evidence is already there and '
             'is not being retained. Note that the paragraph does not claim '
             'the feelings can be removed — it says the opposite: <em>we may '
             'never be able to banish these feelings entirely</em>.'),
    dict(stem='How does <em>pluralistic ignorance</em> relate to impostor '
              'feelings, as the text describes it?',
         options=[
             'It is a cause: it hides from each person that the doubt is '
             'shared by everyone',
             'It is a consequence: sufferers stay quiet, which leaves others '
             'feeling alone',
             'It is another name for the same thing, used by a different '
             'group of researchers',
             'It is unrelated: one describes a group effect and the other an '
             'individual one'],
         correct=0,
         why='The mechanism runs one way in the text: because nobody says it '
             'out loud, each person concludes their own doubt is exceptional. '
             'The <em>consequence</em> reading is not absurd — the cycle does '
             'feed itself — but paragraph 6 introduces it as the reason there '
             'is <em>no easy way to dismiss</em> the feeling.'),
    # Rewritten. The original asked about "the scientist who documented
    # laboratory problems", who does not appear in this passage at all.
    dict(stem='Paragraph 3 reports that some students believed their '
              'acceptance had been an admissions error. What is that detail '
              'doing in the argument?',
         options=[
             'Giving a concrete form to a claim that would otherwise stay '
             'abstract',
             'Showing that university admissions processes are less reliable '
             'than assumed',
             'Explaining why Clance decided to change career from therapy to '
             'research',
             'Proving that the students were in fact right about their own '
             'ability'],
         correct=0,
         why='It is evidence of the <strong>strength</strong> of the belief: '
             'these students preferred to believe an institution had made a '
             'clerical mistake than that they had earned their place. The '
             'detail makes "unwarranted sense of insecurity" concrete.'),
    # Rewritten. The original quoted a "threshold of accomplishment"
    # sentence that does not occur in the passage.
    dict(stem='In paragraph 5, what does <em>spiral into</em> add that '
              '<em>lead to</em> would not?',
         options=[
             'That the process accelerates, feeds itself, and is hard to stop',
             'That the process is gradual, and therefore easier to interrupt',
             'That the outcome is uncertain and may not arrive at all',
             'That the cause and the effect are really the same thing'],
         correct=0,
         why='A spiral tightens as it turns. <em>Lead to</em> is neutral about '
             'speed and about escape; <strong>spiral into</strong> carries '
             'both momentum and difficulty of exit, which is why it collocates '
             'with <em>crisis</em>, <em>debt</em> and <em>decline</em>.'),
    dict(stem='Paragraph 4 says the phenomenon <em>may be</em> more prevalent '
              'in some groups. What does the hedge accomplish?',
         options=[
             'It marks the evidence as real but not yet settled, which is the '
             'honest position',
             'It weakens the claim and suggests the author does not really '
             'believe it',
             'It is a stylistic habit of academic prose that has no real '
             'effect on the meaning',
             'It signals that the author disagrees but is obliged to report '
             'the finding'],
         correct=0,
         why='Hedging in academic English is not timidity. It marks the '
             'difference between a well-replicated finding and a suggestive '
             'one. Compare <em>surefire</em> in paragraph 7 — the same author '
             'dropping the hedge, and the one place the text overcommits.'),
]

# ── grammar ───────────────────────────────────────────────────────────
NOM_GAPS = [
    ('They discovered that many people feel anxious. &nbsp;&rarr;&nbsp; '
     'Their ______ of widespread anxiety…', ['discovery'],
     'discover → <strong>discovery</strong>. The verb becomes the head noun '
     'and the clause collapses into a noun phrase.'),
    ('People feel fraudulent. &nbsp;&rarr;&nbsp; pervasive feelings of '
     '______', ['fraudulence'],
     'fraudulent → <strong>fraudulence</strong>. The suffix <em>-ence</em> '
     'makes an abstract noun from the adjective.'),
    ('The group was ignorant of what others thought. &nbsp;&rarr;&nbsp; '
     'pluralistic ______', ['ignorance'],
     'ignorant → <strong>ignorance</strong>. Same move, same suffix family.'),
    ('Students are accepted by the university. &nbsp;&rarr;&nbsp; their '
     '______ by the university', ['acceptance'],
     'accept → <strong>acceptance</strong>. Note that the agent survives as '
     '<em>by the university</em> — nominalisation lets you keep it or drop '
     'it, and dropping it is how these sentences become impersonal.'),
]

HEDGE = [
    dict(stem='Imposterism ______ be more prevalent among underrepresented '
              'groups.',
         options=['may', 'will', 'must', 'does'], correct=0,
         why='<strong>May</strong> marks possibility. <em>Will</em> and '
             '<em>must</em> both assert; <em>does</em> emphasises. Only '
             '<em>may</em> leaves the finding open.'),
    dict(stem='This ______ to suggest that cultural factors amplify the '
              'experience.',
         options=['appears', 'proves', 'shows', 'serves'], correct=0,
         why='<strong>Appears to suggest</strong> is doubly hedged and '
             'entirely normal in academic prose. <em>Proves</em> and '
             '<em>shows</em> claim far more than the evidence carries.'),
    dict(stem='There ______ to be no level of success at which these feelings '
              'stop.',
         options=['seems', 'is known', 'is proven', 'is agreed'], correct=0,
         why='<strong>Seems</strong>. The others assert that the matter is '
             'settled — and a negative universal ("no level at which…") is '
             'exactly the kind of claim that cannot be settled.'),
]

COLLOC = [
    dict(stem='to ______ self-doubt', options=['harbour', 'commit', 'achieve',
                                               'ignore'], correct=0,
         why='<strong>Harbour</strong> is the academic collocate: you harbour '
             'self-doubt, resentment, suspicion. <em>Have self-doubt</em> is '
             'not wrong, but it is markedly weaker.'),
    dict(stem='to ______ an accolade', options=['garner', 'reach', 'commit',
                                                'attend'], correct=0,
         why='<strong>Garner</strong> — to accumulate over time. '
             '<em>Receive</em> is also correct and plainer; <em>garner</em> is '
             'the one you meet in journalism and literary prose.'),
    dict(stem='to ______ a belief', options=['entertain', 'exceed', 'dismiss',
                                             'banish'], correct=0,
         why='<strong>Entertain a belief</strong> — to hold it provisionally, '
             'without committing. <em>Dismiss</em> and <em>banish</em> both '
             'collocate with <em>belief</em> too, but they mean the opposite '
             'of what is wanted here.'),
    dict(stem='to ______ feelings of fraudulence',
         options=['perpetuate', 'commit', 'achieve', 'attain'], correct=0,
         why='<strong>Perpetuate</strong> — to cause something to continue '
             'indefinitely. It is the verb the research literature uses about '
             'self-reinforcing beliefs.'),
]

DM_MATCH = [
    ('Concession', 'To call it a syndrome is to downplay how universal it is'),
    ('Condition', 'Once you are aware of the phenomenon, you can…'),
    ('Cause and result', 'That assumption can spiral into a feeling that…'),
    ('Contrast', 'We may never banish them entirely, but we can talk openly'),
    ('Concession in a clause', 'No accolade, however prestigious, seemed to…'),
    ('Hedged generalisation', 'It may be more prevalent among…'),
]

ERR_GAPS = [
    ('Wrong: <em>Despite of her achievements, she doubted herself.</em> '
     '&nbsp;&rarr;&nbsp; ______ her achievements, she doubted herself.',
     ['Despite|despite'],
     '<strong>Despite</strong> takes no <em>of</em>. It is <em>in spite '
     'of</em> that carries one, and the two get crossed. ✓ despite her '
     'achievements ✗ despite of her achievements'),
    ('Wrong: <em>It may effects experienced professionals.</em> '
     '&nbsp;&rarr;&nbsp; It may ______ experienced professionals.',
     ['affect'],
     '<strong>Affect</strong> is the verb; <em>effect</em> is almost always '
     'the noun. After <em>may</em> you need the bare verb, so both the word '
     'and the <em>-s</em> were wrong.'),
    ('Wrong: <em>The phenomenon is more prevalently in some groups.</em> '
     '&nbsp;&rarr;&nbsp; The phenomenon is more ______ in some groups.',
     ['prevalent'],
     '<strong>Prevalent</strong> — an adjective after <em>is</em>. The '
     '<em>-ly</em> form would need a verb to modify, and there is none.'),
    ('Wrong: <em>She could not shake the feeling which she had not '
     'deserved it.</em> &nbsp;&rarr;&nbsp; …the feeling ______ she had not '
     'deserved it.', ['that'],
     'After <em>feeling</em>, <em>idea</em>, <em>fact</em>, <em>belief</em>, '
     'the clause that says <em>what</em> the feeling is takes '
     '<strong>that</strong>. <em>Which</em> introduces a relative clause '
     'about a thing, which is a different job.'),
    ('Wrong: <em>Talking about it is better than keep quiet.</em> '
     '&nbsp;&rarr;&nbsp; …better than ______ quiet.', ['keeping'],
     'Both sides of <em>than</em> have to match. <em>Talking</em> is a '
     'gerund, so <strong>keeping</strong> must be too.'),
]


def read_slide(ek, e, tk, t, text, nk, note):
    return '''
    <section class="slide" data-type="teach" data-bg="%s/hero.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="card read-text" style="padding:24px 30px">
          <p class="prose" style="font-size:20px;line-height:1.6">%s</p>
          <p class="prose dim" style="margin-top:14px;padding-top:12px;
             border-top:1px solid var(--border);font-size:15px"
             data-i18n="%s">%s</p>
        </div>
      </div>
    </section>
''' % (F, ek, e, tk, t, text, nk, note)


def build():
    for label, qs in [('Comprehension', COMP), ('Hedging', HEDGE),
                      ('Collocations', COLLOC)]:
        D.assert_no_key_is_longest(qs, label)

    logo = D.logo_from(TPL)
    S = [D.cover(logo, 'Impostor <em>Syndrome</em>',
                 'Why do high achievers feel like frauds? — advanced reading, '
                 'academic style and a cultural comparison',
                 [('Level', 'C1 &middot; Academic English'),
                  ('Focus', 'Psychology &amp; society'),
                  ('Count', '45 slides')])]

    S += [D.teach('preE', 'Before you read', 'preT',
                  'Three things to hold in mind',
                  [('pre1h', 'The claim',
                    'Accomplishment does not settle the question of whether '
                    'you deserved it.',
                    'pre1n', 'Decide now whether you believe that, and see '
                    'whether the text changes your mind.'),
                   ('pre2h', 'The cultural question',
                    'Kenson (謙遜) — modesty as a social virtue.',
                    'pre2n', 'Does a culture that expects public modesty make '
                    'private doubt easier to voice, or harder? There is no '
                    'single right answer, and the text does not give one.'),
                   ('pre3h', 'The language',
                    'Watch for <em>may be</em>, <em>appears to</em>, '
                    '<em>tends to</em>.',
                    'pre3n', 'The grammar section is built from sentences in '
                    'the reading. Mark the careful ones as you go.')],
                  folder=F)]

    for n in range(4):
        group = VOCAB[n * 3:(n + 1) * 3]
        S += [D.teach('vE', 'Vocabulary', 'vT%d' % (n + 1),
                      'Twelve words (%d of 4)' % (n + 1),
                      [(None, '%s <span class="dim" style="font-size:15px">'
                        '(%s)</span>' % (w, p), d, nk, note)
                       for w, p, d, nk, note, _ in group],
                      folder=F)]

    for n, rows in enumerate([VOCAB_GAPS[:3], VOCAB_GAPS[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'vgE', 'Vocabulary in use', 'vgT',
                    'Complete the sentence', folder=F, size=17, width=170,
                    hint='One word per gap, in the form the sentence needs.'
                         if n == 0 else None,
                    hint_key='vgHint' if n == 0 else None)]
    S += [D.match(VOCAB_MATCH, 'vmE', 'Vocabulary', 'vmT',
                  'Match the term to its definition', 'vmHint',
                  'Click a term, then click its definition.',
                  'Note <strong>impostor phenomenon</strong>: that is the term '
                  'the research literature uses. This lesson previously '
                  'claimed <em>imposterism</em> was the preferred one.',
                  folder=F)]

    for i, (pk, text, nk, note, _ja) in enumerate(PARAS):
        S += [read_slide('rdE', 'The text', 'rdT%d' % (i + 1),
                         'Reading &mdash; paragraph %d of 8' % (i + 1),
                         text, nk, note)]

    S += ["".join(D.mc(i + 1, len(COMP), q, 'cE', 'Critical comprehension',
                       'cT', 'Read for what is implied', folder=F)
                  for i, q in enumerate(COMP))]

    S += [D.teach('nomE', 'Academic style', 'nomT',
                  'Nominalisation: turn the verb into a noun',
                  [('nom1h', 'The move',
                    'They found that people felt fraudulent. &rarr; '
                    'Their finding of pervasive fraudulence.',
                    'nom1n', 'The verb becomes the head noun and the clause '
                    'collapses into a noun phrase.'),
                   ('nom2h', 'Why it is done',
                    'Denser, more formal, and impersonal.',
                    'nom2n', 'It lets you drop the agent. <em>Their '
                    'acceptance</em> does not say who accepted them.'),
                   ('nom3h', 'The cost',
                    'Overdone, it becomes unreadable.',
                    'nom3n', 'Two nominalisations in a sentence is style; four '
                    'is fog. C1 writing is knowing where to stop.')],
                  folder=F)]
    for n, rows in enumerate([NOM_GAPS[:2], NOM_GAPS[2:]]):
        S += [D.gap(n + 1, 2, rows, None, 'ngE', 'Academic style', 'ngT',
                    'Write the noun form', folder=F, size=17, width=180,
                    hint='One word: the noun that the verb or adjective '
                         'becomes.' if n == 0 else None,
                    hint_key='ngHint' if n == 0 else None)]

    S += [D.teach('hedE', 'Academic style', 'hedT',
                  'Hedging: claiming exactly as much as the evidence allows',
                  [('hed1h', 'The devices',
                    'may &middot; might &middot; appears to &middot; tends to '
                    '&middot; suggests',
                    'hed1n', 'Modal verbs, reporting verbs, and adverbs of '
                    'frequency all do this work.'),
                   ('hed2h', 'What it is not',
                    'It is not politeness, and it is not weakness.',
                    'hed2n', 'This is where it differs from kenson (謙遜). '
                    'Kenson is about the speaker; hedging is about the '
                    'evidence.'),
                   ('hed3h', 'The test',
                    'Would a replication failure embarrass this sentence?',
                    'hed3n', 'If yes, hedge it. Paragraph 7 of the reading '
                    'fails that test — <em>surefire</em> is the one place the '
                    'text overcommits.')],
                  folder=F)]
    S += ["".join(D.mc(i + 1, len(HEDGE), q, 'hgE', 'Academic style', 'hgT',
                       'Choose the hedge', folder=F)
                  for i, q in enumerate(HEDGE))]

    S += [D.teach('colE', 'Academic style', 'colT',
                  'Collocation: the verb that belongs with the noun',
                  [('col1h', 'Why it matters at C1',
                    'The grammar can be perfect and the phrase still wrong.',
                    'col1n', '<em>Have self-doubt</em> is not an error. '
                    '<em>Harbour self-doubt</em> is what a reader of academic '
                    'English expects.'),
                   ('col2h', 'How to learn them',
                    'Store the pair, never the single word.',
                    'col2n', 'Learn <em>garner an accolade</em>, not '
                    '<em>garner</em>. The vocabulary cards in this lesson give '
                    'the collocates for exactly this reason.'),
                   ('col3h', 'Register travels with them',
                    'garner &middot; harbour &middot; perpetuate &middot; '
                    'entertain',
                    'col3n', 'All four are formal. Using one in casual speech '
                    'is as marked as using <em>get</em> in a paper.')],
                  folder=F)]
    S += ["".join(D.mc(i + 1, len(COLLOC), q, 'cgE', 'Academic style', 'cgT',
                       'Complete the collocation', folder=F)
                  for i, q in enumerate(COLLOC))]

    S += [D.match(DM_MATCH, 'dmE', 'Academic style', 'dmT',
                  'Match the function to the sentence from the text', 'dmHint',
                  'Click a function, then click the sentence that performs it.',
                  'Every sentence here is from the reading. Two rows of the '
                  'old version of this table quoted sentences that were not in '
                  'the text at all.', folder=F)]

    S += [D.teach('errE', 'Before the error correction', 'errT',
                  'Five mistakes, and why each one happens',
                  [('err1h', 'despite / in spite of',
                    'One takes <em>of</em>; the other never does.',
                    'err1n', 'The two get crossed, and <em>despite of</em> is '
                    'the result. There is no such phrase.'),
                   ('err2h', 'affect / effect &middot; -ly on adjectives',
                    'affect = verb &middot; effect = noun',
                    'err2n', 'And an adjective after <em>is</em> stays an '
                    'adjective: <em>is more prevalent</em>, not <em>is more '
                    'prevalently</em>.'),
                   ('err3h', 'that / which &middot; parallel gerunds',
                    'the feeling <strong>that</strong>… &middot; better than '
                    '<strong>keeping</strong> quiet',
                    'err3n', 'After feeling, idea, fact and belief, the clause '
                    'takes <em>that</em>. And both sides of <em>than</em> must '
                    'take the same form.')],
                  folder=F)]
    for n, rows in enumerate([ERR_GAPS[:3], ERR_GAPS[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'egE', 'Error correction', 'egT',
                    'Write the correction', folder=F, size=15, width=140,
                    hint='One word each. Only the wrong word changes.'
                         if n == 0 else None,
                    hint_key='egHint' if n == 0 else None)]

    S += [D.teach('cu1E', 'Cultural connections', 'cu1T',
                  '謙遜 (kenson) and impostor feelings',
                  [('cu1ah', 'Kenson is public',
                    'Downplaying your ability out loud is polite.',
                    'cu1an', 'It is a social performance, and everyone in the '
                    'room knows it is one.'),
                   ('cu1bh', 'Impostor feeling is private',
                    'It is a belief the person wishes they did not hold.',
                    'cu1bn', 'The difference is whether you would be relieved '
                    'to stop.'),
                   ('cu1ch', 'The open question',
                    'Does a script for public modesty help or hide?',
                    'cu1cn', 'It may make the words available — or it may make '
                    'the real thing impossible to distinguish from the '
                    'performance.')],
                  folder=F),
          D.teach('cu2E', 'Cultural connections', 'cu2T',
                  '空気を読む and pluralistic ignorance',
                  [('cu2ah', 'The same mechanism',
                    'Both involve reading what others appear to feel.',
                    'cu2an', 'And both involve getting it wrong, in the same '
                    'direction, at the same time as everyone else.'),
                   ('cu2bh', 'Where they differ',
                    'One is a skill; the other is an error.',
                    'cu2bn', 'Reading the room is something you can be good '
                    'at. Pluralistic ignorance is what happens when everyone '
                    'reads it correctly and it is still wrong.'),
                   ('cu2ch', 'Why the text cares',
                    'It is the reason talking about it works.',
                    'cu2cn', 'One person saying it out loud breaks the '
                    'ignorance for everyone in earshot.')],
                  folder=F),
          D.teach('cu3E', 'Cultural connections', 'cu3T',
                  '受験 (juken) and the achievement paradox',
                  [('cu3ah', 'The setup',
                    'Years of preparation for one selection.',
                    'cu3an', 'Entry is framed as the culmination of the '
                    'effort — the point at which the question is settled.'),
                   ('cu3bh', 'What happens inside',
                    'Everyone in the room passed the same exam.',
                    'cu3bn', 'Paragraph 5: highly skilled people assume '
                    'everyone else is equally skilled. A selective '
                    'institution makes that assumption locally true.'),
                   ('cu3ch', 'The paradox',
                    'The harder the selection, the less it settles.',
                    'cu3cn', 'This is a good example for the writing task: '
                    'universal psychology, culturally specific trigger.')],
                  folder=F)]

    S += [D.results(),
          D.activate('To what extent is it universal?', 'Use at least four:',
                     ['it may be', 'appears to', 'this raises the question of',
                      'far from being', 'harbour', 'perpetuate',
                      'disproportionately'],
                     'Speaking &middot; in pairs',
                     'One of you argues that the phenomenon is universal. The '
                     'other argues that culture shapes it.',
                     ['Universal side: use two pieces of evidence from the '
                      'text, and hedge both to exactly the strength the text '
                      'supports.',
                      'Cultural side: use kenson or juken as a specific case. '
                      'A general claim about "Japanese culture" will not do.',
                      'Both: find one point where you actually agree, and say '
                      'what it is in one sentence.',
                      'Both: identify one claim your opponent overstated, and '
                      'offer them the hedge that would fix it.'],
                     'Writing &middot; 200&ndash;250 words',
                     'To what extent is impostor syndrome a universal '
                     'psychological experience, and to what extent is it '
                     'shaped by cultural and social factors? Use evidence from '
                     'the text and at least two nominalisations.',
                     'The question of whether impostor feelings are universal '
                     'or culturally contingent is…')]
    return S


if __name__ == '__main__':
    import i18n_impostor
    s = D.assemble(TPL, OUT, "".join(build()), PALETTE,
                   'Impostor Syndrome — Advanced English · C1',
                   i18n_impostor, langs=('en', 'ja'))
    s = s.replace('</style>\n</head>', CSS + '</style>\n</head>', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes' % (OUT, len(s)))
