# -*- coding: utf-8 -*-
"""Ordering Food & Drink (A1, Part 2) — rebuilt as a deck.

The old page was one long scroll with four exercise blocks stacked on top of
each other. Everything scored survives — six situations, the eight-blank
restaurant dialogue, six phrase/meaning pairs and five sentences to repair —
but it now runs one screen at a time, takes its palette from the bar artwork,
and opens with the language stated plainly instead of diving straight into
questions. At A1 the rules have to be on the wall before anyone is tested.

The defect worth recording: four of the six multiple-choice keys were the
longest option on their slide. That matters more here than in a C1 lesson,
because a beginner who does not yet know the phrase falls back on surface
cues, and length is the easiest cue there is. All the distractors were
lengthened to match; not one key was shortened.
"""
import re, sys

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-food-ordering-a1-part2.html'
FOLDER = 'FoodA1P2'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0b0e09;
  --surface       : #171c12;
  --surface2      : #21291a;
  --border        : #cd6553;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #f69f90;
  --accent-bright : #ffaa9b;
  --accent-dim    : #ea5940;
  --secondary     : #325569;
  --contrast      : #1deda7;''' % FOLDER

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from food_mc import MC

# ── The dialogue, in two halves. Each line is (speaker, text). ──────────
# ______ marks a blank; the answer follows in ANSWERS in the same order.
DIALOGUE_A = [
    ('Waiter', 'Good evening! Do you have a ______?'),
    ('You', 'Yes, for two. Could you ______ a good ______?'),
    ('Waiter', 'Our soup of the day is excellent. And how would you like your steak &mdash; rare, ______, or well done?'),
]
ANSWERS_A = ['reservation', 'recommend', 'starter', 'medium']

DIALOGUE_B = [
    ('You', 'Medium, please. Is service ______ in the bill?'),
    ('Waiter', 'Yes, it is. Would you like to see the ______ menu?'),
    ('You', 'Yes please. Could we ______ the chocolate cake? And could we have ______ bills?'),
]
ANSWERS_B = ['included', 'dessert', 'share', 'separate']

# Alphabetical, deliberately. A bank listed in gap order is an answer key:
# the learner reads straight down it and never looks at the sentences.
BANK = sorted(ANSWERS_A + ANSWERS_B)

WHY_A = ('A reservation is the booking; you recommend a dish to somebody; the starter is the '
         'first course; and the steak scale runs rare - medium - well done, with nothing else on it.')
WHY_B = ('Service included means the tip is already on the bill. Share takes no preposition here, '
         'and separate bills is the fixed phrase - not divided or single.')

MATCH = [
    ('Is this dish gluten-free?', 'Checking a dish is safe for a wheat intolerance'),
    ('Could I have it on the side?', 'Asking for a sauce or extra separately'),
    ('I&rsquo;d like to make a complaint.', 'Telling the waiter something is wrong'),
    ('Can we get a doggy bag?', 'Asking to take leftover food home'),
    ('What&rsquo;s the dish of the day?', 'Asking what today&rsquo;s special is'),
    ('We&rsquo;re ready to order now.', 'Telling the waiter you want to order'),
]

FIX = [
    ('Could you <s>bringing</s> me a glass of water, please?', 'bring',
     'After <em>Could you&hellip;</em> we use the plain infinitive with no <em>to</em> and no <em>-ing</em>: <strong>Could you bring me&hellip;?</strong>'),
    ('I&rsquo;m allergic <s>at</s> shellfish. Does this dish contain any?', 'to',
     'The preposition is fixed: <strong>allergic to</strong>. Worth learning as one word, because getting it wrong is the one mistake here that could actually matter.'),
    ('We&rsquo;d like a table for <s>fours</s> people, please.', 'four',
     'Numbers do not take an <em>-s</em> when they describe a noun: <strong>a table for four people</strong>.'),
    ('Excuse me, I think I <s>orderer</s> the pasta, not the risotto.', 'ordered',
     '<em>Order</em> is a regular verb, so the past simple is <strong>ordered</strong>.'),
    ('Is the service charge <s>include</s> in the price?', 'included',
     'This is a passive: <em>be</em> plus the past participle. <strong>Is the service charge included?</strong>'),
]


