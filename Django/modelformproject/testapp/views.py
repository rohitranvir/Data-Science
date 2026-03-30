from django.shortcuts import render

from testapp.forms import Studentform
# Create your views here.
def student_view(request):

    if request.method=="POST":
        form=Studentform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Student imported successfully..............")
    form = Studentform()
    mydict={"form":form}
    return render(request,'testapp/std.html',mydict)
