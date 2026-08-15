# -*- coding: utf-8 -*-
"""Camps eleven, twelve and thirteen — the far end of the ridge."""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
sys.path.insert(0, 'lesson-template')
import trail_diagram as D
from build_c10 import (assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE,
                       MARK_FORK, MARK_CLOCK, MARK_PANES)


def js(examples_a, examples_b, ids, colours):
    return '''var %s = [
%s
];
var %s = [
%s
];

function renderList(id, items){
  var ul = document.getElementById(id);
  ul.innerHTML = "";
  items.forEach(function(txt){
    var li = document.createElement("li");
    li.innerHTML = txt;
    ul.appendChild(li);
  });
}
renderList("%s-list", %s);
renderList("%s-list", %s);

function pulseShape(el){
  el.style.transformOrigin = "center";
  el.animate(
    [{ opacity: 1 }, { opacity: 0.6 }, { opacity: 1 }],
    { duration: 380, easing: "ease-out" }
  );
}
[["%s","%s","%s"],
 ["%s","%s","%s"]].forEach(function(pair){
  var el = document.getElementById(pair[0]);
  if (!el) return;
  var activate = function(){
    pulseShape(el);
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    var panel = document.getElementById(pair[1]);
    if (panel) panel.style.outline = "2px solid " + pair[2];
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){
    if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); }
  });
});

''' % ('exA', "\n".join('  "%s",' % e for e in examples_a).rstrip(','),
       'exB', "\n".join('  "%s",' % e for e in examples_b).rstrip(','),
       ids[1], 'exA', ids[3], 'exB',
       ids[0], ids[1], colours[0], ids[2], ids[3], colours[1])


def interactive(marker, label, title, intro, svg, panels):
    return '''<div class="camp" id="order">
      %s
      <div class="camp-label">%s</div>
      <h2>%s</h2>
      <div class="diagram-card">
        <p class="diagram-intro">%s</p>
        <div class="diagram-stage">
          %s
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel" id="%s">
            <h4>%s</h4>
            <ul id="%s-list"></ul>
          </div>
          <div class="diagram-panel is-now" id="%s">
            <h4>%s</h4>
            <ul id="%s-list"></ul>
          </div>
        </div>
      </div>
    </div>

    ''' % (marker, label, title, intro, svg,
           panels[0], panels[1], panels[0], panels[2], panels[3], panels[2])


def signals(title_a, items_a, title_b, items_b, note):
    return '''<div class="camp" id="signals">
      %s
      <div class="camp-label">Trail markers</div>
      <h2>Signal words</h2>
      <div class="signal-groups">
        <div class="signal-box">
          <h3>%s</h3>
          <ul>
%s
          </ul>
        </div>
        <div class="signal-box">
          <h3>%s</h3>
          <ul>
%s
          </ul>
        </div>
      </div>
      <p class="example" style="margin-top:14px">%s</p>
    </div>

    ''' % (MARK_CLOCK, title_a, "\n".join('            <li>%s</li>' % i for i in items_a),
           title_b, "\n".join('            <li>%s</li>' % i for i in items_b), note)


def chart(h3, note, headers, rows):
    return '''      <div class="chart-wrap">
        <h3>%s</h3>
        <p class="chart-note">%s</p>
        <table class="conj">
          <thead><tr>%s</tr></thead>
          <tbody>
%s
          </tbody>
        </table>
      </div>
''' % (h3, note, "".join('<th>%s</th>' % h for h in headers),
       "\n".join('            <tr><td class="subj">%s</td>%s</tr>'
                 % (r[0], "".join('<td>%s</td>' % c for c in r[1:])) for r in rows))


def fork(title, note, headers, rows, example, links):
    return '''<div class="camp" id="vs-simple">
      %s
      <div class="camp-label">The fork in the path</div>
      <h2>%s</h2>
      <div class="chart-wrap" style="margin-top:18px">
        <p class="chart-note" style="margin-bottom:16px">%s</p>
        <table class="conj">
          <thead><tr>%s</tr></thead>
          <tbody>
%s
          </tbody>
        </table>
        <p class="example" style="margin-top:14px">%s</p>
      </div>
      <div class="btnrow" style="margin-top:16px">
%s
      </div>
    </div>

    ''' % (MARK_FORK, title, note, "".join('<th>%s</th>' % h for h in headers),
           "\n".join('            <tr><td class="subj">%s</td>%s</tr>'
                     % (r[0], "".join('<td>%s</td>' % c for c in r[1:])) for r in rows),
           example,
           "\n".join('        <a class="route-link" href="%s">%s</a>' % (h, t) for h, t in links))


def questions(items):
    out = ['var questions = [']
    for q in items:
        out.append('  {')
        out.append('    prompt: "%s",' % q[0])
        out.append('    hint: "%s",' % q[1])
        out.append('    correct: "%s",' % q[2])
        out.append('    options: [%s],' % ", ".join('"%s"' % o for o in q[3]))
        out.append('    explain: "%s"' % q[4])
        out.append('  },')
    out[-1] = out[-1].rstrip(',')
    out.append('];\n\n')
    return "\n".join(out)


