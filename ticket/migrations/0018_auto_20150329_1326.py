# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0017_ticketsauditlogentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketsauditlogentry',
            name='action_user',
        ),
        migrations.RemoveField(
            model_name='ticketsauditlogentry',
            name='assign_to',
        ),
        migrations.RemoveField(
            model_name='ticketsauditlogentry',
            name='create_by',
        ),
        migrations.DeleteModel(
            name='TicketsAuditLogEntry',
        ),
    ]
