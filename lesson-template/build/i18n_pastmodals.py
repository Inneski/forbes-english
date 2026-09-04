# -*- coding: utf-8 -*-
"""Interface strings for Past Modals in Minecraft (B2), English and German."""
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
}

T = {}

T['en'] = dict(
    coverTitle='Past <em>Modals</em>',
    coverSub='What you should have done, what you could have done, and how you know',
    chipLevel='B2 · Upper-intermediate', chipFocus='Modals + have + past participle',
    chipCount='16 slides',

    formEyebrow='Before the questions', formTitle='One shape, five jobs',
    fo1h='The shape never changes', fo1b=
        'Every one of these is <strong>modal + have + past participle</strong>. The '
        'modal carries the meaning; <em>have + p.p.</em> only says that we are talking '
        'about the past.',
    fo1n='<em>Have</em> never becomes <em>had</em> here, whoever the subject is.',
    fo2h='Looking back at a mistake', fo2b=
        '<strong>Should have</strong> is advice given too late: the right thing did not '
        'happen. <strong>Could have</strong> is the chance that existed and was not '
        'taken.',
    fo2n='Both point at a past that could have gone differently. Only <em>should</em> blames.',
    fo3h='Working out what happened', fo3b=
        '<strong>Must have</strong> is near-certainty from evidence. <strong>Might '
        'have</strong> is a guess. <strong>Needn&rsquo;t have</strong> says it was done '
        'and was not needed.',
    fo3n='<em>Needn&rsquo;t have</em> is the one learners miss: the action <em>did</em> happen.',

    sureEyebrow='The deduction pair', sureTitle='How certain are you?',
    su1h='Almost certain', su1b=
        '<strong>Must have.</strong> There are footprints round the chest, so the thief '
        '<em>must have</em> been here. You did not see it; the evidence leaves little '
        'room for anything else.',
    su1n='Roughly 90% or more. Not proof — a conclusion.',
    su2h='One possibility of several', su2b=
        '<strong>Might have</strong> or <strong>could have.</strong> Nobody saw who broke '
        'the bridge, so it <em>might have</em> been a griefer. It is a guess, offered as '
        'a guess.',
    su2n='Under 50%. <em>May have</em> is the same idea in a more formal register.',
    su3h='The negative flips', su3b=
        'For a confident negative, English uses <strong>can&rsquo;t have</strong>, not '
        '<em>mustn&rsquo;t have</em>: <em>she can&rsquo;t have finished already</em>.',
    su3n='<em>Mustn&rsquo;t have</em> is one of the commonest B2 errors, and it is not English.',

    regEyebrow='The regret pair', regTitle='The past that did not happen',
    re1h='Should have', re1b=
        '<em>You <strong>should have</strong> built the walls higher.</em> The right '
        'action, identified afterwards. It carries criticism, so it lands hard.',
    re1n='<em>Shouldn&rsquo;t have</em> criticises something that <em>was</em> done.',
    re2h='Could have', re2b=
        '<em>You <strong>could have</strong> used the Elytra.</em> The ability or the '
        'opportunity was there and went unused. No blame attached.',
    re2n='It also softens a suggestion: <em>you could have asked me</em> is gentler than <em>should</em>.',
    re3h='Needn&rsquo;t have', re3b=
        '<em>He <strong>needn&rsquo;t have</strong> walked &mdash; there was a horse.</em> '
        'He walked. It was wasted effort. The action happened.',
    re3n='Compare <em>didn&rsquo;t need to walk</em>, which usually means he did not walk at all.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='Choose the modal that fits',
    m1why='<strong>Should have put.</strong> Advice or criticism after the fact &mdash; '
          'storing the diamonds was the right thing to do, and it did not happen.',
    m2why='<strong>Must have built.</strong> Torches and smooth walls are evidence, and '
          'Steve is drawing a confident conclusion from it. That is deduction, not '
          'obligation.',
    m3why='<strong>Could have destroyed.</strong> The explosion had the power to destroy '
          'everything and did not. A past possibility that went unrealised.',
    m4why='<strong>Needn&rsquo;t have bothered.</strong> Leo did collect the wood; it was '
          'simply unnecessary. <em>Shouldn&rsquo;t have</em> would make it a mistake '
          'rather than wasted effort, and <em>mustn&rsquo;t have</em> is not English.',
    m5why='<strong>Might have been.</strong> Nobody saw it, so this is an uncertain guess '
          '&mdash; one explanation among several, offered as such.',

    fibEyebrow='Activity 2 · The exact form', fibTitle='Complete the sentence',
    fibHint='Two words each time: a modal, then <em>have</em>.',
    f1why='<strong>Should have prepared.</strong> Regret and criticism about a past '
          'action that was the right one and did not happen.',
    f2why='<strong>Could have found.</strong> Alex had the map, so the opportunity '
          'existed. She did not use it. Ability or chance, unrealised.',
    f3why='<strong>Needn&rsquo;t have walked.</strong> He walked &mdash; that is the '
          'point. The horse made it unnecessary, but the walking happened.',
    f4why='<strong>Must have been.</strong> The footprints are the evidence, and the '
          'conclusion follows from them with near-certainty.',
    f5why='<strong>Might have caused.</strong> Nobody knows, so the flood is offered as '
          'one possible explanation rather than the answer.',

    matchEyebrow='Activity 3 · Meaning', matchTitle='Match the sentence to what it does',
    matchHint='Click a sentence, then click what it means.',
    matchWhy='Five modals, five jobs: deduction, criticism, wasted effort, a guess, and '
             'an unused opportunity. The form is identical in all five &mdash; only the '
             'modal tells you which one you are reading.',

    actTitle='Account for the disaster', actUse='Use at least four:',
    actSpeakBrief='One of you runs the server and wants to know what happened. The other '
                  'was there. Four minutes each, then swap.',
    actSpeak1='The base was destroyed overnight. Say what happened and how sure you are.',
    actSpeak2='Your partner blames you. Say what you could have done, without conceding a mistake.',
    actSpeak3='Describe something you needn’t have done last week.',
    actSpeak4='Give three deductions, each more confident than the last.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write the incident report a server admin would post after the raid. '
                  'Say what must have happened, what might have happened, and what the '
                  'team should have done — and keep the three levels of certainty '
                  'distinct.',
    actPlaceholder='From the state of the east wall, the raiders must have…',

    resPerfect='Full marks. You can place a past action on the scale from guess to certainty.',
    resStrong='Strong. The regret pair is secure — check the deduction pair once more.',
    resMid='Good base. Go back to the certainty slide: most misses are must/might.',
    resLow='Read the three opening slides again. The form never changes; only the modal does.',
)

