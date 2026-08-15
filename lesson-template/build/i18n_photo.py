# -*- coding: utf-8 -*-
"""Interface strings for Advanced Photography (B2), English and German."""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Advanced <em>Photography</em>',
    coverSub='The exposure triangle, the lens, and the words for what light is doing',
    chipLevel='B2 · Upper-intermediate', chipFocus='Photography', chipCount='16 slides',
    expEyebrow='Before the questions · 1 of 3',
    expTitle='The exposure triangle — three ways to the same brightness',
    e1h='Aperture — f/1.8 to f/22',
    e1b='Also sets <strong>depth of field</strong>: wide open, only the eyes are sharp; stopped down, the whole street is.',
    e2h='Shutter — 1/1000s to 30s',
    e2b='Also decides <strong>motion</strong>: fast freezes the athlete, slow turns them into a streak. This is the creative choice, not just the exposure one.',
    e3h='ISO — 100 to 25,600',
    e3b='Costs you <strong>noise</strong>. ISO is what you spend when aperture and shutter are already committed — a payment, not a free gain.',
    lensEyebrow='Before the questions · 2 of 3',
    lensTitle='The lens, and the four faults it is known by',
    l1h='prime vs zoom',
    l1b='In exchange it opens wider than a zoom at the same price — which is the whole reason people carry them.',
    l2h='bokeh',
    l2b='Not how much blur, but what kind. Smooth round highlights are prized; busy, edged ones are not.',
    l3h='chromatic aberration',
    l3b='Coloured fringing — purple or green — on high-contrast edges. Branches against a bright sky show it first.',
    l4h='vignetting',
    l4b='A fault when the lens does it, a technique when you do: it holds the eye in the middle of the frame.',
    compEyebrow='Before the questions · 3 of 3',
    compTitle='Reading the light, and arranging the frame',
    c1h='Metering &amp; the histogram',
    c1b='Black on the left, white on the right. Data piled against either edge is <em>clipped</em> — that detail no longer exists.',
    c2h='Bracketing',
    c2b='Insurance against light you cannot meter — and the raw material of HDR.',
    c3h='Composition',
    c3b='The thirds grid gives four intersections. Dead centre is static; slightly off is what makes a frame move.',
    qEyebrow='Through the lens', qTitle='Choose the precise term',
    gapEyebrow='The exact word', gapTitle='Develop your vocabulary',
    gapHint='Two of the eight words in the bank belong to no gap here.',
    bankLabel='Word bank:',
    matchEyebrow='Term and definition', matchTitle='Five you will meet in any camera menu',
    matchHint='Click a term, then click its definition.',
    ordEyebrow='The commission', ordTitle='Put the professional workflow in order',
    ordHint='Click the stages in the order they happen.',
    actTitle='Talk about a photograph', actUse='Use at least four:',
    actWriteKind='Writing · 150–200 words',
    actSpeakBrief='Bring one photograph each — yours, or one you admire. Describe it technically.',
    actSpeak1='Guess the settings from the picture: wide or narrow aperture? Fast or slow shutter? How can you tell?',
    actSpeak2='Where is the subject in the frame, and what would change if it were dead centre?',
    actSpeak3='Your partner has taken a picture that is too dark. Diagnose it in three questions.',
    actSpeak4='Argue for one of these: a prime lens, or a zoom. Use <em>depth of field</em> at least once.',
    actWriteBrief='Write the brief for a shoot you would like to do: what it is for, who sees it, and what the light needs to be doing.',
    actPlaceholder='The brief: a series of six portraits, shot in available light,',
    resPerfect='Full marks. You can name what a lens is doing and what it is doing wrong.',
    resStrong='Strong. The triangle is secure — the lens faults are what reward another pass.',
    resMid='A good base. Go back to the three opening slides; the vocabulary only sticks once the mechanism does.',
    resLow='Read the three teaching slides again, then run it once more. Aperture, shutter, ISO — everything else hangs off those.',
)

