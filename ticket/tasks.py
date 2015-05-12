__author__ = 'had'
from django.core.mail import send_mail
from ticket.models import Tickets, User
from django.utils.translation import ugettext as _
from celery import shared_task, task
from djangoticket.email_config import  USER, PASSWORD
from djangoticket.settings import MEDIA_ROOT
import hashlib

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



@task
def follow_on_ticket(object_id, values):
    """
    object_id  est l'id du ticket et values les valeurs qui ont changé sur le ticket
    Envoi un email à chaque reponse , ou chaque éditions du tickets.
    """

    ticket = Tickets.objects.get(pk=object_id)
    recp = ticket.create_by.email
    content = values.get('follow_by')+ _(' à changé ') + values.get('field')[0] + \
                _(' de ')+ values.get('oldvalue') + _(' à ') + values.get('newvalue')


    send_mail(values.get('follow_by') +_(' a modifier votre ticket : ')+ ticket.title,
                    content,
                    USER,  [recp], fail_silently=False)





def handle_uploaded_file(f):
    """ Fonction qui écrit le fichier envoyé avec le ticket"""

    with open(MEDIA_ROOT + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

