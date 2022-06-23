from django.urls import path

from news.views import CategoryNews
from photo.views import PhotoNewView
from video.views import VideoView
from .views import HomeView

app_name = 'Home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('video-service', VideoView.as_view(), name='video'),  # video category
    path('photo-service', PhotoNewView.as_view(), name='photo'),  # video category
    path('<slug:slug>', CategoryNews.as_view(), name='category')  # category navbar
]
