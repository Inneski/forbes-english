# -*- coding: utf-8 -*-
"""The First King of Prussia: Prepositions of Power (C1, Part 4). House
style 2, 18 slides, on the two Friedrich/ plates.

Rebuilt 2026-11-06 from `friedrich_prepositions_c1.html`: five multiple
choice, five dropdown gap-fills and a five-gap cloze passage about
Friedrich I's self-coronation. All fifteen items are kept. The cloze is now
TYPED, so a gap where two prepositions are right (rest ON / UPON) can
accept both; a dropdown could only mark one of them wrong.

Fixed — the page's own explanations conceded most of these:
  * Two right answers offered side by side: CONTINGENT ON / UPON, INSISTED
    ON / UPON, RESTED ON / UPON (twice), and "without dispute" ("possible
    but less idiomatic"). One of each pair is gone from the options.
  * "Contingent upon … is archaic": it is not; it is standard formal
    English. The explanation now says both are right.
  * Also correct as written: "the coronation ceremony AT Königsberg",
    "elevate his house BEYOND the rank of elector", "in pursuit of
    recognition", "not merely in luxury but IN TERMS OF symbolic intent".
    Stems or distractors changed so the key is the only answer.
  * The prepositions now come as a recap AFTER the items (a card before
    them would hand out the answers).

Run from the repo root:  py lesson-template/build/build_friedrich_prepositions.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='friedrich_prepositions_c1.html',
    title='The First King of Prussia: Prepositions of Power (C1)',
    folder='Friedrich',
    hero='friedrich-closeup',
    scheme='slate',
    art={
        'talk': ('talk', 'two speech bubbles above a gilded crown on a cushion'),
        'b': ('law', 'a treaty document with a wax seal beside a quill'),
        'act': ('pair', 'two Baroque chairs facing each other in an empty hall'),
    },
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


MC = [
    q('Friedrich I was acutely conscious ____ the need to project royal magnificence in order to legitimise his new title.',
      ['of', 'about', 'regarding', 'towards'], 1),
    q('The coronation took place ____ East Prussia, far from the Emperor’s court in Vienna.', ['in', 'at', 'within', 'by'], 2),
    q('Friedrich’s elevation to kingship was contingent ____ the support of the Holy Roman Emperor, Leopold I.',
      ['on', 'from', 'about', 'to'], 3),
    q('His court became renowned ____ its lavish spending on architecture, the arts and elaborate ritual.',
      ['for', 'because of', 'through', 'as'], 4),
    q('Friedrich insisted ____ being called “King in Prussia” rather than “King of Prussia” — a distinction of real diplomatic weight.',
      ['on', 'about', 'for', 'at'], 5),
]
FITB = [
    q('The Brandenburg court was transformed ____ gaining recognition as a major European power.',
      ['with a view to', 'in search of', 'by means of', 'in exchange of'], 6),
    q('Friedrich’s claim to kingship rested ____ a complex argument of dynastic right and imperial negotiation.',
      ['on', 'onto', 'over', 'across'], 7),
    q('Founding the Prussian Academy of Sciences in 1700 was very much ____ keeping with the Enlightenment ideal of the learned monarch.',
      ['in', 'within', 'at', 'by'], 8),
    q('The Treaty of Utrecht confirmed that the Hohenzollern title was ____ dispute, cementing Friedrich’s gamble as a lasting triumph.',
      ['beyond', 'under', 'above', 'past'], 9),
    q('Friedrich spent lavishly ____ proportion to the state’s actual revenues, bringing it close to bankruptcy.',
      ['out of', 'beyond', 'in excess of', 'without'], 10),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Which historical ruler do you find most interesting?',
        'Why do leaders spend money on ceremonies and palaces?',
        'Is image more important than power?',
        'Which building in your country was built to impress?',
        'Can a title change how people see you?',
        'What would you build if you were a king or queen?',
    ], 'talk', 3),
    ('mc', 'e1', 'mcT', MC, 'friedrich-profile', None),
    ('mc', 'e2', 'mcT', FITB, 'b', 'left'),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('Born ______ the Hohenzollern dynasty, he inherited the Electorate of Brandenburg — a Protestant state of modest means.',
         ['into'], 'w11'),
        ('Yet Friedrich was determined to elevate his house ______ the rank of mere elector and ______ the ranks of European royalty.',
         ['above', 'into'], 'w12'),
    ]),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('His strategy rested heavily ______ the cultivation of Baroque splendour.', ['on|upon'], 'w14'),
        ('His court at Berlin rivalled Versailles not merely in luxury but ______ symbolic intent.', ['in'], 'w15'),
    ]),
    ('rules', 'eR', 'recT', [
        ('pAdj', [(None, 'conscious OF · aware OF'), (None, 'renowned FOR · famous FOR'), (None, 'contingent ON / UPON')], None),
        ('pVerb', [(None, 'insist ON / UPON'), (None, 'rest ON / UPON'), (None, 'be born INTO a family'),
                   (None, 'elevate ABOVE · transform INTO')], None),
        ('pFixed', [(None, 'with a view to + -ing'), (None, 'in keeping with'), (None, 'beyond dispute · beyond doubt'),
                    (None, 'out of proportion to')], None),
    ], None),
    ('talk', 'eT', 'tk2T', [
        'Which leader today is <strong>renowned for</strong> their image?',
        'Is power <strong>contingent on</strong> public opinion?',
        'What is <strong>beyond dispute</strong> about your country’s history?',
        'When is spending <strong>out of proportion to</strong> its results?',
        'What would you <strong>insist on</strong> if you ran a country?',
        'Which tradition is <strong>in keeping with</strong> your country’s values?',
    ], None, 3),
]
SPEC['chips'] = ['in keeping with', 'beyond dispute', 'renowned for', 'insist on', 'contingent on', 'with a view to', 'out of proportion to']

W = {
    'en': [
        'CONSCIOUS OF, like AWARE OF and MINDFUL OF. “Conscious about” is non-standard in formal writing.',
        'IN with regions, countries and cities: in East Prussia. AT is for a point or a venue.',
        'CONTINGENT ON (or UPON — both are standard, UPON more formal) = depending on a condition.',
        'RENOWNED FOR, like FAMOUS FOR and NOTED FOR. RENOWNED AS needs a noun: renowned as a patron.',
        'INSIST ON (or UPON, more formal) + -ING: insisted on being called …',
        'WITH A VIEW TO + -ING = with the aim of. “In search of gaining” and “in exchange of” are not English.',
        'REST ON (or UPON) = be based on. ONTO is movement onto a surface.',
        'IN KEEPING WITH: a fixed phrase meaning consistent with.',
        'BEYOND DISPUTE = not open to challenge, like BEYOND DOUBT. UNDER DISPUTE means the opposite.',
        'OUT OF PROPORTION TO = not balanced with. IN EXCESS OF means more than an amount.',
        'BORN INTO a family, a class or a dynasty. (BORN TO is with parents: born to a king.)',
        'ELEVATE ABOVE = lift higher than; and INTO the ranks of = a change of status.',
        '',
        'REST ON or REST UPON: both are right here; UPON is more formal.',
        'The parallel “not merely IN luxury but IN symbolic intent” repeats IN.',
    ],
    'de': [
        'CONSCIOUS OF, wie AWARE OF und MINDFUL OF („sich bewusst sein“). „Conscious about“ ist im formellen Englisch nicht üblich.',
        'IN bei Regionen, Ländern und Städten: in East Prussia. AT steht für einen Punkt oder Veranstaltungsort.',
        'CONTINGENT ON (oder UPON — beide sind Standard, UPON förmlicher) = abhängig von einer Bedingung.',
        'RENOWNED FOR, wie FAMOUS FOR und NOTED FOR („berühmt für“). RENOWNED AS braucht ein Nomen: renowned as a patron.',
        'INSIST ON (oder UPON, förmlicher) + -ING: insisted on being called … („bestand darauf“).',
        'WITH A VIEW TO + -ING = mit dem Ziel. „In search of gaining“ und „in exchange of“ sind kein Englisch.',
        'REST ON (oder UPON) = beruhen auf. ONTO ist Bewegung auf eine Fläche.',
        'IN KEEPING WITH: feste Wendung für „im Einklang mit“.',
        'BEYOND DISPUTE = unbestreitbar, wie BEYOND DOUBT. UNDER DISPUTE bedeutet das Gegenteil („umstritten“).',
        'OUT OF PROPORTION TO = in keinem Verhältnis zu. IN EXCESS OF heißt mehr als eine Menge.',
        'BORN INTO eine Familie, einen Stand, eine Dynastie. (BORN TO bei Eltern: born to a king.)',
        'ELEVATE ABOVE = über etwas erheben; INTO the ranks of = ein Wechsel des Standes.',
        '',
        'REST ON oder REST UPON: hier ist beides richtig; UPON ist förmlicher.',
        'Die Parallele „not merely IN luxury but IN symbolic intent“ wiederholt IN.',
    ],
    'es': [
        'CONSCIOUS OF, como AWARE OF y MINDFUL OF («consciente de»). «Conscious about» no es estándar en inglés formal.',
        'IN con regiones, países y ciudades: in East Prussia. AT es para un punto o un lugar concreto.',
        'CONTINGENT ON (o UPON — los dos son estándar, UPON más formal) = que depende de una condición.',
        'RENOWNED FOR, como FAMOUS FOR y NOTED FOR («famoso por»). RENOWNED AS necesita un sustantivo: renowned as a patron.',
        'INSIST ON (o UPON, más formal) + -ING: insisted on being called … («insistió en»).',
        'WITH A VIEW TO + -ING = con el objetivo de. «In search of gaining» e «in exchange of» no son inglés.',
        'REST ON (o UPON) = basarse en. ONTO es movimiento sobre una superficie.',
        'IN KEEPING WITH: expresión fija que significa «en consonancia con».',
        'BEYOND DISPUTE = indiscutible, como BEYOND DOUBT. UNDER DISPUTE significa lo contrario («en disputa»).',
        'OUT OF PROPORTION TO = desproporcionado respecto a. IN EXCESS OF significa más de una cantidad.',
        'BORN INTO una familia, una clase o una dinastía. (BORN TO es con los padres: born to a king.)',
        'ELEVATE ABOVE = elevar por encima de; INTO the ranks of = un cambio de rango.',
        '',
        'REST ON o REST UPON: aquí los dos son correctos; UPON es más formal.',
        'El paralelismo «not merely IN luxury but IN symbolic intent» repite IN.',
    ],
}

T = {
    'en': dict(
        coverTitle='The First King <br><em>of Prussia</em>',
        coverSub='Friedrich I crowned himself King in Prussia in 1701. The prepositions of power, politics and Baroque statecraft, through one of Europe’s most theatrical monarchs.',
        chipLevel='C1', chipFocus='prepositions · collocations', chipCount='18 slides',
        eW='Warm-up', eT='Let’s talk', eR='Review', e1='Collocations', e2='Formal phrases', e3='The cloze passage',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the preposition',
        gapT='Complete the passage', gHint='One preposition in each gap.',
        recT='Prepositions of power', pAdj='Adjective + preposition', pVerb='Verb + preposition', pFixed='Fixed phrases',
        actTitle='The coronation debate', actUse='Use at least four:',
        actSpeakBrief='In pairs: one of you advises Friedrich, the other is his treasurer.',
        actSpeak1='Adviser: argue that a lavish coronation is IN KEEPING WITH royal dignity and done WITH A VIEW TO recognition.',
        actSpeak2='Treasurer: argue that the spending is OUT OF PROPORTION TO the state’s revenues.',
        actSpeak3='Agree what must be BEYOND DISPUTE before the ceremony, and what it is CONTINGENT ON.',
        actWriteKind='Writing',
        actWriteBrief='Write a short historical commentary (150–200 words) on Friedrich I: was his coronation a wise investment or an extravagance? Use at least six of the prepositional phrases from this lesson.',
        actPlaceholder='Friedrich I was acutely conscious of …',
    ),
    'de': dict(
        coverTitle='The First King <br><em>of Prussia</em>',
        coverSub='Friedrich I. krönte sich 1701 selbst zum König in Preußen. Die Präpositionen von Macht, Politik und barocker Staatskunst — anhand eines der theatralischsten Monarchen Europas.',
        chipLevel='C1', chipFocus='Präpositionen · Kollokationen', chipCount='18 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Wiederholung', e1='Kollokationen', e2='Formelle Wendungen', e3='Der Lückentext',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die Präposition',
        gapT='Ergänze den Text', gHint='Eine Präposition pro Lücke.',
        recT='Präpositionen der Macht', pAdj='Adjektiv + Präposition', pVerb='Verb + Präposition', pFixed='Feste Wendungen',
        actTitle='Die Krönungsdebatte', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Eine Person berät Friedrich, die andere ist sein Schatzmeister.',
        actSpeak1='Berater: Argumentiere, dass eine prunkvolle Krönung der königlichen Würde entspricht (IN KEEPING WITH) und auf Anerkennung zielt (WITH A VIEW TO).',
        actSpeak2='Schatzmeister: Argumentiere, dass die Ausgaben in keinem Verhältnis zu den Einnahmen stehen (OUT OF PROPORTION TO).',
        actSpeak3='Einigt euch, was vor der Zeremonie unbestreitbar sein muss (BEYOND DISPUTE) und wovon sie abhängt (CONTINGENT ON).',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einen kurzen historischen Kommentar (150–200 Wörter) über Friedrich I.: War seine Krönung eine kluge Investition oder Verschwendung? Verwende mindestens sechs Wendungen aus dieser Lektion.',
        actPlaceholder='Friedrich I was acutely conscious of …',
    ),
    'es': dict(
        coverTitle='The First King <br><em>of Prussia</em>',
        coverSub='Federico I se coronó rey en Prusia en 1701. Las preposiciones del poder, la política y el arte de gobernar barroco, a través de uno de los monarcas más teatrales de Europa.',
        chipLevel='C1', chipFocus='preposiciones · colocaciones', chipCount='18 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Repaso', e1='Colocaciones', e2='Expresiones formales', e3='El texto con huecos',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la preposición',
        gapT='Completa el texto', gHint='Una preposición en cada hueco.',
        recT='Las preposiciones del poder', pAdj='Adjetivo + preposición', pVerb='Verbo + preposición', pFixed='Expresiones fijas',
        actTitle='El debate de la coronación', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: uno aconseja a Federico y el otro es su tesorero.',
        actSpeak1='Consejero: defiende que una coronación espléndida va en consonancia con la dignidad real (IN KEEPING WITH) y busca el reconocimiento (WITH A VIEW TO).',
        actSpeak2='Tesorero: defiende que el gasto es desproporcionado respecto a los ingresos (OUT OF PROPORTION TO).',
        actSpeak3='Acuerden qué debe ser indiscutible antes de la ceremonia (BEYOND DISPUTE) y de qué depende (CONTINGENT ON).',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un breve comentario histórico (150–200 palabras) sobre Federico I: ¿fue su coronación una inversión sensata o un derroche? Usa al menos seis expresiones de esta lección.',
        actPlaceholder='Friedrich I was acutely conscious of …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        if w:
            T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
