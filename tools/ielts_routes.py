# -*- coding: utf-8 -*-
"""The five IELTS routes: every lesson, in teaching order, with its copy.

THIS IS THE SOURCE OF TRUTH for the IELTS route pages and for the lesson
lists on the landing page. `tools/build_ielts_routes.py` writes the five
route pages (`ielts-writing.html` ...) from it, and `tools/build_ielts_hub.py`
reads it for `ielts.html`. Both run from `tools/build_hubs.py`.

    To add a lesson:  put it in the right track below, in teaching order,
                      then  py tools/build_hubs.py  and  py tools/seo.py.
    Do NOT edit the route pages by hand. The builder refuses to overwrite a
    page that was edited since it last wrote it, and says which one.

Strings are HTML, entities and all, exactly as they appear on the page.

What is NOT typed here, because it comes from somewhere that knows better:
- Free or Pro, and each lesson's level: the catalogue (`seo.lessons()`).
- The route's level span in the kicker ("C1", "B2–C1"): the same levels.
- Lesson counts, and "all but two end with writing you produce": counted
  from this list and from the decks themselves. In a lede or a teaching
  note, `{count}` and `{Count}` become the number of lessons in words,
  `{silent}` the sentence about which lessons end without production, and
  `{levels}` "The whole set is C1" or "Everything is C1 except ...".
- The route's order, number, name and colour family: `ROUTES` in
  `tools/build_ielts_hub.py`, which also holds the landing page's copy for
  each route. A new route needs an entry there, here, and in `PAGES` in
  `tools/seo.py` (its title and description).

Per route:
  hub        the page this route builds
  module     the first part of the kicker (the level span and route number
             are added to it)
  h1         (small line, big word)
  lede       paragraphs under the H1
  callout    the one thing to know before starting; its <strong> leads
  art        the route picture (the landing page uses the same one)
  hero_pos   its object-position in the route page's 4:3 frame, chosen so
             the subject the alt text names stays in view
  tracks     groups of lessons, each with a heading and a one-line note
  reference  free reference material listed after the lessons (not counted)
  teach      the note for teachers
Per lesson: file, title (the full deck title is fine: both the landing page
and the route page shorten "IELTS Academic Writing: The Report" to "The
Report"), desc, and
tags — descriptive only. "Free", "Pro", "New", "Start here" and levels are
added by the builder, never typed.
"""

