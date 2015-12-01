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

    if 'title' in data and len(data['title']) > 0:
        papers = papers.filter(title__icontains=data['title'])
        filtered = True

    if 'author' in data and len(data['author']) > 0:
        papers = papers.filter(author__icontains=data['author'])
        filtered = True

    if 'journal' in data and len(data['journal']) > 0:
        papers = papers.filter(journal__name__icontains=data['journal'])
        filtered = True

    # if 'year_start' in data and len(data['year_start']) > 0:
        # papers = papers.filter(title__icontains=data['title'])

    if filtered:
        return render(request, 'base/search.html', {'paperform': paperform, 'dateform': dateform, 'papers': papers})
    else:
        return render(request, 'base/search.html', {'paperform': paperform, 'dateform': dateform})

