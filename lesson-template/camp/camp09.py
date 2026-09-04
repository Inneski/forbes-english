# -*- coding: utf-8 -*-
"""Camp 9 - Past Perfect, Part 1: the earlier past.

Syllabus codes (claude/tense-subgroups-syllabus.md): PPF1 an earlier past, one
thing before another (B1); PPF2 after / before / by the time / when (B1); plus
the form load - one 'had' for every subject, the third form, hadn't, Had...?
Backshift, the third conditional and wish are Part 2.

Chassis: camp 3, the past simple - because every past perfect sentence has a
past simple in it (the LATER action), and that camp's brown ink is what the
later action wears here, beside the past perfect's own maroon.

Artwork: past-perfect-time-signals/, the Maroon Memory Vault - 41 scenes, all
dark red brick and lantern light. Hero bg18: the gate at sunset, one character
walking out, the only sky in the set with real blue in it.
"""

CHASSIS = 'blockcamp-past-simple.html'
ART = 'past-perfect-time-signals/'


def bg(n):
    return '%sbg%02d.jpg' % (ART, n)


def sup(es, de):
    return ('<span class="sup" data-lang="es"><b>ES</b><span>%s</span></span>'
            '<span class="sup" data-lang="de"><b>DE</b><span>%s</span></span>' % (es, de))


def q(s):
    return s.replace('"', '&quot;')


def sec(kind, n, side, vpos, inner, attrs=''):
    v = ' data-vpos="%s"' % vpos if vpos else ''
    a = (' ' + attrs) if attrs else ''
    return ('<section class="slide" data-type="%s" data-bg="%s" data-side="%s"%s%s>\n%s\n    </section>'
            % (kind, bg(n), side, v, a, inner))


def head(eyebrow_key, eyebrow, title_key, title, count=''):
    eb = ('<span data-i18n="%s">%s</span> &middot; %s' % (eyebrow_key, eyebrow, count)
          if count else '<span data-i18n="%s">%s</span>' % (eyebrow_key, eyebrow))
    return ('      <div class="slide-head"><div>\n'
            '        <div class="eyebrow">%s</div>\n'
            '        <h2 class="slide-title" data-i18n="%s">%s</h2>\n'
            '      </div></div>' % (eb, title_key, title))


# ── role markup ───────────────────────────────────────────────────────
def had(t='had'):
    return '<em class="t-ppf">%s</em>' % t


def pp(t):
    return '<em class="pp">%s</em>' % t


def past(t):
    return '<em class="t-past">%s</em>' % t


NEG = '<em class="neg">n&rsquo;t</em>'
NOT = '<em class="neg">not</em>'


def card(hkey, h, bkey, b, chips, es, de):
    ex = ''.join('<span>%s</span>' % c for c in chips)
    return ('          <div class="card">\n'
            '            <p class="prose"><strong data-i18n="%s">%s</strong></p>\n'
            '            <p class="prose" data-i18n="%s" style="margin-top:8px;font-size:18px">%s</p>\n'
            '            <p class="prose dim" style="margin-top:8px;font-size:15px">'
            '<span class="exlist">%s</span>%s</p>\n'
            '          </div>' % (hkey, h, bkey, b, ex, sup(es, de)))


def cards(*cs):
    return ('      <div class="slide-body">\n'
            '        <div class="cols" style="grid-template-columns:1fr 1fr">\n'
            + '\n'.join(cs) + '\n        </div>\n      </div>')


def para_block(hkey, h, es, de, rows):
    out = ['          <div class="para-block">',
           '            <div class="para-head" data-i18n="%s">%s</div>%s' % (hkey, h, sup(es, de))]
    for subj, verb in rows:
        out.append('            <div class="para-row"><span class="para-subj">%s</span>'
                   '<span class="para-verb">%s</span></div>' % (subj, verb))
    out.append('          </div>')
    return '\n'.join(out)


def para(blocks, note_key, note):
    return ('      <div class="slide-body">\n        <div class="para">\n'
            + '\n'.join(blocks) + '\n        </div>\n'
            '        <p class="para-note" style="text-align:center;margin-top:14px;font-size:13px" '
            'data-i18n="%s">%s</p>\n      </div>' % (note_key, note))


def mc(n, of, bgn, side, vpos, tkey, title, stem, es, de, opts, why, hint_key, hint, attrs=''):
    """opts: list of (text, explain or None). Exactly one None = the key."""
    rows = []
    for text, ex in opts:
        if ex is None:
            rows.append('          <button class="opt" data-correct>%s</button>' % text)
        else:
            rows.append('          <button class="opt" data-explain="%s">%s</button>' % (q(ex), text))
    return sec('mc', bgn, side, vpos,
        head('qEyebrow', 'Practice', tkey, title, '%d / %d' % (n, of)) + '\n'
        '      <div class="slide-body">\n'
        '        <p class="q-stem">%s%s</p>\n'
        '        <div class="opts">\n%s\n        </div>\n'
        '        <p class="feedback" data-explain="%s"></p>\n'
        '        <div class="hint-wrap"><button class="btn hint-btn" data-action="hint" data-i18n="btnHint">Hint</button>'
        '<p class="hint-panel" data-i18n="%s">%s</p></div>\n'
        '      </div>' % (stem, sup(es, de), '\n'.join(rows), q(why), hint_key, hint), attrs)


def ex(en, es, de):
    """A wrong-answer explanation with its gloss, as the engine renders it."""
    return '%s%s' % (en, sup(es, de))


# ══════════════════════════════════════════════════════════════════════
# THE SLIDES
# ══════════════════════════════════════════════════════════════════════
S = []

# 2 ── What it means ────────────────────────────────────────────────────
S.append(sec('teach', 2, 'right', 'top',
    head('useEyebrow', 'What it means', 'useTitle', 'Two pasts, and one came first') + '\n' +
    cards(
        card('useH1', 'The earlier action', 'useB1',
             'It was already finished when the story arrived.',
             ['the bridge <b>%s %s</b>' % (had(), pp('fallen')),
              'they <b>%s %s</b>' % (had(), pp('left'))],
             'el puente se hab&iacute;a ca&iacute;do &middot; se hab&iacute;an ido',
             'die Br&uuml;cke war eingest&uuml;rzt &middot; sie waren gegangen'),
        card('useH2', 'The later action', 'useB2',
             'The story itself. Plain past simple.',
             ['Dale <b>%s</b>' % past('arrived'),
              'we <b>%s</b> the note' % past('found')],
             'Dale lleg&oacute; &middot; encontramos la nota',
             'Dale kam an &middot; wir fanden die Notiz'))))

# 3 ── The form: one 'had' ──────────────────────────────────────────────
S.append(sec('teach', 6, 'right', 'top',
    head('formEyebrow', 'The form', 'formTitle', 'One &lsquo;had&rsquo; for everyone') + '\n' +
    para([
        para_block('formA', 'Every subject', 'una sola forma: had', 'eine Form f&uuml;r alle: had', [
            ('I / you / we / they', 'we %s %s' % (had(), pp('left'))),
            ('he / she / it', 'she %s %s' % (had(), pp('left')))]),
        para_block('formB', 'Spoken', 'ella se hab&iacute;a ido', 'sie war gegangen', [
            ('short form', 'she%s %s' % (had('&rsquo;d'), pp('left'))),
            ('no &lsquo;has&rsquo;, no &lsquo;did&rsquo;', 'she <s>has left</s> &middot; <s>did left</s>')]),
    ], 'formNote',
    '<span class="formula">SUBJECT + %s + %s</span>'
    '<span class="dictum">ONE &lsquo;HAD&rsquo; FOR ALL &mdash; THIRD FORM AFTER IT!</span>'
    % (had(), pp('PAST PARTICIPLE')))))

# 4 ── Regular participles ──────────────────────────────────────────────
S.append(sec('teach', 8, 'right', '',
    head('edEyebrow', 'The third form', 'edTitle', 'Regular verbs: the same -ed') + '\n' +
    para([
        para_block('edA', 'Most verbs', 'solo a&ntilde;ade -ed', 'einfach -ed anh&auml;ngen', [
            ('repair', '%s repair%s' % (had(), pp('ed'))),
            ('lock', '%s lock%s' % (had(), pp('ed')))]),
        para_block('edB', 'Verbs ending in e', 'solo a&ntilde;ade -d', 'nur -d anh&auml;ngen', [
            ('close', '%s close%s' % (had(), pp('d'))),
            ('arrive', '%s arrive%s' % (had(), pp('d')))]),
        para_block('edC', 'Double the consonant', 'la consonante se dobla', 'der Konsonant wird verdoppelt', [
            ('stop', '%s sto%s' % (had(), pp('pped'))),
            ('plan', '%s pla%s' % (had(), pp('nned')))]),
    ], 'edNote',
    '<span class="formula">regular: past simple = third form</span>'
    '<span class="formula">study &rarr; %s &nbsp; carry &rarr; %s</span>'
    % (pp('studied'), pp('carried'))), 'data-w="wide"'))

