# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0044_auto_20150416_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='description',
            field=models.TextField(verbose_name='Description', null=True),
        ),
    ]
