from django.shortcuts import render
from testapp.forms import SignupForm
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
def logout_view(request):
    return render(request,'testapp/Logout.html')
def Signup_view(request):

    if request.method=="POST":
        form=SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
    form = SignupForm()
    return render(request,'testapp/signup.html',{'form':form})
