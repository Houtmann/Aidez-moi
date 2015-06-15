# coding=utf-8

# The MIT License (MIT)
# Copyright (c) [2015] [Houtmann Hadrien]
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the Aidez-moi), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractBaseUser
from djangoticket.settings import MEDIA_ROOT
import reversion



class Entity(models.Model):
    """
    Modele pour créer des entités, exemple service comptabilité
    """
    name = models.TextField(
        verbose_name=_('Nom'))

    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True)

    telephone = models.TextField(
        verbose_name=_('Téléphone'),
        null=True,
        blank=True)

    adress = models.TextField(
        verbose_name=_('Adresse'),
        null=True,
        blank=True)

    postal = models.TextField(
        verbose_name=_('Code postal'),
        null=True,
        blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Tickets(models.Model):

    title = models.TextField(
        verbose_name=_('Titre'),
        max_length=150)

    content = models.TextField(
        verbose_name=_('Contenu'), )

    create_by = models.ForeignKey(
        User,
        verbose_name=_('Crée par'), )

    created = models.DateTimeField(
        verbose_name=_('Crée le'), )

    last_edited = models.DateTimeField(
        verbose_name=_('Edité le'),
        auto_now=True)

    category = models.ForeignKey(
        'TicketCategory',
        verbose_name=_('Catégorie'),
        null=True,
        blank=True)

    # Marque le ticket comme incomplete et attente d'informations
    complete = models.BooleanField(
        default=1,
        verbose_name=_('Complet'))

    depends_on = models.CharField(
        null=True,
        blank=True,
        verbose_name=_('Dépend'),
        max_length=100)

    file = models.FileField(
        null=True,
        blank=True,
        upload_to='media')

    date_closed = models.DateTimeField(
        verbose_name=_('Date de cloture le'),
        blank=True,
        null=True)

    date_assigned = models.DateTimeField(
        verbose_name=_('Assigné le'),
        blank=True,
        null=True)

    date_resolved = models.DateTimeField(
        verbose_name=_('Résolution le'),
        blank=True,
        null=True)

    ask_to_delete = models.BooleanField(
        default=0)

    entity = models.ForeignKey(
        Entity,
        verbose_name=_('Entité'),
        blank=True,
        null=True)

    TYPES_CHOICES = (
        ('INCIDENT', _('Incident')),
        ('ASK', _('Demande')),)

    types = models.CharField(
        max_length=15,
        verbose_name=_('Types'),
        choices=TYPES_CHOICES)

    OPEN_STATUS = 'OPEN'

    STATUS_CHOICES = (
        ('OPEN', _('Ouvert')),
        ('RESOLVED', _('Résolus')),
        ('CLOSED', _('Clos')),
    )

    PRIORITY_CHOICES = (
        ('CRITICAL', _('Critique')),
        ('HIGH', _('Haute')),
        ('NORMAL', _('Normal')),
        ('LOW', _('Basse')),
        ('VERYLOW', _('Très basse')),)

    assign_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_to',
        blank=True,
        null=True,
        verbose_name=(_('Assigné à')),
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=OPEN_STATUS,
        verbose_name=_('Statut'), )

    priority = models.CharField(
        max_length=15,
        choices=PRIORITY_CHOICES,
        default='NORMAL',
        blank='NORMAL',
        help_text=_(
        '1 = Highest Priority, 5 = Low Priority'),
        verbose_name=_('Priorité'), )

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.title
reversion.register(Tickets)

class TicketCategory(models.Model):
    """
    Nom de catégorie pour mieux cibler les tickets
    """
    category = models.TextField(verbose_name=_('Catégorie'), max_length=500)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.category


class Follow(models.Model):
    """
    Pour suivre les changements et les reponse d'un ticket
    """

    follow_by = models.ForeignKey(
        User,
        related_name='follower')

    follow = models.TextField(
        blank=True,
        null=True)

    ticket = models.ForeignKey(
        Tickets,
        related_name='ticket_id')

    date_follow = models.DateTimeField(
        auto_now=True, )

    old_value = models.TextField(
        blank=True,
        null=True)

    new_value = models.TextField(
        blank=True,
        null=True)



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ticket_per_page = models.IntegerField(
                        default=25,
                        verbose_name=_('Nombre de ticket par page'))
    active_mail = models.BooleanField(
                        default=0,
                        verbose_name=_('Mail actif')
                                      )

