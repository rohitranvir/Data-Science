from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})