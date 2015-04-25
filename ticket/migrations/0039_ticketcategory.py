# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0038_auto_20150411_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  primary_key=True,
                                  auto_created=True,
                                  serialize=False)),
                ('category', models.TextField()),
            ],
        ),
    ]
