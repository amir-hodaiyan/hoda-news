from .models import ConfigVideoModel, VideoPostModel
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Count
from django.http import Http404


class VideoView(ListView):
    template_name = 'video/category_video_page.html'

    @staticmethod
    def config_video_post():
        # Config qty most view
        try:
            qty_most_views = get_object_or_404(ConfigVideoModel, status='p').qty_most_views
        except Http404:  # Default config
            qty_most_views = 8

        # Config qty video in page
        try:
            qty_video_in_page = get_object_or_404(ConfigVideoModel, status='p').qty_video_in_page
        except Http404:  # Default config
            qty_video_in_page = 8

        return qty_most_views, qty_video_in_page

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_post = VideoPostModel.objects.filter(status=True)

        list_video_post = VideoPostModel.objects.filter(status=True, is_important_video=False)
        number_video = self.config_video_post()[1]
        most_visit = self.config_video_post()[0]

        pagination = Paginator(list_video_post, number_video)
        page_number = self.request.GET.get('p')
        data_page = pagination.get_page(page_number)

        context.update({
            'more_videos': data_page,
            'paginator_': pagination,
            'top_video': video_post.filter(position=0, is_important_video=True),
            'top_left_video': video_post.filter(position__range=[1, 4], is_important_video=True),
            'most_visit_video': video_post.filter(ip_address__isnull=False).annotate(num_visit = Count('ip_address')).order_by('-num_visit')[0: most_visit]
            })
        return context


class DetailVideoView(ListView):
    template_name = 'video/detail_video_page.html'

    @staticmethod
    def get_size(bite_size):
        size = bite_size / 1024

        if size <= 1023:
            return f'{round(size, 2)}KB'
        else:
            size = size / 1024
            if size <= 1023:
                return f'{round(size, 2)}MB'
            else:
                size = size / 1024
                if size <= 1023:
                    return f'{round(size, 2)}GB'

    def get_queryset(self, **kwargs):
        video_obj = get_object_or_404(VideoPostModel, status=True, slug_video=self.kwargs['slug'], id=self.kwargs['id'])
        size_video = self.get_size(video_obj.video.size)

        ip_address = self.request.user.ip
        if ip_address not in video_obj.ip_address.all():
            video_obj.ip_address.add(ip_address)

        return video_obj, size_video, video_obj.ip_address.count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        video_post = VideoPostModel.objects.filter(status=True)
        most_visit = VideoView.config_video_post()[0]

        context.update({
            'details_video': queryset[0],
            'size': queryset[1],
            'number_of_visit': queryset[2],
            'most_visit_video': video_post.filter(ip_address__isnull=False).annotate(num_visit = Count('ip_address')).order_by('-num_visit')[0: most_visit]
        })
        return context
