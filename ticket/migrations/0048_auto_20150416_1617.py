# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0047_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='entity',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
