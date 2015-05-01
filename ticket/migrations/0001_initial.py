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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.TextField(verbose_name='Nom')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('telephone', models.TextField(null=True, verbose_name='Téléphone', blank=True)),
                ('adress', models.TextField(null=True, verbose_name='Adresse', blank=True)),
                ('postal', models.TextField(null=True, verbose_name='Code postal', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('follow', models.TextField(null=True, blank=True)),
                ('date_follow', models.DateTimeField(auto_now=True)),
                ('field', models.CharField(max_length=100, null=True)),
                ('old_value', models.TextField(null=True)),
                ('new_value', models.TextField(null=True)),
                ('follow_by', models.ForeignKey(related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('category', models.TextField(verbose_name='Catégorie', db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.TextField(verbose_name='Titre')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('created', models.DateTimeField(verbose_name='Crée le')),
                ('last_edited', models.DateTimeField(auto_now=True, verbose_name='Edité le')),
                ('complete', models.BooleanField(verbose_name='Complet', default=1)),
                ('depends_on', models.CharField(max_length=100, null=True, verbose_name='Dépend', blank=True)),
                ('types', models.IntegerField(choices=[(1, 'Incident'), (2, 'Demande')], verbose_name='Types')),
                ('status', models.CharField(max_length=15, choices=[('OPEN', 'Ouvert'), ('RESOLVED', 'Résolus'), ('CLOSED', 'Clos')], verbose_name='Statut', default='OPEN')),
                ('priority', models.CharField(choices=[('CRITICAL', 'Critique'), ('HIGH', 'Haute'), ('NORMAL', 'Normal'), ('LOW', 'Basse'), ('VERYLOW', 'Très basse')], verbose_name='Priorité', blank='NORMAL', default='NORMAL', max_length=15, help_text='1 = Highest Priority, 5 = Low Priority')),
                ('assign_to', models.ForeignKey(verbose_name='Assigné à', null=True, blank=True, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='Catégorie', null=True, blank=True, to='ticket.TicketCategory')),
                ('create_by', models.ForeignKey(verbose_name='Crée par', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('entity', models.ForeignKey(verbose_name='Entité', to='ticket.Entity')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='follow',
            name='ticket',
            field=models.ForeignKey(related_name='ticket_id', to='ticket.Tickets'),
        ),
    ]
