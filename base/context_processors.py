from .models import SocialNetworkModel, CategoryModel, FooterModel
from news.models import NewsModel, ConfigNewsModel
from django.shortcuts import get_object_or_404
from photo.models import PhotoNewsModel
from video.views import VideoView
from django.db.models import Count
from django.http import Http404
from video.models import VideoPostModel


def config_news_model(field_code):
    try:
        obj = get_object_or_404(ConfigNewsModel, status='p')
        filed = {
            2: obj.number_most_views,
            3: obj.number_category_news,
            4: obj.number_editor_selection_news,
            5: obj.number_hot_news
        }
        return filed[field_code]
    except Http404:  # Default
        return 6


def filter_true(obj):
    return obj.objects.filter(status=True)


def post(request):
    num_video = VideoView.config_video_post()[0]
    publish_video = VideoPostModel.objects.filter(status=True, ip_address__isnull=False)
    return {
        'social_networks': filter_true(SocialNetworkModel),
        'categories': filter_true(CategoryModel),
        'photo_service_count': PhotoNewsModel.objects.count(),
        'footer': FooterModel.objects.filter(status='p'),
        'hot_news': filter_true(NewsModel).filter(hotNews=True),
        'most_view_video': publish_video.annotate(num_visit=Count('ip_address')).order_by('-num_visit')[:num_video],
        'categories_footer': CategoryModel.objects.filter(have_children=False),
        'hot_news_footer': filter_true(NewsModel).filter(hotNews=True)[:config_news_model(5)],
        'editor_selection': filter_true(NewsModel).filter(editor_selection=True)[:config_news_model(4)],
        'most_view_news': filter_true(NewsModel).filter(ip_address__isnull=False).annotate(
            num_visit=Count('ip_address')).order_by('-num_visit')[:config_news_model(2)]}
