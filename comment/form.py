from captcha.fields import CaptchaField
from django import forms

from .models import CommentModel


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = CommentModel
        fields = ['comment', 'full_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
