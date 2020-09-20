import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from crum import get_current_user

class coffeeQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expLevel = models.CharField(max_length=200)
    brewMethod = models.CharField(max_length=200)
    prefTaste = models.CharField(max_length=200)
    time_answered = models.DateTimeField(default = timezone.now)
    
    def save(self, *args, **kwargs):
        currUser = get_current_user()
        print(f"currUser: {currUser}")
        self.user = currUser
        super(coffeeQuiz, self).save(*args, **kwargs)

    def __str__(self):
        return self.brewMethod