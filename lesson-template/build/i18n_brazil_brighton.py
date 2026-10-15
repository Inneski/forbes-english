# -*- coding: utf-8 -*-
"""Interface strings for Cold, Colder, the Coldest — From Brazil to Brighton
(A1, adult). English, German, Spanish and Portuguese.

Portuguese is here because the learner the deck was written for is
Brazilian: it is Brazilian Portuguese (VOCÊ, "ônibus", "caminhão"), not the
European Portuguese of the shared chrome in chrome_i18n.py.

What translates: the chrome, slide titles, the rule on every teach card, the
accent situation, every explanation, the task instructions. What does not
(HOUSE-STYLE §8): the reading panels, stems, options, gap sentences, the sort
and order pieces, the English examples under the cards, and the translation
rows — those are the target language on purpose. The translation game is
<UI language> ⇄ English (Portuguese when the UI is English), so tw1-tw6 and
trHint are written about each language's OWN sentences: the German tw2 says
German gives age with BE as English does, the Spanish one that TIENE is the
trap.

Grammar words in CAPS, cited words in double quotes, as in the other decks.

coverSub is also the meta description: tools/seo.py strips tags WITHOUT
adding a space, so each <br> has a space in front of it.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord']

T = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='Cold, Colder,<br><em>the Coldest</em>',
    coverSub='From Brazil to Brighton: AM / IS / ARE, comparatives and superlatives, DOES / DOESN’T and the Brighton accent — <br>with a Portuguese ⇄ English translation game.',
    chipLevel='A1', chipFocus='am / is / are · -er / -est · does', chipCount='27 slides',

    d1t='Hello from Brighton', d1n='Stage 1 · I am, he is, they are',
    d2t='Cold, Colder, the Coldest', d2n='Stage 2 · comparing places',
    d3t='Does He Drive a Taxi?', d3n='Stage 3 · jobs, does and doesn’t',

    e1='Am · is · are', e2='-er · -est', e3='Does · doesn’t',
    e4='The Brighton accent', e5='Translate', eR='The rule', eV='New words',

    p1t='Meet Ana', p2t='Brazil or Scotland?', p3t='Rafael’s new job',

    tAt='AM, IS or ARE?',
    tA1='With I, always AM.',
    tA2='One person or one thing: IS.',
    tA3='More than one person: ARE. TEACHERS = THEY, so ARE.',
    tA4='In English you ARE an age. Never "I have 32 years".',

    tBt='Comparing: two rules and two surprises',
    tB1='Short words: add -ER to compare two things, THE + -EST for number one. Use THAN: "colder THAN Brighton".',
    tB2='One vowel + one consonant at the end: write the consonant twice. HOT → HOTTER.',
    tB3='Long words: put MORE or THE MOST in front. Never "expensiver".',
    tB4='GOOD is irregular. Learn it by heart!',

    gapT='Write the missing word',
    gapHint1='Write AM, IS or ARE.',
    gapHint2='Use the word in brackets. Compare: -ER, or a new word.',
    g1w='I → AM: "I AM from Curitiba."',
    g2w='Rafael and Lucas = THEY → ARE.',
    g3w='Callum = HE → IS.',
    g4w='HOT: one vowel + one consonant, so the T doubles: HOTTER.',
    g5w='GOOD → BETTER → THE BEST. Never "gooder".',
    g6w='BIG: one vowel + one consonant, so the G doubles: BIGGER.',

    mcT='Choose the right word', mc4T='Which letter is missing?',
    q1w='TEACHERS is more than one person = THEY → ARE.',
    q2w='Age takes BE: "He IS sixteen months old." In English you never HAVE an age.',
    q3w='Two places, and THAN: COLDER THAN. Never "more cold".',
    q4w='Number one of all the cities: THE COLDEST. One syllable takes -EST, not MOST.',
    q5w='A question with he, she or it starts with DOES: "DOES your husband DRIVE …?"',
    q6w='HE + DOESN’T + DRIVE. After DOESN’T the verb has no -S.',
    c8='In Brighton, many people say WATER like this. Which letter do they not say?',
    q8w='The T disappears. This is the glottal stop: "wa’er", "Brigh’on".',

    sortT='-ER / -EST or MORE / THE MOST?',
    sortHint='Tap each word, then put it in the right box.',
    binA='-ER / -EST', binB='MORE / THE MOST',
    sortWhy='Short words take -ER / -EST: colder, bigger, hotter, smaller, older. Long words take MORE / THE MOST: more expensive, more beautiful, more difficult, more interesting, more famous.',

    jAt='Four drivers',
    jA1='Drives a lorry: a very big vehicle for things, not people. (American: TRUCK.)',
    jA2='Drives a van: smaller than a lorry. Vans bring parcels to your door.',
    jA3='Drives people in a taxi, and they pay.',
    jA4='Drives a rich person’s car for them. Say it "SHOW-fer".',

    tCt='DOES and DOESN’T',
    tC1='With he, she, it, the verb takes -S.',
    tC2='A question starts with DOES. The -S moves to DOES, so the verb has no -S.',
    tC3='DOESN’T = DOES NOT. After it, the verb has no -S.',
    tC4='With I, you, we and they: DO and DON’T.',

    orderT='Make the question',
    orderHint='Tap the words in the right order. One word is extra!',
    o1w='"DOES Rafael DRIVE a van?" DOES has the -S, so DRIVES is the extra word.',

    tEt='How they talk in Brighton',
    tE1='In the south of England, many people don’t say R at the end of a word.',
    tE2='But before a vowel, they sometimes add an R!',
    tE3='Many people stop the sound in the throat instead of saying T.',

    trT='Translate the sentence',
    trHint='Write it in English. Tap the switch to go the other way: English → Português.',
    tw1='"Eu sou do Brasil." = "I am from Brazil." SOU = AM. DO BRASIL = FROM Brazil.',
    tw2='"Meu filho tem dezesseis meses." = "My son is sixteen months old." In Portuguese you HAVE an age (TEM). In English you ARE an age (IS).',
    tw3='"A Escócia é mais fria que o Brasil." = "Scotland is colder than Brazil." MAIS FRIA = COLDER. QUE = THAN.',
    tw4='"… a cidade mais fria do Brasil." = "… the coldest city IN Brazil." After THE + -EST, a place takes IN, not OF.',
    tw5='"Seu marido dirige um táxi?" = "Does your husband drive a taxi?" The question starts with DOES, and DRIVE has no -S.',
    tw6='"Ele não dirige um caminhão." = "He doesn’t drive a lorry." NÃO = DOESN’T. CAMINHÃO = LORRY (American: TRUCK).',

    # ── activation ───────────────────────────────────────────────────
    actTitle='Where do you want to live?',
    actUse='Use at least three:',
    actSpeakBrief='Talk about your city, your family and the country of your dreams.',
    actSpeak1='Compare two cities you know: "Brighton is colder than … but …"',
    actSpeak2='Ask about a person in your partner’s family: "Does your brother drive? What does he do?"',
    actSpeak3='Your dream country: "I want to live in … because it is the most …"',
    actWriteKind='Writing · 50–80 words',
    actWriteBrief='Write a message to your English teacher. Say where you are from, who is in your family, and where you want to live — and why.',
    actPlaceholder='Hi! I am from …',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Cold, Colder,<br><em>the Coldest</em>',
    coverSub='Von Brasilien nach Brighton: AM / IS / ARE, Komparativ und Superlativ, DOES / DOESN’T und der Brighton-Akzent — <br>mit einem Übersetzungsspiel Portugiesisch ⇄ Englisch.',
    chipLevel='A1', chipFocus='am / is / are · -er / -est · does', chipCount='27 Folien',

    d1t='Hallo aus Brighton', d1n='Teil 1 · I am, he is, they are',
    d2t='Cold, Colder, the Coldest', d2n='Teil 2 · Orte vergleichen',
    d3t='Fährt er Taxi?', d3n='Teil 3 · Berufe, does und doesn’t',

    e1='Am · is · are', e2='-er · -est', e3='Does · doesn’t',
    e4='Der Brighton-Akzent', e5='Übersetzen', eR='Die Regel', eV='Neue Wörter',

    p1t='Das ist Ana', p2t='Brasilien oder Schottland?', p3t='Rafaels neuer Job',

    tAt='AM, IS oder ARE?',
    tA1='Mit I immer AM.',
    tA2='Eine Person oder eine Sache: IS.',
    tA3='Mehr als eine Person: ARE. TEACHERS = THEY, also ARE.',
    tA4='Auf Englisch BIST du ein Alter, wie im Deutschen: "I AM 32".',

    tBt='Vergleichen: zwei Regeln und zwei Überraschungen',
    tB1='Kurze Wörter: -ER, um zwei Dinge zu vergleichen, THE + -EST für Nummer eins. Mit THAN: "colder THAN Brighton".',
    tB2='Ein Vokal + ein Konsonant am Ende: den Konsonanten doppelt schreiben. HOT → HOTTER.',
    tB3='Lange Wörter: MORE oder THE MOST davor. Nie "expensiver".',
    tB4='GOOD ist unregelmäßig. Auswendig lernen!',

    gapT='Schreib das fehlende Wort',
    gapHint1='Schreib AM, IS oder ARE.',
    gapHint2='Nimm das Wort in Klammern. Vergleiche: -ER oder ein neues Wort.',
    g1w='I → AM: "I AM from Curitiba."',
    g2w='Rafael und Lucas = THEY → ARE.',
    g3w='Callum = HE → IS.',
    g4w='HOT: ein Vokal + ein Konsonant, also wird das T doppelt: HOTTER.',
    g5w='GOOD → BETTER → THE BEST. Nie "gooder".',
    g6w='BIG: ein Vokal + ein Konsonant, also wird das G doppelt: BIGGER.',

    mcT='Wähl das richtige Wort', mc4T='Welcher Buchstabe fehlt?',
    q1w='TEACHERS ist mehr als eine Person = THEY → ARE.',
    q2w='Das Alter nimmt BE: "He IS sixteen months old." Auf Englisch HAT man nie ein Alter.',
    q3w='Zwei Orte und THAN: COLDER THAN. Nie "more cold".',
    q4w='Nummer eins von allen Städten: THE COLDEST. Eine Silbe nimmt -EST, nicht MOST.',
    q5w='Eine Frage mit he, she oder it beginnt mit DOES: "DOES your husband DRIVE …?"',
    q6w='HE + DOESN’T + DRIVE. Nach DOESN’T hat das Verb kein -S.',
    c8='In Brighton sagen viele Leute WATER so. Welchen Buchstaben sagen sie nicht?',
    q8w='Das T verschwindet. Das ist der Knacklaut (glottal stop): "wa’er", "Brigh’on".',

    sortT='-ER / -EST oder MORE / THE MOST?',
    sortHint='Tipp ein Wort an und leg es in die richtige Box.',
    binA='-ER / -EST', binB='MORE / THE MOST',
    sortWhy='Kurze Wörter nehmen -ER / -EST: colder, bigger, hotter, smaller, older. Lange Wörter nehmen MORE / THE MOST: more expensive, more beautiful, more difficult, more interesting, more famous.',

    jAt='Vier Fahrer',
    jA1='Fährt einen Lastwagen: ein sehr großes Fahrzeug für Waren, nicht für Menschen. (Amerikanisch: TRUCK.)',
    jA2='Fährt einen Lieferwagen: kleiner als ein Lastwagen. Er bringt Pakete an die Tür.',
    jA3='Fährt Leute im Taxi, und sie bezahlen.',
    jA4='Fährt das Auto einer reichen Person. Sprich: "SHOW-fer".',

    tCt='DOES und DOESN’T',
    tC1='Mit he, she, it bekommt das Verb ein -S.',
    tC2='Eine Frage beginnt mit DOES. Das -S wandert zu DOES, also hat das Verb kein -S.',
    tC3='DOESN’T = DOES NOT. Danach hat das Verb kein -S.',
    tC4='Mit I, you, we und they: DO und DON’T.',

    orderT='Bau die Frage',
    orderHint='Tipp die Wörter in der richtigen Reihenfolge an. Ein Wort ist zu viel!',
    o1w='"DOES Rafael DRIVE a van?" DOES hat das -S, also ist DRIVES zu viel.',

    tEt='So spricht man in Brighton',
    tE1='Im Süden Englands sagen viele Leute kein R am Ende eines Wortes.',
    tE2='Aber vor einem Vokal fügen sie manchmal ein R ein!',
    tE3='Viele Leute stoppen den Laut im Hals, statt T zu sagen.',

    trT='Übersetze den Satz',
    trHint='Schreib ihn auf Englisch. Mit dem Schalter geht es andersherum: English → Deutsch.',
    tw1='"Ich komme aus Brasilien." = "I am from Brazil." (oder "I come from Brazil.") AUS = FROM.',
    tw2='"Mein Sohn ist sechzehn Monate alt." = "My son is sixteen months old." Wie im Deutschen: das Alter mit BE (IS). Im Portugiesischen HAT man es!',
    tw3='"Schottland ist kälter als Brasilien." = "Scotland is colder than Brazil." KÄLTER = COLDER. ALS = THAN.',
    tw4='"… die kälteste Stadt in Brasilien." = "… the coldest city IN Brazil." DIE KÄLTESTE = THE COLDEST. Nach THE + -EST steht vor einem Ort IN, nicht OF.',
    tw5='"Fährt dein Mann Taxi?" = "Does your husband drive a taxi?" Die Frage beginnt mit DOES, und DRIVE hat kein -S.',
    tw6='"Er fährt keinen Lastwagen." = "He doesn’t drive a lorry." KEINEN = DOESN’T … A. LASTWAGEN = LORRY (amerikanisch: TRUCK).',

    actTitle='Wo möchtest du leben?',
    actUse='Benutze mindestens drei:',
    actSpeakBrief='Sprich über deine Stadt, deine Familie und das Land deiner Träume.',
    actSpeak1='Vergleiche zwei Städte, die du kennst: "Brighton is colder than … but …"',
    actSpeak2='Frag nach einer Person in der Familie deines Partners: "Does your brother drive? What does he do?"',
    actSpeak3='Dein Traumland: "I want to live in … because it is the most …"',
    actWriteKind='Schreiben · 50–80 Wörter',
    actWriteBrief='Schreib eine Nachricht an deinen Englischlehrer. Sag, woher du kommst, wer in deiner Familie ist und wo du leben möchtest — und warum.',
    actPlaceholder='Hi! I am from …',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Cold, Colder,<br><em>the Coldest</em>',
    coverSub='De Brasil a Brighton: AM / IS / ARE, comparativos y superlativos, DOES / DOESN’T y el acento de Brighton — <br>con un juego de traducción portugués ⇄ inglés.',
    chipLevel='A1', chipFocus='am / is / are · -er / -est · does', chipCount='27 diapositivas',

    d1t='Hola desde Brighton', d1n='Parte 1 · I am, he is, they are',
    d2t='Cold, Colder, the Coldest', d2n='Parte 2 · comparar lugares',
    d3t='¿Conduce un taxi?', d3n='Parte 3 · trabajos, does y doesn’t',

    e1='Am · is · are', e2='-er · -est', e3='Does · doesn’t',
    e4='El acento de Brighton', e5='Traducir', eR='La regla', eV='Palabras nuevas',

    p1t='Te presento a Ana', p2t='¿Brasil o Escocia?', p3t='El nuevo trabajo de Rafael',

    tAt='¿AM, IS o ARE?',
    tA1='Con I, siempre AM.',
    tA2='Una persona o una cosa: IS.',
    tA3='Más de una persona: ARE. TEACHERS = THEY, así que ARE.',
    tA4='En inglés la edad va con BE. Nunca "I have 32 years" (TENGO 32 años).',

    tBt='Comparar: dos reglas y dos sorpresas',
    tB1='Palabras cortas: -ER para comparar dos cosas, THE + -EST para la número uno. Con THAN: "colder THAN Brighton".',
    tB2='Una vocal + una consonante al final: la consonante se escribe dos veces. HOT → HOTTER.',
    tB3='Palabras largas: MORE o THE MOST delante. Nunca "expensiver".',
    tB4='GOOD es irregular. ¡Apréndelo de memoria!',

    gapT='Escribe la palabra que falta',
    gapHint1='Escribe AM, IS o ARE.',
    gapHint2='Usa la palabra entre paréntesis. Compara: -ER, o una palabra nueva.',
    g1w='I → AM: "I AM from Curitiba."',
    g2w='Rafael y Lucas = THEY → ARE.',
    g3w='Callum = HE → IS.',
    g4w='HOT: una vocal + una consonante, así que la T se dobla: HOTTER.',
    g5w='GOOD → BETTER → THE BEST. Nunca "gooder".',
    g6w='BIG: una vocal + una consonante, así que la G se dobla: BIGGER.',

    mcT='Elige la palabra correcta', mc4T='¿Qué letra falta?',
    q1w='TEACHERS es más de una persona = THEY → ARE.',
    q2w='La edad va con BE: "He IS sixteen months old." En inglés nunca TIENES una edad.',
    q3w='Dos lugares, y THAN: COLDER THAN. Nunca "more cold".',
    q4w='La número uno de todas las ciudades: THE COLDEST. Una sílaba lleva -EST, no MOST.',
    q5w='Una pregunta con he, she o it empieza con DOES: "DOES your husband DRIVE …?"',
    q6w='HE + DOESN’T + DRIVE. Después de DOESN’T el verbo no lleva -S.',
    c8='En Brighton, mucha gente dice WATER así. ¿Qué letra no dicen?',
    q8w='La T desaparece. Es el golpe de glotis (glottal stop): "wa’er", "Brigh’on".',

    sortT='¿-ER / -EST o MORE / THE MOST?',
    sortHint='Toca cada palabra y ponla en la caja correcta.',
    binA='-ER / -EST', binB='MORE / THE MOST',
    sortWhy='Las palabras cortas llevan -ER / -EST: colder, bigger, hotter, smaller, older. Las largas llevan MORE / THE MOST: more expensive, more beautiful, more difficult, more interesting, more famous.',

    jAt='Cuatro conductores',
    jA1='Conduce un camión: un vehículo muy grande para cosas, no para personas. (En EE. UU.: TRUCK.)',
    jA2='Conduce una furgoneta: más pequeña que un camión. Trae paquetes a tu puerta.',
    jA3='Lleva a personas en un taxi, y ellas pagan.',
    jA4='Conduce el coche de una persona rica. Se dice "SHOW-fer".',

    tCt='DOES y DOESN’T',
    tC1='Con he, she, it, el verbo lleva -S.',
    tC2='Una pregunta empieza con DOES. La -S pasa a DOES, así que el verbo no lleva -S.',
    tC3='DOESN’T = DOES NOT. Después, el verbo no lleva -S.',
    tC4='Con I, you, we y they: DO y DON’T.',

    orderT='Forma la pregunta',
    orderHint='Toca las palabras en el orden correcto. ¡Sobra una palabra!',
    o1w='"DOES Rafael DRIVE a van?" DOES ya tiene la -S, así que sobra DRIVES.',

    tEt='Así se habla en Brighton',
    tE1='En el sur de Inglaterra, mucha gente no pronuncia la R al final de una palabra.',
    tE2='¡Pero antes de una vocal, a veces añaden una R!',
    tE3='Mucha gente corta el sonido en la garganta en vez de decir la T.',

    trT='Traduce la frase',
    trHint='Escríbela en inglés. Toca el interruptor para ir al revés: English → Español.',
    tw1='"Soy de Brasil." = "I am from Brazil." SOY = AM. DE BRASIL = FROM Brazil.',
    tw2='"Mi hijo tiene dieciséis meses." = "My son is sixteen months old." En español TIENES una edad (TIENE). En inglés la edad va con BE (IS).',
    tw3='"Escocia es más fría que Brasil." = "Scotland is colder than Brazil." MÁS FRÍA = COLDER. QUE = THAN.',
    tw4='"… la ciudad más fría de Brasil." = "… the coldest city IN Brazil." Después de THE + -EST, un lugar lleva IN, no OF.',
    tw5='"¿Tu marido conduce un taxi?" = "Does your husband drive a taxi?" La pregunta empieza con DOES, y DRIVE no lleva -S.',
    tw6='"Él no conduce un camión." = "He doesn’t drive a lorry." NO = DOESN’T. CAMIÓN = LORRY (en EE. UU.: TRUCK).',

    actTitle='¿Dónde quieres vivir?',
    actUse='Usa al menos tres:',
    actSpeakBrief='Habla de tu ciudad, tu familia y el país de tus sueños.',
    actSpeak1='Compara dos ciudades que conoces: "Brighton is colder than … but …"',
    actSpeak2='Pregunta por una persona de la familia de tu compañero: "Does your brother drive? What does he do?"',
    actSpeak3='El país de tus sueños: "I want to live in … because it is the most …"',
    actWriteKind='Escritura · 50–80 palabras',
    actWriteBrief='Escribe un mensaje a tu profesor de inglés. Di de dónde eres, quién hay en tu familia y dónde quieres vivir, y por qué.',
    actPlaceholder='Hi! I am from …',
)

# ══════════════════════════════════════════════════════════════════════
#  PORTUGUESE (Brazilian)
# ══════════════════════════════════════════════════════════════════════
T['pt'] = dict(
    coverTitle='Cold, Colder,<br><em>the Coldest</em>',
    coverSub='Do Brasil a Brighton: AM / IS / ARE, comparativos e superlativos, DOES / DOESN’T e o sotaque de Brighton — <br>com um jogo de tradução português ⇄ inglês.',
    chipLevel='A1', chipFocus='am / is / are · -er / -est · does', chipCount='27 slides',

    d1t='Olá de Brighton', d1n='Parte 1 · I am, he is, they are',
    d2t='Cold, Colder, the Coldest', d2n='Parte 2 · comparando lugares',
    d3t='Ele dirige um táxi?', d3n='Parte 3 · profissões, does e doesn’t',

    e1='Am · is · are', e2='-er · -est', e3='Does · doesn’t',
    e4='O sotaque de Brighton', e5='Traduzir', eR='A regra', eV='Palavras novas',

    p1t='Conheça a Ana', p2t='Brasil ou Escócia?', p3t='O novo emprego do Rafael',

    tAt='AM, IS ou ARE?',
    tA1='Com I, sempre AM.',
    tA2='Uma pessoa ou uma coisa: IS.',
    tA3='Mais de uma pessoa: ARE. TEACHERS = THEY, então ARE.',
    tA4='Em inglês, idade é com BE. Nunca "I have 32 years" (TENHO 32 anos).',

    tBt='Comparar: duas regras e duas surpresas',
    tB1='Palavras curtas: -ER para comparar duas coisas, THE + -EST para a número um. Com THAN: "colder THAN Brighton".',
    tB2='Uma vogal + uma consoante no fim: escreva a consoante duas vezes. HOT → HOTTER.',
    tB3='Palavras longas: MORE ou THE MOST na frente. Nunca "expensiver".',
    tB4='GOOD é irregular. Decore!',

    gapT='Escreva a palavra que falta',
    gapHint1='Escreva AM, IS ou ARE.',
    gapHint2='Use a palavra entre parênteses. Compare: -ER, ou uma palavra nova.',
    g1w='I → AM: "I AM from Curitiba."',
    g2w='Rafael e Lucas = THEY → ARE.',
    g3w='Callum = HE → IS.',
    g4w='HOT: uma vogal + uma consoante, então o T dobra: HOTTER.',
    g5w='GOOD → BETTER → THE BEST. Nunca "gooder".',
    g6w='BIG: uma vogal + uma consoante, então o G dobra: BIGGER.',

    mcT='Escolha a palavra certa', mc4T='Qual letra está faltando?',
    q1w='TEACHERS é mais de uma pessoa = THEY → ARE.',
    q2w='Idade é com BE: "He IS sixteen months old." Em inglês você nunca TEM uma idade.',
    q3w='Dois lugares, e THAN: COLDER THAN. Nunca "more cold".',
    q4w='A número um de todas as cidades: THE COLDEST. Uma sílaba leva -EST, não MOST.',
    q5w='Uma pergunta com he, she ou it começa com DOES: "DOES your husband DRIVE …?"',
    q6w='HE + DOESN’T + DRIVE. Depois de DOESN’T o verbo não tem -S.',
    c8='Em Brighton, muita gente fala WATER assim. Qual letra eles não falam?',
    q8w='O T desaparece. É a oclusiva glotal (glottal stop): "wa’er", "Brigh’on".',

    sortT='-ER / -EST ou MORE / THE MOST?',
    sortHint='Toque em cada palavra e coloque na caixa certa.',
    binA='-ER / -EST', binB='MORE / THE MOST',
    sortWhy='Palavras curtas levam -ER / -EST: colder, bigger, hotter, smaller, older. Palavras longas levam MORE / THE MOST: more expensive, more beautiful, more difficult, more interesting, more famous.',

    jAt='Quatro motoristas',
    jA1='Dirige um caminhão: um veículo muito grande para coisas, não para pessoas. (Nos EUA: TRUCK.)',
    jA2='Dirige uma van: menor que um caminhão. Vans entregam encomendas na sua porta.',
    jA3='Leva pessoas de táxi, e elas pagam.',
    jA4='Dirige o carro de uma pessoa rica. Fala-se "SHOW-fer".',

    tCt='DOES e DOESN’T',
    tC1='Com he, she, it, o verbo ganha -S.',
    tC2='Uma pergunta começa com DOES. O -S passa para o DOES, então o verbo fica sem -S.',
    tC3='DOESN’T = DOES NOT. Depois dele, o verbo fica sem -S.',
    tC4='Com I, you, we e they: DO e DON’T.',

    orderT='Monte a pergunta',
    orderHint='Toque nas palavras na ordem certa. Sobra uma palavra!',
    o1w='"DOES Rafael DRIVE a van?" O DOES já tem o -S, então DRIVES é a palavra que sobra.',

    tEt='Como se fala em Brighton',
    tE1='No sul da Inglaterra, muita gente não pronuncia o R no fim da palavra.',
    tE2='Mas antes de uma vogal, às vezes eles colocam um R a mais!',
    tE3='Muita gente para o som na garganta em vez de falar o T.',

    trT='Traduza a frase',
    trHint='Escreva em inglês. Toque no botão para ir ao contrário: English → Português.',
    tw1='"Eu sou do Brasil." = "I am from Brazil." SOU = AM. DO BRASIL = FROM Brazil.',
    tw2='"Meu filho tem dezesseis meses." = "My son is sixteen months old." Em português você TEM uma idade (TEM). Em inglês você É uma idade (IS).',
    tw3='"A Escócia é mais fria que o Brasil." = "Scotland is colder than Brazil." MAIS FRIA = COLDER. QUE = THAN.',
    tw4='"… a cidade mais fria do Brasil." = "… the coldest city IN Brazil." Depois de THE + -EST, o lugar leva IN, não OF.',
    tw5='"Seu marido dirige um táxi?" = "Does your husband drive a taxi?" A pergunta começa com DOES, e DRIVE fica sem -S.',
    tw6='"Ele não dirige um caminhão." = "He doesn’t drive a lorry." NÃO = DOESN’T. CAMINHÃO = LORRY (nos EUA: TRUCK).',

    actTitle='Onde você quer morar?',
    actUse='Use pelo menos três:',
    actSpeakBrief='Fale sobre a sua cidade, a sua família e o país dos seus sonhos.',
    actSpeak1='Compare duas cidades que você conhece: "Brighton is colder than … but …"',
    actSpeak2='Pergunte sobre uma pessoa da família do seu colega: "Does your brother drive? What does he do?"',
    actSpeak3='O país dos seus sonhos: "I want to live in … because it is the most …"',
    actWriteKind='Escrita · 50–80 palavras',
    actWriteBrief='Escreva uma mensagem para o seu professor de inglês. Diga de onde você é, quem é a sua família e onde você quer morar — e por quê.',
    actPlaceholder='Hi! I am from …',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %3d keys' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else 'ok',
              ('EXTRA %s' % sorted(x)) if x else '')
