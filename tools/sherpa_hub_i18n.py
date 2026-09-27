#!/usr/bin/env python3
"""The Sherpa hub's translations, and the tool that puts them in the page.

    python tools/sherpa_hub_i18n.py            # inject into sherpa-tensing-route-map.html
    python tools/sherpa_hub_i18n.py --check    # exit 1 if anything is missing

Innes, 2026-09-26: "sherpa hub page needs the full languages that are in the
rest of the sherpa course" — the ten the camps offer for their examples:
English plus German, Spanish, French, Italian, Portuguese, Russian, Arabic,
Chinese and Japanese.

HOW THE PAGE USES THIS. English is the page source (for search, no-script
visitors and tools/check_route_map.py). Every translated element carries
data-t="key" (its innerHTML), data-t-aria="key" (aria-label) or
data-t-title="key" (title); the page captures the English from the DOM and
swaps in LANGS[lang][key]. Sentences the progress script builds (the lock
note, the start button, lock reasons, "from camp 3") go through
window.sherpaT(key, {vars}) and need an English value in EN as well.
The dictionaries are injected between /*I18N:start*/ and /*I18N:end*/ in
the page's language script. The choice is remembered (sherpa.lang.v1) and
?lang=xx sets it. Arabic text is set right to left, element by element, so
the maps and the grid keep their layout.

WHAT IS NOT TRANSLATED, on purpose: tense and lesson names (they are the
names of the lessons, and what a learner is learning), grammar forms in
CAPS, the English example sentences, zone names inside the SVG maps. The
guide's bold shape names (simple, continuous ...) stay English too.

The check: every key used in the page exists in every language; every
{placeholder} in the English survives in each translation; no HTML tag is
lost or added (a translation keeps the same <b>, <em>, <strong> and <a>
tags as the English it replaces); the fences are present.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'sherpa-tensing-route-map.html')
FENCE = re.compile(r'/\*I18N:start\*/.*?/\*I18N:end\*/', re.S)

# English for the sentences the progress script builds (static English is in the page)
EN = dict(
    carryOn='Carry on: camp {n} &middot; {name}', headDown='Head down: {name}', offRoute='Off the route: {name}',
    again='Climb it again: camp one', startFree='Start at camp one &middot; free',
    lockNote='<strong>{c} of 13</strong> camps &middot; <strong>{d} of 9</strong> descents &mdash; {tail}',
    tailAll='everything is open.', tailWhole='the whole mountain is open, both faces.',
    tailDefault='nine of the camps open a passive; <em>used to</em> comes off camp 2 or 3, <em>be used to</em> off camp 2, the causative off your first descent.',
    teachOff='I&rsquo;m teaching this &mdash; open everything', teachOn='Locks off &mdash; everything is open',
    teachWhy='Learners open each passive, and the three lessons off the route, by finishing the camp it comes from. Teachers, and anyone in a hurry, can open the lot.',
    pair='camp {n}, {tense}', whyDescent='Finish {pair} and this one opens.',
    whyUsedTo='Finish camp 2 or camp 3 &mdash; used to is a present-simple habit, moved into the past.',
    whyBeUsedTo='Finish camp 2, present simple &mdash; be used to is a state, not an event.',
    whyCausative='Finish any one descent camp &mdash; the causative is a passive wearing a hat.',
    srLocked=' (locked: {why})', srDone=' (done)', fromOpen='from camp {n}', fromLocked='after camp {n}',
    hintNoCamp='{label}: no camp here &mdash; see the note below the lists.', hintLocked='{label}: {why}',
)

LANGS = {}

LANGS['de'] = dict(
    langGroup='Sprache', sub='ein Weg hinauf durch die Zeitformen', eyebrow='Routenkarte',
    h1='Dreizehn Lager, zwei Seiten',
    lead='Der Aufstieg im Aktiv, geordnet danach, wie oft du jede Zeitform wirklich brauchst. Der Abstieg im Passiv: dieselben dreizehn Lager in umgekehrter Reihenfolge &mdash; neun davon mit einem Passiv, das sich zu lernen lohnt.',
    countsAria='Was auf der Route liegt', cUp='Lager bergauf', cDown='Passivformen bergab', cOff='abseits der Route', cFree='kostenlos',
    everyStop='Alle Stationen', mapKick='Die Karte', mapH2='Hinauf im Aktiv, hinab im Passiv',
    mapHow='Der Weg hinauf hat keine Sperren: Fang bei dem Lager an, das du brauchst. Jede Station auf dem Weg hinab öffnet sich, wenn du das Lager abschließt, aus dem sie kommt; bis dahin ist ihre Markierung grau.',
    guideKick='Neu hier?', guideLine='Zwei Minuten dazu, was eine Zeitform ist, was Aktiv und Passiv bedeuten und warum die Lager in dieser Reihenfolge kommen.',
    guideBtn='Was sehe ich hier?', ascH='Der Aufstieg', ascSub='Aktiv &middot; vom Basislager zum Gipfel',
    descH='Der Abstieg', descSub='Passiv &middot; vom Gipfel ins Tal',
    ascAria='Der Aufstieg: ein Berg mit dreizehn farbigen Lagermarkierungen auf einem Weg vom Basislager zum Gipfel, eine für jede Zeitform im Aktiv, und zwei Wolken für used to und be used to. Alle Stationen stehen auch unter der Karte.',
    descAria='Der Abstieg: derselbe Berg bei Nacht, mit einer Rauten-Markierung für jede Zeitform im Passiv, vom Gipfel abwärts. Neun sind Lektionen, die sich jeweils öffnen, wenn du ihr Lager abschließt; vier bleiben dunkel, weil niemand diese Passivformen benutzt. Der Mond ist das Kausativ. Alle Stationen stehen auch unter der Karte.',
    lgColour='farbig &mdash; antippen und los', lgGrey='grau &mdash; öffnet sich, wenn du das zugehörige Lager abschließt',
    lgShape='Kreis = Aktiv, Raute = Passiv', ascList='Der Aufstieg &middot; Aktiv',
    zFH='Basislager', zFSub='die brauchst du jeden Tag', zRH='Der Grat', zRSub='häufig, aber mit mehr Sorgfalt',
    zSH='Gipfelsturm', zSSub='selten, meist im geschriebenen Englisch',
    descList='Der Abstieg &middot; Passiv', descListSub='jede öffnet sich, wenn du das Lager abschließt, aus dem sie kommt',
    offH='Abseits der Route', offSub='keine Zeitformen, aber sie streiten mit einer',
    offUsedTo='ab Lager 2 oder 3', offBeUsedTo='ab Lager 2', offCausative='ab deiner ersten Abstiegsstation',
    free='Gratis', level='Niveau', aboutRoute='Über die Route', whereH='Wo du stehst',
    darkH='Vier Stationen des Abstiegs bleiben absichtlich dunkel',
    darkP='Das Passiv des present perfect continuous, des past perfect continuous, des future continuous und des future perfect continuous lässt sich bilden &mdash; HAS BEEN BEING CLEANED, WILL BE BEING CLEANED &mdash;, aber Muttersprachler meiden jede dieser Formen und formulieren den Satz um. Da gibt es nichts zu lernen, also gibt es dort kein Lager.',
    teachH='Du unterrichtest?',
    teachP='Der Schalter unter der Karte hebt in diesem Browser alle Fortschrittssperren auf einmal auf &mdash; für die Leinwand im Unterricht oder eine Klasse, die den Aufstieg schon kennt. Pro-Lektionen brauchen weiterhin Pro. <a href="block-camp.html">Block Camp</a> steigt durch neun dieser Zeitformen, in einer Welt aus Blöcken.',
    proP='<strong>Vier Lektionen sind kostenlos, ohne Anmeldung:</strong> Lager eins und zwei, das Passiv aus Lager eins und <em>used to</em>. Pro öffnet die anderen einundzwanzig und jede weitere Lektion auf der Website.',
    plans='Tarife und Preise',
    gKick='Bevor du losgehst', gTitle='Was du hier siehst', gClose='Anleitung schließen',
    g1H='Eine Zeitform ist eine Zeit und eine Form',
    g1P='Jede Zeitform legt eine Handlung in die Vergangenheit, die Gegenwart oder die Zukunft und gibt ihr eine von vier Formen: <b>simple</b> (die einfache Tatsache), <b>continuous</b> (gerade im Gange), <b>perfect</b> (der Blick zurück von einem späteren Punkt aus: jetzt oder ein Zeitpunkt in der Vergangenheit oder Zukunft) oder <b>perfect continuous</b> (im Gange bis zu diesem Punkt). Drei Zeiten, vier Formen: zwölf der dreizehn Lager. Jede Form unten ist &bdquo;she&ldquo; + CLIMB, und die Zahl ist ihr Lager.',
    gCaption='Die zwölf Zeitformen nach Zeit und Form; jede verlinkt auf ihr Lager.',
    gGoing='Das übrige, Lager 5, ist eine Zukunft, die man schon kommen sieht.',
    g2H='Zwei Seiten: Aktiv und Passiv',
    gAsc='<b>Der Aufstieg &middot; Aktiv.</b> Wer handelt, steht vorn.',
    gDesc='<b>Der Abstieg &middot; Passiv.</b> Was von der Handlung betroffen ist, steht vorn, und wer handelt, kann wegfallen.',
    g2P='Dieselbe Zeitform, umgedreht: Das Passiv ist BE in dieser Zeitform + PAST PARTICIPLE. Deshalb ist jede Station auf dem Weg hinab der Zwilling eines Lagers auf dem Weg hinauf, und sie öffnet sich, wenn du dieses Lager abschließt.',
    g3H='Warum diese Reihenfolge',
    g3P='Die Lager steigen in der Reihenfolge an, in der du sie brauchst, nicht in der Reihenfolge der Grammatikbücher. Die <b>Basislager</b> sind die Zeitformen, die du jeden Tag benutzt; <b>der Grat</b> ist häufig, braucht aber mehr Sorgfalt; der <b>Gipfelsturm</b> ist selten und meist geschrieben. Vier Passivformen haben kein Lager: Man kann sie bilden &mdash; HAS BEEN BEING CLEANED &mdash;, aber niemand sagt sie.',
    g3Map='Auf der Karte ist ein Kreis aktiv, eine Raute passiv, und grau heißt: noch nicht offen; eine blasse Raute mit &bdquo;no camp&ldquo; öffnet sich nie. Die Wolken sind &bdquo;used to&ldquo; und &bdquo;be used to&ldquo;; der Mond ist das Kausativ.',
    startFree='Im ersten Lager beginnen &middot; kostenlos', backMap='Zurück zur Karte',
    carryOn='Weiter: Lager {n} &middot; {name}', headDown='Bergab: {name}', offRoute='Abseits der Route: {name}',
    again='Noch einmal hinauf: Lager eins',
    lockNote='<strong>{c} von 13</strong> Lagern &middot; <strong>{d} von 9</strong> Abstiegsstationen &mdash; {tail}',
    tailAll='alles ist offen.', tailWhole='der ganze Berg ist offen, auf beiden Seiten.',
    tailDefault='neun der Lager öffnen ein Passiv; <em>used to</em> kommt ab Lager 2 oder 3, <em>be used to</em> ab Lager 2, das Kausativ ab deiner ersten Abstiegsstation.',
    teachOff='Ich unterrichte das &mdash; alles öffnen', teachOn='Sperren aus &mdash; alles ist offen',
    teachWhy='Lernende öffnen jedes Passiv und die drei Lektionen abseits der Route, indem sie das Lager abschließen, aus dem es kommt. Lehrkräfte und alle, die es eilig haben, können alles öffnen.',
    pair='Lager {n} ({tense})', whyDescent='Schließ {pair} ab, dann öffnet sich diese Station.',
    whyUsedTo='Schließ Lager 2 oder Lager 3 ab &mdash; used to ist eine Gewohnheit aus dem present simple, in die Vergangenheit verschoben.',
    whyBeUsedTo='Schließ Lager 2 (present simple) ab &mdash; be used to ist ein Zustand, kein Ereignis.',
    whyCausative='Schließ irgendeine Station des Abstiegs ab &mdash; das Kausativ ist ein Passiv mit Hut.',
    srLocked=' (gesperrt: {why})', srDone=' (erledigt)', fromOpen='aus Lager {n}', fromLocked='nach Lager {n}',
    hintNoCamp='{label}: hier gibt es kein Lager &mdash; siehe die Notiz unter den Listen.', hintLocked='{label}: {why}',
)

LANGS['es'] = dict(
    langGroup='Idioma', sub='una ruta de subida por los tiempos verbales', eyebrow='Mapa de la ruta',
    h1='Trece campamentos, dos caras',
    lead='La subida, en voz activa, ordenada según la frecuencia con que de verdad usarás cada tiempo. La bajada, en voz pasiva: los mismos trece campamentos al revés &mdash; nueve de ellos con una pasiva que merece la pena aprender.',
    countsAria='Qué hay en la ruta', cUp='campamentos de subida', cDown='pasivas de bajada', cOff='fuera de la ruta', cFree='gratis',
    everyStop='Todas las paradas', mapKick='El mapa', mapH2='Subida en activa, bajada en pasiva',
    mapHow='La subida no tiene candados: empieza en el campamento que necesites. Cada parada de la bajada se abre cuando terminas el campamento del que viene; hasta entonces, su marca es gris.',
    guideKick='¿Primera vez aquí?', guideLine='Dos minutos sobre qué es un tiempo verbal, qué significan activa y pasiva, y por qué los campamentos van en este orden.',
    guideBtn='¿Qué estoy viendo?', ascH='La subida', ascSub='voz activa &middot; del campamento base a la cumbre',
    descH='La bajada', descSub='voz pasiva &middot; de la cumbre al valle',
    ascAria='La subida: una montaña con trece marcas de colores en un camino del campamento base a la cumbre, una por cada tiempo en voz activa, y dos nubes para used to y be used to. Todas las paradas aparecen también debajo del mapa.',
    descAria='La bajada: la misma montaña de noche, con un rombo para cada tiempo en voz pasiva, de la cumbre hacia abajo. Nueve son lecciones y cada una se abre cuando terminas su campamento; cuatro siguen a oscuras porque nadie usa esas pasivas. La luna es el causativo. Todas las paradas aparecen también debajo del mapa.',
    lgColour='en color &mdash; toca para ir', lgGrey='gris &mdash; se abre cuando terminas su campamento',
    lgShape='círculo = voz activa, rombo = voz pasiva', ascList='La subida &middot; voz activa',
    zFH='Campamentos base', zFSub='los usarás a diario', zRH='La cresta', zRSub='frecuentes, pero piden más cuidado',
    zSH='Ataque a la cumbre', zSSub='raros, sobre todo en inglés escrito',
    descList='La bajada &middot; voz pasiva', descListSub='cada una se abre cuando terminas el campamento del que viene',
    offH='Fuera de la ruta', offSub='no son tiempos, pero discuten con uno',
    offUsedTo='desde el campamento 2 o 3', offBeUsedTo='desde el campamento 2', offCausative='desde tu primera parada de bajada',
    free='Gratis', level='Nivel', aboutRoute='Sobre la ruta', whereH='Dónde estás',
    darkH='Cuatro paradas de la bajada siguen a oscuras a propósito',
    darkP='Las pasivas del present perfect continuous, del past perfect continuous, del future continuous y del future perfect continuous se pueden formar &mdash;HAS BEEN BEING CLEANED, WILL BE BEING CLEANED&mdash;, pero los hablantes nativos las evitan todas y dan la vuelta a la frase. Ahí no hay nada que aprender, así que no hay campamento.',
    teachH='¿Das clase?',
    teachP='El interruptor debajo del mapa quita de una vez todos los candados de progreso en este navegador &mdash; para la pantalla de clase, o para un grupo que ya ha hecho la subida. Las lecciones Pro siguen necesitando Pro. <a href="block-camp.html">Block Camp</a> recorre nueve de estos tiempos en un mundo hecho de bloques.',
    proP='<strong>Cuatro lecciones son gratis, sin registrarte:</strong> los campamentos uno y dos, la pasiva del campamento uno y <em>used to</em>. Pro abre las otras veintiuna, y todas las demás lecciones del sitio.',
    plans='Planes y precios',
    gKick='Antes de subir', gTitle='Qué estás viendo', gClose='Cerrar la guía',
    g1H='Un tiempo verbal es un momento y una forma',
    g1P='Cada tiempo verbal sitúa una acción en el pasado, el presente o el futuro, y le da una de cuatro formas: <b>simple</b> (el hecho sin más), <b>continuous</b> (en curso), <b>perfect</b> (mirando atrás desde un punto posterior: ahora, o un momento del pasado o del futuro) o <b>perfect continuous</b> (en curso hasta ese punto). Tres momentos, cuatro formas: doce de los trece campamentos. Cada forma de abajo es &laquo;she&raquo; + CLIMB, y el número es su campamento.',
    gCaption='Los doce tiempos por momento y forma; cada uno enlaza con su campamento.',
    gGoing='El que sobra, el campamento 5, es un futuro que ya se ve venir.',
    g2H='Dos caras: activa y pasiva',
    gAsc='<b>La subida &middot; activa.</b> Quien hace la acción va primero.',
    gDesc='<b>La bajada &middot; pasiva.</b> Va primero aquello a lo que le ocurre la acción, y quien la hace puede desaparecer.',
    g2P='El mismo tiempo, dado la vuelta: la pasiva es BE en ese tiempo + el PAST PARTICIPLE. Por eso cada parada de la bajada es la gemela de un campamento de la subida, y se abre cuando terminas ese campamento.',
    g3H='Por qué este orden',
    g3P='Los campamentos suben en el orden en que los vas a necesitar, no en el de los libros de gramática. Los <b>campamentos base</b> son los tiempos que usas a diario; <b>la cresta</b> es frecuente pero pide más cuidado; el <b>ataque a la cumbre</b> es raro y sobre todo escrito. Cuatro pasivas no tienen campamento: se pueden formar &mdash;HAS BEEN BEING CLEANED&mdash;, pero nadie las dice.',
    g3Map='En el mapa, un círculo es voz activa, un rombo es voz pasiva, y el gris significa que aún no está abierto; un rombo tenue marcado &laquo;no camp&raquo; no se abre nunca. Las nubes son &laquo;used to&raquo; y &laquo;be used to&raquo;; la luna es el causativo.',
    startFree='Empezar en el campamento 1 &middot; gratis', backMap='Volver al mapa',
    carryOn='Sigue: campamento {n} &middot; {name}', headDown='Baja: {name}', offRoute='Fuera de la ruta: {name}',
    again='Vuelve a subir: campamento uno',
    lockNote='<strong>{c} de 13</strong> campamentos &middot; <strong>{d} de 9</strong> paradas de bajada &mdash; {tail}',
    tailAll='todo está abierto.', tailWhole='toda la montaña está abierta, por las dos caras.',
    tailDefault='nueve de los campamentos abren una pasiva; <em>used to</em> se abre desde el campamento 2 o 3, <em>be used to</em> desde el 2, y el causativo desde tu primera parada de bajada.',
    teachOff='Estoy dando clase &mdash; abrir todo', teachOn='Sin candados &mdash; todo está abierto',
    teachWhy='Los alumnos abren cada pasiva, y las tres lecciones fuera de la ruta, terminando el campamento del que vienen. Los profesores, y quien tenga prisa, pueden abrirlo todo.',
    pair='el campamento {n} ({tense})', whyDescent='Termina {pair} y esta se abre.',
    whyUsedTo='Termina el campamento 2 o el 3 &mdash; used to es un hábito del present simple llevado al pasado.',
    whyBeUsedTo='Termina el campamento 2 (present simple) &mdash; be used to es un estado, no un suceso.',
    whyCausative='Termina cualquier parada de la bajada &mdash; el causativo es una pasiva con sombrero.',
    srLocked=' (bloqueado: {why})', srDone=' (hecho)', fromOpen='del campamento {n}', fromLocked='tras el campamento {n}',
    hintNoCamp='{label}: aquí no hay campamento &mdash; mira la nota debajo de las listas.', hintLocked='{label}: {why}',
)

LANGS['fr'] = dict(
    langGroup='Langue', sub='un itinéraire qui gravit les temps verbaux', eyebrow="Carte de l'itinéraire",
    h1='Treize camps, deux faces',
    lead="La montée, à la voix active, classée selon la fréquence à laquelle tu utiliseras vraiment chaque temps. La descente, à la voix passive\xa0: les treize mêmes camps dans l'autre sens &mdash; dont neuf avec un passif qui vaut la peine d'être appris.",
    countsAria="Ce qu'il y a sur l'itinéraire", cUp='camps à la montée', cDown='passifs à la descente', cOff="hors de l'itinéraire", cFree='gratuites',
    everyStop='Toutes les étapes', mapKick='La carte', mapH2="En montant à l'actif, en descendant au passif",
    mapHow="La montée n'a pas de verrou\xa0: commence au camp dont tu as besoin. Chaque étape de la descente s'ouvre quand tu termines le camp d'où elle vient\xa0; en attendant, son repère est gris.",
    guideKick='Nouveau ici\xa0?', guideLine="Deux minutes pour comprendre ce qu'est un temps, ce que veulent dire actif et passif, et pourquoi les camps viennent dans cet ordre.",
    guideBtn="Qu'est-ce que j'ai sous les yeux\xa0?", ascH='La montée', ascSub="voix active &middot; du camp de base au sommet",
    descH='La descente', descSub='voix passive &middot; du sommet à la vallée',
    ascAria='La montée\xa0: une montagne avec treize repères de couleur sur un chemin du camp de base au sommet, un pour chaque temps à la voix active, et deux nuages pour used to et be used to. Toutes les étapes sont aussi listées sous la carte.',
    descAria="La descente\xa0: la même montagne la nuit, avec un losange pour chaque temps à la voix passive, du sommet vers le bas. Neuf sont des leçons, chacune s'ouvre quand tu termines son camp\xa0; quatre restent sombres parce que personne n'utilise ces passifs. La lune, c'est le causatif. Toutes les étapes sont aussi listées sous la carte.",
    lgColour='en couleur &mdash; touche pour y aller', lgGrey='gris &mdash; s\'ouvre quand tu termines son camp',
    lgShape='cercle = voix active, losange = voix passive', ascList='La montée &middot; voix active',
    zFH='Camps de base', zFSub='à utiliser tous les jours', zRH="L'arête", zRSub='fréquents, mais demandent plus de soin',
    zSH='Assaut final', zSSub="rares, surtout à l'écrit",
    descList='La descente &middot; voix passive', descListSub="chacune s'ouvre quand tu termines le camp d'où elle vient",
    offH="Hors de l'itinéraire", offSub="ce ne sont pas des temps, mais ils se disputent avec l'un d'eux",
    offUsedTo='après le camp 2 ou 3', offBeUsedTo='après le camp 2', offCausative='après ta première étape de descente',
    free='Gratuit', level='Niveau', aboutRoute="À propos de l'itinéraire", whereH="Où tu en es",
    darkH='Quatre étapes de la descente restent sombres exprès',
    darkP="Les passifs du present perfect continuous, du past perfect continuous, du future continuous et du future perfect continuous peuvent se construire &mdash; HAS BEEN BEING CLEANED, WILL BE BEING CLEANED &mdash; mais les anglophones natifs les évitent tous et reformulent la phrase. Il n'y a rien à apprendre là, donc il n'y a pas de camp.",
    teachH='Tu enseignes\xa0?',
    teachP="L'interrupteur sous la carte lève d'un coup tous les verrous de progression dans ce navigateur &mdash; pour l'écran de la classe, ou pour un groupe qui a déjà fait la montée. Les leçons Pro demandent toujours Pro. <a href=\"block-camp.html\">Block Camp</a> gravit neuf de ces temps dans un monde fait de blocs.",
    proP="<strong>Quatre leçons sont gratuites, sans inscription\xa0:</strong> les camps un et deux, le passif qu'ouvre le camp un, et <em>used to</em>. Pro ouvre les vingt et une autres, et toutes les autres leçons du site.",
    plans='Formules et tarifs',
    gKick='Avant de monter', gTitle='Ce que tu as sous les yeux', gClose='Fermer le guide',
    g1H='Un temps, c\'est un moment et une forme',
    g1P="Chaque temps place une action dans le passé, le présent ou le futur, et lui donne l'une des quatre formes\xa0: <b>simple</b> (le fait tout court), <b>continuous</b> (en cours), <b>perfect</b> (un regard en arrière depuis un point ultérieur\xa0: maintenant, ou un moment du passé ou du futur) ou <b>perfect continuous</b> (en cours jusqu'à ce point). Trois moments, quatre formes\xa0: douze des treize camps. Chaque forme ci-dessous est &laquo;&nbsp;she&nbsp;&raquo; + CLIMB, et le numéro est son camp.",
    gCaption='Les douze temps par moment et par forme\xa0; chacun renvoie à son camp.',
    gGoing="Celui qui reste, le camp 5, est un futur qu'on voit déjà venir.",
    g2H='Deux faces\xa0: actif et passif',
    gAsc="<b>La montée &middot; actif.</b> Celui qui agit vient en premier.",
    gDesc="<b>La descente &middot; passif.</b> Ce qui subit l'action vient en premier, et celui qui agit peut disparaître.",
    g2P="Le même temps, retourné\xa0: le passif, c'est BE à ce temps + le PAST PARTICIPLE. Voilà pourquoi chaque étape de la descente est la jumelle d'un camp de la montée, et s'ouvre quand tu termines ce camp.",
    g3H='Pourquoi cet ordre',
    g3P="Les camps montent dans l'ordre où tu en auras besoin, pas dans celui des livres de grammaire. Les <b>camps de base</b> sont les temps que tu utilises tous les jours\xa0; <b>l'arête</b> est fréquente mais demande plus de soin\xa0; l'<b>assaut final</b> est rare et surtout écrit. Quatre passifs n'ont pas de camp\xa0: on peut les construire &mdash; HAS BEEN BEING CLEANED &mdash; mais personne ne les dit.",
    g3Map="Sur la carte, un cercle est actif, un losange est passif, et le gris veut dire pas encore ouvert\xa0; un losange pâle marqué &laquo;&nbsp;no camp&nbsp;&raquo; ne s'ouvre jamais. Les nuages sont &laquo;&nbsp;used to&nbsp;&raquo; et &laquo;&nbsp;be used to&nbsp;&raquo;\xa0; la lune, c'est le causatif.",
    startFree='Commencer au camp un &middot; gratuit', backMap='Retour à la carte',
    carryOn='Continue\xa0: camp {n} &middot; {name}', headDown='Descends\xa0: {name}', offRoute="Hors de l'itinéraire\xa0: {name}",
    again='Remonte\xa0: camp un',
    lockNote='<strong>{c} sur 13</strong> camps &middot; <strong>{d} sur 9</strong> étapes de descente &mdash; {tail}',
    tailAll='tout est ouvert.', tailWhole='toute la montagne est ouverte, sur ses deux faces.',
    tailDefault="neuf des camps ouvrent un passif\xa0; <em>used to</em> s'ouvre après le camp 2 ou 3, <em>be used to</em> après le camp 2, et le causatif après ta première étape de descente.",
    teachOff="J'enseigne ce cours &mdash; tout ouvrir", teachOn='Verrous levés &mdash; tout est ouvert',
    teachWhy="Les apprenants ouvrent chaque passif, et les trois leçons hors de l'itinéraire, en terminant le camp correspondant. Les enseignants, et ceux qui sont pressés, peuvent tout ouvrir.",
    pair='le camp {n} ({tense})', whyDescent="Termine {pair} et celle-ci s'ouvre.",
    whyUsedTo='Termine le camp 2 ou le camp 3 &mdash; used to est une habitude du present simple, transposée au passé.',
    whyBeUsedTo="Termine le camp 2 (present simple) &mdash; be used to est un état, pas un événement.",
    whyCausative="Termine n'importe quelle étape de la descente &mdash; le causatif est un passif qui porte un chapeau.",
    srLocked=' (verrouillé\xa0: {why})', srDone=' (terminé)', fromOpen='du camp {n}', fromLocked='après le camp {n}',
    hintNoCamp='{label}\xa0: pas de camp ici &mdash; lis la note sous les listes.', hintLocked='{label}. {why}',
)

LANGS['it'] = dict(
    langGroup='Lingua', sub='un percorso in salita tra i tempi verbali', eyebrow='Mappa del percorso',
    h1='Tredici campi, due versanti',
    lead='La salita, in forma attiva, ordinata in base a quanto spesso userai davvero ogni tempo. La discesa, in forma passiva: gli stessi tredici campi al contrario &mdash; nove dei quali con un passivo che vale la pena imparare.',
    countsAria="Che cosa c'è sul percorso", cUp='campi in salita', cDown='passivi in discesa', cOff='fuori percorso', cFree='gratis',
    everyStop='Tutte le tappe', mapKick='La mappa', mapH2="Su all'attivo, giù al passivo",
    mapHow="La salita non ha lucchetti: comincia dal campo che ti serve. Ogni tappa della discesa si apre quando finisci il campo da cui viene; fino ad allora il suo segnaposto è grigio.",
    guideKick='Sei nuovo qui?', guideLine="Due minuti su che cos'è un tempo verbale, che cosa significano attivo e passivo, e perché i campi sono in quest'ordine.",
    guideBtn='Che cosa sto guardando?', ascH='La salita', ascSub='forma attiva &middot; dal campo base alla vetta',
    descH='La discesa', descSub='forma passiva &middot; dalla vetta a valle',
    ascAria="La salita: una montagna con tredici segnaposti colorati su un sentiero dal campo base alla vetta, uno per ogni tempo in forma attiva, e due nuvole per used to e be used to. Tutte le tappe sono elencate anche sotto la mappa.",
    descAria="La discesa: la stessa montagna di notte, con un rombo per ogni tempo in forma passiva, dalla vetta in giù. Nove sono lezioni, ognuna si apre quando finisci il suo campo; quattro restano al buio perché nessuno usa quei passivi. La luna è il causativo. Tutte le tappe sono elencate anche sotto la mappa.",
    lgColour='a colori &mdash; tocca per andare', lgGrey='grigio &mdash; si apre quando finisci il suo campo',
    lgShape='cerchio = forma attiva, rombo = forma passiva', ascList='La salita &middot; forma attiva',
    zFH='Campi base', zFSub='li userai ogni giorno', zRH='La cresta', zRSub='frequenti, ma chiedono più attenzione',
    zSH='Assalto alla vetta', zSSub="rari, soprattutto nell'inglese scritto",
    descList='La discesa &middot; forma passiva', descListSub='ognuna si apre quando finisci il campo da cui viene',
    offH='Fuori percorso', offSub='non sono tempi, ma litigano con uno di loro',
    offUsedTo='dopo il campo 2 o 3', offBeUsedTo='dopo il campo 2', offCausative='dopo la tua prima tappa in discesa',
    free='Gratis', level='Livello', aboutRoute='Sul percorso', whereH='A che punto sei',
    darkH='Quattro tappe della discesa restano al buio apposta',
    darkP="I passivi del present perfect continuous, del past perfect continuous, del future continuous e del future perfect continuous si possono costruire &mdash; HAS BEEN BEING CLEANED, WILL BE BEING CLEANED &mdash; ma i madrelingua li evitano tutti e riformulano la frase. Lì non c'è niente da imparare, quindi non c'è un campo.",
    teachH='Insegni?',
    teachP='L\'interruttore sotto la mappa toglie in un colpo solo tutti i lucchetti di avanzamento in questo browser &mdash; per lo schermo in aula, o per una classe che ha già fatto la salita. Le lezioni Pro richiedono comunque Pro. <a href="block-camp.html">Block Camp</a> sale lungo nove di questi tempi in un mondo fatto di blocchi.',
    proP='<strong>Quattro lezioni sono gratis, senza registrazione:</strong> i campi uno e due, il passivo che si apre con il campo uno e <em>used to</em>. Pro apre le altre ventuno, e tutte le altre lezioni del sito.',
    plans='Piani e prezzi',
    gKick='Prima di salire', gTitle='Che cosa stai guardando', gClose='Chiudi la guida',
    g1H='Un tempo verbale è un momento e una forma',
    g1P="Ogni tempo colloca un'azione nel passato, nel presente o nel futuro, e le dà una di quattro forme: <b>simple</b> (il fatto e basta), <b>continuous</b> (in corso), <b>perfect</b> (uno sguardo indietro da un punto successivo: adesso, o un momento del passato o del futuro) o <b>perfect continuous</b> (in corso fino a quel punto). Tre momenti, quattro forme: dodici dei tredici campi. Ogni forma qui sotto è &laquo;she&raquo; + CLIMB, e il numero è il suo campo.",
    gCaption='I dodici tempi per momento e forma; ognuno porta al suo campo.',
    gGoing='Quello che resta, il campo 5, è un futuro che si vede già arrivare.',
    g2H='Due versanti: attivo e passivo',
    gAsc="<b>La salita &middot; attivo.</b> Chi compie l'azione viene prima.",
    gDesc="<b>La discesa &middot; passivo.</b> Viene prima ciò che subisce l'azione, e chi la compie può sparire.",
    g2P="Lo stesso tempo, capovolto: il passivo è BE in quel tempo + il PAST PARTICIPLE. Per questo ogni tappa della discesa è la gemella di un campo della salita, e si apre quando finisci quel campo.",
    g3H="Perché quest'ordine",
    g3P="I campi salgono nell'ordine in cui ti serviranno, non in quello dei libri di grammatica. I <b>campi base</b> sono i tempi che usi ogni giorno; <b>la cresta</b> è frequente ma chiede più attenzione; l'<b>assalto alla vetta</b> è raro e soprattutto scritto. Quattro passivi non hanno un campo: si possono costruire &mdash; HAS BEEN BEING CLEANED &mdash; ma nessuno li dice.",
    g3Map="Sulla mappa, un cerchio è attivo, un rombo è passivo, e il grigio vuol dire non ancora aperto; un rombo tenue con scritto &laquo;no camp&raquo; non si apre mai. Le nuvole sono &laquo;used to&raquo; e &laquo;be used to&raquo;; la luna è il causativo.",
    startFree='Comincia dal campo uno &middot; gratis', backMap='Torna alla mappa',
    carryOn='Continua: campo {n} &middot; {name}', headDown='Scendi: {name}', offRoute='Fuori percorso: {name}',
    again='Risali: campo uno',
    lockNote='<strong>{c} su 13</strong> campi &middot; <strong>{d} su 9</strong> tappe in discesa &mdash; {tail}',
    tailAll='è tutto aperto.', tailWhole='tutta la montagna è aperta, su entrambi i versanti.',
    tailDefault='nove dei campi aprono un passivo; <em>used to</em> si apre dopo il campo 2 o 3, <em>be used to</em> dopo il campo 2, e il causativo dopo la tua prima tappa in discesa.',
    teachOff='Sto insegnando &mdash; apri tutto', teachOn='Lucchetti tolti &mdash; è tutto aperto',
    teachWhy="Gli studenti aprono ogni passivo, e le tre lezioni fuori percorso, finendo il campo da cui vengono. Gli insegnanti, e chi ha fretta, possono aprire tutto.",
    pair='il campo {n} ({tense})', whyDescent='Finisci {pair} e questa si apre.',
    whyUsedTo="Finisci il campo 2 o il campo 3 &mdash; used to è un'abitudine del present simple spostata nel passato.",
    whyBeUsedTo='Finisci il campo 2 (present simple) &mdash; be used to è uno stato, non un evento.',
    whyCausative='Finisci una qualsiasi tappa della discesa &mdash; il causativo è un passivo con il cappello.',
    srLocked=' (bloccato: {why})', srDone=' (fatto)', fromOpen='dal campo {n}', fromLocked='dopo il campo {n}',
    hintNoCamp='{label}: qui non c\'è un campo &mdash; leggi la nota sotto gli elenchi.', hintLocked='{label}. {why}',
)

LANGS['pt'] = dict(
    langGroup='Idioma', sub='uma trilha de subida pelos tempos verbais', eyebrow='Mapa da trilha',
    h1='Treze acampamentos, duas faces',
    lead='A subida, na voz ativa, ordenada pela frequência com que você vai realmente usar cada tempo. A descida, na voz passiva: os mesmos treze acampamentos ao contrário &mdash; nove deles com uma passiva que vale a pena aprender.',
    countsAria='O que há na trilha', cUp='acampamentos na subida', cDown='passivas na descida', cOff='fora da trilha', cFree='grátis',
    everyStop='Todas as paradas', mapKick='O mapa', mapH2='Subida na ativa, descida na passiva',
    mapHow="A subida não tem cadeados: comece pelo acampamento de que você precisa. Cada parada da descida se abre quando você termina o acampamento de onde ela vem; até lá, o marcador dela fica cinza.",
    guideKick='Primeira vez aqui?', guideLine="Dois minutos sobre o que é um tempo verbal, o que significam ativa e passiva, e por que os acampamentos vêm nesta ordem.",
    guideBtn='O que estou vendo?', ascH='A subida', ascSub='voz ativa &middot; do acampamento-base ao cume',
    descH='A descida', descSub='voz passiva &middot; do cume ao vale',
    ascAria="A subida: uma montanha com treze marcadores coloridos numa trilha do acampamento-base ao cume, um para cada tempo na voz ativa, e duas nuvens para used to e be used to. Todas as paradas também estão listadas abaixo do mapa.",
    descAria="A descida: a mesma montanha à noite, com um losango para cada tempo na voz passiva, do cume para baixo. Nove são lições, e cada uma se abre quando você termina o acampamento dela; quatro ficam apagadas porque ninguém usa essas passivas. A lua é o causativo. Todas as paradas também estão listadas abaixo do mapa.",
    lgColour='colorido &mdash; toque para ir', lgGrey='cinza &mdash; abre quando você termina o acampamento de origem',
    lgShape='círculo = voz ativa, losango = voz passiva', ascList='A subida &middot; voz ativa',
    zFH='Acampamentos-base', zFSub='você vai usar todo dia', zRH='A crista', zRSub='comuns, mas pedem mais cuidado',
    zSH='Ataque ao cume', zSSub='raros, sobretudo no inglês escrito',
    descList='A descida &middot; voz passiva', descListSub='cada uma se abre quando você termina o acampamento de onde ela vem',
    offH='Fora da trilha', offSub='não são tempos, mas discutem com um deles',
    offUsedTo='depois do acampamento 2 ou 3', offBeUsedTo='depois do acampamento 2', offCausative='depois da sua primeira parada na descida',
    free='Grátis', level='Nível', aboutRoute='Sobre a trilha', whereH='Onde você está',
    darkH='Quatro paradas da descida ficam apagadas de propósito',
    darkP='As passivas do present perfect continuous, do past perfect continuous, do future continuous e do future perfect continuous podem ser formadas &mdash; HAS BEEN BEING CLEANED, WILL BE BEING CLEANED &mdash; mas os falantes nativos evitam todas elas e reformulam a frase. Não há nada para aprender ali, então não há acampamento.',
    teachH='Você dá aula?',
    teachP="O botão abaixo do mapa tira de uma vez todos os cadeados de progresso neste navegador &mdash; para a tela da sala de aula, ou para uma turma que já fez a subida. As lições Pro continuam exigindo Pro. <a href=\"block-camp.html\">Block Camp</a> sobe por nove destes tempos num mundo feito de blocos.",
    proP="<strong>Quatro lições são grátis, sem cadastro:</strong> os acampamentos um e dois, a passiva que o acampamento um abre, e <em>used to</em>. O Pro abre as outras vinte e uma, e todas as outras lições do site.",
    plans='Planos e preços',
    gKick='Antes de subir', gTitle='O que você está vendo', gClose='Fechar o guia',
    g1H='Um tempo verbal é um momento e uma forma',
    g1P="Cada tempo coloca uma ação no passado, no presente ou no futuro, e dá a ela uma de quatro formas: <b>simple</b> (o fato puro), <b>continuous</b> (em andamento), <b>perfect</b> (um olhar para trás a partir de um ponto posterior: agora, ou um momento do passado ou do futuro) ou <b>perfect continuous</b> (em andamento até esse ponto). Três momentos, quatro formas: doze dos treze acampamentos. Cada forma abaixo é &ldquo;she&rdquo; + CLIMB, e o número é o acampamento dela.",
    gCaption='Os doze tempos por momento e forma; cada um leva ao seu acampamento.',
    gGoing='O que sobra, o acampamento 5, é um futuro que já dá para ver chegando.',
    g2H='Duas faces: ativa e passiva',
    gAsc='<b>A subida &middot; ativa.</b> Quem faz a ação vem primeiro.',
    gDesc='<b>A descida &middot; passiva.</b> Vem primeiro aquilo que sofre a ação, e quem a faz pode sumir.',
    g2P="O mesmo tempo, virado ao contrário: a passiva é BE nesse tempo + o PAST PARTICIPLE. Por isso cada parada da descida é gêmea de um acampamento da subida, e se abre quando você termina esse acampamento.",
    g3H='Por que esta ordem',
    g3P="Os acampamentos sobem na ordem em que você vai precisar deles, não na dos livros de gramática. Os <b>acampamentos-base</b> são os tempos que você usa todo dia; <b>a crista</b> é comum, mas pede mais cuidado; o <b>ataque ao cume</b> é raro e sobretudo escrito. Quatro passivas não têm acampamento: dá para formá-las &mdash; HAS BEEN BEING CLEANED &mdash; mas ninguém as diz.",
    g3Map='No mapa, um círculo é a voz ativa, um losango é a voz passiva, e o cinza quer dizer que ainda não abriu; um losango apagado marcado &ldquo;no camp&rdquo; nunca se abre. As nuvens são &ldquo;used to&rdquo; e &ldquo;be used to&rdquo;; a lua é o causativo.',
    startFree='Começar no acampamento um &middot; grátis', backMap='Voltar ao mapa',
    carryOn='Continue: acampamento {n} &middot; {name}', headDown='Desça: {name}', offRoute='Fora da trilha: {name}',
    again='Suba de novo: acampamento um',
    lockNote='<strong>{c} de 13</strong> acampamentos &middot; <strong>{d} de 9</strong> paradas na descida &mdash; {tail}',
    tailAll='tudo está aberto.', tailWhole='a montanha inteira está aberta, nas duas faces.',
    tailDefault='nove dos acampamentos abrem uma passiva; <em>used to</em> se abre depois do acampamento 2 ou 3, <em>be used to</em> depois do 2, e o causativo depois da sua primeira parada na descida.',
    teachOff='Estou dando aula &mdash; abrir tudo', teachOn='Sem cadeados &mdash; tudo está aberto',
    teachWhy='Os alunos abrem cada passiva, e as três lições fora da trilha, terminando o acampamento de onde elas vêm. Professores, e quem estiver com pressa, podem abrir tudo.',
    pair='o acampamento {n} ({tense})', whyDescent='Termine {pair} e esta parada se abre.',
    whyUsedTo='Termine o acampamento 2 ou o 3 &mdash; used to é um hábito do present simple levado para o passado.',
    whyBeUsedTo='Termine o acampamento 2 (present simple) &mdash; be used to é um estado, não um acontecimento.',
    whyCausative='Termine qualquer parada da descida &mdash; o causativo é uma passiva de chapéu.',
    srLocked=' (bloqueado: {why})', srDone=' (feito)', fromOpen='do acampamento {n}', fromLocked='depois do acampamento {n}',
    hintNoCamp='{label}: aqui não há acampamento &mdash; veja a nota abaixo das listas.', hintLocked='{label}. {why}',
)

LANGS['ru'] = dict(
    langGroup='Язык', sub='маршрут вверх по английским временам', eyebrow='Карта маршрута',
    h1='Тринадцать лагерей, два склона',
    lead='Подъём — в активном залоге, и лагеря на нём расставлены по тому, как часто тебе на самом деле понадобится каждое время. Спуск — в пассивном: те же тринадцать лагерей в обратном порядке &mdash; у девяти из них есть пассив, который стоит выучить.',
    countsAria='Что есть на маршруте', cUp='лагерей на подъёме', cDown='пассивов на спуске', cOff='в стороне от маршрута', cFree='бесплатных',
    everyStop='Все остановки', mapKick='Карта', mapH2='Вверх — в активном залоге, вниз — в пассивном',
    mapHow='На подъёме нет замков: начинай с того лагеря, который тебе нужен. Каждая остановка на спуске открывается, когда ты проходишь лагерь, к которому она привязана; до этого её отметка серая.',
    guideKick='Впервые здесь?', guideLine='Две минуты о том, что такое время глагола, что значат актив и пассив и почему лагеря идут в таком порядке.',
    guideBtn='Что здесь показано?', ascH='Подъём', ascSub='активный залог &middot; от базового лагеря до вершины',
    descH='Спуск', descSub='пассивный залог &middot; от вершины к подножию',
    ascAria='Подъём: гора с тринадцатью цветными отметками лагерей на тропе от базового лагеря до вершины, по одной на каждое время в активном залоге, и двумя облаками для used to и be used to. Все остановки перечислены и под картой.',
    descAria='Спуск: та же гора ночью, с ромбом для каждого времени в пассивном залоге, от вершины вниз. Девять из них — уроки, каждый открывается, когда ты проходишь его лагерь; четыре остаются тёмными, потому что этими пассивами никто не пользуется. Луна — это каузатив. Все остановки перечислены и под картой.',
    lgColour='цветная &mdash; нажми, чтобы перейти', lgGrey='серая &mdash; откроется, когда пройдёшь её лагерь',
    lgShape='круг = активный залог, ромб = пассивный залог', ascList='Подъём &middot; активный залог',
    zFH='Базовые лагеря', zFSub='нужны каждый день', zRH='Гребень', zRSub='встречаются часто, но требуют внимания',
    zSH='Штурм вершины', zSSub='редкие, в основном в письменном английском',
    descList='Спуск &middot; пассивный залог', descListSub='каждая открывается, когда ты проходишь лагерь, к которому она привязана',
    offH='В стороне от маршрута', offSub='это не времена, но они спорят с одним из них',
    offUsedTo='после лагеря 2 или 3', offBeUsedTo='после лагеря 2', offCausative='после твоей первой остановки на спуске',
    free='Бесплатно', level='Уровень', aboutRoute='О маршруте', whereH='Где ты сейчас',
    darkH='Четыре остановки спуска намеренно остаются тёмными',
    darkP='Пассив от present perfect continuous, past perfect continuous, future continuous и future perfect continuous построить можно &mdash; HAS BEEN BEING CLEANED, WILL BE BEING CLEANED, &mdash; но носители языка избегают всех этих форм и перестраивают фразу. Учить там нечего, поэтому и лагеря там нет.',
    teachH='Ты преподаёшь?',
    teachP='Переключатель под картой разом снимает все замки в этом браузере &mdash; для показа на экране в классе или для группы, которая уже проходила этот подъём. Для уроков Pro по-прежнему нужен Pro. <a href="block-camp.html">Block Camp</a> проходит девять из этих времён в мире из блоков.',
    proP='<strong>Четыре урока бесплатны, без регистрации:</strong> лагеря 1 и 2, пассив, который открывается после лагеря 1, и <em>used to</em>. Pro открывает оставшиеся двадцать один и все другие уроки на сайте.',
    plans='Тарифы и цены',
    gKick='Перед подъёмом', gTitle='Что здесь показано', gClose='Закрыть справку',
    g1H='Время — это момент и форма',
    g1P='Каждое время помещает действие в прошлое, настоящее или будущее и придаёт ему одну из четырёх форм: <b>simple</b> (просто факт), <b>continuous</b> (в процессе), <b>perfect</b> (взгляд назад из более поздней точки: сейчас или момент в прошлом либо будущем) или <b>perfect continuous</b> (в процессе вплоть до этой точки). Три момента, четыре формы: двенадцать из тринадцати лагерей. Каждая ячейка таблицы ниже — это &laquo;she&raquo; + CLIMB, а число — номер её лагеря.',
    gCaption='Двенадцать времён по моменту и форме; каждое ведёт в свой лагерь.',
    gGoing='Оставшийся, лагерь 5, — это будущее, которое уже видно издалека.',
    g2H='Два склона: актив и пассив',
    gAsc='<b>Подъём &middot; актив.</b> Тот, кто действует, стоит первым.',
    gDesc='<b>Спуск &middot; пассив.</b> Первым стоит то, с чем происходит действие, а того, кто действует, можно опустить.',
    g2P='То же время, только наоборот: пассив — это BE в этом времени + PAST PARTICIPLE. Поэтому каждая остановка на спуске — близнец лагеря на подъёме и открывается, когда ты проходишь этот лагерь.',
    g3H='Почему такой порядок',
    g3P='Лагеря идут в том порядке, в каком они тебе понадобятся, а не как в учебниках грамматики. <b>Базовые лагеря</b> — это времена, которыми ты пользуешься каждый день; времена <b>гребня</b> встречаются часто, но требуют внимания; <b>штурм вершины</b> — это редкие времена, в основном из письменной речи. У четырёх пассивов нет лагеря: их можно построить &mdash; HAS BEEN BEING CLEANED, &mdash; но никто так не говорит.',
    g3Map='На карте круг — это актив, ромб — пассив, а серый цвет значит «ещё не открыто»; бледный ромб с надписью &laquo;no camp&raquo; не откроется никогда. Облака — это &laquo;used to&raquo; и &laquo;be used to&raquo;; луна — каузатив.',
    startFree='Начать с первого лагеря &middot; бесплатно', backMap='Назад к карте',
    carryOn='Дальше: лагерь {n} &middot; {name}', headDown='Вниз: {name}', offRoute='В стороне от маршрута: {name}',
    again='Подняться ещё раз: лагерь 1',
    lockNote='<strong>{c} из 13</strong> лагерей &middot; <strong>{d} из 9</strong> остановок спуска &mdash; {tail}',
    tailAll='всё открыто.', tailWhole='вся гора открыта, оба склона.',
    tailDefault='девять лагерей открывают по пассиву; <em>used to</em> открывается после лагеря 2 или 3, <em>be used to</em> — после лагеря 2, каузатив — после твоей первой остановки на спуске.',
    teachOff='Я преподаю &mdash; открыть всё', teachOn='Замки сняты &mdash; всё открыто',
    teachWhy='Ученики открывают каждый пассив и каждый из трёх уроков в стороне от маршрута, проходя лагерь, к которому он привязан. Преподаватели и все, кто спешит, могут открыть всё сразу.',
    pair='лагерь {n} ({tense})', whyDescent='Пройди {pair}, и эта остановка откроется.',
    whyUsedTo='Пройди лагерь 2 или лагерь 3, ведь used to — это привычка из present simple, перенесённая в прошлое.',
    whyBeUsedTo='Пройди лагерь 2 (present simple), ведь be used to — это состояние, а не событие.',
    whyCausative='Пройди любую остановку на спуске, ведь каузатив — это пассив в шляпе.',
    srLocked=' (закрыто: {why})', srDone=' (пройдено)', fromOpen='из лагеря {n}', fromLocked='после лагеря {n}',
    hintNoCamp='{label}: здесь нет лагеря &mdash; см. пояснение под списками.', hintLocked='{label}: {why}',
)

LANGS['ar'] = dict(
    langGroup='اللغة', sub='طريق صاعد عبر الأزمنة', eyebrow='خريطة الطريق',
    h1='ثلاثة عشر مخيمًا، ووجهان',
    lead='الصعود بصيغة المبني للمعلوم، مرتّبًا بحسب عدد المرات التي ستحتاج فيها فعلًا إلى كل زمن. والنزول بصيغة المبني للمجهول: المخيمات الثلاثة عشر نفسها بترتيب معكوس &mdash; لتسعة منها صيغة مجهول تستحق التعلّم.',
    countsAria='ما يوجد على الطريق', cUp='مخيمًا في الصعود', cDown='صيغ مجهول في النزول', cOff='خارج الطريق', cFree='مجانية',
    everyStop='كل المحطات', mapKick='الخريطة', mapH2='صعودًا بالمعلوم، ونزولًا بالمجهول',
    mapHow='لا أقفال في طريق الصعود: ابدأ من المخيم الذي تحتاجه. وكل محطة في طريق النزول تُفتح حين تُنهي المخيم الذي تأتي منه؛ وحتى ذلك الحين تبقى علامتها رمادية.',
    guideKick='جديد هنا؟', guideLine='دقيقتان عن معنى الزمن، ومعنى المبني للمعلوم والمبني للمجهول، ولماذا تأتي المخيمات بهذا الترتيب.',
    guideBtn='ما الذي أراه؟', ascH='الصعود', ascSub='المبني للمعلوم &middot; من المخيم الأساسي إلى القمة',
    descH='النزول', descSub='المبني للمجهول &middot; من القمة إلى الوادي',
    ascAria='الصعود: جبل عليه ثلاث عشرة علامة ملوّنة للمخيمات على درب من المخيم الأساسي إلى القمة، علامة لكل زمن بصيغة المبني للمعلوم، وسحابتان لـ used to و be used to. كل المحطات مذكورة أيضًا تحت الخريطة.',
    descAria='النزول: الجبل نفسه ليلًا، عليه معيّن لكل زمن بصيغة المبني للمجهول، من القمة إلى الأسفل. تسعة منها دروس، يُفتح كل منها حين تُنهي مخيمه؛ وأربعة تبقى مظلمة لأن أحدًا لا يستعمل صيغ المجهول تلك. والقمر هو صيغة السببية. كل المحطات مذكورة أيضًا تحت الخريطة.',
    lgColour='ملوّنة &mdash; اضغط للانتقال', lgGrey='رمادية &mdash; تُفتح حين تُنهي مخيمها',
    lgShape='دائرة = المبني للمعلوم، معيّن = المبني للمجهول', ascList='الصعود &middot; المبني للمعلوم',
    zFH='المخيمات الأساسية', zFSub='تستعملها كل يوم', zRH='الحافة', zRSub='شائعة، لكنها تحتاج إلى عناية أكبر',
    zSH='الهجوم على القمة', zSSub='نادرة، وأغلبها في الإنجليزية المكتوبة',
    descList='النزول &middot; المبني للمجهول', descListSub='كل واحدة تُفتح حين تُنهي المخيم الذي تأتي منه',
    offH='خارج الطريق', offSub='ليست أزمنة، لكنها تتجادل مع زمن',
    offUsedTo='بعد المخيم 2 أو 3', offBeUsedTo='بعد المخيم 2', offCausative='بعد أول محطة لك في النزول',
    free='مجاني', level='المستوى', aboutRoute='عن الطريق', whereH='أين أنت الآن',
    darkH='أربع محطات في النزول تبقى مظلمة عن قصد',
    darkP='يمكن اشتقاق المبني للمجهول من present perfect continuous و past perfect continuous و future continuous و future perfect continuous &mdash; HAS BEEN BEING CLEANED، WILL BE BEING CLEANED &mdash; لكن أهل اللغة يتجنّبون هذه الصيغ كلها ويعيدون صياغة الجملة بدلًا منها. فليس هناك ما يُتعلَّم، ولذلك لا مخيم هناك.',
    teachH='هل تُدرِّس؟',
    teachP='المفتاح الموجود تحت الخريطة يرفع كل أقفال التقدّم في هذا المتصفح دفعة واحدة &mdash; لشاشة الصف، أو لمجموعة أنهت الصعود من قبل. دروس Pro ما زالت تحتاج إلى Pro. <a href="block-camp.html">Block Camp</a> يصعد عبر تسعة من هذه الأزمنة في عالم مبني من المكعّبات.',
    proP='<strong>أربعة دروس مجانية، بلا تسجيل دخول:</strong> المخيمان الأول والثاني، والمبني للمجهول الذي يفتحه المخيم الأول، و<em>used to</em>. أما Pro فيفتح الدروس الواحد والعشرين الباقية، وكل درس آخر في الموقع.',
    plans='الخطط والأسعار',
    gKick='قبل أن تصعد', gTitle='ما الذي تراه', gClose='إغلاق الدليل',
    g1H='الزمن وقتٌ وشكل',
    g1P='كل زمن يضع الحدث في الماضي أو الحاضر أو المستقبل، ويعطيه واحدًا من أربعة أشكال: <b>simple</b> (الحقيقة المجرّدة)، <b>continuous</b> (قيد الحدوث)، <b>perfect</b> (نظرة إلى الوراء من نقطة لاحقة: الآن، أو لحظة في الماضي أو المستقبل) أو <b>perfect continuous</b> (قيد الحدوث حتى تلك النقطة). ثلاثة أوقات، وأربعة أشكال: اثنا عشر مخيمًا من أصل ثلاثة عشر. كل صيغة أدناه هي &laquo;she&raquo;&rlm; + CLIMB، والرقم هو مخيمها.',
    gCaption='الأزمنة الاثنا عشر بحسب الوقت والشكل؛ كل واحد منها يقود إلى مخيمه.',
    gGoing='أما الزمن المتبقّي، المخيم 5، فمستقبلٌ ترى بوادره من الآن.',
    g2H='وجهان: المعلوم والمجهول',
    gAsc='<b>الصعود &middot; المبني للمعلوم.</b> الفاعل يأتي أولًا.',
    gDesc='<b>النزول &middot; المبني للمجهول.</b> يأتي أولًا ما يقع عليه الفعل، ويمكن أن يختفي الفاعل.',
    g2P='الزمن نفسه، مقلوبًا: المبني للمجهول هو BE في ذلك الزمن + PAST PARTICIPLE. ولهذا فكل محطة في النزول توأمٌ لمخيم في الصعود، وتُفتح حين تُنهي ذلك المخيم.',
    g3H='لماذا هذا الترتيب',
    g3P='تصعد المخيمات بحسب ترتيب حاجتك إليها، لا بالترتيب الذي تتبعه كتب القواعد. <b>المخيمات الأساسية</b> هي الأزمنة التي تستعملها كل يوم؛ و<b>الحافة</b> شائعة لكنها تحتاج إلى عناية أكبر؛ و<b>الهجوم على القمة</b> نادر وأغلبه مكتوب. أربع صيغ للمجهول لا مخيم لها: يمكن بناؤها &mdash; HAS BEEN BEING CLEANED &mdash; لكن لا أحد يقولها.',
    g3Map='على الخريطة، الدائرة للمبني للمعلوم، والمعيّن للمبني للمجهول، والرمادي يعني أنه لم يُفتح بعد؛ والمعيّن الباهت المكتوب عليه &laquo;no camp&raquo; لا يُفتح أبدًا. السحابتان هما &laquo;used to&raquo; و&laquo;be used to&raquo;؛ والقمر هو صيغة السببية.',
    startFree='ابدأ من المخيم الأول &middot; مجانًا', backMap='العودة إلى الخريطة',
    carryOn='&#x2067;تابع: المخيم {n} &middot; {name}&#x2069;', headDown='&#x2067;انزل: {name}&#x2069;', offRoute='&#x2067;خارج الطريق: {name}&#x2069;',
    again='اصعد من جديد: المخيم الأول',
    lockNote='&#x2067;<strong>{c} من 13</strong> مخيمًا &middot; <strong>{d} من 9</strong> محطات نزول &mdash; {tail}&#x2069;',
    tailAll='كل شيء مفتوح.', tailWhole='الجبل كله مفتوح، بوجهيه.',
    tailDefault='تسعة من المخيمات تفتح صيغة مجهول؛ <em>used to</em> يُفتح بعد المخيم 2 أو 3، و<em>be used to</em> بعد المخيم 2، وصيغة السببية بعد أول محطة لك في النزول.',
    teachOff='أنا أُدرِّس هذا &mdash; افتح كل شيء', teachOn='الأقفال مرفوعة &mdash; كل شيء مفتوح',
    teachWhy='يفتح المتعلّمون كل صيغة مجهول، والدروس الثلاثة خارج الطريق، بإنهاء المخيم الذي تأتي منه. أما المعلّمون، ومن كان على عجلة، فيمكنهم فتح كل شيء.',
    pair='المخيم {n} ({tense})', whyDescent='أنهِ {pair} فتُفتح هذه المحطة.',
    whyUsedTo='أنهِ المخيم 2 أو المخيم 3 &mdash; used to عادةٌ من present simple نُقلت إلى الماضي.',
    whyBeUsedTo='أنهِ المخيم 2 (present simple) &mdash; be used to حالةٌ لا حدث.',
    whyCausative='أنهِ أي محطة في النزول &mdash; صيغة السببية مبنيٌّ للمجهول يعتمر قبعة.',
    srLocked=' (مقفل: {why})', srDone=' (مُنجَز)', fromOpen='من المخيم {n}', fromLocked='بعد المخيم {n}',
    hintNoCamp='&#x2067;{label}: لا مخيم هنا &mdash; انظر الملاحظة تحت القوائم.&#x2069;', hintLocked='&#x2067;{label}: {why}&#x2069;',
)

LANGS['zh'] = dict(
    langGroup='语言', sub='一条向上穿越时态的路线', eyebrow='路线图',
    h1='十三座营地，两面山坡',
    lead='上山用主动语态，按你实际用到各个时态的频率排列。下山用被动语态：还是这十三座营地，顺序反过来&mdash;&mdash;其中九座有值得学的被动语态。',
    countsAria='路线上有什么', cUp='座上山营地', cDown='个下山被动语态', cOff='节路线外的课', cFree='节免费课',
    everyStop='所有站点', mapKick='地图', mapH2='上山用主动，下山用被动',
    mapHow='上山的路没有锁：从你需要的营地开始。下山路上的每一站，要等你完成它所对应的营地才会打开；在那之前，它的标记是灰色的。',
    guideKick='第一次来？', guideLine='用两分钟了解什么是时态、主动和被动是什么意思，以及营地为什么按这个顺序排列。',
    guideBtn='这张地图怎么看？', ascH='上山', ascSub='主动语态 &middot; 从大本营到山顶',
    descH='下山', descSub='被动语态 &middot; 从山顶到山谷',
    ascAria='上山：一座山，从大本营到山顶的小路上有十三个彩色营地标记，每个对应一个主动语态的时态，还有两朵云，分别是 used to 和 be used to。所有站点也列在地图下方。',
    descAria='下山：夜里的同一座山，从山顶往下，每个被动语态的时态都有一个菱形标记。其中九个是课程，完成对应的营地就会打开；四个一直是暗的，因为没人用那些被动形式。月亮是使役结构。所有站点也列在地图下方。',
    lgColour='彩色&mdash;&mdash;点击即可前往', lgGrey='灰色&mdash;&mdash;完成对应的营地后打开',
    lgShape='圆形 = 主动语态，菱形 = 被动语态', ascList='上山 &middot; 主动语态',
    zFH='基础营地', zFSub='天天都用得上', zRH='山脊', zRSub='常用，但需要多加注意',
    zSH='冲顶', zSSub='少见，多用于书面英语',
    descList='下山 &middot; 被动语态', descListSub='每一站都在你完成对应的营地后打开',
    offH='路线之外', offSub='它们不是时态，却总和某个时态较劲',
    offUsedTo='完成营地 2 或 3 后', offBeUsedTo='完成营地 2 后', offCausative='完成你的第一个下山站后',
    free='免费', level='级别', aboutRoute='关于这条路线', whereH='你现在的位置',
    darkH='下山路上有四站故意不点亮',
    darkP='present perfect continuous、past perfect continuous、future continuous 和 future perfect continuous 的被动语态都能造出来&mdash;&mdash;HAS BEEN BEING CLEANED、WILL BE BEING CLEANED&mdash;&mdash;但母语者全都避免使用，而是把句子换个说法。那里没什么可学的，所以也就没有营地。',
    teachH='你在教这门课吗？',
    teachP='地图下方的开关可以在这个浏览器里一次解除所有进度锁&mdash;&mdash;适合课堂大屏幕，或已经爬过一遍的班级。Pro 课程仍然需要 Pro。<a href="block-camp.html">Block Camp</a> 在一个由方块搭成的世界里攀登其中九个时态。',
    proP='<strong>四节课免费，无需注册：</strong>营地一和营地二、营地一打开的被动语态，以及 <em>used to</em>。Pro 解锁其余二十一节课，以及网站上的所有其他课程。',
    plans='方案与价格',
    gKick='出发之前', gTitle='看懂这张地图', gClose='关闭说明',
    g1H='时态 = 时间 + 形态',
    g1P='每个时态都把动作放在过去、现在或将来，并给它四种形态之一：<b>simple</b>（单纯的事实）、<b>continuous</b>（正在进行）、<b>perfect</b>（从较晚的某个时间点回头看：现在，或过去、将来的某一刻）或 <b>perfect continuous</b>（一直持续到那个时间点）。三个时间，四种形态：十三座营地中的十二座。下面每个形式都是 &ldquo;she&rdquo; + CLIMB，数字是它所在的营地。',
    gCaption='十二个时态，按时间和形态排列；每个都链接到自己的营地。',
    gGoing='剩下的那一座，营地 5，是一个你已经看得见、正在到来的将来。',
    g2H='两面山坡：主动与被动',
    gAsc='<b>上山 &middot; 主动。</b>做动作的人在前面。',
    gDesc='<b>下山 &middot; 被动。</b>承受动作的事物在前面，做动作的人可以不出现。',
    g2P='同一个时态，倒过来：被动语态就是该时态的 BE + PAST PARTICIPLE。所以下山的每一站都是上山某个营地的双胞胎，完成那个营地它就会打开。',
    g3H='为什么是这个顺序',
    g3P='营地按照你会需要它们的顺序往上排，而不是语法书的顺序。<b>基础营地</b>是你每天都用的时态；<b>山脊</b>很常用，但需要多加注意；<b>冲顶</b>少见，多出现在书面语里。有四个被动语态没有营地：它们造得出来&mdash;&mdash;HAS BEEN BEING CLEANED&mdash;&mdash;但没人这么说。',
    g3Map='在地图上，圆形是主动，菱形是被动，灰色表示还没打开；标着 &ldquo;no camp&rdquo; 的浅色菱形永远不会打开。两朵云是 &ldquo;used to&rdquo; 和 &ldquo;be used to&rdquo;；月亮是使役结构。',
    startFree='从营地一开始 &middot; 免费', backMap='回到地图',
    carryOn='继续：营地 {n} &middot; {name}', headDown='下山：{name}', offRoute='路线之外：{name}',
    again='再爬一次：营地一',
    lockNote='营地 <strong>{c}/13</strong> &middot; 下山站 <strong>{d}/9</strong>&mdash;&mdash;{tail}',
    tailAll='全部已打开。', tailWhole='整座山的两面都已打开。',
    tailDefault='九座营地各自打开一个被动语态；<em>used to</em> 在营地 2 或 3 之后打开，<em>be used to</em> 在营地 2 之后，使役结构在你的第一个下山站之后。',
    teachOff='我在教这个&mdash;&mdash;全部打开', teachOn='锁已解除&mdash;&mdash;全部已打开',
    teachWhy='学习者完成对应的营地，就能打开每个被动语态和三节路线外的课。老师和赶时间的人可以一次全部打开。',
    pair='营地 {n}（{tense}）', whyDescent='完成{pair}，这一站就会打开。',
    whyUsedTo='完成营地 2 或营地 3&mdash;&mdash;used to 是把 present simple 的习惯搬到了过去。',
    whyBeUsedTo='完成营地 2（present simple）&mdash;&mdash;be used to 是一种状态，而不是一个事件。',
    whyCausative='完成任意一个下山站&mdash;&mdash;使役结构就是戴了帽子的被动语态。',
    srLocked='（已锁：{why}）', srDone='（已完成）', fromOpen='来自营地 {n}', fromLocked='营地 {n} 之后',
    hintNoCamp='{label}：这里没有营地&mdash;&mdash;请看列表下方的说明。', hintLocked='{label}：{why}',
)

LANGS['ja'] = dict(
    langGroup='言語', sub='時制をのぼっていくルート', eyebrow='ルートマップ',
    h1='13のキャンプ、2つの斜面',
    lead='登りは能動態で、実際によく使う時制から順に並んでいます。下りは受動態で、同じ13のキャンプを逆の順にたどります。そのうち9つには、学ぶ価値のある受動態があります。',
    countsAria='ルートにあるもの', cUp='登りのキャンプ', cDown='下りの受動態', cOff='ルート外のレッスン', cFree='レッスン無料',
    everyStop='すべての地点', mapKick='マップ', mapH2='登りは能動態、下りは受動態',
    mapHow='登りの道にロックはありません。必要なキャンプから始めてください。下りの各地点は、その元になるキャンプを終えると開きます。それまでは印が灰色です。',
    guideKick='はじめてですか？', guideLine='時制とは何か、能動態と受動態とは何か、そしてキャンプがなぜこの順に並んでいるのかを2分で説明します。',
    guideBtn='このマップの見かたは？', ascH='登り', ascSub='能動態 &middot; ベースキャンプから山頂へ',
    descH='下り', descSub='受動態 &middot; 山頂からふもとへ',
    ascAria='登り：ベースキャンプから山頂への道に、13の色つきのキャンプの印が並ぶ山。印は能動態の時制ごとに1つずつで、ほかに used to と be used to を表す2つの雲があります。すべての地点は、マップの下の一覧にも載っています。',
    descAria='下り：夜の同じ山。山頂から下へ、受動態の時制ごとにひし形の印があります。9つはレッスンで、それぞれそのキャンプを終えると開きます。4つは誰も使わない受動態なので暗いままです。月は使役です。すべての地点は、マップの下の一覧にも載っています。',
    lgColour='色つき：タップで移動', lgGrey='灰色：そのキャンプを終えると開く',
    lgShape='丸 = 能動態、ひし形 = 受動態', ascList='登り &middot; 能動態',
    zFH='ベースキャンプ', zFSub='毎日使うもの', zRH='稜線', zRSub='よく使うが、注意が必要',
    zSH='山頂アタック', zSSub='まれで、主に書き言葉の英語',
    descList='下り &middot; 受動態', descListSub='それぞれ、元のキャンプを終えると開きます',
    offH='ルート外', offSub='時制ではないが、ある時制とぶつかり合うもの',
    offUsedTo='キャンプ2か3のあと', offBeUsedTo='キャンプ2のあと', offCausative='最初の下りの地点のあと',
    free='無料', level='レベル', aboutRoute='このルートについて', whereH='現在地',
    darkH='下りの4つの地点は、わざと暗いままにしています',
    darkP='present perfect continuous、past perfect continuous、future continuous、future perfect continuous の受動態は、どれも作ることはできます（HAS BEEN BEING CLEANED、WILL BE BEING CLEANED）。しかしネイティブスピーカーはそのすべてを避け、文を言い換えます。学ぶことが何もないので、そこにはキャンプがありません。',
    teachH='授業で使いますか？',
    teachP='マップの下のスイッチで、このブラウザーでの進行状況のロックを一度にすべて外せます。教室のスクリーンに映すときや、すでに一度登ったクラスに便利です。Pro のレッスンには引き続き Pro が必要です。<a href="block-camp.html">Block Camp</a> は、ブロックでできた世界でこのうち9つの時制を登ります。',
    proP='<strong>4つのレッスンは無料で、登録も不要です：</strong>キャンプ1と2、キャンプ1が開く受動態、そして <em>used to</em>。Pro では残りの21レッスンと、サイトのほかのすべてのレッスンが開きます。',
    plans='プランと料金',
    gKick='登る前に', gTitle='このマップの見かた', gClose='ガイドを閉じる',
    g1H='時制＝時と形',
    g1P='どの時制も、動作を過去・現在・未来のどこかに置き、4つの形のどれかを与えます：<b>simple</b>（そのままの事実）、<b>continuous</b>（進行中）、<b>perfect</b>（あとの時点から振り返る：今、または過去か未来のある時点）、<b>perfect continuous</b>（その時点まで進行中）。3つの時と4つの形で、13のキャンプのうち12になります。下の形はすべて「she」+ CLIMB で、数字はそのキャンプの番号です。',
    gCaption='12の時制を時と形で並べたもの。それぞれ自分のキャンプにつながっています。',
    gGoing='残りの1つ、キャンプ5は、もう来るのが見えている未来です。',
    g2H='2つの斜面：能動態と受動態',
    gAsc='<b>登り &middot; 能動態。</b>動作をする人が先に来ます。',
    gDesc='<b>下り &middot; 受動態。</b>動作を受けるものが先に来て、動作をする人は省かれることもあります。',
    g2P='同じ時制を裏返したもの：受動態は、その時制の BE + PAST PARTICIPLE です。だから下りの各地点は登りのキャンプの双子で、そのキャンプを終えると開きます。',
    g3H='なぜこの順番か',
    g3P='キャンプは文法書の順ではなく、あなたが必要になる順に登っていきます。<b>ベースキャンプ</b>は毎日使う時制、<b>稜線</b>はよく使うが注意が必要なもの、<b>山頂アタック</b>はまれで主に書き言葉です。4つの受動態にはキャンプがありません。作ることはできます（HAS BEEN BEING CLEANED）が、誰もそうは言いません。',
    g3Map='マップでは、丸が能動態、ひし形が受動態、灰色はまだ開いていないことを表します。「no camp」と書かれた薄いひし形は、決して開きません。雲は「used to」と「be used to」、月は使役です。',
    startFree='キャンプ1から始める &middot; 無料', backMap='マップに戻る',
    carryOn='続きから：キャンプ{n} &middot; {name}', headDown='下りへ：{name}', offRoute='ルート外：{name}',
    again='もう一度登る：キャンプ1',
    lockNote='キャンプ <strong>{c}/13</strong> &middot; 下りの地点 <strong>{d}/9</strong>&mdash;&mdash;{tail}',
    tailAll='すべて開いています。', tailWhole='山全体が、両方の斜面とも開いています。',
    tailDefault='9つのキャンプがそれぞれ受動態を開きます。<em>used to</em> はキャンプ2か3のあと、<em>be used to</em> はキャンプ2のあと、使役は最初の下りの地点のあとに開きます。',
    teachOff='授業で使う：すべて開く', teachOn='ロック解除中：すべて開いています',
    teachWhy='学習者は、元になるキャンプを終えることで各受動態とルート外の3つのレッスンを開きます。先生や急いでいる人は、すべてを一度に開けます。',
    pair='キャンプ{n}（{tense}）', whyDescent='{pair}を終えると、ここが開きます。',
    whyUsedTo='キャンプ2かキャンプ3を終えてください。used to は present simple の習慣を過去に移したものです。',
    whyBeUsedTo='キャンプ2（present simple）を終えてください。be used to は出来事ではなく状態です。',
    whyCausative='下りの地点をどれか1つ終えてください。使役は帽子をかぶった受動態です。',
    srLocked='（ロック中：{why}）', srDone='（完了）', fromOpen='キャンプ{n}から', fromLocked='キャンプ{n}のあと',
    hintNoCamp='{label}：ここにはキャンプがありません。一覧の下の説明を見てください。', hintLocked='{label}：{why}',
)

# ── the check and the injection ─────────────────────────────────────────
TAGS = re.compile(r'</?(?:b|em|strong|a)\b[^>]*>')


def page_keys(src):
    return sorted(set(re.findall(r'data-t(?:-aria|-title)?="([A-Za-z0-9]+)"', src)))


def check(src):
    bad = []
    if not FENCE.search(src):
        bad.append('the /*I18N:start*/ ... /*I18N:end*/ fence is missing from the page')
    keys = set(page_keys(src)) | set(EN)
    english = {}
    for k in page_keys(src):
        m = re.search(r'<(\w+)[^>]*\bdata-t="%s"[^>]*>(.*?)</\1>' % k, src, re.S)
        if m:
            english[k] = m.group(2)
    english.update(EN)
    for lang, d in LANGS.items():
        for k in sorted(keys - set(d)):
            bad.append('%s: no %s' % (lang, k))
        for k in sorted(set(d) - keys):
            bad.append('%s: %s is not used on the page' % (lang, k))
        for k, v in d.items():
            src_en = english.get(k)
            if src_en is None:
                continue
            for ph in set(re.findall(r'\{[a-z]+\}', src_en)):
                if ph not in v:
                    bad.append('%s.%s drops %s' % (lang, k, ph))
            if sorted(t.split()[0].strip('<>/') for t in TAGS.findall(src_en)) != \
               sorted(t.split()[0].strip('<>/') for t in TAGS.findall(v)):
                bad.append('%s.%s has different tags from the English' % (lang, k))
    return bad


def inject(src):
    block = '/*I18N:start*/var EN = %s, T = %s;/*I18N:end*/' % (
        json.dumps(EN, ensure_ascii=False), json.dumps(LANGS, ensure_ascii=False))
    return FENCE.sub(lambda _: block, src, count=1)


def main():
    src = io.open(PAGE, encoding='utf-8').read()
    bad = check(src)
    for b in bad:
        print('FAIL ' + b)
    if '--check' in sys.argv:
        new = inject(src)
        stale = new != src
        print('%s: %d problem(s)%s, %d languages' % ('PASS' if not bad and not stale else 'FAIL', len(bad),
              '; the page is stale, run without --check' if stale else '', len(LANGS) + 1))
        sys.exit(1 if bad or stale else 0)
    if bad:
        sys.exit('! not injected: %d problem(s)' % len(bad))
    new = inject(src)
    if new != src:
        io.open(PAGE, 'w', encoding='utf-8', newline='\n').write(new)
    print('injected %d languages into %s' % (len(LANGS) + 1, os.path.basename(PAGE)))


if __name__ == '__main__':
    main()
