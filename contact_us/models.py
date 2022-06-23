from django.utils.translation import gettext_lazy as _
from plagin.utils import jpublish_
from django.db import models


class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = _('ContactUs')
        ordering = ['-reviewed', '-created']
        db_table = 'contact_us'

    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'))
    subject = models.CharField(_('subject'), max_length=100)
    massage = models.TextField(_('massage'))
    created = models.DateTimeField(_('created date'), auto_now_add=True)
    reviewed = models.BooleanField(_('reviewed'), default=False)

    def __str__(self):
        return self.subject
