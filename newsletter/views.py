from django.shortcuts import render
from django.urls import path
from .models import Newsletter
#from . import views

# Create your views here.

# urlpatterns = [
#     path('', views.newsletter, name='newsletter')
# ]

# def get_subscribe(request):
#     emails = Newsletter.objects.all()
#     context = {
#         'emails' : emails
#     }
#     return render(request, 'templates/newsletter.html', context)