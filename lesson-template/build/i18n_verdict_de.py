# -*- coding: utf-8 -*-
"""German strings for Anatomy of a Verdict. See i18n_verdict.py.

Written in-session, informal "du" as the course chrome; no native check yet.
T is the chrome, N the narrative glosses behind the Translate button. Every
CAPS grammar token stays in English."""
T = dict(
    coverTitle='Anatomy of a <em>Verdict</em>',
    coverSub='Elf Geschworene sagen, sie hat ihn gestoßen. Du bist die Nummer zwölf, und du bist dir nicht sicher.',
    chipLevel='C1 · Fortgeschritten', chipFocus='Konzession · die Sprache des Arguments',
    chipCount='60–75 Minuten',
    btnContinue='Weiter →',
    actBefore='Bevor du beginnst',

    howEyebrow='So läuft die Beratung', howTitle='Jedes Argument hat seinen Preis.',
    howDp='Punkte', howDpBody='Ein richtiges Argument bringt <strong>+1 Punkt</strong>.',
    howTime='Geduld',
    howTimeBody='Der Raum beginnt mit vier. Ein falsches Argument kostet eine. Bei null hört dir niemand mehr zu.',
    howClues='Stimmen',
    howCluesBody='Vier Geschworene lassen sich umstimmen. Für das beste Urteil brauchst du alle vier.',
    ledDp='Punkte', ledTime='Geduld', ledClues='Stimmen',

    labEyebrow='Bevor ihr beratet', labTitle='Wie man einen Punkt zugesteht.',
    voteTurned='Eine Stimme wechselt', voteHeld='Die Stimme bleibt',
    chooseA='Die Aufnahme abspielen', chooseB='Das Treppenhaus prüfen',
    chooseC='Den Zeugen befragen', chooseD='Die Zeit nachrechnen',
    explainFirst='Begründe deine Wahl auf Englisch, bevor du klickst.',

    boardEyebrow='Dein Schlussplädoyer · Sprechrunde', boardTitle='Trag den Fall laut vor.',
    lockEyebrow='Das letzte Argument', lockTitle='Vervollständige beide Sätze.',

    ledgerEyebrow='Der letzte Stimmzettel liegt vor', ledgerTitle='Deine Bilanz entscheidet das Urteil.',
    gold='Einstimmig', goldBody='Jede Stimme umgestimmt, und der Raum hört noch zu.',
    silver='Mehrheit', silverBody='Genug Argumente hielten für ein Mehrheitsurteil.',
    shadow='Kein Urteil', shadowBody='Der Raum kommt nie zur Ruhe.',
    ledgerNote='Enden, die du nicht verdient hast, sind gesperrt.',
    branchLocked='Deine Bilanz trägt dieses Urteil nicht',
    endGold='Einstimmiges Urteil', endSilver='Mehrheitsurteil', endShadow='Keine Einigung',
    revealKick='Was die Beweise belegen konnten',
    resRoute='Gewertet werden nur die Fragen, die auf deinem Weg lagen.',

    glossShow='Übersetzen', glossHide='Übersetzung ausblenden',
    resPerfect='Makellos. Jedes Argument hielt.',
    resStrong='Starke Arbeit. Der Raum hat dir zugehört.',
    resMid='Ein ordentlicher Fall, mit Lücken, die eine Anwältin fände.',
    resLow='Der Zweifel war berechtigt. Die Argumente nicht.',

    actTitle='Jetzt argumentierst du selbst.',
    actUse='Verwende mindestens drei davon',
    actSpeakBrief='Zu zweit oder zu dritt. Erst zugestehen, dann den Punkt drehen.',
    actSpeak1='Du bist Victor. Argumentiere, dass Ruth schuldig ist. Dein Gegenüber gesteht jeden Punkt zu und dreht ihn dann.',
    actSpeak2='Du verteidigst Ruth. Gib drei Fakten gegen sie zu und zeige, warum keiner davon einen Stoß beweist.',
    actSpeak3='Denk an ein Mal, als du deine Meinung geändert hast. Erkläre, was du noch glaubst und was sie geändert hat.',
    actWriteKind='Schreiben · 150–250 Wörter',
    actWriteBrief='Schreib die Notiz, die der Obmann dem Richter schickt, und erkläre, wie die Geschworenen zu ihrem '
                  'Urteil kamen. Gestehe drei Punkte gegen Ruth zu und drehe jeden davon.',
    actPlaceholder='Sehr geehrter Herr Richter …',
)