T['de'] = dict(
    coverTitle='Modalverben der <em>Vergangenheit</em>',
    coverSub='Was du hättest tun sollen, was du hättest tun können — und woher du es weißt',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Modalverb + have + Partizip II',
    chipCount='16 Folien',

    formEyebrow='Vor den Fragen', formTitle='Eine Form, fünf Aufgaben',
    fo1h='Die Form ändert sich nie', fo1b=
        'Alle heißen <strong>modal + have + past participle</strong>. Das Modalverb trägt '
        'die Bedeutung; <em>have + Partizip II</em> sagt nur, dass es um die Vergangenheit '
        'geht.',
    fo1n='<em>Have</em> wird hier nie zu <em>had</em>, egal welches Subjekt.',
    fo2h='Rückblick auf einen Fehler', fo2b=
        '<strong>Should have</strong> ist ein Rat, der zu spät kommt: Das Richtige ist '
        'nicht passiert. <strong>Could have</strong> ist die Chance, die es gab und die '
        'ungenutzt blieb.',
    fo2n='Beide zeigen auf eine Vergangenheit, die anders hätte laufen können. Nur <em>should</em> wirft etwas vor.',
    fo3h='Herausfinden, was geschah', fo3b=
        '<strong>Must have</strong> ist nahezu Gewissheit aus Indizien. <strong>Might '
        'have</strong> ist eine Vermutung. <strong>Needn&rsquo;t have</strong> heißt: Es '
        'wurde getan und war unnötig.',
    fo3n='<em>Needn&rsquo;t have</em> wird oft übersehen: Die Handlung <em>ist</em> passiert.',

    sureEyebrow='Das Deduktionspaar', sureTitle='Wie sicher bist du?',
    su1h='Fast sicher', su1b=
        '<strong>Must have.</strong> Rund um die Truhe sind Fußspuren, also <em>must '
        'have</em> der Dieb hier gewesen sein. Du hast es nicht gesehen; die Indizien '
        'lassen kaum etwas anderes zu.',
    su1n='Etwa 90% und mehr. Kein Beweis — eine Schlussfolgerung.',
    su2h='Eine Möglichkeit von mehreren', su2b=
        '<strong>Might have</strong> oder <strong>could have.</strong> Niemand hat gesehen, '
        'wer die Brücke zerstört hat, also <em>might have</em> es ein Griefer gewesen sein. '
        'Eine Vermutung, als Vermutung gesagt.',
    su2n='Unter 50%. <em>May have</em> ist dasselbe in förmlicherem Register.',
    su3h='Die Verneinung kippt', su3b=
        'Für eine sichere Verneinung nimmt das Englische <strong>can&rsquo;t have</strong>, '
        'nicht <em>mustn&rsquo;t have</em>: <em>she can&rsquo;t have finished already</em>.',
    su3n='<em>Mustn&rsquo;t have</em> ist einer der häufigsten B2-Fehler — und kein Englisch.',

    regEyebrow='Das Bedauernspaar', regTitle='Die Vergangenheit, die nicht stattfand',
    re1h='Should have', re1b=
        '<em>You <strong>should have</strong> built the walls higher.</em> Die richtige '
        'Handlung, im Nachhinein erkannt. Das enthält Kritik und kommt entsprechend an.',
    re1n='<em>Shouldn&rsquo;t have</em> kritisiert etwas, das <em>getan wurde</em>.',
    re2h='Could have', re2b=
        '<em>You <strong>could have</strong> used the Elytra.</em> Die Fähigkeit oder die '
        'Gelegenheit war da und blieb ungenutzt. Ohne Vorwurf.',
    re2n='Es mildert auch einen Vorschlag: <em>you could have asked me</em> klingt sanfter als <em>should</em>.',
    re3h='Needn&rsquo;t have', re3b=
        '<em>He <strong>needn&rsquo;t have</strong> walked &mdash; there was a horse.</em> '
        'Er ist gelaufen. Vergebliche Mühe. Die Handlung hat stattgefunden.',
    re3n='Vergleiche <em>didn&rsquo;t need to walk</em> — das heißt meist, er ist gar nicht gelaufen.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Wähle das passende Modalverb',
    m1why='<strong>Should have put.</strong> Rat oder Kritik im Nachhinein — die Diamanten '
          'wegzuschließen wäre richtig gewesen und ist nicht passiert.',
    m2why='<strong>Must have built.</strong> Fackeln und glatte Wände sind Indizien, und '
          'Steve zieht daraus einen sicheren Schluss. Deduktion, keine Verpflichtung.',
    m3why='<strong>Could have destroyed.</strong> Die Explosion hätte alles zerstören '
          'können und tat es nicht. Eine Möglichkeit, die sich nicht erfüllt hat.',
    m4why='<strong>Needn&rsquo;t have bothered.</strong> Leo hat das Holz gesammelt; es war '
          'nur unnötig. <em>Shouldn&rsquo;t have</em> machte daraus einen Fehler statt '
          'vergeblicher Mühe, und <em>mustn&rsquo;t have</em> gibt es nicht.',
    m5why='<strong>Might have been.</strong> Niemand hat es gesehen, also eine unsichere '
          'Vermutung — eine Erklärung von mehreren.',

    fibEyebrow='Aufgabe 2 · Die genaue Form', fibTitle='Vervollständige den Satz',
    fibHint='Jeweils zwei Wörter: ein Modalverb, dann <em>have</em>.',
    f1why='<strong>Should have prepared.</strong> Bedauern und Kritik über eine richtige '
          'Handlung, die ausblieb.',
    f2why='<strong>Could have found.</strong> Alex hatte die Karte, die Gelegenheit war da. '
          'Sie hat sie nicht genutzt.',
    f3why='<strong>Needn&rsquo;t have walked.</strong> Er ist gelaufen — genau darum geht '
          'es. Das Pferd machte es unnötig, aber gelaufen ist er.',
    f4why='<strong>Must have been.</strong> Die Fußspuren sind das Indiz, und der Schluss '
          'folgt daraus mit hoher Sicherheit.',
    f5why='<strong>Might have caused.</strong> Niemand weiß es, also wird die Flut als eine '
          'mögliche Erklärung angeboten, nicht als die Antwort.',

    matchEyebrow='Aufgabe 3 · Bedeutung', matchTitle='Ordne dem Satz seine Funktion zu',
    matchHint='Klicke einen Satz an, dann seine Bedeutung.',
    matchWhy='Fünf Modalverben, fünf Aufgaben: Deduktion, Kritik, vergebliche Mühe, '
             'Vermutung und eine ungenutzte Gelegenheit. Die Form ist in allen fünf '
             'gleich — nur das Modalverb sagt, welche gemeint ist.',

    actTitle='Erkläre die Katastrophe', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer leitet den Server und will wissen, was passiert ist. Der andere '
                  'war dabei. Je vier Minuten, dann tauschen.',
    actSpeak1='Die Basis wurde über Nacht zerstört. Sag, was passiert ist und wie sicher du bist.',
    actSpeak2='Dein Partner gibt dir die Schuld. Sag, was du anders hättest machen können.',
    actSpeak3='Beschreibe etwas, das du letzte Woche nicht hättest tun müssen.',
    actSpeak4='Nenne drei Schlussfolgerungen, jede sicherer als die vorige.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreibe den Vorfallsbericht, den ein Server-Admin nach dem Überfall '
                  'posten würde. Sag, was passiert sein muss, was passiert sein könnte und '
                  'was das Team hätte tun sollen — und halte die drei Sicherheitsgrade '
                  'auseinander.',
    actPlaceholder='From the state of the east wall, the raiders must have…',

    resPerfect='Volle Punktzahl. Du kannst eine vergangene Handlung zwischen Vermutung und Gewissheit einordnen.',
    resStrong='Stark. Das Bedauernspaar sitzt — sieh dir das Deduktionspaar noch einmal an.',
    resMid='Gute Grundlage. Zurück zur Sicherheits-Folie: die meisten Fehler sind must/might.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Die Form ändert sich nie, nur das Modalverb.',
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
