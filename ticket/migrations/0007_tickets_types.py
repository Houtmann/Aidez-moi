# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_ask_del'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='types',
            field=models.IntegerField(
                verbose_name='Types', default=1, choices=[
                    (1, 'Incident'), (2, 'Demande')]),
            preserve_default=False,
        ),
    ]
