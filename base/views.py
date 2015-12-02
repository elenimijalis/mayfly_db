from django.shortcuts import render, get_object_or_404
from models import Paper
from .forms import PaperForm, DateForm

def paper_detail(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    return render(request, 'base/paper_detail.html', {'paper': paper})

def get_title(request):
    papers = Paper.objects.all()

    # figure out date_start and date_end from database
    dates = [paper.date for paper in papers if isinstance(paper.date, int)]
    date_min = min(dates)
    date_max = max(dates)

    data = request.GET
    paperform = PaperForm(request.GET)
    if 'date_start' not in data:
        dateform = DateForm(initial={'date_start': 1800, 'date_end': 2015})
    else:
        dateform = DateForm(request.GET)

    if 'title' in data and len(data['title']) > 0:
        papers = papers.filter(title__icontains=data['title'])

    if 'author' in data and len(data['author']) > 0:
        papers = papers.filter(author__icontains=data['author'])

    if 'journal' in data and len(data['journal']) > 0:
        papers = papers.filter(journal__name__icontains=data['journal'])

    # start_date and end_date will always be populated
    if 'date_start' in data and len(data['date_start']) > 0:
        papers = papers.filter(date__gte=data['date_start'])
        papers = papers.filter(date__lte=data['date_end'])

    # try to base this on if base url
    return render(request, 'base/search.html', {'paperform': paperform, 'dateform': dateform, 'papers': papers})

