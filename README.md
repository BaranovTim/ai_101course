# AI 101 Academy 

An interactive AI education platform for the Cayman Islands community.
Django + PostgreSQL backend, Tailwind-styled frontend with React components,
Stripe payments, PDF certificates, and a proactive AI tutor.

## Quick start

> **Setting up on a brand-new computer?** Follow the step-by-step guide in
> **[SETUP.md](SETUP.md)** — it covers installing Python/Git, creating `.env`,
> and initializing the database from scratch.

```bash
./scripts/start.sh
```

Then open **http://127.0.0.1:8000** — admin at **/admin/** (user `admin` / `admin12345` — change this!).

The script starts the bundled PostgreSQL server (if not already running) and the
Django dev server. Stop the database later with `./scripts/stop_db.sh`.

## How it works for learners

- Learners buy **tracks, not individual courses**: the **General track** is the
  base purchase, and career tracks (Accounting, Hospitality, Banking, …) can be
  added on top. One payment unlocks every course in the track — forever,
  including courses added later.
- Sign up and pick a career at signup — the matching career track is recommended
  first on the catalog, pricing page, and dashboard.
- **The first lesson of every course is free** (including its quiz and the AI tutor).
- **Verified students** (upload a student ID in Settings, staff approves)
  automatically get the track's student price.
- Progress tracking, interactive quizzes, a proactive AI assistant that pops up
  to help after wrong quiz answers, and a professional PDF certificate per
  completed course.

## Building courses — the Studio (staff)

Staff members get a **Studio** link in the sidebar (or go to **/studio/**) —
a full course builder inside the site, no Django admin needed:

1. **New Track** — name, audience, price/student price (in cents: `10000` = $100).
   Tracks are what learners buy.
2. **New Course** — assign it to a track, then **Manage Content**.
3. **Add modules and lessons** on the course page. Lessons support an optional
   **image upload**, HTML content (with `prompt-box` / `callout` styled boxes),
   optional **instructions**, a video URL, and an exercise prompt.
4. **Add Quiz** next to any lesson opens the **Quiz Builder** — questions and
   answer choices are edited together on one page: type choices, tick the
   correct one, set the pass mark, save once. (This replaces the clunky
   Django-admin flow where choices lived on a separate page.)
5. Publish — the first lesson of each course is automatically the free preview.

The classic Django admin at **/admin/** still works for everything else
(users, payments, enrollments, student verification).

**Student verification:** /admin/ → Profiles → filter by "Verification pending" →
preview the uploaded ID → select rows → action **"Approve student verification"**.

**Seed content:** `python manage.py seed_course` loads the ready-made
General track with the full "AI 101" course (5 modules, 21 lessons, 61 quiz
questions). Re-running it refreshes that content; it never touches other tracks.

## Database (PostgreSQL + DBeaver)

PostgreSQL runs locally from the pip-installed `pgserver` package, data in `./pgdata`.

| Setting | Value |
|---|---|
| Host | `127.0.0.1` |
| Port | `5432` |
| Database | `ai101db` |
| Username | `ai101` |
| Password | `ai101pass` |

## Keys & configuration (`.env`)

| Variable | Needed for | Where to get it | Without it |
|---|---|---|---|
| `STRIPE_PUBLISHABLE_KEY` + `STRIPE_SECRET_KEY` | Real card payments | dashboard.stripe.com → Developers → API keys | A clearly-labeled local payment **simulator** runs instead |
| `STRIPE_WEBHOOK_SECRET` | Webhook signature verification | `stripe listen --forward-to 127.0.0.1:8000/payments/webhook/` | Payments still verified on the success page |
| `ANTHROPIC_API_KEY` | Live AI tutor & assistant chat | console.anthropic.com | A built-in offline tutor answers instead |

Everything else (database, media uploads, certificates, quizzes, student
verification, avatars) works with **no external keys**.

## Project layout

```
ai101_academy/   Django settings & root urls
accounts/        signup, profile (avatar, student ID), password change
courses/         courses/modules/lessons/quizzes, progress, PDF certificates
payments/        Stripe checkout + webhook + dev simulator, student pricing
tutor/           AI tutor chat (Anthropic claude-opus-4-8 + offline fallback)
templates/       Tailwind pages (Lumina Learning design system)
static/js/       React quiz player, tutor chat, assistant widget, effects.js (animations)
media/           uploaded lesson images, avatars, student IDs (gitignored)
pgdata/          PostgreSQL data directory (gitignored)
```

## Tech stack

Python 3.9 · Django 4.2 LTS · PostgreSQL 16 (pgserver) · Tailwind CSS (CDN) ·
React 18 (CDN, no build step) · Stripe · ReportLab · Pillow · Anthropic API

The frontend ships an animation layer (`static/js/effects.js` + CSS in
`templates/partials/head.html`): particle neural-network hero canvas, scroll-reveal
transitions, count-up stats, a typewriter headline, floating gradient blobs, an
infinite audience marquee, 3D card tilt, animated progress bars, and an animated
"aurora" CTA — all disabled automatically for users with reduced-motion enabled.
