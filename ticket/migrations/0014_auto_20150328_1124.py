# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0013_auto_20150323_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ask_del',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='ask_del',
        ),
        migrations.AddField(
            model_name='historicaltickets',
            name='date_closed',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicaltickets',
            name='date_resolved',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tickets',
            name='date_closed',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tickets',
            name='date_resolved',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
