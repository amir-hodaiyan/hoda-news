from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from base.models import CategoryModel
from comment.form import CommentForm
from .models import NewsModel


class DetailsNews(View):
    template_name = 'news_app/detail_news.html'
    from_class = CommentForm

    def save_count_visit_post(self, post):
        ip_client = self.request.user.ip

        if ip_client not in post.ip_address.all():
            post.ip_address.add(ip_client)

    def setup(self, request, *args, **kwargs):
        id_ = kwargs['id']
        slug_ = kwargs['slug']
        self.news = get_object_or_404(NewsModel, status=True, slug=slug_, id=id_)
        comment = get_object_or_404(NewsModel, status=True, slug=slug_, id=id_).comments.filter(status=True)
        self.context = {'details': self.news, 'comments': comment, 'id': id_}
        return super().setup(request, *args, **kwargs)

    def get(self, request, **kwargs):
        self.save_count_visit_post(self.news)
        context = self.context
        context.update({'form': self.from_class})
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.news_id = kwargs['id']
            new_form.save()
            messages.success(request, _('Your message has been successfully sent.'), 'success')
            return redirect('News:details', kwargs['id'], kwargs['slug'])
        else:
            context = self.context
            context.update({'form': form})
            return render(request, self.template_name, context)


class CategoryNews(ListView):
    template_name = 'news_app/category_news.html'

    def get_queryset(self, *args, **kwargs):
        slug_category = self.kwargs['slug']

        list_data = get_object_or_404(CategoryModel, slug=slug_category, status=True).news.filter(status=True)
        paginator = Paginator(list_data, 6)
        page_number = self.request.GET.get('p')
        category_news = paginator.get_page(page_number)
        return [category_news, paginator]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'category_title': get_object_or_404(CategoryModel, slug=self.kwargs['slug'], status=True).title,
            'paginator_': self.get_queryset()[1],
            'category_news': self.get_queryset()[0]
        })
        return context
