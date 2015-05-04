__author__ = 'had'
from django.core.mail import send_mail
from ticket.models import Tickets, User, Follow
from celery import shared_task


@shared_task
def send_new_ticket_all_staff(object):
    """
    Envoi un mail à tous les membres du staff
    Prend un paramètre un objet pour le corps du mail
    """
    staff = User.objects.filter(is_staff=True)
    for email in staff.values('email'):
        recp = email.get('email')

        send_mail('Nouveau ticket :'+ object.title,
                   object.content,
                  'hhoutmann@gmail.com',  [recp], fail_silently=False)

@shared_task
def follow_on_ticket(object):
    pass


