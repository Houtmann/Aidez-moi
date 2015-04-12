__author__ = 'had'
from ticket.models import Tickets
import django_tables2 as tables
from django_tables2.utils import A

class CourtColumn(tables.Column):
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


class TicketsTables(tables.Table):
    title = tables.LinkColumn('view', args=[A('id')])
    priority = CourtColumn()

    class Meta:
        model = Tickets
        attrs = {"class": "paleblue"}
        exclude = ('content',)