ROUTES = [{'hub': 'ielts-writing.html',
  'module': 'Academic module',
  'h1': ('IELTS Academic', 'Writing'),
  'lede': ['{Count} lessons, in order. <strong>Start with the Report.</strong> Task 1 comes '
           'first here because it comes first on the paper — but <strong>Task 2 carries twice '
           'the marks</strong>, so that is where the hours should go. The numbering is '
           'teaching order, which is why the model answers (Part 4) sit before the timed '
           'practice (Part 3).',
           'Every lesson is click-through and scored where scoring teaches something. '
           '{silent}'],
  'callout': '<strong>This is the Academic module.</strong> Task 2 is the same on General '
             'Training, but GT Task 1 is a letter, not a report — so the Task 1 lessons below '
             'will not match a GT paper.',
  'art': 'ielts-model-answers/hero.jpg',
  'hero_pos': '75% 50%',
  'art_alt': 'Illustration of a wall of card-index drawers, one pulled open with a sheet of '
             'paper rising out of it',
  'tracks': [{'h': 'Task 1 — the report',
              'note': '20 minutes · 150 words · first on the paper, and the shorter of the two',
              'lessons': [{'file': 'forbes-english-ielts-academic-writing-part1.html',
                           'title': 'IELTS Academic Writing: The Report',
                           'desc': 'How a Task 1 report is built, paragraph by paragraph — '
                                   'with the rule that decides everything: report what you '
                                   'see, never what you think about it.',
                           'tags': ['Part 1']},
                          {'file': 'forbes-english-ielts-intro-overview-part7.html',
                           'title': 'The First Two Paragraphs',
                           'desc': 'The introduction and the overview — the two paragraphs '
                                   'that decide your Task Achievement band, and the one '
                                   'paragraph you cannot leave out. Works for Task 2 openings '
                                   'too.',
                           'tags': ['Part 7', 'Intro &amp; overview']},
                          {'file': 'forbes-english-ielts-bar-charts-c1.html',
                           'title': 'The Bar Chart',
                           'desc': 'Introduction, overview, two body paragraphs — built around '
                                   "a live animated chart of the lesson's own data, so you can "
                                   'see what each sentence is describing.',
                           'tags': ['Task 1']},
                          {'file': 'forbes-english-ielts-line-graph-part8.html',
                           'title': 'The Line Graph',
                           'desc': 'Direction, degree and tense, built around a live two-line '
                                   'chart — the two trend grammars, why <em>steadily</em> does '
                                   'not mean slowly, and how to describe a decade without '
                                   'describing every point on it.',
                           'tags': ['Part 8', 'Trends &amp; tense']},
                          {'file': 'forbes-english-ielts-maps-and-data-c1.html',
                           'title': 'Maps &amp; Accurate Data',
                           'desc': 'Two modules: the location language a map report runs on, '
                                   'and the vocabulary of approximation for the many values '
                                   'that are not exact numbers.',
                           'tags': ['Task 1']}]},
             {'h': 'Task 2 — the essay',
              'note': '40 minutes · 250 words · about two-thirds of the Writing score, so this '
                      'is where the hours go',
              'lessons': [{'file': 'forbes-english-ielts-academic-writing-part1b.html',
                           'title': 'IELTS Academic Writing: The Essay',
                           'desc': 'The shape of a Task 2 essay, the four question types and '
                                   'how to spot them, and the linking words bank to keep open '
                                   'while you write.',
                           'tags': ['Part 1b']},
                          {'file': 'forbes-english-ielts-writing-lab-part2.html',
                           'title': 'The IELTS Writing Lab',
                           'desc': 'The five essay types and how to tell them apart before you '
                                   'write a word — plus a scored linking-words test and a '
                                   'second chart to read.',
                           'tags': ['Part 2', 'Essay types']},
                          {'file': 'forbes-english-ielts-writing-lab-part2b.html',
                           'title': 'Linking Words &amp; Data Practice',
                           'desc': 'The connectors examiners reward — concession, emphasis, '
                                   'weighing up, summarising — drilled and scored, then put to '
                                   'work on a real line chart and a set of topic paragraphs to '
                                   'reorder.',
                           'tags': ['Part 2b', 'Linking words']},
                          {'file': 'forbes-english-ielts-model-answers-part4.html',
                           'title': 'The Model Answer Vault',
                           'desc': 'Two band 9 essays taken apart move by move — then the same '
                                   'two questions answered at band 6, so you can see exactly '
                                   'what the difference costs.',
                           'tags': ['Part 4', 'Band 9 vs band 6']},
                          {'file': 'forbes-english-ielts-outweigh-part5.html',
                           'title': 'Weighing It Up',
                           'desc': 'The two types that get written as though they were '
                                   'something else — "do the advantages outweigh?" and "what '
                                   'problems, what measures?" — each with a band 9 answer and '
                                   'the band 6 that forgot to answer.',
                           'tags': ['Part 5', 'Outweigh &amp; measures']},
                          {'file': 'forbes-english-ielts-two-questions-part6.html',
                           'title': 'Two Questions, One Essay',
                           'desc': 'The fifth and last type — two questions inside one prompt, '
                                   'both marked — and a side-by-side of all five types with '
                                   'the one habit that tells them apart.',
                           'tags': ['Part 6', 'All five types']},
                          {'file': 'forbes-english-ielts-writing-studio-part3.html',
                           'title': 'The Writing Studio',
                           'desc': 'Now write two of your own, timed, with planning fields and '
                                   'a live word counter. Nothing here is auto-scored — it '
                                   'downloads for a teacher to mark.',
                           'tags': ['Part 3', 'Timed practice']}]}],
  'reference': [{'h': 'Reference',
                 'note': 'free · no sign-in · keep it open while you write',
                 'lessons': [{'file': 'ielts-question-bank.html',
                              'title': 'Question Bank &amp; Ideas',
                              'desc': '{bank} &mdash; artificial intelligence, gentrification, '
                                      'energy and immigration included &mdash; filterable by '
                                      'topic and by essay type, and under each topic, '
                                      'arguments for both sides. For when you know the shape '
                                      'and have nothing to say.',
                              'tags': []}]}],
  'teach': {'h': 'Teaching this rather than sitting it?',
            'p': ['Parts 1 to 3 run as a course; Part 4 works on its own as a marking clinic, '
                  "and the Writing Studio exports a learner's planning notes and final essay "
                  'as a plain text file for correction. {levels} — bring a strong '
                  'B2 class and expect to slow down.']}},
 {'hub': 'ielts-speaking.html',
  'module': 'One test for both modules',
  'h1': ('IELTS', 'Speaking'),
  'lede': ['Eleven to fourteen minutes, three parts, one examiner. <strong>Academic and '
           'General Training sit the same test</strong> and it is marked the same way, so '
           'everything here applies whichever module you are taking.',
           'All four criteria are about language, not knowledge &mdash; Fluency &amp; '
           'Coherence, Lexical Resource, Grammar and Pronunciation, a quarter each. The topic '
           'is only an excuse to produce English.'],
  'callout': '<strong>Parts 1 and 2 first.</strong> Part 3 is the abstract discussion and it '
             'needs the other two working before it is worth attempting. Pronunciation runs '
             'alongside all three &mdash; it is a quarter of the mark in every part of the '
             'test.',
  'art': 'ielts-speaking/hero.jpg',
  'hero_pos': '35% 50%',
  'art_alt': 'Illustration of a bare room at dusk with two chairs facing each other across a '
             'small table',
  'tracks': [{'h': 'The route &mdash; three parts, and the quarter that runs through all of '
                   'them',
              'note': '4&ndash;5 minutes of questions &middot; a card, one minute to prepare '
                      'and two to talk &middot; then the discussion',
              'lessons': [{'file': 'forbes-english-ielts-speaking-part1-2.html',
                           'title': 'Answering at Length',
                           'desc': 'How long an answer should be, four ways to extend one '
                                   'without waffling, what an examiner hears as memorised, and '
                                   'how to fill two minutes when you have run out at forty '
                                   'seconds.',
                           'tags': ['Parts 1 &amp; 2']},
                          {'file': 'forbes-english-ielts-speaking-part3.html',
                           'title': 'Part 3 &mdash; the discussion',
                           'desc': 'Five or six questions on the same topic as your card, but '
                                   'abstract, and the examiner is allowed to push back. Moving '
                                   'from your own life to the general case is the skill, and '
                                   'it is the one Part 1 does not teach.',
                           'tags': ['Part 3']},
                          {'file': 'forbes-english-ielts-pronunciation.html',
                           'title': 'Pronunciation &amp; fluency',
                           'desc': 'A quarter of the marks sits on pronunciation and most '
                                   'candidates never practise it deliberately. Stress, '
                                   'chunking and the pauses that read as thinking rather than '
                                   'as stalling &mdash; and why an accent costs nothing at '
                                   'all.',
                           'tags': ['25% of the marks']}]}],
  'reference': [],
  'teach': {'h': 'Teaching this rather than sitting it?',
            'p': ['The first lesson ends in a paired examiner-and-candidate task with a clock, '
                  'so it runs in a room without preparation. One learner holds the timing and '
                  'cuts the other off at two minutes &mdash; being stopped mid-sentence is '
                  'part of the real test, and practising it removes most of the shock.']}},
 {'hub': 'ielts-listening.html',
  'module': 'One test for both modules',
  'h1': ('IELTS', 'Listening'),
  'lede': ['Thirty minutes, four sections, forty questions. <strong>Academic and General '
           'Training sit the identical Listening paper</strong>, so nothing here changes with '
           'your module.',
           'Every recording is played <strong>once</strong>. That single fact shapes the whole '
           'skill: reading the questions before the audio starts matters more than anything '
           'you do while it is running.'],
  'callout': '<strong>Start with the mechanics.</strong> The first lesson is question types, '
             'transfer rules and the traps that cost marks &mdash; no recording needed. The '
             'four section lessons that follow each play their recording once, as the test '
             'does.',
  'art': 'ielts-listening/hero.jpg',
  'hero_pos': '25% 50%',
  'art_alt': 'Illustration of a chalkboard with a listening exercise sketched on it',
  'tracks': [{'h': 'The mechanics &mdash; before you listen to anything',
              'note': 'Question types &middot; the answer sheet &middot; what loses marks that '
                      'has nothing to do with hearing',
              'lessons': [{'file': 'forbes-english-ielts-listening-part9.html',
                           'title': 'How the Listening Test Works',
                           'desc': 'The four sections and what changes between them, every '
                                   'question type you can meet, the word limit and why it is '
                                   'absolute, how numbers and times should be written, and the '
                                   'map task that is lost by losing your place rather than by '
                                   'missing a word.',
                           'tags': ['No audio needed']}]},
             {'h': 'The four sections &mdash; one lesson each',
              'note': 'One recording per lesson &middot; each plays its section once, as the '
                      'test does',
              'lessons': [{'file': 'forbes-english-ielts-listening-s1.html',
                           'title': 'Section 1 &mdash; the everyday conversation',
                           'desc': 'Two speakers arranging something practical, and a form to '
                                   'complete. The easiest section on the paper and the one '
                                   'where careless spelling and stray words throw away marks '
                                   'that were already won.',
                           'tags': ['Audio', 'Form completion']},
                          {'file': 'forbes-english-ielts-listening-s2.html',
                           'title': 'Section 2 &mdash; the monologue and the map',
                           'desc': 'One speaker describing a place to people who are standing '
                                   'in it. Placing things on a layout while a voice walks you '
                                   'round it, which is a skill of orientation rather than of '
                                   'vocabulary.',
                           'tags': ['Audio', 'Places and positions']},
                          {'file': 'forbes-english-ielts-listening-s3.html',
                           'title': 'Section 3 &mdash; the academic discussion',
                           'desc': 'Three voices &mdash; two students and a tutor &mdash; '
                                   'disagreeing, correcting each other and changing their '
                                   'minds. Tracking who says what is the whole difficulty, and '
                                   'it is where most candidates first drop.',
                           'tags': ['Audio', 'Three speakers']},
                          {'file': 'forbes-english-ielts-listening-s4.html',
                           'title': 'Section 4 &mdash; the lecture',
                           'desc': 'One voice, several minutes, no break in the middle and no '
                                   'second chance to re-read the questions. Note completion at '
                                   'speed, and how to recover the thread after you have lost '
                                   'it.',
                           'tags': ['Audio', 'Note completion']}]},
             {'h': 'Drills &mdash; numbers, spelling and accents',
              'note': 'Short drills with audio &middot; tested constantly, taught rarely',
              'lessons': [{'file': 'forbes-english-ielts-listening-drills.html',
                           'title': 'Numbers, spelling and accents',
                           'desc': 'Short drills on the things that are tested constantly and '
                                   'taught rarely: spelled-out names, <em>double</em> and '
                                   '<em>treble</em>, dates and times, and the range of accents '
                                   'the test deliberately uses.',
                           'tags': ['Audio', 'Drills']}]}],
  'reference': [],
  'teach': {'h': 'Teaching this rather than sitting it?',
            'p': ['The first lesson runs in a room with no equipment at all &mdash; it is '
                  'question types and transfer rules, and it ends in a paired task where one '
                  'learner reads a set of directions aloud while the other follows them on a '
                  'plan. That single exercise reproduces most of what makes Section 2 hard.']}},
 {'hub': 'ielts-reading.html',
  'module': 'Both modules',
  'h1': ('IELTS', 'Reading'),
  'lede': ['Sixty minutes, three sections, forty questions. <strong>Academic and General '
           'Training differ in the texts, not in the technique</strong> &mdash; Academic sets '
           'three long passages, General Training starts with shorter texts, and the question '
           'types are the same, as is everything on this route.',
           'There is no transfer time. On paper, Listening gives you ten minutes at the end to '
           'copy your answers across; Reading gives you none, and answers left on the question '
           'paper score nothing.'],
  'callout': '<strong>True, False, Not Given first.</strong> It is the type candidates find '
             'hardest to call, and the difficulty is technique rather than vocabulary: '
             'candidates answer from what they know instead of from what the passage says.',
  'art': 'ielts-reading/hero.jpg',
  'hero_pos': '75% 50%',
  'art_alt': 'Illustration of a long reading-room table under a single hanging lamp, with '
             'papers stacked at one end',
  'tracks': [{'h': 'The question types &mdash; the one that costs the most, first',
              'note': '3 sections &middot; 40 questions &middot; 60 minutes &middot; no time '
                      'at the end to transfer anything',
              'lessons': [{'file': 'forbes-english-ielts-reading-tfng.html',
                           'title': 'True, False, Not Given',
                           'desc': 'The whole lesson is one distinction: FALSE means a '
                                   'sentence in the passage contradicts the statement, NOT '
                                   'GIVEN means the passage is silent. Plus the qualifier that '
                                   'decides a third of them &mdash; most against all, may '
                                   'against is.',
                           'tags': ['Both modules']},
                          {'file': 'forbes-english-ielts-reading-ynng.html',
                           'title': 'Yes, No, Not Given',
                           'desc': 'True, False, Not Given&rsquo;s sibling: the same three-way '
                                   'choice, asked about what the writer thinks rather than '
                                   'what the passage says. The skill is finding the sentence '
                                   'in which the writer speaks &mdash; and reading the '
                                   'concession, the turn and the hedge.',
                           'tags': ['The writer&rsquo;s views']},
                          {'file': 'forbes-english-ielts-reading-headings.html',
                           'title': 'Matching Headings',
                           'desc': 'A type whose list of headings follows no order, so the '
                                   'technique is different: read for the main idea and what '
                                   'the paragraph is doing, not just what it is about, and '
                                   'leave the headings that fit two paragraphs until last.',
                           'tags': ['Out of order']},
                          {'file': 'forbes-english-ielts-reading-completion.html',
                           'title': 'Summary and sentence completion',
                           'desc': 'Where the word limit does the damage. Answers come '
                                   'straight from the passage, spelling counts, and &ldquo;no '
                                   'more than two words&rdquo; means a three-word answer '
                                   'scores nothing however right it is.',
                           'tags': ['Word limit']}]}],
  'reference': [],
  'teach': {'h': 'Teaching this rather than sitting it?',
            'p': ['The first lesson ends with a task that needs no preparation and no exam '
                  'material: one learner writes four statements about any passage in the room '
                  '&mdash; a news article will do &mdash; and the other answers, then has to '
                  'read out the line that decided each verdict. No line, no FALSE. It is the '
                  'whole skill, and it exposes the guessing immediately.']}},
 {'hub': 'ielts-vocabulary.html',
  'module': 'Speaking &amp; Writing',
  'h1': ('IELTS', 'Vocabulary'),
  'lede': ['Lexical Resource is <strong>a quarter of the marks in Speaking and a quarter in '
           'Writing</strong>. It is the same criterion in both rooms, which makes it one of '
           'the best returns on revision time in the exam.',
           'It is also the one candidates most often revise backwards, because the descriptors '
           'do not ask for rare words. They ask for less common words used <em>accurately</em> '
           'and <em>flexibly</em>, and they penalise inaccuracy by name.'],
  'callout': '<strong>Words you have to use, not words you have to read.</strong> A word you '
             'can recognise scores nothing. The route is built around collocation, paraphrase '
             'and topic banks &mdash; the three things that turn recognition into production.',
  'art': 'ielts-vocabulary/hero.jpg',
  'hero_pos': '25% 50%',
  'art_alt': 'Illustration of an old wooden card-index cabinet standing alone against a large '
             'plain wall, one drawer open',
  'tracks': [{'h': 'The criterion first, then the banks that feed it',
              'note': '25% of Speaking &middot; 25% of Writing &middot; the same criterion, '
                      'marked twice',
              'lessons': [{'file': 'forbes-english-ielts-lexical-resource.html',
                           'title': 'Lexical Resource &mdash; what is actually scored',
                           'desc': 'Precision over rarity, the pairing rather than the word, '
                                   'and paraphrase as the skill that pays in two papers at '
                                   'once. Ends by building one page of a topic bank in five '
                                   'minutes, which is the method the rest of the route uses.',
                           'tags': ['Speaking &amp; Writing']},
                          {'file': 'forbes-english-ielts-vocabulary-environment.html',
                           'title': 'Topic bank &mdash; environment and energy',
                           'desc': 'The first of the banks, built by idea rather than '
                                   'alphabetically: emissions, renewables, consumption and '
                                   'waste, each arriving with two phrases and an argument '
                                   'already attached.',
                           'tags': ['Topic bank']},
                          {'file': 'forbes-english-ielts-vocabulary-work.html',
                           'title': 'Topic bank &mdash; work, automation and cities',
                           'desc': 'Three topics that come up again and again in Part 3 and '
                                   'Task 2, and the collocations that make an answer on any of '
                                   'them sound like someone who has thought about it before.',
                           'tags': ['Topic bank']}]}],
  'reference': [],
  'teach': {'h': 'Teaching this rather than sitting it?',
            'p': ['The first lesson&rsquo;s activation stage needs a pen and nothing else: '
                  'pairs build one page of a topic bank in five minutes, then argue the topic '
                  'for two minutes using the phrases on the page. The rule that makes it work '
                  'is that every entry must be a pairing &mdash; a verb with its noun, or an '
                  'adjective with its noun. Bare words are not allowed: each word goes in with '
                  'the words it travels with.']}}]
