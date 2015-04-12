# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0037_userprofile_entity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='entity',
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
    ]
