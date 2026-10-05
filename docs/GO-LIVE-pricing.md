# Pricing go-live — the checklist

Everything for the new pricing (Innes's handoff of 3 Oct 2026, steps 1–9) is
on branch **`pricing-go-live`** (worktree `../FORBES-pricing`). Nothing in it
is live until it is merged into `main` and pushed. The database and Stripe
parts are already done and do nothing until the new Worker is live.

A second branch, **`rollback-guard`**, holds one commit on top of `main`: the
old webhook answers 500 to the one-off sales' events instead of
mis-recording them. It is never live on its own. The release merges it first
(B3), so a revert of the release (D) brings the old webhook back *with* the
guard. Without it, a €49 marking sale reaching the old Worker after a
rollback is written as Pro for life, IELTS gets a 90-day end, and refunds are
lost (measured; see the commit).

## A. Before go-live (Innes)

1. **Privacy notice and terms page.** Both need the seller's name and
   address. The privacy notice must exist before `RESEND_API_KEY` is set (it
   names Supabase, Stripe, Cloudflare and Resend as processors, and US
   transfers); the terms page carries the 14-day withdrawal information for
   digital content bought by EU consumers. Link both from `pricing.html`'s
   price note and from Stripe's Checkout settings. Then:
   - save the terms URL in Stripe (Settings → Business → Public details →
     Terms of service);
   - **then** set the Worker variable `TERMS_URL` to the same URL. Checkout
     then asks every buyer to agree to the terms and to immediate access,
     which ends the 14-day right of withdrawal. In that order: Stripe
     refuses every checkout that asks for consent while it has no terms URL.
2. **Resend.** Account, domain `forbesenglish.com` verified (DNS records at
   the names Resend gives; leave the root MX/SPF alone), API key added as the
   Worker **secret** `RESEND_API_KEY`, one test email sent and received.
   Steps: `deploy/06-environment-variables.md`.
3. **Marking products and Managed Payments.** Ask Stripe support whether
   "IELTS essays marked by a teacher, with written feedback" is eligible.
   If not, set `managed: false` for `ielts_marking` and `marking` in
   `CHECKOUT_PRODUCTS` (`src/index.js`). That makes Innes the seller of
   those sales: Stripe collects **no VAT** on them, and the €69 product
   includes the IELTS lessons (digital content). So it needs a VAT decision
   first: Stripe Tax, or his own registration / OSS. Also reword the receipt
   answer in `pricing.html` ("Who will I see on my receipt…"), which says
   essay marking is sold through Link.
4. **Quests for Missions 4, 8 and 12** (Present Continuous 1b, Past
   Continuous 1b, Future Simple 1b): built, published, and tagged
   (`update public.lessons set term = 1, mission = 4 where file = '…';`).
   The first buyer reaches Mission 4 on day 21.

Already done: Stripe products, prices, metadata and the `FOUNDER` code
(IDs in `docs/HANDOFF.md`); webhook endpoint with all six events; Managed
Payments on; schema (steps 1 and 9, both applied); Term 1/Term 2 tagging.

## B. Go-live, in one sitting

The release is made in a worktree of its own, never in the shared main
checkout: there, a peer's push can publish the merge before the checks have
run, and a file a peer has staged makes git refuse the merge. Inside a
linked worktree the git guard stands down, so plain `git add` and
`git commit` work.

1. **Bring the branch up to date and test it**, in `../FORBES-pricing`:
   ```bash
   git fetch origin
   git merge origin/main
   node deploy/test-paywall.mjs
   node deploy/test-webhook.mjs
   node deploy/test-weekly.mjs
   node deploy/test-ranges.mjs
   ```
   Then the browser test, which needs Playwright. A worktree has no
   `node_modules` of its own, so borrow the main checkout's:
   `NODE_PATH=../FORBES/node_modules node deploy/test-account.cjs` (bash), or
   `$env:NODE_PATH="..\FORBES\node_modules"; node deploy/test-account.cjs`
   (PowerShell). All must pass. If `git merge origin/main` changed
   `src/index.js`, also check that the release still merges cleanly (B3).
2. **Supabase SQL editor:** run the exemption block at the end of
   `deploy/schema-pricing.sql` ("current subscribers keep every Block Camp
   mission"). Expect one row per current subscriber (2 on 5 Oct). If B3–B5
   do not finish in this sitting, run it again when you resume.
3. **Make the release**, starting in the main checkout (`../FORBES`):
   ```bash
   git fetch origin
   git worktree add ../FORBES-release -b release origin/main
   cd ../FORBES-release
   git merge --no-ff rollback-guard -m "Rollback guard for the pricing release"
   git merge --no-ff --no-commit pricing-go-live
   ```
   Both merges must be clean. (`pricing-go-live` already contains
   `rollback-guard`, with its own webhook kept, so `src/index.js` does not
   conflict. If a merge conflicts anyway, stop and resolve it before going
   on.)
4. **Regenerate and check, in `../FORBES-release`, with the merge still open:**
   ```bash
   py tools/build_hubs.py
   py tools/seo.py
   py lesson-template/checker/check-access.py
   node lesson-template/check-library.js --vs-origin
   git status
   ```
   The builders rewrite `rpg.html`, the topic hubs, `library.html`,
   `llms.txt`, `lesson-meta.json`, `sitemap.xml` and `tools/lessons.json`,
   and replace some hashed pictures in `grammar-hub/` and `rpg-hub/` (new
   files in, old ones out). Commit **everything `git status` shows**, not a
   fixed list, as the merge itself, so one revert undoes all of it:
   ```bash
   git add -A
   git commit -m "Pricing go-live: Block Camp Term 1, IELTS, essay marking, Forbes English Pro"
   ```
5. **Push and tidy up:**
   ```bash
   git push origin HEAD:main
   cd ../FORBES
   git worktree remove ../FORBES-release
   git branch -D release
   ```
   If the push is refused because `main` moved, in `../FORBES-release`:
   `git fetch origin && git merge origin/main`, re-run B4's builders, commit,
   push. The Worker and the pages go live within minutes. Note the release
   merge's commit id (the one made in B4) for D.

## C. Check it is live

- `https://forbesenglish.com/api/paywall-status` →
  `configOk: true`, `blockCampDripReady: true`, `term1Missions: [1…12]`,
  `mission1Free: true`, `hasBlockCampPrice / hasIeltsPrice /
  hasIeltsMarkingPrice / hasMarkingPrice / hasFounderPromo: true`;
  `hasMissionEmail` and `hasMarkingMail` true once Resend is set;
  `hasTermsConsent` true once `TERMS_URL` is set.
- **As soon as `blockCampDripReady` is true: run the exemption block again**
  (B2). It catches anyone who subscribed between B2 and the deploy; rows it
  already set are not touched. Expect `UPDATE 0` unless someone subscribed in
  between.
- `https://forbesenglish.com/api/founder-status` → `{"limit":50,"remaining":50}`.
- `pricing.html` shows "Founder price … 50 of 50 left" and €12.
- A Pro lesson in a private window → the gate page, labelled with its plan.
- **One real purchase**, on an account that is not the owner's (the owner
  sees everything): Block Camp Term 1 with the founder price. Then:
  Stripe → the webhook delivery is 200; the account page shows "Week 1 of
  12", Mission 1 open and the six specials; Mission 2 shows "Opens …".
  Pricing → Buy Term 1 again → "You already have Block Camp Term 1".
  Refund it in Stripe and reload: the access is gone (that tests
  `charge.refunded`). The test uses one founder place (49 left; a refund
  does not give it back).
- Cloudflare → the Worker → Logs: one `mission emails: {…}` line an hour.
- A log line "paid one-off with no supabase_user_id" means a sale not
  started from the site (a Payment Link, a dashboard checkout): find that
  `cs_…` session in Stripe and grant it by hand.

## D. If it goes wrong

Revert the release merge, again in a worktree of its own (a peer's staged
file in the shared checkout makes `git revert` refuse), starting in the main
checkout:

```bash
git fetch origin
git worktree add ../FORBES-rollback -b rollback origin/main
cd ../FORBES-rollback
git revert -m 1 <release merge commit>
git push origin HEAD:main
cd ../FORBES
git worktree remove ../FORBES-rollback
git branch -D rollback
```

The old Worker and pages come back, with the rollback guard: a one-off sale
it receives (a checkout opened before the rollback can still be paid for 24
hours), and any async payment, refund or lost dispute, is answered 500 and
nothing is written, so Stripe holds the event and retries it for three
days. When the release is pushed again, the pricing Worker grants or closes
each of them properly. After re-deploying, run the exemption block again.

If the pricing Worker will not be back within three days: archive the four
one-off prices in Stripe (no new checkouts), and deal with the held events
by hand from Stripe → Developers → Webhooks → the endpoint's failed
deliveries (grant or refund each sale). While the old Worker is live, a
Block Camp row opens every Block Camp lesson (Term 2 too) and Sherpa; that
is harmless and ends when the release returns. The regenerated pages revert
with the merge. Afterwards, check nobody was mis-recorded:
`select id from profiles where subscription_status = 'active' and stripe_subscription_id is null and not owner;`
should return nothing.

## E. After

`git worktree remove ../FORBES-pricing`, `git branch -d pricing-go-live` and
`git branch -d rollback-guard` once released. Follow-ups noted in
`docs/HANDOFF.md`: the Lookout's padlocks for Term 1 buyers (`camp-flags.js`
needs each entry's term), an essay upload that spends a credit itself.
