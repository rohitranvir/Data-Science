from django import forms

from testapp.models import student


class Studentform(forms.ModelForm):
    name=forms.CharField()
    marks=forms.IntegerField()
    class Meta:
        model=student
        fields='__all__'