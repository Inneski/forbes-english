# -*- coding: utf-8 -*-
"""Interface strings for Manifestation: Can You Think It Into Being? (B2).

English, German and Spanish (DE and ES written in-session, no native
check). Every string the learner reads is keyed here, so a further
language is one module (i18n_manifestation_<code>.py exporting T) plus the
code in LANGS.

NOT translated, deliberately (HOUSE-STYLE §8): the headword on each teach
card, its example line, every question option, the gap sentences, the
order chunks, the match terms and the sort items — they are the English
being taught. Situations (ctx) and stems with no blank in them translate,
as deck.mc allows. Cited phrases are in double quotes.
"""
import importlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord',
        'resPerfect', 'resStrong', 'resMid', 'resLow']

LANGS = ('en', 'de', 'es')

T = {}

T['en'] = dict(
    coverTitle='Manifestation: <em>Can You Think It Into Being?</em>',
    coverSub='Vision boards, the law of attraction, and the English of reporting a '
             'claim without believing it',
    chipLevel='B2 · Upper intermediate', chipFocus='Reporting claims · passive &amp; hedging',
    chipCount='35 slides',

    d1t='Think It, Get It', d1n='Part 1 · the vocabulary of manifesting',
    d2t='Said to Work', d2n='Part 2 · reporting a claim with distance',
    d3t='What the Evidence Says', d3n='Part 3 · hedging, and the psychology',
    d4t='Somewhere in the Middle', d4n='Part 4 · giving a balanced view',

    e1='The trend', e2='The claims', e3='The evidence', e4='Your view',

    p1t='Believe it and it will come',
    p1a='To <strong>manifest</strong> something is to bring it into your life by '
        'believing it will happen: picturing it, writing it down, saying it out loud. '
        'The idea is old, but <em>The Secret</em> (2006) made it a bestseller and '
        'TikTok made it a trend. In 2024 Cambridge Dictionary chose '
        '<strong>manifest</strong> as its Word of the Year.',
    p1b='Supporters call it focus. Critics call it wishful thinking with better marketing.',
    p2t='Reporting a claim without believing it',
    p2a='Careful writers rarely say "manifesting works". They <strong>report the '
        'claim</strong> and keep their distance: <strong>It is claimed that</strong> '
        'picturing success brings it closer. Manifesting <strong>is said to</strong> '
        'work best if you feel grateful in advance.',
    p2b='The passive puts the claim into the sentence without putting your name on it. '
        'That is why the news, essays and reports use it so much.',
    p3t='What the research says',
    p3a='The psychologist Gabriele Oettingen spent years testing positive thinking. '
        'People who only <strong>fantasised</strong> about success tended to put in less '
        'effort, and achieve less, than people who also pictured the '
        '<strong>obstacles</strong> in the way.',
    p3b='Her method, WOOP (Wish, Outcome, Obstacle, Plan), keeps the dream and adds '
        'the plan. That part of manifesting seems to work.',
    p4t='Half right is not the same as right',
    p4a='Most people do not think manifesting is magic, or that it is nonsense. They '
        'think it is <strong>half right</strong>: writing a goal down helps; the universe '
        'does not. A balanced view <strong>concedes</strong> the good point first, then '
        'says where the idea <strong>falls down</strong>.',
    p4b='It is the shape of a strong discussion answer, and of a strong essay paragraph.',

    vt1='The vocabulary of manifesting', vt2='The sceptic’s vocabulary',
    vt3='Three patterns for a claim', vt4='Adverbs that keep their distance',
    vt5='Saying what the evidence shows', vt6='Why it seems to work',
    vt7='Giving a balanced view',

    # teach-card bodies (the headword and the example stay in English)
    c1='To bring something into your life by believing in it and picturing it. The '
       'older meaning is "to show clearly".',
    c2='A board of pictures and words showing the life you want, kept where you see '
       'it every day.',
    c3='A short positive sentence about yourself, repeated in the present tense as if '
       'it were already true.',
    c4='Believing something because you want it to be true, not because the evidence '
       'says so.',
    c5='The belief that positive or negative thoughts bring positive or negative events. '
       'No scientific evidence supports it.',
    c6='A prediction that comes true because believing it changes how people behave.',
    c7='The reporting verb in the passive, then the whole claim as a clause. Also: it '
       'is claimed / believed / thought / reported that.',
    c8='The subject of the claim moves to the front. The reporting verb is passive; '
       'the infinitive carries the claim.',
    c9='For a claim about the past, use the perfect infinitive: to have done, to have '
       'made, to have sold.',
    c10='You doubt the claim, and you want the listener to know it.',
    c11='You are repeating what you heard or read, without judging it.',
    c12='A claim that has not been proved, usually about wrongdoing. Common in the news.',
    c13='A polite, precise way of saying a claim is probably false.',
    c14='Presents a conclusion carefully and leaves room to be wrong.',
    c15='Describes a pattern, not a rule. Research rarely proves "always".',
    c16='Noticing the evidence that supports what you already believe, and forgetting '
        'the rest.',
    c17='Feeling better because you expect to, not because of the treatment itself.',
    c18='Two things happening together does not mean one causes the other.',
    c19='Concedes a point in favour before you criticise.',
    c20='Introduces the weak point of an idea.',
    c21='Agrees in part, but refuses the strongest version of a claim.',

    mt1='Name it', mt2='Report it', mt3='Test it', mt4='Weigh it up',
    gt1='Claims, word by word', gt2='The balanced view, word by word',
    gh='Use the word bank. One word per gap.',
    bankLabel='Word bank:',
    gw1='"Is said to" is followed by the infinitive: to work.',
    gw2='A claim about the past takes the perfect infinitive: to have sold.',
    gw3='"It is claimed that" puts the reporting verb in the passive, then the clause.',
    gw4='"To have been translated": the perfect infinitive, in the passive, because '
        'the book did not translate itself.',
    gw5='"There’s something to be said for" concedes a point in favour.',
    gw6='"Where it falls down is" introduces the weak point.',
    gw7='"I’d stop short of" agrees in part and refuses the strongest version.',
    gw8='"It would seem that" presents a conclusion carefully.',

    ot1='Build the claim about the past', ot2='Build the distanced claim',
    oh1='Build the sentence. Every piece is used.',
    ow1='"Is thought to have sold": the reporting verb in the passive, then the perfect '
        'infinitive, because the sales are in the past.',
    oh2='Build the sentence. One piece is left over.',
    ow2='After "are believed" comes the infinitive: "to help". "That" belongs to the '
        'other pattern, "It is believed that…".',

    mtt='Match the word to its meaning',
    matchHint='Click a word, then its meaning.',
    matchWhy='All five are from this part of the lesson.',

    x1='Maya writes "I am a published author" on a card and reads it every morning. '
       'She has not finished her book yet.',
    s1='What is she using?',
    q1w='An affirmation is a positive sentence repeated as if it were already true. '
        'A vision board uses pictures.',
    x2='Tom is sure the team will reject his idea, so he presents it nervously and '
       'badly. They reject it.',
    s2='His belief changed his behaviour, and that changed the result. What is this?',
    q2w='A self-fulfilling prophecy works through behaviour: the belief changes what '
        'you do. The law of attraction claims thoughts change events directly.',
    x3='A journalist wants to report the claim without agreeing with it.',
    s3='Which sentence does that?',
    q3w='"Is claimed to" reports the claim and keeps the writer’s distance. "Is '
        'claiming" is wrong: a reporting verb in this pattern is a simple passive.',
    x4='"Lucky girl syndrome" is a TikTok version of manifesting: you tell yourself, '
       'all day, that you are lucky. The claim is about the past.',
    q4w='A claim about the past takes the perfect infinitive: is believed to have '
        'started.',
    x5='In one study, students who spent a few minutes fantasising about a perfect week '
       'ended up feeling less energetic, and achieved less.',
    s5='Which summary is the most careful?',
    q5w='"It would seem" and "can" report the finding without claiming more than one '
        'study shows. "Proves", "always" and "definitely" go too far.',
    x6='Your friend says: "I manifested this job! I wrote it in my journal every day."',
    s6='Which reply questions the claim politely?',
    q6w='The reply congratulates first, then offers another cause, carefully. "Has been '
        'proved" overclaims; "allegedly" is for unproved wrongdoing.',
    x7='Lena says manifesting works: she manifested a parking space three times this '
       'month. She drives into town every day.',
    s7='What is the most likely explanation?',
    q7w='She remembers the three days it worked and forgets the twenty days it did not. '
        'That is confirmation bias.',
    x8='In a discussion, you want to agree in part, then criticise.',
    s8='Which answer is balanced?',
    q8w='It concedes first ("something to be said for it"), then names the weak point '
        '("where it falls down is").',
    x9='A manifesting coach sells a £400 course that promises "money in thirty days".',
    s9='Which sentence reports this most carefully?',
    q9w='"Is claimed to bring" reports the promise without agreeing with it. "Was '
        'proved" and "the coach knows" both state it as fact.',

    st='Fact, or kept at a distance?',
    sh='Drag each sentence into the column it belongs in.',
    sb1='States it as fact', sb2='Keeps its distance',
    sw='A sentence keeps its distance with a passive reporting verb (is said to), a '
       'distancing adverb (supposedly) or a hedge (tends to, it would seem).',

    actTitle='Your turn: wishful thinking or real results?',
    actUse='Use at least three:',
    actSpeakBrief='In pairs or small groups. Two minutes per speaker.',
    actSpeak1='A friend is about to spend £400 on a manifesting course. Report what it '
              'claims, at a distance, and say what you would do instead.',
    actSpeak2='Choose a goal you really have. Talk it through the WOOP way: the wish, '
              'the outcome, the obstacle and the plan.',
    actSpeak3='Give the balanced view: what manifesting gets right, where it falls down, '
              'and what you would stop short of saying.',
    actWriteKind='Writing · 150–250 words',
    actWriteBrief='Write an article for a student magazine: "Manifesting: does it work?" '
                  'Report at least two claims at a distance (is said to, it is claimed '
                  'that), give the evidence, and end with your balanced view.',
    actPlaceholder='Manifesting: does it work? …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_manifestation_%s' % _c).T
    except ImportError:
        pass


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'
