from django.shortcuts import render
from testapp.forms import Nameform,Ageform,Gfform
# Create your views here.
def name_view(request):
    form=Nameform()
    # username=request.session.get('name','Guest')
    return render(request,'testapp/index.html',{'form':form})
    # request.session['name']=username
    # return response
    # def age_view(request):
def age_view(request):
    name=request.GET.get('name','GUEST')
    request.session['name']=name
    form=Ageform()
    return render(request,'testapp/age.html',{'form':form,'name':name})
def gf_view(request):
    age=request.GET.get('age','Not provided')
    name=request.session.get('name','Guest')
    request.session['age']=age
    form=Gfform()
    return render(request,'testapp/gf.html',{'form':form,'age':age,'name':name})
def result_view(request):
    name=request.session.get('name','Guest')
    age=request.session.get('age','Not provided')
    gf=request.GET.get('Gfname','Not provided')
    request.session['gf']=gf
    return render(request,'testapp/result.html',{'name':name,'age':age,'gf':gf})
