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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description', blank=True, null=True)),
                ('telephone', models.TextField(verbose_name='Téléphone', blank=True, null=True)),
                ('adress', models.TextField(verbose_name='Adresse', blank=True, null=True)),
                ('postal', models.TextField(verbose_name='Code postal', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('follow', models.TextField(blank=True, null=True)),
                ('date_follow', models.DateTimeField(auto_now=True)),
                ('old_value', models.TextField(blank=True, null=True)),
                ('new_value', models.TextField(blank=True, null=True)),
                ('follow_by', models.ForeignKey(related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category', models.TextField(max_length=500, verbose_name='Catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=150, verbose_name='Titre')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('created', models.DateTimeField(verbose_name='Crée le')),
                ('last_edited', models.DateTimeField(verbose_name='Edité le', auto_now=True)),
                ('complete', models.BooleanField(verbose_name='Complet', default=1)),
                ('depends_on', models.CharField(max_length=100, verbose_name='Dépend', blank=True, null=True)),
                ('file', models.FileField(upload_to='media', blank=True, null=True)),
                ('date_closed', models.DateTimeField(verbose_name='Date de cloture le', blank=True, null=True)),
                ('date_assigned', models.DateTimeField(verbose_name='Assigné le', blank=True, null=True)),
                ('date_resolved', models.DateTimeField(verbose_name='Résolution le', blank=True, null=True)),
                ('ask_to_delete', models.BooleanField(default=0)),
                ('types', models.CharField(max_length=15, verbose_name='Types', choices=[('INCIDENT', 'Incident'), ('ASK', 'Demande')])),
                ('status', models.CharField(max_length=15, verbose_name='Statut', choices=[('OPEN', 'Ouvert'), ('RESOLVED', 'Résolus'), ('CLOSED', 'Clos')], default='OPEN')),
                ('priority', models.CharField(max_length=15, verbose_name='Priorité', blank='NORMAL', help_text='1 = Highest Priority, 5 = Low Priority', choices=[('CRITICAL', 'Critique'), ('HIGH', 'Haute'), ('NORMAL', 'Normal'), ('LOW', 'Basse'), ('VERYLOW', 'Très basse')], default='NORMAL')),
                ('assign_to', models.ForeignKey(verbose_name='Assigné à', blank=True, to=settings.AUTH_USER_MODEL, null=True, related_name='assigned_to')),
                ('category', models.ForeignKey(verbose_name='Catégorie', blank=True, to='ticket.TicketCategory', null=True)),
                ('create_by', models.ForeignKey(verbose_name='Crée par', to=settings.AUTH_USER_MODEL)),
                ('entity', models.ForeignKey(verbose_name='Entité', to='ticket.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='follow',
            name='ticket',
            field=models.ForeignKey(related_name='ticket_id', to='ticket.Tickets'),
        ),
    ]
