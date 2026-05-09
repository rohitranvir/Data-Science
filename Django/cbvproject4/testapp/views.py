from testapp.models import Company
from django.views.generic import ListView,UpdateView,DetailView,DeleteView,CreateView,UpdateView
class CompanyListView(ListView):
    model=Company
class CompanyDetailView(DetailView):
    model=Company
class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'
class CompanyUpdateCIew(UpdateView):
    model=Company
    fields='__all__'
