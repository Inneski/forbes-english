# -*- coding: utf-8 -*-
"""Skiing at the Resort (B1). House style 2, 23 slides, on the Skiing/
plates.

Rebuilt 2026-11-06 from `forbes-english-skiing-B1.html` (EN + DE): five
multiple choice, five true/false, five word-bank gaps and five sentence
builds. All twenty are kept; Spanish added. The two Skiing/ plates are
real (birch-forest cross-country for the cover, the downhill jump for a
block); the rest are stand-ins, slots prefixed b1- because the B2 skiing
page shares the folder.

Fixed: true/false 1, "You MUST wear a helmet when you go skiing", was
keyed TRUE while its own explanation said helmets are "strongly
recommended (and in many resorts required for children)" — for most adults
the statement is false. It now says SHOULD.
Added: a recap of the resort words, speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_skiing_b1.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='forbes-english-skiing-B1.html',
    title='Skiing at the Resort (B1)',
    folder='Skiing',
    hero='birch-forest-cross-country',
    cover_pos='18% 50%',
    scheme='cool',
    act='b1-act',
    art={
        'b1-talk': ('talk', 'two speech bubbles above a pair of crossed skis in the snow'),
        'b1-a': ('mountain', 'a chairlift climbing a snowy mountain, flat shapes'),
        'b1-act': ('pair', 'two chairs on a mountain hut terrace with two hot drinks'),
    },
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


MC = [
    q('You want to go to the top of the mountain. What do you take?',
      ['A chairlift or gondola that goes up the mountain', 'A taxi or a bus that drives up the mountain road',
       'A boat that takes you across the lake to the village', 'A bicycle that you pedal all the way up the hill'], 1),
    q('What do you call the clothes that keep you warm and dry in the snow?',
      ['A ski jacket, salopettes and thermal layers', 'A swimsuit and flip-flops for the cold weather',
       'A suit and tie for a formal occasion outside', 'A raincoat and wellington boots for the rain'], 2),
    q('A slope for beginners is called a “green” or “blue” run. What does this tell you?',
      ['The run is easy and gentle, good for learning', 'The slope is closed and dangerous for all skiers',
       'The slope is only for children under twelve', 'The run is very steep and only for experts'], 3),
    q('At the end of the day your friends invite you for “après-ski”. What will you do?',
      ['Have a drink or a meal with friends at the resort', 'Go to bed early because you are tired after skiing',
       'Put on your ski equipment and ski one more run', 'Buy new ski equipment for the next morning'], 4),
    q('You fall on the slope and hurt your knee. Who should you call for help?',
      ['A member of the ski patrol, who gives first aid', 'The ski instructor teaching a lesson nearby',
       'The restaurant staff in the lodge at the bottom', 'The ticket seller at the main lift station'], 5),
]
TF = [
    q('True or false? <em>You should wear a helmet when you go skiing, to protect your head.</em>', ['True', 'False'], 6),
    q('True or false? <em>A “nursery slope” is a very steep and difficult run for expert skiers.</em>', ['False', 'True'], 7),
    q('True or false? <em>Ski boots connect to the skis with a piece of equipment called a binding.</em>', ['True', 'False'], 8),
    q('True or false? <em>You can ski on any mountain in the world, even without snow.</em>', ['False', 'True'], 9),
    q('True or false? <em>A ski pass lets you use the lifts at a ski resort.</em>', ['True', 'False'], 10),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Have you ever been skiing or snowboarding?',
        'Do you prefer the mountains or the beach?',
        'What do you wear when it is very cold?',
        'Is skiing popular in your country?',
        'Would you try a ski lesson? Why, or why not?',
        'What is the coldest place you have been to?',
    ], 'b1-talk', 3),
    ('mc', 'e1', 'mcT', MC, 'b1-a', None),
    ('mc', 'e2', 'mcT2', TF, 'downhill-cliff-jump', 'left'),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('Before you can ski down the mountain, you need to buy a lift ______ at the ticket office.', ['pass'], 'w11'),
        ('The snow was very icy, so the skier lost her ______ and fell before she reached the bottom.', ['balance'], 'w12'),
        ('We rented our ______ — skis, poles and boots — from the shop next to the ski school.', ['equipment'], 'w13'),
    ], ['balance', 'equipment', 'helmet', 'pass', 'slope']),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('The afternoon was warm and the ______ started to melt, making the slope wet and heavy.', ['snow'], 'w14'),
        ('My sister signed up for a group ______ with an instructor because she had never skied before.', ['lesson'], 'w15'),
    ], ['lesson', 'resort', 'snow', 'helmet']),
    ('order', 'e4', 'orderT', 'orderHint', [
        (['She put on', 'her ski boots', 'and walked carefully', 'to the chairlift.'], None, 'w16'),
        (['The children', 'are having', 'a ski lesson', 'with their instructor', 'on the nursery slope.'], None, 'w17'),
        (['We have', 'never been', 'to a ski resort', 'before this holiday.'], None, 'w18'),
        (['You should', 'always check', 'the weather forecast', 'before going skiing', 'in the mountains.'], None, 'w19'),
        (['The resort', 'was very busy', 'because it had snowed', 'heavily the night before.'], None, 'w20'),
    ], 'b1-a', 'left'),
    ('rules', 'eR', 'recT', [
        ('pUp', [(None, 'a chairlift · a gondola'), (None, 'a lift pass / ski pass'), (None, 'a green / blue / red / black run')], None),
        ('pGear', [(None, 'a ski jacket · salopettes'), (None, 'thermal layers · a helmet'), (None, 'skis · poles · boots · bindings')], None),
        ('pPeople', [(None, 'an instructor · a group lesson'), (None, 'the ski patrol · first aid'), (None, 'the nursery slope · après-ski')], None),
    ], None),
    ('talk', 'eT', 'tk2T', [
        'Describe your perfect day at a ski <strong>resort</strong>.',
        'Would you rather take a <strong>group lesson</strong> or a private one?',
        'What would you do at <strong>après-ski</strong>?',
        'Have you ever lost your <strong>balance</strong> and fallen?',
        'Which <strong>equipment</strong> would you rent, and which would you buy?',
        'What <strong>should</strong> every beginner know before skiing?',
    ], None, 3),
]
SPEC['chips'] = ['lift pass', 'ski patrol', 'equipment', 'après-ski', 'nursery slope', 'chairlift', 'instructor']

W = {
    'en': [
        'A CHAIRLIFT or a GONDOLA (a small cabin on a cable) takes you up the mountain.',
        'A waterproof SKI JACKET, SALOPETTES (ski trousers) and THERMAL LAYERS underneath.',
        'Colours show how hard a run is: green and blue are the easiest, for beginners.',
        'APRÈS-SKI is French for “after skiing”: drinks, food and friends at the end of the day.',
        'The SKI PATROL are trained in safety and first aid on the mountain.',
        'TRUE: a helmet is strongly recommended, and many resorts require one for children.',
        'FALSE: the nursery slope is the gentlest area, where beginners learn.',
        'TRUE: BINDINGS clip the boots to the skis and release in a bad fall.',
        'FALSE: skiing needs snow, natural or made by snow machines.',
        'TRUE: a SKI PASS (lift pass) lets you use the lifts all day.',
        'A LIFT PASS is the ticket for the ski lifts.',
        'BALANCE: keeping your body stable. Ice makes it harder.',
        'EQUIPMENT: skis, poles, boots and a helmet. Many people rent it.',
        'SNOW melts when the temperature rises above zero.',
        'A ski LESSON is a class with an instructor; group lessons are cheaper.',
        'PUT ON is the phrasal verb for clothes and equipment; the past simple tells the sequence.',
        'The present continuous (ARE HAVING) for something happening now.',
        'HAVE NEVER BEEN: an experience that has not happened up to now.',
        'SHOULD + verb gives advice; BEFORE + -ING (before going).',
        'BECAUSE gives the reason; HAD SNOWED happened before the resort was busy.',
    ],
    'de': [
        'Ein CHAIRLIFT (Sessellift) oder eine GONDOLA (Gondel) bringt dich auf den Berg.',
        'Eine wasserdichte SKI JACKET, SALOPETTES (Skihose) und THERMAL LAYERS (Funktionswäsche) darunter.',
        'Farben zeigen, wie schwer eine Piste ist: Grün und Blau sind am leichtesten, für Anfänger.',
        'APRÈS-SKI heißt auf Französisch „nach dem Skifahren“: Getränke, Essen und Freunde am Ende des Tages.',
        'Die SKI PATROL (Pistenrettung) ist für Sicherheit und Erste Hilfe am Berg ausgebildet.',
        'RICHTIG: Ein Helm wird dringend empfohlen, und viele Skigebiete schreiben ihn für Kinder vor.',
        'FALSCH: Der NURSERY SLOPE (Übungshang) ist der flachste Bereich, wo Anfänger lernen.',
        'RICHTIG: BINDINGS (Bindungen) befestigen die Schuhe an den Skiern und lösen bei einem Sturz.',
        'FALSCH: Skifahren braucht Schnee, natürlichen oder aus Schneekanonen.',
        'RICHTIG: Ein SKI PASS (Skipass) erlaubt dir, den ganzen Tag die Lifte zu benutzen.',
        'Ein LIFT PASS ist die Fahrkarte für die Lifte.',
        'BALANCE: das Gleichgewicht halten. Eis macht es schwerer.',
        'EQUIPMENT: Ski, Stöcke, Schuhe und Helm (Ausrüstung). Viele leihen sie aus.',
        'SNOW (Schnee) schmilzt, wenn die Temperatur über null steigt.',
        'Eine Ski-LESSON ist eine Stunde mit einem Lehrer; Gruppenkurse sind billiger.',
        'PUT ON ist das Phrasal Verb für Kleidung und Ausrüstung; das Past Simple zeigt die Reihenfolge.',
        'Present Continuous (ARE HAVING) für etwas, das gerade passiert.',
        'HAVE NEVER BEEN: eine Erfahrung, die bis jetzt nicht passiert ist.',
        'SHOULD + Verb gibt einen Rat; BEFORE + -ING (before going).',
        'BECAUSE nennt den Grund; HAD SNOWED geschah, bevor das Skigebiet voll war.',
    ],
    'es': [
        'Un CHAIRLIFT (telesilla) o una GONDOLA (telecabina) te sube a la montaña.',
        'Una SKI JACKET impermeable, SALOPETTES (pantalón de esquí) y THERMAL LAYERS (ropa térmica) debajo.',
        'Los colores indican la dificultad: verde y azul son las pistas más fáciles, para principiantes.',
        'APRÈS-SKI significa en francés «después de esquiar»: bebidas, comida y amigos al final del día.',
        'La SKI PATROL (patrulla de pistas) está formada en seguridad y primeros auxilios.',
        'VERDADERO: el casco es muy recomendable, y muchas estaciones lo exigen a los niños.',
        'FALSO: el NURSERY SLOPE (pista de principiantes) es la zona más suave, donde se aprende.',
        'VERDADERO: las BINDINGS (fijaciones) sujetan las botas a los esquís y se sueltan en una caída.',
        'FALSO: para esquiar hace falta nieve, natural o de cañones.',
        'VERDADERO: un SKI PASS (forfait) te permite usar los remontes todo el día.',
        'Un LIFT PASS es el billete para los remontes.',
        'BALANCE: mantener el equilibrio. El hielo lo hace más difícil.',
        'EQUIPMENT: esquís, bastones, botas y casco (equipo). Mucha gente lo alquila.',
        'La SNOW (nieve) se derrite cuando la temperatura sube de cero.',
        'Una LESSON de esquí es una clase con un monitor; las de grupo son más baratas.',
        'PUT ON es el phrasal verb para ropa y equipo; el past simple da la secuencia.',
        'El present continuous (ARE HAVING) para algo que pasa ahora.',
        'HAVE NEVER BEEN: una experiencia que no ha ocurrido hasta ahora.',
        'SHOULD + verbo da un consejo; BEFORE + -ING (before going).',
        'BECAUSE da la razón; HAD SNOWED ocurrió antes de que la estación se llenara.',
    ],
}

T = {
    'en': dict(
        coverTitle='Skiing at <br><em>the Resort</em>',
        coverSub='Ski-resort English: lifts and passes, clothes and equipment, the ski patrol and après-ski — in twenty questions and sentences.',
        chipLevel='B1', chipFocus='ski-resort vocabulary', chipCount='23 slides',
        eW='Warm-up', eT='Let’s talk', eR='Review', e1='Resort vocabulary', e2='True or false?', e3='Complete the sentences', e4='Build the sentences',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best answer', mcT2='Is it true or false?',
        gapT='Complete the sentence', gHint='One word from the bank in each gap.',
        orderT='Build the sentence', orderHint='Click the pieces in order to build the sentence.',
        recT='The resort words', pUp='Going up', pGear='What you wear', pPeople='People and places',
        actTitle='The ski trip', actUse='Use at least four:',
        actSpeakBrief='In pairs: one of you works at the resort’s information desk, the other is a first-time visitor.',
        actSpeak1='Visitor: ask how to get up the mountain and what you need to buy.',
        actSpeak2='Desk: recommend equipment, a lesson and the right runs for a beginner.',
        actSpeak3='Visitor: ask what to do if you have an accident, and where to go for après-ski.',
        actWriteKind='Writing',
        actWriteBrief='Write a message to a friend (100–120 words) about your first day at a ski resort: what you rented, your lesson, what happened on the slope and what you did in the evening.',
        actPlaceholder='Hi Max! Today was my first day on skis …',
    ),
    'de': dict(
        coverTitle='Skiing at <br><em>the Resort</em>',
        coverSub='Englisch im Skigebiet: Lifte und Skipässe, Kleidung und Ausrüstung, Pistenrettung und Après-Ski — in zwanzig Fragen und Sätzen.',
        chipLevel='B1', chipFocus='Wortschatz Skigebiet', chipCount='23 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Wiederholung', e1='Wortschatz Skigebiet', e2='Richtig oder falsch?', e3='Ergänze die Sätze', e4='Bilde die Sätze',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die beste Antwort', mcT2='Richtig oder falsch?',
        gapT='Ergänze den Satz', gHint='Ein Wort aus der Liste pro Lücke.',
        orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an, um den Satz zu bilden.',
        recT='Die Wörter im Skigebiet', pUp='Nach oben', pGear='Was man trägt', pPeople='Menschen und Orte',
        actTitle='Die Skireise', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Eine Person arbeitet an der Info des Skigebiets, die andere ist zum ersten Mal da.',
        actSpeak1='Gast: Frag, wie man auf den Berg kommt und was man kaufen muss.',
        actSpeak2='Info: Empfiehl Ausrüstung, einen Kurs und die richtigen Pisten für Anfänger.',
        actSpeak3='Gast: Frag, was man bei einem Unfall tut und wo es Après-Ski gibt.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einem Freund eine Nachricht (100–120 Wörter) über deinen ersten Tag im Skigebiet: was du ausgeliehen hast, deinen Kurs, was auf der Piste passiert ist und was du am Abend gemacht hast.',
        actPlaceholder='Hi Max! Today was my first day on skis …',
    ),
    'es': dict(
        coverTitle='Skiing at <br><em>the Resort</em>',
        coverSub='Inglés en la estación de esquí: remontes y forfaits, ropa y equipo, la patrulla de pistas y el après-ski, en veinte preguntas y oraciones.',
        chipLevel='B1', chipFocus='vocabulario de la estación de esquí', chipCount='23 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Repaso', e1='Vocabulario de la estación', e2='¿Verdadero o falso?', e3='Completa las oraciones', e4='Construye las oraciones',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la mejor respuesta', mcT2='¿Verdadero o falso?',
        gapT='Completa la oración', gHint='Una palabra de la lista en cada hueco.',
        orderT='Construye la oración', orderHint='Haz clic en las piezas en orden para construir la oración.',
        recT='Las palabras de la estación', pUp='Para subir', pGear='Lo que te pones', pPeople='Personas y lugares',
        actTitle='El viaje de esquí', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: uno trabaja en el punto de información de la estación y el otro viene por primera vez.',
        actSpeak1='Visitante: pregunta cómo subir a la montaña y qué tienes que comprar.',
        actSpeak2='Información: recomienda equipo, una clase y las pistas adecuadas para un principiante.',
        actSpeak3='Visitante: pregunta qué hacer si tienes un accidente y dónde hay après-ski.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un mensaje a un amigo (100–120 palabras) sobre tu primer día en una estación de esquí: qué alquilaste, tu clase, qué pasó en la pista y qué hiciste por la noche.',
        actPlaceholder='Hi Max! Today was my first day on skis …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
