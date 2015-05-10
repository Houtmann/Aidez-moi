__author__ = 'had'
from django.core.mail import send_mail
from ticket.models import Tickets, User
from django.utils.translation import ugettext as _
from celery import shared_task, task
from djangoticket.email_config import  USER, PASSWORD


@task
def send_new_ticket_all_staff(object, user):
    """
    Envoi un mail à tous les membres du staff
    Prend un paramètre un objet pour le corps du mail
    """

    staff = User.objects.filter(is_staff=True)
    for email in staff.values('email'):
        recp = email.get('email')

        send_mail(user +_(' a posté" un Nouveau ticket : ')+ object.title,
                    object.content,
                    USER,  [recp], fail_silently=False)


@shared_task
def follow_on_ticket(object):
    """
    Envoi un email à chaque reponse , ou chaque éditions du tickets.
    """
    pass


