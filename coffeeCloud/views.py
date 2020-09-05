from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from.models import Beans
from.forms import DailyLogForm, NewBeansForm, ContactForm, BeanToLog

beanChoice = []

def home(request):
    #dict is passed into template. Can be accessed by 'products' key.
    catalogue = {
        #'products' key is refernced in template to loop through
        'products': Beans.objects.all()
    }
    #2nd argument must pass as html file within parent folder
    return render(request, "coffeeCloud/home.html", catalogue)

def about(request):
    return render(request, "coffeeCloud/about.html", {'title': 'About us'})

def pub_homepage(request):
    return render(request, "coffeeCloud/pub_homepage.html")

def dailyLog(request):
    #TODO: allow notes field to accept and show HTML chips in real time
    # conditional to handle post and get requests
    if request.method == 'POST':
        # usercreationform auto maps to user db. don't need to do new route
        form = DailyLogForm(request.POST)
        if form.is_valid():
            user = request.user
            form.user = user.id
            form.save()
            # flash message if form is valid, daily log success
            messages.success(request, f'Your brew has been logged! Enjoy your coffee :)')
            # url's can be returned with the name="" given in urls.py
            return redirect('coffeeCloud-dailyLog')
    else:
        beanToLog = request.session['beanToLog']
        print(beanToLog)
        beanToLog = Beans.objects.filter(name=beanToLog)
        user = request.user
        form = DailyLogForm(user=user, beanToLog=beanToLog)
    return render(request, "coffeeCloud/dailyLog.html", {'form': form})

def addBean(request):
    #TODO: Try using session middleware to store the user's beans.
    # conditional to handle post and get requests
    if request.method == 'POST':
        # usercreationform auto maps to user db. don't need to do new route
        form = NewBeansForm(request.POST)
        if form.is_valid():
            currUser = request.user
            print(f"curr user: {currUser.id}")
            form.save()
            # flash message if form is valid, daily log success
            messages.success(request, f'Thank you! Your beans will be added to our public database! '
                                      f'Log your first cup here :)')
            # url's can be returned with the name="" given in urls.py
            return redirect('coffeeCloud-dailyLog')
    else:
        form = NewBeansForm()
    return render(request, "coffeeCloud/addBean.html", {'form': form})

def myBeans(request):
    #get curr user
    user = request.user
    beans = Beans.objects.filter(user=user)
    allUserBeans = {
        'products': beans
    }
    return render(request, "coffeeCloud/myBeans.html", allUserBeans)

def contactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['geraldckj13@gmail.com'])

            messages.success(request, f'Thank you for getting in touch! We will respond to your ticket ASAP')
            return redirect('coffeeCloud-home')
    else:
        form = ContactForm()
    return render(request, "coffeeCloud/contactForm.html", {'form': form})


def logChoice(request):
    # TODO: Allow choice in dropdown to autopopulate daily log field
    if request.method == 'POST':
        form = BeanToLog(request.user, request.POST)
        if form.is_valid():
            chosenBean = form.cleaned_data['BeanToLog']
            # get value of chosen bean from html
            print(f'chosenBean: {chosenBean}')
            chosenBean = str(chosenBean)
            request.session['beanToLog'] = chosenBean
            # tmp = request.session['beanToLog']
            # print(tmp)

            return redirect('coffeeCloud-dailyLog')
    else:
        user = request.user
        #shows user most recent logged bean
        userBean = Beans.objects.filter(user=user)
        pastBean = {
            'pastBean': userBean
        }
        print(pastBean)
        form = BeanToLog(user=user)
        return render(request, 'coffeeCloud/logChoice.html', {"form": form, 'pastBean': userBean})

def chipTest(request):
    return render(request, "coffeeCloud/chipTest.html")

def chipTest2(request):
    return render(request, "coffeeCLoud/chipTest2.html")
