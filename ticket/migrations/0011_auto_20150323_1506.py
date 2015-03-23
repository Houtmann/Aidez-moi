# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_ticketchange'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='ticket_id',
            new_name='ticket',
        ),
    ]
