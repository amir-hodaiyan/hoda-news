from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()


class ResetForm(PasswordResetForm):
    captcha = CaptchaField()
