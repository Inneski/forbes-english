# -*- coding: utf-8 -*-
"""Interface strings for the Stranger Things English test (A2–B1).

English, German and Spanish, all three complete. The generic chrome —
buttons, score label, the plural-aware word counter — is lifted verbatim
from `chrome_i18n.py` rather than retranslated, because it is identical
in every deck on the site.

Scope boundary, per the house style: the app's own chrome translates, the
English being taught does not. Question stems, options, gap sentences,
example sentences and the activation chips all stay in English in every
language.

**Part 2 is the deliberate exception, and it is the point of this deck.**
It is an L1 → English translation task, so the *prompt* beside each box is
content that has to translate: a German learner must be shown `der Herbst`
and a Spanish learner `el otoño`, or the task does not exist for them. The
prompts therefore live here, as the ten `v*p` keys, and switch with the
selector like any other string. The answer is always the English word, and
the English word never appears in any prompt in any language — asserted at
build time across all three, in `build_stranger_test.py`.

Two prompts had to be written rather than translated:

* **English has no L1 for an English speaker.** "Translate *der Herbst*"
  is not a task you can set someone whose first language is English, so
  the English layer substitutes the nearest honest equivalent: a
  definition or a picture-clue that identifies the word without naming
  it or any of its accepted spellings — "the season between summer and
  winter, when the woods turn orange" for *autumn*, "you roll a heavy
  ball down a lane to knock over ten pins" for *bowling alley*. The
  learner still has to produce the word from meaning; the route to it is
  a definition instead of a first language. Every English clue is checked
  at build time against every accepted answer on its own slide, so a clue
  cannot leak the word it is asking for or its neighbour's.
* **The German prompt for the roller disco is a loanword.** German
  really does say *die Rollerdisco*, which hands over the answer intact.
  The prompt here is *die Rollschuhdisco*, which is the native German
  compound, means the same thing, and asks the learner for the English.
  The build asserts that no prompt in any language contains its own
  answer, which is how the loanword was caught.

`build_stranger_test.py` reads T['en'] directly, so a slide and its
English string cannot drift apart: there is one copy of each.
"""
import json
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext',
        'actEyebrow', 'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    # ── cover ──
    coverTitle='Stranger Things: <em>the English Test</em>',
    coverSub='Say where things are in a picture, name what you can see, and '
             'get has, have, nor and the two present tenses right',
    chipLevel='A2&ndash;B1',
    chipFocus='Picture description &amp; grammar',
    chipTime='45&ndash;60 minutes',
    chipCount='NN slides',

    # ── eyebrows ──
    tOrient='Orientation',
    tPic='Language focus &middot; Describing a picture',
    tVocab='Language focus &middot; Words for the scene',
    tTask='How the next part works',
    tGram='Language focus &middot; Grammar',

    # ── 2. orientation ──
    oT='How this works',
    oa='Read first, answer after',
    ob='Twenty-eight points',
    on='Nothing is tested before it has been taught. Every question tells you '
       'why your answer was right or wrong, so read the feedback even when '
       'you score. Your running total sits at the top of every slide.',

    # ── 3. positions: how far away ──
    p1T='How far away is it?',
    p1a='in the foreground',
    p1b='in the middle',
    p1c='in the background',
    p1n='These three answer one question: how far from you is it? Use them '
        'with <em>is</em> or <em>is standing</em> &mdash; <em>the deer is in '
        'the foreground</em>.',

    # ── 4. positions: which side ──
    p2T='Which side, which corner, who is touching whom',
    p2a='on the right-hand side',
    p2b='in the bottom left-hand corner',
    p2c='a hand on her shoulder',
    p2n='British English hyphenates <em>right-hand</em> and <em>left-hand</em>. '
        'A corner needs two words: top or bottom, then left or right.',

    # ── 9. autumn words ──
    v1T='An autumn day in the woods',
    v1a='autumn',
    v1b='leaves',
    v1c='a scarf',
    v1n='Both <em>leaf</em> and <em>scarf</em> change f to ves in the plural, '
        'like <em>half &rarr; halves</em> and <em>shelf &rarr; shelves</em>.',

    # ── 10. colour and light ──
    v2T='Colour and light',
    v2a='rusty',
    v2b='bright',
    v2c='shining through',
    v2n='<em>Shine</em> is irregular: shine &rarr; shone. Light <em>shines '
        'through</em> something &mdash; through the trees, through a window, '
        'through the dark.',

    # ── 11. two places ──
    v3T='Two places the kids go',
    v3a='a bowling alley',
    v3b='a rollerdisco',
    v3n='<em>Bowling alley</em> is two words; <em>rollerdisco</em> is usually '
        'written as one, though you will also see <em>roller disco</em>.',

    # ── 12. open land ──
    v4T='Three kinds of open land',
    v4a='a plain',
    v4b='a desert',
    v4c='a field',
    v4n='Flat is not the same as dry. A plain can be green farmland; a desert '
        'can have dunes and hills. <em>Plain</em> is also an adjective meaning '
        'simple or ordinary &mdash; a plain shirt has no pattern.',

    # ── 13. how part 2 works ──
    tkT='Writing the word, not choosing it',
    tka='What you will see',
    tkb='What to type',
    tkn='One attempt per box. Press Enter or click Check. Spelling counts, so '
        'the plurals on the last few slides are worth a second look.',

    # ── 23. has / have ──
    g1T='has or have',
    g1a='he, she, it &rarr; has',
    g1b='I, you, we, they &rarr; have',
    g1n='A single name is he, she or it: <em>Eleven has</em>. Two names joined '
        'by <em>and</em> are they: <em>Mike and Dustin have</em>.',

    # ── 24. has / have traps ──
    g2T='Two traps',
    g2a='There is no form <em>haves</em>',
    g2b='has got and have got',
    g2n='In questions and negatives the little verb takes the -s, and '
        '<em>have</em> goes back to its plain form: <em>Does she have a '
        'torch?</em> &mdash; never <em>Does she has</em>.',

    # ── 27. nor ──
    g3T='Where nor really belongs',
    g3a='neither &hellip; nor',
    g3b='nor + inversion',
    g3n='Watch the word order after <em>nor</em>: the verb jumps in front of '
        'the subject. <em>Nor does she listen</em>, not <em>nor she does '
        'listen</em>.',

    # ── 28. and where or is right ──
    g4T='&mdash; and where or is right',
    g4a='One verb, two things &rarr; or',
    g4b='Give nor a verb of its own',
    g4n='So <em>or</em> after a negative is good English. What is wrong is '
        '<em>neither &hellip; or</em>, and <em>nor she does</em>.',

    # ── 31. state and action ──
    g5T='Happening now, or simply true?',
    g5a='Happening right now &rarr; be + -ing',
    g5b='States &rarr; present simple',
    g5n='A few verbs do both, with two meanings: <em>they look serious</em> '
        '(= they seem) but <em>they are looking at the map</em> (= an action '
        'in progress).',

    # ── 32. there is / there are ──
    g6T='there is and there are',
    g6a='there is + one thing',
    g6b='there are + more than one',
    g6n='The verb agrees with what comes after it, not with <em>there</em>. '
        'And <em>there are</em> introduces something new, while <em>they '
        'are</em> points back at something already mentioned.',

    # ── activity headers ──
    a1E='Part 1 &middot; Describing a picture',
    a1T='Where is it in the picture?',
    a2E='Part 2 &middot; Into English',
    a2T='Write the English word',
    a3E='Part 3 &middot; The word that fits',
    a3T='Which word belongs here?',
    a4E='Part 4 &middot; Subject and verb',
    a4T='Which form fits the subject?',
    a5E='Part 5 &middot; Joining two negatives',
    a5T='Choose the link word',
    a6E='Part 6 &middot; Now, or always?',
    a6T='Choose the correct form',
    bankLabel='Word bank:',

    # ── Part 2 prompts — the L1 slot. In English: a definition, never the
    #    word itself and never any spelling the box accepts. ──
    v1p='the season between summer and winter, when the woods turn orange',
    v2p='the flat green parts of a tree &mdash; write the plural',
    v3p='you wind this round your neck when it is cold',
    v4p='giving out a lot of light; the opposite of dim',
    v5p='you roll a heavy ball down a lane to knock over ten pins',
    v6p='you put on skates and go round and round to pop music',
    v7p='so dry that almost nothing grows there &mdash; sand and bare rock',
    v8p='a wide area of flat land with no hills in it',
    v9p='a piece of land with a hedge or a fence round it, where crops grow',
    v10p='the reddish-brown colour of old iron left out in the rain',

    # ── Part 2 hints: the scaffold, never the answer ──
    h1='Two words for the woods in October.',
    h2='One thing you wear, one word for strong light.',
    h3='Two places the kids go at the weekend.',
    h4='Two kinds of open country: one is only dry, one is only flat.',
    h5='One piece of farmland, one colour.',

    # ── Part 4 hints ──
    h6='Look at the subject of each sentence first.',
    h7='One of these subjects is a single thing, the other is a group.',

    # ── results ──
    resPerfect='Full marks. You can place things in a picture, you produced '
               'every word from meaning alone, and you kept the two present '
               'tenses apart. That last one is where most of this level '
               'comes undone.',
    resStrong='Strong. Look at where the misses fall. The position phrases '
              'and the nouns tend to stick after one pass; the tenses and the '
              'link words need re-reading against real sentences every time.',
    resMid='A pass. Go back to the slides on the two present tenses and on '
           'nor. Between them they carry a third of the marks, and both are '
           'about choosing between two forms rather than knowing one word.',
    resLow='Work through the language slides again before you retry. Every '
           'word and every rule tested here is explained on a slide before '
           'the questions start.',

    # ── activation ──
    actTitle='Hawkins in autumn',
    actUse='Use at least four:',
    actSpeakBrief='Sit so that only one of you can see the screen: you are '
                  'describing a photograph to someone who has to draw it.',
    actSpeak1='Describe the cover picture &mdash; foreground, middle, '
              'background, and which side the animal is on. Your partner '
              'draws it without looking.',
    actSpeak2='Swap. One minute on an autumn evening in your own town: the '
              'trees, the light, what people are wearing.',
    actSpeak3='Both: it is Friday night and you cannot agree. Argue for the '
              'bowling alley against the rollerdisco, and say what is '
              'happening at each right now.',
    actWriteKind='Writing &middot; 100&ndash;150 words',
    actWriteBrief='Write to a friend who has never been to Hawkins. Describe '
                  'the photograph you are sending &mdash; say where each '
                  'thing is in it &mdash; then what the town is like in '
                  'autumn and what people are doing there right now.',
    # A real character, not an entity: applyLang assigns this to
    # el.placeholder as a JS string, and a DOM property assignment does not
    # decode entities — HOUSE-STYLE §13 in its attribute form.
    actPlaceholder='Dear Barb, I am sending you a photograph of the woods …',
)

