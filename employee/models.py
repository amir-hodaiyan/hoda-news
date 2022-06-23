from django.core.validators import MinValueValidator
from django.db import models
from plagin.utils import jpublish_
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

ROL_CHOICES = (('w', _('writer')), ('p', _('photographer')))


class EmployeesModel(models.Model):
    class Meta:
        verbose_name_plural = _('employees')
        verbose_name = _('employee')
        ordering = ['-last_name']
        db_table = 'employee'

    first_name = models.CharField(_('First Name'), max_length=20)
    last_name = models.CharField(_('Last Name'), max_length=50)
    bio = models.TextField(_('Bio'))
    profile_photo = models.ImageField(_('Profile photo'), upload_to='employee/%Y/%m')
    membership_date = models.DateField(_('Membership date'))
    rol = models.CharField(_('Rol'), choices=ROL_CHOICES, max_length=1, default='w')
    counter = models.IntegerField(_('Quantity'), default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def thumbnail(self):
        return format_html(
            f'<img src="{self.profile_photo.url}" '
            f'alt="{self.profile_photo}" style="width: 90px; height: 80;border-radius: 3px">')

    def jalali_membership(self):
        return jpublish_(self.membership_date)

    thumbnail.short_description = _('thumbnail')
    jalali_membership.short_description = _('membership date')
