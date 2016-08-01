# World of Water Parks

- This calls the YouTube API by searching for a given search term PLUS the names of countries. It is the result of a couple hours of fooling around.

- It's a Python3.5 app, uses Flask, and next I want to cache the results of the queries in a SQLite3 database. Search doesn't work, it's all hardcoded.

- You need to plug your YouTube API key into config.py, copied from config_template.py

- No docs or comments yet.

- The only search, "water parks," is hard-coded and it currently only searches for 20 countries. The full country list is ridiculous and it seems to take 3-5 minutes to load the page since it has to hit the YouTube API nearly 200 times.

- Whoot.

