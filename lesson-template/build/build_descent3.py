# -*- coding: utf-8 -*-
"""Descent three · past simple passive — the pilot for the whole descent."""
import sys
sys.path.insert(0, '/tmp')
sys.path.insert(0, 'lesson-template')
import passive_diagram as P
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES
from build_c11_12_13 import chart, fork, signals, interactive, questions, js

CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Descent briefing</div>
      <h2>When to use it</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The passive is not a different tense. It is the same past simple with the doer let go &mdash; and the reason you let them go is always one of these six.</p>
      ''' + rule_grid([
    ('You do not know who',
     'Nobody can tell you the doer, so the sentence does without one.',
     '"The window <em>was broken</em> during the night."'),
    ('The doer does not matter',
     'The event is the news; who did it is a footnote.',
     '"The bridge <em>was built</em> in 1890."'),
    ('The doer is obvious',
     'Saying it would be a waste of everyone&#39;s time.',
     '"He <em>was arrested</em> on Tuesday."'),
    ('You would rather not say',
     'The most quietly political sentence in English does exactly this.',
     '"A mistake <em>was made</em>."'),
    ('Putting the important thing first',
     'English gives the front of the sentence to what the sentence is about.',
     '"Three villages <em>were evacuated</em>."'),
    ('Putting the doer back with <em>by</em>',
     'When the doer <em>is</em> the point, it goes at the end, where the weight falls.',
     '"The report <em>was written</em> by an intern."'),
]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the passive</div>
      <h2>How it&#39;s built</h2>
      ''' + rule_grid([
    ('Affirmative', 'subject + was / were + <strong>past participle</strong>', '"The letter <em>was sent</em> on Friday."'),
    ('Negative', "subject + wasn&#39;t / weren&#39;t + past participle", '"The forms <em>weren&#39;t signed</em>."'),
    ('Yes / No questions', 'Was / Were + subject + past participle?', '"<em>Was it repaired</em>?"'),
    ('With the doer', 'subject + was / were + participle + <strong>by</strong> + doer', '"It <em>was repaired</em> by the landlord."'),
], 'form-grid') + chart(
    'Turning an active sentence around',
    'Three moves, always in the same order: the object comes to the front, the verb becomes '
    '<em>was/were</em> + participle, and the old subject either disappears or goes to the back behind '
    '<em>by</em>.',
    ['Active', 'Passive', 'What moved'],
    [['The storm damaged the roof.', 'The roof was damaged.', 'The roof came first; the storm went.'],
     ['Someone stole my bike.', 'My bike was stolen.', '<em>Someone</em> was carrying no information.'],
     ['Brunel built the bridge.', 'The bridge was built by Brunel.', 'Brunel matters, so he stayed &mdash; at the end.'],
     ['They cancelled the trains.', 'The trains were cancelled.', 'Plural subject, so <em>were</em>.']]) + chart(
    'Conjugation chart',
    'Only <em>be</em> changes, exactly as it does in camp three: <em>was</em> for I, he, she and it; '
    '<em>were</em> for the rest. The participle never moves.',
    ['Subject', 'Affirmative', 'Negative', 'Question'],
    [['It', 'It was found', "It wasn&#39;t found", 'Was it found?'],
     ['They', 'They were found', "They weren&#39;t found", 'Were they found?'],
     ['I', 'I was asked', "I wasn&#39;t asked", 'Was I asked?'],
     ['You', 'You were asked', "You weren&#39;t asked", 'Were you asked?'],
     ['We', 'We were told', "We weren&#39;t told", 'Were we told?']]) + chart(
    'Three mistakes worth naming',
    'Almost every error with the passive is one of these three.',
    ['Not this', 'This', 'Why'],
    [['The window was break.', 'The window was broken.',
      'After <em>be</em> comes the third form, never the infinitive or the past simple.'],
     ['It was happened last night.', 'It happened last night.',
      'Verbs with no object have no passive &mdash; happen, arrive, die, exist, seem.'],
     ['The bridge was built from Brunel.', 'The bridge was built by Brunel.',
      'The doer takes <em>by</em>. <em>With</em> is for the instrument: cut with a knife.']]) + '''
    </div>

    ''' + fork(
    'Active or passive?',
    'Neither is better. The question is only what the sentence is about &mdash; because whatever you put '
    'at the front is what the reader will think it is about.',
    ['Question', 'Passive', 'Active'],
    [['What is the sentence about?', 'The thing it happened to.<br>"The roof <em>was damaged</em>."',
      'The one who did it.<br>"The storm <em>damaged</em> the roof."'],
     ['Do you know the doer?', 'Often not &mdash; and you do not need to.', 'Yes, and you are naming them.'],
     ['Where does the doer go?', 'At the end with <em>by</em>, or nowhere at all.', 'At the front, as the subject.'],
     ['Which is shorter?', 'Longer by two or three words.', 'Usually shorter. Prefer it when both work.']],
    'The pair worth remembering: <em>"I made a mistake"</em> and <em>"A mistake was made"</em> say the '
    'same thing about the world and completely different things about the speaker. That choice is the '
    'passive&#39;s real power, and the reason to know when someone is using it on you.',
    [('sherpa-tensing-camp-three-past-simple.html', '&larr; Camp three &middot; past simple, active'),
     ('sherpa-tensing-route-map.html', 'The route map')]) + signals(
    None or 'Reach for the passive when',
    ['the doer is unknown', 'the doer is irrelevant', 'the doer is obvious',
     'the process is the point', 'a report or notice needs distance', 'the object is the topic'],
    'Verbs with no passive at all',
    ['happen &middot; occur', 'arrive &middot; go &middot; come', 'die &middot; live',
     'exist &middot; belong', 'seem &middot; appear', 'become &middot; fall'],
    'The test for whether a verb can go passive: does it take an object? <em>They built it</em> has one, '
    'so it turns. <em>It happened</em> has none, so it cannot.') + interactive(
    MARK_PANES, 'Interactive', 'The event, and the doer you dropped',
    'The block is the same past simple block as the ascent, lit from above instead of fading into the '
    'dark &mdash; because the tense has not changed, only the light. Inside it sits a dashed box: the '
    'doer. It is drawn inside the event rather than beside it because the doer is not a moment in time, '
    'it is a part of the sentence &mdash; and it is dashed because most of the time nobody says it. '
    'Click either to see it in a sentence.',
    P.past_simple_passive('pspb', groups=True),
    ['panel-event', 'The event &mdash; now the subject',
     'panel-agent', 'The doer &mdash; optional, and usually gone'])

