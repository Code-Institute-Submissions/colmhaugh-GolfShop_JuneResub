from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_subscribe, name='newsletter'),
    #path('add/', views.get_subscribe, name='subscribe'),    
]