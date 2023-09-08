# forms.py
from django import forms

class BlogSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
