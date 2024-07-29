from modeltranslation.translator import register, TranslationOptions

from .models import *

@register(SeoSettings)
class SeoSettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'keywords', 'description', 'author')

@register(HeaderSettings)
class HeaderSettingsTranslationOptions(TranslationOptions):
    fields = ('bot', 'logo_alt', 'right_button_title', 'search_placeholder')

@register(FooterSettings)
class FooterSettingsTranslationOptions(TranslationOptions):
    fields = ('body', 'copyright')

@register(FooterLinkCategory)
class FooterLinkCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(FooterLink)
class FooterLinkTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'location')

@register(SocialSettings)
class SocialSettingsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(MoreTitles)
class MoreTitlesTranslationOptions(TranslationOptions):
    fields = ('home', 'related_news', 'news_page', 'search_title', 'news_category_title', 'social_title', 'empty_news')

@register(ErrorTexts)
class ErrorTextsTranslationOptions(TranslationOptions):
    fields = ('error_404_title', 'error_404_body', 'error_500_title', 'error_500_body')