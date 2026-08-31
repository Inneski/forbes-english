# -*- coding: utf-8 -*-
"""Station 9 — Active → Passive.

The first station on the way down. It teaches the SWAP and nothing else: the
tense-specific passives are stations 11 to 15 and they all rest on this one.

House style being obeyed here, all of it argued for on Part I:
  - structure before sentence: the paradigm and the formula do the teaching
  - one colour per job: BE is `aux` green in every passive on every slide,
    the participle is `pp` violet, and the accent is only ever the thing the
    slide is teaching
  - VERB, never BASE VERB
  - nothing scrolls; if it does not fit it splits
"""

BG = 'past-continuous-time-signals/%s'
PP = 'present-perfect-time-signals/%s'
PPC = 'present-perfect-continuous-time-signals/%s'
FS = 'future-simple-will/%s'


def head(eyebrow, title):
    return ('      <div class="slide-head"><div>\n'
            '        <div class="eyebrow">%s</div>\n'
            '        <h2 class="slide-title">%s</h2>\n'
            '      </div></div>' % (eyebrow, title))


def sec(kind, bg, side, vpos, inner, extra=''):
    v = ' data-vpos="%s"' % vpos if vpos else ''
    return ('<section class="slide" data-type="%s" data-bg="%s" data-side="%s"%s%s>\n%s\n    </section>'
            % (kind, bg, side, v, extra, inner))


def gloss(es, de):
    return ('<span class="sup" data-lang="es"><b>ES</b><span>%s</span></span>'
            '<span class="sup" data-lang="de"><b>DE</b><span>%s</span></span>' % (es, de))


def mc(n, bg, side, vpos, title, stem, correct, wrong, es='', de=''):
    opts = ['        <button class="opt" data-correct>%s</button>' % correct]
    for text, why in wrong:
        opts.append('        <button class="opt" data-explain="%s">%s</button>'
                    % (why.replace('"', '&quot;'), text))
    return sec('mc', bg, side, vpos,
        '      <div class="slide-head"><div>\n'
        '        <div class="eyebrow">Practice &middot; %d / 6</div>\n'
        '        <h2 class="slide-title">%s</h2>\n'
        '      </div></div>\n'
        '      <div class="slide-body">\n'
        '        <p class="q-stem">%s%s</p>\n'
        '        <div class="opts">\n%s\n        </div>\n'
        '      </div>' % (n, title, stem, gloss(es, de) if es else '', '\n'.join(opts)))


