__author__ = 'had'
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django_tables2 import RequestConfig
from ticket.forms import TicketForm, ResponseForm, StatusForm
from ticket.models import Tickets, UserProfile, Follow
from ticket.tables import TicketsTables
from django.contrib import messages
from django.utils.translation import ugettext as _
from ticket.tasks import send_new_ticket_all_staff, incomplete_ticket
from djangoticket.settings import USE_MAIL
import json


@login_required(login_url='login/')
def home(request):
    if request.user.is_staff:
        ticket_list = Tickets\
                          .objects\
                          .select_related('create_by',
                                          'assign_to',
                                          'category')\
                          .filter()\
                          .order_by('-created')[:10:1]

        ticket_incomplete = Tickets.objects.filter(complete=0).count()

    else:
        ticket_list = Tickets.objects.filter(
            create_by=request.user).order_by('-created')[:10:1]

        ticket_incomplete = Tickets.objects.filter(
            create_by=request.user,
            complete=0).count()

    return render(request, 'home.html', {'ticket_list': ticket_list})