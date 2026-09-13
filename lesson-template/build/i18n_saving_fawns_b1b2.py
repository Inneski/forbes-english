# -*- coding: utf-8 -*-
"""Interface strings for Saving Fawns from the Mower (B1-B2) — EN, DE, ES.

German carries over the original scrolling page's own translations. Spanish
is new — the original was EN+DE only; EN+DE+ES has been the standing
minimum since 2026-09-04.
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
    coverSub='Every spring, drone pilots fly thermal cameras over fields at dawn to find '
             'fawns hidden in the grass — before the combine harvesters arrive',
    chipLevel='B1&ndash;B2 · Upper intermediate', chipFocus='Reading, vocabulary and grammar',
    chipCount='40 questions',

    vocEyebrow='Before you read', vocTitle1='Key vocabulary (1/2)', vocTitle2='Key vocabulary (2/2)',
    t1h='fawn', t1b='a young deer, especially with its mother',
    t2h='doe', t2b='a female deer, the mother of a fawn',
    t3h='instinct', t3b='natural, unlearned behaviour',
    t4h='combine harvester', t4b='a large machine that cuts and processes crops',
    t5h='thermal imaging camera', t5b='a camera that detects heat instead of light',
    t6h='to relocate', t6b='to move something to a different place, often temporarily',

    readEyebrow='The article',
    read1Title='Why the freezing instinct fails',
    p1h='An instinct with no answer for machines',
    p1b='Every spring, deer give birth in the tall grass and meadows of the countryside. A '
        'newborn fawn has almost no scent and cannot run fast, so its main defence against '
        'danger is a simple instinct: freeze completely still and stay hidden in the grass. '
        'This instinct works well against foxes and wild boar &mdash; but it fails '
        'completely against something a fawn has never evolved to recognise: a '
        '<strong>combine harvester</strong>. A farmer cutting a field in early summer often '
        'cannot see a fawn lying motionless in the grass until it is far too late.',
    read2Title='Reading the field from above',
    p2h='Eyes in the cool morning air',
    p2b='This is why a growing network of volunteers now flies drones fitted with '
        '<strong>thermal imaging cameras</strong> over fields in the very early morning, '
        'just before the mowing season begins. At dawn, the ground is still cool, and a '
        "fawn's body heat stands out clearly on camera as a bright shape against a cool, "
        'dark background &mdash; a difference that disappears by mid-morning, once the sun '
        'has warmed the whole field.',
    read3Title='A careful, temporary rescue',
    p3h='Minimal contact, minimal disturbance',
    p3b='When a drone pilot spots a fawn, they alert a small ground team, who approach the '
        'animal carefully &mdash; usually wearing gloves and avoiding leaving their scent '
        'behind, since a doe may reject a fawn that smells of humans. The fawn isn&rsquo;t '
        'carried away. Instead, it&rsquo;s temporarily placed under a box or behind a '
        'barrier of cut branches, safely out of the mower&rsquo;s path. Once the field has '
        'been cut, the fawn is released again close to where it was found, so the doe can '
        'find it.',
    read4Title='A network that depends on cooperation',
    p4h='Farmers, hunters, pilots and volunteers',
    p4b='This work depends on close cooperation between people who don&rsquo;t always see '
        'the countryside the same way: farmers, hunters, drone pilots, and volunteer '
        'conservationists. Farmers announce their mowing dates in advance; hunters and '
        'local rescue groups organise teams; drone pilots donate their time and their '
        'expensive thermal equipment. In German, conservationists sometimes call an '
        'unnecessary fawn death the &ldquo;M&auml;htod&rdquo; &mdash; literally, '
        '&ldquo;mowing death.&rdquo; In a single season, a well-organised regional network '
        'can locate and relocate several thousand fawns before the blades ever reach them.',

    rEyebrow='Reading comprehension', rTitle='Answer based on the article above',
    r1stem="Why does a fawn's freezing instinct fail against farm machinery?",
    r2stem='According to the text, when do drone teams usually fly over the fields, and why?',
    r3stem='What happens to a fawn once a drone pilot finds it?',
    r4stem='Why do rescue teams avoid touching fawns with bare hands?',
    r5stem='Who is involved in the rescue network described in the article?',
    r6stem='What German term does the article mention for an unnecessary fawn death caused by mowing?',
    r7stem='What role does the farmer play in the network described?',
    r8stem='According to the article, how many fawns can a well-organised regional network relocate in a single season?',
    r1why='The article explains the instinct evolved against predators like foxes, not '
          'machines — freezing offers no protection from a mower.',
    r2why="At dawn, the ground is still cool, so a fawn's body heat contrasts sharply on a thermal camera.",
    r3why='The article describes a temporary, local relocation — under a box or behind cut '
          'branches — followed by release nearby.',
    r4why='The article notes that a doe may reject a fawn carrying a human scent, so '
          'rescuers wear gloves.',
    r5why='The article lists exactly this mix of people cooperating: farmers, hunters, '
          'drone pilots, and volunteers.',
    r6why='"Mähtod" literally means "mowing death" — the term the article gives for '
          'this kind of accident.',
    r7why='The article says farmers announce their mowing dates in advance, which lets '
          'rescue teams organise around them.',
    r8why='The article states that a well-organised network across one region can relocate '
          'several thousand fawns per season.',

    vEyebrow='Vocabulary in context', vTitle='Choose the word that fits',
    v1why='A <b>fawn</b> is a young deer — the animal at the centre of this whole rescue effort.',
    v2why='A <b>doe</b> is a female deer — the mother of a fawn.',
    v3why='An <b>instinct</b> is unlearned, natural behaviour an animal is born with.',
    v4why='To <b>mow</b> means to cut grass or crops with a machine.',
    v5why='A <b>combine harvester</b> is the large machine that cuts and processes crops.',
    v6why='A <b>thermal imaging camera</b> shows heat differences rather than visible light.',
    v7why='A <b>drone</b> is a small remotely-controlled flying aircraft, ideal for '
          'searching fields from above.',
    v8why='A <b>drone pilot</b> is a person trained to fly a drone.',
    v9why='A <b>volunteer</b> offers to help without being paid.',
    v10why='To <b>relocate</b> means to move something to a different place, here temporarily.',

    sortEyebrow='Word sorting', sortTitle='Sort each word into its category',
    sortHint='Match each word to the category it belongs to.',
    sortWhy='People do the rescuing, equipment helps them find and shield a fawn, animals '
            'are what the network protects, and actions describe what happens during the '
            'rescue.',
    catPeople='People &amp; Roles', catEquipment='Equipment',
    catAnimals='Animals', catActions='Actions &amp; Process',

    grammarEyebrow='Before the questions', grammarTitle='Three patterns from the article',
    gc1h='Passive present simple',
    gc1b='Use <strong>am/is/are + past participle</strong> when the action matters more '
         'than who does it: &ldquo;Thousands of fawns <em>are found</em> hidden in fields '
         'across the countryside.&rdquo;',
    gc2h='First conditional',
    gc2b='<strong>If + present simple, &hellip; will + infinitive</strong>, for a real, '
         'likely situation: &ldquo;If a pilot <em>spots</em> a fawn early, the team '
         '<em>will have</em> time to act.&rdquo;',
    gc3h='Must, don&rsquo;t have to, should',
    gc3b='<strong>Must</strong> = an essential rule. <strong>Don&rsquo;t have to</strong> = '
         'not legally necessary. <strong>Should</strong> = sensible advice, not a rule: '
         '&ldquo;You <em>must</em> wear gloves, farmers <em>don&rsquo;t have to</em> report '
         'mowing dates by law, and you <em>should</em> approach a fawn calmly.&rdquo;',

    gEyebrow='Grammar focus', gTitle='Choose the correct form',
    g1why='Passive present simple: <b>are found</b> — the focus is on the fawns, not on '
          'who finds them.',
    g2why='Passive negative present simple: <b>is not touched</b>.',
    g3why='Passive present simple with plural subject: <b>are announced</b>.',
    g4why='Passive present simple: <b>are donated</b> — the cameras are the subject, '
          'receiving the action.',
    g5why='First conditional: <i>if</i> + present simple (<i>spots</i>), + <i>will</i> + '
          'infinitive (<i>will have</i>), for a real, likely situation.',
    g6why='<i>Checks</i> (present simple condition) + <i>won&rsquo;t survive</i> '
          '(will-future result) — a real, general possibility.',
    g7why='First conditional pattern: <i>will reject</i> (result) + <i>smells</i> '
          '(condition, present simple).',
    g8why='<b>Must</b> expresses a strong obligation — something essential, not optional.',
    g9why='<b>Don&rsquo;t have to</b> means something isn&rsquo;t legally necessary, even '
          'if people often choose to do it.',
    g10why='<b>Should</b> gives sensible advice or a recommendation, rather than a strict rule.',

    actTitle='Talk and write about fawn rescue', actUse='Use at least four:',
    actSpeakBrief='Discuss in pairs or small groups, then compare answers with another group.',
    actSpeak1='You are a volunteer drone pilot. Explain to a farmer, in clear terms, why he '
              'must tell your team his mowing dates in advance.',
    actSpeak2='A neighbour says the rescue network is a waste of time and money. Defend it '
              '&mdash; use at least one figure from the article.',
    actSpeak3='Your team has just found a fawn, and the farmer wants to start mowing in ten '
              'minutes. Decide together, fast, what you do next.',
    actWriteKind='Writing · 150&ndash;250 words',
    actWriteBrief='Write a short public notice for local farmers, explaining the fawn '
                  'rescue network and exactly what you need from them before they mow.',
    actPlaceholder='Every spring, our network asks farmers to&hellip;',

    resPerfect='Full marks. You read the article closely and the grammar patterns are secure.',
    resStrong='Strong. Most of the article and the vocabulary landed — check the grammar '
              'patterns you missed.',
    resMid='A good base. Read the article again, slowly, and look at the passive and '
          'first-conditional examples once more.',
    resLow='Read the article again from the start, then try the questions a second time. '
          'The vocabulary repeats across all four activities.',
)

T['de'] = dict(
    coverTitle='Rehkitze vor dem <em>Mähdrescher</em>',
    coverSub='Jeden Frühling fliegen Drohnenpiloten bei Morgendämmerung mit '
             'Wärmebildkameras über die Felder, um versteckte Rehkitze im Gras '
             'zu finden — bevor die Mähdrescher eintreffen',
    chipLevel='B1&ndash;B2 · Obere Mittelstufe', chipFocus='Lesen, Wortschatz und Grammatik',
    chipCount='40 Fragen',

    vocEyebrow='Bevor du liest', vocTitle1='Wichtige Wörter (1/2)', vocTitle2='Wichtige Wörter (2/2)',
    t1h='fawn', t1b='ein junges Reh, besonders mit seiner Mutter (das Rehkitz)',
    t2h='doe', t2b='ein weibliches Reh, die Mutter eines Kitzes (die Rehgeiß / Ricke)',
    t3h='instinct', t3b='natürliches, nicht erlerntes Verhalten (der Instinkt)',
    t4h='combine harvester', t4b='eine große Maschine, die Getreide schneidet und verarbeitet (der Mähdrescher)',
    t5h='thermal imaging camera', t5b='eine Kamera, die Wärme statt Licht erkennt (die Wärmebildkamera)',
    t6h='to relocate', t6b='etwas — oft vorübergehend — an einen anderen Ort bringen (umsiedeln)',

    readEyebrow='Der Artikel',
    read1Title='Warum der Instinkt versagt',
    p1h='Ein Instinkt ohne Antwort auf Maschinen',
    p1b='Jedes Frühjahr bringen Rehe ihre Jungen im hohen Gras und auf den Wiesen der '
        'Landschaft zur Welt. Ein neugeborenes Rehkitz hat fast keinen Eigengeruch und kann '
        'nicht schnell laufen, deshalb ist seine wichtigste Verteidigung ein einfacher '
        'Instinkt: völlig regungslos verharren und sich im Gras verstecken. Dieser '
        'Instinkt funktioniert gut gegen Füchse und Wildschweine — versagt aber '
        'vollständig gegenüber etwas, das ein Rehkitz nie kennengelernt hat: '
        'einen <strong>Mähdrescher</strong>. Ein Landwirt, der im Frühsommer ein '
        'Feld mäht, kann ein reglos daliegendes Kitz im Gras oft erst viel zu spät sehen.',
    read2Title='Das Feld von oben lesen',
    p2h='Augen in der kühlen Morgenluft',
    p2b='Deshalb fliegt ein wachsendes Netzwerk von Freiwilligen inzwischen mit '
        '<strong>Wärmebildkameras</strong> ausgestattete Drohnen sehr früh morgens '
        'über die Felder, kurz bevor die Mähsaison beginnt. Bei Sonnenaufgang ist '
        'der Boden noch kühl, und die Körperwärme eines Rehkitzes hebt sich '
        'auf der Kamera deutlich als heller Fleck vor dem kühlen, dunklen Hintergrund '
        'ab — ein Unterschied, der bis zum späten Vormittag verschwindet, sobald die '
        'Sonne das ganze Feld erwärmt hat.',
    read3Title='Eine vorsichtige, vorübergehende Rettung',
    p3h='Minimaler Kontakt, minimale Störung',
    p3b='Entdeckt ein Drohnenpilot ein Rehkitz, alarmiert er ein kleines Bodenteam, das sich '
        'dem Tier vorsichtig nähert — meist mit Handschuhen, um keinen menschlichen '
        'Geruch zu hinterlassen, da eine Ricke ein nach Mensch riechendes Kitz verstoßen '
        'könnte. Das Kitz wird nicht weggetragen, sondern vorübergehend unter '
        'einer Kiste oder hinter einer Barriere aus geschnittenen Ästen versteckt, '
        'sicher außerhalb der Mähbahn. Nach dem Mähen wird das Kitz wieder in '
        'der Nähe seines Fundorts freigelassen, damit die Ricke es wiederfindet.',
    read4Title='Ein Netzwerk, das auf Zusammenarbeit beruht',
    p4h='Landwirte, Jäger, Piloten und Freiwillige',
    p4b='Diese Arbeit hängt von enger Zusammenarbeit zwischen Menschen ab, die die '
        'Landschaft nicht immer gleich betrachten: Landwirten, Jägern, Drohnenpiloten '
        'und ehrenamtlichen Naturschützern. Landwirte kündigen ihre Mähtermine '
        'im Voraus an; Jäger und örtliche Rettungsgruppen organisieren Teams; '
        'Drohnenpiloten spenden ihre Zeit und ihre teure Wärmebildausrüstung. Auf '
        'Deutsch nennen Naturschützer einen unnötigen Rehkitztod manchmal '
        '&bdquo;Mähtod&rdquo;. In einer einzigen Saison kann ein gut organisiertes '
        'regionales Netzwerk mehrere tausend Rehkitze aufspüren und retten, bevor die '
        'Messer sie erreichen.',

    rEyebrow='Leseverständnis', rTitle='Beantworte anhand des Artikels oben',
    r1stem='Warum versagt der Erstarrungsinstinkt eines Rehkitzes gegen Landmaschinen?',
    r2stem='Wann fliegen Drohnenteams laut Text üblicherweise über die Felder, und '
           'warum?',
    r3stem='Was passiert mit einem Rehkitz, sobald ein Drohnenpilot es findet?',
    r4stem='Warum vermeiden Rettungsteams es, Rehkitze mit bloßen Händen zu berühren?',
    r5stem='Wer ist laut Artikel an dem beschriebenen Rettungsnetzwerk beteiligt?',
    r6stem='Welchen deutschen Begriff nennt der Artikel für einen unnötigen, durch '
           'das Mähen verursachten Rehkitztod?',
    r7stem='Welche Rolle spielt der Landwirt in dem beschriebenen Netzwerk?',
    r8stem='Wie viele Rehkitze kann laut Artikel ein gut organisiertes regionales Netzwerk '
           'in einer einzigen Saison retten?',
    r1why='Der Instinkt hat sich gegen Fressfeinde wie Füchse entwickelt, nicht gegen '
          'Maschinen — Stillhalten schützt nicht vor einem Mähwerk.',
    r2why='Bei Morgendämmerung ist der Boden noch kühl, sodass sich die '
          'Körperwärme eines Kitzes auf der Wärmebildkamera deutlich abhebt.',
    r3why='Der Artikel beschreibt eine vorübergehende, örtliche Umsiedlung — unter '
          'einer Kiste oder hinter Astwerk — mit anschließender Freilassung in der Nähe.',
    r4why='Laut Artikel kann eine Ricke ein Kitz ablehnen, das nach Menschen riecht, '
          'deshalb tragen Helfer Handschuhe.',
    r5why='Der Artikel nennt genau diese Gruppe von Mitwirkenden: Landwirte, Jäger, '
          'Drohnenpiloten und Freiwillige.',
    r6why='&bdquo;Mähtod&rdquo; bedeutet wörtlich &bdquo;Tod durch Mähen&rdquo; '
          '— genau der Begriff, den der Artikel dafür nennt.',
    r7why='Der Artikel sagt, Landwirte geben ihre Mähtermine im Voraus bekannt, damit '
          'sich Rettungsteams danach richten können.',
    r8why='Der Artikel besagt, dass ein gut organisiertes regionales Netzwerk mehrere '
          'Tausend Kitze pro Saison retten kann.',

    vEyebrow='Wortschatz im Kontext', vTitle='Wähle das passende Wort',
    v1why='Ein <b>fawn</b> ist ein junges Reh — das Tier, um das sich diese ganze '
          'Rettungsaktion dreht.',
    v2why='Eine <b>doe</b> ist ein weibliches Reh — die Mutter eines Kitzes.',
    v3why='Ein <b>instinct</b> ist angeborenes, nicht erlerntes Verhalten.',
    v4why='<i>to mow</i> bedeutet, Gras oder Getreide mit einer Maschine zu schneiden '
          '(mähen).',
    v5why='Ein <b>combine harvester</b> ist die große Maschine, die Getreide schneidet '
          'und verarbeitet (Mähdrescher).',
    v6why='Eine <b>thermal imaging camera</b> zeigt Wärmeunterschiede statt sichtbarem '
          'Licht (Wärmebildkamera).',
    v7why='Eine <b>drone</b> ist ein kleines, ferngesteuertes Fluggerät, ideal zum '
          'Absuchen von Feldern von oben.',
    v8why='Ein <b>drone pilot</b> ist eine Person, die ausgebildet ist, eine Drohne zu fliegen.',
    v9why='Ein <b>volunteer</b> hilft freiwillig, ohne bezahlt zu werden.',
    v10why='<i>to relocate</i> bedeutet, etwas — hier vorübergehend — an einen anderen '
           'Ort zu bringen.',

    sortEyebrow='Wörter sortieren', sortTitle='Sortiere jedes Wort in seine Kategorie',
    sortHint='Ordne jedes Wort der passenden Kategorie zu.',
    sortWhy='Personen retten, Ausrüstung hilft beim Finden und Schützen eines '
            'Rehkitzes, Tiere sind das, was das Netzwerk schützt, und Handlungen '
            'beschreiben, was während der Rettung passiert.',
    catPeople='Personen &amp; Rollen', catEquipment='Ausrüstung',
    catAnimals='Tiere', catActions='Handlungen &amp; Ablauf',

    grammarEyebrow='Vor den Fragen', grammarTitle='Drei Muster aus dem Artikel',
    gc1h='Passiv im Present Simple',
    gc1b='Benutze <strong>am/is/are + Partizip Perfekt</strong>, wenn die Handlung '
         'wichtiger ist als die Person, die sie ausführt: &bdquo;Thousands of fawns '
         '<em>are found</em> hidden in fields across the countryside.&ldquo;',
    gc2h='Erster Konditionalsatz',
    gc2b='<strong>If + Present Simple, &hellip; will + Infinitiv</strong>, für eine '
         'reale, wahrscheinliche Situation: &bdquo;If a pilot <em>spots</em> a fawn early, '
         'the team <em>will have</em> time to act.&ldquo;',
    gc3h='Must, don’t have to, should',
    gc3b='<strong>Must</strong> = eine wesentliche Regel. <strong>Don’t have '
         'to</strong> = rechtlich nicht notwendig. <strong>Should</strong> = ein '
         'sinnvoller Rat, keine Regel: &bdquo;You <em>must</em> wear gloves, farmers '
         '<em>don’t have to</em> report mowing dates by law, and you '
         '<em>should</em> approach a fawn calmly.&ldquo;',

    gEyebrow='Grammatik', gTitle='Wähle die richtige Form',
    g1why='Passiv im Present Simple: <b>are found</b> — der Fokus liegt auf den Kitzen, '
          'nicht darauf, wer sie findet.',
    g2why='Passiv verneint im Present Simple: <b>is not touched</b>.',
    g3why='Passiv im Present Simple mit Plural-Subjekt: <b>are announced</b>.',
    g4why='Passiv im Present Simple: <b>are donated</b> — die Kameras sind das Subjekt und '
          'erhalten die Handlung.',
    g5why='Erster Konditionalsatz: <i>if</i> + Present Simple (<i>spots</i>), + '
          '<i>will</i> + Infinitiv (<i>will have</i>), für eine reale, '
          'wahrscheinliche Situation.',
    g6why='<i>checks</i> (Bedingung im Present Simple) + <i>won’t survive</i> '
          '(will-future-Ergebnis) — eine reale, allgemeine Möglichkeit.',
    g7why='Struktur des ersten Konditionalsatzes: <i>will reject</i> (Ergebnis) + '
          '<i>smells</i> (Bedingung, Present Simple).',
    g8why='<i>must</i> drückt eine starke Verpflichtung aus — etwas Wesentliches, '
          'nicht Optionales.',
    g9why='<i>don’t have to</i> bedeutet, dass etwas rechtlich nicht notwendig ist, '
          'auch wenn es oft freiwillig getan wird.',
    g10why='<i>should</i> gibt einen sinnvollen Ratschlag oder eine Empfehlung, keine '
           'strenge Regel.',

    actTitle='Sprich und schreibe über Rehkitzrettung', actUse='Benutze mindestens vier:',
    actSpeakBrief='Diskutiert zu zweit oder in kleinen Gruppen und vergleicht dann eure '
                  'Antworten mit einer anderen Gruppe.',
    actSpeak1='Du bist ein freiwilliger Drohnenpilot. Erkläre einem Landwirt klar, '
              'warum er deinem Team seine Mähtermine vorher mitteilen muss.',
    actSpeak2='Ein Nachbar sagt, das Rettungsnetzwerk sei Zeit- und Geldverschwendung. '
              'Verteidige es — benutze mindestens eine Zahl aus dem Artikel.',
    actSpeak3='Euer Team hat gerade ein Rehkitz gefunden, und der Landwirt will in zehn '
              'Minuten mit dem Mähen beginnen. Entscheidet schnell gemeinsam, was ihr '
              'jetzt tut.',
    actWriteKind='Schreiben · 150–250 Wörter',
    actWriteBrief='Schreibe einen kurzen öffentlichen Aushang für Landwirte vor '
                  'Ort, der das Rehkitz-Rettungsnetzwerk erklärt und genau sagt, was du '
                  'von ihnen vor dem Mähen brauchst.',
    actPlaceholder='Jedes Frühjahr bittet unser Netzwerk Landwirte darum, …',

    resPerfect='Volle Punktzahl. Du hast den Artikel genau gelesen, und die Grammatikmuster sitzen.',
    resStrong='Stark. Der Artikel und der Wortschatz sitzen größtenteils — '
              'überprüfe die Grammatikmuster, die du verpasst hast.',
    resMid='Eine gute Grundlage. Lies den Artikel noch einmal langsam und schau dir die '
          'Passiv- und Erster-Konditionalsatz-Beispiele noch einmal an.',
    resLow='Lies den Artikel noch einmal von Anfang an und mach dann die Fragen ein zweites '
          'Mal. Der Wortschatz wiederholt sich in allen vier Übungen.',
)

T['es'] = dict(
    coverTitle='Salvando a los cervatillos de la <em>cosechadora</em>',
    coverSub='Cada primavera, los pilotos de drones sobrevuelan los campos al amanecer con '
             'cámaras térmicas para encontrar cervatillos escondidos en la hierba '
             'antes de que lleguen las cosechadoras',
    chipLevel='B1&ndash;B2 · Intermedio alto', chipFocus='Lectura, vocabulario y gramática',
    chipCount='40 preguntas',

    vocEyebrow='Antes de leer', vocTitle1='Vocabulario clave (1/2)', vocTitle2='Vocabulario clave (2/2)',
    t1h='fawn', t1b='una cría de ciervo, sobre todo junto a su madre',
    t2h='doe', t2b='una cierva, la madre de un cervatillo',
    t3h='instinct', t3b='un comportamiento natural y no aprendido (el instinto)',
    t4h='combine harvester', t4b='una gran máquina que siega y procesa cultivos (la cosechadora)',
    t5h='thermal imaging camera', t5b='una cámara que detecta calor en vez de luz (la cámara térmica)',
    t6h='to relocate', t6b='mover algo a otro lugar, a menudo temporalmente (reubicar)',

    readEyebrow='El texto',
    read1Title='Por qué falla el instinto de quedarse quieto',
    p1h='Un instinto sin respuesta ante las máquinas',
    p1b='Cada primavera, los ciervos tienen crías en la hierba alta y los prados del '
        'campo. Un cervatillo recién nacido casi no tiene olor y no puede correr '
        'rápido, así que su principal defensa contra el peligro es un instinto '
        'sencillo: quedarse completamente inmóvil y esconderse en la hierba. Este '
        'instinto funciona bien contra zorros y jabalíes &mdash; pero falla por '
        'completo ante algo que un cervatillo nunca ha aprendido a reconocer: una '
        '<strong>cosechadora</strong>. Un agricultor que siega un campo a principios de '
        'verano a menudo no puede ver a un cervatillo inmóvil en la hierba hasta que '
        'ya es demasiado tarde.',
    read2Title='Leyendo el campo desde el aire',
    p2h='Ojos en el aire fresco de la mañana',
    p2b='Por eso una red creciente de voluntarios sobrevuela ahora los campos con drones '
        'equipados con <strong>cámaras térmicas</strong>, muy temprano por la '
        'mañana, justo antes de que empiece la temporada de siega. Al amanecer, el '
        'suelo todavía está frío, y el calor corporal de un cervatillo '
        'destaca claramente en la cámara como una forma brillante sobre un fondo '
        'frío y oscuro &mdash; una diferencia que desaparece a media mañana, en '
        'cuanto el sol ha calentado todo el campo.',
    read3Title='Un rescate cuidadoso y temporal',
    p3h='Contacto mínimo, molestia mínima',
    p3b='Cuando un piloto de dron localiza un cervatillo, avisa a un pequeño equipo en '
        'tierra, que se acerca al animal con cuidado &mdash; normalmente con guantes y '
        'evitando dejar su olor, ya que una cierva podría rechazar a un cervatillo que '
        'huela a humano. El cervatillo no se lleva a otro sitio. En su lugar, se coloca '
        'temporalmente bajo una caja o detrás de una barrera de ramas cortadas, a '
        'salvo del paso de la segadora. Una vez segado el campo, el cervatillo se suelta '
        'de nuevo cerca de donde fue encontrado, para que la cierva pueda encontrarlo.',
    read4Title='Una red que depende de la cooperación',
    p4h='Agricultores, cazadores, pilotos y voluntarios',
    p4b='Este trabajo depende de una estrecha cooperación entre personas que no '
        'siempre ven el campo de la misma manera: agricultores, cazadores, pilotos de '
        'drones y voluntarios conservacionistas. Los agricultores avisan de sus fechas de '
        'siega con antelación; los cazadores y los grupos de rescate locales organizan '
        'equipos; los pilotos de drones donan su tiempo y su costoso equipo térmico. '
        'En alemán, los conservacionistas a veces llaman a una muerte innecesaria de '
        'un cervatillo &ldquo;Mähtod&rdquo; &mdash; literalmente, &ldquo;muerte por '
        'siega&rdquo;. En una sola temporada, una red regional bien organizada puede '
        'localizar y reubicar varios miles de cervatillos antes de que las cuchillas '
        'lleguen hasta ellos.',

    rEyebrow='Comprensión lectora', rTitle='Responde basándote en el texto de arriba',
    r1stem='¿Por qué falla el instinto de quedarse quieto de un cervatillo ante la '
           'maquinaria agrícola?',
    r2stem='Según el texto, ¿cuándo suelen volar los equipos de drones sobre '
           'los campos, y por qué?',
    r3stem='¿Qué le ocurre a un cervatillo una vez que un piloto de dron lo '
           'encuentra?',
    r4stem='¿Por qué evitan los equipos de rescate tocar a los cervatillos con '
           'las manos desnudas?',
    r5stem='¿Quién participa en la red de rescate descrita en el artículo?',
    r6stem='¿Qué término alemán menciona el artículo para una '
           'muerte innecesaria de un cervatillo causada por la siega?',
    r7stem='¿Qué papel juega el agricultor en la red descrita?',
    r8stem='Según el artículo, ¿cuántos cervatillos puede reubicar una '
           'red regional bien organizada en una sola temporada?',
    r1why='El artículo explica que el instinto evolucionó contra depredadores '
          'como los zorros, no contra máquinas — quedarse quieto no protege de una '
          'segadora.',
    r2why='Al amanecer, el suelo todavía está frío, así que el calor '
          'corporal de un cervatillo contrasta claramente en una cámara térmica.',
    r3why='El artículo describe una reubicación temporal y local — bajo una caja '
          'o detrás de ramas cortadas — seguida de la suelta cerca de allí.',
    r4why='El artículo señala que una cierva puede rechazar a un cervatillo que '
          'lleva olor humano, por eso los rescatadores llevan guantes.',
    r5why='El artículo enumera exactamente esta mezcla de personas cooperando: '
          'agricultores, cazadores, pilotos de drones y voluntarios.',
    r6why='&ldquo;Mähtod&rdquo; significa literalmente &ldquo;muerte por siega&rdquo; '
          '— el término que da el artículo para este tipo de accidente.',
    r7why='El artículo dice que los agricultores avisan de sus fechas de siega con '
          'antelación, lo que permite a los equipos de rescate organizarse.',
    r8why='El artículo afirma que una red bien organizada en una región puede '
          'reubicar varios miles de cervatillos por temporada.',

    vEyebrow='Vocabulario en contexto', vTitle='Elige la palabra que encaja',
    v1why='Un <b>fawn</b> es una cría de ciervo — el animal en el centro de todo este '
          'esfuerzo de rescate.',
    v2why='Una <b>doe</b> es una cierva — la madre de un cervatillo.',
    v3why='Un <b>instinct</b> es un comportamiento natural y no aprendido con el que nace '
          'un animal.',
    v4why='<i>to mow</i> significa cortar hierba o cultivos con una máquina (segar).',
    v5why='Una <b>combine harvester</b> es la gran máquina que siega y procesa '
          'cultivos (cosechadora).',
    v6why='Una <b>thermal imaging camera</b> muestra diferencias de calor en lugar de luz '
          'visible.',
    v7why='Un <b>drone</b> es una pequeña aeronave controlada a distancia, ideal para '
          'buscar en campos desde el aire.',
    v8why='Un <b>drone pilot</b> es una persona entrenada para pilotar un dron.',
    v9why='Un <b>volunteer</b> se ofrece a ayudar sin cobrar.',
    v10why='<i>to relocate</i> significa mover algo a otro lugar, aquí de forma '
           'temporal.',

    sortEyebrow='Clasificar palabras', sortTitle='Clasifica cada palabra en su categoría',
    sortHint='Une cada palabra con la categoría a la que pertenece.',
    sortWhy='Las personas hacen el rescate, el equipo les ayuda a encontrar y proteger a '
            'un cervatillo, los animales son lo que protege la red, y las acciones '
            'describen lo que ocurre durante el rescate.',
    catPeople='Personas y roles', catEquipment='Equipo',
    catAnimals='Animales', catActions='Acciones y proceso',

    grammarEyebrow='Antes de las preguntas', grammarTitle='Tres estructuras del artículo',
    gc1h='Voz pasiva en presente simple',
    gc1b='Usa <strong>am/is/are + participio pasado</strong> cuando la acción importa '
         'más que quién la hace: &ldquo;Thousands of fawns <em>are found</em> '
         'hidden in fields across the countryside.&rdquo;',
    gc2h='Primer condicional',
    gc2b='<strong>If + presente simple, &hellip; will + infinitivo</strong>, para una '
         'situación real y probable: &ldquo;If a pilot <em>spots</em> a fawn early, '
         'the team <em>will have</em> time to act.&rdquo;',
    gc3h='Must, don’t have to, should',
    gc3b='<strong>Must</strong> = una regla esencial. <strong>Don’t have to</strong> '
         '= no es legalmente necesario. <strong>Should</strong> = un consejo sensato, no '
         'una regla: &ldquo;You <em>must</em> wear gloves, farmers <em>don’t have '
         'to</em> report mowing dates by law, and you <em>should</em> approach a fawn '
         'calmly.&rdquo;',

    gEyebrow='Gramática', gTitle='Elige la forma correcta',
    g1why='Voz pasiva en presente simple: <b>are found</b> — el foco está en los '
          'cervatillos, no en quién los encuentra.',
    g2why='Voz pasiva negativa en presente simple: <b>is not touched</b>.',
    g3why='Voz pasiva en presente simple con sujeto plural: <b>are announced</b>.',
    g4why='Voz pasiva en presente simple: <b>are donated</b> — las cámaras son el '
          'sujeto y reciben la acción.',
    g5why='Primer condicional: <i>if</i> + presente simple (<i>spots</i>), + <i>will</i> + '
          'infinitivo (<i>will have</i>), para una situación real y probable.',
    g6why='<i>checks</i> (condición en presente simple) + <i>won’t survive</i> '
          '(resultado con will-future) — una posibilidad real y general.',
    g7why='Estructura del primer condicional: <i>will reject</i> (resultado) + '
          '<i>smells</i> (condición, presente simple).',
    g8why='<b>Must</b> expresa una obligación fuerte — algo esencial, no opcional.',
    g9why='<b>Don’t have to</b> significa que algo no es legalmente necesario, aunque '
          'mucha gente lo haga igualmente.',
    g10why='<b>Should</b> da un consejo sensato o una recomendación, no una regla '
           'estricta.',

    actTitle='Habla y escribe sobre el rescate de cervatillos',
    actUse='Usa al menos cuatro:',
    actSpeakBrief='Discutid en parejas o en grupos pequeños, y luego comparad vuestras '
                  'respuestas con otro grupo.',
    actSpeak1='Eres un piloto de dron voluntario. Explícale a un agricultor, con '
              'claridad, por qué debe avisar a tu equipo de sus fechas de siega con '
              'antelación.',
    actSpeak2='Un vecino dice que la red de rescate es una pérdida de tiempo y dinero. '
              'Defiéndela usando al menos una cifra del artículo.',
    actSpeak3='Vuestro equipo acaba de encontrar un cervatillo, y el agricultor quiere '
              'empezar a segar en diez minutos. Decidid juntos, rápido, qué '
              'hacéis a continuación.',
    actWriteKind='Escritura · 150–250 palabras',
    actWriteBrief='Escribe un breve aviso público para los agricultores de la zona, '
                  'explicando la red de rescate de cervatillos y exactamente qué '
                  'necesitas de ellos antes de que sieguen.',
    actPlaceholder='Cada primavera, nuestra red pide a los agricultores que…',

    resPerfect='Puntuación perfecta. Has leído el artículo con atención '
              'y las estructuras gramaticales están asentadas.',
    resStrong='Muy bien. La mayoría del artículo y el vocabulario se entienden — '
              'revisa las estructuras gramaticales que fallaste.',
    resMid='Buena base. Lee el artículo otra vez, despacio, y repasa los ejemplos de '
          'voz pasiva y primer condicional.',
    resLow='Lee el artículo otra vez desde el principio y luego intenta las preguntas '
          'una segunda vez. El vocabulario se repite en las cuatro actividades.',
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
