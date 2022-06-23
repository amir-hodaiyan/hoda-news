from random import randint

from django.contrib import admin
from django.db import IntegrityError
from django.utils.translation import gettext_lazy as _

from .models import VideoPostModel, ConfigVideoModel


@admin.action(description=_('Convert to important videos'))
def is_important_video(model_admin, request, queryset):
    queryset.update(is_important_video=True)
    model_admin.message_user(request, _('Selected videos have become important.'))


@admin.action(description=_('Convert to normal videos'))
def not_important_video(model_admin, request, queryset):
    queryset.update(is_important_video=False)
    model_admin.message_user(request, _('Selected videos have become normal.'))


@admin.action(description=_('Convert to publish videos'))
def make_published(model_admin, request, queryset):
    queryset.update(status=True)
    model_admin.message_user(request, _('Selected videos were published.'))


@admin.action(description=_('Convert to draft videos'))
def make_drafted(model_admin, request, queryset):
    queryset.update(status=False)
    model_admin.message_user(request, _('Selected videos were drafted.'))


@admin.action(description=_('Copy videos'))
def copy_items(model_admin, request, queryset):
    for query in queryset:
        new_query = query
        new_query.id = new_query.position = None
        while True:
            try:
                new_query.slug_video += str(randint(1, 1000))
                break
            except IntegrityError:
                continue
        new_query.save()
    model_admin.message_user(request, _('Selected videos were copied.'))


@admin.register(VideoPostModel)
class VideoPostAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = ('title_video', f'title_video_{not_lang_code}', 'slug_video', 'description_video',
                               f'description_video_{not_lang_code}', 'poster_video', 'video', 'category', 'status',
                               'created', 'updated')
        fieldsets = (
            (None, {'fields': list_generic_config}),
            (_('important-video'), {'fields': ('is_important_video', 'position')}))
        return fieldsets

    list_display = ('title_video', 'number_visit', 'thumbnail', 'jpublish',
                    'category_str', 'is_important_video', 'status', 'position')

    list_filter = ('created', 'status', 'is_important_video')
    search_fields = ('title_video', 'body')
    prepopulated_fields = {"slug_video": ("title_video",)}
    readonly_fields = ('created', 'updated')
    actions = [make_published, make_drafted, is_important_video, not_important_video, copy_items]


@admin.register(ConfigVideoModel)
class ConfigVideoAdmin(admin.ModelAdmin):
    list_display = ['qty_most_views', 'qty_video_in_page', 'status']
