from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from coffeeQuiz.forms import coffeeQuiz

def coffeeTasteQuiz(request):
    if request.POST:
        formQuiz = coffeeQuiz(request.POST)
        if formQuiz.is_valid():
            formQuiz.save()
        # flash message if form is valid, daily log success
            messages.success(request, f'Your result have been received.')
            return redirect('coffeeCloud-home')

        else:
            print("form not valid")
    formQuiz = coffeeQuiz()
    return render(request, "coffeeQuiz/coffeeTasteQuiz.html", {'coffeeTasteQuiz':formQuiz})

#TODO: Figure out how to make form post properly