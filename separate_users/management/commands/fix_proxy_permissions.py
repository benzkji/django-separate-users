import inspect
import sys

from django.contrib.auth.management import _get_all_permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.apps import apps


# where this comes from: https://gist.github.com/magopian/7543724#gistcomment-2185491
# as django adds permissions for proxy models in another app for the proxies parent
# also, epic: https://code.djangoproject.com/ticket/11154
# also: https://stackoverflow.com/questions/38391729/how-to-retrieve-all-permissions-of-a-specific-model-in-django
class Command(BaseCommand):
    help = "Fix permissions for proxy models."

    def handle(self, *args, **options):
        for model in apps.get_models():
            opts = model._meta
            sys.stdout.write('{}-{}\n'.format(opts.app_label, opts.object_name.lower()))
            ctype, created = ContentType.objects.get_or_create(
                app_label=opts.app_label,
                model=opts.object_name.lower())

            argspecs = inspect.getargspec(_get_all_permissions)
            if len(argspecs[0]) == 2:
                # django < 1.10
                all_permissions = _get_all_permissions(opts, ctype)
            else:
                all_permissions = _get_all_permissions(opts)
            for codename, name in all_permissions:
                sys.stdout.write('  --{}\n'.format(codename))
                p, created = Permission.objects.get_or_create(
                    codename=codename,
                    content_type=ctype,
                    defaults={'name': name})
                if created:
                    sys.stdout.write('Adding permission {}\n'.format(p))
