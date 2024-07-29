from modeltranslation.translator import register, TranslationOptions

from .models import NavType, OneNavbar, TwoNavbar, ThreeNavbar

@register(NavType)
class NavTypeTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(OneNavbar)
class OneNavbarTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(TwoNavbar)
class TwoNavbarTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ThreeNavbar)
class ThreeNavbarTranslationOptions(TranslationOptions):
    fields = ('title',)
