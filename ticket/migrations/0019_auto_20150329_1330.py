# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0018_auto_20150329_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickethistory',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='TicketHistory',
        ),
    ]
