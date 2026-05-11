from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
from django.db.models import Q,Avg,Sum,Min,Max,Count
def aggregate_view(request):
    avg=Employee.objects.aggregate(Avg('esal'))
    sum = Employee.objects.aggregate(Sum('esal'))
    min = Employee.objects.aggregate(Min('esal'))
    max = Employee.objects.aggregate(Max('esal'))
    count = Employee.objects.aggregate(Count('esal'))
    return render(request,'testapp/average.html',{'avg':avg ['esal__avg'],'sum':sum ['esal__sum'],'max':max ['esal__max'],'count':count ['esal__count'],'min':min ['esal__min']})
def retrive_view(request):
    # emp_list=Employee.objects.filter(esal__lt=18000)
    # emp_list = Employee.objects.filter(ename__contains='Mark')
    # emp_list = Employee.objects.filter(id__in=[1,2,3])
    # emp_list = Employee.objects.filter(esal__range=[10000,18000])
    # emp_list = Employee.objects.filter(ename__startswith='M')
    # emp_list = Employee.objects.filter(ename__endswith='y')
    # emp_list = Employee.objects.filter(ename__endswith='y') | Employee.objects.filter(esal__lt=18000)
    # emp_list =Employee.objects.filter(Q(ename__startswith='S')|Q(esal__lte=25000))
    # emp_list = Employee.objects.filter(~Q(ename__startswith='S') | Q(esal__lte=25000))
    # emp_list = Employee.objects.exclude(ename__startswith='S')
    # emp_list = Employee.objects.filter(~Q(ename__startswith='S') | Q(esal__lte=25000))
    # emp_list=Employee.objects.values_list('ename','esal')
    emp_list = Employee.objects.only('ename', 'esal')
    return render(request, 'testapp/specificcolumns.html', {'emp_list': emp_list})

    # return render(request,'testapp/index.html',{'emp_list':emp_list})