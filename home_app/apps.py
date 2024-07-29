from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_app'
    verbose_name = _("Bosh sahifa sozlamalari")
