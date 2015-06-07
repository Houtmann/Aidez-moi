# coding=utf-8
__author__ = 'had'
from ticket.models import Tickets
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _



class PriorityColumn(tables.Column):
    """
    Class qui sert à colorer les cellules en fonction de leurs
    priorité
    """

    def render(self, value):
        if value == dict(Tickets.PRIORITY_CHOICES).get('CRITICAL') :
            self.attrs = {"td": {"bgcolor": "FF3333"}}

        elif value == dict(Tickets.PRIORITY_CHOICES).get('HIGH'):
            self.attrs = {"td": {"bgcolor": "FF8585"}}

        elif value == dict(Tickets.PRIORITY_CHOICES).get('LOW'):
            self.attrs = {"td": {"bgcolor": "FFC299"}}

        elif value == dict(Tickets.PRIORITY_CHOICES).get('VERYLOW'):
            self.attrs = {"td": {"bgcolor": "FFE2CE"}}

        elif value == dict(Tickets.PRIORITY_CHOICES).get('NORMAL'):
            self.attrs = {}

        return value


class StatusColumn(tables.Column):
    """
    Class met un badge en fonction du status
    """

    def render(self, value):

        if value == dict(Tickets.STATUS_CHOICES).get('OPEN'):
            return mark_safe(
                '<div class="ui center orange label">'+ _('Ouvert')+ '</div>')

        elif value == dict(Tickets.STATUS_CHOICES).get('CLOSED'):
            return mark_safe(
                '<div class="ui center black label">' + _('Clos') + '</div>')

        elif value == dict(Tickets.STATUS_CHOICES).get('RESOLVED'):
            return mark_safe('<div class="ui green label">' +_('Résolus') + '</div>')


class TitleColumn(tables.LinkColumn):
    """
    Classe qui surcharge la colonne titre afin de limiter le titre en caractère pour ne pas
    déformer le tableau
    L'astuce et de limiter la variable value: value[:126]
    """
    def render(self, value, record, bound_column):
        return self.render_link(reverse('view', args=[record.id]), value[:70])


class TicketsTables(tables.Table):

    title = TitleColumn('view', args=[A('id')])
    priority = PriorityColumn()
    status = StatusColumn()

    class Meta:
        model = Tickets
        attrs = {"class": "paleblue"}
        exclude = ('content', 'depends_on',
                   'file', 'date_resolved',
                   'date_closed', 'date_assigned',
                   'ask_to_delete', 'complete')
