from django.conf import settings


# simplified mode, where editors (staff) and frontendusers (non staff) are in the same list
NON_SUPERUSER_MODE = getattr(settings, 'SEPARATE_USERS_NON_SUPERUSER_MODE', False)