# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0030_auto_20150331_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='follow_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='follower'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='follow',
            name='ticket',
            field=models.ForeignKey(related_name='ticket_id', default=1, to='ticket.Tickets'),
            preserve_default=False,
        ),
    ]