def esc(t):
    return t.replace('"', '&quot;')


def mc_slide(i, q, bg=None):
    opts = "\n          ".join(
        '<button class="opt"%s>%s</button>' % (' data-correct' if n == q['correct'] else '', o)
        for n, o in enumerate(q['options']))
    return '''
    <section class="slide" data-type="mc"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="qEyebrow">In the restaurant</span> &middot; %d / 6</div>
        <h2 class="slide-title" data-i18n="qTitle">What do you say?</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">%s</p>
        <div class="opts">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (' data-bg="%s/%s"' % (FOLDER, bg) if bg else '', i, q['stem'], opts, esc(q['why']))


def dialogue_slide(n, lines, answers, why, bg=None):
    """One half of the restaurant exchange, blanks as inputs."""
    pool = list(answers)
    rows = []
    for who, text in lines:
        out = text
        while '______' in out:
            out = out.replace(
                '______',
                '<input class="gap" data-answer="%s" aria-label="gap" style="width:190px">' % pool.pop(0), 1)
        rows.append(
            '<p class="prose" style="font-size:20px;margin-bottom:14px">'
            '<span class="dim" style="font-size:14px;letter-spacing:.08em;'
            'text-transform:uppercase;margin-right:10px">%s</span>%s</p>' % (who, out))
    rows = ['<div class="card">%s</div>' % "".join(rows)]
    chips = " ".join('<span class="bank-chip">%s</span>' % w for w in BANK)
    return '''
    <section class="slide" data-type="gap"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="gapEyebrow">The whole meal, in order</span> &middot; %d / 2</div>
        <h2 class="slide-title" data-i18n="gapTitle">Complete the conversation</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target" style="margin-bottom:12px">
          <span class="act-target-label" data-i18n="bankLabel">Word bank:</span>
          %s
        </div>
        %s
        <p class="feedback" data-explain="%s"></p>
        <div style="margin-top:10px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
''' % (' data-bg="%s/%s"' % (FOLDER, bg) if bg else '', n, chips,
       "\n        ".join(rows), esc(why))


def fix_slide(n, items, bg=None):
    rows = "\n        ".join(
        '''<div class="card gap-row" style="padding:12px 16px">
          <p class="q-stem" style="margin-bottom:0;font-size:18px">%s
            <span class="dim" style="font-size:15px;margin-left:10px" data-i18n="fixLabel">It should be:</span>
            <input class="gap" data-answer="%s" aria-label="correction" style="width:190px">
          </p>
          <p class="feedback" data-explain="%s"></p>
        </div>''' % (bad, ans, esc(why))
        for bad, ans, why in items)
    return '''
    <section class="slide" data-type="gap"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="fixEyebrow">One word out of place</span> &middot; %d / 2</div>
        <h2 class="slide-title" data-i18n="fixTitle">Repair the sentence</h2>
      </div></div>
      <div class="slide-body">
        <p class="prose dim" style="margin-bottom:4px;font-size:16px" data-i18n="fixHint">
          The crossed-out word is wrong. Type the word that belongs there.
        </p>
        %s
        <div style="margin-top:10px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
