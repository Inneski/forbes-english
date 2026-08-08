# Deploying Forbes English to forbesenglish.com

Follow these in order. Each one is a self-contained step — stop after any of them and pick back up later.

1. [`01-github.md`](01-github.md) — push this repo to GitHub
2. [`02-cloudflare-pages.md`](02-cloudflare-pages.md) — deploy the static site
3. [`03-namecheap-dns.md`](03-namecheap-dns.md) — point forbesenglish.com at it

At this point the site is **live** on your domain. Steps 4–6 add the subscription/paywall layer on top, whenever you're ready:

4. [`04-supabase-setup.md`](04-supabase-setup.md) — database + login (run [`schema.sql`](schema.sql))
5. [`05-stripe-setup.md`](05-stripe-setup.md) — subscription product + webhook
6. [`06-environment-variables.md`](06-environment-variables.md) — wire the two together

The actual server-side code for checkout + webhook already exists in [`src/index.js`](../src/index.js) at the repo root — it's a Cloudflare Worker script that handles `/api/create-checkout-session` and `/api/stripe-webhook` directly and falls through to static file serving for everything else. No extra setup beyond the environment variables in step 6.

What's *not* done yet, on purpose — these need your input on UX before I build them:
- The actual login/signup UI on the site
- Which lessons (if any) sit behind the paywall vs. staying free
- The account/subscribe page users land on

We'll design those together once the infrastructure above is live and tested.
