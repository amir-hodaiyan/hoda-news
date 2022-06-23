from django.core.validators import FileExtensionValidator
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from base.models import CategoryModel, IpAddressModel
from plagin.utils import jpublish_
from django.utils.translation import get_language


class ConfigVideoModel(models.Model):
    STATUS_CHOICES = (
        ('p', _('publish')),
        (None, _('draft'))
    )

    class Meta:
        verbose_name_plural = _('configs')
        verbose_name = _('config')
        db_table = 'video_config'

    qty_most_views = models.PositiveSmallIntegerField(_('Most viewed'),
                                                      help_text=_('Number of videos in the most viewed.'))
    qty_video_in_page = models.PositiveSmallIntegerField(_('Every Page'),
                                                         help_text=_('Number of videos in the every page.'))
    status = models.CharField(_('Status'), choices=STATUS_CHOICES, unique=True, max_length=9, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class VideoPostModel(models.Model):
    video_validators = FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])
    POSITION_VIDEO = (
        (None, '-'),
        ('0', _('Main')),
        ('1', _('subsidiary1')),
        ('2', _('subsidiary2')),
        ('3', _('subsidiary3')),
        ('4', _('subsidiary4')),
    )

    class Meta:
        verbose_name_plural = _('News movies')
        verbose_name = _('News movie')
        ordering = ['status', '-created']
        db_table = 'video_post'

    title_video = models.CharField(_('Title video'), max_length=100)
    slug_video = models.SlugField(_('Slug video'), unique=True, allow_unicode=True)
    description_video = models.TextField(_('Description video'))
    poster_video = models.ImageField(_('Poster Video'), upload_to='video/poster/%Y/%m')
    video = models.FileField(_('Video'), upload_to='video/video/%Y/%m', validators=[video_validators])
    category = models.ManyToManyField(CategoryModel, related_name='video', verbose_name=_('Category'))
    ip_address = models.ManyToManyField(IpAddressModel, blank=True, editable=False, verbose_name=_('Visit'))
    updated = models.DateTimeField(_('Updated date'), auto_now=True)
    created = models.DateTimeField(_('Created date'), auto_now_add=True)
    is_important_video = models.BooleanField(_('Important videos'), default=False)
    position = models.CharField(_('Position'), unique=True, null=True, blank=True, max_length=8, choices=POSITION_VIDEO)
    status = models.BooleanField(_('Status'), default=True)

    def __str__(self):
        return self.title_video

    def get_absolute_url(self):
        return reverse("video:detail_video", kwargs={'id': self.id, 'slug': self.slug_video})

    def category_str(self):
        return ', '.join(([str(category_) for category_ in self.category.all()]))

    def jpublish(self):
        if get_language() == 'fa':
            return jpublish_(self.updated)
        else:
            return self.updated.strftime('%Y/%m/%d')

    def number_visit(self):
        return self.ip_address.count()

    def thumbnail(self):
        return format_html(
            f'<img src="{self.poster_video.url}" alt="{self.title_video}"'
            f' style="width: 90px; height: 80; border-radius: 3px">')

    thumbnail.short_description = _('thumbnail')
    number_visit.short_description = _('visit')
    jpublish.short_description = _('Publication date')
    category_str.short_description = _('category')
