# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0015_auto_20150328_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='ask_del',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  primary_key=True,
                                  auto_created=True,
                                  serialize=False)),
                ('ask_del', models.BooleanField(default=0)),
                ('ticket', models.ForeignKey(to='ticket.Tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  primary_key=True,
                                  auto_created=True,
                                  serialize=False)),
                ('field', models.CharField(max_length=100)),
                ('old_value', models.TextField()),
                ('new_value', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('ticket', models.ForeignKey(to='ticket.Tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='historicaltickets',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalTickets',
        ),
    ]
