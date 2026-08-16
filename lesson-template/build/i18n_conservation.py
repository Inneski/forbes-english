# -*- coding: utf-8 -*-
"""Interface strings for Conservation Travel (C1/C2), English and German.

The taught items stay in English — the article is the object of study. German
carries the explanation around it.

The English half was lifted mechanically out of `build_conservation.py` rather
than retyped, so the two cannot drift. Change a teaching string in the builder
and re-lift.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    t1e="Before the first question",
    t1t="Five of the six questions ask what the article <em>implies</em>",
    t1ah="Not what it says",
    t1an="You are being asked what follows from the text &mdash; which is why you can locate a sentence and still choose wrong.",
    t1bh="The distractors are usually true",
    t1bn="Several name real problems that conservation projects elsewhere do face. Truth is not the test; relevance is.",
    t1ch="The habit that helps",
    t1cn="A detail can be there to prove a point, to concede one, or to set a scene. Which it is decides the answer.",

    t2e="Worked example",
    t2t="Two readings of the same sentence",
    t2ah="The sentence",
    t2an="About the Mashpi glass frog, documented after five years of survey work in the Chocó cloud forest.",
    t2bh="The shallow reading",
    t2bn="True, and it answers nothing. It treats the clause as a fact about an animal.",
    t2ch="The reading being tested",
    t2cn="The clause is an <em>argument for the reserve</em>. That is what it is doing in the paragraph, and that is the answer.",

    t3e="The transferable one",
    t3t="Naming by comparison &mdash; &ldquo;Europe&rsquo;s Yellowstone&rdquo;",
    t3ah="What it imports",
    t3an="This is the load the phrase is meant to carry, and the article says so in the sentences around it.",
    t3bh="What it does not",
    t3bn="A comparison never imports everything. If it did, it would be an identity claim rather than a comparison.",
    t3ch="Deciding which",
    t3cn="The next sentences here are about reintroduced species and old-growth forest. So: ecology, not commerce. The context selects the load.",

    t4e="The vocabulary, one",
    t4t="Scarcity and loss",
    t4ah="rare",
    t4an="Not <em>scarce</em>, which is about supply against demand, and not <em>endangered</em>, which is about trajectory.",
    t4bh="face extinction",
    t4bn="Of a species or a whole system. <em>Face</em> is doing work: it frames the outcome as still ahead and still avoidable.",
    t4ch="millennia",
    t4cn="A Latin plural that survived intact into formal English. Reach for it when the span itself is the point.",

    t5e="The vocabulary, two",
    t5t="Transformation and heritage",
    t5ah="retraining",
    t5an="The prefix carries the argument: the skills were already there &mdash; the forest knowledge, the tracking &mdash; and were redirected, not replaced.",
    t5bh="traditional",
    t5bn="Neutral here, deliberately. Elsewhere it can imply outdated; set alongside modern science as an equal partner, it does not.",
    t5ch="cultural",
    t5cn="An ordinary word inside a fixed official title. The capitals belong to the title, not to the word.",

    t6e="The five projects",
    t6t="What each one is actually protecting",
    t6ah="Ecuador &middot; Mashpi",
    t6an="24 new species recorded, the glass frog among them.",
    t6bh="Romania &middot; the Carpathians",
    t6bn="The one the Yellowstone comparison is about.",
    t6ch="Costa Rica &middot; the turtles",
    t6cn="Against poaching, with round-the-clock monitoring.",
    t6dh="Polynesia &amp; Japan",
    t6dn="One protects a habitat, the other a practice. The last activity asks you to tell those apart.",

    coverTitle="Conservation <em>Travel</em>",
    coverSub="From cloud forests to coral reefs — five projects, and the difference between what a text says and what it means",
    chipLevel="C1 · C2",
    chipFocus="Inference & the vocabulary of loss",
    chipCount="21 slides",
    qEyebrow="What does it imply?",
    qTitle="Choose the reading the article supports",
    gapEyebrow="The article’s own words",
    gapTitle="Complete the sentence",
    gapHint="Every word in the bank is used exactly once on this slide.",
    bankLabel="Word bank:",
    ordEyebrow="Sequence",
    ordTitle="The Coral Gardeners restoration process",
    ordTitle2="How the Mashpi Reserve came about",
    ordHint="Drag the steps into order — or click one, then the position you want it in.",
    sortEyebrow="The five projects",
    sortTitle="What is each one protecting?",
    sortHint="Drag each into a box — or click it, then the box. A wrong first placement costs that item’s point.",
    resNext="You can read the argument. Now make one →",
    resPerfect="Full marks. You separated what the article says from what it means — that is the whole of C1 reading.",
    resStrong="Strong. Go back over the comparison slide before you write; that is the one that transfers furthest.",
    resMid="A solid base. Most of the lost marks are on inference, not vocabulary — re-read the worked example.",
    resLow="Start again from the opening slides. The distractors are true; the question is which one is the point.",
    actEyebrow="Activation",
    actTitle="Make the case for one project",
    actUse="Use at least four:",
    actSpeakKind="Speaking · in pairs",
    actSpeakBrief="One of you has funding for exactly one of the five projects. The other wants it spent somewhere else.",
    actSpeak1="Argue for a project that protects a <em>practice</em> rather than a species. Notice that it is harder, and say why.",
    actSpeak2="Use <em>face extinction</em> once, accurately — about something that can actually become extinct.",
    actSpeak3="Make one claim your partner has to infer rather than one you state outright. Then ask them what they took from it.",
    actSpeak4="Compare your project to a famous one. Then say which properties the comparison carries and which it does not.",
    actWriteKind="Writing · 250–300 words",
    actWriteBrief="A funding case for one project: what it protects, what is lost without it, and what a visitor actually contributes. Do not overstate — the strongest version concedes the weakest part of the case.",
    actPlaceholder="This project protects…",
)

T['de'] = dict(
    t1e="Vor der ersten Frage",
    t1t="Fünf der sechs Fragen zielen darauf, was der Artikel <em>impliziert</em>",
    t1ah="Nicht, was dasteht",
    t1an="Verständnisfragen haben eine auffindbare Antwort. Diese nicht. Gefragt ist, was aus dem Text folgt — deshalb können Sie den Satz finden und trotzdem falsch wählen.",
    t1bh="Die Distraktoren stimmen meist",
    t1bn="Sie sind nur nicht der Punkt des Artikels. Mehrere benennen reale Probleme anderer Naturschutzprojekte. Geprüft wird nicht Wahrheit, sondern Relevanz.",
    t1ch="Die hilfreiche Gewohnheit",
    t1cn="Fragen Sie, was der Satz <em>tut</em>, nicht nur, was er berichtet. Ein Detail kann belegen, einräumen oder eine Szene setzen — welches davon, entscheidet die Antwort.",

    t2e="Beispiel",
    t2t="Zwei Lesarten desselben Satzes",
    t2ah="Der Satz",
    t2an="<em>It could have vanished before science knew it existed.</em> Über den Mashpi-Glasfrosch, dokumentiert nach fünf Jahren Feldarbeit im Chocó-Nebelwald.",
    t2bh="Die flache Lesart",
    t2bn="„Ein seltener Frosch wurde gefunden.“ Wahr — und beantwortet nichts. Sie behandelt den Nebensatz als Tatsache über ein Tier.",
    t2ch="Die geprüfte Lesart",
    t2cn="„Undokumentierte Arten gehen verloren, das Reservat ist dringend.“ Der Nebensatz ist ein <em>Argument für das Reservat</em>. Das tut er im Absatz, und das ist die Antwort.",

    t3e="Die übertragbare Fertigkeit",
    t3t="Benennen durch Vergleich — „Europe&rsquo;s Yellowstone“",
    t3ah="Was der Vergleich mitbringt",
    t3an="Maßstab, Ambition, Rewilding auf kontinentaler Ebene, zurückgekehrte Großsäuger. Das ist die Last, die er tragen soll, und der Artikel sagt es in den umgebenden Sätzen.",
    t3bh="Was nicht",
    t3bn="Die Parkplätze, die Besucherzahlen, die Finanzierung, die Nationalität. Ein Vergleich bringt nie alles mit — sonst wäre er eine Gleichsetzung.",
    t3ch="Wie man entscheidet",
    t3cn="Lesen Sie, was direkt danach folgt. Hier: ausgewilderte Arten und Urwald. Also Ökologie, nicht Kommerz. Der Kontext wählt die Last aus.",

    t4e="Wortschatz I",
    t4t="Knappheit und Verlust",
    t4ah="rare",
    t4an="An sich selten. <em>Rare high-altitude ecosystems.</em> Nicht <em>scarce</em> (Angebot gegen Nachfrage) und nicht <em>endangered</em> (Entwicklung).",
    t4bh="face extinction",
    t4bn="Die feste Verbindung. Von einer Art oder einem ganzen System. <em>Face</em> arbeitet mit: Es rahmt das Ergebnis als noch bevorstehend und noch abwendbar.",
    t4ch="millennia",
    t4cn="Plural von <em>millennium</em>. <em>Over two millennia.</em> Ein lateinischer Plural, der im formellen Englisch überlebt hat. Nehmen Sie ihn, wenn die Zeitspanne selbst der Punkt ist.",

    t5e="Wortschatz II",
    t5t="Wandel und Erbe",
    t5ah="retraining",
    t5an="<em>Retraining its loggers and poachers as researchers.</em> Das Präfix trägt das Argument: Die Fähigkeiten waren da — Waldkenntnis, Fährtenlesen — und wurden umgelenkt, nicht ersetzt.",
    t5bh="traditional",
    t5bn="Hier bewusst neutral. Anderswo kann es „überholt“ mitschwingen lassen; neben moderner Wissenschaft als gleichwertig gestellt, tut es das nicht.",
    t5ch="cultural",
    t5cn="<em>Important Intangible Folk Cultural Property</em> — Japans formelle Bezeichnung für die Ama. Ein gewöhnliches Wort in einem festen Titel. Die Großschreibung gehört dem Titel.",

    t6e="Die fünf Projekte",
    t6t="Was jedes davon eigentlich schützt",
    t6ah="Ecuador · Mashpi",
    t6an="Eine Holzkonzession aufgekauft und in ein Nebelwaldreservat verwandelt. 24 neue Arten erfasst, darunter der Glasfrosch.",
    t6bh="Rumänien · Karpaten",
    t6bn="Rewilding im großen Maßstab — Wisent, Luchs, Urwald. Das Projekt, um das es beim Yellowstone-Vergleich geht.",
    t6ch="Costa Rica · Schildkröten",
    t6cn="Nachtpatrouillen, Gelege in bewachte Aufzuchtstationen umgesiedelt. Gegen Wilderei, mit Überwachung rund um die Uhr.",
    t6dh="Polynesien &amp; Japan",
    t6dn="Coral Gardeners pflanzen widerstandsfähige Korallen; die Ama tauchen mit angehaltenem Atem. Eines schützt einen Lebensraum, das andere eine Praxis.",

    coverTitle="Naturschutz<em>reisen</em>",
    coverSub="Vom Nebelwald zum Korallenriff — fünf Projekte, und der Unterschied zwischen dem, was ein Text sagt, und dem, was er meint",
    chipLevel="C1 · C2",
    chipFocus="Inferenz & der Wortschatz des Verlusts",
    chipCount="21 Folien",
    qEyebrow="Was wird impliziert?",
    qTitle="Wählen Sie die Lesart, die der Artikel stützt",
    gapEyebrow="Die Worte des Artikels",
    gapTitle="Vervollständigen Sie den Satz",
    gapHint="Jedes Wort aus dem Wortspeicher wird auf dieser Folie genau einmal verwendet.",
    bankLabel="Wortspeicher:",
    ordEyebrow="Reihenfolge",
    ordTitle="Der Restaurierungsprozess von Coral Gardeners",
    ordTitle2="Wie das Mashpi-Reservat entstand",
    ordHint="Ziehen Sie die Schritte in die richtige Reihenfolge — oder klicken Sie einen Schritt und dann die Position.",
    sortEyebrow="Die fünf Projekte",
    sortTitle="Was schützt jedes davon?",
    sortHint="Ziehen Sie jeden Eintrag in ein Feld — oder klicken Sie erst den Eintrag, dann das Feld. Eine falsche erste Zuordnung kostet den Punkt.",
    resNext="Sie können das Argument lesen. Jetzt führen Sie eines →",
    resPerfect="Volle Punktzahl. Sie haben getrennt, was der Artikel sagt, von dem, was er meint — das ist der Kern des Lesens auf C1.",
    resStrong="Stark. Sehen Sie die Vergleichsfolie noch einmal an, bevor Sie schreiben; sie trägt am weitesten.",
    resMid="Eine solide Grundlage. Die meisten verlorenen Punkte liegen bei der Inferenz, nicht beim Wortschatz — lesen Sie das Beispiel erneut.",
    resLow="Beginnen Sie noch einmal bei den Einstiegsfolien. Die Distraktoren stimmen; die Frage ist, welcher der Punkt ist.",
    actEyebrow="Anwendung",
    actTitle="Führen Sie den Fall für ein Projekt",
    actUse="Verwenden Sie mindestens vier:",
    actSpeakKind="Sprechen · zu zweit",
    actSpeakBrief="Eine Person hat Mittel für genau eines der fünf Projekte. Die andere will sie anderswo ausgeben.",
    actSpeak1="Argumentieren Sie für ein Projekt, das eine <em>Praxis</em> schützt und keine Art. Merken Sie, dass es schwerer ist — und sagen Sie warum.",
    actSpeak2="Verwenden Sie <em>face extinction</em> einmal korrekt — für etwas, das tatsächlich aussterben kann.",
    actSpeak3="Formulieren Sie eine Behauptung so, dass Ihr Gegenüber sie erschließen muss. Fragen Sie dann, was angekommen ist.",
    actSpeak4="Vergleichen Sie Ihr Projekt mit einem berühmten. Sagen Sie dann, welche Eigenschaften der Vergleich trägt und welche nicht.",
    actWriteKind="Schreiben · 250–300 Wörter",
    actWriteBrief="Ein Förderantrag für ein Projekt: was es schützt, was ohne es verloren geht, und was ein Besucher tatsächlich beiträgt. Nicht übertreiben — die stärkste Fassung räumt den schwächsten Punkt ein.",
    actPlaceholder="This project protects…",
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
