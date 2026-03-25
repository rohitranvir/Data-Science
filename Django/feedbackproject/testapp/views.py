from django.shortcuts import render
from testapp.forms import Feedback
# Create your views here.
def feedbackform(request):
    submited=False
    name=""
    rollno=""
    email=""
    feedback=""
    if request.method=="POST":
        form=Feedback(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['rollno'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['feedback'])
            name=form.cleaned_data['name']
            rollno=form.cleaned_data['rollno']
            email=form.cleaned_data['email']
            feedback=form.cleaned_data['feedback']
            submited = True
    form=Feedback()
    my_dict={'form':form,'submited':submited,'name':name,'rollno':rollno,'email':email,'feedback':feedback}
    return render(request,'testapp/index.html',my_dict)