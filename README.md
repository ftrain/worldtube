# World of Water Parks

- This calls the YouTube API by searching for a given search term PLUS the names of countries. It is the result of a couple hours of fooling around.

- It may or may not be finished, it's just a sketch.

- It's a Python3.5 app, uses Flask.

- You need to plug your YouTube API key into config.py, copied from config_template.py

- No docs or comments yet.

- Next I want to cache the results of the queries in a SQLite3 database.

- The full country list is ridiculous and it seems to take 3-5 minutes to load the page since it has to hit the YouTube API nearly 200 times.

- It'd be nice to flag a YouTube query as started and done in the DB so that we can show partial results and people can reload as their global search fleshes in.

- Known limits of SQLite3 for anything with multiple users, should probably be Postgres.

- Whoot.
