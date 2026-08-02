# Step 4 — Supabase (auth + subscriber data)

## Create the project

1. Go to https://supabase.com → sign up / log in
2. **New project** → name it `forbes-english`, set a database password (save it somewhere), pick a region close to your users
3. Wait ~2 minutes for provisioning

## Run the schema

1. In the Supabase dashboard, go to **SQL Editor** → **New query**
2. Paste in the contents of `deploy/schema.sql` (in this same folder)
3. Click **Run**

This creates a `profiles` table that tracks, per logged-in user, whether they have an active subscription — kept in sync automatically by the Stripe webhook (Step 5).

## Get your API keys

1. **Project Settings** (gear icon) → **API**
2. Copy:
   - **Project URL** (looks like `https://xxxxx.supabase.co`)
   - **anon public** key (safe to use in browser-side code)
   - **service_role** key (⚠️ secret — server-side only, never put this in any HTML/JS the browser loads)

You'll need these in Step 6 when wiring the site's login and the Cloudflare Function environment variables.

## Enable email login

1. **Authentication** → **Providers** → make sure **Email** is enabled (it is by default)
2. **Authentication** → **URL Configuration** → set **Site URL** to `https://forbesenglish.com` once the domain is live (use the `.pages.dev` URL for now if the domain isn't ready yet)

Tell me once you have your Project URL + anon key + service_role key and we'll move to Stripe.
