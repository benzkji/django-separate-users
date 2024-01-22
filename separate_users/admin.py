from django.urls import re_path
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from separate_users.models import FrontendUser, Editor


# admin.site.unregister(get_user_model())

class SeparateUserAdminBase(UserAdmin):

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
    readonly_fields = ['date_joined', 'last_login', 'is_superuser', 'groups', 'user_permissions', ]
    list_filter = ['is_active', 'groups', ]
    list_display = ['username', 'get_complete_name', 'is_active', 'get_groups', ]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm('separate_users.change_editor'):
            return self.readonly_fields + ['is_staff']
        return self.readonly_fields


admin.site.register(FrontendUser, FrontendUserAdmin)


class EditorAdmin(SeparateUserAdminBase):
    exclude = []
    readonly_fields = ['date_joined', 'last_login', 'is_superuser', 'user_permissions', ]
    list_filter = ['is_active', 'groups', ]
    list_display = ['username', 'get_complete_name', 'is_active', 'get_groups', ]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm('separate_users.change_frontenduser'):
            return self.readonly_fields + ['is_staff']
        return self.readonly_fields

admin.site.register(Editor, EditorAdmin)
