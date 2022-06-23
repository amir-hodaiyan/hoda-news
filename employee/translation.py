from modeltranslation.translator import register, TranslationOptions

from .models import EmployeesModel


@register(EmployeesModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'bio')
