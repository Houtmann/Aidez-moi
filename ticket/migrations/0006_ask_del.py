# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20150318_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ask_del',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ask_del', models.BooleanField(default=0)),
                ('ticket', models.ForeignKey(to='ticket.Tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
