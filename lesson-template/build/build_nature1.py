# -*- coding: utf-8 -*-
"""Nature Agency Part 1 (C1) — rebuilt as a deck.

What it replaced was not a lesson. It was a 50-item autograded assessment on a
scrolling page with no teaching content of any kind: every explanatory sentence
sat inside a post-answer `explanation:` string, so the only way to learn a rule
was to get the item testing it wrong.

Defects carried by the old file and fixed here:

  * All 17 Section 1 keys were `correct: 0`. A runtime shuffle hid it live, but
    a static deck would have inherited a 100% "always A" key.

    The keys are now deranged to, in slide order:

        2 0 3 1  1 3 0 2  3 1 2 0  3 1 2 0  3

    That sequence is deliberate, not incidental. It spreads the key across all
    four positions (4/4/4/5) and carries no run, no alternation and no repeat
    at the pair boundaries, where a learner meeting the same word twice is
    most likely to look for one. Do not "tidy" it back into an order that
    reads more nicely in the source — nicely-ordered is the defect.

  * The key was the longest option in 10 of 17 items (mean key 62.1 chars
    against 50.3 for distractors). **Four distractors were lengthened — Q1[0],
    Q2[3], Q4[0] and Q10[3] — and no key was shortened.** That direction is
    the whole point: shortening a key to satisfy the ratio throws away the
    precision that made it the right answer, and the guard passes either way.
    A later pass that evens up the option lengths by trimming will silently
    restore the tell, so if `assert_no_key_is_longest` ever fails here, add
    words to a distractor.
  * Section 3 could not be lost: one point per correct match, no penalty and no
    cap on wrong ones, and an exit gate requiring all 16. Every learner scored
    16/16 and a third of the total was free. It is now two `sort` slides, where
    a wrong first placement forfeits that item's point. NOTE: the `match`
    engine in the template has the same defect and it is NOT fixed here — the
    template comment asks for that to be changed deliberately rather than as a
    side effect of one lesson rebuild.
  * Four explanations cross-referenced a sibling item ("Compare this with the
    verb sense…") and broke under the question shuffle. In a deck the order is
    static, so each contrast pair is now adjacent and the second item of a pair
    is the one that refers back.
  * `s2q3` rejected `shoegaze` while its own explanation offered it; `s2q11`
    rejected unhyphenated `hunky dory`. Alternates now go in via `data-answer`
    pipes.
  * `s2q2`'s hint contradicted its stem ("A **small** ___" / "a **large**
    number of people").
  * Factual: the otter decline was blamed on water quality declining "in the
    1980s". The cause was organochlorine pesticides from the late 1950s; the
    1980s are when otters began to recover. Corrected in the stem.
  * `parking lot` in an otherwise entirely British file (badger cull, town
    council, marsh harrier, hides) — now `car park`.
  * The intro promised "formal and legal" vocabulary and delivered no legal
    item. The register slide now teaches the formal senses these words carry.

The teaching content is the real change. Section 1 is not 17 unrelated words:
it is five polysemy contrasts — `report`, `critic`, `decay`, `reconcile` and
`dwell` are each tested twice — plus seven single items. The handoff names four
of those pairs and counts them as "eight polysemy contrasts"; `dwelled` /
`dwell on` at Q9/Q10 is a fifth pair with exactly the same shape. Every item
asks the learner to pick the right *sense* of a word they already know. The
eight teaching slides name that skill, give the three tells for doing it, and
draw the two contrasts the old file put in adjacent items and never joined up:
`prevalent` / `rampant` and `reconcile X with Y` / `reconcile with Y`.

`report` = the sound of a gunshot appeared only as an unexplained distractor,
in a lesson whose subject matter is poaching and culls. It is taught now.
`domineering` was used twice in Q12 — once as a distractor, once in the
feedback string — but not defined until Section 3. It is taught before use.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-nature-agency-part1.html'
F = 'NatureAgency'

# Derived: python3 lesson-template/extract-palette.py NatureAgency/hero.jpg
# Every body-text row in the contrast report passes.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0d0e09;
  --surface       : #1b1c12;
  --surface2      : #27291a;
  --border        : #9a6a48;
  --text          : #f5f3f2;
  --text-dim      : #bfafa3;
  --accent        : #e09968;
  --accent-bright : #efc0a0;
  --accent-dim    : #be692e;
  --secondary     : #96b9c9;
  --contrast      : #1dedde;''' % F

# ── Section 1 · sense discrimination ──────────────────────────────────
# Key positions, in slide order: 2 0 3 1 1 3 0 2 3 1 2 0 3 1 2 0 3
MC = [
    # report — the pair, adjacent, noun sense first
    dict(stem='<strong>A report is circulating among the field staff</strong> that the '
              'reserve&rsquo;s funding will be halved, though nothing has come from Head Office.',
         options=['A formal written record submitted to Head Office at the end of a survey period',
                  'A loud sharp sound made by an explosion, a firearm or a breaking branch',
                  'A piece of information that is unsupported by firm evidence and may not be true',
                  'An official complaint made to a supervisor about a colleague&rsquo;s conduct'],
         correct=2,
         why='Here <strong>a report</strong> is an unverified rumour &mdash; note <em>circulating</em>, '
             'and <em>nothing has come from Head Office</em>. The collocation is the tell.'),
    dict(stem='Elena is required to <strong>report</strong> any sighting of the protected marsh '
              'harrier to Director Bergmann within twenty-four hours.',
         options=['Give a spoken or written account of something observed, heard or investigated',
                  'Formally accuse someone of wrongdoing before an authority or a tribunal',
                  'Circulate an unverified account of something among colleagues at work',
                  'Submit an itemised expense claim for reimbursement at the end of a field survey'],
         correct=0,
         why='The verb sense. Two slides, one word, two grammars: <em>a report circulates</em> '
             '(noun, rumour), <em>you report a sighting</em> (verb, account). '
             'A third sense &mdash; the <em>report</em> of a rifle &mdash; comes later.'),
    # critic — the pair
    dict(stem='One vocal <strong>critic</strong> on the town council called the wetland restoration '
              'a waste of taxpayer money before it had even begun.',
         options=['A person who judges literary, artistic or musical works professionally',
                  'A person who examines the accuracy of financial records and accounts',
                  'A person who gives evidence in a legal case brought against an agency',
                  'A person who expresses an unfavourable opinion of something'],
         correct=3,
         why='The everyday sense: someone who objects. <em>Vocal</em> and <em>called it a waste</em> '
             'set the register &mdash; this is opposition, not expertise.'),
    dict(stem='Before joining the agency, Tomas worked as a <strong>critic</strong> for a '
              'nature-writing magazine, reviewing books on rewilding and conservation.',
         options=['A person who publicly expresses an unfavourable opinion of something or someone in a formal setting',
                  'A person who judges the merits of literary, artistic or musical works, especially professionally',
                  'A person who edits and fact-checks manuscripts before they go to press',
                  'A person who reports breaking news for a newspaper or broadcaster'],
         correct=1,
         why='The professional sense. <em>Worked as a critic for a magazine, reviewing books</em> '
             '&mdash; the job title and the object of the verb both point at it. '
             'A critic in this sense is not necessarily unfavourable.'),
    # decay — the pair, verb then noun
    dict(stem='Fallen branches left on the forest floor <strong>decay</strong> slowly, returning '
              'nutrients to the soil over several years.',
         options=['The state or process of rotting, considered as a condition of the material',
                  'Rot or decompose through the action of bacteria and fungi',
                  'Grow rapidly and spread across a wide area of ground',
                  'Lose colour gradually after long exposure to direct sunlight'],
         correct=1,
         why='A verb here &mdash; <em>branches decay</em>. The grammar is the whole tell: '
             'it has a subject and no article in front of it.'),
    dict(stem='Inspectors noted visible <strong>decay</strong> in the old hide&rsquo;s wooden '
              'supports and recommended it be rebuilt before winter.',
         options=['Rot or decompose through the action of bacteria and fungi over time',
                  'A sudden structural collapse brought on by flooding or by frost damage',
                  'The natural weathering of stone caused by wind and driving rain',
                  'The state or process of rotting or decomposition'],
         correct=3,
         why='The noun. Same word, one slide apart: <em>branches decay</em> is the process happening, '
             '<em>visible decay</em> is the condition you can see. <em>Visible</em> only modifies a noun.'),
    # reconcile — the pair, the preposition tell
    dict(stem='The final report tries to <strong>reconcile</strong> the ecologists&rsquo; survey data '
              '<strong>with</strong> the much lower figures submitted by the landowner.',
         options=['Find a way in which two opposing accounts can both be made to fit',
                  'Restore friendly relations between two people after a period of tension',
                  'Check a long technical document for spelling and grammatical errors',
                  'Translate a specialist report into plain language for the general public'],
         correct=0,
         why='<strong>Reconcile X with Y</strong> &mdash; two objects, two sets of figures. '
             'You are making things fit, not making peace.'),
    dict(stem='After weeks of tension over the badger cull, Bergmann finally '
              '<strong>reconciled with</strong> the local farmers&rsquo; union at a community meeting.',
         options=['Find a way in which two opposing accounts can both be made to fit together',
                  'Formally apologise in writing for a mistake made in an official capacity',
                  'Restore friendly relations after a disagreement',
                  'Reach a negotiated compromise over a disputed sum of money'],
         correct=2,
         why='<strong>Reconcile with Y</strong> &mdash; no direct object. One slide back it was '
             '<em>reconcile the data with the figures</em>. The syntax picks the sense for you, '
             'and it generalises: count the objects before you choose.'),
    # dwell — the pair the audit missed
    dict(stem='Otters once <strong>dwelled</strong> along this stretch of river, before pesticide '
              'run-off emptied it from the late 1950s onwards.',
         options=['Migrated seasonally between two separate habitats along the same river',
                  'Built temporary shelters at the water&rsquo;s edge during the breeding season',
                  'Thought or spoke at length about something, usually something unhappy',
                  'Lived in or at a specified place'],
         correct=3,
         why='The literal sense: to dwell somewhere is to live there. Formal, and slightly '
             'archaic &mdash; which is why it survives mostly in <em>dwelling</em>.'),
    dict(stem='Bergmann told Elena not to <strong>dwell on</strong> the failed grant application '
              'and to focus instead on next month&rsquo;s survey.',
         options=['Live in or at a specified place for an extended period of time',
                  'Think, speak or write at length about something, especially something unhappy',
                  'Double-check a piece of work several times over before submitting it',
                  'Postpone an unwelcome task until a more favourable opportunity happens to arise'],
         correct=1,
         why='Add <strong>on</strong> and the word stops being about place and starts being about '
             'attention. Same tell as <em>reconcile</em> one pair ago: the preposition decides.'),
    # singles
    dict(stem='From the <strong>outset</strong>, the reserve&rsquo;s managers made clear that public '
              'access would be limited during the breeding season.',
         options=['The final stage of a long-running and expensive restoration project',
                  'A formal announcement made to the press about a change in policy',
                  'The start or beginning of something',
                  'An unexpected complication that delays progress on an agreed plan'],
         correct=2,
         why='<em>From the outset</em> is a fixed phrase meaning from the very beginning. '
             'It belongs to the formal register a field officer writes in.'),
    dict(stem='Despite decades of research into peatland restoration, Dr Reyes remained remarkably '
              '<strong>humble</strong> about her own contribution to the field.',
         options=['Having or showing a modest estimate of one&rsquo;s own importance',
                  'Asserting one&rsquo;s will over other people in an arrogant, controlling way',
                  'Reluctant to share credit for a discovery with more junior colleagues',
                  'Uncertain or hesitant when speaking in front of a large public audience'],
         correct=0,
         why='<strong>Humble</strong> is not the same as timid. Its near-opposite is '
             '<strong>domineering</strong> &mdash; taught two slides back, and worth holding on to: '
             'it comes round again later in the lesson.'),
    dict(stem='Priya had a <strong>hunch</strong> that the missing otter tracks led towards the old '
              'mill, and she turned out to be right.',
         options=['A documented conclusion supported by evidence gathered in the field',
                  'A formal hypothesis to be tested through a properly controlled experiment',
                  'A piece of practical advice offered informally by a senior colleague',
                  'A feeling or guess based on intuition rather than on known facts'],
         correct=3,
         why='A <strong>hunch</strong> is explicitly not evidence. The sentence tells you she was '
             'right, which is the point: a hunch can be correct and still be a hunch.'),
    dict(stem='The interns were <strong>curious</strong> about why the agency had chosen this '
              'particular floodplain for reintroducing beavers.',
         options=['Suspicious that something relevant was being deliberately kept from them',
                  'Eager to know or learn something',
                  'Unconvinced by the official explanation they had been given at the briefing',
                  'Reluctant to ask questions during a briefing in front of senior staff'],
         correct=1,
         why='The plain sense. <strong>Curious</strong> has a second one &mdash; <em>a curious '
             'decision</em> means an odd one &mdash; but <em>curious about</em> fixes it as interest.'),
    dict(stem='The new wildlife corridor gives roe deer <strong>uninterrupted</strong> access '
              'between the two forest blocks for the first time in decades.',
         options=['Closely monitored by rangers on foot at all hours of the day and night',
                  'Legally protected under the terms of national conservation legislation',
                  'Without a break in continuity',
                  'Open to the animals only during certain clearly specified months'],
         correct=2,
         why='Literally <em>not interrupted</em> &mdash; unbroken in space here, though the same '
             'word covers time. The prefix does the work; nothing else in the sentence needs to.'),
    # the anchor pair, adjacent, contrast finally drawn
    dict(stem='Illegal snaring is far more <strong>prevalent</strong> in this region than the '
              'agency&rsquo;s official figures suggest.',
         options=['Widespread in a particular area or at a particular time',
                  'Completely eliminated after many years of sustained enforcement work',
                  'Difficult to detect reliably using the survey methods currently available',
                  'Limited to a single, well-documented location within the reserve boundary'],
         correct=0,
         why='<strong>Prevalent</strong> reports how common something is and passes no judgement. '
             'The disapproval in this sentence comes from <em>illegal</em>, not from the word itself.'),
    dict(stem='Invasive Japanese knotweed had grown <strong>rampant</strong> along the riverbank, '
              'choking out the native reeds and sedges.',
         options=['Slow to establish itself successfully in an unfamiliar new environment',
                  'Confined to a small and easily managed patch beside the water&rsquo;s edge',
                  'Dependent on one specific soil type in order to survive and spread',
                  'Flourishing or spreading unchecked, especially something unwelcome'],
         correct=3,
         why='<strong>Rampant</strong> carries both <em>widespread</em> and <em>bad, and nobody is '
             'stopping it</em>. That is the whole difference from <em>prevalent</em> one slide back: '
             'a species is prevalent, an invasive species is rampant. Never a compliment.'),
]

# ── Section 2 · the exact word ────────────────────────────────────────
# Grouped four/four/three/three/three. Each slide's bank is alphabetised, and
# the gaps within a slide are ordered so the bank is not an answer key.
ITEMS = {
    'shoegazing': ('On the drive back from the coast, Tomas played an old ______ album, all reverb '
                   'and blurred guitars, and nobody said a word for an hour.',
                   'shoegazing|shoegaze',
                   'The genre is <strong>shoegazing</strong>, often shortened to '
                   '<strong>shoegaze</strong>. Both are accepted.'),
    'sewn': ('Elena&rsquo;s field jacket, freshly ______ after a tear from barbed wire, kept her '
             'warm through the dawn survey.',
             'sewn',
             '<strong>Sewn</strong> is the past participle of <em>sew</em>. '
             '<em>Sown</em> is seed, not thread &mdash; a different verb entirely.'),
    'crowd': ('A small ______ gathered at the visitor centre to watch the release of the '
              'rehabilitated red kites.',
              'crowd',
              'A <strong>crowd</strong> is any gathered group. It takes <em>small</em> perfectly '
              'well &mdash; the word carries no size of its own.'),
    'programmer': ('The agency hired a ______ to rebuild the database that tracks '
                   'protected-species sightings across the region.',
                   'programmer|developer',
                   'A <strong>programmer</strong> writes the code. <em>Developer</em> is accepted; '
                   '<em>programme</em> would be the thing, not the person.'),
    'ministry': ('Funding for the reserve ultimately comes from the ______ responsible for '
                 'environment and agriculture.',
                 'ministry|department',
                 'A <strong>ministry</strong> is a government department headed by a minister. '
                 'Formal register &mdash; this is how a funding line is described in writing.'),
    'discount': ('Local schools receive a ______ on entry fees when they book a guided tour of '
                 'the wetlands.',
                 'discount|reduction',
                 'A <strong>discount</strong> is money off a stated price. You <em>receive</em> or '
                 '<em>get</em> one; you do not <em>make</em> one.'),
    'contribution': ('Dr Reyes&rsquo;s ______ to the peatland restoration project was recognised '
                     'with a national conservation award.',
                     'contribution',
                     'A <strong>contribution</strong> is what you add to a shared effort. '
                     'Note the preposition: a contribution <em>to</em>, never <em>for</em>.'),
    'assessor': ('An independent ______ visits the site every spring to check that the grazing '
                 'plan is being followed correctly.',
                 'assessor|inspector',
                 'An <strong>assessor</strong> judges whether a standard has been met. '
                 'Formal, and near-legal &mdash; the register this lesson promised.'),
    'headlight': ('A deer froze in the beam of the truck&rsquo;s ______ before darting back into '
                  'the trees.',
                  'headlight|headlights',
                  'Singular or plural both work here. <strong>Headlight</strong> is one word, '
                  'like <em>headland</em> and <em>headwater</em>.'),
    'glitterati': ('The gala to launch the new nature documentary drew more ______ than genuine '
                   'conservationists, according to Tomas.',
                   'glitterati',
                   '<strong>Glitterati</strong> &mdash; fashionable celebrities, always plural, '
                   'always faintly disparaging. Built from <em>glitter</em> on the pattern of '
                   '<em>literati</em>.'),
    'hunky-dory': ('Everything seemed ______ on the survey until the boat&rsquo;s engine cut out '
                   'halfway across the lake.',
                   'hunky-dory|hunky dory',
                   '<strong>Hunky-dory</strong> means fine, with no problems. Usually hyphenated; '
                   'unhyphenated is accepted.'),
    'occupy': ('A pair of peregrine falcons has come to ______ the old quarry cliff face every '
               'spring since 2019.',
               'occupy',
               'To <strong>occupy</strong> a site is to be present in it and hold it. Transitive '
               '&mdash; it takes the place as a direct object, with no preposition.'),
    'chatter': ('The ______ in the staff room died down the moment Director Bergmann walked in '
                'with the budget figures.',
                'chatter',
                '<strong>Chatter</strong> is light, continuous talk, and it is uncountable '
                '&mdash; <em>the chatter</em>, never <em>a chatter</em>.'),
    'interpretation': ('The visitor centre&rsquo;s new ______ panels explain how the reedbeds '
                       'filter pollutants from the river.',
                       'interpretation',
                       '<strong>Interpretation</strong> is the museum and heritage term for '
                       'explaining a site to visitors. A technical sense of a word you already '
                       'know &mdash; exactly the skill this lesson opened with.'),
    'swagger': ('The new field officer walked in with a ______ that made the older rangers doubt '
                'he would last a week outdoors.',
                'swagger',
                'A <strong>swagger</strong> is a walk that advertises confidence. Almost always '
                'unearned when someone else describes it.'),
    'company': ('The agency contracted a private ______ to remove the invasive rhododendron from '
                'the eastern slope.',
                'company|contractor|firm',
                '<strong>Company</strong>, <strong>firm</strong> and <strong>contractor</strong> '
                'all fit. Note the other sense hiding here: <em>in the company of</em> is people, '
                'not a business.'),
    'ersatz': ('The canteen&rsquo;s coffee was a kind of ______ brew made from roasted chicory, '
               'since the real thing had not been delivered.',
               'ersatz',
               '<strong>Ersatz</strong> &mdash; an inferior substitute for the real thing. '
               'Borrowed from German, and it keeps a faint sneer in English that it does not '
               'have there.'),
}

# Three gaps a slide: four overflowed the 720px canvas. Within each slide the
# gaps are ordered so that the alphabetised bank is not an answer key.
GROUPS = [
    ['shoegazing', 'sewn', 'crowd'],
    ['programmer', 'ministry', 'discount'],
    ['contribution', 'assessor', 'headlight'],
    ['occupy', 'glitterati', 'hunky-dory'],
    ['swagger', 'chatter', 'interpretation'],
    ['ersatz', 'company'],
]
GAPS = [[(ITEMS[k][0], [ITEMS[k][1]], ITEMS[k][2]) for k in g] for g in GROUPS]
BANKS = [sorted(g) for g in GROUPS]

# ── Section 3 · register sort ─────────────────────────────────────────
# Was 16 free points on an unloseable matching grid. Sorting is scored
# properly, and binning by register exercises the third tell from slide 3.
BINS = ['Everyday', 'Formal or technical', 'Figurative or idiomatic']
SORT1 = [
    ('quick on the draw', 2), ('shoot from the hip', 2),
    ('insufficient', 1), ('skirting', 1), ('accompany', 1),
    ('detour', 0), ('chapter', 0), ('decent', 0),
]
SORT2 = [
    ('fall apart', 2), ('showdown', 2),
    ('receipt', 1), ('civil war', 1), ('encyclopedia', 1),
    ('domineering', 0), ('car park', 0), ('laundry', 0),
]

CHIPS = ['report', 'critic', 'decay', 'reconcile with', 'dwell on',
         'prevalent', 'rampant', 'in receipt of']


def build():
    D.assert_no_key_is_longest(MC, 'NatureAgency1')
    for n, (rows, bank) in enumerate(zip(GAPS, BANKS), 1):
        D.assert_bank_is_not_a_key(bank, [a.split('|')[0] for _, aa, _ in rows for a in aa])
    logo = D.logo_from(TPL)

    teach = (
        # 1 · name the skill
        D.teach('t1e', 'Before the first question',
                't1t', 'This section is not testing whether you know these words',
                [('t1ah', 'You already know them',
                  'Every word in the next seventeen items is one a C1 speaker has met before.',
                  't1an', 'Not one of them is rare. That is deliberate, and it is the point of the exercise.'),
                 ('t1bh', 'It tests which <em>sense</em>',
                  'Each item asks you to pick the right sense of a familiar word.',
                  't1bn', 'Usually the second sense &mdash; the formal, technical or idiomatic one, '
                          'not the one you learned first.'),
                 ('t1ch', 'Five words appear twice',
                  '<em>report</em>, <em>critic</em>, <em>decay</em>, <em>reconcile</em>, <em>dwell</em>.',
                  't1cn', 'Each is tested once in each sense, on consecutive slides. '
                          'When you meet a word for the second time, ask what changed.')],
                cols='1fr 1fr 1fr', folder=F),
        # 2 · the method
        D.teach('t2e', 'The transferable part',
                't2t', 'Three tells for picking the right sense',
                [('t2ah', '1 &middot; The collocation',
                  'What sits next to the word.',
                  't2an', '<em>A report circulates</em> is a rumour. '
                          '<em>To report a sighting</em> is an account. Same word, different company.'),
                 ('t2bh', '2 &middot; The grammar',
                  'Noun or verb; transitive or not; which preposition follows.',
                  't2bn', '<em>Reconcile X with Y</em> makes two things fit. '
                          '<em>Reconcile with Y</em> repairs a relationship. Count the objects.'),
                 ('t2ch', '3 &middot; The register',
                  'How formal the sentence around it is.',
                  't2cn', 'A formal sentence pulls a formal sense. '
                          '<em>In receipt of your letter</em> is not the slip from a till.')],
                cols='1fr 1fr 1fr', folder=F, bg='station.jpg'),
        # 3 · report, all three senses including the gunshot
        D.teach('t3e', 'Contrast one',
                't3t', '<em>report</em> &mdash; three senses, and one of them is a sound',
                [('t3ah', 'a report <span class="dim">(noun)</span>',
                  'An unverified account going round. <em>A report is circulating that&hellip;</em>',
                  't3an', 'Also the formal written kind &mdash; <em>the annual report</em>. '
                          'The article and the verb around it tell you which.'),
                 ('t3bh', 'to report <span class="dim">(verb)</span>',
                  'To give an account of what you saw. <em>Report any sighting within 24 hours.</em>',
                  't3bn', 'Takes a direct object. Also <em>report to</em> someone &mdash; '
                          'the person you answer to.'),
                 ('t3ch', 'the report <span class="dim">(of a rifle)</span>',
                  'The sharp crack of a firearm. <em>Two reports from the far ridge.</em>',
                  't3cn', 'Rare in general English and routine in this one. On a reserve dealing '
                          'with poaching and culls, it is the sense you will need in writing.')],
                cols='1fr 1fr 1fr', folder=F),
        # 4 · critic and decay
        D.teach('t4e', 'Contrast two and three',
                't4t', '<em>critic</em> and <em>decay</em> &mdash; opinion, and word class',
                [('t4ah', 'critic &mdash; the objector',
                  'Someone who says a thing is bad. <em>A vocal critic on the council.</em>',
                  't4an', 'Unfavourable by definition. Comes with <em>vocal</em>, <em>fierce</em>, '
                          '<em>outspoken</em>.'),
                 ('t4bh', 'critic &mdash; the reviewer',
                  'Someone whose job is judging work. <em>A critic for a magazine.</em>',
                  't4bn', 'Carries no judgement at all. A critic in this sense can love everything '
                          'they review.'),
                 ('t4ch', 'decay &mdash; verb, then noun',
                  '<em>Branches decay</em> (the process). <em>Visible decay</em> (the condition).',
                  't4cn', 'The article is the tell. Adjectives such as <em>visible</em> or '
                          '<em>advanced</em> can only modify the noun.')],
                cols='1fr 1fr 1fr', folder=F, bg='lake.jpg'),
        # 5 · reconcile — the syntax tell
        D.teach('t5e', 'Contrast four',
                't5t', '<em>reconcile</em> &mdash; the preposition tells you the sense',
                [('t5ah', 'reconcile X <em>with</em> Y',
                  'Make two accounts fit. <em>Reconcile the survey data with the landowner&rsquo;s figures.</em>',
                  't5an', 'Two objects. Bookkeeping, evidence, competing versions of a number. '
                          'Nothing to do with feelings.'),
                 ('t5bh', 'reconcile <em>with</em> Y',
                  'Repair a relationship. <em>Bergmann reconciled with the farmers&rsquo; union.</em>',
                  't5bn', 'No direct object. People, or groups of them.'),
                 ('t5ch', 'Why it generalises',
                  'Count the objects before you choose the sense.',
                  't5cn', 'The same test settles <em>dwell</em> on the next slide, and dozens of '
                          'verbs beyond this lesson.')],
                cols='1fr 1fr 1fr', folder=F),
        # 6 · dwell — the pair the audit missed
        D.teach('t6e', 'Contrast five',
                't6t', '<em>dwell</em> &mdash; add a preposition, change the subject',
                [('t6ah', 'dwell <span class="dim">(somewhere)</span>',
                  'To live in a place. <em>Otters once dwelled along this river.</em>',
                  't6an', 'Formal and a little archaic. It survives mostly in <em>dwelling</em>, '
                          'which is the word a planning document uses for a house.'),
                 ('t6bh', 'dwell <em>on</em> <span class="dim">(something)</span>',
                  'To think or talk about it at length. <em>Don&rsquo;t dwell on the failed application.</em>',
                  't6bn', 'Almost always something unhappy. To dwell on a success is to boast; '
                          'the word expects a grievance.'),
                 ('t6ch', 'Same tell as <em>reconcile</em>',
                  'One preposition moves the word from place to attention.',
                  't6cn', 'Two pairs, one rule. This is the tell worth carrying out of the lesson.')],
                cols='1fr 1fr 1fr', folder=F, bg='lake.jpg'),
        # 7 · the anchor
        D.teach('t7e', 'The pair that matters most here',
                't7t', '<em>prevalent</em> or <em>rampant</em> &mdash; both mean widespread',
                [('t7ah', 'prevalent',
                  'Common in a place or a time. <em>Snaring is prevalent in this region.</em>',
                  't7an', 'Neutral. It reports a frequency and passes no judgement. '
                          'Any disapproval in the sentence comes from other words.'),
                 ('t7bh', 'rampant',
                  'Spreading unchecked, and unwelcome. <em>Knotweed had grown rampant.</em>',
                  't7bn', 'Carries two things at once: widespread, <em>and</em> bad, '
                          '<em>and</em> nobody is stopping it. Never a compliment.'),
                 ('t7ch', 'For a conservation agency',
                  'A native species is <strong>prevalent</strong>. An invasive species is <strong>rampant</strong>.',
                  't7cn', 'Choosing the wrong one in a site report either understates a problem '
                          'or editorialises about a healthy population.')],
                cols='1fr 1fr 1fr', folder=F, bg='prairie.jpg'),
        # 8 · register — makes good on the "formal and legal" promise
        D.teach('t8e', 'Register',
                't8t', 'The formal senses these same words carry',
                [('t8ah', 'in receipt of',
                  '<em>We are in receipt of your objection.</em>',
                  't8an', 'Formal acknowledgement that something arrived. Not the slip of paper &mdash; '
                          'the same word doing near-legal work.'),
                 ('t8bh', 'to launder',
                  '<em>Funds laundered through a shell company.</em>',
                  't8bn', 'From <em>laundry</em>. To wash money is to make illegal money look clean. '
                          'Also <em>airing dirty laundry</em> &mdash; private disputes made public.'),
                 ('t8ch', 'the decay of an institution',
                  '<em>The slow decay of enforcement in the region.</em>',
                  't8cn', 'The rot sense, applied to something abstract. '
                          'This is the register a field officer writes reports in.'),
                 ('t8dh', 'domineering',
                  '<em>A domineering site manager.</em>',
                  't8dn', 'Arrogant and controlling &mdash; the near-opposite of <em>humble</em>, '
                          'which you will meet shortly.')],
                cols='1fr 1fr 1fr 1fr', folder=F, bg='station.jpg'),
    )

    slides = (
        D.cover(logo, 'The <em>Nature Agency</em>',
                'Elena Voss&rsquo;s first weeks as a field officer &mdash; and the second sense '
                'of every word she already knew',
                [('Level', 'C1 &middot; Advanced'), ('Focus', 'Sense discrimination &amp; register'),
                 ('Count', '36 slides')])
        + "".join(teach)
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Which sense is it?',
                       'qTitle', 'Read the sentence, then choose', folder=F,
                       bg=('prairie.jpg' if i % 3 == 1 else 'lake.jpg' if i % 3 == 2 else None))
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, len(GAPS), rows, BANKS[n], 'gapEyebrow', 'The exact word',
                        'gapTitle', 'Complete the briefing', folder=F,
                        hint_key='gapHint',
                        hint='Every word in the bank is used exactly once on this slide.',
                        bg='station.jpg' if n % 2 else None,
                        width=200, size=17)
                  for n, rows in enumerate(GAPS))
        + D.sort_slide(BINS, SORT1, 'sortEyebrow', 'Register',
                       'sortTitle', 'Sort these by how formal they are',
                       'sortHint', 'Drag each term into a box &mdash; or click the term, then the box. '
                                   'A wrong first placement costs that term&rsquo;s point.',
                       'The third tell from the opening slides, used on its own. Register is what '
                       'tells you that <em>in receipt of</em> and <em>a receipt</em> are the same '
                       'word doing two different jobs.',
                       folder=F, bg='prairie.jpg')
        + D.sort_slide(BINS, SORT2, 'sortEyebrow', 'Register',
                       'sortTitle2', 'Sort these by how formal they are',
                       'sortHint', 'Drag each term into a box &mdash; or click the term, then the box. '
                                   'A wrong first placement costs that term&rsquo;s point.',
                       '<em>Showdown</em> and <em>quick on the draw</em> both come from westerns; '
                       '<em>civil war</em> is the technical term for a specific kind of conflict. '
                       'Where a phrase comes from is often the fastest guide to when you can use it.',
                       folder=F)
        + D.results('resNext', 'You can pick the sense. Now produce it →')
        + D.activate('Write the site report', 'Use at least four:', CHIPS,
                     'Speaking &middot; in pairs',
                     'One field officer, one landowner. The survey figures do not agree.',
                     ['Report a sighting formally, then report a rumour. Make the difference audible.',
                      'Say the snaring is <em>prevalent</em>. Then say the knotweed is <em>rampant</em>. '
                      'Explain to your partner why you did not swap the words.',
                      'Reconcile your figures with theirs &mdash; then reconcile with them.',
                      'Disagree without becoming domineering.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the summary paragraph of a site report: what you observed, what is '
                     'disputed, and what you recommend. Formal register throughout.',
                     'Site report — eastern slope, October')
    )

    import i18n_nature1 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'The Nature Agency — Sense &amp; Register (C1) | Forbes English', I)
    # The template ships --bg-opacity at 0.72, which assumes a hero that is
    # mid-tone or darker. This hero is a pale sky over pale prairie, and at 0.72
    # on a dark palette the sky comes through bright enough that the sort-bin
    # labels and the results text stop reading against it — house style rule 3.
    # Everything with its own card surface was fine either way; the two slides
    # that place text straight onto the wash were not.
    s = s.replace('  --bg-opacity: 0.72;', '  --bg-opacity: 0.40;', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    n = s.count('<section class="slide')
    print('wrote %s — %d <section class="slide" (checker header is authoritative), '
          '%d MC, %d gap slides, 2 sorts, %d bytes' % (OUT, n, len(MC), len(GAPS), len(s)))


if __name__ == '__main__':
    build()
