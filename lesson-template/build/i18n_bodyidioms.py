# -*- coding: utf-8 -*-
"""Interface strings for Elbow Grease (C1) — EN, DE and ES.

Part two of the body-parts pair; `i18n_bodyparts.py` is part one and its
docstring carries the reasoning both share. The scope boundary is the same:
chrome, hints, teaching card bodies, MC contexts and stems and the activation
briefs travel; the ten idioms, the eighteen verbs, their definitions, the gap
sentences, the word banks, the sort items, the MC options and the activation
chips stay in English, because they are the language under test.

The match feedback again carries the glossary in German and Spanish
(`m1Why`…`m3Why`). On this deck that is worth more than it was on part one:
*slap*, *smack*, *pat* and *shove* all come out as **schlagen** or **stoßen**
in a pocket dictionary, and the whole point of the matching round is that
English separates them. Seeing the four collapse into two German words, after
answering, is the lesson.

**The idioms are deliberately not glossed anywhere.** A German equivalent for
*keep your chin up* is *Kopf hoch* — a different body part, which is the
interesting fact, and printing it beside the English would let a learner
reverse-engineer the gap fill from their own language instead of from the
sentence. The activation slide is where that comparison belongs, out loud.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'btnCopy', 'btnCopied',
        'wordCount', 'btnOpen', 'actEyebrow']

TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'",
           'glossShow': "'Translate'",
           'ledClues': "'Clues'",
           'ledDp': "'DP'",
           'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'",
           'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'",
           'ledDp': "'DP'",
           'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'",
           'glossShow': "'Traducir'",
           'ledClues': "'Pistas'",
           'ledDp': "'DP'",
           'ledTime': "'Tiempo'"},
}

T = {}

# ── ENGLISH ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Elbow <em>Grease</em>',
    coverSub='Ten idioms the body is hiding in, and eighteen verbs for what hands actually do',
    chipLevel='C1 &middot; Idiom &amp; collocation',
    chipFocus='Fixed phrases, and the verbs of contact',
    chipCount='NSLIDES slides',

    t1Eyebrow='Why the body is in there at all',
    t1Title='Three things a body idiom will not let you do',
    t1b1='The part is fixed. <em>Keep your head up</em> exists, but it is about pride and posture &mdash; a different idea.',
    t1n1='Swap the body part and you are no longer speaking English.',
    t1b2='The meaning is not in the words: no thumb is involved, and nothing is written down.',
    t1n2='It opens a sentence: <em>As a rule of thumb, allow twenty minutes.</em>',
    t1b3='Here the spelling carries the picture: your toes up against a painted line, waiting.',
    t1n3='<em>Tow</em> is a rope. This is the commonest written error at C1.',

    s1Eyebrow='Stage one &middot; ten idioms',
    d1Title='Ten idioms, one body',
    d1Note='Chin to heel',
    gapEyebrow='Complete the idiom',
    bankLabel='Word bank:',
    g1Title='Chin, heels, stomach',
    g1Hint='One word per gap. The bank holds three you will not need.',
    g2Title='Thumb, toe, cheek',
    g2Hint='Same again. Two of these are about following the rules, one is about breaking them.',
    g3Title='Chest and lip',
    g3Hint='Two gaps. Both idioms are about saying something &mdash; or about not saying it.',
    g4Title='Eye and elbow',
    g4Hint='Two more. One of them takes a verb rather than a part of the body.',

    qEyebrow='Say it precisely',
    qTitle='Which one is the English?',
    q1Ctx='You are writing to new staff, and you want to say they are expected to follow the rules during probation.',
    q1Stem='Which one is the idiom?',
    q2Ctx='A company says all the right things about the environment and does none of them.',
    q2Stem='Which phrase says that?',
    q3Ctx='A colleague asks how long to allow per kilometre on a hill walk. You have no exact figure, only experience.',
    q3Stem='What are you giving them?',
    q4Ctx='Your friend is about to say the wrong name, and you are sitting right next to them.',
    q4Stem='What do you do?',
    q5Ctx='At the stadium gate an officer checks you quickly for anything hidden.',
    q5Stem='What are they doing?',

    t2Eyebrow='What hands do',
    t2Title='Three families, and the difference is the movement',
    t2b1='Hard, fast and usually unwelcome: a flat hand, a flat hand again, then the whole arm.',
    t2n1='<em>Smack</em> is louder than <em>slap</em>; <em>shove</em> needs no hand at all.',
    t2b2='Kind contact. The difference between them is the movement: along, down, back and forth, around.',
    t2n2='You <em>pat</em> a dog twice; you <em>stroke</em> it for a minute.',
    t2b3='No contact with the other person whatsoever &mdash; the body is signalling instead.',
    t2n3='Which is why these four survive a video call and the others do not.',

    s2Eyebrow='Stage two &middot; eighteen verbs',
    d2Title='What hands do',
    d2Note='Eighteen verbs',
    m1Title='Gentle contact',
    m1Hint='Six verbs, six purposes. Click a verb, then the reason somebody would do it.',
    m1Why='All six are welcome contact, and all six are ordinary at C1. The one to watch is '
          '<em>nudge</em>: it is as often a hint as a touch &mdash; <em>nudge someone '
          'towards a decision</em>.',
    m2Title='Hard contact',
    m2Hint='Six more. Five of them hurt; one is a search.',
    m2Why='<em>Slap</em> and <em>smack</em> are both an open hand, <em>smack</em> the '
          'louder. <em>Shove</em> is the whole arm and needs no hand. <em>Frisk</em> is '
          'police and stadium language and is not violence at all.',
    m3Title='Contact with nobody',
    m3Hint='Six signals. Not one of them touches the person it is aimed at.',
    m3Why='These are the gestures that carry meaning on their own. <em>Thumb</em> and '
          '<em>swallow</em> are the two that surprise people: <em>thumb a lift</em>, '
          '<em>thumb through a magazine</em>, <em>swallow your pride</em>.',

    sortEyebrow='All eighteen, sorted',
    sortTitle='Hurts, comforts, or signals?',
    sortHint='Twelve verbs, three intentions. Drop each one where it belongs.',
    sortBin1='Hurts',
    sortBin2='Comforts',
    sortBin3='Signals',
    sortWhy='The intention is what picks the verb in English, not the body part. That is '
            'why <em>pat</em> and <em>smack</em> are the same flat hand and are never '
            'interchangeable.',

    g5Title='The verb in the sentence',
    g5Hint='Three gaps, base form each time. The bank holds three you will not need.',

    resNext='You can recognise them. Saying one, on purpose, at the right moment, is next &rarr;',
    resPerfect='Every one. These are the phrases that make C1 sound like C1.',
    resStrong='Strong. Look at the misses &mdash; most idiom errors here are one wrong body part.',
    resMid='Halfway. Go back to the two teaching slides: the fixed part is the whole difficulty.',
    resLow='Work through the ten idioms again, one screen at a time, then run it a second time.',

    actTitle='Now use them out loud',
    actUse='Use at least four:',
    actSpeakKind='Discussion &middot; in pairs',
    actSpeakBrief='Twelve minutes, then swap. Tell the story; your partner listens for the phrases and stops you when a good one goes past unused.',
    actSpeak1='Tell your partner about a time you dug your heels in. What were you asked to do, and why did you refuse?',
    actSpeak2='Somebody on your team says all the right things and does none of them. Say that to them, without the word <em>lazy</em>.',
    actSpeak3='Name a job in your home that needs real elbow grease, and say honestly who ends up doing it.',
    actSpeak4='Mime three of the eighteen verbs. Your partner names each one and says why somebody would do it.',
    actWriteKind='Writing &middot; 150&ndash;200 words',
    actWriteBrief='Write to a friend who has had a bad month: a job that fell through and a plan that collapsed. Tell them to keep their chin up without writing that sentence. Get something off your own chest while you are there, and offer one practical thing you will actually do.',
    actPlaceholder='I heard about the interview, and honestly…',
)

# ── GERMAN ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Elbow <em>Grease</em>',
    coverSub='Zehn Redewendungen, in denen sich der Körper versteckt, und achtzehn Verben für das, was Hände wirklich tun',
    chipLevel='C1 &middot; Redewendung &amp; Kollokation',
    chipFocus='Feste Wendungen und die Verben der Berührung',
    chipCount='NSLIDES Folien',

    t1Eyebrow='Warum überhaupt der Körper',
    t1Title='Drei Dinge, die eine Körper-Redewendung nicht erlaubt',
    t1b1='Das Körperteil steht fest. <em>Keep your head up</em> gibt es, aber es meint Stolz und Haltung &mdash; eine andere Idee.',
    t1n1='Tausch das Körperteil aus, und es ist kein Englisch mehr.',
    t1b2='Die Bedeutung steckt nicht in den Wörtern: kein Daumen ist beteiligt, und nichts ist aufgeschrieben.',
    t1n2='Es eröffnet den Satz: <em>As a rule of thumb, allow twenty minutes.</em>',
    t1b3='Hier trägt die Schreibweise das Bild: die Zehen an einer aufgemalten Linie, wartend.',
    t1n3='<em>Tow</em> ist ein Seil. Das ist der häufigste Schreibfehler auf C1-Niveau.',

    s1Eyebrow='Etappe eins &middot; zehn Redewendungen',
    d1Title='Zehn Redewendungen, ein Körper',
    d1Note='Vom Kinn bis zur Ferse',
    gapEyebrow='Vervollständige die Redewendung',
    bankLabel='Wortspeicher:',
    g1Title='Chin, heels, stomach',
    g1Hint='Ein Wort pro Lücke. Der Speicher enthält drei Wörter, die du nicht brauchst.',
    g2Title='Thumb, toe, cheek',
    g2Hint='Dasselbe noch einmal. Zwei davon handeln vom Regelnbefolgen, eines vom Regelnbrechen.',
    g3Title='Chest and lip',
    g3Hint='Zwei Lücken. Beide Wendungen handeln vom Sagen &mdash; oder vom Nicht-Sagen.',
    g4Title='Eye and elbow',
    g4Hint='Zwei weitere. In eine davon gehört ein Verb statt eines Körperteils.',

    qEyebrow='Sag es genau',
    qTitle='Welches davon ist Englisch?',
    q1Ctx='Du schreibst an neue Mitarbeitende und willst sagen, dass sie sich in der Probezeit an die Regeln halten sollen.',
    q1Stem='Welches ist die Redewendung?',
    q2Ctx='Ein Unternehmen sagt alles Richtige zum Umweltschutz und tut nichts davon.',
    q2Stem='Welche Wendung sagt das?',
    q3Ctx='Ein Kollege fragt, wie viel Zeit man pro Kilometer bergauf einplanen soll. Du hast keine genaue Zahl, nur Erfahrung.',
    q3Stem='Was gibst du ihm?',
    q4Ctx='Dein Freund ist dabei, den falschen Namen zu sagen, und du sitzt direkt neben ihm.',
    q4Stem='Was tust du?',
    q5Ctx='Am Stadioneingang tastet dich ein Ordner kurz nach versteckten Gegenständen ab.',
    q5Stem='Was tut er da?',

    t2Eyebrow='Was Hände tun',
    t2Title='Drei Familien &mdash; der Unterschied ist die Bewegung',
    t2b1='Hart, schnell und meist unerwünscht: flache Hand, wieder flache Hand, dann der ganze Arm.',
    t2n1='<em>Smack</em> ist lauter als <em>slap</em>; <em>shove</em> braucht gar keine Hand.',
    t2b2='Freundliche Berührung. Der Unterschied liegt in der Bewegung: entlang, nach unten, hin und her, herum.',
    t2n2='Einen Hund <em>pat</em> man zweimal; <em>stroke</em> man eine Minute lang.',
    t2b3='Überhaupt keine Berührung der anderen Person &mdash; der Körper gibt ein Signal.',
    t2n3='Deshalb funktionieren diese vier auch in einer Videokonferenz und die anderen nicht.',

    s2Eyebrow='Etappe zwei &middot; achtzehn Verben',
    d2Title='Was Hände tun',
    d2Note='Achtzehn Verben',
    m1Title='Sanfte Berührung',
    m1Hint='Sechs Verben, sechs Absichten. Klicke ein Verb an, dann den Grund, warum man es tut.',
    m1Why='tickle = kitzeln &middot; stroke = streicheln &middot; pat = tätscheln &middot; '
          'hug = umarmen &middot; nudge = anstupsen (auch: einen Wink geben) &middot; '
          'squeeze = drücken',
    m2Title='Harte Berührung',
    m2Hint='Sechs weitere. Fünf tun weh; eines ist eine Durchsuchung.',
    m2Why='slap = ohrfeigen &middot; smack = klatschend schlagen &middot; shove = stoßen '
          '&middot; pinch = kneifen &middot; frisk = abtasten &middot; rub = reiben. Achtung: '
          'schlagen deckt im Deutschen <em>slap</em>, <em>smack</em> und mehr ab &mdash; im '
          'Englischen sind es verschiedene Verben.',
    m3Title='Berührung von niemandem',
    m3Hint='Sechs Signale. Keines berührt die Person, an die es gerichtet ist.',
    m3Why='nod = nicken &middot; wink = zwinkern &middot; clap = klatschen &middot; '
          'thumb = per Anhalter fahren / durchblättern &middot; sniff = schnüffeln, '
          'naserümpfen &middot; swallow = schlucken (auch: hinunterschlucken)',

    sortEyebrow='Alle achtzehn, sortiert',
    sortTitle='Tut weh, tröstet oder signalisiert?',
    sortHint='Zwölf Verben, drei Absichten. Ordne jedes dorthin, wo es hingehört.',
    sortBin1='Tut weh',
    sortBin2='Tröstet',
    sortBin3='Signalisiert',
    sortWhy='Im Englischen wählt die Absicht das Verb, nicht das Körperteil. Deshalb sind '
            '<em>pat</em> und <em>smack</em> dieselbe flache Hand und trotzdem nie '
            'austauschbar.',

    g5Title='Das Verb im Satz',
    g5Hint='Drei Lücken, jeweils die Grundform. Der Speicher enthält drei Wörter zu viel.',

    resNext='Erkennen kannst du sie. Eine davon bewusst im richtigen Moment zu sagen, kommt jetzt &rarr;',
    resPerfect='Alles richtig. Das sind die Wendungen, die C1 nach C1 klingen lassen.',
    resStrong='Stark. Sieh dir die Fehler an &mdash; fast immer ist es ein falsches Körperteil.',
    resMid='Halbe Strecke. Geh zu den beiden Erklärfolien zurück: das feste Körperteil ist die ganze Schwierigkeit.',
    resLow='Arbeite die zehn Redewendungen noch einmal einzeln durch und starte dann neu.',

    actTitle='Jetzt laut verwenden',
    actUse='Verwende mindestens vier:',
    actSpeakKind='Gespräch &middot; zu zweit',
    actSpeakBrief='Zwölf Minuten, dann Wechsel. Erzähl die Geschichte; dein Gegenüber hört auf die Wendungen und unterbricht, wenn eine passende ungenutzt vorbeigeht.',
    actSpeak1='Erzähl von einer Situation, in der du dich stur gestellt hast. Was solltest du tun, und warum hast du dich geweigert?',
    actSpeak2='Jemand in deinem Team sagt alles Richtige und tut nichts davon. Sag ihm das &mdash; ohne das Wort <em>lazy</em>.',
    actSpeak3='Nenne eine Arbeit bei dir zu Hause, die richtig Muskelkraft verlangt, und sag ehrlich, wer sie am Ende macht.',
    actSpeak4='Spiel drei der achtzehn Verben pantomimisch vor. Dein Gegenüber benennt jedes und sagt, warum man es tut.',
    actWriteKind='Schreiben &middot; 150&ndash;200 Wörter',
    actWriteBrief='Schreib an eine Freundin, die einen schlechten Monat hatte: eine Stelle geplatzt, ein Plan zusammengebrochen. Sag ihr, sie soll den Kopf nicht hängen lassen &mdash; ohne diesen Satz zu schreiben. Red dir selbst dabei etwas von der Seele und biete eine konkrete Sache an, die du wirklich tun wirst.',
    actPlaceholder='I heard about the interview, and honestly…',
)

# ── SPANISH ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Elbow <em>Grease</em>',
    coverSub='Diez expresiones en las que se esconde el cuerpo, y dieciocho verbos para lo que hacen las manos',
    chipLevel='C1 &middot; Modismos y colocaciones',
    chipFocus='Frases fijas y los verbos del contacto',
    chipCount='NSLIDES diapositivas',

    t1Eyebrow='Por qué aparece el cuerpo',
    t1Title='Tres cosas que un modismo corporal no te deja hacer',
    t1b1='La parte del cuerpo es fija. <em>Keep your head up</em> existe, pero habla de orgullo y de postura: otra idea.',
    t1n1='Cambia la parte del cuerpo y deja de ser inglés.',
    t1b2='El significado no está en las palabras: no hay pulgar y no hay nada escrito.',
    t1n2='Abre la frase: <em>As a rule of thumb, allow twenty minutes.</em>',
    t1b3='Aquí la ortografía sostiene la imagen: los dedos del pie junto a una línea pintada, esperando.',
    t1n3='<em>Tow</em> es una cuerda. Es el error escrito más frecuente en C1.',

    s1Eyebrow='Etapa uno &middot; diez modismos',
    d1Title='Diez modismos, un cuerpo',
    d1Note='De la barbilla al talón',
    gapEyebrow='Completa el modismo',
    bankLabel='Banco de palabras:',
    g1Title='Chin, heels, stomach',
    g1Hint='Una palabra por hueco. El banco trae tres que no vas a necesitar.',
    g2Title='Thumb, toe, cheek',
    g2Hint='Otra vez igual. Dos van de cumplir las reglas; una, de saltárselas.',
    g3Title='Chest and lip',
    g3Hint='Dos huecos. Las dos expresiones van de decir algo, o de no decirlo.',
    g4Title='Eye and elbow',
    g4Hint='Dos más. En uno de ellos va un verbo y no una parte del cuerpo.',

    qEyebrow='Dilo con precisión',
    qTitle='¿Cuál es el inglés?',
    q1Ctx='Escribes a personal nuevo y quieres decir que durante el periodo de prueba deben ceñirse a las normas.',
    q1Stem='¿Cuál es el modismo?',
    q2Ctx='Una empresa dice todo lo correcto sobre el medio ambiente y no hace nada de ello.',
    q2Stem='¿Qué frase lo dice?',
    q3Ctx='Un colega pregunta cuánto tiempo calcular por kilómetro de subida. No tienes una cifra exacta, sólo experiencia.',
    q3Stem='¿Qué le estás dando?',
    q4Ctx='Tu amigo está a punto de decir el nombre equivocado y estás sentado justo a su lado.',
    q4Stem='¿Qué haces?',
    q5Ctx='En la entrada del estadio un vigilante te cachea rápidamente por si llevas algo escondido.',
    q5Stem='¿Qué está haciendo?',

    t2Eyebrow='Lo que hacen las manos',
    t2Title='Tres familias, y la diferencia es el movimiento',
    t2b1='Duro, rápido y casi siempre no deseado: mano abierta, mano abierta otra vez, y luego el brazo entero.',
    t2n1='<em>Smack</em> suena más fuerte que <em>slap</em>; <em>shove</em> no necesita mano.',
    t2b2='Contacto amable. Lo que los separa es el movimiento: a lo largo, hacia abajo, de ida y vuelta, alrededor.',
    t2n2='A un perro se le <em>pat</em> dos veces; se le <em>stroke</em> durante un minuto.',
    t2b3='Ningún contacto con la otra persona: el cuerpo está haciendo una señal.',
    t2n3='Por eso estos cuatro sobreviven a una videollamada y los demás no.',

    s2Eyebrow='Etapa dos &middot; dieciocho verbos',
    d2Title='Lo que hacen las manos',
    d2Note='Dieciocho verbos',
    m1Title='Contacto suave',
    m1Hint='Seis verbos, seis motivos. Pulsa un verbo y luego la razón por la que alguien lo haría.',
    m1Why='tickle = hacer cosquillas &middot; stroke = acariciar &middot; pat = dar '
          'palmaditas &middot; hug = abrazar &middot; nudge = dar un codazo suave (también: '
          'insinuar) &middot; squeeze = apretar',
    m2Title='Contacto duro',
    m2Hint='Seis más. Cinco duelen; uno es un registro.',
    m2Why='slap = abofetear &middot; smack = golpear con la palma &middot; shove = empujar '
          '&middot; pinch = pellizcar &middot; frisk = cachear &middot; rub = frotar. Ojo: '
          '<em>golpear</em> cubre <em>slap</em>, <em>smack</em> y más; en inglés son verbos '
          'distintos.',
    m3Title='Contacto con nadie',
    m3Hint='Seis señales. Ninguna toca a la persona a la que va dirigida.',
    m3Why='nod = asentir &middot; wink = guiñar &middot; clap = aplaudir &middot; '
          'thumb = hacer autostop / hojear &middot; sniff = olfatear, despreciar &middot; '
          'swallow = tragar (también: tragarse el orgullo)',

    sortEyebrow='Los dieciocho, ordenados',
    sortTitle='¿Duele, consuela o señala?',
    sortHint='Doce verbos, tres intenciones. Coloca cada uno donde corresponde.',
    sortBin1='Duele',
    sortBin2='Consuela',
    sortBin3='Señala',
    sortWhy='En inglés la intención elige el verbo, no la parte del cuerpo. Por eso '
            '<em>pat</em> y <em>smack</em> son la misma mano abierta y nunca son '
            'intercambiables.',

    g5Title='El verbo en la frase',
    g5Hint='Tres huecos, siempre en forma base. El banco trae tres que sobran.',

    resNext='Reconocerlas ya sabes. Decir una, a propósito, en el momento justo, viene ahora &rarr;',
    resPerfect='Todas. Estas son las frases que hacen que C1 suene a C1.',
    resStrong='Muy bien. Mira los fallos: casi todos son una parte del cuerpo equivocada.',
    resMid='A mitad de camino. Vuelve a las dos diapositivas de explicación: la parte fija es toda la dificultad.',
    resLow='Repasa los diez modismos uno a uno y hazlo otra vez.',

    actTitle='Ahora úsalas en voz alta',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Conversación &middot; en parejas',
    actSpeakBrief='Doce minutos y se cambia. Cuenta la historia; tu pareja escucha las frases y te para cuando dejas pasar una que encajaba.',
    actSpeak1='Cuenta una vez en que te plantaste y no cediste. ¿Qué te pedían y por qué te negaste?',
    actSpeak2='Alguien de tu equipo dice todo lo correcto y no hace nada. Díselo, sin usar la palabra <em>lazy</em>.',
    actSpeak3='Nombra una tarea de tu casa que exige esfuerzo de verdad y di honestamente quién acaba haciéndola.',
    actSpeak4='Representa con mímica tres de los dieciocho verbos. Tu pareja nombra cada uno y dice por qué alguien lo haría.',
    actWriteKind='Escritura &middot; 150&ndash;200 palabras',
    actWriteBrief='Escribe a un amigo que ha tenido un mal mes: un trabajo que se cayó y un plan que se vino abajo. Dile que no se desanime sin escribir esa frase. Desahógate tú también un poco y ofrécele una cosa concreta que vayas a hacer de verdad.',
    actPlaceholder='I heard about the interview, and honestly…',
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
