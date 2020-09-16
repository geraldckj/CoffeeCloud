from django.shortcuts import render, redirect
from coffeeQuiz.forms import coffeeQuiz

def coffeeTasteQuiz(request):
    if request.method == "POST":
        formQuiz = coffeeQuiz(request.POST)
        if formQuiz.is_valid():
            formQuiz.user = request.user_id
            formQuiz.save()
            return redirect('coffeeCloud-home')
        else:
            print("form not valid")
    formQuiz = coffeeQuiz()
    return render(request, "coffeeQuiz/coffeeTasteQuiz.html", {'coffeeTasteQuiz':formQuiz})
