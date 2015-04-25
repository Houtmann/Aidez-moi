# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0042_auto_20150415_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='category',
            field=models.ForeignKey(
                to='ticket.TicketCategory',
                verbose_name='Catégorie'),
        ),
    ]
