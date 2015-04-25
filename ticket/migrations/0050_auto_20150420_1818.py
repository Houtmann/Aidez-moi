# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0049_auto_20150416_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='category',
            field=models.ForeignKey(
                null=True,
                blank=True,
                verbose_name='Catégorie',
                to='ticket.TicketCategory'),
        ),
    ]