# 5 ── Irregular participles ────────────────────────────────────────────
S.append(sec('teach', 10, 'right', '',
    head('irEyebrow', 'The third form', 'irTitle', 'Irregular: learn the third form') + '\n' +
    para([
        para_block('irA', 'A different third form', 'ir &rarr; gone &middot; ver &rarr; seen', 'gehen &rarr; gone &middot; sehen &rarr; seen', [
            ('go / %s' % past('went'), pp('gone')),
            ('see / %s' % past('saw'), pp('seen')),
            ('take / %s' % past('took'), pp('taken'))]),
        para_block('irB', 'The same as the past', 'encontrar &rarr; found &middot; hacer &rarr; made', 'finden &rarr; found &middot; machen &rarr; made', [
            ('find / %s' % past('found'), pp('found')),
            ('make / %s' % past('made'), pp('made')),
            ('have / %s' % past('had'), pp('had'))]),
        para_block('irC', 'be', 'ser, estar &rarr; been', 'sein &rarr; been', [
            ('be / %s' % past('was'), pp('been')),
            ('never', '<s>had was</s>'),
            ('always', '%s %s' % (had(), pp('been')))]),
    ], 'irNote',
    '<span class="formula">after %s: <b>%s</b>, never %s</span>'
    % (had(), pp('gone'), past('went'))), 'data-w="wide" style="--col-w:70%"'))

# 6 ── Saying no, and asking ─────────────────────────────────────────────
S.append(sec('teach', 15, 'left', 'top',
    head('noEyebrow', 'The form', 'noTitle', 'Saying no, and asking') + '\n' +
    para([
        para_block('noA', 'Say no', 'a&ntilde;ade not, o n&rsquo;t', 'not oder n&rsquo;t dazu', [
            ('long', 'she %s %s %s' % (had(), NOT, pp('seen'))),
            ('short', 'she %s%s %s' % (had(), NEG, pp('seen')))]),
        para_block('noB', 'Ask', '&rsquo;Had&rsquo; abre la pregunta', '&rsquo;Had&rsquo; er&ouml;ffnet die Frage', [
            ('&lsquo;had&rsquo; goes first', '%s she %s it?' % (had('Had'), pp('seen'))),
            ('short answers', 'Yes, she %s. &middot; No, she %s%s.' % (had(), had(), NEG))]),
        para_block('noC', 'Question words', 'la palabra interrogativa va primero', 'das Fragewort steht zuerst', [
            ('what', 'What %s %s?' % (had(), pp('happened'))),
            ('where', 'Where %s they %s?' % (had(), pp('gone')))]),
    ], 'noNote',
    '<span class="formula">SUBJECT + %s%s + %s</span>'
    '<span class="formula">%s + SUBJECT + %s ?</span>'
    % (had(), NEG, pp('PAST PARTICIPLE'), had('Had'), pp('PAST PARTICIPLE')))))

# 7 ── The order of events, drawn as a scale ────────────────────────────
S.append(sec('teach', 4, 'right', 'top',
    head('lineEyebrow', 'Which came first?', 'lineTitle', 'Earlier, later, now') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="card freq">\n'
    '          <div class="freq-v">\n'
    '            <div class="freq-rail-v"></div>\n'
    '            <div class="freq-row"><div class="freq-word">the cart %s %s</div><div class="freq-pct">earlier</div>'
    '<div class="freq-gloss">past perfect%s</div></div>\n'
    '            <div class="freq-row"><div class="freq-word">we %s</div><div class="freq-pct">later</div>'
    '<div class="freq-gloss">past simple%s</div></div>\n'
    '            <div class="freq-row"><div class="freq-word">I am telling you</div><div class="freq-pct">now</div>'
    '<div class="freq-gloss">present%s</div></div>\n'
    '          </div>\n'
    '          <p class="freq-rule" data-i18n="lineRule"><span class="formula">the earlier one takes %s &mdash; <b>always</b></span></p>\n'
    '        </div>\n'
    '      </div>'
    % (had(), pp('crashed'), sup('el carro se hab&iacute;a estrellado', 'der Wagen war verungl&uuml;ckt'),
       past('arrived'), sup('llegamos', 'wir kamen an'),
       sup('te lo cuento', 'ich erz&auml;hle es dir'), had())))

# 8 ── Time signals ─────────────────────────────────────────────────────
S.append(sec('teach', 21, 'left', 'top',
    head('sigEyebrow', 'Time signals', 'sigTitle', 'Words that set the order') + '\n' +
    cards(
        card('sigH1', 'Between the two actions', 'sigB1',
             'One word says which came first.',
             ['<b>before</b> we arrived', '<b>after</b> it had closed',
              '<b>by the time</b> we came', '<b>when</b> she looked'],
             'antes de que llegáramos &middot; después de que cerrara &middot; para cuando vinimos &middot; cuando ella miró',
             'bevor wir ankamen &middot; nachdem es geschlossen hatte &middot; als wir kamen, schon &middot; als sie hinsah'),
        card('sigH2', 'Inside the verb', 'sigB2',
             'These sit between &lsquo;had&rsquo; and the participle.',
             ['%s <b>already</b> %s' % (had(), pp('left')),
              '%s <b>just</b> %s' % (had(), pp('closed')),
              '%s <b>never</b> %s' % (had(), pp('seen')),
              '%s%s %s <b>yet</b>' % (had(), NEG, pp('arrived'))],
             'ya se había ido &middot; acababa de cerrar &middot; nunca había visto &middot; aún no había llegado',
             'war schon gegangen &middot; hatte gerade geschlossen &middot; hatte nie gesehen &middot; war noch nicht angekommen')),
    'data-w="wide" style="--wcols:1" data-tr="beside"'))

# ── Practice ─────────────────────────────────────────────────────────
S.append(mc(1, 6, 30, 'right', 'top', 'qTitleFirst', 'Which happened first?',
    'By the time we reached the vault, the guards had locked the gate.',
    'Para cuando llegamos a la c&aacute;mara, los guardias hab&iacute;an cerrado la puerta.',
    'Als wir die Kammer erreichten, hatten die Wachen das Tor schon verschlossen.',
    [('the guards locked the gate', None),
     ('we reached the vault', ex('That is the later action &mdash; it is in the past simple.',
                                 'Esa es la acci&oacute;n posterior: est&aacute; en pasado simple.',
                                 'Das ist die sp&auml;tere Handlung &mdash; sie steht im Past Simple.')),
     ('both at the same moment', ex('&lsquo;had locked&rsquo; puts the locking earlier, not at the same time.',
                                    '&rsquo;had locked&rsquo; pone el cierre antes, no al mismo tiempo.',
                                    '&rsquo;had locked&rsquo; setzt das Verschlie&szlig;en fr&uuml;her an, nicht gleichzeitig.')),
     ('the sentence does not say', ex('It does say: the past perfect is always the earlier one.',
                                      'S&iacute; lo dice: el past perfect es siempre lo anterior.',
                                      'Doch, er sagt es: das Past Perfect ist immer das Fr&uuml;here.'))],
    ex('<strong>had locked</strong> is the past perfect, so it happened before we reached the vault.',
       '&rsquo;had locked&rsquo; es past perfect: pas&oacute; antes',
       '&rsquo;had locked&rsquo; ist Past Perfect: es geschah vorher'),
    'hint1', 'Find the &lsquo;had&rsquo;. Whatever follows it happened first.'))

