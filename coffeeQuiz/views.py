from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from coffeeQuiz.forms import coffeeQuiz
from coffeeCloud.models import Beans
from itertools import chain

def coffeeTasteQuiz(request):
    if request.POST:
        formQuiz = coffeeQuiz(request.POST)
        if formQuiz.is_valid():
            formQuiz.save()
        # flash message if form is valid, daily log success
            messages.success(request, f'Your result have been received.')
            expLevel = formQuiz.cleaned_data['expLevel']
            brewMethod = formQuiz.cleaned_data['brewMethod']
            prefTaste = formQuiz.cleaned_data['prefTaste']
            print(f"expLevel: {expLevel}")
            print(f"brewMethod: {brewMethod}")
            print(f"prefTaste: {prefTaste}")
            region = []
            if prefTaste == ("africa"):
                region.append('Africa')
                region.append('Ethiopia')
                region.append('Kenya')

            elif prefTaste == "indonesia/india":
                region.append('Indonesia')
                region.append('India')
            
            elif prefTaste == "brazil/columbia":
                region.append('Brazil')
                region.append('Columbia')
            count = 0
            reccomendedBean = []
            for place in region:
                count += 1
                reccBean = Beans.objects.filter(region=place)
                print(f"loop count:{count}" )
                print(reccBean)
                for bean in reccBean:
                    print(f"Bean: {bean}")
                    reccomendedBean.append(str(bean))
            print(f"list of reccomended beans: {reccomendedBean}")
            request.session['reccomendedBean'] = reccomendedBean
            
            #TODO: return redirect into quiz reccomendation page
            return redirect('coffeeQuiz-reccomendedBeans')

        else:
            print("form not valid")
    formQuiz = coffeeQuiz()
    return render(request, "coffeeQuiz/coffeeTasteQuiz.html", {'coffeeTasteQuiz':formQuiz})

#view for reccomended beans from quiz
def reccomendations(request):
    reccomendedBean = request.session['reccomendedBean']
    print(F"beans received from quiz: {reccomendedBean}")
    beansToDisplay = {}
    prevQuery = None
    for item in reccomendedBean:
        print(f"Bean to query: {item}")
        tmp = Beans.objects.filter(name=item)
        if not prevQuery: #prevQuery is None
            print(f"query results: {tmp}")
            prevQuery = tmp
        else: #prevQuery has smth inside
            prevQuery = chain(prevQuery, tmp)
            
    beansToDisplay = {
        'reccBean': prevQuery
    }
    return render(request, "coffeeQuiz/reccomendedBeans.html", beansToDisplay)