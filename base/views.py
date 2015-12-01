from django.shortcuts import render, get_object_or_404
from models import Paper
from .forms import PaperForm, DateForm

def paper_detail(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    return render(request, 'base/paper_detail.html', {'paper': paper})

def get_title(request):
    data = request.GET
    paperform = PaperForm(request.GET)
    dateform = DateForm(request.GET)
    filtered = False

    papers = Paper.objects.all()

    # figure out date_start and date_end from database
    dates = [paper.date for paper in papers if isinstance(paper.date, int)]
    date_min = min(dates)
    date_max = max(dates)

    if 'title' in data and len(data['title']) > 0:
        papers = papers.filter(title__icontains=data['title'])
        filtered = True

    if 'author' in data and len(data['author']) > 0:
        papers = papers.filter(author__icontains=data['author'])
        filtered = True

    if 'journal' in data and len(data['journal']) > 0:
        papers = papers.filter(journal__name__icontains=data['journal'])
        filtered = True

    # start_date and end_date will always be populated
    # but check to see if start and end are the same to determine filtered status
    if 'date_start' in data and len(data['date_start']) > 0:
        # should this be deleted? if so, ALL papers will show on page load
        # but what if someone wants to filter on all dates? maybe look at url..?
        if data['date_start'] != date_min or data['date_end'] != date_max:
            papers = papers.filter(date__gte=data['date_start'])
            papers = papers.filter(date__lte=data['date_end'])
            filtered = True

    # somehow set slider vals (if filtered is false, set as max/min)
    if filtered:
        return render(request, 'base/search.html', {'paperform': paperform, 'dateform': dateform, 'papers': papers})
    else:
        return render(request, 'base/search.html', {'paperform': paperform, 'dateform': dateform})

