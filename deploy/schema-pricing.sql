-- Forbes English — pricing go-live (2026-10-03).
--
-- Block Camp Term 1 (€19, 16 weeks, one mission a week), IELTS (€25 / €69
-- with marking, 90 days), Marking add-on (€49). The full plan is unchanged
-- and still lives on `profiles`. Builds on schema-tracks.sql.
--
-- APPLIED 2026-10-03 as Supabase migration `pricing_go_live_schema`.

-- ── Lessons: which term and mission a Block Camp item belongs to ───────
-- A quest carries the same term/mission as its deck. Null = not in a term.
alter table public.lessons
  add column if not exists term    int check (term > 0),
  add column if not exists mission int check (mission > 0);

-- ── user_plans: term, drip start, marking credits ───────────────────────
alter table public.user_plans
  add column if not exists term            int check (term > 0),
  add column if not exists starts_at       timestamptz not null default now(),
  add column if not exists marking_credits int not null default 0
    check (marking_credits >= 0);

-- A marking add-on bought without an IELTS plan is its own row.
alter table public.user_plans drop constraint if exists user_plans_product_check;
alter table public.user_plans add constraint user_plans_product_check
  check (product in ('blockcamp', 'ielts', 'marking'));

-- ── profiles: drip start for full-plan subscribers ──────────────────────
-- Set by the Worker on a subscriber's first Block Camp request.
alter table public.profiles
  add column if not exists blockcamp_first_open timestamptz;

-- ── profiles: browsers may read their own row, never write it ───────────
-- schema.sql shipped "Users can update their own profile" and the default
-- table grants, so any signed-in user could PATCH their own row through
-- the REST API with the anon key and set owner = true or
-- subscription_status = 'active', and with this change backdate
-- blockcamp_first_open. No page writes to profiles; rows are created by
-- handle_new_user() (security definer) and updated by the Stripe webhook
-- with the service role, neither of which these revokes touch.
drop policy if exists "Users can update their own profile" on public.profiles;
revoke insert, update, delete on public.profiles from anon, authenticated;
