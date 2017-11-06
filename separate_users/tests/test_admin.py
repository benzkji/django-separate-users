# -*- coding: utf-8 -*-
# from django.test import override_settings
from django.test.testcases import TestCase
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from separate_users.models import Editor, FrontendUser
from separate_users.tests.utils.django_utils import create_superuser


class AdminTestCase(TestCase):
    """
    check some basic admin views
    TODO: check with custom User Model!
    """
    def setUp(self):
        self.auth_custom_user = 'test_app_custom_user.CustomUser'
        self.superuser = create_superuser()
        self.client.login(username='admin', password='secret')
        self.frontenduser = FrontendUser.objects.create(username='frontend')
        self.editor = Editor.objects.create(username='editor')

    def tearDown(self):
        pass

    def changelist(self, user_version):
        url = reverse('admin:separate_users_{}_changelist'.format(user_version))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_frontend_user_changelist(self):
        self.changelist('frontenduser')

    def test_editor_changelist(self):
        self.changelist('editor')

    # @override_settings(
    #     AUTH_USER_MODEL = 'test_app_custom_user.CustomUser'
    # )
    # def test_frontend_user_changelist_custom_user(self):
    #     self.changelist('frontenduser')
    #
    # @override_settings(
    #     AUTH_USER_MODEL = 'test_app_custom_user.CustomUser'
    # )
    # def test_editor_changelist_custom_user(self):
    #     with self.modify_settings(INSTALLED_APPS={
    #         'append': 'test_app_custom_user',
    #         'remove': [
    #             'test_app',
    #         ],
    #     }):
    #         self.changelist('editor')

    def change(self, user_version, id):
        url = reverse(
            'admin:separate_users_{}_change'.format(user_version),
            args=[id]
        )
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_change_frontenduser(self):
        self.change('frontenduser', self.frontenduser.id)

    def test_change_editor(self):
        self.change('editor', self.editor.id)

    def password_change(self, user_version, id):
        url = reverse(
            'admin:separate_users_{}_password_change'.format(user_version),
            args=[id]
        )
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_frontenduser_password_change(self):
        self.password_change('frontenduser', self.frontenduser.id)

    def test_editor_password_change(self):
        self.password_change('editor', self.editor.id)
