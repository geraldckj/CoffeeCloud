from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class beans(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    description = models.TextField()
    dateRoast = models.DateTimeField(default=timezone.now)

#reviews that users can leave behind for beans, merch & accessories
#if diff classes of products are introduced, might need to add new review tables for each
class Reviews(models.Model):
    #relationship fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(beans, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    review = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)

