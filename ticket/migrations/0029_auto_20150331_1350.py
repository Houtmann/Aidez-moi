# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0028_auto_20150330_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Follow', models.TextField(null=True, blank=True)),
                ('date_follow', models.DateTimeField(auto_now=True)),
                ('field', models.CharField(null=True, max_length=100)),
                ('old_value', models.TextField(null=True)),
                ('new_value', models.TextField(null=True)),
                ('Follow_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(null=True, to='ticket.Tickets', related_name='ticket_id', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='response',
            name='response_by',
        ),
        migrations.RemoveField(
            model_name='response',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='response',
        ),
        migrations.RemoveField(
            model_name='tickethistory',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='TicketHistory',
        ),
    ]