S.append(mc(2, 6, 14, 'right', 'top', 'qTitleForm', 'Choose the right form',
    'Dale ______ the beacon before the storm came.',
    'Dale ______ el faro antes de que llegara la tormenta.',
    'Dale ______ das Leuchtfeuer, bevor der Sturm kam.',
    [('has repaired', ex('&lsquo;has&rsquo; belongs to now. The storm came, so this is all in the past.',
                         '&rsquo;has&rsquo; es de ahora. Todo esto es pasado.',
                         '&rsquo;has&rsquo; geh&ouml;rt zum Jetzt. Das hier ist alles vorbei.')),
     ('had repaired', None),
     ('had repair', ex('After &lsquo;had&rsquo; comes the third form, not the base verb.',
                       'Tras &rsquo;had&rsquo; va la tercera forma, no la base.',
                       'Nach &rsquo;had&rsquo; kommt die dritte Form, nicht die Grundform.')),
     ('had repairing', ex('No -ing here. &lsquo;had&rsquo; takes the third form.',
                          'Sin -ing. &rsquo;had&rsquo; lleva la tercera forma.',
                          'Kein -ing hier. &rsquo;had&rsquo; nimmt die dritte Form.'))],
    ex('The repair came first, the storm second: <strong>had</strong> + third form.',
       'primero la reparaci&oacute;n, luego la tormenta',
       'zuerst die Reparatur, dann der Sturm'),
    'hint2', 'Two past actions. The one that came first takes &lsquo;had&rsquo;.'))

S.append(mc(3, 6, 12, 'left', 'top', 'qTitleThird', '&lsquo;went&rsquo; or &lsquo;gone&rsquo;?',
    'When Audrey arrived, the others had already ______.',
    'Cuando Audrey lleg&oacute;, los dem&aacute;s ya se hab&iacute;an ______.',
    'Als Audrey ankam, waren die anderen schon ______.',
    [('went', ex('&lsquo;went&rsquo; is the second form. After &lsquo;had&rsquo; you need the third.',
                 '&rsquo;went&rsquo; es la segunda forma. Tras &rsquo;had&rsquo; va la tercera.',
                 '&rsquo;went&rsquo; ist die zweite Form. Nach &rsquo;had&rsquo; braucht es die dritte.')),
     ('go', ex('That is the base verb. &lsquo;had&rsquo; never takes it.',
               'Esa es la forma base. &rsquo;had&rsquo; nunca la lleva.',
               'Das ist die Grundform. &rsquo;had&rsquo; nimmt sie nie.')),
     ('gone', None),
     ('going', ex('No -ing after &lsquo;had&rsquo;.',
                  'Sin -ing tras &rsquo;had&rsquo;.',
                  'Kein -ing nach &rsquo;had&rsquo;.'))],
    ex('go &rarr; went &rarr; <strong>gone</strong>. The third form goes after &lsquo;had&rsquo;.',
       'go &rarr; went &rarr; gone: la tercera forma',
       'go &rarr; went &rarr; gone: die dritte Form'),
    'hint3', 'go &rarr; went &rarr; ? &nbsp; The third column of the verb table.'))

S.append(mc(4, 6, 26, 'right', 'top', 'qTitleAsk', 'Asking and saying no',
    '______ the water reached the hall before you closed the door?',
    '&iquest;______ el agua al vest&iacute;bulo antes de que cerraras la puerta?',
    '______ das Wasser die Halle erreicht, bevor du die T&uuml;r geschlossen hast?',
    [('Did', ex('After &lsquo;Did&rsquo; the verb would be plain &lsquo;reach&rsquo;. This one is &lsquo;reached&rsquo;.',
                'Tras &rsquo;Did&rsquo; el verbo ser&iacute;a &rsquo;reach&rsquo;. Aqu&iacute; es &rsquo;reached&rsquo;.',
                'Nach &rsquo;Did&rsquo; hie&szlig;e das Verb &rsquo;reach&rsquo;. Hier steht &rsquo;reached&rsquo;.')),
     ('Has', ex('&lsquo;Has&rsquo; is now. You closed the door in the past.',
                '&rsquo;Has&rsquo; es ahora. La puerta se cerr&oacute; en el pasado.',
                '&rsquo;Has&rsquo; ist jetzt. Die T&uuml;r wurde in der Vergangenheit geschlossen.')),
     ('Was', ex('&lsquo;Was&rsquo; would need -ing. It does not go with &lsquo;reached&rsquo;.',
                '&rsquo;Was&rsquo; necesitar&iacute;a -ing. No va con &rsquo;reached&rsquo;.',
                '&rsquo;Was&rsquo; br&auml;uchte -ing. Es passt nicht zu &rsquo;reached&rsquo;.')),
     ('Had', None)],
    ex('<strong>Had</strong> opens the question, and the third form stays where it was.',
       '&rsquo;Had&rsquo; abre la pregunta',
       '&rsquo;Had&rsquo; er&ouml;ffnet die Frage'),
    'hint4', 'Which word goes first in a past perfect question?'))

S.append(mc(5, 6, 17, 'left', 'top', 'qTitleForm', 'Choose the right form',
    'They ______ the map, so they got lost.',
    'No ______ el mapa, as&iacute; que se perdieron.',
    'Sie ______ die Karte nicht gelesen, also verliefen sie sich.',
    [('hadn&rsquo;t readed', ex('&lsquo;read&rsquo; is irregular. Its third form is &lsquo;read&rsquo;.',
                                '&rsquo;read&rsquo; es irregular: su tercera forma es &rsquo;read&rsquo;.',
                                '&rsquo;read&rsquo; ist unregelm&auml;&szlig;ig: die dritte Form ist &rsquo;read&rsquo;.')),
     ('didn&rsquo;t had read', ex('&lsquo;didn&rsquo;t&rsquo; and &lsquo;had&rsquo; never go together.',
                                  '&rsquo;didn&rsquo;t&rsquo; y &rsquo;had&rsquo; nunca van juntos.',
                                  '&rsquo;didn&rsquo;t&rsquo; und &rsquo;had&rsquo; gehen nie zusammen.')),
     ('hadn&rsquo;t reading', ex('No -ing after &lsquo;hadn&rsquo;t&rsquo;.',
                                 'Sin -ing tras &rsquo;hadn&rsquo;t&rsquo;.',
                                 'Kein -ing nach &rsquo;hadn&rsquo;t&rsquo;.')),
     ('hadn&rsquo;t read', None)],
    ex('Not reading came first, getting lost second: <strong>hadn&rsquo;t</strong> + third form.',
       'primero no leer, luego perderse',
       'zuerst nicht lesen, dann sich verlaufen'),
    'hint5', 'The &lsquo;not&rsquo; goes on &lsquo;had&rsquo;, and the verb after it does not change.'))

S.append(mc(6, 6, 23, 'left', 'top', 'qTitleOrder', 'Which sentence puts it first?',
    'Which sentence says the lantern was already dark when we came in?',
    '&iquest;Qu&eacute; frase dice que la linterna ya estaba apagada cuando entramos?',
    'Welcher Satz sagt, dass die Laterne schon aus war, als wir hereinkamen?',
    [('When we entered the vault, the lantern went out.', ex('Two past simples: the lantern went out at that moment, not before.',
                                                           'Dos pasados simples: se apag&oacute; en ese momento, no antes.',
                                                           'Zwei Past Simple: sie ging in dem Moment aus, nicht vorher.')),
     ('When we had entered the vault, the lantern went out.', ex('That puts our entering first and the lantern second.',
                                                               'Eso pone primero nuestra entrada y despu&eacute;s la linterna.',
                                                               'Das setzt unser Hereinkommen zuerst und die Laterne danach.')),
     ('When we entered the vault, the lantern had gone out.', None),
     ('When we enter the vault, the lantern goes out.', ex('That is the present, and this all happened in the past.',
                                                          'Eso es presente, y todo esto pas&oacute; en el pasado.',
                                                          'Das ist Gegenwart, und das alles war in der Vergangenheit.'))],
    ex('<strong>had gone out</strong> is the earlier action, so the lantern was already dark.',
       '&rsquo;had gone out&rsquo; es lo anterior: ya estaba apagada',
       '&rsquo;had gone out&rsquo; ist das Fr&uuml;here: sie war schon aus'),
    'hint6', 'The lantern part is the earlier one. Which sentence gives it &lsquo;had&rsquo;?',
    'data-w="wide" style="--wcols:1"'))

# sort
S.append(sec('sort', 25, 'left', 'top',
    head('sortEyebrow', 'Practice', 'sortTitle', 'Same as the past, or different?') + '\n'
    '      <div class="slide-body">\n'
    '        <p class="order-hint" data-i18n="sortHint">Click a third form, then click its group.</p>\n'
    '        <div class="sort" data-bins="same as the past | different">\n'
    '          <span class="sort-item" data-bin="0">found</span>\n'
    '          <span class="sort-item" data-bin="0">made</span>\n'
    '          <span class="sort-item" data-bin="0">built</span>\n'
    '          <span class="sort-item" data-bin="0">repaired</span>\n'
    '          <span class="sort-item" data-bin="1">gone</span>\n'
    '          <span class="sort-item" data-bin="1">seen</span>\n'
    '          <span class="sort-item" data-bin="1">been</span>\n'
    '          <span class="sort-item" data-bin="1">taken</span>\n'
    '          <span class="sort-item" data-bin="1">eaten</span>\n'
    '        </div>\n'
    '        <p class="feedback" data-explain="%s"></p>\n'
    '      </div>' % q('found, made, built and repaired look the same in the past simple. gone, seen, been, taken and eaten do not &mdash; those are the ones to learn.')))

