from django import forms
from django.core import validators
# def start_with_S(value):
#     if value[0].lower()!='s':
#         raise forms.ValidationError("Name should be start with s or S")
# def gmail_val(val):
#     if val[-10]!='@gmail.com':
#         raise forms.ValidationError("Mail extension should be gmail")
class Feedback(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_Data=super().clean()
        inpname=cleaned_Data['name']
        inpemail = cleaned_Data['email']
        inpfeed = cleaned_Data['feedback']
        rol = cleaned_Data['rollno']
        if inpname[0].lower()!= 's':
            self.add_error("name","Name should be start with S or s")
        if not inpemail.endswith('@gmail.com'):
            self.add_error("email","Email should be Ends with @gmail.com ")
        if len(inpfeed)<5:
            self.add_error("feedback","Feed back length must be grether that 5")
        if rol ==0 or rol<0:
            self.add_error("rollno","Roll Number should be greather than 0")

    # def clean_name(self):
    #     nam=self.cleaned_data["name"]
    #     if len(nam)<4:
    #         raise forms.ValidationError("Name length can not be less that 4")
    #     return nam
    # def name_rollno(self):
    #     rol=self.cleaned_data["rollno"]
    #     if rol<=0:
    #         raise forms.ValidationError("roll NUmber can not be less than 1")
    #     return rol
    # def name_email(self):
    #     eml=self.cleaned_data["email"]
    #     # if rol<=0:
    #     #     raise forms.ValidationError("roll NUmber can not be less than 1")
    #     return eml
    # def name_rollno(self):
    #     feed=self.cleaned_data["rollno"]
    #     # if rol<=0:
    #     #     raise forms.ValidationError("roll NUmber can not be less than 1")
    #     return feed