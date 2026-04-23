from django.urls import path
from rest_restframework_simplejwt.views import TokenObtainpairView

from firstproject.firstproject.urls import urlpatterns
from .views import RegisterView,ProfileView
urlpatterns=[
    path('register/',RegisterView.as_view()),
path('login/',TokenObtainpairView.as_view()),
path('profile/',ProfileView.as_view()),

]
