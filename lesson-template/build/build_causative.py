# -*- coding: utf-8 -*-
"""The moon: the causative — you arrange it, somebody else does it."""
import sys
sys.path.insert(0, '/tmp')
sys.path.insert(0, 'lesson-template')
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES
from build_c11_12_13 import chart, fork, signals, interactive, questions, js, palette

SLATE, PALE, INK = "#4A6E80", "#CFE0E7", "#2A4854"


def diagram(uid='cs', groups=False):
    you = ('<rect x="88" y="150" width="104" height="149" rx="4" fill="#2F4A57"/>\n'
           '      <text x="140" y="182" text-anchor="middle" class="diagram-caption" fill="#E8F1F5" '
           'style="font-size:12px;letter-spacing:.04em" pointer-events="none">YOU</text>\n'
           '      <text x="140" y="206" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" '
           'fill="#B7CDD8" pointer-events="none">arrange it</text>\n'
           '      <text x="140" y="228" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" '
           'fill="#B7CDD8" pointer-events="none">and pay for it</text>')
    them = ('<rect x="278" y="118" width="118" height="181" rx="4" fill="none" stroke="#7FA6B6" '
            'stroke-width="1.6" stroke-dasharray="5 4"/>\n'
            '      <text x="337" y="150" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" '
            'font-weight="700" fill="#9FC0CE" letter-spacing="1.4" pointer-events="none">SOMEBODY ELSE</text>\n'
            '      <text x="337" y="176" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" '
            'fill="#9FC0CE" pointer-events="none">does the work</text>\n'
            '      <text x="337" y="196" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" '
            'fill="#9FC0CE" pointer-events="none">and is rarely named</text>')
    thing = ('<rect x="452" y="150" width="118" height="149" rx="4" fill="#7FA6B6"/>\n'
             '      <text x="511" y="182" text-anchor="middle" class="diagram-caption" fill="#132029" '
             'style="font-size:12px;letter-spacing:.04em" pointer-events="none">THE THING</text>\n'
             '      <text x="511" y="206" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" '
             'fill="#1E323C" pointer-events="none">gets done</text>')
    if groups:
        you = ('<g class="diagram-shape" id="shape-you" tabindex="0" role="button" '
               'aria-label="Show causative examples">\n        %s\n      </g>' % you)
        them = ('<g class="diagram-shape" id="shape-them" tabindex="0" role="button" '
                'aria-label="Show the unnamed doer examples">\n        %s\n      </g>' % them)
    return '''<svg%s viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Three boxes across a line: you, who arrange it; a dashed box for somebody else, who does the work and is rarely named; and the thing, which gets done.">
      <defs>
        <marker id="cs-%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M0,1 L9,5 L0,9 z" fill="#7FA6B6"/>
        </marker>
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
      <line x1="24" y1="299" x2="616" y2="299" stroke="#1c130c" stroke-width="2"/>
      %s
      %s
      %s
      <line x1="200" y1="224" x2="270" y2="224" stroke="#7FA6B6" stroke-width="1.6" marker-end="url(#cs-%s)"/>
      <line x1="404" y1="224" x2="444" y2="224" stroke="#7FA6B6" stroke-width="1.6" marker-end="url(#cs-%s)"/>
      <text x="235" y="214" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="700" fill="#7FA6B6" pointer-events="none">have / get</text>
      <text x="424" y="214" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="700" fill="#7FA6B6" pointer-events="none">done</text>
      <text x="140" y="317" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#5E7683" pointer-events="none">the subject of the sentence</text>
      <text x="511" y="317" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#5E7683" pointer-events="none">what actually changes</text>
    </svg>''' % ('' if groups else ' class="hero-diagram"', uid, you, them, thing, uid, uid)


CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Moon briefing</div>
      <h2>When to use it</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The causative is the sentence for work you <strong>arrange</strong> rather than do. You are still the subject &mdash; it is your money and your decision &mdash; but the hands belong to somebody you usually do not bother to name.</p>
      ''' + rule_grid([
    ('A service you pay for', 'The classic use, and the reason it exists.',
     '"I <em>had</em> my hair <em>cut</em> on Friday."'),
    ('Work on a house, a car, a tooth', 'Anywhere a professional does the thing to your thing.',
     '"We <em>had</em> the kitchen <em>rewired</em>."'),
    ('<em>Get</em> instead of <em>have</em>', 'More informal, and slightly more effort on your part.',
     '"I must <em>get</em> this jacket <em>cleaned</em>."'),
    ('Something bad that happened to you', 'Here you arranged nothing. This is the other causative.',
     '"They <em>had</em> their car <em>stolen</em>."'),
    ('Making somebody do it', 'With a person and no <em>to</em>: this one is about authority.',
     '"She <em>had</em> the porter <em>carry</em> the bags."'),
    ('Persuading somebody to do it', '<em>Get</em> + person takes <em>to</em>. <em>Have</em> never does.',
     '"I <em>got</em> my brother <em>to</em> help."'),
]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building it</div>
      <h2>How it&#39;s built</h2>
      ''' + rule_grid([
    ('The everyday one', 'subject + have + <strong>thing</strong> + past participle', '"I <em>had</em> the car <em>serviced</em>."'),
    ('The informal one', 'subject + get + <strong>thing</strong> + past participle', '"I <em>got</em> the car <em>serviced</em>."'),
    ('With a person, using <em>have</em>', 'subject + have + <strong>person</strong> + infinitive', '"He <em>had</em> the plumber <em>look</em> at it."'),
    ('With a person, using <em>get</em>', 'subject + get + <strong>person</strong> + <em>to</em> + infinitive', '"He <em>got</em> the plumber <em>to look</em> at it."'),
], 'form-grid') + chart(
    'The word order is the whole trick',
    'The thing comes <em>before</em> the participle, never after it. Put the participle next to '
    '<em>have</em> and you have written the present perfect instead, which says something completely '
    'different about who did the work.',
    ['Sentence', 'Means', 'Who did it'],
    [['I <em>had cut</em> my hair.', 'Present perfect: I did it myself, earlier.', 'You, with scissors.'],
     ['I <em>had my hair cut</em>.', 'Causative: I arranged it.', 'A hairdresser.'],
     ['I <em>have repaired</em> the roof.', 'I climbed up and repaired it.', 'You.'],
     ['I <em>have had the roof repaired</em>.', 'I paid somebody to.', 'A roofer.']]) + chart(
    'It moves through every tense',
    'Only <em>have</em> changes. The thing and the participle behind it never move, so once you can hear '
    'the order you can build it in any tense on the mountain.',
    ['Tense', 'Example', 'Camp'],
    [['Present simple', 'I <em>have</em> my hair cut every month.', 'Camp two'],
     ['Past simple', 'I <em>had</em> my hair cut on Friday.', 'Camp three'],
     ['Present perfect', 'I <em>have had</em> my hair cut.', 'Camp four'],
     ['Future', 'I<em>&#39;ll have</em> my hair cut before the wedding.', 'Camp seven'],
     ['Continuous', 'I<em>&#39;m having</em> my hair cut at three.', 'Camp one']]) + chart(
    'Three mistakes worth naming',
    'Almost every error with the causative is one of these three.',
    ['Not this', 'This', 'Why'],
    [['I had cut my hair at the salon.', 'I had my hair cut at the salon.',
      'The thing goes between <em>had</em> and the participle. Otherwise you cut it yourself.'],
     ['I had the plumber to look at it.', 'I had the plumber look at it.',
      '<em>Have</em> + person takes the bare infinitive. Only <em>get</em> takes <em>to</em>.'],
     ['I had my hair cutted.', 'I had my hair cut.',
      'It is the third form, and for <em>cut</em> that is <em>cut</em>.']]) + '''
    </div>

    ''' + fork(
    '<em>Have</em> or <em>get</em>?',
    'They are close enough that most of the time either works. Where they differ is in how much effort '
    'the sentence implies on your part, and what follows when a person is involved.',
    ['Question', 'have', 'get'],
    [['Register', 'Neutral, and slightly more formal.', 'Informal, and more common in speech.'],
     ['With a person?', 'Bare infinitive: "have him look".', 'Takes <em>to</em>: "get him <em>to</em> look".'],
     ['Any effort implied?', 'None. You simply arranged it.', 'Some. You had to persuade or chase.'],
     ['Something bad?', 'Yes: "they had their car stolen".', 'Yes: "he got his phone taken".']],
    'The pair that shows the order: <em>"I had cut my hair"</em> &mdash; I stood in front of a mirror with '
    'scissors. <em>"I had my hair cut"</em> &mdash; I sat in a chair and paid. Three words, same words, and '
    'the only difference is where <em>my hair</em> sits.',
    [('sherpa-tensing-cloud-used-to.html', '&larr; The clouds &middot; used to'),
     ('sherpa-tensing-route-map.html', 'The route map')]) + signals(
    None or 'Where you will meet it',
    ['at the hairdresser&#39;s', 'at the garage', 'at the dentist&#39;s',
     'building work &middot; repairs', 'printing &middot; framing &middot; dry cleaning',
     'anything you pay somebody to do'],
    'The other causative &mdash; nothing arranged',
    ['have your car stolen', 'have your phone taken', 'have your flight cancelled',
     'get your fingers burnt', 'have your wallet lifted', 'have your hours cut'],
    'A useful habit: if you can put <em>somebody else did it, and I organised it</em> after the sentence '
    'and it still makes sense, the causative is the form you want.') + interactive(
    MARK_PANES, 'Interactive', 'You, them, and the thing',
    'Three boxes and two arrows. You are still the subject on the left, because it was your decision and '
    'your money. The thing on the right is what actually changes. The dashed box in the middle is whoever '
    'did the work &mdash; drawn dashed for the same reason as on the descent, because English lets you '
    'leave them out entirely. Click your box or theirs to see it in a sentence.',
    diagram('csb', groups=True),
    ['panel-you', 'You &mdash; the one who arranged it',
     'panel-them', 'Them &mdash; the one who did it'])

