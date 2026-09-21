# Forbes English at Work — the series bible

Five coursebooks, A1 to C2, for people who use English at work. This folder is
the whole design: the world the books are set in, the cast, the four strands
every unit is built from, the page plan, the writing rules, and the artwork
spec. The five level files beside it hold all 75 units, each one specified
down to its model dialogue and its two pictures, so that any writer, any
illustrator or any session can pick up a unit and produce it without asking a
question.

**Working title.** The syllabus this grew from was drafted as a "conceptual
reimagining" of an Oxford University Press series, and it still carried that
series' name and the name of one of its sections. Both are OUP's. The series
here is *Forbes English at Work*; the section is *In the Room* (§3). The title
is a placeholder until Innes chooses one and runs a trademark search on it —
nothing else in these files depends on it.

| file | what it is |
|---|---|
| `README.md` | this: the bible |
| `level-1-day-one.md` | 15 units, A1/A2 |
| `level-2-joining-in.md` | 15 units, A2/B1 |
| `level-3-taking-charge.md` | 15 units, B1+/B2 |
| `level-4-setting-the-course.md` | 15 units, B2/C1 |
| `level-5-the-long-game.md` | 15 units, C1/C2 |
| `build_book.py`, `print_book.js`, `content_book1.py` | lay a book out as A4 pages: `py docs/at-work/build_book.py 1` writes `book-1.html`, `node docs/at-work/print_book.js 1` renders `book-1.pdf` (not committed) and reports any page whose content overflows. Six pages a unit in the editorial style (§4), a hero across the top of each opener, a dashed slot for every picture, the AI dialogue tagged as a draft. `content_book<n>.py` holds the exercises the spec does not: matching, gapped text, rule cards, practice, gist questions, role cards, the listening script and questions, the pronunciation note, the grammar reference |

---

## 1. The series at a glance

| | title | CEFR | the year it covers | company | city | the learner's proxy |
|---|---|---|---|---|---|---|
| 1 | **Day One** | A1/A2 | surviving the modern workplace | Greenline Office, recycled office furniture, 30 people | Bristol | Lena Hartmann, new marketing assistant |
| 2 | **Joining In** | A2/B1 | participating and collaborating | Tidewater, online outdoor-gear retailer, 120 people | Rotterdam | Noor Haddad, new product-team member |
| 3 | **Taking Charge** | B1+/B2 | managing and organising | Larkline, e-bike maker, 400 people | Copenhagen | Daniel Mensah, new operations manager |
| 4 | **Setting the Course** | B2/C1 | strategising and leading | Arden Health, telemedicine scale-up, 900 people | Berlin | Grace Mbeki, new Director of Operations |
| 5 | **The Long Game** | C1/C2 | influencing, innovating and executive diplomacy | Meridian Group, listed industrial group in transition, 40,000 people | London and Zürich | Mei-Lin Chao, new Chief Strategy Officer |

Each book is one working year seen through one newcomer. The newcomer is the
learner's proxy: the person who does not yet know how things work here, asks
the questions the learner would ask, and is a little further on by Unit 15.
Every model dialogue puts the proxy in the room, so the learner is always
rehearsing their own part.

**Back-cover copy, one line per level:**

1. *Day One* — Your first year in an English-speaking workplace, one small
   step at a time: names, times, tools, trains, orders, visitors and what to
   say when the screen freezes.
2. *Joining In* — You have a seat at the table. Now take part: updates,
   brainstorms, customer problems, dashboards and the small words that keep a
   team polite.
3. *Taking Charge* — Someone has to run this. Sprints, supply chains,
   forecasts, a PR crisis and the difficult one-to-one — the language of the
   person responsible.
4. *Setting the Course* — Where is this company going, and can you say it so
   a board believes you? Strategy, investors, restructuring, and the art of
   pushing back.
5. *The Long Game* — At the top table, words are decisions. Keynotes,
   governance, geopolitics, succession, activism and the address you give on
   the way out.

---

## 2. One world, five companies

The five books share a universe. Nobody has to know this to teach one unit,
but a teacher who works through the series will notice, and it costs nothing.

