from django import forms

class PaperForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)
    journal = forms.CharField(required=False)
    keyword = forms.CharField(required=False)

class DateForm(forms.Form):
    date_start = forms.IntegerField(label='Start', required=False)
    date_end = forms.IntegerField(label='End', required=False)
