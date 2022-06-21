from django.shortcuts import render
#from newsletter.models import 

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')