- **Greenline Office** (Book 1) makes desks and chairs from recycled plastic
  and reclaimed wood, sells them online, and delivers in its own van. Larkline
  (Book 3) buys its office furniture from Greenline; the Greenline desk is in
  the background of every Larkline office scene.
- **Tidewater** (Book 2) sells outdoor gear online across Europe. It stocks
  Larkline e-bikes from Book 3, Unit 10 onwards, and its customer-support
  team is the one that fields the complaints when a Larkline battery recall
  hits in Book 3, Unit 13.
- **Larkline** (Book 3) makes e-bikes in Copenhagen with frames from a factory
  in Portugal and batteries from Asia. Its Head of People, Beatriz Costa,
  leaves at the end of Book 3 and reappears in Book 4 as Arden's Head of
  People. Meridian (Book 5) makes a bid for Larkline in Book 5, Unit 6.
- **Arden Health** (Book 4) is a video-consultation platform with 900 staff
  and a Series C round behind it. Larkline offers Arden to its employees;
  Meridian's board looks at Arden as an acquisition target and walks away.
- **Meridian Group** (Book 5) is a listed engineering group moving from
  oil-and-gas services into grid technology and renewables, with a board, a
  regulator, an activist shareholder and a union.

None of the companies, people, products or places is real. **No real company,
product, platform or person is ever named** — not as a competitor, not as a
comparison, not in a dialogue. "The video-call app", "a spreadsheet", "the
chat tool" do the job and never date.

### The cast

Each book has five recurring characters and a handful of walk-ons (a
customer, a supplier, a journalist). Five is the number a reader can hold and
a recording budget can afford. Pronouns are fixed here so that the books agree
with each other.

**Book 1 — Greenline Office, Bristol**

| name | role | pronouns | how the silhouette is known |
|---|---|---|---|
| Lena Hartmann | new marketing assistant, from Hamburg | she | gold shoulder bag |
| Tom Reilly | warehouse and deliveries | he | flat cap |
| Ana Ruiz | sales, works remotely from Valencia | she | headset, usually on a screen |
| Sam Okafor | founder and managing director | he | round glasses |
| Priya Nair | IT — everything with a plug | she | laptop under one arm |

**Book 2 — Tidewater, Rotterdam**

| name | role | pronouns | known by |
|---|---|---|---|
| Noor Haddad | new in the product team | she | green rucksack |
| Marco Bellini | customer-support lead | he | mug, always |
| Jonas Weber | data and product analyst | he | second monitor |
| Aisha Warsame | freelance designer, London | she | tablet and stylus |
| Katrin de Vries | team lead | she | long scarf |

**Book 3 — Larkline, Copenhagen**

| name | role | pronouns | known by |
|---|---|---|---|
| Daniel Mensah | new operations manager, from Manchester | he | amber cycling helmet |
| Elin Sørensen | product owner | she | notebook and pen |
| Yusuf Demir | marketing and creator partnerships | he | phone on a tripod |
| Beatriz Costa | Head of People | she | lanyard |
| Ken Ito | finance lead | he | calculator watch |

**Book 4 — Arden Health, Berlin**

| name | role | pronouns | known by |
|---|---|---|---|
| Grace Mbeki | new Director of Operations, from Johannesburg | she | cobalt coat |
| Nadia Rahimi | CEO and co-founder | she | standing, never seated |
| Felix Brandt | CTO | he | hoodie |
| Ravi Chandran | CFO | he | folder of papers |
| Beatriz Costa | Head of People (joined from Larkline) | she | lanyard |

**Book 5 — Meridian Group, London and Zürich**

| name | role | pronouns | known by |
|---|---|---|---|
| Mei-Lin Chao | new Chief Strategy Officer | she | plum umbrella |
| Kwame Asante | Group Chief Executive | he | fountain pen |
| Helena Strand | Chair of the Board | she | silver hair, tall chair |
| Ilse Vogel | General Counsel | she | ring binder |
| Victor Aldana | activist investor, 9% shareholder | he | phone at his ear |

---

## 3. The four strands — and why "Practically Speaking" became "In the Room"

