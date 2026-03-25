from django import forms
class Feedback(forms.Form):
    name=forms.CharField(max_length=60)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)