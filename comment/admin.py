from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import CommentModel


@admin.action(description=_('Convert to read comments'))
def make_ready(model_admin, request, queryset):
    queryset.update(is_ready=True)
    model_admin.message_user(request, _('Selected comments were read.'))


@admin.action(description=_('Convert to unread comments.'))
def make_unready(model_admin, request, queryset):
    queryset.update(is_ready=False)
    model_admin.message_user(request, _('Selected comments were unread.'))


@admin.action(description=_('Publish selected comments.'))
def make_published(model_admin, request, queryset):
    queryset.update(status=True)
    model_admin.message_user(request, _('The selected comments were published.'))


@admin.action(description=_('Draft Selected comments'))
def make_drafted(model_admin, request, queryset):
    queryset.update(status=False)
    model_admin.message_user(request, _('The selected comments were drafted.'))


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'comment', 're_comment', 'status', 'is_ready']
    list_filter = ['created', 'status', 'is_ready']
    search_fields = ['full_name', 'email', 'comment', 're_comment']
    actions = [make_published, make_drafted, make_ready, make_unready]
