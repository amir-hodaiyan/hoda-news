from django.urls import re_path

from news.views import DetailsNews

app_name = 'News'
urlpatterns = [
    re_path(r'^(?P<id>[0-9]+)/(?P<slug>[-\w]+)$', DetailsNews.as_view(), name='details'),  # detail news
]
