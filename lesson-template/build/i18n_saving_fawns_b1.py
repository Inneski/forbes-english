# -*- coding: utf-8 -*-
"""Interface strings for Saving Fawns from the Mower (B1) — EN, DE, ES.

German carries over the original scrolling page's own translations (the
`deQ`/`expDE`/`de-para` content it already shipped) rather than being
retranslated from scratch. Spanish is new — the original page was EN+DE
only, and the standing rule since 2026-09-04 is EN+DE+ES as the minimum.

Per house style §8: reading-comprehension questions have no blank, so they
translate whole (stem_key). Vocabulary-in-context and Grammar Focus keep a
blank and stay English — only their explanations translate. The reading
passage and the glossary translate in full, same as the original.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Saving Fawns from the <em>Mower</em>',
    coverSub='Drones, thermal cameras and a rescue network that saves thousands of fawns every spring',
    chipLevel='B1 · Intermediate', chipFocus='Reading, vocabulary and grammar',
    chipCount='40 questions',

    vocEyebrow='Before you read', vocTitle1='Key vocabulary (1/3)',
    vocTitle2='Key vocabulary (2/3)', vocTitle3='Key vocabulary (3/3)',
    t1h='fawn', t1b='a baby deer',
    t2h='doe', t2b='a mother deer',
    t3h='instinct', t3b='natural behaviour, not learned',
    t4h='drone', t4b='a small flying machine, no pilot inside',
    t5h='drone pilot', t5b='the person flying the drone',
    t6h='thermal imaging camera', t6b='a camera that sees heat',
    t7h='combine harvester', t7b='a big machine that cuts fields',
    t8h='volunteer', t8b='a person who helps for free',
    t9h='to mow', t9b='to cut grass or crops with a machine',
    t10h='to spot', t10b='to see or notice something',
    t11h='to relocate', t11b='to move something a short distance',
    t12h='gloves', t12b='you wear these on your hands',

    readEyebrow='The article',
    read1Title='Why fawns are at risk',
    p1h='A simple instinct',
    p1b='Every spring, deer have babies in the tall grass and fields. A baby deer is '
        'called a <strong>fawn</strong>. A fawn has almost no smell, so foxes cannot '
        'find it easily. When a fawn feels danger, it does something simple: it stays '
        'completely still. This works well against foxes. But it does not work against '
        'a big farm machine called a <strong>combine harvester</strong>. The machine '
        'cannot see a small fawn hiding in the grass.',
    read2Title='How drones find them',
    p2h='Eyes in the sky',
    p2b='This is why many volunteers now use drones to help. A <strong>drone</strong> '
        'is a small flying machine with a camera. Early in the morning, the drone flies '
        'over the field. The camera can see body heat. In the cool morning air, a '
        'fawn&rsquo;s warm body is easy to see on the camera. Later in the day, the '
        'whole field gets warm from the sun, so this does not work anymore. That is why '
        'the drone teams fly at dawn.',
    read3Title='What the rescue team does',
    p3h='The rescue',
    p3b='When the drone pilot finds a fawn, a small team walks to it. They wear gloves. '
        'Why? Because the mother deer might not want her baby anymore if it smells like '
        'a human. The team does not carry the fawn far away. They put a box or some '
        'branches over it, near the same spot. This keeps the fawn safe while the '
        'farmer cuts the field. After the work is finished, the team lets the fawn go '
        'again, close to where they found it.',
    read4Title='Who makes it work',
    p4h='Teamwork, and the numbers',
    p4b='This project needs many different people working together: farmers, hunters, '
        'drone pilots, and volunteers. Farmers tell the team when they plan to cut a '
        'field. Then the team can check it first. In German, people call an accident '
        'like this a &ldquo;M&auml;htod&rdquo; &mdash; it means &ldquo;mowing '
        'death&rdquo;. With good teamwork, one region can save many thousands of fawns '
        'every year.',

    rEyebrow='Reading comprehension', rTitle='Answer using the text above',
    r1stem='Why does staying still not help a fawn near a mowing machine?',
    r2stem='Why do drone teams fly early in the morning?',
    r3stem='What happens to a fawn after the team finds it?',
    r4stem='Why do rescue teams wear gloves?',
    r5stem='Who works together in this rescue project, according to the text?',
    r6stem='What German word does the text use for an accidental fawn death caused by mowing?',
    r7stem='What do farmers do to help the rescue team, according to the text?',
    r8stem='According to the text, how many fawns can a region save in one year with good teamwork?',
    r1why='The instinct works against animals like foxes. A machine is different — it '
          'does not see the fawn either way.',
    r2why='In the cool morning, warm bodies stand out clearly on the camera. Later, the '
          'sun warms everything and this difference disappears.',
    r3why='The text says the team covers the fawn nearby and then releases it close to '
          'the same spot after mowing.',
    r4why='The text explains: a mother deer might not want her baby anymore if it '
          'smells of humans.',
    r5why='The text names exactly this group: farmers, hunters, drone pilots, and '
          'volunteers.',
    r6why='"Mähtod" means "mowing death" — the exact word the text gives us.',
    r7why='The text says farmers tell the team their plans, so the team can check the '
          'field before mowing.',
    r8why='The text says one region can save many thousands of fawns every year with '
          'good teamwork.',

    vEyebrow='Vocabulary in context', vTitle='Choose the word that fits',
    v1why='A <b>fawn</b> is a baby deer.',
    v2why='A <b>doe</b> is a mother deer.',
    v3why='An <b>instinct</b> is natural behaviour an animal is born with.',
    v4why='To <b>mow</b> means to cut grass with a machine.',
    v5why='A <b>combine harvester</b> is the big machine that cuts fields.',
    v6why='A <b>thermal imaging camera</b> shows heat, so warm animals are easy to see.',
    v7why='A <b>drone</b> is a small flying machine with a camera.',
    v8why='A <b>drone pilot</b> is a person trained to fly a drone.',
    v9why='A <b>volunteer</b> helps without being paid.',
    v10why='To <b>relocate</b> means to move something, here just a short distance.',

    sortEyebrow='Word sorting', sortTitle='Sort each word into its category',
    sortHint='Match each word to the category it belongs to.',
    sortWhy='People do the rescuing, equipment helps them find and cover a fawn, '
            'animals are what the project protects, and actions describe what '
            'happens during the rescue.',
    catPeople='People &amp; Roles', catEquipment='Equipment',
    catAnimals='Animals', catActions='Actions &amp; Process',

    grammarEyebrow='Before the questions', grammarTitle='Three patterns from the text',
    gc1h='Passive present simple',
    gc1b='Use <strong>am/is/are + past participle</strong> when the action matters '
         'more than who does it: &ldquo;Fawns <em>are found</em> early in the '
         'morning.&rdquo;',
    gc2h='First conditional',
    gc2b='<strong>If + present simple, &hellip; will + infinitive</strong>, for a '
         'real, likely situation: &ldquo;If a pilot <em>spots</em> a fawn early, the '
         'team <em>will have</em> time to help.&rdquo;',
    gc3h='Must, don&rsquo;t have to, should',
    gc3b='<strong>Must</strong> = a strong rule. <strong>Don&rsquo;t have to</strong> '
         '= not necessary. <strong>Should</strong> = friendly advice, not a rule: '
         '&ldquo;You <em>must</em> wear gloves, but you <em>don&rsquo;t have to</em> '
         'carry the fawn far, and you <em>should</em> stay calm.&rdquo;',

    gEyebrow='Grammar focus', gTitle='Choose the correct form',
    g1why='Passive present simple: <b>are found</b> — the sentence is about the '
          'fawns, not about who finds them.',
    g2why='Passive negative present simple: <b>is not touched</b>.',
    g3why='Passive present simple, plural subject: <b>are announced</b>.',
    g4why='Passive present simple: <b>are donated</b> — the cameras receive the '
          'action.',
    g5why='First conditional: <i>if</i> + present simple (<i>spots</i>) + '
          '<i>will</i> + infinitive (<i>will have</i>), for a real, likely '
          'situation.',
    g6why='<i>Checks</i> (present simple condition) + <i>won&rsquo;t survive</i> '
          '(will-future result).',
    g7why='First conditional pattern: <i>will reject</i> (result) + <i>smells</i> '
          '(condition, present simple).',
    g8why='<b>Must</b> shows a strong obligation — something necessary.',
    g9why='<b>Don&rsquo;t have to</b> means something is not necessary, even if '
          'people often choose to do it.',
    g10why='<b>Should</b> gives friendly advice, not a strict rule.',

    actTitle='Talk and write about fawn rescue', actUse='Use at least four:',
    actSpeakBrief='Discuss in pairs or small groups, then compare answers with '
                  'another group.',
    actSpeak1='You are a volunteer drone pilot. Explain to a farmer, in simple '
              'terms, why he must tell your team his mowing dates in advance.',
    actSpeak2='A neighbour says the rescue project is a waste of time and money. '
              'Defend it — use at least one number from the text.',
    actSpeak3='Your team has just found a fawn, and the farmer wants to start '
              'mowing in ten minutes. Decide together, fast, what you do next.',
    actWriteKind='Writing · 150–250 words',
    actWriteBrief='Write a short public notice for local farmers, explaining the '
                  'fawn rescue project and exactly what you need from them before '
                  'they mow.',
    actPlaceholder='Every spring, our team asks farmers to…',

    resPerfect='Full marks. You read the text closely and the grammar patterns are secure.',
    resStrong='Strong. Most of the text and the vocabulary landed — check the '
              'grammar patterns you missed.',
    resMid='A good base. Read the article again, slowly, and look at the passive '
          'and first-conditional examples once more.',
    resLow='Read the article again from the start, then try the questions a '
          'second time. The vocabulary repeats across all four activities.',
)

T['de'] = dict(
    coverTitle='Rehkitzrettung vor dem <em>Mähdrescher</em>',
    coverSub='Drohnen, Wärmebildkameras und ein Rettungsnetzwerk, das jedes Frühjahr '
             'tausende Rehkitze rettet',
    chipLevel='B1 · Mittelstufe', chipFocus='Lesen, Wortschatz und Grammatik',
    chipCount='40 Fragen',

    vocEyebrow='Bevor du liest', vocTitle1='Wichtige Wörter (1/3)',
    vocTitle2='Wichtige Wörter (2/3)', vocTitle3='Wichtige Wörter (3/3)',
    t1h='fawn', t1b='ein Reh-Baby (das Rehkitz)',
    t2h='doe', t2b='eine Rehmutter (die Rehgeiß)',
    t3h='instinct', t3b='natürliches, angeborenes Verhalten (der Instinkt)',
    t4h='drone', t4b='eine kleine Flugmaschine ohne Pilot (die Drohne)',
    t5h='drone pilot', t5b='die Person, die die Drohne fliegt (der/die Drohnenpilot(in))',
    t6h='thermal imaging camera', t6b='eine Kamera, die Wärme sieht (die Wärmebildkamera)',
    t7h='combine harvester', t7b='eine große Maschine, die Felder mäht (der Mähdrescher)',
    t8h='volunteer', t8b='eine Person, die kostenlos hilft (der/die Freiwillige)',
    t9h='to mow', t9b='Gras oder Felder mit einer Maschine schneiden (mähen)',
    t10h='to spot', t10b='etwas sehen oder entdecken (entdecken)',
    t11h='to relocate', t11b='etwas ein kurzes Stück weit bewegen (umsiedeln)',
    t12h='gloves', t12b='die trägt man an den Händen (die Handschuhe)',

    readEyebrow='Der Text',
    read1Title='Warum Rehkitze in Gefahr sind',
    p1h='Ein einfacher Instinkt',
    p1b='Jeden Frühling bekommen Rehe Babys im hohen Gras und auf den Feldern. Ein '
        'Reh-Baby heißt <strong>Rehkitz</strong>. Ein Rehkitz hat fast keinen Geruch, '
        'deshalb finden Füchse es nicht leicht. Wenn ein Rehkitz Gefahr spürt, '
        'macht es etwas Einfaches: Es bleibt völlig still liegen. Das funktioniert '
        'gut gegen Füchse. Aber es funktioniert nicht gegen eine große '
        'Landmaschine, den <strong>Mähdrescher</strong>. Die Maschine kann ein '
        'kleines Rehkitz im Gras nicht sehen.',
    read2Title='Wie Drohnen sie finden',
    p2h='Augen am Himmel',
    p2b='Deshalb helfen jetzt viele Freiwillige mit <strong>Drohnen</strong>. Eine '
        'Drohne ist eine kleine Flugmaschine mit einer Kamera. Früh am Morgen '
        'fliegt die Drohne über das Feld. Die Kamera kann Körperwärme '
        'sehen. In der kühlen Morgenluft ist die Körperwärme eines '
        'Rehkitzes gut auf der Kamera zu erkennen. Später am Tag wird das ganze '
        'Feld von der Sonne warm, deshalb funktioniert das dann nicht mehr. Deshalb '
        'fliegen die Drohnen-Teams bei Sonnenaufgang.',
    read3Title='Was das Rettungsteam macht',
    p3h='Die Rettung',
    p3b='Wenn der Drohnenpilot ein Rehkitz findet, geht ein kleines Team dorthin. Sie '
        'tragen Handschuhe. Warum? Weil die Mutter ihr Baby vielleicht nicht mehr '
        'will, wenn es nach Mensch riecht. Das Team trägt das Rehkitz nicht weit '
        'weg. Sie stellen eine Kiste oder Äste darüber, ganz in der Nähe. '
        'So bleibt das Rehkitz sicher, während der Landwirt das Feld mäht. '
        'Nach der Arbeit lässt das Team das Rehkitz wieder frei, nah an der '
        'Stelle, wo sie es gefunden haben.',
    read4Title='Wer dafür sorgt, dass es funktioniert',
    p4h='Teamarbeit, und die Zahlen',
    p4b='Dieses Projekt braucht viele verschiedene Menschen, die zusammenarbeiten: '
        'Landwirte, Jäger, Drohnenpiloten und Freiwillige. Landwirte sagen dem '
        'Team, wann sie ein Feld mähen wollen. Dann kann das Team es vorher '
        'kontrollieren. Auf Deutsch nennt man so einen Unfall einen '
        '&bdquo;Mähtod&rdquo; &mdash; das bedeutet &bdquo;Tod durch '
        'Mähen&rdquo;. Mit guter Teamarbeit kann eine Region jedes Jahr viele '
        'tausend Rehkitze retten.',

    rEyebrow='Leseverständnis', rTitle='Beantworte mithilfe des Textes oben',
    r1stem='Warum hilft es einem Rehkitz nicht, still liegen zu bleiben, wenn eine '
           'Mähmaschine kommt?',
    r2stem='Warum fliegen die Drohnen-Teams früh am Morgen?',
    r3stem='Was passiert mit einem Rehkitz, nachdem das Team es gefunden hat?',
    r4stem='Warum tragen die Rettungsteams Handschuhe?',
    r5stem='Wer arbeitet laut Text bei diesem Rettungsprojekt zusammen?',
    r6stem='Welches deutsche Wort benutzt der Text für einen versehentlichen '
           'Rehkitz-Tod beim Mähen?',
    r7stem='Was tun Landwirte laut Text, um dem Rettungsteam zu helfen?',
    r8stem='Wie viele Rehkitze kann laut Text eine Region mit guter Teamarbeit in '
           'einem Jahr retten?',
    r1why='Der Instinkt funktioniert gegen Tiere wie Füchse. Eine Maschine ist '
          'anders — sie sieht das Rehkitz so oder so nicht.',
    r2why='In der kühlen Morgenluft heben sich warme Körper deutlich auf '
          'der Kamera ab. Später erwärmt die Sonne alles, und der '
          'Unterschied verschwindet.',
    r3why='Der Text sagt, das Team deckt das Rehkitz in der Nähe zu und lässt '
          'es nach dem Mähen wieder in der Nähe frei.',
    r4why='Der Text erklärt: Eine Rehmutter will ihr Baby vielleicht nicht mehr, '
          'wenn es nach Menschen riecht.',
    r5why='Der Text nennt genau diese Gruppe: Landwirte, Jäger, Drohnenpiloten '
          'und Freiwillige.',
    r6why='&bdquo;Mähtod&rdquo; bedeutet &bdquo;Tod durch Mähen&rdquo; — '
          'genau das Wort aus dem Text.',
    r7why='Der Text sagt, Landwirte teilen dem Team ihre Pläne mit, damit das '
          'Team das Feld vorher kontrollieren kann.',
    r8why='Der Text sagt, eine Region kann mit guter Teamarbeit jedes Jahr viele '
          'tausend Rehkitze retten.',

    vEyebrow='Wortschatz im Kontext', vTitle='Wähle das passende Wort',
    v1why='Ein <b>fawn</b> ist ein Reh-Baby (Rehkitz).',
    v2why='Eine <b>doe</b> ist eine Rehmutter.',
    v3why='Ein <b>instinct</b> ist ein natürliches, angeborenes Verhalten.',
    v4why='<i>to mow</i> bedeutet, Gras mit einer Maschine zu schneiden (mähen).',
    v5why='Ein <b>combine harvester</b> ist die große Maschine, die Felder '
          'mäht (Mähdrescher).',
    v6why='Eine <b>thermal imaging camera</b> zeigt Wärme, deshalb sind warme '
          'Tiere leicht zu sehen (Wärmebildkamera).',
    v7why='Eine <b>drone</b> ist eine kleine Flugmaschine mit Kamera.',
    v8why='Ein <b>drone pilot</b> ist eine Person, die eine Drohne fliegen kann.',
    v9why='Ein <b>volunteer</b> hilft, ohne bezahlt zu werden.',
    v10why='<i>to relocate</i> bedeutet, etwas — hier nur kurz — an einen anderen '
           'Ort zu bringen.',

    sortEyebrow='Wörter sortieren', sortTitle='Sortiere jedes Wort in seine Kategorie',
    sortHint='Ordne jedes Wort der passenden Kategorie zu.',
    sortWhy='Personen retten, Ausrüstung hilft beim Finden und Zudecken eines '
            'Rehkitzes, Tiere sind das, was das Projekt schützt, und Handlungen '
            'beschreiben, was während der Rettung passiert.',
    catPeople='Personen &amp; Rollen', catEquipment='Ausrüstung',
    catAnimals='Tiere', catActions='Handlungen &amp; Ablauf',

    grammarEyebrow='Vor den Fragen', grammarTitle='Drei Muster aus dem Text',
    gc1h='Passiv im Present Simple',
    gc1b='Benutze <strong>am/is/are + Partizip Perfekt</strong>, wenn die Handlung '
         'wichtiger ist als die Person, die sie ausführt: &bdquo;Rehkitze '
         '<em>are found</em> früh am Morgen.&ldquo;',
    gc2h='Erster Konditionalsatz',
    gc2b='<strong>If + Present Simple, &hellip; will + Infinitiv</strong>, für '
         'eine reale, wahrscheinliche Situation: &bdquo;If a pilot <em>spots</em> a '
         'fawn early, the team <em>will have</em> time to help.&ldquo;',
    gc3h='Must, don’t have to, should',
    gc3b='<strong>Must</strong> = eine strenge Regel. <strong>Don’t have '
         'to</strong> = nicht notwendig. <strong>Should</strong> = ein '
         'freundlicher Rat, keine Regel: &bdquo;You <em>must</em> wear gloves, but '
         'you <em>don’t have to</em> carry the fawn far, and you '
         '<em>should</em> stay calm.&ldquo;',

    gEyebrow='Grammatik', gTitle='Wähle die richtige Form',
    g1why='Passiv im Present Simple: <b>are found</b> — der Satz handelt von den '
          'Rehkitzen, nicht davon, wer sie findet.',
    g2why='Passiv verneint im Present Simple: <b>is not touched</b>.',
    g3why='Passiv im Present Simple, Plural-Subjekt: <b>are announced</b>.',
    g4why='Passiv im Present Simple: <b>are donated</b> — die Kameras erhalten die '
          'Handlung.',
    g5why='Erster Konditionalsatz: <i>if</i> + Present Simple (<i>spots</i>) + '
          '<i>will</i> + Infinitiv (<i>will have</i>), für eine reale, '
          'wahrscheinliche Situation.',
    g6why='<i>checks</i> (Bedingung im Present Simple) + <i>won’t survive</i> '
          '(will-future-Ergebnis).',
    g7why='Struktur des ersten Konditionalsatzes: <i>will reject</i> (Ergebnis) + '
          '<i>smells</i> (Bedingung, Present Simple).',
    g8why='<i>must</i> zeigt eine starke Verpflichtung — etwas Notwendiges.',
    g9why='<i>don’t have to</i> bedeutet, dass etwas nicht notwendig ist, auch '
          'wenn es oft trotzdem getan wird.',
    g10why='<i>should</i> gibt einen freundlichen Ratschlag, keine strenge Regel.',

    actTitle='Sprich und schreibe über Rehkitzrettung', actUse='Benutze mindestens vier:',
    actSpeakBrief='Diskutiert zu zweit oder in kleinen Gruppen und vergleicht dann '
                  'eure Antworten mit einer anderen Gruppe.',
    actSpeak1='Du bist ein freiwilliger Drohnenpilot. Erkläre einem Landwirt '
              'einfach, warum er deinem Team seine Mähtermine vorher mitteilen '
              'muss.',
    actSpeak2='Ein Nachbar sagt, das Rettungsprojekt sei Zeit- und Geldverschwendung. '
              'Verteidige es — benutze mindestens eine Zahl aus dem Text.',
    actSpeak3='Euer Team hat gerade ein Rehkitz gefunden, und der Landwirt will in '
              'zehn Minuten mit dem Mähen beginnen. Entscheidet schnell '
              'gemeinsam, was ihr jetzt tut.',
    actWriteKind='Schreiben · 150–250 Wörter',
    actWriteBrief='Schreibe einen kurzen öffentlichen Aushang für '
                  'Landwirte vor Ort, der das Rehkitz-Rettungsprojekt erklärt '
                  'und genau sagt, was du von ihnen vor dem Mähen brauchst.',
    actPlaceholder='Jedes Frühjahr bitten wir Landwirte darum, …',

    resPerfect='Volle Punktzahl. Du hast den Text genau gelesen, und die '
              'Grammatikmuster sitzen.',
    resStrong='Stark. Der Text und der Wortschatz sitzen größtenteils — '
              'überprüfe die Grammatikmuster, die du verpasst hast.',
    resMid='Eine gute Grundlage. Lies den Text noch einmal langsam und schau dir '
          'die Passiv- und Erster-Konditionalsatz-Beispiele noch einmal an.',
    resLow='Lies den Text noch einmal von Anfang an und mach dann die Fragen ein '
          'zweites Mal. Der Wortschatz wiederholt sich in allen vier Übungen.',
)

T['es'] = dict(
    coverTitle='Salvando a los cervatillos de la <em>cosechadora</em>',
    coverSub='Drones, cámaras térmicas y una red de rescate que salva miles de '
             'cervatillos cada primavera',
    chipLevel='B1 · Intermedio', chipFocus='Lectura, vocabulario y gramática',
    chipCount='40 preguntas',

    vocEyebrow='Antes de leer', vocTitle1='Vocabulario clave (1/3)',
    vocTitle2='Vocabulario clave (2/3)', vocTitle3='Vocabulario clave (3/3)',
    t1h='fawn', t1b='una cría de ciervo (el cervatillo)',
    t2h='doe', t2b='una cierva madre',
    t3h='instinct', t3b='un comportamiento natural, no aprendido (el instinto)',
    t4h='drone', t4b='una pequeña máquina voladora sin piloto (el dron)',
    t5h='drone pilot', t5b='la persona que pilota el dron',
    t6h='thermal imaging camera', t6b='una cámara que ve el calor (la cámara térmica)',
    t7h='combine harvester', t7b='una gran máquina que siega los campos (la cosechadora)',
    t8h='volunteer', t8b='una persona que ayuda sin cobrar (el/la voluntario/a)',
    t9h='to mow', t9b='cortar hierba o cultivos con una máquina (segar)',
    t10h='to spot', t10b='ver o detectar algo',
    t11h='to relocate', t11b='mover algo una corta distancia (reubicar)',
    t12h='gloves', t12b='se llevan en las manos (los guantes)',

    readEyebrow='El texto',
    read1Title='Por qué los cervatillos corren peligro',
    p1h='Un instinto sencillo',
    p1b='Cada primavera, los ciervos tienen crías en la hierba alta y en los '
        'campos. A una cría de ciervo se le llama <strong>cervatillo</strong>. '
        'Un cervatillo casi no tiene olor, así que los zorros no lo encuentran '
        'fácilmente. Cuando un cervatillo siente peligro, hace algo sencillo: se '
        'queda completamente quieto. Esto funciona bien contra los zorros. Pero no '
        'funciona contra una gran máquina agrícola llamada '
        '<strong>cosechadora</strong>. La máquina no puede ver a un pequeño '
        'cervatillo escondido en la hierba.',
    read2Title='Cómo los drones los encuentran',
    p2h='Ojos en el cielo',
    p2b='Por eso muchos voluntarios usan ahora drones para ayudar. Un '
        '<strong>dron</strong> es una pequeña máquina voladora con una '
        'cámara. A primera hora de la mañana, el dron vuela sobre el campo. '
        'La cámara puede ver el calor corporal. Con el aire fresco de la '
        'mañana, el cuerpo caliente de un cervatillo se ve fácilmente en la '
        'cámara. Más tarde, todo el campo se calienta con el sol, así '
        'que esto deja de funcionar. Por eso los equipos de drones vuelan al '
        'amanecer.',
    read3Title='Qué hace el equipo de rescate',
    p3h='El rescate',
    p3b='Cuando el piloto del dron encuentra un cervatillo, un pequeño equipo '
        'camina hasta él. Llevan guantes. ¿Por qué? Porque la cierva '
        'madre podría no querer a su cría si huele a humano. El equipo no '
        'se lleva al cervatillo lejos. Le ponen encima una caja o unas ramas, cerca '
        'del mismo sitio. Esto mantiene seguro al cervatillo mientras el agricultor '
        'siega el campo. Cuando termina el trabajo, el equipo deja libre al '
        'cervatillo otra vez, cerca de donde lo encontraron.',
    read4Title='Quién hace que funcione',
    p4h='Trabajo en equipo, y las cifras',
    p4b='Este proyecto necesita a muchas personas diferentes trabajando juntas: '
        'agricultores, cazadores, pilotos de drones y voluntarios. Los agricultores '
        'avisan al equipo de cuándo piensan segar un campo. Así el equipo '
        'puede revisarlo antes. En alemán, a un accidente así se le llama '
        '&ldquo;Mähtod&rdquo; &mdash; significa &ldquo;muerte por '
        'siega&rdquo;. Con buen trabajo en equipo, una región puede salvar '
        'muchos miles de cervatillos cada año.',

    rEyebrow='Comprensión lectora', rTitle='Responde usando el texto de arriba',
    r1stem='¿Por qué quedarse quieto no ayuda a un cervatillo cerca de una '
           'segadora?',
    r2stem='¿Por qué vuelan los equipos de drones a primera hora de la '
           'mañana?',
    r3stem='¿Qué le pasa a un cervatillo después de que el equipo lo '
           'encuentra?',
    r4stem='¿Por qué llevan guantes los equipos de rescate?',
    r5stem='¿Quiénes trabajan juntos en este proyecto de rescate, según '
           'el texto?',
    r6stem='¿Qué palabra alemana usa el texto para una muerte accidental '
           'de un cervatillo causada por la siega?',
    r7stem='¿Qué hacen los agricultores para ayudar al equipo de rescate, '
           'según el texto?',
    r8stem='Según el texto, ¿cuántos cervatillos puede salvar una '
           'región en un año con buen trabajo en equipo?',
    r1why='El instinto funciona contra animales como los zorros. Una máquina '
          'es diferente: no ve al cervatillo de todos modos.',
    r2why='En el fresco de la mañana, los cuerpos calientes destacan claramente '
          'en la cámara. Más tarde, el sol calienta todo y la diferencia '
          'desaparece.',
    r3why='El texto dice que el equipo tapa al cervatillo cerca y luego lo suelta '
          'cerca del mismo sitio después de segar.',
    r4why='El texto explica: una cierva madre podría no querer ya a su cría '
          'si huele a humanos.',
    r5why='El texto nombra exactamente a este grupo: agricultores, cazadores, '
          'pilotos de drones y voluntarios.',
    r6why='&ldquo;Mähtod&rdquo; significa &ldquo;muerte por siega&rdquo; — '
          'exactamente la palabra que da el texto.',
    r7why='El texto dice que los agricultores comparten sus planes con el equipo, '
          'para que el equipo pueda revisar el campo antes de segar.',
    r8why='El texto dice que una región puede salvar muchos miles de '
          'cervatillos cada año con buen trabajo en equipo.',

    vEyebrow='Vocabulario en contexto', vTitle='Elige la palabra que encaja',
    v1why='Un <b>fawn</b> es una cría de ciervo (cervatillo).',
    v2why='Una <b>doe</b> es una cierva madre.',
    v3why='Un <b>instinct</b> es un comportamiento natural con el que nace un '
          'animal.',
    v4why='<i>to mow</i> significa cortar hierba con una máquina (segar).',
    v5why='Una <b>combine harvester</b> es la gran máquina que siega los campos '
          '(cosechadora).',
    v6why='Una <b>thermal imaging camera</b> muestra el calor, por eso los animales '
          'calientes se ven fácilmente (cámara térmica).',
    v7why='Un <b>drone</b> es una pequeña máquina voladora con cámara.',
    v8why='Un <b>drone pilot</b> es una persona entrenada para pilotar un dron.',
    v9why='Un <b>volunteer</b> ayuda sin que le paguen.',
    v10why='<i>to relocate</i> significa mover algo — aquí solo una corta '
           'distancia.',

    sortEyebrow='Clasificar palabras', sortTitle='Clasifica cada palabra en su categoría',
    sortHint='Une cada palabra con la categoría a la que pertenece.',
    sortWhy='Las personas hacen el rescate, el equipo les ayuda a encontrar y tapar '
            'a un cervatillo, los animales son lo que protege el proyecto, y las '
            'acciones describen lo que ocurre durante el rescate.',
    catPeople='Personas y roles', catEquipment='Equipo',
    catAnimals='Animales', catActions='Acciones y proceso',

    grammarEyebrow='Antes de las preguntas', grammarTitle='Tres estructuras del texto',
    gc1h='Voz pasiva en presente simple',
    gc1b='Usa <strong>am/is/are + participio pasado</strong> cuando la acción '
         'importa más que quién la hace: &ldquo;Los cervatillos <em>are '
         'found</em> a primera hora de la mañana.&rdquo;',
    gc2h='Primer condicional',
    gc2b='<strong>If + presente simple, &hellip; will + infinitivo</strong>, para '
         'una situación real y probable: &ldquo;If a pilot <em>spots</em> a '
         'fawn early, the team <em>will have</em> time to help.&rdquo;',
    gc3h='Must, don’t have to, should',
    gc3b='<strong>Must</strong> = una regla estricta. <strong>Don’t have '
         'to</strong> = no es necesario. <strong>Should</strong> = un consejo '
         'amistoso, no una regla: &ldquo;You <em>must</em> wear gloves, but you '
         '<em>don’t have to</em> carry the fawn far, and you <em>should</em> '
         'stay calm.&rdquo;',

    gEyebrow='Gramática', gTitle='Elige la forma correcta',
    g1why='Voz pasiva en presente simple: <b>are found</b> — la frase habla de '
          'los cervatillos, no de quién los encuentra.',
    g2why='Voz pasiva negativa en presente simple: <b>is not touched</b>.',
    g3why='Voz pasiva en presente simple, sujeto plural: <b>are announced</b>.',
    g4why='Voz pasiva en presente simple: <b>are donated</b> — las cámaras '
          'reciben la acción.',
    g5why='Primer condicional: <i>if</i> + presente simple (<i>spots</i>) + '
          '<i>will</i> + infinitivo (<i>will have</i>), para una situación '
          'real y probable.',
    g6why='<i>checks</i> (condición en presente simple) + <i>won’t '
          'survive</i> (resultado con will-future).',
    g7why='Estructura del primer condicional: <i>will reject</i> (resultado) + '
          '<i>smells</i> (condición, presente simple).',
    g8why='<b>Must</b> indica una obligación fuerte — algo necesario.',
    g9why='<b>Don’t have to</b> significa que algo no es necesario, aunque '
          'mucha gente lo haga igualmente.',
    g10why='<b>Should</b> da un consejo amistoso, no una regla estricta.',

    actTitle='Habla y escribe sobre el rescate de cervatillos',
    actUse='Usa al menos cuatro:',
    actSpeakBrief='Discutid en parejas o en grupos pequeños, y luego comparad '
                  'vuestras respuestas con otro grupo.',
    actSpeak1='Eres un piloto de dron voluntario. Explícale a un agricultor, '
              'en términos sencillos, por qué debe avisar a tu equipo de '
              'sus fechas de siega con antelación.',
    actSpeak2='Un vecino dice que el proyecto de rescate es una pérdida de '
              'tiempo y dinero. Defiéndelo usando al menos una cifra del texto.',
    actSpeak3='Vuestro equipo acaba de encontrar un cervatillo, y el agricultor '
              'quiere empezar a segar en diez minutos. Decidid juntos, rápido, '
              'qué hacéis a continuación.',
    actWriteKind='Escritura · 150–250 palabras',
    actWriteBrief='Escribe un breve aviso público para los agricultores de la '
                  'zona, explicando el proyecto de rescate de cervatillos y '
                  'exactamente qué necesitas de ellos antes de que sieguen.',
    actPlaceholder='Cada primavera, nuestro equipo pide a los agricultores que…',

    resPerfect='Puntuación perfecta. Has leído el texto con atención y '
              'las estructuras gramaticales están asentadas.',
    resStrong='Muy bien. La mayoría del texto y el vocabulario se entienden — '
              'revisa las estructuras gramaticales que fallaste.',
    resMid='Buena base. Lee el artículo otra vez, despacio, y repasa los '
          'ejemplos de voz pasiva y primer condicional.',
    resLow='Lee el artículo otra vez desde el principio y luego intenta las '
          'preguntas una segunda vez. El vocabulario se repite en las cuatro '
          'actividades.',
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
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
