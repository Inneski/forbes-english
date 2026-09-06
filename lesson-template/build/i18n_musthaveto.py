# -*- coding: utf-8 -*-
"""Interface strings for Must & Have To — Minecraft Edition (A2).

English, German and Spanish. Teach-card bodies use the six-item form so the
rule travels with its heading; the English being taught stays English.
MC/gap explanations are keys (mc1why, g1why…) rather than literal text, so
they translate with everything else — this is an A2 deck and a learner who
cannot yet read the explanation has not been taught anything by it.
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
    coverTitle='Must &amp; <em>Have To</em>',
    coverSub='Two ways to say you have no choice &mdash; and why the game '
             'keeps testing the difference',
    chipLevel='A2 &middot; Elementary', chipFocus='must vs have to &amp; the negative trap',
    chipCount='16 slides',

    rwEyebrow='Before you play', rwTitle='Whose rule is it?',
    rw1h="MUST &mdash; it's your own idea",
    rw1b='Use <strong>must</strong> when the obligation comes from you '
         '&mdash; your own opinion, feeling or decision. <em>I must save my '
         'progress before I log off.</em>',
    rw1n='<em>Must you&hellip;?</em> sounds very formal in a question. '
         '<em>Do you have to&hellip;?</em> is what people actually say.',
    rw2h="HAVE TO &mdash; someone else's rule",
    rw2b='Use <strong>have to</strong> when the obligation comes from outside '
         'you &mdash; a rule, a law, another person. <em>In survival mode '
         'you have to eat, or your health drops.</em>',
    rw2n='<strong>Has to</strong> for he / she / it: <em>Steve has to sleep '
         'before morning.</em>',

    trEyebrow='The trap', trTitle="Mustn't is not the opposite of must",
    tr1h="MUSTN'T &mdash; forbidden",
    tr1b="<strong>Mustn't</strong> means it is forbidden &mdash; do not do "
         "this. <em>You mustn't dig straight down; lava might be "
         "waiting.</em>",
    tr1n='A warning sign uses <em>mustn&rsquo;t</em>, never <em>don&rsquo;t '
         'have to</em>.',
    tr2h="DON'T HAVE TO &mdash; no obligation",
    tr2b="<strong>Don't have to</strong> means there's no obligation "
         "&mdash; you can if you want, but nothing forces you. <em>In "
         "creative mode you don't have to mine for resources.</em>",
    tr2n='Opposites in meaning, not just in form. Confusing these two is the '
         'single most common mistake with this grammar.',

    pfEyebrow='Other times', pfTitle='Must has no past &mdash; and no future',
    pf1h='HAD TO &mdash; the past',
    pf1b="<strong>Must</strong> doesn't change for the past. Use "
         "<strong>had to</strong> instead. <em>I had to respawn three times "
         "last night.</em>",
    pf1n='Same for questions and negatives: <em>Did you have to fight it '
         'alone?</em>',
    pf2h='WILL HAVE TO &mdash; the future',
    pf2b='For an obligation that starts later, use <strong>will have '
         'to</strong>. <em>After this update, you will have to find a new '
         'seed.</em>',
    pf2n='Never <em>will must</em> &mdash; two modal-like forms never stack.',

    mcEyebrow='Activity 1 &middot; Which form?', mcTitle='Choose the correct word',
    mc1why="<strong>Must</strong> &mdash; this is Steve's own urgent feeling, "
           'not a rule anyone gave him.',
    mc2why='<strong>Have to</strong> &mdash; this comes from the server rules, '
           "not from the player's own feelings.",
    mc3why="<strong>Mustn't</strong> &mdash; this is a prohibition. Entering "
           'without light is forbidden, not just unwise.',
    mc4why="<strong>Don't have to</strong> &mdash; there's no obligation to "
           'collect wood, though you still could if you wanted to. It '
           "isn't forbidden, so <em>are not allowed to</em> and "
           "<em>mustn't</em> are both wrong.",
    mc5why="<strong>Had to</strong> &mdash; this happened in the past, and "
           '<em>must</em> has no past form.',
    mc6why='<strong>Has to</strong> &mdash; third person (she) plus an '
           "external requirement set by the quest, not Alex's own idea.",

    gapEyebrow='Activity 2 &middot; Type it in', gapTitle='Complete the sentence',
    gapHint='Contractions and full forms are both fine &mdash; '
            '<em>mustn&rsquo;t</em> or <em>must not</em>, either works.',
    g1why='Prohibition &mdash; a firm &ldquo;no&rdquo;, not a missing '
          'obligation.',
    g2why='External requirement (the game mode&rsquo;s own rule) plus third '
          'person.',
    g3why='Past obligation &mdash; <em>must</em> has no past form of its own.',
    g4why='No obligation, not a prohibition &mdash; you still could gather '
          'resources if you wanted to.',
    g5why="Internal obligation &mdash; this is the speaker's own feeling, "
          'not an outside rule.',
    g6why='An external rule that applies to everyone &mdash; not the '
          "player's personal feeling.",

    matchEyebrow='Activity 3 &middot; The six forms',
    matchTitle='Match the form to what it means',
    matchHint='Click a form, then click what it means.',
    matchWhy='All six describe an obligation, but the source (you, or '
             'outside you), the direction (required, or forbidden) and the '
             'time (past, present, future) are each different. That '
             'three-way split is the whole grammar point.',

    actTitle='Explain the rules of your world', actUse='Use at least four:',
    actSpeakBrief='One of you is an experienced player explaining the rules '
                  'to someone brand new. Two minutes each, then swap.',
    actSpeak1='Tell your partner three things a new player must do in their '
              'first ten minutes.',
    actSpeak2="Warn your partner about two things they mustn't do, and "
              'explain why.',
    actSpeak3="Say one thing you don't have to do in easy mode, and one "
              'thing you do have to do.',
    actSpeak4='Describe something that happened to you in a game and explain '
              'what you had to do about it.',
    actWriteKind='Writing &middot; 100&ndash;130 words',
    actWriteBrief='Write a short survival guide for a new player joining your '
                  'favourite game or world. Say what they must do, what they '
                  "mustn't do, and what they don't have to worry about. Use "
                  'at least one sentence with <em>had to</em>, about '
                  'something that has already happened to you.',
    actPlaceholder='The first thing you have to do is…',

    resPerfect='Perfect score. You know exactly whose rule it is, every '
               'time.',
    resStrong="Very good. Look again at <em>mustn't</em> versus <em>don't "
              'have to</em> &mdash; that trap costs the last point most '
              'often.',
    resMid='Good foundation. Go back to the first two slides: ask '
           '<em>whose</em> rule it is before you pick a form.',
    resLow='Reread the three teaching slides. Three questions &mdash; you, '
           'or someone else? required, or forbidden? now, past, or future? '
           '&mdash; and the rest is vocabulary.',
)

T['de'] = dict(
    coverTitle='Must &amp; <em>Have To</em>',
    coverSub='Zwei Wege zu sagen, dass du keine Wahl hast &mdash; und warum '
             'das Spiel den Unterschied ständig abfragt',
    chipLevel='A2 &middot; Grundstufe',
    chipFocus='must vs. have to &amp; die Verneinungsfalle',
    chipCount='16 Folien',

    rwEyebrow='Bevor du spielst', rwTitle='Wessen Regel ist das?',
    rw1h='MUST &mdash; deine eigene Idee',
    rw1b='Benutze <strong>must</strong>, wenn die Verpflichtung von dir selbst '
         'kommt &mdash; deine eigene Meinung, dein Gefühl oder deine '
         'Entscheidung. <em>I must save my progress before I log off.</em>',
    rw1n='<em>Must you&hellip;?</em> klingt in einer Frage sehr förmlich. '
         '<em>Do you have to&hellip;?</em> ist das, was man wirklich sagt.',
    rw2h='HAVE TO &mdash; die Regel eines anderen',
    rw2b='Benutze <strong>have to</strong>, wenn die Verpflichtung von außen '
         'kommt &mdash; eine Regel, ein Gesetz, eine andere Person. <em>In '
         'survival mode you have to eat, or your health drops.</em>',
    rw2n='<strong>Has to</strong> für he / she / it: <em>Steve has to sleep '
         'before morning.</em>',

    trEyebrow='Die Falle', trTitle='Mustn&rsquo;t ist nicht das Gegenteil von must',
    tr1h='MUSTN&rsquo;T &mdash; verboten',
    tr1b="<strong>Mustn't</strong> bedeutet, dass etwas verboten ist &mdash; "
         "tu das nicht. <em>You mustn't dig straight down; lava might be "
         "waiting.</em>",
    tr1n='Ein Warnschild benutzt <em>mustn&rsquo;t</em>, niemals <em>don&rsquo;t '
         'have to</em>.',
    tr2h='DON&rsquo;T HAVE TO &mdash; keine Verpflichtung',
    tr2b="<strong>Don't have to</strong> bedeutet, dass keine Verpflichtung "
         "besteht &mdash; du kannst, wenn du willst, aber nichts zwingt "
         "dich. <em>In creative mode you don't have to mine for "
         "resources.</em>",
    tr2n='Gegensätze in der Bedeutung, nicht nur in der Form. Diese beiden '
         'zu verwechseln ist der häufigste Fehler bei dieser Grammatik.',

    pfEyebrow='Andere Zeiten', pfTitle='Must hat keine Vergangenheit &mdash; und keine Zukunft',
    pf1h='HAD TO &mdash; die Vergangenheit',
    pf1b='<strong>Must</strong> ändert sich nicht für die Vergangenheit. '
         'Benutze stattdessen <strong>had to</strong>. <em>I had to respawn '
         'three times last night.</em>',
    pf1n='Genauso bei Fragen und Verneinungen: <em>Did you have to fight it '
         'alone?</em>',
    pf2h='WILL HAVE TO &mdash; die Zukunft',
    pf2b='Für eine Verpflichtung, die erst später beginnt, benutze '
         '<strong>will have to</strong>. <em>After this update, you will '
         'have to find a new seed.</em>',
    pf2n='Niemals <em>will must</em> &mdash; zwei modalähnliche Formen '
         'stehen nie zusammen.',

    mcEyebrow='Aktivität 1 &middot; Welche Form?', mcTitle='Wähle das richtige Wort',
    mc1why='<strong>Must</strong> &mdash; das ist Steves eigenes dringendes '
           'Gefühl, keine Regel, die ihm jemand gegeben hat.',
    mc2why='<strong>Have to</strong> &mdash; das kommt von den '
           'Serverregeln, nicht von den Gefühlen des Spielers.',
    mc3why="<strong>Mustn't</strong> &mdash; das ist ein Verbot. Ohne Licht "
           'hineinzugehen ist verboten, nicht nur unklug.',
    mc4why="<strong>Don't have to</strong> &mdash; es besteht keine "
           'Verpflichtung, Holz zu sammeln, auch wenn man es könnte. Es ist '
           "nicht verboten, also sind <em>are not allowed to</em> und "
           "<em>mustn't</em> beide falsch.",
    mc5why='<strong>Had to</strong> &mdash; das ist in der Vergangenheit '
           'passiert, und <em>must</em> hat keine Vergangenheitsform.',
    mc6why='<strong>Has to</strong> &mdash; dritte Person (she) plus eine '
           'äußere Anforderung der Quest, nicht Alex&rsquo; eigene Idee.',

    gapEyebrow='Aktivität 2 &middot; Trag es ein', gapTitle='Vervollständige den Satz',
    gapHint='Kurz- und Vollformen sind beide richtig &mdash; '
            '<em>mustn&rsquo;t</em> oder <em>must not</em>, beides '
            'funktioniert.',
    g1why='Verbot &mdash; ein klares &bdquo;nein&ldquo;, keine fehlende '
          'Verpflichtung.',
    g2why='Äußere Anforderung (die Regel des Spielmodus) plus dritte '
          'Person.',
    g3why='Verpflichtung in der Vergangenheit &mdash; <em>must</em> hat '
          'keine eigene Vergangenheitsform.',
    g4why='Keine Verpflichtung, kein Verbot &mdash; man könnte trotzdem '
          'Rohstoffe sammeln, wenn man wollte.',
    g5why='Innere Verpflichtung &mdash; das ist das eigene Gefühl des '
          'Sprechers, keine äußere Regel.',
    g6why='Eine äußere Regel, die für alle gilt &mdash; kein persönliches '
          'Gefühl des Spielers.',

    matchEyebrow='Aktivität 3 &middot; Die sechs Formen',
    matchTitle='Ordne die Form ihrer Bedeutung zu',
    matchHint='Klicke auf eine Form und dann auf ihre Bedeutung.',
    matchWhy='Alle sechs beschreiben eine Verpflichtung, aber die Quelle '
             '(du selbst, oder von außen), die Richtung (verpflichtend, '
             'oder verboten) und die Zeit (Vergangenheit, Gegenwart, '
             'Zukunft) sind jeweils unterschiedlich. Diese dreifache '
             'Unterscheidung ist der ganze Grammatikpunkt.',

    actTitle='Erkläre die Regeln deiner Welt', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer von euch ist ein erfahrener Spieler, der einem '
                  'völligen Neuling die Regeln erklärt. Zwei Minuten pro '
                  'Person, dann wechselt ihr.',
    actSpeak1='Nenne deinem Partner drei Dinge, die ein neuer Spieler in '
              'den ersten zehn Minuten tun muss.',
    actSpeak2='Warne deinen Partner vor zwei Dingen, die er nicht tun darf, '
              'und erkläre warum.',
    actSpeak3='Nenne eine Sache, die du im leichten Modus nicht tun musst, '
              'und eine, die du tun musst.',
    actSpeak4='Beschreibe etwas, das dir in einem Spiel passiert ist, und '
              'erkläre, was du deswegen tun musstest.',
    actWriteKind='Schreiben &middot; 100&ndash;130 Wörter',
    actWriteBrief='Schreibe einen kurzen Überlebensleitfaden für einen neuen '
                  'Spieler in deinem Lieblingsspiel. Sag, was er tun muss, '
                  'was er nicht tun darf, und worüber er sich keine Sorgen '
                  'machen muss. Benutze mindestens einen Satz mit <em>had '
                  'to</em>, über etwas, das dir schon passiert ist.',
    actPlaceholder='The first thing you have to do is…',

    resPerfect='Perfekte Punktzahl. Du weißt jedes Mal genau, wessen Regel '
               'es ist.',
    resStrong='Sehr gut. Schau dir <em>mustn&rsquo;t</em> und <em>don&rsquo;t '
              'have to</em> noch einmal an &mdash; diese Falle kostet am '
              'häufigsten den letzten Punkt.',
    resMid='Gute Grundlage. Geh zurück zu den ersten beiden Folien: frag '
           'zuerst, <em>wessen</em> Regel es ist, bevor du eine Form '
           'wählst.',
    resLow='Lies die drei Lehrfolien noch einmal. Drei Fragen &mdash; du, '
           'oder jemand anderes? verpflichtend, oder verboten? jetzt, '
           'Vergangenheit, oder Zukunft? &mdash; der Rest ist Wortschatz.',
)

T['es'] = dict(
    coverTitle='Must &amp; <em>Have To</em>',
    coverSub='Dos formas de decir que no tienes elección &mdash; y por qué '
             'el juego no deja de poner a prueba la diferencia',
    chipLevel='A2 &middot; Elemental',
    chipFocus='must vs. have to &amp; la trampa negativa',
    chipCount='16 diapositivas',

    rwEyebrow='Antes de jugar', rwTitle='¿De quién es la regla?',
    rw1h='MUST &mdash; es tu propia idea',
    rw1b='Usa <strong>must</strong> cuando la obligación viene de ti mismo '
         '&mdash; tu propia opinión, sentimiento o decisión. <em>I must '
         'save my progress before I log off.</em>',
    rw1n='<em>Must you&hellip;?</em> suena muy formal en una pregunta. '
         '<em>Do you have to&hellip;?</em> es lo que la gente dice en '
         'realidad.',
    rw2h='HAVE TO &mdash; la regla de otra persona',
    rw2b='Usa <strong>have to</strong> cuando la obligación viene de fuera '
         'de ti &mdash; una regla, una ley, otra persona. <em>In survival '
         'mode you have to eat, or your health drops.</em>',
    rw2n='<strong>Has to</strong> para he / she / it: <em>Steve has to '
         'sleep before morning.</em>',

    trEyebrow='La trampa', trTitle='Mustn&rsquo;t no es lo contrario de must',
    tr1h='MUSTN&rsquo;T &mdash; prohibido',
    tr1b="<strong>Mustn't</strong> significa que está prohibido &mdash; no "
         "hagas esto. <em>You mustn't dig straight down; lava might be "
         "waiting.</em>",
    tr1n='Un cartel de advertencia usa <em>mustn&rsquo;t</em>, nunca '
         '<em>don&rsquo;t have to</em>.',
    tr2h='DON&rsquo;T HAVE TO &mdash; sin obligación',
    tr2b="<strong>Don't have to</strong> significa que no hay obligación "
         "&mdash; puedes si quieres, pero nada te obliga. <em>In creative "
         "mode you don't have to mine for resources.</em>",
    tr2n='Son opuestos en significado, no solo en forma. Confundir estos '
         'dos es el error más común con esta gramática.',

    pfEyebrow='Otros tiempos', pfTitle='Must no tiene pasado &mdash; ni futuro',
    pf1h='HAD TO &mdash; el pasado',
    pf1b='<strong>Must</strong> no cambia para el pasado. Usa en su lugar '
         '<strong>had to</strong>. <em>I had to respawn three times last '
         'night.</em>',
    pf1n='Igual en preguntas y negaciones: <em>Did you have to fight it '
         'alone?</em>',
    pf2h='WILL HAVE TO &mdash; el futuro',
    pf2b='Para una obligación que empieza más adelante, usa <strong>will '
         'have to</strong>. <em>After this update, you will have to find a '
         'new seed.</em>',
    pf2n='Nunca <em>will must</em> &mdash; dos formas modales nunca van '
         'juntas.',

    mcEyebrow='Actividad 1 &middot; ¿Qué forma?', mcTitle='Elige la palabra correcta',
    mc1why='<strong>Must</strong> &mdash; es el propio sentimiento urgente '
           'de Steve, no una regla que le haya dado nadie.',
    mc2why='<strong>Have to</strong> &mdash; esto viene de las reglas del '
           'servidor, no de los sentimientos del jugador.',
    mc3why="<strong>Mustn't</strong> &mdash; esto es una prohibición. "
           'Entrar sin luz está prohibido, no solo es poco prudente.',
    mc4why="<strong>Don't have to</strong> &mdash; no hay obligación de "
           'recoger madera, aunque podrías si quisieras. No está prohibido, '
           "así que <em>are not allowed to</em> y <em>mustn't</em> son "
           'ambas incorrectas.',
    mc5why='<strong>Had to</strong> &mdash; esto ocurrió en el pasado, y '
           '<em>must</em> no tiene forma de pasado.',
    mc6why='<strong>Has to</strong> &mdash; tercera persona (she) más un '
           'requisito externo de la misión, no la propia idea de Alex.',

    gapEyebrow='Actividad 2 &middot; Escríbelo', gapTitle='Completa la frase',
    gapHint='Las contracciones y las formas completas valen igual &mdash; '
            '<em>mustn&rsquo;t</em> o <em>must not</em>, cualquiera de las '
            'dos funciona.',
    g1why='Prohibición &mdash; un &ldquo;no&rdquo; firme, no una '
          'obligación ausente.',
    g2why='Requisito externo (la propia regla del modo de juego) más '
          'tercera persona.',
    g3why='Obligación en el pasado &mdash; <em>must</em> no tiene forma de '
          'pasado propia.',
    g4why='Sin obligación, no una prohibición &mdash; aun así podrías '
          'recoger recursos si quisieras.',
    g5why='Obligación interna &mdash; es el propio sentimiento del '
          'hablante, no una regla externa.',
    g6why='Una regla externa que se aplica a todo el mundo &mdash; no el '
          'sentimiento personal del jugador.',

    matchEyebrow='Actividad 3 &middot; Las seis formas',
    matchTitle='Relaciona la forma con su significado',
    matchHint='Haz clic en una forma y luego en lo que significa.',
    matchWhy='Las seis describen una obligación, pero el origen (tú, o '
             'fuera de ti), la dirección (obligatorio, o prohibido) y el '
             'tiempo (pasado, presente, futuro) son distintos en cada '
             'caso. Esa triple distinción es todo el punto gramatical.',

    actTitle='Explica las reglas de tu mundo', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno de vosotros es un jugador experimentado que explica '
                  'las reglas a alguien totalmente nuevo. Dos minutos cada '
                  'uno, luego cambiad.',
    actSpeak1='Dile a tu compañero tres cosas que un jugador nuevo debe '
              'hacer en sus primeros diez minutos.',
    actSpeak2='Advierte a tu compañero de dos cosas que no debe hacer, y '
              'explica por qué.',
    actSpeak3='Di una cosa que no tienes que hacer en el modo fácil, y una '
              'que sí tienes que hacer.',
    actSpeak4='Describe algo que te pasó en un juego y explica qué tuviste '
              'que hacer al respecto.',
    actWriteKind='Escritura &middot; 100&ndash;130 palabras',
    actWriteBrief='Escribe una breve guía de supervivencia para un jugador '
                  'nuevo en tu juego o mundo favorito. Di qué debe hacer, '
                  'qué no debe hacer, y de qué no tiene que preocuparse. '
                  'Usa al menos una frase con <em>had to</em>, sobre algo '
                  'que ya te haya pasado.',
    actPlaceholder='The first thing you have to do is…',

    resPerfect='Puntuación perfecta. Sabes exactamente de quién es la regla, '
               'siempre.',
    resStrong='Muy bien. Repasa <em>mustn&rsquo;t</em> frente a '
              '<em>don&rsquo;t have to</em> &mdash; esa trampa es la que '
              'más a menudo cuesta el último punto.',
    resMid='Buena base. Vuelve a las dos primeras diapositivas: pregúntate '
           '<em>de quién</em> es la regla antes de elegir una forma.',
    resLow='Vuelve a leer las tres diapositivas de teoría. Tres preguntas '
           '&mdash; ¿tú, o alguien más? ¿obligatorio, o prohibido? ¿ahora, '
           'pasado, o futuro? &mdash; y el resto es vocabulario.',
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
