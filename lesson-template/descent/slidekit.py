# -*- coding: utf-8 -*-
"""Slide shapes for the descent, matching the published Part I markup exactly.

Every helper emits what a Part I deck already contains. Nothing here invents a
class: the shell, the engine and the checker all key off these names, and a
near-miss looks fine on the slide and fails silently in the gates.
"""


def head(eyebrow, title):
    return ('      <div class="slide-head"><div>\n'
            '        <div class="eyebrow">%s</div>\n'
            '        <h2 class="slide-title">%s</h2>\n'
            '      </div></div>' % (eyebrow, title))


def sec(kind, bg, side, vpos, inner):
    v = ' data-vpos="%s"' % vpos if vpos else ''
    return ('<section class="slide" data-type="%s" data-bg="%s" data-side="%s"%s>\n%s\n    </section>'
            % (kind, bg, side, v, inner))


def gloss(es, de):
    if not es and not de:
        return ''
    return ('<span class="sup" data-lang="es"><b>ES</b><span>%s</span></span>'
            '<span class="sup" data-lang="de"><b>DE</b><span>%s</span></span>' % (es, de))


def para(blocks, note=''):
    """A paradigm: the house's way of showing structure instead of a sentence."""
    out = ['      <div class="slide-body">', '        <div class="para">']
    for title, rows, g in blocks:
        out.append('          <div class="para-block">')
        out.append('            <div class="para-head">%s</div>%s' % (title, g))
        for subj, verb in rows:
            out.append('            <div class="para-row"><span class="para-subj">%s</span>'
                       '<span class="para-verb">%s</span></div>' % (subj, verb))
        out.append('          </div>')
    out.append('        </div>')
    if note:
        out.append('        <p class="para-note"><span class="formula">%s</span></p>' % note)
    out.append('      </div>')
    return '\n'.join(out)


def cards(pairs):
    """Two cards side by side - used for the active/passive contrast."""
    out = ['      <div class="slide-body">',
           '        <div class="cols" style="grid-template-columns:1fr 1fr">']
    for title, lead, examples, g in pairs:
        out.append('          <div class="card">')
        out.append('            <p class="prose"><strong>%s</strong></p>' % title)
        out.append('            <p class="prose" style="margin-top:8px;font-size:18px">%s</p>' % lead)
        ex = ''.join('<span>%s</span>' % e for e in examples)
        out.append('            <p class="prose dim" style="margin-top:8px;font-size:15px">'
                   '<span class="exlist">%s</span>%s</p>' % (ex, g))
        out.append('          </div>')
    out.extend(['        </div>', '      </div>'])
    return '\n'.join(out)


def mc(n, of, bg, side, vpos, title, stem, correct, wrong, es='', de='', why=''):
    """A multiple-choice slide.  `why` explains why the KEY is right.

    THE FEEDBACK ELEMENT IS WHAT MAKES ANY OF THIS VISIBLE, and it was missing.
    The engine's feedback() opens with

        const el = slide.querySelector('.feedback');
        if (!el) return;

    and this helper emitted no such element, so every call was a no-op: the
    per-distractor explanations went into the DOM as data-explain attributes
    and were never once shown, right and wrong alike produced no message at
    all, and a learner got no reason for anything. Eighteen written
    explanations per deck reaching nobody - the same defect as the pooled gap
    note in docs/HANDOFF.md, in a second place.

    `why` fills the slide-level data-explain, which the engine falls back to
    when the clicked option has none of its own (`ownExplain || el.dataset
    .explain`). So a right answer is explained by `why` and a wrong one by its
    own line, which is the behaviour the engine was always written for.
    """
    opts = ['        <button class="opt" data-correct>%s</button>' % correct]
    for text, w in wrong:
        opts.append('        <button class="opt" data-explain="%s">%s</button>'
                    % (w.replace('"', '&quot;'), text))
    fb = ('        <p class="feedback" data-explain="%s"></p>' % why.replace('"', '&quot;')
          if why else '        <p class="feedback"></p>')
    return sec('mc', bg, side, vpos,
        '      <div class="slide-head"><div>\n'
        '        <div class="eyebrow">Practice &middot; %d / %d</div>\n'
        '        <h2 class="slide-title">%s</h2>\n'
        '      </div></div>\n'
        '      <div class="slide-body">\n'
        '        <p class="q-stem">%s%s</p>\n'
        '        <div class="opts">\n%s\n        </div>\n'
        '%s\n'
        '      </div>' % (n, of, title, stem, gloss(es, de), '\n'.join(opts), fb))


def sort(bg, side, vpos, title, hint, bins, items, explain):
    rows = '\n'.join('          <span class="sort-item" data-bin="%d">%s</span>' % (b, t)
                     for b, t in items)
    return sec('sort', bg, side, vpos,
        head('Practice', title) + '\n'
        '      <div class="slide-body">\n'
        '        <p class="order-hint">%s</p>\n'
        '        <div class="sort" data-bins="%s">\n%s\n        </div>\n'
        '        <p class="feedback" data-explain="%s"></p>\n'
        '      </div>' % (hint, ' | '.join(bins), rows, explain.replace('"', '&quot;')))


