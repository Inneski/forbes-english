# Step 2 — Deploy on Cloudflare Pages

## Create a Cloudflare account (if you don't have one)

1. Go to https://dash.cloudflare.com/sign-up
2. Sign up with your email, verify it

## Create the Pages project

1. In the Cloudflare dashboard, go to **Workers & Pages** (left sidebar)
2. Click **Create** → **Pages** → **Connect to Git**
3. Authorize Cloudflare to access your GitHub account, then pick the `forbes-english` repo
4. Build settings:
   - **Framework preset**: None
   - **Build command**: *(leave blank — this is plain static HTML, nothing to build)*
   - **Build output directory**: `/` (the repo root, since `index.html` lives there)
5. Click **Save and Deploy**

Cloudflare will give you a URL like `forbes-english-xyz.pages.dev` within a minute or two — that's your site, live, before the custom domain is even connected.

## What "auto-deploy" means going forward

Every time you `git push` to the `main` branch (from this Claude session or your own terminal), Cloudflare automatically rebuilds and redeploys the site within about a minute. No manual redeploy step needed.

## Connect forbes-english.com

Once the Pages project exists:

1. In the Pages project, go to **Custom domains** → **Set up a custom domain**
2. Enter `forbesenglish.com` and follow the prompts — Cloudflare will detect that the domain isn't on Cloudflare's nameservers yet and walk you through adding it

This links to **Step 3** (Namecheap DNS) — you'll need to do that part in parallel/after.

Once your Pages project is live and you've started the custom domain step, tell me and we'll move to Step 3.
