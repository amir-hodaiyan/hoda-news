from modeltranslation.translator import register, TranslationOptions

from .models import NewsModel


@register(NewsModel)
class ConfigNewsMTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
