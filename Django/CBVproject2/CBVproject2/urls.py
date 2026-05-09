from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.BookListView2.as_view()),
    path('list2/', views.BookListView.as_view(), name='createbook'),
    path('create/', views.BookCreateView.as_view()),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='updatebook'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),  # put LAST
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete'),
]