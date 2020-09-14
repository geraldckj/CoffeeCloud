from django.contrib import admin
from coffeeCloud.models import *


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)


send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]


admin.site.register(Reviews)
admin.site.register(Beans)
admin.site.register(DailyLog)
admin.site.register(Subscriber)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)
