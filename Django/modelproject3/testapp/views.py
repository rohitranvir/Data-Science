from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_view(request):
    # stu_list=Student.objects.all()
    # stu_list = Student.objects.filter(marks__lt=50)
    # stu_list = Student.objects.filter(name__startswith='S')
    stu_list = Student.objects.all().order_by('-marks')
    my_dic={'my_list':stu_list}
    return render(request,'testapp/demo.html',my_dic)