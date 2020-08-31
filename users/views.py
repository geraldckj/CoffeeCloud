from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import userRegisterForm

#create user  registration view
def register(request):
    #conditional to handle post and get requests
    if request.method == 'POST':
        #usercreationform auto maps to user db. don't need to do new route
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save() #saving user in User db
            name = form.cleaned_data.get('first_name')
            #flash message if form is valid, user register success
            messages.success(request, f'Hey {name}, your account has been registered! You can now login')
            #url's can be returned with the name="" given in urls.py
            return redirect('login')
    else:
        form = userRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

