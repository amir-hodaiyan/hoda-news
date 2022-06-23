from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from plagin.utils import jpublish_

from base.models import IpAddressModel, CategoryModel
from employee.models import EmployeesModel


class ConfigNewsModel(models.Model):
    STATUS_CHOICES = (('p', _('Apply config')), (None, _('Draft config')))

    class Meta:
        verbose_name_plural = verbose_name = _('Config news')

    number_most_views = models.PositiveSmallIntegerField(_('Quantity most view'))
    number_category_news = models.PositiveSmallIntegerField(_('Quantity category news'))
    number_hot_news = models.PositiveSmallIntegerField(_('Quantity hot news'))
    number_editor_selection_news = models.PositiveSmallIntegerField(_('Quantity editor selection news'))

    status = models.CharField(_('Apply config'), choices=STATUS_CHOICES, unique=True, max_length=9, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def status_admin(self):
        if self.status:
            return format_html(f'<b style="color: green;font-size: 14px">{_("yes")}</b>')
        return format_html(f'<b style="color: red;font-size: 14px">{_("No")}</b>')

    status_admin.short_description = _('Is Apply config?')


class NewsModel(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = _('News')
        ordering = ['status', '-updated']
        db_table = 'news'

    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), allow_unicode=True, unique=True)
    body = models.TextField(_('body'))
    image = models.ImageField(_('image'), upload_to='news/%Y/%m')
    ip_address = models.ManyToManyField(IpAddressModel, blank=True, related_name='visit', editable=False,
                                        verbose_name=_('ip address'))

    category = models.ManyToManyField(CategoryModel, related_name='news', verbose_name=_('category'))

    writer = models.ForeignKey(EmployeesModel, on_delete=models.CASCADE, related_name='news_writer', verbose_name=_('writer'))

    status = models.BooleanField(_('status published'))
    hotNews = models.BooleanField(_('hot news'), default=False)
    editor_selection = models.BooleanField(_('editor selection'), default=False)
    updated = models.DateTimeField(_('updated date'), auto_now=True)
    created = models.DateTimeField(_('created date'), auto_now=True)

    def __str__(self):
        return self.title

    def number_of_visit(self):
        return self.ip_address.count()

    def thumbnail(self):
        return format_html(
            f'<img src="{self.image.url}" alt="{self.title}" style="width: 90px; height: 80; border-radius: 3px">')

    def get_category(self):
        return ' , '.join([str(category_) for category_ in self.category.all()])

    def get_slug_category(self):
        title_news = self.category.all()[0]
        return CategoryModel.objects.get(title=title_news).slug

    def get_absolute_url(self):
        return reverse('News:details', kwargs={'id': self.id, 'slug': self.slug})

    def jalali_update(self):
        return jpublish_(self.updated)

    jalali_update.short_description = _('update date')
    get_category.short_description = _('category')
    thumbnail.short_description = _('thumbnail')
    number_of_visit.short_description = _('number of visited')
