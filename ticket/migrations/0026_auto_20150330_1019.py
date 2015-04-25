# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0025_auto_20150329_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickethistory',
            name='date_change',
            field=models.DateTimeField(
                default=datetime.datetime(
                    2015,
                    3,
                    30,
                    8,
                    19,
                    46,
                    468510,
                    tzinfo=utc),
                auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tickethistory',
            name='ticket',
            field=models.ForeignKey(
                null=True,
                related_name='ticket_id',
                blank=True,
                to='ticket.Tickets'),
            preserve_default=True,
        ),
    ]
