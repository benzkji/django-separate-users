from django.conf import settings
from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


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


class FrontendUser(UserModel):

    objects = FrontendUserManager()

    def save(self, *args, **kwargs):
        self.is_staff = False
        super(FrontendUser, self).save(*args, **kwargs)

    class Meta:
        proxy = True


class Editor(UserModel):

    objects = EditorManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        super(Editor, self).save(*args, **kwargs)

    class Meta:
        proxy = True