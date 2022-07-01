from django.urls import path
from . import views

urlpatterns = [
    path('newsletter', views.get_subscribe, name='newsletter')   
]