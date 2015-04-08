__author__ = 'had'
from ticket.models import Tickets
import django_tables2 as tables

class TicketsTables(tables.Table):
    class Meta:
        model = Tickets
        attrs = {"class": "paleblue"}
        exclude = ('content',)