from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee'
    verbose_name = _('employee')
