from django.urls import re_path

from .views import DetailVideoView

app_name = 'video'
urlpatterns = [
    re_path('detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)$', DetailVideoView.as_view(), name='detail_video')
]
