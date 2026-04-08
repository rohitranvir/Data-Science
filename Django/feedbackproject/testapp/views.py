from django.shortcuts import render
from testapp.forms import Feedback
# Create your views here.
def feedbackform(request):
    submited=False
    name=""
    rollno=""
    email=""
    feedback=""
    result=""
    password=""
    rpassword=""
    if request.method=="POST":
        form=Feedback(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['rollno'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['feedback'])
            print(form.cleaned_data['password'])
            print(form.cleaned_data['rpassword'])
            result="Form validation successfull "
            name=form.cleaned_data['name']
            rollno=form.cleaned_data['rollno']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            rpassword=form.cleaned_data['rpassword']
            feedback=form.cleaned_data['feedback']
            submited = True
        else:
            result = "form validation faild"
    if submited==False:
        result="Form validation Failed"
    if request.method != "POST":
        form = Feedback()
    my_dict={'form':form,'submited':submited,'name':name,'rollno':rollno,'email':email,'feedback':feedback,"result":result,'rpassword':rpassword,'password':rpassword}
    return render(request,'testapp/home.html',my_dict)