# match
S.append(sec('match', 9, 'left', 'top',
    head('matchEyebrow', 'Practice', 'matchTitle', 'Match the third form') + '\n'
    '      <div class="slide-body">\n'
    '        <p class="prose dim" style="margin-bottom:8px;font-size:17px" data-i18n="matchHint">Click a verb, then click its third form.</p>\n'
    '        <div class="match-pair" data-term="go" data-def="gone" data-term-es="ir" data-term-de="gehen" data-def-es="ido" data-def-de="gegangen"></div>\n'
    '        <div class="match-pair" data-term="see" data-def="seen" data-term-es="ver" data-term-de="sehen" data-def-es="visto" data-def-de="gesehen"></div>\n'
    '        <div class="match-pair" data-term="be" data-def="been" data-term-es="ser, estar" data-term-de="sein" data-def-es="sido, estado" data-def-de="gewesen"></div>\n'
    '        <div class="match-pair" data-term="take" data-def="taken" data-term-es="coger" data-term-de="nehmen" data-def-es="cogido" data-def-de="genommen"></div>\n'
    '        <div class="match-pair" data-term="fall" data-def="fallen" data-term-es="caer" data-term-de="fallen" data-def-es="ca&iacute;do" data-def-de="gefallen"></div>\n'
    '        <div class="match-grid"></div>\n'
    '        <p class="feedback" data-explain="%s"></p>\n'
    '      </div>' % q('These go after &lsquo;had&rsquo;, and none of them is the past simple form.')))

# gap 1
def gaprow(before, answer, after, why, es, de, width=190):
    return ('        <div class="card gap-row" style="padding:12px 16px">\n'
            '          <p class="q-stem" style="margin-bottom:0;font-size:19px">%s'
            '<input class="gap" data-answer="%s" aria-label="gap" style="width:%dpx">%s%s</p>\n'
            '          <p class="feedback" data-explain="%s"></p>\n'
            '        </div>' % (before, answer, width, after, sup(es, de), q(why)))

S.append(sec('gap', 33, 'left', 'top',
    head('gap1Eyebrow', 'Practice', 'gap1Title', 'Write the third form', '1 / 2') + '\n'
    '      <div class="slide-body">\n'
    '        <p class="prose dim" style="margin-bottom:6px;font-size:16px" data-i18n="gap1Hint">Type the verb in brackets in its third form.</p>\n'
    + gaprow('Audrey had ', 'repaired', ' the beacon before dark. <span class="dim">(repair)</span>',
             ex('Regular, so it is the same as the past simple: -ed.', 'regular: -ed, igual que el pasado simple', 'regelm&auml;&szlig;ig: -ed, wie im Past Simple'),
             'Audrey hab&iacute;a ______ el faro antes del anochecer. (reparar)',
             'Audrey hatte das Leuchtfeuer vor Einbruch der Dunkelheit ______. (reparieren)') + '\n'
    + gaprow('The bridge had ', 'fallen', ' by the time we came. <span class="dim">(fall)</span>',
             ex('fall &rarr; fell &rarr; <strong>fallen</strong>. The third form, not &lsquo;fell&rsquo;.', 'fall &rarr; fell &rarr; fallen', 'fall &rarr; fell &rarr; fallen'),
             'El puente se hab&iacute;a ______ para cuando llegamos. (caer)',
             'Die Br&uuml;cke war ______, als wir kamen. (einst&uuml;rzen)') + '\n'
    + gaprow('We had ', 'seen', ' the vault twice before. <span class="dim">(see)</span>',
             ex('see &rarr; saw &rarr; <strong>seen</strong>. &lsquo;had saw&rsquo; does not exist.', 'see &rarr; saw &rarr; seen', 'see &rarr; saw &rarr; seen'),
             'Ya hab&iacute;amos ______ la c&aacute;mara dos veces. (ver)',
             'Wir hatten die Kammer schon zweimal ______. (sehen)') + '\n'
    '        <div style="margin-top:10px">\n'
    '          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>\n'
    '        </div>\n'
    '      </div>'))

# gap 2
def gaprow2(*a, **k):
    # three rows plus a word bank and a hint: 3px less padding per row is the
    # 12px the LAYOUT gate measured this slide over by
    return gaprow(*a, **k).replace('padding:12px 16px', 'padding:9px 16px').replace('width:190px', 'width:150px')

# right/top: measured by check-placement.py, x2.57 quieter than the left
S.append(sec('gap', 36, 'right', 'top',
    head('gap2Eyebrow', 'Practice', 'gap2Title', 'Which word fits?', '2 / 2') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="act-target" style="margin-bottom:6px">\n'
    '          <span class="act-target-label" data-i18n="bankLabel">Word bank:</span>\n'
    '          <span class="bank-chip">already</span> <span class="bank-chip">yesterday</span> <span class="bank-chip">yet</span> <span class="bank-chip">before</span>\n'
    '          <span class="dim" style="font-size:15px;margin-left:8px" data-i18n="gap2Hint">one is past simple &mdash; leave it out</span>\n'
    '        </div>\n'
    + gaprow2('The guards had ', 'already', ' locked it. <span class="dim">(done first)</span>',
             ex('<strong>already</strong> = done before the other thing.', 'ya: hecho antes', 'schon: vorher erledigt'),
             'Los guardias ______ lo hab&iacute;an cerrado. (hecho antes)',
             'Die Wachen hatten es ______ verschlossen. (vorher erledigt)') + '\n'
    + gaprow2('She had not found it ', 'yet', '. <span class="dim">(still not done)</span>',
             ex('<strong>yet</strong> = still not done, up to then.', 'a&uacute;n no, hasta entonces', 'bis dahin noch nicht'),
             'Ella ______ no lo hab&iacute;a encontrado. (hasta entonces, no)',
             'Sie hatte es ______ nicht gefunden. (bis dahin nicht)') + '\n'
    + gaprow2('It had cracked ', 'before', ' we looked. <span class="dim">(order word)</span>',
             ex('<strong>before</strong> joins the two. &lsquo;Yesterday&rsquo; is past simple.', '&rsquo;yesterday&rsquo; es pasado simple', '&rsquo;yesterday&rsquo; ist Past Simple'),
             'Se hab&iacute;a agrietado ______ de que mir&aacute;ramos. (palabra de orden)',
             'Es war gerissen, ______ wir hinsahen. (Ordnungswort)') + '\n'
    '        <div style="margin-top:4px">\n'
    '          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>\n'
    '        </div>\n'
    '      </div>'))

# order x2
def order(bgn, side, vpos, answer, why, es, de):
    return sec('order', bgn, side, vpos,
        head('ord1Eyebrow', 'Practice', 'ord1Title', 'Build the sentence') + '\n'
        '      <div class="slide-body">\n'
        '        <p class="order-hint"><span data-i18n="ord1Hint">Click the words in the right order.</span>%s</p>\n'
        '        <div class="order" data-answer="%s"></div>\n'
        '        <div style="margin-top:12px">\n'
        '          <button class="btn" data-action="check-order" data-i18n="btnCheck">Check</button>\n'
        '        </div>\n'
        '        <p class="feedback" data-explain="%s"></p>\n'
        '      </div>' % (sup(es, de), answer, q(why)), 'data-nudge="up"')

S.append(order(38, 'right', 'top', 'the bridge | had fallen | before | we arrived .',
    'The earlier action takes &lsquo;had&rsquo;; &lsquo;before&rsquo; joins it to the later one.',
    'El puente se hab&iacute;a ca&iacute;do antes de que llegáramos.',
    'Die Br&uuml;cke war eingest&uuml;rzt, bevor wir ankamen.'))
# left/bottom: measured, x4.02 quieter - the characters stand on the right
S.append(order(39, 'left', 'bottom', 'had | you | seen | the map | before ?',
    '&lsquo;Had&rsquo; goes first in a question, and the third form stays after the subject.',
    '&iquest;Hab&iacute;as visto el mapa antes?',
    'Hattest du die Karte vorher gesehen?'))

