# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0031_auto_20150401_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.CharField(
                choices=[
                    ('OPEN',
                     'Open'),
                    ('RESOLVED',
                     'Resolved'),
                    ('CLOSED',
                     'Closed')],
                default='OPEN',
                max_length=15),
            preserve_default=True,
        ),
    ]
