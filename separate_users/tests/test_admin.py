# -*- coding: utf-8 -*-
from time import sleep

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.testcases import TestCase


class AdminTestCase(TestCase):
    """
    test some basic admin views
    make test generic,
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

    def test_staff_user_passwordchange(self):
        exit()

    def test_frontend_user_passwordchange(self):
        exit()
