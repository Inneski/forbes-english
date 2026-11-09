# -*- coding: utf-8 -*-
"""At the Tennis Club: Giving Instructions (A2, workplace English for
reception and facility staff). House style 1, 14 slides.

Rebuilt 2026-11-06 from `forbes-tennis-a2.html`: Julie on reception and
Raymond on the courts at a Vienna racket-sports hall, five "what does she
say?" items, five word-bank gaps and a five-pair situation match. All
fifteen are kept. The one real plate, Tennis/racket-court-net.jpg, carries
the first block; the 1200x671 library card is not a hero, so the cover is a
stand-in and the card stays the thumbnail.

Fixed:
  * Gap 1, "You ___ to check in", was keyed NEED while HAVE — also right —
    sat in the same word bank and was marked wrong. Typed now, it accepts
    both.
  * MC 2: "I am sorry, but those shoes are not suitable here" is a perfectly
    good thing to say. The stem now asks Raymond to tell the guest what to
    DO, which only the instruction does.
Added: the instruction structures as rule cards, speaking, activation.

Run from the repo root:  py lesson-template/build/build_tennis_a2.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H
import deck as D

SPEC = dict(
    out='forbes-tennis-a2.html',
    title='At the Tennis Club: Giving Instructions (A2)',
    folder='Tennis',
    scheme='sage',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09). hero = the racket plate
    # that was the first block's picture; the rest are Midjourney renders,
    # his style images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'a tennis racket and ball lying on a clay court by the net',
        'talk': 'a sports club reception counter with a bell, racket bags and an indoor tennis hall behind',
        'q-checkin': 'a receptionist at a tennis club desk calling over a guest who walks past with a racket bag',
        'q-shoes': 'a pair of muddy street shoes standing on a clean blue indoor tennis court',
        'q-booking': 'a court booking board at a tennis club, every slot full, a guest with a racket looking at it',
        'q-agreed': 'a hand holding a phone with an online booking confirmation, a tennis court behind',
        'q-surface': 'a close-up of a hard tennis court surface scuffed by a black shoe sole',
        'talk2': 'a coach and a guest talking at the net of an indoor tennis court',
        'results': 'a tennis ball resting on the white baseline of a court in evening light',
    },
    pop={'hero': (None, 'square'), 'q-shoes': (None, 'free'), 'talk2': (None, 'blob')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


MC = [
    q('A guest walks to the court without checking in. What does Julie say?',
      ['Could you please check in at reception first?', 'You are not allowed inside the building today.',
       'Please wait here until a coach arrives shortly.', 'Your reservation is not showing on our system.'], 1),
    q('A guest is wearing street shoes on the court. Raymond tells them what to do:',
      ['You need to wear proper tennis shoes on the court.', 'I am sorry, but those shoes are not suitable here.',
       'Your shoes look nice, but they are the wrong style.', 'We only allow white shoes on all of our courts.'], 2),
    q('A guest wants to play but has no booking. Julie explains:',
      ['You have to book a court in advance to play here.', 'The courts are all full because of a big tournament.',
       'Our system is down, so it can’t show free courts.', 'Please come back tomorrow when we have more space.'], 3),
    q('The guest accepted the shoe rule when booking online, but forgot. Julie reminds them:',
      ['You agreed to this rule when you made your booking.', 'This rule is written on a sign near the entrance door.',
       'The website explained all of our court policies.', 'Other guests have the same problem quite often too.'], 4),
    q('A guest asks why tennis shoes are required. Julie explains:',
      ['Street shoes can damage the court surface very quickly.', 'The club owner decided this rule a long time ago.',
       'Other members sometimes complain about dirty floors.', 'Tennis shoes are on sale in our little shop.'], 5),
]
PAIRS = [('Guest has no booking', 'You need to reserve a court first.'),
         ('Street shoes on the court', 'Please change into tennis shoes.'),
         ('Guest skipped reception', 'Could you check in with us first?'),
         ('Guest asks about the rule', 'Street shoes can damage the surface.'),
         ('Guest forgot the confirmation', 'You agreed to this when you booked.')]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Do you play tennis, squash or padel?',
        'What rules are there at your gym or sports club?',
        'Have you ever forgotten a rule at a hotel or a club?',
        'How do you ask a guest or a customer to do something politely?',
        'What do you say when a customer is annoyed?',
        'Do you speak English at work? When?',
    ], 'talk', 3),
    ('stage',),
    ('rules', 'eR', 'rT', [
        ('Could you please …?', ['rP1'], '<strong>Could you please</strong> check in first?'),
        ('You need to / have to …', ['rN1'], 'You <strong>need to</strong> book a court in advance.'),
        ('You must … / … is required', ['rM1'], 'Tennis shoes <strong>are required</strong> on all courts.'),
        ('… is not allowed', ['rA1'], 'Street shoes <strong>are not allowed</strong> on the court.'),
    ], None),
    ('mc', 'e1', 'mcT', MC, ['q-checkin', 'q-shoes', 'q-booking', 'q-agreed', 'q-surface'], None),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('You ______ to check in at reception before using the court.', ['need|have'], 'g1'),
        ('Street shoes are not ______ on the court at Tennis Punks Vienna.', ['allowed'], 'g2'),
        ('You ______ wear tennis shoes. This is a club rule for everyone.', ['must'], 'g3'),
    ], ['allowed', 'must', 'need', 'sorry', 'welcome']),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('Could you ______ show me your booking confirmation at the desk?', ['please'], 'g4'),
        ('Tennis shoes are ______ on all courts. This keeps the surface in good condition.', ['required'], 'g5'),
    ], ['required', 'sorry', 'please', 'welcome']),
    ('raw', None),
    ('talk', 'eT', 'tk2T', [
        'Give a guest an instruction with <strong>Could you please …?</strong>',
        'Tell a guest a rule with <strong>You need to …</strong>',
        'What is <strong>not allowed</strong> at your workplace?',
        'What is <strong>required</strong> for your job?',
        'Explain why a rule exists: <strong>… can damage …</strong>',
        'How do you remind someone politely that they <strong>agreed</strong> to something?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['Could you please', 'you need to', 'not allowed', 'you have to', 'required', 'you agreed']

W = {
    'en': [
        '“Could you please …?” gives an instruction politely, without sounding rude.',
        'YOU NEED TO … tells the guest exactly what to do. “Not suitable” only says what is wrong.',
        'YOU HAVE TO is for a rule that is not optional: polite but firm.',
        'A fact the guest already accepted: polite, and it avoids an argument.',
        'CAN gives the risk — a clear, logical reason for the rule.',
    ],
    'de': [
        '„Could you please …?“ gibt höflich eine Anweisung, ohne unhöflich zu klingen.',
        'YOU NEED TO … sagt dem Gast genau, was er tun soll. „Not suitable“ sagt nur, was falsch ist.',
        'YOU HAVE TO steht für eine Regel, die nicht freiwillig ist: höflich, aber bestimmt.',
        'Eine Tatsache, die der Gast schon akzeptiert hat: höflich, und es vermeidet Streit.',
        'CAN nennt das Risiko — ein klarer, logischer Grund für die Regel.',
    ],
    'es': [
        '«Could you please …?» da una instrucción con educación, sin sonar brusco.',
        'YOU NEED TO … le dice al cliente exactamente qué hacer. «Not suitable» solo dice qué está mal.',
        'YOU HAVE TO es para una norma que no es opcional: educado pero firme.',
        'Un hecho que el cliente ya aceptó: educado, y evita una discusión.',
        'CAN expresa el riesgo: una razón clara y lógica para la norma.',
    ],
}
G = {
    'en': ['NEED TO (or HAVE TO): the action is necessary. Both are right here.', 'NOT ALLOWED = forbidden: clear and polite.',
           'MUST: a strict rule for everyone.', 'COULD YOU PLEASE …? — a polite request.', 'REQUIRED = obligatory: a little more formal.'],
    'de': ['NEED TO (oder HAVE TO): Die Handlung ist nötig. Hier ist beides richtig.', 'NOT ALLOWED = verboten: klar und höflich.',
           'MUST: eine strenge Regel für alle.', 'COULD YOU PLEASE …? — eine höfliche Bitte.', 'REQUIRED = vorgeschrieben: etwas förmlicher.'],
    'es': ['NEED TO (o HAVE TO): la acción es necesaria. Aquí los dos son correctos.', 'NOT ALLOWED = prohibido: claro y educado.',
           'MUST: una norma estricta para todos.', 'COULD YOU PLEASE …? — una petición educada.', 'REQUIRED = obligatorio: un poco más formal.'],
}

T = {
    'en': dict(
        coverTitle='At the <br><em>Tennis Club</em>',
        coverSub='Workplace English for reception and facility staff: giving clear, polite instructions to guests — between the baseline and the front desk.',
        chipLevel='A2', chipFocus='instructions · rules · polite requests', chipCount='14 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='What does Julie say?', e2='Complete the rule', e3='Situations',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best thing to say',
        rT='Giving instructions', rP1='A polite request.', rN1='Something necessary.', rM1='A strict rule.', rA1='Something forbidden.',
        gapT='Complete the sentence', gHint='One word from the bank in each gap.',
        matchT='Situation and instruction', matchHint='Click a situation, then the right instruction.',
        matchWhy='Each situation needs its own instruction: book, change shoes, check in, explain, remind.',
        actTitle='At the front desk', actUse='Use at least four:',
        actSpeakBrief='In pairs: one of you works at reception, the other is a guest who does not know the rules.',
        actSpeak1='Guest: arrive without a booking, in street shoes. Receptionist: give two clear instructions.',
        actSpeak2='Guest: ask WHY. Receptionist: explain the reason politely.',
        actSpeak3='Swap roles at a place you know: a gym, a hotel, a swimming pool.',
        actWriteKind='Writing',
        actWriteBrief='Write a short welcome email to new club members (70–90 words) with four rules: what they NEED TO do, what is REQUIRED, what is NOT ALLOWED, and one polite request.',
        actPlaceholder='Welcome to Tennis Punks Vienna! Please …',
    ),
    'de': dict(
        coverTitle='At the <br><em>Tennis Club</em>',
        coverSub='Englisch im Beruf für Empfang und Platzpersonal: Gästen klare, höfliche Anweisungen geben — zwischen Grundlinie und Rezeption.',
        chipLevel='A2', chipFocus='Anweisungen · Regeln · höfliche Bitten', chipCount='14 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Was sagt Julie?', e2='Ergänze die Regel', e3='Situationen',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die beste Antwort',
        rT='Anweisungen geben', rP1='Eine höfliche Bitte.', rN1='Etwas Notwendiges.', rM1='Eine strenge Regel.', rA1='Etwas Verbotenes.',
        gapT='Ergänze den Satz', gHint='Ein Wort aus der Liste pro Lücke.',
        matchT='Situation und Anweisung', matchHint='Klicke eine Situation an, dann die passende Anweisung.',
        matchWhy='Jede Situation braucht ihre eigene Anweisung: buchen, Schuhe wechseln, einchecken, erklären, erinnern.',
        actTitle='An der Rezeption', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Eine Person arbeitet am Empfang, die andere ist ein Gast, der die Regeln nicht kennt.',
        actSpeak1='Gast: Komm ohne Buchung und in Straßenschuhen. Empfang: Gib zwei klare Anweisungen.',
        actSpeak2='Gast: Frag WARUM. Empfang: Erklär den Grund höflich.',
        actSpeak3='Tauscht die Rollen an einem Ort, den ihr kennt: Fitnessstudio, Hotel, Schwimmbad.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib eine kurze Willkommens-E-Mail an neue Clubmitglieder (70–90 Wörter) mit vier Regeln: was sie tun müssen (NEED TO), was vorgeschrieben ist (REQUIRED), was nicht erlaubt ist (NOT ALLOWED) und eine höfliche Bitte.',
        actPlaceholder='Welcome to Tennis Punks Vienna! Please …',
    ),
    'es': dict(
        coverTitle='At the <br><em>Tennis Club</em>',
        coverSub='Inglés profesional para recepción y personal de instalaciones: dar instrucciones claras y educadas a los clientes, de la pista al mostrador.',
        chipLevel='A2', chipFocus='instrucciones · normas · peticiones educadas', chipCount='14 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='¿Qué dice Julie?', e2='Completa la norma', e3='Situaciones',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la mejor respuesta',
        rT='Dar instrucciones', rP1='Una petición educada.', rN1='Algo necesario.', rM1='Una norma estricta.', rA1='Algo prohibido.',
        gapT='Completa la oración', gHint='Una palabra de la lista en cada hueco.',
        matchT='Situación e instrucción', matchHint='Haz clic en una situación y después en la instrucción correcta.',
        matchWhy='Cada situación necesita su instrucción: reservar, cambiarse de zapatos, registrarse, explicar, recordar.',
        actTitle='En la recepción', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: uno trabaja en recepción y el otro es un cliente que no conoce las normas.',
        actSpeak1='Cliente: llega sin reserva y con zapatos de calle. Recepción: da dos instrucciones claras.',
        actSpeak2='Cliente: pregunta POR QUÉ. Recepción: explica la razón con educación.',
        actSpeak3='Cambien los papeles en un lugar que conozcan: un gimnasio, un hotel, una piscina.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un correo breve de bienvenida a los nuevos socios (70–90 palabras) con cuatro normas: lo que tienen que hacer (NEED TO), lo obligatorio (REQUIRED), lo que no está permitido (NOT ALLOWED) y una petición educada.',
        actPlaceholder='Welcome to Tennis Punks Vienna! Please …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w
    for i, g in enumerate(G[c], 1):
        T[c]['g%d' % i] = g

E = T['en']
MATCH = D.match(PAIRS, 'e3', E['e3'], 'matchT', E['matchT'], 'matchHint', E['matchHint'], 'matchWhy')
SPEC['flow'] = [('raw', MATCH) if st == ('raw', None) else st for st in SPEC['flow']]

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
