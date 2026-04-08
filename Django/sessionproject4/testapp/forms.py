from django import forms
class Additemform(forms.Form):
    itemname=forms.CharField(max_length=30)
    quantity=forms.IntegerField()