''' % (' data-bg="%s/%s"' % (FOLDER, bg) if bg else '', n, rows)


HEAD = '''
    <section class="slide is-active" data-type="cover">
      <div class="cover-inner">
        {LOGO}
        <h1 class="cover-title" data-i18n="coverTitle">Ordering Food &amp; <em>Drink</em></h1>
        <p class="cover-sub" data-i18n="coverSub">Part two: from the door to the bill, in the words people actually use</p>
        <div class="cover-meta">
          <span class="chip" data-i18n="chipLevel">A1 &middot; Part 2 of 2</span>
          <span class="chip" data-i18n="chipFocus">Restaurant English</span>
          <span class="chip" data-i18n="chipCount">16 slides</span>
        </div>
        <div style="margin-top:34px">
          <button class="btn btn-solid btn-lg" data-action="next" data-i18n="btnStart">Begin →</button>
        </div>
      </div>
    </section>

    <section class="slide" data-type="teach" data-bg="{F}/counter.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="shapeEyebrow">Before the questions</div>
        <h2 class="slide-title" data-i18n="shapeTitle">Three phrases carry the whole meal</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr 1fr">
          <div class="card">
            <p class="prose"><strong>I&rsquo;d like&hellip;</strong></p>
            <p class="prose" style="margin-top:8px;font-size:18px">&ldquo;I&rsquo;d like the soup, please.&rdquo;</p>
            <p class="prose dim" style="margin-top:8px;font-size:15px" data-i18n="p1">To order. Short for <em>I would like</em> — softer than <em>I want</em>, which sounds like a demand.</p>
          </div>
          <div class="card">
            <p class="prose"><strong>Could you&hellip;?</strong></p>
            <p class="prose" style="margin-top:8px;font-size:18px">&ldquo;Could you bring some water?&rdquo;</p>
            <p class="prose dim" style="margin-top:8px;font-size:15px" data-i18n="p2">To ask for something. The verb after it never changes: <em>bring</em>, not <em>to bring</em> or <em>bringing</em>.</p>
          </div>
          <div class="card">
            <p class="prose"><strong>Excuse me&hellip;</strong></p>
            <p class="prose" style="margin-top:8px;font-size:18px">&ldquo;Excuse me, my soup is cold.&rdquo;</p>
            <p class="prose dim" style="margin-top:8px;font-size:15px" data-i18n="p3">To get attention, and to open a complaint. Without it the same sentence sounds angry.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="slide" data-type="teach" data-bg="{F}/kitchen.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="menuEyebrow">The menu, in order</div>
        <h2 class="slide-title" data-i18n="menuTitle">The words on the card, and the ones you will be asked</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose"><strong data-i18n="courseH">The courses</strong></p>
            <p class="prose" style="margin-top:8px;font-size:19px">
              <strong>starter</strong> &rarr; <strong>main course</strong> &rarr; <strong>dessert</strong>
            </p>
            <p class="prose dim" style="margin-top:8px;font-size:16px" data-i18n="courseB">
              American menus say <em>appetizer</em> and <em>entrée</em> instead of <em>starter</em> and <em>main course</em>. Same meal.
            </p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="askH">Three questions you will be asked</strong></p>
            <p class="prose" style="margin-top:8px;font-size:18px">&ldquo;Still or sparkling?&rdquo;</p>
            <p class="prose" style="margin-top:4px;font-size:18px">&ldquo;How would you like your steak?&rdquo;</p>
            <p class="prose" style="margin-top:4px;font-size:18px">&ldquo;Anything else?&rdquo;</p>
            <p class="prose dim" style="margin-top:8px;font-size:16px" data-i18n="askB">
              Steak has exactly three answers: <em>rare</em>, <em>medium</em>, <em>well done</em>.
            </p>
          </div>
        </div>
      </div>
    </section>
'''

MATCH_SLIDE = '''
    <section class="slide" data-type="match" data-bg="{F}/pass.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="matchEyebrow">What it really means</div>
        <h2 class="slide-title" data-i18n="matchTitle">Six phrases you will hear or need</h2>
      </div></div>
      <div class="slide-body">
        <p class="prose dim" style="margin-bottom:14px;font-size:17px" data-i18n="matchHint">
          Click a phrase, then click what it means.
        </p>
%s
        <div class="match-grid"></div>
        <p class="feedback" data-explain="Two of these are worth memorising whole: is this dish gluten-free is the safest way to ask about any ingredient, and could I have it on the side works for every sauce, dressing and side dish on any menu."></p>
      </div>
    </section>
