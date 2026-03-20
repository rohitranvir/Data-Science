from django.shortcuts import render
from testapp.models import temp
# Create your views here.
def temp_view(request):
    my_list=temp.objects.all()
    my_dict={"my_list":my_list}
    return render(request,'testapp/index.html',my_dict)