# results
S.append(sec('results', 41, 'left', 'top',
    '      <div class="slide-body" style="align-items:center;text-align:center">\n'
    '        <div class="score-big"><span id="scoreVal">0</span><span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>\n'
    '        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>\n'
    '        <p class="prose dim" style="margin-top:14px" data-i18n="resNext">Now use it &rarr;</p>\n'
    '      </div>'))

# activate
S.append('<section class="slide" data-type="activate" data-bg="%s">\n' % bg(40) +
    head('actEyebrow', 'Activation', 'actTitle', 'Now tell us what had happened') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="act-target">\n'
    '          <span class="act-target-label" data-i18n="actUse">Use at least three:</span>\n'
    '          <span class="bank-chip">had gone</span>\n'
    '          <span class="bank-chip">had already</span>\n'
    '          <span class="bank-chip">hadn&rsquo;t</span>\n'
    '          <span class="bank-chip">Had you</span>\n'
    '          <span class="bank-chip">before</span>\n'
    '          <span class="bank-chip">by the time</span>\n'
    '          <span class="bank-chip">seen</span>\n'
    '          <span class="bank-chip">found</span>\n'
    '        </div>\n'
    '        <div class="cols act-cols">\n'
    '          <div class="card act-card">\n'
    '            <div class="act-kind"><span class="act-icon">&#128483;</span><span data-i18n="actSpeakKind">Discussion &middot; in pairs</span></div>\n'
    '            <p class="act-brief" data-i18n="actSpeakBrief">In pairs. One minute each, then swap.</p>\n'
    '            <ul class="act-list">\n'
    '              <li data-i18n="actSpeak1">Tell your partner about a time you arrived somewhere and something had already happened.</li>\n'
    '              <li data-i18n="actSpeak2">Ask your partner three questions that start with &lsquo;Had you ever &hellip; before &hellip;?&rsquo;</li>\n'
    '              <li data-i18n="actSpeak3">Say two things that had not happened yet when you woke up this morning.</li>\n'
    '            </ul>\n'
    '          </div>\n'
    '          <div class="card act-card">\n'
    '            <div class="act-kind"><span class="act-icon">&#9997;&#65039;</span><span data-i18n="actWriteKind">Writing &middot; 60&ndash;80 words</span></div>\n'
    '            <p class="act-brief" data-i18n="actWriteBrief">Write about a day that went wrong. What had happened before you noticed?</p>\n'
    '            <textarea class="act-input" id="actInput" data-i18n-ph="actPlaceholder" placeholder="By the time I arrived, …" aria-label="Written response"></textarea>\n'
    '            <div class="act-foot">\n'
    '              <span class="act-count" id="actCount">0 words</span>\n'
    '              <button class="btn act-copy" data-action="copy-writing" data-i18n="btnCopy">Copy</button>\n'
    '            </div>\n'
    '            <div class="act-print" id="actPrint" aria-hidden="true"></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div style="margin-top:14px;text-align:center">\n'
    '          <button class="btn" data-action="restart" data-i18n="btnRestart">Start again</button>\n'
    '        </div>\n'
    '      </div>\n    </section>')


