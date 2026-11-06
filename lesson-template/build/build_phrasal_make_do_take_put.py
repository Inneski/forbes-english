# -*- coding: utf-8 -*-
"""Phrasal Verbs: make, do, take, put (B1-B2). House style 2, 23 slides.

Rebuilt 2026-11-06 from `phrasal_verbs_test.html`, a sixteen-item
vocabulary check with no teaching. All sixteen items are kept. The
meanings are a recap AFTER the items (four pill-tab cards, the meanings
translated), not before them, so the check still checks.

Fixed:
  * Q14 "The strange smell ___ me eating anything there" with the key PUT
    OFF built "put off me eating": the object goes between verb and
    particle (PUT ME OFF). The stem now has "put me ___ eating" and the
    item tests the particle.
  * Q11 "his daughter took on the family business" is possible English;
    TOOK ON is replaced with TOOK IN.
Added: a gap slide (the particles), two speaking fields, the activation.

Run from the repo root:  py lesson-template/build/build_phrasal_make_do_take_put.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='phrasal_verbs_test.html',
    title='Phrasal Verbs: make, do, take, put (B1–B2)',
    folder='PhrasalMakeDoTakePut',
    scheme='slate',
    art={
        'hero': ('build', 'four building blocks stacked into a small tower, one block being lifted on'),
        'talk': ('talk', 'two speech bubbles over a small table'),
        'a': ('home', 'a run-down cottage with a ladder against the wall and a paint pot'),
        'b': ('work', 'a desk with a new staff badge, a laptop and a cup of coffee'),
        'act': ('pair', 'two chairs at a café table'),
    },
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


MD = [
    q('The burglars broke in through the back window and ____ several valuable paintings before anyone noticed.',
      ['made off with', 'made up for', 'did away with', 'put out'], 1),
    q('He forgot her birthday, so he bought her flowers to ____ it.', ['make up for', 'make of', 'do without', 'take on'], 2),
    q('I’m not sure what to ____ his strange behaviour lately.', ['make of', 'make up', 'do away with', 'put away'], 3),
    q('Nobody believed his excuse — everyone thought he’d ____ the whole story.', ['made up', 'made off with', 'done up', 'taken in'], 4),
    q('The new head teacher wants to ____ the old uniform rules completely.', ['do away with', 'do without', 'make up for', 'put off'], 5),
    q('During the strike, the office had to ____ its usual delivery service for two weeks.',
      ['do without', 'do away with', 'make of', 'take back'], 6),
    q('After that long hike, I could really ____ a hot shower.', ['do with', 'do without', 'make up', 'put on'], 7),
    q('They bought a run-down cottage and spent a year ____ it before moving in.',
      ['doing up', 'doing away with', 'putting away', 'taking on'], 8),
]
TP = [
    q('The company is ____ ten new staff for the busy season.', ['taking on', 'taking back', 'taking in', 'putting on'], 9),
    q('The lecture was so complex that I couldn’t ____ half of what was said.', ['take in', 'take back', 'take on', 'put out'], 10),
    q('After the founder retired, his daughter ____ the family business.', ['took over', 'took in', 'took back', 'put out'], 11),
    q('As soon as he apologised, I asked him to ____ what he’d said about my work.', ['take back', 'take in', 'take on', 'put off'], 12),
    q('Could you ____ some background music while we wait for the guests?', ['put on', 'put out', 'put away', 'put off'], 13),
    q('The strange smell coming from the kitchen put me ____ eating anything there.', ['off', 'out', 'away', 'on'], 14),
    q('Please ____ your toys before your friends arrive.', ['put away', 'put out', 'put off', 'put on'], 15),
    q('It took the fire crew almost an hour to ____ the flames.', ['put out', 'put off', 'put away', 'put on'], 16),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Have you ever renovated a room or a flat?',
        'What could you not live without?',
        'What music do you listen to while you work?',
        'Have you ever invented an excuse?',
        'Who would you like to work with in five years?',
        'What do you do when you can’t understand a lecture?',
    ], 'talk', 3),
    ('mc', 'e1', 'mcT', MD, 'a', None),
    ('mc', 'e2', 'mcT', TP, 'b', 'left'),
    ('rules', 'eR', 'recT', [
        ('make', ['m1', 'm2', 'm3', 'm4'], None),
        ('do', ['d1', 'd2', 'd3', 'd4'], None),
        ('take', ['t1', 't2', 't3', 't4'], None),
        ('put', ['p1', 'p2', 'p3', 'p4'], None),
    ], None),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('Please put your phones ______ during the exam.', ['away'], 'gw1'),
        ('The hospital has taken ______ two new nurses this month.', ['on'], 'gw2'),
        ('I could really ______ with a coffee right now.', ['do'], 'gw3'),
    ]),
    ('talk', 'eT', 'tk2T', [
        'Is there anything at work you would like to <strong>do away with</strong>?',
        'What helps you <strong>take in</strong> new information?',
        'How do you <strong>make up for</strong> a mistake with a friend?',
        'What do you <strong>put off</strong> doing for as long as possible?',
        'What could you <strong>do with</strong> right now?',
        'Would you like to <strong>take over</strong> a business one day?',
    ], None, 3),
]
SPEC['chips'] = ['take on', 'put off', 'do with', 'make up for', 'take back', 'do away with', 'put away']

W = {
    'en': [
        'MAKE OFF WITH something = steal it and escape.', 'MAKE UP FOR something = do something good to balance something bad.',
        'MAKE OF someone or something = understand or have an opinion of them.', 'MAKE something UP = invent something untrue.',
        'DO AWAY WITH something = get rid of it for good.', 'DO WITHOUT something = manage when you don’t have it.',
        'COULD DO WITH something = would like it, need it.', 'DO something UP = repair and decorate it.',
        'TAKE someone ON = give them a job.', 'TAKE something IN = understand and remember it.',
        'TAKE OVER = take control of something from someone else.', 'TAKE something BACK = say you were wrong to say it.',
        'PUT something ON = start music, a film, the radio.', 'PUT someone OFF (doing) something = make them not want to do it. The object goes in the middle: PUT ME OFF.',
        'PUT something AWAY = put it back where it belongs.', 'PUT something OUT = stop a fire burning.',
    ],
    'de': [
        'MAKE OFF WITH something = etwas stehlen und damit abhauen.', 'MAKE UP FOR something = etwas wiedergutmachen.',
        'MAKE OF someone or something = jemanden/etwas einschätzen, sich einen Reim darauf machen.', 'MAKE something UP = sich etwas ausdenken, erfinden.',
        'DO AWAY WITH something = etwas abschaffen.', 'DO WITHOUT something = ohne etwas auskommen.',
        'COULD DO WITH something = etwas gut gebrauchen können.', 'DO something UP = etwas renovieren.',
        'TAKE someone ON = jemanden einstellen.', 'TAKE something IN = etwas aufnehmen, verstehen.',
        'TAKE OVER = etwas übernehmen.', 'TAKE something BACK = etwas zurücknehmen (eine Aussage).',
        'PUT something ON = etwas anmachen (Musik, einen Film).', 'PUT someone OFF (doing) something = jemandem die Lust auf etwas verderben. Das Objekt steht in der Mitte: PUT ME OFF.',
        'PUT something AWAY = etwas wegräumen.', 'PUT something OUT = etwas löschen (ein Feuer).',
    ],
    'es': [
        'MAKE OFF WITH something = robar algo y huir.', 'MAKE UP FOR something = compensar algo.',
        'MAKE OF someone or something = entender, qué pensar de algo o alguien.', 'MAKE something UP = inventarse algo.',
        'DO AWAY WITH something = eliminar, abolir algo.', 'DO WITHOUT something = arreglárselas sin algo.',
        'COULD DO WITH something = venirle bien algo, necesitarlo.', 'DO something UP = reformar algo.',
        'TAKE someone ON = contratar a alguien.', 'TAKE something IN = asimilar, entender algo.',
        'TAKE OVER = hacerse cargo de algo, tomar el control.', 'TAKE something BACK = retirar lo dicho.',
        'PUT something ON = poner algo (música, una película).', 'PUT someone OFF (doing) something = quitarle a alguien las ganas de algo. El objeto va en medio: PUT ME OFF.',
        'PUT something AWAY = guardar algo en su sitio.', 'PUT something OUT = apagar algo (un fuego).',
    ],
}
REC = {
    'en': ['OFF WITH = steal and escape', 'UP FOR = make a bad thing better', 'OF = understand, think of', 'UP = invent',
           'AWAY WITH = get rid of', 'WITHOUT = manage without', 'COULD DO WITH = would like', 'UP = repair and decorate',
           'ON = give a job to', 'IN = understand', 'OVER = take control', 'BACK = say you were wrong',
           'ON = start music or a film', 'OFF = make someone not want to', 'AWAY = put back in its place', 'OUT = stop a fire'],
    'de': ['OFF WITH = stehlen und abhauen', 'UP FOR = wiedergutmachen', 'OF = verstehen, einschätzen', 'UP = erfinden',
           'AWAY WITH = abschaffen', 'WITHOUT = ohne auskommen', 'COULD DO WITH = gut gebrauchen können', 'UP = renovieren',
           'ON = einstellen', 'IN = aufnehmen, verstehen', 'OVER = übernehmen', 'BACK = zurücknehmen',
           'ON = anmachen (Musik, Film)', 'OFF = die Lust verderben', 'AWAY = wegräumen', 'OUT = löschen'],
    'es': ['OFF WITH = robar y huir', 'UP FOR = compensar', 'OF = entender, opinar', 'UP = inventar',
           'AWAY WITH = eliminar', 'WITHOUT = arreglárselas sin', 'COULD DO WITH = venir bien', 'UP = reformar',
           'ON = contratar', 'IN = asimilar', 'OVER = hacerse cargo', 'BACK = retirar lo dicho',
           'ON = poner (música, película)', 'OFF = quitar las ganas', 'AWAY = guardar', 'OUT = apagar (un fuego)'],
}

T = {
    'en': dict(
        coverTitle='Make, Do, <br><em>Take, Put</em>',
        coverSub='Sixteen phrasal verbs with make, do, take and put, in sentences: choose the right one, check what each means, then use them.',
        chipLevel='B1–B2', chipFocus='phrasal verbs', chipCount='23 slides',
        eW='Warm-up', eT='Let’s talk', eR='Review', e1='Make and do', e2='Take and put', e3='Your turn',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the phrasal verb', recT='What they mean',
        gapT='Write the missing word', gHint='One word in each gap: the verb or the particle.',
        gw1='PUT something AWAY: put it where it belongs, out of sight.',
        gw2='TAKE someone ON: give them a job.',
        gw3='COULD DO WITH something: would like it.',
        actTitle='Make it yours', actUse='Use at least three:',
        actSpeakBrief='In pairs. Use the phrasal verbs to talk about your own life.',
        actSpeak1='Tell your partner about a home, a room or a car that someone DID UP.',
        actSpeak2='What rule at work or school would you DO AWAY WITH? What would you PUT OFF if you could?',
        actSpeak3='Tell a story about a time someone MADE something UP, or had to MAKE UP FOR a mistake.',
        actWriteKind='Writing',
        actWriteBrief='Write a short email to a colleague (120–150 words) about changes at work: who the company is TAKING ON, what it is DOING AWAY WITH, and what everyone COULD DO WITH. Use five phrasal verbs from this lesson.',
        actPlaceholder='Hi Chris, …',
    ),
    'de': dict(
        coverTitle='Make, Do, <br><em>Take, Put</em>',
        coverSub='Sechzehn Phrasal Verbs mit make, do, take und put im Satz: Wähle das richtige, prüfe, was es bedeutet, und verwende es dann selbst.',
        chipLevel='B1–B2', chipFocus='Phrasal Verbs', chipCount='23 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Wiederholung', e1='Make und do', e2='Take und put', e3='Du bist dran',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle das Phrasal Verb', recT='Was sie bedeuten',
        gapT='Ergänze das fehlende Wort', gHint='Ein Wort pro Lücke: das Verb oder die Partikel.',
        gw1='PUT something AWAY: etwas wegräumen.',
        gw2='TAKE someone ON: jemanden einstellen.',
        gw3='COULD DO WITH something: etwas gut gebrauchen können.',
        actTitle='Mach sie zu deinen', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit. Sprecht mit den Phrasal Verbs über euer eigenes Leben.',
        actSpeak1='Erzähl deinem Partner von einer Wohnung, einem Zimmer oder einem Auto, das jemand renoviert hat (DID UP).',
        actSpeak2='Welche Regel bei der Arbeit oder in der Schule würdest du abschaffen (DO AWAY WITH)? Was würdest du aufschieben (PUT OFF), wenn du könntest?',
        actSpeak3='Erzähl von einem Mal, als jemand sich etwas ausgedacht hat (MADE UP) oder einen Fehler wiedergutmachen musste (MAKE UP FOR).',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einer Kollegin eine kurze E-Mail (120–150 Wörter) über Veränderungen bei der Arbeit: wen die Firma einstellt (TAKING ON), was sie abschafft (DOING AWAY WITH) und was alle gut gebrauchen könnten (COULD DO WITH). Verwende fünf Phrasal Verbs aus dieser Lektion.',
        actPlaceholder='Hi Chris, …',
    ),
    'es': dict(
        coverTitle='Make, Do, <br><em>Take, Put</em>',
        coverSub='Dieciséis phrasal verbs con make, do, take y put en oraciones: elige el correcto, comprueba qué significa y después úsalo.',
        chipLevel='B1–B2', chipFocus='phrasal verbs', chipCount='23 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Repaso', e1='Make y do', e2='Take y put', e3='Tu turno',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige el phrasal verb', recT='Lo que significan',
        gapT='Escribe la palabra que falta', gHint='Una palabra en cada hueco: el verbo o la partícula.',
        gw1='PUT something AWAY: guardar algo en su sitio.',
        gw2='TAKE someone ON: contratar a alguien.',
        gw3='COULD DO WITH something: venirle bien algo.',
        actTitle='Hazlos tuyos', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas. Usen los phrasal verbs para hablar de su vida.',
        actSpeak1='Cuéntale a tu compañero de una casa, una habitación o un coche que alguien reformó (DID UP).',
        actSpeak2='¿Qué norma del trabajo o de la escuela eliminarías (DO AWAY WITH)? ¿Qué aplazarías (PUT OFF) si pudieras?',
        actSpeak3='Cuenta una vez en que alguien se inventó algo (MADE UP) o tuvo que compensar un error (MAKE UP FOR).',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un correo corto a una compañera (120–150 palabras) sobre cambios en el trabajo: a quién está contratando la empresa (TAKING ON), qué está eliminando (DOING AWAY WITH) y qué le vendría bien a todo el mundo (COULD DO WITH). Usa cinco phrasal verbs de esta lección.',
        actPlaceholder='Hi Chris, …',
    ),
}
KEYS = ['m1', 'm2', 'm3', 'm4', 'd1', 'd2', 'd3', 'd4', 't1', 't2', 't3', 't4', 'p1', 'p2', 'p3', 'p4']
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w
    for k, r in zip(KEYS, REC[c]):
        T[c][k] = r

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
