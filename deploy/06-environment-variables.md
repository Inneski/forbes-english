# Step 6 — Wire the environment variables

The Worker script needs secrets to talk to Stripe and Supabase. These get set in Cloudflare, never committed to the repo.

## In Cloudflare Pages

Your Pages project → **Settings** → **Environment variables** → add each of these for the **Production** environment (and Preview too, if you want the same behaviour on preview deploys):

| Variable | Value | Where it came from |
|---|---|---|
| `STRIPE_SECRET_KEY` | `sk_test_...` | Stripe → Developers → API keys |
| `STRIPE_PRICE_ID_MONTHLY` | `price_...` | Stripe → Forbes English Pro → the monthly price |
| `STRIPE_PRICE_ID_SEMIANNUAL` | `price_...` | Stripe → Forbes English Pro → the six-month price |
| `STRIPE_PRICE_ID_ANNUAL` | `price_...` | Stripe → Forbes English Pro → the annual price |
| `STRIPE_WEBHOOK_SECRET` | `whsec_...` | Stripe → Developers → Webhooks → your endpoint |
| `SITE_URL` | `https://forbesenglish.com` | — |
| `SUPABASE_URL` | `https://xxxxx.supabase.co` | Supabase → Settings → API |
| `SUPABASE_SERVICE_ROLE_KEY` | `eyJ...` (long string) | Supabase → Settings → API — ⚠️ the **service_role** key, not anon |

The checkout function expects the browser to tell it which plan the visitor picked (`"monthly"`, `"semiannual"`, or `"annual"`) — that comes from whichever pricing button they click on the site, once the Subscribe UI is wired up.

After saving, **redeploy** the Pages project (Deployments tab → ⋯ on the latest → Retry deployment) so the functions pick up the new variables.

## In the site's browser-side code

