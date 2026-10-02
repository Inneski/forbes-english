# -*- coding: utf-8 -*-
"""Interface strings for The School Visit: Correction Test (A2–B1).

English, German and Spanish (DE and ES written in-session, no native
check). A further language is one module (i18n_schoolvisit_<code>.py
exporting T) plus its code in LANGS.

NOT translated, deliberately (HOUSE-STYLE §8): every sentence to correct,
every gap sentence, every multiple-choice option — they are the English
under test. What translates is the chrome: stage names, slide titles,
instructions, the four "ask the author" prompts (the learner's own language
is the point of that section) and every explanation. Grammar forms in CAPS,
cited words in double quotes, in each language's own quotation marks.

Slide titles name the scene, never the grammar point or the answer.

The person who invited the author is "my neighbour" throughout. Innes,
2026-10-02: "take real names out" — the source sheet named a real child.
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
    coverTitle='The School Visit: <em>Correction Test</em>',
    coverSub='An author is invited to talk to a class about her book — twenty-seven things to put right before she goes',
    chipLevel='A2–B1 · Pre-intermediate', chipFocus='Error correction',
    chipCount='32 slides',

    # ── stage dividers ────────────────────────────────────────────────
    d1t='Correct the Mistakes', d1n='Part 1 · ten sentences, one error each',
    d2t='Complete the Sentences', d2n='Part 2 · eight gaps',
    d3t='Ask the Author', d3n='Part 3 · four questions from the children',
    d4t='Choose the Right Expression', d4n='Part 4 · five quick decisions',

    # ── stage eyebrows ────────────────────────────────────────────────
    e1='Correct the mistakes', e2='Complete the sentences',
    e3='Ask the author', e4='Choose the right expression',

    # ── section opener panels ─────────────────────────────────────────
    s1t='One mistake in each sentence',
    s1a='The story: my neighbour has asked me to talk about my book at her school. Every sentence below is something I said about it, and every one has exactly one mistake — the kind a Spanish speaker makes for a reason.',
    s1b='Type the whole sentence, corrected. Capitals don’t matter, a missing full stop or comma is not a mistake, and more than one correction is accepted where English allows it.',

    s2t='Fill the gap',
    s2a='Eight sentences from the same story, each with a word or a verb form missing. Where there is a verb in brackets, put it in the form the sentence needs.',
    s2b='Read the whole sentence first. The clue is usually beside the gap: “when I was young”, “when she … up”, “don’t … TV”.',

    s3t='The children have questions',
    s3a='A class of children is going to ask about the book. Each prompt gives you what a child wants to know, in your own language. Write it as a natural English question.',
    s3b='Short and direct is right: children don’t ask in long sentences. A question mark at the end is fine with or without.',

    s4t='Two ways to say it — one is English',
    s4a='Five quick decisions on the points the test keeps coming back to: SAY and TELL, TO and FOR, and where the subject of a sentence goes.',
    s4b='Pick the one that is correct English. The other is what a learner usually says.',

    # ── Part 1 · correct the mistakes: the scene, never the answer ───
    aHint='Type the corrected sentence.',
    a1t='The invitation', a2t='A warning', a3t='The synopsis',
    a4t='A difficult book', a5t='One hard page', a6t='The paragraph',
    a7t='The power cut', a8t='Evenings at home', a9t='The generator',
    a10t='Yesterday’s weather',

    a1w='WANT takes a person and a TO-infinitive: “wants me to give”. There is no “wants that I” in English.',
    a2w='TELL takes the person directly: “told me that”. SAY needs TO before the person: “said to me that”. “Said me” is never possible.',
    a3w='“The synopsis” is singular, so DOESN’T. More natural still: “There’s no problem with the synopsis of my book.”',
    a4w='A negative in the past is DIDN’T + the base verb: “didn’t understand”. “No understand” is Spanish word order.',
    a5w='DIDN’T + base verb again. If the problem is still true today, DOESN’T understand works too — “no understand” never does.',
    a6w='A purpose is TO + verb (“to explain”) or FOR + -ING (“for explaining”). FOR + base verb does not exist.',
    a7w='English uses one negative. DON’T … ANYTHING, or KNOW NOTHING — never “don’t … nothing”.',
    a8w='A habit is Present Simple: “I don’t watch”. And one negative only: “don’t watch anything” or simply “don’t watch TV”.',
    a9w='An English sentence needs a subject. “We have a generator in our house”, or “There is a generator in my house”. A place cannot be the subject of HAVE.',
    a10w='RAIN is a verb: “it was raining” (in progress all day) or “it rained”. “Was rain” mixes the two.',

    # ── Part 2 · complete the sentences ──────────────────────────────
    bHint='One answer per gap. The usual contracted forms are accepted.',
    b1t='Questions from the floor', b2t='Growing up', b3t='Television',
    b4t='The storm',

    b11w='A moment in the future, and the sweating is in progress at that moment: WILL BE + -ING, the Future Continuous.',
    b12w='“When I was young” puts the sentence in the past: HAD. “Used to have” also works.',
    b13w='After WHEN in a time clause we use the Present Simple for the future: “when she grows up”, not “will grow”.',
    b14w='A reported question: ASKED + person + WHETHER (or IF). “Asked” is in the past because the asking is over.',
    b15w='After a negative, ANY: “don’t watch any TV”. MUCH is also right — “don’t watch much TV”.',
    b16w='After a negative, ANYTHING. “I don’t watch anything on TV” — or “much”, which is also accepted.',
    b17w='A power CUT (British) or a power OUTAGE (American): the electricity stops.',
    b18w='TOLD + person: “told me she wanted”. With SAY it would be “said she wanted”, with no “me”.',

    # ── Part 3 · ask the author ───────────────────────────────────────
    cHint='Write the question in natural English.',
    c1t='What the children ask', c2t='More hands up',
    c1x='A child wants to know what inspired you to write your book.',
    c2x='A child wants to know what your book is about.',
    c3x='A child wants to know whether children can read your book too.',
    c4x='You said no. The child wants to know why.',
    c1w='WHAT + Past Simple: “What inspired you to write your book?” INSPIRE takes a person and a TO-infinitive.',
    c2w='The preposition goes at the end: “What’s your book about?” — never “About what is your book?”',
    c3w='CAN + subject + verb: “Can kids read your book too?” “Too” or “as well” at the end, or “also” before the verb.',
    c4w='“Why not?” — two words. The full question, “Why can’t they?”, is the same idea.',

    # ── Part 4 · choose the right expression ─────────────────────────
    m1t='The presentation', m2t='The interesting book', m3t='A picture',
    m4t='The diagram', m5t='At home',
    m5x='Which sentence means “We have a generator in our house” — said correctly?',
    m5s='Choose the correct sentence.',
    m1w='TELL + person: “told me about the presentation”. SAY cannot take “me” directly.',
    m2w='SAY + THAT: “said that the book was interesting”. TELL would need a person first: “told me that”.',
    m3w='Purpose with a verb: TO + base form, “to explain”. FOR + base verb is not English.',
    m4w='After an adjective like USEFUL, a purpose is FOR + -ING: “useful for explaining”. “For explain” is never right.',
    m5w='The subject is the people who own it: “We have a generator in our house”. “In our house” is a place, not a subject.',

    # ── activation ────────────────────────────────────────────────────
    actTitle='Your turn: the school visit',
    actUse='Use at least four:',
    actSpeakBrief='In pairs. One of you is the author, the other is a child in the class; swap after three questions.',
    actSpeak1='The child asks what the book is about, what inspired it, and whether children can read it. The author answers in full sentences.',
    actSpeak2='The author tells the class about the day the power went out at home — what was happening, what they did, how they felt.',
    actSpeak3='Report the conversation to a third person: “She asked me whether …”, “I told her that …”.',
    actWriteKind='Writing · 80–120 words',
    actWriteBrief='Write the opening of your talk to the class: who asked you to come, what your book is about, what inspired you to write it, and whether the children can read it. Use at least four chips.',
    actPlaceholder='Good morning, everyone. My neighbour asked me to …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_schoolvisit_%s' % _c).T
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
