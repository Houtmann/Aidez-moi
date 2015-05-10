__author__ = 'had'
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django_tables2 import RequestConfig
from ticket.forms import TicketForm, ResponseForm, StatusForm
from ticket.models import Tickets, UserProfile, Follow
from ticket.views.auth import home
from ticket.tables import TicketsTables
from django.contrib import messages
from django.utils.translation import ugettext as _
from ticket.tasks import send_new_ticket_all_staff, handle_uploaded_file
from djangoticket.settings import USE_MAIL

from django.shortcuts import get_object_or_404

from ticket.models import Tickets
from zipfile impor tar

def downloadLogs(req, dir):
    response = HttpResponse(mimetype='application/x-gzip')
    response['Content-Disposition'] = 'attachment; filename=download.tar.gz'
    tarred = tarfile.open(fileobj=response, mode='w:gz')
    tarred.add(dir)
    tarred.close()

    return response)