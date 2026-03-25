from django import forms
class Feedback(forms.Form):
    name=forms.CharField(max_length=60)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    def clean_name(self):
        nam=self.cleaned_data["name"]
        if len(nam)<4:
            raise forms.ValidationError("Name length can not be less that 4")
        return nam