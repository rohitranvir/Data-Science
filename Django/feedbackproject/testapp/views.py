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
    if request.method=="POST":
        form=Feedback(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['rollno'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['feedback'])
            result="Form validation successfull "
            name=form.cleaned_data['name']
            rollno=form.cleaned_data['rollno']
            email=form.cleaned_data['email']
            feedback=form.cleaned_data['feedback']
            submited = True
        else:
            result = "form validation faild"
    if submited==False:
        result="Form validation Failed"
    if request.method != "POST":
        form = Feedback()
    my_dict={'form':form,'submited':submited,'name':name,'rollno':rollno,'email':email,'feedback':feedback,"result":result}
    return render(request,'testapp/index.html',my_dict)