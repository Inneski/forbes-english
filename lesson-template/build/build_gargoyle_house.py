# -*- coding: utf-8 -*-
"""The Gargoyle House, Parts 1 and 2 (C1). House style 1, two decks.

Built 2026-11-14 from a list of 100 words and phrases Innes pasted ("make an
interior design themed english class focussing on this vocabulary"). It is
the second vocabulary lesson for the same field as
`interior-design-vocabulary.html`. One hundred items is two classes, so the
list is split 50 / 50 along one story: a small design studio takes on a
run-down country house for a newly rich client.

  Part 1, The Brief: the house, the client, the studio, the pitch.
  Part 2, The Build: the contract, the site, the politics, the crisis.

Each chapter is read -> match six -> choose -> write: a short scene with six
of the words in it, those six matched to meanings, then the rest of the
chapter's words as multiple choice and typed gaps. Every item on the list is
scored exactly once.

Several entries on the list carry a dictionary's first sense, not the one a
designer meets (RUN DOWN a pedestrian, TACKY paint, BLINKERED horses, REMIT
a debt, UPFRONT = at the front, EXPLOIT). The deck teaches the useful sense
and names the other in the explanation; TACKY keeps the listed one, because
wet paint is the trade's own use of it. OUTSTANDING is on the list twice and
is tested twice (an unpaid invoice, excellent plasterwork).

Explanations are English sentences, not keys: the words being explained are
the lesson, and they stay in English in every language (HOUSE-STYLE §7).

Run from the repo root:  py lesson-template/build/build_gargoyle_house.py [1|2]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import hs2quiz as H

F = 'GargoyleHouse'


def q(stem, options, why):
    return dict(stem=stem, options=options, correct=0, why=why)


def story(ek, tk, text):
    return '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">x</div>
        <h2 class="slide-title" data-i18n="%s">x</h2>
      </div></div>
      <div class="slide-body">
        <div class="card" style="padding:22px 28px">
          <p class="prose" style="font-size:23px;line-height:1.5">%s</p>
          <p class="prose dim" style="margin-top:12px;font-size:16.5px" data-i18n="stNote">x</p>
        </div>
      </div>
    </section>
''' % (ek, tk, text)


# ── the chapters ───────────────────────────────────────────────────────
# (eyebrow key, story title key, story, match pairs, mc items, gap rows, bank,
#  plate briefs: story + one per mc item)
P1 = [
    ('e1', 's1T',
     'Ashby Hall has stood empty for nine years. Stone <strong>gargoyles</strong> lean out from the roof, each face '
     'more <strong>grotesque</strong> than the last. The <strong>gutters</strong> are full of moss, one '
     '<strong>drainpipe</strong> hangs loose, and the whole place looks <strong>run-down</strong>. Inside, under '
     'dust sheets, the family <strong>heirlooms</strong> are still waiting.',
     [('gargoyle', 'a carved stone figure that spouts rainwater'),
      ('gutter', 'the open channel along the edge of a roof'),
      ('drainpipe', 'the pipe that takes rainwater down a wall'),
      ('grotesque', 'ugly and distorted in a strange way'),
      ('run-down', 'in poor condition after years of neglect'),
      ('heirloom', 'a valuable object passed down in a family')],
     'A GARGOYLE throws water clear of the wall; the GUTTER collects it and the DRAINPIPE carries it down. '
     'RUN DOWN is also a verb: a car can run somebody down.',
     [q('The last Lord Ashby had no children, so the house passed to a distant ____.',
        ['heir', 'heirloom', 'novice', 'gargoyle'],
        'An HEIR is legally entitled to property or a title when its owner dies. The H is silent: “air”.'),
      q('His niece Clara, a thirty-year-old ____, inherited the hall, the debts and forty clocks.',
        ['heiress', 'heirloom', 'hostess', 'heretic'],
        'An HEIRESS is a woman who inherits, usually a fortune. An HEIRLOOM is the object, not the person.'),
      q('The portraits show very few sons: ____, in which the blood does not clot, ran in the family.',
        ['hemophilia', 'insomnia', 'arthritis', 'amnesia'],
        'HEMOPHILIA (British spelling: haemophilia) is hereditary, and even a small cut bleeds badly.'),
      q('In the entrance stands a stuffed bear holding a lamp and wearing a top hat. Truly ____!',
        ['bizarre', 'concise', 'esteemed', 'agile'],
        'BIZARRE: very strange, often in a way that amuses you.')],
     [('The east wing is so ______ that part of the ceiling has fallen in.', ['dilapidated'],
       'DILAPIDATED: fallen into ruin. The verb DILAPIDATE is rare; the adjective is common.'),
      ('Nobody had understood the ______ of the job: sixty-two rooms.', ['magnitude'],
       'MAGNITUDE: the great size or extent of something.'),
      ('Don’t touch that door: the paint is still ______.', ['tacky'],
       'TACKY paint or glue is not fully dry. Informally, TACKY also means cheap and in bad taste.')],
     ['tacky', 'dilapidated', 'magnitude'],
     ['a grand, crumbling English country house with stone gargoyles along the roof, moss in the gutters',
      'an elderly lord alone at the end of a very long dining table',
      'a young woman holding a huge ring of old keys in a hall full of clocks',
      'a wall of old family portraits in gilt frames on a staircase',
      'a stuffed bear in a top hat holding a lamp in a grand entrance hall']),
    ('e2', 's2T',
     'The buyer is Bianca Voss, who made a fortune in three years. The neighbours call her <strong>nouveau '
     'riche</strong>. She is <strong>capricious</strong>: marble on Monday, bamboo by Friday. Her ideas are '
     '<strong>outrageous</strong> (a gold lift, a shark tank) and she is <strong>oblivious</strong> to the cost. '
     'She is no <strong>conformist</strong>, and when the council says no, she <strong>puts her foot down</strong>.',
     [('nouveau riche', 'newly rich, and thought to be showy'),
      ('capricious', 'changing your mind suddenly, for no clear reason'),
      ('outrageous', 'shockingly bold and unusual'),
      ('oblivious', 'not aware of what is happening'),
      ('conformist', 'someone who follows the accepted rules'),
      ('put your foot down', 'refuse firmly to give way')],
     'NOUVEAU RICHE is a criticism: new money with no taste. You are OBLIVIOUS TO or OF something.',
     [q('She wants a ____ library: philosophy, opera scores, nothing popular.',
        ['highbrow', 'grotesque', 'oblivious', 'run-down'],
        'HIGHBROW: scholarly and refined in taste, sometimes said with a smile. The opposite is LOWBROW.'),
      q('For the tower she wants a silent room for ____: twenty minutes with a mantra, twice a day.',
        ['Transcendental Meditation', 'Experimental Renovation', 'Environmental Mediation', 'Transatlantic Navigation'],
        'TRANSCENDENTAL MEDITATION (TM) is a technique of silent meditation with a repeated mantra.'),
      q('“I love the shark tank,” said Tom. It was a ____: he didn’t want to hurt her feelings.',
        ['white lie', 'heirloom', 'dead weight', 'comedown'],
        'A WHITE LIE is a small, harmless lie told to be kind or polite.')],
     [('Every new window must ______ to the rules for historic buildings.', ['conform'],
       'CONFORM TO a rule or standard: comply with it. A CONFORMIST conforms.'),
      ('The neighbours are ______: they reject every idea that is new or foreign.', ['narrow-minded|narrow minded|blinkered'],
       'NARROW-MINDED: unwilling to listen to other people’s views.'),
      ('Like a horse that sees only the road ahead, the planning officer was ______.', ['blinkered|narrow-minded|narrow minded'],
       'BLINKERS stop a horse looking sideways, so a BLINKERED person cannot see other points of view.')],
     ['blinkered', 'conform', 'narrow-minded'],
     ['a glamorous woman in a bright suit stepping out of a gold sports car in front of an old mansion',
      'a tall library with a rolling ladder and a marble bust',
      'a small round tower room with one cushion on the floor and a candle',
      'a huge aquarium with a small shark built into a living room wall']),
    ('e3', 's3T',
     'Marlowe &amp; Finch is a small studio with a big name. Its <strong>esteemed</strong> founder, Edith Marlowe, '
     'has won every prize, yet she never <strong>rests on her laurels</strong>. Her drawings are '
     '<strong>meticulous</strong> and her ideas <strong>forward-thinking</strong>. Tom, the <strong>novice</strong>, '
     'joined on Monday. Ashby Hall will be his <strong>baptism of fire</strong>.',
     [('esteemed', 'highly respected and admired'),
      ('rest on your laurels', 'stop trying because of past success'),
      ('meticulous', 'very careful about every detail'),
      ('forward-thinking', 'in favour of new ideas and progress'),
      ('novice', 'a person who is new to a job or field'),
      ('baptism of fire', 'a very hard first experience')],
     'In ancient Greece winners wore a crown of LAUREL leaves; to REST ON YOUR LAURELS is to live off old victories.',
     [q('During her ____ as president of the Design Guild, Edith doubled its membership.',
        ['tenure', 'tenant', 'commute', 'clause'],
        'TENURE: the period for which someone holds an office or a post.'),
      q('The opera house foyer was the ____ of her career: nothing since has matched it.',
        ['pinnacle', 'guise', 'remit', 'gutter'],
        'The PINNACLE is the highest, most successful point. On a building it is a small pointed tower.'),
      q('With its clean lines and honest materials, the studio is the ____ of good taste.',
        ['epitome', 'epitomize', 'heirloom', 'magnitude'],
        'THE EPITOME OF something is a perfect example of it. Four syllables: e-PIT-o-me.'),
      q('Tom’s daily ____ is ninety minutes each way by train.',
        ['commute', 'tenure', 'remit', 'cue'],
        'COMMUTE (noun and verb): the regular journey between home and work.')],
     [('The studio works in an ______ way: short phases, with the plan reviewed every week.', ['agile'],
       'AGILE project management divides work into short phases and keeps adapting the plan.'),
      ('Tom climbed the scaffolding with surprising ______.', ['agility'],
       'AGILITY is the noun: the ability to move quickly and easily.'),
      ('Edith’s oak staircases ______ the style of the studio.', ['epitomize|epitomise'],
       'EPITOMIZE (British also EPITOMISE): be a perfect example of.')],
     ['epitomize', 'agile', 'agility'],
     ['an elegant older woman architect at a drawing board in a bright studio, a shelf of trophies behind her',
      'a gold medal on a ribbon lying on rolled architectural plans',
      'a grand opera house foyer with a sweeping staircase',
      'a calm room with one wooden chair and a linen curtain',
      'a young man asleep on a commuter train holding a cardboard tube of drawings']),
    ('e4', 's4T',
     'The pitch is on Friday. Edith <strong>maps out</strong> every room on one long sheet of paper. The concept is '
     '“Metamorphosis”: like a <strong>caterpillar</strong>, the hall will <strong>morph</strong> into something '
     'lighter. This is no quick <strong>revamp</strong>. Her slides are <strong>concise</strong>, and she gives a '
     'clear <strong>rationale</strong> for every decision.',
     [('map out', 'plan something in detail'),
      ('caterpillar', 'the larva that becomes a butterfly'),
      ('morph', 'change gradually into something else'),
      ('revamp', 'give something a new, improved form'),
      ('concise', 'short and to the point'),
      ('rationale', 'the reasons behind a decision')],
     'MORPH comes from computer animation, where one image changes smoothly into another. REVAMP is a verb and a noun.',
     [q('The estate agent ____ the hall: “a jewel”, he said, ignoring the hole in the roof.',
        ['talked up', 'mapped out', 'put down', 'locked down'],
        'TALK something UP: describe it so that it sounds better or more attractive than it is.'),
      q('Edith left her best sketch on the table as ____, and Bianca picked it up at once.',
        ['bait', 'cue', 'remit', 'clause'],
        'BAIT is food on a hook to catch a fish, and so anything used to tempt someone.'),
      q('When Edith nods, that is Tom’s ____ to switch on the lights of the model.',
        ['cue', 'bait', 'guise', 'tenure'],
        'A CUE is a signal to begin, like the line that tells an actor to come on stage.')],
     [('The design will ______ old oak and new glass into one story.', ['weave'],
       'WEAVE: make cloth from threads, and so make one whole from many connected parts.'),
      ('Cut the third chandelier: it is ______.', ['superfluous'],
       'SUPERFLUOUS: more than is needed. The stress is on PER: su-PER-flu-ous.'),
      ('Bianca’s own plan was so ______ that nobody could follow it.', ['convoluted'],
       'CONVOLUTED: complicated and hard to follow.')],
     ['convoluted', 'weave', 'superfluous'],
     ['a very long sheet of paper unrolled across a studio floor, covered in room sketches',
      'an estate agent in a shiny suit gesturing proudly at a house with a hole in its roof',
      'a single beautiful sketch of a staircase lying on a table under a lamp',
      'a small architectural model of a mansion glowing with tiny lights in a dark room']),
]

P2 = [
    ('e1', 's1T',
     'The contract runs to ninety pages. One <strong>clause</strong> is <strong>explicit</strong>: thirty per cent '
     'must be paid <strong>upfront</strong>. The garden is outside the studio’s <strong>remit</strong>. On site the '
     'crew speak five languages, so English is the <strong>lingua franca</strong>, though the foreman’s Glasgow '
     '<strong>colloquialisms</strong> defeat everyone.',
     [('clause', 'a separate section of a contract'),
      ('explicit', 'stated clearly, leaving no doubt'),
      ('upfront', 'paid in advance'),
      ('remit', 'the area a person is responsible for'),
      ('lingua franca', 'a shared language between different speakers'),
      ('colloquialism', 'an informal, everyday expression')],
     'A CLAUSE is also a unit of grammar with a subject and a verb. As a verb, REMIT means cancel a debt or '
     'a punishment. UPFRONT can simply mean at the front.',
     [q('The lawyer’s paragraph was ____: nobody on site could work out what it meant.',
        ['incomprehensible', 'intelligible', 'inconceivable', 'indispensable'],
        'INCOMPREHENSIBLE: impossible to understand.'),
      q('Tom rewrote it in plain English so that it was ____ to the whole crew.',
        ['intelligible', 'incomprehensible', 'superfluous', 'capricious'],
        'INTELLIGIBLE: clear enough to be understood. Not the same as INTELLIGENT.'),
      q('We must ____ the floor plan this week: after Friday, no more changes.',
        ['lock down', 'talk up', 'suck up', 'run down'],
        'LOCK DOWN a plan: fix it so that it cannot change. In a prison, a LOCKDOWN confines everyone to their cells.')],
     [('Two invoices are still ______: we are waiting for forty thousand pounds.', ['outstanding'],
       'OUTSTANDING: not yet paid, done or dealt with.'),
      ('“The marble will arrive ______,” wrote the supplier. Probably in May, then.', ['in due course'],
       'IN DUE COURSE: at the right time, not yet. Formal, and often a polite way to promise nothing.'),
      ('Bianca made it ______ clear that she would not pay twice.', ['abundantly'],
       'ABUNDANTLY means in large quantities; ABUNDANTLY CLEAR is a fixed pair: very clear indeed.')],
     ['abundantly', 'outstanding', 'in due course'],
     ['a thick contract and a fountain pen on a desk beside a hard hat',
      'a lawyer hidden behind a towering stack of papers',
      'a young man pinning one large sheet of plain writing to a site noticeboard, builders reading it',
      'a floor plan on a table with a heavy padlock resting on it']),
    ('e2', 's2T',
     'By June the work is <strong>in full swing</strong>: forty people, three cranes. Bianca wants to '
     '<strong>accelerate</strong> everything. The crew run on <strong>caffeine</strong>, and Tom arrives '
     '<strong>pumped</strong> every morning. The new skylight <strong>exploits</strong> every hour of daylight. '
     '<strong>Kudos</strong> to the carpenters: the staircase is finished early.',
     [('in full swing', 'at its busiest and most active'),
      ('accelerate', 'move or happen faster'),
      ('caffeine', 'the substance in coffee that keeps you awake'),
      ('pumped', 'full of energy and enthusiasm (informal)'),
      ('exploit', 'make full use of a resource'),
      ('kudos', 'praise for an achievement')],
     'KUDOS is singular and uncountable: “kudos TO the carpenters”, never “a kudo”.',
     [q('Coffee is a ____: a substance that raises the level of activity in the body.',
        ['stimulant', 'stimulator', 'sedative', 'supplement'],
        'A STIMULANT is a substance, like caffeine. A STIMULATOR is a thing or a device that stimulates.'),
      q('The physio gave the roofer a muscle ____, a small device that sends pulses into his back.',
        ['stimulator', 'stimulant', 'sedative', 'accelerator'],
        'A STIMULATOR is a device or agent that raises activity; the substance is a STIMULANT.'),
      q('Tom stood on the finished roof at sunrise, ____: he had never felt so alive.',
        ['exhilarated', 'exploited', 'dilapidated', 'oblivious'],
        'EXHILARATED: very happy and full of energy. The H is silent: ig-ZIL-a-ray-tid.'),
      q('The plasterwork is ____: the best that Edith has seen in forty years.',
        ['outstanding', 'superfluous', 'upfront', 'recurring'],
        'OUTSTANDING: exceptionally good. The same word means “not yet paid”; the context tells you which.')],
     [('Tom ran up six floors and arrived ______, unable to speak.', ['panting'],
       'PANT: breathe with short, quick breaths after effort.'),
      ('The interns felt ______: long hours, no pay and no thanks.', ['exploited'],
       'You EXPLOIT daylight (use it fully), but EXPLOITED people are used unfairly.')],
     ['exploited', 'panting'],
     ['a country house covered in scaffolding with cranes and many tiny busy builders',
      'a row of espresso cups on a workbench among tools',
      'a roofer lying on a treatment table with small pads on his back',
      'a young man standing on a new roof at sunrise with his arms wide',
      'a plasterer finishing an ornate ceiling rose from a ladder']),
    ('e3', 's3T',
     'Then Bianca’s “style consultant”, Rex, arrives. He is <strong>obsequious</strong> with her and rude to '
     'everyone else, and he <strong>sucks up</strong> at every meeting. Under the <strong>guise</strong> of helping, '
     'he rewrites the plans: Bianca is the puppet, Rex the <strong>puppeteer</strong>. His gold ceiling '
     '<strong>polarizes</strong> the team. To Edith, it is <strong>heresy</strong>.',
     [('obsequious', 'too eager to please or obey'),
      ('suck up', 'flatter someone to gain an advantage (informal)'),
      ('guise', 'an outward appearance that hides the truth'),
      ('puppeteer', 'a person who works puppets'),
      ('polarize', 'divide people into two opposing groups'),
      ('heresy', 'an opinion against accepted belief')],
     'You SUCK UP TO a person. HERESY began as a religious word and is now used, half joking, of any shocking opinion.',
     [q('“Brilliant, Bianca! Pure genius!” Rex’s ____ praise made the carpenters roll their eyes.',
        ['sycophantic', 'meticulous', 'concise', 'explicit'],
        'SYCOPHANTIC: praising powerful people too much in order to gain something. The person is a SYCOPHANT.'),
      q('Rex carries nothing, draws nothing and decides nothing. On site he is ____.',
        ['dead weight', 'in full swing', 'a stimulant', 'an heirloom'],
        'DEAD WEIGHT: the weight of something that cannot move itself, and so a person who adds nothing to a team.'),
      q('Rex claims an ____ with a famous Milan studio, but nobody there has heard of him.',
        ['affiliation', 'affiliate', 'agility', 'epitome'],
        'An AFFILIATION is an official connection with an organization. AFFILIATE is the verb.'),
      q('He seems ____ by one design guru: he repeats her rules without ever questioning them.',
        ['indoctrinated', 'exhilarated', 'dilapidated', 'accelerated'],
        'INDOCTRINATED: taught to accept a set of beliefs without questioning them.')],
     [('The gold ceiling is ______: half the team love it and half hate it.', ['divisive'],
       'DIVISIVE: causing disagreement between people. Something divisive POLARIZES them.'),
      ('While everyone worked, Rex lay ______ in a deckchair, not moving at all.', ['inert'],
       'INERT: without the power or the will to move.'),
      ('The studio is ______ with the Design Guild: officially connected to it.', ['affiliated'],
       'AFFILIATED WITH or TO an organization: officially attached to it.')],
     ['affiliated', 'inert', 'divisive'],
     ['a man in a flashy scarf bowing low to a glamorous woman on a building site',
      'a man clapping wildly while carpenters behind him roll their eyes',
      'a man asleep in a deckchair in the middle of a busy building site',
      'a business card with a tiny map of Italy on it, held between two fingers',
      'a man reading aloud from a thick book held up like a holy text']),
    ('e4', 's4T',
     'In August things <strong>go south</strong>. The gold ceiling cracks, the leak in the tower is a '
     '<strong>recurring</strong> problem, and the crew file a <strong>grievance</strong> about Rex. One site meeting '
     'turns into a <strong>farce</strong>, with three people shouting at once. Edith’s position is becoming '
     '<strong>untenable</strong>. At last she <strong>intervenes</strong>: Rex goes, or the studio does.',
     [('go south', 'get worse, lose value or fail'),
      ('recurring', 'happening again and again'),
      ('grievance', 'a complaint about unfair treatment'),
      ('farce', 'a ridiculous, badly organized event'),
      ('untenable', 'impossible to defend or continue'),
      ('intervene', 'step in to change what is happening')],
     'A FARCE is first a kind of comic play, full of absurd situations. You FILE or AIR a grievance.',
     [q('The next meeting was ____: the plans were upside down and the projector caught fire.',
        ['farcical', 'meticulous', 'concise', 'esteemed'],
        'FARCICAL: absurd, like a farce.'),
      q('For Rex, serving coffee at the opening party was quite a ____ after “directing” the project.',
        ['comedown', 'pinnacle', 'kudos', 'tenure'],
        'A COMEDOWN is a loss of status or importance.'),
      q('Damp is ____ to oak panelling: slowly, it destroys the wood.',
        ['detrimental', 'superfluous', 'obsequious', 'intelligible'],
        'DETRIMENTAL TO something: harmful to it.'),
      q('A year ago it was ____ that anyone would live here. Now Bianca has moved in.',
        ['inconceivable', 'incomprehensible', 'intelligible', 'indoctrinated'],
        'INCONCEIVABLE: impossible to imagine or believe. INCOMPREHENSIBLE is impossible to understand.')],
     [('In the end Bianca had to ______ that Edith was right about the ceiling.', ['concede'],
       'CONCEDE: admit that something is true after first denying it.'),
      ('We ______ one detail: nobody had ordered any door handles.', ['overlooked'],
       'OVERLOOK: fail to notice something. A room can also OVERLOOK the garden: have a view of it.'),
      ('______ the roof was finished before the storm!', ['thank God|thank god|thank goodness'],
       'THANK GOD: said when you are relieved. THANK GOODNESS is the milder form.')],
     ['thank God', 'concede', 'overlooked'],
     ['a large crack running across a gold ceiling, plaster dust falling onto a table',
      'a meeting table in chaos with a smoking projector and plans upside down',
      'a man in a flashy scarf glumly carrying a tray of coffee cups at a party',
      'dark damp stains spreading across old oak wall panelling',
      'a glamorous woman relaxed in an armchair by a fire in a beautifully restored room']),
]

PARTS = {
    1: dict(
        chapters=P1,
        out='the-gargoyle-house-part-1.html',
        title='The Gargoyle House, Part 1: The Brief (C1)',
        warm=['Which building in your town would you love to restore?',
              'Old house or new flat: where would you rather live?',
              'What is the strangest thing you have seen in someone’s home?',
              'Have you ever worked for a difficult client?',
              'What was your first week in your first job like?',
              'What makes a presentation easy to follow?'],
        talk2=['Describe a building you know that is <strong>run-down</strong> or <strong>dilapidated</strong>.',
               'Is anything in your home an <strong>heirloom</strong>?',
               'When did you last have to <strong>put your foot down</strong>?',
               'What was your <strong>baptism of fire</strong> at work?',
               'Which detail in a room is usually <strong>superfluous</strong>?',
               'Is it ever right to tell a client a <strong>white lie</strong>?'],
        chips=['run-down', 'heirloom', 'capricious', 'put your foot down', 'meticulous', 'map out', 'revamp', 'rationale'],
        briefs=dict(hero='a grand old English country house with stone gargoyles on the roof, one big gargoyle in the foreground',
                    talk='a street of old townhouses, one of them covered in ivy with a For Sale sign',
                    talk2='two designers talking over fabric samples and a house model at a big table',
                    results='a stone gargoyle with a bright butterfly resting on its nose'),
    ),
    2: dict(
        chapters=P2,
        out='the-gargoyle-house-part-2.html',
        title='The Gargoyle House, Part 2: The Build (C1)',
        warm=['Have you ever lived through building work at home?',
              'Which languages do you hear in your workplace?',
              'How much coffee is too much?',
              'What do you do when a colleague flatters the boss?',
              'Tell us about a project that went wrong.',
              'Who usually steps in when your team argues?'],
        talk2=['Which design trend is <strong>divisive</strong> in your field?',
               'Describe a meeting that turned into a <strong>farce</strong>.',
               'What should always be paid <strong>upfront</strong>?',
               'When is it hard to <strong>concede</strong> that a client is right?',
               'What is a <strong>recurring</strong> problem in your projects?',
               'Who deserves <strong>kudos</strong> on your team, and why?'],
        chips=['in full swing', 'upfront', 'remit', 'outstanding', 'go south', 'grievance', 'intervene', 'concede'],
        briefs=dict(hero='an old English country house wrapped in scaffolding, a stone gargoyle wearing a yellow hard hat in the foreground',
                    talk='a kitchen full of dust sheets, a ladder and paint pots, a kettle on a crate',
                    talk2='builders and designers sharing coffee on a scaffold at sunset',
                    results='a restored country house glowing at dusk, a stone gargoyle smiling on the roof'),
    ),
}

# ── chrome ─────────────────────────────────────────────────────────────
T = {
    1: {
        'en': dict(
            coverTitle='The Gargoyle House <br><em>The Brief</em>',
            coverSub='A small design studio, a crumbling country house and a client with outrageous ideas. Part one of two.',
            chipLevel='C1', chipFocus='50 words · design · clients',
            e1='1 · The house', e2='2 · The client', e3='3 · The studio', e4='4 · The pitch',
            s1T='Ashby Hall', s2T='Bianca Voss', s3T='Marlowe &amp; Finch', s4T='Friday, ten o’clock',
            actTitle='Your own pitch', actUse='Use at least five:',
            actSpeakBrief='In pairs: one of you is the designer, the other the new owner of a run-down building.',
            actSpeak1='Owner: describe the building and your most outrageous idea for it.',
            actSpeak2='Designer: map out your concept, and give the rationale for each decision.',
            actSpeak3='Designer: put your foot down about one idea. Owner: don’t give way easily.',
            actWriteBrief='Write the opening of a pitch (150–200 words) to the owner of a dilapidated building: what you found on your first visit, your concept for the revamp, and the rationale. Keep it concise.',
            actPlaceholder='On our first visit to the hall, we found …',
        ),
        'de': dict(
            coverTitle='The Gargoyle House <br><em>The Brief</em>',
            coverSub='Ein kleines Designstudio, ein verfallendes Landhaus und eine Kundin mit unerhörten Ideen. Teil eins von zwei.',
            chipLevel='C1', chipFocus='50 Wörter · Design · Kunden',
            e1='1 · Das Haus', e2='2 · Die Kundin', e3='3 · Das Studio', e4='4 · Die Präsentation',
            s1T='Ashby Hall', s2T='Bianca Voss', s3T='Marlowe &amp; Finch', s4T='Freitag, zehn Uhr',
            actTitle='Deine eigene Präsentation', actUse='Verwende mindestens fünf:',
            actSpeakBrief='Zu zweit: Eine Person ist Designerin, die andere besitzt seit Kurzem ein heruntergekommenes Gebäude.',
            actSpeak1='Besitzerin: Beschreib das Gebäude und deine verrückteste Idee dafür.',
            actSpeak2='Designerin: Stell dein Konzept vor und begründe jede Entscheidung.',
            actSpeak3='Designerin: Sprich bei einer Idee ein Machtwort. Besitzerin: Gib nicht so leicht nach.',
            actWriteBrief='Schreib den Anfang einer Präsentation (150–200 Wörter) für die Besitzerin eines verfallenen Gebäudes: was ihr beim ersten Besuch vorgefunden habt, euer Konzept für die Erneuerung und die Begründung. Fass dich kurz.',
            actPlaceholder='On our first visit to the hall, we found …',
        ),
        'es': dict(
            coverTitle='The Gargoyle House <br><em>The Brief</em>',
            coverSub='Un pequeño estudio de diseño, una casa de campo en ruinas y una clienta con ideas escandalosas. Primera parte de dos.',
            chipLevel='C1', chipFocus='50 palabras · diseño · clientes',
            e1='1 · La casa', e2='2 · La clienta', e3='3 · El estudio', e4='4 · La presentación',
            s1T='Ashby Hall', s2T='Bianca Voss', s3T='Marlowe &amp; Finch', s4T='Viernes, a las diez',
            actTitle='Tu propia presentación', actUse='Usa al menos cinco:',
            actSpeakBrief='En parejas: uno es el diseñador y el otro acaba de comprar un edificio en mal estado.',
            actSpeak1='Propietario: describe el edificio y tu idea más escandalosa para él.',
            actSpeak2='Diseñador: expón tu concepto y da la razón de cada decisión.',
            actSpeak3='Diseñador: plántate ante una de las ideas. Propietario: no cedas fácilmente.',
            actWriteBrief='Escribe el comienzo de una presentación (150–200 palabras) para el dueño de un edificio en ruinas: qué encontrasteis en la primera visita, vuestro concepto para la reforma y sus razones. Sé conciso.',
            actPlaceholder='On our first visit to the hall, we found …',
        ),
    },
    2: {
        'en': dict(
            coverTitle='The Gargoyle House <br><em>The Build</em>',
            coverSub='The contract is signed and the cranes arrive. Then the client’s style consultant turns up. Part two of two.',
            chipLevel='C1', chipFocus='50 words · contracts · teams',
            e1='1 · The contract', e2='2 · In full swing', e3='3 · The consultant', e4='4 · August',
            s1T='Ninety pages', s2T='Forty people, three cranes', s3T='Enter Rex', s4T='Things go south',
            actTitle='The site meeting', actUse='Use at least five:',
            actSpeakBrief='In threes: the designer, the client and the client’s new consultant meet on site. The project is late.',
            actSpeak1='Designer: say what has gone south, and which invoices are outstanding.',
            actSpeak2='Consultant: talk up your own ideas. Client: decide whose side you are on.',
            actSpeak3='Designer: intervene. Explain what is outside your remit, and what you will not concede.',
            actWriteBrief='Write an email (150–200 words) from the designer to the client after a farcical site meeting: what went wrong, the recurring problems, what must be paid upfront, and what you need her to concede.',
            actPlaceholder='Dear Bianca, after this morning’s meeting I feel I must …',
        ),
        'de': dict(
            coverTitle='The Gargoyle House <br><em>The Build</em>',
            coverSub='Der Vertrag ist unterschrieben, die Kräne rollen an. Dann taucht der Stilberater der Kundin auf. Teil zwei von zwei.',
            chipLevel='C1', chipFocus='50 Wörter · Verträge · Teams',
            e1='1 · Der Vertrag', e2='2 · In vollem Gange', e3='3 · Der Berater', e4='4 · August',
            s1T='Neunzig Seiten', s2T='Vierzig Leute, drei Kräne', s3T='Auftritt Rex', s4T='Es geht bergab',
            actTitle='Die Baubesprechung', actUse='Verwende mindestens fünf:',
            actSpeakBrief='Zu dritt: Designerin, Kundin und der neue Berater der Kundin treffen sich auf der Baustelle. Das Projekt ist in Verzug.',
            actSpeak1='Designerin: Sag, was schiefgelaufen ist und welche Rechnungen noch offen sind.',
            actSpeak2='Berater: Preise deine eigenen Ideen an. Kundin: Entscheide, auf wessen Seite du stehst.',
            actSpeak3='Designerin: Greif ein. Erklär, wofür du nicht zuständig bist und wo du nicht nachgibst.',
            actWriteBrief='Schreib eine E-Mail (150–200 Wörter) der Designerin an die Kundin nach einer grotesken Baubesprechung: was schiefging, welche Probleme immer wiederkehren, was im Voraus zu zahlen ist und wo sie nachgeben muss.',
            actPlaceholder='Dear Bianca, after this morning’s meeting I feel I must …',
        ),
        'es': dict(
            coverTitle='The Gargoyle House <br><em>The Build</em>',
            coverSub='Contrato firmado, llegan las grúas. Y entonces aparece el asesor de estilo de la clienta. Segunda parte de dos.',
            chipLevel='C1', chipFocus='50 palabras · contratos · equipos',
            e1='1 · El contrato', e2='2 · A pleno ritmo', e3='3 · El asesor', e4='4 · Agosto',
            s1T='Noventa páginas', s2T='Cuarenta personas, tres grúas', s3T='Entra Rex', s4T='Todo se tuerce',
            actTitle='La reunión de obra', actUse='Usa al menos cinco:',
            actSpeakBrief='En grupos de tres: la diseñadora, la clienta y su nuevo asesor se reúnen en la obra. El proyecto va con retraso.',
            actSpeak1='Diseñadora: di qué ha salido mal y qué facturas siguen pendientes.',
            actSpeak2='Asesor: ensalza tus propias ideas. Clienta: decide de qué lado estás.',
            actSpeak3='Diseñadora: intervén. Explica qué queda fuera de tus competencias y en qué no vas a ceder.',
            actWriteBrief='Escribe un correo (150–200 palabras) de la diseñadora a la clienta tras una reunión de obra absurda: qué salió mal, los problemas que se repiten, qué hay que pagar por adelantado y en qué necesitas que ceda.',
            actPlaceholder='Dear Bianca, after this morning’s meeting I feel I must …',
        ),
    },
}

SHARED = {
    'en': dict(eW='Warm-up', eT='Let’s talk', tk1T='Before we go in', tk2T='Over to you',
               stNote='Six words are in bold. What do they mean here? You will match them next.',
               mT='Match the six words', mH='Choose a word, then its meaning.',
               mcT='Choose the best word', gapT='Write the missing word', gHint='Use the word bank. Change the form if you need to.',
               actWriteKind='Writing', slides='slides'),
    'de': dict(eW='Zum Einstieg', eT='Sprechen wir', tk1T='Bevor wir hineingehen', tk2T='Jetzt du',
               stNote='Sechs Wörter sind fett gedruckt. Was bedeuten sie hier? Gleich ordnest du sie zu.',
               mT='Ordne die sechs Wörter zu', mH='Wähle ein Wort, dann seine Bedeutung.',
               mcT='Wähle das beste Wort', gapT='Ergänze das fehlende Wort', gHint='Nimm die Wortliste. Ändere die Form, wenn nötig.',
               actWriteKind='Schreiben', slides='Folien'),
    'es': dict(eW='Para empezar', eT='A conversar', tk1T='Antes de entrar', tk2T='Te toca',
               stNote='Hay seis palabras en negrita. ¿Qué significan aquí? Después las vas a relacionar.',
               mT='Relaciona las seis palabras', mH='Elige una palabra y luego su significado.',
               mcT='Elige la mejor palabra', gapT='Escribe la palabra que falta', gHint='Usa el banco de palabras.',
               actWriteKind='Escritura', slides='diapositivas'),
}


def build(n):
    P = PARTS[n]
    E = dict(T[n]['en'], **SHARED['en'])
    pre = 'p%d-' % n
    count = 5 + sum(3 + len(ch[5]) for ch in P['chapters'])
    Tn = {}
    for c in ('en', 'de', 'es'):
        d = dict(T[n][c], **SHARED[c])
        d['chipCount'] = '%d %s' % (count, d.pop('slides'))
        Tn[c] = d
    E = Tn['en']
    plates = {'hero': P['briefs']['hero'], pre + 'talk': P['briefs']['talk'],
              pre + 'talk2': P['briefs']['talk2'], pre + 'results': P['briefs']['results']}
    flow = [('talk', 'eW', 'tk1T', P['warm'], pre + 'talk', 3)]
    for i, (ek, tk, text, pairs, mwhy, mcs, gaps, bank, briefs) in enumerate(P['chapters'], 1):
        slots = ['%sc%d-%d' % (pre, i, k) for k in range(len(briefs))]
        plates.update(zip(slots, briefs))
        flow += [
            ('stage',),
            ('raw', story(ek, tk, text), slots[0]),
            ('raw', D.match(pairs, ek, E[ek], 'mT', E['mT'], 'mH', E['mH'], mwhy)),
            ('mc', ek, 'mcT', mcs, slots[1:], None),
            ('gap', ek, 'gapT', 'gHint', gaps, bank),
        ]
    flow += [('stage',), ('talk', 'eT', 'tk2T', P['talk2'], pre + 'talk2', 3)]
    SPEC = dict(out=P['out'], title=P['title'], folder=F, style='hs1', hero='p%d-hero' % n,
                cover_name='pop-cover-p%d' % n, plates=plates, flow=flow, chips=P['chips'],
                results=pre + 'results', title_px=58)
    plates['p%d-hero' % n] = plates.pop('hero')
    H.check_keys(Tn)
    H.build(SPEC, Tn)
    return plates


if __name__ == '__main__':
    for n in ([int(a) for a in sys.argv[1:]] or [1, 2]):
        build(n)
