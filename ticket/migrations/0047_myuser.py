# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0046_auto_20150416_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id',
                 models.AutoField(primary_key=True,
                                  verbose_name='ID',
                                  auto_created=True,
                                  serialize=False)),
                ('password', models.CharField(
                    verbose_name='password', max_length=128)),
                ('last_login',
                 models.DateTimeField(verbose_name='last login',
                                      blank=True,
                                      null=True)),
                ('entity', models.ForeignKey(to='ticket.Entity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
