from django.shortcuts import render
from models import Paper
from .forms import PaperForm

def get_title(request):
    data = request.GET
    form = PaperForm(request.GET)

    papers = Paper.objects.all()

    if 'title' in data and len(data['title']) > 0:
        papers = papers.filter(title__icontains=data['title'])
    else:
        return render(request, 'base/search.html', {'form': form})

    if 'author' in data and len(data['author']) > 0:
        papers = papers.filter(author__icontains=data['author'])

    if 'journal' in data and len(data['journal']) > 0:
        papers = papers.filter(journal__name__icontains=data['journal'])

    # if 'year_start' in data and len(data['year_start']) > 0:
        # papers = papers.filter(title__icontains=data['title'])

    return render(request, 'base/search.html', {'form': form, 'papers': papers})
