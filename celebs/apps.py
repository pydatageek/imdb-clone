from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CelebsConfig(AppConfig):
    name = 'celebs'
    verbose_name = _('Celeb')