N = {
    'casefile': '<strong>Dienstag</strong> Ruth und Simon streiten. Simon nimmt es mit dem Handy auf.<br>'
                '<strong>Mittwoch 14:25</strong> Eine Türklingelkamera zeigt Ruths Lieferwagen, der die Mühle verlässt.<br>'
                '<strong>14:30</strong> Kit, der Lehrling, sagt, er habe einen Schrei gehört.<br>'
                '<strong>14:52</strong> Ruth ruft den Notruf. Simon liegt am Fuß der eisernen Treppe.',
    'casefile-note': 'Niemand hat den Sturz gesehen. Das Geländer der Galerie ist gebrochen. Ruth sagt, sie habe Ton gekauft.',
    'dec1-a': 'Dein Fach. Jede Sekunde von Simons Aufnahme, jedes Echo, jede Lücke.',
    'dec1-b': 'Priyas Fach. Die Polizeifotos, das Geländer, der Bluterguss.',
    'dec2-a': 'Kit Marlow, neunzehn, der Lehrling. Er sagt, er habe einen Schrei gehört.',
    'dec2-b': 'Eine Türklingelkamera, ein weißer Lieferwagen, ein Notruf. Siebenundzwanzig Minuten.',
    'agnes-yes': 'Agnes legt ihren Bleistift hin. „Na gut. Nicht schuldig, vorerst.“ Ihre Hand geht mit deiner hoch.',
    'agnes-no': 'Agnes runzelt die Stirn über den Satz und schreibt nichts auf. „Versuch es später noch einmal, Liebes.“ Ihre Stimme bleibt, wo sie war.',
    'priya-yes': 'Priya steht auf und geht zum Fenster. Als sie sich wieder setzt, stimmt sie mit dir.',
    'priya-no': 'Priya schüttelt den Kopf. „Ich ändere meine Stimme nicht wegen eines Gefühls.“ Der Raum wird ungeduldig.',
    'gerald-yes': 'Gerald zieht die Uhr wieder an und schaut auf den Tisch. „Nicht schuldig. Schreiben Sie es auf.“ Der Obmann hat sich bewegt.',
    'gerald-no': 'Gerald schaut wieder auf die Uhr. „Ich denke, wir haben genug gehört.“ Seine Stimme bewegt sich nicht.',
    'victor-yes': 'Victor öffnet die Hände. Lange sagt er nichts. Dann: „Nicht schuldig.“ Zwölf zu null.',
    'victor-no': 'Victor verschränkt wieder die Arme. „Ich habe gesagt, was ich zu sagen habe.“ Der Raum muss ohne ihn auskommen.',
    'board': 'Vor der letzten Abstimmung sag drei Zugeständnisse laut: Gib jedes Mal eine Tatsache gegen Ruth zu, dann dreh sie.',
    'end-gold': 'Zwölf Zettel, ein Wort. Ruth Adair umklammert das Geländer der Anklagebank und weint nicht. '
                'Du wirst nie wissen, was auf dieser Treppe geschah. Genau darum ging es: Niemand in diesem Raum konnte es wissen.',
    't-end-gold': 'Urteil · einstimmig · nicht schuldig',
    'end-silver': 'Elf zu eins genügt nach so langer Zeit, sagt der Richter. Victor wollte sich nicht bewegen, und vielleicht konnte er es nie. '
                  'Ruth geht hinaus in den Regen, und du gehst hinter ihr hinaus.',
    't-end-silver': 'Urteil · elf zu eins · nicht schuldig',
    'end-shadow': 'Vier Stunden, drei Abstimmungen, und der Raum kommt nie zur Ruhe. Der Richter entlässt euch. '
                  'Es wird einen neuen Prozess geben, zwölf neue Geschworene, dieselbe Aufnahme.',
    't-end-shadow': 'Kein Urteil · keine Einigung · neuer Prozess',
    'reveal-a': '<strong>Was die Beweise belegten</strong><br>Sie stritten am Tag davor. Ruth log darüber, wann sie losfuhr. '
                'Simon stürzte zwischen zwei und drei von der Galerie.',
    'reveal-b': '<strong>Was sie nie belegten</strong><br>Einen Stoß. Der Krach war weit von Ruths Stimme entfernt, das Geländer war morsch, '
                'der Zeuge trug Kopfhörer, und der Lieferwagen war unterwegs.',
    'reveal-c': 'Geschworene entscheiden nicht, was geschehen ist. Sie entscheiden, ob die Beweise einen vernünftigen Zweifel lassen.',

    's-room1': 'Gerald Pryce, der Obmann, zählt die Zettel. „Elf schuldig. Einer nicht schuldig.“ Alle Köpfe drehen sich zu dir.',
    'c-room1': 'Ruth hat Simon am Tag davor angeschrien. Du hast trotzdem Zweifel.',
    's-room2': 'Danny Rourke fährt Taxi und hat zu allem eine Meinung. „Sie war wütend. Er ist tot. Fertig.“',
    'c-room2': 'Du gibst zu, dass sie wütend war. Wut allein beweist nichts.',
    's-room3': 'Agnes Bell, eine pensionierte Schulleiterin, hat vier Seiten mit Bleistift gefüllt. Sie schaut auf. „Na los. Überzeug mich.“',
    'c-room3': 'Ruth hat die Polizei angelogen, wann sie losgefahren ist. Das kannst du nicht bestreiten.',
    's-room4': 'Der Gerichtsdiener bringt den Laptop. Simons Handyaufnahme läuft noch einmal: Geschrei, ein Krach, dann Ruth, die weint.',
    'c-room4': 'Du bist Toningenieurin. Der Krach lässt sich kaum verorten.',
    's-room6': 'Gerald schaut auf die Uhr. „Hören Sie, ich respektiere Sie. Aber es steht elf zu eins, und mein Zug geht um sechs.“',
    'c-room6': 'Du respektierst Gerald auch. Trotzdem willst du, dass die Beweise noch einmal geprüft werden.',
    's-rec1': 'Kopfhörer auf. Ruths Stimme: „Du machst nie etwas fertig!“ Dann Simon, lachend. Danny beugt sich vor. „Hörst du das? Wütend.“',
    'c-rec1': 'Sie klingt wütend. Aber Simon lacht, also hatte er keine Angst.',
    's-rec2': 'Du spielst den Krach fünfmal in Schleife. Das Echo ist lang: Es geschah weit vom Handy entfernt, nahe der Küche.',
    'c-rec2': 'Ruths Stimme ist genau im Moment des Krachs nah am Handy.',
    's-rec4': 'Du spielst Danny das Echo vor, dann die Lücke in der Datei. Er ist ausnahmsweise still. „Na gut. Es ist nicht so klar, wie ich dachte.“',
    'c-rec4': 'Danny hält sie immer noch für fähig dazu. Aber er gibt zu, dass es Zweifel gibt.',
    's-stair1': 'Priya Sandhu, Notaufnahmeschwester, breitet die Polizeifotos unter der Lampe aus. Eiserne Treppe, hohe Galerie, ein Geländer, das an einem Bolzen hängt.',
    'c-stair1': 'Das Geländer ist gebrochen. Die Anklage sagt, Ruth habe es bei einem Kampf zerbrochen.',
    's-stair2': 'Priya packt ihren eigenen Arm. „Eine Hand hinterlässt so ein Mal. Ein Geländer auch, wenn man im Fallen danach greift.“',
    'c-stair2': 'Du versuchst auf jede Weise, den Bluterguss als Griff zu lesen. Er passt immer noch zu einem Sturz.',
    's-stair4': 'Auf dem Foto ist der Bolzen durchgerostet. Im März schrieb Simon einem Handwerker wegen des Geländers. Er hat ihn nie bestellt.',
    'c-stair4': 'Ruth war vielleicht auf der Treppe, vielleicht nicht. Das Geländer war ohnehin gefährlich.',
    's-after1': 'Das Mittagessen kommt in Plastikboxen. Victor Lane, ein Vermieter, hat seine nicht angerührt. „Künstlertypen. Die lügen alle.“',
    'c-after1': 'Victor hat sie nach ihrem Beruf beurteilt, nicht nach den Beweisen. Du bleibst ruhig.',
    's-after2': 'Gerald lässt ein zweites Mal abstimmen. Die Hände gehen diesmal langsamer hoch. Victor schlägt auf den Tisch. „Das ist lächerlich.“',
    'c-after2': 'Die Abstimmung hat sich bewegt. Victor ist so sicher wie zuvor.',
    's-after3': 'Du stehst mit Agnes und Priya am Fenster. Regen auf dem Parkplatz. „Er ist kein schlechter Mensch“, sagt Agnes. „Nur müde.“',
    'c-after3': 'Victor ist unhöflich. Agnes findet, er verdient trotzdem Gehör.',
    's-wit1': 'Kit Marlow, der Lehrling, sagte vor Gericht, er habe um halb drei „einen Schrei, dann einen dumpfen Schlag“ aus dem Treppenhaus gehört.',
    'c-wit1': 'Kit klang ehrlich. Er trug an der Töpferscheibe aber auch Kopfhörer.',
    's-wit2': 'Beweisstück 14: Kits Kopfhörer, auf der Scheibe gefunden. Du kennst dieses Modell. Es blendet fast alles aus.',
    'c-wit2': 'Kits Musik war laut. Ein Schrei könnte trotzdem durchdringen, gerade so.',
    's-wit3': 'Gerald setzt die Kopfhörer selbst auf und spielt Musik. Agnes schreit hinter ihm. Gerald dreht sich nicht um.',
    'c-wit3': 'Gerald hat fast nichts gehört. Er wollte nach Hause. Jetzt will er es richtig machen.',
    's-clock1': 'Die Türklingelkamera eines Nachbarn zeigt, wie Ruths Lieferwagen die Mühle um 14:25 verlässt. Ihr Notruf kommt um 14:52.',
    'c-clock1': 'Simon starb zwischen zwei und drei, die Zeiten entlasten sie also nicht.',
    's-clock2': 'Das Navi des Lieferwagens wurde vor Gericht verlesen: zwölf Minuten zum Tonhändler, zwölf zurück, ein Halt unterwegs.',
    'c-clock2': 'Sie hätte schnell fahren können. Das Navi sagt, sie hielt sich ans Tempolimit.',
    's-clock3': 'Gerald nimmt seine Uhr ab und legt sie auf den Tisch. „Zwölf hin, zwölf zurück und ein Halt. Das geht nicht auf.“',
    'c-clock3': 'Geralds Zug ist ihm wichtig. Die Zeitleiste ist ihm jetzt wichtiger.',
    's-vote1': 'Es steht wieder elf zu eins, diesmal andersherum. Victor schaut auf seine Hände. „Mein Sohn ist auch gegangen. Hat nie gesagt, warum.“',
    'c-vote1': 'Victor leidet. Du verstehst ihn, und du brauchst trotzdem seine Stimme.',
    's-vote2': 'Der Gerichtsdiener klopft. Gerald streckt die Hand nach den Zetteln aus. Victors kommt als letzter auf den Stapel.',
    'c-vote2': 'Du wirst nie wissen, was auf dieser Treppe geschah. Der Zweifel ist vernünftig.',
}
