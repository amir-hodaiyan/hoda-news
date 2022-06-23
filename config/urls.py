from account.config import site_header, site_title
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

admin.site.site_header = site_header
admin.site.site_title = site_title

# from django_otp.admin import OTPAdminSite
# admin.site.__class__ = OTPAdminSite

urlpatterns = i18n_patterns(
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('captcha/', include('captcha.urls')),
    path('4F2W9EG1VEEFFE4KMVI47FPD/', admin.site.urls),
    path('photo-service/', include('photo.urls')),
    path('video-service/', include('video.urls')),
    path('details-news/', include('news.urls')),
    path('contact-us/', include('contact_us.urls')),
    path('employee/', include('employee.urls')),
    path('account/', include("account.urls")),
    path('', include('home.urls')))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
