# -*- coding: utf-8 -*-
from django.contrib.auth.models import Permission
# from django.test import Client
from django.test import TestCase


# compat
import django
if django.VERSION[:2] < (1, 10):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse


class PermissionsTestCase(TestCase):
    """
    check if permissions are there, after management command was run.
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_permissions_initially(self):
        """
        check if not there initially - this will fail if django fixes the bug! nice to know.
        """
        self.assertEqual(self.permission_count('separate_users', 'add_frontenduser'), 0)
        self.assertEqual(self.permission_count('separate_users', 'add_editor'), 0)

    def test_permission_management_command(self):
        from django.core.management import call_command
        call_command('fix_proxy_permissions', )
        self.assertEqual(self.permission_count('separate_users', 'add_frontenduser'), 1)
        self.assertEqual(self.permission_count('separate_users', 'add_editor'), 1)

    def permission_count(self, app_label, codename):
        count = Permission.objects.filter(
            content_type__app_label=app_label,
            codename=codename,
        ).count()
        return count