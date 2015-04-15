# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0040_tickets_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategory',
            name='category',
            field=models.TextField(db_index=True),
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='category',
        ),
        migrations.AddField(
            model_name='tickets',
            name='category',
            field=models.ForeignKey(default=1, to='ticket.TicketCategory'),
            preserve_default=False,
        ),
    ]