def palette(ink, ink_soft, paper, accent, dark, light, lighter):
    return '''  :root{
    --ink:%s;
    --ink-soft:%s;
    --paper:%s;
    --card:#FFFFFF;
    --accent:%s;
    --accent-dark:%s;
    --accent-light:%s;
    --accent-lighter:%s;
    --good:#1E7A4C;
    --good-bg:#E5F5EC;
    --bad:#B23A3A;
    --bad-bg:#FBEAEA;
    --radius:14px;
  }''' % (ink, ink_soft, paper, accent, dark, light, lighter)


RESULTS = lambda clean, solid, first: [
    ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."', clean),
    ('"Solid progress. Worth a look back at camp five before camp eight."', solid),
    ('"Good first attempt. The will/going to fork is the part to read again."', first),
    ('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── THE INTERACTIVE DIAGRAM CAMP ── */'),
    ('// ── NOW vs WILL diagram interactivity ──', '// ── the diagram, made clickable ──'),
]

# ═════════════════════════════════════════════════════════════════════
# CAMP ELEVEN · PAST PERFECT CONTINUOUS
# ═════════════════════════════════════════════════════════════════════
E11_CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      ''' + rule_grid([
    ('How long, up to a past moment',
     'It had been running for a while before something else in the past happened.',
     '"We <em>had been walking</em> for six hours when we saw the hut."'),
    ('The cause of a past state',
     'Why somebody or something was the way you found them.',
     '"His hands were shaking. He <em>had been carrying</em> the pack all day."'),
    ('Repeated, up to that point',
     'The same thing over and over, right up to the moment it stopped.',
     '"She <em>had been calling</em> all morning before he answered."'),
    ('Reported speech',
     'A present perfect continuous shifts back one step when you report it.',
     '"I&#39;ve been waiting." &rarr; He said he <em>had been waiting</em>.'),
    ('The third conditional',
     'An unreal past, with the activity rather than the result in focus.',
     '"If I <em>had been paying</em> attention, I would have seen it."'),
    ('The activity, not the total',
     'How the time was filled, rather than what came out of it.',
     '"I <em>had been reading</em> it." (not necessarily finished)'),
]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      ''' + rule_grid([
    ('Affirmative', 'subject + had been + <strong>-ing</strong>', '"They <em>had been waiting</em> for hours."'),
    ('Negative', "subject + hadn't been + -ing", '"It <em>hadn&#39;t been raining</em> long."'),
    ('Yes / No questions', 'Had + subject + been + -ing?', '"<em>Had you been running</em>?"'),
    ('Wh- questions', 'How long + had + subject + been + -ing?', '"How long <em>had they been driving</em>?"'),
], 'form-grid') + chart(
    'Conjugation chart',
    'Four pieces, and not one of them changes for the subject. <em>Had</em> is the same for everybody, '
    '<em>been</em> never moves, and the <em>-ing</em> form is fixed. This is the easiest tense on the '
    'mountain to conjugate and one of the hardest to know when to use.',
    ['Subject', 'Affirmative', 'Negative', 'Question'],
    [['I', 'I had been working', "I hadn't been working", 'Had I been working?'],
     ['You', 'You had been working', "You hadn't been working", 'Had you been working?'],
     ['He / She / It', 'She had been working', "She hadn't been working", 'Had she been working?'],
     ['We', 'We had been working', "We hadn't been working", 'Had we been working?'],
     ['They', 'They had been working', "They hadn't been working", 'Had they been working?']]) + chart(
    'The verbs that refuse the -ing',
    'A state is not an activity, so it cannot be in progress. When the meaning is a state, camp ten '
    'takes over: <em>had known</em>, never <em>had been knowing</em>.',
    ['Group', 'Verbs', 'Say this instead'],
    [['Thinking', 'know, believe, understand', '"I <em>had known</em> him for years."'],
     ['Feeling', 'like, love, hate, want', '"She <em>had wanted</em> it since March."'],
     ['Having', 'own, belong, have (= possess)', '"They <em>had had</em> the flat a year."'],
     ['Being', 'be, seem', '"It <em>had been</em> quiet all night."']]) + chart(
    'Three mistakes worth naming',
    'Almost every error with this tense is one of these three.',
    ['Not this', 'This', 'Why'],
    [['I was walking for six hours when we arrived.', 'I had been walking for six hours when we arrived.',
      'A duration measured back from a past moment needs the perfect, not camp six.'],
     ['I had been knowing him for years.', 'I had known him for years.',
      'State verbs refuse the continuous, so camp ten takes it.'],
     ['I had been reading three books.', 'I had read three books.',
      'A number is a result, and results belong to camp ten.']]) + '''
    </div>

    ''' + fork(
    'Continuous or simple?',
    'Camp ten and camp eleven both sit behind a past moment. The question is only ever which half you '
    'are pointing at: the <em>activity</em> that filled the time, or the <em>result</em> that was '
    'sitting there when you arrived.',
    ['Question', 'Past perfect continuous', 'Past perfect simple'],
    [['What is in focus?', 'The activity and how long it ran.<br>"He <em>had been painting</em>."',
      'The finished result.<br>"He <em>had painted</em> the fence."'],
     ['With a number?', 'Never. "He had been writing three emails" is wrong.',
      'Always. "He had written three emails."'],
     ['With a state verb?', 'Never &mdash; know, be, own refuse it.', 'Always. "He had known her for years."'],
     ['And camp six?', 'Measures a <em>duration</em> up to the past moment.',
      'Camp six just says what was going on at it: "I <em>was walking</em> when&hellip;"']],
    'The pair that shows the whole difference: <em>"I was walking when the storm hit"</em> &mdash; that '
    'is what was going on. <em>"I had been walking for six hours when the storm hit"</em> &mdash; that '
    'is how long it had been going on for. Camp six gives you the scene; camp eleven gives you the bill.',
    [('sherpa-tensing-camp-ten-past-perfect.html', '&larr; Camp ten &middot; past perfect'),
     ('sherpa-tensing-camp-eight-present-perfect-continuous.html', 'Camp eight &middot; present perfect continuous')]) + signals(
    MARK_CLOCK and 'How long it had run',
    ['for &middot; since', 'how long &hellip;?', 'all morning / all day / all night',
     'before &middot; by the time', 'until then', 'the whole time'],
    'The evidence, back then',
    ['he was out of breath', 'the ground was still wet', 'her eyes were red',
     'there was paint on his hands', 'the kitchen smelled of it', 'that was why they were late'],
    'A useful habit: find the past simple first &mdash; that is the moment you are standing on. Then ask '
    'how long the other thing had already been going when you got there.') + interactive(
    MARK_PANES, 'Interactive', 'The stretch, and what it left',
    'Two brown pegs mark past simple events: the one on the left is where it started, the one on the '
    'right is the moment you are measuring to. Between them the trail is the same action happening over '
    'and over &mdash; faint behind, solid at the head. The purple zone above is what that activity had '
    'left by the time you arrived. NOW stands well clear on the right, because none of this reaches it. '
    'Click either shape to see it in a sentence.',
    D.camp_eleven('ppcb', groups=True),
    ['panel-run', 'The stretch &mdash; how long it had run',
     'panel-evidence', 'The evidence &mdash; how things stood then'])

