# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0032_auto_20150402_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTickets',
            fields=[
                ('id',
                 models.IntegerField(auto_created=True,
                                     blank=True,
                                     db_index=True,
                                     verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('create_by_id',
                 models.IntegerField(null=True,
                                     blank=True,
                                     db_index=True)),
                ('created', models.DateTimeField()),
                ('last_edited', models.DateTimeField(
                    editable=False, blank=True)),
                ('types', models.IntegerField(
                    choices=[(1, 'Incident'), (2, 'Demande')], verbose_name='Types')),
                ('assign_to_id',
                 models.IntegerField(null=True,
                                     blank=True,
                                     db_index=True,
                                     verbose_name='Assigned to')),
                ('status', models.CharField(default='OPEN', max_length=15, choices=[
                 ('OPEN', 'Open'), ('RESOLVED', 'Resolved'), ('CLOSED', 'Closed')])),
                ('priority',
                 models.CharField(default='NORMAL',
                                  help_text='1 = Highest Priority, 5 = Low Priority',
                                  blank='NORMAL',
                                  max_length=15,
                                  choices=[('CRITICAL',
                                            'Critical'),
                                           ('HIGH',
                                            'High'),
                                           ('NORMAL',
                                            'Normal'),
                                           ('LOW',
                                            'Low'),
                                           ('VERYLOW',
                                            'Very Low')])),
                ('history_id',
                 models.AutoField(primary_key=True,
                                  serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(
                    max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user',
                 models.ForeignKey(null=True,
                                   to=settings.AUTH_USER_MODEL,
                                   on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical tickets',
            },
            bases=(models.Model,),
        ),
    ]
