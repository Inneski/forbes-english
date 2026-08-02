# Step 3 — Point forbesenglish.com at Cloudflare

Cloudflare's recommended path is to move the domain's **nameservers** to Cloudflare (not just add a couple of DNS records) — this also gets you free HTTPS, DDoS protection, and fast global CDN caching automatically.

## In Cloudflare

1. Dashboard → **Add a site** → type `forbesenglish.com` → choose the **Free** plan
2. Cloudflare scans your existing DNS records and shows you a summary — just continue
3. Cloudflare gives you **two nameservers**, something like:
   ```
   ada.ns.cloudflare.com
   milo.ns.cloudflare.com
   ```
   (yours will be different — copy the exact ones shown)

## In Namecheap

1. Log into https://www.namecheap.com → **Domain List** → click **Manage** next to `forbesenglish.com`
2. Find **Nameservers** (near the top of the domain overview page)
3. Change the dropdown from "Namecheap BasicDNS" to **Custom DNS**
4. Paste in the two Cloudflare nameservers from above (one per line)
5. Click the checkmark/save

## Wait for propagation

This can take anywhere from 10 minutes to a few hours. Cloudflare will email you once it detects the switch and activates the domain. You can also check status on the Cloudflare dashboard — it'll show "Active" once done.

## Back in Cloudflare Pages

Once the domain shows **Active** in Cloudflare:

1. Go back to your Pages project → **Custom domains**
2. Add `forbesenglish.com` and `www.forbesenglish.com`
3. Cloudflare will auto-create the DNS records needed since it now controls the domain's DNS — no manual record entry required

That's it — `forbesenglish.com` should resolve to your site with HTTPS automatically issued.

Tell me once the domain shows Active in Cloudflare and we'll sanity-check everything together.
