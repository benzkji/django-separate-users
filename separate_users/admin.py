from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.http import JsonResponse

from separate_users.models import FrontendUser, Editor


# admin.site.unregister(get_user_model())


class FrontendUserAdmin(UserAdmin):
    readonly_fields = ['date_joined', 'last_login', 'is_staff', 'is_superuser', 'groups', 'user_permissions', ]
    list_filter = ['is_active', 'groups', ]
    list_display = ['username', 'is_active', ]


admin.site.register(FrontendUser, FrontendUserAdmin)


class EditorAdmin(UserAdmin):
    exclude = []
    readonly_fields = ['date_joined', 'last_login', 'is_staff', 'is_superuser', 'user_permissions', ]
    list_filter = ['is_active', 'groups', ]
    list_display = ['username', 'is_active', ]


admin.site.register(Editor, EditorAdmin)
