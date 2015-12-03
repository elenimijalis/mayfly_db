from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from models import Paper, Journal, Keyword
from .forms import PaperForm, DateForm

def paper_detail(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    return render(request, 'base/paper_detail.html', {'paper': paper})

def get_title(request):
    papers = Paper.objects.all()
    # return render(request, 'base/paper_list.html', {'papers': papers})

    # figure out date_start and date_end from database
    dates = [paper.date for paper in papers if isinstance(paper.date, int)]
    date_min = min(dates)
    date_max = max(dates)


    data = request.GET
    paperform = PaperForm(request.GET)

    if 'date_start' not in data:
        dateform = DateForm(initial={'date_start': date_min, 'date_end': date_max})
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
        papers = papers.filter(Q(date__gte=data['date_start']) | Q(date__isnull=True))
        papers = papers.filter(Q(date__lte=data['date_end'])   | Q(date__isnull=True))

    if 'keyword' in data and len(data['keyword']) > 0:
        papers = papers.filter(keywords__keyword__icontains=data['keyword'])

    return render(request, 'base/search.html', {
        'paperform': paperform,
        'date_min': date_min,
        'date_max': date_max,
        'dateform': dateform,
        'papers': papers})

def journal_list(request):
    journals = Journal.objects.all()
    return render(request, 'base/journal_list.html', {'journals': journals})

def keyword_list(request):
    keywords = Keyword.objects.all()
    return render(request, 'base/keyword_list.html', {'keywords': keywords})

