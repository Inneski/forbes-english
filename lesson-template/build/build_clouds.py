# -*- coding: utf-8 -*-
"""The first two clouds: used to, and to be used to + -ing."""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
sys.path.insert(0, 'lesson-template')
import cloud_diagram as C
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES
from build_c11_12_13 import chart, fork, signals, interactive, questions, js, palette

# ═════════════════════════════════════════════════════════════════════
UT = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Cloud briefing</div>
      <h2>When to use it</h2>
      <p class="chart-note" style="margin:-6px 0 18px">This is not a tense. It is one fixed form that exists only in the past and always means the same thing: <strong>this was true, and it is not true now</strong>. The gap between the block and NOW is the entire point of saying it.</p>
      ''' + rule_grid([
    ('A habit that has stopped', 'Something you did regularly and do not do any more.',
     '"I <em>used to</em> smoke."'),
    ('A state that has changed', 'Not an action at all &mdash; a way things were.',
     '"There <em>used to</em> be a bakery on this corner."'),
    ('Repeated over a stretch of years', 'The years are vague on purpose; do not date them.',
     '"We <em>used to</em> walk to school every day."'),
    ('The contrast is the message', 'You are not reporting the past. You are pointing at the change.',
     '"I <em>used to</em> hate coffee."'),
    ('Only ever the past', 'There is no present form. For a present habit, use the present simple.',
     '"I <em>drink</em> coffee." not "I use to drink coffee."'),
    ('Careful with the missing <em>d</em>', 'The <em>d</em> vanishes after <em>did</em>, exactly as in any past question.',
     '"<em>Did</em> you <em>use to</em> live here?"'),
]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building it</div>
      <h2>How it&#39;s built</h2>
      ''' + rule_grid([
    ('Affirmative', 'subject + <strong>used to</strong> + infinitive', '"She <em>used to</em> cycle to work."'),
    ('Negative', "subject + didn&#39;t <strong>use to</strong> + infinitive", '"I <em>didn&#39;t use to</em> like it."'),
    ('Questions', 'Did + subject + <strong>use to</strong> + infinitive?', '"<em>Did</em> he <em>use to</em> smoke?"'),
    ('Never changes', 'No person, no number, no <em>-s</em>. One form for everybody.', '"They <em>used to</em>." &middot; "He <em>used to</em>."'),
], 'form-grid') + chart(
    'Where the <em>d</em> goes',
    'The only spelling difficulty in the whole form. <em>Did</em> already carries the past, so the verb '
    'behind it drops back to its plain form &mdash; <em>use</em>, not <em>used</em>. It is the same rule '
    'as <em>did you want</em>, not <em>did you wanted</em>.',
    ['Form', 'Spelling', 'Example'],
    [['Affirmative', 'use<strong>d</strong> to', '"I used to run."'],
     ['Negative', "didn&#39;t <strong>use</strong> to", "\"I didn&#39;t use to run.\""],
     ['Question', 'did &hellip; <strong>use</strong> to', '"Did you use to run?"'],
     ['Never', 'did &hellip; used to', 'This is the commonest written error.']]) + chart(
    '<em>Used to</em> or <em>would</em>?',
    'Both can tell you about the old days, and they are not interchangeable. <em>Would</em> handles '
    'repeated <em>actions</em>; it cannot handle <em>states</em>. <em>Used to</em> handles both, which '
    'makes it the safer choice.',
    ['Meaning', 'used to', 'would'],
    [['A repeated action', '"We used to walk there."', '"We would walk there." &mdash; fine'],
     ['A state', '"There used to be a shop."', '"There would be a shop." &mdash; wrong'],
     ['Living somewhere', '"I used to live in Rome."', '"I would live in Rome." &mdash; wrong'],
     ['Opening a story', 'Either works.', 'Common in writing: "Every summer we would&hellip;"']]) + chart(
    'Three mistakes worth naming',
    'Almost every error with this form is one of these three.',
    ['Not this', 'This', 'Why'],
    [['I use to play tennis.', 'I used to play tennis. / I play tennis.',
      'There is no present <em>use to</em>. Decide which you mean.'],
     ['I didn&#39;t used to like it.', 'I didn&#39;t use to like it.',
      '<em>Did</em> carries the past, so the <em>d</em> comes off.'],
     ['I used to live here for ten years.', 'I lived here for ten years.',
      'A stated length of time makes it a fact, not a contrast. Past simple.']]) + '''
    </div>

    ''' + fork(
    '<em>Used to</em> or past simple?',
    'Both are past and both are true. The difference is what you are drawing attention to: the past '
    'simple reports, and <em>used to</em> points at the change.',
    ['Question', 'used to', 'Past simple'],
    [['What is it doing?', 'Contrasting then with now.<br>"I <em>used to</em> live in Rome."',
      'Reporting a fact.<br>"I <em>lived</em> in Rome for two years."'],
     ['With a length of time?', 'No. It loses the contrast.', 'Yes. "for two years", "from 1998 to 2001".'],
     ['A one-off event?', 'Never. "I used to break my leg" is nonsense.', 'Always. "I broke my leg in 2010."'],
     ['A date?', 'No.', 'Yes. "I moved there in 1998."']],
    'The pair that shows it: <em>"I lived in Rome for two years"</em> tells you where I was. <em>"I used '
    'to live in Rome"</em> tells you where I am not. Same past, entirely different point.',
    [('sherpa-tensing-camp-three-past-simple.html', '&larr; Camp three &middot; past simple'),
     ('sherpa-tensing-cloud-be-used-to.html', 'The other cloud &middot; to be used to')]) + signals(
    None or 'Words that go with it',
    ['back then &middot; in those days', 'when I was younger', 'not any more &middot; no longer',
     'before &middot; once', 'as a child', 'we always &hellip; in those days'],
    'Words that push you to past simple',
    ['for two years', 'from 1998 to 2001', 'in 1998', 'last summer', 'twice &middot; three times',
     'the day I arrived'],
    'A useful habit: say the sentence and then add <em>&hellip; but not any more</em>. If that sounds '
    'redundant rather than wrong, <em>used to</em> is the right form.') + interactive(
    MARK_PANES, 'Interactive', 'The block, and the gap after it',
    'The slate block is what was true. The red line is where it stopped, and it stops hard &mdash; this '
    'form has no soft ending. What matters most is the empty dashed box: the stretch between the block '
    'and NOW where the thing is simply not true any more. That gap is what you are actually communicating '
    'when you say <em>used to</em>. Click either to see it in a sentence.',
    C.used_to('utb', groups=True),
    ['panel-then', 'Then &mdash; what used to be true',
     'panel-gone', 'Now &mdash; what replaced it'])

