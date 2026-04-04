from django.shortcuts import render
from testapp.models import FilterModel
# Create your views here.
def data_view(request):
    records=FilterModel.objects.all()
    return render(request,'testapp/index.html',{"records":records})