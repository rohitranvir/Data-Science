from django import forms
class Loginform(forms.Form):
    name=forms.CharField(max_length=30)