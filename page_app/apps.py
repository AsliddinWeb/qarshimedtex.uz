from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PageAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'page_app'
    verbose_name = _("Sahifalar")

