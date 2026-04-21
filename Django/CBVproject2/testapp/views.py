from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView
# Create your views here.

# ===>  FBV

# def book_view(request):
#     book_list=Book.objects.all()
#     return render(request,'testapp/result.html',{'book_list':book_list})

# ===> CBV
class BookListView(ListView):
    model=Book
    # Default tamplatefile ModelName_list.html =>Book_list.html
    #Default context Object dictionary  book_list

    # our OWN Customized
    template_name = 'testapp/Book.html'
    context_object_name = 'books'