# ══════════════════════════════════════════════════════════════════════
# THE DICTIONARY - lesson keys only; chrome comes from the chassis
# ══════════════════════════════════════════════════════════════════════
F_HAD = '<em class=\\"t-ppf\\">had</em>'
I18N = {
 'en': {
  'partLink': 'Route map &rarr;',
  'coverTitle': 'Past Perfect',
  'coverSub': 'Part 1: the earlier past',
  'chipLevel': 'B1 &middot; Grammar',
  'chipCount': '22 slides',
  'useEyebrow': 'What it means', 'useTitle': 'Two pasts, and one came first',
  'useH1': 'The earlier action', 'useB1': 'It was already finished when the story arrived.',
  'useH2': 'The later action', 'useB2': 'The story itself. Plain past simple.',
  'formEyebrow': 'The form', 'formTitle': 'One &lsquo;had&rsquo; for everyone',
  'formA': 'Every subject', 'formB': 'Spoken',
  'formNote': '<span class="formula">SUBJECT + <em class="t-ppf">had</em> + <em class="pp">PAST PARTICIPLE</em></span><span class="dictum">ONE &lsquo;HAD&rsquo; FOR ALL &mdash; THIRD FORM AFTER IT!</span>',
  'edEyebrow': 'The third form', 'edTitle': 'Regular verbs: the same -ed',
  'edA': 'Most verbs', 'edB': 'Verbs ending in e', 'edC': 'Double the consonant',
  'edNote': '<span class="formula">regular: past simple = third form</span><span class="formula">study &rarr; <em class="pp">studied</em> &nbsp; carry &rarr; <em class="pp">carried</em></span>',
  'irEyebrow': 'The third form', 'irTitle': 'Irregular: learn the third form',
  'irA': 'A different third form', 'irB': 'The same as the past', 'irC': 'be',
  'irNote': '<span class="formula">after <em class="t-ppf">had</em>: <b><em class="pp">gone</em></b>, never <em class="t-past">went</em></span>',
  'noEyebrow': 'The form', 'noTitle': 'Saying no, and asking',
  'noA': 'Say no', 'noB': 'Ask', 'noC': 'Question words',
  'noNote': '<span class="formula">SUBJECT + <em class="t-ppf">had</em><em class="neg">n&rsquo;t</em> + <em class="pp">PAST PARTICIPLE</em></span><span class="formula"><em class="t-ppf">Had</em> + SUBJECT + <em class="pp">PAST PARTICIPLE</em> ?</span>',
  'lineEyebrow': 'Which came first?', 'lineTitle': 'Earlier, later, now',
  'lineRule': '<span class="formula">the earlier one takes <em class="t-ppf">had</em> &mdash; <b>always</b></span>',
  'sigEyebrow': 'Time signals', 'sigTitle': 'Words that set the order',
  'sigH1': 'Between the two actions', 'sigB1': 'One word says which came first.',
  'sigH2': 'Inside the verb', 'sigB2': 'These sit between &lsquo;had&rsquo; and the participle.',
  'qTitleFirst': 'Which happened first?', 'qTitleForm': 'Choose the right form',
  'qTitleThird': '&lsquo;went&rsquo; or &lsquo;gone&rsquo;?', 'qTitleAsk': 'Asking and saying no',
  'qTitleOrder': 'Which sentence puts it first?',
  'hint1': 'Find the &lsquo;had&rsquo;. Whatever follows it happened first.',
  'hint2': 'Two past actions. The one that came first takes &lsquo;had&rsquo;.',
  'hint3': 'go &rarr; went &rarr; ? &nbsp; The third column of the verb table.',
  'hint4': 'Which word goes first in a past perfect question?',
  'hint5': 'The &lsquo;not&rsquo; goes on &lsquo;had&rsquo;, and the verb after it does not change.',
  'hint6': 'The lantern part is the earlier one. Which sentence gives it &lsquo;had&rsquo;?',
  'sortTitle': 'Same as the past, or different?', 'sortHint': 'Click a third form, then click its group.',
  'matchTitle': 'Match the third form', 'matchHint': 'Click a verb, then click its third form.',
  'gap1Title': 'Write the third form', 'gap1Hint': 'Type the verb in brackets in its third form.',
  'gap2Title': 'Which word fits?',
  'gap2Hint': 'one is past simple &mdash; leave it out',
  'ord1Title': 'Build the sentence', 'ord1Hint': 'Click the words in the right order.',
  'resLow': 'Go back to the dictum. One &lsquo;had&rsquo; for all, and the third form after it.',
  'resMid': 'Look again at the verb after &lsquo;had&rsquo;. That is where the points go.',
  'resStrong': 'Strong. Check the misses, then tell the story.',
  'resPerfect': 'Full marks. Now tell the story &mdash; earlier action first.',
  'actTitle': 'Now tell us what had happened',
  'actSpeak1': 'Tell your partner about a time you arrived somewhere and something had already happened.',
  'actSpeak2': 'Ask your partner three questions that start with &lsquo;Had you ever &hellip; before &hellip;?&rsquo;',
  'actSpeak3': 'Say two things that had not happened yet when you woke up this morning.',
  'actWriteBrief': 'Write about a day that went wrong. What had happened before you noticed?',
  'actPlaceholder': 'By the time I arrived, …',
 },
 'de': {
  'partLink': 'Routenkarte &rarr;',
  'coverTitle': 'Past Perfect',
  'coverSub': 'Teil 1: die fr&uuml;here Vergangenheit',
  'chipLevel': 'B1 &middot; Grammatik',
  'chipCount': '22 Folien',
  'useEyebrow': 'Was es bedeutet', 'useTitle': 'Zwei Vergangenheiten, eine kam zuerst',
  'useH1': 'Die fr&uuml;here Handlung', 'useB1': 'Sie war schon vorbei, als die Geschichte ankam.',
  'useH2': 'Die sp&auml;tere Handlung', 'useB2': 'Die Geschichte selbst. Einfaches Past Simple.',
  'formEyebrow': 'Die Form', 'formTitle': 'Ein &lsquo;had&rsquo; f&uuml;r alle',
  'formA': 'Jedes Subjekt', 'formB': 'Gesprochen',
  'formNote': '<span class="formula">SUBJEKT + <em class="t-ppf">had</em> + <em class="pp">PAST PARTICIPLE</em></span><span class="dictum">EIN &lsquo;HAD&rsquo; F&Uuml;R ALLE &mdash; DANACH DIE DRITTE FORM!</span>',
  'edEyebrow': 'Die dritte Form', 'edTitle': 'Regelm&auml;&szlig;ige Verben: dasselbe -ed',
  'edA': 'Die meisten Verben', 'edB': 'Verben auf e', 'edC': 'Konsonant verdoppeln',
  'edNote': '<span class="formula">regelm&auml;&szlig;ig: Past Simple = dritte Form</span><span class="formula">study &rarr; <em class="pp">studied</em> &nbsp; carry &rarr; <em class="pp">carried</em></span>',
  'irEyebrow': 'Die dritte Form', 'irTitle': 'Unregelm&auml;&szlig;ig: dritte Form lernen',
  'irA': 'Eine andere dritte Form', 'irB': 'Wie die Vergangenheit', 'irC': 'be',
  'irNote': '<span class="formula">nach <em class="t-ppf">had</em>: <b><em class="pp">gone</em></b>, nie <em class="t-past">went</em></span>',
  'noEyebrow': 'Die Form', 'noTitle': 'Verneinen und fragen',
  'noA': 'Verneinen', 'noB': 'Fragen', 'noC': 'Fragew&ouml;rter',
  'noNote': '<span class="formula">SUBJEKT + <em class="t-ppf">had</em><em class="neg">n&rsquo;t</em> + <em class="pp">PAST PARTICIPLE</em></span><span class="formula"><em class="t-ppf">Had</em> + SUBJEKT + <em class="pp">PAST PARTICIPLE</em> ?</span>',
  'lineEyebrow': 'Was kam zuerst?', 'lineTitle': 'Fr&uuml;her, sp&auml;ter, jetzt',
  'lineRule': '<span class="formula">das Fr&uuml;here bekommt <em class="t-ppf">had</em> &mdash; <b>immer</b></span>',
  'sigEyebrow': 'Zeitsignale', 'sigTitle': 'W&ouml;rter, die die Reihenfolge festlegen',
  'sigH1': 'Zwischen den beiden Handlungen', 'sigB1': 'Ein Wort sagt, was zuerst kam.',
  'sigH2': 'Im Verb', 'sigB2': 'Diese stehen zwischen &lsquo;had&rsquo; und dem Partizip.',
  'qTitleFirst': 'Was geschah zuerst?', 'qTitleForm': 'W&auml;hle die richtige Form',
  'qTitleThird': '&lsquo;went&rsquo; oder &lsquo;gone&rsquo;?', 'qTitleAsk': 'Fragen und verneinen',
  'qTitleOrder': 'Welcher Satz setzt es zuerst?',
  'hint1': 'Such das &lsquo;had&rsquo;. Was danach kommt, geschah zuerst.',
  'hint2': 'Zwei Handlungen in der Vergangenheit. Die fr&uuml;here bekommt &lsquo;had&rsquo;.',
  'hint3': 'go &rarr; went &rarr; ? &nbsp; Die dritte Spalte der Verbtabelle.',
  'hint4': 'Welches Wort steht in einer Past-Perfect-Frage zuerst?',
  'hint5': 'Das &lsquo;not&rsquo; h&auml;ngt an &lsquo;had&rsquo;, und das Verb danach &auml;ndert sich nicht.',
  'hint6': 'Die Laterne ist das Fr&uuml;here. Welcher Satz gibt ihr &lsquo;had&rsquo;?',
  'sortTitle': 'Wie die Vergangenheit, oder anders?', 'sortHint': 'Klick eine dritte Form, dann ihre Gruppe.',
  'matchTitle': 'Finde die dritte Form', 'matchHint': 'Klick ein Verb, dann seine dritte Form.',
  'gap1Title': 'Schreib die dritte Form', 'gap1Hint': 'Schreib das Verb in Klammern in der dritten Form.',
  'gap2Title': 'Welches Wort passt?',
  'gap2Hint': 'eins ist Past Simple &mdash; lass es weg',
  'ord1Title': 'Bau den Satz', 'ord1Hint': 'Klick die W&ouml;rter in der richtigen Reihenfolge.',
  'resLow': 'Zur&uuml;ck zum Merksatz. Ein &lsquo;had&rsquo; f&uuml;r alle, und danach die dritte Form.',
  'resMid': 'Schau dir das Verb nach &lsquo;had&rsquo; noch einmal an. Dort liegen die Punkte.',
  'resStrong': 'Stark. Pr&uuml;f die Fehler, dann erz&auml;hl die Geschichte.',
  'resPerfect': 'Volle Punktzahl. Jetzt erz&auml;hl die Geschichte &mdash; das Fr&uuml;here zuerst.',
  'actTitle': 'Jetzt erz&auml;hl uns, was passiert war',
  'actSpeak1': 'Erz&auml;hl deinem Partner von einem Moment, als du irgendwo ankamst und schon etwas passiert war.',
  'actSpeak2': 'Stell deinem Partner drei Fragen, die mit &lsquo;Had you ever &hellip; before &hellip;?&rsquo; beginnen.',
  'actSpeak3': 'Nenn zwei Dinge, die heute Morgen beim Aufwachen noch nicht passiert waren.',
  'actWriteBrief': 'Schreib &uuml;ber einen Tag, der schiefging. Was war passiert, bevor du es gemerkt hast?',
  'actPlaceholder': 'By the time I arrived, …',
 },
 'es': {
  'partLink': 'Mapa de ruta &rarr;',
  'coverTitle': 'Past Perfect',
  'coverSub': 'Parte 1: el pasado anterior',
  'chipLevel': 'B1 &middot; Gram&aacute;tica',
  'chipCount': '22 diapositivas',
  'useEyebrow': 'Qu&eacute; significa', 'useTitle': 'Dos pasados, y uno fue primero',
  'useH1': 'La acci&oacute;n anterior', 'useB1': 'Ya hab&iacute;a terminado cuando lleg&oacute; la historia.',
  'useH2': 'La acci&oacute;n posterior', 'useB2': 'La historia misma. Pasado simple, sin m&aacute;s.',
  'formEyebrow': 'La forma', 'formTitle': 'Un solo &lsquo;had&rsquo; para todos',
  'formA': 'Todos los sujetos', 'formB': 'Hablado',
  'formNote': '<span class="formula">SUJETO + <em class="t-ppf">had</em> + <em class="pp">PAST PARTICIPLE</em></span><span class="dictum">UN &lsquo;HAD&rsquo; PARA TODOS &mdash; &iexcl;DESPU&Eacute;S, LA TERCERA FORMA!</span>',
  'edEyebrow': 'La tercera forma', 'edTitle': 'Verbos regulares: el mismo -ed',
  'edA': 'La mayor&iacute;a', 'edB': 'Verbos acabados en e', 'edC': 'Doblar la consonante',
  'edNote': '<span class="formula">regular: pasado simple = tercera forma</span><span class="formula">study &rarr; <em class="pp">studied</em> &nbsp; carry &rarr; <em class="pp">carried</em></span>',
  'irEyebrow': 'La tercera forma', 'irTitle': 'Irregulares: aprende la tercera forma',
  'irA': 'Una tercera forma distinta', 'irB': 'Igual que el pasado', 'irC': 'be',
  'irNote': '<span class="formula">tras <em class="t-ppf">had</em>: <b><em class="pp">gone</em></b>, nunca <em class="t-past">went</em></span>',
  'noEyebrow': 'La forma', 'noTitle': 'Negar y preguntar',
  'noA': 'Negar', 'noB': 'Preguntar', 'noC': 'Palabras interrogativas',
  'noNote': '<span class="formula">SUJETO + <em class="t-ppf">had</em><em class="neg">n&rsquo;t</em> + <em class="pp">PAST PARTICIPLE</em></span><span class="formula"><em class="t-ppf">Had</em> + SUJETO + <em class="pp">PAST PARTICIPLE</em> ?</span>',
  'lineEyebrow': '&iquest;Qu&eacute; fue primero?', 'lineTitle': 'Antes, despu&eacute;s, ahora',
  'lineRule': '<span class="formula">lo anterior lleva <em class="t-ppf">had</em> &mdash; <b>siempre</b></span>',
  'sigEyebrow': 'Se&ntilde;ales de tiempo', 'sigTitle': 'Palabras que marcan el orden',
  'sigH1': 'Entre las dos acciones', 'sigB1': 'Una palabra dice cu&aacute;l fue primero.',
  'sigH2': 'Dentro del verbo', 'sigB2': 'Van entre &lsquo;had&rsquo; y el participio.',
  'qTitleFirst': '&iquest;Qu&eacute; pas&oacute; primero?', 'qTitleForm': 'Elige la forma correcta',
  'qTitleThird': '&iquest;&lsquo;went&rsquo; o &lsquo;gone&rsquo;?', 'qTitleAsk': 'Preguntar y negar',
  'qTitleOrder': '&iquest;Qu&eacute; frase lo pone primero?',
  'hint1': 'Busca el &lsquo;had&rsquo;. Lo que va detr&aacute;s pas&oacute; primero.',
  'hint2': 'Dos acciones pasadas. La que fue primero lleva &lsquo;had&rsquo;.',
  'hint3': 'go &rarr; went &rarr; ? &nbsp; La tercera columna de la tabla de verbos.',
  'hint4': '&iquest;Qu&eacute; palabra va primero en una pregunta en past perfect?',
  'hint5': 'El &lsquo;not&rsquo; va con &lsquo;had&rsquo;, y el verbo de despu&eacute;s no cambia.',
  'hint6': 'La linterna es lo anterior. &iquest;Qu&eacute; frase le da &lsquo;had&rsquo;?',
  'sortTitle': '&iquest;Igual que el pasado, o distinta?', 'sortHint': 'Pulsa una tercera forma y luego su grupo.',
  'matchTitle': 'Une con la tercera forma', 'matchHint': 'Pulsa un verbo y luego su tercera forma.',
  'gap1Title': 'Escribe la tercera forma', 'gap1Hint': 'Escribe el verbo entre par&eacute;ntesis en su tercera forma.',
  'gap2Title': '&iquest;Qu&eacute; palabra encaja?',
  'gap2Hint': 'una es pasado simple: d&eacute;jala fuera',
  'ord1Title': 'Construye la frase', 'ord1Hint': 'Pulsa las palabras en el orden correcto.',
  'resLow': 'Vuelve al lema. Un &lsquo;had&rsquo; para todos, y despu&eacute;s la tercera forma.',
  'resMid': 'Mira otra vez el verbo que va tras &lsquo;had&rsquo;. Ah&iacute; est&aacute;n los puntos.',
  'resStrong': 'Muy bien. Revisa los fallos y luego cuenta la historia.',
  'resPerfect': 'Todo correcto. Ahora cuenta la historia: primero lo anterior.',
  'actTitle': 'Ahora cu&eacute;ntanos qu&eacute; hab&iacute;a pasado',
  'actSpeak1': 'Cu&eacute;ntale a tu pareja una vez que llegaste a un sitio y algo ya hab&iacute;a pasado.',
  'actSpeak2': 'Hazle a tu pareja tres preguntas que empiecen con &lsquo;Had you ever &hellip; before &hellip;?&rsquo;',
  'actSpeak3': 'Di dos cosas que a&uacute;n no hab&iacute;an pasado cuando te despertaste esta ma&ntilde;ana.',
  'actWriteBrief': 'Escribe sobre un d&iacute;a que sali&oacute; mal. &iquest;Qu&eacute; hab&iacute;a pasado antes de que te dieras cuenta?',
  'actPlaceholder': 'By the time I arrived, …',
 },
}

