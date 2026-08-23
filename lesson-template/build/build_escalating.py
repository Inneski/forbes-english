# -*- coding: utf-8 -*-
"""Escalating a Complaint (C1) — reconstructed builder for a deck that shipped
without one.

The page went out on 2a15f20; the sandbox that wrote build_escalating.py and
i18n_escalating.py was reclaimed before either was committed, so for a while
forbes-escalating-a-complaint-c1.html was a generated file with no generator —
maintainable only by hand-editing, which house style says is a one-shot repair
that the next build overwrites. Everything below was lifted back out of the
shipped HTML: no stem, option, explanation, sort item, gap or chip is new, and
the intent is that a re-run reproduces what is already live.

The lesson. A junior at an interior-architecture practice (Marlowe Vane) is
paired with a colleague who uploads nothing until the night before a deadline
and then puts both names on the concept work; he has told the line manager she
will not collaborate, and the line manager will not take sides. The learner
writes the email that goes one level up. The language points are the ones that
survive being forwarded to the person complained about: evidence rather than
adjectives, a pattern rather than an incident, a named ask, the agentless
passive (<em>it has been suggested that</em>) for the counter-story, and the
distinction between a fact on the record and a claim about someone's intent.

Shape: 4 teach → 2 sort → 2 gap → 2 order → 8 mc → results → activate, 21
slides, 34 scored points. The engine scores a sort per item and a gap per
input, not per slide, so the twelve question slides are worth 16 + 8 + 2 + 8
rather than twelve.

Three things worth knowing before you change anything here.

* The hero is DesignPitch/podium.jpg, borrowed from another lesson, and the
  palette below is the mechanical output of

      python3 lesson-template/extract-palette.py DesignPitch/podium.jpg

  pasted verbatim. Swapping the hero is therefore a one-line change to F/HERO
  plus a re-run of that script and this builder; do not hand-tune a channel.

* Every option's data-explain rides on the mc(explains=…) argument, and the
  key's slot is None on purpose — the key is explained by the slide-level
  feedback, so a learner who picks a distractor is told what is wrong with
  their answer rather than what was right about somebody else's.

* Nine of the note strings that this builder emits are SHORTER than the value
  the same key carries in i18n_escalating's T['en'] — case3, case4, factNote1,
  factNote2, moves1-4 and proto2. That divergence is in the shipped page and is
  reproduced here rather than repaired; see the warning at the top of
  i18n_escalating.py for what it is and how to close it.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-escalating-a-complaint-c1.html'
F = 'DesignPitch'
HERO = 'podium.jpg'          # borrowed from the design-pitch lesson for now
BG = 'pair.jpg'              # second background, on the case file and activation

# Mechanically derived — the verbatim output of
#     python3 lesson-template/extract-palette.py DesignPitch/podium.jpg
# on this repo, whose contrast report reads PASS on every row (text on surface
# 15.63:1, accent on surface 4.72:1, the tightest of them). Never hand-pick a
# value in here; re-run the script instead.
#
# Five of these are one unit off the values in the page as shipped — border,
# accent, accent-bright, accent-dim and contrast each differ by 1 in a single
# channel. The script is deterministic on this machine, so that is a rounding
# difference in whatever Pillow the original sandbox had, not a hand-tune. The
# derived values are the ones recorded, because they are the ones the tool
# reproduces.
PALETTE = '''  --hero: url('%s/%s');

  --void          : #0e0d09;
  --surface       : #1c1b12;
  --surface2      : #28261a;
  --border        : #6d524c;
  --text          : #f5f2f2;
  --text-dim      : #bfa8a3;
  --accent        : #c56d5a;
  --accent-bright : #dc998a;
  --accent-dim    : #8c4738;
  --secondary     : #a8c0c1;
  --contrast      : #2bdea8;''' % (F, HERO)

# ── the teaching slides ────────────────────────────────────────────────
# (eyebrow_key, eyebrow, title_key, title, [(head_key, head, body, note_key,
# note)], bg). The body line is the quotable example and stays in English in
# both languages; the head and the note translate.
CASE = ('caseEyebrow', 'The case file', 'caseTitle',
        'Marlowe Vane, interior architecture &mdash; and the colleague you are paired with', [
    ('caseH1', 'The pattern',
     '<em>Nothing on the drive until the night before. Then both names on it.</em>',
     'case1', 'Three schemes running. Nothing appears on the shared drive from him until the night before the deadline, and then the concept work goes up under both names.'),
    ('caseH2', 'What he is good at',
     '<em>He reads a room, and he talks well in it.</em>',
     'case2', 'Clients like him, and they ask for him. That is real, and any complaint you make has to survive it being true.'),
    ('caseH3', 'The counter-story',
     '<em>&ldquo;She refuses to collaborate.&rdquo;</em>',
     'case3', 'You did stop sending him drafts &mdash; because sending them was costing you the authorship of them.'),
    ('caseH4', 'The blockage',
     '<em>&ldquo;It is teamwork. Get on with it.&rdquo;</em>',
     'case4', 'Your line manager has heard his version, will not take sides, and hands you his section at 48 hours&rsquo; notice.'),
], BG)

MOVES = ('movesEyebrow', 'Before you write anything', 'movesTitle',
         'Four moves that separate an escalation from a complaint', [
    ('movesH1', 'Evidence, not adjectives',
     '<em>21:40 on 14 May</em> &mdash; not <em>lazy</em>.',
     'moves1', 'Dates, file histories, who was in the room. <em>Unreliable</em> is a conclusion, and nobody asked you for conclusions.'),
    ('movesH2', 'The pattern, not the incident',
     '<em>Three schemes</em> &mdash; not <em>last Tuesday</em>.',
     'moves2', 'One occasion is a bad week. Three dated occasions are a way of working. Managers act on patterns.'),
    ('movesH3', 'A specific ask',
     '<em>Named owners at kick-off.</em>',
     'moves3', 'Say what decision you want made. An escalation with no ask is a complaint delivered higher up, and it comes back down.'),
    ('movesH4', 'Name the counter-story first',
     '<em>&ldquo;It has been suggested that&hellip;&rdquo;</em>',
     'moves4', 'Said first it is context. Said second it is a defence, and by then she has already heard his.'),
], None)

PROTO = ('protoEyebrow', 'Two rules that decide how you are heard', 'protoTitle',
         'Go through, not around &mdash; and leave the man standing', [
    ('protoH1', 'Through, not around',
     '<em>I raised this with Ruth on 19 May and we agreed a split; I am bringing it to you because the position is unchanged.</em>',
     'proto1', 'One date and one sentence is the whole move. Leave it out and her first question is not about him — it is why you did not take this to Ruth, and now you are the one explaining yourself.'),
    ('protoH2', 'Concede what is true',
     '<em>He is better with clients than I am, and I would want him kept on that side of it.</em>',
     'proto2', 'A complaint that says a colleague is bad at everything reads as personal &mdash; and the strength you leave out is the one your reader has seen for herself.'),
], None)

# The before/after rewrite. Both cards carry the same three grievances; only the
# right-hand one can be quoted back at you without damage.
FACT = ('factEyebrow', 'The single hardest rewrite', 'factTitle',
        'Write it so that it survives being forwarded to him', [
    ('factH1', 'What you want to send',
     '<em>He never does any work and takes the credit for mine. Now he is spreading lies about me, and Ruth does not care.</em>',
     'factNote1', 'Every claim is about character and intent. None of it can be checked, all of it can be denied.'),
    ('factH2', 'What you can be quoted on',
     '<em>On each of the last three schemes his first upload was after 21:00 on the day of the deadline. On 14 May the boards I posted on 2 May went to the client as joint work. I raised the split with Ruth on 19 May.</em>',
     'factNote2', 'Same three grievances, nothing softened. He can dispute what it means; not that it happened.'),
], None)

TEACH = [CASE, MOVES, PROTO, FACT]

# ── two sorts ──────────────────────────────────────────────────────────
# Both are 2 bins × 4 items. The first sorts on whether a line can be checked,
# the second on the line the whole lesson turns on: recorded fact against a
# claim about what the man intended.
SORT_A = dict(
    title_key='sortTitleA', title='Which of these belongs in the email?',
    hint_key='sortHintA', hint='Click a line, then click the box it belongs in.',
    bins=['Goes in the email', 'Leave it out'],
    items=[('The file history for the last three deadlines', 0),
           ('The date I raised it with Ruth', 0),
           ('The decision I am asking the firm to make', 0),
           ('One sentence on what he is better at', 0),
           ('What other people in the studio say about him', 1),
           ('My view of his character', 1),
           ('The word &ldquo;lies&rdquo;', 1),
           ('A hint that I might resign over it', 1)],
    why='The test is not whether a line is true, it is whether it can be <strong>checked</strong> and whether it points at a decision. Everything in the left-hand box does both. Everything in the right-hand box asks your reader to take your word for something, and the one she is least likely to take your word for is your reading of his character.')

SORT_B = dict(
    title_key='sortTitleB', title='Fact, or a claim about what he intended?',
    hint_key='sortHintB', hint='A claim about intent is the fastest way to lose a reader. Sort each line.',
    bins=['Fact on the record', 'Claim about intent'],
    items=[('No files were uploaded before 21:40 on 14 May', 0),
           ('The boards went to the client without my name', 0),
           ('Ruth moved his section to me on the Friday', 0),
           ('He has missed the internal deadline three times', 0),
           ('He is holding back to force my hand', 1),
           ('He set out to take the credit', 1),
           ('He wants me to look uncooperative', 1),
           ('He has no intention of ever contributing', 1)],
    why='The left-hand box is a record; the right-hand box is a theory about a man&rsquo;s mind. The theories may well be correct — that is not the point. They cannot be shown, they can all be denied in one line, and every one of them hands him the reply <em>that is not what I was thinking at all</em>, which is the only reply he needs.')

SORTS = [SORT_A, SORT_B]

# ── the vocabulary of escalation ───────────────────────────────────────
# One bank across both screens, each word used exactly once, so a learner who
# finishes screen one has narrowed screen two. Sorted alphabetically, which is
# also what keeps it out of gap order — see assert_bank_is_not_a_key.
BANK = ['attribution', 'concede', 'escalating', 'grievance', 'outset',
        'precedent', 'remit', 'undermine']

GAP_HINT = ('gapHint', 'One word per gap. Each word in the bank is used exactly once across the two screens.')

GAPS = [
    ([('I want to be clear that I am ______ this, not filing a formal grievance.', ['escalating'], None),
      ('The issue is the ______ of the concept boards, not who is the better designer.', ['attribution'], None),
      ('I would like the deliverables named and owned from the ______ of the next scheme.', ['outset'], None),
      ('Being handed his section at 48 hours&rsquo; notice sits outside my ______.', ['remit'], None)],
     'You <strong>escalate</strong> an issue and you <strong>file</strong> or <strong>raise</strong> a grievance — naming the difference tells your reader you have not started a formal process. <strong>Attribution</strong> is the noun for whose name goes on the work. <strong>From the outset</strong> is fixed: never <em>from the beginning of the outset</em>, and never <em>at the outset of</em> when you mean throughout. Your <strong>remit</strong> is what you were given to do; note it is uncountable in this sense — <em>outside my remit</em>, never <em>outside my remits</em>.'),
    ([('I am happy to ______ that he is far better than I am in front of a client.', ['concede'], None),
      ('I have no wish to ______ Ruth, and I would welcome her being in the room.', ['undermine'], None),
      ('If it is repeated on the next scheme it sets a ______ I cannot sustain.', ['precedent'], None),
      ('A formal ______ would be the next step, and I would rather not take it.', ['grievance'], None)],
     '<strong>Concede</strong> takes a <em>that</em>-clause and means giving ground you did not have to give — which is why it is worth more than <em>admit</em> here. To <strong>undermine</strong> someone is to weaken them from underneath, quietly; saying you have no wish to do it is how you signal you know that going over a manager&rsquo;s head can look like exactly that. You <strong>set</strong> a precedent and it is countable. A <strong>grievance</strong> is the formal procedure with a name — mentioning that you are not using it yet is a stronger move than using it.'),
]

# Narrower than deck.py's 190px default: eight of these gaps sit mid-sentence in
# a 19px stem and the row must not wrap.
GAP_WIDTH = 180

# ── the two sentences the email is built out of ────────────────────────
# Chunked at the joints being taught, never mid-phrase: the ask narrows one
# qualifier at a time, and the pre-empt separates the passive from what follows.
ORDERS = [
    dict(title_key='ordTitleA', title='The ask',
         hint_key='ordHintA', hint='Click the parts in order. This is the sentence the whole email exists to deliver.',
         items=['What I am asking for',
                'is a written split of deliverables',
                'at project kick-off',
                'with named owners',
                'and a date beside each one'],
         why='The ask goes at the front of its own sentence and then gets narrower with every phrase: <em>a split</em> → <em>written</em> → <em>at kick-off</em> → <em>named</em> → <em>dated</em>. By the end there is nothing left for anyone to interpret, which is the whole purpose. Put this sentence in the first paragraph as well as the last.'),
    dict(title_key='ordTitleB', title='The pre-empt',
         hint_key='ordHintB', hint='Click the parts in order. Say it before she hears it from him.',
         items=['I am aware',
                'it has been suggested',
                'that I am unwilling to collaborate',
                'and I would like to set out',
                'why I changed how I share drafts'],
         why='<strong>It has been suggested</strong> is an agentless passive doing real work: it puts the claim on the table without naming who made it, so your reader is not forced to defend anybody. <strong>I am aware</strong> in front of it says you are not wounded, and <strong>I would like to set out</strong> promises an explanation rather than a denial.'),
]

# ── eight versions of the same email ───────────────────────────────────
# The distractors are deliberately the same length as the key and wrong for a
# reason the lesson has taught — a verdict on the manager, an absolute, a hedge
# that is still a claim about intent, an ask with nothing in it. Per-option
# data-explain everywhere except the key, whose reasoning is the slide feedback.
QUESTIONS = [
    dict(
        stem='Anneke Brandt is the level above your line manager. Which opening keeps you inside the chain of command?',
        options=[
            'I have tried raising this with Ruth more than once and got nowhere, so I am coming to you.',
            'I raised this with Ruth on 19 May; I am bringing it to you as the position is unchanged.',
            'Ruth has refused to deal with this properly, so it now falls to you to sort the problem out.',
            'I hope you do not mind my writing to you directly rather than troubling Ruth with all of it.',
        ],
        correct=1,
        explains=[
            'Reads as a running battle. <em>Got nowhere</em> is a verdict on Ruth, and it invites Anneke to defend her.',
            None,
            '<em>Refused</em> is an accusation against your own manager, and <em>it falls to you</em> tells a director what her job is.',
            'Apologising for writing suggests you know you should not have. Show the route instead of excusing it.',
        ],
        why='Going <strong>through</strong> a level rather than around it is a date and a sentence, and it costs you nothing. The other three all make Ruth the subject — she failed, she refused, she must not be troubled — and the moment your reader is thinking about Ruth she has stopped thinking about the work.'),
    dict(
        stem='Which sentence still looks reasonable if Anneke forwards the whole email straight to him?',
        options=[
            'Tobias contributes nothing at concept stage and has never done so on any project of ours.',
            'Everyone on our floor knows perfectly well that Tobias leaves all of the concept work to me.',
            'Tobias appears to be fundamentally uninterested in ever doing his share of the concept work.',
            'The shared folder records no uploads from Tobias before 21:40 on three separate deadlines.',
        ],
        correct=3,
        explains=[
            '<em>Nothing</em> and <em>never</em> are absolutes, and one counter-example from him destroys the whole email.',
            'Recruiting the floor makes it studio politics. It also cannot be checked, which is the same problem twice.',
            '<em>Appears to be fundamentally uninterested</em> is hedged, but it is still a claim about what he wants.',
            None,
        ],
        why='A system record. He can argue about what it means; he cannot argue that it says something else. The other three are conclusions about him, and a conclusion forwarded to its subject reads as an attack whether or not it is accurate.'),
    dict(
        stem='An escalation has to end in a decision somebody can actually make. Which one of these is that?',
        options=[
            'I am asking for deliverables to be named and owned at kick-off, with a date beside each.',
            'I would like you to be aware of how this has been affecting me over the last few months.',
            'I would like something to be done about the way the work is being shared on this account.',
            'I want you to know that the current situation is not one I can carry on with much longer.',
        ],
        correct=0,
        explains=[
            None,
            '<em>Be aware</em> asks for nothing. Awareness is not an action, and nobody can be held to having had it.',
            '<em>Something</em> is the giveaway. If you cannot name the change, she has to design it, and she will not.',
            'True, but it is a statement about you rather than a request. It also reads as the opening of an ultimatum.',
        ],
        why='Named, owned, dated — she can say yes to it on Monday. <em>Be aware</em>, <em>something to be done</em> and <em>I cannot carry on</em> all leave the decision with her to invent, and a director with no decision in front of her sends the email back down to Ruth.'),
    dict(
        stem='&ldquo;He refuses to collaborate&rdquo; is already circulating. Which line deals with it best?',
        options=[
            'Whatever he has told you about my refusing to collaborate is, I am afraid, simply untrue.',
            'I would rather not respond to studio gossip, which I think probably speaks well enough for itself.',
            'It has been suggested that I will not collaborate. I did change how I share drafts.',
            'If anyone has said that I refuse to collaborate, I would like to know exactly who said it.',
        ],
        correct=2,
        explains=[
            'A flat denial invites a comparison of two accounts, and he has already given his to Ruth.',
            'Refusing to answer leaves the claim standing. Calling it gossip also tells a director how to weigh it.',
            None,
            'Asking who said it turns the email into an investigation of the studio, with you as the one investigating.',
        ],
        why='Named first, it is context and you control what comes next. The impersonal <strong>it has been suggested</strong> keeps the accusation off any one person, and <strong>I did change</strong> concedes the true half before anyone can produce it as evidence.'),
    dict(
        stem='One line concedes what he is genuinely better at. Which version does the job?',
        options=[
            'He is, I will admit, capable of being fairly personable when there are clients in the room.',
            'He is better with clients than I am and I would want him kept on that side of it.',
            'To be fair to him, he does at least manage to turn up and talk when it really matters.',
            'I have nothing against him personally and I am sure that he has his strengths somewhere.',
        ],
        correct=1,
        explains=[
            '<em>I will admit</em> and <em>capable of being</em> take the compliment back inside the same sentence.',
            None,
            '<em>At least manage to</em> is sarcasm. Read aloud in a meeting it does more damage than saying nothing.',
            'Generic goodwill with no content. <em>Somewhere</em> tells your reader you could not think of anything.',
        ],
        why='Specific, unqualified, and it names where he should stay — which quietly proposes the split you are asking for. A concession that costs you nothing is not a concession, and your reader has watched him in front of a client herself.'),
    dict(
        stem='Three of these you can put in front of anyone. Which one can you not evidence, however true it feels?',
        options=[
            'The boards I posted on 2 May went to the client on 14 May without my name anywhere on them.',
            'His first upload to the shared folder was timestamped 21:40 on the day of the deadline.',
            'Ruth reassigned his section of the drawings to me on the Friday before the deadline.',
            'He set out to take the credit for the concept work and he timed the upload to do it.',
        ],
        correct=3,
        explains=[
            'A date, a date and an absence. All three are checkable in about a minute.',
            'A timestamp is the strongest sentence in the whole email precisely because you did not write it.',
            'A fact about what Ruth did, with no adjective attached to why she did it.',
            None,
        ],
        why='<strong>Set out to</strong> and <strong>timed it</strong> are claims about intention, and intention is the one thing no file history will ever show. Put the same facts down without the motive and let your reader draw it herself — she will, and then it is her conclusion rather than your accusation.'),
    dict(
        stem='You want her to see the cost of leaving it alone. Which version is not a threat?',
        options=[
            'If the split stays as it is, December is met by one person working two weekends.',
            'If nothing changes I will have to think seriously about whether I stay at the firm.',
            'Unless the split of work is changed before December, I will decline the next scheme.',
            'Somebody is going to have to explain to the client why the drawings arrived late.',
        ],
        correct=0,
        explains=[
            None,
            'Once resignation is on the table the subject is your future, not the split, and she has to escalate it herself.',
            'An explicit ultimatum with a deadline on it. Even if you mean it, this is the version you say out loud later.',
            'Vague and slightly menacing. <em>Somebody</em> means her, and she will hear that.',
        ],
        why='The consequence lands on the <strong>project</strong>, not on her. A first conditional about the schedule is information she needs; a first conditional about what you will do next is a demand, and directors answer demands by removing the person making them.'),
    dict(
        stem='Ruth is copied in. How do you describe her handling of it without making an accusation?',
        options=[
            'Ruth has taken his side without ever once asking me for my version of what happened.',
            'Ruth does not want to know, and frankly I do not think she has read any of my emails.',
            'I raised the split with Ruth on 19 May. Her position is that it is a matter for us.',
            'I would rather not say what Ruth has or has not done, as you can judge all that yourself.',
        ],
        correct=2,
        explains=[
            '<em>Taken his side</em> is the accusation. You may believe it; you cannot show it, and she will deny it.',
            'Two accusations in one line, and <em>frankly</em> announces that you know it is one.',
            None,
            'A refusal to say, which reads as an invitation to think the worst. Directors notice the manoeuvre.',
        ],
        why='A date and her stated position, in her own terms, with no verdict on either. It is also the version Ruth can read without being ambushed — which matters, because she is copied in and you still have to work for her on Monday.'),
]

# ── activation ─────────────────────────────────────────────────────────
# The eight bank words plus the two sentence frames the order slides built, so
# the speaking task cannot be completed in B1 English.
CHIPS = ['escalate', 'raise it with', 'the attribution of', 'from the outset',
         'outside my remit', 'set a precedent', 'I would concede that',
         'what I am asking for is', 'it has been suggested that', 'I would welcome']

SPEAK = [
    'You are the junior. Your partner is Anneke Brandt, Associate Director. Her first question is: &ldquo;What is it you actually want me to do?&rdquo;',
    'Swap. Anneke opens with: &ldquo;Ruth tells me you will not work with him.&rdquo; Answer without attacking either of them.',
    'Now he is in the room. Say the same three things with him sitting there. What has to change, and what must not?',
    'Argue the other side: when is escalating the wrong move, and what does it cost you?',
]


def build():
    D.assert_no_key_is_longest(QUESTIONS, 'ESCALATION')
    for rows, _ in GAPS:
        D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in rows for a in aa])

    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Escalating a <em>Complaint</em>',
                'Taking a problem to the next level of management without becoming the problem',
                [('Level', 'C1 &middot; Workplace conflict'),
                 ('Focus', 'Evidence, register and the ask'),
                 ('Count', 'COUNT slides')])

        + "".join(D.teach(ek, e, tk, t, cards, folder=F, bg=bg)
                  for ek, e, tk, t, cards, bg in TEACH)

        + "".join(D.sort_slide(s['bins'], s['items'],
                               'sortEyebrow', 'Sort it before you send it',
                               s['title_key'], s['title'],
                               s['hint_key'], s['hint'], s['why'])
                  for s in SORTS)

        + "".join(D.gap(i + 1, len(GAPS), rows, BANK,
                        'gapEyebrow', 'The language of escalation',
                        'gapTitle', 'Complete the sentence',
                        hint=GAP_HINT[1], hint_key=GAP_HINT[0], why=why,
                        width=GAP_WIDTH)
                  for i, (rows, why) in enumerate(GAPS))

        + "".join(D.order(o['items'], 'ordEyebrow', 'Build the sentence',
                          o['title_key'], o['title'],
                          o['hint_key'], o['hint'], o['why'])
                  for o in ORDERS)

        + "".join(D.mc(i + 1, len(QUESTIONS), q,
                       'qEyebrow', 'Choose the version that works',
                       'qTitle', 'Which one would you actually send?',
                       explains=q['explains'])
                  for i, q in enumerate(QUESTIONS))

        + D.results('resNext', 'Recognising the register is the easy half. Now produce it &rarr;')

        + D.activate('Now make the case out loud', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs. Three minutes each, then swap roles and run it again with the second prompt.',
                     SPEAK,
                     'Writing &middot; 180&ndash;220 words',
                     'Write the email to Anneke Brandt. Three dated facts, one concession, one specific ask, and one line pre-empting the claim that you refuse to collaborate. No adjectives about his character.',
                     'Dear Anneke, I raised this with Ruth on 19 May and I am writing to you because…',
                     folder=F, bg=BG)
    )

    import i18n_escalating as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Escalating a Complaint: Taking It to the Next Level (C1)',
                   I, langs=('en', 'de'))
    # The chip has to say the number the checker reports, and the raw section
    # count is one higher than that — the template's authoring comment contains
    # the string '<section class="slide' too.
    n = s.count('<section class="slide')
    s = s.replace('COUNT slides', '%d slides' % (n - 1))
    # …and so does the cover chip's English translation, or the number changes
    # the moment a learner touches the switcher. The German chipCount is a word
    # this cannot rewrite ("Folien"); edit i18n_escalating if the count moves.
    s = s.replace('chipCount: "21 slides"', 'chipCount: "%d slides"' % (n - 1))
    open(OUT, 'w', encoding='utf-8').write(s)
    # The engine scores a sort per item and a gap per input, not per slide, so
    # two sorts and two gap screens are worth 24 of the 34 points between them.
    sort_pts = sum(len(x['items']) for x in SORTS)
    gap_pts = sum(len(r) for r, _ in GAPS)
    print('wrote %s — %d slides, %d scored (%d sort, %d gap, %d order, %d mc), '
          '%d bytes' % (OUT, n - 1,
                        sort_pts + gap_pts + len(ORDERS) + len(QUESTIONS),
                        sort_pts, gap_pts, len(ORDERS), len(QUESTIONS), len(s)))


if __name__ == '__main__':
    build()
