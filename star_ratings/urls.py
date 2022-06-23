from __future__ import unicode_literals
from django.urls import re_path
from . import app_settings
from .views import Rate

app_name = 'star_ratings'
urlpatterns = [
    re_path(r'(?P<content_type_id>\d+)/(?P<object_id>' + app_settings.STAR_RATINGS_OBJECT_ID_PATTERN + ')/',
            Rate.as_view(), name='rate'),
]

