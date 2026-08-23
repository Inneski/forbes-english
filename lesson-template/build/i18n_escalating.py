# -*- coding: utf-8 -*-
"""Interface strings for Escalating a Complaint (C1) — English and German.

Reconstructed. The builder for this deck was lost with the sandbox that wrote
it, so this module and build_escalating.py were rebuilt from the shipped page;
every string here is lifted out of forbes-escalating-a-complaint-c1.html rather
than retranslated, so a re-run reproduces what shipped.

Same scope boundary as every other deck: the switcher translates the app's own
chrome — cover, section titles, the four moves, the activation briefs, the
result bands. It does NOT translate the English being taught, so every stem,
option, gap sentence, word bank, sort item, order chunk and explanation stays
in English in both languages. The two roleplay quotations inside actSpeak1 and
actSpeak2 stay in English for the same reason: they are the lines the learner
has to answer, not instructions about the task.

Two shapes differ from the sibling builders and are deliberate:

  * LIFT is longer than usual because this deck has an Open button and a word
    bank. btnOpen comes from CHROME with the rest; bankLabel does not — it is
    lesson text, declared in T.
  * TAIL is a second chrome block emitted after the sorted body rather than
    merged into it. The template's deck chrome carries six data-i18n keys no
    lesson declares — the branch-mode ledger's three labels, the two glossary
    buttons and the locked-branch message — and check-lesson.js's I18N gate
    fails any deck where a data-i18n does not resolve. They are chrome, so they
    are copied verbatim from the template rather than re-invented per lesson.

WARNING — a divergence carried over from the shipped page, deliberately not
"fixed" here. Nine values in T['en'] are LONGER than the text the builder emits
into the same slot: case3, case4, factNote1, factNote2, moves1, moves2, moves3,
moves4 and proto2. The shipped HTML carries the trimmed sentences; T['en']
carries the full ones, so the slide grows when a learner switches to German and
back to English. That is the fingerprint of a hand-edit made to the generated
HTML after the layout gate failed, which is exactly the failure mode CLAUDE.md
warns about. Reproducing it was the point of this reconstruction; correcting it
is a separate, deliberate edit — pick one of the two texts for each of the nine
keys, put it in both places, and re-run the checker.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

# Emitted from CHROME verbatim, sorted in with the body.
LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'btnOpen', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

# Template chrome no lesson declares. Raw JS literals, emitted after the body.
TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'",
           'glossShow': "'Translate'",
           'ledClues': "'Clues'",
           'ledDp': "'DP'",
           'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll tr\u00e4gt dieses Ende nicht'",
           'glossHide': "'Ausblenden'",
           'glossShow': "'\u00dcbersetzen'",
           'ledClues': "'Hinweise'",
           'ledDp': "'DP'",
           'ledTime': "'Zeit'"},
}

T = {}

T['en'] = dict(
    coverTitle='Escalating a <em>Complaint</em>',
    coverSub='Taking a problem to the next level of management without becoming the problem',
    chipLevel='C1 &middot; Workplace conflict',
    chipFocus='Evidence, register and the ask',
    chipCount='21 slides',

    caseEyebrow='The case file',
    caseTitle='Marlowe Vane, interior architecture &mdash; and the colleague you are paired with',
    caseH1='The pattern',
    case1='Three schemes running. Nothing appears on the shared drive from him until the night before the deadline, and then the concept work goes up under both names.',
    caseH2='What he is good at',
    case2='Clients like him, and they ask for him. That is real, and any complaint you make has to survive it being true.',
    caseH3='The counter-story',
    case3='He is telling people you refuse to collaborate. You did stop sending him drafts &mdash; because sending them was costing you the authorship of them.',
    caseH4='The blockage',
    case4='Your line manager has heard his version, will not take sides, and hands you his section at 48 hours&rsquo; notice. Her word for this is teamwork.',

    movesEyebrow='Before you write anything',
    movesTitle='Four moves that separate an escalation from a complaint',
    movesH1='Evidence, not adjectives',
    moves1='Dates, file histories, version numbers, who was in the room. <em>Lazy</em>, <em>unreliable</em> and <em>dishonest</em> are conclusions, and you are not being asked for conclusions.',
    movesH2='The pattern, not the incident',
    moves2='One occasion is a bad week. Three dated occasions are a way of working. Senior managers act on patterns and dismiss incidents.',
    movesH3='A specific ask',
    moves3='Say what decision you want made. An escalation with no ask is only a complaint delivered higher up, and it will be sent back down.',
    movesH4='Name the counter-story first',
    moves4='If something is being said about you, say it yourself before it reaches the room. Said first it is context; said second it is a defence.',

    protoEyebrow='Two rules that decide how you are heard',
    protoTitle='Go through, not around &mdash; and leave the man standing',
    protoH1='Through, not around',
    proto1='One date and one sentence is the whole move. Leave it out and her first question is not about him — it is why you did not take this to Ruth, and now you are the one explaining yourself.',
    protoH2='Concede what is true',
    proto2='Give him the thing he is genuinely better at, in one sentence, early. A complaint that says a colleague is bad at everything reads as personal &mdash; and the one strength you leave out is the one your reader has seen for herself.',

    factEyebrow='The single hardest rewrite',
    factTitle='Write it so that it survives being forwarded to him',
    factH1='What you want to send',
    factNote1='Every claim here is about character and intent. None of it can be checked, all of it can be denied, and forwarded to him it makes you the difficult one.',
    factH2='What you can be quoted on',
    factNote2='Same three grievances, nothing softened. Dates, a system record, and a fact about attribution. He can dispute what it means; he cannot dispute that it happened.',

    sortEyebrow='Sort it before you send it',
    sortTitleA='Which of these belongs in the email?',
    sortHintA='Click a line, then click the box it belongs in.',
    sortTitleB='Fact, or a claim about what he intended?',
    sortHintB='A claim about intent is the fastest way to lose a reader. Sort each line.',

    bankLabel='Word bank:',
    gapEyebrow='The language of escalation',
    gapTitle='Complete the sentence',
    gapHint='One word per gap. Each word in the bank is used exactly once across the two screens.',

    ordEyebrow='Build the sentence',
    ordTitleA='The ask',
    ordHintA='Click the parts in order. This is the sentence the whole email exists to deliver.',
    ordTitleB='The pre-empt',
    ordHintB='Click the parts in order. Say it before she hears it from him.',

    qEyebrow='Choose the version that works',
    qTitle='Which one would you actually send?',

    actTitle='Now make the case out loud',
    actUse='Use at least four:',
    actSpeakBrief='In pairs. Three minutes each, then swap roles and run it again with the second prompt.',
    actSpeak1='You are the junior. Your partner is Anneke Brandt, Associate Director. Her first question is: &ldquo;What is it you actually want me to do?&rdquo;',
    actSpeak2='Swap. Anneke opens with: &ldquo;Ruth tells me you will not work with him.&rdquo; Answer without attacking either of them.',
    actSpeak3='Now he is in the room. Say the same three things with him sitting there. What has to change, and what must not?',
    actSpeak4='Argue the other side: when is escalating the wrong move, and what does it cost you?',
    actWriteKind='Writing &middot; 180&ndash;220 words',
    actWriteBrief='Write the email to Anneke Brandt. Three dated facts, one concession, one specific ask, and one line pre-empting the claim that you refuse to collaborate. No adjectives about his character.',
    actPlaceholder='Dear Anneke, I raised this with Ruth on 19 May and I am writing to you because…',

    resPerfect='Full marks. You can hear the difference &mdash; now write it, which is a slower skill.',
    resStrong='Strong. Look again at the ones you missed: most of them turn on a claim about intent.',
    resMid='A workable base. Re-read the two rewrite slides before the writing task.',
    resLow='Go back through the four moves. Almost every miss here is an adjective doing the work a date should do.',
)

T['de'] = dict(
    coverTitle='Eine Beschwerde <em>eskalieren</em>',
    coverSub='Ein Problem an die nächsthöhere Ebene tragen, ohne selbst zum Problem zu werden',
    chipLevel='C1 &middot; Konflikte am Arbeitsplatz',
    chipFocus='Belege, Register und die konkrete Bitte',
    chipCount='21 Folien',

    caseEyebrow='Die Fallakte',
    caseTitle='Marlowe Vane, Innenarchitektur &mdash; und der Kollege, mit dem Sie im Team sind',
    caseH1='Das Muster',
    case1='Drei laufende Projekte. Auf dem gemeinsamen Laufwerk erscheint von ihm nichts bis zum Abend vor der Abgabe &mdash; und dann steht die Konzeptarbeit unter beiden Namen.',
    caseH2='Was er gut kann',
    case2='Die Kunden mögen ihn und fragen nach ihm. Das ist echt, und jede Beschwerde muss standhalten, obwohl es stimmt.',
    caseH3='Die Gegendarstellung',
    case3='Er erzählt herum, Sie verweigerten die Zusammenarbeit. Sie haben tatsächlich aufgehört, ihm Entwürfe zu schicken &mdash; weil es Sie die Urheberschaft daran kostete.',
    caseH4='Die Blockade',
    case4='Ihre direkte Vorgesetzte kennt seine Version, will sich nicht festlegen und übergibt Ihnen seinen Teil 48 Stunden vor Abgabe. Ihr Wort dafür lautet Teamarbeit.',

    movesEyebrow='Bevor Sie irgendetwas schreiben',
    movesTitle='Vier Schritte, die eine Eskalation von einer Beschwerde trennen',
    movesH1='Belege statt Adjektive',
    moves1='Daten, Dateiverläufe, Versionsnummern, wer im Raum war. <em>Lazy</em>, <em>unreliable</em> und <em>dishonest</em> sind Schlussfolgerungen &mdash; und nach denen fragt niemand.',
    movesH2='Das Muster, nicht der Vorfall',
    moves2='Ein Vorfall ist eine schlechte Woche. Drei datierte Vorfälle sind eine Arbeitsweise. Führungskräfte handeln bei Mustern und legen Vorfälle beiseite.',
    movesH3='Eine konkrete Bitte',
    moves3='Sagen Sie, welche Entscheidung Sie wollen. Eine Eskalation ohne Bitte ist nur eine Beschwerde eine Ebene höher &mdash; und sie kommt zurück.',
    movesH4='Die Gegendarstellung zuerst benennen',
    moves4='Wird etwas über Sie erzählt, sagen Sie es selbst, bevor es den Raum erreicht. Zuerst gesagt ist es Kontext; danach gesagt ist es eine Verteidigung.',

    protoEyebrow='Zwei Regeln darüber, wie Sie gehört werden',
    protoTitle='Durch die Ebene, nicht an ihr vorbei &mdash; und lassen Sie ihm seine Stärke',
    protoH1='Durch, nicht vorbei',
    proto1='Ein Datum und ein Satz — mehr ist es nicht. Fehlt das, lautet ihre erste Frage nicht, was er getan hat, sondern warum Sie nicht zu Ruth gegangen sind. Dann erklären Sie sich selbst.',
    protoH2='Zugeben, was stimmt',
    proto2='Räumen Sie ihm früh und in einem Satz das ein, worin er wirklich besser ist. Wer sagt, ein Kollege könne gar nichts, klingt persönlich &mdash; und ausgerechnet die weggelassene Stärke hat Ihre Leserin selbst gesehen.',

    factEyebrow='Die schwierigste Umschrift',
    factTitle='Schreiben Sie es so, dass es standhält, wenn er es weitergeleitet bekommt',
    factH1='Was Sie schicken wollen',
    factNote1='Jede Aussage hier betrifft Charakter und Absicht. Nichts davon ist überprüfbar, alles bestreitbar &mdash; und weitergeleitet macht es Sie zur schwierigen Person.',
    factH2='Wofür man Sie zitieren kann',
    factNote2='Dieselben drei Beschwerden, nichts abgeschwächt. Daten, ein Systemprotokoll und eine Tatsache zur Urheberschaft. Er kann die Deutung bestreiten, nicht den Vorgang.',

    sortEyebrow='Sortieren, bevor Sie senden',
    sortTitleA='Was davon gehört in die E-Mail?',
    sortHintA='Klicken Sie eine Zeile an und dann das Feld, in das sie gehört.',
    sortTitleB='Tatsache oder Behauptung über seine Absicht?',
    sortHintB='Eine Behauptung über Absichten verliert Ihre Leserin am schnellsten. Sortieren Sie jede Zeile.',

    bankLabel='Wortliste:',
    gapEyebrow='Die Sprache der Eskalation',
    gapTitle='Vervollständigen Sie den Satz',
    gapHint='Ein Wort pro Lücke. Jedes Wort der Liste wird auf den beiden Folien genau einmal gebraucht.',

    ordEyebrow='Bauen Sie den Satz',
    ordTitleA='Die Bitte',
    ordHintA='Klicken Sie die Teile der Reihe nach an. Für diesen Satz existiert die ganze E-Mail.',
    ordTitleB='Die Vorwegnahme',
    ordHintB='Klicken Sie die Teile der Reihe nach an. Sagen Sie es, bevor sie es von ihm hört.',

    qEyebrow='Wählen Sie die Fassung, die funktioniert',
    qTitle='Welche würden Sie wirklich abschicken?',

    actTitle='Jetzt tragen Sie den Fall mündlich vor',
    actUse='Mindestens vier verwenden:',
    actSpeakBrief='Zu zweit. Je drei Minuten, dann Rollen tauschen und mit der zweiten Aufgabe wiederholen.',
    actSpeak1='Sie sind die Junior-Kraft. Ihr Gegenüber ist Anneke Brandt, Associate Director. Ihre erste Frage: &ldquo;What is it you actually want me to do?&rdquo;',
    actSpeak2='Tauschen. Anneke beginnt mit: &ldquo;Ruth tells me you will not work with him.&rdquo; Antworten Sie, ohne eine der beiden Personen anzugreifen.',
    actSpeak3='Jetzt sitzt er mit im Raum. Sagen Sie dieselben drei Dinge in seiner Anwesenheit. Was muss sich ändern &mdash; und was auf keinen Fall?',
    actSpeak4='Vertreten Sie die Gegenseite: Wann ist Eskalieren der falsche Schritt, und was kostet es Sie?',
    actWriteKind='Schreiben &middot; 180&ndash;220 Wörter',
    actWriteBrief='Schreiben Sie die E-Mail an Anneke Brandt. Drei datierte Tatsachen, ein Zugeständnis, eine konkrete Bitte und ein Satz, der dem Vorwurf der Verweigerung zuvorkommt. Keine Adjektive über seinen Charakter.',
    actPlaceholder='Dear Anneke, I raised this with Ruth on 19 May and I am writing to you because…',

    resPerfect='Volle Punktzahl. Sie hören den Unterschied &mdash; jetzt schreiben Sie ihn, das dauert länger.',
    resStrong='Stark. Sehen Sie sich die Fehler noch einmal an: Meist hängen sie an einer Behauptung über Absichten.',
    resMid='Eine brauchbare Grundlage. Lesen Sie die beiden Umschrift-Folien noch einmal, bevor Sie schreiben.',
    resLow='Gehen Sie die vier Schritte noch einmal durch. Fast jeder Fehler ist ein Adjektiv, wo ein Datum stehen müsste.',
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
