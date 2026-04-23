from django.contrib import admin
from django.urls import path
from api.views import get_books,create_books,book_details
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('books/', get_books,name='get_books'),
    path('books/create',create_books,name='create_book'),
    path('books/<int:id>',book_details,name='book_details')
]