UT_Q = questions([
    ("I _____ smoke, but I gave up ten years ago.", "A habit that stopped.", "used to",
     ["used to", "use to", "am used to", "was used to"],
     "A stopped past habit takes used to, with the d."),
    ("There _____ be a bakery on this corner.", "A past state.", "used to",
     ["used to", "would", "use to", "is used to"],
     "Used to handles states as well as actions. Would cannot: there would be a bakery is wrong."),
    ("I _____ like coffee when I was a child.", "Negative form.", "didn&#39;t use to",
     ["didn&#39;t use to", "didn&#39;t used to", "am not used to", "wasn&#39;t used to"],
     "Did already carries the past, so the d comes off: didn&#39;t use to."),
    ("_____ you _____ live in Manchester?", "Question form.", "Did ... use to",
     ["Did ... use to", "Did ... used to", "Are ... used to", "Were ... used to"],
     "Did + use to, with no d. This is the commonest written error in the whole form."),
    ("I _____ in Rome for two years.", "There is a length of time here.", "lived",
     ["lived", "used to live", "was used to living", "would live"],
     "A stated duration makes it a plain past fact, so the past simple. Used to would lose the point."),
    ("We _____ to school every day when we were small.", "A repeated action.", "used to walk",
     ["used to walk", "use to walk", "are used to walking", "were used to walk"],
     "A repeated past action that has stopped: used to walk. Would walk would also work here."),
    ("I _____ coffee every morning now.", "Is this the past at all?", "drink",
     ["drink", "use to drink", "used to drink", "am used to drink"],
     "There is no present used to. A present habit is simply the present simple."),
    ("She _____ her leg in 2010.", "A one-off event.", "broke",
     ["broke", "used to break", "would break", "use to break"],
     "Used to needs something repeated or continuous. One event takes the past simple."),
    ("Every summer we _____ swim in the lake.", "A repeated action in a story.", "would",
     ["would", "used", "use", "are used to"],
     "For repeated past actions, would is a natural alternative to used to, especially in writing."),
    ("There _____ be a cinema here, but they knocked it down.", "State, not action.", "used to",
     ["used to", "would", "is used to", "use to"],
     "Would cannot carry a state. Used to can, which is why it is the safer form."),
    ("He _____ have a beard.", "The contrast is the message.", "used to",
     ["used to", "would", "use to", "was used to"],
     "Have here is a state, so would is out. Used to says: he doesn&#39;t now."),
    ("I _____ get up at five when I worked on the farm.", "A habit, long since ended.", "used to",
     ["used to", "am used to", "was used to", "use to"],
     "A stopped past habit. Was used to would mean it did not bother me, which is a different sentence."),
    ("They _____ own a boat, but they sold it.", "State plus contrast.", "used to",
     ["used to", "would", "use to", "are used to"],
     "Own is a state verb, so would is impossible. Used to carries both the past and the change."),
    ("_____ he _____ smoke before he met you?", "Question, past state.", "Did ... use to",
     ["Did ... use to", "Did ... used to", "Was ... used to", "Is ... used to"],
     "Did + use to. Was he used to smoking would ask something else entirely."),
])

