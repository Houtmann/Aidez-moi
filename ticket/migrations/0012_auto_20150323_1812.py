# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_auto_20150323_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date_closed', models.DateTimeField()),
                ('date_resolved', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ticketchange',
            name='followup',
        ),
        migrations.DeleteModel(
            name='TicketChange',
        ),
        migrations.AddField(
            model_name='tickets',
            name='last_edited',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 23, 17, 12, 13, 530647, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tickets',
            name='created',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
