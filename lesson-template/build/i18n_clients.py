# -*- coding: utf-8 -*-
"""Interface strings for Talking with Clients (B2), English and German."""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Talking with <em>Clients</em>',
    coverSub='Meetings, calls and negotiations — and the register that holds them together',
    chipLevel='B2 · Professional English', chipFocus='Client communication',
    chipCount='14 slides',
    movesEyebrow='Before the questions',
    movesTitle='Four moves that carry a client conversation',
    mv1h='1 · Acknowledge first',
    mv1b='Say what you heard before you say what you think. Skipping this is what makes a correct answer land badly.',
    mv2h='2 · Soften the refusal',
    mv2b='<em>I’m afraid</em> costs nothing and changes everything. A bare <em>no</em> reads as a door closing.',
    mv3h='3 · Offer something',
    mv3b='Every refusal needs a second half. Without one you have ended the conversation, not answered it.',
    mv4h='4 · Confirm the action',
    mv4b='Who does what, by when. <em>At some point</em> and <em>fairly soon</em> are not commitments.',
    tempEyebrow='Register', tempTitle='The same refusal at three temperatures',
    t1h='Too cold',
    t1b='True, and the relationship is now over. A policy is not an answer to a person.',
    t2h='About right',
    t2b='Refuses clearly, then opens a door. The client can still say yes to something.',
    t3h='Too warm',
    t3b='Agreeing to everything is not service. It tells the client you had no view in the first place.',
    qEyebrow='In front of the client', qTitle='What do you say?',
    gapEyebrow='The exact word', gapTitle='Business English runs on collocation',
    gapHint='Five of the ten words in the bank belong to no gap here.',
    bankLabel='Word bank:',
    matchEyebrow='Office idiom', matchTitle='Five phrases nobody ever explains to you',
    matchHint='Click a phrase, then click what it means.',
    actTitle='Handle the difficult client', actUse='Use at least four:',
    actWriteKind='Writing · 120–160 words',
    actSpeakBrief='One of you is the client and is not in a good mood. Swap after each round.',
    actSpeak1='The client is confused about the timeline. Explain it without sending them back to the brief.',
    actSpeak2='They ask for a 20% discount. Refuse, and keep them talking.',
    actSpeak3='They propose something you think is wrong. Disagree without saying no.',
    actSpeak4='Close the meeting so that both of you leave holding something specific.',
    actWriteBrief='A long-standing client writes that your response times have slipped and they are questioning the partnership. Reply.',
    actPlaceholder='Dear Ms Okafor,',
    resPerfect='Full marks. You can refuse, disagree and close without ever sounding cold or weak.',
    resStrong='Strong. The collocations are secure — the register slide is what rewards another pass.',
    resMid='A good base. Look again at the four moves; most of the misses come from skipping the first one.',
    resLow='Read the two opening slides again, then run it once more. Acknowledge first, always.',
)

T['de'] = dict(
    coverTitle='Gespräche mit <em>Kunden</em>',
    coverSub='Meetings, Anrufe und Verhandlungen — und das Register, das sie zusammenhält',
    chipLevel='B2 · Berufsenglisch', chipFocus='Kundenkommunikation',
    chipCount='14 Folien',
    movesEyebrow='Vor den Aufgaben',
    movesTitle='Vier Schritte, die ein Kundengespräch tragen',
    mv1h='1 · Zuerst bestätigen',
    mv1b='Sagen Sie, was Sie gehört haben, bevor Sie sagen, was Sie denken. Wer das überspringt, wirkt selbst mit der richtigen Antwort schroff.',
    mv2h='2 · Die Absage abfedern',
    mv2b='<em>I’m afraid</em> kostet nichts und verändert alles. Ein nacktes <em>no</em> klingt wie eine zufallende Tür.',
    mv3h='3 · Etwas anbieten',
    mv3b='Jede Absage braucht eine zweite Hälfte. Ohne sie haben Sie das Gespräch beendet, nicht beantwortet.',
    mv4h='4 · Die Handlung festhalten',
    mv4b='Wer macht was, bis wann. <em>At some point</em> und <em>fairly soon</em> sind keine Zusagen.',
    tempEyebrow='Register', tempTitle='Dieselbe Absage in drei Temperaturen',
    t1h='Zu kalt',
    t1b='Sachlich richtig — und die Beziehung ist beendet. Eine Richtlinie ist keine Antwort an einen Menschen.',
    t2h='Genau richtig',
    t2b='Sagt klar ab und öffnet dann eine Tür. Die Kundschaft kann immer noch zu etwas Ja sagen.',
    t3h='Zu warm',
    t3b='Allem zuzustimmen ist kein Service. Es sagt der Kundschaft, dass Sie von vornherein keine Haltung hatten.',
    qEyebrow='Vor der Kundschaft', qTitle='Was sagen Sie?',
    gapEyebrow='Das genaue Wort', gapTitle='Berufsenglisch lebt von Kollokationen',
    gapHint='Fünf der zehn Wörter in der Liste gehören in keine dieser Lücken.',
    bankLabel='Wortliste:',
    matchEyebrow='Büro-Wendung', matchTitle='Fünf Wendungen, die Ihnen niemand erklärt',
    matchHint='Klicken Sie auf eine Wendung und dann auf ihre Bedeutung.',
    actTitle='Die schwierige Kundschaft bedienen', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 120–160 Wörter',
    actSpeakBrief='Eine Person ist die Kundschaft und schlecht gelaunt. Nach jeder Runde tauschen.',
    actSpeak1='Die Kundschaft versteht den Zeitplan nicht. Erklären Sie ihn, ohne auf das Briefing zu verweisen.',
    actSpeak2='Sie fordert 20 % Rabatt. Lehnen Sie ab und halten Sie das Gespräch offen.',
    actSpeak3='Sie schlägt etwas vor, das Sie für falsch halten. Widersprechen Sie, ohne Nein zu sagen.',
    actSpeak4='Beenden Sie das Meeting so, dass beide Seiten etwas Konkretes in der Hand haben.',
    actWriteBrief='Eine langjährige Kundin schreibt, Ihre Reaktionszeiten hätten nachgelassen, und stellt die Zusammenarbeit infrage. Antworten Sie.',
    actPlaceholder='Dear Ms Okafor,',
    resPerfect='Volle Punktzahl. Sie können absagen, widersprechen und abschließen, ohne kalt oder schwach zu klingen.',
    resStrong='Stark. Die Kollokationen sitzen — die Registerfolie lohnt einen zweiten Durchgang.',
    resMid='Eine gute Grundlage. Sehen Sie sich die vier Schritte noch einmal an; die meisten Fehler entstehen, weil der erste fehlt.',
    resLow='Lesen Sie die beiden Einstiegsfolien noch einmal und starten Sie neu. Immer zuerst bestätigen.',
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
