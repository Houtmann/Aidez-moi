
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _, ugettext





class UserProfile(models.Model):

    user = models.OneToOneField(User)




class Tickets(models.Model):

    title = models.TextField()
    content = models.TextField()
    create_by = models.ForeignKey(User)
    created = models.DateTimeField()
    last_edited = models.DateTimeField(auto_now=True)

    TYPES_CHOICES = (
        (1, 'Incident'),
        (2, 'Demande'),)

    types = models.IntegerField(
        ('Types'),
        choices=TYPES_CHOICES )

    OPEN_STATUS = 1
    RESOLVED_STATUS = 3
    CLOSED_STATUS = 4

    STATUS_CHOICES = (
        (OPEN_STATUS, 'Open'),
        (RESOLVED_STATUS, 'Resolved'),
        (CLOSED_STATUS, 'Closed'),
    )

    PRIORITY_CHOICES = (
        (1, 'Critical'),
        (2, 'High'),
        (3, 'Normal'),
        (4, 'Low'),
        (5, 'Very Low'),)


    assign_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_to',
        blank=True,
        null=True,
        verbose_name=('Assigned to'),
        )

    status = models.IntegerField(
        ('Status'),
        choices=STATUS_CHOICES,
        default=OPEN_STATUS, )

    priority = models.IntegerField(
        ('Priority'),
        choices=PRIORITY_CHOICES,
        default=3,
        blank=3,
        help_text=('1 = Highest Priority, 5 = Low Priority'),)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.title



class TicketHistory(models.Model):
    date_closed = models.DateTimeField()
    date_resolved = models.DateTimeField()



class ask_del(models.Model):
    """
    Tables pour marquer les objects à supprimer
    """
    ticket = models.ForeignKey(Tickets)
    ask_del = models.BooleanField(default=0) # Marque le ticket pour le suppression



class response(models.Model):

    response_by = models.ForeignKey(User)
    response = models.TextField()
    ticket = models.ForeignKey(Tickets)
    date_response = models.DateTimeField(auto_now=True)