# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0027_auto_20150330_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickethistory',
            name='field',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tickethistory',
            name='new_value',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tickethistory',
            name='old_value',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
