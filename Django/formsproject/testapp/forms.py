from django import forms
class StudentForms(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
