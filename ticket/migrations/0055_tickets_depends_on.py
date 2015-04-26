# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0054_auto_20150422_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='depends_on',
            field=models.CharField(blank=True, max_length=100, verbose_name='Dépend', null=True),
        ),
    ]
