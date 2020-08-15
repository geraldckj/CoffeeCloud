from django.shortcuts import render
from django.http import HttpResponse

#dummy data for products to be compared
products = [
    {
        'company':'PPP coffee',
        'region':'Columbian',
        'roastLevel':'Medium',
        'process':'Honey Processed',
        'roastDate':'August 27 2020'
    },
    {
        'company':'Nylon coffee',
        'region':'Africa',
        'roastLevel':'Light',
        'process':'Natural Processed',
        'roastDate':'July 10 2020'
    }
]



def home(request):
    #dict is passed into template. Can be accessed by 'products' key.
    catalogue = {
        #'products' key is refernced in template to loop through
        'products' : products
    }
    #2nd argument must pass as html file within parent folder
    return render(request, "coffeeCloud/home.html", catalogue)

def about(request):
    return render(request, "coffeeCloud/about.html", {'title': 'About us'})