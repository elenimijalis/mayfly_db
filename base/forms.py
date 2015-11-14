from django import forms

class PaperForm(forms.Form):
    title = forms.CharField(label='Title', required=False)
    author = forms.CharField(label='Author', required=False)
    journal = forms.CharField(label='Journal', required=False)
    year_start = forms.IntegerField(label='', required=False)
    year_end = forms.IntegerField(label='', required=False)
