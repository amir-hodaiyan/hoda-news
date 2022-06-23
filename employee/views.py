from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from news.models import NewsModel
from .models import EmployeesModel


class Writer(ListView):
    template_name = 'employee/writer.html'

    def get_queryset(self, **kwargs):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_writer = int(str(self.request.path)[-1:])
        page = self.request.GET.get('p')

        writer_obj = get_object_or_404(EmployeesModel, id=id_writer)
        list_all_news = NewsModel.objects.filter(status=True, writer=writer_obj)
        paginator = Paginator(list_all_news, 6)

        context.update({
            'list_post_every_writer': paginator.get_page(page),
            'writer': writer_obj,
            'id_writer': id_writer,
        })
        return context