# ══════════════════════════════════════════════════════════════════════
# TRANSLATE ON REQUEST - keyed by the exact normalised English on screen
# ══════════════════════════════════════════════════════════════════════
TR_PAIRS = [
 # mc 1
 ('By the time we reached the vault, the guards had locked the gate.', 'Para cuando llegamos a la cámara, los guardias habían cerrado la puerta.', 'Als wir die Kammer erreichten, hatten die Wachen das Tor schon verschlossen.'),
 ('the guards locked the gate', 'los guardias cerraron la puerta', 'die Wachen verschlossen das Tor'),
 ('we reached the vault', 'llegamos a la cámara', 'wir erreichten die Kammer'),
 ('both at the same moment', 'ambas en el mismo momento', 'beide im selben Moment'),
 ('the sentence does not say', 'la frase no lo dice', 'der Satz sagt es nicht'),
 # mc 2
 ('Dale ______ the beacon before the storm came.', 'Dale ______ el faro antes de que llegara la tormenta.', 'Dale ______ das Leuchtfeuer, bevor der Sturm kam.'),
 ('has repaired', 'ha reparado (presente)', 'hat repariert (Gegenwart)'),
 ('had repaired', 'había reparado', 'hatte repariert'),
 ('had repair', '(forma base: no existe)', '(Grundform: gibt es nicht)'),
 ('had repairing', '(con -ing: no existe)', '(mit -ing: gibt es nicht)'),
 # mc 3
 ('When Audrey arrived, the others had already ______.', 'Cuando Audrey llegó, los demás ya se habían ______.', 'Als Audrey ankam, waren die anderen schon ______.'),
 ('went', 'fue, fueron (segunda forma)', 'ging, gingen (zweite Form)'),
 ('go', 'ir (forma base)', 'gehen (Grundform)'),
 ('gone', 'ido (tercera forma)', 'gegangen (dritte Form)'),
 ('going', 'yendo (-ing)', 'gehend (-ing)'),
 # mc 4
 ('______ the water reached the hall before you closed the door?', '¿______ el agua al vestíbulo antes de que cerraras la puerta?', '______ das Wasser die Halle erreicht, bevor du die Tür geschlossen hast?'),
 ('Did', '(pasado simple)', '(Past Simple)'),
 ('Has', '(presente perfecto)', '(Present Perfect)'),
 ('Was', '(pasado de ‘be’)', '(Vergangenheit von ‘be’)'),
 ('Had', '(past perfect)', '(Past Perfect)'),
 # mc 5
 ('They ______ the map, so they got lost.', 'No ______ el mapa, así que se perdieron.', 'Sie ______ die Karte nicht gelesen, also verliefen sie sich.'),
 (u"hadn’t readed", '(no existe)', '(gibt es nicht)'),
 (u"didn’t had read", '(no existe)', '(gibt es nicht)'),
 (u"hadn’t reading", '(no existe)', '(gibt es nicht)'),
 (u"hadn’t read", 'no habían leído', 'hatten nicht gelesen'),
 # mc 6
 ('Which sentence says the lantern was already dark when we came in?', '¿Qué frase dice que la linterna ya estaba apagada cuando entramos?', 'Welcher Satz sagt, dass die Laterne schon aus war, als wir hereinkamen?'),
 ('When we entered the vault, the lantern went out.', 'Cuando entramos en la cámara, la linterna se apagó.', 'Als wir die Kammer betraten, ging die Laterne aus.'),
 ('When we had entered the vault, the lantern went out.', 'Cuando habíamos entrado en la cámara, la linterna se apagó.', 'Als wir die Kammer betreten hatten, ging die Laterne aus.'),
 ('When we entered the vault, the lantern had gone out.', 'Cuando entramos en la cámara, la linterna se había apagado.', 'Als wir die Kammer betraten, war die Laterne ausgegangen.'),
 ('When we enter the vault, the lantern goes out.', 'Cuando entramos en la cámara, la linterna se apaga.', 'Wenn wir die Kammer betreten, geht die Laterne aus.'),
 # sort
 ('found', 'encontrado', 'gefunden'), ('made', 'hecho', 'gemacht'), ('built', 'construido', 'gebaut'),
 ('repaired', 'reparado', 'repariert'), ('seen', 'visto', 'gesehen'), ('been', 'sido, estado', 'gewesen'),
 ('taken', 'cogido', 'genommen'), ('eaten', 'comido', 'gegessen'),
 ('same as the past', 'igual que el pasado', 'wie die Vergangenheit'), ('different', 'distinta', 'anders'),
 # match
 ('see', 'ver', 'sehen'), ('be', 'ser, estar', 'sein'), ('take', 'coger', 'nehmen'),
 ('fall', 'caer', 'fallen'), ('find', 'encontrar', 'finden'), ('fallen', 'caído', 'gefallen'),
 # gap 1 (the engine strips the input, leaving before + after)
 ('Audrey had the beacon before dark. (repair)', 'Audrey había ______ el faro antes del anochecer. (reparar)', 'Audrey hatte das Leuchtfeuer vor Einbruch der Dunkelheit ______. (reparieren)'),
 ('(repair)', '(reparar)', '(reparieren)'),
 ('The bridge had by the time we came. (fall)', 'El puente se había ______ para cuando llegamos. (caer)', 'Die Brücke war ______, als wir kamen. (einstürzen)'),
 ('(fall)', '(caer)', '(einstürzen)'),
 ('We had the vault twice before. (see)', 'Ya habíamos ______ la cámara dos veces. (ver)', 'Wir hatten die Kammer schon zweimal ______. (sehen)'),
 ('(see)', '(ver)', '(sehen)'),
 # gap 2
 ('already', 'ya', 'schon'), ('yesterday', 'ayer', 'gestern'), ('yet', 'todavía, aún', 'noch (nicht)'), ('before', 'antes', 'bevor, vorher'),
 ('The guards had locked it. (done first)', 'Los guardias ______ lo habían cerrado. (hecho antes)', 'Die Wachen hatten es ______ verschlossen. (vorher erledigt)'),
 ('(done first)', '(hecho antes)', '(vorher erledigt)'),
 ('She had not found it . (still not done)', 'Ella ______ no lo había encontrado. (hasta entonces, no)', 'Sie hatte es ______ nicht gefunden. (bis dahin nicht)'),
 ('(still not done)', '(hasta entonces, no)', '(bis dahin nicht)'),
 ('It had cracked we looked. (order word)', 'Se había agrietado ______ de que miráramos. (palabra de orden)', 'Es war gerissen, ______ wir hinsahen. (Ordnungswort)'),
 ('(order word)', '(palabra de orden)', '(Ordnungswort)'),
 # order
 ('the bridge', 'el puente', 'die Brücke'), ('had fallen', 'se había caído', 'war eingestürzt'),
 ('we arrived .', 'llegamos .', 'wir kamen an .'),
 ('had', 'había', 'hatte'), ('you', 'tú', 'du'), ('the map', 'el mapa', 'die Karte'), ('before ?', 'antes ?', 'vorher ?'),
 # activation chips
 ('had gone', 'se había ido', 'war gegangen'), ('had already', 'ya había', 'hatte schon'),
 (u"hadn’t", 'no había', 'hatte nicht'), ('Had you', '¿Habías …?', 'Hattest du …?'),
 ('by the time', 'para cuando', 'als … schon'),
 # cover
 ('Past Perfect', 'Pluscuamperfecto', 'Plusquamperfekt'),
 # formulas
 ('SUBJECT + had + PAST PARTICIPLE', 'SUJETO + had + PARTICIPIO PASADO', 'SUBJEKT + had + PARTIZIP PERFEKT'),
 ("SUBJECT + hadn't + PAST PARTICIPLE", "SUJETO + hadn't + PARTICIPIO PASADO", "SUBJEKT + hadn't + PARTIZIP PERFEKT"),
 ('Had + SUBJECT + PAST PARTICIPLE ?', 'Had + SUJETO + PARTICIPIO PASADO ?', 'Had + SUBJEKT + PARTIZIP PERFEKT ?'),
 ('ONE ‘HAD’ FOR ALL — THIRD FORM AFTER IT!', 'UN ‘HAD’ PARA TODOS — ¡DESPUÉS, LA TERCERA FORMA!', 'EIN ‘HAD’ FÜR ALLE — DANACH DIE DRITTE FORM!'),
 ('regular: past simple = third form', 'regular: pasado simple = tercera forma', 'regelmäßig: Past Simple = dritte Form'),
 ('study → studied carry → carried', 'study → studied · carry → carried', 'study → studied · carry → carried'),
 ('after had: gone, never went', 'tras had: gone, nunca went', 'nach had: gone, nie went'),
 ('the earlier one takes had — always', 'lo anterior lleva had — siempre', 'das Frühere bekommt had — immer'),
 # teach chips
 ('the bridge had fallen', 'el puente se había caído', 'die Brücke war eingestürzt'),
 ('they had left', 'se habían ido', 'sie waren gegangen'),
 ('Dale arrived', 'Dale llegó', 'Dale kam an'),
 ('we found the note', 'encontramos la nota', 'wir fanden die Notiz'),
 ('before we arrived', 'antes de que llegáramos', 'bevor wir ankamen'),
 ('after it had closed', 'después de que cerrara', 'nachdem es geschlossen hatte'),
 ('by the time we came', 'para cuando vinimos', 'als wir kamen, schon'),
 ('when she looked', 'cuando ella miró', 'als sie hinsah'),
 ('had already left', 'ya se había ido', 'war schon gegangen'),
 ('had just closed', 'acababa de cerrar', 'hatte gerade geschlossen'),
 ('had never seen', 'nunca había visto', 'hatte nie gesehen'),
 ("hadn't arrived yet", 'aún no había llegado', 'war noch nicht angekommen'),
]
TR = {'es': {k: v for k, v, _ in TR_PAIRS}, 'de': {k: v for k, _, v in TR_PAIRS}}


