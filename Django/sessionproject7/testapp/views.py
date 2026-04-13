from django.shortcuts import render
from testapp.forms import Additemform
# Create your views here.
def add_item(request):
    form=Additemform()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render(request,'testapp/additem.html',{'form':form})
def display_item(request):
    return render(request,'testapp/displayitem.html')
