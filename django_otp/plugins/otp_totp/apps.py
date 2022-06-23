from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DefaultConfig(AppConfig):
    name = 'django_otp.plugins.otp_totp'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = _('OTP')
