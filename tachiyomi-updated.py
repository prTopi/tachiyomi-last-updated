#!/usr/bin/env python
from argparse import ArgumentParser
from sqlite3 import connect
from datetime import date, timedelta

ap = ArgumentParser(description="Reads Tachiyomi database and lists all "
                    "series which haven't been updated in specified time.")
ap.add_argument("-y", "--years", type=int, default=0, help="Number of years")
ap.add_argument("-m", "--months", type=int, default=0, help="Number of months")
ap.add_argument("-d", "--days", type=int, default=0, help="Number of days")
args = ap.parse_args()
with connect("tachiyomi.db") as db:
    c = db.cursor()
    manga = dict(c.execute("SELECT _id, title FROM mangas WHERE favorite=1")
                  .fetchall())
    print("You have a total of {0} manga!\n".format(len(manga)))
    chaps = c.execute("SELECT manga_id, date_upload FROM chapters WHERE "
                      "manga_id IN ({0})".format(','.join('?' for _ in manga)),
                      list(manga))
    chapterTimes = {x: 0 for x in manga}
    for line in chaps:
        mangaId, value = line
        if chapterTimes[mangaId] < value:
            chapterTimes[mangaId] = value
    days = int(args.years) * 365 + int(args.months) * 30.417 + int(args.days)
    lastDate = date.today() - timedelta(days=days)
    for x in chapterTimes:
        value = str(chapterTimes[x])
        if len(value) > 3:
            time = date.fromtimestamp(int(value[:-3]))
            if time < lastDate:
                print(">", manga[x])
