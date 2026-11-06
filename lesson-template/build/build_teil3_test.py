# -*- coding: utf-8 -*-
"""Adverbs, Will & So / Neither (B1, German support). House style 2, 25 slides.

Rebuilt 2026-11-06 from `teil3_part2_test.html` (Übungsheft Teil 3, Part 2):
three German rule panels and a fifteen-item test, five per topic. The rules
are pill-tab cards before each block, in EN/DE/ES; the German line under
each item is the click-to-reveal gloss, with Spanish added. All fifteen
items are kept.

Fixed:
  * Q6 "I'm sure he ___ ideas": WON'T HAVE was just as correct; the reason
    ("Sam is a good friend") was only in the German line. It is in the stem.
  * Q7 "She certainly ___ to Jane's party": ISN'T COMING is correct. Now a
    wrong form ("won't to come").
  * Q4 "He ran really ___ and won": WELL is correct English, and QUICK is
    accepted informally. Both replaced with forms that do not exist.
  * Q2's explanation said "adjectives ending in -e simply add -ly: careful
    → carefully". CAREFUL ends in L; most adjectives just add -LY.
Added: a gap slide for adverbs, a sentence build for WON'T, the two
speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_teil3_test.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='teil3_part2_test.html',
    title='Adverbs, Will & So / Neither (B1)',
    folder='Teil3Test',
    scheme='rose',
    art={
        'hero': ('star', 'a shooting star over the roof of a small house at night'),
        'talk': ('talk', 'two speech bubbles above two people seen from behind, on a sofa'),
        'a': ('sport', 'a running track with one runner far ahead of the others, flat shapes'),
        'b': ('idea', 'a glass ball on a small round table, glowing softly'),
        'c': ('people', 'two figures side by side, each with an identical speech bubble'),
        'act': ('pair', 'two chairs and two cups at a small round table'),
    },
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n, gl='g%d' % n)


ADV = [
    q('She smiled ____. It was a wonderful day.', ['happily', 'happyly', 'happily’s', 'happy'], 1),
    q('He did his homework ____ and made no mistakes.', ['carefully', 'careful', 'carely', 'caringly'], 2),
    q('Which sentence is correct?', ['He speaks Italian brilliantly.', 'He speaks Italian brilliant.',
                                    'He speaks Italian brilliantely.', 'He speaks brilliantly Italian.'], 3),
    q('He ran really ____ and won the race.', ['fast', 'fastly', 'fastily', 'more fastly'], 4),
    q('It was a ____ Monday morning.', ['normal', 'normally', 'normaly', 'norm'], 5),
]
WILL = [
    q('Ask Sam — he’s always full of ideas. I’m sure he ____ some ideas about what we can do.',
      ['’ll have', '’ll has', 'won’t have', 'will having'], 6),
    q('She certainly ____ to Jane’s party — they had an argument.',
      ['won’t come', 'will come', 'won’t comes', 'won’t to come'], 7),
    q('Which sentence is correct?', ['I’ll become a famous footballer.', 'I’ll became a famous footballer.',
                                    'I’ll becoming a famous footballer.', 'I wills become a famous footballer.'], 8),
    q('It ____ fun. I won’t know anyone at the party.', ['won’t be', 'will be', 'won’t is', 'will isn’t'], 9),
    q('Perhaps I ____ at home and do my homework.', ['’ll stay', 'stays', '’ll staying', 'will stayed'], 10),
]
SO = [
    q('A: I like rap music. — B: ____', ['So do I.', 'Neither do I.', 'So have I.', 'So did I.'], 11),
    q('A: I can’t go to Dave’s party. — B: ____', ['Neither can I.', 'So can I.', 'Neither do I.', 'Neither did I.'], 12),
    q('A: I went to bed late last night. — B: ____', ['So did I.', 'So do I.', 'So have I.', 'Neither did I.'], 13),
    q('A: I haven’t got any money. — B: ____', ['Neither have I.', 'So have I.', 'Neither do I.', 'Neither did I.'], 14),
    q('A: I didn’t enjoy the book. — B: ____', ['Neither did I.', 'So did I.', 'Neither do I.', 'Neither have I.'], 15),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'How do you usually spend Saturday evenings?',
        'What do you do quickly, and what do you do slowly?',
        'What will the weather be like tomorrow?',
        'Do you like rap music?',
        'What can’t you do that you would like to do?',
        'Who in your family speaks English well?',
    ], 'talk', 3),
    ('rules', 'eR', 'rAt', [
        ('adjective + -ly', ['rA1', 'rA2'], 'quick → <strong>quickly</strong> · happy → <strong>happily</strong> · terrible → <strong>terribly</strong>'),
        ('pExc', ['rA3'], 'good → <strong>well</strong> · fast → <strong>fast</strong>'),
        ('pJob', ['rA4'], 'a <strong>careful</strong> driver · she drives <strong>carefully</strong>'),
    ], None),
    ('mc', 'e1', 'mcT', ADV, 'a', None),
    ('gap', 'e1', 'gapT', 'gHint', [
        ('She sings ______ (beautiful).', ['beautifully'], 'gw1'),
        ('He drives very ______ (careful).', ['carefully'], 'gw2'),
        ('They speak English really ______ (good).', ['well'], 'gw3'),
    ]),
    ('rules', 'eR', 'rWt', [
        ('will / ’ll + verb', ['rW1'], 'I<strong>’ll go</strong>. She<strong>’ll win</strong>.'),
        ('won’t + verb', ['rW2'], 'I <strong>won’t know</strong> anyone. It <strong>won’t be</strong> fun.'),
        ('pSame', ['rW3'], 'he <strong>will go</strong> — never “he wills go”, “he will goes”'),
    ], None),
    ('mc', 'e2', 'mcT', WILL, 'b', 'left'),
    ('order', 'e2', 'orderT', 'orderHint', [
        (['I', 'won’t', 'be', 'late', 'tomorrow.'], ['not'], 'o1w'),
    ], 'b', 'left'),
    ('rules', 'eR', 'rSt', [
        ('So + verb + I', ['rS1'], 'I like rap. — <strong>So do I.</strong>'),
        ('Neither + verb + I', ['rS2'], 'I can’t swim. — <strong>Neither can I.</strong>'),
        ('pMirror', ['rS3'], 'I <strong>went</strong> → So <strong>did</strong> I · I <strong>haven’t</strong> → Neither <strong>have</strong> I'),
    ], None),
    ('mc', 'e3', 'mcT', SO, 'c', None),
    ('talk', 'eT', 'tk2T', [
        'Tell your partner something you <strong>can’t</strong> do. Do they say “<strong>Neither can I</strong>”?',
        'What <strong>will</strong> you do tonight?',
        'Name a food you don’t like. Does your partner say “<strong>Neither do I</strong>”?',
        'What do you do <strong>well</strong>? What do you do <strong>badly</strong>?',
        'Do you drive <strong>carefully</strong>, or <strong>fast</strong>?',
        'Where <strong>will</strong> you be in five years?',
    ], None, 3),
]
SPEC['chips'] = ['well', 'won’t', 'So do I', 'carefully', 'Neither can I', 'will', 'fast']

W = {
    'en': [
        'An adjective in -Y: Y becomes -ILY. happy → HAPPILY.',
        'Most adjectives just add -LY: careful → CAREFULLY. It describes the verb DID.',
        'The adverb comes after the verb and its object: speaks Italian BRILLIANTLY. brilliant + -LY.',
        'FAST is an exception: the adjective and the adverb are the same. “Fastly” does not exist.',
        'MONDAY MORNING is a noun, so we need an adjective: NORMAL. Adjectives never take -LY.',
        'WILL / ’LL + the base verb: no -S, no -ING, the same for every person. And Sam is full of ideas.',
        'WON’T = WILL NOT, then the base verb: WON’T COME. No -S and no TO.',
        'After ’LL the verb is always the base form: BECOME, not became or becoming. “Wills” does not exist.',
        'A negative prediction: WON’T + the base form BE.',
        'PERHAPS + WILL: deciding now, not a fixed plan. ’LL + the base form STAY.',
        'A positive present simple sentence (LIKE): So + DO + I.',
        'A negative sentence with CAN’T: Neither + CAN + I. A modal is repeated; no DO.',
        'A positive past simple sentence (WENT): So + DID + I.',
        'A negative sentence with HAVEN’T: Neither + HAVE + I. Repeat HAVE, not DO.',
        'A negative past simple sentence (DIDN’T): Neither + DID + I.',
    ],
    'de': [
        'Ein Adjektiv auf -Y: Y wird zu -ILY. happy → HAPPILY.',
        'Die meisten Adjektive bekommen einfach -LY: careful → CAREFULLY. Es beschreibt das Verb DID.',
        'Das Adverb steht nach dem Verb und seinem Objekt: speaks Italian BRILLIANTLY. brilliant + -LY.',
        'FAST ist eine Ausnahme: Adjektiv und Adverb sind gleich. „Fastly“ gibt es nicht.',
        'MONDAY MORNING ist ein Nomen, also brauchen wir ein Adjektiv: NORMAL. Adjektive bekommen nie -LY.',
        'WILL / ’LL + Grundform: kein -S, kein -ING, für alle Personen gleich. Und Sam hat immer Ideen.',
        'WON’T = WILL NOT, dann die Grundform: WON’T COME. Kein -S und kein TO.',
        'Nach ’LL steht immer die Grundform: BECOME, nicht became oder becoming. „Wills“ gibt es nicht.',
        'Eine negative Vorhersage: WON’T + die Grundform BE.',
        'PERHAPS + WILL: eine Entscheidung jetzt, kein fester Plan. ’LL + die Grundform STAY.',
        'Ein positiver Satz im Present Simple (LIKE): So + DO + I.',
        'Ein negativer Satz mit CAN’T: Neither + CAN + I. Ein Modalverb wird wiederholt, kein DO.',
        'Ein positiver Satz im Past Simple (WENT): So + DID + I.',
        'Ein negativer Satz mit HAVEN’T: Neither + HAVE + I. HAVE wiederholen, nicht DO.',
        'Ein negativer Satz im Past Simple (DIDN’T): Neither + DID + I.',
    ],
    'es': [
        'Un adjetivo en -Y: la Y se vuelve -ILY. happy → HAPPILY.',
        'La mayoría de los adjetivos solo añaden -LY: careful → CAREFULLY. Describe el verbo DID.',
        'El adverbio va después del verbo y su objeto: speaks Italian BRILLIANTLY. brilliant + -LY.',
        'FAST es una excepción: el adjetivo y el adverbio son iguales. «Fastly» no existe.',
        'MONDAY MORNING es un sustantivo, así que necesitamos un adjetivo: NORMAL. Los adjetivos nunca llevan -LY.',
        'WILL / ’LL + verbo base: sin -S, sin -ING, igual para todas las personas. Y Sam siempre tiene ideas.',
        'WON’T = WILL NOT, y después el verbo base: WON’T COME. Sin -S y sin TO.',
        'Después de ’LL el verbo siempre va en forma base: BECOME, no became ni becoming. «Wills» no existe.',
        'Una predicción negativa: WON’T + la forma base BE.',
        'PERHAPS + WILL: decides ahora, no es un plan fijo. ’LL + la forma base STAY.',
        'Una oración afirmativa en present simple (LIKE): So + DO + I.',
        'Una oración negativa con CAN’T: Neither + CAN + I. El modal se repite; sin DO.',
        'Una oración afirmativa en past simple (WENT): So + DID + I.',
        'Una oración negativa con HAVEN’T: Neither + HAVE + I. Se repite HAVE, no DO.',
        'Una oración negativa en past simple (DIDN’T): Neither + DID + I.',
    ],
}

T = {
    'en': dict(
        coverTitle='Adverbs, Will <br><em>&amp; So / Neither</em>',
        coverSub='Three topics, one test: adverbs of manner (how something happens), WILL and WON’T for the future, and SO DO I / NEITHER CAN I for agreeing.',
        chipLevel='B1', chipFocus='-ly · will / won’t · so / neither', chipCount='25 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Adverbs', e2='Will / won’t', e3='So / neither',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the right answer',
        rAt='Adverbs of manner: how something happens',
        rA1='Most adjectives add -LY. An adjective in -Y takes -ILY.',
        rA2='An adjective in -LE drops the E: -LY.',
        pExc='Exceptions', rA3='GOOD → WELL. FAST stays FAST.',
        pJob='Adjective or adverb?', rA4='The adverb describes the verb; the adjective describes the noun.',
        gapT='Write the adverb', gHint='Make an adverb from the word in brackets.',
        gw1='beautiful + -LY → BEAUTIFULLY. It describes how she sings.',
        gw2='careful + -LY → CAREFULLY.',
        gw3='GOOD is irregular: the adverb is WELL.',
        rWt='Will and won’t: the future',
        rW1='Predictions and decisions you make now.',
        rW2='WON’T = WILL NOT.',
        pSame='The same for everyone', rW3='No -S, and after WILL always the base verb.',
        orderT='Build the sentence', orderHint='Click the pieces in order. One piece is left over.',
        o1w='WON’T already means WILL NOT, so NOT is left over.',
        rSt='So do I, neither can I: agreeing',
        rS1='Agree with a POSITIVE sentence.',
        rS2='Agree with a NEGATIVE sentence.',
        pMirror='The mirror', rS3='The verb copies the first sentence: DO, DID, HAVE, CAN …',
        actTitle='Me too, me neither', actUse='Use at least three:',
        actSpeakBrief='In pairs. Find out how much you have in common.',
        actSpeak1='Say five true things about you. Your partner answers with SO … I or NEITHER … I, or “Really? I don’t!”',
        actSpeak2='Describe how you do three things — drive, cook, speak English: CAREFULLY, BADLY, WELL, FAST …',
        actSpeak3='Make three predictions about next year with WILL and WON’T.',
        actWriteKind='Writing',
        actWriteBrief='Write a message to a new classmate (100–120 words): how you do things (three adverbs), what you WILL and WON’T do this weekend, and one thing you can’t do.',
        actPlaceholder='Hi Tom, …',
    ),
    'de': dict(
        coverTitle='Adverbs, Will <br><em>&amp; So / Neither</em>',
        coverSub='Drei Themen, ein Test: Adverbien der Art und Weise (wie etwas passiert), WILL und WON’T für die Zukunft, und SO DO I / NEITHER CAN I für „ich auch / ich auch nicht“.',
        chipLevel='B1', chipFocus='-ly · will / won’t · so / neither', chipCount='25 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Adverbien', e2='Will / won’t', e3='So / neither',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die richtige Antwort',
        rAt='Adverbien: wie etwas passiert',
        rA1='Die meisten Adjektive bekommen -LY. Ein Adjektiv auf -Y bekommt -ILY.',
        rA2='Ein Adjektiv auf -LE verliert das E: -LY.',
        pExc='Ausnahmen', rA3='GOOD → WELL. FAST bleibt FAST.',
        pJob='Adjektiv oder Adverb?', rA4='Das Adverb beschreibt das Verb, das Adjektiv das Nomen.',
        gapT='Schreib das Adverb', gHint='Bilde ein Adverb aus dem Wort in Klammern.',
        gw1='beautiful + -LY → BEAUTIFULLY. Es beschreibt, wie sie singt.',
        gw2='careful + -LY → CAREFULLY.',
        gw3='GOOD ist unregelmäßig: Das Adverb ist WELL.',
        rWt='Will und won’t: die Zukunft',
        rW1='Vorhersagen und Entscheidungen, die du jetzt triffst.',
        rW2='WON’T = WILL NOT.',
        pSame='Für alle gleich', rW3='Kein -S, und nach WILL immer die Grundform.',
        orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
        o1w='WON’T heißt schon WILL NOT, also bleibt NOT übrig.',
        rSt='So do I, neither can I: ich auch, ich auch nicht',
        rS1='Zustimmung zu einem POSITIVEN Satz.',
        rS2='Zustimmung zu einem NEGATIVEN Satz.',
        pMirror='Der Spiegel', rS3='Das Verb spiegelt den ersten Satz: DO, DID, HAVE, CAN …',
        actTitle='Ich auch, ich auch nicht', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit. Findet heraus, wie viel ihr gemeinsam habt.',
        actSpeak1='Sag fünf wahre Dinge über dich. Dein Partner antwortet mit SO … I oder NEITHER … I, oder „Really? I don’t!“',
        actSpeak2='Beschreib, wie du drei Dinge machst — Autofahren, Kochen, Englisch sprechen: CAREFULLY, BADLY, WELL, FAST …',
        actSpeak3='Mach drei Vorhersagen für nächstes Jahr mit WILL und WON’T.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einem neuen Mitschüler eine Nachricht (100–120 Wörter): wie du Dinge machst (drei Adverbien), was du dieses Wochenende machst und nicht machst (WILL / WON’T) und eine Sache, die du nicht kannst.',
        actPlaceholder='Hi Tom, …',
    ),
    'es': dict(
        coverTitle='Adverbs, Will <br><em>&amp; So / Neither</em>',
        coverSub='Tres temas, una prueba: adverbios de modo (cómo pasa algo), WILL y WON’T para el futuro, y SO DO I / NEITHER CAN I para decir «yo también / yo tampoco».',
        chipLevel='B1', chipFocus='-ly · will / won’t · so / neither', chipCount='25 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='Adverbios', e2='Will / won’t', e3='So / neither',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la respuesta correcta',
        rAt='Adverbios de modo: cómo pasa algo',
        rA1='La mayoría de los adjetivos añaden -LY. Un adjetivo en -Y lleva -ILY.',
        rA2='Un adjetivo en -LE pierde la E: -LY.',
        pExc='Excepciones', rA3='GOOD → WELL. FAST queda FAST.',
        pJob='¿Adjetivo o adverbio?', rA4='El adverbio describe el verbo; el adjetivo describe el sustantivo.',
        gapT='Escribe el adverbio', gHint='Forma un adverbio con la palabra entre paréntesis.',
        gw1='beautiful + -LY → BEAUTIFULLY. Describe cómo canta.',
        gw2='careful + -LY → CAREFULLY.',
        gw3='GOOD es irregular: el adverbio es WELL.',
        rWt='Will y won’t: el futuro',
        rW1='Predicciones y decisiones que tomas ahora.',
        rW2='WON’T = WILL NOT.',
        pSame='Igual para todos', rW3='Sin -S, y después de WILL siempre el verbo base.',
        orderT='Construye la oración', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
        o1w='WON’T ya significa WILL NOT, así que sobra NOT.',
        rSt='So do I, neither can I: yo también, yo tampoco',
        rS1='Para estar de acuerdo con una oración AFIRMATIVA.',
        rS2='Para estar de acuerdo con una oración NEGATIVA.',
        pMirror='El espejo', rS3='El verbo copia la primera oración: DO, DID, HAVE, CAN …',
        actTitle='Yo también, yo tampoco', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas. Descubran cuánto tienen en común.',
        actSpeak1='Di cinco cosas verdaderas sobre ti. Tu compañero responde con SO … I o NEITHER … I, o «Really? I don’t!»',
        actSpeak2='Describe cómo haces tres cosas — conducir, cocinar, hablar inglés: CAREFULLY, BADLY, WELL, FAST …',
        actSpeak3='Haz tres predicciones sobre el próximo año con WILL y WON’T.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un mensaje a un compañero nuevo (100–120 palabras): cómo haces las cosas (tres adverbios), qué harás y qué no harás este fin de semana (WILL / WON’T) y una cosa que no sabes hacer.',
        actPlaceholder='Hi Tom, …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

GLOSS = {
    'de': dict(
        g1='Sie lächelte glücklich. Es war ein wunderbarer Tag.', g2='Er machte seine Hausaufgaben sorgfältig und machte keine Fehler.',
        g3='Welcher Satz ist richtig?', g4='Er lief wirklich schnell und gewann das Rennen.', g5='Es war ein normaler Montagmorgen.',
        g6='Frag Sam — er hat immer Ideen. Ich bin sicher, dass er ein paar Ideen hat, was wir machen können.',
        g7='Sie kommt bestimmt nicht zu Janes Party — sie haben sich gestritten.', g8='Welcher Satz ist richtig?',
        g9='Das wird keinen Spaß machen. Ich werde auf der Party niemanden kennen.',
        g10='Vielleicht bleibe ich zu Hause und mache meine Hausaufgaben.',
        g11='A: Ich mag Rap. — B: Ich auch.', g12='A: Ich kann nicht zu Daves Party gehen. — B: Ich auch nicht.',
        g13='A: Ich bin gestern spät ins Bett gegangen. — B: Ich auch.', g14='A: Ich habe kein Geld. — B: Ich auch nicht.',
        g15='A: Das Buch hat mir nicht gefallen. — B: Mir auch nicht.',
    ),
    'es': dict(
        g1='Sonrió feliz. Fue un día maravilloso.', g2='Hizo los deberes con cuidado y no cometió errores.',
        g3='¿Qué oración es correcta?', g4='Corrió muy rápido y ganó la carrera.', g5='Era un lunes por la mañana normal.',
        g6='Pregúntale a Sam: siempre tiene ideas. Seguro que tiene alguna idea de lo que podemos hacer.',
        g7='Seguro que no va a la fiesta de Jane: han discutido.', g8='¿Qué oración es correcta?',
        g9='No va a ser divertido. No conoceré a nadie en la fiesta.', g10='Quizás me quede en casa y haga los deberes.',
        g11='A: Me gusta el rap. — B: A mí también.', g12='A: No puedo ir a la fiesta de Dave. — B: Yo tampoco.',
        g13='A: Anoche me acosté tarde. — B: Yo también.', g14='A: No tengo dinero. — B: Yo tampoco.',
        g15='A: No me gustó el libro. — B: A mí tampoco.',
    ),
}

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T, GLOSS)
