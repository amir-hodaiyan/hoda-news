from django import template
from plagin import utils
from plagin.utils import jpublish_, publish_

register = template.Library()


@register.simple_tag
def current_date(lang_code):
    if lang_code == 'fa':
        return utils.current_jalali_data()
    else:
        return utils.current_date()


@register.simple_tag
def jalali_date(datetime, lang_code):
    if lang_code == 'fa':
        return jpublish_(datetime)
    else:  # lang_code == 'en':
        return publish_(datetime)
