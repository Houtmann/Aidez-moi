# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0052_auto_20150422_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='incomplete',
            field=models.BooleanField(verbose_name='Incomplet', default=0),
        ),
    ]
