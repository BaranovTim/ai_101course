# AI 101 Academy 🧠

An interactive AI education platform for the Cayman Islands community.
Django + PostgreSQL backend, Tailwind-styled frontend with React components,
Stripe payments, PDF certificates, and a proactive AI tutor.

## Quick start

```bash
./scripts/start.sh
```

Then open **http://127.0.0.1:8000** — admin at **/admin/** (user `admin` / `admin12345` — change this!).

The script starts the bundled PostgreSQL server (if not already running) and the
Django dev server. Stop the database later with `./scripts/stop_db.sh`.

## How it works for learners

- Sign up and pick a **track** (accounting, hospitality, banking, …) — courses
  matching the track are recommended first.
- **The first lesson of every course is free** (including its quiz and the AI tutor).
  From lesson two onward the course must be purchased ("Pro").
- One-time payment per course via Stripe. **Verified students** (upload a student
  ID in Settings, admin approves) automatically get the course's student price.
- Progress tracking, interactive quizzes, a proactive AI assistant that pops up
  to help after wrong quiz answers, and a professional PDF certificate on completion.

## Creating courses (admin guide)

Everything is authored in the Django admin — no code needed:

1. **/admin/ → Courses → Add Course** — title, tagline, track, price
   (in cents: `10000` = $100), optional student price, publish.
   Add modules inline on the same page.
2. **Open a Module → add Lessons inline** — order, title, type, duration.
   Open a lesson to add the body (**Content**, HTML supported with the
   `prompt-box` / `callout` styled classes), an optional **image**, optional
   **instructions** (highlighted step-by-step box), an optional video URL,
   and an optional exercise prompt.
3. **Quizzes → Add Quiz** — pick the lesson and pass mark, add questions inline,
   then open each question to add its answer choices (tick the correct one).
   The explanation field is shown to learners after answering — the AI assistant
   also uses it when it offers help.
4. Publish the course — the first lesson is automatically the free preview.

**Student verification:** /admin/ → Profiles → filter by "Verification pending" →
preview the uploaded ID → select rows → action **"Approve student verification"**.

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
static/js/       React quiz player, tutor chat, proactive assistant widget
media/           uploaded lesson images, avatars, student IDs (gitignored)
pgdata/          PostgreSQL data directory (gitignored)
```

## Tech stack

Python 3.9 · Django 4.2 LTS · PostgreSQL 16 (pgserver) · Tailwind CSS (CDN) ·
React 18 (CDN, no build step) · Stripe · ReportLab · Pillow · Anthropic API
