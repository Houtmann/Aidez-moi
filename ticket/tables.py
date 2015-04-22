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
      if value == 'Critique':
            self.attrs ={"td": {"bgcolor": "FF3333"}}

      elif value == 'Haute':
            self.attrs ={"td": {"bgcolor": "FF8585"}}
      elif value == 'BAsse':
            self.attrs ={"td": {"bgcolor": "FFC299"}}
      elif value == 'Très basse':
            self.attrs ={"td": {"bgcolor": "FFE2CE"}}
      elif value =='Normal':
          self.attrs ={}

      return value

class StatusColumn(tables.Column):
    """
    Class met un badge en fonction du status
    """
    def render(self, value):
        if value == 'Ouvert':
            return mark_safe('<span class="uk-badge uk-badge-success">Ouvert</span>')
        elif value == 'Clos':
            return mark_safe('<span class="uk-badge uk-badge-warning">Clos</span>')
        elif value == 'Resolus':
            return mark_safe('<span class="uk-badge">Resolus</span>')



class TicketsTables(tables.Table):
    title = tables.LinkColumn('view', args=[A('id')])
    priority = PriorityColumn()
    status = StatusColumn()

    class Meta:
        model = Tickets
        attrs = {"class": "paleblue"}
        exclude = ('content',)