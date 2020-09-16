import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    time_answered = models.DateTimeField()
    def __str__(self):
        return self.choice_text   
    def was_answered_reccently (self):
        return self.time_answered >= timezone.now() - datetime.timedelta(days=1)

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=200)

class coffeeQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expLevel = models.CharField(max_length=200)
    brewMethod = models.CharField(max_length=200)
    prefTaste = models.CharField(max_length=200)
    time_answered = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.brewMethod


    
