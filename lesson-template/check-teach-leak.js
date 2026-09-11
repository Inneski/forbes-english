#!/usr/bin/env node
/**
 * check-teach-leak.js — does a teaching slide print the answer to an item?
 *
 * Written 2026-09-11 after a multi-agent audit found twelve examples across the
 * three preposition decks that were the item sentences verbatim. "The keys are
 * in the drawer" on a teach slide, then "The keys are ______ the drawer" four
 * slides later; "In 1998, on Saturday mornings, at 9 a.m." answered three time
 * items at once. Ten of B1's twenty-one place/time/movement items were answered
 * in print immediately before they were asked.
 *
 * Nothing caught it because nothing was looking: check-lesson.js verifies that
 * every question HAS an explanation, never that the question is still worth
 * asking. A learner could score without reading a word of the target language.
 *
 * WHAT IT LOOKS FOR, and why it is not a word-overlap score. The first version
 * of this file counted shared content words with a threshold, and it did not
 * fail the known-broken deck it was written from — "the keys are in the drawer"
 * shares only two content words with its item. A fuzzy score was the wrong
 * instrument. The leak has an exact shape:
 *
 *   the teach slide prints THE KEY followed by THE WORDS THAT FOLLOW THE GAP.
 *
 * `<em>on</em> Saturday mornings` on a teach card, then `______ Saturday
 * mornings` in an item keyed `on`. That is a filled-in answer, and it is
 * detectable with no threshold at all. A second pass catches the other shape —
 * a long verbatim run of the stem reproduced in the card, which is how "the
 * bank sits between the bakery and the pharmacy" leaked.
 *
 * The rule a builder should follow is not "never illustrate" — it is that the
 * RULE travels and the SENTENCE does not. Change the nouns.
 *
 * Usage:
 *   node lesson-template/check-teach-leak.js <lesson>.html [...]
 *   node lesson-template/check-teach-leak.js *.html --quiet   # only leaks
 *
 * Exit 1 if any leak is found. Deliberately NOT wired into check-lesson.js:
 * that gate runs on 114 shipped decks and this would fail an unknown number of
 * them at once. Run it when you write or revise a deck; fix what it finds.
 */
const fs = require('fs')

