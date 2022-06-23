from django.core.validators import MaxValueValidator as Max
from django.core.validators import MinValueValidator as Min

from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from base.validators import tel_validators

STATUS_CHOICES = (
    ('p', _('Apply')),
    (None, _('Draft'))
)


class CategoryModel(models.Model):
    class Meta:
        verbose_name_plural = _('categories')
        verbose_name = _('category')
        ordering = ['positions', '-status', '-title']
        db_table = 'category'

    slug = models.SlugField(_('Slug category'), max_length=50, unique=True)
    title = models.CharField(_('Title category'), max_length=100)
    parent = models.ForeignKey('self', verbose_name=_('Parent category'), related_name='children',
                               null=True, blank=True, on_delete=models.SET_NULL)
    positions = models.IntegerField(_('Category position'), unique=False)
    status = models.BooleanField(_('Status published'), default='p')
    have_children = models.BooleanField(_('Have children?'), default=False)
    publish_in_home = models.BooleanField(_('Publish in home?'), default=False,
                                          help_text=_('Publish the latest news of this category on the home page'))

    def __str__(self):
        return self.title


class IpAddressModel(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class SocialNetworkModel(models.Model):
    class Meta:
        verbose_name = _('SocialNetwork')
        verbose_name_plural = _('SocialNetworks')
        db_table = 'social_network'

    title = models.CharField(_('Title network'), max_length=80)
    class_icon = models.CharField(_('Font awesome class'), max_length=100)
    address = models.URLField(_('Address network'), unique=True)
    status = models.BooleanField(_('Status publish'), default=True)

    def __str__(self):
        return self.title


class FooterModel(models.Model):
    class Meta:
        verbose_name_plural = _('Footers')
        verbose_name = _('Footer')
        ordering = ['-status']
        db_table = 'footer'

    description = models.TextField(_('Description footer'))
    tel = models.CharField(_('Tel'), max_length=11, validators=[tel_validators])
    email = models.EmailField(_('Email'))
    logo = models.ImageField(_('Logo'), upload_to='footer')
    status = models.CharField(_('Status publish'), max_length=9, choices=STATUS_CHOICES,
                              default=None, null=True, blank=True, unique=True)

    def __str__(self):
        return _('footer config') + str(self.id)

    def thumbnail(self):
        return format_html(
            f'<img src="{self.logo.url}" style="width: 90px; height: 80; border-radius: 3px">')

    thumbnail.short_description = _('thumbnail')