assemble(
    hero('Off the route &middot; used to',
         "The thing you don't do any more",
         'A cloud rather than a camp, because this is not a tense. It is one fixed form that lives only '
         'in the past and always says the same thing: <em>this was true, and it is not any more</em>. '
         'The gap between the block and NOW is not empty space &mdash; it is the meaning.',
         C.used_to('ut')),
    UT,
    js([], [], ['shape-then', 'panel-then', 'shape-gone', 'panel-gone'], ['#3F6577', '#A8B6BD'])
    .replace('var exA = [\n\n];', '''var exA = [
  "I <em>used to</em> smoke.",
  "There <em>used to</em> be a bakery on this corner.",
  "We <em>used to</em> walk to school every day."
];''')
    .replace('var exB = [\n\n];', '''var exB = [
  "&hellip; I <em>gave up</em> ten years ago.",
  "&hellip; now it&#39;s a phone shop.",
  "&hellip; these days everyone drives."
];'''),
    UT_Q,
    palette('#16232A', '#54707D', '#F6FAFB', '#3F6577', '#2A4854', '#C7DAE1', '#EAF2F5'),
    '<title>Sherpa Tensing - The Clouds: Used To</title>',
    [('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── THEN vs NOW DIAGRAM ── */'),
     ('// ── NOW vs WILL diagram interactivity ──', '// ── the block and the gap after it ──'),
     ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
      '"Clean run. You know where the d goes and when the past simple is the better sentence."'),
     ('"Solid progress. Worth a look back at camp five before camp eight."',
      '"Solid progress. Worth a look at the other cloud before you go on."'),
     ('"Good first attempt. The will/going to fork is the part to read again."',
      '"Good first attempt. The missing d is the part to read again."'),
     ('Camp seven', 'This cloud')],
    'sherpa-tensing-cloud-used-to.html')
