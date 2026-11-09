# -*- coding: utf-8 -*-
"""Grammar Dojo — Exercises: Should Have, Must & Have To (A2-B1, German
support). House style 2, 19 slides, on the Taekwondo/ plates.

Rebuilt 2026-11-06 from `taekwondo-exercises.html`, fifteen one-at-a-time
items (multiple choice, typed answers, word order) with a German line under
each. All fifteen are kept; the German line is the click-to-reveal gloss,
with Spanish added. The art is the family's own: Taekwondo/hero, solo_kick,
pads_drill and handshake.

Fixed:
  * The four should-have items had the key as the only long option
    ("should have kept" against "must keep", "had kept"). The distractors
    are now wrong forms of the same length.
  * The typed items gave their meaning only in German ("We ___ — fighting!
    (Wir dürfen nicht aufgeben!)"), which a Spanish or English learner
    cannot answer. Each now carries the verb in brackets.
  * "I ___ not so nervous!" expected "should not have been" while the
    sentence already printed "not". The NOT is in the brackets now.
  * The must / have to items are kept, but their explanations say HAVE TO
    is the natural choice for a rule from outside, not that MUST is wrong:
    "Visitors must bow" is good English on a sign.
Added: two should-have gaps, decoys on two builds, speaking, activation.

Run from the repo root:  py lesson-template/build/build_taekwondo_exercises.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='taekwondo-exercises.html',
    title='Grammar Dojo — Should Have, Must & Have To (A2–B1)',
    folder='Taekwondo',
    scheme='rose',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09). Two live Taekwondo
    # plates plus Midjourney renders (his style images, --stylize 200, the
    # live plates' slate blue / coral / cream named in the prompt).
    plates={
        'hero': 'a black belt in a fighting stance, a red sun behind',
        'pads_drill': 'a coach holding pads for a student’s kick',
        'x-talk': 'two taekwondo students stretching on mats before training, talking',
        'x-guard': 'a sparring fighter dropping his guard as a kick comes at his head',
        'x-late': 'a fighter kicking a moment too late as the opponent steps away',
        'x-sparring': 'two students in headguards sparring in a dojo, a coach watching',
        'x-feet': 'a fighter caught flat-footed, the opponent darting round him',
        'o-bow': 'students bowing as they step into a dojo',
        'o-dobok': 'a white dobok and a belt laid out neatly on a changing-room bench',
        'o-pushups': 'a tired student doing push-ups on the dojo mat after training',
        'x-patterns': 'a row of students practising a pattern together in a calm dojo',
        'x-regret': 'a student sitting alone on the dojo floor, head in hands, after losing',
        'x-harder': 'a determined student kicking a heavy bag late at night',
        'x-talk2': 'a coach and a student talking on the dojo bench after a match',
        'x-results': 'a pair of sparring gloves and a headguard on a dojo mat',
    },
    pop={'hero': (None, 'square'), 'x-harder': (None, 'free'), 'x-talk2': (None, 'free')},
    results='x-results',
)


def q(stem, options, n, gl):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n, gl=gl)


REGRET = [
    q('I ____ my guard up!', ['should have kept', 'should have keep', 'should has kept', 'should had kept'], 1, 'g1'),
    q('I ____ earlier!', ['should have kicked', 'should have kick', 'should has kicked', 'should had kicked'], 2, 'g2'),
    q('We ____ more sparring.', ['should have practised', 'should have practise', 'should has practised', 'should had practised'], 3, 'g3'),
    q('I ____ my feet faster!', ['should have moved', 'should have move', 'should has moved', 'should had moved'], 4, 'g4'),
]
MIXED = [
    q('“I ____ train harder.” — You WANT to; it comes from you.', ['must', 'must to', 'has to', 'musts'], 11, 'g11'),
    q('“She ____ bow to the coach.” — It is a dojo RULE.', ['has to', 'have to', 'should have', 'had'], 12, 'g12'),
    q('“We ____ fight today — just patterns!” — The coach said so.', ['don’t have to', 'mustn’t', 'shouldn’t have', 'don’t must'], 13, 'g13'),
    q('Which sentence is a past regret?', ['I should have listened.', 'I must have listened.', 'I have to listened.', 'I should listen.'], 15, 'g15'),
]
APOS = lambda *xs: '|'.join(sorted({v for x in xs for v in (x, x.replace('’', "'"), x.replace("'", '’'))}))

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Do you do a sport or a martial art?',
        'What rules are there where you train or work?',
        'What do you have to do every morning?',
        'What must you do better this year?',
        'What should you have done differently last week?',
        'Who is the strictest coach or teacher you have had?',
    ], 'x-talk', 3),
    ('stage',),
    ('rules', 'eR', 'rT', [
        ('should have + participle', ['rS1'], 'I <strong>should have kept</strong> my guard up! · I <strong>shouldn’t have jumped</strong>.'),
        ('must + verb', ['rM1', 'rM2'], 'I <strong>must train</strong> harder. · We <strong>mustn’t give up</strong>!'),
        ('have to / has to + verb', ['rH1', 'rH2'], 'We <strong>have to bow</strong>. · I <strong>had to do</strong> 50 push-ups.'),
    ], None),
    ('mc', 'e1', 'mcT', REGRET, ['x-guard', 'x-late', 'x-sparring', 'x-feet'], None),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('I ______ (must / train) harder every day!', ['must train'], 'w5'),
        ('She ______ (must / practise) her roundhouse kick.', ['must practise|must practice'], 'w6'),
        ('We ______ (must not / give up) — keep fighting!', [APOS('must not give up', 'mustn’t give up')], 'w7'),
    ]),
    ('stage',),
    ('order', 'e3', 'orderT', 'orderHint', [
        (['We', 'have to', 'bow', 'when we enter', 'the dojo.'], ['has to'], 'w8'),
        (['He', 'has to', 'wear', 'a white', 'dobok.'], ['have to'], 'w9'),
        (['I', 'had to do', '50 push-ups', 'after training.'], None, 'w10'),
    ], ['o-bow', 'o-dobok', 'o-pushups'], None),
    ('mc', 'e4', 'mcT', MIXED, ['x-harder', 'pads_drill', 'x-patterns', 'x-regret'], None),
    ('gap', 'e1', 'gapT', 'gHint2', [
        ('I ______ (not / be) so nervous!', [APOS('shouldn’t have been', 'should not have been')], 'w14'),
        ('You ______ (listen) to the coach!', ['should have listened'], 'gw1'),
        ('We ______ (not / jump) — it was too risky.', [APOS('shouldn’t have jumped', 'should not have jumped')], 'gw2'),
    ]),
    ('talk', 'eT', 'tk2T', [
        'What <strong>should</strong> you <strong>have done</strong> at your last training or meeting?',
        'What do you <strong>have to</strong> wear for your sport or job?',
        'What <strong>must</strong> you remember before an important day?',
        'What did you <strong>have to</strong> do as a child that you hated?',
        'What <strong>don’t</strong> you <strong>have to</strong> do at the weekend?',
        'What <strong>shouldn’t</strong> you <strong>have said</strong> once?',
    ], 'x-talk2', 3),
]
SPEC['chips'] = ['must', 'should have', 'don’t have to', 'had to', 'shouldn’t have', 'has to']

W = {
    'en': [
        'A past regret: SHOULD HAVE + the past participle → SHOULD HAVE KEPT.',
        'SHOULD HAVE + participle: kick → KICKED.',
        'SHOULD HAVE + participle: practise → PRACTISED. HAVE never changes to HAS after SHOULD.',
        'SHOULD HAVE + participle: move → MOVED.',
        'Your own decision: MUST + the base verb → MUST TRAIN.',
        'MUST + the base verb: MUST PRACTISE (American: practice).',
        'Forbidden by yourself: MUST NOT / MUSTN’T + base verb → MUSTN’T GIVE UP.',
        'A rule from outside: WE HAVE TO + verb. With WE it is HAVE, so HAS TO is left over.',
        'HE / SHE → HAS TO. HAVE TO is left over.',
        'The past of both MUST and HAVE TO is HAD TO.',
        'It comes from you: MUST. (HAVE TO is also possible, but MUST says it is your own wish.)',
        'A rule from outside: HAS TO is the natural choice. (A written rule can say MUST: “Students must bow.”)',
        'No need: DON’T HAVE TO. MUSTN’T would mean fighting is forbidden.',
        'A past regret about yourself: SHOULDN’T HAVE BEEN so nervous.',
        'A regret: SHOULD HAVE + participle. MUST HAVE LISTENED is a guess, not a regret.',
    ],
    'de': [
        'Ein Bedauern über die Vergangenheit: SHOULD HAVE + Partizip → SHOULD HAVE KEPT („hätte … halten sollen“).',
        'SHOULD HAVE + Partizip: kick → KICKED.',
        'SHOULD HAVE + Partizip: practise → PRACTISED. Nach SHOULD wird HAVE nie zu HAS.',
        'SHOULD HAVE + Partizip: move → MOVED.',
        'Dein eigener Wille: MUST + Grundform → MUST TRAIN.',
        'MUST + Grundform: MUST PRACTISE (amerikanisch: practice).',
        'Selbst verboten: MUST NOT / MUSTN’T + Grundform → MUSTN’T GIVE UP („wir dürfen nicht aufgeben“).',
        'Eine Regel von außen: WE HAVE TO + Verb. Bei WE heißt es HAVE, also bleibt HAS TO übrig.',
        'HE / SHE → HAS TO. HAVE TO bleibt übrig.',
        'Die Vergangenheit von MUST und HAVE TO ist HAD TO („musste“).',
        'Es kommt von dir: MUST. (HAVE TO geht auch, aber MUST sagt, dass es dein eigener Wunsch ist.)',
        'Eine Regel von außen: HAS TO ist die natürliche Wahl. (Eine schriftliche Regel kann MUST sagen: „Students must bow.“)',
        'Nicht nötig: DON’T HAVE TO („müssen nicht“). MUSTN’T hieße, Kämpfen ist verboten („dürfen nicht“).',
        'Ein Bedauern über dich selbst: SHOULDN’T HAVE BEEN so nervous („hätte nicht so nervös sein sollen“).',
        'Ein Bedauern: SHOULD HAVE + Partizip. MUST HAVE LISTENED ist eine Vermutung, kein Bedauern.',
    ],
    'es': [
        'Un lamento sobre el pasado: SHOULD HAVE + participio → SHOULD HAVE KEPT («debería haber mantenido»).',
        'SHOULD HAVE + participio: kick → KICKED.',
        'SHOULD HAVE + participio: practise → PRACTISED. Después de SHOULD, HAVE nunca cambia a HAS.',
        'SHOULD HAVE + participio: move → MOVED.',
        'Tu propia decisión: MUST + verbo base → MUST TRAIN.',
        'MUST + verbo base: MUST PRACTISE (en EE. UU.: practice).',
        'Te lo prohíbes tú: MUST NOT / MUSTN’T + verbo base → MUSTN’T GIVE UP («no podemos rendirnos»).',
        'Una regla de fuera: WE HAVE TO + verbo. Con WE es HAVE, así que sobra HAS TO.',
        'HE / SHE → HAS TO. Sobra HAVE TO.',
        'El pasado de MUST y de HAVE TO es HAD TO («tuve que»).',
        'Viene de ti: MUST. (HAVE TO también es posible, pero MUST dice que es tu propio deseo.)',
        'Una regla de fuera: HAS TO es lo natural. (Una norma escrita puede decir MUST: «Students must bow».)',
        'No hace falta: DON’T HAVE TO («no tenemos que»). MUSTN’T significaría que pelear está prohibido.',
        'Un lamento sobre ti mismo: SHOULDN’T HAVE BEEN so nervous («no debería haber estado tan nervioso»).',
        'Un lamento: SHOULD HAVE + participio. MUST HAVE LISTENED es una suposición, no un lamento.',
    ],
}

T = {
    'en': dict(
        coverTitle='Grammar Dojo: <br><em>Exercises</em>',
        coverSub='Should have, must and have to, trained the taekwondo way: fifteen moves to choose, type and build, then your own.',
        chipLevel='A2–B1', chipFocus='should have · must · have to', chipCount='19 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Should have', e2='Must', e3='Have to', e4='Must or have to?',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the right form',
        rT='Three super moves',
        rS1='Regret: you wish you had done something differently.',
        rM1='It comes from YOU: your own feeling or wish.', rM2='No past form: use HAD TO.',
        rH1='It comes from OUTSIDE: a rule, a coach, a teacher.', rH2='HE / SHE HAS TO. The past is HAD TO.',
        gapT='Write the missing words', gHint='Use the words in brackets.', gHint2='A regret: SHOULD (NOT) HAVE + the verb in brackets.',
        gw1='A regret: SHOULD HAVE LISTENED.', gw2='A regret about something you did: SHOULDN’T HAVE JUMPED.',
        orderT='Build the sentence', orderHint='Click the pieces in order. Sometimes one piece is left over.',
        actTitle='After the match', actUse='Use at least three:',
        actSpeakBrief='In pairs: one of you is a coach, the other has just lost a match.',
        actSpeak1='Athlete: say three things you SHOULD HAVE done differently.',
        actSpeak2='Coach: say what the athlete MUST do now, and what they HAVE TO do before the next match.',
        actSpeak3='Swap roles. Talk about a real day when something went wrong.',
        actWriteKind='Writing',
        actWriteBrief='Write a short training diary entry (80–100 words) after a hard day: what you SHOULD HAVE done, what you MUST do tomorrow, and what you HAVE TO do because of the rules.',
        actPlaceholder='Today I should have …',
    ),
    'de': dict(
        coverTitle='Grammar Dojo: <br><em>Exercises</em>',
        coverSub='Should have, must und have to, trainiert wie im Taekwondo: fünfzehn Moves zum Wählen, Tippen und Bauen, dann deine eigenen.',
        chipLevel='A2–B1', chipFocus='should have · must · have to', chipCount='19 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Should have', e2='Must', e3='Have to', e4='Must oder have to?',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die richtige Form',
        rT='Drei Super-Moves',
        rS1='Bedauern: Du wünschst, du hättest etwas anders gemacht („hätte … sollen“).',
        rM1='Kommt von DIR: dein eigenes Gefühl, dein Wunsch.', rM2='Keine Vergangenheitsform: Nimm HAD TO.',
        rH1='Kommt von AUSSEN: eine Regel, ein Coach, eine Lehrerin.', rH2='HE / SHE HAS TO. Die Vergangenheit ist HAD TO.',
        gapT='Ergänze die fehlenden Wörter', gHint='Verwende die Wörter in Klammern.', gHint2='Ein Bedauern: SHOULD (NOT) HAVE + das Verb in Klammern.',
        gw1='Ein Bedauern: SHOULD HAVE LISTENED („hättest zuhören sollen“).', gw2='Ein Bedauern über etwas, das du getan hast: SHOULDN’T HAVE JUMPED.',
        orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an. Manchmal bleibt ein Teil übrig.',
        actTitle='Nach dem Kampf', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit: Eine Person ist Coach, die andere hat gerade einen Kampf verloren.',
        actSpeak1='Sportler: Sag drei Dinge, die du anders hättest machen sollen (SHOULD HAVE).',
        actSpeak2='Coach: Sag, was der Sportler jetzt tun muss (MUST) und was er vor dem nächsten Kampf tun muss (HAVE TO).',
        actSpeak3='Tauscht die Rollen. Sprecht über einen echten Tag, an dem etwas schiefging.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einen kurzen Trainingstagebuch-Eintrag (80–100 Wörter) nach einem harten Tag: was du hättest machen sollen (SHOULD HAVE), was du morgen tun musst (MUST) und was du wegen der Regeln tun musst (HAVE TO).',
        actPlaceholder='Today I should have …',
    ),
    'es': dict(
        coverTitle='Grammar Dojo: <br><em>Exercises</em>',
        coverSub='Should have, must y have to, entrenados al estilo taekwondo: quince movimientos para elegir, escribir y construir, y después los tuyos.',
        chipLevel='A2–B1', chipFocus='should have · must · have to', chipCount='19 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='Should have', e2='Must', e3='Have to', e4='¿Must o have to?',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la forma correcta',
        rT='Tres súper movimientos',
        rS1='Lamento: te gustaría haber hecho algo de otra manera («debería haber …»).',
        rM1='Viene de TI: tu propio sentimiento o deseo.', rM2='No tiene pasado: usa HAD TO.',
        rH1='Viene de FUERA: una regla, un entrenador, una profesora.', rH2='HE / SHE HAS TO. El pasado es HAD TO.',
        gapT='Escribe las palabras que faltan', gHint='Usa las palabras entre paréntesis.', gHint2='Un lamento: SHOULD (NOT) HAVE + el verbo entre paréntesis.',
        gw1='Un lamento: SHOULD HAVE LISTENED («deberías haber escuchado»).', gw2='Un lamento por algo que hiciste: SHOULDN’T HAVE JUMPED.',
        orderT='Construye la oración', orderHint='Haz clic en las piezas en orden. A veces sobra una pieza.',
        actTitle='Después del combate', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas: uno es entrenador y el otro acaba de perder un combate.',
        actSpeak1='Deportista: di tres cosas que deberías haber hecho de otra manera (SHOULD HAVE).',
        actSpeak2='Entrenador: di lo que el deportista debe hacer ahora (MUST) y lo que tiene que hacer antes del próximo combate (HAVE TO).',
        actSpeak3='Cambien los papeles. Hablen de un día real en que algo salió mal.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe una entrada corta de tu diario de entrenamiento (80–100 palabras) después de un día duro: lo que deberías haber hecho (SHOULD HAVE), lo que debes hacer mañana (MUST) y lo que tienes que hacer por las reglas (HAVE TO).',
        actPlaceholder='Today I should have …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

GLOSS = {
    'de': dict(g1='Ich hätte meine Deckung oben halten sollen!', g2='Ich hätte früher kicken sollen!',
               g3='Wir hätten mehr Sparring üben sollen.', g4='Ich hätte meine Füße schneller bewegen sollen!',
               g11='„Ich muss härter trainieren.“ — Dein eigener Wille!', g12='„Sie muss sich vor dem Coach verbeugen.“ — Das ist eine Regel!',
               g13='„Wir müssen heute nicht kämpfen — nur Formen!“ — Der Coach hat es gesagt.',
               g15='Welcher Satz drückt ein vergangenes Bedauern aus?'),
    'es': dict(g1='¡Debería haber mantenido la guardia alta!', g2='¡Debería haber pateado antes!',
               g3='Deberíamos haber practicado más combate.', g4='¡Debería haber movido los pies más rápido!',
               g11='«Tengo que entrenar más.» — ¡Es tu propia voluntad!', g12='«Tiene que hacer una reverencia al entrenador.» — ¡Es una regla!',
               g13='«Hoy no tenemos que pelear, ¡solo formas!» — Lo ha dicho el entrenador.',
               g15='¿Qué oración expresa un lamento sobre el pasado?'),
}

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T, GLOSS)
