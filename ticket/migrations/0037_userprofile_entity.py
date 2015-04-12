# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0036_entity'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='entity',
            field=models.ForeignKey(default=1, to='ticket.Entity'),
            preserve_default=False,
        ),
    ]