print('cloud: used to')

# ═════════════════════════════════════════════════════════════════════
BUT = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Cloud briefing</div>
      <h2>When to use it</h2>
      <p class="chart-note" style="margin:-6px 0 18px">One letter from its neighbour and nothing like it. This is not a past habit &mdash; it is a <strong>present state</strong>, a description of how you are right now, and it takes a noun or an <em>-ing</em> form, never an infinitive.</p>
      ''' + rule_grid([
    ('Something has stopped being strange', 'The state of finding a thing normal, having once found it odd.',
     '"I<em>&#39;m used to</em> the noise now."'),
    ('It takes a noun or an <em>-ing</em>', 'Never an infinitive. This is the error that gives it away.',
     '"I<em>&#39;m used to</em> <em>getting</em> up early."'),
    ('It moves through the tenses', 'It is an ordinary adjective phrase, so <em>be</em> does the usual work.',
     '"I <em>was used to</em> it by then." &middot; "You<em>&#39;ll be used to</em> it soon."'),
    ('<em>Get</em> used to = the process', 'Becoming familiar, rather than already being familiar.',
     '"I<em>&#39;m getting used to</em> the shifts."'),
    ('The negative is common and useful', 'Most often you are explaining why something is hard.',
     '"She<em>&#39;s not used to</em> the cold."'),
    ('It says nothing about the past', 'Unlike its neighbour, it makes no claim that anything has stopped.',
     '"I<em>&#39;m used to</em> living alone." &mdash; and I still do'),
]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building it</div>
      <h2>How it&#39;s built</h2>
      ''' + rule_grid([
    ('Affirmative', 'subject + am / is / are + <strong>used to</strong> + noun or -ing', '"He<em>&#39;s used to</em> the早 shifts."'),
    ('Negative', 'subject + am / is / are + not + used to + &hellip;', '"They<em>&#39;re not used to</em> the heat."'),
    ('Questions', 'Am / Is / Are + subject + used to + &hellip;?', '"<em>Are</em> you <em>used to</em> it yet?"'),
    ('Becoming', 'get / am getting / got + <strong>used to</strong> + &hellip;', '"I <em>got used to</em> it quickly."'),
], 'form-grid') + chart(
    'The three forms, side by side',
    'This is the chart worth learning by heart. Three phrases, one letter apart, three different jobs.',
    ['Form', 'Means', 'Example'],
    [['used to + infinitive', 'a past habit that has stopped', '"I used to live here." &mdash; I don&#39;t now'],
     ['be used to + -ing', 'a present state: it is normal to me', '"I&#39;m used to living here." &mdash; I still do'],
     ['get used to + -ing', 'the process of becoming familiar', '"I&#39;m getting used to living here."'],
     ['would + infinitive', 'a repeated past action only', '"We would walk there every Sunday."']]) + chart(
    'What can follow it',
    'After <em>used to</em> in this phrase comes a <em>thing</em>, never an action in its plain form. '
    'If you can put <em>it</em> there, you can put an <em>-ing</em> there.',
    ['Follows with', 'Example', 'Right?'],
    [['a noun', '"I&#39;m used to the noise."', 'Yes'],
     ['a pronoun', '"I&#39;m used to it."', 'Yes'],
     ['an <em>-ing</em> form', '"I&#39;m used to working nights."', 'Yes'],
     ['an infinitive', '"I&#39;m used to work nights."', 'No &mdash; this is the classic error']]) + chart(
    'Three mistakes worth naming',
    'Almost every error with this phrase is one of these three.',
    ['Not this', 'This', 'Why'],
    [['I&#39;m used to get up early.', 'I&#39;m used to getting up early.',
      'After this <em>to</em> comes a thing, not an action. The <em>-ing</em> makes it a thing.'],
     ['I used to the noise.', 'I&#39;m used to the noise.',
      'The phrase needs <em>be</em>. Without it you have accidentally written the other form.'],
     ['I&#39;m used to live here.', 'I used to live here. / I&#39;m used to living here.',
      'Both are English and they mean opposite things. Decide which you mean.']]) + '''
    </div>

    ''' + fork(
    'Which of the two do you want?',
    'They differ by one word and they point in opposite directions. <em>Used to</em> looks back and says '
    'something ended. <em>Be used to</em> looks at now and says something is normal.',
    ['Question', 'be used to + -ing', 'used to + infinitive'],
    [['When is it true?', 'Now.<br>"I&#39;m used to the cold."', 'It was true, and stopped.<br>"I used to hate the cold."'],
     ['What follows?', 'A noun or an <em>-ing</em>.', 'An infinitive.'],
     ['Can it change tense?', 'Yes: was used to, will be used to.', 'No. Past only.'],
     ['Is <em>be</em> there?', 'Always.', 'Never.']],
    'The pair that decides it: <em>"I used to live alone"</em> &mdash; I have a flatmate now. <em>"I&#39;m '
    'used to living alone"</em> &mdash; I still do, and it suits me. One word apart, and the second one is '
    'the only one that tells you where I live today.',
    [('sherpa-tensing-cloud-used-to.html', '&larr; The other cloud &middot; used to'),
     ('sherpa-tensing-route-map.html', 'The route map')]) + signals(
    None or 'Words that go with it',
    ['now &middot; by now &middot; yet', 'soon &middot; after a while', 'still not used to',
     'gradually', 'it took me a month', 'you&#39;ll get used to it'],
    'The giveaway that you want the other one',
    ['not any more', 'back then', 'when I was younger', 'in those days',
     'but I gave up', 'and now I don&#39;t'],
    'A useful habit: try replacing the phrase with <em>familiar with</em>. If the sentence still works, '
    'you want <em>be used to</em>. If it collapses, you want <em>used to</em>.') + interactive(
    MARK_PANES, 'Interactive', 'A state that runs through now',
    'The brown peg is where it started &mdash; the first day, when the thing was still strange. From '
    'there the band runs on, and the dots grow more solid as it becomes ordinary. Crucially it does not '
    'stop at NOW: it goes straight through and out the other side, because this is a description of how '
    'you are, not a report of something finished. The violet zone above is that present state. Click '
    'either to see it in a sentence.',
    C.be_used_to('butb', groups=True),
    ['panel-state', 'The stretch &mdash; strange, then ordinary',
     'panel-nowstate', 'Now &mdash; how you are today'])

