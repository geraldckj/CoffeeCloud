from .views import *
from django import forms
from django.forms import ModelForm
from .models import DailyLog, Beans
from crispy_forms.helper import FormHelper
from threading import local

#TODO: figure out how to dynamically pass currUserID into forms.py from either views or model

#django creates forms in template straight from these classes.
#pass class as a variable into views.py, then pass var into template's crispy forms

brewMethodChoices = [
    ("V60", 'V60'),
    ("Chemex", 'Chemex'),
    ("Espresso", 'Espresso'),
    ("Aeropress", 'Aeropress'),
    ("Mokapot", 'Mokapot'),
    ("French Press", 'French press')
]

activities = [
    ("resting", "Resting"),
    ("working", "Working"),
    ("exercising", "Exercising"),
    ("eating", "Eating")
]

roastLevel = [
    ("light", "Light"),
    ("medium", "Medium"),
    ("dark", "Dark"),
]

class DailyLogForm(ModelForm):
    #source for innit method
    #https://stackoverflow.com/questions/2237064/passing-arguments-to-a-dynamic-form-in-django

    def __init__(self, *args, **kwargs):
        choices = Beans.objects.all()
        placeholder = Beans.objects.first()
        super(DailyLogForm, self).__init__(*args, **kwargs)
        self.fields['bean'] = forms.ModelChoiceField(choices)
        self.fields['bean'].initial = placeholder
    class Meta:
        #telling form what model it interacts with. When form is saved, it is saved into User db
        model = DailyLog

        fields = ['title', 'bean', 'brewMethod', 'prevActivity', 'taste',
                  'mood', 'cNotes', 'remarks']
        widgets = {
            'brewMethod': forms.Select(choices=brewMethodChoices, attrs={'class': 'form-control'}),
            'prevActivity': forms.Select(choices=activities, attrs={'class': 'form-control'}),
        }
        labels = {
            "brewMethod": "Brew Method",
            "bean": "Beans",
            'taste': 'Rate your cup',
            'mood': 'Rate your mood while having this cup',
            'cNotes': 'What notes do you get in your cup? Separate each note with a comma',
            'title': 'Log title',
            'prevActivity': 'What were you doing before your cup?',
        }

class NewBeansForm(ModelForm):
    class Meta:
        model = Beans
        fields = ['company', 'name', 'region', 'roast', 'process', 'dateRoast', 'notes', 'description']
        widgets = {
            'roast': forms.Select(choices=roastLevel, attrs={'class': 'form-control'})
        }

        labels = {
            "company": "Roaster",
            "name": "Bean Name",
            'region': 'Region',
            'roast': 'Roast Level',
            'dateRoast': 'Roast Date',
            'notes': 'Roasters normally give you a few tasting notes. Tell us what they are!',
            'description': 'Remarks',
        }

    def __init__(self, *args, **kwargs):
        placeholder = "Medium"
        super(NewBeansForm, self).__init__(*args, **kwargs)
        self.fields['roast'].initial = placeholder

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
