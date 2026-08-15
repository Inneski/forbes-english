# Lesson builders

Every 16:9 deck on this site is **generated**, not hand-written. This
folder is the source; the `.html` in the repo root is the output. Edit a
lesson by editing its builder and re-running it — editing the generated
HTML works once and is then overwritten by the next build.

These files lived in `/tmp` for a long time, which meant that when a
session ended the only way to change a shipped lesson was to hand-edit
80,000 characters of generated markup. That is why they are here now.

## The two shared modules

**`deck.py`** — the slide builders every lesson uses: `cover`, `teach`,
`mc`, `gap`, `match`, `order`, `sort_slide`, `results`, `activate`, and
`assemble`, which stitches the slides into a copy of the template,
replaces the palette block and writes the `UI_I18N` object.

It also carries two build-time guards, and they exist because both
defects shipped before anyone was measuring:

- `assert_no_key_is_longest` — the correct option must not be
  conspicuously the longest. The test is a ratio **and** an absolute
  floor of four characters, because on one-word options from a closed
  set (`can / could / must / should`) a key two characters longer
  carries no information at all.
- `assert_bank_is_not_a_key` — a word bank must not list the gap answers
  in gap order. Alphabetise instead; it also keeps the bank stable
  across reloads, so a printed hand-out matches the screen.

**`chrome_i18n.py`** — generic interface strings (buttons, score labels,
the plural-aware `wordCount` function) for all ten languages, lifted from
`forbes-c1-negotiation.html`, which is the worked reference. Lift from
here rather than retranslating. Russian's `wordCount` is a multi-line
arrow function, so it was lifted with a brace-aware scan rather than a
line regex.

## Two things `deck.py` now does for you

**`mc(..., explains=[...])`** takes one explanation per option, so a learner
who picks a distractor is told why *their* answer was wrong rather than why
the key was right. Five builders did this by injecting `data-explain` onto
the buttons after calling `D.mc`; those still work and produce identical
markup, so they have not been rewritten, but **new builders should pass
`explains=`**. `None` in the list leaves that option to the slide-level
explanation.

**`assemble()` sets `data-theme` from the palette.** It reads `--void`,
computes its relative luminance, and adds `data-theme="light"` above 0.2.
Two shipped decks carried a light palette with no attribute, so the light
primitives never applied and their insets and hairlines — white on cream —
were invisible. It used to be a line each builder had to remember. It is not
any more; a builder that still does the replace itself is harmless, because
the attribute is already there and the replace finds nothing.

## Import path

Every builder must import from the repo:

```python
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
```

**Not `/tmp`.** Fifty-four of them used to, which meant that on a fresh
session — where `/tmp` is empty — they could not import `deck` at all and no
lesson could be rebuilt. The modules they needed lived only in `/tmp` too;
`camp_diagrams`, `passive_kit`, `sailing_map` and five others were rescued
into this folder for the same reason.

## Building a lesson

```bash
cd /path/to/forbes-english
python3 lesson-template/build/build_<name>.py
node lesson-template/check-lesson.js <lesson>.html   # must exit clean
```

Each `build_<name>.py` pairs with an `i18n_<name>.py` holding that
lesson's own strings. The i18n module imports its builder to pull shared
data tables (vocabulary notes, reading notes) rather than duplicating
them — safe in both directions, because the builder only imports the
i18n module inside its `__main__` block.

Every builder opens with a docstring recording what was wrong with the
lesson it replaced. That is deliberate: it is the only place the
reasoning survives, and it stops a later pass quietly reintroducing a
defect that was removed on purpose. **It does not belong on a slide** —
learner-facing text should never mention a previous version of the
lesson.

## Helpers

- **`shot2.js`** — screenshot given slides. It navigates with the real
  `.nav-btn[data-action="next"]`, because forcing `is-active` bypasses
  `goTo()` and per-slide `data-bg` backgrounds then never apply. Verify
  artwork with this, not by forcing classes.
- **`rendersvg.js`** — render an `.svg` to PNG for eyeballing.

## Conventions worth keeping

- Palettes are derived: `python3 lesson-template/extract-palette.py
  <hero> [--light]`. Every body-text row in the contrast report must
  PASS. Never hand-pick.
- Slide-count chips: read the number from `check-lesson.js`'s own header
  line. Counting `<section class="slide` in the source returns N+1.
- The shell's working directory resets between calls; run builders from
  the repo root.

## Two builders are not builders

`build_gf.py` and `build_kool.py` read their already-built lesson and
extract a JS block from it. They were one-shot converters, they cannot
regenerate their deck from the template, and they fail if run. Left in place
because they record how those two lessons were made; do not expect them to
run.

## Order matters for the sherpa decks

`sherpa-tensing-camp-one` and `camp-two` are written by one builder and then
post-processed by another that **appends** the shared route-timeline CSS
without checking whether it is already there. Running the whole build set
twice injects it twice. Regenerate those two singly, or check the output.