T['de'] = dict(
    coverTitle='<em>Fotografie</em> für Fortgeschrittene',
    coverSub='Das Belichtungsdreieck, das Objektiv und die Wörter dafür, was das Licht gerade tut',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Fotografie', chipCount='16 Folien',
    expEyebrow='Vor den Aufgaben · 1 von 3',
    expTitle='Das Belichtungsdreieck — drei Wege zur selben Helligkeit',
    e1h='Blende — f/1.8 bis f/22',
    e1b='Bestimmt auch die <strong>Schärfentiefe</strong>: weit offen ist nur das Auge scharf, abgeblendet die ganze Straße.',
    e2h='Verschluss — 1/1000s bis 30s',
    e2b='Bestimmt auch die <strong>Bewegung</strong>: kurz friert die Läuferin ein, lang macht einen Strich aus ihr. Das ist die gestalterische Entscheidung, nicht nur die belichtungstechnische.',
    e3h='ISO — 100 bis 25.600',
    e3b='Kostet <strong>Rauschen</strong>. ISO ist das, was man ausgibt, wenn Blende und Verschluss schon festgelegt sind — eine Zahlung, kein Geschenk.',
    lensEyebrow='Vor den Aufgaben · 2 von 3',
    lensTitle='Das Objektiv und die vier Fehler, an denen man es erkennt',
    l1h='Festbrennweite vs. Zoom',
    l1b='Dafür öffnet sie weiter als ein Zoom derselben Preisklasse — genau deshalb schleppt man sie mit.',
    l2h='bokeh',
    l2b='Nicht wie viel Unschärfe, sondern welche Art. Weiche runde Lichter sind begehrt, unruhige mit harten Rändern nicht.',
    l3h='chromatische Aberration',
    l3b='Farbsäume — violett oder grün — an kontrastreichen Kanten. Zweige vor hellem Himmel zeigen es zuerst.',
    l4h='Vignettierung',
    l4b='Ein Fehler, wenn das Objektiv es tut, eine Technik, wenn Sie es tun: Sie hält den Blick in der Bildmitte.',
    compEyebrow='Vor den Aufgaben · 3 von 3',
    compTitle='Das Licht lesen und das Bild ordnen',
    c1h='Messung &amp; Histogramm',
    c1b='Schwarz links, Weiß rechts. Was sich an einem Rand staut, ist <em>beschnitten</em> — diese Zeichnung existiert nicht mehr.',
    c2h='Belichtungsreihe',
    c2b='Eine Versicherung gegen Licht, das man nicht zuverlässig messen kann — und das Rohmaterial für HDR.',
    c3h='Bildaufbau',
    c3b='Das Drittelraster ergibt vier Schnittpunkte. Genau mittig wirkt statisch; leicht daneben bringt das Bild in Bewegung.',
    qEyebrow='Durch das Objektiv', qTitle='Wählen Sie den genauen Begriff',
    gapEyebrow='Das genaue Wort', gapTitle='Wortschatz entwickeln',
    gapHint='Zwei der acht Wörter in der Liste gehören in keine dieser Lücken.',
    bankLabel='Wortliste:',
    matchEyebrow='Begriff und Definition', matchTitle='Fünf, die in jedem Kameramenü stehen',
    matchHint='Klicken Sie auf einen Begriff und dann auf seine Definition.',
    ordEyebrow='Der Auftrag', ordTitle='Bringen Sie den Arbeitsablauf in die richtige Reihenfolge',
    ordHint='Klicken Sie die Phasen in der Reihenfolge an, in der sie stattfinden.',
    actTitle='Über ein Foto sprechen', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 150–200 Wörter',
    actSpeakBrief='Bringen Sie je ein Foto mit — ein eigenes oder eines, das Sie bewundern. Beschreiben Sie es technisch.',
    actSpeak1='Raten Sie die Einstellungen aus dem Bild: offene oder geschlossene Blende? Kurze oder lange Zeit? Woran erkennt man es?',
    actSpeak2='Wo sitzt das Motiv im Bild, und was änderte sich, wenn es genau mittig säße?',
    actSpeak3='Ihr Gegenüber hat ein zu dunkles Bild gemacht. Diagnostizieren Sie es in drei Fragen.',
    actSpeak4='Argumentieren Sie für eines von beiden: Festbrennweite oder Zoom. Verwenden Sie mindestens einmal <em>depth of field</em>.',
    actWriteBrief='Schreiben Sie das Briefing für ein Shooting, das Sie machen möchten: wofür es ist, wer es sieht und was das Licht tun soll.',
    actPlaceholder='The brief: a series of six portraits, shot in available light,',
    resPerfect='Volle Punktzahl. Sie können benennen, was ein Objektiv tut — und was es falsch macht.',
    resStrong='Stark. Das Dreieck sitzt — die Objektivfehler lohnen einen zweiten Durchgang.',
    resMid='Eine gute Grundlage. Zurück zu den drei Einstiegsfolien; der Wortschatz bleibt erst, wenn der Mechanismus sitzt.',
    resLow='Lesen Sie die drei Lehrfolien noch einmal und starten Sie neu. Blende, Zeit, ISO — alles andere hängt daran.',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
