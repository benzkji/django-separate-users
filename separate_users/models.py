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
        return super(FrontendUserManager, self)\
            .get_queryset()\
            .filter(is_staff=False, is_superuser=False)


class EditorManager(UserManager):

    def get_queryset(self):
        return super(EditorManager, self)\
            .get_queryset()\
            .filter(is_staff=True, is_superuser=False)


class SeparateUserBase(object):

    class Meta:
        proxy = True

    def get_groups(self):
        return ', '.join([str(item) for item in self.groups.all()])

    get_groups.short_description = ("Groups")


class FrontendUser(SeparateUserBase, UserModel):

    objects = FrontendUserManager()

    def save(self, *args, **kwargs):
        self.is_staff = False
        super(FrontendUser, self).save(*args, **kwargs)


class Editor(SeparateUserBase, UserModel):

    objects = EditorManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        super(Editor, self).save(*args, **kwargs)

    class Meta:
        proxy = True
