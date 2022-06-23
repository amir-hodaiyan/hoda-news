from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from re import compile


def tel_validators(tel):
    regex = compile(r'^09\d{9}$')
    if not regex.match(tel):
        raise ValidationError(_('You must enter a phone number.'))
