from django.shortcuts import render
import datetime
# Create your views here.
def infor(request):
    time=datetime.datetime.now()
    name='Django'
    prereq='Python'
    my_dict={'time':time,'name':name,'prereq':prereq}
    return render(request,'testapp/result.html',my_dict)