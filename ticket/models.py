from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractBaseUser

class Tickets( models.Model):

    title = models.TextField(verbose_name=_('Titre'),)
    content = models.TextField(verbose_name=_('Contenu'),)
    create_by = models.ForeignKey(User, verbose_name=_('Crée par'),)
    created = models.DateTimeField(verbose_name=_('Crée le'),)
    last_edited = models.DateTimeField(verbose_name=_('Edité le'),auto_now=True)
    category = models.ForeignKey('TicketCategory',verbose_name=_('Catégorie'), null=True, blank=True )

    TYPES_CHOICES = (
        (1, _('Incident')),
        (2, 'Demande'),)

    types = models.IntegerField(
        ('Types'),
        choices=TYPES_CHOICES )

    OPEN_STATUS = 'OPEN'
    RESOLVED_STATUS = 3
    CLOSED_STATUS = 4

    STATUS_CHOICES = (
        ('OPEN', _('Open')),
        ('RESOLVED', _('Resolved')),
        ('CLOSED', _('Closed')),
    )

    PRIORITY_CHOICES = (
        ('CRITICAL', _('Critical')),
        ('HIGH', _('High')),
        ('NORMAL', _('Normal')),
        ('LOW', _('Low')),
        ('VERYLOW', _('Very Low')),)

    assign_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_to',
        blank=True,
        null=True,
        verbose_name=(_('Assigné à')),
        )

    status = models.CharField(max_length=15
        ,
        choices=STATUS_CHOICES,
        default=OPEN_STATUS,
        verbose_name=_('Statut'),)

    priority = models.CharField(max_length=15
        ,
        choices=PRIORITY_CHOICES,
        default='NORMAL',
        blank='NORMAL',
        help_text=_(('1 = Highest Priority, 5 = Low Priority')),
        verbose_name=_('Priorité'),)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.title


class TicketCategory(models.Model):
    """
    Nom de catégorie pour mieux cibler les tickets
    """
    category = models.TextField(verbose_name=_('Catégorie'), db_index=True)
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

    follow_by = models.ForeignKey(User, related_name='follower')
    follow = models.TextField(blank=True, null=True)
    ticket = models.ForeignKey(Tickets, related_name='ticket_id')
    date_follow = models.DateTimeField(auto_now=True, )

    field = models.CharField(max_length=100, null=True)
    old_value = models.TextField(null=True)
    new_value = models.TextField(null=True)


class Entity(models.Model):
    """
    Modele pour créer des entités, exemple service comptabilité
    """
    name = models.TextField(verbose_name=_('Nom'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    telephone = models.TextField(verbose_name=_('Téléphone'), null=True, blank=True)
    adress = models.TextField(verbose_name=_('Adresse'), null=True, blank=True)
    postal = models.TextField(verbose_name=_('Code postal'), null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    entity = models.ForeignKey(Entity, verbose_name=_('Entité'))

