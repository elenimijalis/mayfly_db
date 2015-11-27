from django.shortcuts import render
from models import Paper
from .forms import PaperForm

def get_title(request):
    data = request.GET
    form = PaperForm(request.GET)
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
        return render(request, 'base/search.html', {'form': form, 'papers': papers})
    else:
        return render(request, 'base/search.html', {'form': form})

