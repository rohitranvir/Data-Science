from django import forms
from testapp.models import Movie
class Moviesform(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"