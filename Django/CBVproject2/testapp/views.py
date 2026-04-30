from django.views.generic import ListView, DetailView
from testapp.models import Book

class BookListView(ListView):
    model = Book
    template_name = 'testapp/Book_list.html'
    context_object_name = 'books'
class BookDetailView(DetailView):
    model = Book
    template_name = 'testapp/Book_detail.html'
    context_object_name = 'book'