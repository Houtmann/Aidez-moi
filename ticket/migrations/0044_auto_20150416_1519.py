# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0043_auto_20150415_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id',
                 models.AutoField(primary_key=True,
                                  auto_created=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.TextField(verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('telephone',
                 models.TextField(null=True,
                                  verbose_name='Téléphone')),
                ('adress',
                 models.TextField(null=True,
                                  verbose_name='Adresse')),
                ('postal',
                 models.TextField(null=True,
                                  verbose_name='Code postal')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='entity',
            field=models.ForeignKey(to='ticket.Entity', default=1),
            preserve_default=False,
        ),
    ]
