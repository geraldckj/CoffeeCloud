from django.shortcuts import render
from django.http import HttpResponse
from.models import Beans

def home(request):
    #dict is passed into template. Can be accessed by 'products' key.
    catalogue = {
        #'products' key is refernced in template to loop through
        'products' : Beans.objects.all()
    }
    #2nd argument must pass as html file within parent folder
    return render(request, "coffeeCloud/home.html", catalogue)

def about(request):
    return render(request, "coffeeCloud/about.html", {'title': 'About us'})

def pub_homepage(request):
    return render(request, "coffeeCloud/pub_homepage.html")