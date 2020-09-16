from django.contrib import admin
from coffeeCloud.models import Reviews, Beans, DailyLog, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


admin.site.register(Reviews)
admin.site.register(Beans)
admin.site.register(DailyLog)
admin.site.register(Feedback, FeedbackAdmin)