const text = t => t.replace(/<[^>]*>/g, ' ')
                   .replace(/&mdash;|&ndash;/g, ' ')
                   .replace(/&middot;/g, ' ')
                   .replace(/&[a-z]+;|&#\d+;/gi, ' ')
                   .replace(/\s+/g, ' ').trim()

const toks = t => text(t).toLowerCase().match(/[a-z0-9][a-z0-9'.]*/g) || []

const THRESHOLD_RUN = 4   // verbatim tokens of a stem reproduced in a card

// True when the card cites `span` ANYWHERE at least half emphasised.
//
// Deliberately permissive, and the permissiveness is the point: one card may
// print the same phrase twice, once as a clean citation (<em>in charge of</em>)
// and once with split emphasis to show the tail varies (in charge <em>of</em>,
// in favour <em>of</em>). Requiring every occurrence to be emphasised let the
// second poison the first and re-flagged five legitimate phrase lists. If the
// deck names it as vocabulary once, it is vocabulary.
function isCited(t, span) {
  for (let i = 0; i + span.length <= t.toks.length; i++) {
    if (!span.every((w, k) => t.toks[i + k] === w)) continue
    const marked = span.filter((_, k) => t.emph[i + k]).length
    if (marked * 2 >= span.length) return true
  }
  return false
}
let failed = false
const quiet = process.argv.includes('--quiet')
const files = process.argv.slice(2).filter(a => !a.startsWith('--'))

if (!files.length) {
  console.error('usage: node lesson-template/check-teach-leak.js <lesson>.html ...')
  process.exit(2)
}

for (const file of files) {
  const html = fs.readFileSync(file, 'utf8')
  const slides = html.split(/<section class="slide/).slice(1)
  const teach = []
  const leaks = []

  slides.forEach((s, i) => {
    const type = (s.match(/data-type="([^"]+)"/) || [])[1]

    if (type === 'teach') {
      // NOTE the [^"]* — the card's note is <p class="prose dim">, and that is
      // where most of the leaking examples actually live. Matching only the
      // exact class caught 2 of the 10 leaks in the deck this was written from.
      const body = (s.match(/<p class="prose[^"]*"[^>]*>([\s\S]*?)<\/p>/g) || []).join(' ')
      // EMPHASIS DENSITY is what separates a citation from a narration, and it
      // is the whole reason this gate does not cry wolf.
      //
      // An idiom deck MUST print its idioms: you cannot teach "on behalf of"
      // without writing "on behalf of", and the card that teaches both ends of
      // a bookended phrase writes "<em>on</em> the verge <em>of</em>" — split
      // emphasis, on purpose. Those are citations. Meanwhile "<em>in</em> the
      // drawer" and "<em>on</em> Saturday mornings" emphasise only the answer
      // and narrate the rest: that is a sentence, and the item that follows is
      // answered in print.
      //
      // So: mark every token as emphasised or not, and exempt a match when at
      // least half of it sits inside <em>/<strong>. Measured against the deck
      // this was written from, that drops 10 false positives and keeps all 14
      // real leaks.
      const parts = body.split(/(<(?:em|strong)>[\s\S]*?<\/(?:em|strong)>)/)
      const flat = [], emph = []
      for (const part of parts) {
        const isEm = /^<(?:em|strong)>/.test(part)
        for (const w of toks(part)) { flat.push(w); emph.push(isEm) }
      }
      teach.push({ n: i + 1, toks: flat, emph, raw: text(body) })
      return
    }
    if (type !== 'mc' && type !== 'gap') return

    const stemRaw = (s.match(/class="q-stem"[^>]*>([\s\S]*?)<\/p>/) || [])[1]
    if (!stemRaw) return
    const stem = text(stemRaw)

    // the key: the option marked data-correct
    const key = (s.match(/<button[^>]*\bdata-correct\b[^>]*>([\s\S]*?)<\/button>/) ||
                 s.match(/data-answer="([^"|]+)/) || [])[1]
    if (!key) return
    const keyTok = toks(key)

    // what follows the gap, up to four tokens
    const after = toks(stem.split(/_{3,}/)[1] || '').slice(0, 4)
    const before = toks(stem.split(/_{3,}/)[0] || '')

    for (const t of teach) {
      if (t.n > i + 1) continue                       // only slides seen already

      // ── shape 1: the card prints KEY + the words that follow the gap ──
      if (after.length >= 2) {
        // Longest span first, and STOP at the first span this card cites: the
        // shorter fallbacks are sub-strings of it and would each look less
        // emphasised than the whole, so continuing past a citation re-flags
        // exactly what the exemption just cleared.
        for (let w = Math.min(4, after.length); w >= 2; w--) {
          const span = [...keyTok, ...after.slice(0, w)]
          const want = span.join(' ')
          if (isCited(t, span)) break
          // padded both sides so "of the" cannot match inside "of these"
          if ((' ' + t.toks.join(' ') + ' ').includes(' ' + want + ' ')) {
            leaks.push({ slide: i + 1, from: t.n, stem, shape: 'answer printed',
                         detail: `"${want}"` })
            w = 0; break
          }
        }
      }

      // ── shape 2: a long verbatim run of the stem reproduced in the card ──
      const stemToks = [...before, ...after]
      const hay = ' ' + t.toks.join(' ') + ' '   // padded: see note on `want`
      for (let start = 0; start + THRESHOLD_RUN <= stemToks.length; start++) {
        let len = THRESHOLD_RUN
        while (start + len <= stemToks.length &&
               hay.includes(' ' + stemToks.slice(start, start + len).join(' ') + ' ')) len++
        if (len > THRESHOLD_RUN) {
          const run = stemToks.slice(start, start + len - 1).join(' ')
          if (!leaks.some(l => l.slide === i + 1 && l.from === t.n))
            leaks.push({ slide: i + 1, from: t.n, stem, shape: 'sentence reused',
                         detail: `"${run}"` })
          break
        }
      }
    }
  })

  const seen = new Set()
  const uniq = leaks.filter(l => { const k = l.slide + ':' + l.from + l.detail
                                   if (seen.has(k)) return false; seen.add(k); return true })
  if (uniq.length) {
    failed = true
    console.log(`\n  ${file} — ${uniq.length} leak(s)`)
    for (const l of uniq) {
      console.log(`    slide ${l.slide} answered by teach slide ${l.from}  [${l.shape}]`)
      console.log(`      stem : ${l.stem}`)
      console.log(`      card : ${l.detail}`)
    }
  } else if (!quiet) {
    console.log(`  ${file} — no teach slide prints an item's answer`)
  }
}

if (failed) {
  console.log('\n  Fix by changing the NOUNS in the teach example. The rule has to')
  console.log('  travel; the sentence must not.\n')
}
process.exit(failed ? 1 : 0)
