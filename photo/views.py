from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from photo.models import PhotoNewsModel


class PhotoNewView(ListView):
    template_name = 'photo/photo_category.html'

    def get_queryset(self):
        slider = PhotoNewsModel.objects.filter(status=True, is_important_photo=True)
        photo_news_all = PhotoNewsModel.objects.filter(status=True, is_important_photo=False)

        return slider, photo_news_all

    def get_context_data(self, **kwargs):
        data = self.get_queryset()[1]
        pagination = Paginator(data,3)
        photo_page = pagination.get_page(self.request.GET.get('p'))

        context = super().get_context_data(**kwargs)
        context.update({'sliders': self.get_queryset()[0], 'last_photo': photo_page, 'paginator_': pagination})
        return context


class DetailPhotoView(ListView):
    template_name = 'photo/detail_photo.html'

    def get_queryset(self, **kwargs):
        photo_news = get_object_or_404(PhotoNewsModel, status=True, id=self.kwargs['id'], slug=self.kwargs['slug'])
        detail_photo_news = photo_news.sub_photo.filter(status=True)
        return photo_news, detail_photo_news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'detail_photo_news': self.get_queryset()[1], 'body_photo_news': self.get_queryset()[0]})
        return context
