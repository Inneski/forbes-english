# Getting found: what the site does, and what only Innes can do

Written 2026-09-12, when the question was "how do we get this baby found
online". This is the answer, in two halves: the part that lives in the
repo and runs on every build, and the part that needs an account, a DNS
record or a human, and cannot be done from here.

## What the repo does on every build

Everything below is generated. Do not hand-edit the output; edit the tool
and re-run. The order is fixed:

```bash
python3 tools/build_hubs.py     # the topic pages, from the catalogue
python3 tools/seo.py            # ALWAYS last: titles, meta, sitemap, llms.txt, lesson-meta.json
```

**`tools/topics.py` is the topic map.** Eighteen topics — the tenses,
passive, modals, prepositions, gerunds, conditionals, used to, phrasal
verbs, tense review, business English, IELTS and a vocabulary catch-all —
each with a regex over title-plus-filename, an `OVERRIDES` table for
titles that say nothing about their grammar ("Champions League", "Grammar
Atelier"), and three to four paragraphs of plain-sentence explanation of
the grammar point. That copy is the part a search engine can rank; the
lesson list under it is the part that converts. **A new lesson with an
opaque title goes in `OVERRIDES` or it lands on the vocabulary page.**

**`tools/build_hubs.py` writes `grammar.html` and one page per topic**
(`present-perfect.html`, `passive-voice.html`, …): breadcrumb, the copy,
a facts box, every lesson on the point grouped by level with free ones
first, chips to the other topics, and ItemList + BreadcrumbList JSON-LD.
The stylesheet and top band are lifted from `ielts.html` at build time so
the chrome cannot drift. Slugs are real search phrases; check a new slug
against the root before adding one, because lesson asset folders live
there too.

**`tools/seo.py` changed in four ways:**

1. **Page titles say the grammar point.** `page_title()` appends the
   topic when the printed title does not already contain it: "Minecraft
   B1 Lesson" became "Minecraft B1 Lesson — Modal Verbs (B1) | Forbes
   English". The brand is dropped first when the line passes 70
   characters; the topic and level never are.
2. **`rules()` now reads the teach cards it was written for.** It matched
   `<p class="prose"><strong>` alone, which is the card's *heading* ("The
   form"), never long enough to pass the 40-character floor — so 252 of
   256 lessons published no `teaches` at all. It now joins heading and
   rule ("Since and for: since takes a point, for takes a length") and
   reads Sherpa Tensing's `rule-card` markup too. **Measured: 4 lessons
   with rules before, 104 after.** The RPGs keep their rules in script
   data and still report none.
3. **`lesson-meta.json` carries `teaches` and `topics` per lesson**, and
   the Worker (`personaliseGate()` in `src/index.js`) prints them on every
   Pro gate page as "What this lesson teaches" plus "More on this: →
   topic hub". Same words for a crawler and a visitor — that is what
   keeps it out of cloaking territory. Before this a gated lesson's page
   was a title and two sentences; 266 of 300 lessons are gated.
4. **The hubs are in the sitemap, in `llms.txt` and at the top of the
   library's crawlable list**, and the "Grammar" link in the top band of
   the home page and the IELTS pages points at `grammar.html` instead of
   a library filter.

The home page is a fixed one-screen stage with `overflow: hidden` (see
its own CSS comments), so it did not get a text block. Its crawlable
weight comes from the nav link and from `library.html`.

## What only Innes can do — in this order

None of this is code. All of it is worth more than everything above.

**Status, 2026-09-12:** steps 1 and 2 are DONE. Search Console has a
Domain property for forbesenglish.com, verified by a TXT record that
Cloudflare added through Google's connect flow (do not delete the
`google-site-verification=` TXT record on the zone), and the sitemap is
submitted. Bing Webmaster Tools was created by importing from Search
Console under raarmusic@gmail.com, and the sitemap is submitted there too.
Both were driven from a local session through Innes's own Chrome; the
sign-ins and the OAuth consent were his clicks. Step 3 turned out to be
done already: Cloudflare Web Analytics has been on for forbesenglish.com
(automatic setup) since about August 2026. **Baseline on 2026-09-12: 1
visit in the previous 24 hours.** That is the number everything below is
measured against. Steps 4 and 5 remain.

1. **Google Search Console.** search.google.com/search-console → add a
   *Domain* property for `forbesenglish.com` → verify with the DNS TXT
   record it gives you, added in the Cloudflare DNS panel (the domain's
   nameservers are at Cloudflare; see `deploy/03-namecheap-dns.md`).
   Then Sitemaps → submit `https://forbesenglish.com/sitemap.xml`. Until
   this is done nobody has told Google the site exists, and there is no
   data on what ranks. Check the Pages report a fortnight later for
   "Crawled, not indexed" — that is the list of pages Google thinks are
   thin, and the gate-page excerpt above is the answer to it.
2. **Bing Webmaster Tools.** bing.com/webmasters → "Import from Google
   Search Console". One click; it also feeds DuckDuckGo and the search
   behind ChatGPT.
3. **Cloudflare Web Analytics.** Cloudflare dashboard → Analytics & Logs
   → Web Analytics → enable for the zone. Because the site is served
   through Cloudflare it injects the beacon at the edge; there is no code
   to add. Free, cookieless, and the only way to see whether any of this
   is working.
4. **Links.** A site nobody links to does not rank, whatever the pages
   say. The audience with search intent is *teachers* looking for lesson
   material, more than learners. Where the links come from:
   - your own profiles: Preply / italki / LinkedIn bios, with the URL;
   - ESL teacher communities — r/ESLteachers, r/TEFL, the ELT forums —
     posting a *free* lesson with a sentence on how you use it, not the
     home page;
   - a guest post or two on ELT blogs, linking a hub page;
   - short video clips of a deck on YouTube with the lesson URL in the
     description;
   - a Google Business Profile if you teach in person anywhere.
5. **Make more of the good ones free.** Thirty-four free lessons carry
   the whole site's ranking weight. One strong free lesson per topic hub
   is the minimum; several hubs currently have none (Past Continuous,
   Past Perfect, Future Tenses, Used To). The hub page says "Every lesson
   here is part of Forbes English Pro" on those, which is honest and
   converts nobody.

Expect months. A new site with no history takes time to earn trust even
when everything is right; the first sign it is working is impressions in
Search Console, not visits.

## How to check it is still working

```bash
python3 tools/seo.py --check                 # would rewrite 0 pages
node   lesson-template/check-library.js --vs-origin
```

and, for the rule extraction, count lessons with a non-empty `teaches`
in `lesson-meta.json`. If that number falls after a builder change, the
teach-card markup moved and `rules()` in `tools/seo.py` needs the new
shape.