BUT_Q = questions([
    ("I&#39;m used to _____ up early.", "What follows this to?", "getting",
     ["getting", "get", "got", "have got"],
     "After be used to comes a noun or an -ing form. Getting is the -ing."),
    ("She _____ the cold &mdash; she grew up in Oslo.", "A present state.", "is used to",
     ["is used to", "used to", "was using to", "gets used"],
     "Be + used to describes how she is now. Used to would say she doesn&#39;t any more."),
    ("I _____ live in Rome, but I moved back in 2019.", "Something ended.", "used to",
     ["used to", "am used to", "was used to", "get used to"],
     "A past habit that has stopped, with no be: used to live."),
    ("I _____ living alone &mdash; it suits me.", "Still true.", "am used to",
     ["am used to", "used to", "was used to", "use to"],
     "Be used to + -ing: a present state. It says nothing has stopped."),
    ("It was strange at first, but I _____ it. (get)", "The process of becoming familiar.", "got used to",
     ["got used to", "used to", "was used to get", "get use to"],
     "Get used to is the becoming; be used to is the being."),
    ("They _____ the noise yet.", "Negative, present.", "aren&#39;t used to",
     ["aren&#39;t used to", "didn&#39;t use to", "weren&#39;t used to", "don&#39;t use to"],
     "Yet points at now, so the present of be: aren&#39;t used to."),
    ("_____ you _____ the new system yet?", "Question, present state.", "Are ... used to",
     ["Are ... used to", "Did ... use to", "Were ... used to", "Do ... used to"],
     "Are + subject + used to. Did you use to would ask about a stopped habit."),
    ("By the end of the winter I _____ the dark mornings.", "A past state, not a habit.", "was used to",
     ["was used to", "used to", "am used to", "use to"],
     "Be used to takes the past of be when the state itself is in the past."),
    ("You _____ it in a week or two.", "The process, in the future.", "&#39;ll get used to",
     ["&#39;ll get used to", "&#39;ll use to", "used to", "are used to"],
     "Get used to carries the becoming, and will puts it in the future."),
    ("I&#39;m used to _____ nights, so the shift doesn&#39;t bother me.", "A thing, not an action.", "working",
     ["working", "work", "worked", "be working"],
     "An -ing form turns the action into a thing, which is what this to needs."),
    ("He _____ a beard, but he shaved it off.", "Something ended.", "used to have",
     ["used to have", "is used to have", "is used to having", "was used to have"],
     "A past state that has changed, with no be: used to have."),
    ("She&#39;s not used to _____ so much.", "After not used to.", "walking",
     ["walking", "walk", "walked", "the walk"],
     "The negative changes nothing about what follows: still a noun or an -ing."),
    ("I _____ the traffic here. It still shocks me.", "Negative present state.", "&#39;m not used to",
     ["&#39;m not used to", "didn&#39;t use to", "don&#39;t use to", "wasn&#39;t used to"],
     "Still shocks me puts it firmly in the present, so the present of be."),
    ("We _____ swim in the lake every summer.", "A repeated past action.", "used to",
     ["used to", "are used to", "were used to", "get used to"],
     "No be, and an infinitive follows: a stopped past habit."),
])

