from django import forms
class Nameform(forms.Form):
    name=forms.CharField(max_length=30)
class Ageform(forms.Form):
    age=forms.IntegerField()
class Gfform(forms.Form):
    Gfname=forms.CharField(max_length=30)
