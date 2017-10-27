from .settings import *
# TODO: it doesnt work!

AUTH_USER_MODEL = 'test_app_custom_user.CustomUser'

del(INSTALLED_APPS[INSTALLED_APPS.index('separate_users.tests.test_app')])

print INSTALLED_APPS

INSTALLED_APPS.insert(0, 'separate_users.tests.test_app_custom_user')
