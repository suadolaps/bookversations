from django.contrib import admin
from .models import NewsletterUser, ReadingList

admin.site.register(ReadingList)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'date_added',)


admin.site.register(NewsletterUser, NewsletterAdmin)