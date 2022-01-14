#Model form for searching

from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
    #Specifying the behaviour for the form
    class Meta:
        model = Search
        #Need to leave trailing commas for list, can be a tuple also
        fields = ['address_location', ]