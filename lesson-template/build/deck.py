# -*- coding: utf-8 -*-
"""Shared slide builders for the 16:9 deck house style.

Written after the fourth rebuild in a row re-typed the same six functions with
small drifts between them. Everything a lesson can differ in is an argument;
everything the house style fixes is in here, including the two rules that have
each shipped broken once and are now asserted at build time:

  * no multiple-choice key may be the longest option on its slide
  * no word bank may list the gap answers in gap order

Both are also measured by lesson-template/check-lesson.js. The assertions here
just fail earlier and say why.
"""
import html as _html
import re


# ── guards ─────────────────────────────────────────────────────────────
def assert_no_key_is_longest(mc, label='MC'):
    """mc: list of dicts with 'options' (list) and 'correct' (index)."""
    for n, q in enumerate(mc, 1):
        L = [len(_html.unescape(re.sub(r'<[^>]+>', '', o))) for o in q['options']]
        k = L[q['correct']]
        # The absolute floor matters as much as the comparison. Where the
        # options are single words from a closed set — can / could / must /
        # should — the key being two characters longer carries no information,
        # because the learner can see the whole set. Same floor as the checker.
        assert not (k == max(L) and L.count(max(L)) == 1 and k - sorted(L)[-2] >= 4), (
            '%s Q%d: the key is the only longest option (%d vs %d). Lengthen the '
            'distractors — never shorten the key.' % (label, n, k, sorted(L)[-2]))


def assert_bank_is_not_a_key(bank, answers_in_gap_order):
    # An answer may be a pipe-separated list of accepted spellings; the
    # bank shows the first. And fewer than two answers found in the bank
    # cannot be "in gap order" — an empty list made all() vacuously true
    # and failed every lesson whose answers were all alternatives.
    first = [a.split('|')[0] for a in answers_in_gap_order]
    pos = [bank.index(a) for a in first if a in bank]
    assert len(pos) < 2 or not all(x < y for x, y in zip(pos, pos[1:])), (
        'the word bank lists the gap answers in gap order (%s). Sort the bank '
        'instead — a bank in gap order is an answer key.' % pos)
    return pos


def esc(t):
    return t.replace('"', '&quot;')


def at(slide_html, stop, take=None):
    """Tag any slide with the rail stop it belongs to.

    A post-processor rather than an argument on all nine slide builders:
    the rail is one lesson format's idea, and threading it through every
    signature would tax thirty decks that will never use it."""
    extra = ' data-stop="%d"' % stop + (' data-take="%s"' % take if take else '')
    return slide_html.replace('<section class="slide"',
                              '<section class="slide"' + extra, 1)


def _bg(folder, bg):
    return ' data-bg="%s/%s"' % (folder, bg) if bg else ''


# ── slides ─────────────────────────────────────────────────────────────
def cover(logo, title, sub, chips):
    return '''
    <section class="slide is-active" data-type="cover">
      <div class="cover-inner">
        %s
        <h1 class="cover-title" data-i18n="coverTitle">%s</h1>
        <p class="cover-sub" data-i18n="coverSub">%s</p>
        <div class="cover-meta">
          %s
        </div>
        <div style="margin-top:34px">
          <button class="btn btn-solid btn-lg" data-action="next" data-i18n="btnStart">Begin →</button>
        </div>
      </div>
    </section>
''' % (logo, title, sub,
       "\n          ".join('<span class="chip" data-i18n="chip%s">%s</span>' % (k, v)
                           for k, v in chips))


def teach(eyebrow_key, eyebrow, title_key, title, cards, cols=None, folder='', bg=None):
    """cards: list of (head_key, head, body, note_key, note).

    A six-item card is (head_key, head, body_key, body, note_key, note):
    the body translates too. Worth having at A0-A2, where the rule needs
    to be readable in the learner's own language and only the *examples*
    have to stay in English; at B2 and above the five-item form, with the
    body left in English, is usually the right call."""
    grid = cols or '1fr ' * len(cards)
    cards = [c if len(c) == 6 else (c[0], c[1], None, c[2], c[3], c[4])
             for c in cards]
    body = "\n          ".join(
        '''<div class="card">
            <p class="prose"><strong%s>%s</strong></p>
            <p class="prose"%s style="margin-top:8px;font-size:18px">%s</p>%s
          </div>''' % (' data-i18n="%s"' % hk if hk else '', h,
                       ' data-i18n="%s"' % bk if bk else '', b,
                       ('\n            <p class="prose dim" style="margin-top:8px;font-size:15px"'
                        '%s>%s</p>' % (' data-i18n="%s"' % nk if nk else '', n)) if n else '')
        for hk, h, bk, b, nk, n in cards)
    return '''
    <section class="slide" data-type="teach"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:%s">
          %s
        </div>
      </div>
    </section>
''' % (_bg(folder, bg), eyebrow_key, eyebrow, title_key, title, grid.strip(), body)


