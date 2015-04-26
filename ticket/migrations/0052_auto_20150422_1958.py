# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0051_tickets_incomplete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='priority',
            field=models.CharField(
                choices=[
                    ('CRITICAL',
                     'Critique'),
                    ('HIGH',
                     'Haute'),
                    ('NORMAL',
                     'Normal'),
                    ('LOW',
                     'Basse'),
                    ('VERYLOW',
                     'Très basse')],
                help_text='1 = Highest Priority, 5 = Low Priority',
                default='NORMAL',
                max_length=15,
                blank='NORMAL',
                verbose_name='Priorité'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.CharField(
                default='OPEN',
                choices=[
                    ('OPEN',
                     'Ouvert'),
                    ('RESOLVED',
                     'Résolus'),
                    ('CLOSED',
                     'Clos')],
                max_length=15,
                verbose_name='Statut'),
        ),
    ]
