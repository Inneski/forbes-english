# -*- coding: utf-8 -*-
"""Present Perfect: already, yet, just, ever, never (B1, German support).
House style 2, 28 slides.

Rebuilt 2026-11-06 from `present_perfect_test.html` (Übungsheft Teil 3), a
German-language explanation page followed by a fifteen-question test. The
explanation's four parts — when, the structure, the participle, already /
yet / just, ever / never — are rule cards before the block they serve, in
EN/DE/ES; the German line under each item is the click-to-reveal gloss,
with Spanish added. All fifteen items are kept.

Second correct answers, fixed:
  * Q5 "My favourite band have made a new album" is good British English
    (a band can take a plural verb). Now a singer.
  * Q6 "I've never ordered a taxi" and Q8 "She's never gone to see her
    friend" were both right. NEVER is now EVER, which is wrong in both; Q8
    also says "you missed her by two minutes".
  * Q10 "She already has finished her homework" is possible English. Now
    "her already homework".
  * Q11 "Have you never been to Hollywood?" is a real question (surprise).
  * Q12 "I've not ever broken a bone" is informal but correct.
Added: a gap slide (production), two sentence builds with a decoy, the two
speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_present_perfect_test.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='present_perfect_test.html',
    title='Present Perfect: already, yet, just, ever, never (B1)',
    folder='PresentPerfectTest',
    scheme='sage',
    art={
        'hero': ('travel', 'a suitcase covered in round flat travel stickers, no lettering, on an empty floor'),
        'talk': ('talk', 'two speech bubbles over a small table with two cups'),
        'a': ('build', 'three stacked blocks with a fourth being placed on top: something done, the result now'),
        'b': ('time', 'a clock whose minute hand has only just passed the hour'),
        'c': ('mountain', 'a mountain peak with a small flag planted on top and a path winding up to it'),
        'act': ('pair', 'two chairs facing each other under a world map pinned to the wall'),
    },
)


def q(stem, options, n, gl=True):
    """The key is options[0]; hs2quiz deals it to a position."""
    d = dict(stem=stem, options=options, correct=0, why='w%d' % n)
    if gl:
        d['gl'] = 'g%d' % n
    return d


A = [
    q('My dad ____ to America.', ['has gone', 'have gone', 'has go', 'has went'], 1),
    q('She ____ me the answer.', ['hasn’t given', 'haven’t given', 'hasn’t gave', 'didn’t given'], 2),
    q('____ you ____ the new Billie Eilish song?', ['Have / heard', 'Has / heard', 'Have / hear', 'Did / heard'], 3),
    q('I ____ Indian food lots of times.', ['’ve eaten', '’ve eat', '’ve ate', 'has eaten'], 4),
    q('Which sentence is correct?', ['My favourite singer has made a new album.', 'My favourite singer have made a new album.',
                                    'My favourite singer has make a new album.', 'My favourite singer has maked a new album.'], 5),
]
B = [
    q('I’ve ____ ordered a taxi. It’s outside now.', ['already', 'yet', 'just yet', 'ever'], 6),
    q('We haven’t got our tickets ____.', ['yet', 'already', 'just', 'ever'], 7),
    q('She’s ____ gone out — you missed her by two minutes.', ['just', 'yet', 'already yet', 'ever'], 8),
    q('He ____ his new computer yet, and he’s already broken it!', ['hasn’t used', 'has used', 'haven’t used', 'hasn’t use'], 9),
    q('Which sentence puts “already” in the right place?',
      ['She has already finished her homework.', 'She has finished her already homework.',
       'She has finished already her homework.', 'Already she has finished her homework.'], 10),
]
C = [
    q('Have you ____ been to Hollywood?', ['ever', 'yet', 'ago', 'not ever'], 11),
    q('I’ve ____ broken a bone.', ['never', 'ever', 'no', 'yet'], 12),
    q('Which sentence is correct?', ['She’s never met a famous person.', 'She’s never not met a famous person.',
                                    'She hasn’t never met a famous person.', 'She ever met a famous person.'], 13),
    q('____ she ever won a competition?', ['Has', 'Have', 'Is', 'Did'], 14),
    q('My aunt Jessica ____ to more than fifteen different countries!',
      ['has travelled', 'have travelled', 'has travel', 'has travelling'], 15),
]
APOS = lambda *xs: '|'.join(sorted({v for x in xs for v in (x, x.replace('’', "'"), x.replace("'", '’'))}))

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What is the most interesting place you have been to?',
        'What have you eaten today?',
        'Have you learned anything new this week?',
        'Which film have you seen more than once?',
        'What have you never done, but would like to do?',
        'Which country would you most like to visit?',
    ], 'talk', 3),
    ('rules', 'eR', 'rWhenT', [
        ('pWhen', ['rW1', 'rW2'], 'I lost my keys <strong>yesterday</strong>. → I<strong>’ve lost</strong> my keys. (I don’t have them now!)'),
    ], 'hero'),
    ('rules', 'eR', 'rFormT', [
        ('+ have / has + participle', ['rF1'], 'I<strong>’ve bought</strong> a new book.'),
        ('– haven’t / hasn’t + participle', ['rF2'], 'She <strong>hasn’t called</strong> me.'),
        ('? Have / Has … + participle?', ['rF3'], '<strong>Have</strong> you <strong>seen</strong> this film?'),
    ], None),
    ('rules', 'eR', 'rPartT', [
        ('pReg', [(None, 'walk – walked – <strong>walked</strong>'), (None, 'study – studied – <strong>studied</strong>'),
                  (None, 'travel – travelled – <strong>travelled</strong>'), 'rP1'], None),
        ('pIrr', [(None, 'go – went – <strong>gone</strong>'), (None, 'see – saw – <strong>seen</strong>'),
                  (None, 'buy – bought – <strong>bought</strong>'), (None, 'eat – ate – <strong>eaten</strong>'),
                  'rP2'], None),
    ], None),
    ('mc', 'e1', 'mcT', A, 'a', None),
    ('rules', 'eR', 'rAYJT', [
        ('already', ['rAl1', 'rAl2'], 'I’ve <strong>already</strong> washed the car.'),
        ('yet', ['rYe1', 'rYe2'], 'I haven’t done my homework <strong>yet</strong>. Have you eaten <strong>yet</strong>?'),
        ('just', ['rJu1', 'rJu2'], 'She’s <strong>just</strong> called me.'),
    ], None),
    ('mc', 'e2', 'mcT', B, 'b', 'left'),
    ('rules', 'eR', 'rENT', [
        ('ever', ['rEv1', 'rEv2'], 'Have you <strong>ever</strong> been to London?'),
        ('never', ['rNe1', 'rNe2'], 'I’ve <strong>never</strong> eaten sushi. Not: <s>I haven’t never</s> …'),
    ], 'c'),
    ('mc', 'e3', 'mcT', C, 'c', None),
    ('gap', 'e4', 'gapT', 'gHint', [
        ('I ______ (see) that film twice.', [APOS('have seen', '’ve seen')], 'gw1'),
        ('She ______ (not / finish) her report yet.', [APOS('hasn’t finished', 'has not finished')], 'gw2'),
        ('______ you ever ______ (ride) a horse?', ['Have', 'ridden'], 'gw3'),
    ]),
    ('order', 'e4', 'orderT', 'orderHint', [
        (['Have', 'you', 'ever', 'been', 'to Rome?'], ['went'], 'o1w'),
        (['I', 'haven’t', 'finished', 'my report', 'yet.'], ['never'], 'o2w'),
    ], 'act', 'left'),
    ('talk', 'eT', 'tk2T', [
        'Have you <strong>ever</strong> met a famous person?',
        'What <strong>have</strong> you <strong>already</strong> done today?',
        'What <strong>haven’t</strong> you done <strong>yet</strong> this week?',
        'What have you <strong>just</strong> finished reading or watching?',
        'Which food have you <strong>never</strong> eaten?',
        'How many countries <strong>have</strong> you <strong>travelled</strong> to?',
        'Have you <strong>ever</strong> broken a bone?',
        'What <strong>has changed</strong> in your town recently?',
    ], None, 4),
]
SPEC['chips'] = ['never', 'yet', 'have been', 'just', 'has changed', 'ever', 'already']

W = {
    'en': [
        'HE / SHE / IT → HAS. GO is irregular: go – went – GONE. WENT is the past simple.',
        'The negative with she: HASN’T + participle. give – gave – GIVEN.',
        'A question with YOU: HAVE … HEARD? hear – heard – HEARD.',
        'I + HAVE → I’VE. eat – ate – EATEN: ATE is the past simple, not the participle.',
        'A singer = she or he → HAS. make – made – MADE.',
        'ALREADY = it is done. It goes between HAVE and the participle. EVER is for questions.',
        'YET = not yet. In a negative it goes at the very end of the sentence.',
        'JUST = a moment ago. It goes between HAS and the participle.',
        'HE → HASN’T. YET at the end shows the sentence is negative.',
        'ALREADY sits between HAS and the participle: not after the participle, not first.',
        'EVER = at any time in your life, in questions. YET and AGO do not go here.',
        'NEVER = not at any time. It is already negative, so no extra NOT or NO.',
        'NEVER alone makes it negative. A double negative (“hasn’t never”) is wrong in English.',
        'SHE → HAS at the start of the question. win – won – WON.',
        'SHE → HAS. travel → TRAVELLED: British English doubles the L.',
    ],
    'de': [
        'HE / SHE / IT → HAS. GO ist unregelmäßig: go – went – GONE. WENT ist Past Simple.',
        'Verneinung mit she: HASN’T + Partizip. give – gave – GIVEN.',
        'Eine Frage mit YOU: HAVE … HEARD? hear – heard – HEARD.',
        'I + HAVE → I’VE. eat – ate – EATEN: ATE ist Past Simple, nicht das Partizip.',
        'Eine Sängerin = she oder he → HAS. make – made – MADE.',
        'ALREADY = es ist erledigt. Es steht zwischen HAVE und dem Partizip. EVER ist für Fragen.',
        'YET = noch nicht. In der Verneinung steht es ganz am Satzende.',
        'JUST = gerade eben. Es steht zwischen HAS und dem Partizip.',
        'HE → HASN’T. YET am Ende zeigt, dass der Satz verneint ist.',
        'ALREADY steht zwischen HAS und dem Partizip: nicht nach dem Partizip, nicht am Anfang.',
        'EVER = jemals, in Fragen. YET und AGO passen hier nicht.',
        'NEVER = noch nie. Es ist schon verneint, also kein zusätzliches NOT oder NO.',
        'NEVER allein verneint den Satz. Eine doppelte Verneinung („hasn’t never“) ist auf Englisch falsch.',
        'SHE → HAS am Anfang der Frage. win – won – WON.',
        'SHE → HAS. travel → TRAVELLED: Britisches Englisch verdoppelt das L.',
    ],
    'es': [
        'HE / SHE / IT → HAS. GO es irregular: go – went – GONE. WENT es el past simple.',
        'La negación con she: HASN’T + participio. give – gave – GIVEN.',
        'Una pregunta con YOU: HAVE … HEARD? hear – heard – HEARD.',
        'I + HAVE → I’VE. eat – ate – EATEN: ATE es el past simple, no el participio.',
        'Una cantante = she o he → HAS. make – made – MADE.',
        'ALREADY = ya está hecho. Va entre HAVE y el participio. EVER es para preguntas.',
        'YET = todavía no. En una negación va al final de la oración.',
        'JUST = hace un momento. Va entre HAS y el participio.',
        'HE → HASN’T. YET al final muestra que la oración es negativa.',
        'ALREADY va entre HAS y el participio: no después del participio, no al principio.',
        'EVER = alguna vez en la vida, en preguntas. YET y AGO no van aquí.',
        'NEVER = nunca. Ya es negativo, así que sin NOT ni NO.',
        'NEVER solo ya hace la oración negativa. La doble negación («hasn’t never») es incorrecta en inglés.',
        'SHE → HAS al principio de la pregunta. win – won – WON.',
        'SHE → HAS. travel → TRAVELLED: el inglés británico duplica la L.',
    ],
}

T = {
    'en': dict(
        coverTitle='Present <em>Perfect</em>',
        coverSub='When to use it, how to build it, and where ALREADY, YET, JUST, EVER and NEVER go: the rules, fifteen questions and three sentences to write.',
        chipLevel='B1', chipFocus='have / has + participle', chipCount='28 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='The structure', e2='Already · yet · just',
        e3='Ever · never', e4='Your turn', tk1T='Let’s talk!', tk2T='Let’s talk!',
        rWhenT='When do you use it?', pWhen='Present perfect',
        rW1='Something happened in the past, but you don’t say WHEN.',
        rW2='Or the result is still important NOW.',
        rFormT='The structure',
        rF1='I / you / we / they HAVE; he / she / it HAS. Short: I’VE, SHE’S.',
        rF2='HAVEN’T / HASN’T + the participle.',
        rF3='HAVE / HAS goes first, then the subject, then the participle.',
        rPartT='The participle: the third form', pReg='Regular: + -ed', pIrr='Irregular: learn it',
        rP1='Regular verbs: base + -ED, the same as the past simple.',
        rP2='Irregular verbs: the third form in the verb list. Learn them by heart.',
        rAYJT='Already, yet, just: position is everything',
        rAl1='= it is done.', rAl2='Between HAVE / HAS and the participle.',
        rYe1='= not yet (negative) or by now (question).', rYe2='Always at the END of the sentence.',
        rJu1='= a moment ago.', rJu2='Between HAVE / HAS and the participle.',
        rENT='Ever, never: experiences in your life',
        rEv1='= at any time in your life. In questions.', rEv2='Between HAVE / HAS and the participle.',
        rNe1='= not at any time. In positive sentences!', rNe2='NEVER is already negative: no extra NOT.',
        mcT='Choose the right answer', gapT='Write the verb', gHint='Use the present perfect of the verb in brackets.',
        gw1='I + HAVE + SEEN (see – saw – SEEN): “I’ve seen”.',
        gw2='SHE + HASN’T + FINISHED. YET at the end shows it is negative.',
        gw3='A question: HAVE + you + EVER + RIDDEN (ride – rode – RIDDEN).',
        orderT='Build the sentence', orderHint='Click the pieces in order. One piece is left over.',
        o1w='HAVE + subject + EVER + BEEN. WENT is the past simple, so it is left over.',
        o2w='HAVEN’T + participle … YET at the end. NEVER is left over: with HAVEN’T it would be a double negative.',
        actTitle='Things I have done', actUse='Use at least three:',
        actSpeakBrief='In pairs. Find out about your partner’s life and week.',
        actSpeak1='Ask three questions with HAVE YOU EVER …? Ask one more question about each “yes”.',
        actSpeak2='Tell your partner two things you have ALREADY done this week and two you HAVEN’T done YET.',
        actSpeak3='What have you JUST finished, bought or started? Tell your partner about it.',
        actWriteKind='Writing',
        actWriteBrief='Write a post for a travel website (120–150 words): places you HAVE BEEN to, something you have NEVER done but want to do, and what you have JUST planned.',
        actPlaceholder='I’ve been to …',
    ),
    'de': dict(
        coverTitle='Present <em>Perfect</em>',
        coverSub='Wann man es benutzt, wie man es bildet und wo ALREADY, YET, JUST, EVER und NEVER stehen: die Regeln, fünfzehn Fragen und drei Sätze zum Schreiben.',
        chipLevel='B1', chipFocus='have / has + Partizip', chipCount='28 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Die Struktur', e2='Already · yet · just',
        e3='Ever · never', e4='Du bist dran', tk1T='Sprechen wir!', tk2T='Sprechen wir!',
        rWhenT='Wann benutzt du es?', pWhen='Present Perfect',
        rW1='Etwas ist in der Vergangenheit passiert, aber du sagst nicht, WANN.',
        rW2='Oder das Ergebnis ist JETZT noch wichtig.',
        rFormT='Die Struktur',
        rF1='I / you / we / they HAVE; he / she / it HAS. Kurz: I’VE, SHE’S.',
        rF2='HAVEN’T / HASN’T + Partizip.',
        rF3='HAVE / HAS kommt zuerst, dann das Subjekt, dann das Partizip.',
        rPartT='Das Partizip: die dritte Form', pReg='Regelmäßig: + -ed', pIrr='Unregelmäßig: lernen',
        rP1='Regelmäßige Verben: Grundform + -ED, wie im Past Simple.',
        rP2='Unregelmäßige Verben: die dritte Form aus der Verbliste. Auswendig lernen!',
        rAYJT='Already, yet, just: Die Position ist alles',
        rAl1='= schon, es ist erledigt.', rAl2='Zwischen HAVE / HAS und dem Partizip.',
        rYe1='= noch nicht (Verneinung) oder schon (Frage).', rYe2='Immer am ENDE des Satzes.',
        rJu1='= gerade eben.', rJu2='Zwischen HAVE / HAS und dem Partizip.',
        rENT='Ever, never: Erlebnisse im Leben',
        rEv1='= jemals. In Fragen.', rEv2='Zwischen HAVE / HAS und dem Partizip.',
        rNe1='= noch nie. In positiven Sätzen!', rNe2='NEVER ist schon verneint: kein zusätzliches NOT.',
        mcT='Wähle die richtige Antwort', gapT='Schreib das Verb', gHint='Setze das Verb in Klammern ins Present Perfect.',
        gw1='I + HAVE + SEEN (see – saw – SEEN): „I’ve seen“.',
        gw2='SHE + HASN’T + FINISHED. YET am Ende zeigt die Verneinung.',
        gw3='Eine Frage: HAVE + you + EVER + RIDDEN (ride – rode – RIDDEN).',
        orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
        o1w='HAVE + Subjekt + EVER + BEEN. WENT ist Past Simple und bleibt übrig.',
        o2w='HAVEN’T + Partizip … YET am Ende. NEVER bleibt übrig: Mit HAVEN’T wäre es eine doppelte Verneinung.',
        actTitle='Was ich schon erlebt habe', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit. Findet etwas über das Leben und die Woche des anderen heraus.',
        actSpeak1='Stell drei Fragen mit HAVE YOU EVER …? Stell zu jedem „Ja“ eine weitere Frage.',
        actSpeak2='Erzähl deinem Partner zwei Dinge, die du diese Woche schon gemacht hast (ALREADY), und zwei, die du noch nicht gemacht hast (HAVEN’T … YET).',
        actSpeak3='Was hast du gerade eben beendet, gekauft oder angefangen (JUST)? Erzähl davon.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einen Beitrag für eine Reise-Website (120–150 Wörter): Orte, an denen du warst (HAVE BEEN), etwas, das du noch nie gemacht hast (NEVER) und machen willst, und was du gerade geplant hast (JUST).',
        actPlaceholder='I’ve been to …',
    ),
    'es': dict(
        coverTitle='Present <em>Perfect</em>',
        coverSub='Cuándo se usa, cómo se forma y dónde van ALREADY, YET, JUST, EVER y NEVER: las reglas, quince preguntas y tres oraciones para escribir.',
        chipLevel='B1', chipFocus='have / has + participio', chipCount='28 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='La estructura', e2='Already · yet · just',
        e3='Ever · never', e4='Tu turno', tk1T='¡A conversar!', tk2T='¡A conversar!',
        rWhenT='¿Cuándo se usa?', pWhen='Present perfect',
        rW1='Algo pasó en el pasado, pero no dices CUÁNDO.',
        rW2='O el resultado todavía es importante AHORA.',
        rFormT='La estructura',
        rF1='I / you / we / they HAVE; he / she / it HAS. Corto: I’VE, SHE’S.',
        rF2='HAVEN’T / HASN’T + el participio.',
        rF3='Primero HAVE / HAS, después el sujeto y después el participio.',
        rPartT='El participio: la tercera forma', pReg='Regulares: + -ed', pIrr='Irregulares: a memorizar',
        rP1='Verbos regulares: forma base + -ED, igual que el past simple.',
        rP2='Verbos irregulares: la tercera forma de la lista. Hay que aprenderla de memoria.',
        rAYJT='Already, yet, just: la posición lo es todo',
        rAl1='= ya, está hecho.', rAl2='Entre HAVE / HAS y el participio.',
        rYe1='= todavía no (negación) o ya (pregunta).', rYe2='Siempre al FINAL de la oración.',
        rJu1='= hace un momento.', rJu2='Entre HAVE / HAS y el participio.',
        rENT='Ever, never: experiencias de la vida',
        rEv1='= alguna vez. En preguntas.', rEv2='Entre HAVE / HAS y el participio.',
        rNe1='= nunca. ¡En oraciones afirmativas!', rNe2='NEVER ya es negativo: sin NOT.',
        mcT='Elige la respuesta correcta', gapT='Escribe el verbo', gHint='Pon el verbo entre paréntesis en present perfect.',
        gw1='I + HAVE + SEEN (see – saw – SEEN): «I’ve seen».',
        gw2='SHE + HASN’T + FINISHED. YET al final muestra la negación.',
        gw3='Una pregunta: HAVE + you + EVER + RIDDEN (ride – rode – RIDDEN).',
        orderT='Construye la oración', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
        o1w='HAVE + sujeto + EVER + BEEN. WENT es el past simple, así que sobra.',
        o2w='HAVEN’T + participio … YET al final. Sobra NEVER: con HAVEN’T sería una doble negación.',
        actTitle='Cosas que he hecho', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas. Descubran cosas de la vida y la semana del otro.',
        actSpeak1='Haz tres preguntas con HAVE YOU EVER …? Haz una pregunta más por cada «sí».',
        actSpeak2='Cuéntale a tu compañero dos cosas que ya has hecho esta semana (ALREADY) y dos que todavía no has hecho (HAVEN’T … YET).',
        actSpeak3='¿Qué acabas de terminar, comprar o empezar (JUST)? Cuéntaselo a tu compañero.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe una entrada para una web de viajes (120–150 palabras): lugares donde has estado (HAVE BEEN), algo que nunca has hecho (NEVER) y quieres hacer, y lo que acabas de planear (JUST).',
        actPlaceholder='I’ve been to …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

GLOSS = {
    'de': dict(
        g1='Mein Vater ist nach Amerika gegangen.', g2='Sie hat mir die Antwort nicht gegeben.',
        g3='Hast du das neue Lied von Billie Eilish gehört?', g4='Ich habe schon oft indisch gegessen.',
        g5='Welcher Satz ist richtig?', g6='Ich habe schon ein Taxi bestellt. Es steht jetzt draußen.',
        g7='Wir haben unsere Tickets noch nicht.', g8='Sie ist gerade eben weggegangen — du hast sie um zwei Minuten verpasst.',
        g9='Er hat seinen neuen Computer noch nicht benutzt, und er hat ihn schon kaputt gemacht!',
        g10='Welcher Satz hat „already“ an der richtigen Stelle?', g11='Bist du jemals in Hollywood gewesen?',
        g12='Ich habe mir noch nie einen Knochen gebrochen.', g13='Welcher Satz ist richtig?',
        g14='Hat sie jemals einen Wettbewerb gewonnen?', g15='Meine Tante Jessica ist in mehr als fünfzehn verschiedene Länder gereist!',
    ),
    'es': dict(
        g1='Mi padre se ha ido a Estados Unidos.', g2='No me ha dado la respuesta.',
        g3='¿Has escuchado la nueva canción de Billie Eilish?', g4='He comido comida india muchas veces.',
        g5='¿Qué oración es correcta?', g6='Ya he pedido un taxi. Está fuera.',
        g7='Todavía no tenemos las entradas.', g8='Acaba de salir: la has perdido por dos minutos.',
        g9='Todavía no ha usado su ordenador nuevo, ¡y ya lo ha roto!',
        g10='¿Qué oración pone «already» en el lugar correcto?', g11='¿Has estado alguna vez en Hollywood?',
        g12='Nunca me he roto un hueso.', g13='¿Qué oración es correcta?',
        g14='¿Ha ganado alguna vez un concurso?', g15='¡Mi tía Jessica ha viajado a más de quince países!',
    ),
}

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T, GLOSS)
