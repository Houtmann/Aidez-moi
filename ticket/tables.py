# coding=utf-8
__author__ = 'had'
from ticket.models import Tickets
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
        if value == _('Critique'):
            self.attrs = {"td": {"bgcolor": "FF3333"}}
        elif value == _('Haute'):
            self.attrs = {"td": {"bgcolor": "FF8585"}}
        elif value == _('Basse'):
            self.attrs = {"td": {"bgcolor": "FFC299"}}
        elif value == _('Très basse'):
            self.attrs = {"td": {"bgcolor": "FFE2CE"}}
        elif value == _('Normal'):
            self.attrs = {}

        return value


class StatusColumn(tables.Column):
    """
    Class met un badge en fonction du status
    """

    def render(self, value):

        if value == _('Ouvert'):
            return mark_safe(
                '<div class="ui center orange label">Ouvert</div>')
        elif value == _('Clos'):
            return mark_safe(
                '<div class="ui center black label">Clos</div>')
        elif value == _('Résolus'):
            return mark_safe('<div class="ui center green label">Résolus</div>')


class TicketsTables(tables.Table):
    title = tables.LinkColumn('view', args=[A('id')])
    priority = PriorityColumn()
    status = StatusColumn()

    class Meta:
        model = Tickets
        attrs = {"class": "paleblue"}
        exclude = ('content', 'depends_on',
                   'file', 'date_resolved',
                   'date_closed', 'date_assigned')
