from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_app'
    verbose_name = _("Yangiliklar")
