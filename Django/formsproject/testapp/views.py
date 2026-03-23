from django.shortcuts import render
from testapp.forms import StudentForms
# Create your views here.
def stu_inp_fields(request):
    form=StudentForms()
    my_dict={'form':form}
    return render(request,'testapp/input.html',my_dict)