#!/bin/env python3
from argparse import ArgumentParser
from sqlite3 import connect
from datetime import date, timedelta

parser = ArgumentParser(description='Reads Tachiyomi database and lists '
                        'all series which haven\'t been updated in '
                        'specified time.')
parser.add_argument('-y', '--years', type=int, help='Number of years.',
                    default=0)
parser.add_argument('-m', '--months', type=int, help='Number of months.',
                    default=0)
parser.add_argument('-d', '--days', type=int, help='Number of days.',
                    default=0)
args = parser.parse_args()
with connect('tachiyomi.db') as db:
    c = db.cursor()
    mangas = dict(c.execute("SELECT _id, title FROM mangas WHERE favorite=1")
                  .fetchall())
    print(f'You have a total of {len(mangas)} mango!\n')
    chapters = c.execute('SELECT manga_id, date_upload FROM chapters WHERE '
                         f'manga_id IN ({",".join("?" for _ in mangas)})',
                         list(mangas))
    chapterTimes = {x: 0 for x in mangas}
    for line in chapters:
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
                print(f'> {mangas[x]}')