def match(bg, side, vpos, title, hint, pairs, explain):
    rows = '\n'.join('        <div class="match-pair" data-term="%s" data-def="%s"></div>' % p
                     for p in pairs)
    return sec('match', bg, side, vpos,
        head('Practice', title) + '\n'
        '      <div class="slide-body">\n'
        '        <p class="prose dim" style="margin-bottom:14px;font-size:17px">%s</p>\n'
        '%s\n        <div class="match-grid"></div>\n'
        '        <p class="feedback" data-explain="%s"></p>\n'
        '      </div>' % (hint, rows, explain.replace('"', '&quot;')))


def gap(n, of, bg, side, vpos, title, hint, rows):
    out = []
    for before, answer, after, why, width in rows:
        out.append(
            '        <div class="card gap-row" style="padding:12px 16px">\n'
            '          <p class="q-stem" style="margin-bottom:0;font-size:19px">%s'
            '<input class="gap" data-answer="%s" aria-label="gap" style="width:%dpx">%s</p>\n'
            '          <p class="feedback" data-explain="%s"></p>\n'
            '        </div>' % (before, answer, width, after, why.replace('"', '&quot;')))
    # THE CHECK BUTTON IS NOT OPTIONAL, AND IT WAS MISSING FOR THE WHOLE LINE.
    # checkGaps() is reachable two ways: a [data-action="check"] click, or
    # Enter inside a gap. This helper emitted neither a button nor any other
    # affordance, so both gap slides scored only for a learner who guessed to
    # press Enter - six points a deck reports as earned whether or not anybody
    # could find them. Measured on station 9 before the fix: zero buttons on
    # the slide, and Enter marking all three gaps correct. The engine already
    # expects the button and disables it after marking (`if (btn)`), so this
    # is the slide catching up with the engine, not a new mechanism.
    return sec('gap', bg, side, vpos,
        '      <div class="slide-head"><div>\n'
        '        <div class="eyebrow">Practice &middot; %d / %d</div>\n'
        '        <h2 class="slide-title">%s</h2>\n'
        '      </div></div>\n'
        '      <div class="slide-body">\n'
        '        <p class="prose dim" style="margin-bottom:6px;font-size:16px">%s</p>\n%s\n'
        '        <div style="margin-top:12px">\n'
        '          <button class="btn" data-action="check">Check</button>\n'
        '        </div>\n'
        '      </div>' % (n, of, title, hint, '\n'.join(out)))


def order(bg, side, vpos, answer, explain):
    return sec('order', bg, side, vpos,
        head('Practice', 'Build the sentence') + '\n'
        '      <div class="slide-body">\n'
        '        <p class="order-hint">Click the words in the right order.</p>\n'
        '        <div class="order" data-answer="%s"></div>\n'
        '        <div style="margin-top:12px">\n'
        '          <button class="btn" data-action="check-order">Check</button>\n'
        '        </div>\n'
        '        <p class="feedback" data-explain="%s"></p>\n'
        '      </div>' % (answer, explain.replace('"', '&quot;')))


def results(bg, side, vpos):
    return sec('results', bg, side, vpos,
        '      <div class="slide-body" style="align-items:center;text-align:center">\n'
        '        <div class="score-big"><span id="scoreVal">0</span>'
        '<span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>\n'
        '        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>\n'
        '        <p class="prose dim" style="margin-top:14px">Now use it &rarr;</p>\n'
        '      </div>')


def activate(bg, title, chips, speak, write):
    chiphtml = '\n'.join('          <span class="bank-chip">%s</span>' % c for c in chips)
    sp = '\n'.join('              <li>%s</li>' % x for x in speak)
    wr = '\n'.join('              <li>%s</li>' % x for x in write)
    return ('<section class="slide" data-type="activate" data-bg="%s">\n' % bg +
        head('Activation', title) + '\n'
        '      <div class="slide-body">\n'
        '        <div class="act-target">\n'
        '          <span class="act-target-label">Use at least three:</span>\n%s\n'
        '        </div>\n'
        '        <div class="cols act-cols">\n'
        '          <div class="card act-card">\n'
        '            <div class="act-kind"><span class="act-icon">&#128483;</span><span>Speaking</span></div>\n'
        '            <p class="act-brief">In pairs. One minute each, then swap.</p>\n'
        '            <ul class="act-list">\n%s\n            </ul>\n'
        '          </div>\n'
        '          <div class="card act-card">\n'
        '            <div class="act-kind"><span class="act-icon">&#9997;</span><span>Writing</span></div>\n'
        '            <p class="act-brief">Six lines. Nobody is named.</p>\n'
        '            <ul class="act-list">\n%s\n            </ul>\n'
        '          </div>\n'
        '        </div>\n'
        '      </div>\n    </section>' % (chiphtml, sp, wr))
