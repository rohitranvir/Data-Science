from http.client import responses

from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def age_view(request):
    print(request.GET)
    print(request.COOKIES)
    print(request.GET.get('name','Gita'))
    username=request.GET.get('name','Guest')
    response=render(request,'testapp/age.html',{'name':username})
    response.set_cookie('name',username)
    return response
def gf_view(request):
    username=request.COOKIES.get('name','Unknown')
    age=request.GET.get('age','Not provided')
    response=render(request,'testapp/gf.html',{'name':username,'age':age})
    response.set_cookie('age',age)
    return response
def result(request):
    print(request.COOKIES)
    age=request.COOKIES.get('age','Not provided')
    name = request.COOKIES.get('name','Unknown')
    gfname = request.GET.get('name','Unknown')
    response=render(request,'testapp/result.html',{'gfname':gfname,'age':age,'name':name})
    response.set_cookie('gfname',gfname)
    return response


