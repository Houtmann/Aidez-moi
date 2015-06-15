# coding=utf-8
__author__ = 'had'

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


from django.core.mail import send_mail
from ticket.models import Tickets, User, Follow
from django.utils.translation import ugettext as _
from celery import shared_task, task
from djangoticket.email_config import USER
from djangoticket.settings import MEDIA_ROOT
from django.template.loader import get_template
from django.template import Context
from ticket.templatetags.filter import compare

from django.core.mail import EmailMessage



@task
def send_new_ticket_all_staff(object, user):
    """
    Envoi un mail à tous les membres du staff
    Prend un paramètre un objet pour le corps du mail
    """

    staff = User.objects.filter(is_staff=True)
    for email in staff.values('email'):
        recp = email.get('email')

        send_mail(user + _(' a posté un Nouveau ticket : ') + object.title,
                  object.content,
                  USER,
                  [recp],
                  fail_silently=False)


@task
def follow_on_ticket(object_id, dict1, dict2):

    """
    object_id  est l'id du ticket et values les valeurs qui ont changé sur le ticket
    Envoi un email à chaque reponse , ou chaque éditions du tickets.
    """
    ticket = Tickets.objects.get(pk=object_id)
    recp=ticket.create_by.email
    send_mail(
                _(' Ticket : ') + ticket.title,
                compare(dict1, dict2),
                USER,
                [recp],
                fail_silently=False)



@task
def incomplete_ticket(ticket_id):
    """
    Envoi un email lorsque le staff marque un ticket comme incomplet
    """
    ticket = Tickets.objects.get(pk=ticket_id)

    recp = ticket.create_by.email
    content = "Votre ticket est incomplet nous" \
              " sommes dans l'attente d'informations complémentaires"

    send_mail(_(' Votre ticket ') + ticket.title + _('est incomplet'),
              content,
              USER,
              [recp],
              fail_silently=False)



def handle_uploaded_file(f):
    """ Fonction qui écrit le fichier envoyé avec le ticket"""

    with open(MEDIA_ROOT + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