Every unit has the same four strands, in the same order, so a learner always
knows where they are.

| strand | what it teaches | the page |
|---|---|---|
| **Vocabulary** | the 10–14 words and collocations the unit runs on | one page, before anything is tested |
| **Grammar** | one structure, shown in the unit's own dialogue before it is explained | one page, plus the reference at the back |
| **Communication** | the task of the unit — the thing the learner will do at work | two pages: model dialogue, analysis, practice |
| **In the Room** | the real-time, interpersonal layer: the words that manage the *moment* rather than the *message* | one page: phrase box, listening, mini role-play |

**Why "In the Room".** The fourth strand is the one that makes a competent
speaker sound like a person. Spelling your name on a bad line, showing
interest, apologising and accepting an apology, softening, buying time,
reading the room, using a pause. None of it carries content; all of it decides
how the content lands. "In the Room" names that: it is what you do while you
are in the room with someone — and a video call is a room. It also scales
across the whole series, from *Can you hear me?* in Book 1 to *commanding a
room* in Book 5, Unit 1, which the original syllabus already used as a
phrase. Two alternates if Innes wants a different note: *In the Moment*
(same idea, slightly warmer) and *Say It Well* (plainer, more textbook).

The other three keep their plain names. "Vocabulary", "Grammar" and
"Communication" are the words a learner searches for, and nobody owns them.

---

## 4. Anatomy of a unit

Six pages, A4, so 15 units make a 90-page book before front and back matter
(assumption: A4 portrait, 210 × 297 mm; change the artwork spec in §7 if the
trim changes). The first proof was planned at eight pages and the content of
an A1 unit filled five of them halfway; six is what the content fills to the
foot, measured on Book 1.

Every page is composed to the editorial style (HOUSE-STYLE §15): a flat cream
field, the heading across the full width, and the picture in a framed column
under it, on the right or the left, rounded or arched, wide or narrow. The
sides alternate by unit. The one exception is the opener, whose hero runs
right across the top of the page, with the unit number and title in a dark
strip beneath it.

Three things carried over from the coursebook convention Innes pointed at:
a **running band** across the top of every inner page (unit and title on the
left, section on the right), **tinted panels** for the key words, the phrase
box, the language point and the tip, and section heads written *Section |
topic*. And one thing that is ours: **a grammar page whose unit teaches a
tense takes that tense's colour** from the Sherpa Tensing code (HOUSE-STYLE
§5a) for its band, its formula and its marked words. The rule is never boxed:
it is one open **formula line** set large in that colour, then Form, Use and
Watch out as run-in paragraphs.

| page | section | content |
|---|---|---|
| 1 | **Opener** | the hero across the top; the unit title and strapline; three *can-do* lines beside the unit menu; the lead-in; the story in serif |
| 2 | **Vocabulary** | the word set as chips, a match-the-meaning task beside an arched picture-to-label plate, a gapped text with a word box, a personalisation question |
| 3 | **Grammar** | the four marked sentences and three rule cards beside a narrow plate; six practice items; six word-choice items |
| 4 | **Listen and read** | the model dialogue (recorded: see §6) beside the scene plate, tagged as an AI draft until replaced; two gist questions; a change-three-things re-read; the role-play task and its two role cards |
| 5 | **In the Room** | the phrase box beside an arched plate; a four-question listening; the one-minute role-play; the *Say it right* pronunciation note; a write-it-down task |
| 6 | **The Case and Homework** | the *speaking* and *writing* activation beside a plate, never a quiz, the same rule as the deck activation stage in HOUSE-STYLE §10b; below a rule, the homework: one task to do alone and the five-item self-check whose key is at the back |

**Word budgets.** A page is roughly 300 words of learner-facing text once
the artwork, the rubrics and the white space have taken theirs. A dialogue
that runs long is split across two recordings, never set smaller.

**The spec block in each level file** gives, per unit: title and strapline;
the can-do line; the scenario; the four strands as a table; the lead-in; the
grammar as it lands in the dialogue; the In the Room phrase box; the model
dialogue in full; the case; the homework with its self-check and key; and
the two artwork subjects. That is enough to write the eight pages from.

---