def mc(i, total, q, eyebrow_key, eyebrow, title_key, title, folder='', bg=None,
       ctx=None, explains=None):
    """explains: optional list, one per option, of why THAT option is wrong.

    Without it the slide carries a single explanation, so a learner who picks
    a distractor is told why the key was right rather than why their answer
    was not. Six builders have now worked around that by injecting
    data-explain onto the buttons after calling this function.

    Pass None for an option to leave it to the slide-level explanation.

    Added in d11d5e1, removed by 807e19c on a stale base, restored here.
    Purely additive: a caller that does not pass it gets byte-identical
    output, and that is checked by rebuilding every deck.
    """
    if explains is not None and len(explains) != len(q['options']):
        raise AssertionError(
            'mc: %d explains for %d options — one per option, None to skip'
            % (len(explains), len(q['options'])))

    def _opt(n, o):
        attrs = ' data-correct' if n == q['correct'] else ''
        if explains is not None and explains[n]:
            attrs += ' data-explain="%s"' % esc(explains[n])
        return '<button class="opt"%s>%s</button>' % (attrs, o)

    opts = "\n          ".join(_opt(n, o) for n, o in enumerate(q['options']))
    return '''
    <section class="slide" data-type="mc"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="%s">%s</span> &middot; %d / %d</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
%s        <p class="q-stem">%s</p>
        <div class="opts">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (_bg(folder, bg), eyebrow_key, eyebrow, i, total, title_key, title,
       ('        <p class="q-ctx">%s</p>\n' % ctx) if ctx else '',
       q['stem'], opts, esc(q['why']))


def gap(i, total, rows, bank, eyebrow_key, eyebrow, title_key, title,
        folder='', bg=None, hint=None, hint_key=None, why=None, width=190,
        size=19):
    """rows: list of (sentence_with_BLANK_markers, [answers], why_or_None).

    A sentence with no `______` in it produces a gap-fill with nothing to
    fill: the slide renders, the engine counts a point for it, and no
    learner can ever score that point. It shipped that way on the B1
    modal-verbs deck — five "repair the sentence" items with no input box
    — because nothing failed loudly. Now it does."""
    out = []
    for sentence, answers, w in rows:
        assert sentence.count('______') >= len(answers), (
            'gap: "%s" has %d blank(s) for %d answer(s). A gap-fill with no '
            '______ marker renders an unanswerable question.'
            % (sentence[:60], sentence.count('______'), len(answers)))
        # A row may hold several blanks — "___ she ___ an alien?" is one
        # question, and splitting it into two rows destroys the exercise.
        # It did NOT work until this session: checkGaps() marked a row's
        # first input and stopped, while maxScore counted them all, so the
        # second blank was worth a point nobody could earn. The engine now
        # marks every input in the row and names every miss. What is still
        # worth guarding is the row with more answers than blanks, which is
        # a builder typo rather than a design choice.
        assert sentence.count('______') == len(answers) or not answers, (
            'gap: "%s" has %d blank(s) for %d answer(s) — they must match.'
            % (re.sub(r'<[^>]+>', '', sentence)[:60],
               sentence.count('______'), len(answers)))
        s = sentence
        for a in answers:
            s = s.replace('______',
                          '<input class="gap" data-answer="%s" aria-label="gap" '
                          'style="width:%dpx">' % (a, width), 1)
        out.append('''<div class="card gap-row" style="padding:12px 16px">
          <p class="q-stem" style="margin-bottom:0;font-size:%dpx">%%s</p>%%s
        </div>''' % size % (s, ('\n          <p class="feedback" data-explain="%s"></p>' % esc(w))
                     if w else ''))
    chips = ("\n        <div class=\"act-target\" style=\"margin-bottom:12px\">\n"
             "          <span class=\"act-target-label\" data-i18n=\"bankLabel\">Word bank:</span>\n"
             "          %s\n        </div>"
             % " ".join('<span class="bank-chip">%s</span>' % w for w in bank)) if bank else ''
    return '''
    <section class="slide" data-type="gap"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="%s">%s</span> &middot; %d / %d</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">%s%s
        %s%s
        <div style="margin-top:10px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
