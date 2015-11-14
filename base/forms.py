from django import forms

class PaperForm(forms.Form):
    title = forms.CharField(label='Title', required=False)
    author = forms.CharField(label='Author', required=False)
    journal = forms.CharField(label='Journal', required=False)
    date = forms.IntegerField(label='Year', required=False)
