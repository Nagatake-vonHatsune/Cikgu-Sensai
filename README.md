# Cikgu, Sensai! worksheet library
Open dist/index.html in a browser. The site works offline. Selections exist only in memory. No remote fonts, accounts, cookies, analytics or runtime services.
## Deploy
Push the project to GitHub. Connect the repository to a Cloudflare Worker on your Free plan. Leave the build command empty and set the deploy command to npx wrangler deploy. The static asset directory is dist.
## Add lessons
Edit build.py and run python build.py with PyMuPDF, fontTools and Noto Sans CJK installed (font path in script). Commit the regenerated dist/bank.js. Every PDF page is checked for overflow at full size.

The curriculum/ directory contains scenario families for A1 through C1 in Malay, English and Japanese. Each family makes three independent packs. Edit the matching guided dialogue when changing a scenario. The optional transfer page introduces a change of plan after independent practice. Labels are teaching targets. No learner records are stored.