T['de'] = dict(
    coverTitle='Stranger Things: <em>the English Test</em>',
    coverSub='Sag, wo etwas auf einem Bild ist, benenne, was du siehst, und '
             'triff has, have, nor und die beiden Präsensformen richtig',
    chipLevel='A2&ndash;B1',
    chipFocus='Bildbeschreibung &amp; Grammatik',
    chipTime='45&ndash;60 Minuten',
    chipCount='NN Folien',

    tOrient='Orientierung',
    tPic='Sprachfokus &middot; Ein Bild beschreiben',
    tVocab='Sprachfokus &middot; Wörter für die Szene',
    tTask='So läuft der nächste Teil',
    tGram='Sprachfokus &middot; Grammatik',

    oT='So funktioniert es',
    oa='Erst lesen, dann antworten',
    ob='Achtundzwanzig Punkte',
    on='Nichts wird abgefragt, bevor es erklärt wurde. Bei jeder Aufgabe '
       'erfährst du, warum deine Antwort richtig oder falsch war — lies die '
       'Rückmeldung auch dann, wenn du punktest. Dein Punktestand steht oben '
       'auf jeder Folie.',

    p1T='Wie weit ist es entfernt?',
    p1a='in the foreground',
    p1b='in the middle',
    p1c='in the background',
    p1n='Diese drei beantworten eine Frage: Wie weit ist es von dir entfernt? '
        'Sie stehen mit <em>is</em> oder <em>is standing</em> — <em>the deer '
        'is in the foreground</em>.',

    p2T='Welche Seite, welche Ecke, wer berührt wen',
    p2a='on the right-hand side',
    p2b='in the bottom left-hand corner',
    p2c='a hand on her shoulder',
    p2n='Im britischen Englisch werden <em>right-hand</em> und '
        '<em>left-hand</em> mit Bindestrich geschrieben. Eine Ecke braucht '
        'zwei Angaben: oben oder unten, dann links oder rechts.',

    v1T='Ein Herbsttag im Wald',
    v1a='autumn',
    v1b='leaves',
    v1c='a scarf',
    v1n='<em>leaf</em> und <em>scarf</em> ändern im Plural f zu ves, genau wie '
        '<em>half &rarr; halves</em> und <em>shelf &rarr; shelves</em>.',

    v2T='Farbe und Licht',
    v2a='rusty',
    v2b='bright',
    v2c='shining through',
    v2n='<em>shine</em> ist unregelmäßig: shine &rarr; shone. Licht '
        '<em>shines through</em> etwas — durch die Bäume, durch ein Fenster, '
        'durch die Dunkelheit.',

    v3T='Zwei Orte, an die die Kinder gehen',
    v3a='a bowling alley',
    v3b='a rollerdisco',
    v3n='<em>bowling alley</em> schreibt man getrennt, <em>rollerdisco</em> '
        'meist zusammen — <em>roller disco</em> kommt aber auch vor.',

    v4T='Drei Arten von offenem Land',
    v4a='a plain',
    v4b='a desert',
    v4c='a field',
    v4n='Flach ist nicht dasselbe wie trocken. Eine <em>plain</em> kann grünes '
        'Ackerland sein, ein <em>desert</em> kann Dünen und Hügel haben. '
        '<em>plain</em> ist außerdem ein Adjektiv und heißt schlicht: ein '
        '<em>plain shirt</em> hat kein Muster.',

    tkT='Das Wort schreiben, nicht auswählen',
    tka='Was du siehst',
    tkb='Was du eintippst',
    tkn='Ein Versuch pro Feld. Drücke Enter oder klicke auf Prüfen. Die '
        'Schreibweise zählt — die Pluralformen von den letzten Folien lohnen '
        'einen zweiten Blick.',

    g1T='has oder have',
    g1a='he, she, it &rarr; has',
    g1b='I, you, we, they &rarr; have',
    g1n='Ein einzelner Name ist he, she oder it: <em>Eleven has</em>. Zwei mit '
        '<em>and</em> verbundene Namen sind they: <em>Mike and Dustin '
        'have</em>.',

    g2T='Zwei Fallen',
    g2a='Die Form <em>haves</em> gibt es nicht',
    g2b='has got und have got',
    g2n='In Fragen und Verneinungen trägt das Hilfsverb das -s, und '
        '<em>have</em> steht in der Grundform: <em>Does she have a torch?</em> '
        '— niemals <em>Does she has</em>.',

    g3T='Wohin nor wirklich gehört',
    g3a='neither &hellip; nor',
    g3b='nor + Inversion',
    g3n='Achte auf die Wortstellung nach <em>nor</em>: Das Verb springt vor '
        'das Subjekt. <em>Nor does she listen</em>, nicht <em>nor she does '
        'listen</em>.',

    g4T='&mdash; und wo or richtig ist',
    g4a='Ein Verb, zwei Dinge &rarr; or',
    g4b='Gib nor ein eigenes Verb',
    g4n='<em>or</em> nach einer Verneinung ist also gutes Englisch. Falsch '
        'sind <em>neither &hellip; or</em> und <em>nor she does</em>.',

    g5T='Gerade jetzt oder einfach wahr?',
    g5a='Gerade jetzt &rarr; be + -ing',
    g5b='Zustände &rarr; present simple',
    g5n='Ein paar Verben können beides, mit zwei Bedeutungen: <em>they look '
        'serious</em> (= sie wirken so) gegen <em>they are looking at the '
        'map</em> (= eine Handlung, die gerade läuft).',

    g6T='there is und there are',
    g6a='there is + eine Sache',
    g6b='there are + mehrere',
    g6n='Das Verb richtet sich nach dem, was folgt, nicht nach <em>there</em>. '
        'Und <em>there are</em> führt etwas Neues ein, während <em>they '
        'are</em> auf schon Genanntes zurückweist.',

    a1E='Teil 1 &middot; Ein Bild beschreiben',
    a1T='Wo ist es auf dem Bild?',
    a2E='Teil 2 &middot; Ins Englische',
    a2T='Schreibe das englische Wort',
    a3E='Teil 3 &middot; Das passende Wort',
    a3T='Welches Wort gehört hierher?',
    a4E='Teil 4 &middot; Subjekt und Verb',
    a4T='Welche Form passt zum Subjekt?',
    a5E='Teil 5 &middot; Zwei Verneinungen verbinden',
    a5T='Wähle das Bindewort',
    a6E='Teil 6 &middot; Jetzt oder immer?',
    a6T='Wähle die richtige Form',
    bankLabel='Wortspeicher:',

    v1p='der Herbst',
    v2p='die Blätter',
    v3p='der Schal',
    v4p='hell / leuchtend',
    v5p='die Bowlingbahn',
    v6p='die Rollschuhdisco',
    v7p='die Wüste',
    v8p='die Ebene',
    v9p='das Feld / die Wiese',
    v10p='rostfarben / rostig',

    h1='Zwei Wörter für den Wald im Oktober.',
    h2='Ein Kleidungsstück, ein Wort für starkes Licht.',
    h3='Zwei Orte, an die die Kinder am Wochenende gehen.',
    h4='Zwei Arten offenes Land: eine ist nur trocken, eine ist nur flach.',
    h5='Ein Stück Ackerland, eine Farbe.',

    h6='Sieh dir zuerst das Subjekt jedes Satzes an.',
    h7='Eines dieser Subjekte ist eine einzelne Sache, das andere eine Gruppe.',

    resPerfect='Volle Punktzahl. Du kannst Dinge auf einem Bild verorten, du '
               'hast jedes Wort allein aus der Bedeutung heraus geschrieben, '
               'und du hältst die beiden Präsensformen auseinander. Genau '
               'daran scheitert es auf diesem Niveau am häufigsten.',
    resStrong='Stark. Sieh dir an, wo die Fehler liegen. Die Ortsangaben und '
              'die Nomen sitzen meist nach einem Durchgang; die Zeitformen '
              'und die Bindewörter muss man jedes Mal neu an echten Sätzen '
              'prüfen.',
    resMid='Bestanden. Geh noch einmal zu den Folien über die beiden '
           'Präsensformen und über nor. Zusammen tragen sie ein Drittel der '
           'Punkte, und bei beiden geht es um die Wahl zwischen zwei Formen, '
           'nicht um ein einzelnes Wort.',
    resLow='Arbeite die Sprachfolien noch einmal durch, bevor du es erneut '
           'versuchst. Jedes Wort und jede Regel, die hier abgefragt wird, '
           'steht vor den Aufgaben auf einer Folie.',

    actTitle='Hawkins im Herbst',
    actUse='Mindestens vier verwenden:',
    actSpeakBrief='Setzt euch so, dass nur eine Person den Bildschirm sieht: '
                  'Du beschreibst ein Foto jemandem, der es zeichnen soll.',
    actSpeak1='Beschreibe das Titelbild &mdash; Vordergrund, Mitte, '
              'Hintergrund und auf welcher Seite das Tier steht. Dein Partner '
              'zeichnet es, ohne hinzusehen.',
    actSpeak2='Tauscht. Eine Minute über einen Herbstabend in deiner eigenen '
              'Stadt: die Bäume, das Licht, was die Leute anhaben.',
    actSpeak3='Beide: Es ist Freitagabend und ihr seid euch nicht einig. '
              'Streitet für <em>bowling alley</em> gegen <em>rollerdisco</em> '
              'und sagt, was dort gerade passiert.',
    actWriteKind='Schreiben &middot; 100&ndash;150 Wörter',
    actWriteBrief='Schreib an eine Freundin, die noch nie in Hawkins war. '
                  'Beschreibe das Foto, das du schickst &mdash; sag, wo jedes '
                  'Ding darauf ist &mdash; und dann, wie die Stadt im Herbst '
                  'aussieht und was die Leute dort gerade machen.',
    actPlaceholder='Dear Barb, I am sending you a photograph of the woods …',
)

