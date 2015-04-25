# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0007_tickets_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTickets',
            fields=[
                ('id',
                 models.IntegerField(blank=True,
                                     auto_created=True,
                                     verbose_name='ID',
                                     db_index=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('create_by_id',
                 models.IntegerField(blank=True,
                                     null=True,
                                     db_index=True)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('types', models.IntegerField(
                    verbose_name='Types', choices=[(1, 'Incident'), (2, 'Demande')])),
                ('assign_to_id',
                 models.IntegerField(blank=True,
                                     null=True,
                                     verbose_name='Assigned to',
                                     db_index=True)),
                ('status', models.IntegerField(default=1, verbose_name='Status', choices=[
                 (1, 'Open'), (3, 'Resolved'), (4, 'Closed')])),
                ('priority',
                 models.IntegerField(default=3,
                                     blank=3,
                                     verbose_name='Priority',
                                     help_text='1 = Highest Priority, 5 = Low Priority',
                                     choices=[(1,
                                               'Critical'),
                                              (2,
                                               'High'),
                                              (3,
                                               'Normal'),
                                              (4,
                                               'Low'),
                                              (5,
                                               'Very Low')])),
                ('history_id',
                 models.AutoField(primary_key=True,
                                  serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(
                    max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.SET_NULL,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical tickets',
                'get_latest_by': 'history_date',
            },
            bases=(models.Model,),
        ),
    ]