Q = questions([
    ("I _____ on Friday. (have / my hair / cut)", "Where does the thing go?", "had my hair cut",
     ["had my hair cut", "had cut my hair", "have cut my hair", "had my hair cutted"],
     "The thing goes between had and the participle. Had cut my hair would mean you did it yourself."),
    ("We _____ last month. (have / the kitchen / rewire)", "A professional did the work.", "had the kitchen rewired",
     ["had the kitchen rewired", "had rewired the kitchen", "have the kitchen rewire", "had the kitchen rewiring"],
     "Have + thing + past participle. Rewire / rewired / rewired."),
    ("I must _____ before the interview. (get / this jacket / clean)", "The informal one.", "get this jacket cleaned",
     ["get this jacket cleaned", "get clean this jacket", "get this jacket to clean", "have this jacket cleaning"],
     "Get works exactly like have with a thing: get + thing + participle."),
    ("They _____ outside the station. (have / their car / steal)", "Nothing was arranged here.", "had their car stolen",
     ["had their car stolen", "had stolen their car", "have their car steal", "had their car stole"],
     "The other causative: something bad happened to you. Steal / stole / stolen."),
    ("She _____ the bags. (have / the porter / carry)", "A person, using have.", "had the porter carry",
     ["had the porter carry", "had the porter to carry", "had carried the porter", "had the porter carried"],
     "Have + person takes the bare infinitive, with no to."),
    ("I _____ me with the boxes. (get / my brother / help)", "A person, using get.", "got my brother to help",
     ["got my brother to help", "got my brother help", "got helped my brother", "had my brother to help"],
     "Get + person always takes to. Have never does."),
    ("I _____ myself, and it was a disaster.", "Who held the scissors?", "cut my hair",
     ["cut my hair", "had my hair cut", "got my hair cut", "had cut my hair"],
     "Myself rules out the causative entirely: you did it."),
    ("_____ you _____ yet? (have / the car / service)", "Question with the present perfect.", "Have ... had the car serviced",
     ["Have ... had the car serviced", "Have ... the car serviced", "Did ... had the car serviced", "Have ... serviced the car"],
     "The causative sits inside any tense: have had + thing + participle."),
    ("We _____ next week. (have / the roof / repair)", "Arranged, not done by you.", "are having the roof repaired",
     ["are having the roof repaired", "are having repaired the roof", "have the roof repairing", "are had the roof repaired"],
     "The continuous of an arrangement: are having + thing + participle."),
    ("He _____ at the airport. (have / his phone / take)", "Something bad.", "had his phone taken",
     ["had his phone taken", "had taken his phone", "have his phone take", "had his phone took"],
     "Take / took / taken. Nothing was arranged; it happened to him."),
    ("I _____ before the wedding. (will / have / my suit / press)", "Future.", "will have my suit pressed",
     ["will have my suit pressed", "will have pressed my suit", "will my suit have pressed", "will have my suit press"],
     "Will + have + thing + participle."),
    ("She _____ every six weeks. (have / her hair / colour)", "A routine.", "has her hair coloured",
     ["has her hair coloured", "has coloured her hair", "have her hair coloured", "has her hair colour"],
     "Present simple, third person: has + thing + participle."),
    ("I _____ the quote by Friday. (get / them / send)", "Persuading a person.", "got them to send",
     ["got them to send", "got them send", "got sent them", "had them to send"],
     "Get + person + to + infinitive."),
    ("The photos _____ next week. (have / frame)", "No doer at all.", "are being framed",
     ["are being framed", "are having framed", "have framed", "are had framed"],
     "With no arranger in the sentence, the plain passive does the job."),
])

