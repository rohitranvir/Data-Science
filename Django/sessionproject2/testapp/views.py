from django.shortcuts import render

# Create your views here.
from testapp.forms import Loginform
def home_view(requeest):
    form =Loginform()
    return render(requeest,'testapp/home.html',{"form":form})
def date_and_time_view(request):
    name=request.GET["name"]
    response= render(request,'testapp/datetime.html',{"name":name})
    response.set_cookie('name',name)
    return response
import datetime
def result_view(request):
    name=request.COOKIES.get('name')
    date_time=datetime.datetime.now()
    return render(request,'testapp/result.html',{'name':name,'time':date_time})