# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0003_auto_20150317_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='response',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  auto_created=True,
                                  serialize=False,
                                  primary_key=True)),
                ('response', models.TextField()),
                ('date_response', models.DateTimeField(auto_now=True)),
                ('response_by',
                 models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('ticket_id', models.ForeignKey(to='ticket.Tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