PALETTE = """  --void          : #0e090a;
  --surface       : #1c1214;
  --surface2      : #291a1d;
  --border        : #786330;
  --text          : #f5f4f2;
  --text-dim      : #bfb7a3;
  --accent        : #dfaa2f;
  --accent-bright : #eec568;
  --accent-dim    : #96711c;
  --secondary     : #0f0507;
  --contrast      : #1dbfed;
"""

TOKENS = """  /* THE PAST PERFECT'S OWN COLOUR. #6E0B24 is the route map's maroon, kept
     at its system value for the TOKENS gate. It measures 1.5:1 on this deck's
     surface - unreadable - so the ink is lifted the way --t-past-ink was:
     L* raised in Lab with hue and chroma held (L* 23 -> 59), stopping at the
     first step past 5:1 on the card. 5.5:1 there. */
  --t-past-perfect: #6E0B24;
  --t-past-perfect-ink: #d66d77;
  /* THE PARTICIPLE IS PURPLE WHEREVER IT IS WRITTEN - docs/COLOUR-RULES.md,
     the same token the four perfect decks and the descent carry. */
  --mark-pp: #b39bf5;"""

ROLE_CSS = """em.t-ppf, b.t-ppf { color: var(--t-past-perfect-ink) !important; font-weight: 700; }
em.pp, b.pp { color: var(--mark-pp) !important; font-weight: 700; }
/* A ROLE COLOUR ON A SOLID ACCENT PLATE. The dictum is filled with the
   accent, and the participle violet measured 1.2:1 on the turquoise plate of
   the present perfect deck (docs/COLOUR-RULES.md). This deck's dictum carries
   no role span, so the rule is written here only so the next one copies it. */
.dictum em.pp, .dictum b.pp { color: #4B3B8A !important; }"""

CAMP = dict(
    chassis=CHASSIS,
    file='blockcamp-past-perfect.html',
    doctitle='Block Camp — Past Perfect 1a: The Earlier Past (B1) | Forbes English',
    description='Part 1: the earlier past — one thing had happened before another. Block Camp, unit 9.',
    hero=bg(18),
    palette=PALETTE,
    tokens=TOKENS,
    role_css=ROLE_CSS,
    slides=S,
    i18n=I18N,
    tr=TR,
    part_link='<a class="part-link" id="partLink" href="block-camp-map.html" data-i18n="partLink">Route map &rarr;</a>',
    # The catalogue row this deck gets in Supabase `lessons` (and the same
    # dict appended to tools/lessons.json). Camps 1-3 Part 1 are free; camp 9
    # is pro like every camp from 4 on.
    row=dict(file='blockcamp-past-perfect.html',
             title='Block Camp — Past Perfect 1a: The Earlier Past',
             level='B1', access='pro', deck=True, video=False,
             created_at='2026-09-04T00:00:00+00:00', sort_order=None),
    card='BlockCamp/past-perfect-1a.jpg',
)
