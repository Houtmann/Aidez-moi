# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0053_auto_20150422_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='incomplete',
            field=models.BooleanField(default=1, verbose_name='Complet'),
        ),
    ]
