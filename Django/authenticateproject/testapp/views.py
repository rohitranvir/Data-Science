from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
from django.contrib.auth.decorators import login_required
@login_required
def java_view(request):
    return render(request,'testapp/javaexam.html')
@login_required
def python_view(request):
    return render(request,'testapp/python.html')
@login_required
def aptitude_view(request):
    return render(request,'testapp/aptitude.html')
