# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0048_auto_20150416_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='entity',
            field=models.ForeignKey(verbose_name='Entité', to='ticket.Entity'),
        ),
    ]