assemble(
    hero('Off the route &middot; to be used to',
         'The thing that stopped being strange',
         'One letter from the other cloud and nothing like it. This is not a past habit &mdash; it is a '
         '<em>present state</em>, a description of how you are right now. It takes a noun or an '
         '<em>-ing</em> form, never an infinitive, and it runs straight through NOW instead of stopping '
         'short of it.',
         C.be_used_to('but')),
    BUT,
    js([], [], ['shape-state', 'panel-state', 'shape-nowstate', 'panel-nowstate'], ['#7A6E9B', '#4C4270'])
    .replace('var exA = [\n\n];', '''var exA = [
  "It was strange at first &hellip;",
  "The shifts took me a month &hellip;",
  "Nobody speaks on the train here &hellip;"
];''')
    .replace('var exB = [\n\n];', '''var exB = [
  "&hellip; but I<em>&#39;m used to</em> it now.",
  "&hellip; now I<em>&#39;m used to</em> working nights.",
  "&hellip; and I<em>&#39;ve got used to</em> the quiet."
];'''),
    BUT_Q,
    palette('#1E1A2C', '#5F5878', '#FAF8FD', '#6A5E8C', '#4C4270', '#D6D0E8', '#F0EDF8'),
    '<title>Sherpa Tensing - The Clouds: To Be Used To + -ing</title>',
    [('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── THE STATE THAT RUNS THROUGH NOW ── */'),
     ('// ── NOW vs WILL diagram interactivity ──', '// ── the stretch and the present state ──'),
     ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
      '"Clean run. You never put an infinitive after this one, and you can hear which cloud a sentence wants."'),
     ('"Solid progress. Worth a look back at camp five before camp eight."',
      '"Solid progress. Worth a look at the other cloud before you go on."'),
     ('"Good first attempt. The will/going to fork is the part to read again."',
      '"Good first attempt. The three-forms chart is the part to read again."'),
     ('Camp seven', 'This cloud'),
     ('the早 shifts', 'the early shifts')],
    'sherpa-tensing-cloud-be-used-to.html')
print('cloud: be used to')