## 5. Grading — the level of the language is the level of the grammar

A unit is told in the English of its level. If a sentence needs the point
being taught in order to be understood, it is on the wrong page. If a
dialogue at A1 needs a *will* to work, the dialogue is wrong, not the
syllabus.

| book | dialogue | lines | a sentence | structures available | what is not available yet |
|---|---|---|---|---|---|
| 1 | 80–120 words | 8–13 | about ten words, one clause | *be*, present simple, present continuous, past simple from Unit 6, *can*, *would like*, *going to* from Unit 15 | *will*, perfect tenses, conditionals, passives, relative clauses, reported speech |
| 2 | 110–150 words | 10–12 | about fourteen words | + present perfect, *will*, first and zero conditional, modals of obligation and possibility, passives, past continuous, verb patterns | second conditional, past perfect, reported speech |
| 3 | 160–220 words | 11–15 | about eighteen words, two clauses | + second conditional, past perfect, reported speech, future perfect and continuous | mixed conditionals, inversion, participle clauses |
| 4 | 200–280 words | 12–16 | complex sentences, hedged | + third and mixed conditionals, inversion, advanced passives, participle clauses, relative clauses of every kind | nothing, but nothing is used for show |
| 5 | 250–340 words | 12–20 | as long as the point needs | everything, including the subjunctive, cleft sentences, ellipsis and register shifts within a turn | — |

Vocabulary follows the same rule. Book 1 says *broken*; Book 3 says
*damaged in transit*; Book 5 says *a latent defect*. The word set in each unit
is the ceiling, and the dialogue stays under it.

---

## 6. Writing rules

- **British spelling and usage throughout**, as on the site: *organise,
  colour, programme, a fortnight, Mr* without a stop.
- **The dialogue is a recording script.** Two or three speakers as the norm;
  a team-call scene may run to four, and the five never all speak in one
  recording. A dialogue told in two scenes (*Later, by phone.*) is two
  recordings, and each scene keeps to the limit on its own. First names as
  speaker labels; a one-line stage direction in italics where the setting
  matters. Read it aloud before signing it off: a sentence that cannot be
  said in one breath is two sentences. The word caps in §5 are per sentence,
  not per turn — a turn of three short sentences is fine at A1.
- **In the spec files, the grammar target is in bold and the In the Room
  phrases are in italics** so a reviewer can see at a glance that the
  dialogue hits its targets. Every dialogue uses the grammar target at least
  three times and at least three of its In the Room phrases. The formatting
  is for the spec; in the printed book the dialogue is plain, and the
  Grammar page re-quotes the marked sentences.
- **Every word in the Vocabulary set appears in the unit**, in the dialogue,
  the case, the lead-in or the Vocabulary page's own context text. The spec
  block carries the dialogue, the case and the lead-in; the words those three
  do not reach are the writer's to place on the Vocabulary page, in the
  message thread, web page or form that introduces the set. A word that is
  listed and never used anywhere is a word the learner cannot revise from.
- **The case is two tasks, speak and write**, both set in the unit's story,
  both requiring the grammar and at least four of the words. "Discuss the
  advantages of remote work" is not a task; "You are Ana. Tell Sam what you
  need for the Madrid visit, then write the four-line message to the hotel"
  is.
- **No real brands, products, platforms or people**, anywhere. No meta
  language: the book never refers to itself, to an edition, or to a previous
  version of anything.
- **Names and numbers are read aloud in the recording** as the phrase box
  teaches them, so a Book 1 dialogue that says "two thousand and fifteen"
  prints the words, not the digits.
- **The proxy asks, the others answer.** The newcomer's job in a dialogue
  is to need something. The person who already knows sets the model.
- **Each unit's story moves the year on.** Unit 1 is the first day; Unit 15
  is the end of the year. A writer may add walk-on characters, but the five
  named ones behave consistently across all 15 units, and the events listed
  in §2 happen where §2 says they do.

---

## 7. Artwork

Two pictures per unit, 150 for the series. They are commissioned the way
every other set in this repo is: one style stem, a subject line per slot,
and a composition rule written for the crop that actually arrives.

### The style

