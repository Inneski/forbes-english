-- Funnel count and guest checkout (2026-10-09). APPLIED 2026-10-09 as the
-- Supabase migration `funnel_events_and_guest_checkouts`; kept here so the
-- schema can be read and rebuilt from the repo.
--
-- Why: two campaigns (5-7 Oct) brought 274 visits and no sale, and nothing
-- could say where the visitors stopped. Cloudflare Web Analytics counts
-- visits; the Worker now counts the steps after them (src/index.js, THE
-- FUNNEL). And a buyer no longer needs an account before paying: the
-- purchase finds or makes the account from the email given to Stripe
-- (src/index.js, GUEST CHECKOUT).

-- What happens between an ad and a sale, counted by the Worker. No IP, no
-- account id, no cookie: a row is an event, not a person. RLS on with no
-- policies, so only the service role (the Worker) reads or writes it.
create table if not exists public.funnel_events (
  id bigint generated always as identity primary key,
  at timestamptz not null default now(),
  event text not null check (event in ('landing', 'view', 'checkout', 'paid', 'claim')),
  path text,
  product text,
  outcome text,
  guest boolean,
  ref_host text,
  utm_source text,
  utm_medium text,
  utm_campaign text,
  utm_content text,
  click text,
  country text,
  mobile boolean
);
create index if not exists funnel_events_at on public.funnel_events (at);
alter table public.funnel_events enable row level security;
revoke all on public.funnel_events from anon, authenticated;

-- One row per paid checkout made without signing in: the account it went to,
-- whether the purchase created that account, and whether its one-time
-- sign-in (the success page's) has been used.
create table if not exists public.guest_checkouts (
  session_id text primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  created_account boolean not null,
  created_at timestamptz not null default now(),
  claimed_at timestamptz
);
alter table public.guest_checkouts enable row level security;
revoke all on public.guest_checkouts from anon, authenticated;

-- Per day: how many of each step. security_invoker so RLS applies to anyone
-- but the service role; no grants to anon or authenticated.
create or replace view public.funnel_daily with (security_invoker = true) as
select date_trunc('day', at)::date as day, event,
       coalesce(product, path) as what, outcome, guest,
       utm_source, utm_campaign, count(*) as n
from public.funnel_events
group by 1, 2, 3, 4, 5, 6, 7;
revoke all on public.funnel_daily from anon, authenticated;

-- ── Reading it (Supabase SQL editor) ──────────────────────────────────
-- The last week, step by step:
--   select day, event, what, outcome, utm_campaign, n
--   from funnel_daily where day > now() - interval '7 days'
--   order by day desc, event, n desc;
-- A campaign from click to sale:
--   select event, count(*) from funnel_events
--   where at > now() - interval '7 days' group by event order by 2 desc;
-- Where campaign visitors landed:
--   select path, utm_source, utm_campaign, count(*) from funnel_events
--   where event = 'landing' group by 1, 2, 3 order by 4 desc;
