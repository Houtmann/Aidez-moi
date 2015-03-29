# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0021_auto_20150329_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('o2o', models.OneToOneField(to='ticket.Tickets')),
            ],
            options={
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
