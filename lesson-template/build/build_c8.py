# -*- coding: utf-8 -*-
"""Camp eight · present perfect continuous. Built from camp seven."""
import re, sys
sys.path.insert(0, '/tmp')
sys.path.insert(0, 'lesson-template')
import trail_diagram as D
from build_c10 import (assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE,
                       MARK_FORK, MARK_CLOCK, MARK_PANES)

EIGHT_HERO = hero(
    'Camp eight &middot; present perfect continuous',
    'The tracks you leave behind',
    'Camp four tells you the climb is finished. Camp eight tells you how long you have been at it &mdash; and shows '
    'the mud on your boots. It is the tense for an activity that has been running right up to now, and for one that '
    'has only just stopped and left something behind that anyone can still see.',
    D.camp_eight('ppc'))

EIGHT_CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      ''' + rule_grid([
        ('How long, up to now',
         'It started in the past, it is still going, and the point is the duration.',
         '"We <em>have been walking</em> since dawn."'),
        ('Just stopped &mdash; and it shows',
         'The activity is over, but the evidence of it is in front of you.',
         '"Your hands are filthy. <em>Have</em> you <em>been digging</em>?"'),
        ('The activity, not the total',
         'How the time was spent, rather than what came out of it.',
         '"I<em>&#39;ve been reading</em> that report." (still at it)'),
        ('Repeated, over a stretch of time',
         'The same thing again and again, right up to the present.',
         '"She<em>&#39;s been calling</em> all morning."'),
        ('Explaining a present state',
         'The cause is behind you; the result is standing in front of you.',
         '"I<em>&#39;m exhausted</em>. I<em>&#39;ve been packing</em> all day."'),
        ('Temporary, and often a complaint',
         'With <em>lately</em> and <em>recently</em>, and when you are not pleased about it.',
         '"He<em>&#39;s been leaving</em> the gate open."'),
    ]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      ''' + rule_grid([
        ('Affirmative', 'subject + have / has + been + <strong>-ing</strong>', '"They <em>have been waiting</em>."'),
        ('Negative', "subject + haven't / hasn't + been + -ing", '"It <em>hasn&#39;t been raining</em>."'),
        ('Yes / No questions', 'Have / Has + subject + been + -ing?', '"<em>Have you been running</em>?"'),
        ('Wh- questions', 'How long + have / has + subject + been + -ing?', '"How long <em>have you been waiting</em>?"'),
    ], 'form-grid') + '''
      <div class="chart-wrap">
        <h3>Conjugation chart</h3>
        <p class="chart-note">Three pieces, and only the first one ever changes: <em>have</em> or <em>has</em>, then <em>been</em>, then the <em>-ing</em> form. <em>Been</em> is fixed and the <em>-ing</em> is fixed, which makes this a much easier tense to build than it looks.</p>
        <table class="conj">
          <thead><tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr></thead>
          <tbody>
            <tr><td class="subj">I</td><td>I have been working</td><td>I haven't been working</td><td>Have I been working?</td></tr>
            <tr><td class="subj">You</td><td>You have been working</td><td>You haven't been working</td><td>Have you been working?</td></tr>
            <tr><td class="subj">He / She / It</td><td>She has been working</td><td>She hasn't been working</td><td>Has she been working?</td></tr>
            <tr><td class="subj">We</td><td>We have been working</td><td>We haven't been working</td><td>Have we been working?</td></tr>
            <tr><td class="subj">They</td><td>They have been working</td><td>They haven't been working</td><td>Have they been working?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3><em>For</em> or <em>since</em>?</h3>
        <p class="chart-note">These two words carry most of the meaning of this tense, and they are not interchangeable. <em>For</em> takes a length of time; <em>since</em> takes the moment it started.</p>
        <table class="conj">
          <thead><tr><th>Word</th><th>Takes</th><th>Examples</th></tr></thead>
          <tbody>
            <tr><td class="subj">for</td><td>a length of time</td><td>for two hours &middot; for a week &middot; for ages</td></tr>
            <tr><td class="subj">since</td><td>a starting point</td><td>since dawn &middot; since Monday &middot; since we arrived</td></tr>
            <tr><td class="subj">all &hellip;</td><td>a whole period</td><td>all morning &middot; all day &middot; all week</td></tr>
            <tr><td class="subj">how long</td><td>asks for either</td><td>"How long have you been waiting?"</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>The verbs that refuse the -ing</h3>
        <p class="chart-note">State verbs describe a condition rather than an activity, and a condition cannot be in progress. When the meaning is a state, camp four takes over: <em>have known</em>, not <em>have been knowing</em>.</p>
        <table class="conj">
          <thead><tr><th>Group</th><th>Verbs</th><th>Say this instead</th></tr></thead>
          <tbody>
            <tr><td class="subj">Thinking</td><td>know, believe, understand</td><td>"I <em>have known</em> her for years."</td></tr>
            <tr><td class="subj">Feeling</td><td>like, love, hate, want</td><td>"She <em>has wanted</em> it since March."</td></tr>
            <tr><td class="subj">Having</td><td>own, belong, have (= possess)</td><td>"We <em>have had</em> the flat for a year."</td></tr>
            <tr><td class="subj">Being</td><td>be, seem</td><td>"It <em>has been</em> quiet all week."</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Three mistakes worth naming</h3>
        <p class="chart-note">Almost every error with this tense is one of these three.</p>
        <table class="conj">
          <thead><tr><th>Not this</th><th>This</th><th>Why</th></tr></thead>
          <tbody>
            <tr><td class="subj">I am living here since 2019.</td><td>I have been living here since 2019.</td><td>English measures duration up to now with a perfect tense, never with the present continuous.</td></tr>
            <tr><td class="subj">I have been knowing her for years.</td><td>I have known her for years.</td><td>State verbs refuse the continuous, so camp four takes it.</td></tr>
            <tr><td class="subj">I have been reading three books.</td><td>I have read three books.</td><td>A number is a result, and results belong to camp four.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="camp" id="vs-simple">
      ''' + MARK_FORK + '''
      <div class="camp-label">The fork in the path</div>
      <h2>Continuous or simple?</h2>
      <div class="chart-wrap" style="margin-top:18px">
        <p class="chart-note" style="margin-bottom:16px">Camp four and camp eight both run from the past up to now. The question is only ever which half you are pointing at: the <em>activity</em> that filled the time, or the <em>result</em> sitting at the end of it.</p>
        <table class="conj">
          <thead><tr><th>Question</th><th>Present perfect continuous</th><th>Present perfect simple</th></tr></thead>
          <tbody>
            <tr><td class="subj">What is in focus?</td><td>The activity and how long it ran.<br>"I<em>'ve been painting</em>."</td><td>The finished result.<br>"I<em>'ve painted</em> the fence."</td></tr>
            <tr><td class="subj">Is it finished?</td><td>Often not &mdash; and it doesn't matter.</td><td>Yes. That is the point of saying it.</td></tr>
            <tr><td class="subj">With a number?</td><td>Never. "I've been writing three emails" is wrong.</td><td>Always. "I've written three emails."</td></tr>
            <tr><td class="subj">With a state verb?</td><td>Never &mdash; know, be, own refuse it.</td><td>Always. "I've known her for years."</td></tr>
          </tbody>
        </table>
        <p class="example" style="margin-top:14px">The pair that shows the whole difference: <em>"I've been painting the fence"</em> &mdash; there is paint in my hair and the job may not be done. <em>"I've painted the fence"</em> &mdash; go and look at it, it's finished. One is about me, the other about the fence.</p>
      </div>
      <div class="btnrow" style="margin-top:16px">
        <a class="route-link" href="sherpa-tensing-camp-four-present-perfect.html">&larr; Camp four &middot; present perfect</a>
        <a class="route-link" href="sherpa-tensing-camp-one-present-continuous.html">Camp one &middot; present continuous</a>
      </div>
    </div>

    <div class="camp" id="signals">
      ''' + MARK_CLOCK + '''
      <div class="camp-label">Trail markers</div>
      <h2>Signal words</h2>
      <div class="signal-groups">
        <div class="signal-box">
          <h3>How long it has run</h3>
          <ul>
            <li>for &middot; since</li>
            <li>how long &hellip;?</li>
            <li>all morning / all day / all week</li>
            <li>lately &middot; recently</li>
            <li>these past few weeks</li>
            <li>the whole time</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>The evidence in front of you</h3>
          <ul>
            <li>you're out of breath</li>
            <li>the ground is still wet</li>
            <li>your eyes are red</li>
            <li>there's paint on your hands</li>
            <li>the kitchen smells of it</li>
            <li>that's why I'm exhausted</li>
          </ul>
        </div>
      </div>
      <p class="example" style="margin-top:14px">A useful habit: if you can point at something in the room and say <em>that is how I know</em>, this is the tense. The evidence is doing the work that <em>for</em> and <em>since</em> do in the other half.</p>
    </div>

    <div class="camp" id="run">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>The stretch, and the evidence</h2>
      <div class="diagram-card">
        <p class="diagram-intro">The brown peg on the left is where it started &mdash; that is always a past simple event, <em>since I arrived</em>, <em>since 2019</em>. From there the band of time carries a trail of the same action happening over and over: faint behind, solid at the head, the way a moving thing smears in a still photograph. It arrives at NOW rather than stopping short of it, and past NOW it carries on fading, because this tense usually means the thing is still going &mdash; but never actually promises it. Above sits the other half of the tense in its own zone: the evidence, the thing you can point at in the room right now. Click either to see it in a sentence.</p>
        <div class="diagram-stage">
          ''' + D.camp_eight('ppcb', groups=True) + '''
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel" id="panel-run">
            <h4>The stretch &mdash; how long it has run</h4>
            <ul id="panel-run-list"></ul>
          </div>
          <div class="diagram-panel is-now" id="panel-evidence">
            <h4>The evidence &mdash; what you can see now</h4>
            <ul id="panel-evidence-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

EIGHT_JS = '''var runExamples = [
  "We <em>have been walking</em> since dawn.",
  "She<em>&#39;s been calling</em> all morning.",
  "How long <em>have</em> you <em>been waiting</em>?"
];
var evidenceExamples = [
  "Your hands are filthy &mdash; <em>have</em> you <em>been digging</em>?",
  "The ground is wet. It<em>&#39;s been raining</em>.",
  "I&#39;m exhausted. I<em>&#39;ve been packing</em> all day."
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
renderList("panel-run-list", runExamples);
renderList("panel-evidence-list", evidenceExamples);

function pulseShape(el){
  el.style.transformOrigin = "center";
  el.animate(
    [{ opacity: 1 }, { opacity: 0.6 }, { opacity: 1 }],
    { duration: 380, easing: "ease-out" }
  );
}
[["shape-run","panel-run","#2FA6A1"],
 ["shape-evidence","panel-evidence","#14837E"]].forEach(function(pair){
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

'''

EIGHT_Q = '''var questions = [
  {
    prompt: "We _____ since dawn and my feet are ruined. (walk)",
    hint: "How long, right up to now.",
    correct: "have been walking",
    options: ["have been walking", "are walking", "have walked", "walk"],
    explain: "Since dawn measures a stretch running up to now, and the point is the walking rather than any distance. Present perfect continuous."
  },
  {
    prompt: "Your hands are filthy. _____ you _____ in the garden? (dig)",
    hint: "The evidence is right there.",
    correct: "Have ... been digging",
    options: ["Have ... been digging", "Are ... digging", "Did ... dig", "Have ... dug"],
    explain: "The activity has just stopped and left something you can see. That is what this tense is for."
  },
  {
    prompt: "I _____ that report, but I'm only halfway. (read)",
    hint: "Unfinished, and that's fine.",
    correct: "have been reading",
    options: ["have been reading", "have read", "am reading", "read"],
    explain: "Have read would say the report is finished. The continuous keeps it open, which is what halfway means."
  },
  {
    prompt: "She _____ me all morning. (call)",
    hint: "Again and again, up to now.",
    correct: "has been calling",
    options: ["has been calling", "is calling", "has called", "called"],
    explain: "Repeated action across a period that reaches the present takes the present perfect continuous."
  },
  {
    prompt: "I _____ here since 2019. (live)",
    hint: "Careful with the German pattern.",
    correct: "have been living",
    options: ["have been living", "am living", "live", "was living"],
    explain: "English measures a duration up to now with a perfect tense. \\"I am living here since 2019\\" is the commonest German-speaker error in this camp."
  },
  {
    prompt: "I _____ her for fifteen years. (know)",
    hint: "A state verb.",
    correct: "have known",
    options: ["have known", "have been knowing", "am knowing", "know"],
    explain: "Know is a state verb and refuses the continuous, so the present perfect simple takes the duration instead."
  },
  {
    prompt: "I _____ three emails this morning. (write)",
    hint: "There is a number in the sentence.",
    correct: "have written",
    options: ["have written", "have been writing", "am writing", "was writing"],
    explain: "A number is a result, and results belong to the simple. Have been writing would be right without the three."
  },
  {
    prompt: "It _____ , so the path is still wet. (rain)",
    hint: "Just stopped, evidence in front of you.",
    correct: "has been raining",
    options: ["has been raining", "is raining", "rained", "has rained"],
    explain: "The rain has stopped but its result is visible now. That present evidence is the signature of this tense."
  },
  {
    prompt: "How long _____ you _____ for the bus? (wait)",
    hint: "The question this tense was made for.",
    correct: "have ... been waiting",
    options: ["have ... been waiting", "are ... waiting", "did ... wait", "have ... waited"],
    explain: "How long + present perfect continuous is the standard way to ask about a duration that reaches the present."
  },
  {
    prompt: "He _____ the gate open all week, and the sheep got out. (leave)",
    hint: "A repeated habit, and a complaint.",
    correct: "has been leaving",
    options: ["has been leaving", "leaves", "has left", "was leaving"],
    explain: "Repeated over a period up to now, with irritation attached. Has left would name one occasion."
  },
  {
    prompt: "We _____ the flat since March. (have)",
    hint: "Possession is a state.",
    correct: "have had",
    options: ["have had", "have been having", "are having", "had"],
    explain: "Have meaning possess is a state verb, so it takes the simple: we have had it since March."
  },
  {
    prompt: "I'm exhausted. I _____ all day. (pack)",
    hint: "Explaining a present state.",
    correct: "have been packing",
    options: ["have been packing", "packed", "have packed", "was packing"],
    explain: "The exhaustion now is the result of the activity, which is exactly the job of the present perfect continuous."
  },
  {
    prompt: "She _____ the fence, so there's paint everywhere. (paint)",
    hint: "About her, not about the fence.",
    correct: "has been painting",
    options: ["has been painting", "has painted", "paints", "painted"],
    explain: "Has painted would report a finished fence. The mess points at the activity, so the continuous is right."
  },
  {
    prompt: "They _____ very well lately. (not / sleep)",
    hint: "Lately points at a recent stretch.",
    correct: "haven't been sleeping",
    options: ["haven't been sleeping", "don't sleep", "haven't slept", "weren't sleeping"],
    explain: "Lately marks a period running up to now, and the negative keeps the same three pieces: haven't + been + -ing."
  }
];

'''

EIGHT_PALETTE = '''  :root{
    --ink:#0E2426;
    --ink-soft:#4C6C6D;
    --paper:#F5FBFA;
    --card:#FFFFFF;
    --accent:#0E8A84;
    --accent-dark:#0A625E;
    --accent-light:#AEE3DF;
    --accent-lighter:#E6F6F4;
    --good:#1E7A4C;
    --good-bg:#E5F5EC;
    --bad:#B23A3A;
    --bad-bg:#FBEAEA;
    --radius:14px;
  }'''

assemble(EIGHT_HERO, EIGHT_CAMPS, EIGHT_JS, EIGHT_Q, EIGHT_PALETTE,
         '<title>Sherpa Tensing - Camp Eight: The Tracks You Leave Behind (Present Perfect Continuous)</title>',
         [('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── STRETCH vs EVIDENCE DIAGRAM CAMP ── */'),
          ('// ── NOW vs WILL diagram interactivity ──', '// ── the stretch of time and the evidence it leaves ──'),
          ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
           '"Clean run. You can hear the difference between the activity and the result, and you know which verbs refuse the -ing."'),
          ('"Solid progress. Worth a look back at camp five before camp eight."',
           '"Solid progress. Worth a look back at camp four before camp ten."'),
          ('"Good first attempt. The will/going to fork is the part to read again."',
           '"Good first attempt. The continuous/simple fork is the part to read again."')],
         'sherpa-tensing-camp-eight-present-perfect-continuous.html')
print('camp eight written')
