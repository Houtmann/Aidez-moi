# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0022_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='o2o',
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
