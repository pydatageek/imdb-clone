"""Admin registeries for custom user related models"""

from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as DjangoBaseUserAdmin, GroupAdmin as DjangoBaseGroupAdmin)
from django.utils.translation import gettext_lazy as _

from imagekit.admin import AdminThumbnail

from core.imagegenerators import cached_list_thumb
from .models import Group, User, DjangoBaseGroup


# Django's default Group Model is unregistered from admin
# inorder to register custom one below
admin.site.unregister(DjangoBaseGroup)


@admin.register(User)
class UserAdmin(DjangoBaseUserAdmin):
    """Django's default User Admin is overriden"""
    save_on_top = True
    search_fields = ('username', 'first_name', 'last_name', 'email')

    list_filter = ('is_staff', 'is_superuser', 'is_active')
    list_display = ('admin_thumbnail', 'username',
                    'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username',)
    readonly_fields = ('admin_thumbnail', 'date_joined', 'last_login')

    admin_thumbnail = AdminThumbnail(image_field=cached_list_thumb)
    fieldsets = (
        ('', {
            'fields': ('username', 'password')
        }),
        (_('Personal info'), {
            'fields': (('first_name', 'last_name'), 'email',
                       ('admin_thumbnail', 'image'))
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions')
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )


@admin.register(Group)
class GroupAdmin(DjangoBaseGroupAdmin):
    """Django's default Group Admin is overriden"""