Q = questions([
    ("The window _____ during the night. (break)", "Nobody knows who.", "was broken",
     ["was broken", "was break", "were broken", "was breaked"],
     "Was + the third form: was broken. Break / broke / broken."),
    ("The bridge _____ in 1890. (build)", "The date is the news, not the builder.", "was built",
     ["was built", "was build", "were built", "was builded"],
     "The participle of build is built, and the singular subject takes was."),
    ("Three villages _____ before dawn. (evacuate)", "Plural subject.", "were evacuated",
     ["were evacuated", "was evacuated", "were evacuate", "evacuated"],
     "Villages is plural, so were, and the participle takes -ed: were evacuated."),
    ("The report _____ by an intern. (write)", "The doer is the point here.", "was written",
     ["was written", "was wrote", "were written", "was write"],
     "The doer goes at the end behind by, and the participle of write is written."),
    ("The forms _____ , so the claim failed. (not / sign)", "Negative, plural.", "weren&#39;t signed",
     ["weren&#39;t signed", "wasn&#39;t signed", "weren&#39;t sign", "didn&#39;t signed"],
     "Weren&#39;t + participle. The plural forms takes were."),
    ("_____ the roof _____ in the storm? (damage)", "Question order.", "Was ... damaged",
     ["Was ... damaged", "Did ... damaged", "Were ... damaged", "Was ... damage"],
     "Questions invert be: Was the roof damaged? Roof is singular."),
    ("It _____ last night, and nobody saw it coming. (happen)", "Careful with this verb.", "happened",
     ["happened", "was happened", "were happened", "was happening"],
     "Happen takes no object, so it has no passive. It happened."),
    ("The trains _____ because of the ice. (cancel)", "Plural, and no doer worth naming.", "were cancelled",
     ["were cancelled", "was cancelled", "were cancel", "cancelled by"],
     "Trains is plural, so were cancelled. Who cancelled them adds nothing."),
    ("He _____ on Tuesday morning. (arrest)", "The doer is obvious.", "was arrested",
     ["was arrested", "were arrested", "was arrest", "did arrested"],
     "By the police goes without saying, so the passive drops it."),
    ("My bike _____ outside the station. (steal)", "Someone did it, but who?", "was stolen",
     ["was stolen", "was stole", "were stolen", "was stealed"],
     "Steal / stole / stolen. Someone stole my bike carries no information, so the passive is better."),
    ("The bridge was built _____ Brunel.", "Doer, not instrument.", "by",
     ["by", "from", "with", "of"],
     "The doer of a passive takes by. With is for the instrument: cut with a knife."),
    ("We _____ nothing about the change until Friday. (tell)", "The people affected come first.", "were told",
     ["were told", "was told", "were telled", "did told"],
     "We is plural, so were, and the participle of tell is told."),
    ("A mistake _____ , and the letter went out anyway. (make)", "The famous one.", "was made",
     ["was made", "was maked", "were made", "was make"],
     "Was made. The passive here is doing real work: it removes the person who made it."),
    ("The keys _____ under the mat, exactly where he said. (find)", "Plural subject, irregular participle.", "were found",
     ["were found", "was found", "were finded", "were find"],
     "Keys is plural, so were, and find / found / found."),
])

