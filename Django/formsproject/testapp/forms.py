from django import forms
class StudentForms(forms.Form):
    rollno = forms.IntegerField()
    name=forms.CharField()
    marks=forms.IntegerField()

    def clean_name(self):
        nam=self.cleaned_data["name"]
        if len(nam)<4:
            raise forms.ValidationError("Name length must me greater than 3")
        return nam
