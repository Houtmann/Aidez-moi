# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0034_auto_20150403_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='assign_to',
            field=models.ForeignKey(
                null=True,
                blank=True,
                related_name='assigned_to',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Assigné à'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='content',
            field=models.TextField(verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='create_by',
            field=models.ForeignKey(
                verbose_name='Crée par',
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='created',
            field=models.DateTimeField(verbose_name='Crée le'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='last_edited',
            field=models.DateTimeField(auto_now=True, verbose_name='Edité le'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='priority',
            field=models.CharField(
                blank='NORMAL',
                choices=[
                    ('CRITICAL',
                     'Critical'),
                    ('HIGH',
                     'High'),
                    ('NORMAL',
                     'Normal'),
                    ('LOW',
                     'Low'),
                    ('VERYLOW',
                     'Very Low')],
                default='NORMAL',
                max_length=15,
                help_text='1 = Highest Priority, 5 = Low Priority',
                verbose_name='Priorité'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.CharField(
                choices=[
                    ('OPEN',
                     'Open'),
                    ('RESOLVED',
                     'Resolved'),
                    ('CLOSED',
                     'Closed')],
                default='OPEN',
                verbose_name='Statut',
                max_length=15),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='title',
            field=models.TextField(verbose_name='Titre'),
        ),
    ]
