# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0024_tickethistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ask_del',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='ask_del',
        ),
    ]
