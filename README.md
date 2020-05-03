# tachiyomi-last-updated
Reads Tachiyomi database and lists all series which haven't been updated in specified time.


### Usage
#### Root method
Simply copy `tachiyomi.db` from `/data/data/eu.kanade.tachiyomi{.debug}/databases` to working directory.

#### ADB run-as method (dev version only)
1. While connected to your device, run `adb shell run-as eu.kanade.tachiyomi.debug cp databases/tachiyomi.db /sdcard`
2. Copy `tachiyomi.db` from your device to working directory.

#### ADB backup method
1. While connected to your device, run `adb backup -noapk eu.kanade.tachiyomi`
2. Follow instructions on terminal on and device screen
3. Now you need to extract the android backup file. I won't go into detail as there are projects which deal with this. Search around.
4. Copy `tachiyomi.db` to working directory.

`usage: tachiyomi-updated.py [-h] [-y YEARS] [-m MONTHS] [-w WEEKS] [-d DAYS]`

Should support most common Python versions:
- Python 3: Every version should work, 3.6+ tested
- Python 2 (EOL): Needs 2.7