E11_Q = questions([
    ("We _____ for six hours when we finally saw the hut. (walk)",
     "A duration measured back from a past moment.", "had been walking",
     ["had been walking", "were walking", "have been walking", "had walked"],
     "For six hours + a past moment to measure back from: past perfect continuous. Were walking would only say what was going on."),
    ("His hands were shaking. He _____ the pack all day. (carry)",
     "Why were his hands shaking?", "had been carrying",
     ["had been carrying", "was carrying", "has been carrying", "carried"],
     "The activity came before the shaking hands, and the point is how long it ran. Past perfect continuous."),
    ("She _____ all morning before he finally answered. (call)",
     "Repeated, up to a past point.", "had been calling",
     ["had been calling", "was calling", "has been calling", "called"],
     "Repeated action across a period ending at a past moment takes the past perfect continuous."),
    ('\\"I have been waiting an hour.\\" \\u2192 He said he _____ an hour. (wait)',
     "Reported speech shifts back one step.", "had been waiting",
     ["had been waiting", "has been waiting", "was waiting", "had waited"],
     "A present perfect continuous in the original becomes a past perfect continuous when reported."),
    ("If I _____ attention, I would have seen it. (pay)",
     "The unreal past, with the activity in focus.", "had been paying",
     ["had been paying", "was paying", "have been paying", "had paid"],
     "The third conditional takes if + past perfect; the continuous keeps the focus on the activity rather than a result."),
    ("I _____ him for years before that evening. (know)",
     "A state verb.", "had known",
     ["had known", "had been knowing", "was knowing", "have known"],
     "Know is a state verb and refuses the continuous, so the past perfect simple takes the duration."),
    ("By lunchtime she _____ three reports. (write)",
     "There is a number in the sentence.", "had written",
     ["had written", "had been writing", "was writing", "has written"],
     "A number is a result, and results belong to the simple. Had been writing would be right without the three."),
    ("The path was flooded. It _____ all night. (rain)",
     "The cause of a past state.", "had been raining",
     ["had been raining", "was raining", "has been raining", "rained"],
     "The rain ran up to the moment you found the flooded path, and the duration is the point."),
    ("How long _____ they _____ before the taxi came? (wait)",
     "The question this tense was made for.", "had ... been waiting",
     ["had ... been waiting", "were ... waiting", "have ... been waiting", "had ... waited"],
     "How long + had been + -ing is the standard way to ask about a duration ending at a past moment."),
    ("They _____ well that week, and it showed. (not / sleep)",
     "Negative, four pieces.", "hadn't been sleeping",
     ["hadn't been sleeping", "weren't sleeping", "haven't been sleeping", "hadn't slept"],
     "Hadn't + been + -ing. The past perfect simple would report it as a finished fact rather than a running condition."),
    ("I _____ when the phone rang, and I nearly dropped the pan. (cook)",
     "What was going on, not how long.", "was cooking",
     ["was cooking", "had been cooking", "have been cooking", "had cooked"],
     "With no duration and no need to measure back, camp six is the right tense: the scene, not the bill."),
    ("We _____ there for ten years when the mill closed. (live)",
     "A duration reaching a past event.", "had been living",
     ["had been living", "were living", "have been living", "had lived"],
     "For ten years + a past moment: past perfect continuous. Had lived is also possible, but the continuous keeps the stretch in view."),
    ("He was covered in mud because he _____ the ditch. (clear)",
     "Evidence in the past.", "had been clearing",
     ["had been clearing", "was clearing", "has been clearing", "cleared"],
     "The mud is what the activity left behind at that past moment, which is exactly this tense's job."),
    ("She _____ the same excuse for months before anyone checked. (use)",
     "Repeated over a long stretch.", "had been using",
     ["had been using", "was using", "has been using", "used"],
     "Repeated across a period that ends at a past moment takes the past perfect continuous."),
])