PALETTE = '''  :root{
    --ink:#F2E7DC;
    --ink-soft:#B9A794;
    --paper:#17120E;
    --card:#221A14;
    --accent:#C79A72;
    --accent-dark:#E3C3A4;
    --accent-light:#3D2E22;
    --accent-lighter:#1E1712;
    --good:#7BD3A3;
    --good-bg:#12301F;
    --bad:#F09090;
    --bad-bg:#33191A;
    --radius:14px;
  }'''

DARK_CSS = '''
  /* ── descent overrides: the three places the ascent hard-codes light ── */
  .diagram-panel.is-now{background:#1B2229;border-color:#33434F;}
  .opt-btn{background:var(--card);color:var(--ink);}
  .opt-btn:hover{background:#2C2219;}
  .card,.rule-card,.chart-wrap,.signal-box,.diagram-card,.diagram-panel{box-shadow:0 2px 12px rgba(0,0,0,.45);}
'''

out = assemble(
    hero('Descent three &middot; past simple passive',
         'When nobody did it',
         'Coming down, the same tenses are lit from the other side. The passive keeps the event and lets '
         'the doer go &mdash; because you do not know who, or it does not matter, or you would rather '
         'not say. Same past simple, same place on the line, different subject.',
         P.past_simple_passive('psp')),
    CAMPS,
    js([], [], ['shape-event', 'panel-event', 'shape-agent', 'panel-agent'], ['#C79A72', '#8A7358'])
    .replace('var exA = [\n\n];', '''var exA = [
  "The window <em>was broken</em> during the night.",
  "Three villages <em>were evacuated</em> before dawn.",
  "A mistake <em>was made</em>."
];''')
    .replace('var exB = [\n\n];', '''var exB = [
  "&hellip; <em>by</em> an intern.",
  "&hellip; <em>by</em> Brunel.",
  "&hellip; and most of the time, nothing at all."
];'''),
    Q, PALETTE,
    '<title>Sherpa Tensing - Descent Three: When Nobody Did It (Past Simple Passive)</title>',
    [('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── EVENT vs DOER DIAGRAM CAMP ── */'),
     ('// ── NOW vs WILL diagram interactivity ──', '// ── the event and the dropped doer ──'),
     ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
      '"Clean run. You can turn a sentence around and you know when the doer is worth keeping."'),
     ('"Solid progress. Worth a look back at camp five before camp eight."',
      '"Solid progress. Worth a look back at camp three before the rest of the descent."'),
     ('"Good first attempt. The will/going to fork is the part to read again."',
      '"Good first attempt. The third form is the part to read again."'),
     ('Return to base camp', 'Back to the route map'),
     ('\n</style>', DARK_CSS + '</style>')],
    'sherpa-tensing-descent-three-past-simple-passive.html')
print('descent three written,', len(out), 'bytes')
