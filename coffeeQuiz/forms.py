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

# class DailyLogForm(ModelForm):
#     bean = forms.ModelChoiceField(queryset=Beans.objects.none())
#     #source for innit method
#     #https://stackoverflow.com/questions/2237064/passing-arguments-to-a-dynamic-form-in-django
#     def __init__(self, user, beanToLog, *args, **kwargs):
#         # placeholder = Beans.objects.filter(name=beanToLog)
#         # print(placeholder)
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.fields['bean'].queryset = Beans.objects.filter(user=user)
#         self.fields['bean'].initial = beanToLog
#         self.fields['title'].initial = ""
#         self.helper.layout = Layout(
#             CustomNotesInput()
#         )

#     # def __init__(self, *args, **kwargs):
#     #     choices = Beans.objects.all()
#     #     placeholder = Beans.objects.first()
#     #     super(DailyLogForm, self).__init__(*args, **kwargs)
#     #     self.fields['bean'] = forms.ModelChoiceField(choices)
#     #     self.fields['bean'].initial = placeholder

#     class Meta:
#         #telling form what model it interacts with. When form is saved, it is saved into User db
#         model = DailyLog

#         fields = ['title', 'bean', 'brewMethod', 'prevActivity', 'taste',
#                   'mood', 'cNotes', 'remarks']
#         widgets = {
#             'brewMethod': forms.Select(choices=brewMethodChoices, attrs={'class': 'form-control'}),
#             'prevActivity': forms.Select(choices=activities, attrs={'class': 'form-control'}),
#         }
#         labels = {
#             "brewMethod": "Brew Method",
#             "bean": "Beans",
#             'taste': 'Rate your cup',
#             'mood': 'Rate your mood while having this cup',
#             'cNotes': 'What notes do you get in your cup? Separate each note with a comma',
#             'title': 'Log title',
#             'prevActivity': 'What were you doing before your cup?',
#             'BeanToLog': 'Beans',
#         }

# class NewBeansForm(ModelForm):
#     class Meta:
#         model = Beans
#         fields = ['company', 'name', 'region', 'roast', 'process', 'dateRoast', 'notes', 'description']
#         widgets = {
#             'roast': forms.Select(choices=roastLevel, attrs={'class': 'form-control'})
#         }

#         labels = {
#             "company": "Roaster",
#             "name": "Bean Name",
#             'region': 'Region',
#             'roast': 'Roast Level',
#             'dateRoast': 'Roast Date',
#             'notes': 'Roasters normally give you a few tasting notes. Tell us what they are!',
#             'description': 'Remarks',
#         }

#     def __init__(self, *args, **kwargs):
#         placeholder = "Medium"
#         super(NewBeansForm, self).__init__(*args, **kwargs)
#         self.fields['roast'].initial = placeholder

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)


# class BeanToLog(forms.Form):
#     BeanToLog = forms.ModelChoiceField(queryset=Beans.objects.none())

#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.fields['BeanToLog'].queryset = Beans.objects.filter(user=user)
