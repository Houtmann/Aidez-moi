# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_historicaltickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltickets',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalTickets',
        ),
    ]
