from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import PhotoModel, PhotoNewsModel


@admin.action(description=_('Publish selected items'))
def make_published(model_admin, request, queryset):
    queryset.update(status=True)
    model_admin.message_user(request, _('Selected items were Published.'))


@admin.action(description=_('draft selected items'))
def make_drafted(model_admin, request, queryset):
    queryset.update(status=False)
    model_admin.message_user(request, _('Selected items were drafted.'))


@admin.register(PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail', 'status']
    list_filter = ['created', 'status']
    search_fields = ['title']
    actions = [make_published, make_drafted]
    readonly_fields = ['created']

    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = ('title', f'title_{not_lang_code}', 'image', 'status', 'created')
        fieldsets = ((None, {'fields': list_generic_config}),)
        return fieldsets


@admin.register(PhotoNewsModel)
class PhotoNewsAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = ('title', f'title_{not_lang_code}', 'slug', 'body', f'body_{not_lang_code}', 'photo',
                               'sub_photo', 'photographer', 'status', 'is_important_photo', 'created', 'updated')
        fieldsets = (
            (_('Main'), {'fields': list_generic_config}),
            (_('Home page'), {'fields': ('is_slider_home', 'important_photo_home')}))

        return fieldsets

    list_display = ('title', 'thumbnail', 'jalali_updated', 'name_photographer',
                    'is_important_photo', 'is_slider_home', 'status')

    list_filter = ('updated', 'photographer', 'status')

    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created', 'updated')
    filter_horizontal = ('sub_photo',)
    raw_id_fields = ('photographer',)
    actions = (make_published, make_drafted)
