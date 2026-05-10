from testapp.models import Company
from django.views.generic import ListView,UpdateView,DetailView,DeleteView,CreateView,UpdateView
class CompanyListView(ListView):
    model=Company
class CompanyDetailView(DetailView):
    model=Company
class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'
class CompanyUpdateView(UpdateView):
    model=Company
    fields='__all__'
from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model=Company
    success_url =reverse_lazy('list')