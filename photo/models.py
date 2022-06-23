from django.utils.translation import gettext_lazy as _
from employee.models import EmployeesModel
from django.utils.html import format_html
from plagin.utils import jpublish_
from django.db import models
from django.urls import reverse


class PhotoModel(models.Model):
    class Meta:
        ordering = ['-status', '-created', 'title']
        verbose_name_plural = _('Photo')
        verbose_name = _('Photos')
        db_table = 'photo'

    title = models.CharField(_('title'), max_length=120)
    image = models.ImageField(_('image'), upload_to='Photo_news/%Y/%m')
    status = models.BooleanField(_('status publish'), default=False)
    created = models.DateTimeField(_('created date'), auto_now_add=True)

    def __str__(self):
        return self.title

    def thumbnail(self):
        return format_html(
            f'<img src="{self.image.url}" alt="" style="width: 90px; height: 80; border-radius: 3px">')

    thumbnail.short_description = _('thumbnail')


class PhotoNewsModel(models.Model):
    CHOICES_NEWS = (
        (None, _('-')),
        ('1', _('important image1')),
        ('2', _('important image2')),
        ('3', _('important image3'))
    )

    class Meta:
        verbose_name = verbose_name_plural = _('photo news')
        ordering = ['-status', '-updated', 'photographer']
        db_table = 'photo_news'

    title = models.CharField(_('title'), max_length=120)
    slug = models.SlugField(_('slug'), max_length=200, unique=True, allow_unicode=True)
    body = models.TextField(_('body'))
    photo = models.ImageField(_('main photo'), upload_to='photo_news/%Y/%m')
    sub_photo = models.ManyToManyField(PhotoModel, related_name='photo_news', verbose_name=_('more photo'))
    is_important_photo = models.BooleanField(_('important-photo'), default=False)
    status = models.BooleanField(_('status publish'), default=False)
    created = models.DateTimeField(_('created date'), auto_now_add=True)
    updated = models.DateTimeField(_('created date'), auto_now=True)

    photographer = models.ForeignKey(EmployeesModel, related_name='photo_news', on_delete=models.SET_NULL,
                                     null=True, verbose_name=_('photographer'))

    is_slider_home = models.BooleanField(_('Home slider'), default=False)
    important_photo_home = models.CharField(_('Important home photo'), max_length=1, choices=CHOICES_NEWS, blank=True,
                                            null=True, unique=True)

    def __str__(self):
        return self.title

    def jalali_updated(self):
        return jpublish_(self.updated)

    def jalali_created(self):
        return jpublish_(self.created)

    def name_photographer(self):
        return self.photographer

    def thumbnail(self):
        return format_html(
            f'<img src="{self.photo.url}" alt="{self.title}" style="width: 90px; height: 80; border-radius: 3px">')

    def get_absolute_url(self):
        return reverse('Photo:DetailPhoto', kwargs={'id': self.id, 'slug': self.slug})

    thumbnail.short_description = _('thumbnail')
    jalali_updated.short_description = _('updated date')
    jalali_created.short_description = _('created date')
    name_photographer.short_description = _('photographer')
