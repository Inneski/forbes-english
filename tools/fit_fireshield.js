#!/usr/bin/env node
/*
 * Render every scene of fireshield-pitch.html into the 1280x720 canvas and
 * measure whether it fits.
 *
 * check-lesson.js measures the slides it finds in the DOM. This lesson has one
 * slide that the engine re-renders 32 times, so the checker only ever measures
 * whichever scene happened to be showing. That is the whole deck budget going
 * unchecked, in the one lesson whose content varies most.
 *
 *     node tools/fit_fireshield.js [--lang de]
 *
 * Exits non-zero if any scene overflows, in any offered language — German runs
 * roughly 15% longer than English, so it is the one that overflows first.
 */

const { chromium } = require("playwright");
const path = require("path");

const CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";
const FILE = "file://" + path.join(__dirname, "..", "fireshield-pitch.html");

(async () => {
  const argLang = (process.argv.indexOf("--lang") > -1)
    ? [process.argv[process.argv.indexOf("--lang") + 1]] : null;

  const browser = await chromium.launch({ executablePath: CHROME });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  const errors = [];
  page.on("pageerror", e => errors.push(String(e.message)));
  await page.goto(FILE);
  await page.waitForTimeout(300);

  const langs = argLang || await page.evaluate(() => completeLangs());
  let worst = 0, fails = [];

  for (const lang of langs) {
    await page.evaluate(l => { LANG = l; applyI18n(); }, lang);

    const keys = await page.evaluate(() => Object.keys(SCENES));
    for (const key of keys) {
      const m = await page.evaluate(k => {
        // Put the engine on this scene and draw it into the real canvas.
        current = k;
        show(2);
        render();
        const slide = document.querySelector('.slide[data-type="scene"]');
        const card = slide.querySelector(".card");
        const stage = document.getElementById("stage");
        // Overflow past the 720px stage, and any inner scrolling in the card.
        const cardBottom = card.getBoundingClientRect().bottom;
        return {
          past: Math.round(cardBottom - stage.getBoundingClientRect().bottom),
          inner: Math.max(0, card.scrollHeight - card.clientHeight),
        };
      }, key);

      const over = Math.max(m.past, m.inner);
      if (over > 0) {
        fails.push({ lang, key, past: m.past, inner: m.inner });
        if (over > worst) worst = over;
      }
    }
  }

  // The activation slide is static, so measure it once per language.
  for (const lang of langs) {
    const m = await page.evaluate(l => {
      LANG = l; applyI18n(); show(3);
      const slide = document.querySelector('.slide[data-type="activate"]');
      const stage = document.getElementById("stage");
      return Math.round(slide.scrollHeight - stage.clientHeight);
    }, lang);
    if (m > 0) fails.push({ lang, key: "activate", past: m, inner: 0 });
  }

  console.log(`measured ${langs.length} language(s) x 32 scenes + activation`);
  if (errors.length) console.log("JS errors:\n  " + errors.join("\n  "));

  if (fails.length) {
    console.log(`\n${fails.length} overflow(s), worst ${worst}px past the canvas:`);
    for (const f of fails) {
      console.log(`  [${f.lang}] ${f.key.padEnd(16)} past:${String(f.past).padStart(4)}px  inner:${String(f.inner).padStart(4)}px`);
    }
  } else {
    console.log("\nPASS — every scene fits 1280x720 in every offered language.");
  }

  await browser.close();
  process.exit(fails.length || errors.length ? 1 : 0);
})();
