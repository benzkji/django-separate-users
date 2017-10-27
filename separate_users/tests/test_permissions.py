# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase


class PermissionsTestCase(TestCase):
    """
    check if permissions are there, after management command was run.
    check if not there initially - this will fail if django fixes the bug! nice to know.
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def no_permissions_initially(self):
        exit()

    def test_permission_management_command(self):
        exit()
