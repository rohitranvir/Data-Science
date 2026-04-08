from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'testapp/home.html')
from testapp.forms import Additemform
def add_item_view(request):
    print(request.COOKIES)
    form =Additemform()
    response= render(request,'testapp/additem.html',{"form":form})
    if request.method=='POST':
        form=Additemform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity)
    return response
def diaply_view(request):
    return render(request,'testapp/display.html')