assemble(
    hero('The moon &middot; the causative',
         "Somebody else did it, and you arranged it",
         'Not a tense but a shape, and one English uses constantly. You stay the subject &mdash; it was '
         'your decision and your money &mdash; while the hands belong to a hairdresser, a garage or a '
         'roofer who never makes it into the sentence at all. The whole trick is where you put the thing.',
         diagram('cs')),
    CAMPS,
    js([], [], ['shape-you', 'panel-you', 'shape-them', 'panel-them'], [SLATE, '#7FA6B6'])
    .replace('var exA = [\n\n];', '''var exA = [
  "I <em>had</em> my hair <em>cut</em> on Friday.",
  "We <em>had</em> the kitchen <em>rewired</em>.",
  "I must <em>get</em> this jacket <em>cleaned</em>."
];''')
    .replace('var exB = [\n\n];', '''var exB = [
  "&hellip; <em>by</em> a hairdresser on the high street.",
  "&hellip; <em>by</em> an electrician from the village.",
  "&hellip; and normally you would not mention them at all."
];'''),
    Q,
    palette('#16232A', '#54707D', '#F6FAFB', '#3F6577', '#2A4854', '#C7DAE1', '#EAF2F5'),
    '<title>Sherpa Tensing - The Moon: The Causative</title>',
    [('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── YOU vs THEM DIAGRAM ── */'),
     ('// ── NOW vs WILL diagram interactivity ──', '// ── you, them, and the thing ──'),
     ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
      '"Clean run. The thing goes in the middle, and you know when get needs a to."'),
     ('"Solid progress. Worth a look back at camp five before camp eight."',
      '"Solid progress. Worth another look at the word order before you go on."'),
     ('"Good first attempt. The will/going to fork is the part to read again."',
      '"Good first attempt. Where the thing sits is the part to read again."'),
     ('Camp seven', 'The moon')],
    'sherpa-tensing-cloud-causative.html')
print('causative written')
