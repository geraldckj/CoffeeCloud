from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #nested namespace for configurations
    class Meta:
        #telling form what model it interacts with. When form is saved, it is saved into User db
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']