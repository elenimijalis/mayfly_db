# from django.shortcuts import render
from django import forms
from .models import Paper, Journal
from haystack.forms import SearchForm

# how does this relate to
class My_Form(SearchForm):
    start_date = forms.IntegerField(required=False)
    end_date = forms.IntegerField(required=False)
    author = forms.CharField(required=False)
    journal = forms.CharField(required=False)
    title = forms.CharField(required=False)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(My_Form, self).search()

        if not self.is_valid():
            return self.no_query_found()

#         # Check to see if a start_date was chosen.
        # if self.cleaned_data['start_date']:
            # sqs = sqs.filter(pub_date__gte=self.cleaned_data['start_date'])

        # # Check to see if an end_date was chosen.
        # if self.cleaned_data['end_date']:
            # sqs = sqs.filter(pub_date__lte=self.cleaned_data['end_date'])

        return sqs

# def paper_list(request):
    # papers = Paper.objects.all()
    # return render(request, 'base/paper_list.html', {'papers': papers})
