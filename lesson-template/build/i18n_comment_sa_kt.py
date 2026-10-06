# -*- coding: utf-8 -*-
"""Interface strings for Have Your Say 3 — Key Topics: South Africa (B1-B2).

English, German and Spanish. What translates: the chrome, the slide titles,
the definitions on the key-word cards, every explanation, the task
instructions. What does not, deliberately (HOUSE-STYLE §8): the reading
panels, which ARE the English the class test is written in and which the
questions test; stems, options, gap sentences, the word bank, the sort and
order pieces, the English example under each card, and the activation chips.

Explanations put the words under discussion in CAPS and cite in double
quotes, as the other decks do.

coverSub is also the page's meta description and its line on the vocabulary
hub: tools/seo.py takes the first coverSub it finds (English) and strips the
tags WITHOUT adding a space, so each <br> has a space in front of it. The
breaks keep the subtitle inside the gap between the heart and the map.
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
    coverTitle='Key Topics:<br><em>South Africa</em>',
    coverSub='Independence, apartheid, Nelson Mandela, <br>the Rainbow Nation and South Africa today — <br>five topics for your class-test comment',
    chipLevel='B1–B2', chipFocus='History · society', chipCount='35 slides',
    bankLabel='Word bank:',

    d1t='From Empire to Republic', d1n='Stage 1 · independence',
    d2t='Apartheid and Mandela', d2n='Stage 2 · 1948 to 1994',
    d3t='The Rainbow Nation', d3n='Stage 3 · South Africa today',
    d4t='Putting It Together', d4n='Stage 4 · the key connection',
    d5t='The Whole Story', d5n='Revision · one page',

    e1='Independence', e2='Apartheid', e2b='Nelson Mandela',
    e3='The Rainbow Nation', e3b='South Africa today', e4='The key connection',
    eW='Key words',

    s1t='A country inside an empire',
    s2t='Independent, but not free',
    s3t='A system of separation',
    s4t='How apartheid ended',
    s5t='Prisoner, then president',
    s6t='Why he still matters',
    s7t='Many peoples, one nation',
    s8t='An ideal, not yet a fact',
    s9t='Progress and challenges',

    w1t='Words for a new state',
    w1b1='A country that governs itself but still belongs to an empire, with the British monarch as head of state.',
    w1b2='A country whose head of state is a president, not a king or queen.',
    w1b3='A group of countries, most of them once in the British Empire, that still work together.',
    w2t='Words for apartheid and after',
    w2b1='Keeping groups of people apart by law, for example by race.',
    w2b2='Treating a person or a group worse than others because of who they are.',
    w2b3='Two sides making peace and learning to live together after a conflict.',
    w2b4='An unfair difference between groups — in money, jobs or chances in life.',

    mcT='Choose the right answer',
    gapT='Complete the sentences',
    gapHint='Type one word in each gap. The word bank has more words than you need.',
    sortT='Before or after 1994?',
    sortHint='Drag each sentence into the right box.',
    binA='Under apartheid (1948–1994)', binB='Since 1994',
    orderT='Five events in order',
    orderHint='Click the pieces to tell the story, oldest event first. Click a piece again to take it back.',

    # ── explanations ─────────────────────────────────────────────────
    q1w='In 1910 South Africa became a self-governing DOMINION: it ran its own affairs but was still inside the British Empire. It became a REPUBLIC only in 1961.',
    q2w='1961 is the year of the REPUBLIC: South Africa stopped having the British monarch as head of state and left the Commonwealth.',
    q3w='Apartheid had been law since 1948. In 1961 the country was independent, but most of its people still had no vote and few rights.',
    q4w='Apartheid became official policy in 1948, after the National Party won the election. It lasted until the free election of 1994.',
    q5w='Apartheid controlled daily life, not just politics: where people could live, which schools they went to, which jobs they could do and where they could travel.',
    q6w='Mandela was in prison for 27 years, from 1962 until his release in 1990.',
    q7w='Mandela negotiated the end of apartheid with President F. W. de Klerk. In 1993 the two men shared the Nobel Peace Prize.',
    q8w='After the first democratic election, in 1994, Mandela became South Africa’s first Black president. He served until 1999.',
    q9w='The "Rainbow Nation" describes South Africa as one country of many cultures, peoples and languages, living together despite their differences.',
    q10w='South Africa has 12 official languages, among them Zulu, Xhosa, Afrikaans, English and South African Sign Language.',
    q11w='Democracy is in place and apartheid laws are gone. What remains is INEQUALITY: poverty, unemployment and unequal chances, many of them a result of apartheid.',
    q12w='Independence (1910, 1961) gave South Africa self-government. Freedom and equality for everyone came only with the end of apartheid in 1994.',
    g1w1='Apartheid kept races apart by law: racial SEGREGATION. "Discrimination" is also correct here.',
    g1w2='RECONCILIATION means making peace after a conflict. Mandela chose it over revenge.',
    g1w3='In 1961 South Africa became a REPUBLIC. It had been a DOMINION since 1910.',
    g2w1='The gap between rich and poor is economic INEQUALITY. "Poverty" means being poor; it is not a gap.',
    g2w2='Treating people worse because of their race is DISCRIMINATION.',
    g2w3='Many cultures and languages: a DIVERSE population.',
    sortWhy='Classification by race, no vote for Black South Africans, laws on where people could live, and segregated schools and beaches were apartheid. Votes for all, the 1996 constitution, 12 official languages and Mandela’s presidency came after 1994.',
    orderWhy='1910 the Union of South Africa · 1948 apartheid becomes law · 1961 the republic · 1990 Mandela is released · 1994 the first election open to all races.',

    # ── activation ───────────────────────────────────────────────────
    actTitle='Your turn',
    actUse='Use at least three:',
    actSpeakBrief='Prepare for the test by explaining it out loud. Work with a partner.',
    actSpeak1='A friend says: "South Africa became free in 1961." Correct them politely, and explain what really changed in 1961 and what changed in 1994.',
    actSpeak2='You have one minute to present Nelson Mandela to a class that has never heard of him: what he did, when, and why the world still remembers him.',
    actSpeak3='Is the Rainbow Nation a reality or still a dream? Take a side and give two reasons from South Africa today. Your partner argues the other side.',
    actWriteKind='Writing · 150–250 words',
    actWriteBrief='The test asks you to comment on "Independence gave all South Africans freedom." Write an introduction that names the statement, two or three main paragraphs using at least two key topics, and a conclusion with your opinion.',
    actPlaceholder='In this comment, I want to give my opinion on the statement…',

    resPerfect='Perfect. You know all five topics — you are ready to write.',
    resStrong='Very good. Look again at the dates: 1910, 1948, 1961, 1990, 1994.',
    resMid='A good start. Go back to Stage 1: independence and freedom are not the same thing.',
    resLow='Read the panels again, slowly, then try the questions a second time.',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Kernthemen:<br><em>Südafrika</em>',
    coverSub='Unabhängigkeit, Apartheid, Nelson Mandela, <br>die Regenbogennation und Südafrika heute — <br>fünf Themen für deinen Kommentar',
    chipLevel='B1–B2', chipFocus='Geschichte · Gesellschaft', chipCount='35 Folien',
    bankLabel='Wortliste:',

    d1t='Vom Empire zur Republik', d1n='Etappe 1 · Unabhängigkeit',
    d2t='Apartheid und Mandela', d2n='Etappe 2 · 1948 bis 1994',
    d3t='Die Regenbogennation', d3n='Etappe 3 · Südafrika heute',
    d4t='Alles zusammen', d4n='Etappe 4 · der rote Faden',
    d5t='Die ganze Geschichte', d5n='Wiederholung · eine Seite',

    e1='Unabhängigkeit', e2='Apartheid', e2b='Nelson Mandela',
    e3='Die Regenbogennation', e3b='Südafrika heute', e4='Der rote Faden',
    eW='Schlüsselwörter',

    s1t='Ein Land innerhalb eines Weltreichs',
    s2t='Unabhängig, aber nicht frei',
    s3t='Ein System der Trennung',
    s4t='Wie die Apartheid endete',
    s5t='Erst Gefangener, dann Präsident',
    s6t='Warum er bis heute wichtig ist',
    s7t='Viele Völker, eine Nation',
    s8t='Ein Ideal, noch keine Tatsache',
    s9t='Fortschritte und Herausforderungen',

    w1t='Wörter für einen neuen Staat',
    w1b1='Ein Land, das sich selbst regiert, aber noch zu einem Weltreich gehört; Staatsoberhaupt ist der britische Monarch.',
    w1b2='Ein Land, dessen Staatsoberhaupt ein Präsident ist, kein König und keine Königin.',
    w1b3='Eine Gemeinschaft von Ländern, die meist einmal zum Britischen Weltreich gehörten und bis heute zusammenarbeiten.',
    w2t='Wörter für die Apartheid und danach',
    w2b1='Menschengruppen per Gesetz voneinander trennen, zum Beispiel nach Hautfarbe.',
    w2b2='Einen Menschen oder eine Gruppe schlechter behandeln als andere, weil sie sind, wer sie sind.',
    w2b3='Zwei Seiten schließen nach einem Konflikt Frieden und lernen, miteinander zu leben.',
    w2b4='Ein ungerechter Unterschied zwischen Gruppen — bei Geld, Arbeit oder Lebenschancen.',

    mcT='Wähle die richtige Antwort',
    gapT='Ergänze die Sätze',
    gapHint='Schreib ein Wort in jede Lücke. Die Wortliste hat mehr Wörter, als du brauchst.',
    sortT='Vor oder nach 1994?',
    sortHint='Zieh jeden Satz in das richtige Feld.',
    binA='Unter der Apartheid (1948–1994)', binB='Seit 1994',
    orderT='Fünf Ereignisse in der richtigen Reihenfolge',
    orderHint='Klick die Teile an und erzähl die Geschichte, das älteste Ereignis zuerst. Ein zweiter Klick nimmt ein Teil zurück.',

    q1w='1910 wurde Südafrika ein sich selbst regierendes DOMINION: Es verwaltete sich selbst, blieb aber Teil des Britischen Weltreichs. Eine REPUBLIC wurde es erst 1961.',
    q2w='1961 ist das Jahr der REPUBLIC: Der britische Monarch war nicht mehr Staatsoberhaupt, und Südafrika trat aus dem Commonwealth aus.',
    q3w='Die Apartheid war seit 1948 Gesetz. 1961 war das Land unabhängig, aber die meisten Menschen hatten noch immer kein Wahlrecht und kaum Rechte.',
    q4w='Die Apartheid wurde 1948 offizielle Politik, nachdem die National Party die Wahl gewonnen hatte. Sie dauerte bis zur freien Wahl 1994.',
    q5w='Die Apartheid bestimmte den Alltag, nicht nur die Politik: wo man wohnen durfte, welche Schule man besuchte, welche Arbeit man machen und wohin man reisen durfte.',
    q6w='Mandela war 27 Jahre im Gefängnis, von 1962 bis zu seiner Freilassung 1990.',
    q7w='Mandela verhandelte das Ende der Apartheid mit Präsident F. W. de Klerk. 1993 erhielten die beiden gemeinsam den Friedensnobelpreis.',
    q8w='Nach der ersten demokratischen Wahl 1994 wurde Mandela Südafrikas erster schwarzer Präsident. Er blieb bis 1999 im Amt.',
    q9w='Die "Rainbow Nation" beschreibt Südafrika als ein Land vieler Kulturen, Völker und Sprachen, die trotz ihrer Unterschiede zusammenleben.',
    q10w='Südafrika hat 12 Amtssprachen, darunter Zulu, Xhosa, Afrikaans, Englisch und die Südafrikanische Gebärdensprache.',
    q11w='Die Demokratie besteht, die Apartheidgesetze sind abgeschafft. Geblieben ist die INEQUALITY: Armut, Arbeitslosigkeit und ungleiche Chancen, viele davon eine Folge der Apartheid.',
    q12w='Die Unabhängigkeit (1910, 1961) brachte Südafrika die Selbstregierung. Freiheit und Gleichheit für alle kamen erst mit dem Ende der Apartheid 1994.',
    g1w1='Die Apartheid trennte die Menschen per Gesetz nach Hautfarbe: racial SEGREGATION. "Discrimination" ist hier auch richtig.',
    g1w2='RECONCILIATION heißt Versöhnung nach einem Konflikt. Mandela wählte sie statt Rache.',
    g1w3='1961 wurde Südafrika eine REPUBLIC. Seit 1910 war es ein DOMINION gewesen.',
    g2w1='Die Kluft zwischen Arm und Reich ist economic INEQUALITY. "Poverty" heißt Armut; das ist keine Kluft.',
    g2w2='Menschen wegen ihrer Hautfarbe schlechter zu behandeln ist DISCRIMINATION.',
    g2w3='Viele Kulturen und Sprachen: eine DIVERSE Bevölkerung.',
    sortWhy='Einteilung nach Hautfarbe, kein Wahlrecht für Schwarze, Gesetze über Wohnorte sowie getrennte Schulen und Strände: das war die Apartheid. Wahlrecht für alle, die Verfassung von 1996, 12 Amtssprachen und Mandelas Präsidentschaft kamen nach 1994.',
    orderWhy='1910 die Südafrikanische Union · 1948 die Apartheid wird Gesetz · 1961 die Republik · 1990 Mandela kommt frei · 1994 die erste Wahl für alle.',

    actTitle='Jetzt du',
    actUse='Benutze mindestens drei:',
    actSpeakBrief='Bereite dich auf die Arbeit vor, indem du es laut erklärst. Arbeite mit einem Partner.',
    actSpeak1='Jemand sagt: "Südafrika wurde 1961 frei." Korrigiere die Person höflich und erkläre, was sich 1961 wirklich geändert hat und was 1994.',
    actSpeak2='Du hast eine Minute, um Nelson Mandela einer Klasse vorzustellen, die nie von ihm gehört hat: was er tat, wann, und warum die Welt sich an ihn erinnert.',
    actSpeak3='Ist die Regenbogennation Wirklichkeit oder noch ein Traum? Bezieh Stellung und nenne zwei Gründe aus dem heutigen Südafrika. Dein Partner vertritt die Gegenseite.',
    actWriteKind='Schreiben · 150–250 Wörter',
    actWriteBrief='Kommentiere "Independence gave all South Africans freedom." Schreib eine Einleitung, die die Aussage nennt, zwei oder drei Hauptabsätze mit mindestens zwei Kernthemen und einen Schluss mit deiner Meinung.',
    actPlaceholder='In this comment, I want to give my opinion on the statement…',

    resPerfect='Perfekt. Du kennst alle fünf Themen — du bist bereit zum Schreiben.',
    resStrong='Sehr gut. Schau dir die Jahreszahlen noch einmal an: 1910, 1948, 1961, 1990, 1994.',
    resMid='Ein guter Anfang. Geh zurück zu Etappe 1: Unabhängigkeit und Freiheit sind nicht dasselbe.',
    resLow='Lies die Texte noch einmal langsam und versuch die Fragen dann ein zweites Mal.',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Temas clave:<br><em>Sudáfrica</em>',
    coverSub='Independencia, apartheid, Nelson Mandela, <br>la Nación Arcoíris y la Sudáfrica de hoy: <br>cinco temas para tu comentario',
    chipLevel='B1–B2', chipFocus='Historia · sociedad', chipCount='35 diapositivas',
    bankLabel='Banco de palabras:',

    d1t='Del Imperio a la República', d1n='Etapa 1 · la independencia',
    d2t='El apartheid y Mandela', d2n='Etapa 2 · de 1948 a 1994',
    d3t='La Nación Arcoíris', d3n='Etapa 3 · Sudáfrica hoy',
    d4t='Todo junto', d4n='Etapa 4 · la conexión clave',
    d5t='Toda la historia', d5n='Repaso · una página',

    e1='La independencia', e2='El apartheid', e2b='Nelson Mandela',
    e3='La Nación Arcoíris', e3b='Sudáfrica hoy', e4='La conexión clave',
    eW='Palabras clave',

    s1t='Un país dentro de un imperio',
    s2t='Independiente, pero no libre',
    s3t='Un sistema de separación',
    s4t='Cómo terminó el apartheid',
    s5t='Primero preso, después presidente',
    s6t='Por qué sigue siendo importante',
    s7t='Muchos pueblos, una nación',
    s8t='Un ideal, todavía no un hecho',
    s9t='Avances y retos',

    w1t='Palabras para un nuevo Estado',
    w1b1='Un país que se gobierna a sí mismo pero sigue perteneciendo a un imperio, con el monarca británico como jefe de Estado.',
    w1b2='Un país cuyo jefe de Estado es un presidente, no un rey ni una reina.',
    w1b3='Un grupo de países, casi todos antiguos miembros del Imperio británico, que siguen colaborando.',
    w2t='Palabras para el apartheid y después',
    w2b1='Separar a grupos de personas por ley, por ejemplo por su raza.',
    w2b2='Tratar a una persona o a un grupo peor que a otros por ser quienes son.',
    w2b3='Dos partes que hacen las paces y aprenden a convivir después de un conflicto.',
    w2b4='Una diferencia injusta entre grupos — en dinero, trabajo u oportunidades.',

    mcT='Elige la respuesta correcta',
    gapT='Completa las frases',
    gapHint='Escribe una palabra en cada hueco. El banco tiene más palabras de las que necesitas.',
    sortT='¿Antes o después de 1994?',
    sortHint='Arrastra cada frase a la casilla correcta.',
    binA='Bajo el apartheid (1948–1994)', binB='Desde 1994',
    orderT='Cinco hechos en orden',
    orderHint='Haz clic en las piezas para contar la historia, del hecho más antiguo al más reciente. Otro clic devuelve la pieza.',

    q1w='En 1910 Sudáfrica se convirtió en un DOMINION autónomo: se gobernaba a sí misma, pero seguía dentro del Imperio británico. Solo en 1961 pasó a ser una REPUBLIC.',
    q2w='1961 es el año de la REPUBLIC: el monarca británico dejó de ser jefe de Estado y Sudáfrica salió de la Commonwealth.',
    q3w='El apartheid era ley desde 1948. En 1961 el país era independiente, pero la mayoría de su gente seguía sin voto y casi sin derechos.',
    q4w='El apartheid pasó a ser política oficial en 1948, cuando el National Party ganó las elecciones. Duró hasta las elecciones libres de 1994.',
    q5w='El apartheid controlaba la vida diaria, no solo la política: dónde se podía vivir, a qué escuela se iba, qué trabajos se podían hacer y adónde se podía viajar.',
    q6w='Mandela estuvo 27 años en prisión, desde 1962 hasta su liberación en 1990.',
    q7w='Mandela negoció el fin del apartheid con el presidente F. W. de Klerk. En 1993 ambos compartieron el Premio Nobel de la Paz.',
    q8w='Tras las primeras elecciones democráticas, en 1994, Mandela fue el primer presidente negro de Sudáfrica. Gobernó hasta 1999.',
    q9w='La "Rainbow Nation" describe Sudáfrica como un solo país de muchas culturas, pueblos y lenguas que conviven a pesar de sus diferencias.',
    q10w='Sudáfrica tiene 12 lenguas oficiales, entre ellas el zulú, el xhosa, el afrikáans, el inglés y la lengua de signos sudafricana.',
    q11w='La democracia existe y las leyes del apartheid desaparecieron. Lo que queda es la INEQUALITY: pobreza, desempleo y oportunidades desiguales, muchas de ellas herencia del apartheid.',
    q12w='La independencia (1910, 1961) dio a Sudáfrica el autogobierno. La libertad y la igualdad para todos llegaron solo con el fin del apartheid en 1994.',
    g1w1='El apartheid separaba las razas por ley: racial SEGREGATION. "Discrimination" también es correcto aquí.',
    g1w2='RECONCILIATION es hacer las paces tras un conflicto. Mandela la eligió en lugar de la venganza.',
    g1w3='En 1961 Sudáfrica se convirtió en una REPUBLIC. Desde 1910 había sido un DOMINION.',
    g2w1='La brecha entre ricos y pobres es la economic INEQUALITY. "Poverty" significa pobreza; no es una brecha.',
    g2w2='Tratar peor a las personas por su raza es DISCRIMINATION.',
    g2w3='Muchas culturas y lenguas: una población DIVERSE.',
    sortWhy='La clasificación por raza, la falta de voto para los negros, las leyes sobre dónde vivir y las escuelas y playas separadas eran el apartheid. El voto para todos, la constitución de 1996, las 12 lenguas oficiales y la presidencia de Mandela llegaron después de 1994.',
    orderWhy='1910 la Unión Sudafricana · 1948 el apartheid se hace ley · 1961 la república · 1990 Mandela sale libre · 1994 las primeras elecciones para todas las razas.',

    actTitle='Te toca',
    actUse='Usa al menos tres:',
    actSpeakBrief='Prepárate para el examen explicándolo en voz alta. Trabaja con un compañero.',
    actSpeak1='Alguien dice: "Sudáfrica se hizo libre en 1961." Corrígelo con educación y explica qué cambió de verdad en 1961 y qué cambió en 1994.',
    actSpeak2='Tienes un minuto para presentar a Nelson Mandela a una clase que nunca ha oído hablar de él: qué hizo, cuándo y por qué el mundo lo sigue recordando.',
    actSpeak3='¿Es la Nación Arcoíris una realidad o todavía un sueño? Toma partido y da dos razones de la Sudáfrica de hoy. Tu compañero defiende lo contrario.',
    actWriteKind='Escritura · 150–250 palabras',
    actWriteBrief='Comenta "Independence gave all South Africans freedom." Escribe una introducción que nombre la afirmación, dos o tres párrafos principales con al menos dos temas clave y una conclusión con tu opinión.',
    actPlaceholder='In this comment, I want to give my opinion on the statement…',

    resPerfect='Perfecto. Conoces los cinco temas: ya puedes escribir.',
    resStrong='Muy bien. Repasa las fechas: 1910, 1948, 1961, 1990, 1994.',
    resMid='Buen comienzo. Vuelve a la Etapa 1: independencia y libertad no son lo mismo.',
    resLow='Vuelve a leer los textos despacio y luego intenta las preguntas otra vez.',
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
