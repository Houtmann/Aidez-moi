from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Tickets( models.Model):

    title = models.TextField(verbose_name='Titre',)
    content = models.TextField(verbose_name='Contenu',)
    create_by = models.ForeignKey(User, verbose_name='Crée par',)
    created = models.DateTimeField(verbose_name='Crée le',)
    last_edited = models.DateTimeField(auto_now=True, verbose_name='Edité le',)
    category = models.ForeignKey('TicketCategory')

    TYPES_CHOICES = (
        (1, 'Incident'),
        (2, 'Demande'),)

    types = models.IntegerField(
        ('Types'),
        choices=TYPES_CHOICES )

    OPEN_STATUS = 'OPEN'
    RESOLVED_STATUS = 3
    CLOSED_STATUS = 4

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    )

    PRIORITY_CHOICES = (
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Low'),
        ('VERYLOW', 'Very Low'),)

    assign_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_to',
        blank=True,
        null=True,
        verbose_name=('Assigné à'),
        )

    status = models.CharField(max_length=15
        ,
        choices=STATUS_CHOICES,
        default=OPEN_STATUS,
        verbose_name='Statut',)

    priority = models.CharField(max_length=15
        ,
        choices=PRIORITY_CHOICES,
        default='NORMAL',
        blank='NORMAL',
        help_text=('1 = Highest Priority, 5 = Low Priority'),
        verbose_name='Priorité',)

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
    category = models.TextField(verbose_name='Catégorie', db_index=True)
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


class UserProfile(models.Model):
    user = models.OneToOneField(User)

