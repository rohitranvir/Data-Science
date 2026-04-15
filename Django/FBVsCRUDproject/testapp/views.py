from django.shortcuts import render, redirect

from testapp.models import Employee


# Create your views here.
def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

from testapp.forms import EmployeeForm
def insert_view(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        form.save()
        return redirect('/')
    form=EmployeeForm
    return render(request,'testapp/insert.html',{'form':form})