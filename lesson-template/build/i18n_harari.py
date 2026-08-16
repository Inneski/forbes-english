# -*- coding: utf-8 -*-
"""Interface strings for Harari at Davos (C2), English and German.

The taught items stay in English throughout — the transcript is the object of
study and translating Harari's wording would defeat the lesson. German carries
the explanation around it.

The English half of this file was lifted mechanically out of `build_harari.py`
rather than retyped, so the two cannot drift apart. If you change a teaching
string, change it in the builder and re-lift.

`resNext`, `actEyebrow` and `actSpeakKind` are deliberately NOT in LIFT: this
lesson passes its own text for all three, and lifting would overwrite them with
the generic chrome string at runtime.
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
    t1t="You are not being asked whether you agree with him",
    t1ah="The object is the argument",
    t1an="What is on the test: which sentence is a premise, which is an inference, and whether the second follows from the first.",
    t1bh="Every claim here is his",
    t1bn="Where this deck paraphrases, it says so. You will be asked to tell the difference, because at C2 misreporting a source is the expensive error.",
    t1ch="Analogies are the recurring test",
    t1cn="An analogy illustrates; it does not prove. Each one is worth asking what it captures and where it breaks.",

    t2e="The first distinction",
    t2t="<em>tool</em> and <em>agent</em> &mdash; the word the whole address rests on",
    t2ah="a tool",
    t2an="A knife cuts salad or it does not, and either way the choosing happened somewhere else. Tools have no interests.",
    t2bh="an agent",
    t2bn="Verbatim: <em>&ldquo;It is not just another tool. It is an agent. It can learn and change by itself.&rdquo;</em>",
    t2ch="Why the word is load-bearing",
    t2cn="If AI is a tool, the rest of the speech does not follow. That is why he spends the opening on it rather than on capability.",

    t3e="The second distinction",
    t3t="<em>a person</em> and <em>a legal person</em> are not the same claim",
    t3ah="a legal person",
    t3an="Companies have been legal persons for a century and a half. So, in some jurisdictions, are rivers.",
    t3bh="Why the precedents were safe",
    t3bn="The personhood was a <em>fiction</em> laid over human decisions. That is precisely what made it harmless.",
    t3ch="Why this case differs",
    t3cn="Fiction and fact converge, so the precedents stop governing. This is the hinge of the address, and it is entirely a lexical distinction.",

    t4e="How to weigh an analogy",
    t4t="The mercenaries &mdash; what it carries and where it gives way",
    t4ah="The story, in summary",
    t4an="Marked as a summary because it is one. The transcript is dialogue, not the tidy sentence above.",
    t4bh="What it captures",
    t4bn="And the sharper point: we already accept this about people, which is why the inconsistency about machines is striking.",
    t4ch="Where it gives way",
    t4cn="The analogy borrows its menace from human motive. Strip the motive and you have a capable system, not a usurper. Say so in your writing.",

    t5e="The skill this lesson is really for",
    t5t="Reporting a claim without adopting it",
    t5ah="Neutral: <em>states, notes, observes</em>",
    t5an="Use where the fact is uncontested. Choosing a neutral verb for a contested claim is itself an endorsement.",
    t5bh="Marked: <em>contends, maintains, insists</em>",
    t5bn="Signals a position that others dispute &mdash; without saying whether you do. This is the workhorse of academic writing.",
    t5ch="Structural: <em>concedes, pre-empts, qualifies</em>",
    t5cn="Describes what a move <em>does</em> in the argument. Examiners reward this because it shows you read the structure, not just the content.",

    t6e="The same skill, one level finer",
    t6t="Hedging &mdash; how much weight to put on a claim",
    t6ah="On the claim",
    t6an="<em>If Harari is right that institutions are linguistic, then&hellip;</em> lets you follow an argument without buying it.",
    t6bh="On the strength",
    t6bn="<em>The inference need not follow</em> is a criticism. <em>Does not follow</em> is a stronger one you then have to prove.",
    t6ch="The failure mode",
    t6cn="Hedge the contested step and commit to the rest. A paragraph where every clause is qualified scores worse than one clear claim.",

    coverTitle="Harari at <em>Davos</em>",
    coverSub="An honest conversation on AI and humanity — and how to write about an argument you have not yet decided about",
    chipLevel="C2 · Proficiency",
    chipFocus="Argument analysis & reporting language",
    chipSource="WEF Annual Meeting 2026",
    qEyebrow="Read the argument, not the opinion",
    qTitle="Choose the most exact reading",
    gapEyebrow="His words, not ours",
    gapTitle="Complete the line from the transcript",
    gapHint="Every word in the bank is used exactly once on this slide.",
    bankLabel="Word bank:",
    sortEyebrow="The shape of the argument",
    sortTitle="Premise, inference, or recommendation?",
    sortTitle2="The same three categories, the second thread",
    sortHint="Drag each line into a box — or click the line, then the box. A wrong first placement costs that line’s point.",
    resNext="You can take the argument apart. Now write about it →",
    resPerfect="Full marks. You separated the premises from the inferences — which is the whole of C2 reading.",
    resStrong="Strong. The distinctions hold; go back over the analogy slide before you write.",
    resMid="A solid base. Re-read the two reporting-verb slides — most of the lost marks are there, not in comprehension.",
    resLow="Go back to the opening slides. The point is reading an argument, not agreeing with one.",
    actEyebrow="Activation",
    actTitle="Write about the argument",
    actUse="Use at least four:",
    actSpeakKind="Speaking · in pairs",
    actSpeakBrief="One of you takes Tracey’s position, one takes Harari’s. Neither of you has to believe it.",
    actSpeak1="Report your partner’s last claim back to them using <em>contends</em> or <em>maintains</em> — accurately enough that they accept the summary.",
    actSpeak2="Concede one point genuinely before you answer it. Notice what conceding does to your credibility.",
    actSpeak3="Attack one <em>inference</em> rather than a premise. Say which step you think does not carry.",
    actSpeak4="Take one analogy and say where it gives way, without saying the conclusion is therefore wrong.",
    actWriteKind="Writing · 300–350 words",
    actWriteBrief="Choose one: (1) His closing line is more poignant than rigorous — discuss. (2) A policy briefing endorsing or challenging a ban on AI legal personhood. (3) The rhetorical strategy of the address for this particular audience.",
    actPlaceholder="Harari contends that…",
)

T['de'] = dict(
    t1e="Vor der ersten Frage",
    t1t="Es wird nicht gefragt, ob Sie ihm zustimmen",
    t1ah="Gegenstand ist die Argumentation",
    t1an="Geprüft wird: Welcher Satz ist eine Prämisse, welcher eine Schlussfolgerung — und trägt die zweite die erste.",
    t1bh="Jede Aussage hier stammt von ihm",
    t1bn="Zitierte Zeilen sind wörtlich aus dem Davos-Transkript. Zusammenfassungen sind als solche gekennzeichnet. Auf C2-Niveau ist die Fehlwiedergabe einer Quelle der teure Fehler.",
    t1ch="Analogien sind der wiederkehrende Test",
    t1cn="Eine Analogie veranschaulicht; sie beweist nicht. Fragen Sie bei jeder: Was trifft sie, und wo bricht sie?",

    t2e="Die erste Unterscheidung",
    t2t="<em>tool</em> und <em>agent</em> — das Wort, auf dem die ganze Rede ruht",
    t2ah="a tool — ein Werkzeug",
    t2an="Etwas, <em>durch</em> das gehandelt wird. Ein Messer schneidet oder nicht; entschieden wird anderswo. Werkzeuge haben keine Interessen.",
    t2bh="an agent — ein handelndes Subjekt",
    t2bn="Wörtlich: <em>&bdquo;It is not just another tool. It is an agent. It can learn and change by itself.&ldquo;</em>",
    t2ch="Warum das Wort tragend ist",
    t2cn="Wäre KI ein Werkzeug, folgte der Rest der Rede nicht. Deshalb beginnt er hiermit und nicht mit Leistungsfähigkeit.",

    t3e="Die zweite Unterscheidung",
    t3t="<em>a person</em> und <em>a legal person</em> sind nicht dieselbe Behauptung",
    t3ah="a legal person — Rechtsperson",
    t3an="Ein Rechtssubjekt, das besitzen, Verträge schließen und klagen kann. Muss kein Mensch sein: Unternehmen sind es seit über hundert Jahren, mancherorts auch Flüsse.",
    t3bh="Warum die Präzedenzfälle harmlos waren",
    t3bn="Ein Fluss eröffnet kein Konto. Immer handelte ein Mensch für ihn. Die Rechtsperson war eine <em>Fiktion</em> über menschlichen Entscheidungen — genau das machte sie ungefährlich.",
    t3ch="Warum dieser Fall anders liegt",
    t3cn="Eine KI kann die Rolle selbst ausfüllen. Fiktion und Tatsache fallen zusammen, die Präzedenzfälle greifen nicht mehr. Das ist der Angelpunkt — und er ist rein lexikalisch.",

    t4e="Wie man eine Analogie wiegt",
    t4t="Die Söldner — was sie trägt und wo sie nachgibt",
    t4ah="Die Geschichte, zusammengefasst",
    t4an="Ein britischer König wirbt angelsächsische Kämpfer an. Sie siegen, sehen sich um und behalten das Land. Als Zusammenfassung gekennzeichnet, weil sie eine ist.",
    t4bh="Was sie trifft",
    t4bn="Gekaufte Loyalität lässt sich überbieten. Und schärfer: Bei Menschen akzeptieren wir das längst — deshalb fällt die Inkonsequenz bei Maschinen auf.",
    t4ch="Wo sie nachgibt",
    t4cn="Söldner wollten Land. Was eine KI wollen soll, bleibt unbegründet. Ohne Motiv bleibt ein leistungsfähiges System, kein Usurpator. Schreiben Sie das so.",

    t5e="Wofür diese Lektion eigentlich da ist",
    t5t="Eine Behauptung wiedergeben, ohne sie zu übernehmen",
    t5ah="Neutral: <em>states, notes, observes</em>",
    t5an="<em>Harari notes that corporations already hold legal personhood.</em> Für Unstrittiges. Ein neutrales Verb für eine strittige Behauptung ist selbst schon Zustimmung.",
    t5bh="Markiert: <em>contends, maintains, insists</em>",
    t5bn="<em>He contends that anything made of words will be taken over.</em> Signalisiert eine bestrittene Position — ohne zu sagen, ob Sie sie teilen. Das Arbeitspferd des akademischen Schreibens.",
    t5ch="Strukturell: <em>concedes, pre-empts, qualifies</em>",
    t5cn="<em>He pre-empts the &bdquo;glorified autocomplete&ldquo; objection.</em> Beschreibt, was ein Zug im Argument <em>tut</em>. Prüfer honorieren das, weil es zeigt, dass Sie die Struktur gelesen haben.",

    t6e="Dieselbe Fertigkeit, eine Stufe feiner",
    t6t="Hedging — wie viel Gewicht Sie auf eine Behauptung legen",
    t6ah="Auf die Behauptung",
    t6an="<em>arguably, on his account, if this is right.</em> <em>If Harari is right that institutions are linguistic, then…</em> erlaubt, einem Argument zu folgen, ohne es zu kaufen.",
    t6bh="Auf die Stärke",
    t6bn="<em>tends to, in large part, need not follow.</em> <em>The inference need not follow</em> ist Kritik. <em>Does not follow</em> ist stärker — und muss belegt werden.",
    t6ch="Der typische Fehler",
    t6cn="Alles abzuschwächen liest sich wie gar keine Position. Schwächen Sie den strittigen Schritt ab und stehen Sie zum Rest.",

    coverTitle="Harari in <em>Davos</em>",
    coverSub="Ein ehrliches Gespräch über KI und Menschheit — und wie man über ein Argument schreibt, zu dem man sich noch nicht entschieden hat",
    chipLevel="C2 · Kompetente Sprachverwendung",
    chipFocus="Argumentanalyse & Redewiedergabe",
    chipSource="WEF Jahrestreffen 2026",
    qEyebrow="Lesen Sie das Argument, nicht die Meinung",
    qTitle="Wählen Sie die genaueste Lesart",
    gapEyebrow="Seine Worte, nicht unsere",
    gapTitle="Vervollständigen Sie die Zeile aus dem Transkript",
    gapHint="Jedes Wort aus dem Wortspeicher wird auf dieser Folie genau einmal verwendet.",
    bankLabel="Wortspeicher:",
    sortEyebrow="Der Aufbau des Arguments",
    sortTitle="Prämisse, Schlussfolgerung oder Empfehlung?",
    sortTitle2="Dieselben drei Kategorien, der zweite Strang",
    sortHint="Ziehen Sie jede Zeile in ein Feld — oder klicken Sie erst die Zeile, dann das Feld. Eine falsche erste Zuordnung kostet den Punkt für diese Zeile.",
    resNext="Sie können das Argument zerlegen. Jetzt schreiben Sie darüber →",
    resPerfect="Volle Punktzahl. Sie haben Prämissen von Schlussfolgerungen getrennt — das ist der Kern des Lesens auf C2.",
    resStrong="Stark. Die Unterscheidungen sitzen; sehen Sie die Analogie-Folie noch einmal an, bevor Sie schreiben.",
    resMid="Eine solide Grundlage. Lesen Sie die beiden Folien zur Redewiedergabe erneut — dort liegen die meisten verlorenen Punkte, nicht im Verständnis.",
    resLow="Zurück zu den Einstiegsfolien. Es geht darum, ein Argument zu lesen, nicht ihm zuzustimmen.",
    actEyebrow="Anwendung",
    actTitle="Schreiben Sie über das Argument",
    actUse="Verwenden Sie mindestens vier:",
    actSpeakKind="Sprechen · zu zweit",
    actSpeakBrief="Eine Person vertritt Traceys Position, eine Harari. Niemand muss daran glauben.",
    actSpeak1="Geben Sie die letzte Behauptung Ihres Gegenübers mit <em>contends</em> oder <em>maintains</em> wieder — so genau, dass die Zusammenfassung akzeptiert wird.",
    actSpeak2="Räumen Sie einen Punkt wirklich ein, bevor Sie antworten. Achten Sie darauf, was das Einräumen mit Ihrer Glaubwürdigkeit macht.",
    actSpeak3="Greifen Sie eine <em>Schlussfolgerung</em> an, keine Prämisse. Sagen Sie, welcher Schritt Ihrer Ansicht nach nicht trägt.",
    actSpeak4="Nehmen Sie eine Analogie und sagen Sie, wo sie nachgibt — ohne zu behaupten, die Schlussfolgerung sei deshalb falsch.",
    actWriteKind="Schreiben · 300–350 Wörter",
    actWriteBrief="Wählen Sie eine Aufgabe: (1) Sein Schlusssatz ist eher ergreifend als stringent — diskutieren Sie. (2) Ein Politikpapier, das ein Verbot der KI-Rechtspersönlichkeit befürwortet oder ablehnt. (3) Die rhetorische Strategie der Rede für genau dieses Publikum.",
    actPlaceholder="Harari contends that…",
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
