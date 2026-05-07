from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from testapp.models import Book
from django.urls import reverse_lazy
class BookListView(ListView):
    model = Book
    template_name = 'testapp/Book.html'
    context_object_name = 'books'

class BookListView2(ListView):
    model = Book
    template_name = 'testapp/Book.html'
    # template_name = 'testapp/Book_list.html'
    # context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    # template_name = 'testapp/Book_detail.html'
    # context_object_name = 'book'
class BookCreateView(CreateView):
    model =Book
    fields = '__all__'
    success_url = reverse_lazy('createbook')
class BookUpdateView(UpdateView):
    model=Book
    fields = '__all__'