''' % (_bg(folder, bg), eyebrow_key, eyebrow, i, total, title_key, title, chips,
       ('\n        <p class="prose dim" style="margin-bottom:6px;font-size:16px" '
        'data-i18n="%s">%s</p>' % (hint_key, hint)) if hint else '',
       "\n        ".join(out),
       ('\n        <p class="feedback" data-explain="%s"></p>' % esc(why)) if why else '')


def match(pairs, eyebrow_key, eyebrow, title_key, title, hint_key, hint,
          why, folder='', bg=None):
    rows = "\n".join('        <div class="match-pair" data-term="%s" data-def="%s"></div>' % p
                     for p in pairs)
    return '''
    <section class="slide" data-type="match"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <p class="prose dim" style="margin-bottom:14px;font-size:17px" data-i18n="%s">
          %s
        </p>
%s
        <div class="match-grid"></div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (_bg(folder, bg), eyebrow_key, eyebrow, title_key, title, hint_key, hint,
       rows, esc(why))


def order(items, eyebrow_key, eyebrow, title_key, title, hint_key, hint, why,
          folder='', bg=None):
    assert not any('|' in t for t in items), 'order chunks must not contain "|"'
    return '''
    <section class="slide" data-type="order"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <p class="order-hint" data-i18n="%s">%s</p>
        <div class="order" data-answer="%s"></div>
        <div style="margin-top:12px">
          <button class="btn" data-action="check-order" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (_bg(folder, bg), eyebrow_key, eyebrow, title_key, title, hint_key, hint,
       " | ".join(items), esc(why))


def search(i, total, stem, items, eyebrow_key, eyebrow, title_key, title,
           why, limit=20, folder='', bg=None, stop=None, take=None):
    """Timed identify-the-object hunt. items: list of (name, svg, is_key).

    The names ride on the buttons but the engine keeps them hidden until
    the item is answered — a labelled picture is a reading task, not a
    vocabulary one. Exactly one item may be the key, and there has to be
    a real field to search: two objects is a coin toss with a clock on
    it."""
    keys = [n for n, _, k in items if k]
    assert len(keys) == 1, 'search: exactly one item is the key, got %s' % keys
    assert len(items) >= 4, 'search: %d objects is not a search' % len(items)
    cells = "\n          ".join(
        '<button class="find" data-name="%s"%s>%s</button>'
        % (esc(name), ' data-correct' if is_key else '', svg)
        for name, svg, is_key in items)
    return '''
    <section class="slide" data-type="search"%s%s%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="%s">%s</span> &middot; %d / %d</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">%s</p>
        <div class="search" data-limit="%d">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (_bg(folder, bg),
       ' data-stop="%d"' % stop if stop else '',
       ' data-take="%s"' % take if take else '',
       eyebrow_key, eyebrow, i, total, title_key, title, stem, limit, cells,
       esc(why))


def lock(code, stem, eyebrow_key, eyebrow, title_key, title, why,
         folder='', bg=None, stop=None):
    """Combination lock. The digits were earned one per section."""
    assert code.isdigit(), 'lock: the code must be digits'
    return '''
    <section class="slide" data-type="lock"%s%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem" style="text-align:center">%s</p>
        <div class="lock" data-code="%s"></div>
        <p class="feedback" style="text-align:center" data-explain="%s"></p>
      </div>
    </section>
''' % (_bg(folder, bg), ' data-stop="%d"' % stop if stop else '',
       eyebrow_key, eyebrow, title_key, title, stem, code, esc(why))


def results(next_key='resNext', next_text='Now use it →', folder='', bg=None):
    return '''
    <section class="slide" data-type="results"%s>
      <div class="slide-body" style="align-items:center;text-align:center">''' % _bg(folder, bg) + '''
        <div class="score-big"><span id="scoreVal">0</span><span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>
        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>
        <p class="prose dim" style="margin-top:14px" data-i18n="%s">%s</p>
      </div>
    </section>
''' % (next_key, next_text)


