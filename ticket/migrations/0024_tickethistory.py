# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0023_auto_20150329_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('field', models.CharField(max_length=100)),
                ('old_value', models.TextField()),
                ('new_value', models.TextField()),
                ('ticket', models.ForeignKey(to='ticket.Tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
