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

-- ── Step 2: Term 1 / Term 2 tagging (PENDING — Innes to run) ────────────
-- The session's write was refused by the permission layer on 2026-10-03.
-- Term 1: deck first, quest second, mission as numbered in the handoff.
update public.lessons l set term = 1, mission = v.m
from (values
  ('blockcamp-present-simple.html',1),('block-camp/frostbound-river-rpg.html',1),
  ('blockcamp-present-simple-2.html',2),('block-camp/sherlock-blue-hour-rpg.html',2),
  ('blockcamp-present-continuous.html',3),('block-camp/wonderland-stolen-now-rpg.html',3),
  ('blockcamp-present-continuous-2.html',4),
  ('blockcamp-past-simple.html',5),('block-camp/last-bounty-rpg.html',5),
  ('blockcamp-past-simple-2.html',6),('block-camp/fistful-of-lies-rpg.html',6),
  ('blockcamp-past-continuous.html',7),('block-camp/lost-yellow-road-rpg.html',7),
  ('blockcamp-past-continuous-2.html',8),
  ('blockcamp-going-to.html',9),('block-camp/frankenstein-green-prometheus-rpg.html',9),
  ('blockcamp-going-to-2.html',10),('block-camp/frankenstein-consequences-rpg.html',10),
  ('blockcamp-future-simple.html',11),('block-camp/last-train-home-rpg.html',11),
  ('blockcamp-future-simple-2.html',12)
) v(f, m)
where l.file = v.f;                                   -- expect UPDATE 21

-- Term 2: not on sale. The handoff gives no mission numbers, so mission
-- stays null until Term 2 is priced. Past perfect 1b is not built yet.
update public.lessons set term = 2, mission = null
where file in (
  'blockcamp-present-perfect.html','blockcamp-present-perfect-2.html',
  'block-camp/nautilus-black-archive-rpg.html',
  'blockcamp-present-perfect-continuous.html','blockcamp-present-perfect-continuous-2.html',
  'blockcamp-past-perfect.html',
  'block-camp/twenty-thousand-leagues-rpg.html','block-camp/long-way-home-rpg.html',
  'blockcamp-passive-present-simple.html','blockcamp-passive-present-continuous.html',
  'blockcamp-passive-past-simple.html','blockcamp-passive-past-continuous.html',
  'blockcamp-passive-going-to.html','blockcamp-passive-future-simple.html');  -- expect UPDATE 14

-- ── Step 2b: Block Camp adventures get their track (PENDING — Innes) ─────
-- Grand Hotel's row (added 2026-10-04 by another session) went in as
-- 'general': lessons_default_track() only knows the blockcamp-* deck names,
-- not the block-camp/ folder. Under the per-track gate a Term 1 buyer could
-- not open it. Fix the row and the trigger so the next adventure is right.
update public.lessons set track = 'blockcamp'
where file = 'block-camp/grand-hotel-rpg.html';      -- expect UPDATE 1

create or replace function public.lessons_default_track() returns trigger
language plpgsql as $$
begin
  if new.track is null or new.track = 'general' then
    new.track := case
      when new.file like 'blockcamp-%'            then 'blockcamp'
      when new.file like 'block-camp/%'           then 'blockcamp'
      when new.file like 'forbes-english-ielts-%' then 'ielts'
      when new.file like 'sherpa-tensing-%'       then 'sherpa'
      else 'general' end;
  end if;
  return new;
end $$;

-- ── Go-live: current subscribers keep every Block Camp mission ──────────
-- Run in the same sitting as the pricing-go-live Worker deploy, not before.
-- Innes, 2026-10-04: the weekly drip applies to new subscribers; anyone
-- subscribed when the gate goes live is exempt, so nobody who is already
-- paying loses Missions 2-12. Starting their clock 12 weeks back opens all
-- twelve. Two monthly subscribers on 2026-10-04; the owner is exempt anyway.
update public.profiles
set blockcamp_first_open = now() - interval '12 weeks'
where subscription_status in ('active', 'trialing')
  and not owner
  and blockcamp_first_open is null;                   -- expect UPDATE 2
