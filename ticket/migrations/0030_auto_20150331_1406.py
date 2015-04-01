# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0029_auto_20150331_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='Follow',
            new_name='follow',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='Follow_by',
            new_name='follow_by',
        ),
    ]
