from django.contrib import admin

# Unfold admin
from unfold.admin import ModelAdmin

from .models import OneNavbar, TwoNavbar, ThreeNavbar, NavType
from .forms import TwoNavbarForm, ThreeNavbarForm

class NavTypeAdmin(ModelAdmin):
    list_display = ('title', 'type')
    search_fields = ('title', 'type')

class OneNavbarAdmin(ModelAdmin):
    list_display = ('title', 'link', 'is_submenu', 'nav_type', 'order')
    search_fields = ('title',)
    list_filter = ('is_submenu', 'nav_type')
    ordering = ('order',)  # Default ordering by 'order' field

class TwoNavbarAdmin(ModelAdmin):
    form = TwoNavbarForm
    list_display = ('title', 'link', 'is_submenu', 'one_navbar', 'nav_type', 'order')
    search_fields = ('title',)
    list_filter = ('is_submenu', 'one_navbar', 'nav_type')
    ordering = ('order',)  # Default ordering by 'order' field

class ThreeNavbarAdmin(ModelAdmin):
    form = ThreeNavbarForm
    list_display = ('title', 'link', 'is_submenu', 'two_navbar', 'nav_type', 'order')
    search_fields = ('title',)
    list_filter = ('is_submenu', 'two_navbar', 'nav_type')
    ordering = ('order',)  # Default ordering by 'order' field

admin.site.register(NavType, NavTypeAdmin)
admin.site.register(OneNavbar, OneNavbarAdmin)
admin.site.register(TwoNavbar, TwoNavbarAdmin)
admin.site.register(ThreeNavbar, ThreeNavbarAdmin)
