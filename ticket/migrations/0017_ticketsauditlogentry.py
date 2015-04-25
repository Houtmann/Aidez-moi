# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import audit_log.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0016_auto_20150329_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketsAuditLogEntry',
            fields=[
                ('id',
                 models.IntegerField(blank=True,
                                     auto_created=True,
                                     db_index=True,
                                     verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('created', models.DateTimeField()),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('types', models.IntegerField(
                    choices=[(1, 'Incident'), (2, 'Demande')], verbose_name='Types')),
                ('status', models.IntegerField(choices=[
                 (1, 'Open'), (3, 'Resolved'), (4, 'Closed')], verbose_name='Status', default=1)),
                ('priority',
                 models.IntegerField(choices=[(1,
                                               'Critical'),
                                              (2,
                                               'High'),
                                              (3,
                                               'Normal'),
                                              (4,
                                               'Low'),
                                              (5,
                                               'Very Low')],
                                     verbose_name='Priority',
                                     blank=3,
                                     help_text='1 = Highest Priority, 5 = Low Priority',
                                     default=3)),
                ('action_id',
                 models.AutoField(primary_key=True,
                                  serialize=False)),
                ('action_date', models.DateTimeField(
                    default=django.utils.timezone.now, editable=False)),
                ('action_type',
                 models.CharField(choices=[('I',
                                            'Created'),
                                           ('U',
                                            'Changed'),
                                           ('D',
                                            'Deleted')],
                                  max_length=1,
                                  editable=False)),
                ('action_user',
                 audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL,
                                                       null=True,
                                                       related_name='_tickets_audit_log_entry',
                                                       editable=False)),
                ('assign_to',
                 models.ForeignKey(verbose_name='Assigned to',
                                   to=settings.AUTH_USER_MODEL,
                                   null=True,
                                   related_name='_auditlog_assigned_to',
                                   blank=True)),
                ('create_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
            bases=(models.Model,),
        ),
    ]
