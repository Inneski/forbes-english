# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Tests — German. Same keys as mixed_b1_en.py.

Tense names stay in English (the learner meets them that way in every other
lesson); the other area names translate. English examples stay English.
"""

AREA = dict(
    presSimple='Present Simple', presCont='Present Continuous',
    pastSimple='Past Simple', pastCont='Past Continuous',
    presPerf='Present Perfect', futSimple='Futur mit WILL',
    compar='Komparativ &amp; Superlativ', modals='Modalverben',
    cond='Bedingungssätze', passive='Passiv', relative='Relativsätze',
    questions='Fragen', quant='Mengenwörter', prep='Präpositionen',
    stative='Zustandsverben',
)

COMMON = dict(
    chipLevel='B1 &middot; Mittelstufe',
    chipFocus='35 Punkte &middot; fünf Teile',
    chipCount='{N} Folien',

    eIntro='Bevor du anfängst',
    tIntro='Ein Test, zehn Grammatikbereiche',
    introA='Fünf Teile',
    introAb='10 Multiple Choice &middot; eine Geschichte mit 8 Lücken &middot; '
            '6 richtig oder falsch &middot; 5 Sätze bauen &middot; 6 Fehler '
            'korrigieren.',
    introAn='Jede Antwort wird sofort erklärt.',
    introB='Was getestet wird',
    introBb='Present-, Past- und Perfect-Zeiten, WILL, Vergleiche, Modalverben, '
            'Bedingungssätze, Passiv, Relativsätze und Fragen.',
    introBn='Arbeite allein und schlag nichts nach. Dein Ergebnis nützt nur, '
            'wenn es ehrlich ist.',

    eMC='Teil 1 &middot; Multiple Choice',
    tMC='Wähle die richtige Form',
    eStory='Teil 2 &middot; Lesen',
    eTF='Teil 3 &middot; Richtig oder falsch',
    tTF='Stimmt diese Regel?',
    eOrder='Teil 4 &middot; Sätze bauen',
    tOrder='Bring die Teile in die richtige Reihenfolge',
    hOrder='Klick auf einen Block, um ihn zu setzen; klick auf einen gesetzten '
           'Block, um ihn zurückzunehmen. Ein Punkt für den ganzen Satz.',
    eFix='Teil 5 &middot; Fehlerkorrektur',
    tFix='Finde den Fehler und korrigiere ihn',
    hFix='Jeder Satz hat einen Fehler. Schreib den ganzen Satz noch einmal, '
         'korrigiert.',

    resPerfect='Fehlerfrei. B1-Grammatik sitzt bei dir &mdash; Zeit für B2.',
    resStrong='Solide. Ein paar Lücken sind noch zu schließen; die Liste unten '
              'zeigt genau, welche.',
    resMid='Guter Fortschritt. Lies die Erklärungen zu deinen Fehlern und '
           'versuch es noch einmal.',
    resLow='Weiter üben. Geh die Liste unten langsam durch und mach den Test '
           'morgen noch einmal.',

    actUse='Benutze mindestens drei',
    actSpeakBrief='Zu zweit. Benutze die Grammatik in Klammern.',
    actWriteKind='Schreiben',
)

P1 = dict(
    coverTitle='Gemischter Grammatik<em>test</em>',
    coverSub='Zehn Grammatikbereiche, ein Test: Zeiten, Modalverben, '
             'Bedingungssätze, Passiv und mehr.',
    tStory='Elenas Tag',
    hSt1='Setz das Verb in Klammern in die richtige Form. '
         '&bdquo;Oversleep&ldquo; = verschlafen.',
    hSt2='Setz das Verb in Klammern in die richtige Form. '
         '&bdquo;Borrow&ldquo; = (sich) etwas leihen.',
    hSt3='Die letzte Lücke braucht ein Mengenwort, kein Verb: Wähle eins der '
         'beiden in Klammern.',
    gTournament='&bdquo;Tournament&ldquo; = Turnier.',
    gSeatbelt='&bdquo;Seatbelt&ldquo; = Sicherheitsgurt.',

    x_mc1='&bdquo;Listen!&ldquo; heißt jetzt, die Handlung läuft gerade: IS + '
          'knocking. &bdquo;Knocks&ldquo; ist eine Gewohnheit; '
          '&bdquo;knocked&ldquo; und &bdquo;was knocking&ldquo; sind '
          'Vergangenheit.',
    x_mc2='WHILE + WAS / WERE + -ING für die längere Hintergrundhandlung; das '
          'Past Simple (&bdquo;rang&ldquo;) unterbricht sie. Die anderen drei '
          'sind Gegenwartsformen.',
    x_mc3='SINCE + Zeitpunkt (2019) braucht HAS / HAVE + Partizip. '
          '&bdquo;Lived&ldquo; passt nicht zu &bdquo;since&ldquo;, die '
          'Gegenwartsformen auch nicht.',
    x_mc4='&bdquo;I think&ldquo; leitet eine Meinung über die Zukunft ein: '
          'WILL + Verb. &bdquo;Is winning&ldquo; hieße, das Spiel läuft gerade.',
    x_mc5='Verglichen mit allen Filmen des Jahres, also der Superlativ: THE '
          'BEST. &bdquo;Goodest&ldquo; und &bdquo;more good&ldquo; gibt es '
          'nicht; &bdquo;better&ldquo; vergleicht nur zwei.',
    x_mc6='Ein Gesetz ist eine starke Pflicht: MUST + Verb. &bdquo;Might&ldquo; '
          'und &bdquo;could&ldquo; drücken Möglichkeit aus, &bdquo;would&ldquo; '
          'etwas Gedachtes.',
    x_mc7='Bedingungssatz Typ 1: IF + Present Simple, WILL im anderen '
          'Satzteil. Nach IF steht hier nie WILL.',
    x_mc8='&bdquo;Would learn&ldquo; zeigt eine gedachte Situation, also Typ '
          '2: IF + Past Simple (&bdquo;had&ldquo;).',
    x_mc9='Eine Brücke baut sich nicht selbst, also Passiv: WAS + Partizip. '
          '&bdquo;Built&ldquo; allein ist aktiv, und niemand tut es.',
    x_mc10='WHO für Personen. WHICH für Dinge, WHOSE für Besitz, WHERE für '
           'Orte.',

    x_st1='&bdquo;Usually&ldquo; ist eine Gewohnheit: Present Simple, und '
          '&bdquo;she&ldquo; bekommt -S (&bdquo;gets up&ldquo;). &bdquo;This '
          'morning&ldquo; ist vorbei: Past Simple &bdquo;overslept&ldquo; '
          '(unregelmäßig).',
    x_st2='&bdquo;For almost three years now&ldquo; reicht bis heute: HAS + '
          'lived. HAS BEEN living ist auch richtig.',
    x_st3='WHILE + WAS + -ING für die längere Handlung; das Klopfen '
          '(&bdquo;knocked&ldquo;) unterbricht sie.',
    x_st4='Der Tisch ist reserviert, es ist also eine Verabredung: IS + '
          'meeting. IS GOING TO meet ist auch richtig.',
    x_st5='Bedingungssatz Typ 1. Nach IF Present Simple (&bdquo;is&ldquo;), '
          'nicht WILL; die Folge bekommt WILL + go.',
    x_st6='Im bejahten Satz sagt man A LOT OF. MUCH steht in verneinten Sätzen '
          'und Fragen: &bdquo;They don&rsquo;t serve much seafood.&ldquo;',

    tf1='Wir benutzen das Present Perfect mit einer abgeschlossenen Zeit wie '
        '&bdquo;yesterday&ldquo; oder &bdquo;in 2010&ldquo;.',
    tf2='&bdquo;Must&ldquo; und &bdquo;have to&ldquo; drücken beide eine Pflicht '
        'aus, aber nur &bdquo;have to&ldquo; hat eine Vergangenheitsform: '
        '&bdquo;had to&ldquo;.',
    tf3='Im Bedingungssatz Typ 1 steht &bdquo;will&ldquo; nach &bdquo;if&ldquo;.',
    tf4='Vor einem Superlativ steht meistens &bdquo;the&ldquo;.',
    tf5='Das Passiv ist BE + Partizip.',
    tf6='In Relativsätzen benutzen wir &bdquo;who&ldquo; für Personen und '
        '&bdquo;which&ldquo; für Dinge.',
    x_tf1='Falsch. Eine abgeschlossene Zeit verlangt das Past Simple: '
          '&bdquo;I visited Paris in 2010&ldquo;, nicht &bdquo;I have '
          'visited&ldquo;.',
    x_tf2='Richtig. MUST hat keine eigene Vergangenheitsform, für die '
          'Vergangenheit nehmen wir HAD TO.',
    x_tf3='Falsch. Nach IF steht Present Simple (&bdquo;If it rains&ldquo;); '
          'WILL kommt in den anderen Satzteil (&bdquo;we&rsquo;ll stay '
          'in&ldquo;).',
    x_tf4='Richtig. THE hebt eine Sache als die einzige ihrer Gruppe hervor: '
          'THE best, THE tallest, THE most expensive.',
    x_tf5='Richtig. &bdquo;Is built&ldquo;, &bdquo;was written&ldquo;, '
          '&bdquo;has been finished&ldquo;: immer eine Form von BE + Partizip.',
    x_tf6='Richtig. THAT kann im Alltag beide ersetzen, aber WHO steht nur für '
          'Personen und WHICH nur für Dinge.',

    x_or1='Passiv: Subjekt + WAS + Partizip, dann die Zeit.',
    x_or2='&bdquo;Who lives next door&ldquo; steht direkt nach &bdquo;the '
          'man&ldquo; und sagt, welcher Mann. Dann das Hauptverb, IS.',
    x_or3='Fragewort + DID + Subjekt + Grundform. Nach DID hat das Verb kein '
          '-ED: &bdquo;go&ldquo;, nicht &bdquo;went&ldquo;.',
    x_or4='Bedingungssatz Typ 2: IF + Past Simple (&bdquo;were&ldquo;), dann '
          'WOULD (&rsquo;D) + Verb.',
    x_or5='MUCH vor dem Komparativ verstärkt ihn; THAN leitet das Zweite ein.',

    x_fx1='FOR + Zeitdauer (five years). SINCE + Zeitpunkt (2019, March).',
    x_fx2='Nach IF im Bedingungssatz Typ 1 steht Present Simple: &bdquo;If I '
          'have time&ldquo;. WILL bleibt im anderen Satzteil.',
    x_fx3='&bdquo;Better&ldquo; ist schon ein Komparativ. MORE + BETTER ist nie '
          'richtig.',
    x_fx4='Das Passiv braucht das Partizip: write &rarr; wrote &rarr; WRITTEN.',
    x_fx5='&bdquo;Money&ldquo; ist unzählbar: MUCH, nicht MANY. MANY steht vor '
          'Pluralnomen: &bdquo;many coins&ldquo;.',
    x_fx6='WHICH steht für Dinge. Für eine Person WHO (oder THAT).',

    actTitle='Jetzt benutz es',
    actSpeak1='Dein normaler Morgen, dann was heute Morgen anders war. '
              '(Present Simple, Past Simple)',
    actSpeak2='Was würdest du mit einem ganzen freien Jahr machen? Frag auch '
              'deinen Partner. (Typ 2)',
    actSpeak3='Ein berühmtes Gebäude in deiner Stadt: Wann und von wem wurde es '
              'gebaut? (Passiv)',
    actWriteBrief='Eine E-Mail, 120&ndash;150 Wörter, an einen Freund, der '
                  'nächste Woche kommt: deine Pläne, was er mitbringen muss und '
                  'was ihr macht, wenn es regnet.',
    actPlaceholder='Hi! I can&rsquo;t wait to see you next week&hellip;',
)

P2 = dict(
    coverTitle='Gemischter Grammatiktest <em>Teil 2</em>',
    coverSub='Zehn weitere Grammatikpunkte, alles neue Sätze: Zeiten, '
             'Modalverben, Bedingungssätze, Passiv und mehr.',
    tStory='Diegos Reise',
    hSt1='Setz das Verb in Klammern in die richtige Form.',
    hSt2='Setz das Verb in Klammern in die richtige Form. '
         '&bdquo;Suitcase&ldquo; = Koffer.',
    hSt3='Setz das Verb in Klammern in die richtige Form. '
         '&bdquo;Delayed&ldquo; = verspätet.',
    gForbidden='&bdquo;Forbidden&ldquo; = verboten.',

    x_mc1='&bdquo;Be quiet!&ldquo; heißt jetzt, die Handlung läuft gerade: IS + '
          'sleeping. &bdquo;Sleeps&ldquo; ist eine Gewohnheit; die anderen '
          'beiden sind Vergangenheit.',
    x_mc2='WHILE + WERE + -ING für die Hintergrundhandlung, die das Licht '
          '(&bdquo;went out&ldquo;) unterbrach. Die anderen sind '
          'Gegenwartsformen.',
    x_mc3='&bdquo;For ten years now&ldquo; reicht bis heute: HAVE + known. '
          '&bdquo;Are knowing&ldquo; ist falsch, weil KNOW keine laufende '
          'Handlung ist; &bdquo;knew&ldquo; sagt, dass es vorbei ist.',
    x_mc4='Ein Versprechen ist eine Entscheidung beim Sprechen: WILL + Verb. '
          '&bdquo;Am helping&ldquo; bräuchte eine feste Verabredung.',
    x_mc5='Verglichen mit allen Städten, also der Superlativ: THE + busiEST. '
          '&bdquo;Busier&ldquo; vergleicht zwei; &bdquo;most busiest&ldquo; '
          'sagt es doppelt.',
    x_mc6='&bdquo;Forbidden&ldquo; ist ein Verbot: MUSTN&rsquo;T. '
          '&bdquo;Don&rsquo;t have to&ldquo; heißt, es ist nicht nötig &mdash; '
          'fast das Gegenteil.',
    x_mc7='Bedingungssatz Typ 1: IF + Present Simple, dann WON&rsquo;T / WILL '
          'im anderen Satzteil.',
    x_mc8='&bdquo;Could join&ldquo; zeigt eine gedachte Situation: IF + Past '
          'Simple, und bei BE nehmen wir WERE für alle Personen.',
    x_mc9='Das Bild hat sich nicht selbst gemalt, also Passiv: WAS + Partizip, '
          'und BY nennt den Maler.',
    x_mc10='WHICH (oder THAT) für Dinge. WHO für Personen, WHOSE für Besitz, '
           'WHERE für Orte.',

    x_st1='&bdquo;Every summer&ldquo; ist eine Gewohnheit: Present Simple, und '
          '&bdquo;he&ldquo; bekommt -S.',
    x_st2='&bdquo;Last month&ldquo; ist vorbei: Past Simple &bdquo;booked&ldquo;. '
          'Der Freund hat es vorher empfohlen; &bdquo;recommended&ldquo; und '
          '&bdquo;had recommended&ldquo; sind beide richtig.',
    x_st3='&bdquo;Never &hellip; before&ldquo; ist sein Leben bis jetzt: HAS + '
          'NEVER + visited.',
    x_st4='WHILE + WAS + -ING für die längere Handlung; der Moment, in dem er '
          'es merkte, unterbricht sie.',
    x_st5='Der Sitzplatz ist gewählt, es ist also fest geplant: IS + flying. '
          'IS GOING TO fly ist auch richtig.',
    x_st6='Bedingungssatz Typ 1. Nach IF Present Simple (&bdquo;is&ldquo;); '
          'die Folge bekommt WILL + miss. MIGHT miss ist auch richtig.',

    tf1='Das Present Continuous kann eine feste Verabredung in der Zukunft '
        'ausdrücken, z. B. &bdquo;I&rsquo;m flying to Rome on Monday.&ldquo;',
    tf2='&bdquo;Mustn&rsquo;t&ldquo; und &bdquo;don&rsquo;t have to&ldquo; '
        'bedeuten dasselbe.',
    tf3='Im Bedingungssatz Typ 2 benutzen wir nach I, he, she und it oft '
        '&bdquo;were&ldquo; statt &bdquo;was&ldquo;.',
    tf4='Zweisilbige Adjektive nehmen immer &bdquo;more&ldquo;, nie '
        '&bdquo;-er&ldquo;.',
    tf5='Das Passiv von &bdquo;People speak English here&ldquo; ist '
        '&bdquo;English is spoken here.&ldquo;',
    tf6='&bdquo;Whose&ldquo; benutzt man, um über Besitz zu sprechen.',
    x_tf1='Richtig. Wenn der Plan feststeht (ein Ticket, eine Uhrzeit), ist '
          'das Present Continuous die natürliche Wahl.',
    x_tf2='Falsch. MUSTN&rsquo;T heißt, es ist verboten. DON&rsquo;T HAVE TO '
          'heißt, es ist nicht nötig. Sie sind fast Gegensätze.',
    x_tf3='Richtig. &bdquo;If I were you&ldquo;, &bdquo;If he were '
          'taller&ldquo;. &bdquo;Was&ldquo; hört man oft, aber WERE ist die '
          'Standardform.',
    x_tf4='Falsch. Viele nehmen -ER: happy &rarr; happier, easy &rarr; '
          'easier, narrow &rarr; narrower.',
    x_tf5='Richtig. Das Objekt (&bdquo;English&ldquo;) wird zum Subjekt, und '
          'das Verb wird IS + Partizip.',
    x_tf6='Richtig. &bdquo;Whose car is this?&ldquo; &middot; &bdquo;the man '
          'whose car was stolen&ldquo;.',

    x_or1='Eine Passivfrage: WAS + Subjekt + Partizip, dann BY + wer es getan '
          'hat.',
    x_or2='WHERE leitet einen Satz über einen Ort ein: &bdquo;where we had '
          'dinner&ldquo; sagt, welches Restaurant.',
    x_or3='HOW LONG + HAVE + Subjekt + Partizip: die Frage im Present Perfect.',
    x_or4='Bedingungssatz Typ 2: IF + Past Simple (&bdquo;had&ldquo;), dann '
          'WOULD + Verb.',
    x_or5='THE + Komparativ, THE + Komparativ: zwei Dinge, die sich zusammen '
          'verändern.',

    x_fx1='AGREE ist eine Meinung, keine laufende Handlung, also Present '
          'Simple: &bdquo;I agree&ldquo;.',
    x_fx2='MARRIED TO someone, nicht &bdquo;married with&ldquo;.',
    x_fx3='Nach IF im Bedingungssatz Typ 2 steht Past Simple: &bdquo;If I '
          'had&ldquo;. WOULD bleibt im anderen Satzteil.',
    x_fx4='&bdquo;Easy&ldquo; endet auf -Y, also -IER: EASIER, nicht '
          '&bdquo;more easy&ldquo;.',
    x_fx5='Im Passiv nennt BY, wer es getan hat: &bdquo;sent by the '
          'manager&ldquo;. FOR wäre der Empfänger.',
    x_fx6='WHOSE heißt schon &bdquo;his&ldquo;, also steht &bdquo;his&ldquo; '
          'doppelt. Streich es.',

    actTitle='Jetzt benutz es',
    actSpeak1='Deine Pläne für Samstag, und was du machst, wenn es regnet. '
              '(Present Continuous, Typ 1)',
    actSpeak2='In Arbeit oder Schule: drei Dinge, die du nicht darfst, drei, '
              'die du nicht musst. (Modalverben)',
    actSpeak3='Eine Reise, die schiefging: Was hast du gerade gemacht, als es '
              'passierte? (Past Continuous)',
    actWriteBrief='Eine Bewertung, 120&ndash;150 Wörter, über einen Ort, den '
                  'du kennst: seit wann, wofür er berühmt ist und warum er der '
                  'beste (oder schlechteste) ist.',
    actPlaceholder='I have been to &hellip; three times, and &hellip;',
)
