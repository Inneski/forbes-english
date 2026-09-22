# -*- coding: utf-8 -*-
"""Interface strings for Alan Watts: The Art of Being Present (B1) — EN, DE, ES.

House-style rule 8: the target language stays in English. Every stem, option,
gap sentence, word bank and sentence-building chunk is the thing under test,
so none of it translates. What German and Spanish cover is the chrome — the
cover, the eyebrows, the section titles, the reading prose, the hints, the
discussion prompts and the activation stage.

The reading panels carry their prose as keys rather than bare English. At B1
the passage is the scaffolding a learner reads BEFORE the questions are
answerable at all, so a German learner who cannot read it cannot start. That
is the same call `mc(ctx_key=…)` exists for, applied to a panel.

Teach cards are written in the six-item form (head_key, head, body_key, body,
note_key, note) so the rule text travels with its heading — the five-item
form leaves the body in English under a translated heading, which is the
half-finished screen HOUSE-STYLE §8 exists to prevent.

ledDp/ledTime/ledClues come from CHROME: the template's deck bar carries a
hidden RPG ledger whose three labels are data-i18n, and a deck built from the
current template fails the checker's "data-i18n with no English key" rule
unless they resolve.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'actEyebrow', 'actSpeakKind',
        'btnCopy', 'btnCopied', 'wordCount', 'ledDp', 'ledTime',
        'ledClues', 'actSpeakWord', 'actWriteWord', 'resNext']

T = {}

# ══════════════════════════════════════════════════════════════════════
# ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='The art of <em>being present</em>',
    coverSub='Alan Watts on the self, effortless action and why nothing lasting '
             'would be worth having',
    chipLevel='B1 &middot; Philosophy &amp; wellbeing',
    chipFocus='Reading, vocabulary &amp; sentence building',
    chipCount='COUNT slides',

    bankLabel='Word bank:',

    # ── reading panels ────────────────────────────────────────────────
    eWho='The man',
    tWho='Who was Alan Watts?',
    pWho1='Alan Watts (1915&ndash;1973) was a British philosopher who spent most '
          'of his life explaining Eastern philosophy &mdash; ideas from Zen '
          'Buddhism, Taoism and Hinduism &mdash; to people in the West.',
    pWho2='He believed that many Western people were too focused on the future '
          'and the past, and had forgotten how to live in the present moment.',

    eQuote='In his own words',
    tQuote='The line he is remembered for',
    pQuote1='&ldquo;This is the real secret of life &mdash; to be completely '
            'engaged with what you are doing in the here and now.&rdquo;',
    pQuote2='Everything else in this lesson is an attempt to say that sentence '
            'more slowly.',

    eSelf='Idea one',
    tSelf='The illusion of the separate self',
    pSelf1='Watts argued that most people think of themselves as separate from '
           'the world around them &mdash; like a stranger living inside a body, '
           'looking out at nature.',
    pSelf2='He believed this was a mistake. You are not separate from the '
           'universe; you <mark>are</mark> the universe experiencing itself.',

    eWu='Idea two',
    tWu='Wu wei &mdash; not trying too hard',
    pWu1='In Chinese philosophy there is a concept called <em>wu wei</em>, which '
         'means &ldquo;non-doing&rdquo; or &ldquo;effortless action&rdquo;.',
    pWu2='Watts used it to explain that sometimes the best way to achieve '
         'something is to relax and let it happen, instead of forcing it. He '
         'compared this to falling asleep: <mark>the harder you try, the harder '
         'it becomes</mark>.',

    eImp='Idea three',
    tImp='Impermanence',
    pImp1='Everything changes and nothing lasts forever. Rather than finding '
          'this frightening, Watts encouraged people to accept it and even to '
          'celebrate it.',
    pImp2='He said the beauty of a flower comes partly from the fact that it '
          'will die. In the same way, our lives are precious <mark>because</mark> '
          'they do not last.',

    eLeg='Afterwards',
    tLeg='Why we still hear him',
    pLeg1='Watts wrote more than 25 books and gave hundreds of lectures. The '
          'recordings are still listened to by millions of people today.',
    pLeg2='His message was simple: stop worrying about the future, stop '
          'regretting the past, and learn to be fully alive in this moment.',

    # ── activities ────────────────────────────────────────────────────
    eComp='Reading',
    tComp='What did the passage actually say?',

    eVocab='Vocabulary',
    tVocab='One word per space',
    hVocab='Seven words, seven spaces, each used once. Case does not matter.',

    ePat='Before you build',
    tPat='Three patterns to listen for',
    patA='that + clause',
    patAb='After <em>believe</em>, <em>say</em> or <em>think</em>, the whole '
          'second idea arrives as one block.',
    patAn='Watts believed <strong>that the present moment is real</strong>.',
    patB='the more&hellip; the more&hellip;',
    patBb='Two changes locked together. Both halves take <em>the</em>, and the '
          'comparative comes straight after it.',
    patBn='<strong>The harder</strong> you try, <strong>the more difficult</strong> '
          'it becomes.',
    patC='rather than',
    patCb='Used to put two options side by side and reject the second one.',
    patCn='Accept change <strong>rather than</strong> fear it.',

    eOrder='Sentence building',
    tOrder='Put the parts in order',
    hOrder='Click a block to place it, click a placed block to take it back. '
           'One point for the whole sentence.',

    # ── activation ────────────────────────────────────────────────────
    actTitle='Now say it to someone',
    actUse='Use these',
    actSpeakBrief='In pairs, all three. You need not agree with Watts.',
    actSpeak1='A friend says they are &ldquo;too busy to be present&rdquo;. '
              'Answer with two of Watts&rsquo; ideas &mdash; without saying '
              '&ldquo;meditate&rdquo;.',
    actSpeak2='Describe something you tried too hard at and made worse. What '
              'would <em>wu wei</em> have looked like?',
    actSpeak3='Argue against him. Is &ldquo;stop planning&rdquo; good advice at '
              'your age?',
    actWriteKind='Writing',
    actWriteBrief='150&ndash;200 words to a friend who says the last five years '
                  'were wasted. Use four target expressions and one concession.',
    actPlaceholder='You say those years were wasted, and I see why it feels '
                   'that way&hellip;',
)

# ══════════════════════════════════════════════════════════════════════
# GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Die Kunst, <em>gegenwärtig zu sein</em>',
    coverSub='Alan Watts über das Selbst, das mühelose Handeln und warum nichts '
             'Bleibendes es wert wäre, besessen zu werden',
    chipLevel='B1 &middot; Philosophie &amp; Wohlbefinden',
    chipFocus='Lesen, Wortschatz &amp; Satzbau',
    chipCount='COUNT Folien',

    bankLabel='Wortspeicher:',

    eWho='Der Mensch',
    tWho='Wer war Alan Watts?',
    pWho1='Alan Watts (1915&ndash;1973) war ein britischer Philosoph, der den '
          'größten Teil seines Lebens damit verbrachte, östliche Philosophie '
          '&mdash; Ideen aus Zen-Buddhismus, Taoismus und Hinduismus &mdash; '
          'den Menschen im Westen zu erklären.',
    pWho2='Er war überzeugt, dass viele Menschen im Westen zu sehr auf Zukunft '
          'und Vergangenheit blickten und verlernt hatten, im gegenwärtigen '
          'Augenblick zu leben.',

    eQuote='In seinen eigenen Worten',
    tQuote='Der Satz, für den man ihn kennt',
    pQuote1='&bdquo;This is the real secret of life &mdash; to be completely '
            'engaged with what you are doing in the here and now.&ldquo;',
    pQuote2='Alles Weitere in dieser Lektion ist der Versuch, diesen einen Satz '
            'langsamer zu sagen.',

    eSelf='Gedanke eins',
    tSelf='Die Illusion des getrennten Selbst',
    pSelf1='Watts meinte, die meisten Menschen hielten sich für getrennt von der '
           'Welt um sie herum &mdash; wie ein Fremder, der in einem Körper wohnt '
           'und auf die Natur hinausschaut.',
    pSelf2='Das hielt er für einen Irrtum. Du bist nicht vom Universum getrennt; '
           'du <mark>bist</mark> das Universum, das sich selbst erfährt.',

    eWu='Gedanke zwei',
    tWu='Wu wei &mdash; sich nicht zu sehr bemühen',
    pWu1='In der chinesischen Philosophie gibt es den Begriff <em>wu wei</em>, '
         'also &bdquo;Nicht-Tun&ldquo; oder &bdquo;müheloses Handeln&ldquo;.',
    pWu2='Watts erklärte damit, dass der beste Weg zum Ziel manchmal darin '
         'besteht, loszulassen und es geschehen zu lassen, statt es zu erzwingen. '
         'Er verglich das mit dem Einschlafen: <mark>je mehr man sich bemüht, '
         'desto schwerer wird es</mark>.',

    eImp='Gedanke drei',
    tImp='Vergänglichkeit',
    pImp1='Alles verändert sich, nichts bleibt für immer. Statt das erschreckend '
          'zu finden, ermutigte Watts dazu, es anzunehmen und sogar zu feiern.',
    pImp2='Die Schönheit einer Blume rühre auch daher, dass sie vergehen wird. '
          'Genauso sei unser Leben kostbar, <mark>weil</mark> es nicht andauert.',

    eLeg='Danach',
    tLeg='Warum man ihn noch hört',
    pLeg1='Watts schrieb über 25 Bücher und hielt Hunderte von Vorträgen. Die '
          'Aufnahmen werden bis heute von Millionen Menschen gehört.',
    pLeg2='Seine Botschaft war einfach: Sorge dich nicht um die Zukunft, bereue '
          'nicht die Vergangenheit, und lerne, in diesem Augenblick ganz lebendig '
          'zu sein.',

    eComp='Leseverstehen',
    tComp='Was stand wirklich im Text?',

    eVocab='Wortschatz',
    tVocab='Ein Wort pro Lücke',
    hVocab='Sieben Wörter, sieben Lücken, jedes einmal. Groß- und Kleinschreibung '
           'spielt keine Rolle.',

    ePat='Vor dem Bauen',
    tPat='Drei Muster, auf die du achten solltest',
    patA='that + Nebensatz',
    patAb='Nach <em>believe</em>, <em>say</em> oder <em>think</em> kommt der '
          'ganze zweite Gedanke als ein Block.',
    patAn='Watts believed <strong>that the present moment is real</strong>.',
    patB='the more&hellip; the more&hellip;',
    patBb='Zwei Veränderungen, aneinander gekoppelt. Beide Hälften nehmen '
          '<em>the</em>, und der Komparativ folgt unmittelbar darauf.',
    patBn='<strong>The harder</strong> you try, <strong>the more difficult</strong> '
          'it becomes.',
    patC='rather than',
    patCb='Stellt zwei Möglichkeiten nebeneinander und weist die zweite zurück.',
    patCn='Accept change <strong>rather than</strong> fear it.',

    eOrder='Satzbau',
    tOrder='Bring die Teile in die richtige Reihenfolge',
    hOrder='Klicke einen Block an, um ihn zu setzen, und einen gesetzten Block, '
           'um ihn zurückzunehmen. Ein Punkt für den ganzen Satz.',

    actTitle='Jetzt sag es jemandem',
    actUse='Verwende diese',
    actSpeakBrief='In Paaren, alle drei. Ihr müsst Watts nicht zustimmen.',
    actSpeak1='Ein Freund sagt, er sei &bdquo;zu beschäftigt, um gegenwärtig zu '
              'sein&ldquo;. Antworte mit zwei Gedanken von Watts &mdash; ohne '
              'das Wort &bdquo;meditieren&ldquo;.',
    actSpeak2='Beschreibe etwas, bei dem du dich zu sehr bemüht und es '
              'verschlechtert hast. Wie hätte <em>wu wei</em> ausgesehen?',
    actSpeak3='Widersprich ihm. Ist &bdquo;plane nicht mehr&ldquo; in deinem '
              'Alter ein guter Rat?',
    actWriteKind='Schreiben',
    actWriteBrief='150&ndash;200 Wörter an eine Freundin, die sagt, die letzten '
                  'fünf Jahre seien vergeudet. Vier Zielausdrücke und ein '
                  'Zugeständnis.',
    actPlaceholder='Du sagst, diese Jahre seien vergeudet, und ich verstehe, '
                   'warum&hellip;',
)

# ══════════════════════════════════════════════════════════════════════
# SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='El arte de <em>estar presente</em>',
    coverSub='Alan Watts sobre el yo, la acción sin esfuerzo y por qué nada '
             'duradero valdría la pena',
    chipLevel='B1 &middot; Filosofía y bienestar',
    chipFocus='Lectura, vocabulario y construcción de frases',
    chipCount='COUNT diapositivas',

    bankLabel='Banco de palabras:',

    eWho='El hombre',
    tWho='¿Quién fue Alan Watts?',
    pWho1='Alan Watts (1915&ndash;1973) fue un filósofo británico que dedicó casi '
          'toda su vida a explicar la filosofía oriental &mdash; ideas del '
          'budismo zen, el taoísmo y el hinduismo &mdash; a la gente de '
          'Occidente.',
    pWho2='Creía que muchas personas en Occidente estaban demasiado pendientes '
          'del futuro y del pasado, y habían olvidado cómo vivir en el momento '
          'presente.',

    eQuote='En sus propias palabras',
    tQuote='La frase por la que se le recuerda',
    pQuote1='&laquo;This is the real secret of life &mdash; to be completely '
            'engaged with what you are doing in the here and now.&raquo;',
    pQuote2='Todo lo demás en esta lección es un intento de decir esa frase más '
            'despacio.',

    eSelf='Idea uno',
    tSelf='La ilusión del yo separado',
    pSelf1='Watts sostenía que la mayoría de la gente se considera separada del '
           'mundo que la rodea &mdash; como un extraño que vive dentro de un '
           'cuerpo y mira hacia la naturaleza.',
    pSelf2='Él creía que eso era un error. No estás separado del universo; tú '
           '<mark>eres</mark> el universo experimentándose a sí mismo.',

    eWu='Idea dos',
    tWu='Wu wei &mdash; no esforzarse demasiado',
    pWu1='En la filosofía china existe el concepto de <em>wu wei</em>, que '
         'significa &laquo;no hacer&raquo; o &laquo;acción sin esfuerzo&raquo;.',
    pWu2='Watts lo usaba para explicar que a veces la mejor manera de conseguir '
         'algo es relajarse y dejar que ocurra, en lugar de forzarlo. Lo comparaba '
         'con quedarse dormido: <mark>cuanto más lo intentas, más difícil se '
         'vuelve</mark>.',

    eImp='Idea tres',
    tImp='La impermanencia',
    pImp1='Todo cambia y nada dura para siempre. En lugar de encontrar esto '
          'aterrador, Watts animaba a aceptarlo e incluso a celebrarlo.',
    pImp2='Decía que la belleza de una flor viene en parte de que va a morir. '
          'Del mismo modo, nuestras vidas son valiosas <mark>porque</mark> no '
          'duran.',

    eLeg='Después',
    tLeg='Por qué se le sigue escuchando',
    pLeg1='Watts escribió más de 25 libros y dio cientos de conferencias. Millones '
          'de personas siguen escuchando hoy las grabaciones.',
    pLeg2='Su mensaje era sencillo: deja de preocuparte por el futuro, deja de '
          'lamentar el pasado y aprende a estar plenamente vivo en este momento.',

    eComp='Comprensión lectora',
    tComp='¿Qué decía realmente el texto?',

    eVocab='Vocabulario',
    tVocab='Una palabra por hueco',
    hVocab='Siete palabras, siete huecos, cada una una sola vez. Las mayúsculas '
           'no importan.',

    ePat='Antes de construir',
    tPat='Tres estructuras a las que prestar atención',
    patA='that + oración',
    patAb='Después de <em>believe</em>, <em>say</em> o <em>think</em>, la segunda '
          'idea entera llega como un solo bloque.',
    patAn='Watts believed <strong>that the present moment is real</strong>.',
    patB='the more&hellip; the more&hellip;',
    patBb='Dos cambios unidos entre sí. Las dos mitades llevan <em>the</em>, y el '
          'comparativo va justo detrás.',
    patBn='<strong>The harder</strong> you try, <strong>the more difficult</strong> '
          'it becomes.',
    patC='rather than',
    patCb='Sirve para poner dos opciones una al lado de la otra y rechazar la '
          'segunda.',
    patCn='Accept change <strong>rather than</strong> fear it.',

    eOrder='Construcción de frases',
    tOrder='Ordena las partes',
    hOrder='Haz clic en un bloque para colocarlo y en uno ya colocado para '
           'retirarlo. Un punto por la frase completa.',

    actTitle='Ahora díselo a alguien',
    actUse='Usa estas',
    actSpeakBrief='En parejas, las tres. No hace falta estar de acuerdo con Watts.',
    actSpeak1='Un amigo dice que está &laquo;demasiado ocupado para estar '
              'presente&raquo;. Respóndele con dos ideas de Watts &mdash; sin '
              'decir &laquo;medita&raquo;.',
    actSpeak2='Describe algo en lo que te esforzaste demasiado y empeoraste. '
              '¿Cómo habría sido <em>wu wei</em>?',
    actSpeak3='Discútele. ¿Es &laquo;deja de planificar&raquo; un buen consejo a '
              'tu edad?',
    actWriteKind='Escritura',
    actWriteBrief='150&ndash;200 palabras a un amigo que dice que desperdició '
                  'los últimos cinco años. Cuatro expresiones objetivo y una '
                  'concesión.',
    actPlaceholder='Dices que esos años se desperdiciaron, y entiendo por qué lo '
                   'sientes así&hellip;',
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
