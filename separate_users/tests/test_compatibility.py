# -*- coding: utf-8 -*-
from time import sleep

from django.contrib.auth.models import User
from django.test.testcases import TestCase


class AdminTestCase(TestCase):
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