SLIDES = [
# ── 2 ── what it is ──────────────────────────────────────────────────────
sec('teach', BG % 'bg01.jpg', 'left', 'top',
    head('What it means', 'The same event, told the other way round') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="cols" style="grid-template-columns:1fr 1fr">\n'
    '          <div class="card">\n'
    '            <p class="prose"><strong>Active</strong> &mdash; you start with the doer</p>\n'
    '            <p class="prose" style="margin-top:8px;font-size:18px">Alex built the bridge.</p>\n'
    '            <p class="prose dim" style="margin-top:8px;font-size:15px"><span class="exlist">'
    '<span>the villagers <b>mined</b> the stone</span>'
    '<span>a creeper <b>broke</b> the wall</span></span>' + gloss('Alex construy&oacute; el puente.', 'Alex baute die Br&uuml;cke.') + '</p>\n'
    '          </div>\n'
    '          <div class="card">\n'
    '            <p class="prose"><strong>Passive</strong> &mdash; you start with the thing</p>\n'
    '            <p class="prose" style="margin-top:8px;font-size:18px">The bridge <em class="aux">was</em> <em class="pp">built</em>.</p>\n'
    '            <p class="prose dim" style="margin-top:8px;font-size:15px"><span class="exlist">'
    '<span>the stone <b><em class="aux">was</em> <em class="pp">mined</em></b></span>'
    '<span>the wall <b><em class="aux">was</em> <em class="pp">broken</em></b></span></span>' + gloss('El puente fue construido.', 'Die Br&uuml;cke wurde gebaut.') + '</p>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>'),

# ── 3 ── the swap ────────────────────────────────────────────────────────
sec('teach', PP % 'bg01.jpg', 'right', 'top',
    head('The swap', 'Three moves, and only three') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="para">\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">1 &middot; The object goes to the front</div>\n'
    '            <div class="para-row"><span class="para-subj">active</span><span class="para-verb">Alex built <b>the bridge</b></span></div>\n'
    '            <div class="para-row"><span class="para-subj">passive</span><span class="para-verb"><b>The bridge</b> ...</span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">2 &middot; The verb becomes BE + participle</div>\n'
    '            <div class="para-row"><span class="para-subj">active</span><span class="para-verb"><b>built</b></span></div>\n'
    '            <div class="para-row"><span class="para-subj">passive</span><span class="para-verb"><em class="aux">was</em> <em class="pp">built</em></span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">3 &middot; The doer can leave</div>\n'
    '            <div class="para-row"><span class="para-subj">keep it</span><span class="para-verb">... <b>by Alex</b></span></div>\n'
    '            <div class="para-row"><span class="para-subj">drop it</span><span class="para-verb">... and say nothing</span></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <p class="para-note"><span class="formula">THING + <em class="aux">BE</em> + <b>PAST PARTICIPLE</b> ( + by DOER )</span></p>\n'
    '      </div>'),

# ── 4 ── the participle ──────────────────────────────────────────────────
sec('teach', PPC % 'bg01.jpg', 'left', 'top',
    head('The form', 'The participle is the THIRD form') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="para">\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">Regular &mdash; add -ed</div>\n'
    '            <div class="para-row"><span class="para-subj">VERB</span><span class="para-verb">mine &rarr; mined &rarr; <em class="pp">mined</em></span></div>\n'
    '            <div class="para-row"><span class="para-subj">VERB</span><span class="para-verb">place &rarr; placed &rarr; <em class="pp">placed</em></span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">Irregular &mdash; learn the third one</div>\n'
    '            <div class="para-row"><span class="para-subj">VERB</span><span class="para-verb">build &rarr; built &rarr; <em class="pp">built</em></span></div>\n'
    '            <div class="para-row"><span class="para-subj">VERB</span><span class="para-verb">break &rarr; broke &rarr; <em class="pp">broken</em></span></div>\n'
    '            <div class="para-row"><span class="para-subj">VERB</span><span class="para-verb">take &rarr; took &rarr; <em class="pp">taken</em></span></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <p class="para-note"><span class="formula">the passive ALWAYS uses the <b>THIRD</b> form</span></p>\n'
    '      </div>'),

# ── 5 ── why ─────────────────────────────────────────────────────────────
sec('teach', FS % 'bg01.jpg', 'right', 'top',
    head('Why choose it', 'When the doer is not the point') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="para">\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">You do not know who</div>\n'
    '            <div class="para-row"><span class="para-subj"></span><span class="para-verb">My chest <em class="aux">was</em> <em class="pp">opened</em>.</span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">Everyone already knows who</div>\n'
    '            <div class="para-row"><span class="para-subj"></span><span class="para-verb">The village <em class="aux">was</em> <em class="pp">attacked</em> at night.</span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">The thing matters more</div>\n'
    '            <div class="para-row"><span class="para-subj"></span><span class="para-verb">The diamonds <em class="aux">were</em> <em class="pp">found</em> at level 12.</span></div>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>'),

# ── 6 ── by + agent ──────────────────────────────────────────────────────
sec('teach', PP % 'bg02.jpg', 'left', 'top',
    head('The doer', '&lsquo;by&rsquo; is optional, and usually left out') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="para">\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">Keep &lsquo;by&rsquo; when the doer is news</div>\n'
    '            <div class="para-row"><span class="para-subj">yes</span><span class="para-verb">The map <em class="aux">was</em> <em class="pp">drawn</em> <b>by a villager</b>.</span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">Drop it when it is not</div>\n'
    '            <div class="para-row"><span class="para-subj">no</span><span class="para-verb">The door <em class="aux">was</em> <em class="pp">locked</em>. <span class="dim">(by somebody &mdash; who cares)</span></span></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <p class="para-note"><span class="formula">most passives carry <b>NO</b> &lsquo;by&rsquo; at all</span></p>\n'
    '      </div>'),

# ── 7 ── no object, no passive ───────────────────────────────────────────
sec('teach', PPC % 'bg04.jpg', 'right', 'top',
    head('The limit', 'No object, no passive') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="para">\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">Has an object &rarr; can go passive</div>\n'
    '            <div class="para-row"><span class="para-subj">active</span><span class="para-verb">Steve <b>ate</b> the bread</span></div>\n'
    '            <div class="para-row"><span class="para-subj">passive</span><span class="para-verb">the bread <em class="aux">was</em> <em class="pp">eaten</em></span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">No object &rarr; cannot</div>\n'
    '            <div class="para-row"><span class="para-subj">active</span><span class="para-verb">Steve <b>slept</b></span></div>\n'
    '            <div class="para-row"><span class="para-subj">passive</span><span class="para-verb"><span class="dim">&mdash; there is nothing to put in front</span></span></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <p class="para-note"><span class="formula">arrive &middot; go &middot; sleep &middot; happen &middot; fall &mdash; <b>never</b> passive</span></p>\n'
    '      </div>'),

# ── 8 ── agreement trap ──────────────────────────────────────────────────
sec('teach', FS % 'bg04.jpg', 'left', 'top',
    head('The trap', 'BE agrees with the NEW subject') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="para">\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">One thing</div>\n'
    '            <div class="para-row"><span class="para-subj">the wall</span><span class="para-verb"><em class="aux">was</em> <em class="pp">broken</em></span></div>\n'
    '          </div>\n'
    '          <div class="para-block">\n'
    '            <div class="para-head">More than one</div>\n'
    '            <div class="para-row"><span class="para-subj">the walls</span><span class="para-verb"><em class="aux">were</em> <em class="pp">broken</em></span></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <p class="para-note"><span class="formula">the doer does <b>NOT</b> change <em class="aux">BE</em> &mdash; the thing in front does</span></p>\n'
    '      </div>'),

# ── 9-14 practice ────────────────────────────────────────────────────────
mc(1, BG % 'bg03.jpg', 'right', 'top', 'Choose the passive',
   'The bridge ______ last winter.', 'was built',
   [('built', 'That is the active. There is no BE, so the bridge is doing the building.'),
    ('was build', 'BE is right, but &lsquo;build&rsquo; is the first form. The passive needs the third.'),
    ('is built', 'That is a present passive, and &lsquo;last winter&rsquo; is finished time.')],
   'El puente ______ el invierno pasado.', 'Die Br&uuml;cke ______ letzten Winter.'),

mc(2, PP % 'bg04.jpg', 'left', 'top', 'Choose the passive',
   'The diamonds ______ at level 12.', 'were found',
   [('was found', '&lsquo;Diamonds&rsquo; is more than one, so BE is &lsquo;were&rsquo;.'),
    ('were find', '&lsquo;find&rsquo; is the first form. The third is &lsquo;found&rsquo;.'),
    ('found', 'No BE, so this says the diamonds did the finding.')],
   'Los diamantes ______ en el nivel 12.', 'Die Diamanten ______ auf Ebene 12.'),

mc(3, PPC % 'bg10.jpg', 'right', 'top', 'Active, or passive?',
   'Which sentence has the same meaning as &lsquo;A creeper broke the wall&rsquo;?',
   'The wall was broken by a creeper.',
   [('The wall broke a creeper.', 'That swaps who did what. Now the wall is the doer.'),
    ('The wall was break by a creeper.', 'The passive needs the third form: broken.'),
    ('A creeper was broken by the wall.', 'Both halves are the wrong way round.')],
   '&iquest;Cu&aacute;l significa lo mismo?', 'Welcher Satz bedeutet dasselbe?'),

mc(4, FS % 'bg05.jpg', 'left', 'top', 'Can it go passive?',
   'Which of these can become passive?', 'Alex opened the chest.',
   [('The sun rose.', 'No object. Nothing can move to the front.'),
    ('Steve slept badly.', 'No object, so there is no passive.'),
    ('They arrived at dawn.', '&lsquo;Arrive&rsquo; never takes an object.')],
   '&iquest;Cu&aacute;l puede ser pasiva?', 'Welcher Satz kann Passiv werden?'),

mc(5, PP % 'bg06.jpg', 'right', 'top', 'Which BE?',
   'The torches ______ along the tunnel.', 'were placed',
   [('was placed', '&lsquo;Torches&rsquo; is plural, so BE is &lsquo;were&rsquo;.'),
    ('were place', 'Third form: placed.'),
    ('placed', 'Without BE this is active, and torches cannot place themselves.')],
   'Las antorchas ______ por el t&uacute;nel.', 'Die Fackeln ______ im Tunnel.'),

mc(6, PPC % 'bg11.jpg', 'left', 'top', 'Leave it, or keep it?',
   'Which sentence is better English?', 'My chest was opened.',
   [('My chest was opened by somebody.', '&lsquo;By somebody&rsquo; adds nothing. That is exactly when to drop it.'),
    ('My chest was opened by a person.', 'Same problem: the doer is not news.'),
    ('My chest opened.', 'That says it opened itself.')],
   '&iquest;Cu&aacute;l suena mejor?', 'Welcher Satz klingt besser?'),

# ── 15 sort ──────────────────────────────────────────────────────────────
sec('sort', FS % 'bg08.jpg', 'right', 'top',
    head('Practice', 'Active, or passive?') + '\n'
    '      <div class="slide-body">\n'
    '        <p class="order-hint">Click a sentence, then click what it is.</p>\n'
    '        <div class="sort" data-bins="active | passive">\n'
    '          <span class="sort-item" data-bin="0">Alex built it</span>\n'
    '          <span class="sort-item" data-bin="0">a creeper broke the wall</span>\n'
    '          <span class="sort-item" data-bin="0">the villagers mined it</span>\n'
    '          <span class="sort-item" data-bin="0">Steve ate the bread</span>\n'
    '          <span class="sort-item" data-bin="1">it was built</span>\n'
    '          <span class="sort-item" data-bin="1">the wall was broken</span>\n'
    '          <span class="sort-item" data-bin="1">the stone was mined</span>\n'
    '          <span class="sort-item" data-bin="1">the bread was eaten</span>\n'
    '        </div>\n'
    '        <p class="feedback" data-explain="A passive always has BE plus the third form. No BE, no passive."></p>\n'
    '      </div>'),

# ── 16 match ─────────────────────────────────────────────────────────────
sec('match', PP % 'bg07.jpg', 'left', 'top',
    head('Practice', 'Match the active to its passive') + '\n'
    '      <div class="slide-body">\n'
    '        <p class="prose dim" style="margin-bottom:14px;font-size:17px">Click an active sentence, then click the passive that means the same.</p>\n'
    '        <div class="match-pair" data-term="They lit the torches" data-def="the torches were lit"></div>\n'
    '        <div class="match-pair" data-term="Alex took the map" data-def="the map was taken"></div>\n'
    '        <div class="match-pair" data-term="A creeper broke it" data-def="it was broken"></div>\n'
    '        <div class="match-pair" data-term="Somebody opened the door" data-def="the door was opened"></div>\n'
    '        <div class="match-pair" data-term="They found the diamonds" data-def="the diamonds were found"></div>\n'
    '        <div class="match-pair" data-term="Steve ate the bread" data-def="the bread was eaten"></div>\n'
    '        <div class="match-grid"></div>\n'
    '        <p class="feedback" data-explain="The object of the active is always the subject of the passive."></p>\n'
    '      </div>'),

# ── 17-18 gaps ───────────────────────────────────────────────────────────
sec('gap', PPC % 'bg15.jpg', 'right', 'top',
    '      <div class="slide-head"><div>\n'
    '        <div class="eyebrow">Practice &middot; 1 / 2</div>\n'
    '        <h2 class="slide-title">Write the participle</h2>\n'
    '      </div></div>\n'
    '      <div class="slide-body">\n'
    '        <p class="prose dim" style="margin-bottom:6px;font-size:16px">Type the verb in brackets in its third form.</p>\n'
    '        <div class="card gap-row" style="padding:12px 16px">\n'
    '          <p class="q-stem" style="margin-bottom:0;font-size:19px">The wall was <input class="gap" data-answer="broken" aria-label="gap" style="width:170px">. <span class="dim">(break)</span></p>\n'
    '          <p class="feedback" data-explain="Not &lsquo;broke&rsquo; &mdash; that is the second form."></p>\n'
    '        </div>\n'
    '        <div class="card gap-row" style="padding:12px 16px">\n'
    '          <p class="q-stem" style="margin-bottom:0;font-size:19px">The bread was <input class="gap" data-answer="eaten" aria-label="gap" style="width:170px">. <span class="dim">(eat)</span></p>\n'
    '          <p class="feedback" data-explain="eat &rarr; ate &rarr; eaten. The passive takes the third."></p>\n'
    '        </div>\n'
    '        <div class="card gap-row" style="padding:12px 16px">\n'
    '          <p class="q-stem" style="margin-bottom:0;font-size:19px">The stone was <input class="gap" data-answer="mined" aria-label="gap" style="width:170px">. <span class="dim">(mine)</span></p>\n'
    '          <p class="feedback" data-explain="Regular verb, so the third form is just -ed."></p>\n'
    '        </div>\n'
    '      </div>'),

sec('gap', FS % 'bg10.jpg', 'left', 'top',
    '      <div class="slide-head"><div>\n'
    '        <div class="eyebrow">Practice &middot; 2 / 2</div>\n'
    '        <h2 class="slide-title">&lsquo;was&rsquo;, or &lsquo;were&rsquo;?</h2>\n'
    '      </div></div>\n'
    '      <div class="slide-body">\n'
    '        <p class="prose dim" style="margin-bottom:6px;font-size:16px">Look at the thing in front, not at the doer.</p>\n'
    '        <div class="card gap-row" style="padding:12px 16px">\n'
    '          <p class="q-stem" style="margin-bottom:0;font-size:19px">The torches <input class="gap" data-answer="were" aria-label="gap" style="width:130px"> lit.</p>\n'
    '          <p class="feedback" data-explain="Torches is plural."></p>\n'
    '        </div>\n'
    '        <div class="card gap-row" style="padding:12px 16px">\n'
    '          <p class="q-stem" style="margin-bottom:0;font-size:19px">The door <input class="gap" data-answer="was" aria-label="gap" style="width:130px"> locked by the villagers.</p>\n'
    '          <p class="feedback" data-explain="One door. The villagers are the doer and change nothing."></p>\n'
    '        </div>\n'
    '        <div class="card gap-row" style="padding:12px 16px">\n'
    '          <p class="q-stem" style="margin-bottom:0;font-size:19px">The chests <input class="gap" data-answer="were" aria-label="gap" style="width:130px"> opened.</p>\n'
    '          <p class="feedback" data-explain="Chests is plural, so BE is were."></p>\n'
    '        </div>\n'
    '      </div>'),

# ── 19-20 order ──────────────────────────────────────────────────────────
sec('order', PP % 'bg12.jpg', 'right', 'top',
    head('Practice', 'Build the sentence') + '\n'
    '      <div class="slide-body">\n'
    '        <p class="order-hint">Click the words in the right order.</p>\n'
    '        <div class="order" data-answer="the bridge | was | built | in one night ."></div>\n'
    '        <div style="margin-top:12px">\n'
    '          <button class="btn" data-action="check-order">Check</button>\n'
    '        </div>\n'
    '        <p class="feedback" data-explain="The thing, then BE, then the third form."></p>\n'
    '      </div>'),

sec('order', PPC % 'bg18.jpg', 'left', 'top',
    head('Practice', 'Build the sentence') + '\n'
    '      <div class="slide-body">\n'
    '        <p class="order-hint">Click the words in the right order.</p>\n'
    '        <div class="order" data-answer="the map | was | drawn | by a villager ."></div>\n'
    '        <div style="margin-top:12px">\n'
    '          <button class="btn" data-action="check-order">Check</button>\n'
    '        </div>\n'
    '        <p class="feedback" data-explain="&lsquo;by&rsquo; and the doer come last, after the participle."></p>\n'
    '      </div>'),

# ── 21 results ───────────────────────────────────────────────────────────
sec('results', FS % 'bg11.jpg', 'left', 'top',
    '      <div class="slide-body" style="align-items:center;text-align:center">\n'
    '        <div class="score-big"><span id="scoreVal">0</span><span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>\n'
    '        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>\n'
    '        <p class="prose dim" style="margin-top:14px">Now use it &rarr;</p>\n'
    '      </div>'),

# ── 22 activate ──────────────────────────────────────────────────────────
'<section class="slide" data-type="activate" data-bg="%s">\n' % (PP % 'bg14.jpg') +
    head('Activation', 'Now say what was done') + '\n'
    '      <div class="slide-body">\n'
    '        <div class="act-target">\n'
    '          <span class="act-target-label">Use at least three:</span>\n'
    '          <span class="bank-chip">was built</span>\n'
    '          <span class="bank-chip">were found</span>\n'
    '          <span class="bank-chip">was broken</span>\n'
    '          <span class="bank-chip">was taken</span>\n'
    '          <span class="bank-chip">were lit</span>\n'
    '          <span class="bank-chip">by</span>\n'
    '        </div>\n'
    '        <div class="cols act-cols">\n'
    '          <div class="card act-card">\n'
    '            <div class="act-kind"><span class="act-icon">&#128483;</span><span>Speaking</span></div>\n'
    '            <p class="act-brief">In pairs. One minute each, then swap.</p>\n'
    '            <ul class="act-list">\n'
    '              <li>Describe a room you came back to. What had been moved?</li>\n'
    '              <li>Tell your partner three things in your town that were built before you were born.</li>\n'
    '              <li>Say what was taken, and do not say who took it.</li>\n'
    '            </ul>\n'
    '          </div>\n'
    '          <div class="card act-card">\n'
    '            <div class="act-kind"><span class="act-icon">&#9997;</span><span>Writing</span></div>\n'
    '            <p class="act-brief">Six lines. Nobody is named.</p>\n'
    '            <ul class="act-list">\n'
    '              <li>Write a report of a village after a raid, using only passives.</li>\n'
    '              <li>Then rewrite one line as active. Which one had to name somebody?</li>\n'
    '            </ul>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n    </section>',
]

STATION = dict(
    file='blockcamp-passive-intro.html',
    title='Passive Voice',
    sub='Station 9: the same event, told the other way round',
    level='B1',
    doctitle='Block Camp II — Passive 9: Active → Passive (B1) | Forbes English',
    hero=BG % 'bg01.jpg',
    slides=SLIDES,
)
