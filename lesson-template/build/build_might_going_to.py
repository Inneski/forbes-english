# -*- coding: utf-8 -*-
"""Might vs Going To (A2, German support). House style 2, 23 slides.

Rebuilt 2026-11-06 from `might_vs_going_to_test.html`, a one-question-at-a-
time scrolling test with a German line under every item ("make them house
style 2"). All fifteen items are kept, in order; the German line is now the
template's click-to-reveal gloss (a Translate button under the stem, shown
only when the menu is on Deutsch or Español), with Spanish added.

Fixed in the audit:
  * Q6 "Mum hates loud music, so she ___ like this punk song": the old
    feedback itself said ISN'T GOING TO was "also grammatically possible".
    Now the item tests the form of MIGHT NOT after "I'm not sure".
  * Q1's key ("are going to go to", 18) was the only long option. A
    distractor of the same family now matches it.
  * Q7 and Q14 accepted MIGHT as natural English ("it might rain soon").
    "I'm sure" in both stems makes GOING TO the only answer.
  * Q9 "I'm going to not help you" is grammatical (an emphatic split
    infinitive). Replaced with a distractor that is wrong.
  * Q12/13: "cinema should be the cinema" when the sentence already said
    "the cinema". Distractors rewritten.
Added: the two rules as pill-tab cards, two sentence builds with a decoy,
two speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_might_going_to.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='might_vs_going_to_test.html',
    title='Might vs Going To (A2)',
    folder='MightGoingTo',
    scheme='cool',
    art={
        'hero': ('travel', 'an open suitcase under a sky split between sun and a rain cloud'),
        'talk': ('talk', 'two speech bubbles, one holding a small sun and one a small cloud'),
        'a': ('nature', 'a small house under a sky that is half sunshine and half dark rain cloud'),
        'b': ('time', 'a wall calendar with one day ringed and the next day left blank'),
        'act': ('pair', 'two chairs at a small table with a calendar lying between two cups'),
    },
)


def q(stem, options, correct, n, gl=None):
    d = dict(stem=stem, options=options, correct=correct, why='w%d' % n)
    if gl:
        d['gl'] = gl
    return d


ITEMS_A = [
    q('I bought the tickets yesterday. We ____ the opera tonight.',
      ['might go to', 'are going to go to', 'are going to going to', 'going to go to'], 1, 1, 'g1'),
    q('There’s a 50% chance of rain. We ____ the party outside.',
      ['are going to have', 'might to have', 'might have', 'having'], 2, 2, 'g2'),
    q('Which sentence is correct?',
      ['She might to call later.', 'She mights call later.', 'She might calls later.', 'She might call later.'],
      3, 3, 'gWhich'),
    q('Which sentence is correct?',
      ['He’s going to studies tonight.', 'He’s going to study tonight.', 'He’s going to studied tonight.',
       'He going to study tonight.'], 1, 4, 'gWhich'),
    q('Jim doesn’t eat meat, so I ____ cook steak for him.',
      ['amn’t going to', '’m not going to', 'might not to', 'don’t going to'], 1, 5, 'g5'),
    q('I’m not sure about this punk song for Mum. She ____ like it.',
      ['might not', 'isn’t might', 'doesn’t might', 'might not to'], 0, 6, 'g6'),
    q('Look at those black clouds! I’m sure it ____ rain very soon.',
      ['might', '’s going to', 'might not', 'isn’t going to'], 1, 7, 'g7'),
    q('I’m not sure what I want for dinner. I ____ make pasta, or I ____ just order pizza.',
      ['am going to / am going to', 'might / might', 'might / am going to', 'going to / going to'], 1, 8, 'g8'),
]
ITEMS_B = [
    q('Put the words in order: <em>not / going / I’m / help / to / you</em>',
      ['I’m going not to help you.', 'I’m not going to help you.', 'I’m not going help to you.',
       'Not I’m going to help you.'], 1, 9, 'gOrder'),
    q('Put the words in order: <em>not / understand / might / I / the questions</em>',
      ['I not might understand the questions.', 'I might understand not the questions.',
       'I might not understand the questions.', 'I don’t might understand the questions.'], 2, 10, 'gOrder'),
    q('It’s one o’clock and the interview is at three. William ____ walk there, but he hasn’t decided yet.',
      ['’s going to', 'might', 'is might', 'going to'], 1, 11, 'g11'),
    q('Find the mistake: “We might to go to the cinema tonight.”',
      ['“might” should be “might not”', '“to” should be removed', '“go” should be “goes”',
       '“the” should be removed'], 1, 12, 'gFind'),
    q('Find the mistake: “They aren’t going to plays tennis.”',
      ['“aren’t” should be “don’t”', '“going” should be removed', '“plays” should be “play”',
       '“tennis” needs “the”'], 2, 13, 'gFind'),
    q('The weather app shows a 90% chance of sun all week. “We ____ have a great holiday — I’m sure of it!”',
      ['might', '’re going to', 'might not', 'aren’t going to'], 1, 14, 'g14'),
    q('I can’t decide what to wear. I ____ wear the blue dress, or I ____ wear the red one.',
      ['might / might', '’m going to / ’m going to', 'might / ’m going to', 'going to / might'], 0, 15, 'g15'),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What are you going to do this weekend?',
        'What might you do if the weather is bad?',
        'Have you got any plans for the summer?',
        'Do you check the weather app every day?',
        'What is something you are sure will happen this year?',
        'What is something that might happen, but you’re not sure?',
    ], 'talk', 3),
    ('rules', 'eR', 'rT', [
        ('might + verb', ['rM1', 'rM2'], 'It <strong>might rain</strong> later. It <strong>might not</strong> be cold.'),
        ('be going to + verb', ['rG1', 'rG2'], 'Look at those clouds — it’s <strong>going to rain</strong>.'),
        ('pT', ['rT1'], 'might <strong>go</strong> · going to <strong>go</strong>'),
    ], None),
    ('mc', 'e1', 'mcT', ITEMS_A, 'a', None),
    ('mc', 'e2', 'mcT', ITEMS_B, 'b', 'left'),
    ('order', 'e2', 'orderT', 'orderHint', [
        (['I’m', 'not', 'going to', 'tell', 'him.'], ['don’t'], 'o1w'),
        (['She', 'might', 'not', 'come', 'tonight.'], ['to'], 'o2w'),
    ], 'b', 'left'),
    ('talk', 'eT', 'tk2T', [
        'What <strong>are you going to</strong> cook this week?',
        'Where <strong>might</strong> you go on holiday next year?',
        'What <strong>aren’t you going to</strong> do this weekend?',
        'Look out of the window. <strong>Is it going to</strong> rain?',
        'Who <strong>might</strong> you call tonight?',
        'What job <strong>might</strong> you do in ten years?',
    ], None, 3),
]
SPEC['chips'] = ['might', '’m going to', 'might not', 'isn’t going to', 'are going to', 'might go']

W = {
    'en': [
        'The tickets are bought: a fixed plan, so ARE GOING TO GO. MIGHT would be a guess.',
        '50% is not sure: MIGHT + base verb, MIGHT HAVE. Never MIGHT TO.',
        'After MIGHT, the bare base verb: no TO, no -S, no -ED.',
        'BE + GOING TO + base verb: the ’S (= IS) must be there, and STUDY stays in its base form.',
        'A firm decision from a known fact, so GOING TO. The negative is I’M NOT GOING TO (“amn’t” does not exist).',
        'NOT SURE = MIGHT. The negative is MIGHT NOT + base verb: no DOESN’T, no TO.',
        'You can SEE it coming, and you are SURE: GOING TO. MIGHT is only a possibility.',
        '“Not sure” and two open choices: MIGHT both times.',
        'NOT goes straight after the BE form: I’M NOT GOING TO help.',
        'MIGHT NOT stays together, straight before the base verb.',
        '“Hasn’t decided yet” = a possibility, not a plan: MIGHT.',
        'MIGHT is never followed by TO: “We might go to the cinema tonight.”',
        'After GOING TO the verb stays in its base form: “They aren’t going to play tennis.”',
        '90% and “I’m sure”: strong evidence, so GOING TO.',
        '“Can’t decide”: two open possibilities, MIGHT in both gaps.',
    ],
    'de': [
        'Die Tickets sind gekauft: ein fester Plan, also ARE GOING TO GO. MIGHT wäre eine Vermutung.',
        '50 % ist nicht sicher: MIGHT + Grundform, MIGHT HAVE. Nie MIGHT TO.',
        'Nach MIGHT die reine Grundform: kein TO, kein -S, kein -ED.',
        'BE + GOING TO + Grundform: das ’S (= IS) muss da sein, und STUDY bleibt in der Grundform.',
        'Eine feste Entscheidung aufgrund einer bekannten Tatsache, also GOING TO. Die Verneinung ist I’M NOT GOING TO („amn’t“ gibt es nicht).',
        'NICHT SICHER = MIGHT. Die Verneinung ist MIGHT NOT + Grundform: kein DOESN’T, kein TO.',
        'Man SIEHT es kommen und ist SICHER: GOING TO. MIGHT ist nur eine Möglichkeit.',
        '„Nicht sicher“ und zwei offene Möglichkeiten: beide Male MIGHT.',
        'NOT steht direkt nach der BE-Form: I’M NOT GOING TO help.',
        'MIGHT NOT bleibt zusammen, direkt vor der Grundform.',
        '„Hat sich noch nicht entschieden“ = eine Möglichkeit, kein Plan: MIGHT.',
        'Nach MIGHT steht nie TO: „We might go to the cinema tonight.“',
        'Nach GOING TO bleibt das Verb in der Grundform: „They aren’t going to play tennis.“',
        '90 % und „Ich bin sicher“: starke Hinweise, also GOING TO.',
        '„Kann mich nicht entscheiden“: zwei offene Möglichkeiten, MIGHT in beiden Lücken.',
    ],
    'es': [
        'Las entradas ya están compradas: un plan fijo, así que ARE GOING TO GO. MIGHT sería una suposición.',
        'Un 50 % no es seguro: MIGHT + verbo base, MIGHT HAVE. Nunca MIGHT TO.',
        'Después de MIGHT, el verbo base sin más: sin TO, sin -S, sin -ED.',
        'BE + GOING TO + verbo base: el ’S (= IS) tiene que estar, y STUDY queda en forma base.',
        'Una decisión firme basada en un hecho conocido, así que GOING TO. La negación es I’M NOT GOING TO («amn’t» no existe).',
        'NO ESTOY SEGURO = MIGHT. La negación es MIGHT NOT + verbo base: sin DOESN’T, sin TO.',
        'Lo VES venir y estás SEGURO: GOING TO. MIGHT es solo una posibilidad.',
        '«No estoy seguro» y dos opciones abiertas: MIGHT las dos veces.',
        'NOT va justo después de la forma de BE: I’M NOT GOING TO help.',
        'MIGHT NOT va junto, justo antes del verbo base.',
        '«Aún no lo ha decidido» = una posibilidad, no un plan: MIGHT.',
        'Después de MIGHT nunca va TO: «We might go to the cinema tonight».',
        'Después de GOING TO el verbo queda en forma base: «They aren’t going to play tennis».',
        '90 % y «estoy seguro»: pruebas fuertes, así que GOING TO.',
        '«No me decido»: dos posibilidades abiertas, MIGHT en los dos huecos.',
    ],
}

T = {
    'en': dict(
        coverTitle='Might <br><em>vs Going To</em>',
        coverSub='Two ways to talk about the future: MIGHT when you’re not sure, BE GOING TO for plans and for what you can see coming.',
        chipLevel='A2', chipFocus='might · be going to', chipCount='23 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Plan or maybe?', e2='Form and word order',
        tk1T='Let’s talk!', tk2T='Let’s talk!', rT='Might or going to?',
        rM1='Maybe: about 50/50. You are not sure.',
        rM2='MIGHT + base verb: no TO, no -S. The negative is MIGHT NOT.',
        rG1='A plan you have already made, or something you can see coming.',
        rG2='AM / IS / ARE + GOING TO + base verb. Negative: ’M NOT / ISN’T / AREN’T GOING TO.',
        pT='The trick',
        rT1='Both end in the base verb. Never “might to go”, never “going to goes”.',
        mcT='Choose the right form', orderT='Build the sentence',
        orderHint='Click the pieces in order. One piece is left over.',
        o1w='I’M NOT GOING TO + verb. DON’T is left over: GOING TO never takes DO.',
        o2w='MIGHT NOT + base verb. TO is left over.',
        actTitle='Plans and maybes', actUse='Use at least three:',
        actSpeakBrief='In pairs. Talk about next weekend and next year.',
        actSpeak1='Tell your partner three things you ARE GOING TO do next weekend: real plans.',
        actSpeak2='Tell your partner two things you MIGHT do, but you’re not sure.',
        actSpeak3='Look at the weather or your calendar. Make two predictions with GOING TO and two with MIGHT.',
        actWriteKind='Writing',
        actWriteBrief='Write a message to a friend (80–100 words) about next weekend: what you ARE GOING TO do, what you MIGHT do, and what you’re NOT GOING TO do.',
        actPlaceholder='Hi Lena, …',
    ),
    'de': dict(
        coverTitle='Might <br><em>vs Going To</em>',
        coverSub='Zwei Arten, über die Zukunft zu sprechen: MIGHT, wenn du nicht sicher bist, BE GOING TO für Pläne und für das, was man kommen sieht.',
        chipLevel='A2', chipFocus='might · be going to', chipCount='23 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Plan oder vielleicht?', e2='Form und Wortstellung',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', rT='Might oder going to?',
        rM1='Vielleicht: etwa 50/50. Du bist nicht sicher.',
        rM2='MIGHT + Grundform: kein TO, kein -S. Die Verneinung ist MIGHT NOT.',
        rG1='Ein Plan, den du schon gemacht hast, oder etwas, das man kommen sieht.',
        rG2='AM / IS / ARE + GOING TO + Grundform. Verneinung: ’M NOT / ISN’T / AREN’T GOING TO.',
        pT='Der Trick',
        rT1='Beide enden mit der Grundform. Nie „might to go“, nie „going to goes“.',
        mcT='Wähle die richtige Form', orderT='Bilde den Satz',
        orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
        o1w='I’M NOT GOING TO + Verb. DON’T bleibt übrig: GOING TO nimmt nie DO.',
        o2w='MIGHT NOT + Grundform. TO bleibt übrig.',
        actTitle='Pläne und Vielleichts', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit. Sprecht über das nächste Wochenende und das nächste Jahr.',
        actSpeak1='Erzähl deinem Partner drei Dinge, die du nächstes Wochenende machst (ARE GOING TO): echte Pläne.',
        actSpeak2='Erzähl deinem Partner zwei Dinge, die du vielleicht machst (MIGHT), aber du bist nicht sicher.',
        actSpeak3='Sieh dir das Wetter oder deinen Kalender an. Mach zwei Vorhersagen mit GOING TO und zwei mit MIGHT.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einer Freundin eine Nachricht (80–100 Wörter) über das nächste Wochenende: was du machst (ARE GOING TO), was du vielleicht machst (MIGHT) und was du nicht machst (NOT GOING TO).',
        actPlaceholder='Hi Lena, …',
    ),
    'es': dict(
        coverTitle='Might <br><em>vs Going To</em>',
        coverSub='Dos formas de hablar del futuro: MIGHT cuando no estás seguro, BE GOING TO para planes y para lo que ves venir.',
        chipLevel='A2', chipFocus='might · be going to', chipCount='23 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='¿Plan o quizás?', e2='Forma y orden',
        tk1T='¡A conversar!', tk2T='¡A conversar!', rT='¿Might o going to?',
        rM1='Quizás: más o menos 50/50. No estás seguro.',
        rM2='MIGHT + verbo base: sin TO, sin -S. La negación es MIGHT NOT.',
        rG1='Un plan que ya has hecho, o algo que ves venir.',
        rG2='AM / IS / ARE + GOING TO + verbo base. Negación: ’M NOT / ISN’T / AREN’T GOING TO.',
        pT='El truco',
        rT1='Los dos terminan con el verbo base. Nunca «might to go», nunca «going to goes».',
        mcT='Elige la forma correcta', orderT='Construye la oración',
        orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
        o1w='I’M NOT GOING TO + verbo. Sobra DON’T: GOING TO nunca lleva DO.',
        o2w='MIGHT NOT + verbo base. Sobra TO.',
        actTitle='Planes y quizás', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas. Hablen del próximo fin de semana y del próximo año.',
        actSpeak1='Cuéntale a tu compañero tres cosas que vas a hacer el próximo fin de semana (ARE GOING TO): planes reales.',
        actSpeak2='Cuéntale a tu compañero dos cosas que quizás hagas (MIGHT), pero no estás seguro.',
        actSpeak3='Mira el tiempo o tu agenda. Haz dos predicciones con GOING TO y dos con MIGHT.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un mensaje a una amiga (80–100 palabras) sobre el próximo fin de semana: lo que vas a hacer (ARE GOING TO), lo que quizás hagas (MIGHT) y lo que no vas a hacer (NOT GOING TO).',
        actPlaceholder='Hola, Lena: …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

GLOSS = {
    'de': dict(
        g1='Ich habe die Tickets gestern gekauft. Heute Abend gehen wir in die Oper.',
        g2='Die Regenwahrscheinlichkeit liegt bei 50 %. Vielleicht feiern wir die Party draußen.',
        gWhich='Welcher Satz ist richtig?',
        g5='Jim isst kein Fleisch, also koche ich ihm kein Steak.',
        g6='Bei diesem Punksong für Mama bin ich mir nicht sicher. Vielleicht gefällt er ihr nicht.',
        g7='Schau dir diese schwarzen Wolken an! Ich bin sicher, dass es gleich regnet.',
        g8='Ich weiß nicht genau, was ich zum Abendessen will. Vielleicht mache ich Nudeln, oder ich bestelle einfach Pizza.',
        gOrder='Bring die Wörter in die richtige Reihenfolge.',
        g11='Es ist ein Uhr, und das Vorstellungsgespräch ist um drei. Vielleicht geht William zu Fuß, aber er hat sich noch nicht entschieden.',
        gFind='Finde den Fehler.',
        g14='Die Wetter-App zeigt die ganze Woche 90 % Sonnenwahrscheinlichkeit. „Wir werden einen tollen Urlaub haben — da bin ich sicher!“',
        g15='Ich kann mich nicht entscheiden, was ich anziehe. Vielleicht das blaue Kleid, vielleicht das rote.',
    ),
    'es': dict(
        g1='Compré las entradas ayer. Esta noche vamos a la ópera.',
        g2='Hay un 50 % de probabilidad de lluvia. Quizás hagamos la fiesta fuera.',
        gWhich='¿Qué oración es correcta?',
        g5='Jim no come carne, así que no le voy a cocinar un filete.',
        g6='No estoy seguro de esta canción punk para mamá. Puede que no le guste.',
        g7='¡Mira esas nubes negras! Seguro que llueve muy pronto.',
        g8='No sé bien qué quiero cenar. Quizás haga pasta, o quizás pida una pizza.',
        gOrder='Ordena las palabras.',
        g11='Es la una y la entrevista es a las tres. Puede que William vaya andando, pero aún no lo ha decidido.',
        gFind='Encuentra el error.',
        g14='La aplicación del tiempo da un 90 % de sol toda la semana. «Vamos a pasar unas vacaciones geniales, ¡estoy seguro!»',
        g15='No me decido qué ponerme. Quizás el vestido azul, o quizás el rojo.',
    ),
}

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T, GLOSS)
