from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ConfigNewsModel, NewsModel


@admin.action(description=_('Become hot news'))
def do_hot_news(model_admin, request, queryset):
    queryset.update(hotNews=True)
    model_admin.message_user(request, _('Selections become hot news'))


@admin.action(description=_('Become normally news'))
def not_hot_news(model_admin, request, queryset):
    queryset.update(hotNews=False)
    model_admin.message_user(request, _('Selected items become normal news'))


@admin.action(description=_('Editor Selection'))
def editor_selection(model_admin, request, queryset):
    queryset.update(editor_selection=True)
    model_admin.message_user(request, _('Marked items added to Editor Selection.'))


@admin.action(description=_('No editor selected'))
def not_editor_selection(model_admin, request, queryset):
    queryset.update(editor_selection=False)
    model_admin.message_user(request, _('Marked items removed from Editor Selection.'))


@admin.action(description=_('Publish selected items'))
def make_published(model_admin, request, queryset):
    queryset.update(status=True)
    model_admin.message_user(request, _('Selections published.'))


@admin.action(description=_('Draft Selected Items'))
def make_drafted(model_admin, request, queryset):
    queryset.update(status=False)
    model_admin.message_user(request, _('Selected items were drafted.'))


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail', 'writer', 'number_of_visit', 'get_category',
                    'editor_selection', 'hotNews', 'status']

    list_filter = ['updated', 'writer', 'status', 'hotNews', 'editor_selection']
    search_fields = ['title', 'body']
    actions = [make_published, make_drafted, do_hot_news, not_hot_news, editor_selection, not_editor_selection]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['updated', 'created']

    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = ('title', f'title_{not_lang_code}', 'slug', 'body', f'body_{not_lang_code}', 'image',
                               'category', 'writer', 'status', 'hotNews', 'editor_selection', 'updated', 'created')
        fieldsets = ((None, {'fields': list_generic_config}),)
        return fieldsets


@admin.register(ConfigNewsModel)
class ConfigNewsAdmin(admin.ModelAdmin):
    list_display = ['number_most_views', 'number_category_news',
                    'number_editor_selection_news', 'status_admin']
