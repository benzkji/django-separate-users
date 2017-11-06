# -*- coding: utf-8 -*-
from django.test import override_settings
from django.test.testcases import TestCase


class AdminTestCase(TestCase):
    """
    TODO: check for pre 1.11 ImproperlyConfigured etc.
    TODO: check that MIGRATION_MODULES is configured (migration are written into this app!)
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_improperly_pre_1_11_with_custom_user_model(self):
        pass

    @override_settings(
        MIGRATION_MODULES = {}
    )
    def test_improperly_no_migration_modules(self):
        """
        TOOD: trigger improperly configured!!? but how?
        :return:
        """
        from separate_users.models import FrontendUser
        FrontendUser.objects.all()

