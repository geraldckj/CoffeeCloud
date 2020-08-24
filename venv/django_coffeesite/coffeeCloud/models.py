from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from crum import get_current_user

class Beans(models.Model):
    company = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    process = models.CharField(max_length=200, default=None, blank=True, null=True)
    description = models.TextField()
    dateRoast = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

#reviews that users can leave behind for beans, merch & accessories
#if diff classes of products are introduced, might need to add new review tables for each
class Reviews(models.Model):
    #relationship fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #when adding in shell, can add via id:
    # user_id = user.id
    item = models.ForeignKey(Beans, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Daily Brew")
    bean = models.CharField(max_length=100, default=None, blank=True, null=True)
    brewMethod = models.CharField(max_length=100)
    remarks = models.TextField(default="No remarks")
    dateLogged= models.DateTimeField(default=timezone.now)
    prevActivity = models.CharField(default=None, blank=True, null=True, max_length=100)
    taste = models.IntegerField(default=None, blank=True, null=True)
    mood = models.IntegerField(default=None, blank=True, null=True)
    cNotes = models.TextField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        currUser = get_current_user()
        if currUser and not currUser.pk:
            currUser = None
        self.user = currUser
        super(DailyLog, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
