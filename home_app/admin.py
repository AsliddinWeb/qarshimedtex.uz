from django.contrib import admin

# Unfold admin
from unfold.admin import ModelAdmin

# Unregister user, group models
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin

from .models import *

# Unregister
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(Slider)
class SliderAdmin(ModelAdmin):
    list_display = ('title', 'cap_title', 'target', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'target')
    search_fields = ('title', 'cap_title', 'body')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('cap_title', 'title', 'body', 'button_text', 'button_link', 'target', 'image', 'image_alt')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(HomeAbout)
class HomeAboutAdmin(ModelAdmin):
    list_display = ('title', 'count', 'cap_title')
    search_fields = ('title', 'count_title', 'cap_title')

    fieldsets = (
        (None, {
            'fields': ('count', 'count_title', 'image', 'alt', 'cap_title', 'title', 'body')
        }),
        ('Qulayliklar', {
            'fields': ('title_1', 'body_1', 'title_2', 'body_2')
        }),
        ('Qo\'shimcha Ma\'lumotlar', {
            'fields': ('two_body', 'quote')
        }),
    )

@admin.register(HomeTitles)
class HomeTitlesAdmin(ModelAdmin):
    list_display = ('news_title', 'courses_title', 'news2_title', 'liders_title', 'faq_title', 'partners_title')
    search_fields = ('news_title', 'courses_title', 'news2_title', 'liders_title', 'faq_title', 'partners_title')

    fieldsets = (
        (None, {
            'fields': ('news_cap', 'news_title', 'courses_cap', 'courses_title', 'news2_cap', 'news2_title', 'liders_cap', 'liders_title', 'faq_cap', 'faq_title', 'partners_cap', 'partners_title')
        }),
    )

@admin.register(HomeCourses)
class HomeCoursesAdmin(ModelAdmin):
    list_display = ('title', 'cap_title')
    search_fields = ('title', 'cap_title', 'body')
    list_filter = ('title', 'cap_title')
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('cap_title', 'title', 'body', 'image', 'hover_image')
        }),
    )

@admin.register(HomeLeader)
class HomeLeaderAdmin(ModelAdmin):
    list_display = ('title', 'position', 'facebook_url', 'telegram_url')
    search_fields = ('title', 'position')
    list_filter = ('position',)

@admin.register(FaqTitle)
class FaqTitleAdmin(ModelAdmin):
    list_display = ('cap_title', 'title')
    search_fields = ('cap_title', 'title')
    list_filter = ('cap_title',)

@admin.register(Faq)
class FaqAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ('name', 'phone', 'submit')
    search_fields = ('name', 'phone')
    list_filter = ('submit',)

@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('name', 'phone', 'is_view')
    search_fields = ('name', 'phone')
    list_filter = ('is_view',)