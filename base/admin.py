from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


@admin.action(description=_('Publish selected items.'))
def make_published(model_admin, request, queryset):
    queryset.update(status=True)
    model_admin.message_user(request, _('Published selected items.'))


@admin.action(description=_('Draft selected items.'))
def make_drafted(model_admin, request, queryset):
    queryset.update(status=False)
    model_admin.message_user(request, _('Drafted selected items.'))


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['positions', 'title', 'status', 'parent', 'have_children']
    list_filter = ['status', 'parent', 'have_children']
    actions = [make_published, make_drafted]

    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = ('slug', 'title', f'title_{not_lang_code}',
                               'parent', 'positions', 'status', 'have_children', 'publish_in_home')
        fieldsets = ((None, {'fields': list_generic_config}),)
        return fieldsets


@admin.register(SocialNetworkModel)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    actions = [make_published, make_drafted]

    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = ('title', f'title_{not_lang_code}', 'class_icon', 'address', 'status')
        fieldsets = ((None, {'fields': list_generic_config}),)
        return fieldsets


@admin.register(FooterModel)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['tel', 'email', 'thumbnail', 'status']
    actions = [make_published, make_drafted]

    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = ('description', f'description_{not_lang_code}', 'tel', 'email', 'logo', 'status')
        fieldsets = ((None, {'fields': list_generic_config}),)
        return fieldsets
