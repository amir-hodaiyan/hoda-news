from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactUsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_us'
    verbose_name = _('ContactUs')
