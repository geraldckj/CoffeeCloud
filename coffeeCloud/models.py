from crum import get_current_user
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mass_mail
from django.db import models
from django.utils import timezone


class Beans(models.Model):
    company = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    process = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    dateRoast = models.DateTimeField(default=None, blank=True, null=True)
    notes = models.TextField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        currUser = get_current_user()
        if currUser and not currUser.pk:
            currUser = None
        self.user = currUser
        super(Beans, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# reviews that users can leave behind for beans, merch & accessories
# if diff classes of products are introduced, might need to add new review tables for each
class Reviews(models.Model):
    # relationship fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # when adding in shell, can add via id:
    # user_id = user.id
    item = models.ForeignKey(Beans, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100, default="User did not input title")
    bean = models.CharField(max_length=100, default="User did not input beam")
    brewMethod = models.CharField(max_length=100)
    remarks = models.TextField(default="", blank=True, null=True)
    dateLogged = models.DateTimeField(default=timezone.now)
    prevActivity = models.CharField(
        default=None, blank=True, null=True, max_length=100)
    taste = models.IntegerField(default=None, blank=True, null=True)
    mood = models.IntegerField(default=None, blank=True, null=True)
    cNotes = models.CharField(
        max_length=100, default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        currUser = get_current_user()
        if currUser and not currUser.pk:
            currUser = None
        self.user = currUser
        super(DailyLog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.email


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='uploaded_newsletters/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        subscribers_list = list()
        for sub in subscribers:
            subscribers_list.append(sub)

        html_content = contents + (
                    '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                    request.build_absolute_uri('/delete/')

        send_mass_mail((
            subject=self.subject,
            message=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=subscribers_list), fail_silently=False)
