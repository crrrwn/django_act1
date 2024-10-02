from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app2-home'),
    path('services/', views.services, name='app2-services'),
    path('portfolio/', views.portfolio, name='app2-portfolio'),
]
