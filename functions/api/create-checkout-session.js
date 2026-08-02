// Cloudflare Pages Function — POST /api/create-checkout-session
//
// Called from the site's "Subscribe" button. Creates a Stripe Checkout
// session for the logged-in user and returns the URL to redirect them to.
//
// Required environment variables (set in Cloudflare Pages → Settings →
// Environment variables — see deploy/06-environment-variables.md):
//   STRIPE_SECRET_KEY   e.g. sk_test_...
//   STRIPE_PRICE_ID     e.g. price_1AbC...
//   SITE_URL            e.g. https://forbesenglish.com

export async function onRequestPost(context) {
  const { request, env } = context;

  let body;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ error: "Invalid JSON body" }), { status: 400 });
  }

  const { userId, userEmail } = body;
  if (!userId || !userEmail) {
    return new Response(JSON.stringify({ error: "userId and userEmail are required" }), { status: 400 });
  }

  const params = new URLSearchParams({
    mode: "subscription",
    "line_items[0][price]": env.STRIPE_PRICE_ID,
    "line_items[0][quantity]": "1",
    customer_email: userEmail,
    "metadata[supabase_user_id]": userId,
    success_url: `${env.SITE_URL}/account.html?checkout=success`,
    cancel_url: `${env.SITE_URL}/account.html?checkout=cancelled`,
  });

  const stripeRes = await fetch("https://api.stripe.com/v1/checkout/sessions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: params,
  });

  if (!stripeRes.ok) {
    const errText = await stripeRes.text();
    return new Response(JSON.stringify({ error: "Stripe error", detail: errText }), { status: 502 });
  }

  const session = await stripeRes.json();
  return new Response(JSON.stringify({ url: session.url }), {
    headers: { "Content-Type": "application/json" },
  });
}
