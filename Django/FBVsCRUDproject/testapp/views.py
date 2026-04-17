from django.shortcuts import render, redirect

from testapp.models import Employee
from testapp.forms import EmployeeForm

# Create your views here.a
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST, instance =employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=EmployeeForm(instance=employee)
    return render(request,'testapp/update.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})


def insert_view(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        form.save()
        return redirect('/')
    form=EmployeeForm
    return render(request,'testapp/insert.html',{'form':form})