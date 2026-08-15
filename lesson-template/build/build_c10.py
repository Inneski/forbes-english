# -*- coding: utf-8 -*-
"""Camp ten · past perfect. Built from camp seven, like camps six and nine."""
import re, sys
sys.path.insert(0, '/tmp')
sys.path.insert(0, 'lesson-template')
import camp_ten_diagram as D

BASE = open('sherpa-tensing-camp-seven-future-simple.html', encoding='utf-8').read()


def assemble(hero_section, camps, diagram_js, questions, palette, title,
             extra_replacements, out):
    s = BASE
    A = s.index('<section class="hero" id="hero">')
    B = s.index('</section>', A) + len('</section>')
    C = s.index('<div class="camp" id="rules">')
    Dq = s.index('<div class="camp" id="quiz">')
    E = s.index('var willExamples = [')
    F = s.index('// ── QUIZ ──')
    G = s.index('var questions = [')
    H = s.index('\nvar current = 0;')
    out_s = (s[:A] + hero_section + s[B:C] + camps + s[Dq:E] + diagram_js +
             s[F:G] + questions + s[H:])
    out_s = re.sub(r'  :root\{.*?\n  \}', palette, out_s, count=1, flags=re.S)
    out_s = out_s.replace(
        "<title>Sherpa Tensing - Camp Seven: The Weather You Can't See Yet (Future Simple)</title>",
        title, 1)
    for a, b in extra_replacements:
        out_s = out_s.replace(a, b)
    open(out, 'w', encoding='utf-8').write(out_s)
    return out_s


def hero(eyebrow, h1, para, svg):
    return ('<section class="hero" id="hero">\n    <div>\n'
            '      <span class="eyebrow">%s</span>\n'
            '      <h1>%s</h1>\n      <p>%s</p>\n    </div>\n    %s\n  </section>'
            % (eyebrow, h1, para, svg))


def rule_grid(cards, cls='rule-grid'):
    return '<div class="%s">\n%s\n      </div>' % (cls, "\n".join(
        '        <div class="rule-card">\n          <h3>%s</h3>\n'
        '          <p>%s</p>\n          <div class="ex">%s</div>\n        </div>' % c
        for c in cards))


MARK_FLAG = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
             'stroke-width="2"><path d="M5 3v18M5 4h11l-3 4 3 4H5"/></svg></div>')
MARK_TABLE = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
              'stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/>'
              '<path d="M3 10h18M9 4v16"/></svg></div>')
MARK_FORK = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
             'stroke-width="2"><path d="M12 3v18"/><path d="M7 8l-4 4 4 4M17 8l4 4-4 4"/></svg></div>')
MARK_CLOCK = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
              'stroke-width="2"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></div>')
MARK_PANES = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
              'stroke-width="2"><rect x="3" y="4" width="8" height="16"/>'
              '<rect x="13" y="4" width="8" height="16"/></svg></div>')

# ═════════════════════════════════════════════════════════════════════
TEN_HERO = hero(
    'Camp ten &middot; past perfect',
    'The camp you had already struck',
    'Camp three tells the story. Camp ten tells you what had happened <em>before</em> the story started &mdash; '
    'the step behind the step, the thing that was already over by the time anything else began. It is the only '
    'tense on the mountain that exists purely to put two past events in order.',
    D.camp_ten('pp'))

