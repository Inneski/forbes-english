# -*- coding: utf-8 -*-
s = open('/tmp/pp_stage2.html', encoding='utf-8').read()

# capture the interactive stage SVG before the section is rewritten
_st = s.index('<svg viewBox="0 0 640 344"')
STAGE_SVG = s[_st:s.index('</svg>', _st) + 6]

def swap(a_mark, b_mark, new):
    global s
    a = s.index(a_mark); b = s.index(b_mark, a)
    s = s[:a] + new + s[b:]

# ── interactive section: intro + panels ───────────────────────────────
swap('      <h2>Past vs. now</h2>', '    <div class="camp" id="quiz">',
'''      <h2>Three ropes to now</h2>
      <div class="diagram-card">
        <p class="diagram-intro">The past simple block on the left is closed &mdash; a stated time, over. Everything green is still attached to the present: a period that has not ended, an experience with no date on it, and something that finished moments ago and is still showing. Click any block to see it in sentences.</p>
        <div class="diagram-stage">
          __STAGE__
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel" id="panel-pp">
            <h4 id="panel-pp-title">Present perfect &mdash; still attached</h4>
            <ul id="panel-pp-list"></ul>
          </div>
          <div class="diagram-panel is-now" id="panel-past">
            <h4 id="panel-past-title">Past simple &mdash; cut loose</h4>
            <ul id="panel-past-list"></ul>
          </div>
        </div>
      </div>
    </div>

''')

s = s.replace('__STAGE__', STAGE_SVG, 1)
assert s.count('viewBox="0 0 640 344"') == 2, s.count('viewBox="0 0 640 344"')

# ── diagram JS ────────────────────────────────────────────────────────
swap('// ── PAST vs NOW diagram interactivity ──', '// ── QUIZ ──',
'''// ── THREE ROPES diagram interactivity ──
var SHAPES = {
  "shape-unfinished": {
    panel: "pp",
    title: "Unfinished time period",
    items: [
      "I <em>have lived</em> here for ten years.",
      "She <em>has worked</em> at the clinic since April.",
      "We <em>haven't had</em> a day off this week."
    ]
  },
  "shape-unspecified": {
    panel: "pp",
    title: "Unspecified time",
    items: [
      "<em>Have</em> you ever <em>been</em> to Scotland?",
      "Yes &mdash; I <em>have been</em> there a few times.",
      "He <em>has never eaten</em> oysters."
    ]
  },
  "shape-recent": {
    panel: "pp",
    title: "Very recent &mdash; the result is still here",
    items: [
      "Doris <em>has just made</em> coffee.",
      "They <em>have already left</em>.",
      "The train <em>hasn't arrived</em> yet."
    ]
  },
  "shape-now": {
    panel: "pp",
    title: "Now &mdash; the moment you are speaking from",
    items: [
      "I <em>live</em> here now.",
      "The coffee <em>is</em> still hot.",
      "Everything green above is roped to this box."
    ]
  },
  "shape-past": {
    panel: "past",
    title: "Past simple &mdash; cut loose",
    items: [
      "I <em>moved</em> here ten years ago.",
      "I <em>went</em> to Scotland in 2019.",
      "Doris <em>made</em> the coffee at eight."
    ]
  }
};

function renderPanel(which, title, items){
  document.getElementById("panel-" + which + "-title").innerHTML = title;
  var ul = document.getElementById("panel-" + which + "-list");
  ul.innerHTML = "";
  items.forEach(function(txt){
    var li = document.createElement("li");
    li.innerHTML = txt;
    ul.appendChild(li);
  });
}
renderPanel("pp", SHAPES["shape-unfinished"].title, SHAPES["shape-unfinished"].items);
renderPanel("past", SHAPES["shape-past"].title, SHAPES["shape-past"].items);

function pulseShape(el){
  el.animate(
    [{ filter: "brightness(1)" }, { filter: "brightness(1.14)" }, { filter: "brightness(1)" }],
    { duration: 380, easing: "ease-out" }
  );
}

Object.keys(SHAPES).forEach(function(id){
  var el = document.getElementById(id);
  if (!el) return;
  var cfg = SHAPES[id];
  el.setAttribute("aria-label", "Show examples: " + cfg.title.replace(/<[^>]+>/g, ""));
  var activate = function(){
    pulseShape(el);
    renderPanel(cfg.panel, cfg.title, cfg.items);
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    document.getElementById("panel-" + cfg.panel).style.outline =
      "2px solid " + (cfg.panel === "past" ? "#B08968" : "#0F6E56");
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){
    if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); }
  });
});

''')

