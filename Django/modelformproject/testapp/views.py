from django.shortcuts import render

from testapp.forms import StudentForms
# Create your views here.
def student_view(request):
    form=StudentForms()
    mydict={"form":form}
    return render(request,'testapp/std.html',mydict)
