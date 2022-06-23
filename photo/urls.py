from django.urls import re_path

from .views import DetailPhotoView

app_name = 'Photo'
urlpatterns = [
    re_path(r'^detail-photo/(?P<id>\d+)/(?P<slug>[-\w]+)$', DetailPhotoView.as_view(), name='DetailPhoto'),

]
