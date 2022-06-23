from modeltranslation.translator import register, TranslationOptions
from .models import VideoPostModel


@register(VideoPostModel)
class VideoPostTranslation(TranslationOptions):
    fields = ('title_video', 'description_video')