def activate(title, use_label, chips, speak_kind, speak_brief, speak_items,
             write_kind, write_brief, placeholder, folder='', bg=None):
    lis = "\n              ".join('<li data-i18n="actSpeak%d">%s</li>' % (n + 1, t)
                                 for n, t in enumerate(speak_items))
    return ('''
    <section class="slide" data-type="activate"%s>''' % _bg(folder, bg)) + '''
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="actEyebrow">Activation</div>
        <h2 class="slide-title" data-i18n="actTitle">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target">
          <span class="act-target-label" data-i18n="actUse">%s</span>
          %s
        </div>
        <div class="cols act-cols">
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">🗣</span><span data-i18n="actSpeakKind">%s</span></div>
            <p class="act-brief" data-i18n="actSpeakBrief">%s</p>
            <ul class="act-list">
              %s
            </ul>
          </div>
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">✍️</span><span data-i18n="actWriteKind">%s</span></div>
            <p class="act-brief" data-i18n="actWriteBrief">%s</p>
            <textarea class="act-input" id="actInput" data-i18n-ph="actPlaceholder" placeholder="%s" aria-label="Written response"></textarea>
            <div class="act-foot">
              <span class="act-count" id="actCount">0 words</span>
              <button class="btn act-copy" data-action="copy-writing" data-i18n="btnCopy">Copy</button>
            </div>
            <div class="act-print" id="actPrint" aria-hidden="true"></div>
          </div>
        </div>
        <div style="margin-top:14px;text-align:center">
          <button class="btn" data-action="restart" data-i18n="btnRestart">Start again</button>
        </div>
      </div>
    </section>
''' % (title, use_label,
       "\n          ".join('<span class="bank-chip">%s</span>' % c for c in chips),
       speak_kind, speak_brief, lis, write_kind, write_brief, placeholder)


# ── assembly ───────────────────────────────────────────────────────────
def assemble(tpl_path, out_path, slides, palette, title, i18n_module, langs=('en', 'de'),
             all_langs=('en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')):
    s = open(tpl_path, encoding='utf-8').read()
    a = s.index('    <!-- ── COVER ')
    b = s.index('    <!-- ── DECK CHROME ')
    s = s[:a] + slides + '\n' + s[b:]
    s = re.sub(r"  --hero: url\('sample-hero\.jpg'\);.*?--contrast      : #1ded49;",
               palette, s, count=1, flags=re.S)
    s = s.replace('<title>' + re.search(r'<title>(.*?)</title>', s, re.S).group(1) + '</title>',
                  '<title>%s</title>' % title, 1)
    block = 'const UI_I18N = {\n' + ",\n".join(
        ['  %s: %s' % (c, i18n_module.render(c)) for c in langs]
        + ['  %s: {}' % c for c in all_langs if c not in langs]) + '\n};'
    s = re.sub(r'const UI_I18N = \{.*?\n\};', block, s, count=1, flags=re.S)

    # The theme follows the palette, because it is the palette. Two shipped
    # decks once carried a light palette with no data-theme attribute, so the
    # light primitives never applied and their insets and hairlines — white on
    # cream — were invisible. It was a line each builder had to remember, and
    # two forgot. Added in d11d5e1, removed by 807e19c on a stale base,
    # restored here. A builder that still does the replace itself is harmless:
    # the attribute is already there, so its own replace finds nothing.
    m = re.search(r'--void\s*:\s*#([0-9a-fA-F]{6})', palette)
    if m:
        rgb = [int(m.group(1)[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
        f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
        if 0.2126 * f(rgb[0]) + 0.7152 * f(rgb[1]) + 0.0722 * f(rgb[2]) > 0.2:
            s = s.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)

    open(out_path, 'w', encoding='utf-8').write(s)
    return s


def logo_from(tpl_path):
    s = open(tpl_path, encoding='utf-8').read()
    return re.search(r'(<svg class="fe-logo".*?</svg>)', s, re.S).group(1)


def sort_slide(bins, items, eyebrow_key, eyebrow, title_key, title, hint_key,
               hint, why, folder='', bg=None):
    """items: list of (text, bin_index). bins: list of labels.

    Guards the two ways a sorting task stops being a task: an item that
    belongs to no bin, and a bin that never receives one — sorting into a
    box nothing goes in is a decision the learner cannot get wrong."""
    used = {b for _, b in items}
    assert all(0 <= b < len(bins) for _, b in items), \
        'sort: an item points at a bin that does not exist'
    assert used == set(range(len(bins))), \
        'sort: bin(s) %s receive no items — a bin nothing goes in is not a ' \
        'choice' % sorted(set(range(len(bins))) - used)
    assert len(items) >= 2 * len(bins), \
        'sort: %d items across %d bins is too thin to be worth a slide' % (
            len(items), len(bins))
    chips = "\n          ".join(
        '<span class="sort-item" data-bin="%d">%s</span>' % (b, t)
        for t, b in items)
    return '''
    <section class="slide" data-type="sort"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <p class="order-hint" data-i18n="%s">%s</p>
        <div class="sort" data-bins="%s">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (_bg(folder, bg), eyebrow_key, eyebrow, title_key, title, hint_key, hint,
       " | ".join(bins), chips, esc(why))
