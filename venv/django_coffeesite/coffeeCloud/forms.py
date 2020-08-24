from django import forms
from django.forms import ModelForm
from .models import DailyLog
from crispy_forms.helper import FormHelper

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
class DailyLogForm(forms.ModelForm):
    #nested namespace for configurations
    title = forms.CharField(label="Log title", max_length=150)
    bean = forms.CharField(label="Bean", max_length=100)
    brewMethod = forms.ChoiceField(label="Brew Method", choices=brewMethodChoices)
    remarks = forms.CharField(label="Remarks", max_length=500)
    #newly added
    prevActivity = forms.ChoiceField(label="prevActivity", choices=activities)
    taste = forms.IntegerField(label="Rate your cup /10!", max_value=10)
    mood = forms.IntegerField(label="Rate your mood /10!", max_value=10)
    cNotes = forms.CharField(label="What notes did you taste? Seperate each note with a comma.", max_length= 500)


    class Meta:
        #telling form what model it interacts with. When form is saved, it is saved into User db
        model = DailyLog
        fields = ['title', 'bean', 'brewMethod', 'remarks', 'prevActivity', 'taste',
                  'mood', 'cNotes']
