# -*- coding: utf-8 -*-
"""Swiss Precision: Goodbye, Denglisch! — Common Mistakes for German
Speakers (A2). House style 1, 31 slides.

Rebuilt 2026-11-06 from `forbes-english-swiss-mistakes-a2.html`: four
activities — do / make / take (8), fix the mistake (8), prepositions (8),
a business vocabulary match (8 pairs). All 32 items are kept.

Fixed:
  * Activity 1 printed "DE: take lessons = Unterricht nehmen" under each
    question: the answer, in German. Gone; the explanations translate.
  * Second correct answers, three of them admitted in the old feedback:
    "She works AT a Swiss company" (natural English), "do a course" ("also
    possible"), and British "I don't PLAY much sport". Each distractor is
    now the German-speaker trap the item is about: "VISIT a course"
    (besuchen), "DRIVE sport" (Sport treiben), "work FROM a company".
Added: speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_swiss_mistakes_a2.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H
import deck as D

SPEC = dict(
    out='forbes-english-swiss-mistakes-a2.html',
    title='Swiss Precision: Common Mistakes for German Speakers (A2)',
    folder='SwissMistakes',
    scheme='rose',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'a business traveller with a briefcase on a Swiss train beside a lake and mountains',
        'talk': 'colleagues talking at a coffee machine in a bright Zurich office',
        'a1': 'a woman at an English lesson with her teacher',
        'a2': 'a businessman with a small suitcase hurrying through an airport',
        'a3': 'an office worker at her desk in a modern office building in Zurich',
        'a4': 'two business people shaking hands across a desk',
        'a5': 'a young man signing up for a marketing course at a college desk',
        'a6': 'a woman walking in a park on her way to work',
        'a7': 'consultants presenting to international clients in a meeting room',
        'a8': 'a car factory production line with robot arms',
        'n1': 'a small evening English class around a table',
        'n2': 'an office building in Basel beside the river Rhine',
        'n3': 'people travelling by horse and cart on a country road long ago',
        'n4': 'an elegant expensive hotel lobby with a chandelier',
        'n5': 'a plate of good food on a restaurant table',
        'n6': 'a red Swiss train arriving at a station in Zurich',
        'n7': 'two friends fishing from a small boat on a Swiss lake',
        'n8': 'a sunny Swiss mountain village in summer',
        'b1': 'workers assembling medical equipment in a clean factory',
        'b2': 'a busy woman at her desk covered in papers on a Friday afternoon',
        'b3': 'a horse pulling a carriage along an old road',
        'b4': 'a shop assistant helping very different customers',
        'b5': 'a frustrated traveller at an airline desk after a cancelled flight',
        'b6': 'a modern office building in a German city',
        'b7': 'two hikers walking along a mountain path',
        'b8': 'delivery vans driving along motorways across Europe',
        'talk2': 'two colleagues talking on a terrace overlooking a Swiss lake',
        'results': 'a briefcase and a coffee on a train table, mountains outside the window',
    },
    pop={'hero': (None, 'square'), 'a2': (None, 'free')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


A1 = [
    q('I ____ lessons with an English teacher every week.', ['take', 'make', 'do', 'work'], 1),
    q('I ____ a lot of travelling for my job.', ['do', 'make', 'take', 'go'], 2),
    q('She works ____ a Swiss company in Zurich.', ['for', 'to', 'by', 'from'], 3),
    q('We ____ business with companies in Germany and Austria.', ['do', 'make', 'take', 'have'], 4),
    q('He wants to ____ a course in marketing.', ['take', 'make', 'work', 'visit'], 5),
    q('I don’t ____ much sport, but I walk every day.', ['do', 'make', 'take', 'drive'], 6),
    q('My company ____ services for international clients.', ['provides', 'makes', 'produces', 'gives'], 7),
    q('Volkswagen ____ cars and other vehicles.', ['produces', 'provides', 'works', 'serves'], 8),
]
A2 = [
    q('Which version is correct? <em>“I make English lessons every Tuesday.”</em>',
      ['I take English lessons every Tuesday.', 'I take English lessons in every Tuesday.',
       'I am take English lessons every Tuesday.', 'I take English lesson every Tuesday.'], 9),
    q('Which version is correct? <em>“I work to a company in Basel.”</em>',
      ['I work for a company in Basel.', 'I work by a company in Basel.', 'I work for a company at Basel.',
       'I am work for a company in Basel.'], 10),
    q('Which version is correct? <em>“A long time before, people travelled by horse.”</em>',
      ['A long time ago, people travelled by horse.', 'A long time since, people travelled by horse.',
       'A long time ago, people travelled by the horse.', 'Long time ago, people travelled by horse.'], 11),
    q('Which version is correct? <em>“That’s mean the hotel is expensive.”</em>',
      ['That means the hotel is expensive.', 'That mean the hotel is expensive.',
       'That is means the hotel is expensive.', 'That’s meaning the hotel is expensive.'], 12),
    q('Which version is correct? <em>“The eat must be good.”</em>',
      ['The food must be good.', 'The eating must be good.', 'The food must to be good.', 'The meal must be well.'], 13),
    q('Which version is correct? <em>“Yesterday I made a train to Zurich.”</em>',
      ['Yesterday I took a train to Zurich.', 'Yesterday I taked a train to Zurich.',
       'Yesterday I took a train at Zurich.', 'Yesterday I have took a train to Zurich.'], 14),
    q('Which version is correct? <em>“We made fishing at the weekend.”</em>',
      ['We went fishing at the weekend.', 'We did fishing at the weekend.', 'We went to fishing at the weekend.',
       'We went fishing in the weekend.'], 15),
    q('Which version is correct? <em>“Switzerland has much sun in summer.”</em>',
      ['Switzerland has a lot of sun in summer.', 'Switzerland has many sun in summer.',
       'Switzerland has lot of sun in summer.', 'Switzerland has a lot sun in summer.'], 16),
]
A3 = [
    q('I work ____ a company that produces medical equipment.', ['for', 'to', 'from', 'by'], 17),
    q('I don’t ____ lessons on Friday because I’m busy.', ['take', 'make', 'give', 'hold'], 18),
    q('A long time ____, people used horses instead of cars.', ['ago', 'before', 'since', 'then'], 19),
    q('It depends ____ the type of customer.', ['on', 'of', 'from', 'at'], 20),
    q('I would like compensation ____ the cancelled flight.', ['for', 'about', 'of', 'by'], 21),
    q('The company has a subsidiary ____ Germany.', ['in', 'at', 'on', 'by'], 22),
    q('We travelled two miles ____ foot.', ['on', 'by', 'with', 'per'], 23),
    q('The company provides services ____ Europe.', ['across', 'between', 'along', 'among'], 24),
]
PAIRS = [('employees', 'the people who work for a company'), ('revenue', 'money a company receives from sales'),
         ('subsidiary', 'a company controlled by a larger company'), ('expertise', 'special knowledge and skill in one area'),
         ('well-known', 'famous or familiar to many people'), ('vehicle', 'a car, bus or other transport machine'),
         ('region', 'an area of a country or continent'), ('transferable skills', 'skills you can use in many different jobs')]
MG = {
    'de': {'employees': 'die Mitarbeitenden einer Firma', 'revenue': 'das Geld, das eine Firma durch Verkäufe einnimmt (Umsatz)',
           'subsidiary': 'eine Firma, die von einer größeren kontrolliert wird (Tochtergesellschaft)',
           'expertise': 'besonderes Wissen und Können in einem Bereich', 'well-known': 'bekannt, vielen Menschen vertraut',
           'vehicle': 'ein Auto, ein Bus oder ein anderes Verkehrsmittel (Fahrzeug)', 'region': 'ein Gebiet eines Landes oder Kontinents',
           'transferable skills': 'Fähigkeiten, die man in vielen Berufen nutzen kann'},
    'es': {'employees': 'las personas que trabajan para una empresa', 'revenue': 'el dinero que recibe una empresa por sus ventas (ingresos)',
           'subsidiary': 'una empresa controlada por otra más grande (filial)', 'expertise': 'conocimiento y habilidad especiales en un área',
           'well-known': 'famoso, conocido por mucha gente', 'vehicle': 'un coche, un autobús u otra máquina de transporte',
           'region': 'una zona de un país o continente', 'transferable skills': 'habilidades que puedes usar en muchos trabajos distintos'},
}

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Which English mistake do German speakers make most?',
        'Do you take English lessons, or learn alone?',
        'What do you do in your job?',
        'How do you travel to work?',
        'What did you do last weekend?',
        'Which English word do you always confuse?',
    ], 'talk', 3),
    ('stage',),
    ('mc', 'e1', 'mcT', A1, ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'], None),
    ('stage',),
    ('mc', 'e2', 'mcT2', A2, ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8'], None),
    ('stage',),
    ('mc', 'e3', 'mcT', A3, ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'], None),
    ('raw', None),
    ('talk', 'eT', 'tk2T', [
        'What sport <strong>do you do</strong>, or would you like to do?',
        'Which course would you like to <strong>take</strong>?',
        'Who do you <strong>work for</strong>, and what does the company <strong>provide</strong>?',
        'What did you do <strong>a long time ago</strong> that you don’t do now?',
        'Do you go <strong>on foot</strong>, <strong>by bike</strong> or <strong>by car</strong>?',
        'Where did you <strong>go</strong> skiing or hiking last?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['take lessons', 'work for', 'a long time ago', 'do business', 'on foot', 'a lot of', 'depends on']

W = {
    'en': [
        'We TAKE (or HAVE) lessons. “Make lessons” is Unterricht machen, translated word for word.',
        'We DO activities: travelling, sport, work. MAKE is for producing something.',
        'You work FOR a company, your employer. “Work to” and “work from a company” are German-style.',
        'The fixed phrase is DO BUSINESS WITH someone, although German says Geschäfte machen.',
        'We TAKE a course. “Visit a course” is a translation of einen Kurs besuchen.',
        'We DO sport. “Drive sport” is Sport treiben word for word.',
        'Companies PROVIDE services and PRODUCE goods: services are not physical.',
        'Cars are PRODUCED (or made). PROVIDE is for services.',
        'TAKE lessons, plural LESSONS, and no preposition before EVERY TUESDAY.',
        'Work FOR a company, and IN a city. “I am work” mixes two verb forms.',
        'AGO counts back from now (vor langer Zeit). Keep the A, and BY HORSE has no article.',
        'THAT is he/she/it, so MEANS. “That’s mean” = that is mean: unkind!',
        'EAT is a verb; the noun is FOOD. MUST + the base verb, no TO; GOOD, not WELL.',
        'TAKE a train; the past is TOOK. YESTERDAY → past simple; movement towards a place → TO.',
        'Outdoor activities: GO + -ING (go fishing, go skiing), no TO, and AT THE WEEKEND in British English.',
        'In positive sentences: A LOT OF, not MUCH. The phrase needs both A and OF.',
        'Work FOR an employer. German BEI often becomes FOR.',
        'Students TAKE lessons; teachers GIVE them.',
        'AGO counts back from NOW. BEFORE needs another past point.',
        'DEPEND ON. German abhängen VON makes OF and FROM tempting.',
        'Compensation FOR a problem: for the delay, for the cancelled flight.',
        'Countries and cities take IN: in Germany, in Berlin.',
        'BY car, BY train, BY bus — but ON foot. Learn this one.',
        'ACROSS Europe (or THROUGHOUT Europe) = in many places over the whole area.',
    ],
    'de': [
        'Man sagt TAKE (oder HAVE) lessons. „Make lessons“ ist Unterricht machen, Wort für Wort.',
        'Tätigkeiten nehmen DO: travelling, sport, work. MAKE heißt etwas herstellen.',
        'Man arbeitet FOR a company, für den Arbeitgeber. „Work to“ und „work from a company“ sind Denglisch.',
        'Die feste Wendung ist DO BUSINESS WITH someone, obwohl man auf Deutsch Geschäfte macht.',
        'Man sagt TAKE a course. „Visit a course“ ist einen Kurs besuchen, übersetzt.',
        'Man sagt DO sport. „Drive sport“ ist Sport treiben, Wort für Wort.',
        'Firmen PROVIDE services (bieten Dienstleistungen) und PRODUCE goods (stellen Waren her).',
        'Autos werden PRODUCED (oder made). PROVIDE ist für Dienstleistungen.',
        'TAKE lessons, LESSONS im Plural, und keine Präposition vor EVERY TUESDAY.',
        'Work FOR a company und IN a city. „I am work“ mischt zwei Verbformen.',
        'AGO zählt von jetzt zurück (vor langer Zeit). Das A bleibt, und BY HORSE hat keinen Artikel.',
        'THAT ist he/she/it, also MEANS. „That’s mean“ = das ist gemein!',
        'EAT ist ein Verb; das Nomen ist FOOD. MUST + Grundform ohne TO; GOOD, nicht WELL.',
        'Man nimmt einen Zug: TAKE, Vergangenheit TOOK. YESTERDAY → Past Simple; Richtung → TO.',
        'Aktivitäten draußen: GO + -ING (go fishing, go skiing), ohne TO, und britisch AT THE WEEKEND.',
        'In positiven Sätzen A LOT OF, nicht MUCH. Die Wendung braucht A und OF.',
        'Work FOR für den Arbeitgeber. Deutsch BEI wird oft zu FOR.',
        'Schüler TAKE lessons; Lehrer GIVE sie.',
        'AGO zählt von JETZT zurück. BEFORE braucht einen anderen Punkt in der Vergangenheit.',
        'DEPEND ON. Deutsch abhängen VON macht OF und FROM verlockend.',
        'Entschädigung FOR ein Problem: for the delay, for the cancelled flight.',
        'Länder und Städte nehmen IN: in Germany, in Berlin.',
        'BY car, BY train, BY bus — aber ON foot (zu Fuß). Das muss man lernen.',
        'ACROSS Europe (oder THROUGHOUT Europe) = an vielen Orten in ganz Europa.',
    ],
    'es': [
        'Se dice TAKE (o HAVE) lessons. «Make lessons» es una traducción palabra por palabra del alemán.',
        'Las actividades llevan DO: travelling, sport, work. MAKE es para producir algo.',
        'Se trabaja FOR a company, para quien te contrata. «Work to» y «work from a company» son errores de alemanes.',
        'La expresión fija es DO BUSINESS WITH someone.',
        'Se dice TAKE a course. «Visit a course» viene del alemán einen Kurs besuchen.',
        'Se dice DO sport. «Drive sport» viene del alemán Sport treiben.',
        'Las empresas PROVIDE services y PRODUCE goods: los servicios no son físicos.',
        'Los coches se PRODUCE (o make). PROVIDE es para servicios.',
        'TAKE lessons, LESSONS en plural, y sin preposición antes de EVERY TUESDAY.',
        'Work FOR a company, e IN a city. «I am work» mezcla dos formas verbales.',
        'AGO cuenta hacia atrás desde ahora (hace mucho tiempo). Se mantiene la A, y BY HORSE no lleva artículo.',
        'THAT es he/she/it, así que MEANS. «That’s mean» = eso es cruel.',
        'EAT es un verbo; el sustantivo es FOOD. MUST + verbo base, sin TO; GOOD, no WELL.',
        'TAKE a train; el pasado es TOOK. YESTERDAY → past simple; hacia un lugar → TO.',
        'Actividades al aire libre: GO + -ING (go fishing, go skiing), sin TO, y en británico AT THE WEEKEND.',
        'En oraciones afirmativas, A LOT OF, no MUCH. La expresión necesita A y OF.',
        'Work FOR para quien te contrata. El alemán BEI suele ser FOR.',
        'Los alumnos TAKE lessons; los profesores las GIVE.',
        'AGO cuenta desde AHORA. BEFORE necesita otro punto en el pasado.',
        'DEPEND ON. El alemán abhängen VON hace tentadores OF y FROM.',
        'Compensación FOR un problema: for the delay, for the cancelled flight.',
        'Países y ciudades llevan IN: in Germany, in Berlin.',
        'BY car, BY train, BY bus, pero ON foot (a pie). Hay que memorizarlo.',
        'ACROSS Europe (o THROUGHOUT Europe) = en muchos lugares de toda Europa.',
    ],
}

T = {
    'en': dict(
        coverTitle='Goodbye, <br><em>Denglisch!</em>',
        coverSub='Swiss Precision: the mistakes German speakers make most — do, make and take, tricky prepositions, and business vocabulary.',
        chipLevel='A2', chipFocus='do · make · take · prepositions', chipCount='31 slides',
        eW='Warm-up', eT='Let’s talk', e1='Do, make, take', e2='Fix the mistake', e3='Prepositions', e4='Business words',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the correct word', mcT2='Choose the correct version',
        matchT='Business vocabulary', matchHint='Click a word, then its meaning.', matchWhy='Eight business words: each one with its meaning.',
        actTitle='Goodbye, Denglisch', actUse='Use at least four:',
        actSpeakBrief='In pairs. Introduce yourself and your company to a new contact.',
        actSpeak1='Say who you WORK FOR, what your company PROVIDES or PRODUCES, and where it has a SUBSIDIARY.',
        actSpeak2='Tell your partner about a course you TAKE, or a sport you DO.',
        actSpeak3='Describe a trip: you TOOK a train, you WENT hiking, you walked ON FOOT.',
        actWriteKind='Writing',
        actWriteBrief='Write a short email (80–100 words) to a new client: who you work for, what your company does, and what you did last weekend.',
        actPlaceholder='Dear Mr Keller, I work for …',
    ),
    'de': dict(
        coverTitle='Goodbye, <br><em>Denglisch!</em>',
        coverSub='Swiss Precision: die häufigsten Fehler deutschsprachiger Lernender — do, make und take, knifflige Präpositionen und Wirtschaftsvokabular.',
        chipLevel='A2', chipFocus='do · make · take · Präpositionen', chipCount='31 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', e1='Do, make, take', e2='Korrigiere den Fehler', e3='Präpositionen', e4='Wirtschaftswörter',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle das richtige Wort', mcT2='Wähle die richtige Version',
        matchT='Wirtschaftsvokabular', matchHint='Klicke ein Wort an, dann seine Bedeutung.', matchWhy='Acht Wirtschaftswörter, jedes mit seiner Bedeutung.',
        actTitle='Goodbye, Denglisch', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit. Stell dich und deine Firma einem neuen Kontakt vor.',
        actSpeak1='Sag, für wen du arbeitest (WORK FOR), was deine Firma anbietet oder herstellt (PROVIDES / PRODUCES) und wo sie eine Tochtergesellschaft hat (SUBSIDIARY).',
        actSpeak2='Erzähl von einem Kurs, den du besuchst (TAKE), oder einem Sport, den du treibst (DO).',
        actSpeak3='Beschreib eine Reise: Du hast einen Zug genommen (TOOK), bist wandern gegangen (WENT hiking), bist zu Fuß gegangen (ON FOOT).',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einem neuen Kunden eine kurze E-Mail (80–100 Wörter): für wen du arbeitest, was deine Firma macht und was du letztes Wochenende gemacht hast.',
        actPlaceholder='Dear Mr Keller, I work for …',
    ),
    'es': dict(
        coverTitle='Goodbye, <br><em>Denglisch!</em>',
        coverSub='Swiss Precision: los errores más típicos de quien habla alemán — do, make y take, preposiciones difíciles y vocabulario de empresa.',
        chipLevel='A2', chipFocus='do · make · take · preposiciones', chipCount='31 diapositivas',
        eW='Para empezar', eT='¡A conversar!', e1='Do, make, take', e2='Corrige el error', e3='Preposiciones', e4='Palabras de empresa',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la palabra correcta', mcT2='Elige la versión correcta',
        matchT='Vocabulario de empresa', matchHint='Haz clic en una palabra y después en su significado.', matchWhy='Ocho palabras de empresa, cada una con su significado.',
        actTitle='Goodbye, Denglisch', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas. Preséntate a ti y a tu empresa a un nuevo contacto.',
        actSpeak1='Di para quién trabajas (WORK FOR), qué ofrece o produce tu empresa (PROVIDES / PRODUCES) y dónde tiene una filial (SUBSIDIARY).',
        actSpeak2='Cuéntale a tu compañero un curso que haces (TAKE) o un deporte que practicas (DO).',
        actSpeak3='Describe un viaje: tomaste un tren (TOOK), fuiste de excursión (WENT hiking), caminaste a pie (ON FOOT).',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un correo corto (80–100 palabras) a un cliente nuevo: para quién trabajas, qué hace tu empresa y qué hiciste el fin de semana pasado.',
        actPlaceholder='Dear Mr Keller, I work for …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

E = T['en']
# The match grid needs the full width, so no picture beside it.
# Two slides of four: eight pairs with a gloss under each definition ran
# 74px off the canvas in German and Spanish once answered.
MATCH = ''.join(D.match(PAIRS[i:i + 4], 'e4', E['e4'], 'matchT', E['matchT'], 'matchHint', E['matchHint'],
                        'matchWhy', glosses=MG) for i in (0, 4))
SPEC['flow'] = [st if st != ('raw', None) else ('raw', MATCH) for st in SPEC['flow']]

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
