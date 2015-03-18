# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20150317_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='entity',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='entity',
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
    ]
