from django.shortcuts import render, redirect, reverse
from django.urls import path
from .models import Newsletter
from . import views

# Create your views here.


# def get_subscribe(request):
#     emails = Newsletter.objects.all()
#     context = {
#         'emails' : emails
#     }
#     return render(request, 'templates/newsletter.html', context)

# def get_subscribe(request):
        
#     return render(request, 'newsletter.html')

def get_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('newsletter_email')
        Newsletter.objects.create(email=email)

        return redirect(reverse('newsletter.html'))
    
    return render(request, 'newsletter.html')