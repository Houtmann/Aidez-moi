from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from save_the_change.mixins import SaveTheChange, TrackChanges, BaseChangeTracker
from model_utils import FieldTracker


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

    tracker = FieldTracker()

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.title

    def save(self, *args, **kwargs):
        print(self.tracker.changed())
        for i in self.tracker.changed().items():
            TicketHistory.objects.create(ticket_id=self.pk,
                                         field=i[0],
                                         old_value=i[1],
                                         new_value=getattr(self, i[0]))


        super(Tickets, self).save(*args, **kwargs)




class TicketHistory(models.Model):
    """ Model for track any change on ticket model"""
    
    ticket = models.ForeignKey(Tickets, related_name='ticket_id', blank=True, null=True)
    field = models.CharField(max_length=100)
    old_value = models.TextField()
    new_value = models.TextField()
    date_change = models.DateTimeField(auto_now=True)


class response(models.Model):

    response_by = models.ForeignKey(User)
    response = models.TextField()
    ticket = models.ForeignKey(Tickets)
    date_response = models.DateTimeField(auto_now=True)



