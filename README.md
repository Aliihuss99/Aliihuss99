# Docket Planner

A task manager built for iPad, styled like a navy spreadsheet dashboard.

- **Dashboard**: open, due-today and overdue counts, a monthly "added vs completed" chart, the current week, a focus list, progress by category, and routine progress rings.
- **Tasks**: quick add, filters (Today, Upcoming, No date, All open, Done), search, categories, priorities P1–P3, due dates, notes.
- **Board**: To do / In progress / Done columns.
- **Routines**: a monthly tracker grid with a daily progress row, goals, perfect days and check-in totals.
- Light and dark themes.

## Files

- `src/docket.html` is the app source, written as page content without `<html>`/`<head>`.
- `docs/` is the installable home-screen version built from it (`python3 scripts/build.py`). This version saves data on the device in browser storage.

## Install on iPad

Opening the HTML file from the Files app does not work: iPadOS previews it and throws away anything it saves. Install it from its web address instead.

1. On GitHub open this repo's **Settings → Pages**. Under "Build and deployment" pick **Deploy from a branch**, choose branch `main` and folder `/docs`, then **Save**.
2. After a minute, open **https://aliihuss99.github.io/Aliihuss99/** in Safari on the iPad.
3. Tap Share → **Add to Home Screen**. Always open Docket from that icon.

Data is stored on the iPad inside the home-screen app and works offline. Use **Backup** in the top bar to save a backup file, and **Restore from backup file** to move tasks between devices.
