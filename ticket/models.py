from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from model_utils import FieldTracker


class UserProfile(models.Model):

    user = models.OneToOneField(User)



class Tickets( models.Model):

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
        verbose_name=('Assigned to'),
        )

    status = models.CharField(max_length=15
        ,
        choices=STATUS_CHOICES,
        default=OPEN_STATUS, )

    priority = models.CharField(max_length=15
        ,
        choices=PRIORITY_CHOICES,
        default='NORMAL',
        blank='NORMAL',
        help_text=('1 = Highest Priority, 5 = Low Priority'),)

    tracker = FieldTracker()

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.title

    def save(self, *args, **kwargs):
        if  Tickets.objects.filter(id=self.id).exists():
            for i in self.tracker.changed().items():
                TicketHistory.objects.create(ticket_id=self.pk,
                                         field=i[0],
                                         old_value=i[1],
                                         new_value=getattr(self, i[0]))


        super(Tickets, self).save(*args, **kwargs)




class TicketHistory(models.Model):
    """ Model for track any change on ticket model"""

    ticket = models.ForeignKey(Tickets, related_name='ticket_id', blank=True, null=True)
    field = models.CharField(max_length=100, null=True)
    old_value = models.TextField(null=True)
    new_value = models.TextField(null=True)
    date_change = models.DateTimeField(auto_now=True)


class response(models.Model):

    response_by = models.ForeignKey(User)
    response = models.TextField()
    ticket = models.ForeignKey(Tickets)
    date_response = models.DateTimeField(auto_now=True)



