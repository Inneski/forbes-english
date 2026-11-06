# -*- coding: utf-8 -*-
"""Swiss Precision Part 2: Sounds, Stress and Sounding Natural (A2).
House style 2, 27 slides.

Rebuilt 2026-11-06 from `forbes-english-swiss-mistakes-a2-part2.html`: five
activities — a sound-group sort (13 words), word stress (8), a hotel-review
cloze (10 gaps), "make it natural" (8), a café vocabulary match (8 pairs).
Everything is kept; the sort's per-word notes are a recap card after it.

Fixed:
  * "Make it natural" Q2 listed the same correct sentence TWICE, and a
    third option ("I like eating …") was also correct — the old page even
    said so. One correct option now.
  * Stress: three items offered two spellings of the same stress
    ("em-PLOY-ees" and "em-PLOY-eez"; "en-JOY-able" and "en-JOY-a-ble";
    "trans-FER-able" and "trans-FER-a-ble"). EMPLOYEES also has two
    accepted stresses (em-PLOY-ees, em-ploy-EES), and TRANSFERABLE is
    stressed on the first syllable in American English. Those two words are
    replaced by EMPLOYER and COMPETITIVE, which have one stress each.
  * The hotel word bank listed the answers in gap order: an answer key.
    Alphabetical now, in two banks of five.
  * The sort put KNOCKED under "silent letter", though its -ED is also a
    final /t/: it belonged in two bins. Now KNIFE.
  * "Long before now, this region had many castles" is good English. Now
    "Before a long time" (vor langer Zeit, word for word).
  * The explanation called ENJOY a noun, and said "the moment we arrived"
    was wrong in formal writing. Both corrected.

Run from the repo root:  py lesson-template/build/build_swiss_mistakes_a2_p2.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H
import deck as D

SPEC = dict(
    out='forbes-english-swiss-mistakes-a2-part2.html',
    title='Swiss Precision Part 2: Sounds, Stress and Sounding Natural (A2)',
    folder='SwissMistakes',
    hero='p2-hero',
    scheme='rose',
    art={
        'p2-hero': ('music', 'a cathedral tower with musical notes rising like bells'),
        'p2-talk': ('talk', 'two speech bubbles above a hotel reception bell'),
        'p2-a': ('city', 'an old town street with a cathedral at the end'),
        'p2-act': ('pair', 'two chairs at a café table with two cups and a pastry'),
    },
    act='p2-act',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


STRESS = [
    q('Which shows the correct stress? <strong>employer</strong>', ['em-PLOY-er', 'EM-ploy-er', 'em-ploy-ER', 'EMP-loy-er'], 1),
    q('Which shows the correct stress? <strong>subsidiary</strong>', ['sub-SID-i-ary', 'SUB-si-di-ary', 'sub-sid-I-ary', 'sub-sid-i-ARY'], 2),
    q('Which shows the correct stress? <strong>expertise</strong>', ['ex-per-TISE', 'EX-per-tise', 'ex-PER-tise', 'ex-PERT-ise'], 3),
    q('Which shows the correct stress? <strong>competitive</strong>', ['com-PET-i-tive', 'COM-pe-ti-tive', 'com-pe-TI-tive', 'com-pet-i-TIVE'], 4),
    q('Which shows the correct stress? <strong>revenue</strong>', ['REV-en-ue', 'rev-EN-ue', 'rev-e-NUE', 'REV-E-nue'], 5),
    q('Which shows the correct stress? <strong>enjoyable</strong>', ['en-JOY-able', 'EN-joy-able', 'en-joy-ABLE', 'EN-JOY-able'], 6),
    q('Which shows the correct stress? <strong>personalised</strong>', ['PER-son-al-ised', 'per-SON-al-ised', 'per-son-AL-ised', 'per-son-al-ISED'], 7),
    q('Which shows the correct stress? <strong>cathedral</strong>', ['ca-THE-dral', 'CA-the-dral', 'cath-e-DRAL', 'ca-the-DRAL'], 8),
]
NAT = [
    q('Make it natural: <em>“Where local people go are good restaurants.”</em>',
      ['Good restaurants are where local people go.', 'Restaurants that local people go are good ones.',
       'Where is going the local people a good restaurant.', 'The local peoples go to good restaurants there.'], 9),
    q('Make it natural: <em>“I like eat in cafés because the atmosphere is enjoyable.”</em>',
      ['I like eating in cafés because the atmosphere is enjoyable.', 'I like eat in cafés because the atmosphere is enjoying.',
       'I like eat in cafés because the atmosphere is enjoyable.', 'I like eating in cafés because the atmosphere is enjoying.'], 10),
    q('Make it natural: <em>“The eat in the hotel was tasty.”</em>',
      ['The food in the hotel was tasty.', 'The eaten in the hotel was tasty.', 'The eating in the hotel was tasty.',
       'The meal in the hotel was tasteful.'], 11),
    q('Make it natural: <em>“I prefer restaurants where local peoples go.”</em>',
      ['I prefer restaurants where local people go.', 'I prefer restaurants where local peoples are going.',
       'I prefer the restaurants where local peoples go.', 'I prefer restaurants which local peoples go to.'], 12),
    q('Make it natural: <em>“A long time before, this region had many castles.”</em>',
      ['A long time ago, this region had many castles.', 'A long time since, this region had many castles.',
       'Long ago time, this region had many castles.', 'Before a long time, this region had many castles.'], 13),
    q('Make it natural: <em>“That’s mean the revenue increased.”</em>',
      ['That means the revenue increased.', 'That’s meant the revenue increased.', 'That is meaning the revenue increased.',
       'That mean the revenue it increased.'], 14),
    q('Make it natural: <em>“There is much sun and nearby access to the cathedral.”</em>',
      ['There is a lot of sun, and the cathedral is nearby.', 'There is many sun, and nearby is the cathedral.',
       'There is much sun and the cathedral is near to.', 'There is a lot of sun, and nearby there cathedral.'], 15),
    q('Make it natural: <em>“It has variety of features.”</em>',
      ['It has a variety of features.', 'It has varieties of feature.', 'It has variety features.', 'It has a varieties of features.'], 16),
]
PAIRS = [('gather', 'to come together in one place'), ('brew', 'to make a hot drink like coffee or tea'),
         ('whipped cream', 'cream beaten until it is thick and light'), ('pastry', 'a baked food made from dough, often sweet'),
         ('culture', 'the customs and traditions of a group of people'), ('title', 'an official name or award given to someone'),
         ('even', 'used to stress that something is surprising'), ('whole', 'complete; all of something')]
MG = {
    'de': {'gather': 'sich an einem Ort versammeln', 'brew': 'ein heißes Getränk wie Kaffee oder Tee zubereiten',
           'whipped cream': 'Schlagsahne', 'pastry': 'Gebäck aus Teig, oft süß', 'culture': 'die Bräuche und Traditionen einer Gruppe',
           'title': 'ein offizieller Name oder Titel', 'even': 'betont, dass etwas überraschend ist („sogar“)', 'whole': 'ganz; alles von etwas'},
    'es': {'gather': 'reunirse en un lugar', 'brew': 'preparar una bebida caliente como café o té', 'whipped cream': 'nata montada',
           'pastry': 'un dulce horneado hecho de masa', 'culture': 'las costumbres y tradiciones de un grupo',
           'title': 'un nombre oficial o un título', 'even': 'subraya que algo es sorprendente («incluso»)', 'whole': 'completo; todo'},
}
SORT_ITEMS = [('salmon', 0), ('castle', 0), ('whole', 0), ('knife', 0), ('half', 0),
              ('looked', 1), ('based', 1), ('whipped', 1), ('pleased', 2), ('arrived', 2),
              ('countries', 3), ('produces', 3), ('services', 3)]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Which English word is hardest for you to say?',
        'What is the best hotel you have stayed in?',
        'Do you read reviews before you book?',
        'Where do local people eat in your town?',
        'Which café would you recommend to a visitor?',
        'What is your favourite pastry or cake?',
    ], 'p2-talk', 3),
    ('raw', None),  # the sort, filled in below
    ('rules', 'eR', 'recT', [
        ('pSilent', [(None, 'salmon · half — no L'), (None, 'castle — no T · knife — no K'), (None, 'whole — no W')], None),
        ('pEd', [(None, 'after /k/ /s/ /p/: -ED = /t/'), (None, 'looked · based · whipped'), (None, 'after /z/ /v/: -ED = /d/'),
                 (None, 'pleased · arrived')], None),
        ('pZ', [(None, 'countries — /z/'), (None, 'produces · services — /ɪz/'), (None, 'never an extra vowel at the end')], None),
    ], None),
    ('mc', 'e2', 'mcT', STRESS, 'p2-a', None),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('The hotel was excellent from the moment of our ______.', ['arrival'], 'g1'),
        ('It had easy ______ to the city centre, and there were many restaurants ______.', ['access', 'nearby'], 'g2'),
        ('It offered a good ______ of services, including ______ recommendations for guests.', ['variety', 'personalised|personalized'], 'g3'),
    ], ['access', 'arrival', 'nearby', 'personalised', 'variety']),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('The rooms were ______, the breakfast was ______, and the whole stay was very ______.', ['clean', 'tasty', 'enjoyable'], 'g4'),
        ('One of the best ______ was the view of the old ______.', ['features', 'cathedral'], 'g5'),
    ], ['cathedral', 'clean', 'enjoyable', 'features', 'tasty']),
    ('mc', 'e4', 'mcT', NAT, None, None),
    ('raw', None),  # the match, filled in below
    ('talk', 'eT', 'tk2T', [
        'Describe a hotel stay that was <strong>enjoyable</strong>.',
        'Which café in your town has the best <strong>pastries</strong>?',
        'Where do people <strong>gather</strong> in your town on a Saturday?',
        'What is one of the best <strong>features</strong> of your city?',
        'Is there a <strong>cathedral</strong> or a castle near you?',
        'How do you like your coffee <strong>brewed</strong>?',
    ], None, 3),
]
SPEC['chips'] = ['nearby', 'a variety of', 'enjoyable', 'a lot of', 'one of the best', 'arrival']

W = {
    'en': [
        'em-PLOY-er: the stress is on the verb inside it, emPLOY.',
        'sub-SID-i-ary: stress on the second syllable.',
        'ex-per-TISE: stress on the last syllable — unlike EX-pert.',
        'com-PET-i-tive: stress on the second syllable, as in comPETE.',
        'REV-en-ue: stress on the first syllable; three syllables.',
        'en-JOY-able: the verb ENJOY keeps its stress; -ABLE never takes it.',
        'PER-son-al-ised: stress stays on the root, PERson.',
        'ca-THE-dral: stress on the second syllable.',
        'The subject comes first: “Good restaurants are where local people go.” PEOPLE is already plural.',
        'After LIKE: -ING (or TO + verb). The atmosphere IS ENJOYABLE: an adjective, not ENJOYING.',
        'EAT is only a verb; the noun is FOOD. TASTEFUL means stylish; good flavour is TASTY.',
        'PEOPLE is already plural. PEOPLES means nations.',
        'AGO looks back from now: A LONG TIME AGO. “Before a long time” is vor langer Zeit, word for word.',
        'THAT MEANS: third person + -S. “That’s mean” = that is unkind!',
        'Positive sentences: A LOT OF, not MUCH. NEARBY can end the sentence; NEAR TO needs an object.',
        'Always A VARIETY OF + a plural noun.',
    ],
    'de': [
        'em-PLOY-er: Betont wird das Verb darin, emPLOY.',
        'sub-SID-i-ary: Betonung auf der zweiten Silbe.',
        'ex-per-TISE: Betonung auf der letzten Silbe — anders als EX-pert.',
        'com-PET-i-tive: Betonung auf der zweiten Silbe, wie in comPETE.',
        'REV-en-ue: Betonung auf der ersten Silbe; drei Silben.',
        'en-JOY-able: Das Verb ENJOY behält seine Betonung; -ABLE wird nie betont.',
        'PER-son-al-ised: Die Betonung bleibt auf dem Stamm, PERson.',
        'ca-THE-dral: Betonung auf der zweiten Silbe.',
        'Das Subjekt kommt zuerst: „Good restaurants are where local people go.“ PEOPLE ist schon Plural.',
        'Nach LIKE: -ING (oder TO + Verb). Die Atmosphäre IS ENJOYABLE: ein Adjektiv, nicht ENJOYING.',
        'EAT ist nur ein Verb; das Nomen ist FOOD („das Essen“). TASTEFUL heißt geschmackvoll; lecker ist TASTY.',
        'PEOPLE ist schon Plural („Leute“). PEOPLES heißt Völker.',
        'AGO schaut von jetzt zurück: A LONG TIME AGO. „Before a long time“ ist vor langer Zeit, Wort für Wort.',
        'THAT MEANS: dritte Person + -S („das bedeutet“). „That’s mean“ = das ist gemein!',
        'Positive Sätze: A LOT OF, nicht MUCH. NEARBY kann am Satzende stehen; NEAR TO braucht ein Objekt.',
        'Immer A VARIETY OF + Plural („eine Reihe von“).',
    ],
    'es': [
        'em-PLOY-er: se acentúa el verbo que lleva dentro, emPLOY.',
        'sub-SID-i-ary: acento en la segunda sílaba.',
        'ex-per-TISE: acento en la última sílaba, a diferencia de EX-pert.',
        'com-PET-i-tive: acento en la segunda sílaba, como en comPETE.',
        'REV-en-ue: acento en la primera sílaba; tres sílabas.',
        'en-JOY-able: el verbo ENJOY conserva su acento; -ABLE nunca lo lleva.',
        'PER-son-al-ised: el acento se queda en la raíz, PERson.',
        'ca-THE-dral: acento en la segunda sílaba.',
        'El sujeto va primero: «Good restaurants are where local people go». PEOPLE ya es plural.',
        'Después de LIKE: -ING (o TO + verbo). El ambiente IS ENJOYABLE: un adjetivo, no ENJOYING.',
        'EAT solo es verbo; el sustantivo es FOOD. TASTEFUL significa con estilo; rico es TASTY.',
        'PEOPLE ya es plural. PEOPLES significa pueblos, naciones.',
        'AGO mira hacia atrás desde ahora: A LONG TIME AGO. «Before a long time» es el alemán vor langer Zeit, palabra por palabra.',
        'THAT MEANS: tercera persona + -S. «That’s mean» = eso es cruel.',
        'En afirmativas: A LOT OF, no MUCH. NEARBY puede ir al final; NEAR TO necesita un objeto.',
        'Siempre A VARIETY OF + un sustantivo plural.',
    ],
}
G = {
    'en': ['The moment of our ARRIVAL: a noun after OUR. (“The moment we arrived” is also fine — a verb after WE.)',
           'Easy ACCESS to a place; restaurants NEARBY = close by. Not NEARLY, which means almost.',
           'A VARIETY OF + plural; PERSONALISED = made for you as a person.',
           'CLEAN rooms (not cleaned), TASTY food, an ENJOYABLE stay.',
           'One of the best FEATURES; the old CATHEDRAL, the main church of a city.'],
    'de': ['The moment of our ARRIVAL: ein Nomen nach OUR. („The moment we arrived“ geht auch — ein Verb nach WE.)',
           'Easy ACCESS = leichter Zugang; restaurants NEARBY = in der Nähe. Nicht NEARLY, das heißt fast.',
           'A VARIETY OF + Plural; PERSONALISED = persönlich auf dich zugeschnitten.',
           'CLEAN rooms (nicht cleaned), TASTY food, ein ENJOYABLE Aufenthalt.',
           'One of the best FEATURES (Besonderheiten); die alte CATHEDRAL (Kathedrale).'],
    'es': ['The moment of our ARRIVAL: un sustantivo después de OUR. («The moment we arrived» también vale: un verbo después de WE.)',
           'Easy ACCESS = fácil acceso; restaurants NEARBY = cerca. No NEARLY, que significa casi.',
           'A VARIETY OF + plural; PERSONALISED = hecho para ti.',
           'CLEAN rooms (no cleaned), TASTY food, una estancia ENJOYABLE.',
           'One of the best FEATURES (características); la vieja CATHEDRAL (catedral).'],
}

T = {
    'en': dict(
        bankLabel='Word bank:',
        coverTitle='Swiss Precision, <br><em>Part 2</em>',
        coverSub='Sounds, stress and sounding natural: silent letters and -ED endings, where the stress goes, a hotel review, and café vocabulary.',
        chipLevel='A2', chipFocus='sounds · stress · natural English', chipCount='27 slides',
        eW='Warm-up', eT='Let’s talk', eR='Review', e1='Sound groups', e2='Word stress', e3='A hotel review',
        e4='Make it natural', e5='Café words', tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best answer',
        sortT='Sort the sounds', sortHint='Click a word, then the sound group it belongs to. Say each word aloud first.',
        sortWhy='Silent letters are not said; -ED is /t/ after an unvoiced sound and /d/ after a voiced one; -S and -ES are /z/ or /ɪz/.',
        binA='Silent letter', binB='Final /t/', binC='Final /d/', binD='Final /z/',
        recT='How they sound', pSilent='Silent letters', pEd='-ED endings', pZ='-S and -ES endings',
        gapT='Complete the review', gHint='One word from the bank in each gap.',
        g1=G['en'][0], g2=G['en'][1], g3=G['en'][2], g4=G['en'][3], g5=G['en'][4],
        matchT='Café and food words', matchHint='Click a word, then its meaning.', matchWhy='Each café word with its meaning.',
        actTitle='Review it', actUse='Use at least four:',
        actSpeakBrief='In pairs. Recommend a hotel or a café to your partner.',
        actSpeak1='Describe a hotel stay: the ARRIVAL, the rooms, the breakfast, the best FEATURES.',
        actSpeak2='Recommend a café: what do they BREW, which PASTRY should your partner try?',
        actSpeak3='Say five words from this lesson with the right stress. Your partner checks.',
        actWriteKind='Writing',
        actWriteBrief='Write an online review of a hotel or café (80–100 words): the arrival, the location, the food, and one of the best features.',
        actPlaceholder='The hotel was excellent from the moment of our arrival …',
    ),
    'de': dict(
        bankLabel='Wortliste:',
        coverTitle='Swiss Precision, <br><em>Part 2</em>',
        coverSub='Laute, Betonung und natürliches Englisch: stumme Buchstaben und -ED-Endungen, wo die Betonung liegt, eine Hotelbewertung und Café-Vokabular.',
        chipLevel='A2', chipFocus='Laute · Betonung · natürliches Englisch', chipCount='27 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Wiederholung', e1='Lautgruppen', e2='Wortbetonung', e3='Eine Hotelbewertung',
        e4='Klingt es natürlich?', e5='Café-Wörter', tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die beste Antwort',
        sortT='Sortiere die Laute', sortHint='Klicke ein Wort an, dann seine Lautgruppe. Sprich jedes Wort zuerst laut.',
        sortWhy='Stumme Buchstaben spricht man nicht; -ED ist /t/ nach einem stimmlosen und /d/ nach einem stimmhaften Laut; -S und -ES sind /z/ oder /ɪz/.',
        binA='Stummer Buchstabe', binB='Am Ende /t/', binC='Am Ende /d/', binD='Am Ende /z/',
        recT='So klingen sie', pSilent='Stumme Buchstaben', pEd='-ED-Endungen', pZ='-S- und -ES-Endungen',
        gapT='Ergänze die Bewertung', gHint='Ein Wort aus der Liste pro Lücke.',
        g1=G['de'][0], g2=G['de'][1], g3=G['de'][2], g4=G['de'][3], g5=G['de'][4],
        matchT='Café- und Essenswörter', matchHint='Klicke ein Wort an, dann seine Bedeutung.', matchWhy='Jedes Café-Wort mit seiner Bedeutung.',
        actTitle='Bewerte es', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit. Empfiehl deinem Partner ein Hotel oder ein Café.',
        actSpeak1='Beschreib einen Hotelaufenthalt: die ARRIVAL, die Zimmer, das Frühstück, die besten FEATURES.',
        actSpeak2='Empfiehl ein Café: Was BREW sie dort, welches PASTRY sollte dein Partner probieren?',
        actSpeak3='Sag fünf Wörter aus dieser Lektion mit der richtigen Betonung. Dein Partner prüft.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib eine Online-Bewertung eines Hotels oder Cafés (80–100 Wörter): die Ankunft, die Lage, das Essen und eine der besten Besonderheiten.',
        actPlaceholder='The hotel was excellent from the moment of our arrival …',
    ),
    'es': dict(
        bankLabel='Banco de palabras:',
        coverTitle='Swiss Precision, <br><em>Part 2</em>',
        coverSub='Sonidos, acento y un inglés natural: letras mudas y terminaciones en -ED, dónde va el acento, una reseña de hotel y vocabulario de cafetería.',
        chipLevel='A2', chipFocus='sonidos · acento · inglés natural', chipCount='27 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Repaso', e1='Grupos de sonidos', e2='Acento de palabra', e3='Una reseña de hotel',
        e4='¿Suena natural?', e5='Palabras de cafetería', tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la mejor respuesta',
        sortT='Clasifica los sonidos', sortHint='Haz clic en una palabra y después en su grupo. Di cada palabra en voz alta primero.',
        sortWhy='Las letras mudas no se pronuncian; -ED es /t/ después de un sonido sordo y /d/ después de uno sonoro; -S y -ES son /z/ o /ɪz/.',
        binA='Letra muda', binB='Final /t/', binC='Final /d/', binD='Final /z/',
        recT='Cómo suenan', pSilent='Letras mudas', pEd='Terminaciones -ED', pZ='Terminaciones -S y -ES',
        gapT='Completa la reseña', gHint='Una palabra de la lista en cada hueco.',
        g1=G['es'][0], g2=G['es'][1], g3=G['es'][2], g4=G['es'][3], g5=G['es'][4],
        matchT='Palabras de cafetería y comida', matchHint='Haz clic en una palabra y después en su significado.', matchWhy='Cada palabra con su significado.',
        actTitle='Haz una reseña', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas. Recomienda un hotel o una cafetería a tu compañero.',
        actSpeak1='Describe una estancia en un hotel: la ARRIVAL, las habitaciones, el desayuno, las mejores FEATURES.',
        actSpeak2='Recomienda una cafetería: ¿qué BREW allí, qué PASTRY debería probar tu compañero?',
        actSpeak3='Di cinco palabras de esta lección con el acento correcto. Tu compañero lo comprueba.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe una reseña online de un hotel o una cafetería (80–100 palabras): la llegada, la ubicación, la comida y una de las mejores características.',
        actPlaceholder='The hotel was excellent from the moment of our arrival …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

E = T['en']
SORT = D.sort_slide([E['binA'], E['binB'], E['binC'], E['binD']], SORT_ITEMS, 'e1', E['e1'], 'sortT', E['sortT'],
                    'sortHint', E['sortHint'], 'sortWhy', bin_keys=['binA', 'binB', 'binC', 'binD'])
MATCH = ''.join(D.match(PAIRS[i:i + 4], 'e5', E['e5'], 'matchT', E['matchT'], 'matchHint', E['matchHint'],
                        'matchWhy', glosses=MG) for i in (0, 4))
fills = iter([SORT, MATCH])
SPEC['flow'] = [('raw', next(fills)) if st == ('raw', None) else st for st in SPEC['flow']]

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
