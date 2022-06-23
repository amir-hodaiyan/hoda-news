from django.urls import path

from .views import *

app_name = 'Account'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('sign-up', SignupView.as_view(), name='sign_up'),

    path('change-password', ChangePasswordView.as_view(), name='change_password'),
    path('change-password-done', ChangePasswordDoneView.as_view(), name='change_password_done'),

    path('password-reset-done', PasswordResetDon.as_view(), name='password_reset_done'),
    path('forget-password', ForgetPassword.as_view(), name='forget'),

    path('password-reset/confirm/<uidb64>/<token>', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset-complete', PasswordResetComplete.as_view(), name='password_reset_complete')
]
