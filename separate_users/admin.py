from ansible.plugins.lookup import password
from django.urls import re_path
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q

from separate_users.models import FrontendUser, Editor, NonSuperUser
from . import conf


class HasPasswordFilter(admin.SimpleListFilter):
    title = ("password")
    parameter_name = "pw"

    def lookups(self, request, model_admin):
        lookups = (
            ("set","is set"),
            ("empty","empty"),
        )
        return lookups


    # def custom_queryset(self, request, queryset, filter_value):
    #     queryset = queryset.filter(assignement__status=filter_value)
    #     if not request.user.has_perm("baspo_sig.full_change_assignement"):
    #         queryset = queryset.filter(
    #             assignement__assignee=request.user,
    #         )
    #     return queryset
    #
    def queryset(self, request, queryset):
        if self.value() == 'set':
            return queryset.exclude(password='').exclude(password=None)
        elif self.value() == 'empty':
            return queryset.filter(Q(password='') | Q(password=None))
        else:
            return queryset



class SeparateUserAdminBase(UserAdmin):
    list_display = ['username', 'get_complete_name', 'is_active', 'get_groups', "last_login"]
    list_filter = ['is_active', HasPasswordFilter,  'groups', ]

    def get_urls(self):
        model_name_lower = self.model.__name__.lower()
        return [
            re_path(
                r'^(.+)/password/$',
                self.admin_site.admin_view(self.user_change_password),
                name='separate_users_{}_password_change'.format(model_name_lower),
            ),
        ] + super(SeparateUserAdminBase, self).get_urls()


class FrontendUserAdmin(SeparateUserAdminBase):
    readonly_fields = ['date_joined', 'last_login', 'groups', 'user_permissions', 'is_superuser']

    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm('separate_users.change_editor'):
            return self.readonly_fields + ['is_staff']
        return self.readonly_fields


class EditorAdmin(SeparateUserAdminBase):
    readonly_fields = ['date_joined', 'last_login', 'user_permissions', 'is_superuser']

    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm('separate_users.change_frontenduser'):
            return self.readonly_fields + ['is_staff']
        return self.readonly_fields


class NonSuperUserAdmin(SeparateUserAdminBase):
    readonly_fields = ['date_joined', 'last_login', 'user_permissions', 'is_superuser']


if conf.NON_SUPERUSER_MODE == True:
    admin.site.register(NonSuperUser, NonSuperUserAdmin)
else:
    admin.site.register(FrontendUser, FrontendUserAdmin)
    admin.site.register(Editor, EditorAdmin)
