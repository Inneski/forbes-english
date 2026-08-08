# Step 6 — Wire the environment variables

The two functions in `functions/api/` need secrets to talk to Stripe and Supabase. These get set in Cloudflare, never committed to the repo.

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
