# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_auto_20150328_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltickets',
            name='date_closed',
        ),
        migrations.RemoveField(
            model_name='historicaltickets',
            name='date_resolved',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='date_closed',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='date_resolved',
        ),
    ]
