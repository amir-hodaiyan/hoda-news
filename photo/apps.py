from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PhotoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photo'
    verbose_name = _('photo news')
