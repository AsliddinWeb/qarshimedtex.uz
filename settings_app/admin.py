from django.contrib import admin

# Unfold admin
from unfold.admin import ModelAdmin

from .models import *

class SeoSettingsAdmin(ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'keywords', 'description', 'author')

admin.site.register(SeoSettings, SeoSettingsAdmin)


class HeaderSettingsAdmin(ModelAdmin):
    list_display = ('phone', 'email', 'bot')
    search_fields = ('phone', 'email', 'bot', 'right_button_title', 'search_placeholder')

admin.site.register(HeaderSettings, HeaderSettingsAdmin)

class FooterSettingsAdmin(ModelAdmin):
    list_display = ('copyright',)
    search_fields = ('body', 'copyright')

admin.site.register(FooterSettings, FooterSettingsAdmin)


class FooterLinkCategoryAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(FooterLinkCategory, FooterLinkCategoryAdmin)


class FooterLinkAdmin(ModelAdmin):
    list_display = ('title', 'link', 'category')
    search_fields = ('title', 'link', 'category__title')

admin.site.register(FooterLink, FooterLinkAdmin)


class ContactInfoAdmin(ModelAdmin):
    list_display = ('title', 'location', 'phone', 'email')
    search_fields = ('title', 'location', 'phone', 'email')

admin.site.register(ContactInfo, ContactInfoAdmin)


class SocialSettingsAdmin(ModelAdmin):
    list_display = ('title', 'i_class', 'link')
    search_fields = ('title', 'i_class', 'link')

admin.site.register(SocialSettings, SocialSettingsAdmin)

class MoreTitlesAdmin(ModelAdmin):
    list_display = ('home', 'related_news', 'news_page')
    search_fields = ('home', 'related_news', 'news_page')

admin.site.register(MoreTitles, MoreTitlesAdmin)

class ErrorTextsAdmin(ModelAdmin):
    list_display = ('error_404_title', 'error_500_title')
    search_fields = ('error_404_title', 'error_500_title')
admin.site.register(ErrorTexts, ErrorTextsAdmin)

class TelegramBotSettingsAdmin(ModelAdmin):
    list_display = ('title', 'token')
admin.site.register(TelegramBotSettings, TelegramBotSettingsAdmin)
