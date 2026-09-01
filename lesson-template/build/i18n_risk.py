# -*- coding: utf-8 -*-
"""Interface strings for Managing Risk (C1/C2) — English, German and Spanish.

Innes asked for this lesson with Spanish and German support, so all three
languages are complete and all three appear in the switcher. The remaining
seven stay as {} and are therefore not offered — house style §8: partial is a
failure, empty is an honest placeholder.

Same scope boundary as every other deck, and it matters more here than usual.
The switcher translates the app's own chrome: cover, section titles, task
instructions and hints, the notes under each teaching card, the activation
briefs and the result bands. It does NOT translate the English being taught.
Every stem, option, gap sentence, word bank, sort item, order chunk, match
pair, explanation and activation chip stays in English in all three languages,
because the target language of this lesson IS risk vocabulary — translating
<em>mitigate</em> into <em>abschwächen</em> would hand the learner the answer
to four separate questions.

That is also why the teaching cards use deck.teach's five-item form: the term
and its English definition carry no data-i18n and stay put, while the note
underneath — which is commentary about the term, not the term — translates.
A learner switching to Spanish sees the same English vocabulary with Spanish
guidance around it, which is the support that was asked for.

One deliberate non-translation inside the German and Spanish text: where a
note quotes the English phrase being taught (<em>may well</em>, <em>might
just</em>, <em>inherent risk</em>, <em>Felt by whom?</em>) the quotation stays
in English. It is the object under discussion, not instructions about the task.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

# Emitted from CHROME verbatim, sorted in with the body.
#
# actSpeakKind and resNext are NOT lifted: CHROME carries 'Discussion · in
# pairs' and the generic results line, and this lesson runs its activation in
# threes (chair, risk owner, finance director) and wants its own hand-off
# sentence. Both are declared in T below instead.
LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'btnCopy', 'btnCopied',
        'wordCount', 'btnOpen', 'actEyebrow']

# Template chrome that no lesson declares but check-lesson.js's I18N gate still
# resolves. Raw JS literals, emitted after the body. Copied verbatim from the
# template rather than re-invented per lesson; Spanish added to match.
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
    coverTitle='Managing <em>Risk</em>',
    coverSub='Naming exposure, grading it, owning it and acting on it — without overstating what you know or hiding what you do',
    chipLevel='C1&ndash;C2 &middot; Enterprise risk',
    chipFocus='Precision, calibration and ownership',
    chipCount='NSLIDES slides',

    t1Eyebrow='The four words that get swapped',
    t1Title='<em>Hazard</em>, <em>risk</em>, <em>exposure</em>, <em>issue</em>',
    t1n1='It exists whether or not it ever reaches you.',
    t1n2='The moment it becomes certain, it stops being a risk.',
    t1n3='A quantity, not a judgement.',
    t1n4='Calling it a risk after the fact sounds like hoping.',

    t2Eyebrow='Three fixed patterns',
    t2Title='<em>a risk of</em>, <em>a risk to</em>, <em>at risk of</em>',
    t2n1='Ask yourself: what is the event?',
    t2n2='Ask yourself: what gets hurt?',
    t2n3='Use it when the thing threatened matters more than the risk does.',
    t2n4='All three, in the order a reader expects them.',

    t3Eyebrow='The four responses',
    t3Title='What you can actually do about a risk',
    t3n1='Before controls it is <em>inherent risk</em>; what is left after them is <em>residual risk</em>.',
    t3n2='The event still happens. Only the bill moves.',
    t3n3='Tolerating is a decision on the record. Ignoring is not.',
    t3n4='The only response that can honestly use <em>eliminate</em>.',

    t4Eyebrow='Calibration',
    t4Title='Saying how likely it is, without hiding it',
    t4n1='<em>We may well breach the covenant</em> is a warning, not a maybe.',
    t4n2='<em>Might just</em> is weaker than <em>might</em>, not stronger.',
    t4n3='Understatement a C2 reader hears as emphasis &mdash; and a B2 reader may miss entirely.',

    t5Eyebrow='Three words a board does not confuse',
    t5Title='Appetite, tolerance, capacity',
    t5n1='Chosen deliberately, and minuted.',
    t5n2='A threshold that obliges someone to act, not a preference.',
    t5n3='Not chosen. You can exceed your capacity once.',

    t6Eyebrow='Register',
    t6Title='What the passive may hide &mdash; and what it may not',
    t6n1='Honest work: reporting what happened before you can say who.',
    t6n2='A decision with no decider, so there is nobody to ask.',
    t6n3='If you know who, and the sentence hides them, that is the tell.',

    sortEyebrow='Before you open your mouth',
    sortTitleA='Still ahead of you, or already landed?',
    sortHintA='Click a line, then the box it belongs in. Each pair is the same story on either side of the event.',
    sortTitleB='Which of the four responses is this?',
    sortHintB='Click a line, then the box it belongs in. One of these boxes takes actions that change nothing about the event itself.',

    bankLabel='Word bank:',
    gapEyebrow='The grammar of risk',
    gapTitleA='Complete the pattern',
    gapHintA='One word per gap. Three of the six are not needed.',
    gapTitleB='Complete the response',
    gapHintB='One verb per gap. Three of the six are not needed &mdash; and two of those three are the ones people reach for by mistake.',

    matEyebrow='Precision',
    matTitle='Match the term to what it actually means',
    matHint='Six terms, six definitions. Three of them are routinely used as if they were interchangeable; they are not.',

    ordEyebrow='Build the sentence',
    ordTitleA='Flagging it early',
    ordHintA='Click the parts in order. Soft delivery, hard content.',
    ordTitleB='A register entry',
    ordHintB='Click the parts in order: cause, event, consequence.',

    qEyebrow='Choose the version that survives being forwarded',
    qTitle='Which one would you actually write?',

    actTitle='Now run the risk review',
    actUse='Use at least four:',
    actSpeakKind='Discussion &middot; in threes',
    actSpeakBrief='Ten minutes. One chairs, one owns the risk, one is the finance director who signs the decision.',
    actSpeak1='You own the cobalt exposure: cause, event, consequence, then one recommended response and one you rejected.',
    actSpeak2='Finance director: the recommendation costs &euro;2m a year. Push back using <em>appetite</em>, <em>tolerance</em> and <em>capacity</em>.',
    actSpeak3='The event has now happened. Same room &mdash; every risk is now an issue. Redo it in ninety seconds.',
    actSpeak4='Argue the other side: when is <em>tolerate</em> the professional answer rather than the lazy one?',
    actWriteKind='Writing &middot; 180&ndash;220 words',
    actWriteBrief='Write the escalation email to the sponsor. Name the cause, the event and the consequence; calibrate the probability instead of hedging it; give the response you recommend and the one you rejected; end with a named owner and a date.',
    actPlaceholder='I want to flag early that…',

    resNext='Recognising the register is the easy half. Now say it to a sponsor →',
    resPerfect='Full marks. You can hear the difference &mdash; saying it out loud to someone who outranks you is the other half.',
    resStrong='Strong. Look again at the ones you missed: most of them turn on a probability word doing more work than it should.',
    resMid='A usable base. Re-read the calibration slide and the four responses before you write anything.',
    resLow='Go back through the six teaching slides. Almost every miss here is a word used as if it were a synonym of another one.',
)

# ── GERMAN ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Risiken <em>steuern</em>',
    coverSub='Gefährdungen benennen, abstufen, verantworten und behandeln — ohne zu übertreiben und ohne zu verschleiern',
    chipLevel='C1&ndash;C2 &middot; Unternehmensrisiko',
    chipFocus='Präzision, Abstufung und Verantwortung',
    chipCount='NSLIDES Folien',

    t1Eyebrow='Die vier Wörter, die ständig vertauscht werden',
    t1Title='<em>Hazard</em>, <em>risk</em>, <em>exposure</em>, <em>issue</em>',
    t1n1='Es existiert, ob es Sie je erreicht oder nicht.',
    t1n2='Sobald es sicher ist, ist es kein Risiko mehr.',
    t1n3='Eine Menge, kein Urteil.',
    t1n4='Es hinterher noch <em>risk</em> zu nennen, klingt nach Hoffen.',

    t2Eyebrow='Drei feste Muster',
    t2Title='<em>a risk of</em>, <em>a risk to</em>, <em>at risk of</em>',
    t2n1='Fragen Sie sich: Was ist das Ereignis?',
    t2n2='Fragen Sie sich: Was nimmt Schaden?',
    t2n3='Nutzen Sie es, wenn das Bedrohte wichtiger ist als das Risiko selbst.',
    t2n4='Alle drei, in der Reihenfolge, die eine Leserin erwartet.',

    t3Eyebrow='Die vier Reaktionen',
    t3Title='Was Sie mit einem Risiko tatsächlich tun können',
    t3n1='Vor den Maßnahmen heißt es <em>inherent risk</em>; was danach übrig bleibt, ist <em>residual risk</em>.',
    t3n2='Das Ereignis tritt trotzdem ein. Nur die Rechnung wandert.',
    t3n3='<em>Tolerate</em> ist eine protokollierte Entscheidung. Ignorieren nicht.',
    t3n4='Die einzige Reaktion, die <em>eliminate</em> ehrlich verwenden darf.',

    t4Eyebrow='Abstufung',
    t4Title='Sagen, wie wahrscheinlich es ist, ohne es zu verstecken',
    t4n1='<em>We may well breach the covenant</em> ist eine Warnung, kein Vielleicht.',
    t4n2='<em>Might just</em> ist schwächer als <em>might</em>, nicht stärker.',
    t4n3='Untertreibung, die eine C2-Leserin als Betonung hört &mdash; und die auf B2-Niveau leicht ganz überhört wird.',

    t5Eyebrow='Drei Wörter, die ein Vorstand nicht verwechselt',
    t5Title='Appetite, tolerance, capacity',
    t5n1='Bewusst gewählt und protokolliert.',
    t5n2='Ein Schwellenwert, der jemanden zum Handeln zwingt, keine Vorliebe.',
    t5n3='Nicht wählbar. Ihre <em>capacity</em> können Sie genau einmal überschreiten.',

    t6Eyebrow='Register',
    t6Title='Was das Passiv verbergen darf &mdash; und was nicht',
    t6n1='Ehrliche Arbeit: berichten, was geschehen ist, bevor man sagen kann, durch wen.',
    t6n2='Eine Entscheidung ohne Entscheider &mdash; es gibt niemanden zu fragen.',
    t6n3='Wenn Sie wissen, wer es war, und der Satz die Person verschweigt: genau das ist das Signal.',

    sortEyebrow='Bevor Sie den Mund aufmachen',
    sortTitleA='Noch bevorstehend oder schon eingetreten?',
    sortHintA='Klicken Sie eine Zeile an und dann das Feld, in das sie gehört. Jedes Paar ist dieselbe Geschichte vor und nach dem Ereignis.',
    sortTitleB='Welche der vier Reaktionen ist das?',
    sortHintB='Klicken Sie eine Zeile an und dann das Feld, in das sie gehört. Eines dieser Felder nimmt Maßnahmen auf, die am Ereignis selbst nichts ändern.',

    bankLabel='Wortliste:',
    gapEyebrow='Die Grammatik des Risikos',
    gapTitleA='Vervollständigen Sie das Muster',
    gapHintA='Ein Wort pro Lücke. Drei der sechs werden nicht gebraucht.',
    gapTitleB='Vervollständigen Sie die Reaktion',
    gapHintB='Ein Verb pro Lücke. Drei der sechs werden nicht gebraucht &mdash; und zwei davon sind genau die, zu denen man versehentlich greift.',

    matEyebrow='Präzision',
    matTitle='Ordnen Sie jedem Begriff zu, was er wirklich bedeutet',
    matHint='Sechs Begriffe, sechs Definitionen. Drei davon werden routinemäßig synonym verwendet; sie sind es nicht.',

    ordEyebrow='Bauen Sie den Satz',
    ordTitleA='Früh Bescheid geben',
    ordHintA='Klicken Sie die Teile der Reihe nach an. Weiche Verpackung, harter Inhalt.',
    ordTitleB='Ein Eintrag im Risikoregister',
    ordHintB='Klicken Sie die Teile der Reihe nach an: Ursache, Ereignis, Folge.',

    qEyebrow='Wählen Sie die Fassung, die eine Weiterleitung übersteht',
    qTitle='Welche würden Sie wirklich schreiben?',

    actTitle='Jetzt führen Sie das Risk Review',
    actUse='Mindestens vier verwenden:',
    actSpeakKind='Diskussion &middot; zu dritt',
    actSpeakBrief='Zehn Minuten. Eine leitet, eine verantwortet das Risiko, eine ist die Finanzchefin, die unterschreibt.',
    actSpeak1='Kobalt-Risiko: Ursache, Ereignis, Folge &mdash; dann eine empfohlene und eine verworfene Reaktion.',
    actSpeak2='Finanzchefin: Die Empfehlung kostet 2 Mio. &euro; im Jahr. Halten Sie mit <em>appetite</em>, <em>tolerance</em> und <em>capacity</em> dagegen.',
    actSpeak3='Das Ereignis ist eingetreten. Jedes <em>risk</em> ist jetzt ein <em>issue</em>. In neunzig Sekunden noch einmal.',
    actSpeak4='Gegenseite: Wann ist <em>tolerate</em> die professionelle Antwort und nicht die bequeme?',
    actWriteKind='Schreiben &middot; 180&ndash;220 Wörter',
    actWriteBrief='Schreiben Sie die Eskalations-E-Mail an die Sponsorin. Nennen Sie Ursache, Ereignis und Folge; stufen Sie die Wahrscheinlichkeit ab, statt sie abzuschwächen; nennen Sie die empfohlene und die verworfene Reaktion; schließen Sie mit Name und Datum.',
    actPlaceholder='I want to flag early that…',

    resNext='Das Register zu erkennen ist die leichte Hälfte. Jetzt sagen Sie es einer Sponsorin →',
    resPerfect='Volle Punktzahl. Sie hören den Unterschied &mdash; ihn jemandem über Ihnen laut zu sagen, ist die andere Hälfte.',
    resStrong='Stark. Sehen Sie sich die Fehler noch einmal an: Meist hängt es an einem Wahrscheinlichkeitswort, das zu viel Arbeit leistet.',
    resMid='Eine brauchbare Grundlage. Lesen Sie die Folie zur Abstufung und die vier Reaktionen noch einmal, bevor Sie schreiben.',
    resLow='Gehen Sie die sechs Erklärungsfolien noch einmal durch. Fast jeder Fehler ist ein Wort, das wie ein Synonym eines anderen benutzt wurde.',
)

# ── SPANISH ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Gestionar el <em>riesgo</em>',
    coverSub='Nombrar la exposición, graduarla, asumirla y actuar — sin exagerar lo que sabes ni ocultar lo que haces',
    chipLevel='C1&ndash;C2 &middot; Riesgo corporativo',
    chipFocus='Precisión, graduación y responsabilidad',
    chipCount='NSLIDES diapositivas',

    t1Eyebrow='Las cuatro palabras que se confunden',
    t1Title='<em>Hazard</em>, <em>risk</em>, <em>exposure</em>, <em>issue</em>',
    t1n1='Existe llegue a alcanzarte o no.',
    t1n2='En cuanto es seguro, deja de ser un riesgo.',
    t1n3='Una cantidad, no un juicio.',
    t1n4='Llamarlo <em>risk</em> después del hecho suena a estar esperando que se arregle.',

    t2Eyebrow='Tres patrones fijos',
    t2Title='<em>a risk of</em>, <em>a risk to</em>, <em>at risk of</em>',
    t2n1='Pregúntate: ¿cuál es el suceso?',
    t2n2='Pregúntate: ¿qué sale dañado?',
    t2n3='Úsalo cuando lo amenazado importa más que el riesgo en sí.',
    t2n4='Los tres, en el orden que espera quien lee.',

    t3Eyebrow='Las cuatro respuestas',
    t3Title='Lo que realmente puedes hacer con un riesgo',
    t3n1='Antes de los controles es <em>inherent risk</em>; lo que queda después es <em>residual risk</em>.',
    t3n2='El suceso ocurre igual. Solo se mueve la factura.',
    t3n3='<em>Tolerate</em> es una decisión que consta en acta. Ignorar, no.',
    t3n4='La única respuesta que puede usar <em>eliminate</em> con honestidad.',

    t4Eyebrow='Graduación',
    t4Title='Decir qué probable es, sin esconderlo',
    t4n1='<em>We may well breach the covenant</em> es un aviso, no un quizá.',
    t4n2='<em>Might just</em> es más débil que <em>might</em>, no más fuerte.',
    t4n3='Atenuación que un lector C2 oye como énfasis &mdash; y que en B2 se pierde entera.',

    t5Eyebrow='Tres palabras que un consejo no confunde',
    t5Title='Appetite, tolerance, capacity',
    t5n1='Elegido de forma deliberada y recogido en acta.',
    t5n2='Un umbral que obliga a actuar, no una preferencia.',
    t5n3='No se elige. Tu <em>capacity</em> puedes superarla una sola vez.',

    t6Eyebrow='Registro',
    t6Title='Lo que la pasiva puede ocultar &mdash; y lo que no',
    t6n1='Trabajo honesto: contar lo ocurrido antes de poder decir por quién.',
    t6n2='Una decisión sin decisor, así que no hay a quién preguntar.',
    t6n3='Si sabes quién fue y la frase lo esconde, ahí está la señal.',

    sortEyebrow='Antes de abrir la boca',
    sortTitleA='¿Todavía por delante o ya ocurrido?',
    sortHintA='Haz clic en una línea y luego en su casilla. Cada pareja es la misma historia a un lado y otro del suceso.',
    sortTitleB='¿Cuál de las cuatro respuestas es esta?',
    sortHintB='Haz clic en una línea y luego en su casilla. Una de estas casillas recoge medidas que no cambian nada del suceso en sí.',

    bankLabel='Banco de palabras:',
    gapEyebrow='La gramática del riesgo',
    gapTitleA='Completa el patrón',
    gapHintA='Una palabra por hueco. Tres de las seis no hacen falta.',
    gapTitleB='Completa la respuesta',
    gapHintB='Un verbo por hueco. Tres de los seis no hacen falta &mdash; y dos de esos tres son justo los que se usan por error.',

    matEyebrow='Precisión',
    matTitle='Empareja cada término con lo que de verdad significa',
    matHint='Seis términos, seis definiciones. Tres se usan habitualmente como si fueran intercambiables; no lo son.',

    ordEyebrow='Construye la frase',
    ordTitleA='Avisar a tiempo',
    ordHintA='Haz clic en las partes en orden. Forma suave, contenido firme.',
    ordTitleB='Una entrada del registro de riesgos',
    ordHintB='Haz clic en las partes en orden: causa, suceso, consecuencia.',

    qEyebrow='Elige la versión que aguanta que la reenvíen',
    qTitle='¿Cuál escribirías de verdad?',

    actTitle='Ahora dirige la revisión de riesgos',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Debate &middot; en grupos de tres',
    actSpeakBrief='Diez minutos. Uno preside, otro responde del riesgo, otro es la directora financiera que firma.',
    actSpeak1='Exposición al cobalto: causa, suceso, consecuencia y una respuesta recomendada frente a otra descartada.',
    actSpeak2='Directora financiera: la recomendación cuesta 2 M&euro; al año. Replica con <em>appetite</em>, <em>tolerance</em> y <em>capacity</em>.',
    actSpeak3='El suceso ya ha ocurrido. Todo <em>risk</em> es ahora un <em>issue</em>. Repítelo en noventa segundos.',
    actSpeak4='Postura contraria: ¿cuándo es <em>tolerate</em> la respuesta profesional y no la cómoda?',
    actWriteKind='Escritura &middot; 180&ndash;220 palabras',
    actWriteBrief='Escribe el correo de escalado a la patrocinadora. Nombra la causa, el suceso y la consecuencia; gradúa la probabilidad en vez de atenuarla; indica la respuesta que recomiendas y la que descartaste; termina con un responsable y una fecha.',
    actPlaceholder='I want to flag early that…',

    resNext='Reconocer el registro es la mitad fácil. Ahora díselo a una patrocinadora →',
    resPerfect='Puntuación perfecta. Oyes la diferencia &mdash; decírsela en voz alta a alguien por encima de ti es la otra mitad.',
    resStrong='Muy bien. Vuelve a mirar los fallos: casi todos dependen de una palabra de probabilidad que hace más trabajo del que debería.',
    resMid='Una base aprovechable. Relee la diapositiva de graduación y las cuatro respuestas antes de escribir nada.',
    resLow='Vuelve a las seis diapositivas de explicación. Casi todo fallo aquí es una palabra usada como si fuera sinónimo de otra.',
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
