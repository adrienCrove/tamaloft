from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home, name="Acceuil"),
    path('login',login_user, name="login"),
    path('register',register, name="register"),
    path('about', about, name="about"),
]
