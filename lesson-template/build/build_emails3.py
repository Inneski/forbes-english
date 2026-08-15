# -*- coding: utf-8 -*-
"""Emails, Calls & Follow-ups (Part 3) — rebuilt as a deck.

The old page was a scrolling stack of three exercise blocks that ended on a
score. Everything in it survives — five scenarios, five collocations, five
office idioms — but it now runs one item to a screen, takes its palette from
the Grace Jones artwork, carries all ten languages, and ends by making the
learner actually write an email instead of recognising one.

The defect worth recording: every single one of the five multiple-choice keys
was the longest option on its slide. A learner could have scored five out of
five by always picking the longest and learning nothing about register. It is
the trap this topic invites, because the professional version genuinely is the
wordier one. All fifteen distractors were rewritten to match the key's length
while staying wrong for a reason the lesson teaches.

Gap 1 was repaired later. Two faults, one item:

  * Its feedback argued against `demand` and `reserve`, neither of which is in
    the word bank, and said nothing about `arrange` — which is the first chip
    in the bank and the answer a learner is most likely to try. The bank has
    ten chips and only five are ever the answer, so `arrange` is a live decoy
    with no rebuttal anywhere. "Request an appointment is the standard formal
    collocation" also implies `arrange an appointment` is not standard English,
    and it plainly is.
  * The stem contradicted itself. `for next week` fixes the timing while `at
    your earliest convenience` hands it to the reader, and the phrase was
    attached to the appointment when it belongs to their reply.

The repair keeps `request` as the key rather than switching the stem to
`Could we arrange a time to meet next week?`. That reads well in isolation, but
gap 3 is already `I would like to ______ a time to speak this week` keyed to
`schedule`, and `arrange` and `schedule` are interchangeable in both — two gaps
that can each be answered with the other's key is a worse defect than the one
being fixed. Asking the reader to supply the times is what makes `request`
uniquely right and rules out the two verbs that presume agreement.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-emails calls part3.html'
FOLDER = 'Emails3'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090d0e;
  --surface       : #121a1c;
  --surface2      : #1a2629;
  --border        : #aa5144;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #e87c6c;
  --accent-bright : #f5b1a7;
  --accent-dim    : #d03e28;
  --secondary     : #050e10;
  --contrast      : #1deda4;''' % FOLDER

from emails_mc import MC

GAPS = [
    ('I am writing to ______ an appointment; please let me know which times next week would suit you.',
     'request',
     '<strong>Request</strong> is what you do before there is anything to arrange: you ask, and they decide. '
     '<em>Arrange</em> and <em>schedule</em> both treat the appointment as already agreed and settle its details '
     '&mdash; and the second half of this sentence, which asks them to supply the times, rules that out. '
     '<em>Propose</em> would mean you were offering a time yourself.'),
    ('Please find ______ the documents we discussed during our call on Thursday.',
     'attached',
     '<strong>Please find attached</strong> is the fixed phrase for an email. <em>Enclosed</em> belongs to a paper letter, <em>appended</em> is academic, and <em>included</em> does not take this construction.'),
    ('I would like to ______ a time to speak this week — would Wednesday afternoon suit you?',
     'schedule',
     '<strong>Schedule a time</strong> is the professional collocation. <em>Arrange</em> also works but is vaguer; <em>fix</em> is informal and <em>book</em> is for rooms and travel, not calls.'),
    ('As ______ in my previous email, the deadline has been moved to the 15th.',
     'mentioned',
     '<strong>As mentioned in my previous email</strong> is the neutral way to point backwards. The others are defensible but far less common, and some carry an edge you probably do not want.'),
    ('I wanted to ______ up on the invoice we submitted two weeks ago.',
     'follow',
     '<strong>Follow up on</strong> is the fixed phrasal verb. <em>Chase</em> is informal and internal, <em>check up on</em> implies you are monitoring somebody, and <em>catch up</em> is social.'),
]
# Alphabetical, deliberately. Listing the answers in gap order turns the bank
# from a scaffold into an answer key — the learner reads straight down and
# never looks at the sentences. Sorting also keeps it stable across reloads,
# which a shuffle would not, so a printed hand-out matches the screen.
BANK = sorted(['request', 'attached', 'schedule', 'mentioned', 'follow',
               'propose', 'enclosed', 'arrange', 'stated', 'chase'])

MATCH = [
    ('As per my last email', 'Referring back to something already communicated'),
    ('Looping someone in', 'Adding a person to an email chain or conversation'),
    ('Keep me posted', 'A request to receive regular updates on progress'),
    ('Taking this offline', 'Moving a discussion away from a group setting'),
    ('Action point', 'A specific task assigned to someone after a meeting'),
]


def esc(t):
    return t.replace('"', '&quot;')


def mc_slide(i, q):
    opts = "\n          ".join(
        '<button class="opt"%s>%s</button>' % (' data-correct' if n == q['correct'] else '', o)
        for n, o in enumerate(q['options']))
    return '''
    <section class="slide" data-type="mc"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="qEyebrow">Scenario</span> &middot; %d / 5</div>
        <h2 class="slide-title" data-i18n="qTitle">Which one would you send?</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">%s</p>
        <div class="opts">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % ('', i, q['stem'], opts, esc(q['why']))


def gap_slide(i, items):
    rows = "\n        ".join(
        '''<div class="card gap-row">
          <p class="q-stem" style="margin-bottom:10px">%s</p>
          <p class="feedback" data-explain="%s"></p>
        </div>''' % (line.replace('______', '<input class="gap" data-answer="%s" aria-label="gap">' % ans),
                     esc(why))
        for line, ans, why in items)
    chips = " ".join('<span class="bank-chip">%s</span>' % w for w in BANK)
    return '''
    <section class="slide" data-type="gap">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="gapEyebrow">The exact word</span> &middot; %d / 3</div>
        <h2 class="slide-title" data-i18n="gapTitle">Business English runs on collocation</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target" style="margin-bottom:12px">
          <span class="act-target-label" data-i18n="bankLabel">Word bank:</span>
          %s
        </div>
        %s
        <div style="margin-top:12px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
''' % (i, chips, rows)


HEAD = '''
    <section class="slide is-active" data-type="cover">
      <div class="cover-inner">
        {LOGO}
        <h1 class="cover-title" data-i18n="coverTitle">Emails, Calls &amp; <em>Follow-ups</em></h1>
        <p class="cover-sub" data-i18n="coverSub">Part three: the openers, the collocations and the office idioms that carry a professional exchange</p>
        <div class="cover-meta">
          <span class="chip" data-i18n="chipLevel">B2 &middot; Part 3 of 3</span>
          <span class="chip" data-i18n="chipFocus">Business writing</span>
          <span class="chip" data-i18n="chipCount">15 slides</span>
        </div>
        <div style="margin-top:34px">
          <button class="btn btn-solid btn-lg" data-action="next" data-i18n="btnStart">Begin →</button>
        </div>
      </div>
    </section>

    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="shapeEyebrow">The shape of it</div>
        <h2 class="slide-title" data-i18n="shapeTitle">Four moves, in this order, every time</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose"><strong data-i18n="move1h">1 &middot; Open</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px" data-i18n="move1b">Warm, brief, no news: <em>I hope this email finds you well.</em></p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="move2h">2 &middot; State the purpose</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px" data-i18n="move2b">Immediately, in one line: <em>I am writing to follow up on&hellip;</em></p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="move3h">3 &middot; Make the ask</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px" data-i18n="move3b">Specific, and easy to say yes to: <em>Would Wednesday afternoon suit you?</em></p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="move4h">4 &middot; Close with a commitment</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px" data-i18n="move4b">Who does what, by when: <em>I will send a recap by end of day.</em></p>
          </div>
        </div>
      </div>
    </section>

    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="tempEyebrow">Register</div>
        <h2 class="slide-title" data-i18n="tempTitle">The same message at three temperatures</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr 1fr">
          <div class="card">
            <p class="prose"><strong data-i18n="temp1h">Too cold</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px">&ldquo;I sent the proposal three days ago and am still waiting.&rdquo;</p>
            <p class="prose dim" style="margin-top:8px;font-size:15px" data-i18n="temp1b">Counts the days. Puts the reader on the back foot.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="temp2h">About right</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px">&ldquo;I wanted to check whether you have had a chance to review it.&rdquo;</p>
            <p class="prose dim" style="margin-top:8px;font-size:15px" data-i18n="temp2b">Offers them a reason for the silence. Still asks.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="temp3h">Too warm</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px">&ldquo;Sorry to bother you again, I know how busy you must be!&rdquo;</p>
            <p class="prose dim" style="margin-top:8px;font-size:15px" data-i18n="temp3b">Apologises for existing. Buries the ask.</p>
          </div>
        </div>
      </div>
    </section>
'''

MATCH_SLIDE = '''
    <section class="slide" data-type="match">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="matchEyebrow">Office idiom</div>
        <h2 class="slide-title" data-i18n="matchTitle">Five phrases you will meet this week</h2>
      </div></div>
      <div class="slide-body">
        <p class="prose dim" style="margin-bottom:14px;font-size:17px" data-i18n="matchHint">
          Click a phrase, then click what it means. These are the ones that appear in emails without explanation and are never taught.
        </p>
%s
        <div class="match-grid"></div>
        <p class="feedback" data-explain="Note the tone on two of these: as per my last email is often read as pointed, and taking this offline can mean let us not do this in front of everyone."></p>
      </div>
    </section>
'''

TAIL = '''
    <section class="slide" data-type="results">
      <div class="slide-body" style="align-items:center;text-align:center">
        <div class="score-big"><span id="scoreVal">0</span><span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>
        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>
        <p class="prose dim" style="margin-top:14px" data-i18n="resNext">Recognising the language is half of it. Now produce it →</p>
      </div>
    </section>

    <section class="slide" data-type="activate">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="actEyebrow">Activation</div>
        <h2 class="slide-title" data-i18n="actTitle">Send the difficult one</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target">
          <span class="act-target-label" data-i18n="actUse">Use at least four:</span>
          {CHIPS}
        </div>
        <div class="cols act-cols">
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">🗣</span><span data-i18n="actSpeakKind">Discussion · in pairs</span></div>
            <p class="act-brief" data-i18n="actSpeakBrief">Run these as calls, not conversations. One of you is on a bad line.</p>
            <ul class="act-list">
              <li data-i18n="actSpeak1">Ask a client to repeat a figure you did not catch — twice, without saying &ldquo;what?&rdquo;</li>
              <li data-i18n="actSpeak2">End the call by confirming who does what and by when. Your partner must be able to repeat it back.</li>
              <li data-i18n="actSpeak3">Now the client is annoyed the report was late. Open your reply without defending yourself.</li>
            </ul>
          </div>
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">✍️</span><span data-i18n="actWriteKind">Writing · 120–160 words</span></div>
            <p class="act-brief" data-i18n="actWriteBrief">Third follow-up on an unpaid invoice. Still polite, but no longer pretending it is the first time.</p>
            <textarea class="act-input" id="actInput" data-i18n-ph="actPlaceholder" placeholder="Write your response here…" aria-label="Written response"></textarea>
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
    pos = [BANK.index(a) for _, a, _ in GAPS if a in BANK]
    assert not all(x < y for x, y in zip(pos, pos[1:])), \
        'the word bank lists the gap answers in gap order: %s' % pos


def build():
    _assert_bank_is_not_a_key()
    s = open(TPL, encoding='utf-8').read()
    logo = re.search(r'(<svg class="fe-logo".*?</svg>)', s, re.S).group(1)
    pairs = "\n".join('        <div class="match-pair" data-term="%s" data-def="%s"></div>' % p
                      for p in MATCH)
    chips = "\n          ".join('<span class="bank-chip">%s</span>' % w for w in
                               ['follow up on', 'please find attached', 'as mentioned',
                                'at your earliest convenience', 'keep me posted', 'action point'])
    slides = (HEAD.replace('{LOGO}', logo)
              + "".join(mc_slide(i + 1, q) for i, q in enumerate(MC))
              + gap_slide(1, GAPS[0:2]) + gap_slide(2, GAPS[2:4]) + gap_slide(3, GAPS[4:5])
              + (MATCH_SLIDE % pairs)
              + TAIL.replace('{CHIPS}', chips))

    a = s.index('    <!-- ── COVER ')
    b = s.index('    <!-- ── DECK CHROME ')
    s = s[:a] + slides + '\n' + s[b:]

    s = re.sub(r"  --hero: url\('sample-hero\.jpg'\);.*?--contrast      : #1ded49;",
               PALETTE, s, count=1, flags=re.S)
    s = s.replace('<title>' + re.search(r'<title>(.*?)</title>', s, re.S).group(1) + '</title>',
                  '<title>Emails, Calls &amp; Follow-ups — Part 3</title>', 1)

    import i18n_emails3 as I
    block = 'const UI_I18N = {\n' + ",\n".join(
        '  %s: %s' % (c, I.render(c)) for c in
        ['en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']) + '\n};'
    s = re.sub(r'const UI_I18N = \{.*?\n\};', block, s, count=1, flags=re.S)

    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