Figures are **silhouettes, faceless**, each character told apart by the prop
listed in §2. This is not a stylistic whim: a generated face cannot be kept
consistent across fifteen pictures, and a silhouette with a gold bag can.
It is also the house stem already used for the site's business decks
(`docs/PLAN-foundations-grammar-business.md`), so the books and the site
look like one thing.

```text
<subject>, flat vector illustration, cel-shaded, solid flat colour,
minimalist, Noma Bar style, wide landscape, warm cream ground, black and
slate-blue silhouettes, <LEVEL ACCENT> accent, bright and airy, figures as
simple faceless silhouettes, subject off-centre, no text, no numbers, no
logos --ar 3:2 --style raw
```

**One accent per book, so the five spines read as a set on a shelf.** Name
it in the prompt in words; the print palette is the designer's to fix.

| book | accent | the proxy's prop is in it |
|---|---|---|
| 1 | gold | Lena's bag |
| 2 | sea green | Noor's rucksack |
| 3 | amber | Daniel's helmet |
| 4 | cobalt | Grace's coat |
| 5 | plum | Mei-Lin's umbrella |

### The two slots

| | **opener** | **scene** |
|---|---|---|
| where | full bleed across the unit's opening spread | a band across the top of the Communication page, above the dialogue |
| ratio the frame wants | 3:2 (a 420 × 297 spread is 1.41:1) | 2:1 |
| ask for | `--ar 3:2` | `--ar 2:1` |
| expect | 16:9 — this pipeline has returned 16:9 whatever was asked (`docs/ARTWORK-holding-the-line.md`) | 16:9 |
| so compose | subject inside the **middle 75%**; nothing that matters in the **central 6%** (the gutter) or the **bottom-left quarter** (the unit menu and can-do box sit there) | subject inside the middle 80%; keep the top clear of anything tall, the band is shallow |
| print size | 4,960 px across at 300 dpi. A 2× upscale gives ~2,900 px and prints soft at 175 dpi: run the 4× upscale, or 2× twice | 2,480 px across; a 2× upscale is enough |
| deliver as | PNG, un-split four-up is fine — `tools/prep-artwork.py` picks and hashes | same |

**The middle 75% is the whole instruction for the opener**, exactly as the
middle 65% was for the editorial plates. A 16:9 picture cropped to 3:2
throws away an eighth of its width off each side. A subject composed inside
the band survives; one that spans the full width comes back with a
character cut in half.

### Filenames

`art/book-<n>/u<nn>-opener` and `art/book-<n>/u<nn>-scene`, so
`art/book-1/u03-opener.png` is Book 1, Unit 3, the spread. The level files
list the subject for each one; `<subject>, <stem>` is the prompt.

### The cover

Each book's cover reuses the Unit 1 opener, cropped to the front board, with
the stacked Forbes/ENGLISH lockup from `lesson-template/forbes-logo.svgfrag`
(HOUSE-STYLE §2 has the geometry: two lines, one optical width). The title,
the level name and the CEFR band go in the quiet space the composition rule
leaves at bottom-left.

---

## 8. Front and back matter, every book

- **Map of the book** — the fifteen units against the four strands, one row
  each: the table at the top of each level file, typeset.
- **Meet the team** — the five characters, one line and one silhouette each.
- **Grammar reference** — one page per unit, at the back, with the rule in
  full and the exceptions the unit page had no room for.
- **In the Room phrase bank** — every phrase box in the book, on two pages.
- **Audio scripts** — every model dialogue and every In the Room listening.
- **Word list** — the vocabulary sets, with the unit number, alphabetised.
- **Answer key** — the key to every unit's five-item self-check, in every
  edition; the self-study edition adds keys for the in-unit exercises too.

---

## 9. What is still Innes's call

1. The series title, and a trademark search on it.
2. The trim size, if not A4. §7's numbers follow from it.
3. Whether the recordings are done in-house or commissioned; the dialogues
   are written to be recorded either way.
4. Whether the books carry German and Spanish glossaries. The site rule
   (every deck ships EN, DE and ES) suggests the word lists should, and the
   spec leaves room for it in the back matter.
