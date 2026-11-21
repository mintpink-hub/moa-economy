# Moa Economy ♡

Free static English economics study notebook. No paid APIs, AI, or login.

## Deploy

1. Unzip the archive.
2. Upload **the files inside** `moa-economy` (including hidden `.github` folder) to the **root** of your GitHub repository, replacing old files as needed.
3. In GitHub Settings > Pages, select Deploy from a branch, `main`, `/ (root)`.
4. In Actions, run **Update BBC Business headlines** once via **Run workflow**. Daily cron is best-effort and may be delayed. In repository Settings > Actions > General, ensure workflow permissions allow writing contents if needed.
5. Open your GitHub Pages site. If headlines are unavailable, article paste and studying still work.

## Study

Paste an article and click split. Select consecutive sentence checkboxes and merge; select one and click split, then click a scissors marker between words and apply. Translations and vocabulary are stored in browser localStorage, per date. Back up via JSON export; importing overwrites the current local database.

## Notes

Only BBC RSS titles, snippets and links are published. Full articles are manually pasted for personal study and stored locally in the browser. No full article is uploaded to GitHub. The sentence splitter is heuristic, so abbreviations may require manual editing. When splitting, existing translation and vocabulary remain with the first half for manual adjustment. Records are per browser/device; no automatic sync. Browser popup restrictions may open translation in a tab.