assemble(
    hero('Camp eleven &middot; past perfect continuous',
         'The hours before the hut',
         'Camp eight measures up to now. Camp eleven moves the whole measurement back: an activity that '
         '<em>had been</em> running for a while before something else in the past happened &mdash; and '
         'how things looked by the time it did.',
         D.camp_eleven('ppc')),
    E11_CAMPS,
    js([], [], ['shape-run', 'panel-run', 'shape-evidence', 'panel-evidence'], ['#4B1A7A', '#7A5A3E'])
    .replace('var exA = [\n\n];', '''var exA = [
  "We <em>had been walking</em> for six hours &hellip;",
  "It <em>had been raining</em> all night &hellip;",
  "She <em>had been calling</em> all morning &hellip;"
];''')
    .replace('var exB = [\n\n];', '''var exB = [
  "&hellip; and our legs were finished.",
  "&hellip; so the path was under water.",
  "&hellip; and he still had not picked up."
];'''),
    E11_Q,
    palette('#1E1030', '#584A6E', '#FAF7FD', '#4B1A7A', '#331052', '#D9C9EE', '#F2EBFA'),
    '<title>Sherpa Tensing - Camp Eleven: The Hours Before the Hut (Past Perfect Continuous)</title>',
    RESULTS('"Clean run. You can hear the difference between what was going on and how long it had been going on."',
            '"Solid progress. Worth a look back at camp six and camp ten before camp thirteen."',
            '"Good first attempt. The continuous/simple fork is the part to read again."'),
    'sherpa-tensing-camp-eleven-past-perfect-continuous.html')
print('camp eleven written')

