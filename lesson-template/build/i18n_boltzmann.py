# -*- coding: utf-8 -*-
"""Interface strings for Are You a Boltzmann Brain? (C1).

English, German and Spanish (DE and ES written in-session, no native
check). Every string the learner reads outside the reading panels is keyed
here, so a further language is one module (i18n_boltzmann_<code>.py
exporting T) plus the code in LANGS.

NOT translated, deliberately (HOUSE-STYLE §8): the reading paragraphs on the
four panels (the C1 reading text IS the material), the headword and example
on each teach card, every question option, the gap sentences, the order
chunks, the match terms and the sort items. Situations (ctx) and stems with
no blank in them translate, as deck.mc allows. Grammar tokens in CAPS,
cited words in double quotes.
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
    coverTitle='Are You a <em>Boltzmann Brain?</em>',
    coverSub='Entropy, infinite time and the paradox that keeps cosmologists up at '
             'night, with the English of probability and speculation',
    chipLevel='C1 · Advanced', chipFocus='Probability · speculative modals',
    chipCount='35 slides',

    d1t='Are You Even Real?', d1n='Part 1 · the paradox, and the idioms that tell it',
    d2t='Glass Never Unbreaks', d2n='Part 2 · the vocabulary of order and disorder',
    d3t='Which Is More Likely?', d3n='Part 3 · the language of probability',
    d4t='Before the Beginning', d4n='Part 4 · speculating with MUST, MIGHT and CAN’T',

    e1='The paradox', e2='Entropy', e3='The odds', e4='What came before?',

    p1t='A brain that formed a second ago',
    p2t='Why a broken glass stays broken',
    p3t='One universe, or a heap of brains?',
    p4t='What happened before the Big Bang?',

    vt1='Idioms from the story', vt2='Three more idioms',
    vt3='The physics', vt4='Words for things that do not last',
    vt5='Comparing likelihood', vt6='Talking about the odds',
    vt7='Speculating about the past', vt8='Speculating about now',

    c1='Worry somebody so much that they cannot stop thinking about it.',
    c2='The main thing a person or place is known for.',
    c3='Suggest an idea or a theory for other people to consider.',
    c4='Accept something as true, or as normal, without questioning it.',
    c5='Completely finished, so you can stop thinking about it.',
    c6='Something is wrong, although it is not yet clear what.',
    c7='A measure of how disordered a system is.',
    c8='A system that no energy or matter enters or leaves.',
    c9='Move gradually in one direction, as a general rule.',
    c10='Perfect and untouched, as if completely new.',
    c11='Lasting only a very short time.',
    c12='Happening by itself, with no outside cause.',
    c13='A big difference in probability. For a small one, use SLIGHTLY or A BIT.',
    c14='Clearly first, with nothing else close.',
    c15='It could happen, but in practice it never will.',
    c16='It is probable that…',
    c17='It is possible, but very unlikely.',
    c18='It is almost sure to happen, or to be true.',
    c19='You are almost sure that it happened.',
    c20='It is possible that it happened.',
    c21='You are almost sure that it did NOT happen.',
    c22='You are almost sure that it is true now.',
    c23='It is possibly true now.',
    c24='You are almost sure that it is NOT true now.',

    mt1='Check the story', mt2='Order and disorder', mt3='How likely?',
    mt4='Speculating',

    x1='A colleague has worried about a deadline for a week and is sleeping badly.',
    s1='Which sentence describes this best?',
    q1w='"Keep somebody up at night" means worry somebody so much that they cannot stop '
        'thinking about it. Here the deadline is doing the worrying.',
    x2='Ludwig Boltzmann worked in the nineteenth century.',
    s2='According to the story, who first imagined the brains?',
    q2w='Boltzmann’s work was on entropy. The brains were put forward later, by '
        'cosmologists building on his work.',
    x3='Your flatmate says the washing-up from the party is finally finished.',
    s3='Which reply fits?',
    q3w='"Over and done with" means completely finished. "Something amiss" means '
        'something is wrong; "keeping us up at night" means worrying us.',
    x4='A sandcastle is washed away by the tide and never rebuilds itself.',
    s4='Which sentence explains this in the lesson’s terms?',
    q4w='The sand goes from order to disorder and never back: it TENDS TOWARDS '
        'disorder. Nothing here happens spontaneously in the other direction.',
    x5='Your friend describes a firework display.',
    q5w='"Ephemeral" means lasting a very short time. "Pristine" means perfect and '
        'untouched; "spontaneous" means with no outside cause.',
    x6='A weather app gives rain a 2% chance tomorrow.',
    s6='Which sentence fits the forecast?',
    q6w='Two per cent is possible but very unlikely: A SLIM CHANCE. "The odds are" '
        'and "a near certainty" both mean that rain is likely.',
    x7='Your keys were on the table this morning. Now they are gone, and only your '
       'flatmate has been home.',
    q7w='You are almost sure, and it is about the past: MUST HAVE + moved. MUST is '
        'never followed by HAD or TO.',
    x8='Boltzmann died in 1906. The term "Boltzmann brain" appeared about a '
       'century later.',
    q8w='It is impossible, because the term came after his death: CAN’T HAVE + used.',

    mtt='Match the word to its meaning',
    matchHint='Click a word, then click its meaning.',
    matchWhy='All five words come from the story. "A blip" and "a fluctuation" are '
             'both small, but a fluctuation goes up and down at random.',

    st='Probably true, or probably not?',
    sh='Drag each sentence into the column it belongs in.',
    sb1='Probably true', sb2='Probably not true',
    sw='Probably true: "the odds are", "a near certainty", "by far the most likely", '
       '"slightly more likely than not". Probably not: "a slim chance", "just very '
       'unlikely", "far less likely", "I wouldn’t bet on it".',

    gt1='Complete the sentence', gt2='MUST, MIGHT or CAN’T?',
    gh1='Use the words in the bank. One word in each gap.',
    gh2='Write one word in each gap: MUST, MIGHT or CAN’T.',
    bankLabel='Word bank:',
    gw1='A big difference in probability: VASTLY, FAR or MUCH + more likely.',
    gw2='BY FAR + the most likely: clearly first, with nothing close.',
    gw3='"The odds are that…" means "it is probable that…".',
    gw4='A SLIM chance is a small one.',
    gw5='A NEAR certainty is almost sure.',
    gw6='NOT IMPOSSIBLE, JUST SO + adjective + THAT + result.',
    gw7='Almost sure, about the past: MUST + HAVE + happened.',
    gw8='Impossible, about the past: CAN’T + HAVE + heard.',
    gw9='Possible, about the past: MIGHT (or COULD, MAY) + HAVE + caused.',
    gw10='Almost sure, about now: MUST + BE.',
    gw11='Possible, about now: MIGHT (or COULD, MAY) + BE.',
    gw12='Almost sure it is impossible: CAN’T + form.',

    ot1='Build the sentence',
    oh1='Click the pieces in order.',
    ow1='NOT IMPOSSIBLE, JUST SO + adjective + THAT + result.',
    oh2='Click the pieces in order. One piece is left over.',
    ow2='MUST HAVE + past participle. "Must had" does not exist.',

    actTitle='Your turn: are you a Boltzmann brain?',
    actUse='Use at least three:',
    actSpeakBrief='In pairs or small groups. Two minutes per speaker.',
    actSpeak1='Convince your partner that you are a real person and not a Boltzmann '
              'brain. They argue back. Say how likely each of your arguments is.',
    actSpeak2='What happened before the Big Bang? Give three possibilities, from the '
              'most likely to the least, and speculate with MUST, MIGHT and CAN’T.',
    actSpeak3='Think of something in everyday life that is not impossible, just so '
              'unlikely that nobody will ever see it. Then rank your group’s examples.',
    actWriteKind='Writing · 150–250 words',
    actWriteBrief='Write a post for a popular-science blog: "Am I a Boltzmann brain?" '
                  'Explain the paradox, how the Big Bang seemed to solve it, and why some '
                  'cosmologists are still uneasy. Use three probability phrases and two '
                  'speculative modals.',
    actPlaceholder='Am I a Boltzmann brain? …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_boltzmann_%s' % _c).T
    except ImportError:
        pass


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'