'''

TAIL = '''
    <section class="slide" data-type="results">
      <div class="slide-body" style="align-items:center;text-align:center">
        <div class="score-big"><span id="scoreVal">0</span><span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>
        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>
        <p class="prose dim" style="margin-top:14px" data-i18n="resNext">Now say it out loud. That is the part that transfers →</p>
      </div>
    </section>

    <section class="slide" data-type="activate">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="actEyebrow">Activation</div>
        <h2 class="slide-title" data-i18n="actTitle">Run the whole meal</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target">
          <span class="act-target-label" data-i18n="actUse">Use at least four:</span>
          {CHIPS}
        </div>
        <div class="cols act-cols">
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">🗣</span><span data-i18n="actSpeakKind">Roleplay · in pairs</span></div>
            <p class="act-brief" data-i18n="actSpeakBrief">One waiter, one customer. Then swap, and make the second run harder.</p>
            <ul class="act-list">
              <li data-i18n="actSpeak1">Arrive without a reservation. The waiter must find you a table anyway.</li>
              <li data-i18n="actSpeak2">Order a starter and a main. Ask the waiter to recommend one of them.</li>
              <li data-i18n="actSpeak3">Something is wrong with the food. Complain without once saying &ldquo;bad&rdquo;.</li>
              <li data-i18n="actSpeak4">Ask for separate bills, and check whether service is included.</li>
            </ul>
          </div>
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">✍️</span><span data-i18n="actWriteKind">Writing · 60–90 words</span></div>
            <p class="act-brief" data-i18n="actWriteBrief">Write the conversation you had, as a dialogue. Waiter first.</p>
            <textarea class="act-input" id="actInput" data-i18n-ph="actPlaceholder" placeholder="Waiter: Good evening — do you have a reservation?" aria-label="Written response"></textarea>
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
'''


def _assert_bank_is_not_a_key():
    order = ANSWERS_A + ANSWERS_B
    pos = [BANK.index(a) for a in order if a in BANK]
    assert not all(x < y for x, y in zip(pos, pos[1:])), \
        'the word bank lists the gap answers in gap order: %s' % pos
    return pos


def _assert_no_key_is_longest():
    import html as H
    for n, q in enumerate(MC, 1):
        L = [len(H.unescape(o)) for o in q['options']]
        k = L[q['correct']]
        assert not (k == max(L) and L.count(max(L)) == 1), \
            'Q%d: the key is the longest option (%d vs %s)' % (n, k, sorted(L)[-2])


def build():
    pos = _assert_bank_is_not_a_key()
    _assert_no_key_is_longest()
    s = open(TPL, encoding='utf-8').read()
    logo = re.search(r'(<svg class="fe-logo".*?</svg>)', s, re.S).group(1)
    pairs = "\n".join('        <div class="match-pair" data-term="%s" data-def="%s"></div>' % p
                      for p in MATCH)
    chips = "\n          ".join('<span class="bank-chip">%s</span>' % w for w in
                               ['I&rsquo;d like&hellip;', 'Could you&hellip;?', 'Excuse me',
                                'a table for four', 'still or sparkling',
                                'separate bills', 'the dish of the day'])
    bgs = [None, 'counter.jpg', None, 'kitchen.jpg', None, 'pass.jpg']
    slides = (HEAD.replace('{LOGO}', logo)
              + "".join(mc_slide(i + 1, q, bgs[i]) for i, q in enumerate(MC))
              + dialogue_slide(1, DIALOGUE_A, ANSWERS_A, WHY_A, 'counter.jpg')
              + dialogue_slide(2, DIALOGUE_B, ANSWERS_B, WHY_B, 'counter.jpg')
              + (MATCH_SLIDE % pairs)
              + fix_slide(1, FIX[:3], 'kitchen.jpg')
              + fix_slide(2, FIX[3:], 'kitchen.jpg')
              + TAIL.replace('{CHIPS}', chips))
    slides = slides.replace('{F}', FOLDER)

    a = s.index('    <!-- ── COVER ')
    b = s.index('    <!-- ── DECK CHROME ')
    s = s[:a] + slides + '\n' + s[b:]

    s = re.sub(r"  --hero: url\('sample-hero\.jpg'\);.*?--contrast      : #1ded49;",
               PALETTE, s, count=1, flags=re.S)
    s = s.replace('<title>' + re.search(r'<title>(.*?)</title>', s, re.S).group(1) + '</title>',
                  '<title>Ordering Food &amp; Drink — A1 Part 2</title>', 1)

    import i18n_food as I
    langs = ['en', 'de']
    block = 'const UI_I18N = {\n' + ",\n".join(
        ['  %s: %s' % (c, I.render(c)) for c in langs]
        + ['  %s: {}' % c for c in ['es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']]) + '\n};'
    s = re.sub(r'const UI_I18N = \{.*?\n\};', block, s, count=1, flags=re.S)

    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d fixes, bank positions %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC),
             len(ANSWERS_A) + len(ANSWERS_B), len(MATCH), len(FIX), pos, len(s)))


if __name__ == '__main__':
    build()
