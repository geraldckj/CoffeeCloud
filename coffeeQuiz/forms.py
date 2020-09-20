from django import forms
from django.forms import ModelForm
from coffeeQuiz.models import coffeeQuiz
from crispy_forms.helper import FormHelper



#django creates forms in template straight from these classes.
#pass class as a variable into views.py, then pass var into template's crispy forms

brewMethod = [
    ("Espresso", 'Espresso'),
    ("Filter", 'Filter'),
    ("Immersion", 'Immersion'),
]

expLevel = [
    ("beginner", "Beginner"),
    ("savvy", "Savvy"),
    ("expert", "Expert"),
    ("expert", "Legend"),
]

prefTaste = [
    #option on left is what shows up in db. Option on right is what user sees.
    ("africa", "Berries, Stonefruit. Fruity and complex flavours"),
    ("indonesia/india", "Earthy, herbal, Chocolately"),
    ("brazil/columbia", "Bright, Nutty and Chocolately"),
]

class coffeeQuiz(ModelForm):
    class Meta:
        model = coffeeQuiz
        fields=['expLevel', 'brewMethod', 'prefTaste']
        widgets = {
            'expLevel':forms.Select(choices=expLevel, attrs={'class': 'form-control'}),
            'brewMethod':forms.Select(choices=brewMethod, attrs={'class': 'form-control'}),
            'prefTaste':forms.Select(choices=prefTaste, attrs={'class': 'form-control'}),
        }
        labels = {
            'expLevel': 'How familiar are you with specality coffee?',
            'brewMethod': 'What do you normally brew on?',
            'prefTaste': 'Which option tempts your tastebuds more?'
        }
