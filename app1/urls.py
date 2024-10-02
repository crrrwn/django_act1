# app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app1-home'),
    path('about/', views.about, name='app1-about'),
    path('contact/', views.contact, name='app1-contact'),
]
