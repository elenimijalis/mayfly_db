import csv
import sys
import os

sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'papers_site.settings'
from base.models import Journal

with open('journals.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(csvreader):
        print i
        if i == 0:
            continue
        j_id = int(row[0])
        j_name = row[1]
        j = Journal(name = j_name, orig_id = j_id)
        j.save()