# ═════════════════════════════════════════════════════════════════════
# CAMP TWELVE · FUTURE PERFECT
# ═════════════════════════════════════════════════════════════════════
E12_CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      ''' + rule_grid([
    ('Finished before a future deadline',
     'The action is over by the time the future moment arrives.',
     '"By Friday I <em>will have finished</em> the report."'),
    ('With <em>by the time</em>',
     'The clause that sets the deadline stays in the present.',
     '"By the time you land, we <em>will have left</em>."'),
    ('A total reached by then',
     'Counting up to a future point rather than to now.',
     '"Next month she <em>will have worked</em> here ten years."'),
    ('A confident guess about now',
     'Not future at all &mdash; an assumption about something already done.',
     '"He <em>will have arrived</em> by now."'),
    ('Looking back from the future',
     'Standing at a future moment and describing what is behind you.',
     '"In 2030 we <em>will have forgotten</em> all this."'),
    ('Not done by then',
     'The negative is just as useful, and just as precise.',
     '"They <em>won&#39;t have decided</em> by Monday."'),
]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      ''' + rule_grid([
    ('Affirmative', 'subject + will have + <strong>past participle</strong>', '"I <em>will have finished</em> by six."'),
    ('Negative', "subject + won't have + past participle", '"They <em>won&#39;t have decided</em>."'),
    ('Yes / No questions', 'Will + subject + have + past participle?', '"<em>Will you have eaten</em>?"'),
    ('Wh- questions', 'question word + will + subject + have + participle?', '"How much <em>will it have cost</em>?"'),
], 'form-grid') + chart(
    'Conjugation chart',
    'Nothing changes for the subject &mdash; <em>will have</em> is the same for everybody, exactly as it '
    'is at camp seven. Every difficulty here is in the participle and in the deadline word.',
    ['Subject', 'Affirmative', 'Negative', 'Question'],
    [['I', 'I will have finished', "I won't have finished", 'Will I have finished?'],
     ['You', 'You will have finished', "You won't have finished", 'Will you have finished?'],
     ['He / She / It', 'She will have finished', "She won't have finished", 'Will she have finished?'],
     ['We', 'We will have finished', "We won't have finished", 'Will we have finished?'],
     ['They', 'They will have finished', "They won't have finished", 'Will they have finished?']]) + chart(
    '<em>By</em> or <em>until</em>?',
    'This is the error that costs money in a work email. <em>By Friday</em> means at any point up to and '
    'including Friday &mdash; a deadline. <em>Until Friday</em> means the whole stretch continuing up to '
    'Friday &mdash; a duration. The future perfect takes <em>by</em>.',
    ['Word', 'Means', 'Example'],
    [['by', 'at or before that point &mdash; a deadline', '"I <em>will have sent</em> it by Friday."'],
     ['until', 'right up to that point &mdash; a duration', '"I <em>will be working</em> until Friday."'],
     ['before', 'earlier than that point', '"We <em>will have left</em> before you land."'],
     ['by the time', 'a deadline set by another event', '"By the time it opens, we <em>will have queued</em> an hour."']]) + chart(
    'Three mistakes worth naming',
    'Almost every error with this tense is one of these three.',
    ['Not this', 'This', 'Why'],
    [['By Friday I will finish the report.', 'By Friday I will have finished the report.',
      'A deadline needs the perfect. Will finish names when it happens, not that it is already done.'],
     ['I will have went by then.', 'I will have gone by then.',
      '<em>Have</em> takes the third form, never the past simple.'],
     ['By the time you will arrive, we will have left.', 'By the time you arrive, we will have left.',
      'The clause that sets the deadline stays in the present, even though it is about the future.']]) + '''
    </div>

    ''' + fork(
    'Future perfect or future simple?',
    'Camp seven says <em>when</em> something happens. Camp twelve says it is <em>already done</em> by a '
    'point you name. If there is a deadline in the sentence, you are at camp twelve.',
    ['Question', 'Future perfect', 'Future simple'],
    [['What does it say?', 'It is finished before then.<br>"I <em>will have finished</em> by five."',
      'It happens at that time.<br>"I <em>will finish</em> at five."'],
     ['Which word triggers it?', '<em>by</em>, <em>by the time</em>, <em>before</em>',
      '<em>at</em>, <em>tomorrow</em>, <em>next week</em>'],
     ['A total?', 'Yes. "She will have worked here ten years."', 'No &mdash; it names one event.'],
     ['About the present?', 'Yes, as a confident guess: "He will have landed by now."',
      'No. That is a different job.']],
    'The pair that shows the whole difference: <em>"I will finish at five"</em> &mdash; five o&#39;clock is '
    'when I stop. <em>"I will have finished by five"</em> &mdash; five o&#39;clock is when you can safely '
    'assume it is done, and I may well be finished long before. One is a schedule; the other is a promise.',
    [('sherpa-tensing-camp-seven-future-simple.html', '&larr; Camp seven &middot; future simple'),
     ('sherpa-tensing-camp-ten-past-perfect.html', 'Camp ten &middot; past perfect')]) + signals(
    None or 'Deadline words',
    ['by &middot; by then', 'by the time', 'before', 'in two weeks&#39; time',
     'this time next year', 'by the end of the month'],
    'What it does not take',
    ['until (that is a duration)', 'at five o&#39;clock (that is camp seven)',
     'for two hours (that is camp thirteen)', 'now', 'yesterday', 'while'],
    'A useful habit: if you can put the word <em>already</em> in front of the verb and the sentence still '
    'makes sense at that future moment, the future perfect is right.') + interactive(
    MARK_PANES, 'Interactive', 'Done, and then the deadline',
    'The block is the action, standing in future time. What matters is that it <em>ends before</em> the '
    'dashed line, not on it &mdash; the deadline is a moment you look back from, not a moment when '
    'anything happens. The action itself could be at any point in the shaded stretch; the sentence only '
    'promises it is behind you by then. Click the block or the NOW column to see it in a sentence.',
    D.camp_twelve('fpb', groups=True),
    ['panel-done', 'Future perfect &mdash; already behind you',
     'panel-now', 'The deadline clause &mdash; it stays present'])

