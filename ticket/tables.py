__author__ = 'had'
from ticket.models import Tickets
import django_tables2 as tables
from django_tables2.utils import A

class TicketsTables(tables.Table):
    title = tables.LinkColumn('view', args=[A('id')])
    class Meta:
        model = Tickets
        attrs = {"class": "paleblue"}
        exclude = ('content',)