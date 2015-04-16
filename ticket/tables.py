__author__ = 'had'
from ticket.models import Tickets
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe

class PriorityColumn(tables.Column):
    """
    Class qui sert à colorer les cellules en fonction de leurs
    priorité
    """
    def render(self, value):
      if value == 'Critical':
            self.attrs ={"td": {"bgcolor": "FF3333"}}

      elif value == 'High':
            self.attrs ={"td": {"bgcolor": "FF8585"}}
      elif value == 'Low':
            self.attrs ={"td": {"bgcolor": "FFC299"}}
      elif value == 'Very Low':
            self.attrs ={"td": {"bgcolor": "FFE2CE"}}
      elif value =='Normal':
          self.attrs ={}

      return value

class StatusColumn(tables.Column):
    """
    Class met un badge en fonction du status
    """
    def render(self, value):
        if value == 'Open':
            return mark_safe('<span class="uk-badge uk-badge-success">Ouvert</span>')
        elif value == 'Closed':
            return mark_safe('<span class="uk-badge uk-badge-warning">Clos</span>')
        elif value == 'Resolved':
            return mark_safe('<span class="uk-badge">Resolus</span>')



class TicketsTables(tables.Table):
    title = tables.LinkColumn('view', args=[A('id')])
    priority = PriorityColumn()
    status = StatusColumn()

    class Meta:
        model = Tickets
        attrs = {"class": "paleblue"}
        exclude = ('content',)