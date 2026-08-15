# -*- coding: utf-8 -*-
"""Stranger Things — B1, for German learners. Rebuild as a 16:9 deck.

Same filename, so the live URL does not change.

**The old lesson could not be finished.** `buildFillBlanks` ran
`rowDiv.innerHTML += ' '` *after* `appendChild(slot)`. Re-assigning
innerHTML re-parses the subtree, so the freshly-attached click handler on
both blanks was discarded and the blanks were inert. Section 2 could
therefore produce at most 12 scored events against a gate of
`sectionRequired[2] = 13`, and a learner who answered everything
correctly was locked out of the reading and error sections for good. The
only way through was to deliberately get a match wrong, which produces a
retry and a thirteenth event. Nobody who used this lesson properly ever
saw the second half of it.

**Option D was never the answer.** Not once, in any of the 21
four-option items. B was correct in 19 of 35. q17-q20 ran B,B,B,B.

**The key was the longest option in 10 of 32 items**, and 7 of those 10
were the reading questions — so longest-option alone scored 7/10 on the
comprehension section without reading the passage.

**Twenty-one wrong-answer feedback strings were the single word
`Wrong.`** — every wrong option in q17, q18, q21, q22 and q26. The three
stress items showed identical text whether the learner was right or
wrong. The match activity and both fill-blanks gave no words at all,
only a colour.

**Four of the six vocabulary items keyed on a word the lesson never
taught** (`appeared`, `never openly`, `abandoned`), and the distractors
included `foreboding`, `splendor`, `rugged` and `separable` — C1/C2
words offered to a B1 learner, who can then only work by elimination,
which is exactly what makes the longest-option and always-B heuristics
pay. Present continuous was used as a distractor seven times and never
taught. The first conditional carried two scored items and appeared only
as an unlabelled example inside a vocabulary card. Irregular past
participles were required twice and never listed.

Facts about the show, corrected:

- **"Eleven avoided capture for years" inverts the plot.** She was held
  inside the laboratory for years and escaped in 1983, meeting the boys
  within about a day. The passage said the opposite, and q26 then tested
  that sentence.
- **q11 invented a library scene for Will.** There isn't one, in any
  season, and the lesson's own passage never mentions a library.
- **Text messages in 1983.** q31 and a reference card both used them, in
  a lesson whose header reads HAWKINS 1983 and whose selling point is
  the period. They use walkie-talkies.
- **telekinetic**, not "psychokinetic" — the show's own term, and the
  one the sibling test file uses.

Also fixed: "A underground bunker", "at the Upside Down", the item that
produced "they were never openly open about it", and the two activity
labels reading "1 of 3" in sections that have two activities.

The pronunciation grid is not carried over as it stood. Twenty-seven
items presented as IPA with no audio, no minimal pairs and no production
task, of which twenty-one were unrelated to the lesson (Christianity,
bagpipes, parades, rapport), and whose notes told a learner that the
<gh> in *laughter* is silent (it is /f/, as the IPA printed directly
above it showed) and that /θ/ needs the lip (it does not, and following
that instruction produces /f/). What survives is word stress on words
this lesson actually uses, which can be taught and tested honestly
without audio.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'stranger-things-b1-lesson.html'
F = 'StrangerThings'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0a0d0a;
  --surface       : #151a13;
  --surface2      : #1e261c;
  --border        : #b85545;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #ec8777;
  --accent-bright : #f7bcb3;
  --accent-dim    : #db442d;
  --secondary     : #5e7a84;
  --contrast      : #1deda5;''' % F

CSS = '.card.read-text { background: #121711; }\n'

# ── grammar: which sentence is correct ────────────────────────────────
GRAM1 = [
    dict(stem='Which sentence is correct?',
         options=[
             'Eleven <em>has never seen</em> a creature quite like that one',
             'Eleven <em>doesn&rsquo;t saw</em> a creature quite like that one',
             'Eleven <em>saw</em> a creature like that since her escape',
             'Eleven <em>is seeing</em> creatures like that all her life'],
         correct=0,
         why='<strong>Has never seen</strong> — present perfect, for an '
             'experience up to now with no stated time. <em>Doesn&rsquo;t '
             'saw</em> mixes present and past; <em>since</em> forces the '
             'perfect; and <em>is seeing</em> is the continuous, which is for '
             'right now.'),
    dict(stem='My cat ______ onto the door handle every morning.',
         options=['jumps', 'jumped', 'is jumping', 'has jumped'], correct=0,
         why='<strong>Jumps</strong> — present simple, because <em>every '
             'morning</em> makes it a habit. <em>Jumped</em> is one finished '
             'event; <em>is jumping</em> is happening as you speak.'),
    dict(stem='He ______ it by watching what we do. (one finished action)',
         options=['learned', 'learns', 'has learned', 'is learning'],
         correct=0,
         why='<strong>Learned</strong> — past simple, one completed action. '
             '<em>Has learned</em> is not impossible in isolation, but <em>by '
             'watching what we do</em> points at a specific finished process.'),
    dict(stem='We ______ since our last argument. (they argued; they still '
              'do not speak)',
         options=['haven&rsquo;t spoken', 'don&rsquo;t speak',
                  'didn&rsquo;t speak', 'aren&rsquo;t speaking'], correct=0,
         why='<strong>Haven&rsquo;t spoken</strong> — <em>since</em> takes '
             'the present perfect. German <em>seit</em> uses the present, and '
             '<em>we don&rsquo;t speak since…</em> is the error that produces. '
             'This one is worth memorising as a pair: <em>since</em> → '
             '<em>have/has</em> + participle.'),
    dict(stem='Dustin is really ______ fixing electronics.',
         options=['good at', 'good in', 'good for', 'good to'], correct=0,
         why='<strong>Good at</strong> + noun or <em>-ing</em>. <em>Good '
             'for</em> means beneficial (<em>vegetables are good for you</em>); '
             '<em>good in</em> is the German <em>gut in</em> coming straight '
             'through.'),
]

# ── German traps ──────────────────────────────────────────────────────
GRAM2 = [
    dict(stem='&bdquo;Ich mache meine Hausaufgaben.&ldquo; &rarr; in English:',
         options=['I do my homework every evening',
                  'I make my homework every evening',
                  'I am making my homework every evening'], correct=0,
         why='English <strong>does</strong> homework. It also does sport, does '
             'a task and does its best. <em>Make</em> is the direct '
             'translation of <em>machen</em> and is wrong every time here.'),
    dict(stem='&bdquo;Ich bekomme eine Nachricht.&ldquo; &rarr; in English:',
         options=['I get a message from Mike', 'I become a message from Mike',
                  'I receive becoming a message from Mike'], correct=0,
         why='<strong>Get</strong> or <em>receive</em>. <em>Become</em> means '
             'to turn into something — <em>he became a teacher</em>. '
             '<em>Bekommen</em> and <em>become</em> are false friends, and '
             'this is the most-quoted German-English error there is.'),
    dict(stem='&bdquo;Ich muss für die Prüfung lernen.&ldquo; &rarr; in English:',
         options=['I have to study for the test', 'I must learn for the test',
                  'I need to learn for the test'], correct=0,
         why='<strong>Study for</strong> a test. English <em>learn</em> means '
             'to acquire a skill or fact — you learn Spanish, you learn to '
             'drive. German <em>lernen</em> covers both jobs; English splits '
             'them.'),
    dict(stem='Which sentence has the correct conditional?',
         options=['If I don&rsquo;t study, I will get a bad grade',
                  'If I will not study, I get a bad grade',
                  'If I won&rsquo;t study, I would get a bad grade'],
         correct=0,
         why='First conditional: <strong>if + present simple &rarr; will + '
             'infinitive</strong>. Never <em>will</em> in the if-clause. '
             'German uses the future in both halves (<em>wenn ich nicht '
             'lerne…</em> is present, but learners overcorrect), which is why '
             'this one is worth drilling.'),
    dict(stem='Which sentence uses <em>rely on</em> correctly?',
         options=['Mike relies on his friends when things go wrong',
                  'Mike relies in his friends when things go wrong',
                  'Mike relies with his friends when things go wrong'],
         correct=0,
         why='<strong>Rely on</strong> somebody — always <em>on</em>. Compare '
             '<em>depend on</em>, which takes the same preposition, and '
             '<em>count on</em>, which is the informal version.'),
]

# ── vocabulary ────────────────────────────────────────────────────────
VOCAB_GAPS = [
    ('There is still a lot of ______ around mental health &mdash; people are '
     'afraid to talk about it.', ['stigma'],
     '<strong>Stigma</strong> — a mark of social disgrace attached to a '
     'person or a subject. German: <em>Stigma</em>, and it works the same way.'),
    ('The Demogorgon posed a ______ danger to everyone in Hawkins.',
     ['severe'],
     '<strong>Severe</strong> — very great, very intense, and always about '
     'something bad. A severe danger, a severe winter, a severe injury.'),
    ('Finding Will was ______ &mdash; without him, nothing else mattered.',
     ['crucial'],
     '<strong>Crucial</strong> — critically important to how something turns '
     'out. Stronger than <em>important</em>.'),
    ('She said nothing. She just made a small ______ with her hand.',
     ['gesture'],
     '<strong>Gesture</strong> — a movement of the hand or body that carries '
     'meaning. German <em>Geste</em>.'),
    ('The whole street looked ______, as if everyone had left in a hurry.',
     ['abandoned'],
     '<strong>Abandoned</strong> — left behind and empty. Used of places, '
     'buildings and cars; also of people, where it is a much heavier word.'),
    ('Eleven learned to ______ her friends, and they learned to trust her.',
     ['rely on'],
     '<strong>Rely on</strong> — to depend on somebody with full trust. Two '
     'words, and the preposition is not optional.'),
]

VOCAB_MATCH = [
    ('stigma', 'A mark of social disgrace attached to a person or subject'),
    ('avoid', 'To keep away from something, or stop yourself doing it'),
    ('crucial', 'Critically important to how something turns out'),
    ('severe', 'Very great and very intense &mdash; always of something bad'),
    ('appear', 'To come into sight, often suddenly'),
    ('gesture', 'A movement of the hand or body that carries meaning'),
]

# ── the passage ───────────────────────────────────────────────────────
# Paragraph 3 previously said Eleven "avoided capture for years", which
# inverts the plot: she was held for years and escaped in 1983. The
# comprehension question was built on that sentence.
PARAS = [
    ('r1', '<em>Stranger Things</em> is an American science fiction horror '
     'series set in the fictional town of Hawkins, Indiana, in the 1980s. It '
     'was created by Matt and Ross Duffer &mdash; the Duffer Brothers &mdash; '
     'and first <strong>appeared</strong> on Netflix in 2016. The show '
     '<strong>relies on</strong> nostalgia for 1980s popular culture: the '
     'music, the clothes, and even the lettering of its title sequence.',
     'r1n', 'Two of the bold words are tested later. <em>Appear</em> here '
     'means to become available to the public, not to materialise out of thin '
     'air.'),
    ('r2', 'The story begins when a boy named Will Byers <strong>goes '
     'missing</strong>. His friends Mike, Dustin and Lucas set out to find '
     'him. During their search they meet a strange girl who <strong>has '
     'escaped</strong> from a secret government laboratory. She is known only '
     'as Eleven. Scientists there <strong>taught</strong> her to use her '
     'telekinetic abilities, and treated her as a test subject rather than a '
     'child.',
     'r2n', '<em>Has escaped</em> is present perfect: it happened before this '
     'moment in the story, and the result &mdash; she is out &mdash; still '
     'holds.'),
    ('r3', 'The laboratory is connected to a dark parallel dimension called '
     'the Upside Down. <strong>Certain</strong> creatures there, in '
     'particular a monster called the Demogorgon, pose a <strong>severe</strong> '
     'danger to anyone who meets them. Eleven had been held in the laboratory '
     'for years, and she <strong>avoided</strong> being caught again after '
     'her escape.',
     'r3n', 'Read the order carefully: she was <em>held</em> for years, and '
     '<em>then</em> escaped. A comprehension question depends on it.'),
    ('r4', 'Within days she had formed a bond with Mike, Dustin and Lucas, '
     'learning to trust and <strong>rely on</strong> them. The series '
     'explores friendship, courage, the <strong>stigma</strong> around being '
     'different, and the dangers of government secrecy.',
     'r4n', 'Note <em>within days</em>. Season 1 covers about a week — the '
     'friendship forms fast, which is part of why it lands.'),
]

READ_Q = [
    dict(stem='When and where is <em>Stranger Things</em> set?',
         options=['Hawkins, Indiana, in the 1980s',
                  'Hawkins, Indiana, in the 1990s',
                  'Hawkins, Illinois, in the 1980s',
                  'Hopkins, Indiana, in the 1970s'], correct=0,
         why='Paragraph 1, first sentence. Two of the wrong options change '
             'only one word — the decade or the state — which is exactly how '
             'a reading question in the real test will be built.'),
    dict(stem='Who are the Duffer Brothers?',
         options=['The people who created the series',
                  'Two of the main characters in the series',
                  'Scientists working at the laboratory',
                  'Will Byers&rsquo; older brothers'], correct=0,
         why='Paragraph 1: <em>created by Matt and Ross Duffer</em>. Will '
             'does have an older brother in the show — Jonathan — which is '
             'what makes that option tempting, but the text does not say so.'),
    dict(stem='Why is Eleven able to do what she does?',
         options=['Scientists at the laboratory taught her to use her powers',
                  'She absorbed her power from the Upside Down dimension itself',
                  'She was trained for years by the American military',
                  'She was born with them in Hawkins, Indiana'], correct=0,
         why='Paragraph 2: <em>scientists there taught her to use her '
             'telekinetic abilities</em>. The others are all plausible '
             'science-fiction explanations, and none of them is in the text — '
             'which is the whole skill being tested.'),
    dict(stem='What is the Upside Down?',
         options=['A dark parallel dimension linked to the laboratory',
                  'An underground bunker beneath the town of Hawkins',
                  'The secret government laboratory near Hawkins',
                  'An abandoned school on the edge of the town'], correct=0,
         why='Paragraph 3. Note that the laboratory and the Upside Down are '
             'two different places that are <em>connected</em> — the '
             'commonest misreading of this text.'),
    dict(stem='Which theme is NOT mentioned in the text?',
         options=['Travelling through time', 'The dangers of state secrecy',
                  'The stigma around being different', 'Friendship and courage'],
         correct=0,
         why='Paragraph 4 lists friendship, courage, stigma and government '
             'secrecy. Time travel is not there. With a NOT question, find '
             'the three that <em>are</em> in the text first, and take what is '
             'left.'),
]

CONTEXT_Q = [
    dict(stem='&ldquo;The show <em>relies on</em> nostalgia…&rdquo; &mdash; '
              '<em>rely on</em> here means:',
         options=['to depend on something as a foundation',
                  'to produce something in large amounts',
                  'to keep away from something deliberately',
                  'to forget something that once mattered'], correct=0,
         why='The show <em>depends on</em> nostalgia — it is built on it. '
             'Same verb as <em>Eleven relies on her friends</em>, and the same '
             'preposition.'),
    dict(stem='&ldquo;Scientists <em>taught</em> her…&rdquo; &mdash; '
              '<em>taught</em> is the past of:',
         options=['teach', 'think', 'touch', 'talk'], correct=0,
         why='teach &rarr; <strong>taught</strong>. Compare think &rarr; '
             '<em>thought</em>, which looks almost identical and is a '
             'different verb. Touch and talk are both regular: touched, '
             'talked.'),
    dict(stem='&ldquo;<em>Certain</em> creatures pose a danger…&rdquo; '
              '&mdash; <em>certain</em> here means:',
         options=['some particular ones, not named',
                  'definitely, without any doubt',
                  'safe, and not dangerous at all',
                  'very old, from long ago'], correct=0,
         why='<em>Certain</em> has two quite different jobs. Before a noun it '
             'usually means <strong>some particular ones</strong>. After '
             '<em>be</em> — <em>I am certain</em> — it means sure. Context '
             'decides, every time.'),
    dict(stem='&ldquo;…pose a <em>severe</em> danger…&rdquo; &mdash; '
              '<em>severe</em> means:',
         options=['very great and very intense', 'mild, and easily handled',
                  'sudden, and without warning', 'obvious to everyone'],
         correct=0,
         why='<strong>Severe</strong> is about intensity, not speed and not '
             'visibility. A severe storm, a severe shortage, a severe '
             'injury.'),
    dict(stem='&ldquo;She <em>avoided</em> being caught…&rdquo; &mdash; '
              '<em>avoided</em> means:',
         options=['managed to keep away from it', 'tried hard to make it happen',
                  'accepted it without a fight', 'was pleased when it happened'],
         correct=0,
         why='<strong>Avoid</strong> — keep away from. Note the form after '
             'it: <em>avoid <strong>being</strong> caught</em>, '
             '<em>avoid <strong>talking</strong></em> — always <em>-ing</em>, '
             'never <em>to</em>.'),
]

ERR_GAPS = [
    ('Wrong: <em>We don&rsquo;t spoke since Monday.</em> &nbsp;&rarr;&nbsp; '
     'We ______ since Monday.', ["haven't spoken|have not spoken"],
     '<strong>Since</strong> takes the present perfect: <em>have/has</em> + '
     'past participle. And the participle of <em>speak</em> is '
     '<em>spoken</em>, not <em>spoke</em>.'),
    ('Wrong: <em>I must learn for the history test.</em> &nbsp;&rarr;&nbsp; '
     'I must ______ for the history test.', ['study|revise'],
     '<strong>Study for</strong> a test — or <em>revise for</em> one, in '
     'British English. Both are accepted here.'),
    ('Wrong: <em>If I will not practise, I get a bad grade.</em> '
     '&nbsp;&rarr;&nbsp; If I ______ practise, I will get a bad grade.',
     ["don't|do not"],
     'No <em>will</em> in the if-clause. First conditional: <strong>if + '
     'present simple &rarr; will + infinitive</strong>.'),
    ('Wrong: <em>She is good in playing the guitar.</em> &nbsp;&rarr;&nbsp; '
     'She is good ______ playing the guitar.', ['at'],
     '<strong>Good at</strong>. The preposition is fixed and does not follow '
     'the German.'),
    ('Wrong: <em>I become a message on the walkie-talkie.</em> '
     '&nbsp;&rarr;&nbsp; I ______ a message on the walkie-talkie.',
     ['got|get|received'],
     '<strong>Got</strong>, <em>get</em> or <em>received</em>. Never '
     '<em>become</em>. And in 1983 Hawkins there are no text messages — '
     'walkie-talkies and landlines only.'),
    ('Wrong: <em>Eleven can rely in Mike.</em> &nbsp;&rarr;&nbsp; Eleven can '
     'rely ______ Mike.', ['on'],
     '<strong>Rely on</strong>. Same preposition as <em>depend on</em> and '
     '<em>count on</em>.'),
]

STRESS = [
    dict(stem='Which syllable carries the stress in <em>dangerous</em>?',
         options=['DAN-ger-ous', 'dan-GER-ous', 'dan-ger-OUS'], correct=0,
         why='<strong>DAN</strong>-ger-ous. The <em>-ous</em> ending never '
             'takes the stress: <em>FA-mous</em>, <em>SE-ri-ous</em>, '
             '<em>NER-vous</em>.'),
    dict(stem='Which syllable carries the stress in <em>experiment</em>?',
         options=['ex-PER-i-ment', 'EX-per-i-ment', 'ex-per-I-ment'],
         correct=0,
         why='ex-<strong>PER</strong>-i-ment. German <em>Experiment</em> '
             'stresses the last syllable, which is why this word is worth '
             'practising: the stress moves.'),
    dict(stem='Which syllable carries the stress in <em>laboratory</em> '
              '(British English)?',
         options=['la-BOR-a-t&rsquo;ry', 'LAB-or-a-tory', 'la-bor-A-tory'],
         correct=0,
         why='British English says la-<strong>BOR</strong>-a-t&rsquo;ry, in '
             'four beats. American English says <strong>LAB</strong>-ra-tor-y. '
             'Both are correct; they are simply different.'),
]


def read_slide(ek, e, tk, t, text, nk, note):
    return '''
    <section class="slide" data-type="teach" data-bg="%s/hero.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="card read-text" style="padding:22px 28px">
          <p class="prose" style="font-size:19px;line-height:1.6">%s</p>
          <p class="prose dim" style="margin-top:14px;padding-top:12px;
             border-top:1px solid var(--border);font-size:15px"
             data-i18n="%s">%s</p>
        </div>
      </div>
    </section>
''' % (F, ek, e, tk, t, text, nk, note)


def build():
    for label, qs in [('Grammar 1', GRAM1), ('German traps', GRAM2),
                      ('Reading', READ_Q), ('Vocab in context', CONTEXT_Q),
                      ('Stress', STRESS)]:
        D.assert_no_key_is_longest(qs, label)

    logo = D.logo_from(TPL)
    S = [D.cover(logo, 'Stranger <em>Things</em>',
                 'Hawkins, 1983 — tenses, the German traps, and the words the '
                 'story actually uses',
                 [('Level', 'B1 &middot; for German learners'),
                  ('Focus', 'Tenses &amp; vocabulary'),
                  ('Count', '42 slides')])]

    # ── tenses: three were taught, one was only ever a distractor ──
    S += [D.teach('t1E', 'The four tenses this lesson uses', 't1T',
                  'Present simple and past simple',
                  [('t1ah', 'Present simple &mdash; habits and facts',
                    'My cat <strong>jumps</strong> onto the door handle every '
                    'morning.',
                    't1an', 'Signals: every day, usually, often, never, on '
                    'Mondays. She/he/it takes <em>-s</em>.'),
                   ('t1bh', 'Past simple &mdash; one finished action',
                    'He <strong>learned</strong> it by watching us.',
                    't1bn', 'Signals: yesterday, last week, in 1983, two days '
                    'ago. Regular verbs take <em>-ed</em>; many common ones '
                    'do not.'),
                   ('t1ch', 'The test between them',
                    'Is there a finished time, or a repeated one?',
                    't1cn', 'A stated past time forces the past simple. A '
                    'repeated time forces the present simple. Find the time '
                    'word before you look at the verb.')],
                  folder=F),
          D.teach('t2E', 'The four tenses this lesson uses', 't2T',
                  'Present continuous &mdash; and why it is here',
                  [('t2ah', 'The form',
                    'am / is / are + verb<strong>-ing</strong>',
                    't2an', 'Eleven <em>is hiding</em> in the woods. Right '
                    'now, as we speak.'),
                   ('t2bh', 'Signals',
                    'now &middot; at the moment &middot; Look! &middot; '
                    'Listen!',
                    't2bn', 'If the sentence points at this moment, the '
                    'continuous is the only choice.'),
                   ('t2ch', 'Why it matters here',
                    'It is the commonest wrong answer in this lesson.',
                    't2cn', 'It is the commonest wrong option in the '
                    'questions ahead. You cannot reject a form you have '
                    'never been shown.')],
                  folder=F),
          D.teach('t3E', 'The four tenses this lesson uses', 't3T',
                  'Present perfect &mdash; and the German trap in it',
                  [('t3ah', 'The form',
                    'have / has + <strong>past participle</strong>',
                    't3an', 'I <em>have never seen</em> it. She <em>has '
                    'escaped</em>. We <em>haven\'t spoken</em>.'),
                   ('t3bh', 'When',
                    'Experience up to now, with no stated time.',
                    't3bn', 'And always after <em>since</em> and <em>for</em> '
                    'when the situation still holds.'),
                   ('t3ch', 'The trap',
                    'German <em>seit</em> takes the present. English does not.',
                    't3cn', '✗ <em>We don\'t speak since Monday.</em> ✓ '
                    '<em>We haven\'t spoken since Monday.</em> This single '
                    'pattern is worth more marks than any other on this page.')],
                  folder=F),
          D.teach('t4E', 'The four tenses this lesson uses', 't4T',
                  'The participles you need for the perfect',
                  [(None, 'speak &rarr; spoken &middot; see &rarr; seen',
                    'take &rarr; taken &middot; go &rarr; gone', None, None),
                   (None, 'teach &rarr; taught &middot; think &rarr; thought',
                    'find &rarr; found &middot; get &rarr; got', None, None),
                   (None, 'be &rarr; been &middot; do &rarr; done',
                    'write &rarr; written &middot; know &rarr; known',
                    't4n', 'The perfect needs the third form, not the past '
                    'simple. <em>I have spoke</em> is the error; <em>I have '
                    'spoken</em> is the sentence.')],
                  folder=F),
          D.teach('t5E', 'One more structure', 't5T',
                  'The first conditional',
                  [('t5ah', 'The pattern',
                    'If + <strong>present simple</strong> &rarr; '
                    '<strong>will</strong> + infinitive',
                    't5an', 'If I <em>don\'t study</em>, I <em>will get</em> a '
                    'bad grade.'),
                   ('t5bh', 'The rule that gets broken',
                    'Never <em>will</em> in the if-clause.',
                    't5bn', '✗ <em>If I will not study…</em> — this is the '
                    'single commonest conditional error in German-speaking '
                    'classrooms.'),
                   ('t5ch', 'Why it is called the first',
                    'It is about a real, possible future.',
                    't5cn', 'Two scored items on this page depend on it. '
                    'German uses the present in both halves too, which is '
                    'why the <em>will</em> slips in.')],
                  folder=F)]

    S += [D.teach('gtE', 'German traps', 'gtT',
                  'Four false friends and a fixed preposition',
                  [('gt1h', 'machen &rarr; do, not make',
                    '<strong>do</strong> your homework &middot; do sport '
                    '&middot; do your best',
                    'gt1n', '<em>Make</em> is for producing a thing: make a '
                    'cake, make a noise, make a plan.'),
                   ('gt2h', 'bekommen &rarr; get, not become',
                    '<strong>get</strong> a message &middot; get a present',
                    'gt2n', 'English <em>become</em> = <em>werden</em>. '
                    '&bdquo;I became a message&ldquo; says you turned into '
                    'one.'),
                   ('gt3h', 'lernen &rarr; study or learn',
                    '<strong>study</strong> for a test &middot; '
                    '<strong>learn</strong> Spanish',
                    'gt3n', 'And two fixed forms: <em>good at</em> something, '
                    '<em>rely on</em> somebody. Neither preposition follows '
                    'the German.')],
                  folder=F)]

    S += ["".join(D.mc(i + 1, len(GRAM1), q, 'g1E', 'Grammar &middot; Activity 1',
                       'g1T', 'Choose the correct form', folder=F)
                  for i, q in enumerate(GRAM1))]
    S += ["".join(D.mc(i + 1, len(GRAM2), q, 'g2E', 'Grammar &middot; Activity 2',
                       'g2T', 'Fix the German mistake', folder=F)
                  for i, q in enumerate(GRAM2))]

    S += [D.teach('vE', 'Vocabulary', 'vT',
                  'Six words the story needs',
                  [(None, 'stigma &middot; severe',
                    'a mark of social disgrace &middot; very great, very '
                    'intense', None, None),
                   (None, 'crucial &middot; gesture',
                    'critically important &middot; a meaningful movement of '
                    'the hand', None, None),
                   (None, 'abandoned &middot; rely on',
                    'left behind and empty &middot; to depend on with full '
                    'trust',
                    'vn', 'All six appear in the reading, and four of them '
                    'are tested. Learn them here and the questions later are '
                    'straightforward.')],
                  folder=F)]
    for n, rows in enumerate([VOCAB_GAPS[:3], VOCAB_GAPS[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'vgE', 'Vocabulary &middot; Activity 1',
                    'vgT', 'Complete the sentence', folder=F, size=17,
                    width=150,
                    hint='One word per gap. Every one of them is on the slide '
                         'before this.' if n == 0 else None,
                    hint_key='vgHint' if n == 0 else None)]
    S += [D.match(VOCAB_MATCH, 'vmE', 'Vocabulary &middot; Activity 2', 'vmT',
                  'Match the word to its meaning', 'vmHint',
                  'Click a word, then click its meaning.',
                  'Two of these have a second, commoner meaning in everyday '
                  'English &mdash; <em>severe</em> and <em>appear</em>. The '
                  'reading uses both in this sense.',
                  folder=F)]

    for i, (pk, text, nk, note) in enumerate(PARAS):
        S += [read_slide('rE', 'The text', 'rT%d' % (i + 1),
                         'Reading &mdash; part %d of 4' % (i + 1), text, nk,
                         note)]
    S += ["".join(D.mc(i + 1, len(READ_Q), q, 'rqE', 'Reading &middot; Comprehension',
                       'rqT', 'What does the text say?', folder=F)
                  for i, q in enumerate(READ_Q))]
    S += ["".join(D.mc(i + 1, len(CONTEXT_Q), q, 'rcE',
                       'Reading &middot; Vocabulary in context', 'rcT',
                       'What does the word mean here?', folder=F)
                  for i, q in enumerate(CONTEXT_Q))]

    for n, rows in enumerate([ERR_GAPS[:3], ERR_GAPS[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'eE', 'Spot the mistake', 'eT',
                    'Write the correction', folder=F, size=16, width=150,
                    hint='Each sentence has one error. Write only the part '
                         'that changes.' if n == 0 else None,
                    hint_key='eHint' if n == 0 else None)]

    S += ["".join(D.mc(i + 1, len(STRESS), q, 'sE', 'Word stress', 'sT',
                       'Where does the stress fall?', folder=F)
                  for i, q in enumerate(STRESS))]

    S += [D.results(),
          D.activate('Hawkins, one week later', 'Use at least four:',
                     ['have you ever…?', 'haven&rsquo;t seen', 'since',
                      'if… will', 'rely on', 'good at', 'severe'],
                     'Speaking &middot; in pairs',
                     'One of you was in Hawkins that week. The other is from '
                     'the local paper.',
                     ['Reporter: ask three questions with <em>Have you '
                      'ever…?</em> and one with <em>How long…?</em>',
                      'Witness: answer using <em>since</em> at least twice. '
                      'Watch the tense — <em>since</em> takes the perfect.',
                      'Both: make three first-conditional predictions about '
                      'what happens next in the town.',
                      'Both: say one thing each of you is <em>good at</em>, '
                      'and one person you <em>rely on</em>. Watch both '
                      'prepositions.'],
                     'Writing &middot; 120&ndash;150 words',
                     'Write the newspaper report of the week Will Byers went '
                     'missing. Past simple for what happened, present perfect '
                     'for what has changed since.',
                     'Last November, a twelve-year-old boy went missing in '
                     'Hawkins, Indiana. Since then, …')]
    return S


if __name__ == '__main__':
    import i18n_stranger
    s = D.assemble(TPL, OUT, "".join(build()), PALETTE,
                   'Stranger Things — B1 English', i18n_stranger)
    s = s.replace('</style>\n</head>', CSS + '</style>\n</head>', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes' % (OUT, len(s)))
