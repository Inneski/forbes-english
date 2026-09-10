# vendor/

Third-party browser libraries served from our own origin.

## `supabase-js-2.116.0.min.js`

The UMD build of `@supabase/supabase-js`, byte-identical to what
`https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2` serves.

**Why it is here rather than on the CDN.** Sign-in, the lesson library, the
pricing page and the gate page all fall over completely if this one file
fails to load — the pages render a spinner and nothing else. On a phone that
is not a rare event: content blockers, in-app browsers (Instagram, WhatsApp,
Gmail), school and office Wi-Fi filters and some national networks all block
`cdn.jsdelivr.net` while leaving the site itself reachable. Served from our
own origin the file cannot be blocked separately from the pages that need it,
it costs no extra DNS lookup or TLS handshake on a cold mobile connection,
and Cloudflare serves it from the same edge as everything else.

**It also pins the version.** The old tag was `@2` — a floating major, so the
site silently ran whatever the newest v2 was on any given morning.

### Updating it

```bash
npm pack @supabase/supabase-js@2
tar xzf supabase-supabase-js-*.tgz package/dist/umd/supabase.js
mv package/dist/umd/supabase.js vendor/supabase-js-<version>.min.js
```

Then point the four `<script>` tags at the new filename — `account.html`,
`library.html`, `pricing.html`, `locked.html` — and delete the old file. The
version is in the name so a new one cannot be served from a stale cache.
