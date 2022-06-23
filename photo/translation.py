from modeltranslation.translator import register, TranslationOptions
from .models import PhotoModel, PhotoNewsModel


@register(PhotoModel)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PhotoNewsModel)
class PhotoNewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
