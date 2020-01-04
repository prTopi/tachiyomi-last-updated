# tachiyomi-last-updated
Reads Tachiyomi database and lists all series which haven't been updated in specified time.


### Usage
Needs root (ADB may work, untested.)
Copy tachiyomi.db from `/data/data/eu.kanade.tachiyomi/databases` to working directory.
If using tachiyomi dev version, copy from `/data/data/eu.kanade.tachiyomi.debug/databases` instead.

`usage: tachiyomi-updated.py [-h] [-y YEARS] [-m MONTHS] [-w WEEKS] [-d DAYS]`

Should support most common Python versions:
- Python 3: Every version should work, 3.6+ tested
- Python 2 (EOL): Needs 2.7