# ── quiz ──────────────────────────────────────────────────────────────
q0 = s.index('var questions = [')
q1 = s.index('\n];', q0) + 3
QUIZ = '''var questions = [
  {
    prompt: "I _____ here for ten years \\u2014 and I'm still here. (live)",
    hint: "The ten years are not over.",
    correct: "have lived",
    options: ["have lived", "lived", "live", "am living"],
    explain: "The period is still running, so the present perfect keeps it attached to now: have lived."
  },
  {
    prompt: "I _____ here ten years ago.",
    hint: "\\"Ten years ago\\" is a finished, stated time.",
    correct: "moved",
    options: ["moved", "have moved", "move", "was moving"],
    explain: "A stated finished time sends you back to camp three: past simple, moved."
  },
  {
    prompt: "_____ you ever been to Scotland?",
    hint: "No time is given \\u2014 the question is about experience.",
    correct: "Have",
    options: ["Have", "Did", "Are", "Were"],
    explain: "With ever and no stated time, the present perfect asks about experience: Have you ever been\\u2026?"
  },
  {
    prompt: "Doris has just _____ coffee \\u2014 it's still hot. (make)",
    hint: "Have / has takes the past participle, not the past simple.",
    correct: "made",
    options: ["made", "make", "making", "makes"],
    explain: "Has + past participle. Make \\u2192 made \\u2192 made, so: has just made."
  },
  {
    prompt: "She _____ at the clinic since April. (work)",
    hint: "Since points at a starting point that runs up to now.",
    correct: "has worked",
    options: ["has worked", "worked", "works", "is working"],
    explain: "Since anchors an unfinished period, so the present perfect: has worked."
  },
  {
    prompt: "_____ the report yet?",
    hint: "Yet belongs to something still outstanding.",
    correct: "Have they finished",
    options: ["Have they finished", "Did they finish", "Are they finishing", "Do they finish"],
    explain: "Yet marks something expected but not done, which keeps it in the present perfect: Have they finished\\u2026 yet?"
  },
  {
    prompt: "We _____ to Lisbon last spring. (go)",
    hint: "Last spring names a finished time.",
    correct: "went",
    options: ["went", "have gone", "have been", "were going"],
    explain: "Last spring is stated and finished \\u2014 past simple, went. Have gone would clash with it."
  },
  {
    prompt: "He _____ oysters. (never / eat)",
    hint: "A life experience, counted up to now.",
    correct: "has never eaten",
    options: ["has never eaten", "never ate", "never eats", "was never eating"],
    explain: "Never with no stated time is experience up to the present: has never eaten."
  },
  {
    prompt: "How long _____ you known her?",
    hint: "How long asks about a period still running.",
    correct: "have",
    options: ["have", "did", "are", "do"],
    explain: "How long + present perfect measures a period that reaches the present: How long have you known her?"
  },
  {
    prompt: "The village _____ a lot since the road opened. (change)",
    hint: "Since again \\u2014 and the change is visible now.",
    correct: "has changed",
    options: ["has changed", "changed", "changes", "was changing"],
    explain: "Since opens a period that runs to now, and the result is in front of you: has changed."
  }
];'''
s = s[:q0] + QUIZ + s[q1:]

open('/home/claude/forbes-english/sherpa-tensing-camp-four-present-perfect.html', 'w', encoding='utf-8').write(s)
print('page written')
