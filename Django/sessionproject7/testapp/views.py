from django.shortcuts import render
from testapp.forms import Additemform
# Create your views here.
def add_item(request):
    form=Additemform()
    return render(request,'testapp/additem.html',{'form':form})
