# -*- coding: utf-8 -*-
"""Interface strings for Advanced Dinosaur Facts (C1), English, German, Spanish.

Teach-card bodies translate (the six-item form). The English being taught —
the terminology itself, the question stems, the options and the word bank —
stays English in both builds.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

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

T = {}

T['en'] = dict(
    coverTitle='The Hidden World of <em>Dinosaurs</em>',
    coverSub='Advanced palaeontology, the words the field uses, and the facts that refuse to sit still',
    chipLevel='C1 · Advanced', chipFocus='Academic vocabulary & precision',
    chipCount='16 slides',

    ologyEyebrow='Before the questions', ologyTitle='What each -ology actually studies',
    ol1h='Reading the stem',
    ol1b='<strong>Ichno-</strong> is a track, <strong>osteo-</strong> a bone, '
         '<strong>palyno-</strong> pollen, <strong>tapho-</strong> a burial. The stem '
         'names the evidence; <em>-ology</em> just means the study of it.',
    ol1n='Guess the stem and you can usually guess the field. That is the whole trick.',
    ol2h='Why it matters here',
    ol2b='<strong>Ichnology</strong> reads footprints, so it recovers behaviour — herding, '
         'speed, hunting — from animals whose bones were never found in that place at all.',
    ol2n='<strong>Taphonomy</strong> asks a different question: not what lived, but how it came to be preserved.',
    ol3h='The near-miss is the distractor',
    ol3b='<strong>Phylogenetics</strong> reconstructs relatedness, not fossils. In a '
         'question about footprints it is plausible, adjacent and wrong &mdash; which is '
         'exactly what a good distractor is.',
    ol3n='At C1 the wrong answer is rarely absurd. It is usually the neighbouring term.',

    thermEyebrow='One suffix, five answers', thermTitle='How an animal makes, or fails to make, heat',
    th1h='The two you know',
    th1b='An <strong>ectotherm</strong> takes its heat from outside; an '
         '<strong>endotherm</strong> generates its own. Lizard and mammal, roughly.',
    th1n='<em>Cold-blooded</em> and <em>warm-blooded</em> are the everyday words for these two.',
    th2h='The one in the middle',
    th2b='A <strong>mesotherm</strong> generates heat but runs between the two rates. It '
         'is how a dinosaur can grow at 600 kg a year without a mammal&rsquo;s appetite.',
    th2n='Tuna and some sharks do it today, which is how the idea was testable at all.',
    th3h='The two about stability',
    th3b='<strong>Homeothermic</strong> means holding a steady temperature; '
         '<strong>poikilothermic</strong> means letting it vary. That is a different '
         'question from where the heat comes from.',
    th3n='So an animal can be ectothermic and homeothermic at once. The pairs are not opposites.',

    claimEyebrow='The skill being tested', claimTitle='Read the claim, not the topic',
    cl1h='The number carries the answer',
    cl1b='<em>75%</em> and <em>95%</em> are not rounding. One is the K-Pg event, the other '
         'is the Permian-Triassic. A distractor often differs from the key by a single '
         'figure.',
    cl1n='When two options differ only in a number, the number <em>is</em> the question.',
    cl2h='Watch the scope word',
    cl2b='<em>Exclusively</em>, <em>only</em>, <em>never</em>, <em>confined to</em> — an '
         'absolute makes a claim far easier to falsify, and science rarely writes them.',
    cl2n='A hedge (<em>likely</em>, <em>possibly</em>, <em>broadly accept</em>) is usually the safer bet.',
    cl3h='Plausible is not the same as accepted',
    cl3b='Every distractor here is something a reasonable person might believe. The '
         'question asks what the field currently <em>accepts</em>, which is a narrower '
         'thing than what sounds sensible.',
    cl3n='<em>Most accurately reflects consensus</em> is doing real work in that stem.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='What does the evidence actually support?',
    q1why='<strong>Feathers were likely widespread across coelurosaurs.</strong> The Yixian '
          'Formation in China preserves feathers or proto-feathers in Sinosauropteryx, '
          'Microraptor, Yuanchuavis and others &mdash; so feathers long predate birds, and '
          'served warmth and display before they served flight.',
    q2why='<strong>About 75%.</strong> The K-Pg event took marine invertebrates, mosasaurs, '
          'pterosaurs and non-avian dinosaurs alike. The 95% figure belongs to the '
          'Permian-Triassic extinction, ~252 Ma, which is the worst on record.',
    q3why='<strong>Pneumatised vertebrae.</strong> Air sacs from a bird-like respiratory '
          'system hollowed the bones, cutting skeletal mass by up to 10% and making '
          'gigantism biomechanically possible. The same system supplied the oxygen those '
          'bodies demanded.',
    q4why='<strong>Semi-aquatic.</strong> Nizar Ibrahim&rsquo;s Moroccan material showed dense '
          'compact bones, short hind limbs, paddle-like feet and a pressure-sensitive '
          'snout &mdash; and a diet built on large lobe-finned fish such as Onchopristis.',
    q5why='<strong>600&ndash;700 kg a year.</strong> Bone histology — counting growth rings — '
          'gives the fastest mass accumulation known in any land vertebrate. That rate is '
          'itself the argument for mesothermy or full endothermy.',

    fibEyebrow='Activity 2 · The exact term', fibTitle='The word the field would use',
    fibHint='Eighteen words in the bank; five gaps. The near-misses are there on purpose.',
    bankLabel='Word bank:',
    f1why='<strong>Ichnology</strong> is the study of trace fossils — footprints, burrows, '
          'tail drags. Trackways at sites like the Paluxy River give sauropod herding and '
          'theropod hunting behaviour that no skeleton could.',
    f2why='<strong>Infrasound</strong> is sound below about 20 Hz. The nasal passages of a '
          'crested hadrosaur such as Parasaurolophus could resonate down into that range, '
          'and modern elephants and blue whales use it to carry across kilometres.',
    f3why='<strong>Mesothermic</strong> — the middle metabolism proposed by Grady et al. in '
          '2014. It explains fast juvenile growth without a mammal&rsquo;s caloric demand.',
    f4why='<strong>Carnian.</strong> Argentina&rsquo;s Ischigualasto Formation preserves '
          'Carnian sediments, ~231&ndash;237 Ma, holding the oldest confirmed dinosaurs. The '
          'Carnian Pluvial Episode may have opened the ecological door they walked through.',
    f5why='<strong>Schweitzer.</strong> Mary Schweitzer&rsquo;s 2005 paper described apparent '
          'blood vessels and protein fragments in a T. rex femur. Iron chemistry from '
          'haemoglobin may preserve organic molecules far longer than anyone expected — '
          'still an open question.',

    matchEyebrow='Activity 3 · Five that break the rules',
    matchTitle='Match the animal to what makes it strange',
    matchHint='Click a name, then click what characterises it.',
    matchWhy='Each one refuses a neat category: a dromaeosaur with four wings, an armoured '
             'herbivore with a weapon, a display-feathered dinosaur older than flight, a '
             'skull built for impact, and a theropod that gave up meat.',

    ordEyebrow='Activity 4 · The timeline', ordTitle='Put the milestones in order',
    ordHint='Click a card to place it, click a placed card to take it back.',
    ordWhy='Dinosaurs appear ~233 Ma, peak through the Jurassic ~150 Ma, and end at the '
           'K-Pg boundary ~66 Ma. The last two entries are not about dinosaurs living but '
           'about people finding them: Buckland and Owen name them in the 1820s&ndash;40s, '
           'and the 2000s reopen the whole field with feathers and soft tissue.',

    actTitle='Present the strange fact', actUse='Use at least four:',
    actSpeakBrief='One of you presents, the other is the sceptical colleague who asks for '
                  'the evidence. Four minutes each, then swap.',
    actSpeak1='Explain to a non-specialist why "warm-blooded or cold-blooded" is the wrong question for a dinosaur.',
    actSpeak2='Your colleague says feathers prove dinosaurs could fly. Correct the inference without dismissing them.',
    actSpeak3='Argue what ichnology can tell us that a skeleton cannot — and be specific about what it cannot.',
    actSpeak4='Present the Schweitzer soft-tissue finding, and hedge it as carefully as the evidence deserves.',
    actWriteKind='Writing · 200–250 words',
    actWriteBrief='Write the short "current thinking" box for a museum panel on one of these: '
                  'dinosaur metabolism, feather evolution, or Spinosaurus. State what is '
                  'established, mark what is contested, and give a visitor no false certainty.',
    actPlaceholder='The evidence now broadly supports…',

    resPerfect='Full marks. You can read a scientific claim for its precision, not just its topic.',
    resStrong='Strong. The terminology is secure — the numbers are where a second pass pays.',
    resMid='Good ground. Go back to the third slide: most of the misses are scope words and figures.',
    resLow='Read the three opening slides properly, then run it again. The vocabulary is systematic, not arbitrary.',
)

T['de'] = dict(
    coverTitle='Die verborgene Welt der <em>Dinosaurier</em>',
    coverSub='Fortgeschrittene Paläontologie, die Fachsprache und die Fakten, die nicht stillhalten',
    chipLevel='C1 · Fortgeschritten', chipFocus='Wissenschaftssprache & Präzision',
    chipCount='16 Folien',

    ologyEyebrow='Vor den Fragen', ologyTitle='Was jede -ologie wirklich untersucht',
    ol1h='Den Wortstamm lesen',
    ol1b='<strong>Ichno-</strong> ist die Spur, <strong>osteo-</strong> der Knochen, '
         '<strong>palyno-</strong> der Pollen, <strong>tapho-</strong> die Einbettung. '
         'Der Stamm benennt das Material; <em>-ology</em> heißt nur „die Lehre davon“.',
    ol1n='Wer den Stamm errät, errät meist das Fach. Das ist der ganze Trick.',
    ol2h='Warum das hier zählt',
    ol2b='<strong>Ichnology</strong> liest Fußspuren und gewinnt daraus Verhalten &mdash; '
         'Herdenzug, Geschwindigkeit, Jagd &mdash; von Tieren, deren Knochen dort nie '
         'gefunden wurden.',
    ol2n='<strong>Taphonomy</strong> fragt anderes: nicht was lebte, sondern wie es erhalten blieb.',
    ol3h='Der Beinahe-Treffer ist der Distraktor',
    ol3b='<strong>Phylogenetics</strong> rekonstruiert Verwandtschaft, keine Fossilien. In '
         'einer Frage über Fußspuren ist das plausibel, benachbart und falsch &mdash; genau '
         'das macht einen guten Distraktor aus.',
    ol3n='Auf C1 ist die falsche Antwort selten absurd. Meist ist sie der Nachbarbegriff.',

    thermEyebrow='Ein Suffix, fünf Antworten', thermTitle='Wie ein Tier Wärme erzeugt — oder eben nicht',
    th1h='Die beiden bekannten',
    th1b='Ein <strong>ectotherm</strong> bezieht seine Wärme von außen, ein '
         '<strong>endotherm</strong> erzeugt sie selbst. Echse und Säugetier, grob gesagt.',
    th1n='<em>Wechselwarm</em> und <em>gleichwarm</em> sind die Alltagswörter dafür.',
    th2h='Das dazwischen',
    th2b='Ein <strong>mesotherm</strong> erzeugt Wärme, liegt aber zwischen beiden Raten. '
         'So wächst ein Dinosaurier um 600 kg im Jahr, ohne den Appetit eines Säugetiers.',
    th2n='Thunfische und einige Haie machen es heute — deshalb war die Idee überhaupt prüfbar.',
    th3h='Die beiden über Stabilität',
    th3b='<strong>Homeothermic</strong> heißt konstante Temperatur, '
         '<strong>poikilothermic</strong> schwankende. Das ist eine andere Frage als die, '
         'woher die Wärme kommt.',
    th3n='Ein Tier kann also zugleich ectotherm und homeotherm sein. Die Paare sind keine Gegensätze.',

    claimEyebrow='Die eigentliche Prüfung', claimTitle='Lies die Aussage, nicht das Thema',
    cl1h='Die Zahl trägt die Antwort',
    cl1b='<em>75%</em> und <em>95%</em> sind keine Rundung. Das eine ist das K-Pg-Ereignis, '
         'das andere die Perm-Trias-Grenze. Oft unterscheidet sich der Distraktor nur in '
         'einer Zahl.',
    cl1n='Wenn zwei Optionen sich nur in einer Zahl unterscheiden, <em>ist</em> die Zahl die Frage.',
    cl2h='Achte auf das Reichweitenwort',
    cl2b='<em>Exclusively</em>, <em>only</em>, <em>never</em>, <em>confined to</em> — ein '
         'Absolutum ist viel leichter zu widerlegen, und die Wissenschaft schreibt es selten.',
    cl2n='Eine Abschwächung (<em>likely</em>, <em>possibly</em>, <em>broadly accept</em>) ist meist die sicherere Wahl.',
    cl3h='Plausibel ist nicht anerkannt',
    cl3b='Jeder Distraktor hier ist etwas, das ein vernünftiger Mensch glauben könnte. '
         'Gefragt ist, was die Fachwelt derzeit <em>anerkennt</em> — und das ist enger als '
         'das, was vernünftig klingt.',
    cl3n='<em>Most accurately reflects consensus</em> leistet in dieser Frage echte Arbeit.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Was trägt die Evidenz wirklich?',
    q1why='<strong>Federn waren bei Coelurosauriern wahrscheinlich weit verbreitet.</strong> '
          'Die Yixian-Formation in China liefert Federn oder Protofedern bei '
          'Sinosauropteryx, Microraptor, Yuanchuavis und anderen — Federn sind also älter '
          'als die Vögel und dienten erst Wärme und Schau, dann dem Flug.',
    q2why='<strong>Rund 75%.</strong> Das K-Pg-Ereignis traf Meeresvertebraten, Mosasaurier, '
          'Flugsaurier und die nicht-avianen Dinosaurier gleichermaßen. Die 95% gehören zur '
          'Perm-Trias-Grenze (~252 Ma), dem schwersten Aussterben überhaupt.',
    q3why='<strong>Pneumatisierte Wirbel.</strong> Luftsäcke eines vogelartigen Atemsystems '
          'höhlten die Knochen aus, senkten die Skelettmasse um bis zu 10% und machten '
          'Gigantismus biomechanisch möglich. Dasselbe System lieferte den nötigen Sauerstoff.',
    q4why='<strong>Semiaquatisch.</strong> Nizar Ibrahims marokkanisches Material zeigte '
          'dichte kompakte Knochen, kurze Hinterbeine, paddelartige Füße und eine '
          'drucksensible Schnauze — dazu eine Ernährung aus großen Quastenflossern wie '
          'Onchopristis.',
    q5why='<strong>600&ndash;700 kg pro Jahr.</strong> Knochenhistologie — das Zählen der '
          'Wachstumsringe — ergibt die schnellste Massenzunahme aller bekannten Landwirbeltiere. '
          'Diese Rate ist selbst das Argument für Mesothermie oder volle Endothermie.',

    fibEyebrow='Aufgabe 2 · Der genaue Fachbegriff', fibTitle='Das Wort, das die Fachwelt benutzt',
    fibHint='Achtzehn Wörter im Speicher, fünf Lücken. Die Beinahe-Treffer stehen mit Absicht dort.',
    bankLabel='Wortspeicher:',
    f1why='<strong>Ichnology</strong> ist die Lehre von den Spurenfossilien — Fußspuren, '
          'Bauten, Schleifspuren. Trackways wie am Paluxy River liefern Herdenverhalten und '
          'Jagdstrategien, die kein Skelett zeigen könnte.',
    f2why='<strong>Infrasound</strong> ist Schall unter etwa 20 Hz. Die Nasengänge eines '
          'Hadrosauriers wie Parasaurolophus konnten bis in diesen Bereich resonieren; '
          'Elefanten und Blauwale nutzen ihn heute über Kilometer.',
    f3why='<strong>Mesothermic</strong> — der mittlere Stoffwechsel, den Grady et al. 2014 '
          'vorschlugen. Er erklärt schnelles Jugendwachstum ohne den Kalorienbedarf eines Säugers.',
    f4why='<strong>Carnian.</strong> Die Ischigualasto-Formation in Argentinien bewahrt '
          'karnische Sedimente (~231&ndash;237 Ma) mit den ältesten gesicherten Dinosauriern. '
          'Die karnische Pluvialphase könnte die ökologische Tür geöffnet haben.',
    f5why='<strong>Schweitzer.</strong> Mary Schweitzers Arbeit von 2005 beschrieb scheinbar '
          'erhaltene Blutgefäße und Proteinfragmente in einem T.-rex-Femur. Eisenchemie aus '
          'dem Hämoglobin könnte organische Moleküle weit länger schützen als gedacht — bis '
          'heute offen.',

    matchEyebrow='Aufgabe 3 · Fünf, die aus der Reihe fallen',
    matchTitle='Ordne dem Tier zu, was es merkwürdig macht',
    matchHint='Klicke einen Namen an, dann das, was ihn kennzeichnet.',
    matchWhy='Jedes sprengt eine saubere Kategorie: ein Dromaeosaurier mit vier Flügeln, ein '
             'gepanzerter Pflanzenfresser mit Waffe, ein Schaufeder-Dinosaurier älter als der '
             'Flug, ein Schädel für den Aufprall, und ein Theropode, der auf Fleisch verzichtete.',

    ordEyebrow='Aufgabe 4 · Die Zeitleiste', ordTitle='Bring die Meilensteine in die richtige Reihenfolge',
    ordHint='Klicke eine Karte, um sie zu setzen; klicke eine gesetzte an, um sie zurückzunehmen.',
    ordWhy='Dinosaurier treten ~233 Ma auf, erreichen im Jura ~150 Ma ihren Höhepunkt und '
           'enden an der K-Pg-Grenze ~66 Ma. Die letzten beiden Einträge handeln nicht davon, '
           'wann Dinosaurier lebten, sondern wann Menschen sie fanden: Buckland und Owen '
           'benennen sie in den 1820er&ndash;40er Jahren, und die 2000er öffnen das Fach neu.',

    actTitle='Präsentiere den seltsamen Befund', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer präsentiert, der andere ist die skeptische Kollegin, die Belege '
                  'verlangt. Je vier Minuten, dann tauschen.',
    actSpeak1='Erkläre einem Laien, warum „warmblütig oder kaltblütig“ bei Dinosauriern die falsche Frage ist.',
    actSpeak2='Dein Kollege meint, Federn belegten, dass Dinosaurier fliegen konnten. Korrigiere den Schluss, ohne ihn abzukanzeln.',
    actSpeak3='Argumentiere, was Ichnologie zeigen kann, was ein Skelett nicht zeigt — und sag genau, was sie nicht kann.',
    actSpeak4='Stell den Schweitzer-Befund zum Weichgewebe vor und schwäche ihn so sorgfältig ab, wie die Evidenz es verlangt.',
    actWriteKind='Schreiben · 200–250 Wörter',
    actWriteBrief='Schreibe den Kasten „Aktueller Forschungsstand“ für eine Museumstafel zu '
                  'einem dieser Themen: Dinosaurier-Stoffwechsel, Federevolution oder '
                  'Spinosaurus. Halte fest, was gesichert ist, markiere das Strittige und '
                  'gib den Besuchern keine falsche Sicherheit.',
    actPlaceholder='The evidence now broadly supports…',

    resPerfect='Volle Punktzahl. Du liest eine wissenschaftliche Aussage auf ihre Präzision hin, nicht nur auf ihr Thema.',
    resStrong='Stark. Die Fachbegriffe sitzen — bei den Zahlen lohnt ein zweiter Durchgang.',
    resMid='Gute Grundlage. Geh zurück zur dritten Folie: Die meisten Fehler sind Reichweitenwörter und Zahlen.',
    resLow='Arbeite die drei Einstiegsfolien gründlich durch und wiederhole. Das Vokabular ist systematisch, nicht willkürlich.',
)

T['es'] = dict(
    coverTitle='El mundo oculto de los <em>dinosaurios</em>',
    coverSub='Paleontología avanzada, las palabras que usa el campo y los datos que se niegan a quedarse quietos',
    chipLevel='C1 · Avanzado', chipFocus='Vocabulario académico y precisión',
    chipCount='16 diapositivas',

    ologyEyebrow='Antes de las preguntas', ologyTitle='Qué estudia realmente cada -ología',
    ol1h='Leer la raíz',
    ol1b='<strong>Ichno-</strong> es una huella, <strong>osteo-</strong> un hueso, '
         '<strong>palyno-</strong> polen, <strong>tapho-</strong> un enterramiento. La '
         'raíz nombra la evidencia; <em>-ology</em> solo significa el estudio de eso.',
    ol1n='Adivina la raíz y casi siempre adivinarás el campo. Ese es todo el truco.',
    ol2h='Por qué importa aquí',
    ol2b='La <strong>ichnology</strong> lee huellas, así que recupera comportamiento '
         '— manadas, velocidad, caza — de animales cuyos huesos nunca aparecieron en '
         'ese lugar.',
    ol2n='La <strong>taphonomy</strong> plantea otra pregunta: no qué vivió, sino cómo llegó a conservarse.',
    ol3h='El casi acierto es el distractor',
    ol3b='La <strong>phylogenetics</strong> reconstruye parentescos, no fósiles. En una '
         'pregunta sobre huellas resulta plausible, contigua y equivocada &mdash; que es '
         'exactamente lo que es un buen distractor.',
    ol3n='En C1 la respuesta incorrecta rara vez es absurda. Suele ser el término vecino.',

    thermEyebrow='Un sufijo, cinco respuestas', thermTitle='Cómo genera calor un animal, o cómo no lo genera',
    th1h='Los dos que ya conoces',
    th1b='Un <strong>ectotherm</strong> toma el calor del exterior; un '
         '<strong>endotherm</strong> genera el suyo. Lagarto y mamífero, a grandes rasgos.',
    th1n='<em>Cold-blooded</em> y <em>warm-blooded</em> son las palabras cotidianas para estos dos.',
    th2h='El del medio',
    th2b='Un <strong>mesotherm</strong> genera calor pero funciona entre los dos ritmos. '
         'Así puede crecer un dinosaurio 600 kg al año sin el apetito de un mamífero.',
    th2n='Los atunes y algunos tiburones lo hacen hoy, y por eso la idea pudo ponerse a prueba.',
    th3h='Los dos que hablan de estabilidad',
    th3b='<strong>Homeothermic</strong> significa mantener una temperatura constante; '
         '<strong>poikilothermic</strong>, dejar que varíe. Esa es una pregunta distinta '
         'de la de dónde viene el calor.',
    th3n='Así que un animal puede ser ectotérmico y homeotérmico a la vez. Los pares no son opuestos.',

    claimEyebrow='La destreza que se evalúa', claimTitle='Lee la afirmación, no el tema',
    cl1h='El número lleva la respuesta',
    cl1b='<em>75%</em> y <em>95%</em> no son redondeos. Uno es el evento K-Pg, el otro '
         'el Pérmico-Triásico. Un distractor a menudo se diferencia de la clave en una '
         'sola cifra.',
    cl1n='Cuando dos opciones solo difieren en un número, el número <em>es</em> la pregunta.',
    cl2h='Atención a la palabra de alcance',
    cl2b='<em>Exclusively</em>, <em>only</em>, <em>never</em>, <em>confined to</em> '
         '&mdash; un absoluto hace una afirmación mucho más fácil de refutar, y la '
         'ciencia rara vez los escribe.',
    cl2n='Un matiz (<em>likely</em>, <em>possibly</em>, <em>broadly accept</em>) suele ser la apuesta más segura.',
    cl3h='Plausible no es lo mismo que aceptado',
    cl3b='Todos los distractores de aquí son cosas que una persona razonable podría '
         'creer. La pregunta es qué <em>acepta</em> hoy el campo, que es algo más '
         'estrecho que lo que suena sensato.',
    cl3n='<em>Most accurately reflects consensus</em> está haciendo trabajo de verdad en ese enunciado.',

    mcEyebrow='Actividad 1 · Opción múltiple', mcTitle='¿Qué apoya realmente la evidencia?',
    q1why='<strong>Las plumas estaban probablemente extendidas entre los celurosaurios.</strong> '
          'La Formación Yixian, en China, conserva plumas o protoplumas en '
          'Sinosauropteryx, Microraptor, Yuanchuavis y otros &mdash; así que las plumas '
          'son muy anteriores a las aves y sirvieron para el calor y la exhibición antes '
          'que para el vuelo.',
    q2why='<strong>En torno al 75%.</strong> El evento K-Pg se llevó por igual '
          'invertebrados marinos, mosasaurios, pterosaurios y dinosaurios no avianos. La '
          'cifra del 95% corresponde a la extinción Pérmico-Triásica, hace ~252 Ma, la '
          'peor registrada.',
    q3why='<strong>Vértebras neumatizadas.</strong> Los sacos aéreos de un sistema '
          'respiratorio de tipo aviano ahuecaron los huesos, recortando hasta un 10% de '
          'la masa esquelética y haciendo el gigantismo biomecánicamente posible. Ese '
          'mismo sistema aportaba el oxígeno que exigían esos cuerpos.',
    q4why='<strong>Semiacuático.</strong> El material marroquí de Nizar Ibrahim mostró '
          'huesos compactos y densos, extremidades traseras cortas, pies en forma de '
          'remo y un hocico sensible a la presión &mdash; y una dieta basada en grandes '
          'peces sarcopterigios como Onchopristis.',
    q5why='<strong>600&ndash;700 kg al año.</strong> La histología ósea — contar anillos '
          'de crecimiento — da la acumulación de masa más rápida conocida en un '
          'vertebrado terrestre. Ese ritmo es en sí mismo el argumento a favor de la '
          'mesotermia o de una endotermia plena.',

    fibEyebrow='Actividad 2 · El término exacto', fibTitle='La palabra que usaría el campo',
    fibHint='Dieciocho palabras en el banco; cinco huecos. Los casi aciertos están ahí a propósito.',
    bankLabel='Banco de palabras:',
    f1why='La <strong>ichnology</strong> es el estudio de los fósiles traza — huellas, '
          'madrigueras, marcas de cola. Los rastros de yacimientos como el río Paluxy '
          'dan comportamiento de manada en saurópodos y de caza en terópodos que ningún '
          'esqueleto podría dar.',
    f2why='El <strong>infrasound</strong> es sonido por debajo de unos 20 Hz. Las fosas '
          'nasales de un hadrosaurio con cresta como Parasaurolophus podían resonar en '
          'ese rango, y hoy los elefantes y las ballenas azules lo usan para llegar a '
          'kilómetros de distancia.',
    f3why='<strong>Mesothermic</strong> — el metabolismo intermedio propuesto por Grady '
          'et al. en 2014. Explica el crecimiento juvenil rápido sin la demanda calórica '
          'de un mamífero.',
    f4why='<strong>Carnian.</strong> La Formación Ischigualasto, en Argentina, conserva '
          'sedimentos del Carniense, ~231&ndash;237 Ma, con los dinosaurios confirmados '
          'más antiguos. El Episodio Pluvial Carniense pudo abrirles la puerta ecológica '
          'que atravesaron.',
    f5why='<strong>Schweitzer.</strong> El artículo de Mary Schweitzer de 2005 describió '
          'aparentes vasos sanguíneos y fragmentos de proteína en un fémur de T. rex. La '
          'química del hierro de la hemoglobina podría conservar moléculas orgánicas '
          'mucho más tiempo de lo esperado — sigue siendo una cuestión abierta.',

    matchEyebrow='Actividad 3 · Cinco que rompen las reglas',
    matchTitle='Relaciona el animal con lo que lo hace extraño',
    matchHint='Haz clic en un nombre y luego en lo que lo caracteriza.',
    matchWhy='Cada uno se resiste a una categoría limpia: un dromeosaurio con cuatro '
             'alas, un herbívoro acorazado con un arma, un dinosaurio con plumas de '
             'exhibición anterior al vuelo, un cráneo construido para el impacto y un '
             'terópodo que renunció a la carne.',

    ordEyebrow='Actividad 4 · La cronología', ordTitle='Ordena los hitos',
    ordHint='Haz clic en una tarjeta para colocarla; haz clic en una colocada para retirarla.',
    ordWhy='Los dinosaurios aparecen hace ~233 Ma, alcanzan su apogeo en el Jurásico '
           'hace ~150 Ma y terminan en el límite K-Pg hace ~66 Ma. Las dos últimas '
           'entradas no tratan de dinosaurios viviendo sino de personas encontrándolos: '
           'Buckland y Owen los nombran entre 1820 y 1840, y los años 2000 reabren todo '
           'el campo con plumas y tejido blando.',

    actTitle='Presenta el dato extraño', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno presenta y el otro es el colega escéptico que pide las pruebas. '
                  'Cuatro minutos cada uno, luego cambiad.',
    actSpeak1='Explica a alguien no especialista por qué "de sangre caliente o de sangre fría" es la pregunta equivocada para un dinosaurio.',
    actSpeak2='Tu colega dice que las plumas prueban que los dinosaurios volaban. Corrige la inferencia sin descartarle.',
    actSpeak3='Argumenta qué puede decirnos la ichnology que un esqueleto no puede — y sé concreto sobre lo que no puede.',
    actSpeak4='Presenta el hallazgo de tejido blando de Schweitzer y matízalo con el cuidado que merece la evidencia.',
    actWriteKind='Escritura · 200–250 palabras',
    actWriteBrief='Escribe el breve recuadro de "estado de la cuestión" para un panel de '
                  'museo sobre uno de estos temas: el metabolismo de los dinosaurios, la '
                  'evolución de las plumas o el Spinosaurus. Indica qué está establecido, '
                  'marca qué está en disputa y no des al visitante ninguna certeza falsa.',
    actPlaceholder='The evidence now broadly supports…',

    resPerfect='Puntuación perfecta. Sabes leer una afirmación científica por su precisión, no solo por su tema.',
    resStrong='Muy bien. La terminología está firme — donde compensa una segunda pasada es en las cifras.',
    resMid='Buena base. Vuelve a la tercera diapositiva: casi todos los fallos son palabras de alcance y cifras.',
    resLow='Lee bien las tres diapositivas iniciales y vuelve a intentarlo. El vocabulario es sistemático, no arbitrario.',
)


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
