from django.shortcuts import render
from django.views import View

from base.context_processors import config_news_model
from base.models import CategoryModel
from photo.models import PhotoNewsModel


class HomeView(View):
    template_name = 'home/index.html'

    def get(self, request, **kwargs):
        context = {
            'list_category_published_in_home': CategoryModel.objects.filter(publish_in_home=True, status=True),
            'number_of_news_in_category': config_news_model(3),
            'sliders': PhotoNewsModel.objects.filter(status=True, is_slider_home=True),
            'image_post1': PhotoNewsModel.objects.filter(status=True, important_photo_home=1),
            'image_post2': PhotoNewsModel.objects.filter(status=True, important_photo_home=2),
            'image_post3': PhotoNewsModel.objects.filter(status=True, important_photo_home=3)
        }
        return render(request, self.template_name, context)
