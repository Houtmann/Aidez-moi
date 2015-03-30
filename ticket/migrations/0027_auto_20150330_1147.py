# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0026_auto_20150330_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='priority',
            field=models.CharField(max_length=15, choices=[('CRITICAL', 'Critical'), ('HIGH', 'High'), ('NORMAL', 'Normal'), ('LOW', 'Low'), ('VERYLOW', 'Very Low')], default='NORMAL', blank='NORMAL', help_text='1 = Highest Priority, 5 = Low Priority'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.CharField(max_length=15, default=1, choices=[('OPEN', 'Open'), ('RESOLVED', 'Resolved'), ('CLOSED', 'Closed')]),
            preserve_default=True,
        ),
    ]
