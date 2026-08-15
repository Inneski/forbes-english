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
