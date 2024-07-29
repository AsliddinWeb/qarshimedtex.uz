from modeltranslation.translator import register, TranslationOptions

from .models import Slider, HomeAbout, HomeTitles, HomeCourses, HomeLeader, FaqTitle, Faq, Partner, ContactUs, Message

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('cap_title', 'title', 'body', 'button_text', 'image_alt')

@register(HomeAbout)
class HomeAboutTranslationOptions(TranslationOptions):
    fields = ('count_title', 'title', 'body', 'title_1', 'body_1', 'title_2', 'body_2', 'two_body', 'quote', 'cap_title', 'alt')

@register(HomeTitles)
class HomeTitlesTranslationOptions(TranslationOptions):
    fields = (
        'news_cap', 'news_title',
        'courses_cap', 'courses_title',
        'news2_cap', 'news2_title',
        'liders_cap', 'liders_title',
        'faq_cap', 'faq_title',
        'partners_cap', 'partners_title'
    )

@register(HomeCourses)
class HomeCoursesTranslationOptions(TranslationOptions):
    fields = ('cap_title', 'title', 'body')

@register(HomeLeader)
class HomeLeaderTranslationOptions(TranslationOptions):
    fields = ('title', 'position')

@register(FaqTitle)
class FaqTitleTranslationOptions(TranslationOptions):
    fields = ('cap_title', 'title')

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ContactUs)
class ContactUsTranslationOptions(TranslationOptions):
    fields = ('cap_title', 'title', 'name', 'message', 'body')