E12_Q = questions([
    ("By Friday I _____ the report. (finish)",
     "There is a deadline in the sentence.", "will have finished",
     ["will have finished", "will finish", "am finishing", "will have finish"],
     "By + a future point needs the perfect: it says the report is already done when Friday arrives."),
    ("By the time you land, we _____ . (leave)",
     "One future event sets the deadline for another.", "will have left",
     ["will have left", "will leave", "are leaving", "will have leaved"],
     "By the time sets a deadline, so the main clause takes the future perfect. The participle of leave is left."),
    ("By the time you _____ , we will have left. (arrive)",
     "Careful with the deadline clause itself.", "arrive",
     ["arrive", "will arrive", "will have arrived", "are arriving"],
     "The clause that sets the deadline stays in the present, even though it describes the future."),
    ("Next month she _____ here for ten years. (work)",
     "A total counted up to a future point.", "will have worked",
     ["will have worked", "will work", "works", "will have work"],
     "Counting a total up to a future moment is the future perfect. Will work would only say it happens."),
    ("Don't ring him now &mdash; he _____ by now. (land)",
     "Not future at all.", "will have landed",
     ["will have landed", "will land", "is landing", "has been landing"],
     "The future perfect also carries a confident assumption about something already finished: he will have landed by now."),
    ("They _____ by Monday, so don't expect an answer. (not / decide)",
     "The negative form.", "won't have decided",
     ["won't have decided", "won't decide", "aren't deciding", "won't have decide"],
     "Won't have + participle. It says the decision is still outstanding when Monday comes."),
    ("_____ you _____ by seven? (eat)",
     "Question order.", "Will ... have eaten",
     ["Will ... have eaten", "Will ... eat", "Are ... eating", "Will ... have ate"],
     "Questions invert will: Will you have eaten? The participle of eat is eaten, not ate."),
    ("I _____ at five, so ring me any time after that. (finish)",
     "Is there a deadline here, or a time?", "will finish",
     ["will finish", "will have finished", "will have finish", "am finishing"],
     "At five names when the action happens, not a point to look back from. That is camp seven."),
    ("I _____ it to you by Friday. (send)",
     "A promise with a deadline.", "will have sent",
     ["will have sent", "will have send", "will be sending", "am sending"],
     "By Friday is a deadline, so the future perfect: it will already be sent when Friday comes."),
    ("In 2030 everyone _____ this argument. (forget)",
     "Standing at a future point, looking back.", "will have forgotten",
     ["will have forgotten", "will forget", "forgets", "will have forget"],
     "Looking back from a future moment takes the future perfect, and the participle of forget is forgotten."),
    ("By the end of the tour the band _____ in twelve countries. (play)",
     "A total by a deadline.", "will have played",
     ["will have played", "will play", "plays", "will have play"],
     "A running total counted up to a future point is the future perfect."),
    ("We _____ here until Friday, then we move on. (work)",
     "Until is not a deadline.", "will be working",
     ["will be working", "will have worked", "will have been work", "have worked"],
     "Until marks a stretch continuing up to a point, so the future continuous fits. By would have made it a deadline."),
    ("How much _____ it _____ by the time it's built? (cost)",
     "A wh- question with a deadline.", "will ... have cost",
     ["will ... have cost", "will ... cost", "does ... cost", "will ... have costed"],
     "By the time sets the deadline, so the question takes the future perfect. Cost is the same in all three forms."),
    ("She _____ the keys before you get there. (leave)",
     "Before also sets a point to look back from.", "will have left",
     ["will have left", "will leave", "leaves", "will have leaved"],
     "Before you get there is a deadline, so the action is already behind you: will have left."),
])

assemble(
    hero('Camp twelve &middot; future perfect',
         'Done before you get there',
         'Camp ten looks back from a moment in the past. Camp twelve does the same thing facing the other '
         'way: it stands at a point in the future and tells you what is already behind you by the time '
         'you arrive.',
         D.camp_twelve('fp')),
    E12_CAMPS,
    js([], [], ['shape-done', 'panel-done', 'shape-now', 'panel-now'], ['#454545', '#5C7690'])
    .replace('var exA = [\n\n];', '''var exA = [
  "By Friday I <em>will have finished</em> the report.",
  "We <em>will have left</em> before you land.",
  "She <em>will have worked</em> here ten years."
];''')
    .replace('var exB = [\n\n];', '''var exB = [
  "By the time you <em>land</em> &hellip;",
  "Before it <em>opens</em> &hellip;",
  "As soon as she <em>gets</em> back &hellip;"
];'''),
    E12_Q,
    palette('#1E1E1E', '#5E5E5E', '#F8F8F7', '#454545', '#2A2A2A', '#D2D2D2', '#EFEFEF'),
    '<title>Sherpa Tensing - Camp Twelve: Done Before You Get There (Future Perfect)</title>',
    RESULTS('"Clean run. You can hear a deadline from a time of day, and you keep the by-the-time clause in the present."',
            '"Solid progress. Worth a look back at camp seven before camp thirteen."',
            '"Good first attempt. The by/until distinction is the part to read again."'),
    'sherpa-tensing-camp-twelve-future-perfect.html')
print('camp twelve written')

