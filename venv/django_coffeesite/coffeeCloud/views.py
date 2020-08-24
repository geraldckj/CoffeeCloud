from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Beans
from.forms import DailyLogForm
from django.contrib import messages


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

def dailyLog(request):
    # conditional to handle post and get requests
    if request.method == 'POST':
        # usercreationform auto maps to user db. don't need to do new route
        form = DailyLogForm(request.POST)
        if form.is_valid():
            currUser = request.user
            form.user = currUser.id
            form.save()
            # flash message if form is valid, daily log success
            messages.success(request, f'Your brew has been logged! Enjoy your coffee :)')
            # url's can be returned with the name="" given in urls.py
            return redirect('coffeeCloud-dailyLog')
    else:
        form = DailyLogForm()
    return render(request, "coffeeCloud/dailyLog.html", {'form': form})