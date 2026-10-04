# -*- coding: utf-8 -*-
"""Interface strings for The Mystery of Marilyn Monroe — Prepositions (B1).

English, German and Spanish. Teach cards use the six-item form, so the rule
travels with its heading; the example line under each card is English in
every language and carries no key, because it IS the English being taught.
Explanations are keys too (HOUSE-STYLE §7), so a B1 learner reads the reason
in their own language while the forms under discussion stay English, in
CAPS, with cited words in double quotes.

Not translated, deliberately: stems, options, gap sentences, word banks,
sort sentences, the model paragraph on the stage 2 panel and the activation
chips.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='The Mystery of <em>Marilyn Monroe</em>',
    coverSub='Prepositions of time, place and movement — and the words they always travel with',
    chipLevel='B1 · Intermediate', chipFocus='Prepositions', chipCount='26 slides',
    bankLabel='Word bank:',

    d1t='When It Happened', d1n='Stage 1 · AT, ON and IN for time',
    d2t='Where It Happened', d2n='Stage 2 · place and movement',
    d3t='Words That Travel Together', d3n='Stage 3 · fixed partners',
    e1='Time', e2='Place and movement', e3='Fixed partners',

    # ── stage 1 ──────────────────────────────────────────────────────
    s1t='Three small words, one life',
    s1a='Every date in her story needs a small word in front of it: AT, ON or IN. '
        'Which one depends on how big the piece of time is.',
    s2t='How big is the piece of time?',
    s2ah='AT · an exact point',
    s2ab='Clock times, ages and a few fixed phrases.',
    s2bh='ON · one day',
    s2bb='Dates, days of the week and one particular day.',
    s2ch='IN · a longer stretch',
    s2cb='Months, years, decades and parts of the day.',

    # ── stage 2 ──────────────────────────────────────────────────────
    s3t='Reading a picture',
    s3a='Here is a description of this close-up. Every word in bold says where '
        'something is, or which way it goes.',
    s4t='Where is it?',
    s4ah='IN · inside a space',
    s4ab='Rooms, buildings, cities and countries.',
    s4bh='ON · a surface or a street',
    s4bb='Covers, pages, screens, and the street something is on.',
    s4ch='AT · a point or a level',
    s4cb='A point on a map, an event, or a level in an organisation.',
    s5t='Which way does it go?',
    s5ah='OVER · higher than',
    s5ab='Directly above something, often covering it.',
    s5bh='THROUGH · in one side, out the other',
    s5bb='Movement through a space — or through a hard time, from start to end.',
    s5ch='UNDER · lower than',
    s5cb='Directly below something, often hidden by it.',

    # ── stage 3 ──────────────────────────────────────────────────────
    s6t='Some words come with a partner',
    s6a='Many verbs, nouns and adjectives take one fixed preposition. There is '
        'no rule to work out: you learn them as pairs.',
    s6b='Learn the pair, not the word: FAMOUS FOR, not just "famous".',
    s7t='Partners · 1',
    s7ah='FAMOUS FOR + the reason',
    s7ab='What made someone well known.',
    s7bh='KNOW ABOUT + a topic',
    s7bb='Information on a subject. To KNOW a person takes no preposition.',
    s7ch='DIE FROM / DIE OF + the cause',
    s7cb='The cause of death. DIE FOR means giving your life for a cause.',
    s8t='Partners · 2',
    s8ah='SIGN A CONTRACT WITH',
    s8ab='WITH names the other side of the deal.',
    s8bh='KEEP someone OUT OF',
    s8bb='Stop someone from being part of something.',
    s8ch='A FILE ON + a person',
    s8cb='A file about someone, the way police and spies keep them.',
    s8dh='MARRY someone · MARRIED TO',
    s8db='No preposition after MARRY. After MARRIED, use TO, never WITH.',

    mcT='Choose the right word',
    gapT='Complete the sentences',
    gapHint='Type one word in each gap. The word bank has more words than you need.',
    sortT='Correct, or not?',
    sortHint='Drag each sentence into a box. Four of the eight are wrong.',
    binOk='Correct', binBad='Incorrect',

    # ── explanations ─────────────────────────────────────────────────
    q1w='A date is one single day, so ON: ON 1 June 1926, ON Monday. IN is for '
        'months and years; AT is for clock times.',
    q2w='"The early hours" is a part of the day, like "the morning", so IN: IN the '
        'morning, IN the early hours. But AT night.',
    q3w='A month is a longer stretch of time, so IN: IN January, IN 1954. ON is '
        'only for one day: ON 14 January 1954.',
    q8w='OVER means directly above. She stood OVER the grate, so the air from the train below blew her dress up.',
    q4w='Ages take AT: AT the age of thirty-six, or simply AT thirty-six.',
    q5w='You sign a contract WITH the other side of the deal: WITH a studio, WITH '
        'a company.',
    q6w='KEEP someone OUT OF something means stopping them from being part of it.',
    q7w='A file ON a person is a file about them. That is how police and spies '
        'use the word.',
    g1w1='Rooms take IN: IN her bedroom, IN the kitchen.',
    g1w2='A cover is a surface, so ON: ON the cover, ON page 5, ON the screen.',
    g2w1='Streets take ON: ON Lexington Avenue. Cities take IN: IN New York.',
    g2w2='The train ran UNDER the street, and the air came up THROUGH the grate: '
         'in one side and out the other.',
    g3w1='A level in an organisation takes AT: AT the highest levels, AT the top.',
    g3w2='THROUGH a period means from its start to its end, usually a hard one: '
         'live THROUGH a war, go THROUGH a divorce.',
    sortWhy='FAMOUS FOR, KNOW ABOUT, DIE FROM, A FILE ON, MARRY someone. "By", '
            '"at", "for" and "married with" are the usual slips.',

    # ── activation ───────────────────────────────────────────────────
    actTitle='Your turn',
    actUse='Use at least three:',
    actSpeakBrief='Sixty years on, people still argue about her. Talk it through.',
    actSpeak1='Tell your partner the life of a famous person in one minute — '
              'born, moved, married, died. Put AT, ON or IN in front of every date.',
    actSpeak2='Choose a famous film scene. Describe it so exactly that your '
              'partner could draw it: what is over, under, across and through what.',
    actSpeak3='Accident or cover-up? Argue for one explanation of a famous mystery. '
              'Say who knew about what, and who wanted to keep whom out of what.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='A gallery is showing the portrait from this lesson. Write the '
                  'label for the wall: describe the picture for a visitor who '
                  'cannot see it well, then tell her story in three dates.',
    actPlaceholder='Write your label here…',

    resPerfect='Perfect. Time, place and every fixed partner.',
    resStrong='Strong work. Look again at the partner cards: that is where the last points usually go.',
    resMid='The time words are there. Now practise the pairs: FAMOUS FOR, KNOW ABOUT, DIE FROM.',
    resLow='Go back to Stage 1 and ask one question each time: how big is the piece of time?',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Das Rätsel um <em>Marilyn Monroe</em>',
    coverSub='Präpositionen der Zeit, des Ortes und der Bewegung — und die Wörter, mit denen sie immer zusammen auftreten',
    chipLevel='B1 · Mittelstufe', chipFocus='Präpositionen', chipCount='26 Folien',
    bankLabel='Wortspeicher:',

    d1t='Wann es geschah', d1n='Teil 1 · AT, ON und IN für Zeit',
    d2t='Wo es geschah', d2n='Teil 2 · Ort und Bewegung',
    d3t='Wörter, die zusammengehören', d3n='Teil 3 · feste Partner',
    e1='Zeit', e2='Ort und Bewegung', e3='Feste Partner',

    s1t='Drei kleine Wörter, ein Leben',
    s1a='Jedes Datum in ihrer Geschichte braucht ein kleines Wort davor: AT, ON '
        'oder IN. Welches, hängt davon ab, wie groß das Stück Zeit ist.',
    s2t='Wie groß ist das Stück Zeit?',
    s2ah='AT · ein genauer Punkt',
    s2ab='Uhrzeiten, das Alter und ein paar feste Wendungen.',
    s2bh='ON · ein Tag',
    s2bb='Daten, Wochentage und ein bestimmter Tag.',
    s2ch='IN · ein längerer Zeitraum',
    s2cb='Monate, Jahre, Jahrzehnte und Tageszeiten.',

    s3t='Ein Bild lesen',
    s3a='Hier ist eine Beschreibung dieser Nahaufnahme. Jedes fett gedruckte Wort '
        'sagt, wo etwas ist oder in welche Richtung es geht.',
    s4t='Wo ist es?',
    s4ah='IN · in einem Raum',
    s4ab='Zimmer, Gebäude, Städte und Länder.',
    s4bh='ON · auf einer Fläche oder Straße',
    s4bb='Titelseiten, Buchseiten, Bildschirme und die Straße, an der etwas liegt.',
    s4ch='AT · ein Punkt oder eine Ebene',
    s4cb='Ein Punkt auf der Karte, eine Veranstaltung oder eine Ebene in einer Organisation.',
    s5t='In welche Richtung geht es?',
    s5ah='OVER · höher als',
    s5ab='Direkt über etwas, oft so, dass es dieses bedeckt.',
    s5bh='THROUGH · auf einer Seite hinein, auf der anderen hinaus',
    s5bb='Bewegung durch einen Raum — oder durch eine schwere Zeit, vom Anfang bis zum Ende.',
    s5ch='UNDER · tiefer als',
    s5cb='Direkt unter etwas, oft davon verdeckt.',

    s6t='Manche Wörter haben einen Partner',
    s6a='Viele Verben, Nomen und Adjektive haben eine feste Präposition. Es gibt '
        'keine Regel dafür: Man lernt sie als Paare.',
    s6b='Lerne das Paar, nicht das Wort: FAMOUS FOR, nicht nur "famous".',
    s7t='Partner · 1',
    s7ah='FAMOUS FOR + der Grund',
    s7ab='Wofür jemand bekannt ist.',
    s7bh='KNOW ABOUT + ein Thema',
    s7bb='Wissen über ein Thema. Eine Person KNOW (kennen) braucht keine Präposition.',
    s7ch='DIE FROM / DIE OF + die Ursache',
    s7cb='Die Todesursache. DIE FOR heißt, sein Leben für eine Sache zu geben.',
    s8t='Partner · 2',
    s8ah='SIGN A CONTRACT WITH',
    s8ab='WITH nennt die andere Seite des Vertrags.',
    s8bh='KEEP someone OUT OF',
    s8bb='Jemanden davon abhalten, an etwas beteiligt zu sein.',
    s8ch='A FILE ON + eine Person',
    s8cb='Eine Akte über jemanden, so wie Polizei und Geheimdienste sie führen.',
    s8dh='MARRY someone · MARRIED TO',
    s8db='Nach MARRY steht keine Präposition. Nach MARRIED steht TO, nie WITH.',

    mcT='Wähle das richtige Wort',
    gapT='Vervollständige die Sätze',
    gapHint='Schreibe ein Wort in jede Lücke. Der Wortspeicher hat mehr Wörter, als du brauchst.',
    sortT='Richtig oder nicht?',
    sortHint='Ziehe jeden Satz in ein Feld. Vier der acht sind falsch.',
    binOk='Richtig', binBad='Falsch',

    q1w='Ein Datum ist ein einzelner Tag, also ON: ON 1 June 1926, ON Monday. IN '
        'steht bei Monaten und Jahren, AT bei Uhrzeiten.',
    q2w='"The early hours" ist eine Tageszeit wie "the morning", also IN: IN the '
        'morning, IN the early hours. Aber: AT night.',
    q3w='Ein Monat ist ein längerer Zeitraum, also IN: IN January, IN 1954. ON '
        'steht nur bei einem einzelnen Tag: ON 14 January 1954.',
    q8w='OVER heißt direkt über. Sie stand OVER dem Gitter, also blies die Luft vom Zug darunter ihr Kleid nach oben.',
    q4w='Beim Alter steht AT: AT the age of thirty-six oder einfach AT thirty-six.',
    q5w='Man schließt einen Vertrag WITH der anderen Seite: WITH a studio, WITH a company.',
    q6w='KEEP someone OUT OF something heißt, jemanden davon abzuhalten, Teil davon zu sein.',
    q7w='A file ON a person ist eine Akte über diese Person. So verwenden Polizei '
        'und Geheimdienste das Wort.',
    g1w1='Zimmer haben IN: IN her bedroom, IN the kitchen.',
    g1w2='Eine Titelseite ist eine Fläche, also ON: ON the cover, ON page 5, ON the screen.',
    g2w1='Straßen haben ON: ON Lexington Avenue. Städte haben IN: IN New York.',
    g2w2='Der Zug fuhr UNDER der Straße, und die Luft kam THROUGH das Gitter nach '
         'oben: auf einer Seite hinein, auf der anderen hinaus.',
    g3w1='Eine Ebene in einer Organisation hat AT: AT the highest levels, AT the top.',
    g3w2='THROUGH bei einem Zeitraum heißt vom Anfang bis zum Ende, meist bei '
         'einer schweren Zeit: live THROUGH a war, go THROUGH a divorce.',
    sortWhy='FAMOUS FOR, KNOW ABOUT, DIE FROM, A FILE ON, MARRY someone. "By", '
            '"at", "for" und "married with" sind die typischen Fehler.',

    actTitle='Jetzt du',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Sechzig Jahre später wird immer noch über sie gestritten. Sprecht darüber.',
    actSpeak1='Erzähle deinem Gegenüber in einer Minute das Leben einer berühmten '
              'Person — Geburt, Umzug, Hochzeit, Tod. Setze vor jedes Datum AT, ON oder IN.',
    actSpeak2='Wähle eine berühmte Filmszene. Beschreibe sie so genau, dass dein '
              'Gegenüber sie zeichnen könnte: Was ist über, unter, quer über und durch was?',
    actSpeak3='Unfall oder Vertuschung? Vertritt eine Erklärung für ein berühmtes '
              'Rätsel. Sag, wer was wusste und wer wen woraus heraushalten wollte.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Eine Galerie zeigt das Porträt aus dieser Lektion. Schreibe das '
                  'Schild für die Wand: Beschreibe das Bild für jemanden, der es '
                  'schlecht sehen kann, und erzähle dann ihre Geschichte in drei Daten.',
    actPlaceholder='Schreibe hier dein Schild…',

    resPerfect='Perfekt. Zeit, Ort und alle festen Partner.',
    resStrong='Starke Leistung. Sieh dir die Partner-Karten noch einmal an: Dort gehen meist die letzten Punkte verloren.',
    resMid='Die Zeitwörter sitzen. Übe jetzt die Paare: FAMOUS FOR, KNOW ABOUT, DIE FROM.',
    resLow='Geh zurück zu Teil 1 und frag jedes Mal: Wie groß ist das Stück Zeit?',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='El misterio de <em>Marilyn Monroe</em>',
    coverSub='Preposiciones de tiempo, lugar y movimiento — y las palabras que siempre las acompañan',
    chipLevel='B1 · Intermedio', chipFocus='Preposiciones', chipCount='26 diapositivas',
    bankLabel='Banco de palabras:',

    d1t='Cuándo ocurrió', d1n='Etapa 1 · AT, ON e IN para el tiempo',
    d2t='Dónde ocurrió', d2n='Etapa 2 · lugar y movimiento',
    d3t='Palabras que van juntas', d3n='Etapa 3 · compañeras fijas',
    e1='Tiempo', e2='Lugar y movimiento', e3='Compañeras fijas',

    s1t='Tres palabras pequeñas, una vida',
    s1a='Cada fecha de su historia necesita una palabra pequeña delante: AT, ON o '
        'IN. Cuál depende de lo grande que sea ese trozo de tiempo.',
    s2t='¿Qué tamaño tiene el trozo de tiempo?',
    s2ah='AT · un punto exacto',
    s2ab='Horas, edades y algunas expresiones fijas.',
    s2bh='ON · un día',
    s2bb='Fechas, días de la semana y un día concreto.',
    s2ch='IN · un periodo más largo',
    s2cb='Meses, años, décadas y partes del día.',

    s3t='Leer una imagen',
    s3a='Esta es una descripción de este primer plano. Cada palabra en negrita '
        'dice dónde está algo o hacia dónde va.',
    s4t='¿Dónde está?',
    s4ah='IN · dentro de un espacio',
    s4ab='Habitaciones, edificios, ciudades y países.',
    s4bh='ON · una superficie o una calle',
    s4bb='Portadas, páginas, pantallas y la calle en la que está algo.',
    s4ch='AT · un punto o un nivel',
    s4cb='Un punto en el mapa, un evento o un nivel dentro de una organización.',
    s5t='¿Hacia dónde va?',
    s5ah='OVER · más arriba que',
    s5ab='Justo encima de algo, a menudo cubriéndolo.',
    s5bh='THROUGH · entra por un lado y sale por el otro',
    s5bb='Movimiento a través de un espacio — o de una etapa difícil, de principio a fin.',
    s5ch='UNDER · más abajo que',
    s5cb='Justo debajo de algo, a menudo tapado por ello.',

    s6t='Algunas palabras tienen pareja',
    s6a='Muchos verbos, sustantivos y adjetivos llevan una preposición fija. No '
        'hay ninguna regla que deducir: se aprenden por parejas.',
    s6b='Aprende la pareja, no la palabra: FAMOUS FOR, no solo "famous".',
    s7t='Parejas · 1',
    s7ah='FAMOUS FOR + el motivo',
    s7ab='Por qué alguien es conocido.',
    s7bh='KNOW ABOUT + un tema',
    s7bb='Saber sobre un tema. KNOW a una persona (conocerla) no lleva preposición.',
    s7ch='DIE FROM / DIE OF + la causa',
    s7cb='La causa de la muerte. DIE FOR significa dar la vida por una causa.',
    s8t='Parejas · 2',
    s8ah='SIGN A CONTRACT WITH',
    s8ab='WITH nombra a la otra parte del acuerdo.',
    s8bh='KEEP someone OUT OF',
    s8bb='Impedir que alguien forme parte de algo.',
    s8ch='A FILE ON + una persona',
    s8cb='Un expediente sobre alguien, como los que guardan la policía y los espías.',
    s8dh='MARRY someone · MARRIED TO',
    s8db='Después de MARRY no va preposición. Después de MARRIED va TO, nunca WITH.',

    mcT='Elige la palabra correcta',
    gapT='Completa las frases',
    gapHint='Escribe una palabra en cada hueco. El banco tiene más palabras de las que necesitas.',
    sortT='¿Correcta o no?',
    sortHint='Arrastra cada frase a una caja. Cuatro de las ocho son incorrectas.',
    binOk='Correcta', binBad='Incorrecta',

    q1w='Una fecha es un solo día, así que ON: ON 1 June 1926, ON Monday. IN va '
        'con meses y años; AT, con las horas.',
    q2w='"The early hours" es una parte del día, como "the morning", así que IN: '
        'IN the morning, IN the early hours. Pero AT night.',
    q3w='Un mes es un periodo más largo, así que IN: IN January, IN 1954. ON es '
        'solo para un día: ON 14 January 1954.',
    q8w='OVER significa justo encima. Estaba OVER la rejilla, así que el aire del tren de abajo le levantó el vestido.',
    q4w='Con la edad se usa AT: AT the age of thirty-six, o simplemente AT thirty-six.',
    q5w='Un contrato se firma WITH la otra parte del acuerdo: WITH a studio, WITH a company.',
    q6w='KEEP someone OUT OF something significa impedir que esa persona forme parte de algo.',
    q7w='A file ON a person es un expediente sobre esa persona. Así usan la '
        'palabra la policía y los espías.',
    g1w1='Las habitaciones llevan IN: IN her bedroom, IN the kitchen.',
    g1w2='Una portada es una superficie, así que ON: ON the cover, ON page 5, ON the screen.',
    g2w1='Las calles llevan ON: ON Lexington Avenue. Las ciudades, IN: IN New York.',
    g2w2='El tren pasaba UNDER la calle y el aire subía THROUGH la rejilla: entra '
         'por un lado y sale por el otro.',
    g3w1='Un nivel dentro de una organización lleva AT: AT the highest levels, AT the top.',
    g3w2='THROUGH con un periodo significa de principio a fin, normalmente uno '
         'difícil: live THROUGH a war, go THROUGH a divorce.',
    sortWhy='FAMOUS FOR, KNOW ABOUT, DIE FROM, A FILE ON, MARRY someone. "By", '
            '"at", "for" y "married with" son los errores típicos.',

    actTitle='Te toca',
    actUse='Usa al menos tres:',
    actSpeakBrief='Sesenta años después, todavía se discute sobre ella. Habladlo.',
    actSpeak1='Cuéntale a tu compañero la vida de una persona famosa en un minuto '
              '— nacimiento, mudanza, boda, muerte. Pon AT, ON o IN delante de cada fecha.',
    actSpeak2='Elige una escena de cine famosa. Descríbela con tanta precisión que '
              'tu compañero pueda dibujarla: qué está encima, debajo, de un lado a '
              'otro y a través de qué.',
    actSpeak3='¿Accidente o encubrimiento? Defiende una explicación de un misterio '
              'famoso. Di quién sabía qué y quién quería mantener a quién fuera de qué.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Una galería expone el retrato de esta lección. Escribe la '
                  'cartela de la pared: describe la imagen para alguien que no la '
                  've bien y luego cuenta su historia en tres fechas.',
    actPlaceholder='Escribe aquí tu cartela…',

    resPerfect='Perfecto. Tiempo, lugar y todas las parejas fijas.',
    resStrong='Muy bien. Repasa las tarjetas de parejas: ahí suelen irse los últimos puntos.',
    resMid='Las palabras de tiempo ya están. Ahora practica las parejas: FAMOUS FOR, KNOW ABOUT, DIE FROM.',
    resLow='Vuelve a la Etapa 1 y pregúntate cada vez: ¿qué tamaño tiene el trozo de tiempo?',
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
