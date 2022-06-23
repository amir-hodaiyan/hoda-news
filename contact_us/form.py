from captcha.fields import CaptchaField
from .models import ContactUs
from django import forms


class ContentUsForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ContactUs
        fields = "__all__"
