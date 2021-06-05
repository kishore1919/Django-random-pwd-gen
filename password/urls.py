from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('password/',views.password, name='password'),
]