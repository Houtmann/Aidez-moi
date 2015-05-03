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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Nom')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('telephone', models.TextField(blank=True, null=True, verbose_name='Téléphone')),
                ('adress', models.TextField(blank=True, null=True, verbose_name='Adresse')),
                ('postal', models.TextField(blank=True, null=True, verbose_name='Code postal')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.TextField(blank=True, null=True)),
                ('date_follow', models.DateTimeField(auto_now=True)),
                ('field', models.CharField(null=True, max_length=100)),
                ('old_value', models.TextField(null=True)),
                ('new_value', models.TextField(null=True)),
                ('follow_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='follower')),
            ],
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(max_length=500, verbose_name='Catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Titre')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('created', models.DateTimeField(verbose_name='Crée le')),
                ('last_edited', models.DateTimeField(auto_now=True, verbose_name='Edité le')),
                ('complete', models.BooleanField(default=1, verbose_name='Complet')),
                ('depends_on', models.CharField(blank=True, null=True, max_length=100, verbose_name='Dépend')),
                ('types', models.IntegerField(choices=[('INCIDENT', 'Incident'), ('ASK', 'Demande')], verbose_name='Types')),
                ('status', models.CharField(default='OPEN', max_length=15, choices=[('OPEN', 'Ouvert'), ('RESOLVED', 'Résolus'), ('CLOSED', 'Clos')], verbose_name='Statut')),
                ('priority', models.CharField(default='NORMAL', max_length=15, blank='NORMAL', help_text='1 = Highest Priority, 5 = Low Priority', choices=[('CRITICAL', 'Critique'), ('HIGH', 'Haute'), ('NORMAL', 'Normal'), ('LOW', 'Basse'), ('VERYLOW', 'Très basse')], verbose_name='Priorité')),
                ('assign_to', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='Assigné à', related_name='assigned_to')),
                ('category', models.ForeignKey(null=True, blank=True, verbose_name='Catégorie', to='ticket.TicketCategory')),
                ('create_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Crée par')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.ForeignKey(to='ticket.Entity', verbose_name='Entité')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='follow',
            name='ticket',
            field=models.ForeignKey(to='ticket.Tickets', related_name='ticket_id'),
        ),
    ]
