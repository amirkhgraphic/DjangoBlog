from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ['-created_at']
    list_display = ['email', 'user_name', 'first_name', 'last_name', 'created_at', 'last_login', 'is_active', 'is_staff']
    search_fields = ['email', 'user_name', 'first_name', 'last_name']
    list_filter = ['first_name', 'last_name']
    readonly_fields = ['created_at', 'last_login']
    fieldsets = [
        [_('basic'), {'fields': ['email', 'user_name', 'first_name', 'last_name']}],
        [_('Personal'), {'fields': ['about']}],
        [_('Important dates'), {'fields': ['created_at', 'last_login']}],
        [_('Permissions'), {'fields': ['is_staff', 'is_active']}],
    ]

    add_fieldsets = [
        ['Required Fields', {
            'classes': ['wide'],
            'fields': ['email', 'user_name', 'first_name', 'last_name', 'password1', 'password2'],
        }],
        ['Optional Fields', {
            'classes': ['wide'],
            'fields': ['about', 'is_active', 'is_staff'],
        }],
    ]
