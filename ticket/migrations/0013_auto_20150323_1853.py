# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0012_auto_20150323_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTickets',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', auto_created=True, blank=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('create_by_id', models.IntegerField(db_index=True, blank=True, null=True)),
                ('created', models.DateTimeField()),
                ('last_edited', models.DateTimeField(blank=True, editable=False)),
                ('types', models.IntegerField(choices=[(1, 'Incident'), (2, 'Demande')], verbose_name='Types')),
                ('assign_to_id', models.IntegerField(db_index=True, verbose_name='Assigned to', blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Open'), (3, 'Resolved'), (4, 'Closed')], verbose_name='Status', default=1)),
                ('priority', models.IntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Normal'), (4, 'Low'), (5, 'Very Low')], help_text='1 = Highest Priority, 5 = Low Priority', verbose_name='Priority', default=3, blank=3)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical tickets',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='TicketHistory',
        ),
    ]
