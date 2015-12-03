import django
import csv
import sys
import os
import re

sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'papers_site.settings'
from base.models import Paper, Keyword, Journal
django.setup()

with open('papers.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(csvreader):
        print i

#         if i > 1:
            # sys.exit()

        # skipkheader
        if i == 0:
            continue

        # authors
        author = row[0]

        # date
        date = row[1].strip('.')
        date = date.strip('?')
        bad_things = [
            '-.*',
            ' .*',
            ',.*',
            '\..*',
        ]

        for bad in bad_things:
            date = re.sub(bad, '', date)

        try:
            int(date)
        except:
            date = None

        # title
        title = row[2].strip('.')
        title = re.sub('\^([^^]*)\^', r'<i>\1</i>', title)

        # journal
        try:
            journal = Journal.objects.get(orig_id = int(row[4]))
        except:
            journal = None
            print row[4]

        # volume
        volume = row[5]

        # page start
        page_start = row[6]

        # page end
        page_end = row[7]

        # reprint
        try:
            reprint = bool(row[10])
        except:
            reprint = False

        # pdf
        try:
            pdf = bool(row[12])
        except:
            pdf = False

        paper = Paper(author=author,
                      date=date,
                      title=title,
                      journal=journal,
                      volume = volume,
                      page_start=page_start,
                      page_end=page_end,
                      reprint=reprint,
                      pdf=pdf)
        paper.save()

        # keywords
        kwords = [x.strip() for x in row[8].split(',')]
        for kword in kwords:
            obj, created = Keyword.objects.get_or_create(keyword=kword)
            paper.keywords.add(obj)
