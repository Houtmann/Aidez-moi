# coding=utf-8
__author__ = 'had'

from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django_tables2 import RequestConfig
from ticket.forms import TicketForm, ResponseForm, StatusForm
from ticket.models import Tickets, UserProfile, Follow
from ticket.views.home import home
from ticket.tables import TicketsTables
from django.contrib import messages
from django.utils.translation import ugettext as _
from ticket.tasks import send_new_ticket_all_staff, incomplete_ticket
from djangoticket.settings import USE_MAIL
import json

@login_required(login_url='login/')
def statistic(request):

    return render(request, 'statistics.html', locals())


@login_required(login_url='login/')
def ticket_stats(request, id):
    ticket = Tickets.objects.get(pk=id)
    follow = Follow.objects.filter(ticket=id)
    ticket_date_create = ticket.created
    for i in follow:
        print(i.old_value, i.new_value)

    return render(request, 'statistics.html', locals())
