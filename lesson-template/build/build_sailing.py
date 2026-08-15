# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar — gerunds and infinitives as a sea chart.

Not a Sherpa Tensing camp: this is its own page with its own coastline. It
borrows the machinery — the clickable diagram, the rule cards, the fourteen
checkpoints, the nine-language reveal — because the machinery is the house
style, and drops the mountain's progression gates because there is no mountain
here.

The teaching idea is that the verb lists are geography, not logic. You do not
reason your way to *avoid doing*; you learn the coast. What you can reason
about is the current (every preposition runs west to the -ing shore), the
island (the same verb, two meanings, depending on the channel) and the cape
that flies a false flag (the *to* in *look forward to* is a preposition).
"""
import re, sys, glob
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
sys.path.insert(0, 'lesson-template')
import sailing_map as M

# The camp harnesses rebuild camps ten to thirteen the moment they are
# imported, and those camps carry translation tags this page knows nothing
# about. Snapshot them, import, put them back exactly as they were.
_SNAP = {f: open(f, 'rb').read() for f in glob.glob('sherpa-tensing-camp-*.html')}
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES
from build_c11_12_13 import chart, fork, signals, questions, palette
for _f, _b in _SNAP.items():
    if open(_f, 'rb').read() != _b:
        open(_f, 'wb').write(_b)
        print('restored', _f)

OUT = 'sailing-the-seas-of-grammar.html'

# ─────────────────────────────────────────────────────────────────────
# the examples that carry a translation, in page order
# ─────────────────────────────────────────────────────────────────────
EX = []


def ex(html):
    """Register an example. rule_grid supplies the .ex wrapper itself, so leave
    a marker here and move the data-tr onto that wrapper after assembly —
    nesting .ex inside .ex draws the quote bar twice."""
    EX.append(html)
    return '\x01%d\x01%s' % (len(EX) - 1, html)


def exi(html):
    """The same, but the caller supplies the wrapper."""
    EX.append(html)
    return ('<p class="ex" data-tr="%d" style="margin:14px 0 0">%s</p>'
            % (len(EX) - 1, html))


HERO = hero(
    'Gerunds &amp; infinitives',
    'Sailing the Seas of Grammar',
    'Two shores face each other across one narrow strait. Every harbour on the western shore takes the '
    '<em>-ing</em> form; every harbour on the eastern shore takes <em>to</em> + infinitive. No rule of logic '
    'decides which verb belongs where &mdash; it is geography, and you learn it the way sailors learn a coast. '
    'What you <em>can</em> learn as rules are the three things in the water between them: the current, the '
    'island, and the cape flying a false flag.',
    M.chart('sail'))

# ═════════════════════════════════════════════════════════════════════
WEST = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">The western shore</div>
      <h2>When you take the <em>-ing</em> form</h2>
      <p class="chart-note" style="margin:-6px 0 18px">A gerund is a verb wearing a noun&#39;s coat. Once you see it as a noun, four of these six stop being rules and start being obvious &mdash; nouns go after prepositions, nouns go at the front of sentences, nouns are what you avoid and enjoy and finish.</p>
      ''' + rule_grid([
    ('After the verbs of Gerundia',
     'A closed list you learn rather than work out: <em>avoid, enjoy, finish, mind, suggest, admit, deny, keep, practise, risk, consider, miss, imagine, postpone, give up</em>.',
     ex('She <em>avoided answering</em> the question.')),
    ('After every preposition, without exception',
     'This is the current on the chart. If a preposition comes first, the verb after it can only be <em>-ing</em>.',
     ex('He left <em>without saying</em> goodbye.')),
    ('As the subject of a sentence',
     'English will not start a sentence with a bare verb, so the verb puts on its noun coat.',
     ex('<em>Sailing</em> in fog is dangerous.')),
    ('After <em>go</em>, for activities',
     'Sports and pastimes you go out and do. <em>Go sailing, go fishing, go shopping, go walking</em>.',
     ex('We <em>went swimming</em> before breakfast.')),
    ('After <em>no use, no point, worth</em>',
     'A small family of fixed expressions that all behave the same way.',
     ex('There&#39;s no point <em>arguing</em> with the tide.')),
    ('After a possessive, in careful English',
     '<em>my, your, his, the captain&#39;s</em>. Spoken English usually drops to the object form, and nobody minds.',
     ex('I don&#39;t mind <em>your borrowing</em> the chart.')),
]) + chart(
    'The harbours of Gerundia',
    'Grouped so they are easier to hold. Nothing joins a group for a reason &mdash; the groups are a memory aid, not a rule.',
    ['Group', 'Verbs', 'Example'],
    [['Stopping and avoiding', 'avoid &middot; give up &middot; finish &middot; quit &middot; postpone &middot; put off',
      'They <em>put off leaving</em> until the fog lifted.'],
     ['Liking and not liking', 'enjoy &middot; love &middot; like &middot; hate &middot; don&#39;t mind &middot; can&#39;t stand',
      'I <em>can&#39;t stand waiting</em> on the quay.'],
     ['Saying and not saying', 'admit &middot; deny &middot; suggest &middot; recommend &middot; mention &middot; report',
      'He <em>denied touching</em> the wheel.'],
     ['Carrying on', 'keep &middot; keep on &middot; carry on &middot; practise &middot; spend time',
      'She <em>kept checking</em> the compass.'],
     ['Thinking about it', 'consider &middot; imagine &middot; fancy &middot; risk &middot; involve &middot; miss',
      'We <em>considered turning</em> back.']]) + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
EAST = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The eastern shore</div>
      <h2>When you take <em>to</em> + infinitive</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The infinitive leans forward. Look at the verbs that take it &mdash; <em>want, hope, plan, decide, promise, agree, refuse, expect</em> &mdash; and almost every one of them is about something that has not happened yet. That is not a rule you can rely on, but it is a useful instinct while the list is still settling.</p>
      ''' + rule_grid([
    ('After the verbs of Infinitivia',
     'The other closed list: <em>want, decide, hope, refuse, promise, agree, manage, offer, learn, seem, afford, pretend, expect, plan, fail, choose</em>.',
     ex('They <em>decided to turn</em> back.')),
    ('After a verb <em>and its object</em>',
     'Somebody does something to somebody else: <em>tell, ask, want, expect, advise, allow, remind, warn, teach</em>.',
     ex('He <em>told me to wait</em> on deck.')),
    ('After an adjective',
     '<em>easy, hard, glad, ready, lucky, difficult, important</em> &mdash; the infinitive says what the adjective is about.',
     ex('It was <em>hard to read</em> the chart.')),
    ('To say why you did something',
     'The purpose infinitive. It answers <em>what for?</em> and it is the commonest infinitive of the lot.',
     ex('I climbed the mast <em>to see</em> the shore.')),
    ('After a question word',
     '<em>what, where, when, how, whether</em> + <em>to</em> + infinitive, when the question is unresolved.',
     ex('Nobody knew <em>what to do</em>.')),
    ('After <em>too</em> and <em>enough</em>',
     '<em>too</em> + adjective + <em>to</em>, or adjective + <em>enough</em> + <em>to</em>.',
     ex('The sea was <em>too rough to sail</em>.')),
]) + chart(
    'Verb, then object, then <em>to</em>',
    'These verbs need somebody in the middle. The pattern is fixed: you cannot say <em>he told to wait</em> &mdash; English wants to know who was told.',
    ['Verb', 'Pattern', 'Example'],
    [['tell', 'tell + somebody + to', 'The captain <em>told us to go</em> below.'],
     ['ask', 'ask + somebody + to', 'She <em>asked me to hold</em> the rope.'],
     ['want / expect', 'want + somebody + to', 'They <em>wanted him to stay</em> aboard.'],
     ['advise / warn', 'advise + somebody + to', 'He <em>warned them not to swim</em> there.'],
     ['remind / teach', 'remind + somebody + to', 'Remind me <em>to check</em> the fuel.']]) + chart(
    'The bare infinitive: no <em>to</em> at all',
    'A short list where the <em>to</em> disappears. Getting these wrong is the most audible error in this whole area, because <em>she let me to go</em> stops a listener dead.',
    ['After', 'Form', 'Example'],
    [['make &middot; let', 'no <em>to</em>', 'She <em>let the new hand take</em> the wheel.'],
     ['help', 'both are correct', 'He <em>helped me (to) tie</em> it off.'],
     ['modals', 'no <em>to</em>', 'We <em>must leave</em> before dark.'],
     ['had better', 'no <em>to</em>', 'You <em>had better check</em> the forecast.'],
     ['would rather', 'no <em>to</em>', 'I <em>would rather wait</em> for the tide.']]) + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
DIAGRAM = '''<div class="camp" id="order">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>Read the chart</h2>
      <div class="diagram-card">
        <p class="diagram-intro">Click a landmass. The strait is narrow and the two shores look alike from a distance, which is exactly the problem &mdash; nothing about the <em>meaning</em> of <em>avoid</em> and <em>refuse</em> tells you they belong to different coasts. The island between them is where the same verb serves both, and changes what it means depending on which channel you took to reach it. When the place names have done their job, switch the chart to <em>just the verbs</em> and it becomes the list you actually have to know.</p>
        <div class="name-bar" id="name-bar">
          <span class="name-label">Read the chart as</span>
          <button type="button" data-mode="place" class="on">Place names</button>
          <button type="button" data-mode="verb">Just the verbs</button>
        </div>
        <div class="diagram-stage">
          ''' + M.chart('sailb', clickable=True) + '''
        </div>
        <p class="chart-scroll-hint">Drag the chart sideways to read the far shore.</p>
        <div class="diagram-panels three">
          <div class="diagram-panel is-west" id="panel-gerund">
            <h4>Gerundia &middot; verb + <em>-ing</em></h4>
            <ul id="panel-gerund-list"></ul>
          </div>
          <div class="diagram-panel is-isle" id="panel-isle">
            <h4>Twofold Isle &middot; either</h4>
            <ul id="panel-isle-list"></ul>
          </div>
          <div class="diagram-panel is-east" id="panel-infin">
            <h4>Infinitivia &middot; <em>to</em> + infinitive</h4>
            <ul id="panel-infin-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
CAPE = '''<div class="camp" id="false-cape">
      ''' + MARK_CLOCK + '''
      <div class="camp-label">The False Cape</div>
      <h2>When <em>to</em> is not an infinitive</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Here is the single most useful thing on this page. In <em>look forward to</em>, <em>be used to</em> and their relatives, the word <em>to</em> is a <strong>preposition</strong>, not the front half of an infinitive &mdash; so the current applies and the verb after it can only be <em>-ing</em>. The cape looks like it belongs to the eastern shore. It does not.</p>
      ''' + chart(
    'The test that settles it',
    'Put <em>it</em> after the <em>to</em>. If the sentence still works, the <em>to</em> is a preposition, and whatever follows takes <em>-ing</em>.',
    ['Phrase', 'Does <em>&hellip; to it</em> work?', 'So you say'],
    [['look forward to', 'I look forward <strong>to it</strong>. &#10003;', 'looking forward <em>to seeing</em> you'],
     ['be used to', 'I&#39;m used <strong>to it</strong>. &#10003;', 'used <em>to sailing</em> at night'],
     ['object to', 'They objected <strong>to it</strong>. &#10003;', 'objected <em>to being</em> woken'],
     ['get round to', 'I&#39;ll get round <strong>to it</strong>. &#10003;', 'get round <em>to fixing</em> it'],
     ['when it comes to', 'When it comes <strong>to it</strong>&hellip; &#10003;', 'when it comes <em>to navigating</em>'],
     ['want', 'I want <strong>to it</strong>. &#10007;', 'want <em>to leave</em>']]) + chart(
    'The other traps on this coast',
    'All of them are prepositions wearing the same coat.',
    ['Phrase', 'Wrong', 'Right'],
    [['be used to', 'I&#39;m used to sail at night.', 'I&#39;m used <em>to sailing</em> at night.'],
     ['get used to', 'You&#39;ll get used to work nights.', 'You&#39;ll get used <em>to working</em> nights.'],
     ['look forward to', 'I look forward to hear from you.', 'I look forward <em>to hearing</em> from you.'],
     ['in addition to', 'In addition to carry the mail&hellip;', 'In addition <em>to carrying</em> the mail&hellip;'],
     ['confess to', 'He confessed to take the chart.', 'He confessed <em>to taking</em> the chart.']]) + '''
      <p class="chart-note" style="margin-top:16px"><strong>One more thing worth separating.</strong> <em>Used to</em> and <em>be used to</em> are different words that happen to look alike. <em>I used to sail</em> is a past habit and takes the infinitive. <em>I&#39;m used to sailing</em> is a state of familiarity and takes <em>-ing</em>. The difference is the verb <em>be</em>, and it is the whole difference.</p>
      ''' + exi('I <em>used to sail</em> here. &nbsp;&middot;&nbsp; I<em>&#39;m used to sailing</em> here.') + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
ISLE = fork(
    'Twofold Isle: the same verb, two meanings',
    'These verbs take both forms, and the form changes what the sentence means. This is the only part of gerunds '
    'and infinitives where getting it wrong changes the facts rather than just the grammar &mdash; which is why it '
    'is the part worth learning properly. The pattern underneath is consistent: the <em>-ing</em> form looks back '
    'at something real that happened, and the <em>to</em> form looks forward to something intended.',
    ['Verb', 'With <em>-ing</em> &mdash; looking back', 'With <em>to</em> &mdash; looking forward'],
    [['stop', 'ended the activity<br><em>She stopped reading.</em> (put the book down)',
      'paused in order to do something else<br><em>She stopped to read.</em> (halted, then read)'],
     ['remember', 'the memory of doing it<br><em>I remember posting it.</em> (I can picture it)',
      'not forgetting to do it<br><em>I remembered to post it.</em> (it got done)'],
     ['forget', 'no memory of doing it<br><em>I&#39;ll never forget seeing land.</em>',
      'failed to do it<br><em>I forgot to check the fuel.</em>'],
     ['try', 'experiment with a method<br><em>Try moving the aerial.</em> (see if that helps)',
      'attempt something difficult<br><em>Try to lift it.</em> (make the effort)'],
     ['regret', 'sorry about the past<br><em>I regret telling him.</em>',
      'sorry about what you must now say<br><em>We regret to inform you&hellip;</em>'],
     ['go on', 'continue the same thing<br><em>He went on talking.</em> (didn&#39;t stop)',
      'move to the next thing<br><em>He went on to talk about costs.</em>'],
     ['mean', 'involve, have as a consequence<br><em>This means leaving at four.</em>',
      'intend<br><em>I meant to leave at four.</em>'],
     ['need', 'passive sense &mdash; it needs doing<br><em>The sail needs mending.</em>',
      'active sense &mdash; somebody needs to act<br><em>You need to mend the sail.</em>']],
    'The reliable test: if you can put <em>somebody did it and I know about it</em> behind the sentence, take the '
    '<em>-ing</em> channel. If it has not happened yet, take <em>to</em>.',
    [('sailing-the-seas-of-grammar.html#quiz', 'Straight to the test &rarr;'),
     ('library.html', 'The lesson library')])

SHALLOWS = '''<div class="camp" id="shallows">
      ''' + MARK_FORK + '''
      <div class="camp-label">The Shallows</div>
      <h2>Where the two channels run together</h2>
      <p class="chart-note" style="margin:-6px 0 14px">South of the island the water shoals, the two channels merge, and for a short stretch it stops mattering which one you were in. After the verbs below <strong>both forms are correct and mean the same thing</strong>. This is not a third rule to learn &mdash; it is the absence of one, and it is the only water on the chart where a guess cannot sink you.</p>
      <p class="chart-note" style="margin:0 0 18px">That is worth saying plainly, because everything else on this page is a list you have to memorise. Here you do not. If you cannot remember whether <em>begin</em> is a western verb or an eastern one, the answer is that it does not matter.</p>
      ''' + chart(
    'The verbs in the Shallows',
    'The shoal is small, and this is all of it. Nothing else on the chart is safe to guess at.',
    ['Verb', 'Both of these are right', 'Any difference?'],
    [['begin &middot; start', 'It began raining. / It began to rain.', 'None whatsoever.'],
     ['continue', 'She continued walking. / to walk.', 'The infinitive reads slightly more formal in writing.'],
     ['like &middot; love &middot; hate', 'I like sailing. / I like to sail.',
      'A shade: <em>-ing</em> leans toward enjoying it, <em>to</em> toward choosing it.'],
     ['prefer', 'I prefer walking. / to walk.', 'None.'],
     ['can&#39;t bear', 'I can&#39;t bear waiting. / to wait.', 'None.'],
     ['bother', 'Don&#39;t bother waiting. / to wait.', 'None.'],
     ['intend &middot; propose', 'They intend selling. / to sell.', 'Both work; the infinitive is far commoner.'],
     ['attempt', 'He attempted swimming. / to swim.', 'Both work; the infinitive is far commoner.']]) + chart(
    'Four things worth knowing before you relax',
    'None of these makes the Shallows dangerous. They are the buoys, not the rocks.',
    ['The point', 'Not this', 'This'],
    [['Never stack two <em>-ing</em> forms',
      'It&#39;s starting raining.', 'It&#39;s starting <em>to rain</em>.'],
     ['After <em>would</em>, only the infinitive',
      'I&#39;d like sailing.', 'I&#39;d like <em>to sail</em>.'],
     ['Before a state, prefer the infinitive',
      'I began understanding.', 'I began <em>to understand</em>.'],
     ['Comparing two things: <em>-ing</em>, then <em>to</em>',
      'I prefer to walk than drive.', 'I prefer <em>walking to driving</em>.']]) + '''
      <p class="chart-note" style="margin-top:16px"><strong>The <em>would</em> one is the trap.</strong> <em>I like sailing</em> and <em>I&#39;d like to sail</em> sit one word apart and take different forms, because <em>would like</em> is not really the verb <em>like</em> any more &mdash; it is a polite way of saying <em>want</em>, and <em>want</em> lives on the eastern shore.</p>
      ''' + exi('I like <em>sailing</em>. &nbsp;&middot;&nbsp; I&#39;d like <em>to sail</em>.') + '''
      <p class="chart-note" style="margin-top:18px"><strong>And two verbs that feel as though they belong here but do not.</strong> <em>Enjoy</em> never takes the infinitive &mdash; <em>enjoy to swim</em> is simply wrong &mdash; and <em>want</em> never takes <em>-ing</em>. Being comfortable with a verb is not evidence that it lives in the Shallows. If it is not in the table above, it has a shore.</p>
      ''' + exi('I enjoy <em>swimming</em>. &nbsp;&middot;&nbsp; I want <em>to swim</em>.') + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
SIGNALS = signals(
    'Currents running west &mdash; take <em>-ing</em>',
    ['after any preposition', 'after <em>to</em> when it is a preposition', 'as the subject',
     'after <em>go</em> + activity', 'after <em>no use &middot; no point &middot; worth</em>',
     'after <em>spend / waste</em> + time'],
    'Ropes pulling east &mdash; take <em>to</em>',
    ['after an adjective', 'to say why (purpose)', 'after a question word',
     'after <em>too</em> and <em>enough</em>', 'after verb + object',
     'after <em>would like / love / hate</em>'],
    'One line to keep: a preposition is a current and it only runs one way. If you can find a preposition in '
    'front of the gap, stop looking for a rule &mdash; it is <em>-ing</em>.')

# ═════════════════════════════════════════════════════════════════════
QUIZ = [
    ('We should avoid ___ after dark in these waters.',
     'Cape Avoid sits on the western shore.', 'sailing',
     ['sailing', 'to sail', 'sail', 'to sailing'],
     'Avoid is a Gerundia verb, so it takes the -ing form. There is no reason for it beyond the geography &mdash; you learn the coast.'),
    ('They refused ___ the harbour fees.',
     'Refuse Rock is on the eastern shore.', 'to pay',
     ['to pay', 'paying', 'pay', 'for paying'],
     'Refuse belongs to Infinitivia: refuse to do. Compare deny, which belongs to the other shore and takes -ing.'),
    ('He left the ship without ___ anyone.',
     'What kind of word is <em>without</em>?', 'telling',
     ['telling', 'to tell', 'tell', 'having tell'],
     'Without is a preposition, and every preposition runs west. After any preposition the verb can only be -ing.'),
    ('I look forward to ___ you again next season.',
     'Try putting <em>it</em> after the <em>to</em>.', 'seeing',
     ['seeing', 'see', 'to see', 'have seen'],
     'This is the False Cape. &#8220;I look forward to it&#8221; works, so the to is a preposition, not an infinitive &mdash; and prepositions take -ing.'),
    ('She was tired, so she stopped ___ the chart and rubbed her eyes.',
     'Did she give up the activity, or pause in order to do it?', 'reading',
     ['reading', 'to read', 'read', 'for reading'],
     'Stop + -ing ends the activity: she had been reading and she stopped. Stop + to would mean she halted in order to start reading.'),
    ('Halfway up the mast he stopped ___ at the horizon.',
     'Why did he stop?', 'to look',
     ['to look', 'looking', 'look', 'for looking'],
     'Stop + to is the purpose infinitive: he interrupted the climb so that he could look. He had not been looking before.'),
    ('Remember ___ the log before you turn in.',
     'Has it happened yet?', 'to fill in',
     ['to fill in', 'filling in', 'fill in', 'to filling in'],
     'Remember + to is an instruction about the future: do not forget. Remember + -ing would be a memory of having already done it.'),
    ('I&#39;ll never forget ___ land for the first time.',
     'Is this a memory or an omission?', 'seeing',
     ['seeing', 'to see', 'see', 'to have see'],
     'Forget + -ing is about the memory of something that really happened. Forget + to means you failed to do it.'),
    ('It&#39;s no use ___ about the weather.',
     'A fixed expression from the western shore.', 'complaining',
     ['complaining', 'to complain', 'complain', 'for complain'],
     'It&#39;s no use, there&#39;s no point and it&#39;s worth all take -ing. They travel as a small family.'),
    ('The captain told ___ below.',
     'Who was told?', 'us to go',
     ['us to go', 'to go us', 'us going', 'that go us'],
     'Tell needs an object before the infinitive: tell somebody to do something. &#8220;The captain told to go&#8221; leaves a listener waiting for a name.'),
    ('She let the new hand ___ the wheel for an hour.',
     'One of the verbs that drops the <em>to</em>.', 'take',
     ['take', 'to take', 'taking', 'for taking'],
     'Let and make take the bare infinitive &mdash; no to. &#8220;She let him to take it&#8221; is the most audible error in this area.'),
    ('The fog was too thick ___ the buoy.',
     '<em>too</em> + adjective + what?', 'to see',
     ['to see', 'seeing', 'for seeing', 'that we see'],
     'Too + adjective is always followed by to + infinitive. The same goes for adjective + enough: warm enough to swim.'),
    ('After twenty years at sea, they are used to ___ in rough water.',
     'Is this a past habit, or being accustomed to something?', 'sleeping',
     ['sleeping', 'sleep', 'to sleep', 'have slept'],
     'Be used to means accustomed to, and the to is a preposition &mdash; so it takes -ing. Used to without be is a past habit: they used to sleep.'),
    ('The radio was dead, so she tried ___ the aerial &mdash; and it worked.',
     'Was this an experiment or an effort?', 'moving',
     ['moving', 'to move', 'move', 'for moving'],
     'Try + -ing is experimenting with a method to see whether it helps. Try + to is making an effort at something difficult: she tried to lift it.'),
]

# ═════════════════════════════════════════════════════════════════════
PANEL_GERUND = [
    'She <em>avoided answering</em>.',
    'He left <em>without saying</em> goodbye.',
    '<em>Sailing</em> in fog is dangerous.',
    'We <em>went swimming</em> at dawn.',
    'I look forward <em>to hearing</em> from you.',
]
PANEL_ISLE = [
    '<em>stopped reading</em> &middot; <em>stopped to read</em>',
    '<em>remember posting</em> &middot; <em>remembered to post</em>',
    '<em>try moving</em> it &middot; <em>try to lift</em> it',
    '<em>went on talking</em> &middot; <em>went on to talk</em>',
    'It <em>needs mending</em> &middot; You <em>need to mend</em> it.',
]
PANEL_INFIN = [
    'They <em>decided to turn</em> back.',
    'He <em>told me to wait</em>.',
    'It was <em>hard to read</em>.',
    'I climbed <em>to see</em> the shore.',
    'Too rough <em>to sail</em>.',
]

DIAGRAM_JS = '''var panelGerund = [
  %s
];
var panelIsle = [
  %s
];
var panelInfin = [
  %s
];

function renderList(id, items){
  var ul = document.getElementById(id);
  if (!ul) return;
  ul.innerHTML = "";
  items.forEach(function(txt){
    var li = document.createElement("li");
    li.innerHTML = txt;
    ul.appendChild(li);
  });
}
renderList("panel-gerund-list", panelGerund);
renderList("panel-isle-list", panelIsle);
renderList("panel-infin-list", panelInfin);

function pulseShape(el){
  el.style.transformOrigin = "center";
  el.animate(
    [{ opacity: 1 }, { opacity: 0.55 }, { opacity: 1 }],
    { duration: 380, easing: "ease-out" }
  );
}

// the chart reads two ways: as a coast you learn, or as the bare word list
// underneath it. Both charts on the page switch together.
function sailNames(mode){
  document.querySelectorAll(".sail-chart text.place-name").forEach(function(t){
    t.textContent = t.getAttribute(mode === "verb" ? "data-verb" : "data-place");
    t.style.fontStyle = mode === "verb" ? "italic" : "normal";
  });
  document.querySelectorAll("#name-bar button").forEach(function(b){
    b.classList.toggle("on", b.getAttribute("data-mode") === mode);
    b.setAttribute("aria-pressed", b.getAttribute("data-mode") === mode ? "true" : "false");
  });
}
document.querySelectorAll("#name-bar button").forEach(function(b){
  b.addEventListener("click", function(){ sailNames(b.getAttribute("data-mode")); });
});

// clicking a landmass lights the list that belongs to it. The False Cape
// lights Gerundia, because that is the whole point of the False Cape.
[["sailb-shape-gerund", "panel-gerund", "%s"],
 ["sailb-shape-isle",   "panel-isle",   "%s"],
 ["sailb-shape-infin",  "panel-infin",  "%s"],
 ["sailb-shape-false",  "panel-gerund", "%s"]].forEach(function(pair){
  var el = document.getElementById(pair[0]);
  if (!el) return;
  var activate = function(){
    pulseShape(el);
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    var panel = document.getElementById(pair[1]);
    if (panel){
      panel.style.outline = "2px solid " + pair[2];
      panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){
    if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); }
  });
});

''' % (",\n  ".join('"%s"' % e for e in PANEL_GERUND),
       ",\n  ".join('"%s"' % e for e in PANEL_ISLE),
       ",\n  ".join('"%s"' % e for e in PANEL_INFIN),
       M.G_LAND, M.T_LAND, M.I_LAND, M.G_LAND)

# ═════════════════════════════════════════════════════════════════════
EXTRA_CSS = '''
  /* ── the sea chart ── */
  .diagram-panels.three{grid-template-columns:repeat(3,1fr);}
  @media (max-width:820px){.diagram-panels.three{grid-template-columns:1fr;}}
  .diagram-panel.is-west{background:#FBEEDF;border-color:#E8C99F;}
  .diagram-panel.is-west h4{color:#8A4A16;}
  .diagram-panel.is-isle{background:#F2EAF6;border-color:#D6C0E2;}
  .diagram-panel.is-isle h4{color:#5C3470;}
  .diagram-panel.is-east{background:#EDF4E5;border-color:#C4D9AE;}
  .diagram-panel.is-east h4{color:#31552B;}
  .sail-chart .land,.sail-chart .land-false{transition:filter .15s ease;}
  .sail-chart .land[role="button"]:hover,.sail-chart .land-false[role="button"]:hover{filter:brightness(1.06);}
  .sail-chart .land[role="button"]:focus-visible,
  .sail-chart .land-false[role="button"]:focus-visible{outline:3px solid #12626F;outline-offset:2px;}
  /* a map squeezed onto a phone is a map you cannot read: let it scroll at a
     legible width instead of shrinking the place names to nothing */
  .chart-scroll-hint{display:none;font-size:12.5px;color:var(--ink-soft);margin:9px 2px 0;font-style:italic;}
  .name-bar{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 14px;
            font-family:'Inter',sans-serif;font-size:12.5px;color:var(--ink-soft);}
  .name-bar .name-label{letter-spacing:.06em;text-transform:uppercase;font-weight:700;font-size:11px;}
  .name-bar button{font:inherit;font-weight:600;border:1px solid var(--accent-light);
                   background:var(--card);color:var(--ink-soft);padding:5px 12px;border-radius:999px;
                   cursor:pointer;transition:background .12s ease,color .12s ease;}
  .name-bar button:hover{color:var(--ink);}
  .name-bar button.on{background:var(--accent);color:#FFFFFF;border-color:var(--accent);}
  .sail-chart .place-name{transition:opacity .12s ease;}
  @media (max-width:760px){
    .diagram-stage{overflow-x:auto;-webkit-overflow-scrolling:touch;}
    .diagram-stage .sail-chart{width:720px;max-width:none;}
    .chart-scroll-hint{display:block;}
  }
'''

REPLACEMENTS = [
    ('<div class="brand">Sherpa <span>Tensing</span></div>',
     '<div class="brand">Sailing the <span>Seas of Grammar</span></div>'),
    ('<div class="sub">Forbes English &middot; a route up the tenses</div>',
     '<div class="sub">Forbes English &middot; gerunds and infinitives</div>'),
    ('<a class="up-link" href="sherpa-tensing-route-map.html"><span class="arw" aria-hidden="true">&larr;</span>Route map</a>',
     '<a class="up-link" href="library.html"><span class="arw" aria-hidden="true">&larr;</span>Lesson library</a>'),
    ('<div class="camp-label">Summit log</div>', '<div class="camp-label">Ship&#39;s log</div>'),
    ('<button class="retry-btn" id="retry-btn">Climb again</button>',
     '<button class="retry-btn" id="retry-btn">Sail it again</button>'),
    ('<a class="base-camp" href="sherpa-tensing-route-map.html">&larr; Return to base camp</a>',
     '<a class="base-camp" href="library.html">&larr; Back to the library</a>'),
    ('<a class="next-camp" href="sherpa-tensing-route-map.html">Choose your next camp &rarr;</a>',
     '<a class="next-camp" href="sherpa-tensing-route-map.html">The tenses: Sherpa Tensing &rarr;</a>'),
    ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
     '"Clean run. You can read both shores, and the island did not catch you out."'),
    ('"Solid progress. Worth a look back at camp five before camp eight."',
     '"Solid progress. Twofold Isle is the part worth reading again."'),
    ('"Good first attempt. The will/going to fork is the part to read again."',
     '"Good first attempt. Start with the current: every preposition takes -ing."'),
    ('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── THE SEA CHART ── */'),
    ('// ── NOW vs WILL diagram interactivity ──', '// ── the chart, made clickable ──'),
    ('\n</style>', EXTRA_CSS + '</style>'),
    ('<div class="camp-label">The fork in the path</div>',
     '<div class="camp-label">The strait</div>'),
    ('<div class="camp-label">Trail markers</div>',
     '<div class="camp-label">Tide tables</div>'),
    ('<div class="camp-label">The climb</div>',
     '<div class="camp-label">The crossing</div>'),
    ('"Reach the summit"', '"Make landfall"'),
]

PALETTE = palette('#12262E', '#4E6B77', '#F4F9FA', '#1B7A87', '#0E5460', '#B9DCE1', '#E6F3F5')

s = assemble(
    HERO,
    WEST + EAST + DIAGRAM + CAPE + ISLE + SHALLOWS + SIGNALS,
    DIAGRAM_JS,
    questions(QUIZ),
    PALETTE,
    '<title>Sailing the Seas of Grammar &mdash; Gerunds and Infinitives</title>',
    REPLACEMENTS,
    OUT)

# ── strip the mountain's machinery: there is no camp here to earn ──
s = open(OUT, encoding='utf-8').read()
a = s.index('\n// ── progression:')
b = a + re.search(r'\nsherpaBar\(\);\n', s[a:]).end()
s = s[:a] + '\n' + s[b:]
s = re.sub(r'\n  /\* ── progression: the voice toggle and its lock ── \*/.*?\n(?=  /\*|\})',
           '\n', s, count=1, flags=re.S)

# ── lift the data-tr onto the wrapper rule_grid already drew ──
s = re.sub(r'<div class="ex">\x01(\d+)\x01', r'<div class="ex" data-tr="\1">', s)
assert '\x01' not in s, 'an example marker escaped'

# ── our own examples, our own translations ──
import ex_tr_sail as T
rows = []
for i in range(len(EX)):
    r = T.T.get(i)
    assert r and len(r) == 9, 'missing or short translation for example %d: %s' % (i, EX[i])
    rows.append('"%d": %s' % (i, __import__('json').dumps(r, ensure_ascii=False)))
s = re.sub(r'var EX_TR = \{.*?\};\n', 'var EX_TR = {%s};\n' % ", ".join(rows), s, count=1, flags=re.S)

open(OUT, 'w', encoding='utf-8').write(s)
print('wrote %s — %d examples, %d questions, %d bytes' % (OUT, len(EX), len(QUIZ), len(s)))
