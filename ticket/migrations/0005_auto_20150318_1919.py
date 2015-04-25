# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.IntegerField(
                choices=[
                    (1, 'Open'), (3, 'Resolved'), (4, 'Closed')], default=1, verbose_name='Status'),
            preserve_default=True,
        ),
    ]