# ═════════════════════════════════════════════════════════════════════
# CAMP THIRTEEN · FUTURE PERFECT CONTINUOUS
# ═════════════════════════════════════════════════════════════════════
E13_CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      ''' + rule_grid([
    ('How long, by a future point',
     'The activity will have been running for a measurable stretch when you get there.',
     '"By June we <em>will have been living</em> here ten years."'),
    ('The activity, not the result',
     'What fills the time, rather than what comes out of it.',
     '"At six I <em>will have been driving</em> for eight hours."'),
    ('The cause of a future state',
     'Explaining in advance why somebody will be in the state they are in.',
     '"She&#39;ll be shattered. She <em>will have been travelling</em> all night."'),
    ('It needs a duration',
     'Without <em>for</em>, <em>since</em> or <em>all day</em>, the sentence has nothing to say.',
     '"By then I <em>will have been waiting</em> <strong>two hours</strong>."'),
    ('Never with state verbs',
     'A state cannot be in progress, so camp twelve takes it.',
     '"I <em>will have known</em> her twenty years." not "been knowing"'),
    ('Rare aloud, precise on paper',
     'You will meet it in contracts, plans and reports far more than in conversation.',
     '"By completion the team <em>will have been working</em> on it for three years."'),
]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      ''' + rule_grid([
    ('Affirmative', 'subject + will have been + <strong>-ing</strong>', '"I <em>will have been waiting</em> two hours."'),
    ('Negative', "subject + won't have been + -ing", '"It <em>won&#39;t have been running</em> long."'),
    ('Yes / No questions', 'Will + subject + have been + -ing?', '"<em>Will you have been driving</em> all day?"'),
    ('Wh- questions', 'How long + will + subject + have been + -ing?', '"How long <em>will she have been teaching</em>?"'),
], 'form-grid') + chart(
    'Four pieces, in this order, always',
    'This is the longest verb form in English and the least troublesome, because not one of the four '
    'pieces ever changes. Learn the order and you have learnt the tense.',
    ['Piece', 'What it does', 'Changes?'],
    [['will', 'puts it in the future', 'Never'],
     ['have', 'looks back from that future point', 'Never &mdash; not <em>has</em>'],
     ['been', 'makes it perfect and continuous at once', 'Never'],
     ['-ing', 'the activity itself', 'Never']]) + chart(
    'Conjugation chart',
    'The same for everybody, which is the one mercy this tense offers.',
    ['Subject', 'Affirmative', 'Negative', 'Question'],
    [['I', 'I will have been working', "I won't have been working", 'Will I have been working?'],
     ['You', 'You will have been working', "You won't have been working", 'Will you have been working?'],
     ['He / She / It', 'She will have been working', "She won't have been working", 'Will she have been working?'],
     ['We', 'We will have been working', "We won't have been working", 'Will we have been working?'],
     ['They', 'They will have been working', "They won't have been working", 'Will they have been working?']]) + chart(
    'Three mistakes worth naming',
    'Almost every error with this tense is one of these three.',
    ['Not this', 'This', 'Why'],
    [['By June I will have been living here.', 'By June I will have been living here for ten years.',
      'Without a duration the tense has nothing to measure, and the sentence sounds unfinished.'],
     ['I will have been knowing her twenty years.', 'I will have known her twenty years.',
      'State verbs refuse the continuous, so camp twelve takes it.'],
     ['By six I will have been writing three reports.', 'By six I will have written three reports.',
      'A number is a result, and results belong to camp twelve.']]) + '''
    </div>

    ''' + fork(
    'Continuous or simple?',
    'Camp twelve and camp thirteen both look back from a future point. Camp twelve counts what is '
    '<em>finished</em>; camp thirteen counts <em>how long it has taken</em>. Almost always, a number of '
    'things means twelve and a length of time means thirteen.',
    ['Question', 'Future perfect continuous', 'Future perfect'],
    [['What is counted?', 'A length of time.<br>"I <em>will have been driving</em> eight hours."',
      'A number of finished things.<br>"I <em>will have driven</em> four hundred miles."'],
     ['Is it finished by then?', 'Not necessarily &mdash; and it does not matter.', 'Yes. That is the point.'],
     ['Does it need a duration?', 'Yes. Without one it makes no sense.', 'No.'],
     ['With a state verb?', 'Never.', 'Always. "I will have known her twenty years."']],
    'The pair that shows the whole difference: <em>"By six I will have written three reports"</em> '
    '&mdash; here is what you can put on my desk. <em>"By six I will have been writing for eight '
    'hours"</em> &mdash; here is why I am not writing a fourth.',
    [('sherpa-tensing-camp-twelve-future-perfect.html', '&larr; Camp twelve &middot; future perfect'),
     ('sherpa-tensing-camp-eight-present-perfect-continuous.html', 'Camp eight &middot; present perfect continuous')]) + signals(
    None or 'How long, by then',
    ['for + a length of time', 'since + a starting point', 'by then &middot; by the time',
     'this time next year', 'all day &middot; all week', 'how long &hellip;?'],
    'The state it explains',
    ['she&#39;ll be exhausted', 'the batteries will be flat', 'the soup will be ready',
     'they&#39;ll be sick of it', 'the road will be worn through', 'that&#39;s why he&#39;ll need a break'],
    'A useful habit: say the sentence and listen for a length of time. If there isn&#39;t one, you want camp '
    'twelve instead &mdash; this tense cannot stand up without a duration to lean on.') + interactive(
    MARK_PANES, 'Interactive', 'The stretch, and the total at the end of it',
    'The trail starts at a brown past simple peg, runs straight through NOW without pausing, and keeps '
    'going to the dashed appointment on the right. That is the whole idea: the activity is already under '
    'way and it does not stop when you get there. The grey zone above is the total it will have reached '
    'by that moment &mdash; the ten years, the eight hours, whatever the sentence is really about. Click '
    'either shape to see it in a sentence.',
    D.camp_thirteen('fpcb', groups=True),
    ['panel-run', 'The stretch &mdash; still running when you arrive',
     'panel-evidence', 'The total &mdash; how long, by then'])

