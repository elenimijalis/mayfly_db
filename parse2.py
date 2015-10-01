import csv
import sys
import os
import re

sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'papers_site.settings'
from base.models import Paper

with open('papers.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(csvreader):
        if i == 0:
            continue
        date = row[1].strip('.')
        date = date.strip('?')
        date = re.sub('-.*','',date)
        date = re.sub(' .*','',date)
        date = re.sub(',.*','',date)
        date = re.sub('\..*','',date)
        try:
            int(date)
        except:
            print date
