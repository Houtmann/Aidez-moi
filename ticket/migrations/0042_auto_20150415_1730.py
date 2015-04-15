# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0041_auto_20150415_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategory',
            name='category',
            field=models.TextField(db_index=True, verbose_name='Catégorie'),
        ),
    ]
