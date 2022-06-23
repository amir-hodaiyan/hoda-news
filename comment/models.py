from django.db import models
from django.utils.translation import gettext_lazy as _

from news.models import NewsModel
from plagin.utils import jpublish_


class CommentModel(models.Model):
    class Meta:
        verbose_name_plural = _('comments')
        verbose_name = _('comment')
        ordering = ['-created']
        db_table = 'comment'

    comment = models.TextField(_('comment'))
    re_comment = models.TextField(_('recommend'), null=True, blank=True)
    full_name = models.CharField(_('full name'), max_length=80)
    email = models.EmailField(_('email'))
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, related_name='comments', verbose_name=_('news'))
    status = models.BooleanField(_('status publish'), default=False)
    is_ready = models.BooleanField(_('is ready?'), default=False)
    created = models.DateTimeField(_('created date'), auto_now_add=True)
    update = models.DateTimeField(_('update date'), auto_now=True)

    def __str__(self):
        return self.comment[0:15]

    def comment_admin(self):
        return self.comment[0:20]

    def re_comment_admin(self):
        re_comment = self.re_comment
        if re_comment is not None:
            return re_comment[0:20]

    def jalali_created(self):
        return jpublish_(self.created)

    def jalali_update(self):
        return jpublish_(self.update)

    re_comment_admin.short_description = _('recommend')
    comment_admin.short_description = _('comment')