TEN_CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      ''' + rule_grid([
        ('The earlier of two past actions',
         'Two things happened; this one happened first, and the order matters.',
         '"The train <em>had left</em> before we reached the platform."'),
        ('The reason behind a past event',
         'Why something in the past was the way you found it.',
         '"She was furious. Someone <em>had taken</em> her seat."'),
        ('By a past deadline',
         '<em>by</em> or <em>by the time</em> sets a moment the action had already beaten.',
         '"By 1998 he <em>had climbed</em> all fourteen."'),
        ('Reported speech',
         'A past simple in the original shifts back one step when you report it.',
         '"I lost it." &rarr; He said he <em>had lost</em> it.'),
        ('The third conditional',
         'An unreal past &mdash; what would have happened if things had gone differently.',
         '"If we <em>had started</em> earlier, we would have made it."'),
        ('The first time you ever did something',
         'With <em>never &hellip; before</em> and <em>it was the first time</em>.',
         '"It was the first time I <em>had seen</em> a glacier."'),
    ]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      ''' + rule_grid([
        ('Affirmative', 'subject + had + <strong>past participle</strong>', '"They <em>had gone</em> by then."'),
        ('Negative', "subject + hadn't + past participle", '"I <em>hadn\'t seen</em> it before."'),
        ('Yes / No questions', 'Had + subject + past participle?', '"<em>Had you eaten</em>?"'),
        ('Wh- questions', 'question word + had + subject + past participle?', '"Where <em>had they gone</em>?"'),
    ], 'form-grid') + '''
      <div class="chart-wrap">
        <h3>Conjugation chart</h3>
        <p class="chart-note">This is the shortest chart on the mountain. <em>Had</em> does not change for anybody &mdash; no <em>was</em> and <em>were</em>, no third-person <em>-s</em>. Every difficulty in this tense is in the participle, not the auxiliary.</p>
        <table class="conj">
          <thead><tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr></thead>
          <tbody>
            <tr><td class="subj">I</td><td>I had finished</td><td>I hadn't finished</td><td>Had I finished?</td></tr>
            <tr><td class="subj">You</td><td>You had finished</td><td>You hadn't finished</td><td>Had you finished?</td></tr>
            <tr><td class="subj">He / She / It</td><td>She had finished</td><td>She hadn't finished</td><td>Had she finished?</td></tr>
            <tr><td class="subj">We</td><td>We had finished</td><td>We hadn't finished</td><td>Had we finished?</td></tr>
            <tr><td class="subj">They</td><td>They had finished</td><td>They hadn't finished</td><td>Had they finished?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>The third form &mdash; where the errors live</h3>
        <p class="chart-note">After <em>had</em> comes the participle, which for irregular verbs is not the past simple. Putting the camp-three form here is the single commonest mistake in this tense.</p>
        <table class="conj">
          <thead><tr><th>Infinitive</th><th>Past simple (camp three)</th><th>Participle (camp ten)</th></tr></thead>
          <tbody>
            <tr><td class="subj">go</td><td>went</td><td>had <em>gone</em></td></tr>
            <tr><td class="subj">see</td><td>saw</td><td>had <em>seen</em></td></tr>
            <tr><td class="subj">do</td><td>did</td><td>had <em>done</em></td></tr>
            <tr><td class="subj">take</td><td>took</td><td>had <em>taken</em></td></tr>
            <tr><td class="subj">write</td><td>wrote</td><td>had <em>written</em></td></tr>
            <tr><td class="subj">eat</td><td>ate</td><td>had <em>eaten</em></td></tr>
            <tr><td class="subj">break</td><td>broke</td><td>had <em>broken</em></td></tr>
            <tr><td class="subj">forget</td><td>forgot</td><td>had <em>forgotten</em></td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Three mistakes worth naming</h3>
        <p class="chart-note">Almost every error with this tense is one of these three.</p>
        <table class="conj">
          <thead><tr><th>Not this</th><th>This</th><th>Why</th></tr></thead>
          <tbody>
            <tr><td class="subj">He had went home.</td><td>He had gone home.</td><td><em>Had</em> takes the third form, never the past simple.</td></tr>
            <tr><td class="subj">Yesterday I had gone to the shop.</td><td>Yesterday I went to the shop.</td><td>With no second past event to stand behind, the past perfect has nothing to be earlier <em>than</em>.</td></tr>
            <tr><td class="subj">She has left before I arrived.</td><td>She had left before I arrived.</td><td>Camp four measures back to now; camp ten measures back to a past moment.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="camp" id="vs-simple">
      ''' + MARK_FORK + '''
      <div class="camp-label">The fork in the path</div>
      <h2>Past perfect or past simple?</h2>
      <div class="chart-wrap" style="margin-top:18px">
        <p class="chart-note" style="margin-bottom:16px">Camp three is the default past tense and always will be. Camp ten is a correction you make to it &mdash; you reach for <em>had</em> only when the order of two past events would otherwise be read the wrong way round.</p>
        <table class="conj">
          <thead><tr><th>Question</th><th>Past perfect</th><th>Past simple</th></tr></thead>
          <tbody>
            <tr><td class="subj">What is it?</td><td>The earlier one, already over.<br>"He <em>had left</em>."</td><td>The event you are telling.<br>"He <em>left</em>."</td></tr>
            <tr><td class="subj">One event on its own?</td><td>Never &mdash; it needs a second past moment to be earlier than.</td><td>Always. This is the default.</td></tr>
            <tr><td class="subj">A sequence of events?</td><td>Only when you go back out of order.</td><td>In order, one after another.</td></tr>
            <tr><td class="subj">After <em>before</em> and <em>after</em>?</td><td>Allowed, but optional &mdash; the word already gives the order.</td><td>Usually enough on its own.</td></tr>
          </tbody>
        </table>
        <p class="example" style="margin-top:14px">The pair that shows the whole difference: <em>"When I arrived, he left"</em> &mdash; I got there, then he walked out. <em>"When I arrived, he had left"</em> &mdash; he was already gone; I missed him. Same two words changed, an entirely different afternoon.</p>
      </div>
      <div class="btnrow" style="margin-top:16px">
        <a class="route-link" href="sherpa-tensing-camp-three-past-simple.html">&larr; Camp three &middot; past simple</a>
        <a class="route-link" href="sherpa-tensing-camp-four-present-perfect.html">Camp four &middot; present perfect</a>
      </div>
    </div>

    <div class="camp" id="signals">
      ''' + MARK_CLOCK + '''
      <div class="camp-label">Trail markers</div>
      <h2>Signal words</h2>
      <div class="signal-groups">
        <div class="signal-box">
          <h3>Points back to the earlier action</h3>
          <ul>
            <li>before</li>
            <li>by the time &middot; by then &middot; by 1998</li>
            <li>already &middot; just</li>
            <li>never &hellip; before</li>
            <li>until then</li>
            <li>it was the first time</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>Marks the moment you measure from</h3>
          <ul>
            <li>when</li>
            <li>after that</li>
            <li>so &middot; because</li>
            <li>then</li>
            <li>at that point</li>
            <li>the next morning</li>
          </ul>
        </div>
      </div>
      <p class="example" style="margin-top:14px">A useful habit: find the past simple first. That is the moment you are standing on. Anything that had already happened when you got there is camp ten.</p>
    </div>

    <div class="camp" id="order">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>Which one happened first</h2>
      <div class="diagram-card">
        <p class="diagram-intro">Two blocks in past time, and the arrow between them is the whole grammar point. The dark red block is over before the brown one starts &mdash; that is all <em>had</em> is doing. Click either block to name it and see it in a sentence.</p>
        <div class="diagram-stage">
          ''' + D.camp_ten('ppb', groups=True) + '''
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel" id="panel-earlier">
            <h4>Past perfect &mdash; the earlier one</h4>
            <ul id="panel-earlier-list"></ul>
          </div>
          <div class="diagram-panel is-now" id="panel-later">
            <h4>Past simple &mdash; the main event</h4>
            <ul id="panel-later-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

TEN_JS = '''var earlierExamples = [
  "The train <em>had left</em> &hellip;",
  "Someone <em>had taken</em> her seat &hellip;",
  "By 1998 he <em>had climbed</em> all fourteen &hellip;"
];
var laterExamples = [
  "&hellip; before we <em>reached</em> the platform.",
  "&hellip; so she <em>stood</em> for the whole journey.",
  "&hellip; and then he <em>started</em> on the rest."
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
renderList("panel-earlier-list", earlierExamples);
renderList("panel-later-list", laterExamples);

function pulseShape(el){
  el.style.transformOrigin = "center";
  el.animate(
    [{ opacity: 1 }, { opacity: 0.6 }, { opacity: 1 }],
    { duration: 380, easing: "ease-out" }
  );
}
[["shape-earlier","panel-earlier","#6E0B24"],
 ["shape-later","panel-later","#7A5A3E"]].forEach(function(pair){
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

TEN_Q = '''var questions = [
  {
    prompt: "The train _____ by the time we reached the platform. (leave)",
    hint: "Which of the two happened first?",
    correct: "had left",
    options: ["had left", "left", "has left", "had leave"],
    explain: "The train went first, so it takes the past perfect: had left. Reaching the platform is the moment you measure back from."
  },
  {
    prompt: "She was furious. Someone _____ her seat. (take)",
    hint: "The reason behind a past state.",
    correct: "had taken",
    options: ["had taken", "took", "has taken", "had took"],
    explain: "The seat was taken before she was furious, so it takes the past perfect. Note the participle: taken, not took."
  },
  {
    prompt: "By 1998 he _____ all fourteen peaks. (climb)",
    hint: "A deadline in the past.",
    correct: "had climbed",
    options: ["had climbed", "climbed", "has climbed", "had climb"],
    explain: "By + a past date sets a moment the action had already beaten, which is the past perfect. Has climbed would measure back to today instead."
  },
  {
    prompt: "\\"I lost the key.\\" \\u2192 He said he _____ the key. (lose)",
    hint: "Reported speech shifts back one step.",
    correct: "had lost",
    options: ["had lost", "lost", "has lost", "had lose"],
    explain: "A past simple in the original becomes the past perfect when reported: he said he had lost it."
  },
  {
    prompt: "If we _____ earlier, we would have made it. (start)",
    hint: "The unreal past.",
    correct: "had started",
    options: ["had started", "started", "have started", "had start"],
    explain: "The third conditional takes if + past perfect, then would have + participle. It describes a past that did not happen."
  },
  {
    prompt: "By the time she reached the gate, she _____ the form. (sign)",
    hint: "Which one was already done?",
    correct: "had signed",
    options: ["had signed", "has signed", "was signing", "had sign"],
    explain: "Signing was finished before she reached the gate, so it takes the past perfect: had signed."
  },
  {
    prompt: "When I arrived, he _____ . He was already on the road. (leave)",
    hint: "Did I see him?",
    correct: "had left",
    options: ["had left", "left", "was leaving", "had leaved"],
    explain: "Had left means he was gone before I got there. Left would mean he walked out after I arrived \\u2014 a different afternoon."
  },
  {
    prompt: "They _____ anything all day, and it showed. (not / eat)",
    hint: "Negative, with the participle.",
    correct: "hadn't eaten",
    options: ["hadn't eaten", "didn't eat", "haven't eaten", "hadn't ate"],
    explain: "Hadn't + participle: hadn't eaten. Ate is the past simple form and cannot follow had."
  },
  {
    prompt: "_____ you _____ him before that evening? (meet)",
    hint: "Question order for the past perfect.",
    correct: "Had ... met",
    options: ["Had ... met", "Did ... met", "Have ... met", "Had ... meet"],
    explain: "Questions invert had: Had you met him? The participle of meet is met."
  },
  {
    prompt: "Yesterday I _____ to the shop for bread. (go)",
    hint: "Is there a second past event here at all?",
    correct: "went",
    options: ["went", "had gone", "had went", "have gone"],
    explain: "There is no earlier past event for this to stand behind, so the past simple is the right tense. The past perfect always needs something to be earlier than."
  },
  {
    prompt: "He _____ home before the storm broke. (already / go)",
    hint: "Already sits between the two words.",
    correct: "had already gone",
    options: ["had already gone", "had already went", "already went home", "has already gone"],
    explain: "Already goes between had and the participle: had already gone. The storm breaking is the moment you measure back from."
  },
  {
    prompt: "She told me she _____ the letter that morning. (write)",
    hint: "Reported speech again, irregular participle.",
    correct: "had written",
    options: ["had written", "had wrote", "has written", "was writing"],
    explain: "Reported speech shifts the past back to the past perfect, and the participle of write is written."
  },
  {
    prompt: "The path was wet because it _____ all night. (rain)",
    hint: "Which came first \\u2014 the rain or the wet path?",
    correct: "had rained",
    options: ["had rained", "rained", "has rained", "had rain"],
    explain: "The rain came before the wet path you found, so it takes the past perfect: because it had rained."
  },
  {
    prompt: "It was the first time I _____ a glacier. (never / see)",
    hint: "First time \\u2026 in the past.",
    correct: "had ever seen",
    options: ["had ever seen", "had never saw", "have ever seen", "never saw"],
    explain: "It was the first time takes the past perfect: the first time I had ever seen one. Have ever seen would measure back to today."
  }
];

'''

TEN_PALETTE = '''  :root{
    --ink:#2A0F16;
    --ink-soft:#6B4650;
    --paper:#FDF7F8;
    --card:#FFFFFF;
    --accent:#6E0B24;
    --accent-dark:#4A0718;
    --accent-light:#E7BFC8;
    --accent-lighter:#F9EBEE;
    --good:#1E7A4C;
    --good-bg:#E5F5EC;
    --bad:#B23A3A;
    --bad-bg:#FBEAEA;
    --radius:14px;
  }'''

assemble(TEN_HERO, TEN_CAMPS, TEN_JS, TEN_Q, TEN_PALETTE,
         '<title>Sherpa Tensing - Camp Ten: The Camp You Had Already Struck (Past Perfect)</title>',
         [('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── EARLIER vs LATER DIAGRAM CAMP ── */'),
          ('// ── NOW vs WILL diagram interactivity ──', '// ── which of the two past events came first ──'),
          ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
           '"Clean run. You can hear which of two past events came first, and you only reach for had when the order needs saying."'),
          ('"Solid progress. Worth a look back at camp five before camp eight."',
           '"Solid progress. Worth a look back at camp three before camp eleven."'),
          ('"Good first attempt. The will/going to fork is the part to read again."',
           '"Good first attempt. The question of whether you need had at all is the part to read again."')],
         'sherpa-tensing-camp-ten-past-perfect.html')
print('camp ten written')
