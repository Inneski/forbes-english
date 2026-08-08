// Cloudflare Pages Function — POST /api/stripe-webhook
//
// Stripe calls this whenever a subscription event happens. It verifies the
// request really came from Stripe, then writes the subscription state into
// Supabase using the service_role key (server-side only, bypasses RLS).
//
// Required environment variables (see deploy/06-environment-variables.md):
//   STRIPE_WEBHOOK_SECRET   e.g. whsec_...
//   SUPABASE_URL            e.g. https://xxxxx.supabase.co
//   SUPABASE_SERVICE_ROLE_KEY

export async function onRequestPost(context) {
  const { request, env } = context;

  const signature = request.headers.get("stripe-signature");
  const rawBody = await request.text();

  const isValid = await verifyStripeSignature(rawBody, signature, env.STRIPE_WEBHOOK_SECRET);
  if (!isValid) {
    return new Response("Invalid signature", { status: 400 });
  }

  const event = JSON.parse(rawBody);

  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object;
      const userId = session.metadata?.supabase_user_id;
      const plan = session.metadata?.plan;
      if (userId) {
        await updateProfile(env, userId, {
          stripe_customer_id: session.customer,
          stripe_subscription_id: session.subscription,
          subscription_status: "active",
          ...(plan ? { plan } : {}),
        });
      }
      break;
    }
    case "customer.subscription.updated": {
      const sub = event.data.object;
      const plan = sub.metadata?.plan;
      await updateProfileByCustomer(env, sub.customer, {
        subscription_status: sub.status,
        current_period_end: new Date(sub.current_period_end * 1000).toISOString(),
        ...(plan ? { plan } : {}),
      });
      break;
    }
    case "customer.subscription.deleted": {
      const sub = event.data.object;
      await updateProfileByCustomer(env, sub.customer, {
        subscription_status: "canceled",
      });
      break;
    }
    default:
      // Ignore anything we haven't subscribed to.
      break;
  }

  return new Response(JSON.stringify({ received: true }), {
    headers: { "Content-Type": "application/json" },
  });
}

async function updateProfile(env, userId, fields) {
  await fetch(`${env.SUPABASE_URL}/rest/v1/profiles?id=eq.${userId}`, {
    method: "PATCH",
    headers: supabaseHeaders(env),
    body: JSON.stringify(fields),
  });
}

async function updateProfileByCustomer(env, stripeCustomerId, fields) {
  await fetch(`${env.SUPABASE_URL}/rest/v1/profiles?stripe_customer_id=eq.${stripeCustomerId}`, {
    method: "PATCH",
    headers: supabaseHeaders(env),
    body: JSON.stringify(fields),
  });
}

function supabaseHeaders(env) {
  return {
    "apikey": env.SUPABASE_SERVICE_ROLE_KEY,
    "Authorization": `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}`,
    "Content-Type": "application/json",
    "Prefer": "return=minimal",
  };
}

// Verifies the `Stripe-Signature` header using the raw request body, per
// https://stripe.com/docs/webhooks#verify-manually — implemented with the
// Web Crypto API since Cloudflare Functions don't have Node's `crypto`.
async function verifyStripeSignature(rawBody, signatureHeader, webhookSecret) {
  if (!signatureHeader || !webhookSecret) return false;

  const parts = Object.fromEntries(
    signatureHeader.split(",").map((pair) => pair.split("="))
  );
  const timestamp = parts.t;
  const expectedSig = parts.v1;
  if (!timestamp || !expectedSig) return false;

  const signedPayload = `${timestamp}.${rawBody}`;
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(webhookSecret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sigBuffer = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(signedPayload));
  const computedSig = [...new Uint8Array(sigBuffer)]
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");

  return computedSig === expectedSig;
}
