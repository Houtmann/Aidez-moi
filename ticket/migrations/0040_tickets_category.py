# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0039_ticketcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='category',
            field=models.ManyToManyField(to='ticket.TicketCategory'),
        ),
    ]
