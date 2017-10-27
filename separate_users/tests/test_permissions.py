# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase


class PermissionsTestCase(TestCase):
    """
    TODO: check for pre 1.11 ImproperlyConfigured etc.
    TODO: check that MIGRATION_MODULES is configured (migration are written into this app!)
    """
    username = 'admin'
    password = 'admin'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_frontend_user_changelist(self):
        exit()

    def test_staff_user_changelist(self):
        exit()

    def test_frontend_user_changeview(self):
        exit()

    def test_staff_user_changeview(self):
        exit()