E13_Q = questions([
    ("By June we _____ here for ten years. (live)",
     "A length of time by a future point.", "will have been living",
     ["will have been living", "will have lived", "will live", "are living"],
     "For ten years is a duration measured to a future moment, which is exactly this tense."),
    ("At six I _____ for eight hours. (drive)",
     "The activity, not the distance.", "will have been driving",
     ["will have been driving", "will have driven", "will drive", "am driving"],
     "Eight hours is a length of time, so the continuous. Will have driven would want a number of miles."),
    ("She'll be shattered &mdash; she _____ all night. (travel)",
     "Explaining a future state.", "will have been travelling",
     ["will have been travelling", "will have travelled", "will travel", "travels"],
     "The exhaustion is caused by how long the travelling ran, which is the continuous's job."),
    ("By six I _____ three reports. (write)",
     "There is a number here.", "will have written",
     ["will have written", "will have been writing", "will write", "am writing"],
     "A number is a result, and results take camp twelve. The continuous counts hours, not reports."),
    ("Next year I _____ her for twenty years. (know)",
     "A state verb.", "will have known",
     ["will have known", "will have been knowing", "will know", "am knowing"],
     "Know is a state verb and refuses the continuous, so the future perfect simple takes the duration."),
    ("How long _____ you _____ by the time you retire? (teach)",
     "The question this tense was made for.", "will ... have been teaching",
     ["will ... have been teaching", "will ... have taught", "will ... teach", "do ... teach"],
     "How long + will have been + -ing asks for a duration reaching a future point."),
    ("By then the machine _____ non-stop for a month. (run)",
     "A stretch, right up to that point.", "will have been running",
     ["will have been running", "will have run", "will run", "runs"],
     "For a month is a duration, so the continuous. Will have run would suggest a finished job."),
    ("It _____ long by the time we get there. (not / rain)",
     "The negative form.", "won't have been raining",
     ["won't have been raining", "won't have rained", "won't rain", "isn't raining"],
     "Won't have been + -ing keeps the focus on how long the rain will have run."),
    ("By completion the team _____ on it for three years. (work)",
     "A contract sentence.", "will have been working",
     ["will have been working", "will have worked", "will work", "works"],
     "For three years is a duration measured to a future completion date: future perfect continuous."),
    ("This time next week I _____ on a beach. (lie)",
     "Is there a duration here?", "will be lying",
     ["will be lying", "will have been lying", "will have lain", "am lying"],
     "There is no length of time to measure, only a future moment, so camp nine is right: I will be lying there."),
    ("By the end of the season they _____ for eleven months solid. (tour)",
     "A long stretch, ending at a future point.", "will have been touring",
     ["will have been touring", "will have toured", "will tour", "tour"],
     "Eleven months solid is a duration reaching a future moment, so the continuous."),
    ("By Friday we _____ every room in the building. (paint)",
     "Every room is a total.", "will have painted",
     ["will have painted", "will have been painting", "will paint", "are painting"],
     "Every room is a quantity of finished work, so camp twelve takes it."),
    ("When you land, I _____ for two hours. (wait)",
     "How long, at that future moment.", "will have been waiting",
     ["will have been waiting", "will have waited", "will wait", "am waiting"],
     "For two hours is a duration measured to the moment you land: future perfect continuous."),
    ("By 2040 the glacier _____ for a century. (retreat)",
     "A stretch measured to a future date.", "will have been retreating",
     ["will have been retreating", "will have retreated", "will retreat", "retreats"],
     "For a century is a duration, so the continuous keeps the process rather than the outcome in view."),
])

assemble(
    hero('Camp thirteen &middot; future perfect continuous',
         "The hours you'll have put in",
         'The last camp on the ridge, and the longest verb form in English. Stand at a point in the '
         'future, look back, and measure: by the time you get there, this will <em>have been</em> going '
         'on for a stretch you can name. The stretch is the whole point.',
         D.camp_thirteen('fpc')),
    E13_CAMPS,
    js([], [], ['shape-run', 'panel-run', 'shape-evidence', 'panel-evidence'], ['#7C7C7C', '#4A4A4A'])
    .replace('var exA = [\n\n];', '''var exA = [
  "By June we <em>will have been living</em> here &hellip;",
  "At six I <em>will have been driving</em> &hellip;",
  "By completion they <em>will have been working</em> on it &hellip;"
];''')
    .replace('var exB = [\n\n];', '''var exB = [
  "&hellip; for ten years.",
  "&hellip; for eight hours.",
  "&hellip; for three years."
];'''),
    E13_Q,
    palette('#242424', '#5F5F5F', '#FAFAFA', '#7C7C7C', '#5A5A5A', '#DCDCDC', '#F1F1F1'),
    '<title>Sherpa Tensing - Camp Thirteen: The Hours You Will Have Put In (Future Perfect Continuous)</title>',
    RESULTS('"Clean run. You can hear a length of time from a number of things, and you never leave this tense without a duration."',
            '"Solid progress. Worth a look back at camp eight and camp twelve."',
            '"Good first attempt. The continuous/simple fork is the part to read again."'),
    'sherpa-tensing-camp-thirteen-future-perfect-continuous.html')
print('camp thirteen written')
