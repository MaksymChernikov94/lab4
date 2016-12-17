from django.contrib import admin

from .models import News, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [ChoiceInline]

admin.site.register(News, NewsAdmin)
