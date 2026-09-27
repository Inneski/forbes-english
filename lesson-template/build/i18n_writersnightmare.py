# -*- coding: utf-8 -*-
"""Interface strings for The Writer's Nightmare (B2).

All eleven languages the engine offers. English is here; each other
language lives in its own module, i18n_writersnightmare_<code>.py, so one
file can be written, checked and committed at a time.

NOT translated, deliberately (HOUSE-STYLE §8): the reading passage, every
example sentence, every option and every gap sentence. Those are the
English being taught. What translates is the rule around them: vocabulary
definitions, rule text, pronunciation advice, explanations and chrome.

Grammar tokens are in CAPS and cited words in double quotes, the house rule
for every explanation and rule card.
"""
import importlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord',
        'resPerfect', 'resStrong', 'resMid', 'resLow']

LANGS = ('en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja', 'hr')

T = {}

T['en'] = dict(
    coverTitle="The Writer's <em>Nightmare</em>",
    coverSub='Creativity, the block and the blank page',
    chipLevel='B2 · Upper intermediate', chipFocus='Vocabulary · grammar · sounds',
    chipCount='38 slides',
    bankLabel='Word bank:',

    d1t='The Story', d1n='Part 1 · read',
    d2t='Key Vocabulary', d2n='Part 2 · ten words',
    d3t='Grammar Focus', d3n='Part 3 · three rules',
    d4t='Pronunciation', d4n='Part 4 · eleven words',
    d5t='The Quiz', d5n='Part 5 · eight questions',

    e1='The story', e2='Vocabulary', e3='Grammar', e4='Pronunciation', e5='Quiz',

    st1='The blank page', st2='The opposite effect', st3='A different process',
    st4='A quiet Tuesday', st5='The nightmare is over',
    storyNote='Every word in bold is taught in Part 2.',

    vt1='The block', vt2='The process', vt3='The breakthrough',
    v1='A frightening dream — or, informally, any very difficult or unpleasant situation.',
    v2='People or things that are very different are often drawn to each other.',
    v3='Always behaving or performing in the same way; regular and reliable.',
    v4='Making you extremely tired, in body or in mind.',
    v5='Very great in amount or strength; hard to manage or resist. It can be good or bad.',
    v6='Not changing; firmly set. A "fixed mindset" believes your abilities cannot grow.',
    v7='The process of developing — in size, in skill, or as a person.',
    v8='Without thinking or effort; by itself.',
    v9='Decisions you make between different options.',
    v10='People with great skill or knowledge in a subject.',
    mt='Match the meaning',
    matchHint='Click a word, then the meaning that goes with it.',
    matchWhy='Each word is defined as it is used in the story.',

    gAt='Every sentence needs a subject',
    gAa='Some languages drop the subject, because the verb ending shows who is acting. '
        'English cannot: the subject is ALWAYS there. <em>Writes every morning</em> is '
        'not a sentence. <em>She writes every morning</em> is.',
    gAb='With no real subject, English uses the dummy subject "it": '
        '<em>It is true. It is exhausting to fight the block.</em>',
    gAct='Put the subject back',
    ca1='A person does the action, so name the person.',
    ca2='The real subject, "to fight the block", moves to the end. "It" holds its place at the front.',
    ca3='Nobody is doing this. "It" fills the empty subject position.',

    gBt='Different from, to, than',
    gBa='All three exist, and they are not the same. DIFFERENT FROM is correct '
        'everywhere, so use it when in doubt.',
    gBb='Never "different of". It is a word-for-word translation, and it does not '
        'exist in English.',
    gBct='Three forms, one safe choice',
    cb1='British and American English. Always correct.',
    cb2='British English only, and informal.',
    cb3='American English, mostly before a clause.',

    gCt='Present Simple negatives',
    gCa="SUBJECT + DON'T / DOESN'T + BASE VERB. DON'T with I, you, we, they. "
        "DOESN'T with he, she, it.",
    gCb="After DOESN'T the verb never takes -S: <em>She doesn't write</em>, not "
        "<em>She doesn't writes</em>. The -S is already in DOESN'T.",
    gCct="DON'T or DOESN'T?",
    cc1='"She" takes DOESN\'T, and the verb stays "write".',
    cc2='"Experts" is plural, so DON\'T.',
    cc3='A plural subject: DON\'T + "happen", with no -S.',
    cc4='The dummy subject "it" takes DOESN\'T, like "he" and "she".',

    gt1='Find the subject', gt2='Make it negative', gt3='Put it together',
    gapHint='Type the missing word or words.',
    ga1='There is no real subject at the front, so English needs the dummy subject "it".',
    ga2='Maya is a woman, so the subject is "she". English never drops it.',
    gb1='"She" takes DOESN\'T (or DOES NOT), and the verb stays "write".',
    gb2='"Experts" is plural, so DON\'T (or DO NOT).',
    gc1='"A fixed mindset" is singular: DOESN\'T + the base verb "help", with no -S.',
    gc2='DIFFERENT FROM is always correct. DIFFERENT TO is accepted in British English. '
        'Never "different of".',

    pt1='Silent letters, hidden sounds', pt2='Where the stress falls', pt3='Endings',
    p1='Two syllables, stress on the first. The "gh" is silent: no /g/ and no /h/.',
    p2='Three syllables, stress on the second. The "x" is /gz/ and the "h" is silent.',
    p3='Stress on the first syllable, so the "x" is /ks/. When the stress falls just '
       'after "ex", as in "exhausting", it usually becomes /gz/.',
    p4='Stress on the last syllable. "wh" is just /w/, and -ED is only /d/: no extra syllable.',
    p5='Five syllables, stress on the third. The first vowel is /ɔː/, as in "law", and '
       '"-ally" is said /li/.',
    p6='Stress on the middle syllable. The first and the last are weak: /kən/ and /tənt/.',
    p7='Linked in speech, as one word. The stress is on "true", and its vowel is long.',
    p8='"ch" is /tʃ/, as in "church". -ES adds a syllable after the /dʒ/ sound.',
    p9='One syllable, ending in /θ/, as in "think": the tongue tip between the teeth. '
       'Not /t/, /s/ or /f/.',
    p10='One syllable, ending /kst/. Do not add a vowel: never "fix-ed".',
    p11='"ch" is /tʃ/, the vowel is /ɔɪ/ as in "boy", and -ES adds a syllable.',

    qt='Check yourself',
    q1s='Which sentence is correct English?',
    q2c='Which word is correct in every variety of English?',
    q3c='What does "nightmare" mean here?',
    q4c='How many syllables, and where is the stress?',
    q5c='Make the sentence negative.',
    q6s='When do people say "opposites attract"?',
    q7s='Which word ends in /θ/, the sound in "think"?',
    q8c='Which form is the verb in this sentence?',
    q1w='English always needs a subject, so the dummy subject "it" is required. After '
        'DOESN\'T the verb stays in the base form: "help", not "helps".',
    q2w='DIFFERENT FROM is correct everywhere. DIFFERENT TO is British only. '
        '"Different of" does not exist.',
    q3w='In informal English a "nightmare" is any very difficult or unpleasant situation. '
        'Nobody has to be asleep.',
    q4w='Three syllables, stress on the second: ex-HAUST-ing. The "x" is /gz/ and the '
        '"h" is silent.',
    q5w='"The changes" is plural, so DON\'T, not DOESN\'T. The verb stays in the base '
        'form: "happen".',
    q6w='"Opposites attract" means that people or things that are very different are '
        'often drawn to each other.',
    q7w='"Growth" ends in /θ/, the sound in "think": the tongue tip goes between the teeth.',
    q8w='SUBJECT + DOESN\'T + BASE VERB is the Present Simple negative. It describes a '
        'habit: something she regularly does not do.',

    actTitle='Your turn: beat the block',
    actUse='Use at least three:',
    actSpeakBrief='In pairs or small groups. Give examples, not one-word answers.',
    actSpeak1='Tell your partner about a time you were blocked — in writing, music, work '
              'or study. What did it feel like, and what finally worked?',
    actSpeak2='The story says that forcing ideas has the opposite effect. Argue for or '
              'against: can discipline produce creative work when inspiration is absent?',
    actSpeak3='"Opposites attract" comes from magnets. Think of two more English '
              'expressions from science or nature, and use each in a sentence about creativity.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief="A friend who writes has been blocked for a month. Write them an email "
                  "with advice. Describe your own routine in the Present Simple, with at "
                  "least three negatives using DON'T or DOESN'T.",
    actPlaceholder='Dear …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_writersnightmare_%s' % _c).T
    except ImportError:
        pass


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %3d keys' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else 'ok',
              ('EXTRA %s' % sorted(x)) if x else '')
