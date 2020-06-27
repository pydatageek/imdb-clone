"""Custom User model and related models"""

from django.db import models
from django.contrib.auth.models import (
    AbstractUser, Group as DjangoBaseGroup)
from django.utils.translation import gettext_lazy as _

from core.helpers import get_extension, random_chars


def user_directory_path(instance, filename):
    file_and_ext = get_extension(filename)
    return f'users/{instance.id}/{file_and_ext[0].lower()} \
        -{random_chars(5)}{file_and_ext[1]}'


class User(AbstractUser):
    """Custom User Model inherited from Django's Abstract User model"""
    email = models.EmailField(
        _('email address'), unique=True)  # email is required

    image = models.ImageField(
        _('avatar'), upload_to=user_directory_path,
        blank=True, null=True,
        help_text=_('avatar AKA user image'))


class Group(DjangoBaseGroup):
    """Custom Group Model inherited from Django's default Group model"""
