-- Forbes English — per-track pricing (2026-09-28).
--
-- Three products instead of one:
--   full       the whole library. This is the existing subscription, still
--              held on `profiles` (plan = monthly | semiannual | annual).
--   blockcamp  Block Camp, a recurring parent subscription.
--   ielts      IELTS, one payment for a fixed term (ends_at).
-- Both standalone products also cover the Sherpa Tensing unit.
--
-- The Worker (src/index.js, TRACK_PRODUCTS) decides what covers what; this
-- file only stores it. Run in the Supabase SQL editor, top to bottom.

-- ── Step 1 (APPLIED 2026-09-28) ─────────────────────────────────────────
-- alter table public.lessons add column track text not null default 'general'
--   check (track in ('general','blockcamp','ielts','sherpa'));
-- update public.lessons set track='blockcamp' where file like 'blockcamp-%';
-- update public.lessons set track='ielts'     where file like 'forbes-english-ielts-%';
-- update public.lessons set track='sherpa'    where file like 'sherpa-tensing-%';

-- ── Step 1b: a new lesson gets its track from its filename ─────────────
-- Without this every new catalogue row defaults to 'general', so a new
-- Block Camp, IELTS or Sherpa deck would need the full plan. An explicit
-- non-general track on insert is kept.
create or replace function public.lessons_default_track() returns trigger
language plpgsql as $$
begin
  if new.track is null or new.track = 'general' then
    new.track := case
      when new.file like 'blockcamp-%'            then 'blockcamp'
      when new.file like 'forbes-english-ielts-%' then 'ielts'
      when new.file like 'sherpa-tensing-%'       then 'sherpa'
      else 'general' end;
  end if;
  return new;
end $$;
drop trigger if exists lessons_default_track on public.lessons;
create trigger lessons_default_track before insert on public.lessons
  for each row execute function public.lessons_default_track();

-- ── Step 2 (APPLIED 2026-09-28): plans a user holds besides the full subscription ────────────
create table if not exists public.user_plans (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  product text not null check (product in ('blockcamp','ielts')),
  status text not null default 'active',          -- Stripe status, or 'active' for a one-off
  stripe_subscription_id text unique,             -- null for a one-off payment
  stripe_checkout_session_id text unique,
  ends_at timestamptz,                            -- IELTS term end; null = open-ended
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists user_plans_user_id on public.user_plans(user_id);

drop trigger if exists user_plans_set_updated_at on public.user_plans;
create trigger user_plans_set_updated_at
  before update on public.user_plans
  for each row execute function public.set_updated_at();

-- Read-your-own only. Writes come from the Stripe webhook with the service
-- role, which bypasses RLS, so there is deliberately no insert/update policy.
alter table public.user_plans enable row level security;
drop policy if exists "Users can view their own plans" on public.user_plans;
create policy "Users can view their own plans"
  on public.user_plans for select
  using (auth.uid() = user_id);

-- Check: should list the new table with rls on, and 0 rows.
select relname, relrowsecurity, (select count(*) from public.user_plans) as rows
from pg_class where relname = 'user_plans';
