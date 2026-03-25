from django.shortcuts import render
from testapp.forms import StudentForms
# Create your views here.
def stu_inp_fields(request):
    submited=False
    rollno=""
    name=""
    marks=""
    if request.method=="POST":
        form=StudentForms(request.POST)
        if form.is_valid():
            submited = True
            name=form.cleaned_data["name"]
            rollno = form.cleaned_data["rollno"]
            marks = form.cleaned_data["marks"]

    form=StudentForms()
    my_dict={"rollno":rollno,"name":name,"marks":marks,"submited":submited,"form":form}
    return render(request,'testapp/input.html',my_dict)