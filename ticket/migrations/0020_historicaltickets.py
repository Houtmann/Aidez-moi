# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0019_auto_20150329_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTickets',
            fields=[
                ('id', models.IntegerField(blank=True, auto_created=True, verbose_name='ID', db_index=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('create_by_id', models.IntegerField(blank=True, null=True, db_index=True)),
                ('created', models.DateTimeField()),
                ('last_edited', models.DateTimeField(blank=True, editable=False)),
                ('types', models.IntegerField(choices=[(1, 'Incident'), (2, 'Demande')], verbose_name='Types')),
                ('assign_to_id', models.IntegerField(blank=True, verbose_name='Assigned to', null=True, db_index=True)),
                ('status', models.IntegerField(choices=[(1, 'Open'), (3, 'Resolved'), (4, 'Closed')], default=1, verbose_name='Status')),
                ('priority', models.IntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Normal'), (4, 'Low'), (5, 'Very Low')], verbose_name='Priority', default=3, help_text='1 = Highest Priority, 5 = Low Priority', blank=3)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical tickets',
            },
            bases=(models.Model,),
        ),
    ]
