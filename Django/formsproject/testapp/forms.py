from django import forms
class StudentForms(forms.Form):
    rollno = forms.IntegerField()
    name=forms.CharField()
    marks=forms.IntegerField()
