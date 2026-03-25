from django.shortcuts import render
from testapp.forms import StudentForms
# Create your views here.
def stu_inp_fields(request):
    submited=False
    sname=""
    if request.method=="POST":
        form=StudentForms(request.POST)
        if form.is_valid():
            print("Form data validation success")
            print("Marks : ", form.cleaned_data['rollno'])
            print("Name : ",form.cleaned_data['name'])
            print("Marks : ", form.cleaned_data['marks'])
            sname=form.cleaned_data["name"]
            submited=True
    form = StudentForms()
    my_dict={'form':form,'sname':sname,'submited':submited}
    return render(request,'testapp/input.html',my_dict)