The **anon** Supabase key and **publishable** Stripe key are safe to expose in browser JS (they're designed for that — Supabase's Row Level Security and Stripe's Checkout flow are what actually protect things, not secrecy of these keys). Once you're ready to add login/subscribe buttons to the site, those two values get hardcoded into a small `supabase-client.js` file — I'll write that together with you once you confirm the account details, since it also means deciding which pages get gated and how the login UI should look.

## Testing the webhook before going live

Stripe has a CLI tool (`stripe listen --forward-to localhost:8788/api/stripe-webhook`) for testing webhooks locally, but since this is Cloudflare Functions rather than a local Node server, the simplest test is:

1. Deploy with test-mode keys
2. Stripe dashboard → your webhook → **Send test webhook** → pick `checkout.session.completed`
3. Check Cloudflare Pages → your project → **Functions** logs (or Supabase → Table Editor → `profiles`) to confirm it landed

---

That's the full path from where the repo sits now to a live, subscription-capable `forbesenglish.com`. Steps 1–3 (GitHub → Cloudflare Pages → DNS) get the site *live* on its own; Steps 4–6 (Supabase + Stripe) add the paywall on top whenever you're ready for that part — they don't have to happen in the same sitting.

## The one-off products (pricing go-live, 2026-10-04)

The four price IDs and the FOUNDER promotion code are not secret, so they
live in `wrangler.toml` under `[vars]` beside the full-plan prices:
`STRIPE_PRICE_ID_BLOCKCAMP`, `STRIPE_PRICE_ID_IELTS`,
`STRIPE_PRICE_ID_IELTS_MARKING`, `STRIPE_PRICE_ID_MARKING`,
`STRIPE_PROMO_FOUNDER`. What each purchase grants is read from the Stripe
**product** metadata (`product`, `term`, `marking_credits`), listed in
`docs/HANDOFF.md`. Change a grant there, not in code.

They are sold through **Managed Payments** (Stripe as seller of record: it
charges and remits the VAT and sends the receipts, from Link), per product:
the `managed` flag in `CHECKOUT_PRODUCTS` in `src/index.js`. Stripe's
eligibility rules exclude products that involve human work, which essay
marking does; see docs/HANDOFF.md for the decision on the two marking
products. In the Stripe dashboard:

1. Settings → Managed Payments: on and "Ready to use" (checked 4 Oct 2026).
2. Developers → Webhooks → `forbes-english-worker-live`
   (`we_1UCRVD0R7wvAnqir5hFaGqwg`) must listen to:
   - `checkout.session.completed` and `checkout.session.async_payment_succeeded`
     (a delayed payment method grants on the second, not the first; added
     4 Oct);
   - `customer.subscription.updated` and `customer.subscription.deleted`
     (the full plan);
   - `charge.refunded` and `charge.dispute.closed`: a full refund or a lost
     chargeback closes a one-off grant and clears its essay credits. Nothing
     one-off expires, so without these a refunded buyer keeps everything.

Checkout needs the buyer signed in: the Worker reads the Supabase token from
the Authorization header (pricing.html sends it) or the `fe_at` cookie and
asks Supabase who it is. Nothing in the request body decides the account.

The marking-inbox notice ("essay credits bought") goes through Resend with
the weekly email: see the next section. (Fallback without Resend: a
Cloudflare `[[send_email]]` binding named `MARKING_MAIL` plus
`MARKING_MAIL_FROM` under `[vars]`.)

Tests: `node deploy/test-webhook.mjs` (checkout, founder count, webhook)
and `node deploy/test-paywall.mjs`.

## Email: the weekly "Mission N is open" and the marking inbox (step 9)

Sent through **Resend** (resend.com). Until the key is set, nothing is sent
and nothing else changes; `/api/paywall-status` reports `hasMissionEmail`
and `hasMarkingMail`.

1. Make a Resend account and add the domain **forbesenglish.com**. Resend
   lists DNS records (DKIM, and SPF/MX on a `send` subdomain); add them in
   Cloudflare → forbesenglish.com → DNS at exactly the names Resend shows,
   and wait for Resend to show the domain as verified. **Leave the root MX
   and root SPF records alone**: they are what delivers mail sent *to*
   info@forbesenglish.com today.
2. Create an API key in Resend (sending access is enough).
3. Cloudflare → Workers → forbes-english → Settings → Variables and secrets:
   add `RESEND_API_KEY` as a **secret**. The rest is already in
   `wrangler.toml`: `MAIL_FROM` (info@forbesenglish.com),
   `MAIL_REPLY_TO` and `MARKING_MAIL_TO` (info@forbesenglish.com).
4. Send one real email with the key, from info@forbesenglish.com to your
   own address (Resend's dashboard has a test send), and check it arrives.
   `/api/paywall-status` reporting `hasMissionEmail: true` only says the
   key is *set*, not that sending works.
5. The cron (`[triggers]` in `wrangler.toml`, every hour) deploys with the
   Worker. Cloudflare → the Worker → Settings → Triggers shows it, and the
   Worker's logs (kept by `[observability]`) show one summary line per run:
   `mission emails: {"sent":…,"failed":…,"skipped":…,"deferred":…}`.
   After a reader's Mission 2 comes due there should be a row in
   `blockcamp_mission_emails` with `sent_at` set; a row with `sent_at` empty
   for more than an hour means sending is failing (the log line says why).

Each run stops at `EMAIL_SUBREQUEST_BUDGET` calls (default 40, under the
Workers Free plan's 50); the next hourly run carries on. On the Paid plan,
add `EMAIL_SUBREQUEST_BUDGET = "900"` under `[vars]`.

Who gets the email: every Block Camp reader (Term 1 buyer, or subscriber
with a started clock) whose next mission opened in the last 48 hours; not
Mission 1, not the owner, not anyone with `profiles.blockcamp_emails =
false` (set it by hand when someone replies asking to stop, or uses their
mail app's unsubscribe, which sends a "Stop Block Camp emails" email to
info@forbesenglish.com). Each email is claimed in `blockcamp_mission_emails`
before it is sent and marked sent only when Resend accepts it, so nobody
gets the same mission twice and a failed send is retried. Test:
`node deploy/test-weekly.mjs`.

**Before setting the key:** the site needs a privacy notice that names
Resend (and Supabase, Stripe, Cloudflare) as processors. See
docs/HANDOFF.md.
