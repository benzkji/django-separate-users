from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SeparateUsersConfig(AppConfig):
    name = 'separate_users'
    verbose_name = _("Users")
