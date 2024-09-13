from django.conf import settings
from django.contrib.auth.models import UserManager
from django.core.exceptions import AppRegistryNotReady, ImproperlyConfigured
from django.contrib.auth import get_user_model


try:
    UserModel = get_user_model()
except AppRegistryNotReady:
    if not settings.AUTH_USER_MODEL == 'auth.User':
        raise(ImproperlyConfigured(
            'django-separate-users and django<1.11 wont work with custom user models!'
        ))
    from django.contrib.auth.models import User
    UserModel = User


if not getattr(settings, 'MIGRATION_MODULES', {}).get('separate_users', None):
    raise (ImproperlyConfigured(
        'django-separate-users needs an entry in settings.MIGRATION_MODULES["separate_users"]'
        ' = "your_app", it will write migrations into a pip installed app, otherwise!'
    ))


class FrontendUserManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_staff=False, is_superuser=False)


class EditorManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True, is_superuser=False)


class NonSuperUserManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=False)


class SeparateUserBase(object):

    class Meta:
        proxy = True

    def get_groups(self):
        return ', '.join([str(item) for item in self.groups.all()])

    get_groups.short_description = ("Groups")

    def get_complete_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    get_complete_name.short_description = ("Name")


class FrontendUser(SeparateUserBase, UserModel):

    objects = FrontendUserManager()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.is_staff = False
        super().save(*args, **kwargs)


class Editor(SeparateUserBase, UserModel):

    objects = EditorManager()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.is_staff = True
        super().save(*args, **kwargs)

    class Meta:
        proxy = True


class NonSuperUser(SeparateUserBase, UserModel):

    objects = NonSuperUserManager()

    class Meta:
        proxy = True
        verbose_name = "User"
        verbose_name_plural = "Users"
