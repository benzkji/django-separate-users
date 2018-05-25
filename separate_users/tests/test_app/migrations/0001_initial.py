# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import separate_users.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', separate_users.models.EditorManager()),
            ],
        ),
        migrations.CreateModel(
            name='FrontendUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', separate_users.models.FrontendUserManager()),
            ],
        ),
    ]
