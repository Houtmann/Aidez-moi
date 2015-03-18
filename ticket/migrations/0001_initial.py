# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adress', models.TextField()),
                ('postal', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('title', models.TextField()),
                ('status', models.IntegerField(default=1, verbose_name='Status', choices=[(1, 'Open'), (2, 'Reopened'), (3, 'Resolved'), (4, 'Closed'), (5, 'Duplicate')])),
                ('priority', models.IntegerField(blank=3, default=3, verbose_name='Priority', help_text='1 = Highest Priority, 5 = Low Priority', choices=[(1, 'Critical'), (2, 'High'), (3, 'Normal'), (4, 'Low'), (5, 'Very Low')])),
                ('assign_to', models.ForeignKey(related_name='assigned_to', to=settings.AUTH_USER_MODEL, null=True, verbose_name='Assigned to', blank=True)),
                ('create_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('entity', models.ForeignKey(to='ticket.Entity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('entity', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
