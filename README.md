# Docket Planner

A task manager built for iPad, styled like a navy spreadsheet dashboard.

- **Dashboard**: open, due-today and overdue counts, a monthly "added vs completed" chart, the current week, a focus list, progress by category, and routine progress rings.
- **Tasks**: quick add, filters (Today, Upcoming, No date, All open, Done), search, categories, priorities P1–P3, due dates, notes.
- **Board**: To do / In progress / Done columns.
- **Routines**: a monthly tracker grid with a daily progress row, goals, perfect days and check-in totals.
- Light and dark themes.

## Files

- `src/docket.html` is the app source. It is published as-is as a Claude artifact, where data syncs to your Claude account.
- `docs/` is the installable home-screen version built from it (`python3 scripts/build.py`). This version saves data on the device in browser storage.

## Install on iPad (home-screen version)

1. Turn on GitHub Pages for this repo (Settings → Pages → branch, folder `/docs`).
2. Open the Pages URL in Safari on the iPad.
3. Tap Share → **Add to Home Screen**. Docket opens full-screen like an app.