T['es'] = dict(
    coverTitle='Stranger Things: <em>the English Test</em>',
    coverSub='Di dónde está cada cosa en una imagen, nombra lo que ves y '
             'acierta con has, have, nor y los dos presentes',
    chipLevel='A2&ndash;B1',
    chipFocus='Descripción de imágenes y gramática',
    chipTime='45&ndash;60 minutos',
    chipCount='NN diapositivas',

    tOrient='Orientación',
    tPic='Enfoque lingüístico &middot; Describir una imagen',
    tVocab='Enfoque lingüístico &middot; Palabras para la escena',
    tTask='Cómo funciona la parte siguiente',
    tGram='Enfoque lingüístico &middot; Gramática',

    oT='Cómo funciona esto',
    oa='Primero leer, después responder',
    ob='Veintiocho puntos',
    on='Nada se evalúa antes de haberse explicado. Cada pregunta te dice por '
       'qué tu respuesta fue correcta o incorrecta: lee el comentario también '
       'cuando aciertes. Tu puntuación aparece en la parte superior de cada '
       'diapositiva.',

    p1T='¿A qué distancia está?',
    p1a='in the foreground',
    p1b='in the middle',
    p1c='in the background',
    p1n='Estas tres responden a una sola pregunta: ¿a qué distancia está de '
        'ti? Se usan con <em>is</em> o <em>is standing</em> — <em>the deer is '
        'in the foreground</em>.',

    p2T='Qué lado, qué esquina, quién toca a quién',
    p2a='on the right-hand side',
    p2b='in the bottom left-hand corner',
    p2c='a hand on her shoulder',
    p2n='El inglés británico escribe <em>right-hand</em> y <em>left-hand</em> '
        'con guion. Una esquina necesita dos datos: arriba o abajo, y después '
        'izquierda o derecha.',

    v1T='Un día de otoño en el bosque',
    v1a='autumn',
    v1b='leaves',
    v1c='a scarf',
    v1n='Tanto <em>leaf</em> como <em>scarf</em> cambian f por ves en plural, '
        'igual que <em>half &rarr; halves</em> y <em>shelf &rarr; '
        'shelves</em>.',

    v2T='Color y luz',
    v2a='rusty',
    v2b='bright',
    v2c='shining through',
    v2n='<em>shine</em> es irregular: shine &rarr; shone. La luz <em>shines '
        'through</em> algo — entre los árboles, por una ventana, a través de '
        'la oscuridad.',

    v3T='Dos sitios a los que van los chicos',
    v3a='a bowling alley',
    v3b='a rollerdisco',
    v3n='<em>bowling alley</em> se escribe en dos palabras; '
        '<em>rollerdisco</em> suele escribirse en una, aunque también verás '
        '<em>roller disco</em>.',

    v4T='Tres clases de terreno abierto',
    v4a='a plain',
    v4b='a desert',
    v4c='a field',
    v4n='Llano no es lo mismo que seco. Una <em>plain</em> puede ser campo '
        'verde de cultivo; un <em>desert</em> puede tener dunas y cerros. '
        '<em>plain</em> es además un adjetivo y significa sencillo: una '
        '<em>plain shirt</em> no lleva estampado.',

    tkT='Escribir la palabra, no elegirla',
    tka='Lo que vas a ver',
    tkb='Lo que tienes que escribir',
    tkn='Un intento por casilla. Pulsa Enter o haz clic en Comprobar. La '
        'ortografía cuenta, así que conviene repasar los plurales de las '
        'últimas diapositivas.',

    g1T='has o have',
    g1a='he, she, it &rarr; has',
    g1b='I, you, we, they &rarr; have',
    g1n='Un nombre en singular es he, she o it: <em>Eleven has</em>. Dos '
        'nombres unidos por <em>and</em> son they: <em>Mike and Dustin '
        'have</em>.',

    g2T='Dos trampas',
    g2a='La forma <em>haves</em> no existe',
    g2b='has got y have got',
    g2n='En preguntas y negaciones la -s la lleva el auxiliar y <em>have</em> '
        'vuelve a su forma básica: <em>Does she have a torch?</em> — nunca '
        '<em>Does she has</em>.',

    g3T='Dónde encaja realmente nor',
    g3a='neither &hellip; nor',
    g3b='nor + inversión',
    g3n='Fíjate en el orden después de <em>nor</em>: el verbo se coloca '
        'delante del sujeto. <em>Nor does she listen</em>, no <em>nor she '
        'does listen</em>.',

    g4T='&mdash; y dónde el correcto es or',
    g4a='Un verbo, dos cosas &rarr; or',
    g4b='Dale a nor su propio verbo',
    g4n='Así que <em>or</em> después de una negación es inglés correcto. Lo '
        'que está mal es <em>neither &hellip; or</em> y <em>nor she does</em>.',

    g5T='¿Ocurre ahora o simplemente es así?',
    g5a='Ocurre justo ahora &rarr; be + -ing',
    g5b='Estados &rarr; present simple',
    g5n='Unos pocos verbos admiten las dos formas, con dos significados: '
        '<em>they look serious</em> (= lo parecen) frente a <em>they are '
        'looking at the map</em> (= una acción en curso).',

    g6T='there is y there are',
    g6a='there is + una sola cosa',
    g6b='there are + más de una',
    g6n='El verbo concuerda con lo que viene detrás, no con <em>there</em>. Y '
        '<em>there are</em> presenta algo nuevo, mientras que <em>they '
        'are</em> remite a algo ya mencionado.',

    a1E='Parte 1 &middot; Describir una imagen',
    a1T='¿Dónde está en la imagen?',
    a2E='Parte 2 &middot; Al inglés',
    a2T='Escribe la palabra inglesa',
    a3E='Parte 3 &middot; La palabra que encaja',
    a3T='¿Qué palabra va aquí?',
    a4E='Parte 4 &middot; Sujeto y verbo',
    a4T='¿Qué forma encaja con el sujeto?',
    a5E='Parte 5 &middot; Unir dos negaciones',
    a5T='Elige el nexo',
    a6E='Parte 6 &middot; ¿Ahora o siempre?',
    a6T='Elige la forma correcta',
    bankLabel='Banco de palabras:',

    v1p='el otoño',
    v2p='las hojas',
    v3p='la bufanda',
    v4p='brillante / luminoso',
    v5p='la bolera',
    v6p='la discoteca sobre patines',
    v7p='el desierto',
    v8p='la llanura',
    v9p='el campo / el prado',
    v10p='oxidado / color óxido',

    h1='Dos palabras para el bosque en octubre.',
    h2='Una prenda de ropa y una palabra para la luz fuerte.',
    h3='Dos sitios a los que van los chicos el fin de semana.',
    h4='Dos clases de terreno abierto: uno solo es seco, el otro solo es '
       'llano.',
    h5='Un trozo de tierra de labranza y un color.',

    h6='Fíjate primero en el sujeto de cada oración.',
    h7='Uno de estos sujetos es una sola cosa; el otro, un grupo.',

    resPerfect='Puntuación máxima. Sabes situar las cosas en una imagen, has '
               'escrito cada palabra partiendo solo del significado y '
               'distingues los dos presentes. Eso último es justo donde se '
               'tuerce casi todo en este nivel.',
    resStrong='Muy bien. Mira dónde están los fallos. Las expresiones de '
              'lugar y los sustantivos suelen quedarse a la primera; los '
              'tiempos verbales y los nexos hay que releerlos cada vez sobre '
              'oraciones reales.',
    resMid='Aprobado. Vuelve a las diapositivas sobre los dos presentes y '
           'sobre nor. Entre las dos se llevan un tercio de los puntos, y en '
           'ambas hay que elegir entre dos formas, no recordar una palabra.',
    resLow='Repasa las diapositivas de lengua antes de volver a intentarlo. '
           'Cada palabra y cada regla que se evalúa aquí está explicada en '
           'una diapositiva antes de las preguntas.',

    actTitle='Hawkins en otoño',
    actUse='Usa al menos cuatro:',
    actSpeakBrief='Sentaos de forma que solo una persona vea la pantalla: le '
                  'describes una fotografía a alguien que tiene que dibujarla.',
    actSpeak1='Describe la imagen de la portada &mdash; primer plano, centro, '
              'fondo y en qué lado está el animal. Tu compañero la dibuja sin '
              'mirar.',
    actSpeak2='Cambiad. Un minuto sobre una tarde de otoño en tu propia '
              'ciudad: los árboles, la luz, cómo va vestida la gente.',
    actSpeak3='Los dos: es viernes y no os ponéis de acuerdo. Defended la '
              '<em>bowling alley</em> frente a la <em>rollerdisco</em> y '
              'decid qué está pasando en cada sitio.',
    actWriteKind='Escritura &middot; 100&ndash;150 palabras',
    actWriteBrief='Escribe a un amigo que nunca ha estado en Hawkins. '
                  'Describe la fotografía que le mandas &mdash; di dónde está '
                  'cada cosa &mdash; y cuenta cómo es el pueblo en otoño y '
                  'qué está haciendo la gente allí ahora.',
    actPlaceholder='Dear Barb, I am sending you a photograph of the woods …',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT
                        else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
