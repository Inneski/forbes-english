# -*- coding: utf-8 -*-
"""Interface strings for Lego Car Building (B2), Part II.

English, German and Spanish. Teach-card bodies use the six-item form. The
English being taught — the structures, the sentences, the options — stays
English.
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
    coverTitle='Lego Car Building <em>Part II</em>',
    coverSub='The prepositions verbs insist on, and four ways to say the same thing better',
    chipLevel='B2 · Upper-intermediate', chipFocus='Collocation &amp; sentence transformation',
    chipCount='15 slides',

    coEyebrow='Before the questions', coTitle='The verb chooses the preposition',
    co1h='Fixed, and not negotiable', co1b=
        'A mechanism <strong>consists of</strong> parts &mdash; never <em>from</em>, '
        'never <em>in</em>. A fit <strong>depends on</strong> tolerance, never '
        '<em>from</em>. There is no rule underneath these; the verb simply takes one '
        'preposition.',
    co1n='<em>Consist from</em> and <em>depend from</em> are the two commonest carry-overs from Romance languages.',
    co2h='Two verbs that look alike', co2b=
        'You <strong>replace</strong> one part <em>with</em> another, but you '
        '<strong>substitute</strong> a new part <em>for</em> the old one. The order '
        'reverses, and getting it wrong reverses the sentence.',
    co2n='<em>Substituted the wheels for smaller ones</em> means the smaller ones went on.',
    co3h='Phrases that are learned whole', co3b=
        'Components go on <strong>in sequence</strong>, work is done <strong>in '
        'order</strong>, a part is <strong>in place</strong>. No article, no plural, and '
        'no logic to appeal to.',
    co3n='These are the ones that make writing sound native or not, and they are pure memory.',

    grEyebrow='The two slips', grTitle='One letter, and one word class',
    gr1h='<em>To</em> and <em>too</em>', gr1b=
        '<strong>Too</strong> with two <em>o</em>s means excessively: <em>too rigid to '
        'absorb the impact</em>. <strong>To</strong> with one is the infinitive marker '
        'or a preposition. The sentence usually needs both, one after the other.',
    gr1n='<em>Too X to Y</em>: the first is the degree, the second belongs to the verb.',
    gr2h='Adjectives and adverbs', gr2b=
        'An adjective describes a thing: <em>an <strong>inefficient</strong> '
        'mechanism</em>. An adverb describes an action: <em>it turned '
        '<strong>inefficiently</strong></em>. Ask what the word is attached to.',
    gr2n='If it sits next to a verb, it needs the <em>-ly</em>. Almost always.',
    gr3h='Where errors hide', gr3b=
        'Both of these survive a read-through because the sentence still makes sense. '
        'Proofreading for meaning will not find them; you have to look at what each '
        'word is doing.',
    gr3n='This is why error correction is a separate skill from writing.',

    trEyebrow='Saying it again, better', trTitle='Four structures worth having',
    tr1h='<em>Too&hellip; to&hellip;</em>', tr1b=
        '<em>So stiff that it was impossible to turn</em> becomes <em><strong>too</strong> '
        'stiff <strong>to</strong> turn</em>. Nine words become four and nothing is lost. '
        'The negative is built in &mdash; do not add another.',
    tr1n='<em>Too stiff to not turn</em> is the error this structure invites.',
    tr2h='<em>Only to&hellip;</em>', tr2b=
        '<em>He worked for three hours <strong>only to</strong> discover a mistake.</em> '
        'It marks an outcome that undoes the effort. Not just "and then" &mdash; it '
        'carries the disappointment.',
    tr2n='Effort first, reversal second. The order is part of the meaning.',
    tr3h='<em>Despite</em> and <em>must</em>', tr3b=
        '<strong>Despite</strong> takes a noun phrase, not a clause: <em>despite its '
        'fragile appearance</em>, not <em>despite it looked</em>. And <em>it is '
        'essential that you read</em> becomes <em>you <strong>must</strong> read</em>.',
    tr3n='<em>Despite of</em> does not exist. <em>In spite of</em> does.',

    mcEyebrow='Activity 1 · Transformation', mcTitle='Same meaning, new structure',
    q1why='<strong>The build could not be completed without a pair of tweezers for the '
          'smallest parts.</strong> The passive keeps the condition exactly as it was. '
          'The others change what was impossible, or when.',
    q2why='<strong>He spent three hours assembling the engine block, only to discover '
          'that he had made a mistake.</strong> <em>Only to</em> needs the effort first '
          'and the reversal second. Move it and the disappointment goes.',
    q3why='<strong>The steering mechanism was too stiff to turn smoothly.</strong> '
          '<em>Too + adjective + to + verb</em> already means "so much that it was '
          'impossible". The adjective has to be the original one: stiff, not difficult.',
    q4why='<strong>Despite its fragile appearance, the model proved to be extremely '
          'durable.</strong> <em>Despite</em> takes a noun phrase, and the contrast has '
          'to survive: it looked fragile, it was not.',
    q5why='<strong>All builders must read the instructions carefully before '
          'starting.</strong> <em>It is essential that + base verb</em> maps straight '
          'onto <em>must + base verb</em>. No perfect, no continuous, and the timing '
          'stays.',

    errEyebrow='Activity 2 · Error correction', errTitle='Two wrong words in each sentence',
    errHint='Type the correction only. Each sentence has exactly two.',
    e1why='<strong>From</strong> and <strong>in</strong>. You start <em>from</em> the '
          'chassis and work upwards, and components go on <em>in sequence</em> &mdash; a '
          'fixed phrase with no article.',
    e2why='<strong>Incompatible</strong> and <strong>on</strong>. The axle is '
          '<em>incompatible with</em> the design, and an assembly <em>depends on</em> a '
          'fit. <em>Depends from</em> is a Romance carry-over.',
    e3why='<strong>Of</strong> and <strong>transmitting</strong>. <em>Consist</em> always '
          'takes <em>of</em>, and each cog is doing the transmitting, so the participle '
          'is what modifies it.',
    e4why='<strong>Precisely</strong> and <strong>inefficiently</strong>. Both attach to '
          'verbs &mdash; following, and turning &mdash; so both need the adverb.',
    e5why='<strong>Realising</strong> and <strong>too</strong>. <em>After</em> takes an '
          '<em>-ing</em> form, and <em>too rigid to absorb</em> is the degree structure, '
          'so it is <em>too</em> with two <em>o</em>s.',

    matchEyebrow='Activity 3 · The technical terms', matchTitle='Match the term to its definition',
    matchHint='Click a term, then click what it means.',
    matchWhy='All five are real mechanical engineering and all five are used unchanged '
             'about Lego Technic. <em>Torque</em> and <em>gear ratio</em> are two ends of '
             'the same trade &mdash; gear down and you swap speed for turning force. '
             '<em>Camber</em>, <em>suspension</em> and <em>load capacity</em> are about '
             'keeping contact with the ground and not buckling while you do it.',

    actTitle='Report the fault', actUse='Use at least four:',
    actSpeakBrief='One of you built it and one of you is testing it, and it does not '
                  'work. Four minutes each, then swap.',
    actSpeak1='Describe a mechanism that failed, and say what it depends on that was not there.',
    actSpeak2='Explain something that took far longer than it should have — and use <em>only to</em>.',
    actSpeak3='Concede a fault and defend the design anyway. Start with <em>despite</em>.',
    actSpeak4='Give three instructions a builder must follow, and say why each one matters.',
    actWriteKind='Writing · 150–180 words',
    actWriteBrief='Write the fault report an engineer would file after testing a '
                  'prototype. Say what the mechanism consists of, what the failure '
                  'depended on, what was too weak to hold, and what must change before '
                  'the next build. Keep it factual and keep the collocations right.',
    actPlaceholder='The drive assembly consists of…',

    resPerfect='Full marks. The collocations are the hard part and you have them.',
    resStrong='Strong. Look at the error correction again — the adverb is where the last mark usually goes.',
    resMid='Good base. Go back to the first slide: <em>consist of</em>, <em>depend on</em>, <em>substitute for</em>.',
    resLow='Read the three opening slides again. Prepositions are memory, not logic — and the transformations are four patterns.',
)

T['de'] = dict(
    coverTitle='Lego-Autobau <em>Teil II</em>',
    coverSub='Die Präpositionen, auf denen Verben bestehen — und vier Wege, dasselbe besser zu sagen',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Kollokation und Satzumformung',
    chipCount='15 Folien',

    coEyebrow='Vor den Fragen', coTitle='Das Verb wählt die Präposition',
    co1h='Fest und nicht verhandelbar', co1b=
        'Ein Mechanismus <strong>consists of</strong> Teilen &mdash; nie <em>from</em>, '
        'nie <em>in</em>. Eine Passung <strong>depends on</strong> der Toleranz, nie '
        '<em>from</em>. Darunter liegt keine Regel; das Verb nimmt schlicht eine '
        'Präposition.',
    co1n='<em>Consist from</em> und <em>depend from</em> sind die zwei häufigsten Übertragungen aus romanischen Sprachen.',
    co2h='Zwei Verben, die sich ähneln', co2b=
        'Du <strong>replace</strong>st ein Teil <em>with</em> einem anderen, aber du '
        '<strong>substitute</strong>st ein neues Teil <em>for</em> das alte. Die '
        'Reihenfolge kehrt sich um, und ein Fehler dreht den Satz.',
    co2n='<em>Substituted the wheels for smaller ones</em> heißt: die kleineren kamen dran.',
    co3h='Wendungen, die man ganz lernt', co3b=
        'Bauteile kommen <strong>in sequence</strong> dran, gearbeitet wird <strong>in '
        'order</strong>, ein Teil ist <strong>in place</strong>. Kein Artikel, kein '
        'Plural und keine Logik, auf die man sich berufen könnte.',
    co3n='Genau daran hört man, ob es muttersprachlich klingt — und es ist reines Gedächtnis.',

    grEyebrow='Die zwei Ausrutscher', grTitle='Ein Buchstabe und eine Wortart',
    gr1h='<em>To</em> und <em>too</em>', gr1b=
        '<strong>Too</strong> mit zwei <em>o</em> heißt „zu sehr“: <em>too rigid to '
        'absorb the impact</em>. <strong>To</strong> mit einem ist Infinitivmarker oder '
        'Präposition. Meist braucht der Satz beide, direkt hintereinander.',
    gr1n='<em>Too X to Y</em>: das erste ist der Grad, das zweite gehört zum Verb.',
    gr2h='Adjektive und Adverbien', gr2b=
        'Ein Adjektiv beschreibt eine Sache: <em>an <strong>inefficient</strong> '
        'mechanism</em>. Ein Adverb beschreibt eine Handlung: <em>it turned '
        '<strong>inefficiently</strong></em>. Frag, woran das Wort hängt.',
    gr2n='Steht es neben einem Verb, braucht es das <em>-ly</em>. Fast immer.',
    gr3h='Wo sich Fehler verstecken', gr3b=
        'Beide überleben das Durchlesen, weil der Satz weiterhin Sinn ergibt. Auf Sinn '
        'zu korrigieren findet sie nicht; man muss ansehen, was jedes Wort tut.',
    gr3n='Darum ist Fehlerkorrektur eine eigene Fertigkeit, getrennt vom Schreiben.',

    trEyebrow='Dasselbe, nur besser', trTitle='Vier Strukturen, die sich lohnen',
    tr1h='<em>Too&hellip; to&hellip;</em>', tr1b=
        'Aus <em>so stiff that it was impossible to turn</em> wird <em><strong>too</strong> '
        'stiff <strong>to</strong> turn</em>. Neun Wörter werden vier, ohne Verlust. Die '
        'Verneinung steckt drin — setz keine zweite dazu.',
    tr1n='<em>Too stiff to not turn</em> ist der Fehler, zu dem diese Struktur verleitet.',
    tr2h='<em>Only to&hellip;</em>', tr2b=
        '<em>He worked for three hours <strong>only to</strong> discover a mistake.</em> '
        'Es markiert ein Ergebnis, das die Mühe zunichtemacht. Nicht bloß „und dann“ — es '
        'trägt die Enttäuschung.',
    tr2n='Erst die Mühe, dann die Kehrtwende. Die Reihenfolge gehört zur Bedeutung.',
    tr3h='<em>Despite</em> und <em>must</em>', tr3b=
        '<strong>Despite</strong> nimmt eine Nominalphrase, keinen Nebensatz: <em>despite '
        'its fragile appearance</em>, nicht <em>despite it looked</em>. Und aus <em>it is '
        'essential that you read</em> wird <em>you <strong>must</strong> read</em>.',
    tr3n='<em>Despite of</em> gibt es nicht. <em>In spite of</em> schon.',

    mcEyebrow='Aufgabe 1 · Umformung', mcTitle='Gleiche Bedeutung, neue Struktur',
    q1why='<strong>The build could not be completed without a pair of tweezers for the '
          'smallest parts.</strong> Das Passiv hält die Bedingung genau so, wie sie war. '
          'Die anderen ändern, was unmöglich war, oder wann.',
    q2why='<strong>He spent three hours assembling the engine block, only to discover that '
          'he had made a mistake.</strong> <em>Only to</em> braucht erst die Mühe, dann '
          'die Kehrtwende. Verschiebt man das, ist die Enttäuschung weg.',
    q3why='<strong>The steering mechanism was too stiff to turn smoothly.</strong> <em>Too '
          '+ Adjektiv + to + Verb</em> heißt schon „so sehr, dass es unmöglich war“. Das '
          'Adjektiv muss das ursprüngliche sein: stiff, nicht difficult.',
    q4why='<strong>Despite its fragile appearance, the model proved to be extremely '
          'durable.</strong> <em>Despite</em> nimmt eine Nominalphrase, und der Kontrast '
          'muss erhalten bleiben: es sah zerbrechlich aus, war es aber nicht.',
    q5why='<strong>All builders must read the instructions carefully before starting.</strong> '
          '<em>It is essential that + Grundform</em> geht direkt in <em>must + '
          'Grundform</em> über. Kein Perfekt, keine Verlaufsform, gleiche Zeitlage.',

    errEyebrow='Aufgabe 2 · Fehlerkorrektur', errTitle='Zwei falsche Wörter pro Satz',
    errHint='Tippe nur die Korrektur. Jeder Satz hat genau zwei.',
    e1why='<strong>From</strong> und <strong>in</strong>. Man beginnt <em>from</em> dem '
          'Chassis und arbeitet sich hoch, und Bauteile kommen <em>in sequence</em> dran — '
          'eine feste Wendung ohne Artikel.',
    e2why='<strong>Incompatible</strong> und <strong>on</strong>. Die Achse ist '
          '<em>incompatible with</em> dem Entwurf, und eine Baugruppe <em>depends on</em> '
          'einer Passung. <em>Depends from</em> ist eine romanische Übertragung.',
    e3why='<strong>Of</strong> und <strong>transmitting</strong>. <em>Consist</em> nimmt '
          'immer <em>of</em>, und jedes Zahnrad überträgt selbst — also das Partizip.',
    e4why='<strong>Precisely</strong> und <strong>inefficiently</strong>. Beide hängen an '
          'Verben — folgen und drehen —, also beide als Adverb.',
    e5why='<strong>Realising</strong> und <strong>too</strong>. <em>After</em> nimmt eine '
          '<em>-ing</em>-Form, und <em>too rigid to absorb</em> ist die Gradstruktur, also '
          '<em>too</em> mit zwei <em>o</em>.',

    matchEyebrow='Aufgabe 3 · Die Fachbegriffe', matchTitle='Ordne dem Begriff seine Definition zu',
    matchHint='Klicke einen Begriff an, dann seine Bedeutung.',
    matchWhy='Alle fünf sind echter Maschinenbau und alle fünf werden unverändert über '
             'Lego Technic gesagt. <em>Torque</em> und <em>gear ratio</em> sind zwei Enden '
             'desselben Tauschs — untersetzen heißt Geschwindigkeit gegen Drehmoment '
             'tauschen. <em>Camber</em>, <em>suspension</em> und <em>load capacity</em> '
             'gehen darum, den Bodenkontakt zu halten und dabei nicht einzuknicken.',

    actTitle='Melde den Fehler', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer hat es gebaut, die andere testet es, und es funktioniert nicht. '
                  'Je vier Minuten, dann tauschen.',
    actSpeak1='Beschreibe einen Mechanismus, der versagt hat, und sag, worauf er angewiesen war und was fehlte.',
    actSpeak2='Erzähl von etwas, das viel länger gedauert hat als nötig — und benutze <em>only to</em>.',
    actSpeak3='Räum einen Fehler ein und verteidige den Entwurf trotzdem. Fang mit <em>despite</em> an.',
    actSpeak4='Nenne drei Anweisungen, die ein Bauender befolgen muss, und sag, warum jede zählt.',
    actWriteKind='Schreiben · 150–180 Wörter',
    actWriteBrief='Schreibe den Fehlerbericht, den eine Ingenieurin nach dem Test eines '
                  'Prototyps einreichen würde. Sag, woraus der Mechanismus besteht, wovon '
                  'der Ausfall abhing, was zu schwach zum Halten war und was sich vor dem '
                  'nächsten Bau ändern muss. Sachlich, und mit den richtigen Kollokationen.',
    actPlaceholder='The drive assembly consists of…',

    resPerfect='Volle Punktzahl. Die Kollokationen sind der schwere Teil, und du hast sie.',
    resStrong='Stark. Sieh dir die Fehlerkorrektur noch einmal an — beim Adverb geht meist der letzte Punkt verloren.',
    resMid='Gute Grundlage. Zurück zur ersten Folie: <em>consist of</em>, <em>depend on</em>, <em>substitute for</em>.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Präpositionen sind Gedächtnis, nicht Logik — und die Umformungen sind vier Muster.',
)

T['es'] = dict(
    coverTitle='Construir coches de Lego <em>Parte II</em>',
    coverSub='Las preposiciones que los verbos exigen y cuatro maneras de decir lo mismo mejor',
    chipLevel='B2 · Intermedio alto', chipFocus='Colocación y transformación de frases',
    chipCount='15 diapositivas',

    coEyebrow='Antes de las preguntas', coTitle='El verbo elige la preposición',
    co1h='Fijas y no negociables', co1b=
        'Un mecanismo <strong>consists of</strong> piezas: nunca <em>from</em>, nunca '
        '<em>in</em>. Un ajuste <strong>depends on</strong> la tolerancia, nunca '
        '<em>from</em>. Debajo no hay ninguna regla; el verbo simplemente pide una '
        'preposición.',
    co1n='<em>Consist from</em> y <em>depend from</em> son los dos calcos más comunes de las lenguas románicas.',
    co2h='Dos verbos que se parecen', co2b=
        '<strong>Replace</strong> una pieza <em>with</em> otra, pero '
        '<strong>substitute</strong> una nueva <em>for</em> la vieja. El orden se '
        'invierte, y equivocarse le da la vuelta a la frase.',
    co2n='<em>Substituted the wheels for smaller ones</em> significa que se montaron las pequeñas.',
    co3h='Frases que se aprenden enteras', co3b=
        'Los componentes van <strong>in sequence</strong>, el trabajo se hace <strong>in '
        'order</strong>, una pieza está <strong>in place</strong>. Sin artículo, sin '
        'plural y sin lógica a la que recurrir.',
    co3n='Justo esto es lo que hace que un texto suene nativo o no, y es pura memoria.',

    grEyebrow='Los dos resbalones', grTitle='Una letra y una categoría',
    gr1h='<em>To</em> y <em>too</em>', gr1b=
        '<strong>Too</strong> con dos <em>o</em> significa «demasiado»: <em>too rigid to '
        'absorb the impact</em>. <strong>To</strong> con una es marca de infinitivo o '
        'preposición. La frase suele necesitar las dos, seguidas.',
    gr1n='<em>Too X to Y</em>: la primera es el grado, la segunda pertenece al verbo.',
    gr2h='Adjetivos y adverbios', gr2b=
        'Un adjetivo describe una cosa: <em>an <strong>inefficient</strong> mechanism</em>. '
        'Un adverbio describe una acción: <em>it turned <strong>inefficiently</strong></em>. '
        'Pregunta a qué está pegada la palabra.',
    gr2n='Si va junto a un verbo, necesita el <em>-ly</em>. Casi siempre.',
    gr3h='Dónde se esconden los errores', gr3b=
        'Los dos sobreviven a una relectura porque la frase sigue teniendo sentido. '
        'Corregir buscando sentido no los encuentra; hay que mirar qué hace cada palabra.',
    gr3n='Por eso corregir errores es una destreza aparte de escribir.',

    trEyebrow='Decirlo otra vez, mejor', trTitle='Cuatro estructuras que merecen la pena',
    tr1h='<em>Too&hellip; to&hellip;</em>', tr1b=
        '<em>So stiff that it was impossible to turn</em> pasa a ser <em><strong>too</strong> '
        'stiff <strong>to</strong> turn</em>. Nueve palabras se vuelven cuatro sin perder '
        'nada. La negación va dentro: no añadas otra.',
    tr1n='<em>Too stiff to not turn</em> es el error al que invita esta estructura.',
    tr2h='<em>Only to&hellip;</em>', tr2b=
        '<em>He worked for three hours <strong>only to</strong> discover a mistake.</em> '
        'Marca un resultado que anula el esfuerzo. No es solo «y luego»: lleva la '
        'decepción dentro.',
    tr2n='Primero el esfuerzo, después el revés. El orden forma parte del significado.',
    tr3h='<em>Despite</em> y <em>must</em>', tr3b=
        '<strong>Despite</strong> lleva sintagma nominal, no oración: <em>despite its '
        'fragile appearance</em>, no <em>despite it looked</em>. Y <em>it is essential '
        'that you read</em> pasa a <em>you <strong>must</strong> read</em>.',
    tr3n='<em>Despite of</em> no existe. <em>In spite of</em> sí.',

    mcEyebrow='Actividad 1 · Transformación', mcTitle='Mismo significado, otra estructura',
    q1why='<strong>The build could not be completed without a pair of tweezers for the '
          'smallest parts.</strong> La pasiva conserva la condición tal cual. Las demás '
          'cambian qué era imposible, o cuándo.',
    q2why='<strong>He spent three hours assembling the engine block, only to discover that '
          'he had made a mistake.</strong> <em>Only to</em> necesita primero el esfuerzo y '
          'después el revés. Si se mueve, se va la decepción.',
    q3why='<strong>The steering mechanism was too stiff to turn smoothly.</strong> <em>Too '
          '+ adjetivo + to + verbo</em> ya significa «tanto que era imposible». El adjetivo '
          'tiene que ser el original: stiff, no difficult.',
    q4why='<strong>Despite its fragile appearance, the model proved to be extremely '
          'durable.</strong> <em>Despite</em> lleva sintagma nominal, y el contraste debe '
          'sobrevivir: parecía frágil y no lo era.',
    q5why='<strong>All builders must read the instructions carefully before starting.</strong> '
          '<em>It is essential that + forma base</em> se traduce directamente en <em>must + '
          'forma base</em>. Ni perfecto, ni continuo, y el momento no cambia.',

    errEyebrow='Actividad 2 · Corrección de errores', errTitle='Dos palabras mal en cada frase',
    errHint='Escribe solo la corrección. Cada frase tiene exactamente dos.',
    e1why='<strong>From</strong> e <strong>in</strong>. Se empieza <em>from</em> el chasis '
          'y se sube, y los componentes se montan <em>in sequence</em>, una expresión fija '
          'sin artículo.',
    e2why='<strong>Incompatible</strong> y <strong>on</strong>. El eje es <em>incompatible '
          'with</em> el diseño, y un conjunto <em>depends on</em> un ajuste. <em>Depends '
          'from</em> es un calco románico.',
    e3why='<strong>Of</strong> y <strong>transmitting</strong>. <em>Consist</em> siempre '
          'lleva <em>of</em>, y cada engranaje es el que transmite, así que el participio '
          'es lo que lo modifica.',
    e4why='<strong>Precisely</strong> e <strong>inefficiently</strong>. Los dos se pegan a '
          'verbos — seguir y girar —, así que los dos piden adverbio.',
    e5why='<strong>Realising</strong> y <strong>too</strong>. <em>After</em> pide una forma '
          'en <em>-ing</em>, y <em>too rigid to absorb</em> es la estructura de grado, así '
          'que es <em>too</em> con dos <em>o</em>.',

    matchEyebrow='Actividad 3 · Los términos técnicos', matchTitle='Relaciona el término con su definición',
    matchHint='Haz clic en un término y luego en lo que significa.',
    matchWhy='Los cinco son ingeniería mecánica real y los cinco se usan igual hablando de '
             'Lego Technic. <em>Torque</em> y <em>gear ratio</em> son los dos extremos del '
             'mismo intercambio: desmultiplicar es cambiar velocidad por fuerza de giro. '
             '<em>Camber</em>, <em>suspension</em> y <em>load capacity</em> van de mantener '
             'el contacto con el suelo sin ceder por el camino.',

    actTitle='Informa del fallo', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno lo construyó y el otro lo está probando, y no funciona. Cuatro '
                  'minutos cada uno, luego cambiad.',
    actSpeak1='Describe un mecanismo que falló y di de qué dependía que no estaba ahí.',
    actSpeak2='Cuenta algo que tardó mucho más de lo debido, y usa <em>only to</em>.',
    actSpeak3='Admite un fallo y defiende el diseño igualmente. Empieza con <em>despite</em>.',
    actSpeak4='Da tres instrucciones que un constructor debe seguir y di por qué importa cada una.',
    actWriteKind='Escritura · 150–180 palabras',
    actWriteBrief='Escribe el informe de fallo que presentaría un ingeniero tras probar un '
                  'prototipo. Di de qué consta el mecanismo, de qué dependía el fallo, qué '
                  'era demasiado débil para aguantar y qué debe cambiar antes de la '
                  'siguiente construcción. Con datos y con las colocaciones correctas.',
    actPlaceholder='The drive assembly consists of…',

    resPerfect='Puntuación perfecta. Las colocaciones son lo difícil y las tienes.',
    resStrong='Muy bien. Repasa la corrección de errores: en el adverbio suele irse el último punto.',
    resMid='Buena base. Vuelve a la primera diapositiva: <em>consist of</em>, <em>depend on</em>, <em>substitute for</em>.',
    resLow='Relee las tres diapositivas iniciales. Las preposiciones son memoria, no lógica, y las transformaciones son cuatro patrones.',
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
