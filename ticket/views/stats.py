__author__ = 'had'
from django.shortcuts import render, redirect, render_to_response
from ticket.forms import TicketForm, ResponseForm
from ticket.models import Tickets, UserProfile, Follow
from ticket.views.auth import home
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page
from datetime import datetime
from ticket.tables import TicketsTables
from django_tables2 import RequestConfig

@login_required(login_url='login/')
def statistic(request):

    return render(request, 'statistics.html', locals())