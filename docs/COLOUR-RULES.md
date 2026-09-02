# Block Camp — the colour rules

Every rule below was read out of the 24 published decks on 2026-09-02, not
from memory. Counts are spans on display across the line. The gates that
enforce these live in `lesson-template/checker/check-colour-roles.py` and
`check-unmarked.py`; run both before shipping.

## The three sentences the whole system reduces to

1. **The `be` that MAKES the tense wears the tense.**
   `is/are/am + -ing` → present continuous pink. `was/were + -ing` → past
   continuous yellow. `is/are being` → pink; `was/were being` → yellow.
2. **The `be` that IS the verb wears its own tense.**
   Brown in past simple, slate in present simple.
3. **Green is the helper that carries no meaning of its own.**
   `do / does / did`. And — still unruled — `have / has / had` in the
   perfects. See "Open" at the foot of this file.

## Role colours — the same on every deck

| class | token | hex | what it marks | spans |
|---|---|---|---|---|
| `.aux` | `--mark-aux` | `#46D98A` mint | the meaningless helper: do-support, and `have/has` in the perfects | 255 |
| `.neg` | `--mark-neg` | `#F65AF6` magenta | every `not` and `n't`, always | 135 |
| `.inf` | `--mark-inf` | `#EEC32F` gold | the bare infinitive — after do-support, after a modal, after `going to` | 155 |
| `.modal` | `--mark-modal` | `#FF8A4C` orange | `will / would / can / should` | 100 |
| `.pp` | `--mark-pp` | `#B39BF5` violet | the past participle | 277 |
| `.agent` | `--mark-agent` | `#FFFFFF` white | the doer, in the passive | 36 |
| `.obj` | `--mark-obj` | `#909294` grey | the thing done to | 104 |
| `.freq` | `--mark-freq` | `#3295F4` beacon blue | adverbs of frequency (sampled from bg01's beacon shaft) | 18 |
| `.sig` | `var(--text)` | body colour | a time signal: an ordinary word the prose points at, no tense hue | 16 |
| `.state` / `.action` | `--mark-state` / `--mark-action` | `#5FC8F0` / deck accent | state vs activity, past-continuous-2 only | 14 |

`.verb` is a stale alias of `.inf` — two spans on present-simple. Retire it
rather than adding more.

## Tense colours — the route map

| tense | class | token | hex | spans |
|---|---|---|---|---|
| present simple | `.t-ps`, `.t-present` | `--t-present-simple` | `#7A93B5` slate | 210 |
| present continuous | `.t-pc` | `--t-present-continuous` | `#E68EA6` soft rose | 140 |
| past simple | `.t-past` | `--t-past-simple` | `#B08968` brown | 176 |
| past continuous | `.t-pastc` | `--t-past-continuous` | `#F1D779` yellow | 85 |
| present perfect | `.t-pperf` | `--t-present-perfect` | `#70E0E0` turquoise | 49 |
| going to | `.t-gt` | `--t-going-to` | `#70A43A` lime | 131 |
| future simple | `.t-fs` | `--t-future-simple` | `#F0723F` orange | 1 |

## The token is the system value; the ink is a measurement

A deck may paint a tense in a different hex, because contrast is a property
of that camp's surfaces and artwork, not of the token. Keep the published
token so the TOKENS gate holds the line together; add `--<tense>-ink`
beside it, derived mechanically (L\* raised in Lab, hue and chroma held)
until the ratio **measured off the render** clears 5:1.

| deck | ink | why |
|---|---|---|
| past-simple, past-simple-2, past-continuous-2 | `--t-past-ink: #D5AB89` | brown on a brown camp measured 3.4 / 4.4 / 4.2 : 1 |
| future-simple-2 | `--t-going-to-ink: #7BAF44` | lime on warm cards measured 4.0:1 |
| 12 decks | `#E68EA6` for the pink | softened at Innes's request from the route map's `#E66085` |

**Never measure a colour against an opaque surface.** Every colour defect
this system has shipped was invisible to a token-against-token check,
because the cards are translucent and sit on artwork.

## The standing rules

- **Always split.** The negator comes out of the contraction: `is` + `n't`,
  `do` + `n't`. `won't` is the one exception — it splits into "wo", which is
  not a word.
- **A question splits the chain, it does not change it.** `Is` … `raining`
  both keep the colours they had in the statement.
- **`going to` splits three ways**: `am/are/is` blue, `going to` lime,
  infinitive gold. Splitting the `be` shows how a question inverts and
  leaves room for the past version, `was/were going to`.
- **`was/were` are never brown in a past continuous sentence.**
  **`is/are` are never blue in a present continuous sentence.**
- **A negator is never anything but magenta.** Enforced by NEGCOLOUR — it
  found eleven wearing `.aux` or `.modal` on 2026-09-02.
- **Headings run in the aux green** — eyebrow, para-head, card lead-ins —
  on the 8 descent decks, to set them apart from the station's tense.
- **A struck-through error stays `--text-dim`**, auxiliary or not.
- **Never hardcode `rgba(0,0,0,…)` or `rgba(255,255,255,…)`.** Use the theme
  primitives.
- **Palettes derive mechanically from the hero.** Never hand-pick a colour;
  `extract-palette.py` does it and every row must PASS.
- **Learner-facing text never mentions a previous version of the lesson.**

## The gates

`check-colour-roles.py` — TOKENS (one value per token across the line),
ORPHANS (a class used with no rule behind it), UNTAGGED (a participle after
an auxiliary with no `.pp`), SPLITCHAIN, NEGSPLIT (a contraction left
whole), NEGCOLOUR (a negator in the wrong colour), SECOND FORMS (a past
simple form wearing the participle colour), AUXJOB (`.aux` on a word not
doing an auxiliary's job).

`check-unmarked.py` — a be-contraction on display carrying no role at all.

**Not gated yet**, and both went unseen for months because of it: a past
simple form left unmarked (needs a verb list), and effective contrast
measured off the render rather than off the token.

## Open — one decision, not yet made

If the continuous's `be` is half the tense, then the perfect's `have` is
half the tense in the same way: `has been`, `have seen`. By rule 1 it should
go turquoise. That is ~148 spans across six decks and it is the last green
that is not do-support. Decide it once, not one deck at a time.

Also open: whether the `be` inside an *illustrative* sentence — as opposed
to a taught form — wears its tense colour at all. 33 cases;
`check-unmarked.py --review` lists them.
