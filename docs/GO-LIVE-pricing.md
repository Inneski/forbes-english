# Pricing go-live — the checklist

Everything for the new pricing (Innes's handoff of 3 Oct 2026, steps 1–9) is
on branch **`pricing-go-live`** (worktree `../FORBES-pricing`). Nothing in it
is live until the branch is merged into `main` and pushed. The database and
Stripe parts are already done and do nothing until the new Worker is live.

## A. Before go-live (Innes)

1. **Privacy notice and terms page.** Both need the seller's name and
   address. The privacy notice must exist before `RESEND_API_KEY` is set (it
   names Supabase, Stripe, Cloudflare and Resend as processors, and US
   transfers); the terms page should carry the 14-day withdrawal information
   for digital content bought by EU consumers. Link both from
   `pricing.html`'s price note and from Stripe's Checkout settings.
2. **Resend.** Account, domain `forbesenglish.com` verified (DNS records at
   the names Resend gives; leave the root MX/SPF alone), API key added as the
   Worker **secret** `RESEND_API_KEY`, one test email sent and received.
   Steps: `deploy/06-environment-variables.md`.
3. **Marking products and Managed Payments.** Ask Stripe support whether
   "IELTS essays marked by a teacher, with written feedback" is eligible.
   If not, set `managed: false` for `ielts_marking` and `marking` in
   `CHECKOUT_PRODUCTS` (`src/index.js`).
4. **Quests for Missions 4, 8 and 12** (Present Continuous 1b, Past
   Continuous 1b, Future Simple 1b): built, published, and tagged
   (`update public.lessons set term = 1, mission = 4 where file = '…';`).
   The first buyer reaches Mission 4 on day 21.

Already done: Stripe products, prices, metadata and the `FOUNDER` code
(IDs in `docs/HANDOFF.md`); webhook endpoint with all six events; Managed
Payments on; schema (steps 1 and 9, both applied); Term 1/Term 2 tagging.

## B. Go-live, in one sitting

1. In `../FORBES-pricing`: `git merge main` (main moves every day), then run
   every test:
   ```bash
   node deploy/test-paywall.mjs
   node deploy/test-webhook.mjs
   node deploy/test-weekly.mjs
   node deploy/test-ranges.mjs
   ```
   and, with Playwright, `node deploy/test-account.cjs`. All must pass.
2. **Supabase SQL editor:** run the exemption block at the end of
   `deploy/schema-pricing.sql` ("current subscribers keep every Block Camp
   mission"). Expect one row per current subscriber (2 on 4 Oct).
3. In the main checkout: `git merge --no-ff pricing-go-live` (one merge commit, so step D can revert the whole release at once).
4. Regenerate what the builders own, then check:
   ```bash
   py tools/build_hubs.py
   py tools/seo.py
   py lesson-template/checker/check-access.py
   node lesson-template/check-library.js --vs-origin
   ```
   `build_hubs.py` rebuilds `rpg.html` with the new copy; `seo.py` writes
   `llms.txt`, `lesson-meta.json` (Grand Hotel's track) and the pricing
   page's description. Commit the regenerated files by name with the merge.
5. `git push`. The Worker and the pages go live within minutes.

## C. Check it is live

- `https://forbesenglish.com/api/paywall-status` →
  `configOk: true`, `blockCampDripReady: true`, `term1Missions: [1…12]`,
  `mission1Free: true`, `hasBlockCampPrice / hasIeltsPrice /
  hasIeltsMarkingPrice / hasMarkingPrice / hasFounderPromo: true`,
  `hasMissionEmail` and `hasMarkingMail` true once Resend is set.
- `https://forbesenglish.com/api/founder-status` → `{"limit":50,"remaining":50}`.
- `pricing.html` shows "Founder price … 50 of 50 left" and €12.
- A Pro lesson in a private window → the gate page, labelled with its plan.
- **One real purchase**, on an account that is not the owner's (the owner
  sees everything): Block Camp Term 1 with the founder price. Then:
  Stripe → the webhook delivery is 200; the account page shows "Week 1 of
  12" and Mission 1 open; Mission 2 shows "Mission 2 opens on …". Refund it
  in Stripe and reload: the access is gone (that tests `charge.refunded`).
  The test uses one founder place (49 left; a refund does not give it back).
- Cloudflare → the Worker → Logs: one `mission emails: {…}` line an hour.

## D. If it goes wrong

`git revert -m 1 <merge commit>` on main and push: the old Worker and pages
come back. The database changes are additive and harmless to the old
Worker; the Stripe products can stay. A purchase made in between keeps its
`user_plans` row and is honoured again when the new Worker returns.

## E. After

`git worktree remove ../FORBES-pricing` and `git branch -d pricing-go-live`
once merged. Follow-ups noted in `docs/HANDOFF.md`: the Lookout's padlocks
for Term 1 buyers (`camp-flags.js` needs each entry's term), an essay upload
that spends a credit itself, `library.html`'s IELTS banner ("fourteen
lessons", now 28).
