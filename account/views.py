from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import views, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, ResetForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(views.LoginView):
    template_name = 'account/login/login.html'
    form_class = LoginForm

    def get_success_url(self):
        messages.success(self.request, _("You are successfully Login."), 'success')
        return reverse_lazy('Home:home')


class LogoutView(View):

    @staticmethod
    def get(request):
        logout(request)
        messages.success(request, _("You are successfully logout."), 'success')
        return redirect('Home:home')


class ChangePasswordDoneView(LoginRequiredMixin, views.TemplateView):
    template_name = 'account/change_password/change_password_done.html'


class ChangePasswordView(LoginRequiredMixin, views.PasswordChangeView):
    template_name = 'account/change_password/change_password.html'
    success_url = reverse_lazy('Account:change_password_done')


class SignupView(View):
    template_class = 'account/sign_up/sign_up.html'
    from_class = SignUpForm

    def get(self, request):
        return render(request, self.template_class, {'form': self.from_class})

    def post(self, request):
        form = self.from_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your registration was successful.'), 'success')
            return redirect('Account:login')
        return render(request, self.template_class, {'form': form})


class ForgetPassword(views.PasswordResetView, views.TemplateView):
    form_class = ResetForm
    success_url = reverse_lazy('Account:password_reset_done')
    email_template_name = 'account/forget_password/password_reset_email.html'
    template_name = 'account/forget_password/password_reset.html'


class PasswordResetDon(views.PasswordResetDoneView, views.TemplateView):
    template_name = 'account/forget_password/password_reset_don.html'


class PasswordResetConfirm(views.PasswordResetConfirmView):
    template_name = 'account/forget_password/password_reset_confirm.html'
    success_url = reverse_lazy('Account:password_reset_complete')


class PasswordResetComplete(views.PasswordResetCompleteView):
    template_name = 'account/forget_password/password_reset_complete.html'
