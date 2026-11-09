# -*- coding: utf-8 -*-
"""Linking Devices: The World of Cars (B2). House style 1, 21 slides.

Rebuilt 2026-11-06 from `forbes-linking-devices-cars.html`: five multiple
choice, five drag-into-the-gap items and five sentence builds. All fifteen
are kept; the drag items are multiple choice (one slide each).

Fixed:
  * Gap 3 was keyed WRONG: "The engine produces 400 horsepower. ___, it is
    surprisingly fuel-efficient" took FURTHERMORE, but SURPRISINGLY signals
    a contrast — EVEN SO and DESPITE THIS are right, and both were in the
    pool marked wrong. The key is EVEN SO now, and DESPITE THIS is out.
  * Gap 5 (German precision, Japanese reliability) accepted HOWEVER as well
    as SIMILARLY. HOWEVER is out of the options.
  * Build 1 could be put together in two acceptable orders ("in the long
    term" moves). That piece is joined to its clause.
Added: the linking devices by job as rule cards, speaking, activation.

Run from the repo root:  py lesson-template/build/build_linking_cars.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='forbes-linking-devices-cars.html',
    title='Linking Devices: The World of Cars (B2)',
    folder='LinkingCars',
    scheme='cool',
    style='hs1',
    # MC 1 runs 23px deep beside a frame once answered in DE/ES, and MC 5 is
    # too long for any frame: both take the full width.
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'a vintage sports car on a winding coastal road',
        'talk': 'an electric car charging outside a modern house',
            'la2': 'a red sports car racing past a petrol pump',
        'la3': 'engineers fitting a battery pack into a car chassis in a factory',
        'la4': 'a self-driving car stopping as a cyclist and pedestrians cross in the rain',
        'lb1': 'commuters cycling past a long traffic jam',
        'lb2': 'a car reviewer frowning at the inside of a shiny new car',
        'lb3': 'a powerful car cruising calmly along an empty motorway',
        'lb4': 'a small city car parked in a narrow old street',
        'lb5': 'two cars side by side in a showroom, one silver, one red',
        'lo1': 'a family plugging in their electric car at home at night',
        'lo2': 'a large SUV squeezing down a crowded city street',
        'lo3': 'a row of new charging stations along a motorway',
        'lo4': 'an engineering team celebrating beside a race car in the pits',
        'lo5': 'a driver filling up a big car at a petrol station',
        'talk2': 'two friends talking beside a car in a garage',
        'results': 'a classic car parked at sunset on an empty road',
    },
    pop={'hero': (None, 'square'), 'la2': (None, 'free'), 'talk2': (None, 'blob')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


MC = [
    q('Electric vehicles are becoming increasingly popular. ____, many drivers still worry about running out of battery on long journeys.',
      ['Nevertheless', 'Furthermore', 'Consequently', 'Similarly'], 1),
    q('The new sports car achieved record-breaking acceleration. ____, its fuel consumption was much higher than the standard model’s.',
      ['However', 'As a result', 'In other words', 'Therefore'], 2),
    q('The manufacturer invested heavily in battery technology. ____, the new model can travel over 500 kilometres on one charge.',
      ['As a result', 'By contrast', 'Nonetheless', 'For instance'], 3),
    q('Self-driving systems must detect pedestrians, cyclists and road signs. ____, they must respond correctly in bad weather.',
      ['In addition', 'Although', 'Since', 'Despite this'], 4),
    q('Classic car fans prefer mechanical simplicity. ____ modern cars offer better safety and comfort, they say newer cars have lost their character.',
      ['Even though', 'Given that', 'Owing to', 'Provided that'], 5),
]
GAP = [
    q('Petrol prices rose sharply last year. ____, many commuters switched to cycling or public transport.',
      ['As a result', 'In contrast', 'Nevertheless', 'Despite this'], 6),
    q('The car passed all its safety tests. ____, some reviewers raised concerns about the interior.',
      ['However', 'Therefore', 'Likewise', 'Consequently'], 7),
    q('The engine produces 400 horsepower. ____, it is surprisingly fuel-efficient on motorway journeys.',
      ['Even so', 'Furthermore', 'Similarly', 'As a result'], 8),
    q('City drivers rarely need four-wheel drive. ____, models designed for city use often leave it out.',
      ['For this reason', 'In addition', 'By contrast', 'On the other hand'], 9),
    q('German manufacturers are well known for engineering precision. ____, Japanese brands have a strong reputation for reliability.',
      ['Similarly', 'Therefore', 'As a result', 'For this reason'], 10),
]
ORDERS = [
    (['Although electric cars cost more to buy,', 'they tend to be cheaper to run in the long term', 'because of lower fuel and maintenance costs.'], None, 'w11'),
    (['Sales of SUVs have grown steadily;', 'however,', 'environmental campaigners argue', 'that their popularity raises urban emissions.'], None, 'w12'),
    (['Provided that charging networks keep growing,', 'electric vehicles are likely to', 'replace petrol cars', 'within the next two decades.'], None, 'w13'),
    (['The test driver completed the circuit in record time.', 'As a result,', 'the engineering team celebrated', 'and began planning further improvements.'], None, 'w14'),
    (['Despite rising fuel costs,', 'many drivers still prefer large engines', 'because they value performance', 'over economy.'], None, 'w15'),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Would you buy an electric car? Why, or why not?',
        'What was the first car you drove or remember?',
        'Is a car a necessity or a luxury where you live?',
        'Which matters more to you: speed, comfort or price?',
        'Will self-driving cars ever be safe?',
        'Do you prefer old cars or new ones?',
    ], 'talk', 3),
    ('stage',),
    ('rules', 'eR', 'rT', [
        ('pContrast', [(None, 'however · nevertheless · nonetheless'), (None, 'even so · despite this · by contrast')], 'Electric cars are popular. <strong>Nevertheless</strong>, …'),
        ('pResult', [(None, 'as a result · therefore · consequently'), (None, 'for this reason')], 'Prices rose. <strong>As a result</strong>, …'),
        ('pAdd', [(None, 'in addition · furthermore · similarly · likewise')], 'They must see signs. <strong>In addition</strong>, …'),
        ('pClause', [(None, 'although · even though + clause'), (None, 'despite + noun · provided that + clause')], '<strong>Although</strong> they cost more, …'),
    ], None),
    ('mc', 'e1', 'mcT', MC, [None, 'la2', 'la3', 'la4', None], None),
    ('stage',),
    ('mc', 'e2', 'mcT', GAP, ['lb1', 'lb2', 'lb3', 'lb4', 'lb5'], None),
    ('stage',),
    ('order', 'e3', 'orderT', 'orderHint', ORDERS, ['lo1', 'lo2', 'lo3', 'lo4', 'lo5'], None),
    ('talk', 'eT', 'tk2T', [
        'Electric cars are cheap to run. <strong>However</strong>, … — finish the sentence.',
        'What happens to traffic when petrol prices rise? <strong>As a result</strong>, …',
        '<strong>Although</strong> I like cars, … — finish it about yourself.',
        'Should cities ban old diesel cars? Give a reason with <strong>for this reason</strong>.',
        '<strong>Provided that</strong> … , I would buy an electric car.',
        'Compare two car brands with <strong>by contrast</strong> or <strong>similarly</strong>.',
    ], 'talk2', 3),
]
SPEC['chips'] = ['however', 'as a result', 'in addition', 'although', 'nevertheless', 'provided that', 'despite']

W = {
    'en': [
        'NEVERTHELESS introduces a contrast: popular, but still worrying. FURTHERMORE and SIMILARLY add; CONSEQUENTLY gives a result.',
        'HOWEVER: a contrast — fast, but thirsty. AS A RESULT and THEREFORE give a result; IN OTHER WORDS rephrases.',
        'AS A RESULT: cause and effect — the investment led to the range. BY CONTRAST and NONETHELESS contrast; FOR INSTANCE gives an example.',
        'IN ADDITION adds another requirement. ALTHOUGH and DESPITE THIS contrast; SINCE gives a reason.',
        'EVEN THOUGH + a clause concedes a point: they admit modern cars are safer. GIVEN THAT and OWING TO give reasons; PROVIDED THAT is a condition.',
        'Prices rose, so people switched: a result, AS A RESULT.',
        'They passed the tests, but there were concerns: a contrast, HOWEVER.',
        'SURPRISINGLY signals a contrast with 400 horsepower: EVEN SO. FURTHERMORE would only add.',
        'Drivers don’t need it, so the models leave it out: FOR THIS REASON.',
        'Two countries, each known for a strength: SIMILARLY. THEREFORE would mean one causes the other.',
        'ALTHOUGH opens with a capital letter and a comma; the result clause and the reason follow.',
        'A semicolon, then HOWEVER and a comma, then the contrasting argument.',
        'PROVIDED THAT introduces the condition first; the prediction follows.',
        'Two sentences: the cause, then AS A RESULT and its consequence.',
        'DESPITE + a noun phrase, then the main clause, then the reason with BECAUSE.',
    ],
    'de': [
        'NEVERTHELESS leitet einen Gegensatz ein („dennoch“): beliebt, aber trotzdem Sorgen. FURTHERMORE und SIMILARLY fügen hinzu; CONSEQUENTLY nennt eine Folge.',
        'HOWEVER: ein Gegensatz — schnell, aber durstig. AS A RESULT und THEREFORE nennen eine Folge; IN OTHER WORDS formuliert um.',
        'AS A RESULT: Ursache und Wirkung („infolgedessen“). BY CONTRAST und NONETHELESS stellen gegenüber; FOR INSTANCE nennt ein Beispiel.',
        'IN ADDITION fügt eine weitere Anforderung hinzu („außerdem“). ALTHOUGH und DESPITE THIS stellen gegenüber; SINCE nennt einen Grund.',
        'EVEN THOUGH + Nebensatz räumt etwas ein („obwohl“). GIVEN THAT und OWING TO nennen Gründe; PROVIDED THAT ist eine Bedingung.',
        'Die Preise stiegen, also stiegen die Leute um: eine Folge, AS A RESULT.',
        'Tests bestanden, aber Bedenken: ein Gegensatz, HOWEVER.',
        'SURPRISINGLY zeigt einen Gegensatz zu 400 PS: EVEN SO („trotzdem“). FURTHERMORE würde nur hinzufügen.',
        'Man braucht ihn nicht, also lassen die Modelle ihn weg: FOR THIS REASON („aus diesem Grund“).',
        'Zwei Länder, jedes für eine Stärke bekannt: SIMILARLY („ebenso“). THEREFORE hieße, das eine verursacht das andere.',
        'ALTHOUGH beginnt mit Großbuchstaben und Komma; der Hauptsatz und der Grund folgen.',
        'Ein Semikolon, dann HOWEVER mit Komma, dann das Gegenargument.',
        'PROVIDED THAT nennt zuerst die Bedingung; die Vorhersage folgt.',
        'Zwei Sätze: die Ursache, dann AS A RESULT und die Folge.',
        'DESPITE + Nominalgruppe, dann der Hauptsatz, dann der Grund mit BECAUSE.',
    ],
    'es': [
        'NEVERTHELESS introduce un contraste («sin embargo»): populares, pero aún preocupan. FURTHERMORE y SIMILARLY añaden; CONSEQUENTLY da un resultado.',
        'HOWEVER: un contraste — rápido, pero gasta mucho. AS A RESULT y THEREFORE dan un resultado; IN OTHER WORDS reformula.',
        'AS A RESULT: causa y efecto («como resultado»). BY CONTRAST y NONETHELESS contrastan; FOR INSTANCE da un ejemplo.',
        'IN ADDITION añade otro requisito («además»). ALTHOUGH y DESPITE THIS contrastan; SINCE da una razón.',
        'EVEN THOUGH + oración concede algo («aunque»). GIVEN THAT y OWING TO dan razones; PROVIDED THAT es una condición.',
        'Los precios subieron, así que la gente cambió: un resultado, AS A RESULT.',
        'Pasó las pruebas, pero hubo dudas: un contraste, HOWEVER.',
        'SURPRISINGLY marca un contraste con los 400 caballos: EVEN SO («aun así»). FURTHERMORE solo añadiría.',
        'No lo necesitan, así que los modelos lo omiten: FOR THIS REASON («por esta razón»).',
        'Dos países, cada uno conocido por una virtud: SIMILARLY («del mismo modo»). THEREFORE significaría que uno causa el otro.',
        'ALTHOUGH empieza con mayúscula y lleva coma; luego van la oración principal y la razón.',
        'Un punto y coma, luego HOWEVER con coma, luego el argumento contrario.',
        'PROVIDED THAT presenta primero la condición; después va la predicción.',
        'Dos oraciones: la causa, luego AS A RESULT y su consecuencia.',
        'DESPITE + sintagma nominal, luego la oración principal, luego la razón con BECAUSE.',
    ],
}

T = {
    'en': dict(
        coverTitle='Linking <br><em>Devices</em>',
        coverSub='The world of cars: the words that join ideas — contrast, result, addition and concession — in fifteen sentences about driving.',
        chipLevel='B2', chipFocus='however · as a result · although', chipCount='21 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Choose the link', e2='Fill the gap', e3='Build the sentence',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best linking device',
        rT='Linking devices by job', pContrast='Contrast', pResult='Result', pAdd='Addition', pClause='Inside one sentence',
        orderT='Put the sentence in order', orderHint='Click the pieces in order. Capitals and commas are clues.',
        actTitle='The car debate', actUse='Use at least five:',
        actSpeakBrief='In pairs: should your city ban petrol cars from the centre?',
        actSpeak1='One of you is for, one against. Give two reasons each, linked with AS A RESULT and IN ADDITION.',
        actSpeak2='Answer your partner’s point with HOWEVER or NEVERTHELESS.',
        actSpeak3='Find a compromise that starts with PROVIDED THAT …',
        actWriteKind='Writing',
        actWriteBrief='Write a short opinion paragraph (150–180 words): should cities ban petrol cars? Use at least six linking devices from this lesson, and at least one from each group.',
        actPlaceholder='Although petrol cars are convenient, …',
    ),
    'de': dict(
        coverTitle='Linking <br><em>Devices</em>',
        coverSub='Die Welt der Autos: die Wörter, die Gedanken verbinden — Gegensatz, Folge, Ergänzung und Einräumung — in fünfzehn Sätzen übers Autofahren.',
        chipLevel='B2', chipFocus='however · as a result · although', chipCount='21 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Wähle das Bindewort', e2='Füll die Lücke', e3='Bau den Satz',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle das beste Bindewort',
        rT='Bindewörter nach Aufgabe', pContrast='Gegensatz', pResult='Folge', pAdd='Ergänzung', pClause='Innerhalb eines Satzes',
        orderT='Bring den Satz in Ordnung', orderHint='Klicke die Teile der Reihe nach an. Großbuchstaben und Kommas helfen.',
        actTitle='Die Autodebatte', actUse='Verwende mindestens fünf:',
        actSpeakBrief='Zu zweit: Sollte eure Stadt Benzinautos aus dem Zentrum verbannen?',
        actSpeak1='Eine Person ist dafür, eine dagegen. Nennt je zwei Gründe, verbunden mit AS A RESULT und IN ADDITION.',
        actSpeak2='Antworte auf das Argument deines Partners mit HOWEVER oder NEVERTHELESS.',
        actSpeak3='Findet einen Kompromiss, der mit PROVIDED THAT … beginnt.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einen kurzen Meinungsabsatz (150–180 Wörter): Sollten Städte Benzinautos verbieten? Verwende mindestens sechs Bindewörter aus dieser Lektion, mindestens eins aus jeder Gruppe.',
        actPlaceholder='Although petrol cars are convenient, …',
    ),
    'es': dict(
        coverTitle='Linking <br><em>Devices</em>',
        coverSub='El mundo del coche: las palabras que unen ideas — contraste, resultado, adición y concesión — en quince oraciones sobre conducir.',
        chipLevel='B2', chipFocus='however · as a result · although', chipCount='21 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='Elige el conector', e2='Completa el hueco', e3='Construye la oración',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige el mejor conector',
        rT='Los conectores según su función', pContrast='Contraste', pResult='Resultado', pAdd='Adición', pClause='Dentro de una oración',
        orderT='Ordena la oración', orderHint='Haz clic en las piezas en orden. Las mayúsculas y las comas son pistas.',
        actTitle='El debate del coche', actUse='Usa al menos cinco:',
        actSpeakBrief='En parejas: ¿debería tu ciudad prohibir los coches de gasolina en el centro?',
        actSpeak1='Uno está a favor y otro en contra. Den dos razones cada uno, unidas con AS A RESULT e IN ADDITION.',
        actSpeak2='Responde al argumento de tu compañero con HOWEVER o NEVERTHELESS.',
        actSpeak3='Busquen un acuerdo que empiece con PROVIDED THAT …',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un párrafo de opinión (150–180 palabras): ¿deberían las ciudades prohibir los coches de gasolina? Usa al menos seis conectores de esta lección, al menos uno de cada grupo.',
        actPlaceholder='Although petrol cars are convenient, …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
