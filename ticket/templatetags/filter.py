# coding=utf-8
__author__ = 'had'

from django import template
from ticket.models import Tickets, User
import json

register = template.Library()


def all_tick(user):
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



def transform_to_dict(value):
    return json.loads(value)




register.filter('transform_to_dict', transform_to_dict)
register.filter('ticket_resolved', ticket_resolved)
register.filter('ticket_open', ticket_open)
register.filter('ticket_new', ticket_new)
register.filter('ticket_clos', ticket_clos)
register.filter('all_tick', all_tick)
register.filter('ticket_incomplete', ticket_incomplete)
