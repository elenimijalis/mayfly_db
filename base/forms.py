from django import forms

class PaperForm(forms.Form):
    title = forms.CharField(label='Title', required=False)
    author = forms.CharField(label='Author', required=False)
    journal = forms.CharField(label='Journal', required=False)

class DateForm(forms.Form):
    date_start = forms.IntegerField(label='Start', required=False)
    date_end = forms.IntegerField(label='End', required=False)
