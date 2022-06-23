from django.urls import path

from .views import ContactUsView

app_name = 'ContactUs'
urlpatterns = [
    path("", ContactUsView.as_view(), name="contact_us")
]
