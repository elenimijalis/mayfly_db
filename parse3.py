import django
import sys
import os
import glob

sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'papers_site.settings'
from base.models import Paper, Keyword, Journal
django.setup()

for pdf in glob.glob("media/*.pdf"):
    pdf = pdf.lstrip("media/")
    pdf = pdf.rstrip(".pdf")
    print pdf
    try:
        paper = Paper.objects.get(lookup=pdf)
        pdf = "./" + pdf + ".pdf"
        paper.pdf = pdf
        paper.save()
    except:
        print pdf
