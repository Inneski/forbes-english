# Working on this repo

This is forbesenglish.com — an ESL lesson site. Read this file before doing
anything. It exists because sessions cannot talk to each other, so the repo is
the only shared memory. Anything a future session needs to know belongs here or
in one of the two documents below, not in a chat.

## The default action

**A forbesenglish.com URL means: rebuild that lesson as a 16:9 deck, to house
style. Start immediately.** An attached image is the hero for it. Two or more
images: the landscape one is the cover, the rest become per-slide backgrounds.

This is a standing instruction, not a per-request one. Innes sends a URL and a
picture and expects to get a finished deck back. **Do not open with a round of
questions about audience, level, tone, length or scope** — the audience is his
students, the level is on the lesson, the tone and length are defined in the
house style, and the scope is "the whole lesson, brought up to standard."

Read the lesson, audit it, build it, check it, ship it, then report what you
found and what you changed. `lesson-template/HOUSE-STYLE.md` §14 lists the four
situations that genuinely warrant a question. Everything else: apply the
standard and say what you did.

## Read these two, in this order

1. **`lesson-template/HOUSE-STYLE.md`** — binding. The six rules, the palette
   method, the slide budget, the activation stage, translation, QA.
2. **`docs/HANDOFF.md`** — the live queue, per-lesson audits, and the recurring
   defect pattern to check for in anything not yet rebuilt.

## The pipeline

```bash
python3 lesson-template/extract-palette.py <hero.jpg> [--light]   # every row must PASS
python3 lesson-template/build/build_<name>.py                     # builders live here
node   lesson-template/check-lesson.js <lesson>.html               # must exit clean
python3 tools/seo.py                                              # ALWAYS last
```

**`tools/seo.py` runs after every build, without exception.** It writes the
title, description, canonical, Open Graph and JSON-LD into each page, plus
`sitemap.xml`, `robots.txt` and `lesson-meta.json` — the last of which the
Worker reads to build a real gate page per Pro lesson. A builder re-run
overwrites the generated HTML and takes the SEO block with it, so a deck
shipped without this step goes out with no metadata at all. It is idempotent;
run it twice if you are unsure. `--check` reports without writing.

Every deck is **generated**. Edit the builder in `lesson-template/build/` and
re-run it; hand-editing the generated HTML works once and is then overwritten.
`deck.py` and `chrome_i18n.py` are shared — use them, don't rewrite them.

Palettes are derived mechanically from the hero. Never hand-pick a colour.

Slide-count chips take their number from `check-lesson.js`'s header line —
counting `<section class="slide` in the source returns N+1.

## Publishing

`git push` currently fails with a proxy 403: *"not in this session's authorized
repository set."* That is a session-startup setting, not something you can fix
from inside. Two routes:

- **If you have Chrome tools**, use GitHub's web uploader: `/upload/main` for
  root files, `/upload/main/<folder>` for a new directory — one directory per
  commit. Then verify byte-for-byte: `git fetch origin`, compare
  `git hash-object <file>` against `git rev-parse origin/main:<file>`, and only
  then `git reset --hard origin/main`.
- **If you do not**, commit locally and then call **`SendUserFile` on every
  changed file**. That is your sandbox's only exit. Work committed to a local
  branch that is never pushed is lost when the container is reclaimed — this
  has already happened once, to a finished 36-slide rebuild of
  `forbes-nature-agency-part1`.

Do not leave work sitting on an unpushed branch while waiting for a reply.
Deliver the files first, ask afterwards.

The live site follows `origin/main` within a few minutes.

### Before uploading `library.html`, always run

```bash
node lesson-template/check-library.js --vs-origin     # must PASS
```

**Verifying after the upload is not enough.** A byte-for-byte match against
`origin/main` only proves your bytes landed — which is exactly what a clobber
looks like too. The uploader replaces the file wholesale, so any entry added to
`LESSON_IMAGES` since you last read the file is deleted by your upload, and
nothing errors.

This has now happened twice to the same entry. The second time, `f6be885`
dropped the Stranger Things deck's thumbnail; its parent *did* contain the
commit that added it, so this was not a stale base — it was an in-memory copy
of `library.html` read before that commit and uploaded whole afterwards.
`git fetch` does not help. **Re-read the file from `origin/main` and re-apply
your change to it immediately before uploading.**

The failure is invisible from the front. The lesson keeps working: its row,
its page and its download are all fine. But `comingSoon()` is
`!LESSON_IMAGES[l.file]`, so losing the line turns the card into a disabled
"Coming soon" div and sorts it behind every other lesson. It reports as
"I can't see it", not as an error.

## Standing constraints

- **Learner-facing text must never mention a previous version of the lesson.**
  No "the old version marked this wrong" on a slide. That belongs in the
  builder docstring and the commit message.
- Hamster keeps his name. Do not rename Clarkson, Hammond or May in the
  published Stranger Gears build, and the Stranger Gears front-page image is
  not up for discussion.
- Never hardcode `rgba(0,0,0,…)` or `rgba(255,255,255,…)` in a lesson — use the
  theme primitives in the template.

## Things that have bitten us

- **A grid item wider than its track is aligned to start, not overflowed both
  sides.** This put every deck's stage off the right edge below 1280px — a
  black page on every phone. The stage is now pinned top-left and centred in
  `fitStage()`. Do not reintroduce `place-items: center` on `.stage-wrap`.
- **`--bins-h`-style layout constants belong in one custom property.** The same
  bug class appeared twice: a media query moved one hardcoded `200px` and left
  three others behind.
- A defect class needs a **measurement**, not just a fix. Both the SORT gate and
  the I18N generalisation were verified failing against deliberately broken
  copies before being trusted.

## Before you finish

Update `docs/HANDOFF.md` if you changed the queue, learned something a future
session needs, or found a defect you did not fix. That file is the handover.
