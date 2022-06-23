from modeltranslation.translator import register, TranslationOptions

from .models import CategoryModel, SocialNetworkModel, FooterModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(SocialNetworkModel)
class SocialNetworkTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FooterModel)
class FooterTranslationOptions(TranslationOptions):
    fields = ('description',)
