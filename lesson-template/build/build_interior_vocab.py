# -*- coding: utf-8 -*-
"""Interior Design Vocabulary (C1). House style 1, 31 slides.

Rebuilt 2026-11-06 from `interior-design-vocabulary.html`, a 24-question
one-at-a-time test (audited clean on 2026-09-16). All 24 items are kept in
their four kinds: in context, definitions, situations, odd one out. The
cover is the page's own hero (InteriorDesignVocab/hero.jpg); the block
pictures are stand-ins on the shopping list.

Fixed: Q24's key "pain threshold" was the only long option (14 against
6-9). It is now "threshold", the same length as "imitation", and the
explanation says what a threshold is.
Added: a recap of the words by family, a gap slide, two speaking fields
and the activation. Explanations translate (EN/DE/ES).

Run from the repo root:  py lesson-template/build/build_interior_vocab.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='interior-design-vocabulary.html',
    title='Interior Design Vocabulary (C1)',
    folder='InteriorDesignVocab',
    scheme='warm',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'an interior design scene',
        'talk': 'a sunlit living room with a reading chair, plants and a big window',
        'c1': 'a designer moving furniture around on a large touch screen',
        'c2': 'a loft apartment in an old factory, original steel beams across the ceiling',
        'c3': 'a hotel lobby with loud clashing patterns around a small painting',
        'c4': 'a gleaming brass spiral staircase in a hotel entrance',
        'c5': 'an apartment where one colour and soft light run through every room',
        'c6': 'a designer and a client comparing lamps in a lighting showroom',
        'c7': 'restorers carefully cleaning old patterned floor tiles',
        'c8': 'a rusty corroded metal handrail on a seafront promenade',
        'c9': 'a room mixing vintage chairs, modern lamps and handmade textiles',
        'c10': 'a designer walking from her studio to a client’s apartment across a small square',
        'd1': 'balanced brass scales on a wooden table',
        'd2': 'a designer squashing a complicated model building into one plain cube',
        'd3': 'a doorway between a dark corridor and a bright room',
        'd4': 'a lecturer pointing to an open book on a lectern',
        'd5': 'a conductor leading an orchestra',
        's1': 'a bright warm modern living room with soft textiles',
        's2': 'a quiet hallway between a busy street and a calm spa',
        's3': 'a young designer admiring a modernist concrete staircase',
        's4': 'a discreet ventilation grille in an elegant panelled wall',
        's5': 'a builder shrugging at a small crack in a wall',
        'x1': 'a man shrugging his shoulders',
        'x2': 'a row of armchairs in a showroom, one in a different colour',
        'x3': 'a rusty iron garden gate',
        'x4': 'light falling across a stone doorstep at the threshold of a house',
        'talk2': 'two designers talking over fabric samples at a big table',
        'results': 'an armchair and a floor lamp in an empty sunlit room',
    },
    pop={'hero': (None, 'square'), 'c4': (None, 'free'), 'results': (None, 'free')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


CTX = [
    q('The designer wanted an ____ layout, where the client could move walls and furniture on a digital screen.',
      ['interactive', 'impartial', 'vestigial', 'perforated'], 1),
    q('The old factory conversion kept a few ____ traces of its industrial past, including the original steel beams.',
      ['vestigial', 'all-encompassing', 'reductive', 'artisanal'], 2),
    q('The lobby design was too loud and ____; it distracted from the artwork.',
      ['obtrusive', 'unobtrusive', 'rigorous', 'overarching'], 3),
    q('The new brass staircase was extremely ____ and became the main feature of the hotel entrance.',
      ['conspicuous', 'liminal', 'impartial', 'corroded'], 4),
    q('The architect wanted an ____ design concept that connected all rooms through colour, material and light.',
      ['overarching', 'artisanal', 'perforated', 'liminal'], 5),
    q('The client gave us some ____ on the budget, so we can upgrade the lighting if necessary.',
      ['wiggle room', 'rigour', 'conscription', 'threshold'], 6),
    q('The restoration team tried to ____ the original tiles rather than replace them.',
      ['conserve', 'cite', 'govern', 'corrode'], 7),
    q('The metal handrail had become ____ after years of exposure to sea air.',
      ['corroded', 'galvanized', 'suspended', 'perforated'], 8),
    q('The designer used a ____ of vintage furniture, modern lighting and handmade textiles.',
      ['medley', 'cartel', 'threshold', 'continuum'], 9),
    q('The apartment is only ____ from the client’s studio, so site visits are easy.',
      ['a stone’s throw', 'a continuum', 'an ethnic group', 'a threshold'], 10),
]
DEFN = [
    q('Which word means <em>fair, neutral, and not favouring one side</em>?', ['impartial', 'reductive', 'rigorous', 'liminal'], 11),
    q('Which word describes <em>treating a complex issue in an over-simple way</em>?', ['reductive', 'all-encompassing', 'unbiased', 'artisanal'], 12),
    q('Which word means <em>connected with a transitional stage or space</em>?', ['liminal', 'promenade', 'conduit', 'threshold'], 13),
    q('Which word means <em>to quote something as evidence</em>?', ['cite', 'govern', 'venerate', 'conserve'], 14),
    q('Which word means <em>to control how another word behaves grammatically</em>?', ['govern', 'cite', 'promenade', 'corrode'], 15),
]
SIT = [
    q('A client says, “Modern homes are always cold and ugly.” You explain that this is a ____ view.',
      ['reductive', 'artisanal', 'suspended', 'overarching'], 16),
    q('A hallway between a noisy street and a peaceful spa is a ____ space.', ['liminal', 'conspicuous', 'galvanized', 'perforated'], 17),
    q('A designer deeply respects the work of Carlo Scarpa. We can say she ____ him.', ['venerates', 'cites', 'shrugs off', 'governs'], 18),
    q('A hidden ventilation grille that does not attract attention is ____.', ['unobtrusive', 'obtrusive', 'eye-catching', 'conspicuous'], 19),
    q('If a contractor dismisses a small defect as unimportant, he tries to ____ it.', ['shrug off', 'conserve', 'promenade', 'cite'], 20),
]
ODD = [
    q('Which word does <strong>not</strong> belong with the others?', ['shrug off', 'revere', 'venerate', 'admire'], 21),
    q('Which word does <strong>not</strong> belong with the others?', ['unobtrusive', 'conspicuous', 'eye-catching', 'noticeable'], 22),
    q('Which word does <strong>not</strong> belong with the others?', ['corroded', 'galvanized', 'zinc-coated', 'protected steel'], 23),
    q('Which word does <strong>not</strong> belong with the others?', ['threshold', 'pastiche', 'imitation', 'homage'], 24),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Which room in your home do you spend most time in, and why?',
        'Do you prefer old buildings or new ones?',
        'What makes a hotel lobby feel welcoming?',
        'Have you ever renovated a room? What did you keep?',
        'Which designer or architect do you admire?',
        'What do you notice first when you walk into a room?',
    ], 'talk', 3),
    ('stage',),
    ('mc', 'e1', 'mcT', CTX, ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'], None),
    ('stage',),
    ('mc', 'e2', 'mcT', DEFN, ['d1', 'd2', 'd3', 'd4', 'd5'], None),
    ('stage',),
    ('mc', 'e3', 'mcT', SIT, ['s1', 's2', 's3', 's4', 's5'], None),
    ('stage',),
    ('mc', 'e4', 'mcT', ODD, ['x1', 'x2', 'x3', 'x4'], None),
    ('rules', 'eR', 'recT', [
        ('pSeen', [(None, 'conspicuous · eye-catching · noticeable'), (None, 'obtrusive (too much)'),
                   (None, 'unobtrusive (quietly not there)')], None),
        ('pOld', [(None, 'vestigial traces · conserve the tiles'), (None, 'corroded ≠ galvanized'),
                  (None, 'venerate · revere · admire ≠ shrug off'), (None, 'pastiche · imitation · homage')], None),
        ('pIdeas', [(None, 'an overarching concept · a medley'), (None, 'a reductive view ≠ an impartial one'),
                    (None, 'a liminal space · cite a source'), (None, 'wiggle room · a stone’s throw')], None),
    ], None),
    ('gap', 'e5', 'gapT', 'gHint', [
        ('The new sign was so ______ that every visitor noticed it at once.', ['conspicuous|eye-catching'], 'gw1'),
        ('We kept a few ______ traces of the old mill: two beams and a chimney.', ['vestigial'], 'gw2'),
        ('Is there any ______ room in the budget for better lighting?', ['wiggle'], 'gw3'),
    ]),
    ('talk', 'eT', 'tk2T', [
        'Describe a building you know with a <strong>conspicuous</strong> feature.',
        'Which design idea do you think is <strong>reductive</strong>?',
        'Where in your city is there a <strong>liminal</strong> space?',
        'What would you <strong>conserve</strong> in an old house, and what would you replace?',
        'Which designer do you <strong>venerate</strong>, and why?',
        'When is it good for design to be <strong>unobtrusive</strong>?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['vestigial', 'unobtrusive', 'overarching', 'wiggle room', 'conserve', 'conspicuous', 'liminal']

W = {
    'en': [
        'INTERACTIVE: a system the client can use and change themselves, like a movable digital layout.',
        'VESTIGIAL: a small trace left from an earlier stage, like the old beams.',
        'OBTRUSIVE: too noticeable, in a way that annoys or distracts. UNOBTRUSIVE is the opposite.',
        'CONSPICUOUS: standing out, easy to notice — here in a good, showcase sense.',
        'OVERARCHING: one idea broad enough to cover and connect everything beneath it.',
        'WIGGLE ROOM (informal): a little flexibility inside a fixed limit, such as a budget.',
        'CONSERVE: protect something and keep it as it is — the aim of restoration.',
        'CORRODED: metal slowly damaged by a chemical reaction, such as salt air. GALVANIZED metal is protected against it.',
        'A MEDLEY: a pleasing mixture of different things.',
        'A STONE’S THROW: a very short distance away.',
        'IMPARTIAL: fair, without taking sides.',
        'REDUCTIVE: simplifying something complex until important detail is lost.',
        'LIMINAL: in between — neither fully one state nor the other.',
        'CITE: refer to or quote a source in support of an argument.',
        'GOVERN, in grammar: decide the form of another word (a verb governs its object’s case).',
        'One exaggerated claim about a whole style oversimplifies it: a REDUCTIVE view.',
        'A space between two very different atmospheres is a LIMINAL space.',
        'VENERATE: regard someone with deep respect and admiration.',
        'UNOBTRUSIVE: subtle, not drawing attention. The other three all attract it.',
        'SHRUG OFF: treat something as unimportant.',
        'Revere, venerate and admire are respect. SHRUG OFF means dismiss.',
        'Conspicuous, eye-catching and noticeable mean easy to see. UNOBTRUSIVE means the opposite.',
        'Galvanized, zinc-coated and protected steel are treated against rust. CORRODED is the damage they prevent.',
        'Pastiche, imitation and homage all copy or refer to another style. A THRESHOLD is a doorway, or a limit.',
    ],
    'de': [
        'INTERACTIVE: ein System, das der Kunde selbst bedienen und ändern kann, wie ein verschiebbarer digitaler Grundriss.',
        'VESTIGIAL: eine kleine Spur aus einer früheren Phase, wie die alten Träger.',
        'OBTRUSIVE: zu auffällig, auf störende Weise. UNOBTRUSIVE ist das Gegenteil.',
        'CONSPICUOUS: auffällig, leicht zu bemerken — hier positiv, als Blickfang.',
        'OVERARCHING: eine übergreifende Idee, die alles darunter verbindet.',
        'WIGGLE ROOM (umgangssprachlich): ein wenig Spielraum innerhalb einer festen Grenze, etwa eines Budgets.',
        'CONSERVE: etwas schützen und erhalten, wie es ist — das Ziel einer Restaurierung.',
        'CORRODED: Metall, das durch eine chemische Reaktion wie Salzluft langsam beschädigt wurde. GALVANIZED Metall ist davor geschützt.',
        'A MEDLEY: eine gelungene Mischung verschiedener Dinge.',
        'A STONE’S THROW: nur einen Katzensprung entfernt.',
        'IMPARTIAL: unparteiisch, ohne Partei zu ergreifen.',
        'REDUCTIVE: etwas Komplexes so vereinfachen, dass Wichtiges verloren geht.',
        'LIMINAL: dazwischen — weder ganz das eine noch das andere.',
        'CITE: eine Quelle zitieren, um ein Argument zu stützen.',
        'GOVERN, in der Grammatik: die Form eines anderen Wortes bestimmen (ein Verb regiert den Kasus seines Objekts).',
        'Eine übertriebene Behauptung über einen ganzen Stil vereinfacht ihn zu sehr: eine REDUCTIVE Sicht.',
        'Ein Raum zwischen zwei sehr verschiedenen Atmosphären ist ein LIMINAL Raum.',
        'VENERATE: jemanden zutiefst verehren.',
        'UNOBTRUSIVE: dezent, unauffällig. Die anderen drei ziehen den Blick auf sich.',
        'SHRUG OFF: etwas als unwichtig abtun.',
        'Revere, venerate und admire drücken Respekt aus. SHRUG OFF heißt abtun.',
        'Conspicuous, eye-catching und noticeable heißen leicht zu sehen. UNOBTRUSIVE ist das Gegenteil.',
        'Galvanized, zinc-coated und protected steel sind gegen Rost behandelt. CORRODED ist der Schaden, den das verhindert.',
        'Pastiche, imitation und homage kopieren einen anderen Stil oder spielen darauf an. A THRESHOLD ist eine Türschwelle oder eine Grenze.',
    ],
    'es': [
        'INTERACTIVE: un sistema que el cliente puede usar y cambiar por sí mismo, como una distribución digital que se mueve.',
        'VESTIGIAL: una pequeña huella de una etapa anterior, como las viejas vigas.',
        'OBTRUSIVE: demasiado llamativo, de una forma que molesta o distrae. UNOBTRUSIVE es lo contrario.',
        'CONSPICUOUS: que destaca y se ve fácilmente — aquí en sentido positivo, como pieza central.',
        'OVERARCHING: una idea general que abarca y conecta todo lo demás.',
        'WIGGLE ROOM (informal): un poco de margen dentro de un límite fijo, como un presupuesto.',
        'CONSERVE: proteger algo y mantenerlo como está — el objetivo de una restauración.',
        'CORRODED: metal dañado poco a poco por una reacción química, como el aire salino. El metal GALVANIZED está protegido.',
        'A MEDLEY: una mezcla agradable de cosas distintas.',
        'A STONE’S THROW: a un paso, muy cerca.',
        'IMPARTIAL: justo, sin tomar partido.',
        'REDUCTIVE: simplificar algo complejo hasta perder detalles importantes.',
        'LIMINAL: intermedio — ni del todo una cosa ni la otra.',
        'CITE: citar una fuente para apoyar un argumento.',
        'GOVERN, en gramática: determinar la forma de otra palabra (un verbo rige el caso de su objeto).',
        'Una afirmación exagerada sobre todo un estilo lo simplifica demasiado: una visión REDUCTIVE.',
        'Un espacio entre dos ambientes muy distintos es un espacio LIMINAL.',
        'VENERATE: admirar y respetar profundamente a alguien.',
        'UNOBTRUSIVE: discreto, que no llama la atención. Los otros tres sí la llaman.',
        'SHRUG OFF: quitarle importancia a algo.',
        'Revere, venerate y admire expresan respeto. SHRUG OFF significa quitar importancia.',
        'Conspicuous, eye-catching y noticeable significan fácil de ver. UNOBTRUSIVE es lo contrario.',
        'Galvanized, zinc-coated y protected steel están tratados contra el óxido. CORRODED es el daño que eso evita.',
        'Pastiche, imitation y homage copian otro estilo o lo evocan. A THRESHOLD es un umbral o un límite.',
    ],
}

T = {
    'en': dict(
        coverTitle='Interior Design <br><em>Vocabulary</em>',
        coverSub='Precision language for architecture, heritage and client briefs: 24 words in context, by definition, in situations and as the odd one out.',
        chipLevel='C1', chipFocus='design · heritage · briefs', chipCount='31 slides',
        eW='Warm-up', eT='Let’s talk', eR='Review', e1='In context', e2='Definitions', e3='Situations',
        e4='Odd one out', e5='Your turn', tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best word',
        recT='The words, by family', pSeen='Seen, or not seen', pOld='Old and new', pIdeas='Ideas and briefs',
        gapT='Write the missing word', gHint='One word in each gap.',
        gw1='Easy to notice at once: CONSPICUOUS (or EYE-CATCHING).', gw2='A small trace of the past: VESTIGIAL.',
        gw3='A little flexibility: WIGGLE room.',
        actTitle='The client brief', actUse='Use at least four:',
        actSpeakBrief='In pairs: one of you is a designer, the other a client with an old building to convert.',
        actSpeak1='Client: describe the building and what you want to KEEP. Designer: suggest an OVERARCHING concept.',
        actSpeak2='Designer: say what you would CONSERVE and what is too CORRODED to save.',
        actSpeak3='Agree one feature that will be CONSPICUOUS and one that must be UNOBTRUSIVE.',
        actWriteKind='Writing',
        actWriteBrief='Write a design brief (150–200 words) for converting an old building: the overarching concept, what you will conserve, the feature that will be conspicuous, and where there is wiggle room in the budget.',
        actPlaceholder='The overarching concept for the old mill is …',
    ),
    'de': dict(
        coverTitle='Interior Design <br><em>Vocabulary</em>',
        coverSub='Präzise Sprache für Architektur, Denkmalpflege und Kundenbriefings: 24 Wörter im Kontext, als Definition, in Situationen und als das Wort, das nicht passt.',
        chipLevel='C1', chipFocus='Design · Erbe · Briefings', chipCount='31 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Wiederholung', e1='Im Kontext', e2='Definitionen', e3='Situationen',
        e4='Was passt nicht?', e5='Du bist dran', tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle das beste Wort',
        recT='Die Wörter nach Familien', pSeen='Auffällig oder unauffällig', pOld='Alt und neu', pIdeas='Ideen und Briefings',
        gapT='Ergänze das fehlende Wort', gHint='Ein Wort pro Lücke.',
        gw1='Sofort auffällig: CONSPICUOUS (oder EYE-CATCHING).', gw2='Eine kleine Spur der Vergangenheit: VESTIGIAL.',
        gw3='Ein wenig Spielraum: WIGGLE room.',
        actTitle='Das Kundenbriefing', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Eine Person ist Designerin, die andere eine Kundin mit einem alten Gebäude, das umgebaut werden soll.',
        actSpeak1='Kundin: Beschreib das Gebäude und was du erhalten willst. Designerin: Schlag ein OVERARCHING Konzept vor.',
        actSpeak2='Designerin: Sag, was du erhalten würdest (CONSERVE) und was zu CORRODED ist, um es zu retten.',
        actSpeak3='Einigt euch auf ein Element, das CONSPICUOUS sein soll, und eines, das UNOBTRUSIVE sein muss.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib ein Designbriefing (150–200 Wörter) für den Umbau eines alten Gebäudes: das übergreifende Konzept, was erhalten wird, das auffällige Element und wo das Budget Spielraum hat.',
        actPlaceholder='The overarching concept for the old mill is …',
    ),
    'es': dict(
        coverTitle='Interior Design <br><em>Vocabulary</em>',
        coverSub='Lenguaje preciso para arquitectura, patrimonio y encargos de clientes: 24 palabras en contexto, por definición, en situaciones y como la que sobra.',
        chipLevel='C1', chipFocus='diseño · patrimonio · encargos', chipCount='31 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Repaso', e1='En contexto', e2='Definiciones', e3='Situaciones',
        e4='¿Cuál sobra?', e5='Tu turno', tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la mejor palabra',
        recT='Las palabras, por familias', pSeen='Se ve, o no se ve', pOld='Lo viejo y lo nuevo', pIdeas='Ideas y encargos',
        gapT='Escribe la palabra que falta', gHint='Una palabra en cada hueco.',
        gw1='Se nota enseguida: CONSPICUOUS (o EYE-CATCHING).', gw2='Una pequeña huella del pasado: VESTIGIAL.',
        gw3='Un poco de margen: WIGGLE room.',
        actTitle='El encargo del cliente', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: uno es diseñador y el otro un cliente con un edificio antiguo que reformar.',
        actSpeak1='Cliente: describe el edificio y qué quieres conservar. Diseñador: propone un concepto OVERARCHING.',
        actSpeak2='Diseñador: di qué conservarías (CONSERVE) y qué está demasiado CORRODED para salvarlo.',
        actSpeak3='Acuerden un elemento que será CONSPICUOUS y otro que tiene que ser UNOBTRUSIVE.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un encargo de diseño (150–200 palabras) para reformar un edificio antiguo: el concepto general, lo que se conservará, el elemento que destacará y dónde hay margen en el presupuesto.',
        actPlaceholder='The overarching concept for the old mill is …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
