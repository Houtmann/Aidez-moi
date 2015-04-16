# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0045_auto_20150416_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='adress',
            field=models.TextField(verbose_name='Adresse', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='description',
            field=models.TextField(verbose_name='Description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='postal',
            field=models.TextField(verbose_name='Code postal', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='telephone',
            field=models.TextField(verbose_name='Téléphone', null=True, blank=True),
        ),
    ]
