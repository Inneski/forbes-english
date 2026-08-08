# Step 5 — Stripe (subscriptions)

Stripe Checkout is a page Stripe hosts for you — the site never touches card numbers, so there's no PCI compliance work on your end.

## Create the product

1. Go to https://dashboard.stripe.com/register → sign up
2. Once in, make sure you're in **Test mode** (toggle top-right) while we build this — switch to live mode only when ready to charge real cards
3. **Product catalog** → **Add product**
   - Name: e.g. "Forbes English Pro"
   - Pricing: **Recurring**, pick monthly/annual and the price
   - Save — note the **Price ID** it generates (looks like `price_1AbC...`)

## Get your API keys

**Developers** → **API keys**:
- **Publishable key** (`pk_test_...`) — safe for browser code
- **Secret key** (`sk_test_...`) — ⚠️ server-side only, goes in Cloudflare environment variables, never in HTML/JS

## Create a webhook

This is how Stripe tells your site "this person just paid" / "this person's subscription was cancelled," so Supabase can be updated.

1. **Developers** → **Webhooks** → **Add endpoint**
2. Endpoint URL: `https://forbesenglish.com/api/stripe-webhook` (use your `.pages.dev` URL if the domain isn't live yet)
3. Events to send — select at minimum:
   - `checkout.session.completed`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
4. Save — copy the **Signing secret** (`whsec_...`), used to verify webhook calls are really from Stripe

## What's already scaffolded

`src/index.js` in this repo is the ready-to-configure Cloudflare Worker script implementing this flow — see `deploy/06-environment-variables.md` for wiring it up with your actual keys.

Tell me once you have: the Price ID, the two Stripe keys, and the webhook signing secret, and we'll finish the wiring.
