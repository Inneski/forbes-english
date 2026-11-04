# -*- coding: utf-8 -*-
"""Interface strings for Be Aware of This Cleaner (B1) — English, German, Spanish.

Per house style §8 the English being taught never translates: the post
itself, question stems, options, gap sentences and the target chips stay
English in every build. What translates is the chrome, the teaching cards
(six-item form, so the rule travels with its heading), the explanations and
the task instructions. Grammar patterns stay in CAPS English in every language.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME
from build_beaware import EN_WHY

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'actEyebrow', 'btnCopy', 'btnCopied',
        'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Be Aware of This <em>Cleaner</em>',
    coverSub='A fake warning, a real advert — the English of a Facebook post that went round the Highlands',
    chipLevel='B1 · Intermediate', chipFocus='Reading · cleaning words · present perfect',
    chipCount='19 slides',

    postEyebrow='Read the post · 1 of 2', postTitle='Seen on a community notice board',
    post1n='Read it once for the joke. What do you think is going on?',
    postEyebrow2='Read the post · 2 of 2', postTitle2='… and the reveal',
    post2n='Were you right? Who wrote the post, and what do they want?',

    jokeEyebrow='How it works', jokeTitle='A warning that is really an advert',
    j1h='1 · The set-up',
    j1b='Capital letters, alarm emojis and <strong>PLEASE SHARE</strong>: it looks exactly '
        'like a warning about a criminal.',
    j1n='People share warnings, so the post travels.',
    j2h='2 · The twist',
    j2b='Every “crime” is something a customer wants: grease gone, shiny taps, the place '
        'behind the toilet clean.',
    j2n='The joke is the gap between the tone and the facts.',
    j3h='3 · The reveal',
    j3b='Only at the end: her name, the business, the services, and '
        '<strong>drop me a message</strong>.',
    j3n='Advert first, then the call to action.',

    wordsEyebrow='Vocabulary', wordsTitle='Cleaning words from the post',
    w1h='The dirt',
    w1b='<strong>grease</strong> — oily dirt from cooking<br>'
        '<strong>limescale</strong> — white build-up from water<br>'
        '<strong>grime</strong> — dirt that has been there a long time',
    w1n='All three are uncountable: some grease, NOT a grease.',
    w2h='The result',
    w2b='<strong>spotless</strong> — no marks at all<br>'
        '<strong>sparkling</strong> — clean and bright<br>'
        '<strong>shiny</strong> — reflects the light',
    w2n='“So shiny you can see your face in them.”',
    w3h='The service',
    w3b='<strong>a regular clean</strong> — the normal visit<br>'
        '<strong>a deep clean</strong> — everything, top to bottom<br>'
        '<strong>weekly / fortnightly</strong> — every week / two weeks',
    w3n='A fortnight = two weeks. Very British.',

    gramEyebrow='Grammar', gramTitle='Three structures doing the work',
    g1h='HAS BEEN + PAST PARTICIPLE',
    g1b='“She <strong>has been spotted</strong>.” The passive: we do not say WHO saw her. '
        'It sounds like a news report.',
    g1n='spot → spotted · see → seen',
    g2h='HAS BEEN + for / since',
    g2b='“Grease that <strong>has been</strong> there for years.” It started in the past and '
        'it is still there now.',
    g2n='for years · since 2019 · for ages',
    g3h='KEEP + VERB-ING',
    g3b='“She <strong>keeps coming</strong> back.” Again and again. “She” takes KEEPS.',
    g3n='Also in the post: HAD + PAST PARTICIPLE — “had given up on”.',

    qEyebrow='Check your reading', qTitle='Choose the best answer',
    gapEyebrow='Grammar', gapTitle='Complete the sentences',
    gapHint='Type one item from the word bank. Some are not used.',
    bankLabel='Word bank:',
    matchEyebrow='Phrases', matchTitle='What do they mean?',
    matchHint='Click a phrase, then click its meaning.',

    resNext='Now write your own fake warning →',
    actTitle='Write your own fake warning', actUse='Use at least three:',
    actSpeakKind='Speaking · in pairs',
    actSpeakBrief='Choose a local business — a dog walker, a plumber, a baker, a hairdresser. '
                  'Turn its best quality into a “crime”.',
    actSpeak1='Say your opening warning as dramatically as you can. Your partner guesses the business.',
    actSpeak2='Give three “crimes” it has been spotted committing. Use HAS BEEN + PAST PARTICIPLE.',
    actSpeak3='Say what the worst part is — something customers keep getting. Use KEEP + VERB-ING.',
    actSpeak4='Is this kind of advert clever or annoying? Would you share it? Say why.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write a “BE AWARE” post for a community Facebook page, advertising a real or '
                  'invented local business. Warning first, then the twist, then the reveal and '
                  'how to book.',
    actPlaceholder='🚨 BE AWARE OF THIS MAN!!! 🚨 He has been spotted…',

    resPerfect='Perfect score. You read the joke, the words and the grammar.',
    resStrong='Very good. Check the grammar slide for anything you missed.',
    resMid='A good start. Go back to the vocabulary and grammar slides, then try again.',
    resLow='Read the post again slowly, then the three teaching slides, and repeat.',
)
for n, w in enumerate(EN_WHY):
    T['en']['q%dwhy' % (n + 1)] = w

T['de'] = dict(
    coverTitle='Vorsicht vor dieser <em>Putzfrau</em>',
    coverSub='Eine falsche Warnung, eine echte Werbung — das Englisch eines Facebook-Posts aus den Highlands',
    chipLevel='B1 · Mittelstufe', chipFocus='Lesen · Putzwortschatz · Present Perfect',
    chipCount='19 Folien',

    postEyebrow='Lies den Post · 1 von 2', postTitle='Gesehen auf einem Gemeinde-Schwarzen-Brett',
    post1n='Lies ihn einmal wegen des Witzes. Was ist hier wohl los?',
    postEyebrow2='Lies den Post · 2 von 2', postTitle2='… und die Auflösung',
    post2n='Lagst du richtig? Wer hat den Post geschrieben, und was will diese Person?',

    jokeEyebrow='So funktioniert es', jokeTitle='Eine Warnung, die eigentlich Werbung ist',
    j1h='1 · Der Aufbau',
    j1b='Großbuchstaben, Alarm-Emojis und <strong>PLEASE SHARE</strong>: Es sieht genau aus '
        'wie eine Warnung vor einer Kriminellen.',
    j1n='Warnungen werden geteilt, also verbreitet sich der Post.',
    j2h='2 · Die Wendung',
    j2b='Jedes „Verbrechen“ ist etwas, das sich Kunden wünschen: kein Fett mehr, glänzende '
        'Wasserhähne, sauber hinter der Toilette.',
    j2n='Der Witz liegt im Abstand zwischen Ton und Tatsachen.',
    j3h='3 · Die Auflösung',
    j3b='Erst am Ende: ihr Name, die Firma, die Leistungen und '
        '<strong>drop me a message</strong>.',
    j3n='Erst die Werbung, dann die Handlungsaufforderung.',

    wordsEyebrow='Wortschatz', wordsTitle='Putzwörter aus dem Post',
    w1h='Der Schmutz',
    w1b='<strong>grease</strong> — Fett vom Kochen<br>'
        '<strong>limescale</strong> — Kalk, weiße Ablagerung vom Wasser<br>'
        '<strong>grime</strong> — alter, festsitzender Schmutz',
    w1n='Alle drei sind unzählbar: some grease, NICHT a grease.',
    w2h='Das Ergebnis',
    w2b='<strong>spotless</strong> — blitzsauber, kein Fleck<br>'
        '<strong>sparkling</strong> — sauber und strahlend<br>'
        '<strong>shiny</strong> — glänzend, spiegelt das Licht',
    w2n='„So glänzend, dass du dein Gesicht darin siehst.“',
    w3h='Die Dienstleistung',
    w3b='<strong>a regular clean</strong> — die normale Reinigung<br>'
        '<strong>a deep clean</strong> — Grundreinigung, von oben bis unten<br>'
        '<strong>weekly / fortnightly</strong> — jede Woche / alle zwei Wochen',
    w3n='A fortnight = zwei Wochen. Sehr britisch.',

    gramEyebrow='Grammatik', gramTitle='Drei Strukturen, die die Arbeit machen',
    g1h='HAS BEEN + PAST PARTICIPLE',
    g1b='„She <strong>has been spotted</strong>.“ Das Passiv: Wir sagen nicht, WER sie gesehen '
        'hat. Es klingt wie eine Nachrichtenmeldung.',
    g1n='spot → spotted · see → seen',
    g2h='HAS BEEN + for / since',
    g2b='„Grease that <strong>has been</strong> there for years.“ Es begann in der Vergangenheit '
        'und ist immer noch da.',
    g2n='for years · since 2019 · for ages',
    g3h='KEEP + VERB-ING',
    g3b='„She <strong>keeps coming</strong> back.“ Immer wieder. Mit „she“ heißt es KEEPS.',
    g3n='Auch im Post: HAD + PAST PARTICIPLE — „had given up on“.',

    qEyebrow='Leseverständnis', qTitle='Wähle die beste Antwort',
    q1why='Der Anfang kopiert den Stil einer echten Warnung. Dann stellen sich die '
          '„Verbrechen“ als sehr gutes Putzen heraus — diese Überraschung ist der Witz, und '
          'deshalb wird der Post geteilt.',
    q2why='<strong>Limescale</strong> ist Kalk, die weiße Ablagerung von hartem Wasser. '
          '<strong>Condensation</strong> sind Wassertropfen auf einem kalten Fenster oder '
          'Spiegel — die wischt man einfach weg.',
    q3why='<strong>Grease</strong> ist fettiger Schmutz vom Kochen. Deshalb nennt der Post den '
          'Angriff darauf ein „Verbrechen“ — sonst traut sich niemand ran.',
    q4why='A <strong>fortnight</strong> sind zwei Wochen, also heißt <strong>fortnightly</strong> '
          'alle zwei Wochen. Im britischen Englisch üblich, im amerikanischen selten.',
    q5why='<strong>To spot</strong> someone heißt, jemanden sehen oder bemerken. HAS BEEN + PAST '
          'PARTICIPLE ist das Passiv: Es sagt nicht, WER sie gesehen hat — wie in einer Nachricht.',
    q6why='<strong>To give up on</strong> something heißt, aufhören, es reparieren zu wollen, weil '
          'es hoffnungslos scheint. HAD + PAST PARTICIPLE legt das zeitlich vor Morags Ankunft.',
    q7why='KEEP + VERB-ING heißt immer wieder. In einer Warnung klingt das schrecklich; in einer '
          'Werbung bedeutet es regelmäßige Besuche — wöchentlich oder alle zwei Wochen.',
    q8why='<strong>Every excuse going</strong> = jede Ausrede, die es gibt. Was du auch über die '
          'Unordnung sagst, sie hat es schon gehört — du musst dich also nicht schämen.',
    gapEyebrow='Grammatik', gapTitle='Ergänze die Sätze',
    gapHint='Tippe einen Eintrag aus der Wortliste. Nicht alle werden gebraucht.',
    bankLabel='Wortliste:',
    matchEyebrow='Wendungen', matchTitle='Was bedeuten sie?',
    matchHint='Klicke auf eine Wendung, dann auf ihre Bedeutung.',

    resNext='Jetzt schreib deine eigene falsche Warnung →',
    actTitle='Schreib deine eigene falsche Warnung', actUse='Verwende mindestens drei:',
    actSpeakKind='Sprechen · zu zweit',
    actSpeakBrief='Wähle ein lokales Geschäft — Hundesitter, Klempnerin, Bäcker, Friseurin. '
                  'Mach aus seiner besten Eigenschaft ein „Verbrechen“.',
    actSpeak1='Sprich deine Warnung so dramatisch wie möglich. Dein Partner rät das Geschäft.',
    actSpeak2='Nenne drei „Verbrechen“, bei denen es gesehen wurde. Verwende HAS BEEN + PAST PARTICIPLE.',
    actSpeak3='Sag, was das Schlimmste ist — etwas, das Kunden immer wieder bekommen. Verwende KEEP + VERB-ING.',
    actSpeak4='Ist diese Art Werbung clever oder nervig? Würdest du sie teilen? Warum?',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreib einen „BE AWARE“-Post für eine Gemeinde-Facebookseite, der für ein '
                  'echtes oder erfundenes lokales Geschäft wirbt. Erst die Warnung, dann die '
                  'Wendung, dann die Auflösung und wie man bucht.',
    actPlaceholder='🚨 BE AWARE OF THIS MAN!!! 🚨 He has been spotted…',

    resPerfect='Volle Punktzahl. Du hast den Witz, die Wörter und die Grammatik verstanden.',
    resStrong='Sehr gut. Sieh dir für die Fehler noch einmal die Grammatikfolie an.',
    resMid='Ein guter Anfang. Geh zurück zu Wortschatz und Grammatik und versuch es noch einmal.',
    resLow='Lies den Post langsam noch einmal, dann die drei Lernfolien, und wiederhole.',
)

T['es'] = dict(
    coverTitle='Cuidado con esta <em>limpiadora</em>',
    coverSub='Un aviso falso, un anuncio real — el inglés de un post de Facebook que recorrió las Highlands',
    chipLevel='B1 · Intermedio', chipFocus='Lectura · vocabulario de limpieza · present perfect',
    chipCount='19 diapositivas',

    postEyebrow='Lee el post · 1 de 2', postTitle='Visto en un tablón de anuncios vecinal',
    post1n='Léelo una vez por el chiste. ¿Qué crees que está pasando?',
    postEyebrow2='Lee el post · 2 de 2', postTitle2='… y la revelación',
    post2n='¿Acertaste? ¿Quién escribió el post y qué quiere?',

    jokeEyebrow='Cómo funciona', jokeTitle='Un aviso que en realidad es un anuncio',
    j1h='1 · El planteamiento',
    j1b='Mayúsculas, emojis de alarma y <strong>PLEASE SHARE</strong>: parece exactamente un '
        'aviso sobre una delincuente.',
    j1n='La gente comparte los avisos, así que el post se difunde.',
    j2h='2 · El giro',
    j2b='Cada «delito» es algo que el cliente quiere: sin grasa, grifos brillantes, limpio '
        'detrás del váter.',
    j2n='El chiste está en la distancia entre el tono y los hechos.',
    j3h='3 · La revelación',
    j3b='Solo al final: su nombre, la empresa, los servicios y '
        '<strong>drop me a message</strong>.',
    j3n='Primero el anuncio, luego la llamada a la acción.',

    wordsEyebrow='Vocabulario', wordsTitle='Palabras de limpieza del post',
    w1h='La suciedad',
    w1b='<strong>grease</strong> — grasa de cocinar<br>'
        '<strong>limescale</strong> — cal, depósito blanco del agua<br>'
        '<strong>grime</strong> — mugre que lleva mucho tiempo',
    w1n='Las tres son incontables: some grease, NO a grease.',
    w2h='El resultado',
    w2b='<strong>spotless</strong> — impecable, sin una mancha<br>'
        '<strong>sparkling</strong> — limpio y reluciente<br>'
        '<strong>shiny</strong> — brillante, refleja la luz',
    w2n='«Tan brillantes que te ves la cara en ellos.»',
    w3h='El servicio',
    w3b='<strong>a regular clean</strong> — la limpieza habitual<br>'
        '<strong>a deep clean</strong> — limpieza a fondo, de arriba abajo<br>'
        '<strong>weekly / fortnightly</strong> — cada semana / cada dos semanas',
    w3n='A fortnight = dos semanas. Muy británico.',

    gramEyebrow='Gramática', gramTitle='Tres estructuras que hacen el trabajo',
    g1h='HAS BEEN + PAST PARTICIPLE',
    g1b='«She <strong>has been spotted</strong>.» La pasiva: no decimos QUIÉN la vio. '
        'Suena a noticia.',
    g1n='spot → spotted · see → seen',
    g2h='HAS BEEN + for / since',
    g2b='«Grease that <strong>has been</strong> there for years.» Empezó en el pasado y '
        'sigue ahí ahora.',
    g2n='for years · since 2019 · for ages',
    g3h='KEEP + VERB-ING',
    g3b='«She <strong>keeps coming</strong> back.» Una y otra vez. Con «she» es KEEPS.',
    g3n='También en el post: HAD + PAST PARTICIPLE — «had given up on».',

    qEyebrow='Comprensión lectora', qTitle='Elige la mejor respuesta',
    q1why='El comienzo copia el estilo de un aviso real. Luego los «delitos» resultan ser una '
          'limpieza muy buena — esa sorpresa es el chiste, y por eso la gente lo comparte.',
    q2why='<strong>Limescale</strong> es la cal, el depósito blanco del agua dura. '
          '<strong>Condensation</strong> son gotas de agua en una ventana o un espejo fríos — '
          'se quitan con un trapo.',
    q3why='<strong>Grease</strong> es la suciedad grasienta de cocinar. Por eso el post llama '
          '«delito» a atacarla — nadie más se atreve.',
    q4why='A <strong>fortnight</strong> son dos semanas, así que <strong>fortnightly</strong> '
          'significa cada dos semanas. Es común en inglés británico y raro en el americano.',
    q5why='<strong>To spot</strong> someone es ver o notar a alguien. HAS BEEN + PAST PARTICIPLE '
          'es la pasiva: no dice QUIÉN la vio, igual que una noticia.',
    q6why='<strong>To give up on</strong> something es dejar de intentar arreglarlo porque parece '
          'imposible. HAD + PAST PARTICIPLE lo sitúa antes de que llegara Morag.',
    q7why='KEEP + VERB-ING significa una y otra vez. En un aviso suena terrible; en un anuncio '
          'significa visitas regulares — semanales o quincenales.',
    q8why='<strong>Every excuse going</strong> = todas las excusas que existen. Digas lo que digas '
          'del desorden, ya lo ha oído — así que no hace falta sentir vergüenza.',
    gapEyebrow='Gramática', gapTitle='Completa las frases',
    gapHint='Escribe un elemento del banco de palabras. Algunos no se usan.',
    bankLabel='Banco de palabras:',
    matchEyebrow='Expresiones', matchTitle='¿Qué significan?',
    matchHint='Haz clic en una expresión y luego en su significado.',

    resNext='Ahora escribe tu propio aviso falso →',
    actTitle='Escribe tu propio aviso falso', actUse='Usa al menos tres:',
    actSpeakKind='Expresión oral · en parejas',
    actSpeakBrief='Elige un negocio local — paseador de perros, fontanera, panadero, peluquera. '
                  'Convierte su mejor cualidad en un «delito».',
    actSpeak1='Di tu aviso inicial de la forma más dramática posible. Tu compañero adivina el negocio.',
    actSpeak2='Da tres «delitos» en los que lo han visto. Usa HAS BEEN + PAST PARTICIPLE.',
    actSpeak3='Di qué es lo peor — algo que los clientes reciben una y otra vez. Usa KEEP + VERB-ING.',
    actSpeak4='¿Este tipo de anuncio es ingenioso o molesto? ¿Lo compartirías? Explica por qué.',
    actWriteKind='Expresión escrita · 150–200 palabras',
    actWriteBrief='Escribe un post «BE AWARE» para una página vecinal de Facebook que anuncie un '
                  'negocio local real o inventado. Primero el aviso, luego el giro, luego la '
                  'revelación y cómo reservar.',
    actPlaceholder='🚨 BE AWARE OF THIS MAN!!! 🚨 He has been spotted…',

    resPerfect='Puntuación perfecta. Has entendido el chiste, las palabras y la gramática.',
    resStrong='Muy bien. Repasa la diapositiva de gramática para lo que falló.',
    resMid='Buen comienzo. Vuelve al vocabulario y a la gramática y repite.',
    resLow='Lee el post otra vez despacio, luego las tres diapositivas de teoría, y repite.',
)

TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'", 'glossShow': "'Translate'",
           'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'", 'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'", 'glossShow': "'Traducir'",
           'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    rows += ['    %s: %s' % (k, TAIL[code][k]) for k in sorted(TAIL[code])]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
