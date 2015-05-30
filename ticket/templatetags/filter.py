# coding=utf-8
__author__ = 'had'

from django import template
from ticket.models import Tickets
from django.utils.translation import ugettext as _
import json

register = template.Library()


def all_tick(user):
    """
    :param user:
    :return: Le nombre de ticket crée par l'utilisateur
    """
    try:
        return Tickets.objects.filter(create_by=user).count()
    except:
        pass


def ticket_resolved(user):
    if user.is_staff:
        return Tickets.objects.filter(status='RESOLVED').count()
    else:
        return Tickets.objects.filter(
            create_by=user, status='RESOLVED').count()


def ticket_open(user):
    if user.is_staff:
        return Tickets.objects.filter(
            status='OPEN').exclude(assign_to=None).count()
    else:
        return Tickets.objects.filter(
            create_by=user, status='OPEN').exclude(assign_to=None).count()


def ticket_new(user):
    if user.is_staff:
        return Tickets.objects.filter(assign_to=None).count()
    else:
        return Tickets.objects.filter(create_by=user, assign_to=None).count()


def ticket_clos(user):
    if user.is_staff:
        return Tickets.objects.filter(status='CLOSED').count()
    else:
        return Tickets.objects.filter(create_by=user, status=4).count()


def ticket_incomplete(user):
    if user.is_staff:
        return Tickets.objects.filter(complete=0).count()
    else:
        return Tickets.objects.filter(create_by=user, complete=0).count()


def transform(value):
    for i in value:
        return i


@register.assignment_tag
def compare(dict_one, dict_two):
    """
    :param dict_one: Un dictionnaire
    :param dict_two: Un autre dictionnaire
    :return:
    Retourne les différences entre old_value et new_value dans la table de suivi Follow
    pour l'afficher dans la timeline de suivi de la page d'un ticket
    Compare deux dictionnaires afin de crée un suivi du ticket
    """

    dict1 = json.loads(dict_one)
    dict2 = json.loads(dict_two)
    sharedkeys = set(dict1.keys()).intersection(dict2.keys())

    for key in sharedkeys:
        t1 = dict(Tickets._meta.get_field_by_name(key)[0].flatchoices).get(dict1[key])
        t2 = dict(Tickets._meta.get_field_by_name(key)[0].flatchoices).get(dict2[key])
        yield Tickets._meta.get_field_by_name(key)[0].verbose_name \
              + _(' changé de ') \
              + t1 \
              + _(' à ') \
              + t2


register.filter('ticket_resolved', ticket_resolved)
register.filter('ticket_open', ticket_open)
register.filter('ticket_new', ticket_new)
register.filter('ticket_clos', ticket_clos)
register.filter('all_tick', all_tick)
register.filter('ticket_incomplete', ticket_incomplete)
