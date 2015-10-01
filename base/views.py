from django.shortcuts import render
from .models import Paper, Journal

def paper_list(request):
    papers = Paper.objects.all()
    return render(request, 'base/paper_list.html', {'papers': papers})
