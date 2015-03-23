# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_auto_20150320_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field', models.CharField(max_length=100, verbose_name='Field')),
                ('old_value', models.TextField(null=True, blank=True, verbose_name='Old Value')),
                ('new_value', models.TextField(null=True, blank=True, verbose_name='New Value')),
                ('followup', models.ForeignKey(to='ticket.Tickets', verbose_name='Follow-up')),
            ],
            options={
                'verbose_name_plural': 'Ticket changes',
                'verbose_name': 'Ticket change',
            },
            bases=(models.Model,),
        ),
    ]
